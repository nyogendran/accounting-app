"""Validate governed artifacts, records, sources and Claude Code configuration.

Usage:
  python tools/governance/check.py                 # whole repository
  python tools/governance/check.py --file <path>   # findings for one file
  python tools/governance/check.py --pre-commit    # also check staged changes (git pre-commit hook)
  python tools/governance/check.py --commit-msg <message-file>   # git commit-msg hook
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.governance import approvals, common  # noqa: E402

AGENT_EMAIL_DOMAIN = "@agents.tiqacc.invalid"
DECISION_FOLDER = "ledger/approval-decisions/"
LOCAL_STATE_FOLDER = ".claude/state/"
SOURCE_REGISTER = "docs/sources/source-register.yaml"

# Documented subagent and skill frontmatter keys (code.claude.com/docs, sub-agents and skills pages).
ALLOWED_AGENT_KEYS = {
    "name", "description", "tools", "disallowedTools", "model", "permissionMode", "maxTurns",
    "skills", "mcpServers", "hooks", "memory", "background", "effort", "isolation", "color",
    "initialPrompt", "omitClaudeMd", "autoCompactWindow", "experimental",
}
ALLOWED_SKILL_KEYS = {
    "name", "description", "when_to_use", "argument-hint", "arguments", "disable-model-invocation",
    "user-invocable", "allowed-tools", "disallowed-tools", "model", "effort", "context", "agent",
    "hooks", "paths", "shell", "background", "metadata", "license", "compatibility",
}
AGENT_MODELS = {"inherit", "sonnet", "opus", "haiku", "fable"}
RECORD_FOLDERS = {
    "approval-requests": "AREQ",
    "approval-decisions": "APR",
    "reviews": "REV",
    "evidence": "EVD",
    "workflows": "WF",
}
REVIEW_VERDICTS = ("pass", "non-blocking-findings", "blocking-findings")


@dataclass
class Finding:
    level: str  # error | warning
    path: str
    message: str

    def __str__(self):
        return f"{self.level.upper():7} {self.path}: {self.message}"


class Collector:
    def __init__(self, root: Path):
        self.root = root
        self.items: list[Finding] = []

    def _path(self, path) -> str:
        return common.relative(self.root, path) if isinstance(path, Path) else str(path)

    def error(self, path, message):
        self.items.append(Finding("error", self._path(path), message))

    def warning(self, path, message):
        self.items.append(Finding("warning", self._path(path), message))


# --------------------------------------------------------------------------- artifacts


def _clause_ids(root: Path, relative: str):
    """The clause IDs in a clause index, or None while the index does not exist."""
    path = root / relative
    if not path.is_file():
        return None
    data = common.read_yaml(path) or {}
    return {str(c.get("id")) for c in data.get("clauses") or [] if isinstance(c, dict)}


def check_artifacts(index: common.Index, out: Collector) -> None:
    clause_ids = {kind: _clause_ids(index.root, relative) for kind, relative in common.CLAUSE_INDEXES.items()}
    criteria = index.acceptance_criteria()
    for artifact in index.artifacts.values():
        meta, path = artifact.meta, artifact.path
        for key in ("id", "type", "title", "status", "version", "owner"):
            if meta.get(key) in (None, ""):
                out.error(path, f"missing required field '{key}'")
        kind = meta.get("type")
        status = meta.get("status")
        if kind not in common.ARTIFACT_TYPES:
            out.error(path, f"unknown type '{kind}'")
        if status not in common.STATUSES:
            out.error(path, f"unknown status '{status}' (allowed: {', '.join(common.STATUSES)})")
        version = meta.get("version")
        if not isinstance(version, int) or isinstance(version, bool) or version < 1:
            out.error(path, "version must be an integer of at least 1")
        if kind in common.TYPE_ID_KINDS and common.id_kind(artifact.id) not in common.TYPE_ID_KINDS[kind]:
            out.error(path, f"ID {artifact.id} is not a valid {kind} ID")
        if kind in common.TIERED_TYPES and meta.get("tier") not in (1, 2, 3):
            out.error(path, "tier must be 1, 2 or 3")
        elif "tier" in meta and meta.get("tier") not in (1, 2, 3):
            out.error(path, "tier must be 1, 2 or 3")
        if kind in common.NORMATIVE_TYPES and status != "Draft":
            if not isinstance(meta.get("normative"), dict) or not meta.get("normative"):
                out.error(path, "a normative block is required once the artifact leaves Draft")
        links = meta.get("links") or {}
        if not isinstance(links, dict):
            out.error(path, "links must be a mapping of link type to a list of IDs")
            links = {}
        for link_type, targets in links.items():
            if link_type not in common.LINK_TYPES:
                out.error(path, f"unknown link type '{link_type}'")
                continue
            if not isinstance(targets, list):
                out.error(path, f"link '{link_type}' must be a list of IDs")
                continue
            for target in targets:
                target = str(target)
                clause_kind = common.id_kind(target)
                if clause_kind in common.CLAUSE_INDEXES:
                    known = clause_ids[clause_kind]
                    if known is None:
                        out.warning(path, f"clause {target} cannot be checked until {common.CLAUSE_INDEXES[clause_kind]} exists")
                    elif target not in known:
                        out.error(path, f"link {link_type} -> {target}: not in {common.CLAUSE_INDEXES[clause_kind]}")
                    continue
                if target in criteria or index.exists(target):
                    continue
                out.error(path, f"link {link_type} -> {target}: no such ID")
        for key in ("supersedes", "superseded_by"):
            value = meta.get(key)
            if value and not index.exists(str(value)):
                out.error(path, f"{key} -> {value}: no such ID")
        if status == "Approved":
            state = approvals.approval_state(index, artifact.id)
            if state.state != "valid":
                detail = f" ({state.detail})" if state.detail else ""
                out.error(
                    path,
                    f"status is Approved but its approval state is '{state.state}'{detail}; "
                    "only a captured decision on the current normative hash makes it Approved",
                )


# --------------------------------------------------------------------------- records


def _require(out, path, data, keys):
    for key in keys:
        if data.get(key) in (None, "", []):
            out.error(path, f"missing required field '{key}'")


def check_records(index: common.Index, out: Collector) -> None:
    roles = set((common.load_authority(index.root).get("roles") or {}).keys())
    for record in index.records.values():
        path, data, kind = record.path, record.data, common.id_kind(record.id)
        if path.stem != record.id:
            out.error(path, f"record ID {record.id} does not match its file name")
        if kind is None:
            out.error(path, f"invalid record ID {record.id}")
            continue
        folder = path.parent.name
        if folder in RECORD_FOLDERS and RECORD_FOLDERS[folder] != kind:
            out.error(path, f"{kind} record in the {folder} folder")
        if kind == "AREQ":
            _require(out, path, data, ("type", "created_at", "required_role", "subjects", "combined", "phrase_code"))
            subjects = data.get("subjects") or []
            for subject in subjects:
                if subject.get("id") not in index.artifacts:
                    out.error(path, f"subject {subject.get('id')} does not exist")
            if subjects and data.get("combined") != approvals.combined_hash(subjects):
                out.error(path, "combined hash does not match the subjects")
            if data.get("combined") and data.get("phrase_code") != str(data["combined"])[7:19]:
                out.error(path, "phrase code does not match the combined hash")
            if data.get("required_role") and data["required_role"] not in roles:
                out.error(path, f"unknown role '{data['required_role']}' (not in the authority matrix)")
        elif kind == "APR":
            _require(out, path, data, ("type", "request", "decision", "subjects", "combined", "level", "channel", "recorded_at"))
            request = index.records.get(str(data.get("request")))
            if request is None or request.kind != "AREQ":
                out.error(path, f"approval request {data.get('request')} does not exist")
            else:
                if data.get("combined") != request.data.get("combined"):
                    out.error(path, "subjects do not match the approval request")
            if data.get("decision") not in approvals.DECISIONS:
                out.error(path, f"unknown decision '{data.get('decision')}'")
            if data.get("level") not in ("E1", "E1-op"):
                out.error(path, f"decision level must be E1 or E1-op, not '{data.get('level')}'")
            if data.get("channel") == "stage0-session":
                attestation = data.get("attestation") or {}
                if attestation.get("hook") != "capture-approval" or not attestation.get("prompt_sha256"):
                    out.error(path, "missing hook attestation: Stage 0 decisions are written only by the capture hook")
                if data.get("level") != "E1-op":
                    out.error(path, "Stage 0 decisions are operator-attested (level E1-op), never E1")
            elif data.get("channel") == "git-host":
                out.error(path, "git-host decisions are not accepted until Stage 1 is set up (DEC-0003)")
            else:
                out.error(path, f"unknown channel '{data.get('channel')}'")
        elif kind == "REV":
            _require(out, path, data, ("reviewer", "level", "subjects", "verdict", "created_at"))
            if data.get("level") not in ("E4", "E1"):
                out.error(path, "review level must be E4 (agent) or E1 (person)")
            if data.get("verdict") not in REVIEW_VERDICTS:
                out.error(path, f"verdict must be one of {', '.join(REVIEW_VERDICTS)}")
            for subject in data.get("subjects") or []:
                if isinstance(subject, dict) and "commit" in subject:
                    if not _commit_exists(index.root, str(subject["commit"])):
                        out.error(path, f"review subject {subject['commit']} is not a full commit hash in this repository")
                elif not isinstance(subject, dict) or subject.get("id") not in index.artifacts or not subject.get("hash"):
                    out.error(path, f"review subject {subject} must name an existing artifact with the hash reviewed, or a commit")
        elif kind == "EVD":
            _require(out, path, data, ("kind", "level", "recorded_at"))
            if data.get("level") not in ("E2", "E3"):
                out.error(path, "evidence level must be E2 or E3")
        elif kind == "WF":
            _require(out, path, data, ("type", "title", "steps"))


def check_capture_log(index: common.Index, out: Collector) -> None:
    """Stage 0 decisions must match what the capture hook logged on this machine.

    A committed decision missing from the log is expected on other clones (warning). An uncommitted
    one missing from the log, or any decision that differs from its logged hash, was not written by
    the hook as it stands (error).
    """
    stage0 = [r for r in index.records.values() if r.kind == "APR" and r.data.get("channel") == "stage0-session"]
    if not stage0:
        return
    log = _capture_log(index.root)
    for record in stage0:
        hashes = log.get(record.id)
        if hashes and common.sha256_file(record.path) in hashes:
            continue
        if hashes or not _in_head(index.root, common.relative(index.root, record.path)):
            out.error(
                record.path,
                "not recorded by the capture hook on this machine (missing from the capture log, or changed "
                "after capture); Stage 0 decisions come only from the capture hook",
            )
        else:
            out.warning(record.path, "not in this machine's capture log (expected on other clones)")


# --------------------------------------------------------------------------- sources


def check_sources(index: common.Index, out: Collector) -> None:
    register = index.root / "docs/sources/source-register.yaml"
    for source in index.sources.values():
        identifier = source.get("id")
        if common.id_kind(str(identifier)) != "SRC":
            out.error(register, f"invalid source ID {identifier}")
        entries = list(source.get("files") or []) + list(source.get("derived") or [])
        if not source.get("files"):
            out.error(register, f"{identifier} lists no files")
        for entry in entries:
            target = index.root / str(entry.get("path", ""))
            if not target.is_file():
                out.error(register, f"{identifier}: {entry.get('path')} does not exist")
                continue
            if common.sha256_file(target) != entry.get("sha256"):
                out.error(register, f"{identifier}: SHA-256 of {entry.get('path')} does not match the register")


# --------------------------------------------------------------------------- Claude Code configuration


def _tools(value) -> set:
    if isinstance(value, str):
        return {item.strip() for item in value.split(",") if item.strip()}
    if isinstance(value, list):
        return {str(item).strip() for item in value}
    return set()


def check_claude_config(root: Path, out: Collector) -> None:
    for path in sorted((root / ".claude/agents").glob("*.md")):
        try:
            meta, _ = common.load_artifact(path)
        except Exception as error:
            out.error(path, f"cannot parse frontmatter: {error}")
            continue
        if meta is None:
            out.error(path, "missing frontmatter")
            continue
        unknown = sorted(set(meta) - ALLOWED_AGENT_KEYS)
        if unknown:
            out.error(path, f"unknown key(s) {', '.join(unknown)}: Claude Code ignores unknown keys silently")
        for key in ("name", "description", "tools"):
            if not meta.get(key):
                out.error(path, f"missing '{key}' (without tools, an agent inherits every tool)")
        if meta.get("name") and meta["name"] != path.stem:
            out.error(path, f"name '{meta['name']}' does not match the file name")
        tools = _tools(meta.get("tools"))
        if {"Agent", "Task"} & tools:
            out.error(path, "agents may not have the Agent tool; all delegation runs through the orchestrator")
        if "memory" in meta:
            out.error(path, "per-agent memory is off by design (docs/governance/agent-operating-model.md)")
        model = meta.get("model")
        if model is not None and model not in AGENT_MODELS and not str(model).startswith("claude-"):
            out.error(path, f"unknown model '{model}'")
    for path in sorted((root / ".claude/skills").glob("*/SKILL.md")):
        try:
            meta, _ = common.load_artifact(path)
        except Exception as error:
            out.error(path, f"cannot parse frontmatter: {error}")
            continue
        if meta is None:
            out.error(path, "missing frontmatter")
            continue
        unknown = sorted(set(meta) - ALLOWED_SKILL_KEYS)
        if unknown:
            out.error(path, f"unknown key(s) {', '.join(unknown)}: Claude Code ignores unknown keys silently")
        for key in ("name", "description"):
            if not meta.get(key):
                out.error(path, f"missing '{key}'")
        if meta.get("name") and meta["name"] != path.parent.name:
            out.error(path, f"name '{meta['name']}' does not match the folder name")
    for path in sorted((root / ".claude/rules").glob("**/*.md")):
        try:
            meta, _ = common.load_artifact(path)
        except Exception as error:
            out.error(path, f"frontmatter does not parse, so the rule would load everywhere: {error}")
            continue
        if not meta or "paths" not in meta:
            out.warning(path, "rule has no paths, so it loads in every session")


# --------------------------------------------------------------------------- git checks


def _git(root: Path, *args) -> str:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def _commit_exists(root: Path, sha: str) -> bool:
    if not re.fullmatch(r"[0-9a-f]{40}", sha):
        return False
    result = subprocess.run(["git", "cat-file", "-e", f"{sha}^{{commit}}"], cwd=root, capture_output=True)
    return result.returncode == 0


def _in_head(root: Path, path: str) -> bool:
    result = subprocess.run(["git", "cat-file", "-e", f"HEAD:{path}"], cwd=root, capture_output=True)
    return result.returncode == 0


def _capture_log(root: Path) -> dict:
    entries: dict = {}
    log = root / ".claude/state/capture-log.jsonl"
    if log.is_file():
        for line in log.read_text(encoding="utf-8").splitlines():
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            entries.setdefault(entry.get("id"), set()).add(entry.get("sha256"))
    return entries


def _staged_blob(root: Path, path: str) -> bytes:
    return subprocess.run(["git", "show", f":{path}"], cwd=root, capture_output=True).stdout


def _staged_register(root: Path) -> dict:
    """Path -> SHA-256 for every file listed in the staged source register."""
    try:
        data = yaml.safe_load(_staged_blob(root, SOURCE_REGISTER).decode("utf-8")) or {}
    except (ValueError, yaml.YAMLError):
        return {}
    if not isinstance(data, dict):
        return {}
    registered = {}
    for source in data.get("sources") or []:
        if not isinstance(source, dict):
            continue
        for entry in list(source.get("files") or []) + list(source.get("derived") or []):
            if isinstance(entry, dict) and entry.get("path"):
                registered[str(entry["path"])] = entry.get("sha256")
    return registered


def _check_new_decision(root: Path, path: str, log: dict, out: Collector) -> None:
    """A staged new Stage 0 decision must match what the capture hook logged on this machine."""
    blob = _staged_blob(root, path)
    try:
        data = json.loads(blob.decode("utf-8"))
    except ValueError:
        out.error(path, "decision record is not valid JSON")
        return
    if data.get("channel") != "stage0-session":
        return
    if hashlib.sha256(blob).hexdigest() not in log.get(Path(path).stem, set()):
        out.error(
            path,
            "this decision was not written by the capture hook on this machine, or was altered after "
            "capture; Stage 0 decisions come only from the capture hook",
        )


def _check_new_protected(root: Path, path: str, log: dict, registered: dict, out: Collector) -> None:
    """A file added under a protected path is a captured decision or a newly registered source."""
    if path.startswith(DECISION_FOLDER):
        if path.endswith(".json"):
            _check_new_decision(root, path, log, out)
        else:
            out.error(path, "decision records are JSON files written by the capture hook")
        return
    if path.startswith(LOCAL_STATE_FOLDER):
        out.error(path, "local capture state is protected and is never committed")
        return
    if registered.get(path) != hashlib.sha256(_staged_blob(root, path)).hexdigest():
        out.error(
            path,
            f"a new file under a protected path must be registered with its SHA-256 in {SOURCE_REGISTER} "
            "in the same commit",
        )


def check_staged(root: Path, out: Collector) -> None:
    scopes = common.load_scopes(root)
    try:
        lines = _git(root, "diff", "--cached", "--name-status", "--no-renames").splitlines()
    except RuntimeError as error:
        out.error("git", f"cannot read staged changes: {error}")
        return
    log = _capture_log(root)
    registered = None
    for line in lines:
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        code, path = parts[0][0], parts[1]
        protected = common.glob_match(path, scopes.get("protected"))
        if code == "A":
            if protected:
                if registered is None:
                    registered = _staged_register(root)
                _check_new_protected(root, path, log, registered, out)
            continue
        if common.glob_match(path, scopes.get("append_only")) and _in_head(root, path):
            out.error(path, "this is a committed record; records are never edited after commit")
        if protected:
            out.error(path, "this path is protected (registered source or decision record) and cannot be changed")


def check_commit_message(root: Path, message: str, author_email: str) -> list[Finding]:
    root = Path(root)
    out = Collector(root)
    body = "\n".join(line for line in message.splitlines() if not line.startswith("#"))
    agents = re.findall(r"^Agent:\s*(\S+)\s*$", body, re.MULTILINE)
    if not author_email.lower().endswith(AGENT_EMAIL_DOMAIN):
        if agents:
            out.error("commit", "human commits must not carry an Agent trailer")
        return out.items
    if not agents:
        out.error("commit", "agent commits need an 'Agent: <name>' trailer")
        return out.items
    scopes = common.load_scopes(root)
    configs = dict(scopes.get("agents") or {})
    configs["orchestrator"] = scopes.get("orchestrator") or {"write": ["**"]}
    unknown = [name for name in agents if name not in configs]
    for name in unknown:
        out.error("commit", f"unknown agent '{name}' in the Agent trailer")
    known = [name for name in agents if name in configs]
    try:
        staged = [line for line in _git(root, "diff", "--cached", "--name-only").splitlines() if line]
    except RuntimeError as error:
        out.error("commit", f"cannot read staged changes: {error}")
        return out.items
    for path in staged:
        inside = any(
            common.glob_match(path, configs[name].get("write"))
            and not common.glob_match(path, configs[name].get("deny"))
            for name in known
        )
        if not inside:
            out.error(path, f"{path} is outside the write scope of {', '.join(agents)}")
    return out.items


# --------------------------------------------------------------------------- entry points


def run_checks(root, files=None, pre_commit=False) -> list[Finding]:
    root = Path(root)
    out = Collector(root)
    index = common.load_index(root)
    for path, message in index.problems:
        out.error(path, message)
    for identifier, first, second in index.duplicates:
        out.error(second, f"duplicate ID {identifier} (also in {first})")
    check_artifacts(index, out)
    check_records(index, out)
    check_capture_log(index, out)
    check_sources(index, out)
    check_claude_config(root, out)
    if pre_commit:
        check_staged(root, out)
    findings = out.items
    if files:
        wanted = {str(f).replace("\\", "/") for f in files}
        findings = [f for f in findings if f.path in wanted]
    return findings


def _author_email(root: Path) -> str:
    ident = _git(root, "var", "GIT_AUTHOR_IDENT").strip()
    match = re.search(r"<([^>]*)>", ident)
    return match.group(1) if match else ""


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="TIQACC governance checks.")
    parser.add_argument("--root", type=Path)
    parser.add_argument("--file", action="append")
    parser.add_argument("--pre-commit", action="store_true")
    parser.add_argument("--commit-msg", type=Path)
    parser.add_argument("--quiet", action="store_true", help="print errors only")
    args = parser.parse_args(argv)
    root = args.root or common.find_root()
    if args.commit_msg:
        message = args.commit_msg.read_text(encoding="utf-8")
        findings = check_commit_message(root, message, _author_email(root))
    else:
        findings = run_checks(root, files=args.file, pre_commit=args.pre_commit)
    errors = [f for f in findings if f.level == "error"]
    warnings = [f for f in findings if f.level == "warning"]
    for finding in errors + ([] if args.quiet else warnings):
        print(finding)
    print(f"check: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

"""Shared helpers for the TIQACC governance tools: parsing, hashing, IDs and the repository index."""
from __future__ import annotations

import hashlib
import json
import os
import re
import secrets
import time
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import yaml

STATUSES = ("Draft", "In review", "Proposed", "Approved", "Rejected", "Deferred", "Superseded")

ARTIFACT_TYPES = (
    "governance",
    "objective",
    "requirement",
    "story",
    "policy",
    "rule",
    "invariant",
    "scenario",
    "decision",
    "adr",
    "design",
    "question",
    "issue",
    "change-request",
    "gate",
)

# Types whose meaning lives in a `normative` block once they leave Draft.
NORMATIVE_TYPES = (
    "objective",
    "requirement",
    "story",
    "policy",
    "rule",
    "invariant",
    "scenario",
    "decision",
    "adr",
    "change-request",
    "gate",
)

# Types that must declare a risk tier.
TIERED_TYPES = ("requirement", "story", "policy", "rule", "invariant", "scenario")

LINK_TYPES = (
    "derives_from",
    "refines",
    "governed_by",
    "decided_by",
    "designs",
    "implements",
    "verifies",
    "affects",
    "resolves",
    "supersedes",
    "blocks",
    "waives",
    "related",
)

# Links that change meaning, and therefore the normative hash.
NORMATIVE_LINKS = ("derives_from", "refines", "governed_by", "decided_by", "supersedes")

ULID = r"[0-9A-HJKMNP-TV-Z]{26}"
AREA = r"[A-Z]{2,5}"

ID_PATTERNS = {
    "SRC": r"SRC-\d{3}",
    "S1": r"S1-\d+(?:\.\d+)*-c\d{2,3}",
    "GOV": r"GOV-[A-Z0-9]+(?:-[A-Z0-9]+)*",
    "BO": r"BO-\d{2}",
    "REQ": rf"REQ-{AREA}-\d{{3}}",
    "US": rf"US-{AREA}-\d{{3}}",
    "AC": rf"AC-US-{AREA}-\d{{3}}-\d{{2}}",
    "POL": r"POL-\d{3}",
    "ACR": r"ACR-\d{3}",
    "INV": r"INV-\d{2}",
    "SCN": r"SCN-\d{3}",
    "DEC": r"DEC-\d{4}",
    "ADR": r"ADR-\d{4}",
    "TD": rf"TD-{AREA}-\d{{3}}",
    "API": r"API-[a-z0-9]+(?:-[a-z0-9]+)*",
    "ENT": r"ENT-[a-z0-9]+(?:-[a-z0-9]+)*",
    "TC": rf"TC-{AREA}-\d{{3}}",
    "Q": r"Q-\d{3}",
    "RISK": r"RISK-\d{3}",
    "CR": r"CR-\d{3}",
    "GATE": r"GATE-(?:0|A|B|C|D)(?:-[A-Z0-9]+)*",
    "INCR": r"INCR-\d{3}",
    "REL": r"REL-\d+\.\d+\.\d+",
}
for _prefix in ("ISS", "IR", "IA", "DSP", "BRF", "AREQ", "APR", "WVR", "EVD", "REV", "DEP", "WI", "WF"):
    ID_PATTERNS[_prefix] = rf"{_prefix}-{ULID}"

_COMPILED = {kind: re.compile(rf"^{pattern}$") for kind, pattern in ID_PATTERNS.items()}

# Which ID kinds each artifact type may use.
TYPE_ID_KINDS = {
    "governance": ("GOV",),
    "objective": ("BO",),
    "requirement": ("REQ",),
    "story": ("US",),
    "policy": ("POL",),
    "rule": ("ACR",),
    "invariant": ("INV",),
    "scenario": ("SCN",),
    "decision": ("DEC",),
    "adr": ("ADR",),
    "design": ("TD", "API", "ENT"),
    "question": ("Q",),
    "issue": ("ISS", "IR"),
    "change-request": ("CR",),
    "gate": ("GATE",),
}


def id_kind(identifier: str) -> str | None:
    """Return the ID kind (its prefix) if the identifier is well formed, else None."""
    if not isinstance(identifier, str):
        return None
    for kind, pattern in _COMPILED.items():
        if pattern.match(identifier):
            return kind
    return None


# --------------------------------------------------------------------------- repository


def find_root(start: Path | None = None) -> Path:
    """Locate the repository root: TIQACC_ROOT, CLAUDE_PROJECT_DIR, or the nearest CLAUDE.md."""
    for variable in ("TIQACC_ROOT", "CLAUDE_PROJECT_DIR"):
        value = os.environ.get(variable)
        if value and (Path(value) / "CLAUDE.md").is_file():
            return Path(value).resolve()
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "CLAUDE.md").is_file() and (candidate / "docs").is_dir():
            return candidate
    raise SystemExit("Cannot find the repository root (no CLAUDE.md with a docs folder).")


def relative(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def repo_relative(path_text: str, root: Path) -> str | None:
    """Turn a tool's file path (Windows, POSIX or Git Bash style) into a repository-relative path.

    Returns None for paths outside the repository.
    """
    import posixpath

    text = str(path_text).replace("\\", "/")
    git_bash = re.match(r"^/([a-zA-Z])/(.*)$", text)
    if git_bash:
        text = f"{git_bash.group(1)}:/{git_bash.group(2)}"
    root_text = Path(root).resolve().as_posix()
    if not re.match(r"^[a-zA-Z]:/", text) and not text.startswith("/"):
        text = f"{root_text}/{text}"
    text = posixpath.normpath(text)
    if text.lower() == root_text.lower():
        return ""
    if text.lower().startswith(root_text.lower() + "/"):
        return text[len(root_text) + 1:]
    return None


_GLOB_CACHE: dict = {}


def glob_regex(pattern: str):
    if pattern not in _GLOB_CACHE:
        out, i = "", 0
        while i < len(pattern):
            if pattern.startswith("**", i):
                out += ".*"
                i += 2
            elif pattern[i] == "*":
                out += "[^/]*"
                i += 1
            elif pattern[i] == "?":
                out += "[^/]"
                i += 1
            else:
                out += re.escape(pattern[i])
                i += 1
        _GLOB_CACHE[pattern] = re.compile(f"^{out}$", re.IGNORECASE)
    return _GLOB_CACHE[pattern]


def glob_match(path: str, patterns) -> bool:
    return any(glob_regex(pattern).match(path) for pattern in patterns or [])


# --------------------------------------------------------------------------- parsing


def parse_front_matter(text: str) -> tuple[dict | None, str]:
    """Split YAML front matter from a Markdown body. Returns (None, text) if there is none."""
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    closing = text.find("\n", end + 4)
    front = text[4:end]
    body = text[closing + 1:] if closing != -1 else ""
    meta = yaml.safe_load(front) if front.strip() else {}
    if meta is None:
        meta = {}
    if not isinstance(meta, dict):
        raise ValueError("front matter is not a mapping")
    return meta, body


def load_artifact(path: Path) -> tuple[dict | None, str]:
    return parse_front_matter(path.read_text(encoding="utf-8"))


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def read_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- hashing


def _canonical(value):
    if isinstance(value, str):
        text = unicodedata.normalize("NFC", value).replace("\r\n", "\n")
        return re.sub(r"\s+", " ", text).strip()
    if isinstance(value, dict):
        return {str(key): _canonical(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_canonical(item) for item in value]
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return value


def canonical_json(value) -> str:
    return json.dumps(_canonical(value), sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normative_payload(meta: dict) -> dict:
    payload = {}
    for key in ("id", "type", "tier", "normative", "effective_from", "effective_to"):
        if meta.get(key) is not None:
            payload[key] = meta[key]
    links = meta.get("links") or {}
    normative_links = {
        name: sorted(str(item) for item in (links.get(name) or []))
        for name in NORMATIVE_LINKS
        if links.get(name)
    }
    if normative_links:
        payload["links"] = normative_links
    return payload


def normative_hash(meta: dict) -> str:
    return "sha256:" + sha256_text(canonical_json(normative_payload(meta)))


# --------------------------------------------------------------------------- time and IDs

_CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
_LAST_ULID = [0, 0]


def new_ulid(timestamp_ms: int | None = None, randomness: int | None = None) -> str:
    """Return a ULID. Without arguments, ULIDs from one process are strictly increasing."""
    if timestamp_ms is None and randomness is None:
        timestamp_ms = int(time.time() * 1000)
        if timestamp_ms <= _LAST_ULID[0]:
            timestamp_ms = _LAST_ULID[0]
            randomness = (_LAST_ULID[1] + 1) & ((1 << 80) - 1)
        else:
            randomness = secrets.randbits(80)
        _LAST_ULID[0], _LAST_ULID[1] = timestamp_ms, randomness
    if timestamp_ms is None:
        timestamp_ms = int(time.time() * 1000)
    if randomness is None:
        randomness = secrets.randbits(80)
    value = (timestamp_ms << 80) | randomness
    characters = []
    for _ in range(26):
        characters.append(_CROCKFORD[value & 31])
        value >>= 5
    return "".join(reversed(characters))


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


# --------------------------------------------------------------------------- index

EXCLUDED_DOC_PREFIXES = ("docs/sources/", "docs/governance/templates/")


@dataclass
class Artifact:
    id: str
    path: Path
    meta: dict
    body: str


@dataclass
class Record:
    id: str
    path: Path
    kind: str
    data: dict


@dataclass
class Index:
    root: Path
    artifacts: dict = field(default_factory=dict)
    records: dict = field(default_factory=dict)
    sources: dict = field(default_factory=dict)
    duplicates: list = field(default_factory=list)
    problems: list = field(default_factory=list)

    def exists(self, identifier: str) -> bool:
        return identifier in self.artifacts or identifier in self.records or identifier in self.sources

    def acceptance_criteria(self) -> dict:
        found = {}
        for artifact in self.artifacts.values():
            for criterion in (artifact.meta.get("normative") or {}).get("acceptance_criteria") or []:
                if isinstance(criterion, dict) and criterion.get("id"):
                    found[criterion["id"]] = artifact.id
        return found


def artifact_paths(root: Path):
    docs = root / "docs"
    if not docs.is_dir():
        return
    for path in sorted(docs.rglob("*.md")):
        rel = relative(root, path)
        if rel.startswith(EXCLUDED_DOC_PREFIXES):
            continue
        yield path


def record_paths(root: Path):
    ledger = root / "ledger"
    if not ledger.is_dir():
        return
    for path in sorted(ledger.rglob("*")):
        if path.is_file() and path.suffix in (".json", ".md", ".yaml"):
            yield path


def load_record(path: Path) -> dict:
    if path.suffix == ".json":
        return read_json(path)
    if path.suffix == ".md":
        meta, _ = load_artifact(path)
        return meta or {}
    return read_yaml(path) or {}


def load_index(root: Path) -> Index:
    index = Index(root=root)
    seen = {}

    def register(identifier, where):
        if identifier in seen:
            index.duplicates.append((identifier, seen[identifier], where))
        else:
            seen[identifier] = where

    register_path = root / "docs/sources/source-register.yaml"
    if register_path.is_file():
        try:
            data = read_yaml(register_path) or {}
            for source in data.get("sources") or []:
                if isinstance(source, dict) and source.get("id"):
                    index.sources[source["id"]] = source
                    register(source["id"], relative(root, register_path))
        except Exception as error:  # reported by check
            index.problems.append((register_path, f"cannot parse source register: {error}"))

    for path in artifact_paths(root):
        try:
            meta, body = load_artifact(path)
        except Exception as error:
            index.problems.append((path, f"cannot parse front matter: {error}"))
            continue
        if meta is None or "id" not in meta:
            continue
        identifier = str(meta["id"])
        register(identifier, relative(root, path))
        index.artifacts.setdefault(identifier, Artifact(identifier, path, meta, body))

    for path in record_paths(root):
        try:
            data = load_record(path)
        except Exception as error:
            index.problems.append((path, f"cannot parse record: {error}"))
            continue
        identifier = str(data.get("id", path.stem))
        register(identifier, relative(root, path))
        kind = identifier.split("-", 1)[0]
        index.records.setdefault(identifier, Record(identifier, path, kind, data))

    return index


def load_scopes(root: Path) -> dict:
    path = root / ".claude/hooks/agent-scopes.json"
    return read_json(path) if path.is_file() else {}


def load_authority(root: Path) -> dict:
    path = root / "docs/governance/authority-matrix.yaml"
    return (read_yaml(path) or {}) if path.is_file() else {}

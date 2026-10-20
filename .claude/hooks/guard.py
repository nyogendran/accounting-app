"""PreToolUse guard for TIQACC.

Blocks, for every actor:
  - writes to protected paths (registered sources, decision records);
  - rewriting an existing record under ledger/;
  - shell commands that write to protected paths.
Blocks, by agent name (agent_type in the hook input):
  - file writes outside the agent's scope;
  - shell commands outside the agent's shell profile.
Blocks, for the orchestrator: pushing, force operations, hard resets, recursive deletes and
approving pull requests.

Exit code 2 blocks the tool call and shows the reason to Claude. Any internal error also exits 2
(fail closed). Scopes live in .claude/hooks/agent-scopes.json.
"""
from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.governance import common  # noqa: E402

WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
SHELL_TOOLS = {"Bash", "PowerShell"}

BENIGN_REDIRECTS = re.compile(r"\d?>&\d|\d?>\s*/dev/null|\d?>\s*\$null|\d?>\s*nul\b", re.IGNORECASE)
WRITE_INDICATORS = re.compile(
    r">|\btee\b|\bcp\b|\bmv\b|\brm\b|\bsed\s+-i|\bdd\b|\btruncate\b|\bchmod\b|\bln\b"
    r"|\bSet-Content\b|\bAdd-Content\b|\bOut-File\b|\bRemove-Item\b|\bMove-Item\b|\bCopy-Item\b"
    r"|\bNew-Item\b|\bRename-Item\b|\bClear-Content\b"
    r"|\bgit\s+(checkout|restore|rm|mv)\b|\bpython3?\s+-c\b|\bperl\s+-[pi]",
    re.IGNORECASE,
)
SPLIT = re.compile(r"\s*(?:&&|\|\||;|\||\r?\n)\s*")


@dataclass
class Decision:
    allowed: bool
    reason: str = ""


def allow() -> Decision:
    return Decision(True)


def block(reason: str) -> Decision:
    return Decision(False, reason)


def _protected_fragments(patterns) -> list:
    fragments = []
    for pattern in patterns:
        literal = re.split(r"[*?]", pattern, maxsplit=1)[0]
        if literal:
            fragments.append(literal.lower())
    return fragments


def _decide_write(path_text, root: Path, agent, scopes) -> Decision:
    if not path_text:
        return block("file write without a path")
    rel = common.repo_relative(path_text, root)
    if rel is None:
        return allow()
    if common.glob_match(rel, scopes.get("protected")):
        return block(f"{rel} is protected (registered source or decision record); see CLAUDE.md rules 6 and 7")
    if common.glob_match(rel, scopes.get("append_only")) and (root / rel).exists():
        return block(f"{rel} is an existing record; records are never edited, so create a new record instead")
    if agent:
        config = (scopes.get("agents") or {}).get(agent) or scopes.get("unknown_agent") or {"write": []}
        inside = common.glob_match(rel, config.get("write")) and not common.glob_match(rel, config.get("deny"))
        if not inside:
            return block(f"agent '{agent}' may not write {rel}; its scope is {config.get('write') or 'nothing'}")
    return allow()


def _decide_shell(command: str, agent, scopes) -> Decision:
    text = command.replace("\\", "/")
    cleaned = BENIGN_REDIRECTS.sub(" ", text)
    lowered = cleaned.lower()
    for fragment in _protected_fragments(scopes.get("protected") or []):
        if fragment in lowered and WRITE_INDICATORS.search(cleaned):
            return block(f"shell command would write to a protected path ({fragment})")
    profiles = scopes.get("shell_profiles") or {}
    if agent:
        config = (scopes.get("agents") or {}).get(agent) or scopes.get("unknown_agent") or {}
        profile = profiles.get(config.get("shell", ""), {})
        patterns = [re.compile(p) for p in profile.get("allow", [])]
        for part in SPLIT.split(text.strip()):
            part = BENIGN_REDIRECTS.sub(" ", part).strip()
            if not part:
                continue
            if ">" in part:
                return block(f"agent '{agent}' may not redirect output to files")
            if not any(p.search(part) for p in patterns):
                return block(f"agent '{agent}' may not run '{part}' (shell profile '{config.get('shell')}')")
        return allow()
    for pattern in (profiles.get("orchestrator") or {}).get("deny", []):
        if re.search(pattern, cleaned, re.IGNORECASE):
            return block(f"command matches a blocked pattern ({pattern}); a person must do this")
    return allow()


def decide(payload: dict, root: Path) -> Decision:
    root = Path(root)
    scopes_path = root / ".claude/hooks/agent-scopes.json"
    if not scopes_path.is_file():
        raise FileNotFoundError(f"missing {scopes_path}")
    scopes = json.loads(scopes_path.read_text(encoding="utf-8"))
    tool = payload.get("tool_name") or ""
    tool_input = payload.get("tool_input") or {}
    agent = payload.get("agent_type") or None
    if tool in WRITE_TOOLS:
        path_text = tool_input.get("file_path") or tool_input.get("notebook_path") or tool_input.get("path")
        return _decide_write(path_text, root, agent, scopes)
    if tool in SHELL_TOOLS:
        return _decide_shell(str(tool_input.get("command") or ""), agent, scopes)
    return allow()


def main() -> int:
    try:
        payload = json.loads(sys.stdin.read())
        root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd())
        decision = decide(payload, root)
    except Exception as error:  # fail closed
        print(f"TIQACC governance guard failed closed: {error}", file=sys.stderr)
        return 2
    if decision.allowed:
        return 0
    print(f"Blocked by the TIQACC governance guard: {decision.reason}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())

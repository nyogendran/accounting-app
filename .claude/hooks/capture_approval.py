"""UserPromptSubmit hook: capture Stage 0 approval decisions (DEC-0003).

A decision is recorded only when the whole prompt is exactly one approval phrase, for example
`APPROVE AREQ-<ulid> <code>`. The hook, not an agent, writes the record under
ledger/approval-decisions/. Any other prompt passes through untouched. The hook never blocks a
prompt: if it fails, no decision is recorded, which is the safe outcome.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.governance import approvals  # noqa: E402


def identity(root: Path) -> str:
    user = os.environ.get("USERNAME") or os.environ.get("USER") or "unknown"
    try:
        name = subprocess.run(
            ["git", "config", "user.name"], cwd=root, capture_output=True, text=True, timeout=10
        ).stdout.strip()
    except Exception:
        name = ""
    return f"local:{user} / git:{name or 'unknown'}"


def main() -> int:
    try:
        payload = json.loads(sys.stdin.read())
    except Exception:
        return 0
    prompt = payload.get("prompt") or ""
    if approvals.parse_phrase(prompt) is None:
        return 0
    try:
        root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd())
        result = approvals.capture(root, prompt, str(payload.get("session_id") or ""), identity(root))
        message = f"Approval capture: {result.message}"
    except Exception as error:
        message = f"Approval capture: decision not recorded because the hook failed ({error})."
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": message}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""PostToolUse hook: run the governance checker on a file just written or edited.

Errors are shown to Claude (exit code 2) so they are fixed straight away. The tool call has
already happened, so this hook gives feedback; it cannot undo the write. If the hook itself
fails, it stays silent rather than blocking work.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.governance import check, common  # noqa: E402

CHECKED_PREFIXES = ("docs/", "ledger/", ".claude/agents/", ".claude/skills/", ".claude/rules/")


def main() -> int:
    try:
        payload = json.loads(sys.stdin.read())
        tool_input = payload.get("tool_input") or {}
        path_text = tool_input.get("file_path") or tool_input.get("notebook_path")
        root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd())
        rel = common.repo_relative(path_text, root) if path_text else None
        if not rel or not rel.startswith(CHECKED_PREFIXES):
            return 0
        targets = [rel, "docs/sources/source-register.yaml"] if rel.startswith("docs/sources/") else [rel]
        errors = [f for f in check.run_checks(root, files=targets) if f.level == "error"]
    except Exception:
        return 0
    if not errors:
        return 0
    print("Governance check found problems in the file you just changed:", file=sys.stderr)
    for finding in errors:
        print(f"  {finding}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())

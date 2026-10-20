"""Run the governance tool tests and record the run as E3 evidence.

Usage: python tools/governance/run_tests.py

Writes ledger/evidence/EVD-<ulid>.json with the command, exit code, test counts, HEAD commit, the
tree hash of the working tree (including uncommitted changes) and whether the tree was clean.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.governance import common  # noqa: E402

COMMAND = ["-m", "unittest", "discover", "-s", "tools/governance/tests", "-t", "."]


def git(root: Path, *args, env=None) -> str:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, env=env)
    return result.stdout.strip() if result.returncode == 0 else ""


def working_tree_hash(root: Path) -> str:
    """Tree hash of the working tree, computed in a temporary index so the real index is untouched.

    The temporary index starts as a copy of the real index, so staged file modes (such as an
    executable bit set with `git update-index --chmod=+x` on Windows) match what will be committed.
    """
    index_path = Path(git(root, "rev-parse", "--git-path", "index"))
    real_index = index_path if index_path.is_absolute() else root / index_path
    with tempfile.TemporaryDirectory() as folder:
        temp_index = Path(folder) / "index"
        env = dict(os.environ, GIT_INDEX_FILE=str(temp_index))
        if real_index.is_file():
            shutil.copyfile(real_index, temp_index)
        else:
            git(root, "read-tree", "HEAD", env=env)
        git(root, "add", "-A", env=env)
        return git(root, "write-tree", env=env)


def main() -> int:
    root = common.find_root()
    head = git(root, "rev-parse", "HEAD")
    clean = git(root, "status", "--porcelain") == ""
    tree = working_tree_hash(root)
    process = subprocess.run([sys.executable, *COMMAND], cwd=root, capture_output=True, text=True)
    output = process.stdout + process.stderr
    print(output)
    ran = re.search(r"Ran (\d+) tests?", output)
    failed = re.search(r"FAILED \(([^)]*)\)", output)
    record = {
        "id": f"EVD-{common.new_ulid()}",
        "type": "evidence",
        "kind": "test-run",
        "level": "E3",
        "producer": "tools/governance/run_tests.py",
        "command": "python " + " ".join(COMMAND),
        "exit_code": process.returncode,
        "result": "pass" if process.returncode == 0 else "fail",
        "tests_run": int(ran.group(1)) if ran else None,
        "failures": failed.group(1) if failed else None,
        "head": head,
        "tree": tree,
        "clean": clean,
        "python": sys.version.split()[0],
        "output_sha256": common.sha256_text(output),
        "recorded_at": common.utc_now(),
    }
    target = root / "ledger/evidence" / f"{record['id']}.json"
    common.write_json(target, record)
    print(f"Evidence recorded: {common.relative(root, target)} ({record['result']}, {record['tests_run']} tests)")
    return process.returncode


if __name__ == "__main__":
    sys.exit(main())

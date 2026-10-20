"""Test helpers: a throwaway repository with the minimum governance structure."""
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]


class TempRepo:
    """A temporary repository laid out like TIQACC, without any real content."""

    def __init__(self):
        self.root = Path(tempfile.mkdtemp(prefix="tiqacc-test-"))
        self.write_text("CLAUDE.md", "# test repository\n")
        self.write_text(".gitignore", ".claude/state/\n")
        for folder in (
            "docs/governance/decisions",
            "docs/requirements",
            "docs/sources",
            "ledger/approval-requests",
            "ledger/approval-decisions",
            "ledger/reviews",
            "ledger/evidence",
            ".claude/agents",
            ".claude/skills",
            ".claude/state",
        ):
            (self.root / folder).mkdir(parents=True, exist_ok=True)
        (self.root / ".claude/hooks").mkdir(parents=True, exist_ok=True)
        shutil.copy(
            REPO_ROOT / ".claude/hooks/agent-scopes.json",
            self.root / ".claude/hooks/agent-scopes.json",
        )
        self.write_yaml(
            "docs/governance/authority-matrix.yaml",
            {
                "version": 1,
                "roles": {
                    "governance-owner": {"person": "Test Owner", "delegate": None},
                    "product-owner": {"person": None, "delegate": None},
                },
                "decisions": [],
                "stage0": {"allowed_tiers": [2, 3]},
            },
        )
        self.write_yaml("docs/sources/source-register.yaml", {"version": 1, "sources": []})

    def cleanup(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def path(self, relative):
        return self.root / relative

    def write_text(self, relative, text):
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline="\n")
        return target

    def write_yaml(self, relative, data):
        return self.write_text(relative, yaml.safe_dump(data, sort_keys=False, allow_unicode=True))

    def write_artifact(self, relative, meta, body="Explanation.\n"):
        front = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True)
        return self.write_text(relative, f"---\n{front}---\n\n{body}")

    def git(self, *args, env=None):
        return subprocess.run(
            ["git", *args], cwd=self.root, capture_output=True, text=True, check=True, env=env
        )

    def git_init(self):
        self.git("init", "-q")
        self.git("config", "user.name", "Test Human")
        self.git("config", "user.email", "human@example.com")
        self.git("config", "commit.gpgsign", "false")


def requirement(
    identifier="REQ-GL-001",
    status="Proposed",
    statement="When a journal is approved, the system shall post it to the ledger.",
    tier=2,
    **extra,
):
    meta = {
        "id": identifier,
        "type": "requirement",
        "title": "Post approved journals",
        "status": status,
        "version": 1,
        "owner": "requirements-engineer",
        "tier": tier,
        "normative": {"statement": statement},
    }
    meta.update(extra)
    return meta


def decision(identifier="DEC-0001", status="Proposed", text="Adopt the framework.", **extra):
    meta = {
        "id": identifier,
        "type": "decision",
        "title": "A decision",
        "status": status,
        "version": 1,
        "owner": "orchestrator",
        "tier": 3,
        "normative": {"decision": text},
    }
    meta.update(extra)
    return meta


def story(identifier="US-GL-001", status="Proposed", planned_tests=("TC-GL-001",), **extra):
    meta = {
        "id": identifier,
        "type": "story",
        "title": "Post a journal",
        "status": status,
        "version": 1,
        "owner": "requirements-engineer",
        "tier": 2,
        "normative": {
            "story": "As an accountant, I want approved journals posted, so that balances are current.",
            "value": "Supports BO-01.",
            "acceptance_criteria": [
                {
                    "id": f"AC-{identifier}-01",
                    "given": "an approved balanced journal",
                    "when": "it is posted",
                    "then": "the ledger balances change by its lines",
                    "planned_tests": list(planned_tests),
                }
            ],
        },
    }
    meta.update(extra)
    return meta

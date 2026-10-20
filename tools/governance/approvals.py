"""Approval requests, Stage 0 decision capture and approval state.

Usage:
  python tools/governance/approvals.py hash <ID>
  python tools/governance/approvals.py request --subject <ID> [--subject <ID> ...] --role <role>
                                               [--tier N] [--note TEXT] [--brief BRF-...]
  python tools/governance/approvals.py status <ID>
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.governance import common  # noqa: E402

VERBS = {
    "APPROVE": "approve",
    "REJECT": "reject",
    "REQUEST-CHANGES": "request-changes",
    "DEFER": "defer",
    "ESCALATE": "escalate",
    "REVOKE": "revoke",
}
DECISIONS = tuple(VERBS.values())
PHRASE_RE = re.compile(
    rf"^({'|'.join(VERBS)}) (AREQ-{common.ULID}) ([0-9a-f]{{12}})(?: -- (\S.{{0,499}}))?$"
)
STATE_FOR_DECISION = {
    "revoke": "revoked",
    "reject": "rejected",
    "request-changes": "changes-requested",
    "defer": "deferred",
    "escalate": "escalated",
}


@dataclass
class Phrase:
    decision: str
    request: str
    code: str
    comment: str | None


@dataclass
class CaptureResult:
    status: str  # recorded | rejected | ignored
    message: str
    record: dict | None = None


@dataclass
class ApprovalState:
    state: str  # none | pending | valid | void | revoked | rejected | ... | insufficient-level | unknown
    decision_id: str | None = None
    detail: str = ""


def parse_phrase(prompt) -> Phrase | None:
    """Return the decision phrase if the whole prompt is exactly one, else None."""
    if not isinstance(prompt, str):
        return None
    text = prompt.strip()
    if "\n" in text or "\r" in text:
        return None
    match = PHRASE_RE.match(text)
    if not match:
        return None
    return Phrase(VERBS[match.group(1)], match.group(2), match.group(3), match.group(4))


def combined_hash(subjects) -> str:
    lines = sorted(f"{subject['id']} {subject['hash']}" for subject in subjects)
    return "sha256:" + common.sha256_text("\n".join(lines))


def phrase_for(request: dict, verb: str = "APPROVE") -> str:
    return f"{verb} {request['id']} {request['phrase_code']}"


def _head_commit(root: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, check=True
        )
        return result.stdout.strip() or None
    except Exception:
        return None


def create_request(root, subject_ids, role, tier=None, note="", brief=None, created_by="orchestrator"):
    root = Path(root)
    index = common.load_index(root)
    subjects = []
    tiers = []
    for identifier in subject_ids:
        artifact = index.artifacts.get(identifier)
        if artifact is None:
            raise ValueError(f"unknown artifact {identifier}")
        subjects.append(
            {
                "id": identifier,
                "version": artifact.meta.get("version"),
                "hash": common.normative_hash(artifact.meta),
            }
        )
        if artifact.meta.get("tier") in (1, 2, 3):
            tiers.append(artifact.meta["tier"])
    combined = combined_hash(subjects)
    request = {
        "id": f"AREQ-{common.new_ulid()}",
        "type": "approval-request",
        "created_at": common.utc_now(),
        "created_by": created_by,
        "required_role": role,
        "tier": tier if tier is not None else (min(tiers) if tiers else None),
        "subjects": subjects,
        "combined": combined,
        "phrase_code": combined[7:19],
        "provenance_commit": _head_commit(root),
        "brief": brief,
        "note": note,
    }
    common.write_json(root / "ledger/approval-requests" / f"{request['id']}.json", request)
    return request


def capture(root, prompt, session_id, identity, log=True) -> CaptureResult:
    """Record a decision typed as an exact phrase. Used by the UserPromptSubmit hook."""
    root = Path(root)
    phrase = parse_phrase(prompt)
    if phrase is None:
        return CaptureResult("ignored", "no approval phrase")
    request_path = root / "ledger/approval-requests" / f"{phrase.request}.json"
    if not request_path.is_file():
        return CaptureResult(
            "rejected", f"Decision not recorded: approval request {phrase.request} does not exist."
        )
    request = common.read_json(request_path)
    if request.get("phrase_code") != phrase.code:
        return CaptureResult(
            "rejected",
            f"Decision not recorded: the code does not match {phrase.request}. Copy the phrase exactly.",
        )
    index = common.load_index(root)
    changed = []
    for subject in request.get("subjects", []):
        artifact = index.artifacts.get(subject["id"])
        current = common.normative_hash(artifact.meta) if artifact else None
        if current != subject["hash"]:
            changed.append({"id": subject["id"], "requested_hash": subject["hash"], "current_hash": current})
    record = {
        "id": f"APR-{common.new_ulid()}",
        "type": "approval-decision",
        "request": request["id"],
        "decision": phrase.decision,
        "subjects": request["subjects"],
        "combined": request["combined"],
        "stale": bool(changed),
        "by": {"role": request.get("required_role"), "identity": identity},
        "channel": "stage0-session",
        "level": "E1-op",
        "attestation": {
            "hook": "capture-approval",
            "session_id": session_id,
            "prompt_sha256": common.sha256_text(prompt.strip()),
        },
        "recorded_at": common.utc_now(),
        "comment": phrase.comment,
    }
    if changed:
        record["stale_detail"] = changed
    target = root / "ledger/approval-decisions" / f"{record['id']}.json"
    common.write_json(target, record)
    if log:
        log_path = root / ".claude/state/capture-log.jsonl"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(log_path, "a", encoding="utf-8", newline="\n") as handle:
            entry = {"id": record["id"], "sha256": common.sha256_file(target), "recorded_at": record["recorded_at"]}
            handle.write(json.dumps(entry) + "\n")
    subjects = ", ".join(subject["id"] for subject in request["subjects"])
    message = f"Recorded {record['id']}: {phrase.decision} on {request['id']} ({subjects})."
    if changed:
        message += " STALE: the content changed after the request, so this decision does not count."
    return CaptureResult("recorded", message, record)


def approval_state(root_or_index, artifact_id: str) -> ApprovalState:
    index = root_or_index if isinstance(root_or_index, common.Index) else common.load_index(Path(root_or_index))
    artifact = index.artifacts.get(artifact_id)
    if artifact is None:
        return ApprovalState("unknown", detail=f"{artifact_id} not found")
    current = common.normative_hash(artifact.meta)
    tier = artifact.meta.get("tier")
    allowed_tiers = (common.load_authority(index.root).get("stage0") or {}).get("allowed_tiers", [2, 3])

    requests = {
        record.id: record.data
        for record in index.records.values()
        if record.kind == "AREQ" and any(s.get("id") == artifact_id for s in record.data.get("subjects", []))
    }
    if not requests:
        return ApprovalState("none")
    at_current = {
        request_id
        for request_id, request in requests.items()
        if any(s.get("id") == artifact_id and s.get("hash") == current for s in request.get("subjects", []))
    }
    decisions = sorted(
        (record.data for record in index.records.values() if record.kind == "APR"),
        key=lambda data: (data.get("recorded_at", ""), data.get("id", "")),
    )

    latest_by_approver = {}
    for data in decisions:
        if data.get("request") in at_current and not data.get("stale"):
            key = (data["request"], (data.get("by") or {}).get("identity"))
            latest_by_approver[key] = data
    if latest_by_approver:
        effective = sorted(latest_by_approver.values(), key=lambda d: (d.get("recorded_at", ""), d.get("id", "")))
        approvals_now = [d for d in effective if d.get("decision") == "approve"]
        if approvals_now:
            best = approvals_now[-1]
            if best.get("level") == "E1-op" and tier is not None and tier not in allowed_tiers:
                return ApprovalState(
                    "insufficient-level",
                    best["id"],
                    f"Tier {tier} needs an E1 approval; Stage 0 (E1-op) covers tiers {allowed_tiers}.",
                )
            return ApprovalState("valid", best["id"])
        last = effective[-1]
        return ApprovalState(STATE_FOR_DECISION.get(last.get("decision"), "none"), last.get("id"))
    if at_current:
        return ApprovalState("pending")
    older = [
        d for d in decisions
        if d.get("request") in requests and d.get("decision") == "approve" and not d.get("stale")
    ]
    if older:
        return ApprovalState("void", older[-1]["id"], "the approved content has changed since approval")
    return ApprovalState("none")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Approval requests and approval state.")
    parser.add_argument("--root", type=Path)
    sub = parser.add_subparsers(dest="command", required=True)
    hash_parser = sub.add_parser("hash", help="print the normative hash of an artifact")
    hash_parser.add_argument("id")
    request_parser = sub.add_parser("request", help="create an approval request")
    request_parser.add_argument("--subject", action="append", required=True)
    request_parser.add_argument("--role", required=True)
    request_parser.add_argument("--tier", type=int)
    request_parser.add_argument("--note", default="")
    request_parser.add_argument("--brief")
    status_parser = sub.add_parser("status", help="print the approval state of an artifact")
    status_parser.add_argument("id")
    args = parser.parse_args(argv)
    root = args.root or common.find_root()

    if args.command == "hash":
        artifact = common.load_index(root).artifacts.get(args.id)
        if artifact is None:
            print(f"Unknown artifact {args.id}", file=sys.stderr)
            return 1
        print(common.normative_hash(artifact.meta))
        return 0
    if args.command == "request":
        roles = (common.load_authority(root).get("roles") or {}).keys()
        if args.role not in roles:
            print(f"Unknown role {args.role}; roles: {', '.join(roles)}", file=sys.stderr)
            return 1
        request = create_request(root, args.subject, args.role, args.tier, args.note, args.brief)
        print(f"Approval request {request['id']} for {', '.join(args.subject)} (role {args.role}).")
        print("To decide, type exactly one of these as the whole prompt:")
        for verb in ("APPROVE", "REQUEST-CHANGES", "REJECT"):
            print(f"  {phrase_for(request, verb)}")
        return 0
    state = approval_state(root, args.id)
    print(f"{args.id}: {state.state}" + (f" ({state.decision_id})" if state.decision_id else "")
          + (f" - {state.detail}" if state.detail else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())

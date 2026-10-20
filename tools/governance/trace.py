"""Traceability queries: explain an ID, check readiness, summarise coverage.

Usage:
  python tools/governance/trace.py explain <ID>
  python tools/governance/trace.py readiness <ID>
  python tools/governance/trace.py coverage

Derived states are computed here from evidence and never stored. States that need code, CI or
deployment evidence report "no evidence" until those exist (from L5 and F4).
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.governance import approvals, common  # noqa: E402

# Reviews that must be bound to an artifact's current hash before it is ready (SRC-005, C1).
MANDATORY_REVIEWERS = {
    "requirement": ("requirements-assurance", "accounting-domain-expert"),
    "story": ("requirements-assurance", "accounting-domain-expert"),
    "policy": ("requirements-assurance",),
    "rule": ("requirements-assurance",),
    "invariant": ("requirements-assurance",),
    "scenario": ("requirements-assurance",),
}
SPECIFIABLE = ("requirement", "story", "policy", "rule", "invariant", "scenario")
CLOSED_STATUSES = ("Approved", "Rejected", "Superseded")
LATER_STATES = (
    "Implementation claimed",
    "Implemented",
    "Tested",
    "Agent-reviewed",
    "Reviewed",
    "Deployed",
    "Operationally verified",
)


@dataclass
class Condition:
    name: str
    ok: bool
    detail: str = ""


@dataclass
class Readiness:
    id: str
    ready: bool
    conditions: list = field(default_factory=list)


def reviews_for(index: common.Index, artifact_id: str) -> list:
    found = []
    for record in index.records.values():
        if record.kind != "REV":
            continue
        for subject in record.data.get("subjects") or []:
            if isinstance(subject, dict) and subject.get("id") == artifact_id:
                found.append((record, subject.get("hash")))
    return found


def blocking_items(index: common.Index, artifact_id: str) -> list:
    items = []
    for other in index.artifacts.values():
        blocks = (other.meta.get("links") or {}).get("blocks") or []
        if artifact_id not in [str(b) for b in blocks]:
            continue
        if other.meta.get("type") == "issue":
            if str(other.meta.get("issue_state", "")).lower() == "closed":
                continue
        elif other.meta.get("status") in CLOSED_STATUSES:
            continue
        items.append(other.id)
    return items


def explain(index: common.Index, identifier: str) -> dict:
    artifact = index.artifacts.get(identifier)
    if artifact is None:
        if identifier in index.records:
            record = index.records[identifier]
            return {"id": identifier, "found": True, "record": True, "path": common.relative(index.root, record.path), "data": record.data}
        if identifier in index.sources:
            return {"id": identifier, "found": True, "source": True, "data": index.sources[identifier]}
        return {"id": identifier, "found": False}
    meta = artifact.meta
    current = common.normative_hash(meta)
    state = approvals.approval_state(index, identifier)
    links_out = [(name, str(t)) for name, targets in (meta.get("links") or {}).items() for t in targets or []]
    links_in = []
    for other in index.artifacts.values():
        for name, targets in (other.meta.get("links") or {}).items():
            if identifier in [str(t) for t in targets or []]:
                links_in.append((name, other.id))
    reviews = [
        {
            "id": record.id,
            "reviewer": record.data.get("reviewer"),
            "verdict": record.data.get("verdict"),
            "at_current_hash": digest == current,
        }
        for record, digest in reviews_for(index, identifier)
    ]
    specified = state.state == "valid" and meta.get("type") in SPECIFIABLE
    return {
        "id": identifier,
        "found": True,
        "path": common.relative(index.root, artifact.path),
        "type": meta.get("type"),
        "title": meta.get("title"),
        "status": meta.get("status"),
        "version": meta.get("version"),
        "tier": meta.get("tier"),
        "hash": current,
        "approval": state,
        "links_out": links_out,
        "links_in": links_in,
        "reviews": reviews,
        "blocking": blocking_items(index, identifier),
        "derived": {"Specified": "yes" if specified else "no", **{s: "no evidence" for s in LATER_STATES}},
    }


def render_explain(info: dict) -> str:
    if not info.get("found"):
        return f"{info['id']}: not found"
    if info.get("record") or info.get("source"):
        return f"{info['id']}: {'record' if info.get('record') else 'source'}\n{info['data']}"
    approval = info["approval"]
    lines = [
        f"{info['id']} ({info['type']}): {info['title']}",
        f"  file: {info['path']}",
        f"  status: {info['status']} | version {info['version']} | tier {info['tier']}",
        f"  normative hash: {info['hash']}",
        f"  approval: {approval.state}"
        + (f" ({approval.decision_id})" if approval.decision_id else "")
        + (f" - {approval.detail}" if approval.detail else ""),
    ]
    lines.append("  links out: " + (", ".join(f"{n} -> {t}" for n, t in info["links_out"]) or "none"))
    lines.append("  links in: " + (", ".join(f"{t} ({n})" for n, t in info["links_in"]) or "none"))
    if info["reviews"]:
        for review in info["reviews"]:
            where = "current hash" if review["at_current_hash"] else "older hash (stale)"
            lines.append(f"  review {review['id']}: {review['reviewer']}, {review['verdict']}, {where}")
    else:
        lines.append("  reviews: none")
    lines.append("  blocking: " + (", ".join(info["blocking"]) or "none"))
    lines.append("  derived states: " + "; ".join(f"{k}: {v}" for k, v in info["derived"].items()))
    return "\n".join(lines)


def readiness(index: common.Index, identifier: str) -> Readiness:
    artifact = index.artifacts.get(identifier)
    if artifact is None:
        return Readiness(identifier, False, [Condition("artifact exists", False, "not found")])
    meta = artifact.meta
    current = common.normative_hash(meta)
    conditions = []

    state = approvals.approval_state(index, identifier)
    conditions.append(Condition("approved at current hash", state.state == "valid", state.state))

    missing = []
    for reviewer in MANDATORY_REVIEWERS.get(meta.get("type"), ()):
        ok = any(
            record.data.get("reviewer") == reviewer
            and digest == current
            and record.data.get("verdict") != "blocking-findings"
            for record, digest in reviews_for(index, identifier)
        )
        if not ok:
            missing.append(reviewer)
    conditions.append(
        Condition(
            "mandatory reviews at current hash",
            not missing,
            "missing or blocking: " + ", ".join(missing) if missing else "",
        )
    )

    blockers = blocking_items(index, identifier)
    conditions.append(Condition("no open blocking question or issue", not blockers, ", ".join(blockers)))

    governing = [str(t) for t in (meta.get("links") or {}).get("governed_by") or []]
    unapproved = [t for t in governing if approvals.approval_state(index, t).state != "valid"]
    conditions.append(
        Condition("governing policies and rules approved", not unapproved, ", ".join(unapproved))
    )

    criteria = (meta.get("normative") or {}).get("acceptance_criteria") or []
    untested = [c.get("id", "?") for c in criteria if isinstance(c, dict) and not c.get("planned_tests")]
    conditions.append(
        Condition("every acceptance criterion has a planned test", not untested, ", ".join(untested))
    )

    conditions.append(Condition("risk tier set", meta.get("tier") in (1, 2, 3), str(meta.get("tier"))))
    return Readiness(identifier, all(c.ok for c in conditions), conditions)


def coverage(index: common.Index) -> dict:
    by_type = Counter(a.meta.get("type") for a in index.artifacts.values())
    approval_states = Counter()
    for artifact in index.artifacts.values():
        if artifact.meta.get("type") in common.NORMATIVE_TYPES:
            approval_states[approvals.approval_state(index, artifact.id).state] += 1
    refined = {
        str(t)
        for a in index.artifacts.values()
        for t in (a.meta.get("links") or {}).get("refines") or []
    }
    requirements_without_stories = sorted(
        a.id for a in index.artifacts.values() if a.meta.get("type") == "requirement" and a.id not in refined
    )
    stories_without_tests = sorted(
        a.id
        for a in index.artifacts.values()
        if a.meta.get("type") == "story"
        and any(
            isinstance(c, dict) and not c.get("planned_tests")
            for c in (a.meta.get("normative") or {}).get("acceptance_criteria") or []
        )
    )
    return {
        "by_type": dict(by_type),
        "approval_states": dict(approval_states),
        "requirements_without_stories": requirements_without_stories,
        "stories_without_planned_tests": stories_without_tests,
        "sources": sorted(index.sources),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="TIQACC traceability queries.")
    parser.add_argument("--root", type=Path)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("explain").add_argument("id")
    sub.add_parser("readiness").add_argument("id")
    sub.add_parser("coverage")
    args = parser.parse_args(argv)
    index = common.load_index(args.root or common.find_root())
    if args.command == "explain":
        info = explain(index, args.id)
        print(render_explain(info))
        return 0 if info.get("found") else 1
    if args.command == "readiness":
        result = readiness(index, args.id)
        print(f"{result.id}: {'READY' if result.ready else 'NOT READY'}")
        for condition in result.conditions:
            mark = "ok " if condition.ok else "NO "
            print(f"  [{mark}] {condition.name}" + (f" - {condition.detail}" if condition.detail else ""))
        return 0 if result.ready else 1
    summary = coverage(index)
    for key, value in summary.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

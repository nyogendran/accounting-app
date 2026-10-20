---
name: status-report
description: Produce a TIQACC progress report at a workflow transition - phase and gate, work done, artifacts, verification actually performed, open questions, risks, decisions needed, gate status and next action. Use at every major transition or when asked for status.
---

# Status report

Build the report from the repository, not from memory:

1. Read `docs/governance/project-state.md`, `git log --oneline` since the last report, open items in
   `docs/governance/decisions/` and `docs/governance/risk-register.yaml`.
2. Run `python tools/governance/check.py` and `python tools/governance/trace.py coverage`.
3. Report, in this order:
   - **Phase and gate:** current phase (L0 to L7) and the gate's state: passed, blocked or awaiting
     approval.
   - **Work completed** since the last report, with commit IDs.
   - **Artifacts created or updated**, with IDs and versions.
   - **Verification performed and observed results:** only checks whose output you saw; say what was
     not verified.
   - **Open questions and unresolved contradictions**, each with its decision owner.
   - **Risks and decisions needed from people.**
   - **Next recommended action.**
4. Keep proposed work and completed work clearly separate. Update `docs/governance/project-state.md`
   if it is out of date.

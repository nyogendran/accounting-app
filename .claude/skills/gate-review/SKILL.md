---
name: gate-review
description: Assemble a TIQACC gate package (Gate 0, A, B, C or D) - criteria, evidence, open risks and decisions - and request the approver's captured decision. Use at the end of a lifecycle phase or increment.
argument-hint: <gate> <scope>
---

# Gate review

1. **Read the gate's criteria** in `docs/governance/methodology.md` (Gates table) and, for Gate D,
   the separate customer acceptance rules.
2. **Gather evidence, not claims:**
   - `python tools/governance/check.py` (no errors allowed);
   - `python tools/governance/run_tests.py` when tools or code changed;
   - `python tools/governance/trace.py coverage`, and `readiness` for each in-scope story at Gate C;
   - the tool-path probe in GOV-F0-VALIDATION, re-run with the current Claude Code version and
     recorded with it: the guard judges tool paths the way that version was observed to resolve them
     (RISK-003);
   - the review records, decision records and commits the gate depends on.
3. **Write the gate record** `docs/governance/gates/GATE-<x>[-<scope>].md` from
   `docs/governance/templates/gate.md`: scope, each criterion with its evidence (IDs, commits,
   evidence records), conditions, open risks proposed for acceptance, and what is explicitly not
   covered. Status Proposed.
4. **Commit** the gate record, then create the approval request with the gate record and any
   decisions it confirms as subjects (`decision-brief` skill), for the role the methodology names.
5. **Present** a short summary, the evidence list, the open risks and the phrases. The gate passes
   only when the capture hook (or, later, the git host) records the decision on the current hashes.

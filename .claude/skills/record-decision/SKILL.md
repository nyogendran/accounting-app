---
name: record-decision
description: Record a TIQACC decision (DEC) or architecture decision (ADR) with its context, options and consequences, as Proposed. Use when a person or a workflow reaches a decision that should be traceable.
argument-hint: <short title>
---

# Record a decision

1. Take the next free ID: `DEC-nnnn` in `docs/governance/decisions/` (ADRs: `ADR-nnnn` in
   `docs/architecture/adr/`, owned by the architect from Gate A).
2. Copy `docs/governance/templates/decision.md` (or `adr.md`). Fill the normative block with the
   decision and its conditions; put context, options considered and consequences in the body.
3. Link what motivated it (`derives_from`, `related`) and what it replaces (`supersedes`).
4. Status stays **Proposed**. If a person decided in the conversation, record that under
   `decided_in_session` (date, channel, question, answer, transcribed by), and keep the status
   Proposed until a captured decision confirms it (use the `decision-brief` skill).
5. Run `python tools/governance/check.py`, update `docs/governance/project-state.md`, and commit
   under the agent identity with an `Agent: orchestrator` trailer.

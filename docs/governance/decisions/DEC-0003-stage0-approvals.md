---
id: DEC-0003
type: decision
title: Stage 0 approvals by hook capture
status: Approved
version: 1
owner: orchestrator
tier: 3
normative:
  decision: >-
    Before a git host exists, approvals are captured by a UserPromptSubmit hook when a person types
    an exact approval phrase as the whole prompt. The hook, not an agent, writes the decision record.
    Such approvals are operator-attested (E1-op).
  conditions:
    - E1-op approvals are valid for discovery work and Gate A, never for Tier 1.
    - All Stage 0 approvals are re-confirmed on the git host when Stage 1 starts.
    - A decision on content whose hash changed after the request is recorded as stale and does not count.
links:
  related: [SRC-005]
decided_in_session:
  date: 2026-10-20
  channel: Claude Code session, structured question (G4)
  question: How should approvals work before a git host exists (G4)?
  answer: Stage 0 hook capture (Recommended)
  transcribed_by: orchestrator
---

# DEC-0003: Stage 0 approvals by hook capture

Option (a) of decision G4 in SRC-005. The agent and the person share one OS account until the git
host exists, so this is best effort (RISK-003). The hook also fires on scheduled tasks, subagent
reports and messages from other sessions; it therefore accepts only an exact whole-prompt phrase.

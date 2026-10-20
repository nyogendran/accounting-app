---
id: DEC-0001
type: decision
title: Adopt the governed engineering framework and build F0
status: Approved
version: 1
owner: orchestrator
tier: 3
normative:
  decision: >-
    Adopt the engineering framework designed in SRC-005 (the architecture and operating-model review,
    revision 75 of 20 October 2026) and build its first phase, F0, in this repository.
  conditions:
    - Work proceeds in small, verified local commits under the agent identity, each with an Agent trailer. Nothing is pushed.
    - Gate 0 confirms the framework baseline with a captured decision.
    - Decisions G2 (authority names), G3 (platforms) and G5 (data boundary) stay open and are not assumed.
links:
  related: [SRC-005, SRC-006]
decided_in_session:
  date: 2026-10-20
  channel: Claude Code session, structured question
  question: May I start building F0, the governance core, in the repository now, as described in the review doc?
  answer: Yes, start F0 (Recommended)
  transcribed_by: orchestrator
---

# DEC-0001: Adopt the governed engineering framework and build F0

## Context

SRC-006 (the bootstrap plan of 19 October 2026) proposed a governance framework. The governance owner
asked for an architecture and operating-model review of extended requirements before approving it.
SRC-005 is that review, revised after an independent adversarial review found 25 problems.

## Decision

As stated in the normative block. The approach was chosen in this session; this record stays
Proposed until the decision is captured at Gate 0, because no agent may record an approval.

## Consequences

- F0 delivers only what discovery needs (SRC-005, section F).
- Approvals before a git host exists are operator-attested (DEC-0003) and never count for Tier 1.

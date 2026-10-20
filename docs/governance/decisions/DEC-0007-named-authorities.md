---
id: DEC-0007
type: decision
title: Name the people in the authority matrix (G2)
status: Proposed
version: 1
owner: orchestrator
tier: 3
normative:
  decision: >-
    Fill in the authority matrix with the people the governance owner named on 2026-10-20. Once this
    decision is approved, the orchestrator updates docs/governance/authority-matrix.yaml to match it.
  roles:
    governance-owner: Yogendran (Yogi)
    tech-lead: Yogendran (Yogi)
    security-owner: Yogendran (Yogi)
    release-authority: Yogendran (Yogi)
    product-owner: Shifan Cader, CFO
    tax-specialist: Shifan Cader, CFO, for Sri Lanka and Norway
    qualified-accountant: Rifaz Hajirin
  escalation:
    qualified-accountant: Shifan Cader, CFO
  conditions:
    - Tier-1 accounting policy needs both Rifaz Hajirin (qualified accountant) and Shifan Cader (product owner).
    - Tier-1 releases need both Yogendran (release authority) and Shifan Cader (product owner).
    - Shifan Cader and Rifaz Hajirin confirm their roles, and their GitHub accounts are recorded, when Stage 1 starts.
links:
  related: [DEC-0002, DEC-0003]
---

# DEC-0007: Name the people in the authority matrix (G2)

**Context.** SRC-005 decision G2 asks for named people in the authority matrix before Gate A. Until
now the matrix held only the governance owner, unnamed. The governance owner named the people on
2026-10-20, in answer to the first discovery questions.

**People holding several roles.** The matrix's small-team rule asks for this to be recorded:

- Yogendran holds governance owner, tech lead, security owner and release authority.
- Shifan Cader holds product owner and tax specialist.

The rule against one person being both qualified accountant and product owner for Tier-1 items is
met, because Rifaz Hajirin and Shifan Cader are different people.

**Consequences.**

- Once two people are named, any later change to the authority matrix needs two approvers. That is
  already a rule of the matrix.
- Shifan Cader and Rifaz Hajirin can approve in Stage 0 only by typing a phrase in the governance
  owner's session. That approval is attested by whoever operates the session (E1-op), not by their
  own identity. Their approvals carry their own identity once GitHub approvals (F2) exist.

**Not decided here.**

- Who signs customer module acceptance (SRC-001 §2.16.4).
- Who the Managing Director is, as the specification approver named in SRC-001 section 3.
- Who the tax specialist escalates to; the matrix keeps the qualified accountant.

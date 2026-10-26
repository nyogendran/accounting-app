---
id: DEC-0009
type: decision
title: Clause IDs for SRC-007 (S7) and strict checking of clause links
status: Proposed
version: 1
owner: orchestrator
tier: 3
normative:
  decision: >-
    Clauses of SRC-007 are identified as S7-<section>-c<nn>, numbered in document order within each
    section under the same rules as the SRC-001 clause index, and are defined by
    docs/requirements/clause-index-src007.yaml. S1 IDs stay as they are, defined by
    docs/requirements/clause-index.yaml. A clause link must name a clause in its own source's index;
    it produces a warning only while that index does not exist, and an error once it does.
  conditions:
    - The change is the one in commit dca68c6 (conventions.md v2, check.py, common.py and their tests), reviewed in REV-01M5VHRCEQP734DHRKE29J5YES and REV-01M5VJJW4XDTK3F6EKJ9M0GNWF.
    - The remaining non-blocking findings are tracked, not waived; the first of them (a deleted or uncommitted index degrades links to warnings) is fixed before any artifact that cites S7 clauses is approved.
links:
  related: [SRC-001, SRC-007, DEC-0008, REV-01M5VHRCEQP734DHRKE29J5YES, REV-01M5VJJW4XDTK3F6EKJ9M0GNWF]
---

# DEC-0009: Clause IDs for SRC-007 and strict checking of clause links

**Context.** DEC-0008 proposes SRC-007, the V2.2 specification, as the requirements baseline. Its clauses
need stable IDs before anything can cite them. Conventions change only through a decision approved by
the governance owner, with the checker and its tests changed in the same change
(`docs/governance/conventions.md`).

**What changed (commit dca68c6).**

- A new ID kind, S7, for clauses of SRC-007.
- A map from each clause kind to its own index.
- The checker now enforces a rule the conventions already stated: a linked clause must exist in its
  index. Until now a clause missing from an existing index only produced a warning, and a commit does
  not stop on warnings. The independent review found this (blocking), and the fix was re-reviewed
  (non-blocking).
- All 172 tool tests pass (EVD-01M5VJJMZ19QHQ5HEQ5KZ8HY5H).

**Options considered.**

- (a) Make the checker strict, matching the convention. This is the chosen option.
- (b) Change the convention to say that warnings are intended. Rejected: it would let broken trace
  links into commits.

**Why the governance owner.** It is a change to the framework's conventions and tools (authority
matrix, "Changes to this framework"). It does not depend on DEC-0008: S1 IDs keep working, and S7
IDs stay valid whichever baseline is approved.

**Open, non-blocking (REV-01M5VJJW4XDTK3F6EKJ9M0GNWF):**

- a deleted or uncommitted index degrades its links to warnings;
- a malformed index file stops the checker with an error trace instead of a finding;
- an ID placed in the wrong kind's index is not reported.

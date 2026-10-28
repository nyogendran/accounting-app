---
id: DEC-0010
type: decision
title: Gates A and B per increment, and a foundation increment before release-1 scope is settled
status: Proposed
version: 1
owner: orchestrator
tier: 3
normative:
  decision: >-
    Gates A and B may be passed for one increment at a time, not only for the whole of release 1. The
    first increment is a foundation increment: platform and ledger capabilities that V2.2 states
    plainly, or makes configurable per tenant or entity, and that do not depend on the release-1
    scope decision (Q-029) or on any question still classified as blocking for them. Its Gate A covers
    its own requirements and stories, its Gate B its own architecture decisions (including the stack
    ADR) and design, and its Gate C is unchanged. Release-1 Gates A and B still follow for the rest of
    release 1, and must not contradict what the foundation increment approved without a change
    request.
  conditions:
    - The foundation increment's scope is itself proposed, reviewed by the requirements-assurance agent and approved by the product owner before its requirements are written; each requirement traces to an S7 clause or a decision.
    - Every open question is classified for the foundation increment as blocking or not, with the reason; a blocking question either gets its owner's answer or its capability leaves the increment.
    - Answers recorded as "answer so far" by the governance owner for questions owned by another role (Q-031, Q-032, Q-033, Q-038, Q-040) are working assumptions, labelled as such in every artifact that relies on them, until their owner confirms them.
    - Nothing in methodology.md's risk tiers changes. The foundation is Tier 1 (posting, numbering, periods, audit, authorisation, isolation, money and rounding), so its approvals and merges need named people on the git host (Stage 1, F2); Stage 0 approvals (E1-op) do not count for it. Design, tests and code may be prepared before F2, but no Tier-1 work is approved or merged until F2 is in place.
    - Accounting policy in the increment needs the qualified accountant and the product owner (DEC-0007 conditions).
links:
  related: [DEC-0001, DEC-0003, DEC-0007, DEC-0008, Q-029, Q-031, Q-032, Q-033, Q-038, Q-040, Q-054]
decided_in_session:
  date: 2026-10-28
  channel: Claude Code session
  question: "Can we not conclude the technical design and start the implementation based on the context that we do have at this moment?"
  answer: >-
    The governance owner answered the technical questions the orchestrator listed as preconditions for a
    foundation increment (Q-031, Q-032, Q-033, Q-038, Q-040, Q-054). The decision itself is not yet
    approved.
  transcribed_by: orchestrator
---

# DEC-0010: Gates A and B per increment, and a foundation increment

**Context.** The methodology (`docs/governance/methodology.md`) passes Gate A on the release-1
requirements and Gate B on the release-1 design, then Gate C per increment. Release-1 scope waits on
the product owner and the qualified accountant: Q-029, and the control-account questions before it.
The governance owner asked on 2026-10-28 whether design and build could start on what is known.

Much of V2.2 does not depend on those answers: it is stated plainly, or V2.2 makes it a setting per
tenant or entity, as it does the control enforcement levels (p.27). The governance owner has given
working answers on the questions that shape the platform: the tenant (Q-031), control accounts (Q-032,
Q-033), capacity (Q-038), currency precision (Q-040) and hosting (Q-054).

**Options considered.**

- (a) Keep Gates A and B for the whole of release 1. Nothing is designed or built until release-1
  scope is settled.
- (b) Gates A and B per increment, starting with a foundation increment. **Proposed.**
- (c) Start building without Gates A and B. Rejected: it removes the controls in CLAUDE.md rule 1 and
  the methodology, and would leave Tier-1 code with no approved requirement to test against.

**The foundation increment, as first proposed** (its scope is proposed and approved separately):

- tenants as organisations, with a firm's access to its clients' tenants (Q-031), users, roles and the
  audit log;
- double-entry journals: balanced, unchangeable once posted, corrected by reversal;
- periods, opened and closed;
- gapless numbering series held as configuration;
- the chart of accounts, with control flags and enforcement levels held as settings;
- currencies, with decimal places from each currency's configuration (Q-040).

**Consequences.**

- Design and tests for the foundation can proceed while Shifan and Rifaz answer the question pack.
- Approving and merging the foundation needs F2 (GitHub, Stage 1), because all of it is Tier 1. F2
  needs the repository URL, an instruction to push, and Shifan's and Rifaz's GitHub accounts.
- If an owner's later answer differs from a working answer, the affected foundation artifacts change
  by change request.

**Why the governance owner.** It changes how the framework's gates apply (authority matrix, "Changes
to this framework"). It does not change any gate's approver or evidence.

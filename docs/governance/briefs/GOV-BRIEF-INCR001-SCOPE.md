---
id: GOV-BRIEF-INCR001-SCOPE
type: governance
title: "Decision brief: scope of the foundation increment (INCR-001)"
status: Proposed
version: 1
owner: orchestrator
links:
  related: [GOV-SCOPE-INCR-001, DEC-0010, DEC-0007, Q-007, Q-013, Q-014, Q-031, Q-034, Q-055, Q-056, Q-057, Q-054, REV-01M61MRRKX52P8XHG3NZXSPCZJ, REV-01M61PXHZBS8N3YVQX2XDJHHWH, REV-01M61QHQX58WSCVFQMT2EPXSRD, REV-01M61R5FTD3DD5RK7G0TH7G0NS, REV-01M61SP5CTK2J8YYRVRR7C9DMX, REV-01M61T1JTQRPGVY07V648NPMWA]
---

# Decision brief: what goes into the first piece of TIQACC we build

**For:** Shifan Cader, product owner. **With:** Rifaz Hajirin, qualified accountant, where an item
names the accountant; and Yogendran, security owner, for DEP-9 and the security points.

**Prepared:** 2026-10-28 by the orchestrator, for WF-01M61MRRKX52P8XHG3NZXSPCZH.

## The decision

DEC-0010 (Approved) lets TIQACC be built in increments while the release-1 scope (Q-029) is still
being settled. The first increment is a **foundation**: the ledger and platform parts that every later
module stands on. You are asked to approve **what that foundation contains and what it leaves out**,
and to confirm, one by one, the places where it departs from the plain text of the specification V2.2.

- **Bound to:** GOV-SCOPE-INCR-001 version 6, normative hash
  `sha256:488aba4b44dae53c2b8743aee1ec061a3803c01ebbb64f661ce867239eaa2e79`
  (`docs/requirements/increments/GOV-SCOPE-INCR-001.md`).
- **No approval request yet.** The foundation is Tier 1 (posting, numbering, periods, audit,
  authorisation, money). A Tier-1 approval must carry your own identity on GitHub (F2); an approval
  typed into the governance owner's session does not count for it. The request is raised when F2 is in
  place. Until then this brief is for reading, questions and answers.
- Approving the scope lets requirements be written for it. It does not approve any requirement, design
  or code.

## What the foundation contains (15 capabilities)

1. Tenants (one organisation each) and the register of their legal entities.
2. Users.
3. Roles and permissions, built by the entity's administrator.
4. Segregation of duties.
5. The audit log.
6. Capacity figures (users, entities, volumes) as settings, with a warning as a figure is approached.
7. Currencies, with exchange rates entered by hand.
8. The chart of accounts: accounts, groups, attributes and their statement lines.
9. Creating, amending and blocking accounts through an approval route.
10. Dimensions and the rules for which accounts need them.
11. Control accounts: the flag, the control types and the enforcement levels, held as settings.
12. Manual journals, approved by a second user, locked once posted, and corrected by reversal.
13. Gapless numbering, held as configuration.
14. Financial years and periods: open, soft closed, hard closed, audit locked.
15. Ledger enquiry.

## What it leaves out (29 exclusions), most importantly

- **Every module that depends on the release-1 decision:** receivables, invoicing, payables, bank,
  tax, fixed assets, payroll, inventory and the rest (EXC-16).
- **Year-end close** and the roll to retained earnings (EXC-13). The foundation opens one financial year
  per entity.
- **The adjustment journal, and correcting an entry in a closed period** (EXC-28). V2.2 uses
  "adjustment journal" for two different things (Q-055, checked on pp.37 and 38 of the PDF).
- **A delivered standard chart, and chart upload** (EXC-06): accounts are created one at a time.
- **Journals other than manual:** templates, recurring journals, accruals, intercompany and uploads
  (EXC-15).
- **Tax, opening balances and migration, licensing, attachments, group features**, and a firm's access
  to its clients' books (EXC-19 to EXC-21, EXC-23, EXC-26, EXC-01).

## What you are asked to decide (D-1 to D-7 in the scope)

| Item | You decide | With |
| --- | --- | --- |
| D-1 | Approve the scope. Each departure (DEP-1 to DEP-9) is confirmed or rejected on its own | Each departure's owners |
| D-2 | The open parts of tenant creation (Q-056) and of capacity limits (Q-057) stay out until answered; confirm the three working assumptions taken from the governance owner's answers | Security owner |
| D-3 | No year-end close; one financial year per entity. **Say whether the foundation is meant for live books:** if it is, posting stops at the first year end | Qualified accountant |
| D-4 | The governance panel waits; the events it would show go to the audit log | |
| D-5 | No delivered chart or chart upload | Qualified accountant |
| D-6 | The delivered table of default control levels is not built; levels are set for each entity | Qualified accountant |
| D-7 | Manual journals only; corrections by reversal until Q-055 is answered | Qualified accountant |

**The nine departures from V2.2** (each with its owners in the scope):

- DEP-1: no duplicate check when an account is added.
- DEP-2: no ranked alternatives when a code is refused.
- DEP-3: an entity starts with an empty chart.
- DEP-4: an approver cannot amend a pending entry.
- DEP-5: no year-end close.
- DEP-6: no delivered default control levels.
- DEP-7: a dimension's "Mandatory on" read as a default.
- DEP-8: no tax code on accounts or journal lines.
- DEP-9: a tenant-level administrator role supplied by the product, where V2.2 has the entity's
  administrator build every role.

## Recommendation

Approve the scope, and confirm the departures you agree with. It contains only what V2.2 states
plainly or makes a setting, and it was reviewed six times until no blocking issue remained. Before the
foundation's Gate A, two accounting points must be answered by Rifaz with you: which number series a
correcting reversal uses and at what rate (AP-10), and how it is dated once more than one period is
open (AP-13).

## What it means for the books

- A posted entry is never edited or deleted. In the foundation it is corrected only by a reversal.
- **An error found after its period has closed can be corrected only by reopening that period.** That
  needs management approval and a reason, and it changes the figures already reported for that period.
  An audit-locked period cannot be corrected at all. This lasts until Q-055 is answered.
- 13 accounting-policy points are named in the scope and none is decided. Rifaz owns them with you,
  with the tax specialist where tax is touched.

## Technical points

- The stack is React and .NET on Azure with Azure SQL Database (Q-054 v2). It is recorded in an
  architecture decision at the foundation's Gate B; the scope does not depend on it.
- Three security points are open with the security owner: sign-in and encryption, tenant isolation,
  and tamper evidence.

## Open questions

Eight questions hold parts out of the foundation until they are answered. Each part is a named
exclusion:

- Q-007: changing narrative or dimensions after posting.
- Q-013: posting into a hard-closed period by override.
- Q-014: the account naming standard.
- Q-031: a firm's access to client tenants.
- Q-034: changing an account's control flag once it has history.
- Q-055: the adjustment journal.
- Q-056: who creates tenants and their first administrator.
- Q-057: what happens at a capacity limit.

The other 49 open questions do not block the foundation.

Ten working assumptions taken from the governance owner's answers are labelled in the scope, each
pending its owner (WA-01 to WA-07 and WA-13 to WA-15: Q-001, Q-031, Q-032, Q-033, Q-038, Q-040, Q-054,
Q-056, and Q-057 twice). Five more are the requirements engineer's own readings (WA-08 to WA-12), each
labelled with its owner.

## Reviews

The requirements-assurance agent reviewed the scope six times:

| Review | Version | Verdict |
| --- | --- | --- |
| REV-01M61MRRKX52P8XHG3NZXSPCZJ | v1 | 3 blocking |
| REV-01M61PXHZBS8N3YVQX2XDJHHWH | v2 | 1 blocking |
| REV-01M61QHQX58WSCVFQMT2EPXSRD | v3 | Non-blocking |
| REV-01M61R5FTD3DD5RK7G0TH7G0NS | v4 | Non-blocking |
| REV-01M61SP5CTK2J8YYRVRR7C9DMX | v5 | Non-blocking |
| REV-01M61T1JTQRPGVY07V648NPMWA | v6 | Non-blocking: one cosmetic finding, a label to widen at the next revision |

Every blocking finding was resolved or raised as a question (Q-055 to Q-057).

What was checked on the rendered PDF:

- pp.8, 9, 37, 38, 40 to 42 and 133 to 136;
- every other cited page against the text extraction only.

These are agent reviews (E4). They do not replace your own reading.

## How to decide

Read the scope and send your questions or answers now. The approval request, with the phrase to
approve, comes when F2 (GitHub) is set up, so that your approval carries your own identity.

---
id: GOV-BRIEF-R1-SCOPE
type: governance
title: "Decision brief: release-1 scope and the payroll and fixed-asset route (Q-029)"
status: Proposed
version: 3
owner: orchestrator
links:
  related: [DEC-0008, Q-002, Q-003, Q-029, Q-032, Q-033, Q-034, Q-047, Q-038, Q-039, Q-022, Q-006, GOV-IMPACT-SRC007, GOV-QPACK-L1, REV-01M5EP1W4DYPM707EB79AYEYV1, REV-01M5W1AAYEP3761509T5F5D6NW, REV-01M5W2PMREVQFW5TCYYJQ1K1D6, REV-01M5W4F011JE50FZ3VMWD039DG]
---

# Decision brief: what goes into release 1

**For:** Shifan Cader, product owner. **With:** Rifaz Hajirin, qualified accountant.

**Prepared:** 2026-10-26 by the orchestrator. Version 3, after the review REV-01M5W4F011JE50FZ3VMWD039DG.

**Based on:**

- the specification V2.2 (SRC-007), now the baseline (DEC-0008);
- the impact analysis GOV-IMPACT-SRC007 v2;
- the release phasing v3, whose V2.2 update follows your answers;
- Q-029 v5.

## The decision

The specification says every module is to be built, but not in what order. The requirements agent
proposes five releases. Release 1 is the smallest set on which Finance can run one Sri Lanka entity's
books end to end, in LKR with other currencies.

One question decides the size of release 1: **until the payroll and fixed-asset modules exist, how do
salaries and depreciation reach the ledger?** (Q-029). V2.2 changed this question, so some accounting
questions come first.

## Step 1: control accounts, for Rifaz and you

V2.2 no longer blocks every manual journal to a control account. It sets a level per control type:

| Level | What happens |
| --- | --- |
| Not applied | A manual journal posts like any other |
| Advisory | A manual journal is allowed, with a reason, and listed on an exception report |
| Enforced | A manual journal is refused. "Only the owning sub-ledger posts to it" (p.27) |

How this applies to Tiqri is not yet clear:

- **Q-032, which rule governs.** The chart's attribute table in V2.2 still says manual journals to
  control accounts "are blocked" (p.24), next to the new levels (p.27).
- **Q-033, the starting level.** The specification's delivered defaults (p.27) are:

  | Organisation | Default |
  | --- | --- |
  | Single entity, general ledger only | Not applied |
  | Single entity running sub-ledgers | Advisory, with bank Enforced |
  | Group, or consolidated reporting | Enforced |
  | Multinational, multi-currency or high volume | Enforced, and lowering it is reported |

  Two things are open:
  - Is the default read for Tiqri as a whole, or for each entity? For Tiqri as a whole (several
    countries and currencies), it is probably **Enforced**. For the first entity on its own, it may be
    **Advisory**.
  - Going below Enforced "requires approval, a recorded reason and an effective date" and is reported
    to management on the governance panel (p.27). Does choosing a lower level when an entity is set up
    count as such a lowering?

  The governance panel is a CFO dashboard page that reports configuration changes (2.15.8); it is not
  yet planned for release 1.
- **Q-034, changing a flag later.** V2.2 says a control flag can be changed by approval (p.27), but also
  that it cannot change once the account has transactions (p.30).
- **Q-047, journals against the agreements.** The agreement between each sub-ledger and its control
  account "must be nil" (p.114). If manual journals reach a control account, which governs?

## Step 2: the route for payroll and depreciation (Q-029)

Whatever Step 1 decides, V2.2 still says:

- "No user journal is acceptable as a substitute" for what the system posts (p.8);
- depreciation "must be auto-calculated by the system" (p.90);
- each sub-ledger must agree to its control account, continuously, to nil (p.114).

| | What happens | Size of release 1 | Cost |
| --- | --- | --- | --- |
| **A** | Payroll and depreciation posted by manual journal until release 2 | Smallest | Depends on Step 1. Possible only at Advisory or below. Otherwise it needs a relaxed control or temporary accounts. Either way, the journals are not an accepted substitute, the agreements cannot run, and history before release 2 cannot be rebuilt from a sub-ledger. |
| **B** | Payroll and fixed assets built in release 1 | Largest; the reviewer estimated about double | No payroll or asset control issue. Needs the Sri Lanka payroll rules from the tax specialist. |
| **C** | Payroll fed from the payroll system Tiqri uses today, through the integration interface; fixed assets built in release 1 | Middle | V2.2 can be read two ways. **(1)** Where payroll is not active, the external system "takes its place and feeds TIQACC" (p.11), so it counts as the owning sub-ledger and C works at Enforced. **(2)** Only TIQACC's own payroll module owns the account, so C needs the payroll control type lowered. Rifaz decides which, with you. C also needs Q-022 answered to allow the feed, and Rifaz to confirm how the payroll agreement works without payroll runs. |

**Corporate income tax, under every option.** If corporate income tax waits for release 2, its charge
and instalments post to income tax payable, which is a tax control account (p.84, p.24). That is the
same control-account question as option A, under B and C as well. Either corporate income tax comes
into release 1, or its interim postings follow Step 1 (D-2.7.6, the tax specialist with Rifaz). The
same part of the specification (2.7.6) holds the turnover levy entry, which release 1 needs if the levy
applies (Q-042).

**Recommendation.** The independent review of V1 advised C, **on condition that Rifaz confirms interface
postings count as sub-ledger postings** (REV-01M5EP1W4DYPM707EB79AYEYV1). Under V2.2 that condition is
reading (1) above. If Rifaz confirms reading (1), the V1 reasons stand:

- C lowers no control;
- the specification gives depreciation no interim route;
- it keeps release 1 well below B.

If Rifaz chooses reading (2), C has a control cost like A. This is advice only.

## Proposed releases

| Release | Contents |
| --- | --- |
| **1. Sri Lanka core books** | Platform (users, roles, audit log, numbering, integrations), general ledger with the delivered chart, receivables, tax and non-tax invoicing with the Sri Lanka templates, payables, bank and cash, tax register and returns, supporting documents, reconciliation and close, standard reports, acceptance |
| 2. Complete Sri Lanka books | Payroll and fixed assets (as Step 2 decides), supplier invoice capture, the report builder, corporate income tax (unless it moves to release 1) |
| 3. Further countries and group | Group accounting and consolidation, intercompany, multi-language, the other countries' templates |
| 4. Management depth | CFO dashboard, assistants, treasury, cash-flow forecasting, mobile |
| 5. Other business types | Inventory and manufacturing, standalone modules, other integrations |

Releases 3 and 4 can be swapped.

## Also needed from you for release 1

1. **Capacity (Q-038).** V2.2 builds to a multinational group's scale (2,000 entities, 25 million
   journal lines a month) and proves it in load testing before acceptance, up to a tested ceiling of
   10,000 entities and 100 million lines (p.133). For release-1 acceptance, which applies: that
   ceiling, the multinational figures, or a single-entity scale?
2. **Licensing (Q-039).** V2.2 adds subscription licensing (2.16.5). Which release includes it?
3. **The governance panel (2.15.8).** It reports lowered control levels and changed bank details
   printed on invoices. Is it in release 1?
4. **Countries (Q-003).** Your answer was "all countries defined in the template". Does Norway stay in
   scope? It has no template. A tax specialist for the other countries is named by Yogi, as governance
   owner, in a change to the authority matrix.

The question pack (GOV-QPACK-L1 v3) holds these and every other open question, grouped by person.

## Reviews

- **This brief:** v2 was reviewed and blocked (REV-01M5W4F011JE50FZ3VMWD039DG). Its two blocking
  findings, option C and corporate income tax, are addressed in this version.
- **Impact analysis:** reviewed twice, with the first review blocking (REV-01M5W1AAYEP3761509T5F5D6NW,
  REV-01M5W2PMREVQFW5TCYYJQ1K1D6).
- **The V1 phasing:** reviewed twice (REV-01M5EP1W4DYPM707EB79AYEYV1,
  REV-01M5EQY9R7BC1SY2XDY6S9YA52).

All of these are agent reviews (E4), not approvals.

## How to answer

1. Reply with your answers to Q-032, Q-033, Q-034 and Q-047, with Rifaz.
2. Then reply with your choice for Q-029 (A, B or C) and, for C, Rifaz's reading.
3. Reply on corporate income tax, and on the four points above.

The orchestrator records each answer, re-bases the phasing on V2.2, and prepares the decision record
for your approval. Until GitHub approvals are set up, your approval is typed in Yogi's session and
attested by Yogi (E1-op), and is re-confirmed under your own account later.

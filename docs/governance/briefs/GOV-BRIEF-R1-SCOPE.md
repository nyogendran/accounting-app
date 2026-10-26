---
id: GOV-BRIEF-R1-SCOPE
type: governance
title: "Decision brief: release-1 scope and the payroll and fixed-asset route (Q-029)"
status: Proposed
version: 2
owner: orchestrator
links:
  related: [DEC-0008, Q-002, Q-003, Q-029, Q-032, Q-033, Q-034, Q-038, Q-039, Q-022, Q-006, GOV-IMPACT-SRC007, GOV-QPACK-L1, REV-01M5EP1W4DYPM707EB79AYEYV1, REV-01M5W1AAYEP3761509T5F5D6NW, REV-01M5W2PMREVQFW5TCYYJQ1K1D6]
---

# Decision brief: what goes into release 1

**For:** Shifan Cader, product owner. **With:** Rifaz Hajirin, qualified accountant.

**Prepared:** 2026-10-27 by the orchestrator. Version 2 replaces the withdrawn V1 brief.

**Based on:**

- the specification V2.2 (SRC-007), now the baseline (DEC-0008);
- the impact analysis GOV-IMPACT-SRC007 v2, reviewed twice;
- the release phasing v3, whose V2.2 update follows your answers;
- Q-029 v4.

## The decision

The specification says every module is to be built, but not in what order. The requirements agent
proposes five releases. Release 1 is the smallest set on which Finance can run one Sri Lanka entity's
books end to end, in LKR with other currencies.

One question decides the size of release 1: **until the payroll and fixed-asset modules exist, how do
salaries and depreciation reach the ledger?** (Q-029). V2.2 changed this question, so three short
accounting questions come first.

## Step 1: three questions for Rifaz and you

V2.2 no longer blocks every manual journal to a control account. It sets a level per control type:

| Level | What happens to a manual journal |
| --- | --- |
| Not applied | Posts like any other |
| Advisory | Allowed, with a reason, and listed on an exception report |
| Enforced | Refused |

How this applies to Tiqri is not yet clear:

- **Q-032, which rule governs.** The chart's attribute table in V2.2 still says manual journals to
  control accounts "are blocked" (p.24), next to the new levels (p.27). Which one governs?
- **Q-033, the starting level.** The delivered default depends on the kind of organisation:

  | Organisation | Default |
  | --- | --- |
  | Single entity running sub-ledgers | Advisory, with bank Enforced |
  | Group, or multi-currency | Enforced |

  Tiqri works in several countries and currencies, so the default is probably **Enforced**. Running
  lower needs an approved, reasoned lowering for each control type, reported to management on the
  governance panel (p.27). That panel is not yet planned for release 1. Is the starting level
  Enforced, and may a lower level be chosen at set-up?
- **Q-034, changing a flag later.** V2.2 says a control flag can be changed by approval (p.27), but
  also that it cannot change once the account has transactions (p.30). Which governs?

## Step 2: the route for payroll and depreciation (Q-029)

Whatever Step 1 decides, V2.2 still says:

- "No user journal is acceptable as a substitute" for what the system posts (p.8);
- depreciation "must be auto-calculated by the system" (p.90);
- each sub-ledger must agree to its control account, continuously, to nil (p.114).

| | What happens | Size of release 1 | Cost |
| --- | --- | --- | --- |
| **A** | Payroll and depreciation posted by manual journal until release 2 | Smallest | Possible at Advisory, if Step 1 allows it. Otherwise it needs a relaxed control or temporary accounts. Either way, the journals are not an accepted substitute, the agreements cannot run, and history before release 2 cannot be rebuilt from a sub-ledger. |
| **B** | Payroll and fixed assets built in release 1 | Largest; the reviewer estimated about double | No control issue. Needs the Sri Lanka payroll rules from the tax specialist. |
| **C** | Payroll fed from the payroll system Tiqri uses today, through the integration interface; fixed assets built in release 1 | Middle | Interface postings are not manual journals, so the levels do not affect them. Needs Q-022 answered to allow the feed, and Rifaz to confirm how the payroll agreement works without payroll runs. |

**Recommendation.** The independent review of V1 advised **C**, and V2.2 does not change its reasons:

- C lowers no control;
- the specification gives depreciation no interim route;
- it keeps release 1 well below B.

This is advice only. C needs Tiqri's current payroll system to be able to export its results.

## Proposed releases

| Release | Contents |
| --- | --- |
| **1. Sri Lanka core books** | Platform (users, roles, audit log, numbering, integrations), general ledger with the delivered chart, receivables, tax and non-tax invoicing with the Sri Lanka templates, payables, bank and cash, tax register and returns, supporting documents, reconciliation and close, standard reports, acceptance |
| 2. Complete Sri Lanka books | Payroll and fixed assets (as Step 2 decides), supplier invoice capture, the report builder, corporate income tax (the tax specialist decides) |
| 3. Further countries and group | Group accounting and consolidation, intercompany, multi-language, the other countries' templates |
| 4. Management depth | CFO dashboard, assistants, treasury, cash-flow forecasting, mobile |
| 5. Other business types | Inventory and manufacturing, standalone modules, other integrations |

Releases 3 and 4 can be swapped.

## Also needed from you for release 1

1. **Capacity (Q-038).** V2.2 builds to a multinational group's scale and proves it in load testing
   before acceptance (p.133). The multinational group is 2,000 entities and 25 million journal lines a
   month; the tested ceiling is 10,000 entities and 100 million lines. Is release 1 tested to that, or
   to a single-entity scale?
2. **Licensing (Q-039).** V2.2 adds subscription licensing (2.16.5). Which release includes it?
3. **The governance panel (phasing D-2.15.8).** Lowering a control level and changing the bank details
   printed on invoices are both reported on it. Is it in release 1?
4. **Countries (Q-003).** Your answer was "all countries defined in the template". Does Norway stay in
   scope? It has no template. Who is the tax specialist for the other countries?

The question pack (GOV-QPACK-L1 v2) holds these and every other open question, grouped by person.

## Reviews

- **Impact analysis:** reviewed twice by the assurance agent. The first review was blocking: it
  corrected the starting level, which had been read as Advisory. The re-review was non-blocking
  (REV-01M5W1AAYEP3761509T5F5D6NW, REV-01M5W2PMREVQFW5TCYYJQ1K1D6).
- **The V1 phasing:** reviewed twice (REV-01M5EP1W4DYPM707EB79AYEYV1, REV-01M5EQY9R7BC1SY2XDY6S9YA52).

All of these are agent reviews (E4), not approvals.

## How to answer

1. Reply with your answers to Q-032, Q-033 and Q-034, which Rifaz owns with you.
2. Then reply with your choice for Q-029 (A, B or C), and the four points above.

The orchestrator records each answer, re-bases the phasing on V2.2, and prepares the decision record
for your approval. Until GitHub approvals are set up, your approval is typed in Yogi's session and
attested by Yogi (E1-op), and is re-confirmed under your own account later.

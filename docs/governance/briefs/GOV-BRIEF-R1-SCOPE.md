---
id: GOV-BRIEF-R1-SCOPE
type: governance
title: "Decision brief: release-1 scope and the payroll and fixed-asset route (Q-029)"
status: Proposed
version: 1
owner: orchestrator
links:
  related: [Q-002, Q-029, Q-022, Q-006, BO-01, REV-01M5EP1W4DYPM707EB79AYEYV1, REV-01M5EQY9R7BC1SY2XDY6S9YA52]
---

# Decision brief: what goes into release 1

**For:** Shifan Cader, product owner. **With:** Rifaz Hajirin, qualified accountant. **Prepared:**
2026-10-26 by the orchestrator. **Based on:** the release phasing
(`docs/requirements/release-phasing.yaml` v3, commit 04341a2) and Q-029 v3.

## The decision

SRC-001 says every module is to be built (p.6), but not in what order. The requirements agent has
proposed five releases. Release 1 is the smallest set on which the finance team can run one
service-based Sri Lanka entity's books end to end, in LKR with other currencies.

One question has to be settled before release 1 can be fixed: **until the payroll and fixed-asset
modules exist, how do salaries and depreciation reach the ledger?**

## Proposed releases

| Release | Contents |
| --- | --- |
| **1. Sri Lanka core books** | Platform (users, roles, audit log, numbering, integrations), general ledger, receivables, tax and non-tax invoicing, payables, bank and cash with the posting rules, tax register and returns, supporting documents, balance sheet reconciliation and close, standard reports, non-functional requirements and acceptance |
| 2. Complete Sri Lanka books | Payroll and fixed assets (depending on the choice below), supplier invoice capture by email and scanning, the report builder, corporate income tax (the tax specialist decides) |
| 3. Second country and group | Group accounting and consolidation, intercompany, group tax view, multi-language |
| 4. Management depth | CFO dashboard, assistants, treasury, cash-flow forecasting, mobile |
| 5. Other business types | Inventory and manufacturing, standalone module deployment, other integrations |

Releases 3 and 4 can be swapped if you prefer.

## Why payroll and depreciation need a decision

SRC-001 leaves no easy interim route:

- "No user journal is acceptable as a substitute" for what the system posts itself (p.8).
- "Depreciation must be auto-calculated by the system, not by a spreadsheet" (p.77).
- Payroll and fixed-asset control accounts "accept sub-ledger postings only; manual journals to them
  are blocked" (p.23), and a control flag cannot be changed once an account has transactions
  (p.24). An account left unflagged now cannot be quietly fixed later.

## Options

| | What happens | Size of release 1 | Cost |
| --- | --- | --- | --- |
| **A** | Payroll and depreciation are posted by approved manual journal until release 2 | Smallest: 89 sections plus parts of 18 | Rifaz must choose **(i)** relax the control-account block until release 2, by a change request, or **(ii)** post to interim accounts that are not control accounts and move the balances at release 2. SRC-001 can be read two ways on how they move: through the sub-ledger (R1) or by one approved reclassification (R2). Until release 2 the system does not post payroll or depreciation itself, against p.4 and p.8 |
| **B** | Payroll and fixed assets are built in release 1 | Largest: 112 sections. The reviewer estimates this roughly doubles release 1 | No control is relaxed. Release 1 also needs the Sri Lanka payroll rules from the tax specialist |
| **C** | Payroll results come in from the payroll system Tiqri uses today, through the integration interface. Fixed assets are built in release 1 | Middle: 99 sections | No control is relaxed for fixed assets. Rifaz must confirm that interface postings count as sub-ledger postings, and how payroll payables are reconciled with no payroll run in TIQACC. Payroll returns stay in the current payroll system until release 2 |

## Recommendation

The requirements agent recommends no option. The independent assurance review
(REV-01M5EP1W4DYPM707EB79AYEYV1, advisory only) suggests **C**:

- it relaxes no control;
- SRC-001 gives depreciation no interim route;
- it keeps release 1 well below B.

C works only if:

- Tiqri has a payroll system today that can export its results;
- you answer Q-022 so that an external payroll may feed TIQACC (SRC-001 forbids a third-party payroll
  "synchronising by file transfer", p.90, but lets an external system feed TIQACC where the module is
  not active, p.11).

## Please also confirm

1. The first entity is service-based, with no stock (assumption A-01).
2. Release 1 needs no Sinhala or Tamil documents or screens (assumption A-02). The data model will
   hold other languages from the start.
3. The integrations live at go-live are the bank statement feed and the tax e-filing portal.

## Risks whichever option you choose

- Deferring group accounting is safe only if the chart of accounts is designed as a group chart and
  every entry carries its entity from release 1. Both are kept in release 1.
- Release 1 can't be specified in full until the tenant boundary (Q-031) is set, and until Rifaz and
  you answer the questions in the question pack (GOV-QPACK-L1).
- An entity that switches on payroll or fixed assets after go-live needs its opening data loaded.
  SRC-001 promises that adding a module needs no data migration (p.13). This load is smallest under B.

## Reviews

The phasing was reviewed twice by the requirements assurance agent:

- REV-01M5EP1W4DYPM707EB79AYEYV1 was blocking. It found the control-account conflict, and its findings
  are fixed in v2 and v3.
- REV-01M5EQY9R7BC1SY2XDY6S9YA52 is non-blocking.

Both are agent reviews (E4), not approvals.

## How to answer

Reply with the option (A, B or C), and with anything you want changed in the release table.

- Under A, add Rifaz's choice of (i) or (ii), and of R1 or R2.
- Under C, add Rifaz's confirmation of the two points above.

The orchestrator then records your choice as a decision (DEC, Proposed), updates the phasing and
prepares the approval request. Until GitHub approvals are set up, your approval is typed in Yogi's
session and attested by Yogi (E1-op), and is re-confirmed under your own GitHub account later.

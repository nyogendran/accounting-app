---
id: GOV-QPACK-L1
type: governance
title: "Question pack: open discovery questions for Shifan Cader and Rifaz Hajirin"
status: Proposed
version: 1
owner: orchestrator
links:
  related: [Q-001, Q-002, Q-003, Q-004, Q-005, Q-006, Q-007, Q-008, Q-009, Q-010, Q-011, Q-012, Q-013, Q-014, Q-015, Q-016, Q-017, Q-018, Q-019, Q-020, Q-021, Q-022, Q-023, Q-024, Q-025, Q-026, Q-027, Q-028, Q-029, Q-030, Q-031, GOV-BRIEF-R1-SCOPE]
---

# Question pack: open discovery questions

**For:**

- Shifan Cader, as product owner and tax specialist;
- Rifaz Hajirin, as qualified accountant.

**Prepared:** 2026-10-26 by the orchestrator, from question records Q-001 to Q-031 and the release
phasing (v3).

SRC-001 is the requirements specification. Page numbers refer to it. Where it contradicts itself or
leaves a value open, the agents may not choose; one of you decides. Each question gives:

- what SRC-001 says;
- the possible readings;
- where there is one, the independent reviewer's suggestion. It is advice only (E4).

**How to answer.** Reply with the question number and your answer, for example
"Q-008: as the reviewer suggests". "Not yet" and "need to discuss" are fine answers. Please send
totals and blank or redacted samples only: no real customer, employee or transaction data.

**Priority.**

- **[R1]** Needed before release 1 can be specified.
- **[Later]** Needed before a later release or before acceptance.

| Person | Questions |
| --- | --- |
| Shifan, product owner | 14, plus 9 scope points from the phasing |
| Shifan, tax specialist | 7, plus part of Q-003 |
| Rifaz, qualified accountant | 10, plus 2 scope points and the accounting part of Q-029 |
| Yogi, governance owner | 1 |

The release-1 scope and Q-029 are in a separate decision brief, GOV-BRIEF-R1-SCOPE. Please read it
first.

---

## Part 1. Shifan Cader, product owner

### Confirm what was said at kick-off

These record answers Yogi gave on 2026-10-20. Please confirm them or correct them.

- **Q-001 [R1].** TIQACC is Tiqri's own multi-tenant SaaS product, and Tiqri's finance team is its
  first customer. Consequences:
  - Annexure A's vendor-response format does not apply.
  - The internal team accepts each module (SRC-001 2.16.4).
- **Q-004 [R1].** SRC-001 is accepted as the signed baseline. Section 3 names the Finance Manager,
  Internal Audit and the Managing Director as signatories (p.121). Who are they for Tiqri, or does
  your confirmation stand in for their signatures?

  178 bracketed values in SRC-001 still need confirming, each by its owner. They are listed in a
  separate workbook, which will follow as its own pack.
- **Q-002.** Covered by the decision brief.

### Decisions

- **Q-031 [R1]. What is one tenant?** Is one TIQACC tenant one legal entity, one group of entities,
  or one customer organisation with several groups? SRC-001 uses "tenant" once and never defines it.
  Its group features work across entities that share "One platform · one data set · one chart of
  accounts" (p.13). If one entity were one tenant, a group would be split across tenants. This sets
  the data-isolation boundary, which is an early security and architecture decision. Yogi joins you
  on it, as tech lead and security owner.
- **Q-022 [R1]. May an external payroll system feed TIQACC by file?** SRC-001 says "A third-party
  payroll product synchronising by file transfer is not acceptable" (p.90), but also that where the
  payroll module is not active "the external system takes its place and feeds TIQACC" (p.11).
  - (A) The p.90 rule is about how TIQACC's own payroll module is built. Entities without it may
    feed payroll in by file or by API.
  - (B) No external payroll may feed TIQACC by file.
  - (C) API only.

  Reviewer suggests (A). This matters for option C in the decision brief.
- **Q-006 [R1]. Is data migrated?** Will TIQACC take over opening balances or history from a system
  in use today?
  - If so, from which system and entities, and how many years of history?
  - Does the first entity have balances at go-live, and how are they opened? Manual journals to
    control accounts are blocked (p.24).

  SRC-001 also has an acceptance test that searches for a two-year-old invoice (2.1.5). How should it
  run if no history is migrated?
- **Q-005 [R1]. Annexure B.** Please gather from Finance:
  - **Monthly volumes,** typical and peak, for:
    - entities, currencies and users;
    - customers, invoices and receipts;
    - suppliers, bills and payments;
    - bank lines, fixed assets, stock and payroll.
  - **Invoice formats:** a blank or redacted sample of each tax invoice and non-tax invoice layout in
    use, per country.

  The current chart of accounts is needed only if data is migrated. Rifaz creates the new chart in
  TIQACC.
- **Q-024 [R1]. Service levels.** What does TIQACC commit to its tenants?
  - support response and resolution times by severity;
  - availability;
  - recovery point and recovery time;
  - screen response times.

  SRC-001 refers to an SLA that does not exist yet (p.119). Yogi confirms what is feasible.
- **Q-023 [R1]. Clauses written for a vendor.** Some clauses ask "the vendor" to state something,
  for example the encryption standard (p.9) and where data and backups sit (p.10). Others rest on a
  contract: "at no extra charge", and the handover documentation (2.16.3). The obligations stand.
  For each "vendor states" part, should Tiqri give an internal answer, or drop it?
- **Q-026 [R1]. May the auditor see individual pay?** The auditor may "Read every module and export
  any report" (p.9). But "Payroll amounts are visible only to named payroll users and [role]"
  (p.98). Who is that [role], and is the auditor included?
- **Q-025 [Later]. Retention policy.** What retention policy does a new tenant start with? Should one
  rule (the longer of the tenant's policy and the law) cover all records? Six clauses say "[7] years"
  outright, while p.100 says retention is "not a fixed figure in the software". The legal periods are
  Q-020, below.
- **Q-027 [Later]. Two wrong cross-references.** Please confirm the reviewer's reading. This is
  editorial only.
  - "under 2.10" on p.24 should read 2.12 (reconciliation owners).
  - Budgets cited to 2.2.3 are in 2.2.10 and 2.14.11.

### Scope points from the release phasing

- **Employee expenses [R1].** Release 1 has no payroll, so there is no employee record for expense
  claims. Choose one:
  - keep a minimal employee record in release 1, which raises three questions:
    - is the claim approver taken from the reporting line in that record?
    - is a claim keyed by the employee as a user, or by Finance on the employee's behalf? This affects
      licences and segregation of duties.
    - are the other mandatory employee fields checked only once payroll starts?
  - or defer expense claims, and say how employee expenses are handled meanwhile.
- **Billing types [R1].** Which of milestone, progress, subscription and project billing does Tiqri
  use? (2.3.3)
- **Governance panel [R1].** Is the governance panel of the CFO dashboard in release 1? Without it,
  some measures of objective BO-05 cannot be shown in release 1. (2.15.8)
- **Module activation test [R1].** May the module-activation acceptance test be accepted in parts: in
  release 1, in release 2 and in full in release 5? Its line "activating a second module later …
  requires no migration" (p.17) meets the opening-data load needed when payroll or fixed assets start.
- **Handover and vendor statement [Later].** How do the documentation and handover deliverables
  (2.16.3), and the vendor statement in 2.1.7, apply to Tiqri's own product? (Q-023)
- **The three items in the decision brief** under "Please also confirm":
  - service-based entity;
  - no Sinhala or Tamil in release 1;
  - the go-live integrations.

---

## Part 2. Shifan Cader, tax specialist (Sri Lanka and Norway)

- **Q-003, tax part [R1].** Which statutory reports and tax returns apply in Sri Lanka and in
  Norway?
- **Q-021 [Later; per country before its tax acceptance].** Which return forms, e-filing file
  formats and legally prescribed invoice wording apply in each country? The build needs only the
  configurable mechanism; the content for each country is needed before that country's tax testing.
- **Q-019 [R1]. Is a customer registered for tax?** SRC-001 has a mandatory registration-status field
  that drives the document type, and also says "the presence of a number is what marks the customer
  registered" (p.36). Which governs when the two disagree?
- **Q-018 [R1]. Unregistered customers.** "An unregistered customer cannot be issued a document
  carrying a tax registration reference" (p.48). Which reference does this forbid?
  - (A) The customer's own registration number only.
  - (B) Any registration number, where printing it is not permitted.
- **Q-017 [R1]. Cancelling an issued invoice.** SRC-001 allows cancellation "only before payment and
  before the tax return for that period is filed" (p.48), but elsewhere sends every correction of an
  issued invoice to a credit or debit note. May a tax invoice be cancelled in each country? Rifaz then
  decides the reversing entry.
- **Q-016 [R1]. Credit and debit notes without an original invoice.** SRC-001 allows them "standalone"
  (p.38), but also says every note "references the original document number and inherits its tax
  treatment" (p.48). Are they allowed in each country, and with what tax treatment and limit?
- **Q-015 [R1]. Invoice numbering.** Is the annual restart of the sales tax invoice series fixed for
  every country, or a default set per country? Reviewer suggests: a default, set per country.
- **Q-020 [Later]. Legal retention periods.** What are the legal retention periods in Sri Lanka and
  in Norway for each record type? SRC-001 says "[7] years" for each of these:
  - the audit log;
  - transaction history;
  - fixed assets;
  - payroll;
  - reconciliations;
  - group records.
- **Corporate income tax [R1 scope].** Must corporate income tax be computed in TIQACC for the first
  entity's first filing, or can it wait for release 2? If it waits, the tax charge and instalments
  need the same interim route as payroll (decision brief).
- **Payroll returns, interim [R1, under options A and C].** Until payroll is in TIQACC, may the
  employment income tax and fund contribution returns be prepared outside it, with their schedules
  uploaded (SRC-001 allows this, 2.7.7)?

---

## Part 3. Rifaz Hajirin, qualified accountant

- **Q-029, accounting part [R1].** Your input to the decision brief: under option A, choose (i) or
  (ii), and R1 or R2. Under option C, confirm that interface postings count as sub-ledger postings,
  and say how payroll payables are reconciled.
- **Q-003 [R1].** Please state:
  - the accounting framework for each country and for the group;
  - the financial year end of each entity;
  - the group reporting currency.
- **Q-014 [R1]. Chart-of-accounts naming standard.** SRC-001 requires account names to follow "the
  naming standard in 2.2.2", but 2.2.2 contains none. What is the standard? You will create the chart
  in TIQACC, so this is your rule.
- **Q-007 [R1]. Changing dimensions after posting.** A posted entry's "dimensions" cannot be changed
  by anyone (p.29), yet dimension changes "that alter no value and no account may be permitted after
  approval" (p.29). Choose one:
  - (A) correct by reversal and re-entry only;
  - (B) allow editing in place;
  - (C) the system posts a linked reclassification between dimension values on the same account, so
    the original stays locked. Reviewer suggests (C).

  Also: may (C) be used in closed or filed periods?
- **Q-008 [R1]. Suspense at hard close.** One clause says suspense "must be nil" before close (p.60).
  Another says nil, "or every remaining item explained and approved" (p.64). Reviewer suggests the
  second, because 2.6.11 is where suspense is specified.
- **Q-009 [R1]. Separation on reconciliations.** Preparer, reviewer and approver: two steps or three?
  May a small team release the separation, as p.9 allows ("including preparing and reviewing the same
  reconciliation")? Reviewer suggests: one second step, where review is the approval, releasable for
  every reconciliation including bank. The same question applies to the three-user tax return
  workflow.
- **Q-012 [R1]. Hard close with an unapproved bank reconciliation.** p.62 blocks it with no exception.
  p.101 allows an exception "formally accepted by [role] with a reason recorded" for every
  reconciliation, bank included. Which applies to bank, and who is the [role]?
- **Q-013 [R1]. The override into a closed period.** An authorised finance administrator may post
  "an exceptional journal into a hard-closed period through an override route" (p.33). Corrections are
  otherwise dated in the open period. What may the override be used for? May it correct an entry of
  that closed period?
- **Q-030 [R1]. Expected credit loss.** The provision is "computed on a provision matrix maintained
  by" Finance (p.41). On what basis, and with what loss rates?
- **Revenue recognition [R1 scope].** Which revenue recognition bases do Tiqri's contracts need?
  (2.3.4)
- **Leases [R1 under options B and C].** Does the first entity have leases that create right-of-use
  assets, and on what basis are they accounted for? (2.8.8)
- **Q-010 [R1 under options B and C]. Depreciation day count.** The worked example starts
  depreciation "pro-rata by days" from 1 October, yet charges 60,000 in year 1: exactly 3/12 of
  240,000. By actual days, 92/365, it would be 60,493.15 (p.78). Which day count and leap-year rule
  apply? Should the rule or the figures be corrected before the example becomes a test?
- **Q-011 [R1 under options B and C]. Correcting a depreciation run.** p.29 says "the run itself is
  not re-run". p.79 says a posted run "can be reversed and recalculated only within an open period".
  Reviewer suggests: reversal and recalculation within an open period, with p.29 applying to closed
  periods.

---

## Part 4. Yogi, governance owner

- **Q-028 [Later]. Data residency.** Which role owns the statutory data-residency rules for each
  country? Norway brings EEA data protection rules. The authority matrix has no clear owner; the
  nearest is the tax specialist. This needs a change to the authority matrix, which now needs two
  approvers.

---

## After you answer

The orchestrator does three things:

1. It records each answer in its question record. Answers that set policy become decisions (DEC,
   Proposed) for your approval.
2. It routes accounting answers to the accounting domain agent, to turn into rules and worked
   examples for Rifaz to approve.
3. It updates the release phasing.

No answer is treated as decided until it is recorded and approved.

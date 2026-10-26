---
id: GOV-QPACK-L1
type: governance
title: "Question pack: open questions for Shifan Cader, Rifaz Hajirin and Yogendran"
status: Proposed
version: 2
owner: orchestrator
links:
  related: [DEC-0008, GOV-BRIEF-R1-SCOPE, GOV-IMPACT-SRC007, Q-001, Q-002, Q-003, Q-004, Q-005, Q-006, Q-007, Q-008, Q-009, Q-010, Q-011, Q-012, Q-013, Q-014, Q-015, Q-016, Q-017, Q-018, Q-019, Q-020, Q-021, Q-022, Q-023, Q-024, Q-025, Q-026, Q-027, Q-028, Q-029, Q-030, Q-031, Q-032, Q-033, Q-034, Q-035, Q-036, Q-037, Q-038, Q-039, Q-040, Q-041, Q-042, Q-043, Q-044, Q-045, Q-046, Q-047, Q-048, Q-049, Q-050, Q-051, Q-052, Q-053]
---

# Question pack: open questions

**For:**

- Shifan Cader, as product owner and tax specialist;
- Rifaz Hajirin, as qualified accountant;
- Yogendran, as governance owner and tech lead.

**Prepared:** 2026-10-27 by the orchestrator. Version 2 is written against the specification V2.2
(SRC-007, the baseline under DEC-0008) and replaces the withdrawn V1 pack. Page numbers are V2.2 pages.
"The pack" means SRC-008, Rifaz's business information pack v1.1.

**How to read it.**

- Where the specification contradicts itself or leaves a value open, the agents may not choose; one of
  you decides.
- Each question gives what V2.2 says and any reviewer suggestion, which is advice only.
- **[R1]** marks a question needed before release 1 can be specified; **[Later]**, one needed before a
  later release or before acceptance.
- **New** marks a question raised by V2.2. **Changed** marks a V1 question that V2.2 changed.

**How to answer.** Reply with the question number and your answer, for example "Q-008: as the reviewer
suggests". "Not yet" and "need to discuss" are fine answers. Send totals and blank or redacted samples
only: no real customer, employee or transaction data.

**Read the decision brief GOV-BRIEF-R1-SCOPE first.** Its three questions on control accounts (Q-032,
Q-033, Q-034) and Q-029 matter most.

---

## Part 1. Shifan Cader, product owner

### Control accounts and release 1 (see the brief)

- **Q-032 [R1, new]. Which control-account rule governs?** The attribute table still says manual journals
  to control accounts "are blocked" (p.24), but the posting rule blocks them only "where control
  enforcement is set to Enforced" (p.27). With Rifaz.
- **Q-034 [R1, new]. Can a control flag be set later?** "Changing the flag or the type on an account is a
  change to the chart and passes the approval in 2.2.2 like any other" (p.27), but "control-account status
  cannot be changed once transactions exist" (p.30). With Rifaz.
- **Q-047 [R1, new]. Manual journals below Enforced.** Sub-ledger agreements "must be nil" (p.114), and
  "no balance in it exists without a document behind it" (receivables, p.45). If journals reach control
  accounts at Advisory, which governs? You decide scope; Rifaz the accounting effect.
- **Q-029 [R1, changed].** Payroll and depreciation before their modules exist: options A, B and C, in
  the brief.

### Confirm what was said at kick-off

- **Q-001 [R1].** TIQACC is Tiqri's own multi-tenant SaaS product, and Finance is its first customer.
  V2.2 is still written to a vendor ("Every clause is answered in Annexure A", p.5), and now adds
  subscription licensing (2.16.5).
- **Q-004 [closed].** DEC-0008 made V2.2 the baseline. Still open: the V2.2 sign-off in section 3
  (Finance Manager, Internal Audit, Managing Director) is unsigned. Who signs for Tiqri, or does your
  approval stand in for it? A separate workbook of 190 bracketed values will follow as its own pack.
- **Q-002.** Covered by the brief.

### Scope decisions

- **Q-038 [R1, new]. Capacity for release 1.** "The system is built against the figures below and proved
  against the ceiling in load testing before acceptance" (p.133). The multinational group is 2,000
  entities and 25 million journal lines a month; the ceiling is 10,000 entities and 100 million lines.
  Which scale does release 1 test to? The single-entity customer figure is 5,000 in V2.2 and 25,000 in
  the pack: which is right? With Yogi as tech lead.
- **Q-039 [R1, new]. Licensing.** "Access is sold by subscription" (p.135). In which release, and with
  which prices and terms? Section 3 now asks the vendor (Tiqri) for them.
- **Q-031 [R1]. What is one tenant?** One legal entity, one group, or one customer organisation with
  several groups? V2.2 sets limits "per tenant and per entity" and sells user packs across "every entity
  in the group", which leans towards a tenant holding one group, but does not decide it. With Yogi as
  tech lead and security owner.
- **Q-052 [R1, new]. One group chart, or an entity's own chart?** "A single group chart of accounts
  applies across all [No.] entities" (p.27). But "An entity managing its own financial data independently
  is checked within itself" (p.29). With Rifaz.
- **Q-022 [R1]. May an external payroll feed TIQACC by file?** "A third-party payroll product
  synchronising by file transfer is not acceptable" (p.103), yet where payroll is not active "the external
  system takes its place and feeds TIQACC" (p.11). The reviewer suggests: the first rule constrains
  TIQACC's own payroll module only. Option C in the brief depends on this.
- **Q-006 [R1]. Is data migrated?** From which system, how much history, and how are go-live balances
  opened? Bank is Enforced in every default, so an opening bank balance cannot be keyed as a journal
  (Q-045 for Rifaz).
- **Q-005 [R1, partly answered].** The pack supplies a delivered chart, capacity targets and 14 delivered
  templates. Annexure B still asks for Finance's current monthly volumes and the existing invoice
  formats (p.137): are they still needed?
- **Q-024 [R1]. Service levels.** Support response by severity, availability, recovery point and time.
  V2.2 still refers to an SLA that does not exist ("Severity-based response and resolution times stated
  in the SLA", p.132). With Yogi.
- **Q-023 [R1]. Clauses written for a vendor.** For example the encryption standard "stated in the vendor
  response" (p.9) and "the vendor states where data and backups physically sit" (p.10). 2.16.5 and
  section 3 add more. For each, an internal answer, or drop it?
- **Q-026 [R1]. May the auditor see individual pay?** The auditor may "Read every module and export any
  report" (p.9), but "Payroll amounts are visible only to named payroll users and [role]" (p.111).
- **Q-043 [R1, new].** Is approval to add or amend an account ever optional? V2.2 says "There is no
  second route by which an account can appear" (p.26); the pack makes approval optional for a ledger-only
  entity. With Rifaz.
- **Q-049 [R1, new].** Is "Design B" (the entity inside the account code), offered in the pack, closed?
  V2.2 puts the entity and country "around that code — never digits inside it" (p.25).
- **Q-025 [Later, partly answered].** V2.2 now keeps data from go-live ("Data is held from the day the
  organisation starts on the system", p.113), with the statutory period as a floor. But six clauses
  still say "[7] years". Should they follow the same model?
- **Q-036 [Later, new].** Two rows in V2.2 are corrupted and need Finance's correction: "Customers
  25,000" (p.19) and "Legal entities 1 Numbering series" (p.130).
- **Q-037 [Later, new].** The 2.2.2 acceptance statement (p.31) mostly tests journal upload and chart
  set-up. Which module does each of its tests accept?
- **Q-048 [Later, new].** The pack says it was "Prepared against the requirement specification, version
  1.1". Which version was that? With Rifaz.
- **Q-027 [Later].** Wrong cross-references, editorial only. "under 2.10" (p.30) should read 2.12, and
  V2.2 adds three more. Please confirm the reviewer's readings.

### Scope points from the release phasing [R1]

- **Countries (Q-003).** "All countries defined in the template": does Norway stay in scope? It has no
  template.
- **The governance panel (2.15.8).** Is it in release 1? Lowering a control level, changing an entity
  bank account and changing printed remittance details are all reported on it.
- **Employee expenses.** Without payroll in release 1 there is no employee record. Keep a minimal one,
  or defer expense claims?
- **Billing types.** Which of milestone, progress, subscription and project billing does Tiqri use?
- **The module activation test.** May it be accepted in parts, release by release?
- **Handover and vendor statements.** How do they apply to Tiqri's own product?
- **Confirm:** the first entity is service-based, with no stock; release 1 needs no Sinhala or Tamil;
  the go-live integrations are the bank statement feed and the tax e-filing portal.

---

## Part 2. Shifan Cader, tax specialist

- **Q-003 [R1].** Which statutory reports and tax returns apply in Sri Lanka, and in the other countries
  in scope?
- **Q-042 [R1, new]. The industry levy set.** An entity's industry "activates the industry tax set for
  that sector in that country" (p.16). The pack shows SSCL at 2.5% applied before VAT at 18%. Which levies
  apply to the first entity, in what order and on what base?
- **Q-021 [R1, partly answered for Sri Lanka].** The pack maps the Sri Lanka tax invoice field by field
  to Gazette 2481/22, "Mandatory for every VAT registered person from 1 July 2026". Please confirm the
  gazette, the fields, the MM/DD/YYYY date format and the three total rows. Return forms and e-filing
  formats are still needed.
- **Q-035 [R1, new]. Numbering.** Sales series restart "at the beginning of each financial year" (p.54),
  but where an authority prescribes the sequence, the choice "is made once per entity" (p.22). The pack
  says the Sri Lanka serial continues month to month unless the entity elects to restart. Which applies?
  (Replaces V1's Q-015, which is changed in the same way.)
- **Q-046 [R1, new].** The reset rule offers "Never, annually at the financial year end, or at the start
  of each period" (p.22), but the Sri Lanka serial takes its year from the calendar year. Is a
  calendar-year reset needed? With Yogi.
- **Q-019 [R1]. Is a customer registered?** The status field, or "the presence of a number is what marks
  the customer registered" (p.45)? The pack requires the purchaser's TIN on a tax invoice.
- **Q-018 [R1, partly answered].** "An unregistered customer cannot be issued a document carrying a tax
  registration reference" (p.61). Does this mean the customer's own number only, or any number? The pack
  sends unregistered customers to the non-tax template.
- **Q-051 [R1, new].** Is the pack's non-tax template (SL-NTX-01) for an unregistered supplier, an
  unregistered purchaser, or both?
- **Q-017 [R1]. Cancelling an invoice.** "Cancellation is permitted only before payment and before the
  tax return for that period is filed" (p.60). May a tax invoice be cancelled in Sri Lanka?
- **Q-016 [R1, partly answered].** Credit and debit notes "Against a named invoice or standalone" (p.47)
  against every note that "references the original document number and inherits its tax treatment"
  (p.60). The debit note is now a tax and a non-tax form. The pack says a Sri Lanka tax note cannot be
  issued without a reference.
- **Q-020 [Later, changed].** Statutory retention periods are now "a floor" (p.113), not a deletion
  date. What are the periods per record type in each country?
- **Corporate income tax [R1 scope].** Must it be computed in TIQACC for the first filing, or wait for
  release 2?
- **Payroll returns, interim [R1, options A and C].** May they be prepared outside TIQACC, with their
  schedules uploaded?

---

## Part 3. Rifaz Hajirin, qualified accountant

- **Q-033 [R1, new]. The first entity's control level.** You own this, with Shifan. The defaults are set
  by organisation: a single entity running sub-ledgers starts at "Advisory, and Enforced for bank"; a
  group, or a multi-currency organisation, starts at Enforced, and "lowering it is reported" (p.27).
  Lowering "requires approval, a recorded reason and an effective date" and is reported on the governance
  panel (p.27). Which level does Tiqri start at, per control type? Is choosing a lower level at set-up a
  lowering?
- **Q-032, Q-034 and Q-047 [R1, new].** With Shifan; see Part 1.
- **Q-045 [R1, new]. Opening bank balances.** Bank is Enforced, so an opening balance cannot be keyed
  as a journal. For an uploaded chart, "Opening balances load against it under 2.16.2" (p.26). Does that
  route serve, or what does?
- **Q-053 [R1, new].** A code clash is "resolved by mapping or by renumbering" (p.29), but "No account is
  renumbered to make room" (p.25). Which applies when an entity joins the group chart?
- **Q-041 [R1, new].** The spare range is "reserved outside the five classes" (p.25), but the class
  "determines the natural balance and the statement the account appears in" (p.24). What does an account
  there take?
- **Q-044 [R1, new].** Location applies to all transactions (p.31), but the pack's chart blocks it on
  most balance-sheet accounts. Which?
- **Q-040 [R1, new].** The upload template fixes amounts at "[2] places" (p.35). What about currencies
  with no or three minor units? With Yogi.
- **Q-050 [R1, new].** Some of the pack's specimens are inconsistent. For example, the receipt and
  statement omit the levy: 969,960.00 against the invoice's 994,209.00. Please correct them before any
  becomes test data.
- **Q-003 [R1].** The accounting framework for each country and for the group, each entity's year end,
  and the group reporting currency.
- **Q-014 [R1].** V2.2 still requires names to follow "the naming standard in 2.2.2" (p.24), and 2.2.2
  still has none. What is it?
- **Q-007 [R1]. Dimensions after posting.** "No screen, import, API call or administrator action can
  change its value, account, date, dimensions or party" (p.38), yet dimension changes "that alter no value
  and no account may be permitted after approval" (p.38). The reviewer suggests a linked reclassification
  between dimension values, leaving the original locked.
- **Q-008 [R1].** "Suspense must be nil before a period can be closed" (p.73), against "nil, or every
  remaining item explained and approved" (p.77). The reviewer suggests the second.
- **Q-009 [R1].** Preparer, reviewer and approver of a reconciliation: two steps or three? May a small
  team release it, as p.9 allows, "including preparing and reviewing the same reconciliation"?
- **Q-012 [R1].** "A period cannot be hard-closed while a bank reconciliation for that period is
  unapproved" (p.75), against an exception "formally accepted by [role]" for every reconciliation
  (p.114). Which applies to bank, and who is the [role]?
- **Q-013 [R1].** What may the override route into a hard-closed period be used for (p.42)?
- **Q-030 [R1].** Expected credit loss "is computed on a provision matrix maintained by" Finance (p.50).
  On what basis, and at what loss rates?
- **Revenue recognition [R1 scope].** Which bases do Tiqri's contracts need?
- **Leases [R1 under options B and C].** Are there right-of-use assets, and on what basis?
- **Q-010 [R1 under B and C].** The depreciation example uses "start rule pro-rata by days" (p.91) but
  charges exactly 3/12 of the annual figure. Which day count applies?
- **Q-011 [R1 under B and C].** "the run itself is not re-run" (p.38), against "A posted run can be
  reversed and recalculated only within an open period" (p.92).

---

## Part 4. Yogendran, governance owner and tech lead

- **Q-003 [R1]. A tax specialist for the added countries.** DEC-0007 names Shifan for Sri Lanka and
  Norway only. Naming another is an authority-matrix change, which needs two approvers.
- **Q-028 [Later].** Who owns statutory data-residency rules per country? V2.2 adds erasure "required by
  a privacy law" (p.113), and no role in the matrix owns privacy law. Both settle in the next
  authority-matrix change.
- **As tech lead:** Q-038 (capacity), Q-031 (tenant boundary), Q-040 and Q-046 (with their owners), and
  feasibility for Q-024.

---

## After you answer

The orchestrator records each answer in its question record. Answers that set policy become decisions
(DEC, Proposed) for approval. Accounting answers go to the accounting domain agent, which turns them into
rules and worked examples for Rifaz to approve. The release phasing is then re-based on V2.2. No answer
is treated as decided until it is recorded and approved.

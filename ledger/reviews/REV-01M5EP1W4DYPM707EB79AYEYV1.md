---
id: REV-01M5EP1W4DYPM707EB79AYEYV1
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - commit: f3b3b4c435d8016d02f2edb6cc79689a1828a28a
verdict: blocking-findings
findings:
  - severity: blocking
    text: >-
      [Phasing, D-INT-1 premise] The release 1/2 boundary rests on a route that a release-1 requirement
      blocks. The rationale says payroll and fixed assets "are large modules whose postings can reach the
      ledger meanwhile by approved journal with the working attached (S1-2.11.5-c01)", and D-INT-1, R-01
      and Q-029 name only S1-2-c02 and S1-2.8.3-c01 as the conflict. But 2.2.1 is release 1 in full, and
      it says "Receivables, payables, inventory, payroll, fixed asset, tax and bank control accounts
      accept sub-ledger postings only; manual journals to them are blocked" (S1-2.2.1-c06, p.23) and
      "Posting is blocked to: ... control accounts by manual journal" (S1-2.2.1-c21, p.24). An interim
      payroll journal credits net pay, withholding and fund payables, which 2.12.1 treats as control
      accounts (S1-2.12.1-c06, p.101). An interim depreciation journal credits accumulated depreciation,
      a fixed asset control account. The obvious workaround (leave those accounts unflagged in release 1)
      cannot be undone later: "Control account flag ... Once set, cannot be changed while the account
      carries a balance" (S1-2.2.2-c12, p.24); "Class, group and control-account status cannot be changed
      once transactions exist. A misclassified account is corrected by opening the correct account and
      reclassifying the balance by journal" (S1-2.2.2-c16, pp.24-25). So D-INT-1 option (A) has one of
      two consequences, and neither is stated: (i) release 1 relaxes a release-1 control, or (ii) release
      1 uses interim non-control accounts, and at release 2 new control accounts are opened and the
      balances reclassified. The glossary quotes c06 itself (term "Control account"), so the gap is in the
      phasing's reasoning, not in what the steward read. Why blocking: the product owner would decide the
      release-1 scope on a premise SRC-001 contradicts. Fix: add the control-account consequence to
      D-INT-1, R-01 and Q-029, with the qualified accountant named for (i) or (ii). Deciding roles:
      product-owner, with qualified-accountant.
    citation: >-
      docs/requirements/release-phasing.yaml@f3b3b4c (release_1_rationale; decisions_needed D-INT-1;
      risks R-01); "manual journals to them are blocked" (SRC-001 p.23, §2.2.1, S1-2.2.1-c06); "control
      accounts by manual journal" (p.24, S1-2.2.1-c21); "Once set, cannot be changed while the account
      carries a balance" (p.24, S1-2.2.2-c12); "cannot be changed once transactions exist" (pp.24-25,
      S1-2.2.2-c16); docs/requirements/glossary.yaml@f3b3b4c (term "Control account")
  - severity: non-blocking
    text: >-
      [Phasing, D-INT-1 scope] D-INT-1 asks only about posting payroll and depreciation, but three other
      deferrals rely on the same interim route and are not listed. (a) The employment income tax and
      statutory fund returns (S1-2.7.5-c04, c05) are deferred to release 2. In release 1 they are prepared
      outside the system, against "produce each return from the ledger ... without a spreadsheet standing
      between the two" (S1-2.7-c01, p.68). Under "No obligation in any jurisdiction is tracked outside the
      system" (S1-2.7.7-c01, p.72) they must still be on the release-1 dashboard. SRC-001 allows this, with
      the schedule "Produced by the system from the ledger, or uploaded where prepared outside it"
      (S1-2.7.7-c20, p.73), but the phasing does not say so. SRC-001's own illustrative dashboard rows are
      "EPF — employee and employer", "ETF" and "Payroll income tax" (p.72). (b) For 2.7.6 the
      recommendation is "instalments meanwhile by approved journal". The instalment is an entry-table row
      ("Instalment or payment on account Dr Income tax payable · Cr Bank", S1-2.7.6-c08, p.71), and
      income tax payable is a tax control account (S1-2.2.1-c06). The release-1 row S1-2.7.6-c12
      ("Remittance of any tax to the authority") may already cover the payment. (c) If the first entity
      has leases (D-2.8.8), the right-of-use asset and the lease liability have the same release-1 gap.
      Recommend widening D-INT-1 to all of these. The tax-specialist confirms that the payroll returns and
      CIT instalments may be prepared outside the system for the interim.
    citation: >-
      docs/requirements/release-phasing.yaml@f3b3b4c (2.7.5 split; 2.7.6 needs-decision recommendation;
      2.8.8); SRC-001 pp.68, 71, 72 and 73 as quoted
  - severity: non-blocking
    text: >-
      [Q-029 readings, assurance view] Q-029 sets "No user journal is acceptable as a substitute" (S1-2-c02,
      p.8) against interim journals, and offers (A) an exception, (B) no exception, and (C) an external
      payroll feed. SRC-001 evidence pulls both ways. For journals: "adjustments can also be made by manual
      journal posting where required, under approval and with the supporting working attached"
      (S1-0-c02, p.4); "Any calculation behind a posted figure — accruals, provisions, allocations,
      depreciation, expected credit loss, gratuity — is attached to the journal that posts it"
      (S1-2.11.5-c01, p.100). Against: "Payroll processing" is listed under "What the system posts,
      without a manual journal" (S1-0-c10, p.4); depreciation is "never maintained in a spreadsheet
      alongside it" (S1-2.8-c01, p.75); and the control-account block (first finding). SRC-001 also has
      its own route for a module that is not active: "A module switched off is absent ... none of its
      postings arise" (S1-2.1.7-c09, p.13), and "where it is not activated, the external system takes its
      place and feeds TIQACC through this interface" (S1-2.1.6-c14, p.11). That supports (C) for payroll,
      subject to Q-022. It offers no comparable route for depreciation. Consequences: (A) has the
      control-account cost; (B) roughly doubles release 1; (C) needs a payroll system in use today, which
      is unknown (Q-006), and needs the qualified accountant to confirm that interface postings into
      payroll control accounts count as sub-ledger postings. Recommendation for the decision owner: decide
      Q-029 only after it is amended as in the first finding. Then consider (C) for payroll if a current
      payroll system exists, and the fixed-asset core (2.8.1 to 2.8.5, 2.8.13) in release 1, because
      SRC-001 gives depreciation no interim route. Deciding role: product-owner, with
      qualified-accountant and tax-specialist.
    citation: >-
      Q-029@v1; Q-022@v1; Q-006@v1; SRC-001 pp.4, 8, 11, 13, 75 and 100 as quoted
  - severity: non-blocking
    text: >-
      [Phasing, dependency] Release-1 invoicing depends on part of the item master, which is marked release
      5. The tax determination matrix (2.4.2, release 1) works from three attributes, and the first is
      "Item tax class" (S1-2.4.2-c01, c04, pp.45-46). That attribute is held on the item master: "Tax class
      Yes Standard, zero, exempt; drives 2.4" (S1-2.9.1-c20, p.84). Service items are item-master records
      "used on sales and purchase documents alike" (S1-2.9.1-c03, p.84), and SRC-001 keeps them for a
      service entity whose inventory module is off (S1-2.1.7-c70, p.16). The phasing notes this under
      2.9.1 but leaves it as something the tech lead "may deliver". That is a scope mark, not a technical
      choice. Recommend splitting 2.9.1: service and non-inventory item types, code and description,
      category, base unit, tax class, bulk maintenance and blocking (S1-2.9.1-c02, c03, c10, c13, c14,
      c20, c24 to c26) go to release 1, and the rest stays in release 5. Deciding role: product-owner.
    citation: >-
      docs/requirements/release-phasing.yaml@f3b3b4c (2.9.1 reason); SRC-001 pp.16, 45, 46 and 84 as quoted
  - severity: non-blocking
    text: >-
      [Phasing, dependency] Expense claims in release-1 payables need the employee master, which is
      release 2. "Expense claim Raised by an employee with receipts attached, approved by the manager,
      settled through payroll or by payment" (S1-2.5.2-c07, p.49) posts "Cr Employee payable" (2.5.13,
      p.55). That needs an employee record and a manager, both from 2.10.1. The module-dependent-clauses
      rule does not cover this, because expense claims arise whether payroll is active or not. Recommend
      either a minimal employee record in release 1 (split 2.10.1), or expense claims deferred to release 2
      with the interim route stated. Deciding role: product-owner.
    citation: >-
      SRC-001 p.49, §2.5.2, S1-2.5.2-c07 and p.55, §2.5.13 as quoted; release-phasing.yaml@f3b3b4c (2.5.2,
      2.10.1)
  - severity: non-blocking
    text: >-
      [Phasing, 2.16.2] The recommendation "otherwise opening balances by approved journal and this
      sub-section later" fails in release 1 for the same reason as the first finding. Opening receivables,
      payables, bank and tax balances by journal are manual journals to control accounts (S1-2.2.1-c06).
      Receivables also requires that "no balance in it exists without a document behind it" (S1-2.3-c01,
      p.36), and SRC-001's migration scope loads "open receivables and payables by invoice"
      (S1-2.16.2-c01, p.120). Separately, the phasing creates its own migration need at release 2, whatever
      Q-006 decides. Activating payroll and fixed assets for an entity that has run on release 1 needs
      2.16.2-c01's "fixed asset register with accumulated depreciation" and "employee master with
      year-to-date payroll figures", against the activation promise of "without data migration"
      (S1-2.1.7-c08, p.13). Recommend that 2.16.2 open items and the opening trial balance be release 1 for
      any entity with history, and that a release-2 loading task be recorded. Deciding roles:
      product-owner; qualified-accountant for the opening-balance method.
    citation: >-
      docs/requirements/release-phasing.yaml@f3b3b4c (2.16.2); SRC-001 pp.13, 23, 36 and 120 as quoted
  - severity: non-blocking
    text: >-
      [Phasing, 2.1.8 split and R-02] R-02 names only "Terminology is held as data" (S1-2.1.8-c22) as the
      design constraint for deferring languages, yet c22 itself is marked release 3, and the release-1 rows
      c27 and c28 (tax and statutory terminology "in the words the local framework uses") rely on it. Other
      deferred clauses are also day-one data-model constraints, not features: "Scripts beyond the Latin
      alphabet are supported in full ... in entry, storage, search, sorting, printing and export"
      (S1-2.1.8-c20, p.18), and "A record is created once. Adding a language adds a description to the
      existing record; it never creates a second record" (2.1.8, p.19). A Sri Lanka tenant may hold
      customer or supplier names in a non-Latin script from release 1. Sinhala and Tamil are not in
      SRC-001's minimum language list (S1-2.1.8-c52 to c56, p.20), which A-02 should note. Recommend
      moving c20 (storage, search and sorting), c22 and the master-data description model into release 1
      as constraints. Deciding roles: tech-lead (design) with product-owner.
    citation: >-
      docs/requirements/release-phasing.yaml@f3b3b4c (2.1.8 split; R-02; A-02); SRC-001 pp.18-20 as quoted
  - severity: non-blocking
    text: >-
      [Phasing, acceptance timing] Four acceptance tests are marked against their dependencies. (a)
      S1-2.5.18-c01, "An invoice for more than was received is blocked ... the exception names the quantity
      difference" (p.57), is release 1, but the quantity check applies "only where a goods receipt exists"
      and is "Not applied where the inventory module is not active" (S1-2.5.6-c07, p.52). For a service
      entity (A-01) it belongs with inventory. (b) S1-2.1.7-c84 is deferred whole to release 5, yet its
      parts "an entity configured for services alone completes quotation to receipt with no inventory
      screen, report or posting" and "a user licensed for some modules cannot reach the others through any
      screen, report, search or API call" (p.17) test S1-2.1.7-c07 and c09. Those are release-1 clauses,
      and the module-dependent-clauses rule depends on them. Recommend partial acceptance of c84 in release
      1 (the product owner decides). (c) S1-2.1.5-c17, "a user finds a two-year-old supplier invoice from
      the invoice number printed on the scan alone" (p.11), with S1-2.1.5-c08 and S1-2.11.4-c02 ("the text
      inside the document", "Full-text search across attachments"), needs text recognition on scans in
      release 1, while optical capture (S1-2.11.2-c04) is deferred to release 2 "with supplier invoice
      capture". The saving is smaller than it appears, and the "two-year-old" test cannot run at go-live
      without migrated history (Q-006). (d) S1-2.7.2-c02 (release 1) has the industry selection propose
      the tax types, which S1-2.1.7-c57 (release 5) also specifies.
    citation: >-
      SRC-001 pp.11, 16, 17, 52, 57, 69 and 99 as quoted; release-phasing.yaml@f3b3b4c (2.1.5, 2.1.7,
      2.5.18, 2.7.2, 2.11.2)
  - severity: non-blocking
    text: >-
      [Phasing, accuracy] Three statements need correcting. (a) S1-2.1.7-c25 ("part of the platform, not of
      any one module") is cited as the reason for release 1 in the rationale and in 2.1.2, 2.1.4 and
      2.1.10, but the phasing marks c25 later (release 5, with standalone deployment). Cite it as a fact
      about the platform, or move it. (b) 2.1.6 says "The bank statement feed and the tax e-filing portal
      are named go-live integrations (S1-2.1.6-c17)". c17 reads "[bank statement feed], [POS or
      e-commerce], [attendance device, where used], [tax authority e-filing portal where applicable]"
      (p.11). The list is bracketed (a workbook value to confirm), and two of its four entries are dropped
      without saying so. (c) R-01 says the interim journals leave BO-01's second indicator "unmet until
      release 2". The indicator includes "a stock issue" (S1-2.2.4-c32, p.28), so it is unmet until release
      5, and a service-only tenant cannot meet it at all. BO-01's own text says this correctly.
    citation: >-
      release-phasing.yaml@f3b3b4c (release_1_rationale; 2.1.2; 2.1.4; 2.1.6; 2.1.10; R-01); SRC-001 pp.11,
      14 and 28 as quoted
  - severity: non-blocking
    text: >-
      [BO-03, faithfulness] "An entry becomes a record of account only when a second person approves it"
      generalises the overview figure ("Approval ... by a second person", S1-0-c04, p.4) past what the
      sections allow. Bank lines can "Auto-post" by rule (S1-2.6.5-c06, p.61; S1-2.6.3-c13), and schedule,
      revaluation and period-end entries are "generated and posted by the system on a schedule"
      (S1-2.6.12-c01, p.65). The approval for these sits on the rule or schedule, under maker–checker, not
      on each entry. Read literally, BO-03 forbids auto-posting by rule. "is never edited ... after
      approval" also takes one side of the open S1-2.2.6-c10 against c14 conflict (Q-007), which BO-03
      does not link. Recommend: "... when a second person approves it, or when it is raised by a rule or
      schedule approved under maker–checker", and add Q-007 to related. Deciding role: product-owner.
    citation: >-
      docs/requirements/objectives/BO-03.md@f3b3b4c (normative.statement; links.related); SRC-001 pp.4, 61
      and 65 as quoted; Q-007@v1
  - severity: non-blocking
    text: >-
      [Objectives, coverage and value] The seven cover the overview purpose (S1-0-c01, p.4): records and
      reports (BO-01), automates (BO-06), consistent (BO-01), compliance (BO-04), real-time visibility
      (BO-05), audit trail (BO-02), plus controls (BO-03) and growth (BO-07). Three points for the product
      owner. (a) No objective covers access, security, confidentiality and availability: "accessed through
      a browser from any location with no local installation" (S1-0-c01); 2.1.3; 2.16.1; payroll
      confidentiality (S1-2.10.14-c01). For a multi-tenant product (Q-001) tenant isolation is a business
      outcome, and release-1 sub-sections 2.1.3 and 2.16.1 trace to no objective. (b) Under the proposed
      phasing, none of BO-05's four indicators is reachable in release 1: S1-2.13.7-c01 is release 2;
      S1-2.15.11-c01 and c08 are release 4; c03 is needs-decision. BO-05 is "the one he uses directly",
      so the CFO should see this when deciding D-2.15.8. (c) BO-02's two indicators (S1-2.2.4-c32 "four
      steps", S1-2.11.7-c01 "four clicks") measure the same thing. Nothing invented: every indicator is
      SRC-001's own, brackets are kept in BO-06, and missing measures are left open in BO-03 and BO-07.
    citation: >-
      docs/requirements/objectives/BO-01.md to BO-07.md@f3b3b4c; SRC-001 p.4 (S1-0-c01);
      release-phasing.yaml@f3b3b4c (2.13.2, 2.15, 2.15.8, 2.15.11)
  - severity: non-blocking
    text: >-
      [Actors and glossary, "entity" and tenant] The glossary note on Entity says "Q-001 reads it as a
      tenant of TIQACC", and actors.yaml says that because of Q-001 "'the entity' in SRC-001 is read as a
      tenant". Q-001 records only that TIQACC is "Tiqri's own multi-tenant SaaS product" and makes no
      mapping of entity to tenant, so the reading is the steward's and is attributed to the wrong source.
      It is also ambiguous. SRC-001 uses "entity" both for its author and for each legal entity of a group
      that shares "One platform · one data set · one chart of accounts · one audit trail" (2.1.7 figure,
      p.13) and consolidates (S1-2.14-c01, p.106). Mapping a legal entity to a tenant would split a group
      across tenants. 2.14.2's reason ("a data-model dependency for every module and for multi-tenancy")
      blurs the same line. This is a hidden architecture and security assumption. Recommend a labelled
      assumption or a question: "a tenant holds one group of one or more legal entities". Owners:
      product-owner, with tech-lead and security-owner.
    citation: >-
      docs/requirements/glossary.yaml@f3b3b4c (term Entity, note); docs/requirements/actors.yaml@f3b3b4c
      (notes[0]); release-phasing.yaml@f3b3b4c (2.14.2); Q-001@v1; SRC-001 pp.13 and 106 as quoted
  - severity: non-blocking
    text: >-
      [Actors, states] src001-signatories says "Q-004 records that Tiqri treats SRC-001 as the signed
      baseline, confirmed by Shifan Cader". That copies Q-004's answer but leaves out its open item,
      "Confirmation of the baseline by Shifan Cader as product owner, which is to be recorded as a
      decision". CLAUDE.md records SRC-001 as unsigned, "an authoritative input, not an approved baseline".
      Recommend adding "(open: to be recorded as a decision, Q-004)", so the actor list does not state an
      approval that does not exist.
    citation: >-
      docs/requirements/actors.yaml@f3b3b4c (src001-signatories); Q-004@v1 (Open); CLAUDE.md at f3b3b4c
      (SRC-001 "is unsigned, so it is an authoritative input, not an approved baseline")
  - severity: non-blocking
    text: >-
      [Glossary, minor] (a) "Retention" is glossed only as a supplier-payment retention (S1-2.5.8-c04).
      SRC-001 uses the same word for record retention ("retained for [7] years", S1-2.1.4-c08; S1-2.11.4-c05),
      which Q-020 and Q-025 concern. Add the second sense or qualify the term. (b) "System-generated
      reversal" is marked defined, with "Any journal can be marked to reverse itself." (S1-2.2.7-c18,
      p.31). That is the run-in heading's first sentence, not a definition; form paraphrased would be more
      accurate. No definition contradicts SRC-001, and every defined: false checked is correct.
    citation: >-
      docs/requirements/glossary.yaml@f3b3b4c (terms Retention, System-generated reversal); SRC-001 pp.10,
      31, 53 and 100
created_at: "2026-10-21"
---

# Review of the business objectives, actors, glossary and release phasing at f3b3b4c

Independent E4 review for WF-01M5D0SE8MMS39CTPTXH8ME1HT step 5 (L1 discovery). The subjects are
`docs/requirements/objectives/BO-01.md` to `BO-07.md`, `docs/requirements/actors.yaml`,
`docs/requirements/glossary.yaml` and `docs/requirements/release-phasing.yaml`, at commit
`f3b3b4c435d8016d02f2edb6cc79689a1828a28a`. `git diff --stat f3b3b4c HEAD` shows only
`docs/governance/questions/Q-029.md` and `Q-030.md` added since, so the subject files I read are the
committed ones.

**Decision.** The objectives are faithful to SRC-001, and so are the actor list and the glossary. The
phasing is careful and almost always cites its reasons correctly. One defect is blocking. The interim
journal route on which the release 1/2 boundary rests is blocked by SRC-001 2.2.1, and 2.2.1 is itself
in release 1. Neither D-INT-1 nor Q-029 says so, so the product owner would decide the size of release 1
on an incomplete premise.

**Verdict: blocking-findings.** One finding is blocking and 13 are non-blocking. The blocking one is
fixed by amending D-INT-1, R-01 and Q-029. It does not invalidate the rest of the phasing. I found nothing
invented and no business rule decided by the steward. The nearest cases are:

- the entity-as-tenant reading, which is unlabelled and attributed to the wrong source;
- the "instalments meanwhile by approved journal" recommendation, which is labelled as a recommendation
  and owned by the tax specialist.

## Method and sample sizes

- **Objectives: all 7, every quote.** I checked all 18 indicator `basis` quotes and all 35 evidence quotes
  against the extraction, by Grep and by reading pp.4-8, 23-28, 68-75, 98-104 and 114-119. Every one
  matches; the only differences are line wraps. Each `clause` cited exists, and each says what the
  objective attributes to it.
- **Actors: 30 of 49 sampled** against the extraction. They were preparer, data-entry-sales,
  data-entry-purchases, stores, payroll-officer, approver, finance-manager, administrator, auditor-role,
  delegate, exception-approver, finance-team, finance-user, authorised-finance-administrator, management,
  executive, department-head, director, buyer, receiver, requisitioner, payroll-user, custodian,
  src001-signatories, customer, credit-insurer, payment-processor, rate-source, identity-provider and
  tiqri-provider. All quotes match; the findings cover two notes.
- **Glossary: 42 of 125 terms sampled**, including 14 of the 23 `defined: false`. Defined terms checked:
  Clause, Bracketed value, Entry table, Cross-reference, Acceptance tests, Module activation, Business
  profile, Platform services, Role, Effective permissions, Segregation of duties matrix, Assistant,
  Statutory series, Chart of accounts, Class, Control account, Posting rules engine, Correction entry,
  System-generated reversal, Open, Hard closed, Adjustment period, Special audit adjustment period,
  Transaction, Functional and Reporting currency, Rate types, Non-tax invoice, Credit note, Debit note,
  Proforma invoice, Credit exposure, Ageing buckets, Goods received not invoiced, Unpresented item,
  Depreciation book, Country rule set, Locked payroll run, Report definition, Report by written
  instruction, Consolidation ledger, Topside adjustment, Consolidation run states. Undefined terms
  checked: Vendor, Go-live, Entity, Group, Compensating control, Maker–checker, Sub-ledger, Prior-period
  item, Monetary and non-monetary balances, Expected credit loss, Reverse charge, Turnover levy, EPF and
  ETF, EBITDA. Every quote matches. Every `defined: false` I checked is correct: SRC-001 uses the term
  without saying what it means. No definition contradicts SRC-001, though the note on Entity misattributes
  a reading (finding 12).
- **Phasing: all 187 marks read.** I read in full in the extraction every release-1 sub-section whose
  text cross-references another area: 2.1.5 to 2.1.8, 2.2.1, 2.2.2, 2.2.4, 2.2.10, 2.3.2, 2.4.2, 2.5.2,
  2.5.5, 2.5.6, 2.5.13, 2.5.18, 2.6.5, 2.6.17, 2.7 to 2.7.11, 2.11.1 to 2.11.7, 2.12.1 to 2.12.5, 2.13.1,
  2.13.7 and 2.16.1 to 2.16.4. All 17 splits were checked clause by clause.
- No PDF page was rendered; quotes are against the extraction. My shell profile runs no ad hoc scripts,
  so every count above was made by reading and by Grep.

## 1. Business objectives

| BO | Faithful | Indicators from SRC-001 | Release-1 reachable | Notes |
| --- | --- | --- | --- | --- |
| BO-01 | Yes | Yes (S1-2.12.1-c01, S1-2.2.4-c32) | First yes; second only in release 5 | — |
| BO-02 | Yes | Yes | Yes | Two indicators measure the same thing |
| BO-03 | Overstated | Yes | Yes | Finding 10 |
| BO-04 | Yes | Yes | Yes | — |
| BO-05 | Yes | Yes | No | Finding 11(b) |
| BO-06 | Yes | Bracketed values kept (values 118, 120) | Yes | — |
| BO-07 | Yes | Yes | One of three (S1-2.7.11-c09) | — |

**Coverage.** The seven cover S1-0-c01's purpose, with no overlap that matters: BO-01 is about posting,
BO-06 about routine automation. The gap is access, security, confidentiality and availability
(finding 11(a)). No objective, indicator or target is invented. Where SRC-001 gives no measure (BO-03
over time, BO-07 commercial), the steward leaves it open for the product owner.

## 2. Release phasing

**Dependency soundness under S1-2.1.7-c09.** The module-dependent-clauses rule is sound for postings
that "arise only where the inventory module is active" (S1-2.1.7-c77). It is not sound where the
release-1 transaction exists anyway and needs data from a later area:

- item tax class and service items from the item master (finding 4);
- employees for expense claims (finding 5);
- capital purchases and depreciation into fixed-asset control accounts (findings 1 and 2).

The governance panel dependency is correctly made a decision (2.15.8).

**Release-1 completeness for one service-based Sri Lanka entity.**

| Area | End to end in release 1 | Gap |
| --- | --- | --- |
| Posting | Yes: 2.2, 2.6.10 | — |
| Receivables | Yes, once the service item master is in | Finding 4 |
| Payables | Yes, except expense claims | Finding 5 |
| Bank | Yes | — |
| Tax: VAT, SSCL, WHT, other duties | Yes | — |
| Tax: payroll | Interim, outside the system | Finding 2 |
| Tax: corporate income tax | Needs decision | — |
| Close | Yes: 2.2.8, 2.12 | Staff cost and depreciation journals conflict with 2.2.1 (finding 1) |
| Reporting | Yes: 2.13.1, 2.2.10-c02 | — |
| Opening position | No | Finding 6 |

**Statutory needs for Sri Lanka deferred wrongly.**

- None is deferred without being flagged: VAT, turnover levy, WHT and other duties are release 1.
- The payroll returns are deferred with payroll, and must still be tracked in release 1 (finding 2).
- Which taxes apply is rightly left to the tax specialist (Q-003, Q-021). I assert no Sri Lanka rule.
  EPF, ETF and payroll income tax are named only as they appear in SRC-001's illustrative dashboard.

**Splits.** 15 of the 17 are sensible. Two need changes:

- 2.1.8: data-model clauses are deferred (finding 7);
- 2.1.7: c25 is cited as a release-1 reason while marked later, and c84 is deferred whole (findings 8
  and 9).

Within 2.5.18, c01 belongs with inventory (finding 8).

**The four needs-decision items.**

- 2.8.8: the owner is right, and the case is clear.
- 2.15.8: the owner is right, and the recommendation is reasonable.
- 2.16.2: the owner is right, but the fallback fails (finding 6).
- 2.16.3: the owner is right.

**`decisions_needed`.** Each has the right owner. D-INT-1 should also name the tax specialist, and its
scope should be widened (findings 1 and 2).

**Assumptions A-01 to A-03.** All three are labelled, owned by the product owner, and say what changes if
they are wrong. A-02 should note that Sinhala and Tamil are outside SRC-001's minimum list.

**Risks.** There are four, R-01 to R-04, not three.

| Risk | Real | Mitigated in the phasing | Notes |
| --- | --- | --- | --- |
| R-01 | Yes | Not adequately | Misses the control-account consequence, and misstates the indicator's release (findings 1 and 9) |
| R-02 | Yes | Partly | Its own clause, c22, is deferred (finding 7) |
| R-03 | Yes | Yes | S1-2.2.1-c18 and 2.14.2 are kept in release 1 |
| R-04 | Yes | Yes | Mitigated by the question process |

Three risks are missing:

- the control-account interim;
- the release-2 loading of the fixed-asset register and year-to-date payroll;
- the tenant boundary.

### Q-029 (D-INT-1): competing readings

| Reading | SRC-001 support | Consequence |
| --- | --- | --- |
| (A) Interim manual journals as a time-limited exception | S1-0-c02 ("adjustments ... by manual journal ... where required"); S1-2.11.5-c01 (working for "depreciation ... gratuity" attached to "the journal that posts it") | Conflicts with S1-2-c02, S1-0-c10, S1-2.8-c01 and S1-2.2.1-c06/c21. Needs either a relaxed control or interim non-control accounts plus reclassification at release 2 (S1-2.2.2-c16) |
| (B) No exception | S1-2-c02; S1-2.8.3-c01 | Payroll and fixed assets move into release 1, roughly doubling it |
| (C) Payroll by interface from a current system; fixed assets decided separately | S1-2.1.7-c09; S1-2.1.6-c14 | Depends on Q-022 and on a payroll system existing today (Q-006). The qualified accountant must confirm that interface postings may hit payroll control accounts. SRC-001 gives depreciation no interim route |

**Recommended resolution for the product owner, with the qualified accountant:**

1. Amend Q-029 first (finding 1).
2. Then consider (C) for payroll, and the fixed-asset core in release 1.

This recommends; it does not decide.

## 3. Actors and glossary

- **Actors.** Sampled entries are accurate and stay within their clauses. Bracketed roles are rightly left
  to the workbook. Two notes need correcting (findings 12 and 13).
- **Glossary.** Accurate. `defined: false` is applied correctly. Two minor points (finding 14).

## Outside the subject (for the orchestrator)

Q-030, committed after f3b3b4c, asks "who maintains the provision matrix" and says the clause "continues
with the role". SRC-001 answers this: "computed on a provision matrix maintained by Finance — loss rate
by ageing band, customer group or risk rating" (S1-2.3.10-c01, p.41). The open question is the
measurement policy and the loss rates, not who maintains the matrix.

## Verification (observed)

- `python tools/governance/check.py` before writing this record: `check: 0 error(s), 0 warning(s)`. The
  result after writing it is in the handoff report.
- `git rev-parse f3b3b4c`: `f3b3b4c435d8016d02f2edb6cc79689a1828a28a`. `git diff --stat f3b3b4c HEAD`:
  Q-029.md and Q-030.md only. `git status --short`: empty.
- Grep over glossary.yaml: 125 `term:` entries and 23 `defined: false`, which match the commit message.

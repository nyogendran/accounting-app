---
id: REV-01M5DADKQY1VNR1FMN2414KZ58
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - commit: 6eb263a586a8dade8bae0ee61f03486188b489fa
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [Index, boundary error] S1-2.4.3-c04, c05 and c06 cut two obligations in half. The 2.4.3 list of
      mandatory content is two independent columns (tax invoice, non-tax invoice) that are not
      row-aligned: on extraction line 1971 the third tax-invoice item ends ("where prescribed") on the
      same line on which the fourth non-tax item starts. Splitting by printed line therefore puts the
      non-tax item "Description, quantity and price per line, the currency of the document, and total
      payable" across c04 (line 1971) and c05 (line 1972), and "No tax rate, no tax amount, no tax line
      anywhere on the face" across c05 (line 1973) and c06 (line 1974). c02 to c07 also each pair a
      tax-invoice obligation with an unrelated non-tax one. The "one printed row" rule assumes
      row-aligned cells, which the grids in 2.10.11 and 2.15.4 have and 2.4.3 does not. Line ranges
      cannot separate two columns that share lines, so the fix is one clause for the whole list, or one
      clause per item (8 + 6) sharing a line range with a column attribute, after reading p.46. Until
      then no requirement should cite S1-2.4.3-c04 to c06. This is statutory invoice content, so fix it
      before 2.4 is derived.
    citation: >-
      docs/requirements/clause-index.yaml@6eb263a (S1-2.4.3-c04 lines [1970, 1971], c05 [1972, 1973],
      c06 [1974, 1974]); docs/sources/SRC-001-spec-v1/extracted/spec-v1.txt@6eb263a:1967-1980; "No tax
      rate, no tax amount, no tax line anywhere on the face" (SRC-001 p.46, §2.4.3)
  - severity: non-blocking
    text: >-
      [Index, subheading] The subheading field is positional ("the nearest unnumbered sub-heading
      above") and in places misstates scope. The 2.2.7 entry table and acceptance statement
      (S1-2.2.7-c24 to c31), which cover prepayments, deferred income, accruals and early termination,
      carry "System-generated reversal", the run-in heading of one paragraph. The engine and validation
      rules S1-2.6.10-c08 to c13 and S1-2.6.11-c05 to c11 carry the grid captions "What a rule can be
      configured by" and "Validated before anything posts". S1-2.6.1-c25 (opening a bank or cash
      account) carries "Petty cash and floats". S1-2.6.6-c18 to c22 (the reconciliation screen,
      statuses, attachments, the hard-close block and reopening) carry "Manual intervention" (see the
      extraction-gap finding). The rules also do not say that run-in headings such as "Creating a
      schedule." count as sub-headings, though they are used so. Correct under the stated mechanics;
      recommend that the rules say subheading is positional and is not a statement of scope.
    citation: >-
      docs/requirements/clause-index.yaml@6eb263a (rules; the entries named);
      docs/sources/SRC-001-spec-v1/extracted/spec-v1.txt@6eb263a:1284, 1315, 1326-1339, 2492-2502,
      2626-2639, 2696-2711, 2713-2730
  - severity: non-blocking
    text: >-
      [Index, assumption 2] The rules say "Numbered items restart under each sub-heading, so a citation
      names the section, the subheading and the item number". Numbering also restarts after a table
      with no new sub-heading, so that triple is not unique in three places: S1-2.6.5-c01 and c09 are
      both item 1 with subheading null; S1-2.6.6-c15 and c18 are both item 1 under "Manual
      intervention"; S1-2.7.6-c01 and c14 are both item 1 with subheading null. Clause IDs are unique,
      so recommend citing by clause ID and correcting the sentence.
    citation: >-
      docs/requirements/clause-index.yaml@6eb263a (rules; S1-2.6.5-c01, c09; S1-2.6.6-c15, c18;
      S1-2.7.6-c01, c14); docs/sources/SRC-001-spec-v1/extracted/spec-v1.txt@6eb263a:2579-2597,
      2627-2639, 2998-3018
  - severity: non-blocking
    text: >-
      [Index, assumption 3c] Kind "other" is not one clause per figure only: bands printed in a figure
      are separate "other" clauses (S1-0-c05, S1-0-c06, S1-2.1.7-c02), which the rules allow. Several
      "other" clauses state obligations, for example "a late posting sends the reconciliation back to
      prepared" (S1-2.12.4-c01, p.102), "a fixed-salary entity starts at gross pay — the first stage
      does not arise" (S1-2.10.7-c09, p.95) and "Supporting evidence — the scan, the approval and the
      calculation stay with the transaction, not on a shared drive" (S1-0-c06, p.4). Observation:
      later work must not read "other" as non-normative; one sentence in the rules would say so.
    citation: >-
      docs/requirements/clause-index.yaml@6eb263a (32 clauses of kind other, counted by Grep); SRC-001
      pp.4, 95 and 102 as quoted
  - severity: non-blocking
    text: >-
      [Workbook, owners, assumption 6] Each defaulted owner is defensible, but two classes are split.
      (a) Code structure: the account-code length and group depth (values 25, 26) go to the qualified
      accountant as "chart of accounts design", while the dimension code formats (values 32 to 37),
      which the steward calls "dimension design maintained by Finance", go to the product owner. Q-005
      records that the qualified accountant creates the chart in the built system, and the same
      reasoning covers the dimension codes. (b) Control thresholds: the minor-difference write-off
      threshold (value 56) goes to the qualified accountant as "accounting treatment", while the
      dormant-account period, the manual-journal evidence threshold and the reconciling-item age
      (values 31, 159, 162) go to the product owner with the accountant advising. A threshold is not a
      treatment in either case. Recommend one rule per class, chosen by the orchestrator against the
      authority matrix. No value changes.
    citation: >-
      docs/requirements/bracketed-values.yaml@6eb263a values 25, 26, 31-37, 56, 159, 162; Q-005@v1
      ("the qualified accountant creates it in the built system"); docs/governance/authority-matrix.yaml
      at 6eb263a (decisions)
  - severity: non-blocking
    text: >-
      [Workbook, owners] Service-level targets are split between owners. Availability, recovery point
      and recovery time (values 175 to 177) and response times (values 16, 96, 153, 169) go to the tech
      lead under the brief's "platform" mapping, while the support SLA in the same 2.16.1 table goes to
      the product owner (missing inputs). For Tiqri's own multi-tenant product (Q-001) all of them are
      service commitments to tenants. The authority matrix gives "Requirement scope and priority;
      acceptance of business outcomes" to the product owner and has the tech lead escalate "where cost
      or scope is affected". Recommend the product owner decides them with the tech lead confirming
      feasibility. This follows the orchestrator's mapping, so it is for the orchestrator to confirm,
      not a steward error.
    citation: >-
      docs/requirements/bracketed-values.yaml@6eb263a values 16, 96, 153, 169, 175-177 and the missing
      input "Support SLA"; docs/governance/authority-matrix.yaml at 6eb263a; Q-001@v1
  - severity: non-blocking
    text: >-
      [Workbook, assumptions 5 and 7] Two presentation points, neither an invented value. (a) Value 160
      copies spec_value "7", but its own clause says "[7] years is a placeholder to be confirmed, not a
      fixed figure in the software" (S1-2.11.4-c05, p.100). Under assumption 5's rule ("placeholders are
      null") set it to null or say so in needed_for, so that 7 is not read as the specification's value;
      the same caution fits the other six "[7] years" (values 15, 40, 147, 157, 164, 168). (b) The
      commit message calls the 178 "values to confirm", but values 1 to 3, 80 to 85 and 130 are marked
      "Nothing to confirm", so at most 168 need a decision, while the totals block counts all 178 by
      owner and kind.
    citation: >-
      docs/requirements/bracketed-values.yaml@6eb263a (values 1-3, 80-85, 130, 160; totals); message of
      commit 6eb263a; "[7] years is a placeholder to be confirmed, not a fixed figure in the software"
      (SRC-001 p.100, §2.11.4, 5)
  - severity: non-blocking
    text: >-
      [Workbook, missing inputs] Two additions. (a) The chart-of-accounts naming standard is referenced
      but never given: "Follows the naming standard in 2.2.2; abbreviations and personal shorthand are
      not permitted" (S1-2.2.1-c05, p.23) and "Unique; follows the naming standard" (S1-2.2.2-c08,
      p.24); 2.2.2 contains no standard. Owner: qualified-accountant. (b) The Annexure A list omits one
      more clause addressed to a vendor: "the commercial and technical dependency on any other module
      is stated — not assumed" (S1-2.1.7-c11, p.13). The finding on vendor-addressed clauses names the
      commercial and handover clauses that also need an internal answer.
    citation: >-
      docs/requirements/bracketed-values.yaml@6eb263a (missing_inputs); SRC-001 pp.13, 23 and 24 as
      quoted; Grep "naming standard" over the extraction at 6eb263a: lines 974 and 1031 only
  - severity: non-blocking
    text: >-
      [Claim 1, dimension changes after approval] Genuine contradiction, for dimensions only.
      S1-2.2.6-c10: "No screen, import, API call or administrator action can change its value, account,
      date, dimensions or party" (p.29). S1-2.2.6-c14: "Narrative, internal reference or dimension
      changes that alter no value and no account may be permitted after approval where the entity
      chooses, under approval by [role], with the change recorded" (p.29). S1-2.2.6-c03 adds "nothing
      after it can" be changed (p.28). Narrative and internal reference are not in c10's list, so they do
      not conflict. Readings: (A) c10 governs and "dimension" is dropped from c14, so a wrong dimension is
      corrected by reversal and re-entry; (B) c14 is a per-entity exception to c10, so posted lines become
      mutable in their dimensions and a report by dimension for a reported period can change; (C) c14 is
      realised as a system-generated, linked reclassification entry that moves the amount between
      dimension values on the same account, leaving c10's lock intact. The specification uses (C)'s
      pattern for accounts, "posting a visible journal rather than rewriting history" (S1-2.2.2-c18,
      p.25), and 2.4.6 calls itself "the statutory exception to the amendment route in 2.2.6" (p.48),
      which suggests c14 is deliberate. Consequence: mutable or immutable posted lines is an early
      data-model decision. Deciding role: qualified-accountant. Recommendation: (C), with the accountant
      also deciding whether it applies in closed or filed periods.
    citation: >-
      "No screen, import, API call or administrator action can change its value, account, date,
      dimensions or party" (SRC-001 p.29, §2.2.6 After approval, 1); "Narrative, internal reference or
      dimension changes that alter no value and no account may be permitted after approval" (SRC-001
      p.29, §2.2.6 After approval, 5); SRC-001 pp.25, 28 and 48 as quoted
  - severity: non-blocking
    text: >-
      [Claim 2, suspense at close] Genuine contradiction. S1-2.6.3-c15: "Suspense must be nil before a
      period can be closed." (p.60). S1-2.6.11-c10: "Suspense must be nil, or every remaining item
      explained and approved, before a period can be hard-closed." (p.64). The bank acceptance test sides
      with 2.6.11: "The period cannot be closed while the bank reconciliation carries an unexplained
      difference or suspense carries an unexplained item." (S1-2.6.17-c10, p.67). A specific-versus-
      general reading (bank suspense nil, other suspense explainable) does not hold, because 2.6.11 names
      the bank case as its main one: "an unidentified bank receipt being the main case" (S1-2.6.11-c08,
      p.64). "Closed" here means hard-closed, since a soft-closed period still takes postings
      (S1-2.2.8-c10, p.32). Consequence: whether an explained and approved suspense balance may survive a
      hard close. Deciding role: qualified-accountant. Recommendation: 2.6.11-c10 governs, as the clause
      of the section that specifies suspense ("A requirement is specified once and referenced
      elsewhere", S1-1-c06, p.6) and as what the acceptance test checks; read 2.6.3-c15 as a pointer.
    citation: >-
      "Suspense must be nil before a period can be closed." (SRC-001 p.60, §2.6.3, 7); "Suspense must be
      nil, or every remaining item explained and approved, before a period can be hard-closed." (SRC-001
      p.64, §2.6.11, 6); SRC-001 pp.6, 32 and 67 as quoted
  - severity: non-blocking
    text: >-
      [Claim 3, external payroll] Ambiguity, reconcilable. S1-2.10-c01: "Payroll is native to the system.
      A third-party payroll product synchronising by file transfer is not acceptable, because it breaks
      the audit trail between the payslip and the ledger." (p.90). S1-2.1.6-c14: "where it is not
      activated, the external system takes its place and feeds TIQACC through this interface" (p.11);
      S1-2.1.6-c09 lists "Payroll and workforce management" among the systems to integrate, and file
      import is one of the interface methods (S1-2.1.6-c04, p.11). Reading (A), which reconciles: 2.10
      constrains how TIQACC's own payroll module is delivered (native, not a third-party product attached
      by file), and 2.1.6 governs entities that do not activate it. Reading (B): no external payroll may
      feed TIQACC by file, which contradicts 2.1.6-c04 and c14. Reading (C): external payroll may feed
      only through the API. (A) is supported by the standalone model, in which TIQACC payroll itself
      "delivers its accounting output to an external ledger" (S1-2.1.7-c84, p.17), so 2.10's reason
      cannot be a general ban on separating payslip and ledger. Consequence: whether the integration
      framework accepts payroll journals by file from entities without the payroll module. Deciding role:
      product-owner. Recommendation: (A).
    citation: >-
      "A third-party payroll product synchronising by file transfer is not acceptable" (SRC-001 p.90,
      §2.10); "where it is not activated, the external system takes its place and feeds TIQACC through
      this interface" (SRC-001 p.11, §2.1.6 Systems to be integrated, 1); SRC-001 pp.11 and 17 as quoted
  - severity: non-blocking
    text: >-
      [Claim 4, invoice series reset] Not a contradiction. S1-2.1.10-c18 defines the capability, "Reset
      rule Never, annually at the financial year end, or at the start of each period — set per series"
      (p.21), and S1-2.4.1-c06 states the setting for sales tax series, "restarting at the beginning of
      each financial year ... under the numbering framework in 2.1.10" (p.45): a specific clause using one
      option of the general framework. Residual ambiguity: whether that annual restart is fixed or, like
      the format, illustrative, since "The formats shown above are illustrative; each is set to meet the
      regulatory requirement of the country the document is issued in, without development"
      (S1-2.4.1-c09, p.45) and "every format shown elsewhere in this document is illustrative"
      (S1-2.1.10-c19, p.21). Deciding role: tax-specialist, per country. Recommendation: treat the annual
      restart as the default for sales tax series, set per country.
    citation: >-
      "Reset rule Never, annually at the financial year end, or at the start of each period — set per
      series" (SRC-001 p.21, §2.1.10); "restarting at the beginning of each financial year" (SRC-001 p.45,
      §2.4.1, 1); SRC-001 pp.21 and 45 as quoted
  - severity: non-blocking
    text: >-
      [Claim 5, reconciliation self-review] Ambiguity, reconcilable in the main. 2.1.2 names this
      separation as releasable: "Every other separation — including preparing and reviewing the same
      reconciliation ... — is enforced by default but can be released for a named user as a documented
      exception" (S1-2.1.2-c17, p.9); 2.12.2-c07 (p.101), 2.6.6-c19 (p.62) and the acceptance test
      S1-2.12.5-c03 ("in which case the reconciliation is accepted and flagged as self-reviewed", p.102)
      carry the release, so "self-review is blocked" (S1-2.12.3-c04, p.101) states the default. The
      residue: S1-2.6.16-c13 says "the user who prepares a reconciliation cannot approve it" (p.67); the
      record has both "reviewed" and "approved" states (S1-2.12.2-c08, p.101); and the non-releasable "a
      user cannot approve a document they raised" (S1-2.1.2-c16, p.9) may or may not cover a
      reconciliation. If approval is a third step the preparer can never take, a one-person team still
      cannot finish a reconciliation, against 2.1.2's aim "so that a small finance team with one
      qualified person is not blocked from operating". Deciding role: qualified-accountant.
      Recommendation: one second step (review is the approval), releasable for every reconciliation
      including bank, and 2.1.2-c16 not applied to reconciliations. The same question applies to the
      three-user tax return workflow (S1-2.7.4-c06, p.70).
    citation: >-
      "including preparing and reviewing the same reconciliation" (SRC-001 p.9, §2.1.2 Segregation of
      duties, 6); "self-review is blocked" (SRC-001 p.101, §2.12.3, 4); "the user who prepares a
      reconciliation cannot approve it" (SRC-001 p.67, §2.6.16, 4); SRC-001 pp.62, 70, 101 and 102 as
      quoted
  - severity: non-blocking
    text: >-
      [Claim 6, cross-reference] Not a contradiction: a cross-reference error in SRC-001. "Owner Yes, for
      balance sheet accounts The person responsible for reconciling it under 2.10" (S1-2.2.2-c13, p.24)
      points to "2.10 Payroll and workforce" (p.90); the rule is in 2.12: "Every balance sheet account is
      assigned an owner" (S1-2.12.3-c01, p.101). Read as 2.12. Deciding role: product-owner, as an
      editorial correction; no accounting decision is needed. A weaker case of the same kind: budgets are
      cited to 2.2.3 ("Budget versus actual ... 2.2.3", S1-2.13.1-c14, p.103; module catalogue
      S1-2.1.7-c46, p.15), but 2.2.3 has no budget clause; budgets are specified in "Budget upload by
      account and dimension, multiple versions, locked once approved" (S1-2.2.10-c03, p.36) and 2.14.11.
    citation: >-
      "The person responsible for reconciling it under 2.10" (SRC-001 p.24, §2.2.2); "Every balance sheet
      account is assigned an owner" (SRC-001 p.101, §2.12.3, 1); SRC-001 pp.15, 36, 90 and 103 as quoted
  - severity: non-blocking
    text: >-
      [Claim 7, depreciation example] Ambiguity, not a contradiction. "Category [Office equipment],
      straight line, [20]% per year, residual [0], start rule pro-rata by days. The user enters cost
      [1,200,000] and date in use [1 October]." with "Year 1 — three months 1,200,000 60,000" and "Year 6
      — final nine months 180,000" (S1-2.8.3-c26, c27, c31, p.78). The annual charge is 240,000; 60,000
      and 180,000 are exactly 3/12 and 9/12 of it. That matches the "full month in the month of purchase"
      start rule or a 30/360 day count (90/360, 270/360), not actual days: 1 October to 31 December is 92
      days, and 240,000 × 92/365 = 60,493.15. The example also assumes a 31 December year end, which
      SRC-001 leaves per entity (S1-2.2.8-c02, p.31; Q-003 open). The other rows and the 1,200,000 total
      add up. The figures are declared illustrative (S1-2.8.3-c32, p.78), but the acceptance test relies
      on the start rule: "An asset bought mid-period is charged according to the category's start rule"
      (S1-2.8.16-c02, p.83). Deciding role: qualified-accountant, who should state the day count and
      leap-year treatment of "pro-rata by days" and have the rule or the figures corrected before the
      example becomes test data.
    citation: >-
      "start rule pro-rata by days" and "Year 1 — three months 1,200,000 60,000 60,000 1,140,000" (SRC-001
      p.78, §2.8.3 Worked example); "Pro-rata by days from the date in use, full month in the month of
      purchase, or from the following month" (SRC-001 p.77, §2.8.3); SRC-001 pp.31 and 83 as quoted
  - severity: non-blocking
    text: >-
      [Claim 8, extraction gaps] (a) 2.6.6: confirmed. Items 1 to 3 (lines 2627-2631) follow "Manual
      intervention"; items 1 to 5 (lines 2632-2639) follow with no heading and cover the reconciliation
      screen, statuses, attachments, the hard-close block and reopening. The index boundaries are right
      (S1-2.6.6-c15 to c22); only the subheading of c18 to c22 is uncertain. Whether p.62 has a heading
      there cannot be settled from the extraction. (b) Interleaved tables: I checked all ten by
      reconstruction, not against the PDF (see Method and limits). Nine are split correctly (lines
      574-605, 699-723, 1358-1374, 2857-2866, 3911-3922, 3966-3984, 4070-4078, 4601-4612, 4869-4878);
      1967-1980 (2.4.3) is not, as in the first finding. Two notes: the "Set by" cell "[role], with
      approval" is interleaved into the audit-locked effect text (line 1372), which workbook value 47
      already records; and the 2.7 tax-set row for Entity B shows four values for five columns ("Y — Y
      Y", line 2861), a cell the extraction lost. No decision role: an evidence question to settle from
      pp.46, 62 and 68.
    citation: >-
      docs/sources/SRC-001-spec-v1/extracted/spec-v1.txt@6eb263a:2626-2639, 1372, 2861 and the ten ranges
      named; docs/requirements/clause-index.yaml@6eb263a (S1-2.6.6-c15 to c22)
  - severity: non-blocking
    text: >-
      [Open question, vendor-addressed clauses] Confirmed, with additions. Each of the eleven asks a vendor
      to state, quote or answer, for example "Encryption in transit and at rest, with the standard stated
      in the vendor response" (S1-2.1.3-c03, p.9) and "the vendor states where data and backups physically
      sit" (S1-2.1.3-c04, p.10); under Q-001 there is no vendor to answer. Also vendor-addressed:
      S1-2.1.7-c11 ("the commercial and technical dependency on any other module is stated — not
      assumed", p.13). Not vendor-addressed, but resting on the customer-and-vendor relationship that
      Q-001 removes: "delivered as configuration or an included release, at no extra charge"
      (S1-2.16.1-c06, p.119) and the handover deliverables, in particular "User manual per module, written
      for our processes and not a generic product manual" (S1-2.16.3-c02, p.120). Owners: product-owner
      for scope and commercial terms; security-owner with the tech lead for the encryption standard; the
      tech lead with the security owner for hosting locations. The statutory residency rule per country
      has no clear owner in the authority matrix (nearest: the tax specialist's "Tax and statutory rules
      per jurisdiction"), which the orchestrator should settle. The obligations themselves (encryption,
      residency) stand; only the "vendor states" parts need an internal answer.
    citation: >-
      SRC-001 pp.5, 6, 9, 10, 13, 14, 15, 17, 20, 36, 100, 119 and 120 (the eleven clauses listed in the
      workbook's missing_inputs, plus S1-2.1.7-c11, S1-2.16.1-c06 and S1-2.16.3-c01 to c04); Q-001@v1;
      Grep for "vendor", "quote", "Annexure", "licens" and "our" over the extraction at 6eb263a
  - severity: non-blocking
    text: >-
      [Open question, support SLA] Confirmed. "Support Severity-based response and resolution times
      stated in the SLA, with named escalation contacts" (S1-2.16.1-c05, p.119). A search of the
      repository for "SLA" finds only the extraction and the two reviewed files, so no SLA exists. For
      Tiqri's product it becomes a service commitment to tenants. Owner: product-owner, with the tech
      lead advising. Its severity levels should line up with the acceptance protocol, "No module is
      accepted with an open critical or high defect" (S1-2.16.4-c03, p.120), and with the defect severity
      scale SRC-005 A3 proposes for Gate A.
    citation: >-
      "Severity-based response and resolution times stated in the SLA" (SRC-001 p.119, §2.16.1); Grep
      "\bSLA\b|service level" (case-insensitive) over the repository at 6eb263a: three files; SRC-005 §A3
  - severity: non-blocking
    text: >-
      [Open question, retention] Confirmed, and wider than stated: SRC-001 uses two retention models. Six
      clauses fix a bracketed period, "retained for [7] years": audit log (S1-2.1.4-c08, p.10),
      transaction history (S1-2.2.6-c28, p.30), fixed-asset records (S1-2.8.15-c06, p.83), payroll
      history (S1-2.10.14-c07, p.98), reconciliations (S1-2.12.3-c07, p.101) and group-layer records
      (S1-2.14.13-c07, p.113). Others defer to a configurable rule, "configurable per entity and per
      document type ... the longer of the entity's own policy and the statutory retention period of each
      jurisdiction it operates in" (S1-2.11.4-c05, p.100), which period records (S1-2.2.8-c48, p.33) and
      interface logs (S1-2.1.6-c30, p.12) follow; tax evidence is kept "for the period each jurisdiction
      requires" (S1-2.7.7-c30, p.73). Unstated: whether the six fixed periods also follow the longer-of
      rule per jurisdiction, and what happens to non-document records at the end of retention (the
      disposal rule in S1-2.11.4-c06 covers documents). Owners: tax-specialist for the statutory periods
      per country and record type ("Tax and statutory rules per jurisdiction"); product-owner for the
      default entity policy in a multi-tenant product and for one model across all records.
    citation: >-
      SRC-001 pp.10, 12, 30, 33, 73, 83, 98, 100, 101 and 113 as quoted; Grep "retain|retention" over the
      extraction at 6eb263a
  - severity: non-blocking
    text: >-
      [Open question, statutory forms, formats and wording] Confirmed. "Return format The statutory form
      the return maps to, and the electronic file format for the filing portal where one exists"
      (S1-2.7.1-c11, p.68); "Export in the file format required by each jurisdiction for e-filing or
      e-invoicing" (S1-2.4.7-c04, p.48); "the wording prescribed by [applicable tax law]" (S1-2.4.3-c09,
      p.46); also S1-2.7.4-c07 (p.70) and S1-2.7.9-c09 (p.74). None is in the repository, and all depend
      on the countries in Q-003. Owner: tax-specialist. Timing: SRC-001 says titles and prescribed
      wording "are confirmed in user acceptance testing" (S1-2.4.4-c03, p.47), so the build needs the
      configurable mechanism and each country's content is needed before that country's tax acceptance,
      not before the build starts.
    citation: >-
      SRC-001 pp.46, 47, 48, 68, 70 and 74 as quoted; Q-003@v1
  - severity: non-blocking
    text: >-
      [New, standalone credit and debit notes] Genuine contradiction. "Credit and debit notes Against a
      named invoice or standalone, approved before issue, reversing revenue and tax per 2.4.6"
      (S1-2.3.3-c10, p.38) against "Every credit and debit note references the original document number
      and inherits its tax treatment. Its value cannot exceed the value of the original document"
      (S1-2.4.6-c03, p.48). A standalone note has no original to reference, inherit from or cap against.
      Also ambiguous: whether the cap applies to debit notes, which add a charge ("Additional charge
      against an issued invoice", S1-2.4.1-c05, p.45). Deciding role: tax-specialist (statutory document
      rules per country), with the qualified accountant for the treatment of standalone credits.
      Recommendation: decide per country whether standalone sales credit notes are allowed and, if so,
      their tax treatment and limit.
    citation: >-
      "Against a named invoice or standalone" (SRC-001 p.38, §2.3.3); "Every credit and debit note
      references the original document number and inherits its tax treatment" (SRC-001 p.48, §2.4.6, 3)
  - severity: non-blocking
    text: >-
      [New, cancelling an issued invoice] Requirement gap and ambiguity. "Cancellation is permitted only
      before payment and before the tax return for that period is filed" (S1-2.4.6-c02, p.48), and an
      invoice can reach the state "cancelled" (S1-2.3.2-c05, p.37), but the correction table routes
      issued invoices to "Credit note or debit note under 2.4.6" (S1-2.2.6-c17, p.29), and the
      receivables entry table (2.3.12, p.42) has no row for cancelling an issued invoice whose
      receivable, revenue and output tax have already posted. Unstated: the entry a cancellation raises,
      its period, and when cancellation rather than a credit note applies. Deciding roles: tax-specialist
      (whether a tax invoice may be cancelled in each country) and qualified-accountant (the reversing
      entry).
    citation: >-
      "Cancellation is permitted only before payment and before the tax return for that period is filed"
      (SRC-001 p.48, §2.4.6, 2); "Issued tax or non-tax invoice Credit note or debit note under 2.4.6"
      (SRC-001 p.29, §2.2.6); SRC-001 pp.37 and 42
  - severity: non-blocking
    text: >-
      [New, correcting a posted depreciation run] Genuine contradiction, reconcilable by scope. "Posted
      depreciation Adjustment journal with the working attached; the run itself is not re-run"
      (S1-2.2.6-c21, p.29) against "A posted run can be reversed and recalculated only within an open
      period, by [role]" (S1-2.8.5-c09, p.79) and the acceptance test "a reversal within an open period
      retains both the reversal and the replacement" (S1-2.8.16-c11, p.83). Reconciling reading:
      2.2.6-c21 applies to closed periods, as "A re-run of a posted closed period is blocked" says
      (S1-2.8.5-c10, p.79). Deciding role: qualified-accountant.
    citation: >-
      "the run itself is not re-run" (SRC-001 p.29, §2.2.6); "A posted run can be reversed and
      recalculated only within an open period" (SRC-001 p.79, §2.8.5, 9); SRC-001 p.83 as quoted
  - severity: non-blocking
    text: >-
      [New, tax registration reference for unregistered customers] Ambiguity in an acceptance test. "An
      unregistered customer cannot be issued a document carrying a tax registration reference."
      (S1-2.4.8-c02, p.48). Yet a tax invoice may go to "any customer where the law requires a tax
      invoice" (S1-2.4.1-c01, p.45), the matrix leaves the unregistered case to "[Per jurisdiction rule:
      tax invoice or non-tax invoice]" (S1-2.4.2-c05, p.46), and a tax invoice carries the "Supplier name,
      address and tax registration number" (S1-2.4.3, p.46). Read literally, the test forbids what the
      matrix may require. Readings: the customer's own number only; or any number "where its inclusion is
      not permitted", as the non-tax column of 2.4.3 says. Deciding role: tax-specialist.
    citation: >-
      "An unregistered customer cannot be issued a document carrying a tax registration reference."
      (SRC-001 p.48, §2.4.8, 2); SRC-001 pp.45 and 46 as quoted
  - severity: non-blocking
    text: >-
      [New, hard close with an unapproved bank reconciliation] Ambiguity of the same family as claim 2. "A
      period cannot be hard-closed while a bank reconciliation for that period is unapproved or shows an
      unexplained difference." (S1-2.6.6-c21, p.62) has no exception route, but "A period cannot be
      hard-closed until every in-scope reconciliation is approved, or an exception is formally accepted
      by [role] with a reason recorded." (S1-2.12.3-c06, p.101), and bank and cash are in that scope
      (S1-2.12.1-c07, p.101). Deciding role: qualified-accountant.
    citation: >-
      SRC-001 p.62, §2.6.6, 4 and p.101, §2.12.3, 6 as quoted; "Bank and cash Approved bank reconciliation
      and cash count for the period" (SRC-001 p.101, §2.12.1)
  - severity: non-blocking
    text: >-
      [New, auditor access to individual pay] Ambiguity. The auditor may "Read every module and export
      any report" (S1-2.1.2-c27, p.9) with "access to every module, every attachment and every audit log
      entry" (S1-2.11.6-c01, p.100), but "Payroll amounts are visible only to named payroll users and
      [role]" (S1-2.10.14-c01, p.98). Unless that [role] (workbook value 156) includes the auditor, the
      two conflict. Deciding role: product-owner, with the security owner advising, together with value
      156.
    citation: >-
      SRC-001 pp.9, 98 and 100 as quoted; docs/requirements/bracketed-values.yaml@6eb263a value 156
  - severity: non-blocking
    text: >-
      [New, correcting entries of a closed period] Ambiguity. Corrections are "dated in the current open
      period" (S1-2.2.6-c12, p.29), and an "Entry in a closed period" is corrected by a "Dated adjustment
      journal in the current open period" (S1-2.2.6-c16, p.29), yet "An authorised finance administrator
      may post an exceptional journal into a hard-closed period through an override route"
      (S1-2.2.8-c30, p.33). Unstated whether the override may correct an entry of that period or serves
      only other exceptional entries. Deciding role: qualified-accountant.
    citation: >-
      SRC-001 p.29, §2.2.6 and p.33, §2.2.8 Exceptional posting to a closed period, 1, as quoted
  - severity: non-blocking
    text: >-
      [New, customer tax registration status] Ambiguity. The customer master holds a mandatory "Tax
      registration status ... Registered or not registered; drives the document type in 2.4"
      (S1-2.3.1-c05, p.36) and says of the number "the presence of a number is what marks the customer
      registered" (S1-2.3.1-c06, p.36). That gives two sources of truth for the attribute that drives tax
      determination, and no rule for when they disagree (for example, registered with no number yet
      issued). Deciding role: tax-specialist.
    citation: >-
      "the presence of a number is what marks the customer registered" (SRC-001 p.36, §2.3.1)
created_at: "2026-10-21"
---

# Review of the SRC-001 clause index and bracketed-value workbook at 6eb263a

Independent E4 review for WF-01M5D0SE8MMS39CTPTXH8ME1HT step 2 (L1 discovery). The subjects are
`docs/requirements/clause-index.yaml` and `docs/requirements/bracketed-values.yaml` at commit
`6eb263a586a8dade8bae0ee61f03486188b489fa`. HEAD was that commit and the working tree was clean, so the
files I read are the committed ones.

**Decision.** The index is accurate. I found no invented clause or value, no missed obligation and no
systematic error that would call for a re-run.

- **Index.** The one boundary error is local: the two-column mandatory-content list in 2.4.3 is split
  by printed line, which cuts two non-tax-invoice items across clauses. The other index findings concern
  how `subheading` and item numbers may be read, not where clauses start and end.
- **Workbook.** It copies only what the brackets say. Its owner assignments are defensible one by one
  but split two classes inconsistently.
- **Claimed contradictions.** Of the eight, two are genuine (1, 2), three are ambiguities that
  reconcile (3, 5, 7), two are not contradictions (4, 6), and the extraction gaps are confirmed (8).
- **Open questions.** All four are confirmed, three with additions.
- **New.** I found eight further conflicts or gaps.

**Verdict: non-blocking-findings.** Neither escalation condition in the brief is met. The decisions in
sections D to F belong to the roles named there; this review decides none of them.

## Method and limits

- I read the extraction from p.4 to p.121 (lines 178 to 5081) and all 2,438 index entries in document
  order. For each table, list and paragraph I checked the line range, the kind and the subheading
  against the text. Section B names the 77 clauses I record as the sample and the six sub-sections I
  checked item by item.
- I counted kinds with Grep over the index: `kind: acceptance` 153, `kind: entry` 118, `kind: other` 32.
  These match my count from the extraction:
  - 16 "Acceptance:" statements, plus 137 numbered tests in the 15 "Acceptance tests" sub-sections;
  - 111 rows in the nine tables headed "Entry the system auto-posts", plus the 7 rows of the 2.14.4
    intercompany table.
- **No PDF page was checked.** The Read tool cannot render the PDF here: it answers "pdftoppm is not
  installed". Every statement below about the PDF's layout is a reconstruction from pdfplumber's line
  order, not an observation of the page. pdfplumber writes one visual line per extraction line, words
  left to right, so a column that wraps differently shows up as text from two columns on one line. So
  the brief's request to check at least four interleaved tables against the PDF is not met. I checked
  all ten by reconstruction instead. A person or the orchestrator should compare p.46 and p.62 first,
  then pp.13-14, 16-17, 32, 68, 92-94, 96, 109 and 115.
- My shell profile runs no ad hoc scripts, so the clause checks are by reading and the counts by Grep.
- `created_at` is the session date. The profile cannot read a clock, so the UTC time was not observed.
  This record's ID decodes to 2026-10-20T18:50:43Z, three seconds after the reviewed commit, so the
  review was written after that.

## A. The steward's assumptions

1. **Section "0" for the unnumbered overview: accepted.** The heading is "i TIQACC system overview"
   (p.4). The clause pattern in `tools/governance/common.py` is `S1-\d+(?:\.\d+)*-c\d{2,3}`, so a digit
   is needed. "0" sorts first and collides with no numbered section, and the index rules state the
   mapping.
2. **The `subheading` field: accepted, with its justification corrected.** The field helps readers,
   but:
   - item numbers also restart after a table within one sub-heading (2.6.5, 2.6.6, 2.7.6), so section,
     subheading and item number is not a unique citation; cite by clause ID;
   - the field is positional and in places misleading;
   - run-in headings are used as sub-headings, though the rules do not say so.
3. **Kinds: accepted.**
   - *`acceptance`* for the numbered tests under "Acceptance tests" matches SRC-001's own convention:
     "The tests at the end of each module are the basis on which that module is accepted" (S1-1-c07,
     p.6). The counts are verified.
   - *`entry`* only for "Entry the system auto-posts" tables plus 2.14.4: verified, 118 rows. The 2.14.4
     rows are Dr/Cr entries that the system raises in both entities: "the system auto-creates the
     matching entry in the counterparty entity" (S1-2.14.4-c03, p.109). Tables that describe posting
     effects without Dr/Cr rightly stay `table-row`: S1-0-c07 to c11, and the 2.3.2 and 2.5.4 tables.
   - *One `other` per figure*: true for figures. But bands printed inside a figure are separate `other`
     clauses (S1-0-c05, S1-0-c06, S1-2.1.7-c02), and several `other` clauses carry obligations.
4. **Joined and whole-row anchors: accepted.** I found exactly eight joined anchors:
   - S1-0-c04, S1-1-c15, S1-2.2.3-c15, S1-2.2.4-c02;
   - S1-2.4.4-c04, S1-2.5.6-c02, S1-2.6.3-c01, S1-2.9.12-c01.

   Each is a figure whose first line has fewer than six tokens. Short rows use the whole row, as the
   rules say; S1-2.1.8-c54 ("French German Spanish") is an example. The orchestrator's script verified
   every anchor against its lines.
5. **`spec_value` as written for patterns, null for placeholders: accepted, with one exception.** The
   rule is applied consistently: I counted the same 64 non-null values, and each equals its bracket's
   content. The exception is value 160, which copies "7" although its own clause calls 7 "a placeholder
   to be confirmed".
6. **Defaulted owners: accepted for each value.** All twelve fall under "Requirement scope and
   priority" (product-owner) in the authority matrix, and each names the role that advises:
   - 31, a chart-hygiene threshold;
   - 32 to 37, code formats;
   - 115, a payment-fraud control;
   - 129, an internal review threshold, not a statutory value;
   - 156, a confidentiality role;
   - 159 and 162, control thresholds.

   Two inconsistencies across classes are reported as a finding: 25-26 against 32-37, and 56 against
   31, 159 and 162. Value 156 also bears on the auditor-access finding.
7. **Values 1 to 3: accepted.** They are the convention's own examples: "a role such as [role], a period
   such as [7] years, a threshold such as [30] days" (S1-1-c03, p.6). Listing them makes 181 − 3 = 178
   reconcile with Q-004. The totals should not count them as values to confirm.

## B. Sample review of the index

**Named sample, 77 clauses**, each checked for boundary, kind and subheading:

| Section | Clauses |
| --- | --- |
| 0 | S1-0-c01, c04, c07, c13, c18, c32 |
| 1 | S1-1-c01, c03, c11, c15, c16 |
| 2 | S1-2-c02 |
| 2.1 | S1-2.1.2-c17, c26, c28; S1-2.1.3-c04; S1-2.1.6-c12, c14; S1-2.1.7-c14, c15, c73, c74; S1-2.1.10-c18; S1-2.1.11-c02 |
| 2.2 | S1-2.2.1-c14; S1-2.2.2-c13; S1-2.2.3-c15; S1-2.2.5-c05; S1-2.2.6-c10, c14; S1-2.2.7-c18, c24; S1-2.2.8-c07, c12; S1-2.2.9-c31; S1-2.2.11-c04 |
| 2.3 | S1-2.3.1-c07; S1-2.3.2-c04; S1-2.3.7-c08; S1-2.3.12-c01; S1-2.3.17-c11 |
| 2.4 | S1-2.4.1-c03; S1-2.4.2-c05; S1-2.4.3-c04, c05, c06; S1-2.4.4-c02; S1-2.4.5-c14 |
| 2.5 | S1-2.5.5-c03; S1-2.5.6-c07; S1-2.5.13-c08 |
| 2.6 | S1-2.6.3-c15; S1-2.6.6-c18; S1-2.6.11-c10; S1-2.6.17-c10 |
| 2.7 | S1-2.7-c02; S1-2.7.5-c02; S1-2.7.6-c07 |
| 2.8 | S1-2.8.3-c13, c27; S1-2.8.13-c06 |
| 2.9 | S1-2.9.12-c01, c03 |
| 2.10 | S1-2.10.4-c03; S1-2.10.6-c03; S1-2.10.11-c04 |
| 2.11 to 2.16 | S1-2.11.4-c05; S1-2.12.3-c04; S1-2.12.5-c03; S1-2.13.1-c07; S1-2.14.2-c10; S1-2.14.4-c09; S1-2.15.4-c03; S1-2.15.8-c18; S1-2.16.1-c05 |
| 3 | S1-3-c02, c04 |

Results:

- **Wrong boundary:** S1-2.4.3-c04, c05 and c06.
- **Subheading uncertain:** S1-2.6.6-c18.
- **Subheading positional rather than descriptive:** S1-2.2.7-c24.
- **All others correct.**

**Sub-sections checked end to end**, item by item (158 clauses):

- **Table-heavy, 2.1.7 (S1-2.1.7-c01 to c84, pp.13-17): all correct.** It contains:
  - eight paragraphs and two figure clauses;
  - the standalone-deployment table (c13 to c24, interleaved lines 574-605);
  - the module catalogue (c32 to c52);
  - the entity-level table (c60 to c67);
  - the business-profile table (c70 to c76, interleaved lines 699-723);
  - five numbered lists and the acceptance statement (c84).
- **Table-heavy, 2.4.3 (S1-2.4.3-c01 to c09, p.46): the boundary error in finding 1.**
- **Accounting entries, 2.5.13 (S1-2.5.13-c01 to c21, p.55): all correct.** There are 18 entry rows
  (lines 2334-2355) and 3 numbered items. The 2.14.4 intercompany table (S1-2.14.4-c01 to c15, p.109) is
  also correct.
- **Acceptance tests, 2.6.17 (S1-2.6.17-c01 to c14, p.67) and 2.7.11 (S1-2.7.11-c01 to c15, p.75): all
  correct.**

**Completeness.** By reading, I found no obligation outside a clause. Every line from the overview
heading (179) to the last annexure line (5080) lies inside a clause, except headings, table header rows,
page markers and separators. Sections 2.1, 2.2 and 2.16 carry no text of their own, as the rules say.
Cover-page text (p.1) is a title and tagline only.

**Interleaved tables, by reconstruction.** Nine split correctly:

- 574-605 and 699-723 (2.1.7);
- 1358-1374 (2.2.8);
- 2857-2866 (2.7);
- 3911-3922 and 3966-3984 (2.10.4, 2.10.6);
- 4070-4078 (2.10.11) and 4869-4878 (2.15.4), which are row-aligned two-column grids;
- 4601-4612 (2.14.4).

1967-1980 (2.4.3) is not row-aligned and is split wrongly.

## C. Bracketed-value workbook

I read all 178 entries. For 45 of them I checked owner, `needed_for` and `spec_value` against the clause
text: values 1-3, 9, 10, 11, 14, 15, 17, 20, 25, 26, 31-37, 39, 45, 47, 56, 62-64, 77, 79, 88, 105,
115, 127, 129, 139, 143, 156, 157, 159, 160, 162, 170 and 175-178. This includes every defaulted owner.

- **No value of the steward's invention.** Every non-null `spec_value` equals the content of its
  bracket.
- **Totals reconcile.** I re-counted owners (130, 30, 8, 8, 2), the 64 non-null values and the 55
  role-kind values.
- **`needed_for`.** Each sampled entry describes its clause correctly. Its cross-references (Q-001,
  Q-003, Q-005, Q-006, the conflicting clauses) are accurate.
- **Findings:** the owner splits, the service-level owners, value 160 and the count of values to
  confirm, and the two missing-input additions.

## D. The steward's claimed contradictions

| # | Claim | Classification | Deciding role | Recommended |
| --- | --- | --- | --- | --- |
| 1 | Dimension changes after approval | Genuine contradiction (dimensions only) | qualified-accountant | Linked reclassification entry; c10's lock kept |
| 2 | Suspense at close | Genuine contradiction | qualified-accountant | 2.6.11-c10 governs |
| 3 | External payroll | Ambiguity, reconcilable | product-owner | 2.10 constrains the native module; 2.1.6 serves non-activating entities |
| 4 | Invoice series reset | Not a contradiction; residual ambiguity | tax-specialist | Annual restart as the per-country default |
| 5 | Reconciliation self-review | Ambiguity, reconcilable in the main | qualified-accountant | One releasable second step |
| 6 | Cross-reference "under 2.10" | Not a contradiction: cross-reference error | product-owner (editorial) | Read as 2.12 |
| 7 | Depreciation example | Ambiguity (day count unstated) | qualified-accountant | State the convention; fix rule or figures |
| 8 | Extraction gaps | Confirmed; nine tables right, one wrong | None: evidence | Read pp.46, 62 and 68 |

The quotes, readings and consequences are in the findings.

## E. The steward's open questions

| Question | Result | Owner |
| --- | --- | --- |
| Vendor-addressed clauses | Confirmed. Add S1-2.1.7-c11, and give an internal answer to S1-2.16.1-c06 and S1-2.16.3-c01 to c04 | product-owner; security-owner and tech-lead for S1-2.1.3-c03 and c04; residency-law owner to settle |
| Support SLA | Confirmed: none in the repository | product-owner, tech-lead advising |
| Retention per country, entity policy | Confirmed. SRC-001 has two retention models | tax-specialist (statutory periods); product-owner (default policy, one model) |
| Statutory forms, e-filing formats, prescribed wording | Confirmed. Needed per country before that country's acceptance | tax-specialist |

## F. Further conflicts and gaps

| Topic | Classification | Deciding role |
| --- | --- | --- |
| Standalone credit and debit notes (S1-2.3.3-c10 against S1-2.4.6-c03) | Genuine contradiction | tax-specialist |
| Cancelling an issued invoice (S1-2.4.6-c02; no entry in 2.3.12) | Requirement gap and ambiguity | tax-specialist, qualified-accountant |
| Re-running posted depreciation (S1-2.2.6-c21 against S1-2.8.5-c09) | Genuine contradiction, reconcilable by scope | qualified-accountant |
| Tax registration reference for unregistered customers (S1-2.4.8-c02) | Ambiguity in an acceptance test | tax-specialist |
| Hard close with an unapproved bank reconciliation (S1-2.6.6-c21 against S1-2.12.3-c06) | Ambiguity | qualified-accountant |
| Auditor access to individual pay (S1-2.1.2-c27 against S1-2.10.14-c01) | Ambiguity | product-owner, security-owner advising |
| Correcting entries of a closed period (S1-2.2.6-c12 and c16 against S1-2.2.8-c30) | Ambiguity | qualified-accountant |
| Customer registration status against number (S1-2.3.1-c05, c06) | Ambiguity | tax-specialist |
| Chart-of-accounts naming standard (S1-2.2.1-c05, S1-2.2.2-c08) | Missing input | qualified-accountant |
| Budgets cited to 2.2.3 (S1-2.13.1-c14, S1-2.1.7-c46) | Cross-reference error | product-owner (editorial) |

## G. Severity and verdict

All 28 findings are non-blocking:

- **Index (findings 1 to 4).** Finding 1 is local: it stops requirements from citing S1-2.4.3-c04 to
  c06 until it is fixed, and blocks nothing else. Findings 2 to 4 are about reading the index, and the
  clause IDs stay unique and correct.
- **Workbook (findings 5 to 8).** These concern owner consistency and presentation, plus two missing
  inputs. No value was invented.
- **SRC-001 (findings 9 to 28).** These classify SRC-001's own conflicts and gaps for their owners, so
  that the orchestrator can turn the confirmed ones into question records.

**Verdict: non-blocking-findings.** Neither escalation condition in the brief is met: the index is not
systematically wrong, and nothing was invented. The PDF comparison is still owed, by a person or by the
orchestrator.

## Verification (observed)

- `python tools/governance/check.py` before writing this record: `check: 0 error(s), 0 warning(s)`. The
  result after writing it is in the handoff report.
- `git rev-parse 6eb263a`: `6eb263a586a8dade8bae0ee61f03486188b489fa`. `git status --short`: empty.
  `git diff --stat 6eb263a HEAD`: empty.
- Grep over the index: `kind: acceptance` 153, `kind: entry` 118, `kind: other` 32 occurrences.
- Grep over the extraction:
  - "Entry the system auto-posts" heads nine tables;
  - "Acceptance:" opens sixteen lines;
  - fifteen "Acceptance tests" headings.
- Grep for "SLA" or "service level" (case-insensitive) over the repository: three files (the
  extraction, the index and the workbook).
- Not run: any PDF page rendering. The tool is unavailable here.

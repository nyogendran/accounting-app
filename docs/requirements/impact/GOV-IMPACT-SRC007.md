---
id: GOV-IMPACT-SRC007
type: governance
title: "Impact analysis: re-basing the requirements work from SRC-001 (V1) to SRC-007 (V2.2)"
status: Proposed
version: 1
owner: requirements-engineer
links:
  related: [SRC-001, SRC-007, SRC-008, DEC-0008, DEC-0009, BO-01, BO-02, BO-03, BO-04, BO-05, BO-06, BO-07, BO-08, Q-001, Q-002, Q-003, Q-004, Q-005, Q-006, Q-007, Q-008, Q-009, Q-010, Q-011, Q-012, Q-013, Q-014, Q-015, Q-016, Q-017, Q-018, Q-019, Q-020, Q-021, Q-022, Q-023, Q-024, Q-025, Q-026, Q-027, Q-028, Q-029, Q-030, Q-031, GOV-BRIEF-R1-SCOPE, GOV-QPACK-L1, S7-2-c02, S7-2.2.1-c06, S7-2.2.1-c52, S7-2.2.1-c55, S7-2.2.1-c56, S7-2.2.1-c57, S7-2.2.1-c58, S7-2.2.1-c59, S7-2.2.1-c60, S7-2.2.1-c61, S7-2.8.3-c01, S7-2.4.1-c08, S7-2.1.10-c36, S7-2.11.4-c05, S7-2.2.2-c61, S7-2.4.3-c71, S7-2.16.1-c36, S7-2.2.2-c48, S7-2.1.8-c36, S7-2.15.8-c22, S7-2.16.1-c17]
---

# Impact analysis: from SRC-001 (V1) to SRC-007 (V2.2)

Written by the requirements engineer for WF-01M5VHRCEQP734DHRKE29J5YET step 4. It goes to independent
assurance review and then guides the re-base. **It decides nothing.** Every accounting, tax, scope and
security point below is put to the role that owns it in `docs/governance/authority-matrix.yaml`
(v2): product owner (Shifan Cader), qualified accountant (Rifaz Hajirin), tax specialist (Shifan
Cader, for Sri Lanka and Norway), tech lead, security owner and governance owner (Yogendran).
SRC-008 content is proposed data, not approved policy; where it is quoted as settling something, the
owner who must confirm it is named. Proposed questions are labelled PQ-nn; they are not records.

Inputs read: crosswalk `docs/requirements/crosswalk-src001-to-src007.yaml` v1 (commit 7f6a7ae), the
S1 index v2 and the S7 index v1 (commit 0733090), both extractions, both SRC-008 extractions, and the
artifacts listed in section 6 at their current versions.

## 1. Summary

**What V2.2 changes.** Of SRC-001's 2,444 clauses, 2,427 survive word for word in SRC-007 (51 of them
under a new clause number), 17 change, and 307 clauses are added. Read against the text, none of the
17 is simply dropped: each of the 7 that the crosswalk calls "removed" has a successor in V2.2
(section 3.2). The additions sit in a few places and are large there:

- the general ledger set-up: a delivered standard chart, the account code as a "natural account"
  with entity and country segments around it, code clashes and alternatives, and, most important,
  **control accounts enforced at a level set per entity and control type** (Not applied, Advisory,
  Enforced) instead of always blocked (2.2.1, 2.2.2);
- journal upload with column and value mapping and a published 28-column template (2.2.4);
- numbering formats prescribed by a tax authority (2.1.10), tax and non-tax forms of every sales
  document, industry levies, the tax mechanics on the face of a document, remittance details and a
  delivered template library (2.1.7, 2.4);
- data held from go-live with no retention figure applied by the software (2.11.4, 2.16.1);
- capacity targets with a tested ceiling (2.16.1), and a new sub-section on subscription licensing
  (2.16.5).

**What it means for the work so far.** Every V1-based artifact has to be re-pointed: 1,812 S1 clause
references across them, of which 1,704 change only their prefix and page and 108 need a clause-level
decision (section 6). Five artifacts need more than re-pointing:

- **The control-account conflict behind Q-029 and D-INT-1 shrinks but does not disappear.** V2.2
  lets a single entity running sub-ledgers post a manual journal to a control account at Advisory
  level. But V2.2 also keeps the old blanket block in its attribute table, still rejects a user
  journal as a substitute for a system posting, and still requires every sub-ledger to agree to its
  control account (section 6.4).
- **The bracketed-value workbook** gains 17 values and loses 5, giving 190.
- **The release phasing** needs a mark for 2.16.5, and new marks for parts of 2.2.1, 2.2.2, 2.4.3,
  2.4.8 and 2.16.1.
- **The glossary** needs about 40 new terms, and its definition of "control account" is now wrong.
- **The questions:** Q-025 is largely answered by V2.2, Q-005 is partly answered by SRC-008, and
  Q-015, Q-016, Q-018 and Q-021 are partly answered for Sri Lanka by SRC-008. Each of these needs its
  owner's confirmation.

V2.2 also carries its own contradictions, including two printed corruptions and three wrong
cross-references (section 4). The crosswalk would mislead a mechanical re-base in one way: its 7
"removed" clauses are all changed clauses with successors (section 3.3).

## 2. Method and verification

- **Changed and removed pairs.** Each of the 10 changed and 7 removed crosswalk entries was read in
  both extractions, at the line ranges given by the two indexes.
- **New clauses.** For each new clause, the S7 index entry was read and the extraction text read in
  sequence, sub-section by sub-section.
- **Renumbered pairs.** These were found from the crosswalk with two multiline text searches: pairs
  whose last digit differs (57 pairs) and pairs whose tens digit differs (51 pairs). The union is 58
  pairs: 51 marked same and 7 marked changed. No clause number has three digits. This confirms the
  brief's "51 renumbered" among the same pairs, and adds 7 changed pairs whose number also moved.
- **Bracket tokens.** Every opening "[" in the S7 extraction was listed with its line number by a
  text search in only-matching mode, and counted by hand. There are 193, three of them broken across
  a line (lines 483, 2331 and 2360), as in S1. Leaving out the three signature names on line 5801
  leaves 190 values. Each S7 token was matched to its S1 counterpart in the workbook (v3) by clause
  and context, which gives 173 + 17 = 190, and 178 - 5 + 17 = 190 (section 6.1).
- **S1 reference counts.** These are counts of occurrences of the pattern `S1-<section>-c<nn>`,
  listed with a search in only-matching mode and counted by hand. For release-phasing.yaml the
  listing was paged and the total read from the last page (903). Shorthand continuations ("c21" after
  a full ID, "c01 to c04") are not in these counts; they were searched for separately and are listed
  where they hit a changed clause.
- **SRC-008.** The workbook was read sheet by sheet. Its arithmetic, and the arithmetic of every
  worked example in the template library, was recomputed by hand. The chart's posting rows (206),
  group rows (43) and control-flagged posting rows (68) were counted with text searches.
- **The two printed corruptions** (S7-2.1.8-c36, S7-2.15.8-c22) are cited as the orchestrator
  confirmed them on the rendered PDF, pages 19 and 130. No PDF was rendered for this analysis.

## 3. Clause changes

### 3.1 The 10 changed pairs

| S1 (page) | S7 (page) | What changed in meaning |
| --- | --- | --- |
| S1-0-c13 (p.4) | S7-0-c13 (p.4) | General ledger now covers a "Delivered standard chart of accounts or the entity's own", where V1 said "Chart of accounts". **Meaning change:** the product ships a standard chart (detailed in S7-2.2.1-c33 to c47). |
| S1-2.2.1-c15 (p.23) | S7-2.2.1-c15 (p.24) | Adds "in any configuration" and "The entity and the country are different: they are segments around the account, not dimensions inside it". **Meaning change:** introduces the entity and country segments (S7-2.2.1-c16 to c26). |
| S1-2.2.1-c16 (p.23) | S7-2.2.1-c48 (p.26) | Adds "as set out above", which points to the allocation step of S7-2.2.1-c27 ("steps of [10]"). **Editorial and renumbering**; the gap is now quantified elsewhere. |
| S1-2.2.1-c19 (p.24) | S7-2.2.1-c43 (p.26) | "The whole chart can be exported" becomes "The chart is exportable to Excel at any time"; the clause moves to the sub-heading "Starting the chart". **Editorial and renumbering.** |
| S1-2.2.1-c21 (p.24) | S7-2.2.1-c52 (p.27) | V1 blocked posting to "control accounts by manual journal". V2.2 blocks it only "where control enforcement is set to Enforced, as below". **Major meaning change**; see sections 4.1 and 6.4. |
| S1-2.2.4-c20 (p.27) | S7-2.2.4-c30 (p.34) | Validation adds dimensions checked "against the rules for that account" and "tax code valid where the account is tax bearing", and the report gives "its row number in the original file". **Meaning change:** one more validation rule and a reporting rule. |
| S1-2.2.4-c22 (p.27) | S7-2.2.4-c33 (p.34) | The uploaded batch also shows "which mapping template was used". **Small addition.** |
| S1-2.4.1-c05 (p.45) | S7-2.4.1-c06 (p.54) | V1 had one "Debit note DN-…" row. V2.2 has a tax debit note, "TDN-… carrying the tax the original charged" (S7-2.4.1-c05), and a non-tax one, "NDN-… carrying no tax line" (c06). **Meaning change.** The crosswalk pairs it with c06 only; it is a one-to-two split (section 3.3). |
| S1-2.11.4-c06 (p.100) | S7-2.11.4-c07 (p.113) | "end of its retention period without an approved disposal instruction" becomes "end of any retention period without an approved disposal instruction from the entity". **Editorial**, in the frame of the new retention model of c05 and c06. |
| S1-2.15.8-c22 (p.117) | S7-2.15.8-c22 (p.130) | "Legal entities Consolidation structure Numbering series" is printed "Legal entities 1 Numbering series". **Source error** (section 4.6). |

### 3.2 The 7 removed clauses: all have successors

| S1 (page) | Successor in S7 (page) | What changed |
| --- | --- | --- |
| S1-2.1.7-c57 (p.16) | S7-2.1.7-c57 (p.16) | The first sentence is kept ("proposes its likely tax obligations, as set out in 2.7.2"). V2.2 adds that the industry selection "activates the industry tax set for that sector in that country — the levies the sector attracts, each with its rate, its base, its order of application against the transaction tax, its account and the documents it prints on". **Meaning change (major).** |
| S1-2.1.8-c36 (p.19) | S7-2.1.8-c36 (p.19) | V1: "Customers Name and trading name, where the customer is known by more than one script". V2.2 prints "Customers 25,000". **Source error** (section 4.6). |
| S1-2.2.2-c05 (p.24) | S7-2.2.2-c05 (p.28) | "proposes the next available code within the correct range; a manual code is permitted only within that range and only to [role]" becomes "proposes the code; a code keyed by a user is accepted only within the correct range, only by [role], and only if it is free. A code already taken is refused, with alternatives offered". **Meaning change:** a free-code check, and a refusal that comes with alternatives. |
| S1-2.2.2-c26 (p.25) | S7-2.2.2-c61 (p.31) | V1's acceptance statement appears word for word as the last part of the much longer S7-2.2.2-c61, which also tests upload mapping and chart set-up (section 4.4). **Meaning change:** the clause is extended. |
| S1-2.11.4-c05 (p.100) | S7-2.11.4-c05 and c06 (p.113) | V1: retention "configurable per entity and per document type … [7] years is a placeholder". V2.2: "Data is held from the day the organisation starts on the system … no retention figure is applied by the software of its own accord" (c05), and "A statutory retention period is a floor … never a ceiling at which the system disposes" (c06). **Meaning change (major).** |
| S1-2.16.1-c02 (p.119) | S7-2.16.1-c02 (p.132) | V1: "Volume [X] transactions per month, [n] items, [n] customers, [n] employees". V2.2: "Volume The capacity targets below, sustained without degradation at the stated concurrency", with the table in c07 to c22. **Meaning change:** the values are set in V2.2 itself. |
| S1-3-c03 (p.121) | S7-3-c03 (p.137) | Annexure A adds "the subscription response required by 2.16.5", with nine items, from the basis of charge to the three-year total. **Meaning change.** |

### 3.3 Where this analysis disagrees with the crosswalk

1. **The 7 "removed" entries are changed clauses** with the successors in section 3.2. A re-base that
   follows the crosswalk literally would drop 29 references instead of re-pointing them (17 in the
   workbook, 4 in the phasing, 3 in the glossary, 1 in the actors, and 2 in each of Q-020 and Q-025;
   see section 6). **This is the escalation point in the handoff.** The tool's ratio
   threshold explains it: each of these clauses grew or was corrupted, and difflib scores it under
   0.6.
2. **S1-2.4.1-c05 maps one-to-two** (S7-2.4.1-c05 and c06). The crosswalk records only c06. A
   reference to the V1 debit note has to pick the tax or the non-tax form, or cite both.
3. **"New" therefore overstates what is new.** 9 of the 307 are successors or splits: S7-2.1.7-c57,
   S7-2.1.8-c36, S7-2.2.2-c05, S7-2.2.2-c61, S7-2.4.1-c05, S7-2.11.4-c05, S7-2.11.4-c06,
   S7-2.16.1-c02 and S7-3-c03. That leaves 298 wholly new clauses.
4. **"Same" text can carry changed meaning.** Some identical clauses now sit beside new clauses that
   change how they read:
   - S7-2.2.1-c06 (the blanket block; section 4.1);
   - S7-2.4.1-c08 (the annual restart; section 4.2);
   - the six "[7] years" clauses (section 4.3);
   - S7-2.2.2-c47 and c51 (the control flag cannot change);
   - S7-2.16.1-c01 ("[Y] concurrent users", now beside a table of concurrent users).

   The crosswalk is right to call these the same, but a re-base must not treat them as unaffected.

**Proposed:** a crosswalk version 2, or a successor block added to version 1, that records the 7
successors and the one-to-two split, so that the trace tooling and later re-bases do not repeat the
loss.

### 3.4 Renumbering

The 51 same pairs whose number changes:

- 2.1.10: S1-c32 to c38 become S7-c38 to c44 (7);
- 2.2.1: S1-c17, c18 and c20 become S7-c49, c50 and c51 (3);
- 2.2.2: S1-c07 to c25 become S7-c42 to c60 (19);
- 2.2.4: S1-c21 and c23 become S7-c32 and c34, and S1-c24 to c32 become S7-c75 to c83 (11);
- 2.4.1: S1-c06 to c10 become S7-c08 to c12 (5);
- 2.4.8: S1-c01 to c05 become S7-c15 to c19 (5);
- 2.11.4: S1-c07 becomes S7-c10 (1).

The 7 changed pairs that also move are in section 3.1. Every other pair keeps its number. Page numbers
begin to differ within 2.1.10 (S1-2.1.10-c18 is on p.21, S7-2.1.10-c18 on p.22), and by 16 pages at the end (V1 p.121, V2.2 p.137), so every page citation
needs re-paging, not only the renumbered ones.

### 3.5 The 307 new clauses, by group

| Group | New clauses | Count |
| --- | --- | --- |
| 2.1.7 levies | S7-2.1.7-c57 | 1 |
| 2.1.8 (corruption, section 4.6) | S7-2.1.8-c36 | 1 |
| 2.1.10 prescribed numbering | S7-2.1.10-c32 to c37 | 6 |
| 2.2.1 segments, delivered chart, control enforcement | S7-2.2.1-c16 to c42, c44 to c47, c53 to c68 | 47 |
| 2.2.2 code clashes | S7-2.2.2-c05, c07 to c41, c61 | 37 |
| 2.2.4 upload mapping and template columns | S7-2.2.4-c20 to c29, c31, c35 to c74 | 51 |
| 2.4.x taxes, levies, remittance, template library | S7-2.4.1-c05, c07; S7-2.4.3-c16 to c91; S7-2.4.6-c05 to c09; S7-2.4.8-c01 to c14 | 97 |
| 2.11.4 retention | S7-2.11.4-c05, c06, c08, c09 | 4 |
| 2.16.1 capacity | S7-2.16.1-c02, c07 to c40 | 35 |
| 2.16.5 licensing | S7-2.16.5-c01 to c27 | 27 |
| Section 3 | S7-3-c03 | 1 |
| **Total** | | **307** |

**2.1.7 levies (p.16).** Choosing an entity's industry now does more than propose its tax
obligations. It "activates the industry tax set for that sector in that country", and from then on
"those levies appear on every document they cover and in every return that reports them, without a
template being edited". The set is configuration, and "the entity confirms it against its own
registrations before it is used" (S7-2.1.7-c57). So the industry selection becomes a tax-relevant
setting. Which levies apply to Tiqri's Sri Lanka entity is a tax-specialist question (PQ-12).

**2.1.10 prescribed numbering (pp.22-23).** Where a tax authority prescribes how a document number is
built, the format is held "against the instrument that prescribes it … and the date it takes effect"
(c32). The elements the authority fixes are locked, and the elements it leaves to the entity stay
configurable (c33). An amendment is loaded as a new version, and both versions stay active in an
interim period (c34). An ambiguous rule is configurable, defaults to the specification, and is stored
exactly as printed (c35). "Where the authority prescribes whether a sequence continues across months
or restarts, the choice is made once per entity before the first document is issued" (c36). The
worked example `YYMMM_QQQQ_XXXXX` (c37) continues from the preceding month "unless the entity has
elected to restart monthly or annually". These clauses meet S7-2.4.1-c08 head on (section 4.2).

**2.2.1 segments, delivered chart and control enforcement (pp.25-28).**

- *Account reference.* The six-digit code is the "natural account", identical in every entity and
  "settable between four and ten" digits at implementation (c16, c17). The entity and country
  segments are presentation, composed by the system, never typed, never parsed, and switchable
  across history without changing a balance (c18 to c26).
- *Expanding the chart.* Accounts are allocated "in steps of [10]"; the system proposes the next free
  code in position; there is a spare range outside the five classes; no account is renumbered; and
  the code length is widened group-wide as one approved migration (c27 to c32).
- *Starting the chart.* A delivered standard chart, industry variants, upload of the entity's own
  chart, amending the delivered one, or copying a sister entity's (c33 to c38). The delivered chart
  is "never locked" (c39). Uploads are validated in full (c40); non-compliant charts get a proposed
  mapping, not a silent reshape (c41); the delivered chart is versioned (c42).
- *Approval.* Every change follows 2.2.2, with "no second route" (c44 to c47).
- *Control accounts.* A control account's balance is "owned by a sub-ledger"; the flag and the owning
  type are fixed attributes (c53). "What the flag causes is not fixed": it is set per entity and per
  control type (c54), at Not applied, Advisory or Enforced (c55 to c57). The delivered defaults by
  organisation shape are in c58 to c61. Activating a module proposes raising the level (c63).
  Lowering from Enforced needs approval and is reported (c64). An account keeps its reconciliation
  even when not enforced (c65). There is an exception report at Advisory (c66), flag changes go
  through approval (c67), and an acceptance test covers all of this (c68).

**2.2.2 code clashes (pp.28-31).** No two accounts share a code. The check runs when a code is keyed,
when the request is submitted and at approval (c07). A code is "taken" if it is active, blocked,
archived, deleted, pending or reserved (c08 to c13). A refusal names what holds the code, "There is no
override, for any role" (c14, c15), and comes with ranked alternatives in position (c25 to c33). The
reach of the check follows the chart the entity runs on: its own chart, so the entity alone; or a
shared group chart, so every entity on it (c16 to c19). It does not reach outside a single entity
(c20); the scope is set at entity set-up by [role] (c21); clashes are reported before an entity joins
a group chart (c22, c23). Near duplicates are caught at the duplicate check (c34 to c37). Bulk
uploads are checked row by row and accepted in full or not at all (c38 to c40). The section has its
own acceptance test (c41). Code assignment now checks that a code is free (c05). The extended
acceptance statement c61 is discussed in section 4.4.

**2.2.4 upload mapping and the template columns (pp.33-36).**

- *Mapping.* The published template is downloadable, carries the system's headings, and states the
  rule for each column (c20). Other files are mapped column by column, by header, by position or by
  a saved profile (c21, c22). Mappings are saved per source and reused (c23). Values are mapped as
  well as columns (c24). Real-world file shapes are handled: header row not first, blank rows, total
  rows, merged cells (c25). Dates and numbers are read in the format stated, never guessed (c26).
- *Preview and validation.* Debit and credit columns, or a signed amount (c27). A preview of the
  first "[20]" rows and the batch totals before anything posts (c28). An unmapped mandatory column
  stops the upload (c29). The validation report is downloadable in the uploaded format (c31). The
  same mechanism serves every bulk route (c35).
- *The template column set.* The column set is c36 to c64: 9 header columns and 19 line columns,
  with brackets "[40]" and "[2]". The column meanings are in c65 to c70. A balanced worked file
  follows (c71 to c74): 184,500.00 + 22,800.00 = 207,300.00, which is correct.
- *A rule that matters for D-INT-1.* The account code column refuses "a control account … where the
  entity enforcement level is Enforced" (c47).

**2.4.x taxes, levies, remittance and the template library (pp.54-61).**

- *Two forms of every document.* Every document "exists in a tax form and a non-tax form", chosen by
  the system, each on its own series. This extends to receipts, pro forma and self-billed documents
  (S7-2.4.1-c05, c07).
- *Industry levies (2.4.3-c16 to c25).* A levy prints above the value of supply, with its own rate
  and base. It is resolved per line from the item class, prints nothing when it does not apply, and
  may be rate-based, per unit, banded, capped or fixed, or periodic from the ledger. Each levy is
  dated, and carries its own account and return mapping. The worked example is in c25.
- *Taxes on the face of the document (c26 to c45).* "A template does not decide which taxes it
  shows". Each tax is its own line, in a configured order, naming its base. Withholding prints as a
  memorandum. There are ten tax mechanics (c34 to c43), and a new tax or a rate change is dated
  configuration (c44, c45).
- *Currency block (c46 to c50).* Rate, source and date, with the totals and tax in the functional
  currency, suppressed when the currencies match.
- *Remittance details (c51 to c71).* Drawn from the bank accounts in 2.6.1, selected by currency,
  country and customer, suppressed on delivery notes and receipts. Changing them needs a second
  person and is reported "because an invoice carrying altered remittance details is a known route
  for fraud" (c68).
- *Delivered template library (c72 to c78).* "a statutory template for each country the group
  operates in", plus non-tax, note, receipt, delivery, pro forma, statement and cross-border
  templates.
- *Design (c79 to c87).* A designer and template upload, templates held per entity, country, document
  type, branch and customer, and fixed statutory elements.
- *Statutory change (c88 to c91).* Versioned reissue, with derived templates flagged for
  re-validation.
- *Notes (S7-2.4.6-c05 to c09).* Tax and non-tax forms; every tax reversed at the original rate and
  base; proportionate partial adjustment; the tax effect falls in the period of the note; foreign
  notes carry the original rate.
- *Acceptance (S7-2.4.8-c01 to c14).* New tests for the template library, the remittance block,
  levies, currency and notes. The five V1 tests become c15 to c19.

**2.11.4 retention (p.113).** Data is held from the first day, "no retention figure is applied by the
software of its own accord" (c05). A statutory period is a floor, "never a ceiling" (c06). Closed
periods may move to a slower storage tier but stay queryable "from the same screens, with no restore
request" (c08). Erasure required by a privacy law is "the one exception", recorded, leaving the
accounting record intact (c09).

**2.16.1 capacity (pp.132-134).** The volume row now points to a capacity table (c02), which gives
single-entity, multinational and tested-ceiling figures for 15 measures (c08 to c22). The system "is
built against the figures below and proved against the ceiling in load testing before acceptance"
(c07). No figure is a constant in the source; limits are raised without a release, "set per tenant
and per entity", and warned at "[80]%" (c23 to c28), with an acceptance test (c29). "Every period
since the organisation started on the system remains online" (c30 to c32). The ceiling is not a
licence cap; it is re-proved at a higher level when needed, and "No limit … may be implemented in a
way that cannot be raised" (c33 to c39), with an acceptance test (c40).

**2.16.5 licensing (pp.135-136).** The charge follows the shape of the organisation: per user for a
single entity, user packs across the group otherwise, and "A group accountant with access to forty
entities is one user" (c02 to c07). There are five licence types: full, limited, read-only and
auditor, system or integration account, and vendor support account (c08 to c12). Licences are named
unless the vendor states otherwise; freed on deactivation; consumption shown live, with "active in
the last [90] days"; dormant accounts reported (c13 to c17). A licence limit "may never block a
period close, a statutory return, a tax filing, an audit access request or a data export", nor
degrade or withhold data (c18 to c22). Licensing is separate from capacity; any meter is named in
Annexure A or "is not payable"; modules are licensed per 2.1.7 (c23 to c26). There is an acceptance
test (c27). Much of the sub-section is addressed to "the vendor" (c09, c10, c13, c20, c24), which for
Tiqri's own product is Q-023 territory.

**Section 3 (p.137).** Annexure A now also asks for "the subscription response required by 2.16.5"
(S7-3-c03). Annexure B is unchanged (S7-3-c04), and the sign-off is still unsigned (S7-3-c02).

## 4. Contradictions and source errors inside V2.2

Each item is for its owner to settle. None is resolved here (DEC-0008, condition 4).

### 4.1 Control accounts: the attribute table against the enforcement levels

- **One side.** "Control account flag Yes or no Receivables, payables, inventory, payroll, fixed
  asset, tax and bank control accounts accept sub-ledger postings only; manual journals to them are
  blocked" (S7-2.2.1-c06, p.24, unchanged from V1).
- **Other side.**
  - "control accounts by manual journal where control enforcement is set to Enforced" (S7-2.2.1-c52,
    p.27);
  - "What the flag causes is not fixed" (c54);
  - "Not applied … Any account accepts a manual journal" (c55);
  - "Advisory A manual journal to a control account is allowed, requires a reason" (c56);
  - the delivered defaults (c58 to c61);
  - the acceptance test, "an entity set to Not applied posts a manual journal to receivables control
    without obstruction" (c68, p.28).
- **Verified:** the c06 wording is unchanged in V2.2 and sits on p.24, three pages before the levels.

Two more clauses stand with c06 against Not applied and Advisory:

- "The receivables control account equals the customer ledger continuously, and no balance in it
  exists without a document behind it" (S7-2.3-c01, p.45).
- "These agreements are auto-computed by the system continuously and must be nil" (S7-2.12.1-c01,
  p.114), which the 2.2.4 acceptance repeats: "the sum of every sub-ledger agrees to its control
  account continuously, per 2.12.1" (S7-2.2.4-c83, p.37).

A manual journal at Advisory, which V2.2 permits and tests, makes the receivables agreement non-nil.
V2.2 half answers this by keeping the account on the reconciliation schedule, "The balance still
needs proving" (c65), but 2.12.1 still says "must be nil". **Owner:** the product owner, with the
qualified accountant for the accounting effect (PQ-01, PQ-18).

### 4.2 Sales-document numbering: 2.4.1 against 2.1.10

- **One side.**
  - "Each series is separate, sequential and gapless, restarting at the beginning of each financial
    year" (S7-2.4.1-c08, p.54, unchanged from V1);
  - the series formats `TI-[location]-[YY]-[nnnnnn]` and the other five (S7-2.4.1-c01 to c06);
  - the worked example "No. TI-C1-26-000418" (S7-2.4.4-c01, p.59).
- **Other side.**
  - "Where the authority prescribes whether a sequence continues across months or restarts, the
    choice is made once per entity before the first document is issued" (S7-2.1.10-c36, p.22);
  - the example `YYMMM_QQQQ_XXXXX`, "continuing from the last number issued in the preceding month
    unless the entity has elected to restart monthly or annually" (S7-2.1.10-c37, p.23).
- **Partial reconciliation.** "The formats shown above are illustrative" (S7-2.4.1-c11). That covers
  the format, but not c08's restart rule, which is not marked illustrative.
- **A third problem.** The configurable "Reset rule Never, annually at the financial year end, or at
  the start of each period" (S7-2.1.10-c18, p.22) has no calendar-year restart. The `YY` of the
  prescribed example is the calendar year: "two digits of the calendar year of issue" (c37), and
  SRC-008 says "not the financial year" ('SL tax invoice field map' r42).

**Owner:** the tax specialist for what Sri Lanka and Norway prescribe; the product owner for which
clause governs (Q-015, PQ-03, PQ-17).

### 4.3 The "[7] years" clauses against "no retention figure"

Six clauses still say "retained for [7] years":

- the audit log (S7-2.1.4-c08, p.10);
- transaction history (S7-2.2.6-c28, p.39);
- fixed asset records (S7-2.8.15-c06, p.96);
- payroll history (S7-2.10.14-c07, p.111);
- reconciliations (S7-2.12.3-c07, p.114);
- group records (S7-2.14.13-c07, p.126).

Against them:

- "Data is held from the day the organisation starts on the system, not for a number of years …
  no retention figure is applied by the software of its own accord" (S7-2.11.4-c05, p.113);
- "never a ceiling at which the system disposes" (c06);
- "There is no year count at which data ages out" (S7-2.16.1-c30, p.133).

Read as a floor, "[7] years" fits; read as a period of keeping, it does not. The convention clause
still uses "[7] years" as its example of a bracket (S7-1-c03, p.6). **Owner:** the product owner for
the model (Q-025), with the tax specialist for statutory floors (Q-020).

### 4.4 The 2.2.2 acceptance statement tests 2.2.4 and 2.2.1

S7-2.2.2-c61 (p.31) is printed at the end of 2.2.2 under "Ongoing hygiene reports". It opens with
seven tests of journal-file mapping (2.2.4): "a journal file whose headings differ entirely from the
template is mapped on screen … the validation report returns in the same format carrying the original
row numbers". It then tests chart behaviour (2.2.1): the next free code in a gap; "switching the
entity and country segments on presents every account as LK-01-122010"; adopting the delivered chart;
importing and validating an own chart; "an uploaded chart carrying branch codes inside the account
code is reported with a proposed mapping". Only then does it reach V1's 2.2.2 acceptance text. The
splice is visible in "…without any report being edited; switching…", where a sentence ends with ";"
and runs straight on.

2.2.4's own acceptance (S7-2.2.4-c83, p.37) is unchanged from V1 and tests no mapping. 2.2.1's own
acceptance (S7-2.2.1-c68) tests only the enforcement levels. 2.2.2 has a second acceptance statement
for code clashes (S7-2.2.2-c41, p.30). **Owner:** the product owner, to confirm which module each
test accepts under the acceptance protocol (S7-2.16.4-c01). This is editorial; no accounting decision
is needed (PQ-06).

### 4.5 Cross-reference errors

| Clause (page) | Printed reference | Points to | Where the rule is |
| --- | --- | --- | --- |
| S7-2.4.3-c71 (p.58) | "follow the same controls in 2.5.3" | 2.5.3 Supplier invoice capture by email | 2.5.1: "Bank account details … Change requires maker–checker plus a call-back confirmation flag; every change is reported to [role]" (S7-2.5.1-c08, p.62) and S7-2.5.1-c18 |
| S7-2.16.1-c36 (p.134) | "near-line storage that stays queryable under 2.11.6" | 2.11.6 Audit access and pack | S7-2.11.4-c08 (p.113): closed periods on a slower tier "stay queryable" |
| S7-2.2.2-c48 (p.30) | "The person responsible for reconciling it under 2.10" | 2.10 Payroll | 2.12: "Every balance sheet account is assigned an owner" (S7-2.12.3-c01); carried from V1 (Q-027) |
| S7-2.13.1-c14, S7-2.1.7-c46 | budgets cited to "2.2.3" | 2.2.3 Dimension model | 2.2.10 and 2.14.11; carried from V1 (Q-027) |

Lower confidence: S7-2.16.5-c22 (p.136) puts data export "under 2.16.2", which is data migration into
the system, not export out of it. **Owner:** the product owner (Q-027).

### 4.6 Two printed corruptions

- **S7-2.1.8-c36 (p.19).** The "Master data in more than one language" table prints "Customers
  25,000" where V1 had "Customers Name and trading name, where the customer is known by more than one
  script" (S1-2.1.8-c36, p.19).
- **S7-2.15.8-c22 (p.130).** The configuration-change alert grid prints "Legal entities 1 Numbering
  series" where V1 had "Legal entities Consolidation structure Numbering series" (S1-2.15.8-c22,
  p.117). "Consolidation structure" now appears nowhere in V2.2. Group-structure changes are still
  covered by "Legal entities and group structure … consolidation method changed, per 2.14.1" (2.15.8,
  extraction line 5520), so most of the lost meaning survives elsewhere.

Both were confirmed on the rendered PDF by the orchestrator. **Labelled hypothesis:** both look like
values from a capacity table replaced into the wrong rows. The SRC-008 single-entity column gives
"Customers | 25,000" and "Legal entities | 1" ('Volume and capacity' r27, r22), and V2.2's own
capacity rows begin "Customers 5,000 …" and "Legal entities 1 …" (S7-2.16.1-c17, c14). If so, the
edit meant for 2.16.1-c17 (25,000 single-entity customers) may never have reached it (section 5,
item 1). **Owner:** the product owner, to confirm V1's wording for both rows and the intended 2.16.1
figure (PQ-05, PQ-08).

### 4.7 Smaller tensions noted for the owners

- **Fixed decimals against currency precision.** "Decimal, [2] places" in the upload template
  (S7-2.2.4-c49, c50, c58) does not fit "minor-unit precision per 2.2.9" (2.1.8, p.19) for
  currencies with no or three decimal places. Owner: qualified accountant with the tech lead
  (PQ-10).
- **Widening the code.** Widening the code length "re-pad[s]" every code (S7-2.2.1-c32), against
  "The account code itself can never be changed" (S7-2.2.2-c50) and "No account is renumbered"
  (S7-2.2.1-c31). V2.2 mitigates this with an alias. Owner: tech lead with the qualified
  accountant.
- **Lowering enforcement.** S7-2.2.1-c64 reports every lowering from Enforced, while the
  multinational row of the defaults says "lowering it is reported" (c61), which suggests the report
  is particular to that row. Owner: product owner.

## 5. SRC-008 compared with SRC-007

SRC-008 states that "Where this workbook and the requirement specification differ, the specification
governs. This workbook supplies data; it does not vary a requirement" ('Read me' r16). Its author is
the qualified accountant ('Read me' r4). Where it proposes accounting content, his confirmation is
confirmation by the author. For Tier-1 policy, both Rifaz Hajirin and Shifan Cader are needed
(authority matrix, conditions).

**Where it differs from SRC-007 (SRC-007 governs).**

1. **Single-entity customers.** 5,000 (S7-2.16.1-c17) against 25,000 ('Volume and capacity' r27).
   All the other single-entity, multinational and ceiling figures for the 15 measures agree with
   S7-2.16.1-c08 to c22. Owner: product owner, with the tech lead (PQ-08).
2. **Reserved endings.**
   - 'Code structure' r10 says "x9xx accounts carry provisions, allowances, accumulated depreciation
     and impairment".
   - But accumulated depreciation and amortisation are coded 111210 to 111280, 112210, 112220 and
     113210 ('Chart of accounts' r17 to r23, r30, r31, r37): 10 accounts outside the rule.
   - Provisions 213010, 213020 and 224050 (r88, r89, r116) are also outside it.
   - The x9xx endings are also used for "Sundry income" 420900 and "Sundry expenses" 540900 (r154,
     r216), which are neither contra nor provision accounts.
   - Impairment (111900, 112900) and allowances (121900, 122900) follow the rule.

   Owner: qualified accountant.
3. **Countries.** The template library delivers Sri Lanka, "EU member states, UK", "UAE, Saudi
   Arabia, GCC", India and the United States ('Invoice template library' r6 to r20; library p.1).
   There is no Norway. Q-003 (v2) already records this, and that "All countries defined in the
   template" was the governance owner's answer of 2026-10-26. Owners as Q-003: product owner, tax
   specialist, governance owner.
4. **The levy worked example.** V2.2's arithmetic is correct: 822,000 × 2.5% = 20,550; 822,000 +
   20,550 = 842,550; 842,550 × 18% = 151,659; 842,550 + 151,659 = 994,209 (S7-2.4.3-c25, p.56).
   SRC-008's SL-VAT-01 and SL-VAT-02 use the same figures and name the levy "Social Security
   Contribution Levy @ 2.5%" (library pp.2-3): correct. SL-VAT-03 is correct to the cent (p.4):
   - lines 6,000.00 + 2,520.00 + 2,400.00 = 10,920.00;
   - levy 2.5% of 8,520.00 = 213.00;
   - VAT 18% of 11,133.00 = 2,003.94;
   - total with stamp duty 1.60 = 13,138.54;
   - at 302.45: 3,973,751.42, VAT 606,091.65 and levy 64,421.85.

   SL-TCN-01 (32,000 + 800 + 5,904 = 38,704) and SL-TDN-01 (84,000 + 2,100 + 15,498 = 101,598) are
   correct. **Inconsistent:** RCT-01 and SOA-01 (pp.14, 16) show tax invoice 26JUL_BR03_00412 at
   969,960.00 and a credit note of 37,760.00. Those are 822,000 × 1.18 and 32,000 × 1.18, that is,
   without the levy. SL-VAT-01 shows that invoice at 994,209.00, and SL-TCN-01 shows the note as
   TCN-2026-07-0033 at 38,704.00, while the receipt calls it CN-2026-07-0033. SOA-01's ageing puts the
   opening balance (412,800.00) as "Not yet due" and the 15 July invoice residue (37,760.00) in
   "1–30 days", which looks reversed for 30-day terms at 31 July. The receipt and statement totals
   are internally consistent (932,200 - 37,760 = 894,440; 412,800 + 969,960 - 37,760 - 894,440 =
   450,560). Owner: qualified accountant, before any of these are used as test data (PQ-22).
5. **Approval to add or amend an account.** 'Setup options' r34 and r35 make it "Optional" for
   profile A (single entity, ledger only). V2.2 requires the 2.2.2 route with "no second route by
   which an account can appear" (S7-2.2.1-c44) and maker–checker (S7-2.2.2-c04). Owner: product
   owner with the qualified accountant (PQ-14).
6. **Lowering an enforcement level.** 'Setup options' r16 gives "No" (A), "Approval" (B, C) and
   "Approval and reported" (D). V2.2 requires approval, a reason, an effective date and a report for
   every lowering from Enforced (S7-2.2.1-c64). Owner: product owner.
7. **Profile D wording.** SRC-008 has "Multinational — several countries, several currencies, high
   transaction volume" ('Setup options' r9: all three). V2.2 has "Multinational, multi-currency or
   high volume" (S7-2.2.1-c61: any one). This matters for the first entity (section 6.4).
8. **Flags.** SRC-008 says "An entity may add or remove the flag on an account within those types"
   ('Code structure' r62). V2.2: "Class, group and control-account status cannot be changed once
   transactions exist" (S7-2.2.2-c51) and "Once set, cannot be changed while the account carries a
   balance" (c47).
9. **Location dimension.** The chart blocks location on most balance-sheet accounts, for example
   trade receivables 122010 (r57; 'Code structure' r30). V2.2 makes location mandatory on "All
   transactions" (S7-2.2.3-c06, p.31). Owner: qualified accountant (PQ-15).
10. **A tax that does not apply.** The library prints "a dash" (TAX-REF p.18; SL-VAT-03 p.4). V2.2:
    "shows no amount against it" (S7-2.4.3-c29) and "Nothing appears as a zero or a dash unless the
    authority requires it" (c20).
11. **Exchange rate on an export invoice.** INT-COM-01 records the rate "on the posting, not printed
    on the document" (library p.8). V2.2 prints rate, source and date wherever the document currency
    differs from the functional currency (S7-2.4.3-c46). Owner: tax specialist with the product
    owner.
12. **Account code inside the entity.** The 'Entity in the code' sheet offers "Design B — entity
    inside the code" ("If you still want Design B … Say the word", r29). V2.2 settles Design A: "never
    digits inside it" (S7-2.2.1-c16), and "Nothing in the software parses the reference" (c23). Owner:
    product owner, to confirm that Design B is closed (PQ-21).
13. **Reversal date.** "Reversal date | No" ('Journal upload template' r15) against "Conditional"
    (S7-2.2.4-c44). The rule text agrees; only the mandatory flag differs.
14. **Version prepared against.** SRC-008 was "Prepared against the requirement specification,
    version 1.1" ('Read me' r3), not V2.2. Owner: product owner with the qualified accountant
    (PQ-19).
15. **Template count.** "Fourteen templates are delivered" ('Read me' r10), but the library lists
    fifteen (r6 to r20; library p.1).
16. **Non-tax invoice for whom.** SL-NTX-01 is "for suppliers not registered for VAT" (library p.5),
    while the field map sends the case of an unregistered purchaser to SL-NTX-01 (r14). Owner: tax
    specialist (PQ-23).

**Where it adds data that V2.2 leaves to configuration or brackets (all proposals).**

- **The delivered standard chart** ('Chart of accounts'): 206 posting accounts, 43 group rows and 68
  flagged control accounts. The counts agree with 'Entity in the code' r20 and 'Code structure' r59.
  It includes default tax codes (OUT-STD, IN-STD and others, r29) and per-profile enforcement levels.
  Owners: qualified accountant (chart), tax specialist (tax codes).
- **The spare range** "690000 – 699999 | Unused and reserved" ('Code structure' r19). This is outside
  the class digits 1 to 5 of S7-2.2.1-c03, so such an account has no class, natural balance or
  statement by V2.2's rule (PQ-11).
- **Values for V2.2 brackets:**
  - account code 6 and allocation step 10 ('Setup options' r19, r27);
  - journal reference "up to 40 characters", decimals "two places" ('Journal upload template' r11,
    r21);
  - warning "80 per cent by default" ('Volume and capacity' r43);
  - for Sri Lanka:
    - unregistered purchaser to SL-NTX-01, which bears on value 77 ('SL tax invoice field map' r14);
    - the serial format `YYMMM_QQQQ_XXXXX`, which bears on values 62 to 76 (r41 to r48);
    - the prescribed title and total rows under "Gazette Extraordinary No. 2481/22 of 27 March 2026"
      (r3), which bear on values 79 and 86.
- **Sri Lanka industry tax set** (library p.17): SSCL, Telecommunication Levy, Tourism Development
  Levy and others, "confirmed with its advisers — not assumed by the software". Owner: tax
  specialist (PQ-12).
- **A multi-entity group column**, and 13 measures not in V2.2: manual journals, invoice lines,
  receipts, supplier payments, goods receipts, depreciation lines, documents, dimensions, values per
  dimension, suppliers, fixed assets, interface languages, open periods, integration runs and API
  calls ('Volume and capacity' r8 to r40).
- **A build instruction.** "Build against the 'Multinational group' column" ('Read me' r8;
  'Volume and capacity' r3), and "60 to 70 per cent of a month's postings land in the last four
  working days" (r50).

**Where it agrees.**

- The journal template's 28 columns match S7-2.2.4-c37 to c64 one for one, and its worked file
  matches c71 to c73.
- The segment rules match S7-2.2.1-c16 to c26 ('Code structure' r36 to r42).
- The enforcement defaults A to D match S7-2.2.1-c58 to c61 ('Setup options' r13, r14).
- The code-clash rules match S7-2.2.2 ('Code structure' r65 to r73).
- The ten tax mechanics match S7-2.4.3-c34 to c43 (library p.18).
- The retention and capacity principles match S7-2.11.4 and S7-2.16.1 ('Volume and capacity' r42 to
  r49).

## 6. Effect on each V1-based artifact

### 6.0 Re-pointing: counts and rules

| Artifact (version) | S1 references | Non-mechanical | Mechanical |
| --- | --- | --- | --- |
| bracketed-values.yaml (v3) | 238 | 26 | 212 |
| BO-01 (v1) | 14 | 2 | 12 |
| BO-02 (v2) | 28 | 2 | 26 |
| BO-03 (v2) | 33 | 0 | 33 |
| BO-04 (v1) | 14 | 2 | 12 |
| BO-05 (v2) | 17 | 0 | 17 |
| BO-06 (v1) | 15 | 0 | 15 |
| BO-07 (v2) | 21 | 0 | 21 |
| BO-08 (v2) | 30 | 0 | 30 |
| actors.yaml (v3) | 177 | 6 | 171 |
| glossary.yaml (v2) | 147 | 4 | 143 |
| release-phasing.yaml (v3) | 903 | 38 (+3 shorthand, 2 ranges) | 865 |
| Q-001 to Q-031 | 175 | 28 | 147 |
| **Total** | **1,812** | **108** | **1,704** |

Per question: Q-007 4, Q-008 8, Q-009 12, Q-010 6, Q-011 9, Q-012 6, Q-013 5, Q-014 4, Q-015 6, Q-016 6,
Q-017 6, Q-018 6, Q-019 4, Q-020 8, Q-021 10, Q-022 7, Q-023 18, Q-024 4, Q-025 4, Q-026 6, Q-027 10,
Q-028 2, Q-029 20, Q-030 2 and Q-031 2. Q-001 to Q-006 cite SRC-001 by page only.

**Mapping rules.**

- **R-same.** Same and same number: change `S1-` to `S7-` and take the page from the S7 index entry.
- **R-renum.** One of the 51 renumbered pairs (section 3.4): take the crosswalk's S7 ID and page.
- **R-changed.** One of the 10 changed pairs: take the crosswalk's S7 ID, then re-read the citing
  sentence against the new text (section 3.1). For S1-2.4.1-c05, choose S7-2.4.1-c05, c06 or both.
- **R-successor.** One of the 7 "removed" clauses: use the successor in section 3.2 (not the
  crosswalk), and re-read.
- **R-short.** Shorthand ("S1-2.2.1-c06, c21", "S1-2.4.8-c01 to c05", "S1-2.16.1-c01 to c04"):
  expand each member and apply the rules above.
- **Page citations without an ID** ("SRC-001 p.68"): find the clause, then re-page it from the S7
  index.

The non-mechanical references, by artifact:

- **bracketed-values (26):**
  - R-successor: S1-2.11.4-c05 ×10 (lines 59 ×2, 84, 191, 201, 204 ×2, 208, 212, 230),
    S1-2.16.1-c02 ×5 (lines 215 to 218 and 227), S1-3-c03 ×1 and S1-2.2.2-c05 ×1;
  - R-renum: S1-2.2.1-c18 to c50, S1-2.2.2-c18 to c53, S1-2.2.2-c21 to c56, S1-2.2.2-c08 to c43,
    S1-2.4.1-c09 to c11 and S1-2.11.4-c07 to c10 (6);
  - R-changed: S1-2.4.1-c05 ×3 (values 74 to 76).
- **BO-01, BO-02:** S1-2.2.4-c32 to S7-2.2.4-c83 (R-renum), 2 each. **BO-04:** S1-2.4.8-c05 to
  S7-2.4.8-c19, 2.
- **actors (6):** S1-2.1.10-c32 to c38 ×2, S1-2.1.10-c35 to c41 ×2, S1-2.2.2-c13 to c48, and
  S1-3-c03 to S7-3-c03 (R-successor).
- **glossary (4):** S1-3-c03 (R-successor), S1-2.4.1-c05 (R-changed), and S1-2.11.4-c05 ×2
  (R-successor).
- **release-phasing (38):**
  - S1-2.2.1-c21 ×10 to S7-2.2.1-c52 (R-changed: its meaning changed, so every sentence that cites it
    must be rewritten);
  - S1-2.2.2-c12 ×3 to c47, S1-2.2.2-c16 ×9 to c51, S1-2.2.2-c18 ×4 to c53, S1-2.2.4-c32 ×2 to c83,
    S1-2.4.1-c06 ×2 to c08, S1-2.4.1-c09 to c11, S1-2.4.8-c01 to c15, S1-2.1.10-c35 to c41 and
    S1-2.2.1-c18 to c50;
  - R-successor: S1-2.1.7-c57 ×2, S1-2.1.8-c36 and S1-2.11.4-c05;
  - shorthand "c21" at lines 416, 1422 and 1719;
  - ranges "S1-2.4.8-c01 to c05" (line 663, which becomes S7-2.4.8-c15 to c19) and
    "S1-2.16.1-c01 to c04" (line 1410, which includes the changed c02).
- **questions (28):** Q-014 2, Q-015 4, Q-016 2, Q-018 2, Q-020 2, Q-023 1, Q-025 4, Q-027 2 and
  Q-029 9. They are listed by clause in section 6.5.

The bracketed-value workbook, the glossary and the actors also carry S1 page and extraction-line
fields: 178 `page` and `line` pairs in the workbook, and 147 `page` fields in the glossary. All are
re-derived from the S7 index and extraction.

### 6.1 Bracketed values

- **Totals.** V2.2 has 193 bracket pairs, against 181 in V1. Leaving out the 3 signature names gives
  **190 values**, against 178.
- **Gone (5).**
  - Value 160 ("[7] years is a placeholder", S1-2.11.4-c05). It is replaced by "no retention figure"
    (S7-2.11.4-c05).
  - Values 171 to 174 ("[X] transactions … [n] items, [n] customers, [n] employees", S1-2.16.1-c02).
    These are now set in V2.2's own capacity table (S7-2.16.1-c08 to c22).

  In both cases V2.2 answers them rather than drops them. The product owner confirms the V2.2 figures
  (Q-024, PQ-08).
- **Survive (173).** Every other value is still bracketed in V2.2, with the same token and context,
  under the re-pointed clause. Some need attention:
  - **Values 74 to 76** (the V1 debit note) now sit under the non-tax debit note S7-2.4.1-c06, with
    a new tax-debit-note series beside it.
  - **Value 29** ([role] for code assignment) sits in the changed clause S7-2.2.2-c05, which now also
    requires the code to be free.
  - **Value 25** ("[6] digits", S7-2.2.1-c02) now has a sibling, "[6] digits by default and settable
    between four and ten" (S7-2.2.1-c17).
  - **Value 170** ("[Y] concurrent users", S7-2.16.1-c01) now sits beside a capacity table that
    gives concurrent users of 50, 25,000 and 100,000 (S7-2.16.1-c22). Whether that settles [Y] is for
    the product owner.
  - **Values 9 and 4 to 8** are unchanged in S7-1-c09 to c12.
- **New (17), all to confirm:**

| Proposed n | Clause (page) | Token | Context | Proposed owner (workbook v3 rules) |
| --- | --- | --- | --- | --- |
| 179 | S7-2.2.1-c17 (p.25) | [6] | natural account "[6] digits by default and settable between four and ten" | qualified-accountant (code structure) |
| 180 | S7-2.2.1-c27 (p.25) | [10] | "allocated in steps of [10] inside a sub-group" | qualified-accountant |
| 181 | S7-2.2.1-c46 (p.26) | [role] | adopting a delivered chart "is itself approved, by [role]" | product-owner |
| 182 | S7-2.2.1-c56 (p.27) | [role] | Advisory: "appears on an exception report to [role]" | product-owner (with qualified-accountant, control) |
| 183 | S7-2.2.2-c12 (p.28) | [role] | reserved code "Held back deliberately by [role]" | product-owner |
| 184 | S7-2.2.2-c21 (p.29) | [role] | which chart an entity runs on "is set at entity set-up by [role]" | product-owner |
| 185 | S7-2.2.4-c28 (p.34) | [20] | preview of "the first [20] rows" | product-owner |
| 186 | S7-2.2.4-c40 (p.34) | [40] | journal reference "Text, up to [40] characters" | product-owner |
| 187 | S7-2.2.4-c49 (p.35) | [2] | debit "Decimal, [2] places" | qualified-accountant (PQ-10) |
| 188 | S7-2.2.4-c50 (p.35) | [2] | credit "Decimal, [2] places" | qualified-accountant (PQ-10) |
| 189 | S7-2.2.4-c58 (p.35) | [2] | tax amount "Decimal, [2] places" | qualified-accountant (PQ-10) |
| 190 to 192 | S7-2.4.1-c05 (p.54) | [location], [YY], [nnnnnn] | "TDN-[location]-[YY]-[nnnnnn]" | tax-specialist |
| 193 | S7-2.4.3-c68 (p.58) | [role] | remittance change "reported to [role]" | product-owner (security-owner advising: fraud control) |
| 194 | S7-2.16.1-c26 (p.133) | [80] | warning "[80]% by default" | product-owner (tech lead confirms) |
| 195 | S7-2.16.5-c15 (p.135) | [90] | "active in the last [90] days" | product-owner |

  Reconciliation: 173 + 17 = 190 and 178 - 5 + 17 = 190. By kind, the new values are 5 role, 7
  count or precision ([6], [10], [20], [40] and three [2]), 3 format, 1 percentage and 1 duration.
- **Proposed numbering.** Keep the v3 numbers 1 to 178 for surviving values, mark 160 and 171 to 174
  "answered by SRC-007", and number the new values 179 to 195. The value numbers already quoted
  elsewhere then stay valid: BO-02 value 161, BO-06 values 118 and 120, BO-08 values 175 to 177, the
  phasing's values 17 to 20 and 178, and the Q records. The alternative, renumbering in V2.2
  document order, shifts every value after 2.2.1 and breaks those references.
- **Values that SRC-008 proposes to settle** (owner confirms each; nothing is settled by this list):
  - 25 and 179 = 6, and 180 = 10 ('Setup options' r19, r27);
  - 186 = 40, and 187 to 189 = two places ('Journal upload template' r11, r21);
  - 194 = 80 ('Volume and capacity' r43);
  - for Sri Lanka only:
    - 77 (unregistered purchaser, non-tax invoice: 'SL tax invoice field map' r14);
    - 62 to 76 and 190 to 192 (the series format: r41 to r48);
    - 79 and 86 (Gazette 2481/22: r3).

  The tax values go to the tax specialist and the others to the owners shown.
- **Missing inputs.**
  - Annexure A now also asks for the subscription response (S7-3-c03). That is a vendor-addressed
    item, open under Q-023.
  - Annexure B items 1 to 3 are answered in part by SRC-008. SRC-008 gives a delivered chart, not
    the current chart; recommended build targets, not current volumes; and delivered templates, not
    the "existing" formats. See Q-005 in section 6.5.
  - "The entity's own document retention policy" (S1-2.11.4-c05) changes under the V2.2 model
    (S7-2.11.4-c06).

### 6.2 BO-01 to BO-08

All eight carry S1 IDs in `links.derives_from` and in their indicators' `clause`, both normative.
Each therefore needs a new version, whatever else changes.

- **BO-01.**
  - Indicator 2: re-point to S7-2.2.4-c83 (same text).
  - **Indicator 1** ("Difference between each sub-ledger and its control account | nil, computed
    continuously", S7-2.12.1-c01) **is at risk.** At Not applied or Advisory, V2.2 lets manual
    journals reach control accounts (S7-2.2.1-c55, c56), so the difference need not be nil (section
    4.1).
  - The statement "every sub-ledger agrees to its control account at all times" carries the same
    risk.
  - Owner: product owner, after the qualified accountant on PQ-01 and PQ-18.
- **BO-02.**
  - Indicators: no change (2.11.7, 2.1.11 same).
  - Candidate addition for the product owner: "A trial balance, a statement, a reconciliation or a
    document from the first month of use is reproducible in the form it was issued" (S7-2.16.1-c31).
- **BO-03.**
  - Indicators: no change.
  - Candidate additions: "no role anywhere in the system can override a code clash"
    (S7-2.2.2-c41); "lowering a level from Enforced is refused without approval" (S7-2.2.1-c68); "A
    change to an entity bank account is refused without approval by a second person"
    (S7-2.4.8-c06).
  - The statement may need the enforcement levels, because a manual journal to a control account is
    a control the entity now sets.
- **BO-04.**
  - Indicator 2: re-point to S7-2.4.8-c19. Indicators 1 and 3: no change.
  - Candidate additions: "A new entity in a configured country issues a compliant statutory tax
    invoice on the delivered template on the day it is created" (S7-2.4.8-c01); the levy tests
    (S7-2.4.8-c08 to c11); the prescribed-format lock (S7-2.1.10-c33).
  - The open item on countries now points to Q-003 v2 (template library countries).
- **BO-05.**
  - Indicators: no change.
  - The governance panel it relies on lost "Consolidation structure" in the printed alert grid
    (S7-2.15.8-c22, section 4.6).
- **BO-06.** No change.
- **BO-07.**
  - Indicators: no change.
  - The open item "SRC-001 states no product or commercial objective" is now only partly true. V2.2
    states a subscription model (S7-2.16.5-c01 to c07), though still no tenant or revenue target.
  - Candidate additions: "A second tax activated for a country appears on the next document issued
    … with no template changed and no release" (S7-2.4.8-c10); "every figure in the capacity table
    is raised beyond its tested ceiling … without a code change" (S7-2.16.1-c40).
  - Whether licensing deserves its own objective is for the product owner (PQ-09).
- **BO-08.**
  - Indicators 3 and 4: no change (S7-2.16.1-c03, c04; values 175 to 177).
  - Candidate addition: "the ceiling figures are sustained in load testing at the stated
    concurrency" (S7-2.16.1-c29).
  - The tenant open item gains "Limits are set per tenant and per entity" (S7-2.16.1-c25; Q-031).
  - A licence limit "may never block a period close, a statutory return, a tax filing, an audit
    access request or a data export" (S7-2.16.5-c18) bears on availability.

### 6.3 Actors and glossary

**Actors: new or changed roles and parties in V2.2.**

- *Licence types (S7-2.16.5-c08 to c12).* Full user, limited user, read-only and auditor, system or
  integration account, and vendor support account. These are licence classes, not starting roles;
  they cut across 2.1.2.
- *Regulator (S7-2.16.5-c21).* "An auditor, a regulator or an administrator reaching the audit
  pack".
- *Uploader of a journal batch (S7-2.2.4-c33).*
- *Tax authority as prescriber (S7-2.1.10-c32, c33).* It issues the instrument that fixes a format;
  SRC-008 names the "Commissioner General" for Sri Lanka.
- *Group administrator and entity administrator.* Already present. V2.2 adds that the administrator
  raises capacity limits (S7-2.16.1-c24), sees entitlement (S7-2.16.5-c26) and sets enforcement
  levels (S7-2.2.1-c54).
- *Holder of the template designer permission (S7-2.4.3-c87).* A permission, "not held by default".
- *Five new [role] holders.* Workbook values 181 to 184 and 193.
- *External systems.* Central bank or named rate source per country (S7-2.4.3-c48); tax authority
  number-range issuer (S7-2.1.10-c30, unchanged). SRC-008 adds VIES, ZATCA and the Indian Invoice
  Registration Portal (library pp.9 to 11). Those are proposals, for the tax specialist and tech
  lead, and do not apply to Sri Lanka.
- *Re-point.* The four non-mechanical references in section 6.0, and every page.

**Glossary: entries that change.**

- *"Control account" (S1-2.2.1-c06).* Its quoted definition, "accept sub-ledger postings only;
  manual journals to them are blocked", now reads as V2.2's contested attribute-table wording
  (section 4.1). It should define the account by S7-2.2.1-c53: "one whose balance is owned by a
  sub-ledger rather than by the general ledger", and note the enforcement levels.
- *"Account code".* It becomes the natural account: "[6] digits by default and settable between four
  and ten" (S7-2.2.1-c17).
- *"Debit note (sales)".* It splits into the tax and non-tax forms (S7-2.4.1-c05, c06).
- *"Retention (of records and documents)".* Rewrite from S7-2.11.4-c05 and c06.
- *"Annexure A".* Add the subscription response (S7-3-c03).
- *"Turnover levy (SSCL)".* V2.2 now describes levies (S7-2.4.3-c16: "Most sector levies are charged
  on turnover before the transaction tax"), so this entry becomes part of a wider "levy" entry.
- *"Proforma invoice".* Add its tax and non-tax forms (S7-2.4.1-c07).
- *"Governance panel".* Note the corrupted alert row (S7-2.15.8-c22).
- *All entries.* Re-page. The note "bracketed-values.yaml (v2)" is already stale (v3).

**Glossary: new terms in V2.2.** Natural account; entity segment; country segment; account reference
(S7-2.2.1-c16 to c21). Control enforcement level (Not applied, Advisory, Enforced) and control type or
owning sub-ledger (c53 to c57). Delivered standard chart; industry variant; extension account (c33 to
c38, c25). Allocation step; spare range; reserved code (c27, c30; S7-2.2.2-c12). Chart scope, own
chart or shared group chart; code clash; next best code; near duplicate (S7-2.2.2-c16, c25, c34).
Mapping template; value mapping; published template; mandatory flags "Yes / One of / Per account /
Conditional" (S7-2.2.4-c20 to c24, c65 to c68). Prescribed format (S7-2.1.10-c32). Statutory
template; delivered template library; template designer (S7-2.4.3-c72, c79). Levy; industry tax set;
value of supply (S7-2.1.7-c57; S7-2.4.3-c16, c17). Tax mechanic, and each of the ten mechanics
(S7-2.4.3-c34 to c43). Remittance details (c51). Capacity target; tested ceiling; warning threshold
(S7-2.16.1-c07, c26, c33). Storage tier and near-line storage (S7-2.11.4-c08). Erasure under privacy
law (c09). Statutory retention floor (c06). Per-user subscription; user pack; licence types;
entitlement; meter; dormant account (S7-2.16.5). Tenant (S7-2.16.1-c25, its second use in V2.2
after S7-2.1.1-c01).

Accounting and tax terms keep V2.2's meaning only. Normative definitions belong to the qualified
accountant and the knowledge base (F1).

### 6.4 Release phasing, D-INT-1 and Q-029

**Sub-sections that need a mark or a changed mark** (all proposals, for the product owner).

- **2.16.5 (new): no mark.**
  - Its counting, dashboard and dormant-account rules (c13 to c17) matter once Tiqri charges a
    tenant.
  - Its prohibitions (c18 to c22) are constraints that a release without licence enforcement meets
    trivially.
  - Its commercial terms (c02 to c07, c09, c13, c20, c24) are vendor statements under Q-023.
  - Proposed mark: needs-decision, owner product owner, with the tech lead (PQ-09).
  - The sub-section count goes from 187 to 188.
- **2.16.1: release-1, but larger.** "proved against the ceiling in load testing before acceptance"
  (S7-2.16.1-c07, c29) for a multinational ceiling, for example 100,000,000 journal lines a month,
  is a large part of release-1 acceptance for one Sri Lanka entity. Proposed: needs-decision, owner
  product owner, with the tech lead (PQ-08).
- **2.2.1: release-1 as a whole is no longer the obvious mark.**
  - The control-enforcement clauses (c53 to c68) are release 1 (they bound D-INT-1).
  - The segment clauses (c18 to c21) are switched off for a single entity (c18), so they are a
    release-1 data-model constraint (c22 to c24: composed, never parsed), with the presentation in
    release 3.
  - "Use a delivered industry variant" (c35) depends on the industry templates (2.1.7 c55, c56, c58,
    release 5).
  - "Copy another entity's chart" (c38) needs a second entity (release 3).
  - Proposed: split.
- **2.2.2.** The shared-group-chart reach of the clash check (c18, c19, c22, c23) arrives with group
  accounting (release 3). The single-entity check (c20) is release 1. Proposed: split.
- **2.2.4.** Mapping (c20 to c35) is release 1. The bulk routes for budgets, stock counts and asset
  registers (c35) follow their modules under the existing rule module-dependent-clauses. The "Partner
  entity" column (c59) follows intercompany. No split is needed under the existing rules.
- **2.1.7.** S7-2.1.7-c57 was marked release-1 in v3 together with S1-2.7.2-c02. It now "activates
  the industry tax set". The industry selection therefore has to exist in release 1, while the
  industry templates (c55, c56, c58) are proposed for release 5. Proposed: keep c57 in release 1,
  with a blocking question to the tax specialist on the Sri Lanka levy set (PQ-12).
- **2.1.10.** Release-1. The prescribed-format clauses (c32 to c37) are needed for Sri Lanka if the
  tax specialist confirms SRC-008's statement that Gazette 2481/22 is "Mandatory for every VAT
  registered person from 1 July 2026" ('SL tax invoice field map' r3). The blocking question becomes
  Q-015 as changed (section 6.5).
- **2.4.3.**
  - Release-1: levies (if liable), taxes on the face of the document, the currency block (Q-003:
    "LKR, with multiple currencies"), remittance details, the Sri Lanka statutory template.
  - Templates for other countries follow those countries.
  - The designer (c79 to c87): release 1 or later, for the product owner.
  - Proposed: split.
- **2.4.8.** "Two entities in the same country but different industries" (c08) needs two entities.
  Proposed: split, with c08 in the release of the second entity (release 3 under A-03) or
  needs-decision.
- **2.4.1, 2.4.6.** Release-1 unchanged. Re-point the reasons and add Q-016 (changed) and PQ-03.
- **2.1.8.** The release-3 list includes the corrupted S7-2.1.8-c36. It is marked as it stands, with
  PQ-05.
- **2.11.4.**
  - Release-1. The reason "retention is configurable (S1-2.11.4-c05)" is no longer true.
  - Closed-period storage tiering (c08) is a design point for the tech lead.
  - Privacy erasure (c09) needs an owner (PQ-24, with Q-028).
- **2.15.8.** Unchanged needs-decision; note the corrupted c22.
- **releases.loading_task, R-06 and D-2.16.2.** Under V2.2 the default for a single entity with
  sub-ledgers is "Enforced for bank" (S7-2.2.1-c59). An opening bank balance by manual journal
  would therefore be refused, so it needs the migration route (S7-2.16.2) or another method
  (PQ-16).

**D-INT-1 and Q-029: what remains of the conflict under V2.2.**

*What V2.2 removes.* V1 blocked manual journals to every control account (S1-2.2.1-c06, c21). In V2.2
the block applies "where control enforcement is set to Enforced" (S7-2.2.1-c52). The delivered
default for a "Single entity running sub-ledgers" is "Advisory, and Enforced for bank" (S7-2.2.1-c59,
p.27). At Advisory "A manual journal to a control account is allowed, requires a reason selected from
a configurable list, and appears on an exception report to [role]" (c56). The flag and type stay
recorded at a lower level "so the level can be raised later without the chart being rebuilt" (c55),
and the level is "held per entity and per control type" (c62).

The consequences for option A (interim manual journals for payroll, fixed assets and income tax):

- **A(i)**, relaxing the block by a change request, needs no change request if c52 governs. V2.2
  itself provides the Advisory level.
- **A(ii)**, interim non-control accounts, is no longer needed. The payroll, fixed asset and tax
  accounts can be flagged from release 1 at Advisory. So the flag-immutability trap (S7-2.2.2-c47,
  c51), and readings R1 and R2 of the reclassification route, fall away.
- SRC-008 shows the same reading: its chart flags accumulated depreciation, gratuity and tax accounts
  as control accounts at "Advisory" for profile B ('Chart of accounts' r17 to r23, r88, r89, r68 to
  r70). That is supporting data only.

*What remains.*

1. **Which clause governs.** The attribute table still says "manual journals to them are blocked"
   (S7-2.2.1-c06, p.24). If c06 governs, V1's conflict is unchanged (section 4.1; PQ-01; owner
   product owner, with the qualified accountant).
2. **The substitute rule still stands against interim journals, at any level.** "How to read the
   accounting entry tables. Every posting shown is auto-posted by the system from the transaction
   named. No user journal is acceptable as a substitute" (S7-2-c02, p.8). Payroll is a row of "What
   the system posts, without a manual journal" (S7-0-c10, p.4). Depreciation is "posted by the
   system, and never maintained in a spreadsheet alongside it" (S7-2.8-c01, p.88) and "must be
   auto-calculated by the system, not by a spreadsheet" (S7-2.8.3-c01, p.90). Advisory makes an
   interim journal possible; it does not make it an accepted substitute. The working-papers clause
   that names "depreciation" and "gratuity" (S7-2.11.5-c01) is unchanged and still the only support.
3. **Agreement.** "These agreements are auto-computed by the system continuously and must be nil"
   (S7-2.12.1-c01), with rows for "Fixed asset cost and accumulated depreciation | Asset register
   totals" and "Net pay, withholding tax and fund contribution payables | Payroll run totals not yet
   remitted" (S7-2.12.1-c05, c06, p.114). Without the module there is nothing to agree to, so these
   rows still cannot run in release 1 under option A. The account stays on the reconciliation
   schedule (S7-2.2.1-c65).
4. **Raising to Enforced at release 2.** "Activating a module proposes that the matching control
   type be raised to Enforced" (c63). At Enforced "the balance is reproducible from that sub-ledger at
   any past date" (c57). Balances built by interim Advisory journals in release 1 are not
   reproducible from a sub-ledger for those past dates. Either the loading task rebuilds that history,
   or the claim holds only from the date of raising. Owner: qualified accountant.
5. **The first entity's default level is itself unclear.** Is Tiqri's Sri Lanka entity "Single entity
   running sub-ledgers" (Advisory; c59), or, being "LKR, with multiple currencies" (Q-003),
   "Multinational, multi-currency or high volume" (Enforced, "and lowering it is reported"; c61)?
   SRC-008's profile D needs all three ('Setup options' r9). V2.2's "or" needs any one. Under c61 the
   entity starts at Enforced, and option A needs an approved, reported lowering (c64) for each control
   type. The level is in any case "set per entity and per control type by the administrator" (c54),
   so this is a choice for the qualified accountant and product owner, not a fact (PQ-02).
6. **Unchanged from V1.**
   - Option B (payroll and the fixed-asset core in release 1) avoids every point above.
   - Option C's open points stand as recorded (Q-022; interface postings under S7-2.1.6-c15; the
     payroll row of 2.12.1; 2.10.10 governing interface rules). Interface postings are not manual
     journals, so the enforcement level does not touch them.
   - The corporate income tax interim (D-2.7.6) now posts to a tax control account at Advisory
     rather than into a block.

*Effect on the D-INT-1 text.*

- `against_interim_journals` keeps its S7-2-c02, S7-0-c10, S7-2.8-c01 and S7-2.8.3-c01 points.
  Its control-account point becomes conditional on PQ-01 and on the level chosen (PQ-02).
- `on_moving_balances_later` and option A(ii) become moot if c52 governs.
- Option A's `effect_on_control_account_rule` is rewritten around Advisory, c63, c57 and c64.
- R-01 is rewritten the same way.
- The release-1 rationale's quote of S1-2.2.1-c06 is replaced by both sides of section 4.1.

### 6.5 Questions Q-001 to Q-031

"Re-point" means applying section 6.0, including page citations to SRC-001.

| Q | Status under V2.2 | Detail, with who must confirm |
| --- | --- | --- |
| Q-001 | Open as written; supported | V2.2 is still vendor-addressed (S7-0-c32; S7-3-c03 now asks for a subscription response). Its new 2.16.5, "Access is sold by subscription" (S7-2.16.5-c01), fits answer (b). Product owner confirms. Re-point. |
| Q-002 | Changed | Release 1 now has to cover 2.16.5 and the splits in section 6.4. Phasing v4 follows. Product owner decides. |
| Q-003 | Open as v2 records it | V2.2 delivers "a statutory template for each country the group operates in" (S7-2.4.3-c72) and per-country industry tax sets (S7-2.1.7-c57). SRC-008 has no Norway template. The Norway, framework, year-end and currency points stay with their owners. The tax-specialist gap for non-SL countries stays with the governance owner. |
| Q-004 | No longer applies as written | DEC-0008 makes SRC-007 the baseline; V2.2 is also unsigned (S7-3-c02). The bracketed-value part carries over to the 190 V2.2 values (section 6.1). Proposed: a successor question on SRC-007's sign-off and values. Product owner. |
| Q-005 | Partly answered by SRC-008 | Chart: "This is the standard chart the system is to be delivered with" ('Read me' r6). Volumes: "Recommended build targets across four scales" (r8). Formats: "Fourteen templates" (r10). But Annexure B asks for the *current* chart, *current* monthly volumes and the *existing* formats (S7-3-c04, unchanged), and V2.2 no longer needs volumes for 2.16.1 (section 6.1). To confirm: the product owner (scope), the qualified accountant (the delivered chart, which he authored) and the tax specialist (formats). Whether the current chart is still needed depends on Q-006. |
| Q-006 | Open as written | V2.2 adds the upload of an entity's own chart (S7-2.2.1-c36) and export at any time (S7-2.16.5-c22). The question stands. Product owner. |
| Q-007 to Q-013 | Open as written | 2.2.6, 2.2.8, 2.6, 2.8 and 2.12 are unchanged in V2.2 (crosswalk: all same). Q-010's worked example is unchanged (S7-2.8.3, p.91). Re-point only. Qualified accountant. |
| Q-014 | Open; slightly changed | Re-point S1-2.2.2-c08 to S7-2.2.2-c43. 2.2.2 still has no naming standard. V2.2 adds "A name identical to another account in the same group is refused" and a near-duplicate warning (S7-2.2.2-c35). SRC-008 supplies names, not a standard. Qualified accountant. |
| Q-015 | Changed; partly answered for Sri Lanka | V2.2 adds the per-entity choice of continuing, monthly or annual restart where an authority prescribes it (S7-2.1.10-c36, c37) and keeps the financial-year restart in S7-2.4.1-c08 (section 4.2). SRC-008, for Sri Lanka: "It continues from the number last issued in the preceding month. Where necessary it may instead restart at the beginning of each month or each year; which of the three applies is an entity setting" ('SL tax invoice field map' r45). Tax specialist confirms for Sri Lanka and Norway. Re-point S1-2.4.1-c06 to c08 and S1-2.4.1-c09 to c11. |
| Q-016 | Changed; partly answered for Sri Lanka | The V1 debit note splits into tax and non-tax forms (S7-2.4.1-c05, c06). New note rules are in S7-2.4.6-c05 to c07. The cap in S7-2.4.6-c03 is unchanged, so its effect on debit notes is still unclear. SRC-008, for Sri Lanka tax notes: "It cannot be issued without a valid reference to an issued document" (library pp.6, 7). Tax specialist confirms; qualified accountant on treatment. |
| Q-017 | Open as written | S7-2.4.6-c02 is unchanged. Tax specialist. |
| Q-018 | Changed; partly answered for Sri Lanka | Re-point S1-2.4.8-c02 to S7-2.4.8-c16. SRC-008: "Purchaser's TIN … Mandatory on a tax invoice … Where the customer is not registered, the supply goes on SL-NTX-01" ('SL tax invoice field map' r14). SL-NTX-01 prints a company number and no supplier TIN (library p.5), which suggests reading (B) for Sri Lanka. Tax specialist confirms. |
| Q-019 | Open as written | SRC-008's TIN rule (r14) leans on the number but does not settle status against number. Tax specialist. |
| Q-020 | Changed | Under V2.2 a statutory period is "a floor below which an entity may not dispose" (S7-2.11.4-c06). It is still needed, as the disposal floor, not as a deletion trigger. The six "[7] years" clauses remain (section 4.3). Re-point S1-2.11.4-c05 to S7-2.11.4-c05 and c06. Tax specialist. |
| Q-021 | Partly answered for Sri Lanka | SRC-008 gives the Sri Lanka tax invoice field by field under "Gazette Extraordinary No. 2481/22 of 27 March 2026, Annexure I. Mandatory for every VAT registered person from 1 July 2026" ('SL tax invoice field map' r3 to r50), including title, TINs, date format "MM/DD/YYYY" and the three total rows. It gives no return forms or e-filing formats. Tax specialist confirms. The non-SL templates need a named tax specialist (Q-003). |
| Q-022 | Open as written | S7-2.10-c01 and S7-2.1.6-c14 are unchanged. Product owner. |
| Q-023 | Changed (wider) | New vendor-addressed clauses: S7-2.16.5-c09, c10, c13, c20, c24 and the Annexure A subscription response (S7-3-c03). Re-point S1-2.11.4-c07 to S7-2.11.4-c10. Product owner. |
| Q-024 | Changed (wider) | V2.2 now sets capacity figures and a tested ceiling (S7-2.16.1-c07 to c29) and adds "[80]%". The service-level brackets (values 16, 96, 153, 169 and 175 to 177) remain. Product owner, tech lead confirms feasibility. |
| Q-025 | Largely answered by V2.2 | "Data is held from the day the organisation starts on the system, not for a number of years … no retention figure is applied by the software of its own accord" (S7-2.11.4-c05, p.113). One model: "the longer of that policy and the statutory period" (c06). Disposal: "without an approved disposal instruction from the entity" (c07). What remains is the six "[7] years" clauses (section 4.3). Product owner confirms. Re-point S1-2.11.4-c05 and c06. |
| Q-026 | Open as written | S7-2.16.5-c10 adds an auditor licence type but nothing on pay visibility. Product owner. |
| Q-027 | Changed (wider) | Both V1 errors persist (S7-2.2.2-c48; S7-2.13.1-c14, S7-2.1.7-c46). Add 2.4.3-c71 to 2.5.3, 2.16.1-c36 to 2.11.6, and possibly 2.16.5-c22 to 2.16.2 (section 4.5). Re-point S1-2.2.2-c13 to c48. Product owner. |
| Q-028 | Changed (wider) | Add erasure "required by a privacy law" (S7-2.11.4-c09). Who owns privacy-law rules per country is as open as residency. Governance owner. |
| Q-029 | Changed substantially | See section 6.4. Options A(i) and A(ii) and readings R1 and R2 change; PQ-01 and PQ-02 come before the choice. Re-point S1-2.2.1-c21 to S7-2.2.1-c52 (changed), S1-2.2.2-c12 to c47, c16 to c51 and c18 to c53. Product owner, with the qualified accountant and the tax specialist. |
| Q-030 | Open as written | SRC-008's chart has "122900 Allowance for expected credit loss" (r62), an account, not a policy. Qualified accountant. |
| Q-031 | Open; informed | "Limits are set per tenant and per entity, never globally, so one group raising a limit does not alter any other" (S7-2.16.1-c25). A pack covers "every entity in the group" (S7-2.16.5-c03). SRC-008: "Group-level limits are the sum of entity limits" ('Volume and capacity' r44). This leans towards the review's reading "a tenant holds one group", but does not decide it. Product owner, with the tech lead and the security owner. |

### 6.6 New questions V2.2 raises (proposed, not records)

| PQ | Question | Owner role |
| --- | --- | --- |
| PQ-01 | For control accounts, does S7-2.2.1-c06 ("manual journals to them are blocked") or the enforcement levels (c52, c54 to c61, c68) govern? | product-owner, with qualified-accountant |
| PQ-02 | What enforcement level per control type does the first Sri Lanka entity start at: "Single entity running sub-ledgers" (c59) or "multi-currency" (c61)? | qualified-accountant, with product-owner |
| PQ-03 | Which governs a statutory sales series: the financial-year restart (S7-2.4.1-c08) or the entity's choice (S7-2.1.10-c36)? | tax-specialist (content), product-owner (which clause) |
| PQ-05 | Confirm V1's wording for the corrupted rows S7-2.1.8-c36 and S7-2.15.8-c22. | product-owner |
| PQ-06 | Which module does each test in S7-2.2.2-c61 accept? | product-owner |
| PQ-08 | Single-entity customers: 5,000 (S7-2.16.1-c17) or 25,000 (SRC-008)? Which column is release 1 built and load-tested against: V2.2's "proved against the ceiling … before acceptance" (c07), or SRC-008's "Build against the 'Multinational group' column"? | product-owner, with tech-lead |
| PQ-09 | How does 2.16.5 apply to Tiqri's own product, in which release, and with which commercial values (Annexure A items in S7-3-c03)? | product-owner |
| PQ-10 | Fixed "[2] places" in the upload template, against currency minor units. | qualified-accountant, with tech-lead |
| PQ-11 | What class, natural balance and statement does an account in the spare range (SRC-008: 690000 to 699999) take, given S7-2.2.1-c03? | qualified-accountant |
| PQ-12 | Which industry tax set and levies (SRC-008 IND-TAX: SSCL at 2.5% and others) apply to the first entity, in what order and on what base (S7-2.1.7-c57)? | tax-specialist |
| PQ-14 | Is approval to add or amend an account ever optional, as SRC-008 profile A says, against S7-2.2.1-c44? | product-owner, with qualified-accountant |
| PQ-15 | Location "mandatory on all transactions" (S7-2.2.3-c06) against SRC-008's blocked location on most balance-sheet accounts. | qualified-accountant |
| PQ-16 | How is the opening bank balance loaded where bank is Enforced (S7-2.2.1-c59)? Part of D-2.16.2. | qualified-accountant |
| PQ-17 | A calendar-year restart is missing from the reset rule (S7-2.1.10-c18), against a calendar-year `YY`. | tax-specialist, with tech-lead |
| PQ-18 | Manual journals at Not applied or Advisory against "must be nil" (S7-2.12.1-c01) and "no balance in it exists without a document behind it" (S7-2.3-c01). | qualified-accountant |
| PQ-19 | Which specification version was SRC-008 prepared against ("version 1.1", 'Read me' r3)? | product-owner, with qualified-accountant |
| PQ-21 | Confirm that Design B (entity inside the code), offered in SRC-008, is closed by S7-2.2.1-c16 and c23. | product-owner |
| PQ-22 | Correct SRC-008's inconsistent illustrations (RCT-01, SOA-01 amounts, the credit-note number, ageing, the template count) before any become test data. | qualified-accountant |
| PQ-23 | SL-NTX-01: for an unregistered supplier, an unregistered purchaser, or both? | tax-specialist |
| PQ-24 | Who owns privacy-law erasure rules per country (S7-2.11.4-c09)? Can be folded into Q-028. | governance-owner |

PQ numbers 04, 07, 13 and 20 are not used: those candidates were folded into existing questions
(Q-025, Q-027, Q-018 and Q-003).

## 7. Proposed re-base plan

The order puts first what other artifacts quote.

1. **Assurance review of this analysis.** Then the orchestrator decides how to carry the successor
   map: a crosswalk v2, or a successor block (section 3.3).
2. **New question records for the source-level points** (orchestrator assigns IDs): PQ-01, PQ-03,
   PQ-05, PQ-06, PQ-08 and PQ-19, and the Q-027 additions. These go to the product owner first,
   because several later marks depend on them.
3. **bracketed-values.yaml v4** against SRC-007: 190 values, stable numbers 1 to 178, new 179 to 195,
   S7 lines and pages, the 26 non-mechanical re-points, and the SRC-008 proposals noted in
   `needed_for` without a value set.
4. **glossary.yaml v3** and **actors.yaml v4**: re-point and re-page, the changed entries, and the
   new terms and roles (section 6.3).
5. **BO-01 v2, BO-02 v3, BO-03 v3, BO-04 v2, BO-05 v3, BO-06 v2, BO-07 v3 and BO-08 v3.** Each needs a
   new version, because `derives_from` and the indicator clauses are normative. The substantive
   changes are BO-01's indicator 1 (blocked on PQ-01 and PQ-18) and the candidate indicators, which
   are offered, not added.
6. **Question records.** Q-001 to Q-031 each get a new version that re-points SRC-001 citations to
   SRC-007: Q-003 v3, Q-029 v4, Q-030 v3, and v2 for the rest. The changes in section 6.5 are applied
   in the same versions. Q-004 is closed or superseded by the orchestrator's successor record.
7. **release-phasing.yaml v4**: the 2.16.5 mark, the splits of 2.2.1, 2.2.2, 2.4.3 and 2.4.8, the
   2.16.1 needs-decision, D-INT-1 rewritten as in section 6.4, R-01 and R-06 revised, and the counts
   recomputed for 188 sub-sections.
8. **A revised decision brief and question pack** (orchestrator), replacing the withdrawn
   GOV-BRIEF-R1-SCOPE and GOV-QPACK-L1.

Nothing in steps 3 to 7 needs a person's decision to start. Steps 5 to 7 are cleaner after the
answers to PQ-01, PQ-02 and PQ-05.

## 8. What this analysis does not do

- It sets no value, chooses no option of D-INT-1, and marks no clause.
- It edits no existing artifact, index, crosswalk or question.
- It treats SRC-008 as proposed data throughout. Where SRC-008 would settle a question, the owner
  who must confirm it is named.

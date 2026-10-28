---
id: REV-01M61SP5CTK2J8YYRVRR7C9DMX
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - id: GOV-SCOPE-INCR-001
    hash: sha256:a44f4678af22a9c6d72e3effbab7a36bf736666978e9d1e3db88b53090bbc786
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [NF13: the new tenant-level role departs from plain V2.2 text and is not listed as a departure]
      WA-15 adds "a tenant-level administrator role" that holds the permission to raise capacity figures.
      The rendered PDF, p.8, says "Roles are built by the entity's administrator, not fixed by the vendor"
      (S7-2.1.2-c01) and "Permissions are not bundled into fixed packages that the entity cannot take
      apart" (c02). A role the product supplies, with a permission tied to it, is a vendor-fixed role.
      WA-15 keeps re-assignment under c02 open, but the c01 point is not shown. The governance owner
      chose option (a), so the substance is not in question; what is missing is that the departure is
      not put in front of its owners as DEP-1 to DEP-8 are.
      Two practical points are also undefined. First, who assigns the tenant-level role to a user: that
      is tied to Q-056's open point on how the first administrator is named. Second, whether the
      EXC-27 test route's "one test administrator account" holds this tenant-level role, the entity's
      Administrator role (c26), or both. Without that, CAP-06's raise cannot be tested under the
      proposed route.
      Fix: add a DEP item for c01 with owners (security owner and product owner), and say in the test
      route proposal which role or roles the test administrator holds.
    citation: >-
      "Roles are built by the entity's administrator, not fixed by the vendor" (SRC-007 p.8,
      S7-2.1.2-c01, checked on the rendered PDF); "Administrator | Configuration, user and role
      maintenance, period control and the segregation rules" (p.9, S7-2.1.2-c26, checked on the rendered
      PDF); GOV-SCOPE-INCR-001 v5 WA-15, CAP-03 sixth bullet, departures_from_plain_text, EXC-27
      test_route_proposal; Q-057 v3 "Answer so far, second", NF11
  - severity: non-blocking
    text: >-
      [NF14: version references left over from v4] The scope now rests on Q-056 v3 and Q-057 v3, but
      several places still describe v2.
      (a) D-2 still asks the product owner to confirm "the parts of tenant provisioning that Q-056 v2
      leaves open (which role provisions, how the first administrator is named, what the provisioning
      role can reach afterwards)". It omits self-service sign-up, which EXC-27 now holds open for the
      product owner.
      (b) D-2 also lists "the parts of capacity behaviour that Q-057 v2 leaves open (... a platform
      ceiling)", not v3's wording: whether an enforced upper bound exists, who raises it, and whether it
      is the tested ceiling.
      (c) EXC-27's "what" says "Q-056 v2 leaves open", while its reason cites v3.
      (d) SEC-2 cites "Q-056 v2".
      None of these changes the substance, but D-2 is what the product owner reads and confirms. Fix:
      align D-2 and the other three places with EXC-27 and EXC-29 as written.
    citation: >-
      GOV-SCOPE-INCR-001 v5 D-2, EXC-27 what and reason, EXC-29 what, SEC-2; Q-056 v3 "Still open"; Q-057
      v3 "Answer so far, second", "Still open"
created_at: "2026-10-28"
---

# Delta review of GOV-SCOPE-INCR-001 v5 (commit 1cab48c)

This is an E4 delta review for WF-01M61MRRKX52P8XHG3NZXSPCZH, step 10. It follows
REV-01M61R5FTD3DD5RK7G0TH7G0NS, which is not edited here.

The subject is `docs/requirements/increments/GOV-SCOPE-INCR-001.md` v5 at commit
`1cab48c3e4dc863b2873871973d933d5892fca8e`. `python tools/governance/trace.py explain
GOV-SCOPE-INCR-001` reports version 5, tier 1, no approval, and the normative hash
`sha256:a44f4678af22a9c6d72e3effbab7a36bf736666978e9d1e3db88b53090bbc786`. That matches the brief.

I compared it with Q-056 v3 (commit 8f802c4) and Q-057 v3 (commit 74318b7) as they are committed.
`created_at` gives the date only, because the guard blocks `date`.

**Verdict: non-blocking-findings.** NF10, NF11 and NF12 are resolved. WA-15 brings in only what Q-057
v3 settles. Nothing that is still open is treated as settled. In particular, the scope does not adopt
Q-057 v3's own gloss that "an upper bound above the tenant's own figures is expected": EXC-29 keeps
"whether an upper bound exists that the software enforces" open.

There are two new non-blocking findings. Neither needs a decision before the scope is sent. Approval
still needs F2 (Tier 1).

## Findings from REV-01M61R5FTD3DD5RK7G0TH7G0NS (v4)

| Finding | Status | Evidence in v5 |
| --- | --- | --- |
| NF10 "no unattended sign-up" | Resolved | Q-056 v3 withdraws the gloss. WA-14 keeps only "a named administrative role provisions tenants and onboards clients", and lists sign-up as open. CAP-01 says "INCR-001 assumes nothing about it". EXC-27 and the classification of Q-056 hold self-service open for the product owner. D-2 is stale (NF14 a). |
| NF11 holder of the raise permission | Resolved | WA-15 records option (a) from Q-057 v3: a tenant-level administrator role, "not each entity's Administrator of S7-2.1.2-c26". Re-assignment under c02, other contents of the role and its relation to the entity Administrator are held open with the security owner (CAP-03, WA-15, SEC-2). The departure from c01 is not listed (NF13). |
| NF12 unbounded raise | Resolved | CAP-06, EXC-29, D-2 and stack_dependencies all state that "the holder of the tenant-level administrator role can raise any capacity figure with no upper bound". They put it to the tech lead with the product owner, and settle no bound. |

All earlier findings remain resolved. Q-007 is still "not resolved, reason accepted".

## What the brief asked to check

1. **WA-15 against Q-057 v3.** It matches. The record's second answer settles only option (a). WA-15
   is labelled "governance owner's answer of 2026-10-28 (as security owner), pending the product
   owner, with the security owner for the re-assignment point". The record says "as security owner
   and tech lead"; the difference does not matter.
   - **CAP-03:** the role is defined "only as far as that needs". Its other contents, its relation to
     the entity Administrator and re-assignment are open.
   - **The warning:** it names the tenant-level role, which fits c26's requirement to name "the role
     that may raise it" and adds nothing further.
   - **The unbounded raise:** it is stated as a consequence, not chosen as a policy.
2. **The PDF-check statements are accurate and claim no more than was checked.** The basis says the
   orchestrator checked pp.37, 38, 40 to 42 and 133 to 136, "and every other page cited here was read
   from the text extraction only". The body says the same. This is the orchestrator's statement (E4).
   On the rendered PDF, I re-checked pp.37, 38, 41, 133 and 134 out of that set, and the passages
   match.
3. **New problems.** NF13 (the tenant-level role against c01) and NF14 (stale version references in
   D-2). The other items are consistent:
   - D-1, D-3 to D-7 have not changed in substance.
   - EXC-27 and EXC-29 match the "Still open" lists of Q-056 v3 and Q-057 v3. EXC-29 now cites c35
     and c38.
   - stack_dependencies records Q-054 v2 (React, .NET, Azure, Azure SQL Database) as going to the stack
     ADR, "designs nothing from it". WA-06 still names only Azure, but CAP-01's reliance notes the v2
     addition, so they are consistent.
4. **Questions.** There are 57 classification entries (grep count), Q-001 to Q-057, once each. Eight
   are blocking, and each names its exclusion: Q-007 EXC-11, Q-013 EXC-12, Q-014 EXC-09, Q-031 EXC-01,
   Q-034 EXC-10, Q-055 EXC-28, Q-056 EXC-27, Q-057 EXC-29 (with EXC-21).

## Clauses checked

**On the rendered PDF, by me, in this review** (Read tool, pages rendered as images):

- **p.8:** S7-2.1.2-c01 ("Roles are built by the entity's administrator, not fixed by the vendor"),
  S7-2.1.2-c02 ("Permissions are not bundled into fixed packages that the entity cannot take apart")
  and S7-2.1.2-c08. These match the extraction.
- **p.9:** S7-2.1.2-c13, c14, c16, c17, and S7-2.1.2-c26 ("Administrator | Configuration, user and
  role maintenance, period control and the segregation rules | Amend or delete the audit log or
  transaction history, or approve a document they raised"). These match.
- **p.37:** the 2.2.5 table, including the Adjustment row ("Raised in the period's adjustment period
  for closing or audit adjustments, reportable separately | Finance manager"), the Reversing row and
  the Manual row. These match. The extraction's flattened columns read correctly.
- **p.38:** S7-2.2.6-c10 to c16, including "Dated adjustment journal in the current open period,
  reported as a prior-period item" and "The correction is dated in the current open period". These
  match. This confirms on the PDF the conflict that Q-055 records.
- **p.41:** S7-2.2.8-c07 (the state diagram with "override by [role] only" and "reopen — approval by
  [role], every posting made while reopened listed"), c09 to c11 ("Set by: Finance manager"), and c12
  ("[role], with approval"; "Applied once the audit of that year is finalised"). These match.
- **pp.133 to 134:** S7-2.16.1-c08, c14, c21 to c26, c29, c33 to c35, c38 and c39. These match, word
  for word in the passages the scope and Q-057 quote.

**Against the extraction only:** every other clause cited in my four earlier records on this subject.
The findings of those records that rest on pp.37, 38, 41 and 133 to 134 (B2, B3, NF1, NF12) are now
confirmed on the PDF.

## Verification (observed)

- `python tools/governance/trace.py explain GOV-SCOPE-INCR-001`: the hash above. Four earlier reviews
  are shown as against an older hash (stale).
- `git log -6`: 1cab48c (scope v5), 74318b7 (Q-054 v2, Q-057 v3), 8f802c4 (Q-056 v3), 7d5fc0b (the v4
  review), ee20ce5, 70d7f06.
- The output of `python tools/governance/check.py` with this record in place is in the handoff report.

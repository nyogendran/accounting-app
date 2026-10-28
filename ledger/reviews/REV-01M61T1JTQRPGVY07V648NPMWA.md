---
id: REV-01M61T1JTQRPGVY07V648NPMWA
type: review
reviewer: requirements-assurance
level: E4
subjects:
  - id: GOV-SCOPE-INCR-001
    hash: sha256:488aba4b44dae53c2b8743aee1ec061a3803c01ebbb64f661ce867239eaa2e79
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [NF15, cosmetic: WA-15's label was not widened with its text] v6 adds two points to WA-15's text,
      "who assigns the role to a user, and which role or roles the EXC-27 test administrator holds".
      CAP-03, EXC-27 and SEC-2 all hold these two points open with the security owner. WA-15's label,
      though, still reads "with the security owner for the re-assignment point" only. Nothing is
      misassigned, because the text and SEC-2 name the right owner. Fix at the next revision: "with the
      security owner for the re-assignment, role-assignment and test-administrator points".
    citation: >-
      GOV-SCOPE-INCR-001 v6 WA-15 text and label; CAP-03 sixth bullet; EXC-27 test_dependency; SEC-2
created_at: "2026-10-28"
---

# Final delta review of GOV-SCOPE-INCR-001 v6 (commit 404183c)

This is an E4 delta review for WF-01M61MRRKX52P8XHG3NZXSPCZH, step 12. It follows
REV-01M61SP5CTK2J8YYRVRR7C9DMX, which is not edited here.

The subject is v6 at commit `404183c385b44f88a960ee5c6a11b6f97bb5e1c9`. `trace.py explain` reports
version 6, tier 1, no approval, and the normative hash
`sha256:488aba4b44dae53c2b8743aee1ec061a3803c01ebbb64f661ce867239eaa2e79`. That matches the brief.

I reviewed the full `git diff 1cab48c 404183c` of the subject. `created_at` gives the date only,
because the guard blocks `date`.

**Verdict: non-blocking-findings.** There is one cosmetic finding (NF15). NF13 and NF14 are resolved,
and the v6 changes introduce nothing of substance. On my reading, the scope is ready for its owners to
decide on. Approval still needs F2, because the scope is Tier 1.

## Findings from REV-01M61SP5CTK2J8YYRVRR7C9DMX (v5)

| Finding | Status | Evidence in v6 |
| --- | --- | --- |
| NF13: the tenant-level role departs from c01; role assignment and the test administrator's role are undefined | Resolved | **DEP-9** quotes S7-2.1.2-c01 with its page. It gives the departure as "a role the product supplies, a tenant-level administrator role ... beyond the starting role set of c18 to c27", with owners `[security-owner, product-owner]`. D-1 now says "DEP-1 to DEP-9", and approval_consequence names the owners of DEP-9. **Who assigns the role** and **which role or roles the test administrator holds** are both held open with the security owner, "decided by no one here". This is stated in CAP-02, CAP-03, WA-15, EXC-27 test_dependency, SEC-2 and D-2, together with the dependency of testing the raise on both. |
| NF14: stale v2 references | Resolved | D-2 now cites Q-056 v3 and Q-057 v3. It lists self-service sign-up for the product owner, and v3's upper-bound wording (an enforced bound, who raises it, the tested ceiling of c35 and c38) and licensing. EXC-27 "what", SEC-2 and CAP-02 cite Q-056 v3. The "v2" references left in the file are in the change table "Changes from v3 to v4", where they correctly describe that revision. |

All earlier findings remain resolved. Q-007 is still "not resolved, reason accepted".

## The v6 changes

- **Test-route proposal.** The only change is "holding whichever role or roles the security owner
  decides (open)". It is still marked "PROPOSAL ... not a decision", with approval_note and the D-1
  exclusion. It decides nothing.
- **D-1.** The only change is DEP-8 to DEP-9. This is consistent.
- **D-2.** It is aligned with EXC-27 and EXC-29 as written, and asks for confirmation of DEP-9. D-2
  sits under `decisions_requested_of_product_owner`, while DEP-9 also needs the security owner.
  D-1's rule ("confirmed there by every role named in its owners field") and approval_consequence
  cover this, so it is not inconsistent.
- **Classification.** It is unchanged by the diff. A grep counts 57 entries, Q-001 to Q-057, once
  each. The eight blocking questions keep their exclusions: Q-007 EXC-11, Q-013 EXC-12, Q-014 EXC-09,
  Q-031 EXC-01, Q-034 EXC-10, Q-055 EXC-28, Q-056 EXC-27, Q-057 EXC-29.

## Clauses checked

**On the rendered PDF:** no new pages. DEP-9's quotation of S7-2.1.2-c01 matches p.8, which I checked
on the rendered PDF in REV-01M61SP5CTK2J8YYRVRR7C9DMX. That record lists the other pages checked on the
PDF.

**Against the extraction only:** nothing new in this delta.

## Verification (observed)

- `python tools/governance/trace.py explain GOV-SCOPE-INCR-001`: the hash above. Five earlier reviews
  are shown as against an older hash (stale).
- `git log -2`: 404183c (scope v6), 53e82bc (the v5 review).
- The output of `python tools/governance/check.py` with this record in place is in the handoff report.

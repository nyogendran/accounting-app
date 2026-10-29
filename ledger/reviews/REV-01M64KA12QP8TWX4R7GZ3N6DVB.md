---
id: REV-01M64KA12QP8TWX4R7GZ3N6DVB
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - id: ADR-0002
    hash: sha256:ec151d942e4b00fee76e9fa208c2fc4fda95885bfec6815be3cc61189bac9526
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [V3-NF1, I-12's run-time check has no identity that can see the policies] I-12 has each
      environment check "that every policy is on and every tenant table is covered". I-5 denies the
      tenant application identity VIEW DEFINITION on the security schema. Catalogue views show metadata
      only for securables on which the caller holds some permission. Run under the application
      identity, the check would see no policies, so it fails closed if written as a positive count and
      fails open if written as "is any visible policy off?". Verification (2) ("a policy turned off in a
      test environment stops tenant traffic") would catch the fail-open form, so this is not blocking.
      I-12 also leaves "at intervals" unset, and that interval is the exposure window. Fix: name a
      monitoring identity that may only read the policy and table metadata, add it to the allow-lists
      checked in verification (1), and state that the check is positive (covered tenant tables equal
      all tenant tables, every policy enabled). Set the interval, or name who sets it (security owner,
      or the hosting ADR).
    citation: >-
      ADR-0002 v3 normative.invariants I-5 ("no ... VIEW DEFINITION on the security schema"), I-12;
      verification (1), (2)
  - severity: non-blocking
    text: >-
      [V3-NF2, the platform identity's allow-list has no content, and the sign-in lookup has no key]
      I-11 gives the platform identity "an allow-list of its own (I-5 applies to it in kind)" but does
      not list it. Reads are meant to go "only through procedures keyed on the signed-in user", so the
      allow-list should be EXECUTE on those procedures and no direct SELECT on the tables. Otherwise the
      membership Row-Level Security is the only control on the catalogue and the identities table, which
      it does not cover. Separately, at sign-in there is no user value yet: finding the user from the
      token's subject is a lookup across all users. Fix: state the platform identity's allow-list
      (EXECUTE only on named procedures), say that the sign-in procedure returns only the row matching
      the authenticated subject, and state the allow-list of the "further identity" that writes the
      store.
    citation: >-
      ADR-0002 v3 normative.invariants I-11; verification (1) ("the platform identity ... exceed their
      allow-lists")
  - severity: non-blocking
    text: >-
      [V3-NF3, wording: two classes or three] The decision still says "Data is in two classes: tenant
      data ... and platform data". I-1 now adds read-only reference tables "shared by all tenants that
      hold no tenant's data", which are neither. Verification (1) still says "any table not on the
      platform allow-list", while I-1 calls it "the reviewed allow-list" and puts reference tables on it.
      Nothing is unsafe, but a reader could take reference tables to be outside the allow-list. Fix at
      the next revision: three classes in the decision, and "the reviewed allow-list" in verification
      (1).
    citation: >-
      ADR-0002 v3 normative.decision; I-1; verification (1) first clause
  - severity: non-blocking
    text: >-
      [V3-NF4, carried from V2-NF7: Microsoft Learn quotes not verified by this reviewer] Unchanged in
      v3. The quotes and page commits (d0b41be05c89ea95874c19ddcbf4a115cdb89602,
      2ceb7c07640735a9c49dbb6ff1de511aceead449) rest on the orchestrator's reading of 2026-10-29. This
      reviewer has no web access and has not checked them. They are not registered sources.
      Registration is open with the governance owner.
    citation: >-
      ADR-0002 v3 Evidence and assumptions, first two bullets; Version history, v3 ("V2-NF7: the web
      quotes remain the orchestrator's reading, unregistered")
created_at: "2026-10-29"
---

# Delta review of ADR-0002 v3, tenant isolation (commit 932fd41)

An E4 security delta review. It follows REV-01M64FW5EQK3D8VZT2NB6GH9CM, the v2 review (committed at
9ebc9c4), which is not edited here.

- `trace.py explain ADR-0002` reports version 3, tier 1, status Proposed, no approval, and the normative
  hash `sha256:ec151d942e4b00fee76e9fa208c2fc4fda95885bfec6815be3cc61189bac9526`. That is the hash the
  orchestrator computed before the commit; the two agree.
- The working tree was clean at HEAD 932fd41.
- I reviewed the full `git diff 53278ce 932fd41` of the subject.
- `created_at` gives the date only.

**Verdict: non-blocking-findings.** v3 resolves both v2 blocking findings and V2-NF1 to V2-NF6.
V2-NF7 is carried as V3-NF4. Three new non-blocking points concern precision (V3-NF1 to V3-NF3). No
invariant decides anything the ADR calls open. On my reading, the ADR is ready to go to the security
owner and the tech lead for AS-1 to AS-5, PR-1 and PR-2. Approval needs F2, because the ADR is Tier 1.

## Status of the v2 findings

| v2 | Status | Reason |
| --- | --- | --- |
| V2-B1 | Resolved | I-11 adds a separate platform identity and denies the platform store to the tenant application identity (I-5, "no permission on the platform store"). Reads go through user-keyed procedures, backed by Row-Level Security on memberships keyed on a user value set as in I-4. Verification (1) checks the platform identity's permissions. Verification (2) tests that user X cannot read user Y's memberships and that the tenant identity cannot reach the store. Residual precision: V3-NF2. |
| V2-B2 | Resolved | I-5: procedures run as the caller, contain no dynamic SQL and are unsigned, unless a recorded exception. Verification (1) scans the procedures of both identities for it. |
| V2-NF1 | Resolved | The allow-list holds read-only reference tables (I-1), with SELECT in I-5. Verification (1) exempts foreign keys to reference tables. Wording residual: V3-NF3. |
| V2-NF2 | Resolved | I-5 is now a ceiling ("at most") of effective permissions, inherited ones included. The audit log, and tables that S7-2.1.2 or S7-2.1.4 make unchangeable, get SELECT and INSERT only. Sequences visible to a tenant are not shared. |
| V2-NF3 | Resolved | History tables carry a filter only (I-1, I-4 (c), verification (1)), and history reads are in the suite. |
| V2-NF4 | Resolved | I-4 (e): the column is never converted, and the session value is converted once, explicitly. Predicate functions come from one reviewed template. |
| V2-NF5 | Resolved, with a residual (V3-NF1) | I-12 refuses traffic while a policy is off. Migrations run per tenant with the value set; turning a policy off is the I-8 path, done while tenant traffic is refused. |
| V2-NF6 | Resolved | Unregistered endpoints fail the build. The predicate template is checked. Logs and telemetry are tested. Review of allow-list changes is a review record until F2, then code-owner review. |
| V2-NF7 | Not resolved (carried as V3-NF4) | Outside the author's control: it needs the governance owner to register the pages. |

## Does any invariant decide something called open?

No.

- I-7 keeps the mechanism and leaves who grants and removes memberships to PR-1 (Q-031).
- I-8 leaves operator use to PR-2 (Q-056, SEC-2).
- I-11's "named administrative operations under a further identity" does not say who performs them
  (Q-056 open).
- Holding user identity records in the platform store does not choose the identity provider (SEC-1).
- I-5's insert-only audit log applies the specification's own behaviour (S7-2.1.2, "no role can amend
  or delete the audit log", p.9). It does not settle SEC-3's tamper-evidence question.
- I-12 is a technical control, not a policy choice.
- AS-4's statement that jobs act on behalf of a user is labelled and owned (security owner).

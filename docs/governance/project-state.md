---
id: GOV-STATE
type: governance
title: Project state
status: Proposed
version: 1
owner: orchestrator
---

# Project state

Updated by the orchestrator at every workflow transition. Last update: 2026-10-29.

- **Phase:** L1, discovery. F0 is complete and validated (GOV-F0-VALIDATION).
- **Gate 0:** passed on 2026-10-20. APR-01M5D0D7HCQBRJHRB3V6S76H21 is the governance owner's
  approval (E1-op) on AREQ-01M5CV2YA7AACRYGVH6EG8S0SQ. GATE-0, DEC-0001, DEC-0002, DEC-0003,
  DEC-0005 and DEC-0006 are Approved; each is re-confirmed on the git host when Stage 1 starts.
- **Discovery input received on 2026-10-20** from the governance owner, to be recorded as
  questions and proposed decisions with owners:
  - TIQACC is Tiqri's own multi-tenant SaaS product.
  - Multiple countries: Sri Lanka and others such as Norway; LKR with multi-currency.
  - SRC-001 is accepted as the requirements baseline, confirmed by Shifan Cader.
  - The chart of accounts is maintained by Finance in the system (SRC-001 2.2.1).
  - The requirements agent proposes the release phasing.
- **Discovery questions:** Q-001 to Q-006 record the answers so far, what stays open, and the role
  that confirms each.
- **G2, people: decided.** DEC-0007 is Approved (APR-01M5RN152P364F3ETYB4B9830V, E1-op, 2026-10-25;
  APR-01M5VBMJ6YK3NFBADZ52CBS484 repeats it). The authority matrix is v2: Yogendran is governance
  owner, tech lead, security owner and release authority; Shifan Cader (CFO) is product owner, tax
  specialist and the qualified accountant's escalation point; Rifaz Hajirin is qualified accountant.
- **Open decisions:**
  - G3, platforms: GitHub, with work items in GitHub Projects. Repository
    https://github.com/nyogendran/accounting-app.git (private); the governance owner approved the F2
    set-up on 2026-10-28, then put the GitHub plan on hold the same day. Pushes are made by a person
    (the guard blocks agent pushes). F2 is on hold: it needs the GitHub plan (branch protection and
    code owners on a private repository), a bot identity for agents, Shifan's and Rifaz's GitHub
    accounts, and the gh CLI. While it is on hold, no Tier-1 approval can be given, so the foundation
    scope cannot be approved and its requirements cannot be written (DEC-0010 condition 1). Chat is not
    chosen.
  - G5, data boundary: deferred (DEC-0004).
- **New baseline (2026-10-26).** The governance owner named specification V2.2 the requirements
  baseline. It is registered as SRC-007, and Rifaz's business information pack v1.1 (Annexure B:
  delivered chart of accounts, volumes, invoice templates) as SRC-008 (commit ab1cc70). DEC-0008
  is Approved (APR-01M5VK9AVJG6XW56VT8H69JANM, product owner, E1-op; re-confirmed at Stage 1).
  DEC-0009 is Approved (APR-01M5VK73TV6T342BZ3926JZ8FD): SRC-007 clauses are S7 IDs, and a clause
  link missing from an existing index is an error. The real bank statements and supplier invoices
  received with them stay outside git.
- **Countries (Q-003 v2):** "All countries defined in the template": Sri Lanka, EU and UK, GCC, India,
  US. Open: Norway (no template), first-release countries, and a tax specialist for the added
  countries.
- **Working answers (governance owner, 2026-10-28),** pending their owners' confirmation:
  - Q-031 v3: a tenant is an organisation; a firm (Tiqri, an audit firm or a client) keeps the books of
    client organisations, each its own tenant.
  - Q-032 v3 and Q-033 v2: enforcement levels govern; every control type starts at Advisory, bank
    included.
  - Q-038 v3: release 1 is one entity, 125 named users, 50 at peak and 200,000 journal lines a month,
    per tenant.
  - Q-040 v2: decimal places from each currency's configuration. Q-054: Azure, with Azure SQL Database.
  - Q-054 v2: the application stack is React (frontend) and .NET (backend), latest stable, with a
    highly intuitive UI; pins and the rest go to the stack ADR.
  - Q-056 v3: an owner or tenant administrator provisions tenants and onboards clients (reading open).
    Q-057 v4: a tenant-level administrator role may raise a capacity figure; above it, the upper bound
    is Tiqri's load-tested ceiling, with a warning, not a refusal.
- **PDF check:** poppler is installed (pdftoppm 25.07.0). SRC-007 pp.37, 38, 40-42 and 133-136 were
  checked on the rendered PDF on 2026-10-28; the quotes behind Q-055 and Q-057 match.
- **Foundation scope:** GOV-SCOPE-INCR-001 v6 (WF-01M61MRRKX52P8XHG3NZXSPCZH), reviewed six times;
  the last four found no blocking issue (last REV-01M61T1JTQRPGVY07V648NPMWA). Decision brief
  GOV-BRIEF-INCR001-SCOPE v1 is ready to send to the product owner and the qualified accountant. No
  approval request: Tier 1 needs F2. NF15 (a label) waits for the next revision. Eight questions block parts of it (Q-007, Q-013, Q-014, Q-031, Q-034, Q-055,
  Q-056, Q-057). It is Tier 1, so the product owner's approval needs F2.
- **DEC-0010: Approved** (APR-01M61ME5F96WP1KB4TVNBAH65X, governance owner, E1-op, 2026-10-28;
  re-confirmed at Stage 1). Gates A and B per increment, with a foundation increment (tenants, users
  and roles, audit log, journals, periods, numbering, chart and control levels, currencies) before
  release-1 scope is settled. The increment's content is Tier 1, so its approvals and merges need F2.
- **Blockers:** the V1-based L1 work must be re-based on SRC-007 before it goes to anyone.
- **In progress:** WF-01M5VHRCEQP734DHRKE29J5YET, re-base on SRC-007 (option A, governance owner,
  2026-10-26: questions first, the rest of the re-base while they are answered).
  - Done: S7 clause IDs (DEC-0009); the SRC-007 clause index (2,744 clauses, validated by script and
    against rendered PDF pages); crosswalk v2 (2,427 same, 9 changed, 8 with successors, 298 new); the
    impact analysis GOV-IMPACT-SRC007 v2 (reviewed twice); the re-read list (1,004 of 1,812 references).
  - Done: Q-032 to Q-053 (questions V2.2 raises), Q-029 v5, decision brief GOV-BRIEF-R1-SCOPE v3 and
    question pack GOV-QPACK-L1 v3, reviewed (blocking, then non-blocking: ready to send).
  - Next: re-base the workbook, glossary, actors, objectives and question records, scripted where
    mechanical; then phasing v4 after the answers. Correct GOV-IMPACT-SRC007 section 6.4 item 8 and its
    governance-panel list at its next revision.
- **Done on V1:** WF-01M5D0SE8MMS39CTPTXH8ME1HT, L1 discovery, steps 1 to 8.
  - Built and reviewed: the clause index (2,444 clauses) and the bracketed-value workbook (178 values,
    168 to confirm).
  - Proposed, reviewed twice and revised: business objectives BO-01 to BO-08, actors, a glossary and the
    release phasing (v3).
  - Questions Q-001 to Q-031 are open for their owners.
- **Ready to send:** GOV-BRIEF-R1-SCOPE v3 to the product owner, and GOV-QPACK-L1 v3 to the product
  owner, the qualified accountant and the governance owner.
- **Waiting on people:** answers to Q-032, Q-033, Q-034, Q-047, then Q-029 and the rest of the pack.
- **Next:**
  1. Send GOV-BRIEF-INCR001-SCOPE to Shifan and Rifaz (governance owner; published as a private page,
     https://claude.ai/artifact/YAheZfri2EAcTiYBaRN94e, to be shared by the governance owner); record
     their answers. The approval request follows F2.
  2. ADR-0001, application stack baseline (Q-054 v2), Proposed, Tier 2: approval request
     AREQ-01M630Y03CCX4184YKJ48EMQQD (tech lead) waits for the captured phrase; the governance owner
     wrote "Approved" in prose on 2026-10-29, which is not a captured decision.
  3. ADR-0002, tenant isolation, Proposed, Tier 1: drafted on 2026-10-29 because the governance owner
     asked that day that tenant isolation be considered from the initial design. v1 reviewed
     (REV-01M64CE9TQR7XK2B9WD3HNP5QA, six blocking); v2 answers it and goes to a delta review.
     Approval needs F2; the governance owner is asked whether the small-team fallback (a second named
     person) applies to a Tier-1 ADR. Follow-on ADRs (data access, identity, design system, API style,
     hosting) come after.
  4. Record answers as they arrive; finish the re-base.
  5. F1, knowledge base.
  6. F2 (on hold), once the GitHub details arrive; needed before any Tier-1 approval or merge. Shifan's and Rifaz's approvals need F2 to carry their own
     identity.

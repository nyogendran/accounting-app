---
id: GOV-STATE
type: governance
title: Project state
status: Proposed
version: 1
owner: orchestrator
---

# Project state

Updated by the orchestrator at every workflow transition. Last update: 2026-10-26.

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
  - G3, platforms: GitHub, with work items in GitHub Projects; a private repository exists. Setting
    up F2 needs the repository URL, the plan and an instruction to push. Chat is not chosen.
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
  1. Record answers as they arrive; finish the re-base.
  2. F1, knowledge base.
  3. F2, once the GitHub details arrive. Shifan's and Rifaz's approvals need F2 to carry their own
     identity.

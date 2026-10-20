---
id: GOV-STATE
type: governance
title: Project state
status: Proposed
version: 1
owner: orchestrator
---

# Project state

Updated by the orchestrator at every workflow transition. Last update: 2026-10-20.

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
- **Open decisions:**
  - G2, people: DEC-0007, requested as AREQ-01M5D0SDNEWZ67Y9E82KC2T3KD. Yogendran: governance owner,
    tech lead, security owner, release authority. Shifan Cader (CFO): product owner, escalation
    point, tax. Rifaz Hajirin: qualified accountant.
  - G3, platforms: GitHub, with work items in GitHub Projects; a private repository exists. Setting
    up F2 needs the repository URL, the plan and an instruction to push. Chat is not chosen.
  - G5, data boundary: deferred (DEC-0004).
- **Blockers:** none for L1. Annexure B: monthly volumes and invoice formats are requested from
  Finance; the current chart of accounts is needed only if data is migrated.
- **In progress:** WF-01M5D0SE8MMS39CTPTXH8ME1HT, L1 discovery. Step 1: the requirements agent
  builds the clause index of SRC-001 and the bracketed-value workbook.
- **Next:**
  1. Once DEC-0007 is approved, update the authority matrix.
  2. Independent review of the clause index and workbook (requirements-assurance).
  3. Business objectives, actors, glossary and a proposed release phasing.
  4. F1, knowledge base.
  5. F2, once the GitHub details arrive.

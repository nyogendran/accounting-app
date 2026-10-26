---
id: DEC-0008
type: decision
title: Specification V2.2 (SRC-007) replaces V1 (SRC-001) as the requirements baseline
status: Approved
version: 1
owner: orchestrator
tier: 2
normative:
  decision: >-
    SRC-007, the requirement specification V2.2, is the requirements baseline for TIQACC in place of
    SRC-001. SRC-008, the business information pack v1.1, is a supporting input to it; where SRC-008
    and SRC-007 differ, SRC-007 governs, as SRC-008 itself states.
  conditions:
    - SRC-001 stays registered and unchanged, as the superseded baseline; nothing derived from it is deleted.
    - Work built on SRC-001 (the clause index, the bracketed-value workbook, business objectives, actors, glossary, release phasing and question records) is re-based on SRC-007 through an impact analysis that names every change, before any of it is put to a person for decision.
    - SRC-007 carries no version number on its face and its section 3 sign-off is unsigned; this decision accepts it as the baseline for analysis and build, as Q-004 did for SRC-001, and does not stand in for that sign-off.
    - Contradictions found inside SRC-007 are recorded as questions for their owners and are not resolved by agents.
links:
  related: [SRC-001, SRC-007, SRC-008, Q-004, Q-005]
---

# DEC-0008: Specification V2.2 replaces V1 as the requirements baseline

**Context.** Finance sent a revised specification on 2026-10-21, with the business information pack
that answers the Annexure B request (Q-005). The governance owner reviewed both on 2026-10-26 and said:
"Yes V2 (2.2) is the new requirement baseline", and confirmed the workbook as version 1.1. Both are now
registered: SRC-007 and SRC-008 (commit ab1cc70).

**What changes from V1.** V2.2 is 137 pages against V1's 121. A first comparison by the orchestrator,
sentence by sentence and not yet reviewed, found the substantive changes in these sections:

- the chart of accounts and its delivered standard chart (2.2.1, 2.2.2);
- control accounts enforced at a level set per entity and control type: Not applied, Advisory or
  Enforced (2.2.1);
- journal upload and mapping (2.2.4);
- prescribed numbering formats (2.1.10);
- invoice content, taxes, levies, remittance details and the delivered template library (2.4);
- retention from go-live (2.11.4);
- capacity targets (2.16.1);
- subscription licensing (2.16.5, a new section).

The full impact analysis follows this decision as a workflow step.

**Who decides.** Accepting the requirements baseline is the product owner's decision
(`docs/governance/authority-matrix.yaml`, "Requirement scope and priority"; Q-004). The governance
owner has stated it; the product owner confirms it.

**Consequences.**

- The release-1 decision brief (GOV-BRIEF-R1-SCOPE) and the question pack (GOV-QPACK-L1), both written
  against SRC-001, are withdrawn from circulation until they are revised against SRC-007. In
  particular, V2.2's control enforcement levels change what Q-029 has to decide.
- Clause IDs move from the `S1-` prefix to a new prefix for SRC-007, set by the re-index.

**Not decided here.** Whether the V2.2 sign-off is ever signed, and by whom (SRC-007 section 3).

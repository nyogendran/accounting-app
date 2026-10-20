---
id: GATE-0
type: gate
title: Gate 0 - framework baseline (F0)
status: Proposed
version: 1
owner: orchestrator
tier: 3
normative:
  gate: Gate 0
  scope: >-
    The F0 governance core of SRC-005: CLAUDE.md; methodology, conventions, operating model,
    authority matrix, risk register and templates; tools check, trace, approvals and run_tests with
    tests; hooks guard, validate and capture_approval; project settings; four agents
    (requirements-engineer, requirements-assurance, accounting-domain-expert,
    code-security-reviewer); six skills; one path rule; git hooks; registered sources SRC-001 to SRC-006.
  criteria:
    - Tool tests pass.
    - Hook tests cover allow, block, Windows paths, shell writes and fail-closed.
    - An agent's attempt to write a decision record is blocked.
    - A synthetic requirement goes through drafting, two reviews and a hook-captured approval, and a normative edit then voids it.
    - The governance checker reports no errors on the repository.
    - Each of the four agents has CLAUDE.md in context, writes inside its scope and is blocked outside it.
    - Independent review findings are fixed or dispositioned.
  evidence:
    - GOV-F0-VALIDATION, this gate's validation report.
    - EVD-01M5CT4WP4TFNRCZMNQ0W6C3BP (E3, 167 tests, pass; its tree equals commit 6c0f138 without the evidence file).
    - Independent reviews (E4) REV-01M5C0YAD8BAMX6HNTM9H4WC1E, REV-01M5C2545W1VGNTXKY5DWSCZQV, REV-01M5C44F4G2E9W08D7YH4587J3, REV-01M5C56YPY0TASJC9E84X1PWYS, REV-01M5C6QDYWRZJC39SDZ1FBJEKY, REV-01M5CPZDD4BGSK5HJG00SY8TRH and REV-01M5CT5C97V1T7W6ZHY99DQHJM; the first review's findings are listed in commit d0d422d.
    - The tool-path probe in GOV-F0-VALIDATION (Claude Code 2.1.301, 2026-10-20).
    - WF-01M5BJDGB5536WYT96GNTQWH4K (agent smoke tests, live probes, reviews and fixes).
    - F0 commits db505ac, a75ca66, 3f5afe8, fd099aa, f02ec5c, 8e6a69a, d0d422d, 658ed21, fa9a669, 1a7c423, c449dc1, 0cbf6b6, e1f1bbe, 5892c0f, 0272342, 76fc69f, 8aad214, 32e75b8, 67a91d4, 910069f, 6c0f138 and 41e6ee1.
  conditions:
    - The authority matrix is filled in (G2) before Gate A; until a qualified accountant is named, no accounting policy can be approved.
    - Stage 0 approvals, including this one, are re-confirmed on the git host when Stage 1 starts.
    - Each agent created later (two at Gate A, four at Gate B) passes the same smoke test before its first task.
    - The tool-path probe in GOV-F0-VALIDATION is re-run at each gate, because the guard judges tool paths as the observed Claude Code version resolved them (RISK-003).
  accepted_risks:
    - RISK-003 Agents and people share one OS account until a git host exists.
    - RISK-009 Auto memory loads unreviewed notes into sessions (accepted by DEC-0005).
links:
  related: [GOV-F0-VALIDATION, DEC-0001, DEC-0002, DEC-0003, DEC-0005, DEC-0006, WF-01M5BJDGB5536WYT96GNTQWH4K, REV-01M5C0YAD8BAMX6HNTM9H4WC1E, REV-01M5C2545W1VGNTXKY5DWSCZQV, REV-01M5C44F4G2E9W08D7YH4587J3, REV-01M5C56YPY0TASJC9E84X1PWYS, REV-01M5C6QDYWRZJC39SDZ1FBJEKY, REV-01M5CPZDD4BGSK5HJG00SY8TRH, REV-01M5CT5C97V1T7W6ZHY99DQHJM]
---

# Gate 0: framework baseline

Approving this gate confirms the framework baseline above. The same approval request also confirms
the decisions taken in session on 2026-10-20 (DEC-0001, DEC-0002, DEC-0003, DEC-0005) and DEC-0006.
DEC-0004 (data boundary) stays deferred.

What the approver should look at:

1. The validation report, GOV-F0-VALIDATION: what was verified, and what was not.
2. The conditions and accepted risks above.
3. The independent review findings and how each was handled (in the report).
4. The new convention that every Markdown file under `docs/` carries front matter (finding OQ-1).

Not covered by this gate:

- Framework phases F1 to F6: the knowledge base, git-host approvals, defect and change-impact
  workflows with `trace impact`, CI evidence, chat, and deployment and operational evidence.
- The six agents that DEC-0002 creates at Gate A and Gate B.
- Any requirement, accounting policy, tax treatment or product decision. Those start in L1, and
  accounting policy needs a named qualified accountant.
- The data boundary for external services (DEC-0004, deferred).

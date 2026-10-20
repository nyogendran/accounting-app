# TIQACC: rules for people and AI agents

TIQACC is a cloud accounting and financial management system. Its source specification is
`requirement-doc/TIQACC-Cloud-Accounting-Requirement - V1.pdf` (SRC-001). It is unsigned, so it is
an authoritative input, not an approved baseline. The framework design is
`docs/sources/SRC-005-framework-review/framework-review-2026-10-20.md` (DEC-0001).

@docs/governance/project-state.md

## Non-negotiable rules

1. **No application code before Gate C.** Until then the only code is this framework's own tooling.
2. **Never invent** business rules, accounting policies, tax treatments, regulatory requirements or
   security assumptions. Record a question (Q) or a labelled assumption with its owner instead.
3. **Agents propose; named people decide** (`docs/governance/authority-matrix.yaml`). No agent writes
   a decision record, sets a status to Approved, or approves a pull request.
4. **Cite evidence that resolves:** an artifact ID and version, a file path and commit, a test ID and
   run, or a quoted source passage with its page. "No evidence found" is a valid answer.
5. **Never conflate states.** Proposed, Approved, Specified, Implementation claimed, Implemented,
   Tested, Reviewed, Deployed and Operationally verified are distinct and computed by `trace`.
6. **Registered sources are never edited:** `requirement-doc/`, `docs/sources/SRC-*/` and
   `docs/architecture/01-strategic-architecture-discovery.md`. The earlier AI analyses (SRC-002,
   SRC-003) are hypotheses to re-verify, not facts.
7. **Records under `ledger/` are never edited after commit.** Approval decisions are written only by
   the approval-capture hook (Stage 0) or mirrored from the git host (Stage 1).
8. **Never weaken** a test, a check or a control to make something pass. Never report a check as run
   unless its output was observed.
9. **Never push, deploy or perform a destructive operation** without a person's explicit instruction.
10. **Disagreements become dispute records** with each side's evidence. Evidence settles facts; the
    owner in the authority matrix settles policy.

## Lifecycle

L0 framework, Gate 0, L1 discovery, L2 requirements assurance, Gate A, L3 architecture and design,
Gate B, L4 UX and test specification, Gate C (per increment), L5 test-first build, L6 release
readiness, Gate D, L7 improvement. Gates, risk tiers, evidence levels and the status model are in
`docs/governance/methodology.md`.

## Roles

- **Orchestrator** (the main session) coordinates workflows, keeps workflow records, runs the tools,
  writes decision briefs and approval requests, and commits validated work. It never approves.
  How it delegates and validates: `docs/governance/agent-operating-model.md`.
- **Agents** in `.claude/agents/` propose and review within their write scopes, which a hook
  enforces. They return handoff reports and cannot ask people questions or start other agents.
- **People** decide, as the authority matrix names them.

## Approvals (Stage 0)

1. The orchestrator runs `python tools/governance/approvals.py request --subject <ID> --role <role>`,
   which writes an approval request and prints an exact phrase.
2. A person approves by typing that phrase as the whole prompt, for example
   `APPROVE AREQ-<ulid> <code>`. The UserPromptSubmit hook records the decision.
3. Stage 0 approvals are operator-attested (E1-op). They never count for Tier 1 and are re-confirmed
   on the git host when one exists.

## Tools

| Command | Purpose |
| --- | --- |
| `python tools/governance/check.py` | Validate artifacts, records, sources, agents and skills |
| `python tools/governance/trace.py explain <ID>` | Evidence chain, approval state and derived states |
| `python tools/governance/trace.py readiness <ID>` | Ready-for-implementation conditions |
| `python tools/governance/approvals.py hash <ID>` | Normative hash of an artifact |
| `python tools/governance/run_tests.py` | Run the tool tests and record E3 evidence |

## Conventions

IDs, front matter, normative fields, records, citations and commit trailers are defined in
`docs/governance/conventions.md`. Agent work is committed under the agent identity with an
`Agent: <name>` trailer; one commit per authoring agent.

## Memory

Claude Code's auto memory is enabled (DEC-0005). Its notes are convenience only: never evidence,
never decisions. When a memory note and a repository artifact disagree, the artifact wins.

## Escalate instead of guessing

Stop and escalate when a specification is incomplete or contradictory, when an accounting, tax or
security decision is needed, when evidence is missing or conflicting, or when progress would need a
control to be weakened. Agents escalate to the orchestrator; the orchestrator escalates to the
person named in the authority matrix.

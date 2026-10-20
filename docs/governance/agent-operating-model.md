---
id: GOV-OPERATING-MODEL
type: governance
title: Agent operating model
status: Proposed
version: 1
owner: orchestrator
links:
  decided_by: [DEC-0001, DEC-0002]
---

# Agent operating model

## Roles

**Orchestrator** (the main Claude Code session) is the only workflow coordinator. It opens workflow
records, dispatches agents, runs the governance tools, assembles decision briefs and approval
requests, commits validated work, and reports to people. It never approves, never writes decision
records, and never sets a status to Approved.

**Agents** (`.claude/agents/`) are stateless per invocation. They read the repository, write only
inside their scope, and return a handoff report. Subagents cannot ask people questions and cannot
start other agents; escalation always goes back through the orchestrator.

| Agent | Created | Writes | Shell |
| --- | --- | --- | --- |
| `requirements-engineer` (Requirements Steward) | F0 | `docs/requirements/` (not `assurance/`), `docs/changes/` | `trace`, `check`, read-only git |
| `requirements-assurance` | F0 | `docs/requirements/assurance/`, `ledger/reviews/` | `trace`, `check`, read-only git |
| `accounting-domain-expert` | F0 | `docs/accounting/`, `ledger/reviews/` | `trace`, `check`, read-only git |
| `code-security-reviewer` | F0 | `ledger/reviews/` | Read-only commands and the repository's own test suite |
| `solution-architect`, `technical-designer` | Gate A | `docs/architecture/` (not SRC-002), `docs/design/` | `trace`, `check`, read-only git |
| `ux-designer`, `quality-engineer`, `implementation-engineer`, `devops-release` | Gate B | Defined with the stack ADR | Defined with the stack ADR |

Scopes are enforced by `.claude/hooks/guard.py` using `.claude/hooks/agent-scopes.json`, and again at
commit time by the commit-msg check. Agents read and write only inside the repository and cannot
change directory. Their shell commands may name only paths inside the repository and may not use
command substitution, variables, brace or tilde expansion, background jobs, here-documents or
redirection; options that write files or run programs are blocked however they are quoted.
Built-in agents (Explore, Plan, general-purpose) may be used for read-only research inside the
repository; the guard blocks them from writing anywhere. The guard is a guardrail against mistakes and casual
misuse, not a security boundary: agents and people share one OS account until the git host exists
(RISK-003).

**People** decide, as listed in `docs/governance/authority-matrix.yaml`.

## Delegation

The orchestrator delegates with a task brief (`docs/governance/templates/task-brief.md`): task ID,
objective, inputs (IDs and paths), write scope, exclusions, acceptance criteria and required
verification. One brief, one agent, one scope.

Every agent ends with a handoff report (`docs/governance/templates/handoff-report.md`): what is done
and not done, files changed, IDs created, labelled assumptions, open questions, risks, citations, and
the checks it actually ran with their observed results.

## Validating a handoff

1. Compare the report with the brief's acceptance criteria.
2. Run `python tools/governance/check.py`.
3. Confirm with `git status` that nothing changed outside the agent's scope.
4. Route the work to its independent reviewer (below) before it goes into an approval request.
5. Commit the agent's work separately, with an `Agent:` trailer naming it.

Agent claims are not relayed as facts until verified. If a handoff fails validation, retry once with
a clarified brief, then escalate with the evidence.

## Independence

| Work | Reviewed by |
| --- | --- |
| Requirements and stories (Steward) | Requirements Assurance; Accounting Domain Expert for financial effect |
| Accounting knowledge (Accounting Domain Expert) | Requirements Assurance for consistency; the qualified accountant for normative entries |
| Framework code, hooks and tools | Code and Security Reviewer, then a person |

No agent reviews its own work. Reviews bind to the hash they reviewed; a normative change re-runs
every mandatory review on the diff.

## Concurrency

- One owner per authoritative artifact; others contribute through reviews and findings.
- Agents run in parallel only when their write scopes do not overlap.
- Records are one file each, so parallel work never conflicts on them.

## Workflow records and resuming

Each workflow (C1 to C8 in SRC-005) has a record in `ledger/workflows/` listing its steps and their
state. After an interruption, the orchestrator compares the record with the repository and resumes
from the last completed step. Approvals are never re-run; a missing decision means the step is still
pending.

## Disputes

When findings conflict, the orchestrator opens a dispute record (DSP) with each side's evidence.
Facts are settled by evidence or tests; policy questions go to the owner in the authority matrix.

## Intake

Issues are recorded in `docs/issues/`. When no session is running, nothing is triaged: incident
response is a human process, recorded afterwards. During L5 the orchestrator runs an intake sweep at
least daily.

## Memory

Claude Code's auto memory stays enabled (DEC-0005). Anything in it is a convenience note: it is never
evidence, never a decision, and never overrides a repository artifact. Per-agent memory stays off.

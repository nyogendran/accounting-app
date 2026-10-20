---
name: delegate
description: Delegate a task to one TIQACC agent with a complete task brief, then validate its handoff before anything is committed or sent for approval. Use whenever work goes to requirements-engineer, requirements-assurance, accounting-domain-expert or code-security-reviewer.
argument-hint: <agent> <objective>
---

# Delegate a task

1. **Pick one agent and one scope.** Check the agent's write scope in
   `.claude/hooks/agent-scopes.json`. Never give two agents overlapping scopes at the same time.
2. **Plan the workflow step.** The workflow record `ledger/workflows/WF-<ulid>.yaml` is written once,
   when the workflow ends (records are never rewritten; format in `docs/governance/conventions.md`).
   Generate its ID now so the briefs can cite it.
3. **Generate record IDs** the agent must create (reviews, issues):
   `python -c "from tools.governance import common; print('REV-' + common.new_ulid())"`.
4. **Write the brief** from `docs/governance/templates/task-brief.md`: objective, inputs (IDs and
   paths at versions), write scope, record IDs, exclusions, acceptance criteria, required checks,
   and when to escalate. Pass it as the agent's prompt.
5. **Validate the handoff** when the agent returns:
   - compare the report with each acceptance criterion;
   - run `python tools/governance/check.py`;
   - run `git status --short` and confirm nothing changed outside the agent's scope;
   - treat claims as unverified until you have checked them.
6. **Route to the independent reviewer** (see `docs/governance/agent-operating-model.md`,
   Independence) before the work goes into a decision brief.
7. **Commit the agent's work on its own**, under the agent identity, with an `Agent: <name>`
   trailer naming that agent.
8. If validation fails, retry once with a clarified brief, then escalate to the person named in the
   authority matrix with the evidence.

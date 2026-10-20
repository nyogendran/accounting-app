---
name: decision-brief
description: Prepare a one-page decision brief and a Stage 0 approval request for named TIQACC artifacts, and show the person the exact phrase to approve, reject or request changes. Use when an artifact is ready for a person's decision.
argument-hint: <artifact IDs> <role>
---

# Decision brief and approval request

1. **Check readiness first.** For requirements and stories run
   `python tools/governance/trace.py readiness <ID>`; every mandatory review must be bound to the
   current hash. For other artifacts, confirm the reviews named in
   `docs/governance/agent-operating-model.md` are done.
2. **Check the role** in `docs/governance/authority-matrix.yaml`. Stage 0 approvals (E1-op) cannot
   cover Tier 1; say so and stop if a subject is Tier 1.
3. **Write the brief** from `docs/governance/templates/decision-brief.md`, in plain language for a
   person who will not read diffs: the decision, options, recommendation, value and scope,
   accounting and technical implications, open items and the reviews. Save it under
   `docs/governance/briefs/` or show it in the conversation.
4. **Create the request:**
   `python tools/governance/approvals.py request --subject <ID> [--subject <ID>] --role <role>`.
   It pins each subject's version and normative hash and prints the phrases.
5. **Show the person the phrases exactly as printed** and explain that they must type one as the
   whole prompt. Do not type, paraphrase or confirm a decision on their behalf.
6. After they decide, the capture hook reports the recorded decision. Run
   `python tools/governance/approvals.py status <ID>` and only then set the artifact's status to
   Approved, if the state is `valid`.

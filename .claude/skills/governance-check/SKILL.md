---
name: governance-check
description: Run the TIQACC governance checks and tests, explain the findings, and fix or route them. Use after any change to governed files, before every commit, and before a gate.
---

# Governance check

1. Run `python tools/governance/check.py`. It validates artifacts (front matter, IDs, links,
   statuses, approval linkage), records, source fingerprints, and agent, skill and rule files.
2. For each error, name the file and the rule from `docs/governance/conventions.md` it breaks.
   - Fix it if the file is yours (orchestrator scope).
   - If an agent owns the file, delegate the fix to that agent.
   - Never fix an error by weakening the checker, editing a record, or editing a registered source.
3. Warnings: report them. Clause warnings disappear once the clause index exists.
4. When tools, hooks or settings changed, also run `python tools/governance/run_tests.py`; it records
   E3 evidence in `ledger/evidence/`.
5. Report the commands you ran and their actual output. Never report a check as passed without
   having seen its output.

---
paths:
  - "docs/**"
  - "ledger/**"
---

# Working on governed artifacts

- Front matter, IDs, link types and the normative block follow `docs/governance/conventions.md`.
  Meaning goes in `normative`; the body is explanation only.
- Never set a status to Approved yourself. It becomes Approved only after a captured decision on the
  current normative hash (`python tools/governance/approvals.py status <ID>` shows `valid`).
- Never edit a committed record under `ledger/`, a registered source under `docs/sources/SRC-*/` or
  `requirement-doc/`, or a decision record. Create a new record that references the old one.
- Cite evidence that resolves: IDs at versions, or quoted source passages with page numbers.
- Raise the version when normative content changes; the change voids existing approvals.
- After editing, the validate hook runs the checker on the file; fix every error it reports.

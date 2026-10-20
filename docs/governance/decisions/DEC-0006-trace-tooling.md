---
id: DEC-0006
type: decision
title: Build a thin trace index now; re-evaluate requirements-as-code tools at L5
status: Proposed
version: 1
owner: orchestrator
tier: 3
normative:
  decision: >-
    Build trace as a thin index over this repository's own formats (Markdown with YAML front matter,
    one-file-per-record ledgers). Re-evaluate Sphinx-Needs (lead candidate) and OpenFastTrace (code and
    test coverage) when L5 starts.
  conditions:
    - Keep IDs and link names stable.
    - Add a needs.json-compatible export before L5, so Sphinx-Needs could import without migrating sources.
    - Settle the code and test tag syntax at the start of L5.
links:
  related: [SRC-005]
---

# DEC-0006: Build a thin trace index now; re-evaluate tools at L5

SRC-005 (section F, F0) required a timeboxed evaluation of existing tools before building `trace`.
A research agent evaluated four tools on 2026-10-20 from their own documentation, without installing
anything. Its findings are agent output (E4); the decisive facts below cite the projects' pages.

| Tool | Reads our files as they are? | Typed links | Change detection | Code and test tracing | Runtime |
| --- | --- | --- | --- | --- | --- |
| [Doorstop](https://github.com/doorstop-dev/doorstop/blob/develop/docs/reference/item.md) 3.2 | Partly: imposes its own layout and rewrites item files | No | Suspect links by SHA-256; always includes the body | Weak | Python |
| [StrictDoc](https://strictdoc.readthedocs.io/en/latest/latest/spec/Markdown.html) 0.30.3 | No: its own format | Via roles | Git diff only | Good (experimental) | Python |
| [Sphinx-Needs](https://sphinx-needs.readthedocs.io/en/latest/changelog.html) 9.0.0 | No, but can import a generated `needs.json` | Yes, any number | Hash over chosen fields (new in 9.0.0, released 2026-10-14) | Good, with companion packages | Python and Sphinx |
| [OpenFastTrace](https://github.com/itsallcode/openfasttrace/blob/main/doc/user_guide/use_cases/writing_a_specification.md) 4.11.0 | No: its own ID syntax | Covers and Depends only | Manual revision bump | Best | Java 17 (not installed) |

**Why build now.** No tool reads the governed files as they are, so adopting one in F0 would mean
migrating artifacts and re-approving everything bound to their hashes. No tool computes this
framework's approval hash. The tools' real strength, code and test tracing, has nothing to work on
until L5.

**Unverified:** whether OpenFastTrace ignores YAML front matter; the behaviour of StrictDoc's file
content hash; the sphinx-codelinks marker syntax.

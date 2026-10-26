---
id: REV-01M5VGNKCZN7EBQY282X3KT1S0
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - commit: d83b392795df9261e4d01f52f3cb034ed2f15902
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [Fidelity, the most important finding] Values are written as stored, not as displayed. The
      docstring says so ("Cell values are read as stored"), but it does not say what that means for
      a reader. (a) Dates and times appear as serial numbers, for example 45000 rather than a date.
      (b) A number with a custom format loses the format, so an account code stored as the number 101
      and shown as 0101 appears as 101. Percentages, currency and thousands separators are lost too.
      (c) Doubles appear in their stored form, which can differ from the display, for example
      0.30000000000000004 or 1E-3. (d) Booleans appear as 0 and 1, not TRUE and FALSE. For a chart of
      accounts, (b) matters most: a search for a displayed code can miss it, and a quoted value can
      differ from what a person sees. No content is invented. The workbook stays authoritative, so this
      is a limit of the derived text, not a misrepresentation, provided it is stated. Recommendation:
      add a header line, for example "VALUES as stored: dates as serial numbers, no number formats,
      booleans 0/1", and repeat it in the register's derived note. Before registering, the orchestrator
      should check whether the workbook has numeric codes or dates with custom formats. If it does,
      render them (resolve s to styles.xml numFmtId) or flag them, instead of relying on the note.
    citation: >-
      tools/sources/extract_xlsx.py sha256 efd1e9be...af100b9 (uncommitted, on HEAD d83b392), lines
      5, 57-63 (else-branch emits value.text verbatim; styles.xml is never read)
  - severity: non-blocking
    text: >-
      [Fidelity, silent omissions and ambiguity] (a) A formula cell with no cached <v> is dropped
      without trace (line 63 gives None, line 64 skips it). Excel always caches results, but some
      generators do not. (b) Hidden and very hidden sheets are extracted with no marker, because the
      sheet state attribute is never read, so a reader cannot tell them from visible sheets. (c) Inside
      a cell, line breaks become " / " (line 65), and cells are joined with " | " (line 67). A cell
      whose own text contains " | " or " / " cannot be told apart from a column boundary or a line
      break. The column is then misread, but no text is lost. (d) OOXML escapes such as _x000D_ are
      not decoded and appear literally. (e) _text collects every <t> under <si>, including phonetic
      runs (rPh/t), so East Asian phonetic guides would be appended to the base text. (f) Merged
      cells carry their value only in the top-left cell, which is correct for search. (g)
      Whitespace-only cells are kept (" " is not in (None, "")), which is correct, but a cell made up
      only of line breaks becomes an empty column. None of these alter characters a search depends
      on, except (d). Recommendation: emit a STATE marker on hidden sheets, a marker for formula cells
      without a cached value, and decode _xHHHH_.
    citation: >-
      tools/sources/extract_xlsx.py lines 29-30, 49-53, 57-67, at sha256 efd1e9be...af100b9
  - severity: non-blocking
    text: >-
      [Correctness, package resolution] Each item below fails loudly unless marked as silent. (a)
      xl/workbook.xml and xl/sharedStrings.xml are hard-coded instead of being resolved through
      _rels/.rels and the workbook relationships. A generator that names the shared-strings part
      differently, for example xl/SharedStrings.xml, gives shared = [], and then the first
      shared-string cell raises IndexError. (b) Target resolution (lines 50-51) is right for the
      normal cases, the relative "worksheets/sheet1.xml" and the absolute "/xl/worksheets/sheet1.xml".
      It is wrong in two edge cases. A relative target that begins "xl/" is read as xl/... rather
      than xl/xl/... (silent: a different member is read). An absolute target outside xl/, such as
      "/worksheets/s.xml", is read under xl/ (silent if such a member exists, otherwise KeyError).
      "../" targets are not normalised (KeyError). These need a crafted or unusual file. (c) The r
      attribute is optional in the schema. A cell without r raises TypeError in _column (fail
      closed). A row without r prints "rNone" (silent loss of the row number). (d) A chartsheet, a
      dialogsheet or a Strict OOXML namespace makes find() return None, and iterating it raises
      TypeError (fail closed). (e) Duplicate cell references in a row overwrite each other silently.
      Multi-letter columns are correct (A=0, Z=25, AA=26, XFD=16383), and the sheet order follows
      workbook.xml, which is the tab order.
    citation: >-
      tools/sources/extract_xlsx.py lines 22-26, 38-41, 50-54, 65, 67, at sha256 efd1e9be...af100b9
  - severity: non-blocking
    text: >-
      [Security on untrusted input: what is and is not a real risk] Not a real risk: external entities
      (XXE). ElementTree on expat does not fetch external entities or DTDs. An undefined entity raises
      ParseError. Mitigated: entity expansion ("billion laughs"). The recorded interpreter is Python
      3.14.6 (EVD-01M5VBT1HMH76E5MJ54TPAGGZB), whose bundled expat has had amplification limits since
      expat 2.4.0. I could not observe the expat version, because my shell runs no ad hoc Python. If
      a system expat older than 2.4 were linked, expansion could exhaust memory, which is denial of
      service on the operator's machine only. Not a risk: zip-slip. Member names are only read, never
      used as output paths, and output is the operator's argument. Real but small: a zip bomb or a
      very large member. book.read() and ET.fromstring() decompress and parse each member in full,
      and source.read_bytes() loads the file, with no size cap. The worst outcome is memory exhaustion
      on a locally run, operator-invoked tool, with no write or escalation. A check of
      ZipInfo.file_size against a limit would close it. Low: line forgery. Cell text is safe, because
      splitlines() removes every line break. The sheet name (line 53) and row r (line 67) are written
      unsanitised, so a crafted file could put a line break in them and forge a "===== SHEET" or "rN:"
      line. Excel's interface does not allow it. Out of the tool's control: the derived text is read
      by agents, so workbook content can carry prompt-injection text. Agents must treat it as quoted
      data, as they treat any source.
    citation: >-
      tools/sources/extract_xlsx.py lines 34-41, 53-54, 65, 67, at sha256 efd1e9be...af100b9;
      ledger/evidence/EVD-01M5VBT1HMH76E5MJ54TPAGGZB.json "python": "3.14.6"
  - severity: non-blocking
    text: >-
      [Provenance and tests] (a) The EXTRACTOR header line names no version. Its sibling records
      "pdfplumber <version>", and this tool's behaviour is its own code. The register's produced_by
      for any derived file should therefore name the tool's commit, for example "tools/sources/
      extract_xlsx.py at <commit>, Python 3.14.6", and the tool should be committed before the derived
      file is registered. (b) There are no tests, which matches extract_pdf.py. The parsing rules
      above are easy to cover with synthetic workbooks built in a test (zipfile plus literal XML):
      multi-letter columns, rich-text and inline strings, a missing shared-strings part, absolute and
      relative targets, empty rows, and a hidden sheet. Recommended before it is reused for other
      sources. (c) Determinism: the code is deterministic for a given input and interpreter. Iteration
      follows document order and insertion-ordered dicts, there are no timestamps, and the output uses
      "\n" newlines. That agrees with the orchestrator's report of two byte-identical runs, which I
      did not observe myself.
    citation: >-
      tools/sources/extract_xlsx.py line 46; tools/sources/extract_pdf.py line 21;
      docs/sources/source-register.yaml lines 17-21 (SRC-001 derived entry); docs/governance/conventions.md
      lines 85-86
created_at: "2026-10-26"
---

# Review of tools/sources/extract_xlsx.py (uncommitted)

Independent E4 review for WF-01M5VGNKCZN7EBQY282X3KT1RZ step 1. The subject is the uncommitted file
`tools/sources/extract_xlsx.py`, sha256
`efd1e9bea3bbdab5bb467c44400aa6f36ff9622ebca4cc52e6b09b980af100b9`, in the working tree on HEAD
`d83b392795df9261e4d01f52f3cb034ed2f15902`. The checker accepts only an artifact ID or a commit as a
subject, so the front matter names HEAD, and this paragraph pins the file by hash. If the file changes
before it is committed, this review does not cover it.

**Verdict: non-blocking-findings.** All five findings are non-blocking. The tool reads only the zip
it is given, writes only the path the operator names, and fails closed (raises) on most malformed
input. It does not invent content. Its main limit is fidelity: values are written as stored, not as
displayed (finding 1). That should be stated in the output header and in the register's derived note
before the derived file is used to quote codes, dates or amounts. Whether that limit matters for this
particular workbook depends on its number formats, which I did not inspect.

## Acceptance criteria

| Criterion | Result |
| --- | --- |
| Column mapping, multi-letter | Correct (bijective base-26). A missing `r` attribute fails closed for cells and is silent for rows (finding 3c) |
| Shared strings, rich text | Correct: all `<t>` runs are concatenated. Phonetic runs are also included (finding 2e) |
| Inline strings, booleans, numbers, errors | Inline strings correct. `t="str"`, `t="e"` and `t="d"` are emitted as stored. Booleans appear as 0/1, numbers in stored form (finding 1) |
| Empty rows | Skipped, and row numbers keep their source values, so gaps stay traceable |
| Sheet order | `workbook.xml` `<sheets>` order, which is the tab order. Hidden sheets are not marked (finding 2b) |
| Target resolution | Correct for normal relative and absolute targets. Wrong for two unusual forms (finding 3b) |
| Deterministic output | Yes by construction (finding 5c) |
| Untrusted-input safety | Finding 4: XXE is not a risk, billion laughs is mitigated by the interpreter, and a zip bomb is a local denial of service only |

## Method

- I read `tools/sources/extract_xlsx.py` in full (76 lines) and `tools/sources/extract_pdf.py`
  (36 lines), the review template, the review rules in `docs/governance/conventions.md` (lines
  141-145), the source rules (lines 85-86), the SRC-001 derived entry in the source register, and
  the REV handling in `tools/governance/check.py` (lines 206-217).
- The brief allowed tests on synthetic .xlsx files, but I ran none. My shell profile
  (`review-readonly`) blocks ad hoc Python: the guard refused `python -I -c ...` and `python
  --version`. Every behaviour above comes from reading the code and the OOXML and ElementTree rules.
  I did not observe it. The Python version comes from the evidence record cited in finding 4.
- I did not open the business workbook, and I copied none of its content.

## Verification (observed)

- `git status --short`: ` M docs/governance/questions/Q-003.md`, `?? tools/sources/extract_xlsx.py`.
- `git rev-parse HEAD`: `d83b392795df9261e4d01f52f3cb034ed2f15902`.
- `sha256sum tools/sources/extract_xlsx.py`:
  `efd1e9bea3bbdab5bb467c44400aa6f36ff9622ebca4cc52e6b09b980af100b9`.
- `python tools/governance/check.py` before writing this record: `check: 0 error(s), 0 warning(s)`.
  The result after writing it is in the handoff report.

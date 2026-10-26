---
id: REV-01M5VGWKMQP88KF605MY3AZTRD
type: review
reviewer: code-security-reviewer
level: E4
subjects:
  - commit: d83b392795df9261e4d01f52f3cb034ed2f15902
verdict: non-blocking-findings
findings:
  - severity: non-blocking
    text: >-
      [Delta, finding 1 of REV-01M5VGNKCZN7EBQY282X3KT1S0: addressed as a disclosure] The new header
      line 47, "VALUES as stored, without number formats: dates as serial numbers, booleans as 0 or 1",
      is accurate and is always written, so every derived file carries it. "Without number formats"
      covers leading zeros, percentages, currency and separators. Two minor imprecisions remain. (a)
      Doubles in their stored form (for example 0.30000000000000004) are not mentioned. (b) Cells of
      type t="d" hold ISO 8601 text and appear as that text, not as serial numbers. Neither matters for
      this workbook if the orchestrator's observation holds: all 277 numeric cells use format id 0
      (General), and there are no boolean, error or str cells. I did not verify that observation,
      because I did not open the workbook. The module docstring (line 5) and the register's derived
      note do not yet repeat the limit. The note should repeat it when the file is registered.
    citation: >-
      tools/sources/extract_xlsx.py sha256 60b18d46...02a7218 (uncommitted, on HEAD d83b392), lines 5
      and 47; REV-01M5VGNKCZN7EBQY282X3KT1S0 finding 1
  - severity: non-blocking
    text: >-
      [Delta, finding 2b: closed; the rest of finding 2 stays open] Lines 53 and 55 read the sheet's
      state attribute, defaulting to "visible", and append " (hidden)" or " (veryHidden)" to the
      marker. An explicit state="visible" gets no suffix, which is correct. The suffix comes after the
      closing "=====", so the marker no longer always ends with "=====". No tool in the repository
      parses the marker: a Grep for "===== SHEET" finds only the extractor and my earlier review. Keep
      this in mind if one is written. The state value is written unsanitised, which is the same
      crafted-file line-forgery class as finding 4, and it adds no new class of risk. Still open from
      finding 2, all non-blocking: (a) a formula cell with no cached value is still dropped without a
      marker; the orchestrator observes that this workbook has none, which I did not verify. (c) the
      " | " and " / " separators are still ambiguous. (d) _xHHHH_ escapes are still not decoded. (e)
      phonetic runs are still appended. (g) a cell made up only of line breaks still becomes an empty
      column.
    citation: >-
      tools/sources/extract_xlsx.py lines 53, 55, 60-69, at sha256 60b18d46...02a7218;
      REV-01M5VGNKCZN7EBQY282X3KT1S0 finding 2
  - severity: non-blocking
    text: >-
      [Open and unchanged] Findings 3 (package resolution), 4 (untrusted-input safety) and 5
      (provenance and tests) of REV-01M5VGNKCZN7EBQY282X3KT1S0 are untouched by this delta and stay
      non-blocking. Before the derived file is registered: commit the tool first, and name that
      commit and Python 3.14.6 in produced_by (finding 5a). The EXTRACTOR line still names no
      version.
    citation: >-
      tools/sources/extract_xlsx.py lines 22-26, 34-41, 46, 51-52, 69, at sha256 60b18d46...02a7218;
      REV-01M5VGNKCZN7EBQY282X3KT1S0 findings 3, 4 and 5
created_at: "2026-10-26"
---

# Delta review of tools/sources/extract_xlsx.py (uncommitted)

Independent E4 delta review for WF-01M5VGNKCZN7EBQY282X3KT1RZ step 2. It supplements
REV-01M5VGNKCZN7EBQY282X3KT1S0 and does not replace it.

The subject is the uncommitted file `tools/sources/extract_xlsx.py`, sha256
`60b18d4673bb66d5de38eea3f652020eb96203df0163838971b17f2fa02a7218`, in the working tree on HEAD
`d83b392795df9261e4d01f52f3cb034ed2f15902`. The previous version had sha256
`efd1e9bea3bbdab5bb467c44400aa6f36ff9622ebca4cc52e6b09b980af100b9`. As in the first record, the front
matter names HEAD because the checker accepts only an artifact ID or a commit. The file is pinned by
its hash here.

**Verdict: non-blocking-findings.** I read the whole file and compared it with the version I
reviewed. The delta is exactly the two changes described in the request:

- the new header line 47;
- the state lookup and marker suffix, lines 53 and 55.

Nothing else changed: the remaining lines are identical, two lines further down. The delta introduces
no defect. Finding 1 is addressed as a disclosure, finding 2b is closed, and the rest of finding 2
and findings 3 to 5 stay open and non-blocking.

## Method and verification (observed)

- `sha256sum tools/sources/extract_xlsx.py`:
  `60b18d4673bb66d5de38eea3f652020eb96203df0163838971b17f2fa02a7218`.
- `git rev-parse HEAD`: `d83b392795df9261e4d01f52f3cb034ed2f15902`.
- Grep for `===== SHEET|SHEETS |VALUES as stored` in the repository: only
  `tools/sources/extract_xlsx.py` and `ledger/reviews/REV-01M5VGNKCZN7EBQY282X3KT1S0.md`.
- I ran no code. My shell profile blocks ad hoc Python. I did not open the workbook. Statements about
  its formats and sheets are the orchestrator's observation.
- `python tools/governance/check.py`: reported in the handoff.

"""List the S1 clause references in V1-based artifacts that must be re-read, not only re-pointed, when
re-basing on SRC-007. Read-only; writes one YAML file given as the first argument.

A sub-section is "touched" when SRC-007 added a clause to it, or holds a changed or successor clause
in it (crosswalk v2). A sub-section is "cited" when a new, changed or successor S7 clause names it by
number ("2.12", "2.15.8"); a level-2 citation such as "2.12" cites every sub-section under it. A
reference is listed when its clause is itself not plain "same", or its sub-section is touched or cited.
This widens the re-read set of GOV-IMPACT-SRC007 v2 as REV-01M5W2PMREVQFW5TCYYJQ1K1D6 recommends.

Usage: python tools/sources/reread_refs.py <output.yaml>
"""
import collections
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(r"C:\yogi\tiq-accounting-app")
SKIP = re.compile(r"^(Page \d+ of \d+|===== PAGE \d+ =====)$")
S1_ID = re.compile(r"S1-\d+(?:\.\d+)*-c\d{2,3}")
SECTION_REF = re.compile(r"(?<![\w.\-])(2\.\d{1,2}(?:\.\d{1,2})?)(?![\w\-]|\.\d)")

crosswalk = yaml.safe_load((ROOT / "docs/requirements/crosswalk-src001-to-src007.yaml").read_text(encoding="utf-8"))
index7 = yaml.safe_load((ROOT / "docs/requirements/clause-index-src007.yaml").read_text(encoding="utf-8"))["clauses"]
lines7 = (ROOT / "docs/sources/SRC-007-spec-v2.2/extracted/spec-v2.2.txt").read_text(encoding="utf-8").split("\n")
section7 = {c["id"]: str(c["section"]) for c in index7}
all_sections = sorted(set(section7.values()))

status1 = collections.defaultdict(set)
to7 = collections.defaultdict(list)
for pair in crosswalk["pairs"]:
    status1[pair["s1"]].add(pair["status"])
    to7[pair["s1"]].append(pair["s7"])
moved = {p["s7"] for p in crosswalk["pairs"] if p["status"] != "same"} | set(crosswalk["new"])
touched = {section7[i] for i in moved}

cited = set()
for clause in index7:
    if clause["id"] not in moved:
        continue
    a, b = clause["lines"][0], clause["lines"][-1]
    text = " ".join(l for l in lines7[a - 1:b] if not SKIP.match(l.strip()))
    for number in SECTION_REF.findall(text):
        cited.update(s for s in all_sections if s == number or s.startswith(number + "."))

files = [ROOT / "docs/requirements/bracketed-values.yaml", ROOT / "docs/requirements/actors.yaml",
         ROOT / "docs/requirements/glossary.yaml", ROOT / "docs/requirements/release-phasing.yaml"]
files += sorted((ROOT / "docs/requirements/objectives").glob("BO-*.md"))
files += sorted((ROOT / "docs/governance/questions").glob("Q-*.md"))
rows, per_file, per_reason = [], collections.Counter(), collections.Counter()
total = 0
for path in files:
    for ref in S1_ID.findall(path.read_text(encoding="utf-8")):
        total += 1
        section = ref[3:].rsplit("-c", 1)[0]
        reasons = []
        if status1.get(ref, {"same"}) != {"same"}:
            reasons.append("clause " + "/".join(sorted(status1[ref])))
        if section in touched:
            reasons.append("sub-section touched")
        if section in cited:
            reasons.append("sub-section cited by a new or changed clause")
        if reasons:
            rel = path.relative_to(ROOT).as_posix()
            rows.append({"file": rel, "s1": ref, "s7": to7.get(ref, []), "reasons": reasons})
            per_file[rel] += 1
            for r in reasons:
                per_reason[r] += 1

doc = {
    "version": 1,
    "method": (__doc__ or "").strip(),
    "counts": {"references": total, "to_re_read": len(rows), "by_reason": dict(sorted(per_reason.items())),
               "by_file": dict(sorted(per_file.items())), "touched_subsections": sorted(touched),
               "cited_subsections": sorted(cited)},
    "references": rows,
}
Path(sys.argv[1]).write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8", newline="\n")
print({k: v for k, v in doc["counts"].items() if k in ("references", "to_re_read", "by_reason")})
print("touched:", len(touched), "cited:", len(cited))

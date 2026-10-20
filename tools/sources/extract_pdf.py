"""Extract the text of a PDF source into a UTF-8 text file for search.

The PDF stays authoritative; the extraction is a derived artifact. Each page is
preceded by a marker line so that a quoted clause can be traced to its page.

Usage: python tools/sources/extract_pdf.py <source.pdf> <output.txt>
"""
import hashlib
import sys
from pathlib import Path

import pdfplumber


def extract(source: Path, output: Path) -> None:
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    with pdfplumber.open(source) as pdf:
        lines = [
            f"SOURCE {source.name}",
            f"SOURCE_SHA256 {digest}",
            f"EXTRACTOR pdfplumber {pdfplumber.__version__}",
            f"PAGES {len(pdf.pages)}",
        ]
        for number, page in enumerate(pdf.pages, start=1):
            lines.append("")
            lines.append(f"===== PAGE {number} =====")
            lines.append(page.extract_text() or "")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: extract_pdf.py <source.pdf> <output.txt>")
    extract(Path(sys.argv[1]), Path(sys.argv[2]))

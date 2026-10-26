"""Extract the cell values of an .xlsx source into a UTF-8 text file for search.

The workbook stays authoritative; the extraction is a derived artifact. Each sheet is preceded by a
marker line and each row by its row number, so a quoted cell can be traced to its sheet and row.
Cell values are read as stored (the cached result of a formula, not the formula). Only the standard
library is used.

Usage: python tools/sources/extract_xlsx.py <source.xlsx> <output.txt>
"""
import hashlib
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_ID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
NS = {"m": MAIN}


def _column(reference: str) -> int:
    number = 0
    for letter in re.match(r"[A-Z]+", reference).group(0):
        number = number * 26 + ord(letter) - 64
    return number - 1


def _text(element) -> str:
    return "".join(node.text or "" for node in element.iter(f"{{{MAIN}}}t"))


def extract(source: Path, output: Path) -> None:
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    with zipfile.ZipFile(source) as book:
        names = book.namelist()
        shared = []
        if "xl/sharedStrings.xml" in names:
            shared = [_text(item) for item in ET.fromstring(book.read("xl/sharedStrings.xml")).findall("m:si", NS)]
        workbook = ET.fromstring(book.read("xl/workbook.xml"))
        targets = {rel.get("Id"): rel.get("Target") for rel in ET.fromstring(book.read("xl/_rels/workbook.xml.rels"))}
        sheets = workbook.find("m:sheets", NS)
        lines = [
            f"SOURCE {source.name}",
            f"SOURCE_SHA256 {digest}",
            "EXTRACTOR tools/sources/extract_xlsx.py (standard library)",
            "VALUES as stored, without number formats: dates as serial numbers, booleans as 0 or 1",
            f"SHEETS {len(sheets)}",
        ]
        for sheet in sheets:
            target = targets[sheet.get(REL_ID)].lstrip("/")
            target = target if target.startswith("xl/") else "xl/" + target
            state = sheet.get("state", "visible")
            lines.append("")
            lines.append(f"===== SHEET {sheet.get('name')} =====" + ("" if state == "visible" else f" ({state})"))
            for row in ET.fromstring(book.read(target)).find("m:sheetData", NS):
                cells = {}
                for cell in row:
                    value = cell.find("m:v", NS)
                    if cell.get("t") == "s" and value is not None:
                        text = shared[int(value.text)]
                    elif cell.get("t") == "inlineStr":
                        text = _text(cell)
                    else:
                        text = value.text if value is not None else None
                    if text not in (None, ""):
                        cells[_column(cell.get("r"))] = " / ".join(text.splitlines())
                if cells:
                    lines.append(f"r{row.get('r')}: " + " | ".join(cells.get(i, "") for i in range(max(cells) + 1)))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: extract_xlsx.py <source.xlsx> <output.txt>")
    extract(Path(sys.argv[1]), Path(sys.argv[2]))

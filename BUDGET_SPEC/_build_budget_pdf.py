#!/usr/bin/env python3
"""Build Bhadravati_Budget_Build_Spec.pdf from BUDGET_SPEC/*.md (in file order)."""
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (HRFlowable, PageBreak, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

ROOT = Path(__file__).parent
FILES = ["00_SPEC_LOCKED_BASE.md", "01_furniture.md", "02_wood_joinery.md",
         "03_electrical.md", "04_utilities.md", "05_envelope.md",
         "06_MASTER_BUY_LIST.md", "07_paint.md"]
OUT = ROOT.parent / "Bhadravati_Budget_Build_Spec.pdf"

# Helvetica (WinAnsi) lacks these glyphs — normalize.
SUBS = {"₹": "Rs ", "≈": "~", "→": "->", "✅": "[OK]", "🏆": "*",
        "⚠️": "(!)", "×": "x", "·": "-", "–": "-", "—": "-",
        "≥": ">=", "≤": "<=", "″": "in", "³": "3", "²": "2"}


def clean(s: str) -> str:
    for k, v in SUBS.items():
        s = s.replace(k, v)
    return s


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def rich(s: str) -> str:
    """markdown inline -> reportlab markup"""
    s = esc(clean(s))
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"`([^`]+)`", r"<font face='Courier' size='8'>\1</font>", s)
    return s


H1 = ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=16, leading=20,
                    spaceBefore=6, spaceAfter=8, textColor=colors.HexColor("#3d3630"))
H2 = ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=11.5, leading=15,
                    spaceBefore=10, spaceAfter=4, textColor=colors.HexColor("#5a4f43"))
BODY = ParagraphStyle("Body", fontName="Helvetica", fontSize=9, leading=12.5,
                      alignment=TA_LEFT, spaceAfter=4)
CELL = ParagraphStyle("Cell", fontName="Helvetica", fontSize=7.8, leading=9.8)
CELLH = ParagraphStyle("CellH", fontName="Helvetica-Bold", fontSize=7.8, leading=9.8)
LI = ParagraphStyle("Li", parent=BODY, leftIndent=10, bulletIndent=2)

ACCENT = colors.HexColor("#8a7968")
GRID = colors.HexColor("#d8d0c6")
ALT = colors.HexColor("#f4f0ea")


def make_table(rows):
    data = []
    for i, r in enumerate(rows):
        st = CELLH if i == 0 else CELL
        data.append([Paragraph(rich(c), st) for c in r])
    t = Table(data, repeatRows=1, colWidths=None)
    style = [("BACKGROUND", (0, 0), (-1, 0), ACCENT),
             ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
             ("GRID", (0, 0), (-1, -1), 0.4, GRID),
             ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("TOPPADDING", (0, 0), (-1, -1), 2.5),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
             ("LEFTPADDING", (0, 0), (-1, -1), 3.5),
             ("RIGHTPADDING", (0, 0), (-1, -1), 3.5)]
    for r in range(2, len(rows), 2):
        style.append(("BACKGROUND", (0, r), (-1, r), ALT))
    t.setStyle(TableStyle(style))
    return t


story = []
for fname in FILES:
    path = ROOT / fname
    lines = clean(path.read_text()).split("\n")
    title_done = False
    tbl = []

    def flush():
        if tbl:
            story.append(make_table(tbl))
            story.append(Spacer(1, 6))
            tbl.clear()

    for ln in lines:
        ln = ln.rstrip()
        if re.match(r"^\|.*\|\s*$", ln):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                tbl.append(cells)
            continue
        flush()
        if not ln.strip():
            continue
        if ln.startswith("## Sources") or ln.startswith("## Citation"):
            continue  # per-file source lists stay in .md
        if ln.startswith("# "):
            if story:
                story.append(PageBreak())
            story.append(Paragraph(rich(ln[2:]), H1))
        elif ln.startswith("## "):
            story.append(Paragraph(rich(ln[3:]), H2))
        elif ln.strip() == "---":
            story.append(Spacer(1, 4))
            story.append(HRFlowable(width="100%", thickness=0.6, color=GRID))
            story.append(Spacer(1, 4))
        elif re.match(r"^\s*[-*] ", ln):
            story.append(Paragraph(rich(re.sub(r"^\s*[-*] ", "", ln)), LI, bulletText="•"))
        else:
            m_num = re.match(r"^\s*(\d+)\. ", ln)
            if m_num:
                story.append(Paragraph(rich(ln[m_num.end():]), LI, bulletText=f"{m_num.group(1)}."))
            else:
                story.append(Paragraph(rich(ln), BODY))
    flush()

doc = SimpleDocTemplate(str(OUT), pagesize=A4,
                        leftMargin=14 * mm, rightMargin=14 * mm,
                        topMargin=13 * mm, bottomMargin=13 * mm,
                        title="Bhadravati Budget Build Spec",
                        author="ox-alpha agent pass")

def footer(canv, _doc):
    canv.saveState()
    canv.setFont("Helvetica", 7)
    canv.setFillColor(colors.HexColor("#8a8378"))
    canv.drawString(14 * mm, 8 * mm,
                    "Bhadravati Budget Build Spec - EST prices, verify locally - not fabrication-approved")
    canv.drawRightString(A4[0] - 14 * mm, 8 * mm, f"Page {canv.getPageNumber()}")
    canv.restoreState()


doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f"WROTE {OUT} ({OUT.stat().st_size} bytes)")

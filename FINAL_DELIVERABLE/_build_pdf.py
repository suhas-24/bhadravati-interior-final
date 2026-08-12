#!/usr/bin/env python3
"""Generate Bhadravati FINAL Interior Design client handoff PDF."""
from __future__ import annotations

import os
from datetime import date
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib.colors import Color, HexColor, white, black
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether,
    HRFlowable,
    ListFlowable,
    ListItem,
)

ROOT = Path(__file__).resolve().parent
VIS = ROOT / "_pdf_assets" / "img"
VIS_ORIG = ROOT / "visuals"
ASSETS = ROOT / "_pdf_assets"
OUT = ROOT / "Bhadravati_FINAL_Interior_Design.pdf"

# Brand palette
NN9074 = HexColor("#B5AB9C")
WW0005 = HexColor("#EEEDE9")
NN9088 = HexColor("#E9E3D9")
WW0020 = HexColor("#EDE9E2")
LATTE = HexColor("#C8B9A4")
SLATE = HexColor("#4E4C49")
IDRIA = HexColor("#3D483C")
INK = HexColor("#2C2A26")
MUTED = HexColor("#5C574F")
RULE = HexColor("#D4CEC4")
WARM_BG = HexColor("#F7F4EF")
ACCENT = HexColor("#6B5E4E")

PAGE_W, PAGE_H = A4
MARGIN = 16 * mm


def swatch_row():
    labels = [
        ("NN9074", "A · Puddle Grey", "#B5AB9C"),
        ("WW0005", "A · White Linen", "#EEEDE9"),
        ("NN9088", "B · Ecru Tint", "#E9E3D9"),
        ("WW0020", "B · Virgin White", "#EDE9E2"),
        ("S1241", "Latte MT", "#C8B9A4"),
    ]
    cells = []
    for code, name, hx in labels:
        c = HexColor(hx)
        border = HexColor("#C8C2B8") if hx.upper() in ("#EEEDE9", "#C8B9A4", "#B5AB9C") else HexColor("#3A3834")
        inner = Table(
            [
                [""],
                [Paragraph(f"<b>{code}</b><br/><font size='7'>{name}</font>", ParagraphStyle(
                    "sw", fontName="Helvetica", fontSize=8, leading=10, textColor=INK if hx.upper() not in ("#4E4C49",) else white, alignment=TA_CENTER
                ))],
            ],
            colWidths=[32 * mm],
            rowHeights=[18 * mm, 12 * mm],
        )
        inner.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (0, 0), c),
                    ("BACKGROUND", (0, 1), (0, 1), WARM_BG if hx.upper() != "#4E4C49" else SLATE),
                    ("BOX", (0, 0), (-1, -1), 0.5, border),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("TOPPADDING", (0, 1), (0, 1), 3),
                    ("BOTTOMPADDING", (0, 1), (0, 1), 3),
                ]
            )
        )
        # Fix text on dark slate label row
        if hx.upper() == "#4E4C49":
            inner.setStyle(TableStyle([("TEXTCOLOR", (0, 1), (0, 1), white)]))
        cells.append(inner)
    t = Table([cells], colWidths=[34 * mm] * 5)
    t.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER"), ("LEFTPADDING", (0, 0), (-1, -1), 2), ("RIGHTPADDING", (0, 0), (-1, -1), 2)]))
    return t


def fit_image(path: Path, max_w: float, max_h: float) -> Image:
    with PILImage.open(path) as im:
        w, h = im.size
    scale = min(max_w / w, max_h / h)
    return Image(str(path), width=w * scale, height=h * scale)


def header_footer(canv: canvas.Canvas, doc):
    canv.saveState()
    canv.setFillColor(NN9074)
    canv.rect(0, PAGE_H - 3.5 * mm, PAGE_W, 3.5 * mm, fill=1, stroke=0)
    canv.setFillColor(SLATE)
    canv.rect(0, 0, PAGE_W, 3.5 * mm, fill=1, stroke=0)
    if doc.page > 1:
        canv.setFont("Helvetica", 8)
        canv.setFillColor(MUTED)
        canv.drawString(MARGIN, 6.5 * mm, "Bhadravati — Warm Contemporary Minimalism | FINAL design control")
        canv.drawRightString(PAGE_W - MARGIN, 6.5 * mm, f"{doc.page}")
    canv.restoreState()


def cover_footer(canv: canvas.Canvas, doc):
    canv.saveState()
    canv.setFillColor(NN9074)
    canv.rect(0, PAGE_H - 3.5 * mm, PAGE_W, 3.5 * mm, fill=1, stroke=0)
    canv.setFillColor(SLATE)
    canv.rect(0, 0, PAGE_W, 3.5 * mm, fill=1, stroke=0)
    canv.restoreState()


def build():
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleCover",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=26,
        leading=32,
        textColor=INK,
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    subtitle = ParagraphStyle(
        "SubCover",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=MUTED,
        alignment=TA_CENTER,
        spaceAfter=6,
    )
    h1 = ParagraphStyle(
        "H1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=INK,
        spaceBefore=4,
        spaceAfter=8,
    )
    h2 = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=ACCENT,
        spaceBefore=8,
        spaceAfter=4,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        textColor=INK,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    )
    small = ParagraphStyle(
        "Small",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=11,
        textColor=MUTED,
        alignment=TA_CENTER,
    )
    caption = ParagraphStyle(
        "Cap",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=8,
        leading=10,
        textColor=MUTED,
        alignment=TA_CENTER,
        spaceBefore=3,
        spaceAfter=8,
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        textColor=INK,
        leftIndent=4,
        spaceAfter=3,
    )
    cell = ParagraphStyle(
        "Cell",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=10,
        textColor=INK,
    )
    cell_b = ParagraphStyle(
        "CellB",
        parent=cell,
        fontName="Helvetica-Bold",
    )

    content_w = PAGE_W - 2 * MARGIN
    story = []

    # ——— COVER ———
    story.append(Spacer(1, 28 * mm))
    story.append(Paragraph("BHADRAVATI HOME", ParagraphStyle("brand", parent=subtitle, fontSize=11, textColor=ACCENT, fontName="Helvetica-Bold", spaceAfter=14)))
    story.append(Paragraph("Warm Contemporary Minimalism", title))
    story.append(Paragraph("FINAL Interior Design Package", ParagraphStyle("t2", parent=title, fontSize=16, leading=20, spaceAfter=14)))
    story.append(HRFlowable(width="60%", thickness=1, color=NN9074, spaceBefore=4, spaceAfter=14, hAlign="CENTER"))
    story.append(Paragraph("First-floor studio · Bhadravati, Karnataka", subtitle))
    story.append(Paragraph("Client handoff · Design control (not fabrication-approved)", subtitle))
    story.append(Spacer(1, 8 * mm))

    # Cover hero image
    living = VIS / "01_living_social_zone_daylight.jpg"
    if living.exists():
        story.append(fit_image(living, content_w, 95 * mm))
        story.append(Paragraph("Living — social zone (daylight concept)", caption))

    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph(f"Generated {date.today().isoformat()} · Dual paint schemes A/B · live gallery toggle · coordination: integration_complete", small))
    story.append(PageBreak())

    # ——— DESIGN DIRECTION ———
    story.append(Paragraph("1. Design direction summary", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=8))
    story.append(Paragraph(
        "The home will feel calm, practical, and locally believable — not a pale decorative showroom "
        "and not textbook Japandi. Architecture and usable circulation come before styling.",
        body,
    ))
    story.append(Paragraph(
        "<b>Problems solved:</b> dust/smoke visibility; hard-water streaking; monsoon humidity at wet joinery; "
        "glare under strong daylight; repairability; and prior visual QA failures (wrong openings, flipped kitchen, "
        "invented cabinetry, false gloss, unsafe clearances, climate-mismatched props).",
        body,
    ))
    story.append(Paragraph("Non-negotiables", h2))
    for item in [
        "Existing <b>black granite</b> kitchen remains; <b>shutters only</b>.",
        "Kitchen base + drawers + loft = <b>Century S1241 MT Latte</b> only.",
        "Hardware = <b>brushed stainless recessed</b> pulls (J-pull / finger-pull) — no projecting bars.",
        "Lighting = <b>3000 K</b> warm-neutral baseline; finishes = <b>matte / low-sheen</b>.",
        "No TV feature wall, island, L-kitchen flip, gold strips, slatted Japandi props, or gloss laminates.",
    ]:
        story.append(Paragraph(f"• {item}", bullet))

    story.append(Paragraph("Concept decision", h2))
    concept_data = [
        [Paragraph("<b>Concept</b>", cell_b), Paragraph("<b>Decision</b>", cell_b)],
        [Paragraph("A — Warm Contemporary Minimalism (NN9074 + Latte kitchen + Idria wardrobe)", cell), Paragraph("<b>FINAL</b>", cell_b)],
        [Paragraph("B — Textbook Japandi", cell), Paragraph("Reject as governing style", cell)],
        [Paragraph("C — Dual-tone kitchen / lighter default walls", cell), Paragraph("Reject", cell)],
    ]
    ct = Table(concept_data, colWidths=[125 * mm, 45 * mm])
    ct.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NN9074),
        ("BACKGROUND", (0, 1), (-1, 1), HexColor("#EDE8E0")),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(ct)
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "Studio relationship (plan evidence only): ≈ <b>21 × 18 ft (6401 × 5486 mm)</b>. "
        "Zones: Bedroom SW · Living S-centre · Kitchen SE · Bathroom NW · Wardrobe N-centre · Study NE.",
        body,
    ))
    story.append(PageBreak())

    # ——— PALETTE ———
    story.append(Paragraph("2. Locked palette &amp; finishes", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=8))
    story.append(Paragraph(
        "Two locked <b>paint schemes</b> for walls/ceilings; laminates and hardware stay constant. "
        "The live gallery at GitHub Pages includes a sticky <b>Paint scheme</b> toggle (Scheme A / Scheme B) — "
        "preference persists in localStorage; URL hashes <b>#scheme-a</b> / <b>#scheme-b</b> also work. "
        "Screen hex values are approximate — approve physical chips beside granite under morning / afternoon / 3000 K light.",
        body,
    ))
    story.append(swatch_row())
    story.append(Spacer(1, 3 * mm))

    pal_data = [
        [Paragraph("<b>Role</b>", cell_b), Paragraph("<b>Code / product</b>", cell_b), Paragraph("<b>Notes</b>", cell_b)],
        [Paragraph("Scheme A walls (default)", cell), Paragraph("Birla Opus <b>NN9074</b> Puddle of Grey", cell), Paragraph("#B5AB9C · mid warm greige", cell)],
        [Paragraph("Scheme A ceiling", cell), Paragraph("Birla Opus <b>WW0005</b> White Linen", cell), Paragraph("#EEEDE9 · warm linen white", cell)],
        [Paragraph("Scheme B walls", cell), Paragraph("Birla Opus <b>NN9088</b> Ecru Tint", cell), Paragraph("#E9E3D9 · lighter warm ecru", cell)],
        [Paragraph("Scheme B ceiling", cell), Paragraph("Birla Opus <b>WW0020</b> Virgin White", cell), Paragraph("#EDE9E2 · cleaner warm white", cell)],
        [Paragraph("Kitchen shutters (all)", cell), Paragraph("Century <b>S1241 MT Latte</b>", cell), Paragraph("One code only; matte", cell)],
        [Paragraph("TV cabinet", cell), Paragraph("<b>80236</b> DW Slate Grey (or Latte)", cell), Paragraph("Controlled accent", cell)],
        [Paragraph("Wardrobe face", cell), Paragraph("<b>84689 SU Idria Oak</b> (backup 84687 Lyon) / plywood Option B", cell), Paragraph("Soft woodgrain", cell)],
        [Paragraph("Hardware", cell), Paragraph("Brushed stainless <b>recessed</b> pulls", cell), Paragraph("Kitchen + wardrobe; no bar handles", cell)],
        [Paragraph("Wardrobe doors", cell), Paragraph("<b>3 doors</b> — leaves <b>457 / 457 / 458 mm</b>", cell), Paragraph("1 single L + 1 double R inside 1372 mm clear", cell)],
        [Paragraph("Counter", cell), Paragraph("Existing <b>black granite</b>", cell), Paragraph("Retain; shutters only", cell)],
    ]
    pt = Table(pal_data, colWidths=[32 * mm, 78 * mm, 60 * mm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), SLATE),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, HexColor("#F3EFE8")]),
        ("GRID", (0, 0), (-1, -1), 0.35, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(pt)
    story.append(Spacer(1, 4 * mm))

    pal_img = ASSETS / "img" / "palette_board.jpg"
    if pal_img.exists():
        story.append(fit_image(pal_img, content_w, 78 * mm))
        story.append(Paragraph("Palette board (locked codes)", caption))
    story.append(PageBreak())

    # ——— DIMENSIONS ———
    story.append(Paragraph("3. Key dimensions — K-01 / W-01", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=8))
    story.append(Paragraph(
        "Clear openings are the design baseline until a signed site measure supersedes them. "
        "Granite thickness conflict on drawing (1.50 in vs 15 mm) — measure stone on site.",
        body,
    ))
    story.append(Paragraph("Kitchen register (K-01)", h2))
    k_data = [
        [Paragraph("<b>Item</b>", cell_b), Paragraph("<b>in</b>", cell_b), Paragraph("<b>mm</b>", cell_b)],
        [Paragraph("Module width", cell), Paragraph("106.00", cell), Paragraph("2692", cell)],
        [Paragraph("Ref. wall width", cell), Paragraph("220.00", cell), Paragraph("5588", cell)],
        [Paragraph("Floor → loft underside", cell), Paragraph("102.00", cell), Paragraph("2591", cell)],
        [Paragraph("Loft → lower shelf underside", cell), Paragraph("48.00", cell), Paragraph("1219", cell)],
        [Paragraph("Shelf underside → counter top", cell), Paragraph("23.00", cell), Paragraph("584", cell)],
        [Paragraph("Floor → counter top", cell), Paragraph("31.00", cell), Paragraph("787", cell)],
        [Paragraph("Internal counter depth", cell), Paragraph("19.20", cell), Paragraph("488", cell)],
        [Paragraph("B1 / B2 / B3 clear", cell), Paragraph("48 / 36 / 18", cell), Paragraph("1219 / 914 / 457", cell)],
    ]
    kt = Table(k_data, colWidths=[90 * mm, 40 * mm, 40 * mm])
    kt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NN9074),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, HexColor("#F3EFE8")]),
        ("GRID", (0, 0), (-1, -1), 0.35, RULE),
        ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.append(kt)

    story.append(Paragraph("Wardrobe register (W-01)", h2))
    w_data = [
        [Paragraph("<b>Item</b>", cell_b), Paragraph("<b>in</b>", cell_b), Paragraph("<b>mm</b>", cell_b)],
        [Paragraph("Clear W × H × D", cell), Paragraph("54 × 90 × 19.20", cell), Paragraph("1372 × 2286 × 488", cell)],
        [Paragraph("Left / partition / right", cell), Paragraph("21 / 0.59 / 32.41", cell), Paragraph("533 / 15 / 823", cell)],
        [Paragraph("Three vertical leaves", cell), Paragraph("1 single + 1 double", cell), Paragraph("<b>457 / 457 / 458</b>", cell)],
        [Paragraph("Left openings T→B", cell), Paragraph("12 + 4×19.5", cell), Paragraph("305 + 4×495", cell)],
        [Paragraph("Right stack", cell), Paragraph("12 / 39 hang / 9.5 / 12 / 17.5", cell), Paragraph("305 / 991 / 241 / 305 / 445", cell)],
    ]
    wt = Table(w_data, colWidths=[70 * mm, 50 * mm, 50 * mm])
    wt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), SLATE),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, HexColor("#F3EFE8")]),
        ("GRID", (0, 0), (-1, -1), 0.35, RULE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.append(wt)
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "Circulation targets: primary 900–1200 mm · secondary 600–900 mm · sofa–coffee 450–500 mm · "
        "bed sides ≥600 mm · wardrobe standing clear ≥600 mm (prefer 900 if primary aisle).",
        body,
    ))
    story.append(PageBreak())

    # ——— FLOOR PLAN ———
    story.append(Paragraph("4. Floor plan", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    fp = ASSETS / "img" / "floor_plan_precise.jpg"
    if fp.exists():
        story.append(fit_image(fp, content_w, 175 * mm))
        story.append(Paragraph("Scale-true dimensioned floor plan (relational; not a cut sheet)", caption))
    story.append(PageBreak())

    # ——— LIVING ———
    story.append(Paragraph("5. Living — concept views", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    for path, cap in [
        (VIS / "01_living_social_zone_daylight.jpg", "Living — social zone, daylight"),
        (VIS / "01b_living_from_tv_toward_sofa.jpg", "Living — from TV toward sofa"),
    ]:
        if path.exists():
            story.append(fit_image(path, content_w, 95 * mm))
            story.append(Paragraph(cap, caption))
    story.append(PageBreak())

    # ——— KITCHEN ———
    story.append(Paragraph("6. Kitchen — granite + Latte shutters", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "Existing black granite retained. All shutters Century S1241 MT Latte with recessed brushed stainless pulls.",
        body,
    ))
    for path, cap in [
        (VIS / "02_kitchen_granite_latte_shutters.jpg", "Kitchen — granite with Latte shutters"),
        (VIS / "02b_kitchen_from_fridge_along_run.jpg", "Kitchen — from fridge along run"),
    ]:
        if path.exists():
            story.append(fit_image(path, content_w, 90 * mm))
            story.append(Paragraph(cap, caption))
    story.append(PageBreak())

    # ——— PAINT SCHEME A vs B ———
    story.append(Paragraph("7. Paint schemes A vs B (side-by-side)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "<b>Scheme A</b> (default): walls <b>NN9074</b> Puddle of Grey + ceiling <b>WW0005</b> White Linen. "
        "<b>Scheme B</b>: walls <b>NN9088</b> Ecru Tint + ceiling <b>WW0020</b> Virgin White. "
        "Joinery (Latte shutters, Idria / fluted options, recessed SS) is identical. "
        "Compare live in the gallery paint-scheme toggle; approve chips on site before ordering.",
        body,
    ))
    half_w = (content_w - 6 * mm) / 2
    for a_name, b_name, label in [
        ("01_living_social_zone_daylight.jpg", "01_living_social_zone_daylight_schemeB.jpg", "Living — social zone"),
        ("02_kitchen_granite_latte_shutters.jpg", "02_kitchen_granite_latte_shutters_schemeB.jpg", "Kitchen — granite + Latte"),
    ]:
        a_path = VIS / a_name
        b_path = VIS / b_name
        imgs, caps = [], []
        if a_path.exists():
            imgs.append(fit_image(a_path, half_w, 72 * mm))
            caps.append(Paragraph(f"<b>A</b> · {label}", caption))
        if b_path.exists():
            imgs.append(fit_image(b_path, half_w, 72 * mm))
            caps.append(Paragraph(f"<b>B</b> · {label}", caption))
        if imgs:
            row = Table([imgs], colWidths=[half_w + 3 * mm] * len(imgs))
            row.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("ALIGN", (0, 0), (-1, -1), "CENTER")]))
            story.append(row)
            crow = Table([caps], colWidths=[half_w + 3 * mm] * len(caps))
            story.append(crow)
            story.append(Spacer(1, 2 * mm))
    story.append(PageBreak())

    # ——— WARDROBE A/B ———
    story.append(Paragraph("8. Wardrobe options A / B (3-door)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "Locked: three vertical leaves (1 single + 1 double), widths <b>457 / 457 / 458 mm</b> inside clear "
        "<b>1372 × 2286 × 488 mm</b>. Recessed pulls only. Client chooses face Option A or B after sample review.",
        body,
    ))
    wa = VIS / "05_wardrobe_aluminium_fluted_glass.jpg"
    wb = VIS / "06_wardrobe_plywood_three_door.jpg"
    imgs = []
    caps = []
    half_w = (content_w - 6 * mm) / 2
    if wa.exists():
        imgs.append(fit_image(wa, half_w, 110 * mm))
        caps.append(Paragraph("<b>Option A</b> — Aluminium frame + fluted glass", caption))
    if wb.exists():
        imgs.append(fit_image(wb, half_w, 110 * mm))
        caps.append(Paragraph("<b>Option B</b> — Plywood / Idria face", caption))
    if imgs:
        row = Table([imgs], colWidths=[half_w + 3 * mm] * len(imgs))
        row.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("ALIGN", (0, 0), (-1, -1), "CENTER")]))
        story.append(row)
        crow = Table([caps], colWidths=[half_w + 3 * mm] * len(caps))
        story.append(crow)
    story.append(Spacer(1, 4 * mm))
    # bedroom continuity if space - add on same page if possible
    bed = VIS / "04_bedroom_wardrobe_three_door_plywood.jpg"
    if bed.exists():
        story.append(fit_image(bed, content_w, 75 * mm))
        story.append(Paragraph("Bedroom continuity — three-door plywood wardrobe", caption))
    story.append(PageBreak())

    # ——— NEXT ACTIONS ———
    story.append(Paragraph("9. Next 3 actions &amp; site-measure residuals", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=8))
    actions = [
        ("1. Sign the site-measure sheet",
         "Kitchen, wardrobe niche, and all openings — photograph tape end-to-end. Resolves granite thickness conflict and any PDF/photo dimension disagreements."),
        ("2. Approve the physical sample board",
         "Scheme A chips <b>NN9074 + WW0005</b> and Scheme B chips <b>NN9088 + WW0020</b>, plus S1241 MT Latte, 84689 SU Idria (or plywood Option B), 80236 DW, E3 edges, recessed brushed SS — beside granite under morning / afternoon / 3000 K. Choose paint scheme and wardrobe Option A or B."),
        ("3. Lock fabricator shop drawings + quotation",
         "One kitchen laminate, three wardrobe leaves (single + double, 457/457/458), board grades, edges, recessed hardware, service access — then commission plan-faithful visuals from locked geometry only."),
    ]
    for title_t, detail in actions:
        box = Table(
            [[Paragraph(f"<b>{title_t}</b>", cell_b)], [Paragraph(detail, cell)]],
            colWidths=[content_w],
        )
        box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), HexColor("#E8E2D8")),
            ("BACKGROUND", (0, 1), (-1, 1), WARM_BG),
            ("BOX", (0, 0), (-1, -1), 0.6, RULE),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        story.append(box)
        story.append(Spacer(1, 3 * mm))

    story.append(Paragraph("Site-measure residuals", h2))
    for r in [
        "Confirm K-01 / W-01 clear openings on site (supersede drawing baseline if different).",
        "Measure existing granite thickness (drawing conflict: 1.50 in vs 15 mm).",
        "Verify window/door sizes — prior PDFs may conflict; do not invent dimensions from photos.",
        "Confirm kitchen orientation (sink under window, fridge right, single wall).",
        "Photograph tape measures end-to-end for audit trail.",
    ]:
        story.append(Paragraph(f"• {r}", bullet))

    story.append(Spacer(1, 8 * mm))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=4, spaceAfter=8))
    story.append(Paragraph(
        "<b>Important:</b> Images and diagrams are conceptual. This package is design-control only — "
        "not fabrication-approved until signed site measure and physical sample approval.",
        body,
    ))
    story.append(Paragraph(
        "Companion sources: MASTER_BRIEF.md · design_tokens.json · coordination/swatch_lock.json · scheme_b_swatch_lock.json · live gallery (paint scheme toggle).",
        small,
    ))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Bhadravati FINAL Interior Design — Warm Contemporary Minimalism",
        author="Bhadravati Interior Design Package",
        subject="Client handoff design control PDF",
    )

    def on_first(canv, doc_):
        cover_footer(canv, doc_)

    def on_later(canv, doc_):
        header_footer(canv, doc_)

    doc.build(story, onFirstPage=on_first, onLaterPages=on_later)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    build()

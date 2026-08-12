#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Bhadravati Interior Design V2 client handoff PDF.

Reconciled against SOURCE_OF_TRUTH.md, CONTRADICTIONS.md, V1_BASELINE.md,
PHASE_FRAMEWORK.md. Supersedes FINAL_DELIVERABLE/Bhadravati_FINAL_Interior_Design.pdf.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib.colors import HexColor, white
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
    HRFlowable,
    KeepTogether,
)

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
VIS = ASSETS / "img"
OUT = ROOT / "Bhadravati_Interior_Design_V2.pdf"

# Primary presentation boards (ASSET_INDEX.md) — exclude 02b / 04b / 05b from client PDF
BOARD_PALETTE = ASSETS / "01_visual_palette_board_v2.png"
BOARD_FLOORPLAN = ASSETS / "02_floorplan_concept_v2.png"
BOARD_KITCHEN_ELEV = ASSETS / "03_kitchen_elevation_overlay_v2.png"
BOARD_WARDROBE_ELEV = ASSETS / "04_wardrobe_elevation_overlay_v2.png"  # 3-door 457/457/458
BOARD_QA = ASSETS / "05_qa_contact_sheet_v2.jpg"

NN9074 = HexColor("#B5AB9C")
WW0005 = HexColor("#EEEDE9")
LATTE = HexColor("#C8B9A4")
SLATE = HexColor("#4E4C49")
IDRIA = HexColor("#3D483C")
INK = HexColor("#2C2A26")
MUTED = HexColor("#5C574F")
RULE = HexColor("#D4CEC4")
WARM_BG = HexColor("#F7F4EF")
ACCENT = HexColor("#6B5E4E")
ALERT = HexColor("#8B4513")

PAGE_W, PAGE_H = A4
MARGIN = 14 * mm


def fit_image(path: Path, max_w: float, max_h: float) -> Image:
    with PILImage.open(path) as im:
        w, h = im.size
    scale = min(max_w / w, max_h / h)
    return Image(str(path), width=w * scale, height=h * scale)


def header_footer(canv: canvas.Canvas, doc):
    canv.saveState()
    canv.setFillColor(NN9074)
    canv.rect(0, PAGE_H - 3.2 * mm, PAGE_W, 3.2 * mm, fill=1, stroke=0)
    canv.setFillColor(SLATE)
    canv.rect(0, 0, PAGE_W, 3.2 * mm, fill=1, stroke=0)
    if doc.page > 1:
        canv.setFont("Helvetica", 7.5)
        canv.setFillColor(MUTED)
        canv.drawString(
            MARGIN,
            6 * mm,
            "Bhadravati V2 — Warm Contemporary Minimalism | Design control (not fabrication-approved)",
        )
        canv.drawRightString(PAGE_W - MARGIN, 6 * mm, f"{doc.page}")
    canv.restoreState()


def cover_footer(canv: canvas.Canvas, doc):
    canv.saveState()
    canv.setFillColor(NN9074)
    canv.rect(0, PAGE_H - 3.2 * mm, PAGE_W, 3.2 * mm, fill=1, stroke=0)
    canv.setFillColor(SLATE)
    canv.rect(0, 0, PAGE_W, 3.2 * mm, fill=1, stroke=0)
    canv.restoreState()


def tbl_style(header_bg, header_white=False):
    styles = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, HexColor("#F3EFE8")]),
        ("GRID", (0, 0), (-1, -1), 0.35, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    if header_white:
        styles.append(("TEXTCOLOR", (0, 0), (-1, 0), white))
    return TableStyle(styles)


def build():
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "TitleCover", parent=styles["Title"], fontName="Helvetica-Bold",
        fontSize=24, leading=28, textColor=INK, alignment=TA_CENTER, spaceAfter=6,
    )
    subtitle = ParagraphStyle(
        "SubCover", parent=styles["Normal"], fontName="Helvetica",
        fontSize=11, leading=14, textColor=MUTED, alignment=TA_CENTER, spaceAfter=4,
    )
    h1 = ParagraphStyle(
        "H1", parent=styles["Heading1"], fontName="Helvetica-Bold",
        fontSize=13, leading=16, textColor=INK, spaceBefore=2, spaceAfter=6,
    )
    h2 = ParagraphStyle(
        "H2", parent=styles["Heading2"], fontName="Helvetica-Bold",
        fontSize=10.5, leading=13, textColor=ACCENT, spaceBefore=6, spaceAfter=3,
    )
    body = ParagraphStyle(
        "Body", parent=styles["Normal"], fontName="Helvetica",
        fontSize=9, leading=12, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5,
    )
    small = ParagraphStyle(
        "Small", parent=styles["Normal"], fontName="Helvetica",
        fontSize=7.5, leading=10, textColor=MUTED, alignment=TA_CENTER,
    )
    caption = ParagraphStyle(
        "Cap", parent=styles["Normal"], fontName="Helvetica-Oblique",
        fontSize=7.5, leading=9, textColor=MUTED, alignment=TA_CENTER,
        spaceBefore=2, spaceAfter=6,
    )
    bullet = ParagraphStyle(
        "Bullet", parent=styles["Normal"], fontName="Helvetica",
        fontSize=9, leading=12, textColor=INK, leftIndent=2, spaceAfter=2,
    )
    cell = ParagraphStyle(
        "Cell", parent=styles["Normal"], fontName="Helvetica",
        fontSize=7.5, leading=9.5, textColor=INK,
    )
    cell_b = ParagraphStyle("CellB", parent=cell, fontName="Helvetica-Bold")
    warn = ParagraphStyle(
        "Warn", parent=body, fontName="Helvetica-Bold", textColor=ALERT, fontSize=8.5, leading=11,
    )

    content_w = PAGE_W - 2 * MARGIN
    story = []

    # ——— COVER ———
    story.append(Spacer(1, 18 * mm))
    story.append(Paragraph("BHADRAVATI HOME", ParagraphStyle(
        "brand", parent=subtitle, fontSize=11, textColor=ACCENT, fontName="Helvetica-Bold", spaceAfter=10,
    )))
    story.append(Paragraph("Warm Contemporary Minimalism", title))
    story.append(Paragraph("Interior Design Package — Version 2", ParagraphStyle(
        "t2", parent=title, fontSize=15, leading=18, spaceAfter=8,
    )))
    story.append(HRFlowable(width="55%", thickness=1, color=NN9074, spaceBefore=2, spaceAfter=10, hAlign="CENTER"))
    story.append(Paragraph("First-floor studio · Bhadravati, Karnataka", subtitle))
    story.append(Paragraph("Client handoff · Design control only — not fabrication-approved", subtitle))
    story.append(Paragraph(
        "Supersedes V1: FINAL_DELIVERABLE/Bhadravati_FINAL_Interior_Design.pdf (2026-08-11)",
        ParagraphStyle("sup", parent=small, spaceBefore=4, spaceAfter=6),
    ))
    living = VIS / "01_living_social_zone_daylight.jpg"
    if living.exists():
        story.append(fit_image(living, content_w, 88 * mm))
        story.append(Paragraph("Living — social zone (daylight concept · AI-assisted · verify on site)", caption))
    story.append(Paragraph(
        f"Generated {date.today().isoformat()} · Reconciled to SOURCE_OF_TRUTH + CONTRADICTIONS · "
        "3-door wardrobe · S1241 Latte-all · NN9074 default",
        small,
    ))
    story.append(PageBreak())

    # ——— 0 ETHICS / SCOPE ———
    story.append(Paragraph("0. Scope, ethics & fabrication hold", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "This package is <b>design control</b> for client review and fabricator briefing. "
        "It is <b>not</b> a stamped construction set, shop drawing, accessibility certification, "
        "or permit approval. Visuals are conceptual; dimensions are labelled clear openings until "
        "a signed site-measure sheet supersedes them.",
        body,
    ))
    story.append(Paragraph(
        "FABRICATION HOLD — Do not cut shutters from clear openings alone. Measure granite thickness "
        "(drawing conflict 1.50 in vs 15 mm — pick neither). Approve physical samples under morning / "
        "afternoon / 3000 K light. Disclose: concept images may be AI-assisted; they do not prove constructability.",
        warn,
    ))
    for item in [
        "In scope: concept, zoning, locked finish codes, K-01/W-01 baselines, lighting intent, FF&E sizing, phasing, risks.",
        "Out of scope: structural/MEP engineering, AHJ stamps, aluminium-system shop drawings until fabricator selection.",
        "Procurement ethics: only catalogue-confirmed SKUs; do not order filename typo <b>844485</b> (not locked; catalogue Hector Pine is 84485 SU if ever sampled).",
    ]:
        story.append(Paragraph(f"• {item}", bullet))
    story.append(PageBreak())

    # ——— 1 DIRECTION ———
    story.append(Paragraph("1. Discovery lock — design direction", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "The home will feel calm, practical, and locally believable — not a pale showroom and not textbook Japandi. "
        "Architecture and circulation come before styling. Climate drivers: dust/smoke, hard water, monsoon humidity, strong daylight.",
        body,
    ))
    story.append(Paragraph("Non-negotiables (controlling)", h2))
    for item in [
        "Existing <b>black granite</b> kitchen remains; scope = <b>shutters only</b> (no island, L-flip, waterfall ends, new carcass).",
        "Kitchen base + drawers + loft = <b>Century S1241 MT Latte only</b> — never dual-tone; never 80236 in kitchen.",
        "Wardrobe = <b>3 doors</b> (single L + double R), leaves <b>457 / 457 / 458 mm</b> inside 1372 mm clear — not four leaves; not two slabs.",
        "Hardware = brushed stainless <b>recessed</b> pulls; edges E3 ABS <b>2 mm kitchen / 1 mm wardrobe</b>; lighting <b>3000 K</b>; matte/low-sheen.",
        "Default walls <b>NN9074</b>; ceiling <b>WW0005</b>; NN9088 = Scheme B alternate only.",
        "No TV feature wall, gold strips, gloss/sparkle laminates, or Japandi prop clutter.",
    ]:
        story.append(Paragraph(f"• {item}", bullet))
    concept_data = [
        [Paragraph("<b>Concept</b>", cell_b), Paragraph("<b>Decision</b>", cell_b)],
        [Paragraph("A — Warm Contemporary Minimalism (NN9074 + Latte + Idria)", cell), Paragraph("<b>LOCKED FINAL</b>", cell_b)],
        [Paragraph("B — Textbook Japandi", cell), Paragraph("Reject as governing style", cell)],
        [Paragraph("C — Dual-tone kitchen / NN9088 as default walls", cell), Paragraph("Reject (supersedes Corrected Handover schedule)", cell)],
    ]
    ct = Table(concept_data, colWidths=[120 * mm, 50 * mm])
    ct.setStyle(tbl_style(NN9074))
    story.append(Spacer(1, 2 * mm))
    story.append(ct)
    story.append(PageBreak())

    # ——— 2–4 ZONES / HUMAN FACTORS ———
    story.append(Paragraph("2–4. Site baseline, zoning & human factors", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "Studio envelope ? <b>21 × 18 ft (6401 × 5486 mm)</b> — <b>plan relationship only</b>, not a cut sheet. "
        "Source hierarchy: signed site measure ? dimension_register_v1 ? this package ? renders.",
        body,
    ))
    zones = [
        [Paragraph("<b>Zone</b>", cell_b), Paragraph("<b>Position</b>", cell_b), Paragraph("<b>Intent</b>", cell_b)],
        [Paragraph("Bedroom", cell), Paragraph("SW", cell), Paragraph("Queen bed; 2 nightstands; no dark feature wall", cell)],
        [Paragraph("Living", cell), Paragraph("S-centre", cell), Paragraph("3-seat sofa; round coffee; floating TV cabinet; no TV wall", cell)],
        [Paragraph("Kitchen", cell), Paragraph("SE", cell), Paragraph("Single-wall granite; shutters only; sink under window; fridge extreme right", cell)],
        [Paragraph("Bathroom", cell), Paragraph("NW", cell), Paragraph("Open shower retained; basin outside shower", cell)],
        [Paragraph("Wardrobe", cell), Paragraph("N-centre", cell), Paragraph("54×90×19.20 in niche; 3 doors 457/457/458", cell)],
        [Paragraph("Study", cell), Paragraph("NE", cell), Paragraph("Desk at large window; 2–3 shallow shelves max", cell)],
    ]
    zt = Table(zones, colWidths=[28 * mm, 28 * mm, 114 * mm])
    zt.setStyle(tbl_style(SLATE, header_white=True))
    story.append(zt)
    story.append(Paragraph(
        "Circulation: primary 900–1200 mm · secondary 600–900 mm · sofa–coffee 450–500 mm · "
        "bed sides ?600 mm · wardrobe standing clear ?600 mm (prefer 900). "
        "Counter ~787 mm AFF; hanging bay ~991 mm — verify for users. No accessibility certification claimed. "
        "All door/window sizes = <b>UNVERIFIED</b> (bedroom window conflict: do not hard-code).",
        body,
    ))
    story.append(PageBreak())

    # ——— DIMENSIONS ———
    story.append(Paragraph("Key dimensions — K-01 / W-01 (design baseline)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "Clear openings only. Do not manufacture from these values directly. "
        "Granite thickness: <b>UNKNOWN — measure on site</b> (C-01: 1.50 in vs 15 mm — invent neither).",
        warn,
    ))
    story.append(Paragraph("Kitchen register (K-01)", h2))
    k_data = [
        [Paragraph("<b>Item</b>", cell_b), Paragraph("<b>in</b>", cell_b), Paragraph("<b>mm</b>", cell_b)],
        [Paragraph("Module width", cell), Paragraph("106.00", cell), Paragraph("2692", cell)],
        [Paragraph("Ref. wall width", cell), Paragraph("220.00", cell), Paragraph("5588", cell)],
        [Paragraph("Floor ? loft underside", cell), Paragraph("102.00", cell), Paragraph("2591", cell)],
        [Paragraph("Loft ? lower shelf underside", cell), Paragraph("48.00", cell), Paragraph("1219", cell)],
        [Paragraph("Shelf underside ? counter top", cell), Paragraph("23.00", cell), Paragraph("584", cell)],
        [Paragraph("Floor ? counter top", cell), Paragraph("31.00", cell), Paragraph("787", cell)],
        [Paragraph("Internal counter depth", cell), Paragraph("19.20", cell), Paragraph("488", cell)],
        [Paragraph("B1 / B2 / B3 clear", cell), Paragraph("48 / 36 / 18", cell), Paragraph("1219 / 914 / 457", cell)],
    ]
    kt = Table(k_data, colWidths=[90 * mm, 40 * mm, 40 * mm])
    kt.setStyle(tbl_style(NN9074))
    story.append(kt)
    story.append(Paragraph("B1+B2+B3=102 in; + four 1 in supports = 106 in — arithmetic PASS. Finish lock = S1241 MT Latte (laminate). Kitchen aluminium frame system = open pending fabricator (C-09).", cell))
    story.append(Paragraph("Wardrobe register (W-01)", h2))
    w_data = [
        [Paragraph("<b>Item</b>", cell_b), Paragraph("<b>in</b>", cell_b), Paragraph("<b>mm</b>", cell_b)],
        [Paragraph("Clear W × H × D", cell), Paragraph("54 × 90 × 19.20", cell), Paragraph("1372 × 2286 × 488", cell)],
        [Paragraph("Left / partition / right", cell), Paragraph("21 / 0.59 / 32.41", cell), Paragraph("533 / 15 / 823", cell)],
        [Paragraph("Three vertical leaves (locked)", cell), Paragraph("1 single + 1 double", cell), Paragraph("<b>457 / 457 / 458</b>", cell)],
        [Paragraph("Left openings T?B", cell), Paragraph("12 + 4×19.5", cell), Paragraph("305 + 4×495", cell)],
        [Paragraph("Right stack", cell), Paragraph("12 / 39 hang / 9.5 / 12 / 17.5", cell), Paragraph("305 / 991 / 241 / 305 / 445", cell)],
    ]
    wt = Table(w_data, colWidths=[70 * mm, 50 * mm, 50 * mm])
    wt.setStyle(tbl_style(SLATE, header_white=True))
    story.append(wt)
    story.append(Paragraph("457+457+458=1372 — PASS. Four-leaf language in older V1 chapters is superseded (C-02 / F1).", cell))
    story.append(PageBreak())

    # ——— FLOOR PLAN ———
    story.append(Paragraph("Floor plan (relational)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    fp = BOARD_FLOORPLAN if BOARD_FLOORPLAN.exists() else VIS / "floor_plan_precise.jpg"
    if fp.exists():
        story.append(fit_image(fp, content_w, 170 * mm))
        story.append(Paragraph(
            "V2 zoning floorplan — single-wall kitchen; W-01 3-door wardrobe; relational only. "
            "Cite register depths from SoT (W-01 / counter depth <b>488 mm</b>) — do not OCR plan chips "
            "(leaf widths are <b>457 / 457 / 458</b>; depth is not 458).",
            caption,
        ))
    story.append(PageBreak())

    # ——— COLOR / MATERIALS ———
    story.append(Paragraph("5–7. Color, materials & finishes (locked)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "Hex values for Birla paints are shade-card exact. Laminate hexes are screen approximations — "
        "approve physical chips beside granite under morning / afternoon / 3000 K. "
        "Do not print or procure typo SKU <b>844485</b>.",
        body,
    ))
    # swatches
    swatch_specs = [
        ("NN9074", "A walls", "#B5AB9C"),
        ("WW0005", "A ceiling", "#EEEDE9"),
        ("NN9088", "B walls alt", "#E9E3D9"),
        ("S1241", "Latte MT", "#C8B9A4"),
        ("84689", "Idria Oak SU", "#3D483C"),
        ("80236", "Slate DW", "#4E4C49"),
    ]
    cells = []
    for code, name, hx in swatch_specs:
        c = HexColor(hx)
        dark = hx.upper() == "#4E4C49"
        inner = Table(
            [[""], [Paragraph(
                f"<b>{code}</b><br/><font size='6'>{name}</font>",
                ParagraphStyle("sw", fontName="Helvetica", fontSize=7, leading=9,
                               textColor=white if dark else INK, alignment=TA_CENTER),
            )]],
            colWidths=[26 * mm], rowHeights=[14 * mm, 10 * mm],
        )
        inner.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, 0), c),
            ("BACKGROUND", (0, 1), (0, 1), SLATE if dark else WARM_BG),
            ("BOX", (0, 0), (-1, -1), 0.4, RULE),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))
        cells.append(inner)
    story.append(Table([cells], colWidths=[28 * mm] * 6))
    story.append(Spacer(1, 3 * mm))
    pal = [
        [Paragraph("<b>Role</b>", cell_b), Paragraph("<b>Code</b>", cell_b), Paragraph("<b>Notes</b>", cell_b)],
        [Paragraph("Scheme A walls (default)", cell), Paragraph("Birla <b>NN9074</b> Puddle of Grey", cell), Paragraph("#B5AB9C exact", cell)],
        [Paragraph("Scheme A ceiling", cell), Paragraph("Birla <b>WW0005</b> White Linen", cell), Paragraph("#EEEDE9 exact", cell)],
        [Paragraph("Scheme B walls (alt only)", cell), Paragraph("Birla <b>NN9088</b> Ecru Tint", cell), Paragraph("Shows dust faster", cell)],
        [Paragraph("Scheme B ceiling", cell), Paragraph("Birla <b>WW0020</b> Virgin White", cell), Paragraph("Sample confirm", cell)],
        [Paragraph("Kitchen all shutters", cell), Paragraph("Century <b>S1241 MT Latte</b>", cell), Paragraph("Base+drawers+loft; one code", cell)],
        [Paragraph("TV cabinet only", cell), Paragraph("<b>80236 DW Slate Grey</b> (or Latte)", cell), Paragraph("Controlled accent — not kitchen", cell)],
        [Paragraph("Wardrobe preferred", cell), Paragraph("<b>84689 SU Idria Oak</b>", cell), Paragraph("Backup 84687 Lyon only", cell)],
        [Paragraph("Edges", cell), Paragraph("E3 ABS matched", cell), Paragraph("2 mm kitchen / 1 mm wardrobe; matt", cell)],
        [Paragraph("Hardware", cell), Paragraph("Brushed SS <b>recessed</b>", cell), Paragraph("No projecting bars", cell)],
        [Paragraph("Counter", cell), Paragraph("Existing black granite", cell), Paragraph("Retain; shutters only", cell)],
    ]
    pt = Table(pal, colWidths=[42 * mm, 72 * mm, 56 * mm])
    pt.setStyle(tbl_style(SLATE, header_white=True))
    story.append(pt)
    pal_img = BOARD_PALETTE if BOARD_PALETTE.exists() else VIS / "palette_board.jpg"
    if pal_img.exists():
        story.append(Spacer(1, 2 * mm))
        story.append(fit_image(pal_img, content_w, 95 * mm))
        story.append(Paragraph(
            "Visual palette board V2 — Scheme A locks (NN9074 / WW0005 / S1241 Latte / Idria); do-not-use rules on board. "
            "Idria chip sampled from CenturyPly European Grey product image (not taupe).",
            caption,
        ))
    story.append(PageBreak())

    # ——— PLYWOOD + HARDWARE (from PLYWOOD_HARDWARE_RECOMMENDATION.md §10) ———
    story.append(Paragraph("Boards & hardware (annotated lock)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "From <b>PLYWOOD_HARDWARE_RECOMMENDATION.md</b>. Kitchen = shutters-only on existing black granite. "
        "Wardrobe = full niche carcass + three hinged Idria leaves. Split the board spec — do not buy one core for the whole house.",
        body,
    ))
    story.append(Paragraph("Core boards", h2))
    board_rows = [
        [Paragraph("<b>Location</b>", cell_b), Paragraph("<b>Primary</b>", cell_b), Paragraph("<b>Alternate / note</b>", cell_b)],
        [Paragraph("Kitchen shutters (S1241 MT Latte 0.8 mm · 2 mm E3 ABS · 3000 K)", cell),
         Paragraph("<b>Action Tesa Boilo 18 mm</b>", cell),
         Paragraph("<b>Century Club Prime 18/19 mm</b> if shop will not edge HDF. Laminate <b>both faces</b>. "
                   "<b>Do NOT</b> default kitchen doors to Sainik 710 (official page = IS 303 BWP, not marine IS 710; "
                   "alternate-core cups = hinge tear-out risk).", cell)],
        [Paragraph("Wardrobe carcass + 3 Idria leaves (54×90×19.20 in · 1 mm E3 ABS)", cell),
         Paragraph("<b>Century Sainik 710 18 mm BWP</b> — QR-scan every sheet", cell),
         Paragraph("<b>HDHMR 18 mm</b> calibrated alternate. <b>Boilo too heavy</b> for 90 in doors. "
                   "Never MR, particle board, MDF, or unbranded “710”.", cell)],
    ]
    bt = Table(board_rows, colWidths=[48 * mm, 55 * mm, 67 * mm])
    bt.setStyle(tbl_style(SLATE, header_white=True))
    story.append(bt)
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("Hardware schedule (named series)", h2))
    hw_rows = [
        [Paragraph("<b>Item</b>", cell_b), Paragraph("<b>Spec</b>", cell_b), Paragraph("<b>Lock</b>", cell_b)],
        [Paragraph("Pulls", cell),
         Paragraph("Brushed stainless <b>recessed</b> only (J / finger / recessed)", cell),
         Paragraph("<b>LOCKED</b> — no bars / brass / black", cell)],
        [Paragraph("Hinges", cell),
         Paragraph("<b>Hettich Sensys 8645i</b> 110° integrated soft-close; <b>5 per</b> tall wardrobe leaf", cell),
         Paragraph("Kitchen + wardrobe; not Onsys / clip-on dampers", cell)],
        [Paragraph("Channels (if drawers)", cell),
         Paragraph("<b>Hettich KA 5632</b> (45 kg) or <b>KA 4732</b> Silent System (35 kg)", cell),
         Paragraph("Only if drawers exist", cell)],
        [Paragraph("Wardrobe lock", cell),
         Paragraph("<b>Godrej Curvo 8010</b> (25 mm); 8011 if finished stack thicker", cell),
         Paragraph("SS cover", cell)],
        [Paragraph("Hanging rail", cell),
         Paragraph("Oval <b>30×15 mm</b> + mid-support (Hettich SL 322 / Ebco WRF class)", cell),
         Paragraph("Required at ~centre of 54 in", cell)],
        [Paragraph("Screws", cell),
         Paragraph("<b>SS304</b> in kitchen / wet-risk; Hettich-supplied hinge screws", cell),
         Paragraph("Predrill cups", cell)],
        [Paragraph("Edges", cell),
         Paragraph("E3 ABS matched · <b>2 mm kitchen / 1 mm wardrobe</b>", cell),
         Paragraph("Seal every edge; matt", cell)],
    ]
    ht = Table(hw_rows, colWidths=[32 * mm, 90 * mm, 48 * mm])
    ht.setStyle(tbl_style(IDRIA, header_white=True))
    story.append(ht)
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "<b>Executive lock:</b> Kitchen shutters → Boilo 18 mm (or Club Prime 18/19 mm). "
        "Wardrobe → Sainik 710 18 mm BWP QR-verified (HDHMR 18 mm alternate; not Boilo). "
        "Hettich Sensys 8645i · KA 5632/4732 if drawers · Godrej Curvo 8010 · oval 30×15 mm rail with mid-support · "
        "SS304 kitchen · recessed SS pulls only · seal every edge · laminate both faces of kitchen shutters. "
        "Full evidence + procurement checklist: PLYWOOD_HARDWARE_RECOMMENDATION.md.",
        body,
    ))
    story.append(PageBreak())

    # ——— WELLNESS / LIGHTING / ACOUSTICS / SYSTEMS / CODES ———
    story.append(Paragraph("8–12. Wellness, lighting, acoustics, systems & codes", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "<b>IEQ / climate:</b> Mid-tone washable greige (NN9074), matte wipeable joinery, sealed wet-risk boards (BWP at hinge/splash), "
        "spare laminate/edge for repairability, preserve daylight with sheers for glare/heat. Prefer durability over green theater.",
        body,
    ))
    story.append(Paragraph(
        "<b>Lighting:</b> Baseline <b>3000 K</b> (bedroom lamps 2700–3000 K). Prefer CRI ?90 at kitchen/living finishes. "
        "Mandatory kitchen under-loft linear task (300–750 lux guidance). Living ambient 150–300; bedroom 50–150; study/reading 300–500. "
        "Separate zones + dimming living/bedroom. Accent minimal — no cove glitter.",
        body,
    ))
    story.append(Paragraph(
        "<b>Acoustics:</b> Small hard studio — rugs, closed storage, tight-weave textiles. No specialty acoustic product claims.",
        body,
    ))
    story.append(Paragraph(
        "<b>Systems:</b> Preserve sink plumbing access; do not permanently seal damp zones; do not conceal DB without access; "
        "SS304 at humid risk; moisture-rated bath fittings.",
        body,
    ))
    story.append(Paragraph(
        "<b>Codes awareness (non-certifying):</b> Keep egress/aisles clear of FF&E. New electrical points ? licensed electrician. "
        "No AHJ stamp claimed in this package.",
        body,
    ))
    eve = VIS / "03_evening_material_lighting_detail.jpg"
    if eve.exists():
        story.append(fit_image(eve, content_w, 78 * mm))
        story.append(Paragraph("Evening material / lighting junction — 3000 K intent · conceptual", caption))
    story.append(PageBreak())

    # ——— FF&E / BUDGET ———
    story.append(Paragraph("13–14. FF&E schedule & budget phasing", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    ffe = [
        [Paragraph("<b>Item</b>", cell_b), Paragraph("<b>Approx</b>", cell_b), Paragraph("<b>Notes</b>", cell_b)],
        [Paragraph("3-seat sofa", cell), Paragraph("~2150×875×825 mm", cell), Paragraph("Wipeable taupe; front legs on rug", cell)],
        [Paragraph("Round coffee table", cell), Paragraph("Ø700–800 × H~425", cell), Paragraph("450–500 mm to sofa", cell)],
        [Paragraph("Floating TV cabinet", cell), Paragraph("1400–1800 mm", cell), Paragraph("80236 DW or Latte; no TV wall", cell)],
        [Paragraph("Queen bed + 2 nightstands", cell), Paragraph("Mattress ~1525×2030", cell), Paragraph("Sides ?600 mm where possible", cell)],
        [Paragraph("Study desk + mesh chair", cell), Paragraph("Desk 1200–1500", cell), Paragraph("2–3 shelves ?300 mm deep", cell)],
        [Paragraph("Kitchen shutters B1–B3 + loft", cell), Paragraph("Clear 48/36/18 in", cell), Paragraph("S1241 MT Latte; recessed pulls", cell)],
        [Paragraph("Wardrobe 3 leaves", cell), Paragraph("457/457/458 mm", cell), Paragraph("84689 Idria; Options A/B face", cell)],
    ]
    ft = Table(ffe, colWidths=[48 * mm, 48 * mm, 74 * mm])
    ft.setStyle(tbl_style(NN9074))
    story.append(ft)
    story.append(Paragraph("Budget tiers", h2))
    for t in [
        "<b>Essential:</b> Kitchen Latte shutters + wardrobe 3 leaves + NN9074/WW0005 paint + E3 edges + recessed hardware + kitchen task LED.",
        "<b>Recommended:</b> + TV cabinet, ambient dimming, sofa/curtains/rugs, bedside & study lamps.",
        "<b>Premium:</b> Proven PUR, upgraded boards/lighting, spare laminate kit — still no gloss / island / TV wall.",
    ]:
        story.append(Paragraph(f"• {t}", bullet))
    story.append(Paragraph(
        "Phase 0 measure+samples ? 1 wet/storage core ? 2 light+living ? 3 sleep/work ? 4 optional polish. "
        "Quotes must state board grade/thickness, laminate code/finish, edge brand/thickness, adhesive process, hinge models, warranty exclusions, spares.",
        body,
    ))
    story.append(PageBreak())

    # ——— LIVING VIEWS ———
    story.append(Paragraph("15–16. Living — three-view set (conceptual)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    for path, cap in [
        (VIS / "01_living_social_zone_daylight.jpg", "Living — social zone daylight · no balcony invention · 80236 floating cabinet only"),
        (VIS / "01b_living_from_tv_toward_sofa.jpg", "Living — from TV toward sofa"),
        (VIS / "01c_living_side_across_social.jpg", "Living — side across social zone"),
    ]:
        if path.exists():
            story.append(fit_image(path, content_w, 72 * mm))
            story.append(Paragraph(cap, caption))
    story.append(PageBreak())

    # ——— KITCHEN ———
    story.append(Paragraph("Kitchen — granite retained + S1241 Latte (conceptual)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    story.append(Paragraph(
        "Single-wall existing black granite. All shutters Century S1241 MT Latte with recessed brushed SS pulls. "
        "Fridge extreme right. No waterfall/end-panel invention. Loft/shelf bands schematic vs K-01.",
        body,
    ))
    for path, cap in [
        (VIS / "02_kitchen_granite_latte_shutters.jpg", "Kitchen — granite + Latte shutters"),
        (VIS / "02b_kitchen_from_fridge_along_run.jpg", "Kitchen — from fridge along run (fridge right)"),
        (VIS / "02c_kitchen_loft_shelf_band_detail.jpg", "Kitchen — loft / mid shelf band detail (schematic)"),
    ]:
        if path.exists():
            story.append(fit_image(path, content_w, 68 * mm))
            story.append(Paragraph(cap, caption))
    story.append(PageBreak())

    # ——— KITCHEN ELEVATION (V2 board) ———
    story.append(Paragraph("Kitchen elevation — K-01 (design control)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    story.append(Paragraph(
        "Front elevation with clear openings + V2 chrome: S1241 Latte-all, recessed brushed stainless pulls, "
        "existing granite retained. Drawn bar pulls on source art may not match recessed-pull lock — prefer recessed.",
        body,
    ))
    if BOARD_KITCHEN_ELEV.exists():
        story.append(fit_image(BOARD_KITCHEN_ELEV, content_w, 155 * mm))
        story.append(Paragraph(
            "K-01 elevation overlay V2 — Latte-all shutters; shutters-only; hardware lock = "
            "<b>recessed</b> brushed stainless pulls (C-08) — ignore any drawn bar pulls on source art; not fabrication-approved",
            caption,
        ))
    story.append(PageBreak())

    # ——— SCHEME A vs B ———
    story.append(Paragraph("Paint schemes A vs B (walls/ceilings only)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    story.append(Paragraph(
        "<b>Scheme A (default):</b> NN9074 + WW0005. <b>Scheme B (alternate):</b> NN9088 + WW0020. "
        "Joinery codes unchanged. Supersedes Corrected Handover which showed NN9088 as used default (C-04).",
        body,
    ))
    half = (content_w - 6 * mm) / 2
    for a_n, b_n, label in [
        ("01_living_social_zone_daylight.jpg", "01_living_social_zone_daylight_schemeB.jpg", "Living"),
        ("02_kitchen_granite_latte_shutters.jpg", "02_kitchen_granite_latte_shutters_schemeB.jpg", "Kitchen"),
    ]:
        a, b = VIS / a_n, VIS / b_n
        imgs, caps = [], []
        if a.exists():
            imgs.append(fit_image(a, half, 68 * mm))
            caps.append(Paragraph(f"<b>A</b> · {label}", caption))
        if b.exists():
            imgs.append(fit_image(b, half, 68 * mm))
            caps.append(Paragraph(f"<b>B</b> · {label}", caption))
        if imgs:
            story.append(Table([imgs], colWidths=[half + 3 * mm] * len(imgs)))
            story.append(Table([caps], colWidths=[half + 3 * mm] * len(caps)))
    story.append(PageBreak())

    # ——— WARDROBE ———
    story.append(Paragraph("Wardrobe — 3-door Options A / B", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    story.append(Paragraph(
        "Locked: three leaves <b>457 / 457 / 458 mm</b> inside clear <b>1372 × 2286 × 488 mm</b>. "
        "Preferred face laminate <b>84689 SU Idria Oak</b> (backup 84687 Lyon). Recessed pulls only. "
        "Client chooses Option A or B after samples. Four-leaf text elsewhere is superseded.",
        body,
    ))
    wa, wb = VIS / "05_wardrobe_aluminium_fluted_glass.jpg", VIS / "06_wardrobe_plywood_three_door.jpg"
    imgs, caps = [], []
    if wa.exists():
        imgs.append(fit_image(wa, half, 95 * mm))
        caps.append(Paragraph("<b>Option A</b> — Aluminium frame + fluted glass", caption))
    if wb.exists():
        imgs.append(fit_image(wb, half, 95 * mm))
        caps.append(Paragraph("<b>Option B</b> — Plywood / Idria face", caption))
    if imgs:
        story.append(Table([imgs], colWidths=[half + 3 * mm] * len(imgs)))
        story.append(Table([caps], colWidths=[half + 3 * mm] * len(caps)))
    bed = VIS / "04_bedroom_wardrobe_three_door_plywood.jpg"
    if bed.exists():
        story.append(fit_image(bed, content_w, 70 * mm))
        story.append(Paragraph("Bedroom continuity — three-door plywood wardrobe (not four leaves)", caption))
    story.append(PageBreak())

    # ——— WARDROBE ELEVATION (V2 board — 3-door only) ———
    story.append(Paragraph("Wardrobe elevation — W-01 three-door (locked)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    story.append(Paragraph(
        "Locked leaf widths <b>457 / 457 / 458 mm</b> inside 1372 mm clear. "
        "Four-leaf artwork is superseded and excluded from this client PDF.",
        body,
    ))
    if BOARD_WARDROBE_ELEV.exists():
        story.append(fit_image(BOARD_WARDROBE_ELEV, content_w, 155 * mm))
        story.append(Paragraph(
            "W-01 elevation overlay V2 — 3-door composite (face + dimensioned leaves 457/457/458)",
            caption,
        ))
    story.append(PageBreak())

    # bedroom detail views
    story.append(Paragraph("Bedroom / wardrobe continuity views", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    for path, cap in [
        (VIS / "04b_bedroom_from_wardrobe_toward_bed.jpg", "From wardrobe toward bed"),
        (VIS / "04c_wardrobe_three_door_detail.jpg", "Three-door wardrobe detail"),
    ]:
        if path.exists():
            story.append(fit_image(path, content_w, 85 * mm))
            story.append(Paragraph(cap, caption))
    story.append(PageBreak())

    # ——— 17–19 CD / PM ———
    story.append(Paragraph("17–19. Documentation mindset & install sequence", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    story.append(Paragraph(
        "Drawings/schedules in this pack are <b>design control</b>. Fabricator issues shop drawings after sample sign-off. "
        "Existing vs new: granite existing; shutters/wardrobe leaves new. Dual units follow register (in + mm).",
        body,
    ))
    for s in [
        "Measure & sign site sheet (K-01, W-01, openings) ? photograph tape end-to-end.",
        "Approve sample board (NN9074/WW0005 and/or Scheme B; S1241; 84689; 80236; E3; recessed SS) beside granite @ morning/afternoon/3000 K.",
        "Choose wardrobe Option A or B; lock quote (board grades, laminate codes, edges, hinges, access panels).",
        "Fabricate ? site prep ? install kitchen shutters + wardrobe ? paint ? lighting ? FF&E ? punch.",
    ]:
        story.append(Paragraph(f"• {s}", bullet))
    story.append(PageBreak())

    # ——— NEXT ACTIONS / QA ———
    story.append(Paragraph("20–22. Next actions, residuals & case-study note", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    actions = [
        ("1. Sign the site-measure sheet",
         "Kitchen, wardrobe niche, all openings. Resolves C-01 granite thickness and C-05/C-11 window conflicts."),
        ("2. Approve physical sample board",
         "Scheme A default chips + optional Scheme B; S1241 MT Latte; 84689 Idria; 80236; E3 1&2 mm; recessed brushed SS — beside granite under morning / afternoon / 3000 K. Choose wardrobe A or B."),
        ("3. Lock fabricator shop drawings + quotation",
         "One kitchen laminate (S1241 all); three wardrobe leaves 457/457/458; boards; edges; recessed hardware; service access — then only then commission fabrication-faithful visuals."),
    ]
    for title_t, detail in actions:
        box = Table(
            [[Paragraph(f"<b>{title_t}</b>", cell_b)], [Paragraph(detail, cell)]],
            colWidths=[content_w],
        )
        box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), HexColor("#E8E2D8")),
            ("BACKGROUND", (0, 1), (-1, 1), WARM_BG),
            ("BOX", (0, 0), (-1, -1), 0.5, RULE),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(box)
        story.append(Spacer(1, 2.5 * mm))

    story.append(Paragraph("Open residuals (do not fabricate around these)", h2))
    for r in [
        "C-01 Granite thickness UNKNOWN — measure.",
        "C-05 / C-11 Openings UNVERIFIED — site measure.",
        "Exact kitchen shutter overlay vs B1/B2/B3 clear — shop drawings after system choice (C-09).",
        "Wardrobe overlay/inset/reveals/hinge sides TBD.",
        "AI loft/shelf bands remain schematic.",
    ]:
        story.append(Paragraph(f"• {r}", bullet))

    story.append(Paragraph(
        "<b>Portfolio case note:</b> Site-specific resilient Indian home — dust, monsoon, hard water, repairability. "
        "V2 fixed four-leaf drift, dual-tone kitchen contradiction, and NN9088-as-default confusion from older packs.",
        body,
    ))
    story.append(Spacer(1, 6 * mm))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=2, spaceAfter=6))
    story.append(Paragraph(
        "<b>Important:</b> Images and diagrams are conceptual. Design-control only — not fabrication-approved "
        "until signed site measure and physical sample approval.",
        body,
    ))
    story.append(Paragraph(
        "Control docs: SOURCE_OF_TRUTH.md · CONTRADICTIONS.md · V1_BASELINE.md · MASTER_BRIEF_V2.md · "
        "PHASE_FRAMEWORK.md · design_tokens_v2.json · dimension_register_v1 · assets/ASSET_INDEX.md",
        small,
    ))
    story.append(PageBreak())

    # ——— VISUAL QA CONTACT SHEET (V2) ———
    story.append(Paragraph("Appendix — visual QA contact sheet (V2)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    story.append(Paragraph(
        "Six-up strip for client visual QA: living, kitchen Latte, kitchen detail, wardrobe 3-door, "
        "wardrobe dims, evening light. Historical / dark-cabinet contact sheets excluded. "
        "<b>Do not OCR</b> the wardrobe-dims panel — controlling SoT values follow in the caption.",
        body,
    ))
    if BOARD_QA.exists():
        story.append(fit_image(BOARD_QA, content_w, 160 * mm))
        story.append(Paragraph(
            "QA contact sheet V2 — conceptual only. Wardrobe SoT lock (override baked overlays): "
            "clear niche <b>1372 × 2286 × 488 mm</b>; leaves <b>457 / 457 / 458 mm</b>; "
            "preferred face <b>84689 SU Idria Oak</b>. Do not trust OCR of height/depth typos or wrong laminate names on the sheet.",
            caption,
        ))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=11 * mm,
        bottomMargin=11 * mm,
        title="Bhadravati Interior Design V2 — Warm Contemporary Minimalism",
        author="Bhadravati Interior Design Package V2",
        subject="Client handoff design control PDF — supersedes FINAL_v1",
    )
    doc.build(story, onFirstPage=cover_footer, onLaterPages=header_footer)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes, pages TBD)")
    return OUT


if __name__ == "__main__":
    build()

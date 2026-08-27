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
CORRECTED_VIS = VIS / "corrected_ecru_virgin_white"
OUT = ROOT / "Bhadravati_Interior_Design_V2.pdf"

# Primary presentation boards (ASSET_INDEX.md) — exclude 02b / 04b / 05b from client PDF
# The former board was Scheme A and would contradict the corrected Ecru/Virgin White lock.
# Keep the corrected swatch table below as the PDF source; the full corrected SVG board is in docs/.
BOARD_PALETTE = ASSETS / "01_visual_palette_board_v2_corrected.png"
BOARD_FLOORPLAN = ASSETS / "02_floorplan_concept_v2.png"
BOARD_KITCHEN_ELEV = ASSETS / "03_kitchen_elevation_overlay_v2.png"
BOARD_WARDROBE_ELEV = ASSETS / "04_wardrobe_elevation_overlay_v2.png"  # 3-door 457/457/458
BOARD_QA = ASSETS / "05_qa_contact_sheet_v2.jpg"
EXTERIOR_CONCEPT = ROOT.parent / "docs" / "exterior_colour_concept_nn9589_corrected.png"
EXTERIOR_SWATCH = ROOT.parent / "docs" / "birla_official_swatches_nn9589_nn9590_page133.png"

NN9074 = HexColor("#B5AB9C")
WW0005 = HexColor("#EEEDE9")
NN9088 = HexColor("#E9E3D9")
WW0020 = HexColor("#EDE9E2")
LATTE = HexColor("#A49483")
SLATE = HexColor("#575D5C")
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
    cell_xs = ParagraphStyle(
        "CellXS", parent=styles["Normal"], fontName="Helvetica",
        fontSize=6.4, leading=8.0, textColor=INK,
    )
    cell_xs_b = ParagraphStyle("CellXSB", parent=cell_xs, fontName="Helvetica-Bold")
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
    living = CORRECTED_VIS / "01_living_social_zone_daylight.png"
    if living.exists():
        story.append(fit_image(living, content_w, 88 * mm))
        story.append(Paragraph("Living — social zone (daylight concept · AI-assisted · verify on site)", caption))
    story.append(Paragraph(
        f"Generated {date.today().isoformat()} · Reconciled to SOURCE_OF_TRUTH + CONTRADICTIONS · "
        "3-door wardrobe · S1241 Latte-all · NN9088 Ecru Tint + WW0020 Virgin White",
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
        "Corrected final walls <b>NN9088 Ecru Tint</b>; ceiling <b>WW0020 Virgin White</b>. NN9074/WW0005 retained as a legacy alternate only.",
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
        ("NN9088", "Final walls", "#E9E3D9"),
        ("WW0020", "Final ceiling", "#EDE9E2"),
        ("S1241", "Latte MT", "#A49483"),
        ("84689", "Idria Oak SU", "#3D483C"),
        ("80236", "Slate DW", "#575D5C"),
        ("NN9074", "Legacy wall", "#B5AB9C"),
    ]
    cells = []
    for code, name, hx in swatch_specs:
        c = HexColor(hx)
        dark = hx.upper() in {"#575D5C", "#3D483C", "#4E4C49"}
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
        [Paragraph("Corrected final walls", cell), Paragraph("Birla <b>NN9088</b> Ecru Tint", cell), Paragraph("#E9E3D9 exact", cell)],
        [Paragraph("Corrected final ceiling", cell), Paragraph("Birla <b>WW0020</b> Virgin White", cell), Paragraph("#EDE9E2 exact", cell)],
        [Paragraph("Legacy alternate walls", cell), Paragraph("Birla <b>NN9074</b> Puddle of Grey", cell), Paragraph("Darker greige; optional only", cell)],
        [Paragraph("Legacy alternate ceiling", cell), Paragraph("Birla <b>WW0005</b> White Linen", cell), Paragraph("Optional only", cell)],
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
    pal_img = BOARD_PALETTE
    if pal_img.exists():
        story.append(Spacer(1, 2 * mm))
        story.append(fit_image(pal_img, content_w, 95 * mm))
        story.append(Paragraph(
            "Corrected visual palette board — NN9088 Ecru Tint / WW0020 Virgin White with shared material locks.",
            caption,
        ))
    story.append(PageBreak())

    # ——— BOARDS + HARDWARE (from BOARD_DECISION.md — not Sainik-default) ———
    story.append(Paragraph("Boards & hardware (options + lock)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    story.append(Paragraph(
        "From <b>BOARD_DECISION.md</b> (catalog + user reviews; prior Sainik-wardrobe rec revisited). "
        "Kitchen = shutters-only on existing black granite. Wardrobe = carcass + three hinged Idria leaves. "
        "<b>IS 303:2024</b> = general-purpose MR/BWR/BWP. <b>IS 710:2024</b> = marine. "
        "Product name “710” is not the stamp. Sainik 710 official page = <b>IS 303 BWP</b>. "
        "Greenply Ecotec 710 = IS 303; Greenply <b>710 Marine</b> = IS 710.",
        body,
    ))
    story.append(Paragraph("Locked primary / alternate", h2))
    board_rows = [
        [Paragraph("<b>Location</b>", cell_b), Paragraph("<b>Primary (BOQ)</b>", cell_b), Paragraph("<b>Alternate</b>", cell_b)],
        [Paragraph("Kitchen shutters · S1241 MT Latte 0.8 mm · 2 mm E3 ABS · 3000 K", cell),
         Paragraph("<b>Century Club Prime 19 mm</b> — <b>IS 710</b> on sheet-edge stamp + CenturyPromise QR. Laminate <b>both faces</b>.", cell),
         Paragraph("<b>Boilo 18 mm</b> if CNC/HDF-fluent. <b>Greenply 710 Marine 19 mm</b> (IS 710 stamp). Classic Marine / Bond 710 only if stamped IS 710.", cell)],
        [Paragraph("Wardrobe carcass + 3 Idria leaves · 54×90×19.20 in · 1 mm E3 ABS", cell),
         Paragraph("<b>Club Prime 19 mm</b> or <b>Greenply 710 Marine 19 mm</b> (IS 710 stamp). Same mill as kitchen ply path preferred.", cell),
         Paragraph("<b>HDHMR / HDWR 18 mm</b> if CNC. <b>Boilo too heavy</b> for 90 in doors. <b>Sainik 710 19 mm</b> = contingency only (QR, no core gaps) — <b>not</b> the written default.", cell)],
    ]
    bt = Table(board_rows, colWidths=[48 * mm, 61 * mm, 61 * mm])
    bt.setStyle(tbl_style(SLATE, header_white=True))
    story.append(bt)
    story.append(Paragraph("Options matrix (all cores considered)", h2))
    mx = [
        [Paragraph("<b>Option</b>", cell_xs_b), Paragraph("<b>Official grade</b>", cell_xs_b),
         Paragraph("<b>Kitchen</b>", cell_xs_b), Paragraph("<b>Wardrobe</b>", cell_xs_b),
         Paragraph("<b>Why / why not</b>", cell_xs_b)],
        [Paragraph("Club Prime 19 mm", cell_xs_b), Paragraph("Marine-BWP claimed; confirm IS 710 stamp", cell_xs),
         Paragraph("<b>Y primary</b>", cell_xs), Paragraph("<b>Y primary</b>", cell_xs),
         Paragraph("Composed core + calibration for 0.8 mm + daily cups. Carpenter-native.", cell_xs)],
        [Paragraph("Greenply 710 Marine 19", cell_xs), Paragraph("IS 710 on product page (resole PF)", cell_xs),
         Paragraph("Y peer", cell_xs), Paragraph("Y peer", cell_xs),
         Paragraph("Same role as Club Prime. Not Ecotec.", cell_xs)],
        [Paragraph("Action Tesa Boilo 18", cell_xs), Paragraph("BWP FR HDF (not ply). Density/FR = mill claims", cell_xs),
         Paragraph("Y if CNC", cell_xs), Paragraph("<b>N heavy</b>", cell_xs),
         Paragraph("Homogeneous cups. No independent 3–7 yr diary. ~54 kg/sheet.", cell_xs)],
        [Paragraph("Tesa HDHMR / Greenpanel HDWR 18", cell_xs), Paragraph("IS 12406 family; MR not BWP", cell_xs),
         Paragraph("~ loft", cell_xs), Paragraph("Y CNC", cell_xs),
         Paragraph("Factory shutter. Seal every edge. Open edges swell irreversibly.", cell_xs)],
        [Paragraph("Classic Marine / Bond 710", cell_xs), Paragraph("Dealer IS 710; Classic official page silent", cell_xs),
         Paragraph("~ if stamped", cell_xs), Paragraph("~ if stamped", cell_xs),
         Paragraph("Cost middle. Verbal “marine” is not a stamp.", cell_xs)],
        [Paragraph("Sainik 710 19 mm", cell_xs), Paragraph("<b>IS 303 BWP</b> — not marine IS 710", cell_xs),
         Paragraph("<b>N default</b>", cell_xs), Paragraph("Contingency only", cell_xs),
         Paragraph("Economy / alternate-core risk. Availability ≠ performance. QR still required.", cell_xs)],
        [Paragraph("Ecotec 710 / Vista 710", cell_xs), Paragraph("Ecotec = IS 303; Vista = no IS on site", cell_xs),
         Paragraph("N default", cell_xs), Paragraph("~ until stamp", cell_xs),
         Paragraph("Peer-grade trap. Kitply Gold/Marine only if ISI IS 710.", cell_xs)],
        [Paragraph("Architect / Austin / local 710", cell_xs), Paragraph("Architect = premium claim; Austin inspect-every-sheet", cell_xs),
         Paragraph("Architect = cost", cell_xs), Paragraph("Architect overkill", cell_xs),
         Paragraph("No unique failure mode here. Unbranded 710 = reject.", cell_xs)],
        [Paragraph("Interior MDF / particle board", cell_xs), Paragraph("IS 12406 Gr.2 / IS 3087 · UF", cell_xs),
         Paragraph("<b>N</b>", cell_xs), Paragraph("<b>N</b>", cell_xs),
         Paragraph("Wet swell, hinge tear-out, 4–5 yr write-off.", cell_xs)],
    ]
    mt = Table(mx, colWidths=[36 * mm, 38 * mm, 22 * mm, 26 * mm, 48 * mm])
    mt.setStyle(tbl_style(SLATE, header_white=True))
    story.append(mt)
    story.append(Paragraph(
        "Why Sainik is not the wardrobe lock: 90 in leaves fail by hinge tear-out, sag, and 0.8 mm telegraph — "
        "Sainik does not publish composed-core or screw numbers; “710” ≠ IS 710. Year 3–7 cost is rework, not skipping Club Prime. "
        "Full compare: BOARD_DECISION.md.",
        ParagraphStyle("MxNote", parent=body, fontSize=8, leading=10.5, spaceBefore=2, spaceAfter=4),
    ))
    story.append(PageBreak())

    story.append(Paragraph("Hardware schedule (named series)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6))
    hw_rows = [
        [Paragraph("<b>Item</b>", cell_b), Paragraph("<b>Spec</b>", cell_b), Paragraph("<b>Lock</b>", cell_b)],
        [Paragraph("Pulls", cell),
         Paragraph("Brushed stainless <b>recessed</b> only (J / finger / recessed)", cell),
         Paragraph("<b>LOCKED</b> — no bars / brass / black", cell)],
        [Paragraph("Hinges", cell),
         Paragraph("<b>Hettich Sensys 8645i</b> 110° integrated soft-close; <b>5 per</b> tall wardrobe leaf", cell),
         Paragraph("Kitchen + wardrobe; not Onsys / clip-on dampers. Invoice + carton on site (fakes).", cell)],
        [Paragraph("Channels (if drawers)", cell),
         Paragraph("<b>Hettich KA 5632</b> (45 kg) or <b>KA 4732</b> Silent System (35 kg)", cell),
         Paragraph("Only if drawers exist", cell)],
        [Paragraph("Wardrobe lock", cell),
         Paragraph("<b>Godrej Curvo 8010</b> (25 mm); 8011 if finished stack thicker", cell),
         Paragraph("SS cover. Godrej ≠ concealed hinge.", cell)],
        [Paragraph("Hanging rail", cell),
         Paragraph("Oval <b>30×15 mm</b> + mid-support (Hettich SL 322 / Ebco WRF class)", cell),
         Paragraph("Required at ~centre of 54 in", cell)],
        [Paragraph("Screws", cell),
         Paragraph("<b>SS304</b> in kitchen / wet-risk; Hettich-supplied hinge screws", cell),
         Paragraph("Predrill cups", cell)],
        [Paragraph("Edges", cell),
         Paragraph("E3 ABS matched · <b>2 mm kitchen / 1 mm wardrobe</b>", cell),
         Paragraph("Seal every edge; matt", cell)],
        [Paragraph("Wardrobe hinge value cut", cell),
         Paragraph("<b>Ebco</b> integrated soft-close (named SKU) — wardrobe only", cell),
         Paragraph("Not the kitchen hinge spec", cell)],
    ]
    ht = Table(hw_rows, colWidths=[38 * mm, 84 * mm, 48 * mm])
    ht.setStyle(tbl_style(IDRIA, header_white=True))
    story.append(ht)
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "<b>Executive lock:</b> Kitchen shutters → Club Prime 19 mm IS 710 stamp (or Boilo 18 mm if HDF shop; or Greenply 710 Marine 19 mm). "
        "Wardrobe → Club Prime 19 mm or Greenply 710 Marine 19 mm (HDHMR 18 mm if CNC; not Boilo; Sainik 19 mm contingency only). "
        "Hettich Sensys 8645i · KA 5632/4732 if drawers · Godrej Curvo 8010 · oval 30×15 mm rail with mid-support · "
        "SS304 kitchen · recessed SS pulls only · seal every edge · laminate both faces of kitchen shutters. "
        "Evidence: BOARD_DECISION.md · wiki/01–09 (Honest Interior Source).",
        body,
    ))
    story.append(PageBreak())

    # ——— WIKI LOCKED SPEC + EXPLODED DIAGRAMS ———
    wiki_vis = ROOT / "wiki" / "visuals"
    story.append(Paragraph("Wiki lock — this house (encyclopaedia synthesis)", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    story.append(Paragraph(
        "From <b>wiki/08_BHADRAVATI_LOCKED_SPEC.md</b> after articles 01–06. "
        "Visual method: <b>wiki/09_MODEL_WORKFLOW.md</b> (Grok 4.6 field guide — capture frame, list defects, fix only those; not Trellis). "
        "“710” in a product name is a <b>trademark, not a grade</b>. Sainik 710 and Ecotec 710 print "
        "<b>IS 303 BWP</b>. Greenply <b>710 Marine</b> prints <b>IS 710</b>. Club Prime only if "
        "<b>IS 710 is on the sheet edge</b>. QR ≠ marine. Website ₹/sqft is often the wrong thickness. "
        "Idria Oak is Century <b>European Grey</b> (screen <b>#3D483C</b>), not taupe. "
        "Godrej Curvo 8010 is a <b>lock</b>, not a hinge. Recessed brushed SS only.",
        body,
    ))
    wiki_rows = [
        [Paragraph("<b>Item</b>", cell_b), Paragraph("<b>Lock</b>", cell_b)],
        [Paragraph("Kitchen core", cell),
         Paragraph("<b>Club Prime 19 mm IS 710 stamp</b> (or Boilo 18 mm CNC; or Greenply 710 Marine 19 mm). Not Sainik default.", cell)],
        [Paragraph("Wardrobe core", cell),
         Paragraph("<b>Club Prime or Greenply 710 Marine 19 mm</b>. HDHMR 18 mm if CNC. <b>Not Boilo</b> on 90 in doors. Sainik = contingency.", cell)],
        [Paragraph("Faces", cell),
         Paragraph("<b>S1241 MT</b> Latte all kitchen · <b>84689 SU</b> Idria European Grey wardrobe · <b>80236 DW</b> TV only · finish letters are the SKU.", cell)],
        [Paragraph("Edge / gum", cell),
         Paragraph("E3 <b>ABS 2 mm kitchen / 1 mm wardrobe</b>. Marine/Hi-Per on sheets. PUR edge only if demonstrated.", cell)],
        [Paragraph("Hardware", cell),
         Paragraph("<b>Sensys 8645i</b> (not Onsys), <b>5 cups / 90 in leaf</b>. KA 5632/4732. Curvo <b>8010 lock</b>. Oval 30×15 + mid-support. SS304 wet.", cell)],
        [Paragraph("Community", cell),
         Paragraph("Reddit 403. Fakes are the real risk. No Boilo 2–5 yr diaries. Factory machine edges beat iron-on.", cell)],
    ]
    wt = Table(wiki_rows, colWidths=[38 * mm, 132 * mm])
    wt.setStyle(tbl_style(IDRIA, header_white=True))
    story.append(wt)
    for fname, cap in [
        ("kitchen_exploded.png", "K-01 exploded — granite retained, S1241 MT Latte, B1/B2/B3, 2 mm ABS, recessed SS · conceptual"),
        ("wardrobe_exploded.png", "W-01 exploded — 457/457/458, Idria European Grey #3D483C, 5× Sensys, Curvo 8010 lock · conceptual"),
        ("material_stack.png", "Material stack — both-faces 0.8 mm + ABS wrap · Idria is olive/grey-green, not taupe"),
        ("kitchen_camera.png", "K-01 camera still — S1241 MT Latte #A49483, granite retain, recessed J · conceptual"),
        ("wardrobe_camera.png", "W-01 camera still — 84689 SU Idria European Grey #3D483C, 457/457/458 · conceptual"),
    ]:
        p = wiki_vis / fname
        if p.exists():
            story.append(Spacer(1, 2 * mm))
            story.append(fit_image(p, content_w, 78 * mm))
            story.append(Paragraph(cap, caption))
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
    eve = CORRECTED_VIS / "03_evening_material_lighting_detail.png"
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
        "<b>Essential:</b> Kitchen Latte shutters + wardrobe 3 leaves + NN9088/WW0020 paint + E3 edges + recessed hardware + kitchen task LED.",
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
        (CORRECTED_VIS / "01_living_social_zone_daylight.png", "Living — social zone daylight · no balcony invention · 80236 floating cabinet only"),
        (CORRECTED_VIS / "01b_living_from_tv_toward_sofa.png", "Living — from TV toward sofa"),
        (CORRECTED_VIS / "01c_living_side_across_social.png", "Living — side across social zone"),
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
        (CORRECTED_VIS / "02_kitchen_granite_latte_shutters.png", "Kitchen — granite + Latte shutters"),
        (CORRECTED_VIS / "02b_kitchen_from_fridge_along_run.png", "Kitchen — from fridge along run (fridge right)"),
        (CORRECTED_VIS / "02c_kitchen_loft_shelf_band_detail.png", "Kitchen — loft / mid shelf band detail (schematic)"),
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
        "<b>Corrected final:</b> NN9088 Ecru Tint + WW0020 Virgin White. <b>Legacy alternate:</b> NN9074 + WW0005. "
        "Joinery codes unchanged; the corrected Ecru/ Virgin White render set was visually re-checked against the official shade-card RGB values.",
        body,
    ))
    half = (content_w - 6 * mm) / 2
    for a_n, b_n, label in [
        ("01_living_social_zone_daylight.jpg", "corrected_ecru_virgin_white/01_living_social_zone_daylight.png", "Living"),
        ("02_kitchen_granite_latte_shutters.jpg", "corrected_ecru_virgin_white/02_kitchen_granite_latte_shutters.png", "Kitchen"),
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
    wa, wb = CORRECTED_VIS / "05_wardrobe_aluminium_fluted_glass.png", CORRECTED_VIS / "06_wardrobe_plywood_three_door.png"
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
    bed = CORRECTED_VIS / "04_bedroom_wardrobe_three_door_plywood.png"
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
        (CORRECTED_VIS / "04b_bedroom_from_wardrobe_toward_bed.png", "From wardrobe toward bed"),
        (CORRECTED_VIS / "04c_wardrobe_three_door_detail.png", "Three-door wardrobe detail"),
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
        "Approve sample board (NN9088/WW0020 corrected final; NN9074/WW0005 legacy alternate if desired; S1241; 84689; 80236; E3; recessed SS) beside granite @ morning/afternoon/3000 K.",
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
         "Corrected final NN9088/WW0020 chips; S1241 MT Latte; 84689 Idria; 80236; E3 1&2 mm; recessed brushed SS — beside granite under morning / afternoon / 3000 K. Choose wardrobe A or B."),
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
        "Control docs: SOURCE_OF_TRUTH.md · wiki/00–09 · BOARD_DECISION.md · CONTRADICTIONS.md · "
        "MASTER_BRIEF_V2.md · design_tokens_v2.json · dimension_register_v1.",
        small,
    ))
    story.append(PageBreak())

    # ——— EXTERIOR COLOUR CONCEPT ———
    story.append(Paragraph("Exterior colour concept — industrial-premium envelope", h1))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=4))
    story.append(Paragraph(
        "Corrected concept: Birla Opus <b>NN9589 Studio Pose</b> as the exact muted olive-grey wall field "
        "(<b>#80837D</b> / RGB 128,131,125), with NN9590 No Chance of Sun "
        "(<b>#676B65</b> / RGB 103,107,101) only on existing bands/plinths. "
        "Warm teak-toned door balances the locked interior palette and Idria Oak wardrobe finish.",
        body,
    ))
    if EXTERIOR_CONCEPT.exists():
        story.append(fit_image(EXTERIOR_CONCEPT, content_w, 205 * mm))
        story.append(Paragraph(
            "Corrected conceptual exterior board — NN9589 Studio Pose + NN9590 No Chance of Sun. Preserve existing geometry, openings, drainage, "
            "canopy, grills and signage. Confirm the exact Birla Opus exterior product/tint and approve a physical "
            "façade sample in sun, shade and post-rain conditions before painting.",
            caption,
        ))
    if EXTERIOR_SWATCH.exists():
        story.append(fit_image(EXTERIOR_SWATCH, content_w, 66 * mm))
        story.append(Paragraph(
            "Actual official Birla Opus shade-card reference — page 133: NN9589 Studio Pose and NN9590 No chance of sun.",
            caption,
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

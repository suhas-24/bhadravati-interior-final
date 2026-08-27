# PACKAGE_STATUS — Bhadravati Interior Design V2

**Checked:** 2026-08-27  
**Package root:** `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/`  
**Verdict:** **COMPLETE / READY** for design-control client handoff  
**PDF rebuild for assets 01�05:** **Not required** (already embedded)

**2026-08-27 palette replacement addendum:** Active set is NN9088 Ecru Tint + WW0020 Virgin White + S1241 MT Latte + 83661 SU Sonoma Oak + 80236 DW Slate + existing black granite. Final exterior visual concept is NN9059 Kala Ghoda museum on broad walls, NN9077 Old leaves underfoot on front fascia/balcony bands and splash/plinth zones (full-height only on a shaded lorry-facing side after sample trial), and conceptual NN9079 Dark tidings on the thin roofline edge; roof is muted medium blue-grey with code UNKNOWN / SAMPLE-ONLY. Studio Pose and Idria are rejected. Official Birla pages 104/105 and NN9079 catalogue data were visually checked; exterior product/tint, roof-sheet code and physical façade sample approval remain open.

---

## Summary

| Status | Count | Notes |
|---|---:|---|
| Ready | All listed expected deliverables | Primary client PDF + control docs + boards + generator |
| Missing | 0 | This file was the only gap; now present |
| Needs-refresh | 0 | PDF mtime newer than primary boards; dims match embeds |

---

## Client PDF

| Item | Status | Detail |
|---|---|---|
| `Bhadravati_Interior_Design_V2.pdf` | **Ready** | Exists; **25 pages**; rebuilt 2026-08-27 against corrected Ecru/Virgin White + Sonoma/Kala Ghoda renders |
| Embeds corrected render set | **Ready** | 12 Ecru/Virgin White PNGs are embedded from `assets/img/corrected_ecru_virgin_white/`; legacy palette board is intentionally excluded to prevent stale A-swatch mismatch |
| Excludes `02b` / `04b` / `05b` | **Ready** | Those caution-asset dimensions absent from PDF XObjects |

### Primary board ? PDF embedding

| Board | File | Asset size | In PDF | Page |
|---|---|---|---|---:|
| 01 | `docs/palette_board_schemeB.svg` | vector | Gallery only | — |
| 02 | `assets/02_floorplan_concept_v2.png` | 1696�1503 | Yes | 6 |
| 03 | `assets/03_kitchen_elevation_overlay_v2.png` | 1632�1278 | Yes | 12 |
| 04 | `assets/04_wardrobe_elevation_overlay_v2.png` | 1700�1100 | Yes | 15 |
| 05 | `assets/05_qa_contact_sheet_v2.jpg` | 1656�962 | Yes | 19 |

The PDF was rebuilt after the corrected render set and verified with `_verify_pdf_v2.py`; the old Scheme A palette board is not embedded because it would contradict the corrected pair.

---

## Expected deliverables inventory

### Core documents

| Deliverable | Path | Status |
|---|---|---|
| Client PDF | `Bhadravati_Interior_Design_V2.pdf` | **Ready** |
| Phase / skill log | `PHASE_SKILL_LOG.md` | **Ready** (mtime 09:52; companion doc, not PDF art) |
| Review | `REVIEW.md` | **Ready** (PASS; notes 19-page asset-refreshed PDF) |
| Source of truth | `SOURCE_OF_TRUTH.md` | **Ready** |
| Phase framework | `PHASE_FRAMEWORK.md` | **Ready** |
| Master brief | `MASTER_BRIEF_V2.md` | **Ready** |
| V1 baseline | `V1_BASELINE.md` | **Ready** |
| Contradictions | `CONTRADICTIONS.md` | **Ready** |
| Skills inventory | `SKILLS_INVENTORY.md` | **Ready** |
| Team roles | `TEAM_ROLES.md` | **Ready** |
| Package status | `PACKAGE_STATUS.md` | **Ready** (this file) |

### Generator / tokens

| Deliverable | Path | Status |
|---|---|---|
| PDF generator | `_build_pdf_v2.py` | **Ready** (references boards 01�05) |
| Design tokens | `source/design_tokens_v2.json` | **Ready** |

### Assets � presentation boards (primary)

| Deliverable | Path | Status |
|---|---|---|
| Asset index | `assets/ASSET_INDEX.md` | **Ready** |
| Palette board | `docs/palette_board_schemeB.svg` | **Ready** (corrected pair; gallery) |
| Floorplan concept | `assets/02_floorplan_concept_v2.png` | **Ready** (in PDF) |
| Kitchen elevation | `assets/03_kitchen_elevation_overlay_v2.png` | **Ready** (in PDF) |
| Wardrobe elevation (3-door) | `assets/04_wardrobe_elevation_overlay_v2.png` | **Ready** (in PDF) |
| QA contact sheet | `assets/05_qa_contact_sheet_v2.jpg` | **Ready** (in PDF) |

### Assets � caution / internal only (on disk, not in client PDF)

| Deliverable | Path | Status |
|---|---|---|
| Atmosphere plan ref | `assets/02b_floorplan_atmosphere_reference.png` | **Ready** (internal; correctly excluded) |
| Four-leaf superseded | `assets/04b_wardrobe_elevation_four_leaf_superseded.png` | **Ready** (internal; correctly excluded) |
| Historical QA sheet | `assets/05b_qa_contact_sheet_historical.jpg` | **Ready** (internal; correctly excluded) |

### Assets � room renders / vectors

| Deliverable | Path | Status |
|---|---|---|
| Room / scene images | `assets/img/*` | **Ready** (legacy Scheme A plus corrected Ecru/Virgin White set) |
| SVG sources | `assets/svg/*` | **Ready** (`floor_plan_precise`, palette boards, axonometric) |

---

## Needs-refresh

| Item | Status | Rationale |
|---|---|---|
| Rebuild PDF to embed `assets/01`�`05` | **Not needed** | Boards already embedded; PDF newer than board files; dim QA matches REVIEW |
| Regenerate primary boards | **Not needed** | Present and indexed |
| Companion markdown after PDF | Optional only | `REVIEW.md` / `PHASE_SKILL_LOG.md` updated later the same day; narrative companions, not missing art embeds |

---

## Missing

None after creation of this file.

---

## Absolute paths (key)

- Package: `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/`
- PDF: `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/Bhadravati_Interior_Design_V2.pdf`
- Status: `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/PACKAGE_STATUS.md`
- Generator: `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/_build_pdf_v2.py`

## Post-status caption hygiene (same day)

PDF captions updated for SoT override on QA sheet wardrobe dims (1372×2286×488; 84689 Idria), recessed kitchen pulls (C-08), and floorplan depth 488 mm (not leaf-width OCR). Rebuild was caption-only; boards 01–05 still embedded; 02b/04b/05b still excluded. See `FINAL_QA_CHECKLIST.md` (PASS).

## SKU revalidation — 84689 Idria (2026-08-12)

User challenge that **84689 SU Idria** might be a wrong codename was checked against Century StarLine. **Verdict: CORRECT** — `84689 SU` = **IDRIA OAK** (catalogue p.55 / PDF p.90; index PDF p.143). Backup **84687 SU Lyon Oak** also confirmed (p.57 / PDF p.92). SoT / CONTRADICTIONS C-07 / tokens / FINAL_QA updated with page evidence; PDF chip label normalized to “Idria Oak SU”; PDF rebuilt. Evidence: `source/century_84689_idria_page55_pdfp90.png`.

**Pass 2 (website):** CenturyPly product-page screenshot reconfirms **Idria Oak · 84689 SU · Woodgrains | European Grey · 8×4 ft · 0.8 mm**. Evidence: `source/century_84689_idria_oak_website_2026-08-12.png`. Write-up: `IDRIA_REVALIDATION.md`. No further PDF label fixes.

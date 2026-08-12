# Idria Oak — SKU revalidation (pass 2)

**Date:** 2026-08-12  
**Package:** `Bhadravati_Interior_Design_V2`  
**Question:** Is wardrobe preferred laminate **84689 SU Idria Oak** catalogue-true, or a wrong label (Skagen / missing Oak / wrong finish / wrong thickness / 84688–84687 confusion)?

---

## Verdict: **CORRECT**

| Field | Expected (user) | V2 lock | Match |
|---|---|---|:---:|
| Product name | Idria Oak | Idria Oak | **YES** |
| Code + finish | 84689 SU | 84689 SU | **YES** |
| Category | Woodgrains \| European Grey | European grey oak family (SoT / SVG) | **YES** |
| Sheet size | 8 ft ? 4 ft | StarLine 0.8 mm sheet line | **YES** |
| Thickness | 0.8 mm | Century StarLine 0.8 mm catalogue | **YES** |

**Not Idria:** Skagen Oak = **84688 SU**; Lyon Oak = **84687 SU** (backup only). Do not substitute.

---

## Evidence

### 1. Century StarLine printed catalogue

- File: `/Users/suhas/Downloads/Interiors/Century Laminates StarLine 0.8mm.pdf`
- Printed **p.55** / PDF **p.90**: `84689 SU` / `IDRIA OAK`
- Index PDF **p.143**
- Crop archived: `source/century_84689_idria_page55_pdfp90.png`

### 2. CenturyPly website (user screenshot, 2026-08-12)

Read from image:

- Category: **Woodgrains | European Grey**
- Name: **Idria Oak**
- Code: **84689 SU**
- Size: **8 ft ? 4 ft**
- Thickness: **0.8 mm**

Archived as: `source/century_84689_idria_oak_website_2026-08-12.png`

---

## V2 package audit (this pass)

| Location | Finding |
|---|---|
| Client PDF materials / wardrobe / QA captions | **84689 SU Idria Oak** — no Skagen; Oak present on controlling labels |
| Palette board `01_visual_palette_board_v2.png` | Chip **84689 SU · Idria Oak** (wardrobe face · 3 doors) |
| `source/design_tokens_v2.json` | `84689` / `SU` / `Idria Oak` + website proof path |
| `SOURCE_OF_TRUTH.md` / `CONTRADICTIONS.md` C-07 / `REVIEW.md` | Website + catalogue cited |
| Wrong labels scanned | No remaining Skagen / 84688-as-Idria / 84687-as-preferred / missing Oak on locks |

**PDF rebuild (pass 2):** Not required for labels — commercial name/code/finish already correct.

---

## Pass 3 — visual sample correction (2026-08-12)

**Finding:** SKU / commercial name were correct, but the **on-screen chip appearance was wrong**. Palette board + site swatches used a mid brownish-taupe / Latte-adjacent grain (`#A39178`) that does **not** match Century Idria Oak.

**Correct look (Century evidence):** Woodgrains | European Grey — darker muted olive / grey-green fine vertical woodgrain.

| Before | After |
|---|---|
| Mid taupe-brown synthetic grain · `#A39178` | Century website/catalogue grain sample · screen approx `#3D483C` |

**Actions:**
- Extracted grain tile from `source/century_84689_idria_oak_website_2026-08-12.png` → `source/century_84689_idria_oak_grain_tile.png`
- Rebuilt `assets/01_visual_palette_board_v2.png` Idria chip + hex label
- Recolored `assets/04_wardrobe_elevation_overlay_v2.png` door faces toward Idria grain
- Updated tokens / SVG fills / GitHub Pages site (`docs/index.html` + `swatch_84689_idria_oak.png`)
- Rebuilt client PDF via `_build_pdf_v2.py`

---

## Client lock (unchanged)

Preferred wardrobe face: **Century StarLine 84689 SU Idria Oak (0.8 mm)**  
Backup only: **84687 SU Lyon Oak**

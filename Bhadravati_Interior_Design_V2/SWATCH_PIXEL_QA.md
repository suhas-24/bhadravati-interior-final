# Swatch pixel QA — Bhadravati V2

**Date:** 2026-08-12  
**Method:** Visual Read of official Century/Birla imagery + measured mean RGB from high-res PDF crops (`pymupdf` zoom 3.5) vs current chips.  
**SKU lock unchanged:** 84689 SU Idria Oak · S1241 MT Latte · 80236 DW Slate Grey · NN9074 · WW0005.  
**Board cores unchanged:** Club Prime / Greenply Marine / Boilo as in `BOARD_DECISION.md` (`08db03d`).

Official refs:

- CenturyPly website Idria: `source/century_84689_idria_oak_website_2026-08-12.png`
- Catalogue Idria: StarLine printed p.55 / PDF p.90 (`source/century_84689_idria_page55_pdfp90.png`)
- S1241: StarLine printed p.51 / PDF p.80 Solid MATTE
- 80236 DW: StarLine printed p.7 / PDF p.8 Dyed Wood
- NN9074 / WW0005: Birla Opus shade card published RGB (exact)

---

## Verdict table

| Swatch | Official look | Before (FAIL/PASS) | After | Hex |
|---|---|---|---|---|
| **84689 SU Idria Oak** | Dark European Grey woodgrain; fine **vertical** linear grain; muted olive/charcoal — **not** brown taupe | Palette chip was already website olive grain (**PASS hue**). Wardrobe overlay still **warm brown oak** (**FAIL**). | Recropped website product (UI chrome excluded). Wardrobe doors recolored to Idria grain. | `#3D483C` (mean ~61,72,59) |
| **S1241 MT Latte** | **Solid MATTE** taupe; **no woodgrain** | Palette used **synthetic vertical grain** + lighter `#C8B9A4` (**FAIL**) | Solid catalogue crop `#A49483` rgb 164,148,131. Kitchen overlay shifted toward this. | `#A49483` |
| **80236 DW Slate Grey** | Cool charcoal **dyed wood** with real vertical grain + faint cathedral | Synthetic uniform grain + warm `#4E4C49` (**FAIL**) | Catalogue DW crop `#575D5C` rgb 87,93,92 | `#575D5C` |
| **NN9074 Puddle of Grey** | Solid paint `#B5AB9C` rgb 181,171,156 | Exact fill (**PASS**) | Restored exact shade-card RGB after a bad strip paste | `#B5AB9C` |
| **WW0005 White Linen** | Solid paint `#EEEDE9` rgb 238,237,233 | Exact fill (**PASS**) | Exact fill | `#EEEDE9` |
| **Granite existing black** | Cool black fleck, not quartz | Diagrammatic fleck (**PASS** as site-existing, no manufacturer SKU) | Unchanged | `~#1A1A1A` |
| **NN9088 / GG7140 / GG7162** | Optional only | Hex matches shade card (**PASS**) | Unchanged | published RGB |

### Catalogue vs website Idria (noted, not a SKU change)

| Source | Mean RGB | Hex | Reading |
|---|---|---|---|
| CenturyPly website (locked chip) | 61, 72, 59 | `#3D483B` ? `#3D483C` | Darker olive European Grey — **locked** |
| StarLine print p.55 | 93, 92, 84 | `#5D5C54` | Lighter charcoal print; same SKU, CMYK/scan offset |

Do **not** substitute Skagen 84688 or Lyon 84687. Do **not** use taupe `#A39178`.

---

## FAIL items fixed

1. **S1241 chip was fake woodgrain** ? replaced with Century Solid MATTE catalogue crop (no grain).
2. **S1241 hex too light/beige** (`#C8B9A4`) ? `#A49483` from catalogue chip.
3. **80236 chip was synthetic grain** ? replaced with real DW catalogue crop (vertical grain + cathedral).
4. **80236 hex too warm/dark graphite** (`#4E4C49`) ? `#575D5C` cool slate from catalogue.
5. **Wardrobe elevation overlay showed warm brown oak** ? Idria European Grey website grain on door faces.
6. **Kitchen overlay Latte too light** (mean ~177,165,151) ? shifted toward catalogue `#A49483`.
7. **SVG palette said “4 leaves”** ? **3 doors**; laminate fills updated.
8. **docs/ site swatches** used flat wrong hex; Idria grain URL kept; Slate now uses `swatch_80236_DW_slate_grey.png`.

Kitchen elevation still labels **S1241 MT Latte** (correct SKU — not Idria). Granite in that overlay remains a light speckle vs “black granite” text — existing drawing limitation, not a laminate SKU fail.

---

## Files replaced / added

| Path | Role |
|---|---|
| `assets/01_visual_palette_board_v2.png` | Client palette board chips |
| `assets/img/palette_board.jpg` | JPG copy |
| `assets/03_kitchen_elevation_overlay_v2.png` | Latte hue shift |
| `assets/04_wardrobe_elevation_overlay_v2.png` | Idria grain on doors |
| `source/century_84689_idria_oak_grain_tile.png` | Website recrop |
| `docs/swatch_84689_idria_oak.png` | Site Idria |
| `docs/swatch_S1241_MT_latte.png` | Site Latte (solid) |
| `docs/swatch_80236_DW_slate_grey.png` | Site Slate (DW grain) |
| `FINAL_DELIVERABLE/visuals/swatch_*.png` | Same three |
| `source/design_tokens_v2.json` | Hex approx |
| `docs/index.html` + `docs/coordination/swatch_lock.json` | Site tokens |
| `Bhadravati_Interior_Design_V2.pdf` | Rebuilt after this pass |

Physical sample board beside granite @ morning / afternoon / 3000 K remains mandatory. Screen hex is not a calibrated proof.

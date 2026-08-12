# Bhadravati FINAL Package - QA Findings

**Role:** Final Package QA Lead + Fixer  
**Date:** 2026-08-11  
**Scope:** `FINAL_DELIVERABLE/` audited against MASTER_BRIEF, `design_tokens.json`, docs 01-07, Visual QA Critique, dimension register v1, and all `visuals/` assets.

**Issue count:** **22** (8 blocker - 9 major - 5 minor)

---

## Summary verdict

Package direction (Warm Contemporary Minimalism, Concept A tokens) was correct, but the shipped visuals and text layer had concrete fidelity failures: kitchen granite end-panel/waterfall invention, wrong fridge plan placement, climate-mismatched props, invented balcony architecture, and widespread Windows-1252 encoding mojibake (`-`/`-`/`?` corrupted). Blockers and majors listed below were fixed in this pass; residuals remain for site-measure and a full three-view set per critical room.

---

## Blockers (fixed)

| ID | Issue | Evidence | Fix |
|---|---|---|---|
| B1 | **Kitchen invented granite waterfall / vertical end panel** | Pre-fix `02_kitchen_-png`: left counter continued as floor-to-counter black granite end panel - forbidden by brief (-counter retained; not invented waterfall/end panels-) and Visual QA Critique -B/-3 | Regenerated kitchen (v3) with horizontal granite only + Latte side panel |
| B2 | **Doc/HTML/SVG encoding corruption** | `MASTER_BRIEF.md`, `01`-`08`, `README`, `index.html`, SVGs, `VISUAL_PROMPTS.md` stored as CP1252/mixed bytes (`0x97`, `0x9d`) ? `` / mojibake in UTF-8 readers | Converted text assets to clean UTF-8; restored em dashes, -, ? |
| B3 | **Floor plan fridge on wrong end of kitchen run** | `floor_plan_precise.svg`: fridge north of module (= left when facing east); brief/tokens require fridge **extreme right** | Moved fridge to south/SE; shifted module north; B1?B3 ordered left?right; updated circulation path |
| B4 | **Living invents balcony / French-door railing drama** | Pre-fix `01_living_-png`: black-framed balcony door + outdoor railing not locked by register; risks false openings (QA Critique -1) | Regenerated living without balcony/railing; curtained opening only |
| B5 | **Bedroom large palm prop (climate / geometry mask)** | Pre-fix `04_bedroom_-png`: tall potted palm beside wardrobe - QA Critique -E forbids false plants masking storage/geometry; Japandi-adjacent clutter | Regenerated bedroom; empty corner; four Idria leaves retained |
| B6 | **Kitchen loft / counter geometry not plan-faithful** | Pre-fix kitchen: thick black slab + end panel; weak mid-shelf band vs K-01 (floor?loft 102 in; shelf bands 48 / 23 in) | Regenerated with mid shelf band + loft Latte shutters + painted backsplash; still schematic (residual R1) |
| B7 | **Axonometric fridge annotated -north- of kitchen** | `axonometric_3d.svg` comment + placement implied fridge north of run | Relabelled/repositioned fridge toward extreme-right/south reading |
| B8 | **index.html / docs unreadable separators** | Titles/captions used broken `-` for em dash / multiply (e.g. `54-90-19.2`, `900-1200`) | UTF-8 restore across HTML + markdown |

---

## Majors (fixed unless noted residual)

| ID | Issue | Evidence | Fix / status |
|---|---|---|---|
| M1 | Dual-risk kitchen shutter colour / invented carcass cues | Prior package risk; audit confirmed Latte-all intent in tokens but old PNG end-panel read as new stone carcass | Kitchen regen: all S1241 Latte; shutters-only reading; **residual:** open mid shelves still slightly invented (R2) |
| M2 | Living TV wall compliance | Pre-fix living OK on -no slats-; balcony undermined credibility | Fixed with regen (plain NN9074 + 80236 floating cabinet only) |
| M3 | Wardrobe must be **four** leaves on 54-90-19.2 | Pre-fix 04 already four leaves - PASS; plant was the major defect | Plant removed; four Idria leaves confirmed post-regen |
| M4 | Floor plan punctuation / dim separators corrupted | `21-18`, `1372 - 2286` after bad 0x9d map | Normalized to `21 - 18`, `1372 - 2286 - 488` |
| M5 | Palette board `CRI e90` typo | `palette_board.svg` | Corrected to `CRI ?90` |
| M6 | README file map omitted PNGs | README listed SVGs/HTML but not `01`-`04` PNG concepts | Updated file map |
| M7 | VISUAL_PROMPTS missing waterfall / balcony / plant forbids | Old prompts did not hard-forbid end panels or balcony | Rewrote `VISUAL_PROMPTS.md` with corrected prompts |
| M8 | Three-part visual set per critical room incomplete | QA Critique delivery standard requires wide + opposite + detail per room; package has 4 hero views total | **Residual R3** - not fully regenerated in this pass (time/scope); flagged, not claimed complete |
| M9 | Kitchen tiled backsplash in intermediate regen | v2 kitchen showed glazed tile splash (invented) | Superseded by v3 painted NN9074 splash |

---

## Minors

| ID | Issue | Status |
|---|---|---|
| m1 | Bedroom exterior still reads multi-storey urban facade | Residual - not Bhadravati-specific; mark not verified |
| m2 | Living sparse props on TV cabinet (frame, vessel, mini lamp) | Acceptable; could be emptier |
| m3 | Kitchen gas hob / exact shutter count vs B1/B2/B3 widths | Schematic only - site measure governs |
| m4 | Evening detail TV backlight slightly warm/amber | Intent 3000 K; sample-check under real fixtures |
| m5 | Floor plan still carries authoring comments inside SVG | Harmless; schematic not cut sheet |

---

## What was fixed in this pass

1. Regenerated **01 living**, **02 kitchen**, **03 evening** (retained/confirmed), **04 bedroom** PNGs with corrected prompts.  
2. Rewrote **`visuals/VISUAL_PROMPTS.md`**.  
3. Corrected **`floor_plan_precise.svg`** fridge orientation, B1-B3 order, circulation, UTF-8 dims.  
4. Corrected **`axonometric_3d.svg`** fridge placement note/geometry.  
5. Encoding cleanup across markdown, HTML, SVGs ? UTF-8.  
6. Palette CRI label; README visual file map.  
7. Confirmed tokens in `index.html` swatches match `design_tokens.json` (`#B5AB9C`, `#EEEDE9`, `#C8B9A4`, `#3D483C`, `#4E4C49`).

---

## Residual risks (updated after residual closure pass)

| ID | Risk | Status after residual pass |
|---|---|---|
| R1 | Kitchen loft shelf bands AI-schematic | **Improved / closed for concept** -- closed loft + mid shelf band in `02`/`02b`/`02c`; still not fabrication geometry |
| R2 | Shutter leaf widths / drawer stack vs B1/B2/B3 | **Open** -- site measure / shop drawings |
| R3 | Missing opposite/adjacent views | **Closed** -- three-view sets delivered |
| R4 | All openings unverified | **Open** -- signed site measure |
| R5 | Granite thickness conflict (1.50 in vs 15 mm) | **Open** -- measure stone |
| R6 | Generators may reintroduce waterfall/end panels | **Ongoing process risk** -- re-QA left counter end |

## Post-fix image spot-check

| Asset | Pass notes | Fail / residual |
|---|---|---|
| `01_living_-png` | Floating 80236 only; plain NN9074 TV wall; no balcony; matte; 3000 K pools | Mild styling props on cabinet |
| `02_kitchen_-png` | Single wall; all Latte; fridge right; no waterfall; brushed SS; painted splash | Mid open shelves; loft band schematic; hob not verified |
| `03_evening_-png` | Horizontal granite only; Latte + Slate junction; no gold; matte | Backlight warmth |
| `04_bedroom_-png` | **Four** Idria leaves; no palm; NN9074/WW0005 | Urban exterior view |

---

## Paths touched

- `FINAL_DELIVERABLE/QA_FINDINGS.md` *(this file)*
- `FINAL_DELIVERABLE/visuals/01_living_social_zone_daylight.png`
- `FINAL_DELIVERABLE/visuals/01b_living_from_tv_toward_sofa.png` *(residual pass)*
- `FINAL_DELIVERABLE/visuals/01c_living_side_across_social.png` *(residual pass)*
- `FINAL_DELIVERABLE/visuals/02_kitchen_granite_latte_shutters.png` *(residual regen)*
- `FINAL_DELIVERABLE/visuals/02b_kitchen_from_fridge_along_run.png` *(residual pass)*
- `FINAL_DELIVERABLE/visuals/02c_kitchen_loft_shelf_band_detail.png` *(residual pass)*
- `FINAL_DELIVERABLE/visuals/03_evening_material_lighting_detail.png`
- `FINAL_DELIVERABLE/visuals/04_bedroom_wardrobe_four_shutters.png`
- `FINAL_DELIVERABLE/visuals/04b_bedroom_from_wardrobe_toward_bed.png` *(residual pass)*
- `FINAL_DELIVERABLE/visuals/04c_wardrobe_four_leaf_detail.png` *(residual pass)*
- `FINAL_DELIVERABLE/visuals/VISUAL_PROMPTS.md`
- `FINAL_DELIVERABLE/visuals/floor_plan_precise.svg`
- `FINAL_DELIVERABLE/visuals/axonometric_3d.svg`
- `FINAL_DELIVERABLE/visuals/palette_board.svg`
- `FINAL_DELIVERABLE/visuals/index.html`
- `FINAL_DELIVERABLE/README.md`
- `FINAL_DELIVERABLE/MASTER_BRIEF.md` + `01`-`08` markdown *(encoding)*

---

## Residual closure (2026-08-11 visual QA finisher)

**Scope of this pass:** Close R1 loft-band readability and R3 three-view delivery for Kitchen / Living / Bedroom-wardrobe. Site-measure items (R4-R5) intentionally not fabricated.

### Closed in this pass

| Prior ID | What closed | Evidence |
|---|---|---|
| **R1** (improved) | Kitchen mid open shelves / canisters removed; hero + detail now show continuous mid granite shelf band + **closed** Latte loft shutters with taller loft band vs splash (~48 vs ~23 in intent) | Regenerated `02_-`, added `02b_-`, `02c_-`; Read-tool spot-check |
| **R3** | Three distinct cameras each for Living, Kitchen, Bedroom/wardrobe | Living `01`/`01b`/`01c`; Kitchen `02`/`02b`/`02c`; Bedroom `04`/`04b`/`04c` |
| Gallery / prompts | `index.html` three-view gallery; `VISUAL_PROMPTS.md` updated with K-01 stack table + new angle prompts | UTF-8 rewrite of HTML + prompts |

### Still requires site measure (do not fabricate from PNG)

| ID | Still open | Why |
|---|---|---|
| **R2** | Exact B1/B2/B3 shutter leaf widths / drawer stack vs clear openings | AI shutter count still schematic; overlay after signed measure |
| **R4** | All openings (doors/windows/sills) | Register cites conflicts; PNGs use conceptual curtained/barred openings only |
| **R5** | Granite thickness (1.50 in vs 15 mm conflict) | Drawing conflict unresolved - measure installed stone |
| **R6** | Generator waterfall reintroduction risk | Re-QA left counter end on any future regen |
| **m1** | Bedroom exterior may still read multi-storey urban | Not Bhadravati-verified; ignore for fabrication |
| **m3** | Hob / exact module shutter count | Schematic only |

### Residual post-check (this pass)

| Asset | Pass | Residual |
|---|---|---|
| `02_kitchen_-png` | Closed loft; mid shelf band; no waterfall; fridge right; Latte-all; painted splash; 3000 K | B1/B2/B3 leaf widths schematic |
| `02b_-png` | Adjacent run reading; fridge right; mid band; Latte-all | Exact bay widths schematic |
| `02c_-png` | Mid shelf + loft stack readable; no waterfall | Background doorway props not locked |
| `01` / `01b` / `01c` | Three living cameras; no balcony; 80236 only on TV wall views | Openings unverified |
| `04` / `04b` / `04c` | Four Idria leaves across set; no palm | Urban exterior (m1); labels conceptual |

---

## Orchestration handoff (2026-08-11)

Precision ownership split under `coordination/PROTOCOL.md`. Seeded contracts: `dimension_lock.json` (SVG scale **1 mm = 0.08 px**; prior plan SVG still 0.1 = out of contract), `swatch_lock.json` (Birla hex verified vs extract; laminate hex approx until Color PASS).

**Orchestrator does not regenerate SVG/PNG.** Merge into `index.html` + fill `PRECISION_AUDIT.md` when siblings mark `ready_for_merge`. Live board: `coordination/STATUS.md`. Site-measure residuals R2 / R4 / R5 unchanged.

---

## Orchestration final merge (2026-08-11)

All lanes complete: Color, Dimension (incl. W-01 3-door 457/457/458), wardrobe_door_lock, Visual image_qa (14 PASS / 0 FAIL).

**Merged:** `visuals/index.html` (Option A `05_wardrobe_aluminium_fluted_glass.png` vs Option B `06_wardrobe_plywood_three_door.png`; recessed kitchen+wardrobe; 3-door bedroom set), `PRECISION_AUDIT.md`, `README.md`, `coordination/STATUS.md` = integration_complete.

**Residuals remain site-measure only:** R2 kitchen shutter shop widths, R4 openings, R5 granite thickness, schematic loft/shelf bands.

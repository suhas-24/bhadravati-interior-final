# Bhadravati Interior Design V2 — Asset Index

**Owner:** Visualization / Presentation  
**Purpose:** Client-deliverable page art for the V2 PDF (another agent owns PDF assembly).  
**Concept lock:** Warm Contemporary Minimalism · Scheme A (NN9074 + S1241 Latte + Idria Oak)  
**Status:** Design-control visuals only — not fabrication-approved.

---

## Presentation boards (primary — use these in the PDF)

| File | Absolute path | Role | Recommended PDF placement |
|---|---|---|---|
| `01_visual_palette_board_v2.png` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/01_visual_palette_board_v2.png` | Composite material / colour board with locked primary, hardware/edge/light, optional accents, and DO-NOT-USE rules | Early materials page (after concept statement / before room renders). Full-bleed landscape. |
| `02_floorplan_concept_v2.png` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/02_floorplan_concept_v2.png` | V2 zoning floorplan (single-wall kitchen, W-01 3-door wardrobe, circulation notes) | Plan / zoning page. Prefer this over atmosphere reference. |
| `03_kitchen_elevation_overlay_v2.png` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/03_kitchen_elevation_overlay_v2.png` | K-01 front elevation with clear openings + V2 chrome (Latte, recessed pulls, granite retain) | Kitchen technical / elevation page. Pair with kitchen room renders from `img/`. |
| `04_wardrobe_elevation_overlay_v2.png` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/04_wardrobe_elevation_overlay_v2.png` | W-01 **3-door** elevation composite (face + dimensioned leaf widths 457/457/458) | Wardrobe technical page. **Supersedes** any four-leaf artwork. |
| `05_qa_contact_sheet_v2.jpg` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/05_qa_contact_sheet_v2.jpg` | 6-up QA strip: living, kitchen Latte, kitchen detail, wardrobe 3-door, wardrobe dims, evening light | Optional appendix / visual QA page, or end-matter contact sheet. |

### Supporting / caution assets

| File | Absolute path | Role | Recommended PDF placement |
|---|---|---|---|
| `02b_floorplan_atmosphere_reference.png` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/02b_floorplan_atmosphere_reference.png` | Atmospheric 3D plan from prior Visual Concept package | **Do not use as geometry control.** Optional mood appendix only; kitchen massing may not match single-wall lock. |
| `04b_wardrobe_elevation_four_leaf_superseded.png` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/04b_wardrobe_elevation_four_leaf_superseded.png` | Legacy four-leaf elevation stamped SUPERSEDED | Internal QA only — **exclude from client PDF** unless showing revision history. |
| `05b_qa_contact_sheet_historical.jpg` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/05b_qa_contact_sheet_historical.jpg` | Pre-V2 contact sheet (dark kitchen cabinets) | Internal QA only — **exclude from client PDF**. |

---

## Room / scene renders (`assets/img/`)

Already present JPEG renders for narrative pages. Prefer Scheme A (no `_schemeB` suffix) unless the PDF explicitly compares Scheme B (NN9088).

| File | Suggested page |
|---|---|
| `img/01_living_social_zone_daylight.jpg` | Living hero / daylight |
| `img/01b_living_from_tv_toward_sofa.jpg` | Living alternate view |
| `img/01c_living_side_across_social.jpg` | Living circulation |
| `img/02_kitchen_granite_latte_shutters.jpg` | Kitchen hero (Latte + granite) |
| `img/02b_kitchen_from_fridge_along_run.jpg` | Kitchen run / fridge right |
| `img/02c_kitchen_loft_shelf_band_detail.jpg` | Kitchen loft / shelf band detail |
| `img/03_evening_material_lighting_detail.jpg` | Lighting / 3000 K mood |
| `img/04_bedroom_wardrobe_three_door_plywood.jpg` | Bedroom + wardrobe context |
| `img/04b_bedroom_from_wardrobe_toward_bed.jpg` | Bedroom from wardrobe |
| `img/04c_wardrobe_three_door_detail.jpg` | Wardrobe close-up (also used inside board 04) |
| `img/05_wardrobe_aluminium_fluted_glass.jpg` | Wardrobe Option A |
| `img/06_wardrobe_plywood_three_door.jpg` | Wardrobe Option B face |
| `img/floor_plan_precise.jpg` | Source of board `02` (raw, unframed) |
| `img/palette_board.jpg` | Older dense swatch board — superseded for V2 client PDF by `01_visual_palette_board_v2.png` (still useful if PDF needs denser token dump) |

Scheme B twins (`*_schemeB.jpg`) — optional comparison page only.

---

## Vector sources (`assets/svg/`)

| File | Notes |
|---|---|
| `svg/floor_plan_precise.svg` | Editable plan source for future dimension edits |
| `svg/palette_board.svg` / `palette_board_schemeB.svg` | Editable palette sources |
| `svg/axonometric_3d.svg` | Optional axonometric if PDF wants a 3D diagram |

---

## Quality notes (for PDF agent)

1. **Palette board (`01`)** — Client-ready. Locked codes match `MASTER_BRIEF_V2` / `design_tokens_v2.json`. Woodgrain swatches are approximate composites from available shade PNGs blended to locked hex — physical laminate samples still required.  
2. **Floorplan (`02`)** — Best V2 geometry control (single-wall kitchen, 3-door W-01). Relational only; site measure supersedes.  
3. **Kitchen elevation (`03`)** — Reuses high-quality Visual Concept overlay; chrome adds V2 lock language. Drawn bar pulls on the source elevation may not match recessed-pull lock — footer already flags this; PDF caption should prefer “recessed brushed stainless.”  
4. **Wardrobe elevation (`04`)** — Correct **3-door** configuration. Do not ship `04b` or the Visual Concept four-leaf PNG to the client.  
5. **QA sheet (`05`)** — Useful appendix. Some baked-in overlay text on source room JPGs may still show legacy product wording; prefer titles/captions from this index / brief over OCR of those overlays.  
6. **Do not regenerate** kitchen elevation from scratch — existing overlay quality is higher than a new flat redraw.  
7. **Root shade PNGs** (`80171`, `83386`, `83736`, `844485`, `NN-9088`) were used only as texture grain references; they are **not** the locked product codes (Latte / Idria / Slate).

---

## Suggested PDF page flow (visual spine only)

1. Cover / concept statement  
2. `01_visual_palette_board_v2.png`  
3. `02_floorplan_concept_v2.png`  
4. Living renders (`img/01*`)  
5. Kitchen renders + `03_kitchen_elevation_overlay_v2.png`  
6. Wardrobe Option A/B renders + `04_wardrobe_elevation_overlay_v2.png`  
7. Lighting / evening (`img/03_*`)  
8. Optional: `05_qa_contact_sheet_v2.jpg`  
9. Specs / exclusions / next steps (text-owned by brief agent)

---

## Provenance

| Asset | Built from |
|---|---|
| Palette board | `design_tokens_v2.json` + root shade PNGs + NN-9088 |
| Floorplan V2 | `assets/img/floor_plan_precise.jpg` + V2 lock banner |
| Floorplan atmosphere | `Bhadravati_Visual_Concept_Render/01_finished_floorplan_concept.png` |
| Kitchen elevation | `Bhadravati_Visual_Concept_Render/02_finished_kitchen_elevation_overlay.png` |
| Wardrobe elevation | `img/06_wardrobe_plywood_three_door.jpg` + `img/04c_wardrobe_three_door_detail.jpg` |
| Wardrobe superseded | `Bhadravati_Visual_Concept_Render/03_finished_wardrobe_elevation_overlay.png` |
| QA V2 | Selected `assets/img/*.jpg` |
| QA historical | `Bhadravati_Corrected_Renders/qa_contact_sheet.jpg` |

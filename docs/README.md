# Bhadravati Home -- Final Interior Design Package

**FINAL concept:** Warm Contemporary Minimalism (climate-resilient)  
**Coordination status:** `integration_complete` (Color + Dimension + Wardrobe door + Visual locks)

Design-control handoff for client review and fabricator briefing. Location: first-floor studio, Bhadravati, Karnataka.

---

## Download PDF

**[Bhadravati_FINAL_Interior_Design.pdf](Bhadravati_FINAL_Interior_Design.pdf)** — client handoff package (design direction, locked palette, K-01/W-01 dimensions, concepts, next actions).

---

## Open the visual presentation

Open this folder’s `index.html` (GitHub Pages) or `visuals/index.html` in the deliverable.  
Includes floor plan, axonometric, palette board, three-view room sets, **wardrobe Options A / B**, and a sticky **Paint scheme** toggle (Scheme A / Scheme B). Preference persists in `localStorage` (`bhadravati-paint-scheme`); URL hashes `#scheme-a` / `#scheme-b` also work.

---

## Locked palette and finishes

For the industrial-belt dust/smoke rationale, visual swatch evidence, and the explicit exterior-source gate, see [`BIRLA_OPUS_COLOUR_SELECTION.md`](../BIRLA_OPUS_COLOUR_SELECTION.md).

| Role | Spec |
|------|------|
| Main walls (Scheme A default) | Birla Opus **NN9074** Puddle of Grey `#B5AB9C` |
| Ceiling (Scheme A) | Birla Opus **WW0005** White Linen `#EEEDE9` |
| Main walls (Scheme B) | Birla Opus **NN9088** Ecru Tint `#E9E3D9` |
| Ceiling (Scheme B) | Birla Opus **WW0020** Virgin White `#EDE9E2` |
| Kitchen shutters (all) | Century **S1241 MT Latte** |
| TV cabinet only | **80236** DW Slate Grey |
| Wardrobe niche | W-01 **1372 x 2286 x 488 mm** |
| Wardrobe doors | **3 doors** (1 single L + 1 double R) -- leaves **457 / 457 / 458 mm** |
| Wardrobe Option A | Aluminium frame + fluted glass (`05_...`) |
| Wardrobe Option B | Plywood / Idria face (`06_...`) |
| Handles | **Recessed only** (kitchen + wardrobe) -- no projecting bars |
| Counter | Existing **black granite** (retain) |
| Hardware finish | Brushed stainless (recessed profiles) |
| Lighting baseline | **3000 K** |

Matte / low-sheen finishes throughout. Machine-readable tokens: `design_tokens.json`. Locks: `coordination/*_lock.json` (incl. `scheme_b_swatch_lock.json`) + `image_qa.json`.

**Paint scheme toggle:** sticky segmented control in `index.html` switches CSS swatches, palette board (`palette_board.svg` / `palette_board_schemeB.svg`), and gallery image sources (`*_schemeB.png` when present; falls back to Scheme A with a “Scheme B image pending” badge).

---

## File map

| File | Contents |
|------|----------|
| `01_Design_Direction.md` ... `08_*.md` | Design package chapters |
| `MASTER_BRIEF.md` | Authoritative one-brief summary |
| `design_tokens.json` | Codes, dims, next actions |
| `visuals/index.html` | Presentation gallery (merged) |
| `visuals/01` / `01b` / `01c` | Living three-view set |
| `visuals/02` / `02b` / `02c` | Kitchen three-view (recessed pulls) |
| `visuals/03_*` | Evening junction detail |
| `visuals/04_*three_door*` / `04b` / `04c_*three_door*` | Bedroom plywood 3-door continuity set |
| `visuals/05_wardrobe_aluminium_fluted_glass.png` | **Wardrobe Option A** |
| `visuals/06_wardrobe_plywood_three_door.png` | **Wardrobe Option B** |
| `visuals/*.svg` | Floor plan, axonometric, palette board |
| `visuals/VISUAL_PROMPTS.md` | Prompt archive |
| `QA_FINDINGS.md` | QA audit log |
| `PRECISION_AUDIT.md` | Final precision audit (Orchestrator) |
| `coordination/` | PROTOCOL, STATUS, swatch/dimension/wardrobe_door locks, image_qa |

---

## Next 3 actions

1. **Complete and sign the site-measure sheet** (kitchen, wardrobe, openings).
2. **Approve the physical sample board** and choose wardrobe **Option A or B**.
3. **Lock fabricator shop drawings and quotation** (3-door 457/457/458, recessed pulls, chosen face).

---

## Important note

Images and diagrams are **conceptual**. Design-control only -- not fabrication-approved until signed site measure and physical sample approval.

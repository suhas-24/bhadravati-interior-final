# Bhadravati Home — Source of Truth (Technical Spec Auditor)

**Status:** Verified design-control pack for other agents. **Not fabrication-approved.**  
**Units:** inches unless stated; mm = in ? 25.4 (rounded).  
**Auditor date:** 2026-08-12  
**Rule:** Do not invent SKUs. Codes below are catalogue-confirmed or explicitly flagged UNKNOWN / SAMPLE-ONLY.

---

## Authority hierarchy (do not invert)

1. **Signed site-measure sheet** (photographed tape end-to-end) — supersedes everything when complete.  
2. **`interior_dimension_control/dimension_register_v1.json` + `.md`** — labelled clear openings from K-01 / W-01.  
3. **This file + locked palette in Final Brief / FINAL tokens** — material codes after visual audit.  
4. **Concept renders / handover PDFs** — visual intent only; never cut from them.  
5. **Rendered 21 ? 18 ft plan** — room relationship only; **not** a cut sheet.

---

## Project identity

| Field | Value | Citation |
|---|---|---|
| Location | First-floor studio, Bhadravati, Karnataka | `FINAL_DELIVERABLE/README.md`, Professional PDF |
| Concept (locked) | Warm Contemporary Minimalism — climate-resilient | Final Brief MD; Visual QA Critique |
| Style note | Japandi is optional / not governing | Final Brief MD § Final direction |
| Overall envelope | **21 ft ? 18 ft** (~6401 ? 5486 mm; ~378 sq ft) | Dimension register non-fabrication note; Professional PDF; plan image P-01 |
| Envelope confidence | **plan_relationship_only** | `dimension_register_v1.json` ? `non_fabrication_evidence` |

---

## Rooms (spatial schedule)

Positions follow the supplied rendered plan (P-01) and Professional / Final Brief room schedule. Treat as relational until openings are site-verified.

| Zone | Plan position | Design intent (locked) | Citation |
|---|---|---|---|
| Bedroom | SW / bottom-left | Queen bed; two nightstands; warm textiles; no dark feature wall | Professional PDF p.2–4; Final Brief § Room schedule |
| Living | S-centre / bottom-centre | 3-seat sofa; round coffee table; floating TV cabinet; **no** TV feature wall / marble / slats / gold | Same |
| Kitchen | SE / bottom-right | **Single-wall** existing black granite; shutters only; sink under window; fridge extreme right | Same + Visual QA Critique |
| Bathroom | NW / top-left | Open shower retained; basin outside shower | Same |
| Wardrobe / dressing | N-centre between bath & study | Niche shutters over existing granite carcass | W-01; Professional PDF |
| Study | NE / top-right | Desk at large window; limited shallow shelves | Final Brief § Study |

---

## Key dimensions (design baseline — not cut list)

### Kitchen — K-01

**Evidence:** `WhatsApp Image 2026-08-07 at 9.46.31 PM (1).jpeg` ? register evidence id **K-01**.  
**Source files:**  
- `/Users/suhas/Downloads/Interiors/interior_dimension_control/dimension_register_v1.json`  
- `/Users/suhas/Downloads/Interiors/interior_dimension_control/dimension_register_v1.md`

| Item | in | mm (calc) | Status |
|---|---:|---:|---|
| Overall granite module width | 106.00 | 2692 | labelled clear / module |
| Reference total wall width | 220.00 | 5588 | labelled |
| Floor ? loft underside | 102.00 | 2591 | labelled |
| Loft underside ? lower shelf underside | 48.00 | 1219 | labelled |
| Lower shelf underside ? countertop top | 23.00 | 584 | labelled |
| Floor ? countertop top | 31.00 | 787 | labelled |
| Internal countertop depth | 19.20 | 488 | labelled |
| B1 left clear opening | 48.00 | 1219 | finished clear |
| B2 middle clear opening | 36.00 | 914 | finished clear |
| B3 right clear opening | 18.00 | 457 | finished clear |
| Nominal sides/partitions (?4) | 1.00 each | 25 | drawing assumption |

**Arithmetic (register):** B1+B2+B3 = 102 in; + four 1 in supports = 106 in — **PASS**.

**CRITICAL thickness conflict (do not cut):** drawing assumes **1.50 in** loft/counter/shelf thickness **and** notes **15 mm (0.59 in)** granite for all slabs. **Measure installed stone.** See `CONTRADICTIONS.md` C-01.

**Drawing note (K-01):** requests aluminium shutters for B1/B2/B3 but does **not** specify rail/stile, overlay, gaps, or hardware. Locked **finish** direction for client package is Century laminate (below), not an aluminium-system shop drawing. Fabrication system remains **open** until shop drawings + site measure.

### Wardrobe — W-01

**Evidence:** `WhatsApp Image 2026-08-07 at 9.46.31 PM (2).jpeg` ? **W-01**.

| Item | in | mm (calc) | Status |
|---|---:|---:|---|
| Finished clear width | 54.00 | 1372 | labelled |
| Finished clear height | 90.00 | 2286 | labelled |
| Internal depth | 19.20 | 488 | labelled |
| Left compartment clear | 21.00 | 533 | labelled |
| Granite partition | 0.59 | 15 | labelled |
| Right compartment clear | 32.41 | 823 | labelled |
| Left openings T?B | 12 / 19.5 / 19.5 / 19.5 / 19.5 | 305 / 495… | labelled |
| Right stack T?B | 12 / 39 hang / 9.5 drawer / 12 / 17.5 | 305 / 991 / 241 / 305 / 445 | labelled |

**Arithmetic (register):** 21 + 0.59 + 32.41 = 54; left & right stacks = 90 — **PASS**.

**Door leaf count:** see `CONTRADICTIONS.md` C-02. Latest client lock in FINAL package = **3 leaves** 457 / 457 / 458 mm (sum 1372). Older briefs say **four** narrower leaves. V2 agents must follow the **3-door lock** unless client reverses in writing.

### Openings (UNVERIFIED — do not fabricate)

Cited across Corrected Handover / Professional PDF; **not** in dimension register as measured values:

| Opening | Cited value(s) | Conflict? |
|---|---|---|
| Main door | 1051 mm inward | Unverified |
| Bedroom west window | Professional: two **4 ft ? 4 ft**; Corrected: **4 ft 9 in ? 3 ft** | **YES** — C-05 |
| Bathroom west window | Corrected: **2 ft ? 4 ft**; Professional also notes hand mark **1 ft 8 in** | Unverified / conflicting annotations |
| Study north window | **5.5 ft ? 4 ft** | Unverified |
| Kitchen east window | **3 ft 2 in ? 4 ft** | Unverified |

---

## Materials & finishes (locked codes)

### Paint — Birla Opus (catalogue-verified)

Catalogue: `/Users/suhas/Downloads/Interiors/Birla_Opus_INTERIOR_Shade_Card.pdf`  
Extract: `/Users/suhas/Downloads/Interiors/processed_pdf_text/birla_opus_shade_card_extracted.txt`  
Brief: `/Users/suhas/Downloads/Interiors/Bhadravati_Final_Interior_Design_Brief/Bhadravati_Final_Interior_Design_Brief.md`

| Role | Code | Name | Hex (shade card) | Notes |
|---|---|---|---|---|
| Main walls (Scheme A **default**) | **NN9074** | Puddle of Grey | `#B5AB9C` RGB 181,171,156 | Exact match in shade card |
| Lighter walls (Scheme B alt) | **NN9088** | Ecru Tint | `#E9E3D9` RGB 233,227,217 | Exact; shows dust faster |
| Ceiling (Scheme A) | **WW0005** | White Linen | `#EEEDE9` RGB 238,237,233 | Exact |
| Ceiling (Scheme B) | **WW0020** | Virgin White | Present in shade card as WW 0020 | Used in FINAL Scheme B; confirm physical sample |
| Optional green accent | **GG7140** / **GG7162** | Tender Buds / Old Olive Trees | `#9CAE91` / `#B9CEA4` | One small wall max |
| Study optional | **BB5146** / **BG6116** | Old Novel / Songs from the Valley | `#90B1C3` / `#8BA6A3` | Controlled accent only |
| Limited accent also audited | GG7054 | (name in brief audit list) | Shade card lists GG 7054 | Accent-only; not default |

**Workspace paint sample asset:** `/Users/suhas/Downloads/Interiors/NN-9088.png` — visual sample for **NN9088** only (not default walls).

### Laminates — Century StarLine (catalogue-verified)

Catalogue: `/Users/suhas/Downloads/Interiors/Century Laminates StarLine 0.8mm.pdf`  
Extract: `/Users/suhas/Downloads/Interiors/processed_pdf_text/century_starline_extracted.txt`  
Evidence crop (Idria catalogue PDF): `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/source/century_84689_idria_page55_pdfp90.png`  
Evidence (Idria CenturyPly website, 2026-08-12): `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/source/century_84689_idria_oak_website_2026-08-12.png`

| Role | Code | Finish | Name | Catalogue check | Notes |
|---|---|---|---|---|---|
| Kitchen base + drawers + loft (**all**) | **S1241** | **MT** | Latte | `S1241 MT` / `LATTE` present | **One code only** — no dual-tone kitchen |
| Kitchen backup (if Latte fails sample) | **S1173** | **MT** | Cloud Grey | Present | Backup only |
| TV cabinet (controlled accent) | **80236** | **DW** | Slate Grey | `80236 DW` present | **Not** for kitchen shutters |
| Wardrobe preferred | **84689** | **SU** | Idria Oak | **CONFIRMED** — StarLine printed **p.55** (PDF p.90): `84689 SU` / `IDRIA OAK`; index PDF p.143; **website** confirms Idria Oak / 84689 SU / Woodgrains · European Grey / 8?4 ft / **0.8 mm** | Prefer over Lyon. Also listed as `84689 CL` Crystal Line (PDF p.12) — project lock remains **SU** |
| Wardrobe backup | **84687** | **SU** | Lyon Oak | **CONFIRMED** — StarLine printed **p.57** (PDF p.92): `84687 SU` / `LYON OAK`; index PDF p.143 | Backup only |

**2026-08-12 SKU revalidation (pass 1):** User challenge that “84689 SU Idria” might be wrong was checked against the Century StarLine PDF + extract + index. **Verdict: code and commercial name are correct.** Do not substitute Skagen (`84688 SU`) or Lyon (`84687 SU`) as Idria.

**2026-08-12 SKU revalidation (pass 2 — website):** User-supplied CenturyPly product-page screenshot re-confirms **Idria Oak · 84689 SU · Woodgrains | European Grey · 8 ft ? 4 ft · Thickness 0.8 mm**. See `IDRIA_REVALIDATION.md`.

Laminate hexes in tokens (`#C8B9A4`, `#3D483C`, `#4E4C49`) are **screen approx**. Idria `#3D483C` was re-sampled 2026-08-12 from the CenturyPly product-page image (European Grey olive/grey-green) — prior `#A39178` taupe was a wrong visual approx. Catalogue extract has no RGB. Physical sample required.

### Edge / hardware / lighting

| Item | Spec | Citation |
|---|---|---|
| Edge band | E3 ABS matched to exact laminate; kitchen **2 mm**, wardrobe **1 mm** | Final Brief; E3 extract (1.00 / 2.00 mm available) |
| Edge finish | Matt / soft touch — **not** gloss/sparkle | `swatch_lock.json` |
| Hardware finish | Brushed stainless | Final Brief |
| Handle type (latest lock) | **Recessed** (J-pull / finger-pull) — no projecting bars | `wardrobe_door_lock.json`; FINAL design_tokens |
| Screws (wet risk) | SS304 | Final Brief |
| Lighting CCT | **3000 K** baseline (bedroom lamps 2700–3000 K) | Final Brief; Visual QA |
| Counter | Existing **black granite** — retain; shutters only | Visual QA Critique |

### Boards (substrate — not decorative SKUs)

| Component | Board guidance | Citation |
|---|---|---|
| Kitchen shutters | **Club Prime 19 mm** with **IS 710** stamp (or Boilo 18 mm if CNC; or Greenply 710 Marine 19 mm). Not Sainik default. | `BOARD_DECISION.md` |
| Kitchen loft | 18 mm HDHMR if fully ABS-sealed; else same ply as shutters | Same |
| Wardrobe carcass + 3 leaves | **Club Prime 19 mm** or **Greenply 710 Marine 19 mm**; HDHMR 18 mm if CNC. Sainik 710 19 mm = contingency only. Boilo too heavy. | Same |
| Reject | MR, interior MDF, particle board, unbranded “710”, 16 mm tall doors | Same |
| Adhesive | PUR only if demonstrated on actual machine | Final Brief |

---

## Root laminate PNG samples — asset audit (not locked primary palette)

These files exist in workspace root. They are **not** the locked kitchen/wardrobe primary codes.

| File | Claimed code from filename | Catalogue reality | Use in locked brief? |
|---|---|---|---|
| `/Users/suhas/Downloads/Interiors/80171 DW Light Brown.png` | 80171 DW Light Brown | `80171 DW` / LIGHT BROWN present | **No** — sample only |
| `/Users/suhas/Downloads/Interiors/83386 SU Gravel Oak.png` | 83386 SU Gravel Oak | `83386 SU` / GRAVEL OAK present | **No** — sample only; Final Brief lists as audited wood option family |
| `/Users/suhas/Downloads/Interiors/83736 CL Wiertz Sandalwood.png` | 83736 CL Wiertz Sandalwood | `83736 CL` and `83736 SU` present; name appears as Sandalwood family | **No** — audited option only; spelling **Wiertz / Wirtz** varies in docs |
| `/Users/suhas/Downloads/Interiors/844485 SU Hector Pine.png` | **844485** SU Hector Pine | Catalogue has **`84485 SU` HECTOR PINE** (not 844485). Nearby `84448 SU` is **TEAKWOOD** | **Filename SKU error** — see C-06. Do not order as 844485 |
| `/Users/suhas/Downloads/Interiors/NN-9088.png` | NN-9088 | Matches Birla **NN 9088** Ecru Tint | Scheme B sample only |

**Advance 0.8 mm** catalogue (`Advance 0.8mm (1) (1).pdf`) was visually audited in Final Brief (alt codes 9084/9105/9090/9087/117 etc.) but **no Advance code is locked** for this project. Do not substitute Advance for Century without a new client lock.

---

## Fabrication hold-points (mandatory)

From dimension register:

- Do **not** manufacture shutters from clear-opening values directly; convert after overlay/inset/hardware choice.  
- Confirm plumb/square at top/middle/bottom; granite niches rarely square.  
- Resolve sink/hob/fridge/electrical clearances (kitchen) and door-swing/beam/skirting (wardrobe).  
- Signed site-measure sheet supersedes this register.

---

## Document map (primary citations)

| Document | Absolute path | Role |
|---|---|---|
| Dimension register JSON | `/Users/suhas/Downloads/Interiors/interior_dimension_control/dimension_register_v1.json` | Dimensional SoT |
| Dimension register MD | `/Users/suhas/Downloads/Interiors/interior_dimension_control/dimension_register_v1.md` | Same, human table |
| Final design brief MD | `/Users/suhas/Downloads/Interiors/Bhadravati_Final_Interior_Design_Brief/Bhadravati_Final_Interior_Design_Brief.md` | Palette lock text |
| Visual QA Critique | `/Users/suhas/Downloads/Interiors/Bhadravati_Final_Interior_Design_Brief/Bhadravati_Visual_QA_Critique.md` | Non-negotiables / render fails |
| Professional design PDF | `/Users/suhas/Downloads/Interiors/Bhadravati_Professional_Interior_Design/Bhadravati_Professional_Interior_Design.pdf` | Early complete professional pack |
| **V1 FINAL client PDF** | `/Users/suhas/Downloads/Interiors/FINAL_DELIVERABLE/Bhadravati_FINAL_Interior_Design.pdf` | Most complete client handoff (see `V1_BASELINE.md`) |
| FINAL tokens | `/Users/suhas/Downloads/Interiors/FINAL_DELIVERABLE/design_tokens.json` | Machine codes + dims |
| Swatch lock | `/Users/suhas/Downloads/Interiors/FINAL_DELIVERABLE/coordination/swatch_lock.json` | Hex verification |
| Wardrobe door lock | `/Users/suhas/Downloads/Interiors/FINAL_DELIVERABLE/coordination/wardrobe_door_lock.json` | 3-door 457/457/458 |
| Century extract | `/Users/suhas/Downloads/Interiors/processed_pdf_text/century_starline_extracted.txt` | SKU existence |
| Birla extract | `/Users/suhas/Downloads/Interiors/processed_pdf_text/birla_opus_shade_card_extracted.txt` | Paint RGB/hex |

---

## Explicit unknowns

- Exact kitchen shutter leaf shop widths vs B1/B2/B3 clear (overlay/reveals TBD).  
- Granite thickness (1.50 in vs 15 mm).  
- All door/window sill dimensions (conflicts exist).  
- Hob / sink exact positions beyond “sink under window / fridge right” (pending site confirm).  
- Whether wardrobe face is Option A (aluminium + fluted glass) or Option B (plywood / Idria) — **client choice open**.  
- Physical sample approval for S1241 / 84689 / NN9074 beside granite under morning / afternoon / 3000 K — **not recorded as approved**.

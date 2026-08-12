# Bhadravati Home — V1 Baseline (Technical Spec Auditor)

**Auditor date:** 2026-08-12  
**Purpose:** Identify which existing PDF is the authoritative **V1** client deliverable, what it does well, and what **V2** must fix or improve.  
**Scope rule:** Do not generate the V2 PDF here.

---

## Primary V1 PDF (designated)

| Field | Value |
|---|---|
| **File** | `/Users/suhas/Downloads/Interiors/FINAL_DELIVERABLE/Bhadravati_FINAL_Interior_Design.pdf` |
| **Also mirrored** | `/Users/suhas/Downloads/Interiors/docs/Bhadravati_FINAL_Interior_Design.pdf` |
| **Generated** | 2026-08-11 |
| **Pages** | 10 |
| **Size** | ~1.5 MB |
| **Package status** | `integration_complete` (Color + Dimension + Wardrobe door + Visual locks) |
| **Explicit label in V2 docs** | Supersede target / `FINAL_v1` (`MASTER_BRIEF_V2.md`, `PHASE_SKILL_LOG.md`) |

### Why this is V1 (not older Bhadravati_* packs)

Compared to Aug 7 `Bhadravati_*` PDFs, this FINAL PDF is the **most complete client handover**:

1. Multi-page design-control handoff (direction, palette schemes A/B, dimensions, floor plan, living/kitchen/wardrobe sets, next actions).  
2. Backed by machine tokens + coordination locks (`design_tokens.json`, `swatch_lock.json`, `dimension_lock.json`, `wardrobe_door_lock.json`, `image_qa.json`).  
3. Three-view visual sets for living / kitchen / bedroom–wardrobe + wardrobe Options A/B.  
4. Client overrides already partially applied: **3-door wardrobe**, **recessed** pulls, Scheme A/B paint toggle.  
5. Explicitly treated as V1 by the V2 workstream.

**Not designated as primary V1** (keep as context / do not treat as controlling):

| PDF | Path | Why secondary |
|---|---|---|
| Professional Interior Design (12 pp) | `/Users/suhas/Downloads/Interiors/Bhadravati_Professional_Interior_Design/Bhadravati_Professional_Interior_Design.pdf` | Strong early professional spec (Aug 7); still says **four** wardrobe leaves; lighter visual package than FINAL |
| Corrected Client Handover (8 pp) | `/Users/suhas/Downloads/Interiors/Bhadravati_Corrected_Visualization/Bhadravati_Corrected_Client_Handover_Visualization.pdf` | Large render pack but **material schedule contradicts** locked brief (dual-tone kitchen, Lyon, NN9088 as used) — see `CONTRADICTIONS.md` |
| Client Visualization (8 pp) | `/Users/suhas/Downloads/Interiors/Bhadravati_Client_Visualization/Bhadravati_Client_Interior_Visualization.pdf` | Earlier concept renders; superseded |
| Finished Visual Concept (4 pp) | `/Users/suhas/Downloads/Interiors/Bhadravati_Visual_Concept_Render/Bhadravati_Finished_Interior_Visual_Concept.pdf` | Overlay concept only; no photoreal set |
| Final Brief PDF (3 pp) | `/Users/suhas/Downloads/Interiors/Bhadravati_Final_Interior_Design_Brief/Bhadravati_Final_Interior_Design_Brief.pdf` | Spec text only; prefer the `.md` twin for editing |
| Resilient Indian Home (34 pp) | `/Users/suhas/Downloads/Interiors/The Resilient Indian Home_ A Site-Specific Material and Colour Strategy for Durability and Well-Being in Bhadravati.pdf` | Research / durability essay — **not** a dimensional or SKU handoff |

---

## What V1 is strong at

1. **Correct concept language:** Warm Contemporary Minimalism; climate (dust, hard water, humidity, glare); Japandi not governing.  
2. **Kitchen non-negotiables stated:** retain black granite; shutters only; **S1241 MT Latte** on base + loft + drawers; fridge extreme right; no island / L-flip.  
3. **Dimension tables** aligned to dimension register K-01 / W-01 (106 / 220 / 102 / 48 / 23 / 31 / 19.2; B1–B3 48/36/18; wardrobe 54×90×19.2).  
4. **Paint lock with verified hexes** for NN9074 / WW0005 / NN9088 against Birla shade card.  
5. **Century codes catalogue-confirmed** for S1241 MT, 80236 DW, **84689 SU Idria Oak** (StarLine p.55 / PDF p.90), **84687 SU Lyon Oak** (p.57 / PDF p.92), S1173 MT.  
6. **Visual QA awareness:** forbids waterfall granite ends, balcony invention, gloss, TV feature walls (documented in `QA_FINDINGS.md`).  
7. **Wardrobe Options A/B** (aluminium fluted glass vs plywood/Idria) with recessed hardware direction.  
8. **Site-measure residuals honestly open** (R2 shutter shops, R4 openings, R5 granite thickness).

Supporting package roots:

- `/Users/suhas/Downloads/Interiors/FINAL_DELIVERABLE/`  
- Gallery: `/Users/suhas/Downloads/Interiors/FINAL_DELIVERABLE/visuals/index.html` (and docs mirror)

---

## What V2 must fix / improve

Priority ordered for the next client PDF (content fidelity — not styling fluff).

### Critical (must not ship again)

| ID | Issue in / around V1 | V2 requirement |
|---|---|---|
| F1 | **Four-leaf language still appears** in older chapters / budget text / swatch use-rule / legacy filenames (`*four*`) while door lock says **3 doors 457/457/458** | One global wardrobe story only: **3 leaves, single L + double R, 457/457/458 mm** |
| F2 | **Corrected Handover PDF** still in circulation with dual-tone kitchen (80236 base + Warm Greige loft), Lyon Oak, NN9088 as “materials used” | V2 must state it **supersedes** that material schedule; never copy those codes as current |
| F3 | Granite **1.50 in vs 15 mm** conflict unresolved | Call out as measure-on-site; never pick one for fabrication |
| F4 | Opening sizes conflicting / unverified | Label every opening **UNVERIFIED**; do not hard-dimension doors/windows from plan annotations |
| F5 | Root sample PNG **`844485`** miscodes Hector Pine | Do not print 844485; catalogue is **84485 SU** (or omit sample codes not in locked palette) |

### Major (client clarity / agent safety)

| ID | Issue | V2 requirement |
|---|---|---|
| F6 | Handle language historically mixed (projecting bars vs recessed) | Recessed only; show it consistently in captions |
| F7 | Scheme A vs B paint: Corrected pack used NN9088 as default | Default walls = **NN9074**; NN9088 = alternate only |
| F8 | Kitchen drawing mentions aluminium shutters; package shows laminate faces | Clarify: finish lock = **S1241 MT Latte** laminate (or Option A aluminium face for wardrobe only); kitchen aluminium system = **open / TBD with fabricator** if pursued |
| F9 | Incomplete separation of design-control vs fabrication | Every dim page: “clear openings ? cut list” |
| F10 | Residual AI schematic risks (loft bands, shutter count vs B1/B2/B3) | Caption visuals as schematic; attach register table as controlling |

### Quality / package hygiene

| ID | Issue | V2 requirement |
|---|---|---|
| F11 | Encoding / mojibake history in markdown | Ship clean UTF-8 only |
| F12 | Legacy `four_shutters` filenames aliasing 3-door content | Prefer `three_door` names; avoid four-leaf captions |
| F13 | Budget chapter still says “wardrobe four-leaf” in places | Align budget/phase language to 3-door lock |
| F14 | Swatch lock still says wardrobe “four equal vertical leaves” | Update any copied swatch prose to 3-door |
| F15 | No signed site measure yet | Keep fabrication hold banner on every technical page |

---

## V1 package checklist (for agents using V1 as input)

**Trust for codes / dims:**

- `FINAL_DELIVERABLE/design_tokens.json`  
- `interior_dimension_control/dimension_register_v1.*`  
- `Bhadravati_Final_Interior_Design_Brief/Bhadravati_Final_Interior_Design_Brief.md`  
- `FINAL_DELIVERABLE/coordination/wardrobe_door_lock.json` (door count)  
- `FINAL_DELIVERABLE/coordination/swatch_lock.json` (paint hexes; **ignore** its outdated four-leaf use_rule — see C-02)

**Do not trust as controlling:**

- Material schedule page of Corrected Client Handover Visualization  
- Any render inventing L-kitchen, island, waterfall ends, balcony, TV marble wall  
- Root PNGs 80171 / 83386 / 83736 / 844485 as if they were locked primary finishes  
- 21×18 ft plan for cabinet cut sizes

---

## Handoff to V2 PDF authors

V2 should **supersede**  
`/Users/suhas/Downloads/Interiors/FINAL_DELIVERABLE/Bhadravati_FINAL_Interior_Design.pdf`  
and must remain consistent with:

1. `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/SOURCE_OF_TRUTH.md`  
2. `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/CONTRADICTIONS.md`  
3. `/Users/suhas/Downloads/Interiors/interior_dimension_control/dimension_register_v1.json`

Do **not** invent new laminate/paint SKUs. Flag unknowns as UNKNOWN.

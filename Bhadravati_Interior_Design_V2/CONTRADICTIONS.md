# Bhadravati Home — Contradictions Register (Critical)

**Auditor date:** 2026-08-12  
**Severity:** Items marked **CRITICAL** can cause wrong fabrication, wrong procurement, or client mistrust if agents pick the wrong side.  
**Rule:** Prefer authority hierarchy in `SOURCE_OF_TRUTH.md`. Do not invent a third value.

---

## C-01 — Kitchen granite / slab thickness (CRITICAL)

| Side A | Side B |
|---|---|
| K-01 assumed loft/counter/shelf thickness **1.50 in** | K-01 note: granite thickness assumed **15 mm (0.59 in)** for all slabs |

**Sources:**  
`/Users/suhas/Downloads/Interiors/interior_dimension_control/dimension_register_v1.json` (`kitchen.notes`)  
`/Users/suhas/Downloads/Interiors/interior_dimension_control/dimension_register_v1.md` (“Critical conflict”)

**Resolution for agents:** **Neither** is fabrication-ready. Measure installed stone. Do not average. Do not silently pick 15 mm or 1.50 in.

---

## C-02 — Wardrobe door count: 4 leaves vs 3 doors (CRITICAL)

| Claim | Where it appears |
|---|---|
| **Four** narrower vertical shutters | Final Brief MD § Wardrobe; Professional PDF wardrobe elevation; Visual Concept PDF; Visual QA Critique; early FINAL QA (`QA_FINDINGS` M3); `swatch_lock.json` use_rule for 84689; `06_Budget_Phasing.md` essential tier |
| **Three** doors (1 single L + 1 double R), leaves **457 / 457 / 458 mm** | `FINAL_DELIVERABLE/coordination/wardrobe_door_lock.json` (client directive); `PRECISION_AUDIT.md`; FINAL `design_tokens.json`; `MASTER_BRIEF_V2.md`; image QA overwrites of `*four*` filenames |

**Niche size is not in conflict:** clear opening remains **54 × 90 × 19.20 in** (1372 × 2286 × 488 mm) in both stories.

**Resolution for agents (current lock):** Use **3 doors / 457–457–458 mm** as the controlling client lock for V2. Treat four-leaf text as **superseded** unless client reverses in writing. Do not invent a hybrid (e.g. “3 or 4”).

---

## C-03 — Kitchen shutter colour: dual-tone vs Latte-all (CRITICAL)

| Claim | Where |
|---|---|
| **Same** Century **S1241 MT Latte** on base + drawers + loft | Final Brief MD; Professional PDF; Client Visualization; Visual Concept; Visual QA Critique; FINAL tokens |
| Dual-tone: base **80236 DW Slate Grey** + loft **Warm Greige Matte** (non-SKU name) | Corrected Client Handover Visualization material schedule + kitchen caption |

**Sources (wrong pack):**  
`/Users/suhas/Downloads/Interiors/Bhadravati_Corrected_Visualization/Bhadravati_Corrected_Client_Handover_Visualization.pdf`  
(extracted: `_qa_geometry_review/Bhadravati_Corrected_Client_Handover_Visualization_extracted_text.json`)

**Resolution:** Locked brief wins — **S1241 MT Latte only** for all kitchen shutters. **80236 DW** is TV-cabinet accent only. “Warm Greige Matte” is **not** a Century code — do not procure by that name.

---

## C-04 — Default wall paint: NN9074 vs NN9088 (CRITICAL)

| Claim | Where |
|---|---|
| Default main walls **NN9074 Puddle of Grey**; NN9088 = lighter alternative | Final Brief MD; Professional PDF room schedule; FINAL Scheme A; swatch lock |
| Materials used in renders: walls **NN9088 Ecru Tint** / ceiling WW0005 | Corrected Client Handover Visualization material schedule |

**Resolution:** Default = **NN9074**. NN9088 is Scheme B / client opt-in only. Root sample `NN-9088.png` does **not** make NN9088 the default.

---

## C-05 — Bedroom window size (CRITICAL for architecture fidelity)

| Claim | Where |
|---|---|
| Two **4 ft × 4 ft** windows | Professional PDF spatial layout (“project brief states…”) |
| Bedroom west **4 ft 9 in × 3 ft** | Corrected Handover dimension/QA page |
| Tokens flag conflict: `4ft9in x 3ft_OR_4ft9in x 4ft_conflict` | `FINAL_DELIVERABLE/design_tokens.json` ? `openings_unverified_from_prior_docs` |

**Resolution:** Mark **UNVERIFIED**. Site-measure both width and height. Do not hard-code either value into a fabrication or opening schedule. Renders must not invent a third geometry.

---

## C-06 — Root sample filename `844485` vs catalogue `84485` (CRITICAL procurement)

| Claim | Reality |
|---|---|
| File named **`844485 SU Hector Pine.png`** | Century StarLine extract lists **`84485 SU` HECTOR PINE** |
| Nearby code **`84448 SU`** | Is **TEAKWOOD**, not Hector Pine |

**Sources:**  
`/Users/suhas/Downloads/Interiors/844485 SU Hector Pine.png`  
`/Users/suhas/Downloads/Interiors/processed_pdf_text/century_starline_extracted.txt` (pages ~113 / index)

**Resolution:** Do **not** order **844485** (unknown / likely typo). If referencing Hector Pine sample, catalogue code is **84485 SU**. This code is **not** in the locked primary palette (wardrobe = 84689 / backup 84687).

---

## C-07 — Wardrobe laminate: Idria vs Lyon (major)

| Claim | Where |
|---|---|
| Preferred **84689 SU Idria Oak** | Final Brief; Professional; Visual Concept; FINAL tokens |
| Corrected pack “materials used”: **84687 SU Lyon Oak** | Corrected Client Handover |
| Challenge: “84689 SU Idria” codename may be incorrect | User query 2026-08-12 |

**Catalogue proof (Century StarLine 0.8mm.pdf):**
- **84689 SU = IDRIA OAK** — printed catalogue **p.55** (PDF page **90**); design-code index PDF page **143**. Evidence crop: `source/century_84689_idria_page55_pdfp90.png`.
- **84687 SU = LYON OAK** — printed catalogue **p.57** (PDF page **92**); same index page **143**. Image: `processed_pdf_images/century/page_092.png`.
- Adjacent code **84688 SU = SKAGEN OAK** (also p.55) — do not confuse with Idria.

**Resolution:** Preferred = **84689 SU Idria Oak** (catalogue-confirmed). Lyon **84687** = backup only after sample failure / client choice. Challenge closed — **not a wrong SKU**.

---

## C-08 — Handle type: projecting vs recessed (major)

| Claim | Where |
|---|---|
| Brushed stainless handles (type unspecified / often shown as bars in early concept overlays) | Visual Concept kitchen overlay; older brief hardware line |
| **Recessed** J-pull / finger-pull only; projecting bars forbidden | `wardrobe_door_lock.json`; FINAL `design_tokens.json`; V2 master brief |

**Resolution:** Current client lock = **recessed**. Do not show projecting bar handles in V2 as the approved standard.

---

## C-09 — Kitchen shutter system: aluminium (drawing) vs laminate face (package) (major)

| Claim | Where |
|---|---|
| K-01 requests **aluminium shutters** for B1/B2/B3 (system unspecified) | Dimension register `kitchen.notes` |
| Client finish package specifies **Century S1241 MT Latte** laminate on shutters | Final Brief; Professional; FINAL PDF |

**Resolution:** Do not collapse these into one sentence without nuance. **Finish / colour lock** = S1241 MT Latte. **Frame system** (aluminium framed vs full plywood laminate shutter) remains a fabricator decision requiring shop drawings — unless client selects a specific system in writing. Wardrobe Option A (aluminium + fluted glass) is a **wardrobe** face option, not automatic kitchen approval.

---

## C-10 — Internal FINAL package drift: budget / swatch still say four leaves (major)

Even inside the designated V1 package, after the 3-door lock:

| File | Problem |
|---|---|
| `FINAL_DELIVERABLE/06_Budget_Phasing.md` | Still budgets “wardrobe **four-leaf**” / “4 leaves” |
| `FINAL_DELIVERABLE/coordination/swatch_lock.json` | 84689 use_rule still says “**four** equal vertical leaves” |
| Legacy visual filenames `*four_shutters*` / `*four_leaf*` | Content overwritten to 3-door per `image_qa.json`, but names mislead |

**Resolution for V2:** Globally align to 3-door lock. Do not copy budget/swatch four-leaf prose forward.

---

## C-11 — Bathroom window annotation conflict (moderate)

| Claim | Where |
|---|---|
| Bathroom west **2 ft × 4 ft** | Corrected Handover openings list |
| Hand annotation / visible plan: bathroom window **1 ft 8 in** (partial) | Professional PDF “Visible plan annotations” |

**Resolution:** UNVERIFIED — site measure. Do not fabricate from either.

---

## C-12 — Spelling / finish variance on sample 83736 (minor but procurement-sensitive)

| Variant | Where |
|---|---|
| **83736 CL Wiertz Sandalwood** | Root PNG filename |
| **83736 SU Wirtz Sandalwood** (audited wood option) | Final Brief visual catalogue conclusions |
| Catalogue lists **83736 CL** and **83736 SU** | Century extract |

**Resolution:** Not a locked primary finish. If ever sampled, specify **exact finish code (CL vs SU)** from physical chip; do not mix CL file with SU order language.

---

## C-13 — Envelope 21×18 ft vs fabrication use (process)

| Claim | Where |
|---|---|
| Overall room **21 ft × 18 ft** used on many PDF covers/plans | Professional, Client Viz, Corrected, FINAL |
| Register: rendered plan **must not** derive cabinet/circulation cut dimensions | `dimension_register_v1.json` `non_fabrication_evidence` |

**Resolution:** Keep 21×18 as **relational** only. Not a contradiction of numbers — a **misuse risk** if agents treat it as a cut sheet.

---

## Summary — controlling answers when conflicted

| Topic | Controlling answer |
|---|---|
| Kitchen shutters colour | **S1241 MT Latte** all |
| TV accent laminate | **80236 DW** (or Latte if lighter) |
| Wardrobe laminate | **84689 SU Idria** (backup 84687) |
| Default walls | **NN9074** |
| Ceiling default | **WW0005** |
| Wardrobe leaf count | **3** @ 457/457/458 mm |
| Niche size | **54 × 90 × 19.20 in** |
| Kitchen module | **106 in**; B1/B2/B3 **48/36/18** |
| Granite thickness | **UNKNOWN — measure** |
| Openings | **UNVERIFIED** |
| Code 844485 | **Do not use** (typo; catalogue 84485 if needed) |

---

## Evidence paths (quick)

- Dimension SoT: `/Users/suhas/Downloads/Interiors/interior_dimension_control/dimension_register_v1.json`  
- Palette SoT text: `/Users/suhas/Downloads/Interiors/Bhadravati_Final_Interior_Design_Brief/Bhadravati_Final_Interior_Design_Brief.md`  
- Wrong material schedule: `/Users/suhas/Downloads/Interiors/Bhadravati_Corrected_Visualization/Bhadravati_Corrected_Client_Handover_Visualization.pdf`  
- 3-door lock: `/Users/suhas/Downloads/Interiors/FINAL_DELIVERABLE/coordination/wardrobe_door_lock.json`  
- Catalogue checks: `/Users/suhas/Downloads/Interiors/processed_pdf_text/century_starline_extracted.txt`, `.../birla_opus_shade_card_extracted.txt`

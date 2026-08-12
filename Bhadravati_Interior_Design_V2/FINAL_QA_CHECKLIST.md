# Bhadravati Interior Design V2 ù FINAL Visual + Spec QA Checklist

**Auditor:** Visual + Spec QA workstream (parallel)  
**Date:** 2026-08-12  
**Workspace:** `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/`  
**Cross-checked against:** `SOURCE_OF_TRUTH.md`, `CONTRADICTIONS.md`, `source/design_tokens_v2.json`, `assets/ASSET_INDEX.md`, `_build_pdf_v2.py`  
**Scope:** Design-control client package ù **not fabrication-approved**  
**Commit/push:** None (this workstream does not commit)

---

## Overall verdict: **PASS**

Required lock items below are **PASS**. Residual PDF-rebuild blockers are caption/OCR hygiene (not lock failures) and are listed at the end for the PDF agent.

| Category | Result |
|---|:---:|
| S1241 Latte-all kitchen (no dual-tone) | **PASS** |
| Wardrobe 3-door 457/457/458 (no 4-leaf in client set) | **PASS** |
| NN9074 default / NN9088 alt only | **PASS** |
| No 844485 as primary SKU | **PASS** |
| Excluded superseded assets (02b / 04b / 05b boards) | **PASS** |
| Asset files exist and are usable | **PASS** |

---

## 1. Kitchen ù S1241 Latte-all (no dual-tone) ù **PASS**

| # | Check | Evidence | Result |
|---|---|---|:---:|
| K1 | Kitchen finish lock = Century **S1241 MT Latte** on base + drawers + loft | `SOURCE_OF_TRUTH.md` laminates; `CONTRADICTIONS.md` C-03; `design_tokens_v2.json` `kitchen_shutters_all` | **PASS** |
| K2 | No dual-tone (80236 / ùWarm Greige Matteù) as kitchen story | Palette board `01` DO-NOT-USE: ùNo dual-tone kitchen - Latte onlyù; elevation `03` chrome: ùSAME S1241 MT LATTE ON BASE + LOFTù; kitchen hero `img/02_kitchen_granite_latte_shutters.jpg` uniform Latte | **PASS** |
| K3 | 80236 DW Slate = TV cabinet only, not kitchen | Palette board `01` chip role; SoT + C-03 | **PASS** |
| K4 | Granite retained; shutters-only; single-wall | Floorplan `02` V2 LOCK banner; elevation `03`; SoT rooms schedule | **PASS** |
| K5 | Historical dual-tone / dark kitchen not in client primary set | `05b_qa_contact_sheet_historical.jpg` stamped ùHISTORICAL QA STRIP (pre-V2)ù ù excluded (see ù5) | **PASS** |

---

## 2. Wardrobe ù 3-door 457 / 457 / 458 (no 4-leaf in client set) ù **PASS**

| # | Check | Evidence | Result |
|---|---|---|:---:|
| W1 | Client lock = **3 doors**, leaves **457 / 457 / 458 mm** (sum 1372) | `CONTRADICTIONS.md` C-02; SoT W-01; tokens `leaf_widths_mm`; board `04` dimensioned overlay | **PASS** |
| W2 | Primary elevation shows 3-door single-L + double-R | `04_wardrobe_elevation_overlay_v2.png` (1700ù1100); footer ùSUPERSEDES prior four-leafù | **PASS** |
| W3 | Preferred face = **84689 SU Idria Oak** (backup 84687) | Board `04` chrome; tokens; SoT; **Century StarLine p.55 / PDF p.90 + index PDF p.143** (`84689 SU` / `IDRIA OAK`); Lyon backup StarLine p.57 / PDF p.92 | **PASS** |
| W4 | Four-leaf artwork not in client PDF allowlist | `04b_wardrobe_elevation_four_leaf_superseded.png` red SUPERSEDED banner; `_build_pdf_v2.py` does not reference it | **PASS** |
| W5 | Room renders show three vertical leaves | `img/04*`, `img/06_wardrobe_plywood_three_door.jpg`, QA sheet `05` panels ùWardrobe 3-doorù | **PASS** |

---

## 3. Paint ù NN9074 default / NN9088 alt only ù **PASS**

| # | Check | Evidence | Result |
|---|---|---|:---:|
| P1 | Scheme A default walls = **NN9074** Puddle of Grey `#B5AB9C` | Palette board `01` LOCKED PRIMARY; tokens; SoT; C-04 | **PASS** |
| P2 | Ceiling default = **WW0005** White Linen | Same | **PASS** |
| P3 | **NN9088** = Scheme B / alternate only (not default) | Palette board OPTIONAL row ùScheme B walls (alt)ù; C-04 resolution | **PASS** |
| P4 | Root sample `NN-9088.png` not treated as default wall lock | SoT paint section; ASSET_INDEX provenance | **PASS** |

---

## 4. SKU hygiene ù no 844485 as primary ù **PASS**

| # | Check | Evidence | Result |
|---|---|---|:---:|
| S1 | Locked primary codes exclude 844485 / Hector Pine | Tokens + palette board primaries: NN9074, WW0005, S1241, 84689, 80236, granite | **PASS** |
| S1b | **84689 SU Idria Oak** is catalogue-true (not a false codename) | Century PDF p.90 + index p.143 + SoT revalidation 2026-08-12; evidence `source/century_84689_idria_page55_pdfp90.png` | **PASS** |
| S2 | Filename typo **844485** flagged do-not-order (catalogue **84485 SU** if ever sampled) | `CONTRADICTIONS.md` C-06; SoT root PNG audit; `_build_pdf_v2.py` procurement warning | **PASS** |
| S3 | Root shade PNGs (80171 / 83386 / 83736 / 844485 / NN-9088) not shipped as locked product chips | ASSET_INDEX quality note ù7 ù grain reference only | **PASS** |

---

## 5. Excluded superseded assets (02b / 04b / 05b) ù **PASS**

Client PDF set must use **primary** boards only. These files may remain on disk for internal QA but must **not** be embedded in the client PDF.

| File | Absolute path | Why excluded | In `_build_pdf_v2.py`? | Result |
|---|---|---|---|:---:|
| `02b_floorplan_atmosphere_reference.png` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/02b_floorplan_atmosphere_reference.png` | Atmosphere only; not geometry control | **No** | **PASS** |
| `04b_wardrobe_elevation_four_leaf_superseded.png` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/04b_wardrobe_elevation_four_leaf_superseded.png` | Four-leaf V1; stamped SUPERSEDED | **No** | **PASS** |
| `05b_qa_contact_sheet_historical.jpg` | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/05b_qa_contact_sheet_historical.jpg` | Pre-V2 dark / dual-tone kitchen strip | **No** | **PASS** |

**Allowlist (client primaries):**

| File | Path | Size / pixels | Result |
|---|---|---|:---:|
| `01_visual_palette_board_v2.png` | `.../assets/01_visual_palette_board_v2.png` | 221 KB ù 1800ù1180 | **PASS** |
| `02_floorplan_concept_v2.png` | `.../assets/02_floorplan_concept_v2.png` | 654 KB ù 1696ù1503 | **PASS** |
| `03_kitchen_elevation_overlay_v2.png` | `.../assets/03_kitchen_elevation_overlay_v2.png` | 704 KB ù 1632ù1278 | **PASS** |
| `04_wardrobe_elevation_overlay_v2.png` | `.../assets/04_wardrobe_elevation_overlay_v2.png` | 781 KB ù 1700ù1100 | **PASS** |
| `05_qa_contact_sheet_v2.jpg` | `.../assets/05_qa_contact_sheet_v2.jpg` | 194 KB ù 1656ù962 | **PASS** |

**Note:** Room renders `img/02b_kitchen_from_fridge_along_run.jpg` and `img/04b_bedroom_from_wardrobe_toward_bed.jpg` are **not** the superseded presentation boards; they are valid Scheme A views and may appear in the PDF.

---

## 6. Asset files exist and are usable ù **PASS**

| # | Check | Result |
|---|---|:---:|
| A1 | All five primary boards open as valid RGB PNG/JPEG via Pillow; non-trivial file size | **PASS** |
| A2 | Key room renders present (`01*`, `02*`, `03_*`, `04*`, `05_*`, `06_*`) | **PASS** |
| A3 | SVG sources present under `assets/svg/` | **PASS** |
| A4 | Excluded boards present on disk (for internal QA) and correctly labeled | **PASS** |
| A5 | `ASSET_INDEX.md` paths match filesystem | **PASS** |

---

## Blockers / instructions for PDF rebuild agent

These do **not** reverse the overall PASS on locks, but must be handled before shipping a client PDF that relies on OCR-able baked-in overlay text.

### B1 ù Contact sheet panel ùWardrobe dimsù baked-in text (**HIGH**)

`05_qa_contact_sheet_v2.jpg` middle-bottom panel still shows legacy overlay wording inconsistent with SoT:

| Baked-in (avoid trusting) | Controlling lock |
|---|---|
| Height / depth variants e.g. **2386** / **458** | Clear niche **1372 ù 2286 ù 488 mm** |
| Wrong laminate code/name (e.g. R4089 / ùStile Oakù) | **84689 SU Idria Oak** |

**Action:** Prefer PDF page captions from `MASTER_BRIEF_V2` / tokens / this checklist. Do not OCR that panel into tables. Optionally regenerate panel or crop overlay before embedding. ASSET_INDEX already warns of this.

### B2 ù Kitchen elevation bar pulls vs recessed lock (**MEDIUM**)

`03_kitchen_elevation_overlay_v2.png` source drawing may still show projecting bar pulls; V2 chrome correctly states recessed brushed stainless.

**Action:** Caption must say **recessed** J-pull / finger-pull; do not present drawn bars as approved hardware (C-08).

### B3 ù Floorplan board depth / label hygiene (**MEDIUM**)

`02_floorplan_concept_v2.png` is correct on single-wall + 3-door story, but some on-drawing numeric chips may show **458** where register depth is **488 mm**. Treat plan as relational zoning; cite W-01 / K-01 from SoT in text tables, not from OCR of every chip.

### B4 ù Do not re-include excluded boards (**CRITICAL if violated**)

Never embed:

- `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/02b_floorplan_atmosphere_reference.png`
- `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/04b_wardrobe_elevation_four_leaf_superseded.png`
- `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/05b_qa_contact_sheet_historical.jpg`

Current `_build_pdf_v2.py` allowlist is correct ù keep it that way.

### B5 ù Non-blockers (open by design ù do not invent)

- C-01 granite thickness (1.50 in vs 15 mm) ù measure site  
- C-05 / C-11 openings ù UNVERIFIED  
- C-09 kitchen aluminium frame system vs laminate face ù finish lock = S1241; system open  
- Physical sample approval not recorded  

---

## Citation map (quick)

| Control | Path |
|---|---|
| Spec SoT | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/SOURCE_OF_TRUTH.md` |
| Contradictions | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/CONTRADICTIONS.md` |
| Tokens | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/source/design_tokens_v2.json` |
| Asset index | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/assets/ASSET_INDEX.md` |
| PDF builder | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/_build_pdf_v2.py` |
| This checklist | `/Users/suhas/Downloads/Interiors/Bhadravati_Interior_Design_V2/FINAL_QA_CHECKLIST.md` |

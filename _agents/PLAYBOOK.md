# Agent Playbook — Workflows & QA Gates

Companion to `../AGENTS.md`. Every workflow ends with a gate that must pass before you report done.
**Universal rules:** repo-relative paths · never invent SKUs/dims/prices · nothing is fabrication-approved · update `_agents/STATE.md` when finished.

---

## Workflows

### W1 — Verify a SKU / shade ("is this laminate real?")
1. Search the pre-extracted catalogs first (never open the 15–54 MB PDFs):
   `grep -i "<code>" processed_pdf_text/century_starline_extracted.txt processed_pdf_text/birla_opus_shade_card_extracted.txt processed_pdf_text/e3_ebt_extracted.txt`
2. Record the catalogue page / PDF page exactly (e.g. Century p.55 = PDF p.90).
3. Pull the page image as evidence from `processed_pdf_images/<brand>/` into
   `Bhadravati_Interior_Design_V2/source/` named `<brand>_<code>_<name>_pageNN.pngNN.png`.
4. If a physical chip scan exists at repo root (`80171…png` etc.), do pixel QA against the catalogue swatch (see Gate G2).
5. Write the verdict into `Bhadravati_Interior_Design_V2/SOURCE_OF_TRUTH.md` (+ `CONTRADICTIONS.md` if it contradicts an earlier entry) citing the evidence file.
   Precedent to follow: `IDRIA_REVALIDATION.md` (84689 SU Idria Oak, two-pass verification).

### W2 — Change a dimension or finish
1. Check the authority hierarchy (`AGENTS.md §0`). Dimensions may ONLY come from:
   signed site measure > `interior_dimension_control/dimension_register_v1.json`. Never from photos or renders.
2. Run the arithmetic reconciliation before proposing (register precedent: B1+B2+B3 = 102″; +4×1″ sides = 106″ module ⇒ PASS).
3. Flag thickness assumptions explicitly (known conflict: K-01 loft/shelf 1.5″ vs 15 mm granite note — measure installed stone).
4. Update sources in this order: register JSON/MD → `SOURCE_OF_TRUTH.md` → `design_tokens_v2.json` → relevant lock in `FINAL_DELIVERABLE/coordination/`.
5. Then trigger W4 (rebuild) for anything client-facing.

### W3 — Generate / regenerate renders
1. Read the established prompt conventions: `docs/VISUAL_PROMPTS.md`.
2. Scene naming: `<NN>_<scene>[_<variant>].png`; every Scheme A render gets a `_schemeB` twin unless it's paint-independent.
3. Bake the non-negotiables into every prompt (they are also the QA checklist):
   single-wall kitchen w/ existing black granite, shutters only · fridge extreme right · wardrobe = 3 doors 457/457/458 mm in 1372 mm clear · recessed stainless pulls · matte finishes · 3000 K warm light · NO TV feature wall / island / L-flip / gold strips / slat walls / gloss.
4. New images go to `FINAL_DELIVERABLE/visuals/` (gallery set) and/or `Bhadravati_Interior_Design_V2/assets/img/`.
5. Pass Gate G3, append results to `coordination/image_qa.json` (+ `scheme_b_image_qa.json`), refresh contact sheet.

### W4 — Rebuild the client PDF
1. `cd Bhadravati_Interior_Design_V2 && python3 _build_pdf_v2.py` (embeds primary boards 01–05; excludes internal 02b/04b/05b).
2. `python3 _verify_pdf_v2.py` must PASS (Gate G4).
3. Confirm embed table still true (see `PACKAGE_STATUS.md`: board→page map, asset pixel dims).
4. Caption hygiene: captions must reflect SoT overrides (wardrobe 1372×2286×488 mm, 84689 Idria; recessed pulls C-08; floorplan depth 488 mm).

### W5 — Publish to GitHub Pages
1. Gallery source of truth is `docs/`. Sync changed renders/PDF there (mirrors exist: `docs/coordination/swatch_lock.json` etc.).
2. Sanity-check `docs/index.html` references resolve (no broken relative paths).
3. `git add … && git commit && git push origin main` — CI (`.github/workflows/pages.yml`) deploys automatically on push.
4. After push, verify https://suhas-24.github.io/bhadravati-interior-final/ shows the update (and Scheme B toggle isn't stuck on "pending").

### W6 — Client handover checklist
- [ ] `_verify_pdf_v2.py` PASS; PDF mtime newer than embedded assets
- [ ] `PACKAGE_STATUS.md` refreshed (Ready/Missing/Needs-refresh tables)
- [ ] `REVIEW.md` verdict updated
- [ ] `_agents/STATE.md` updated
- [ ] No UNKNOWN/SAMPLE-ONLY item presented as confirmed
- [ ] AI-visual disclosure present (ethics rule)
- [ ] "Not fabrication-approved" notice intact

---

## Gates (all must PASS before "done")

**G1 Dimension reconciliation** — every sum closes; no value sourced below its authority level; conflicts flagged, not averaged.

**G2 Swatch pixel lock** — rendered/chip colors match locked values in `coordination/swatch_lock.json` / `scheme_b_swatch_lock.json` within tolerance recorded there. Method precedent: `Bhadravati_Interior_Design_V2/SWATCH_PIXEL_QA.md`.

**G3 Image QA** — each render checked against the non-negotiable list + geometry lessons from `_qa_geometry_review/` (past failures: wrong openings, flipped kitchen, invented cabinetry, false gloss, unsafe clearances, climate-mismatched props). Log to `image_qa.json`.

**G4 PDF verify** — `_verify_pdf_v2.py` exit 0; openability verified; excluded assets absent from XObjects.

**G5 Status coherence** — `PACKAGE_STATUS.md`, `REVIEW.md`, `_agents/STATE.md` all tell the same story.

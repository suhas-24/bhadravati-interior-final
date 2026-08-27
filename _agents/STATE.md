# STATE — live project tracker (update after every meaningful change)

**Last updated:** 2026-08-27 · by: Codex (final visual/PDF QA)

## Project
Bhadravati Home — first-floor studio, Bhadravati, Karnataka. Envelope ~21×18 ft (~378 sq ft, plan_relationship_only).
Concept LOCKED: Warm Contemporary Minimalism — climate-resilient (active replacement: NN9088 Ecru Tint + WW0020 Virgin White + S1241 MT Latte + 83661 SU Sonoma Oak; exterior NN9059 + NN9077).

## Current phase position
Phases 0–18 effectively complete (design control). **Blocked at Phase 2 exit:** signed site measure not yet done ⇒ nothing is fabrication-approved.

## Locked (do not relitigate)
See `../AGENTS.md §2`. Machine locks: `FINAL_DELIVERABLE/coordination/*.json`.

## Open items
| # | Item | Type | Where it blocks |
|---|---|---|---|
| 1 | Signed site-measure sheet (photographed tape measurements) | Client action | ALL fabrication; granite thickness conflict K-01 |
| 2 | Physical laminate/paint sample approval | Client action | Fabrication sign-off |
| 3 | Granite thickness conflict (drawing 1.5″ vs 15 mm note) | Site verify | Any counter/shelf/loft cut |
| 4 | Untracked legacy folders + vendor PDFs (53 dirty git entries) | Housekeeping decision | Repo hygiene; commit or ignore deliberately |
| 5 | Confirm exterior Birla Opus product/tint and approve physical NN9059 + NN9077 samples | Client/dealer input | Exterior paint order and end-to-end exterior QA |

## Budget spec package (2026-08-22)
`BUDGET_SPEC/` now holds a research-priced buy list (6 tracks: paint, wood/joinery, electrical, utilities, envelope, furniture) — 40-source citation ledger, EST totals: Essential ≈₹2.9–3.6L, Recommended ≈₹3.9–4.9L. All prices need local quote replacement before ordering; Phase 0 gate unchanged. Client-facing PDF: `Bhadravati_Budget_Build_Spec.pdf` (repo root), rebuilt via `BUDGET_SPEC/_build_budget_pdf.py`.

## Material system research package (2026-08-25)
`MATERIAL_SYSTEM/` now holds the complete deep-research material system (7 specialist tracks + parent engineering): Tier A/B/C build systems, takeoff + cutting plan (verdict: **11×19mm Sainik 710 practical, 10 optimized**; leaves need **2×18mm**, not 1), decision matrix, carpenter build spec, QC/procurement/maintenance protocols, local supplier shortlist (City Plywood Shivamogga primary), and citation ledger. Gate unchanged: nothing fabrication-approved until site measure closes UNKNOWNs U1–U5 (`90_SITE_MEASURE_ADDENDUM.md`). Price conflict to resolve at quote stage: Sainik 710 19mm ₹106–125 vs ₹145–165/sqft across sources.

## Press & modular sourcing dossier (2026-08-25, REVISED after falsification audit)
`SOURCING_PRESS/` — 13-agent fan-out + 3-agent falsification audit. Nekton entry RETRACTED (Bhatkal/Godrej-showroom conflation); Shanthi downgraded to trader w/ official site shanthisawmill.com; Bhagavati rate UNVERIFIED; price caps replaced by sourced bands (pasting ₹8–14/sqft verified via IndiaMART; banding tape ₹3–15/m vs service ₹18–23/m). Survivors: Sri Gowri Shankar (prelam MDF), Richwood Panel Crafts, Taj (unproven), Sri Laxmi Saw Mills CNC (+91 98453 15930, 3-platform confirmed). Live page `docs/sourcing-press.html` now carries a dated Corrections Log §06. Skill created at user request: **absolute-honest-truth** (provenance labels, identity-trap rule, derived-number rule, corrections protocol) — run before ANY future publish.

## Recent history (context)
- 2026-08-07: Aug-7 visualization packs (legacy folders).
- 2026-08-11: FINAL v1 handover (10 pp) + coordination locks.
- 2026-08-12: V2 package complete/ready (19-pp PDF); Idria Oak 84689 SU double-verified; caption hygiene pass; Pages gallery dual-scheme.
- Latest commits apply "Zakariasson Grok screenshot loop" to locked kitchen/wardrobe 3D.

## Switch colour research (2026-08-26)
`/Users/suhas/Storage/Research/modular-switches-2026/colors/FINDINGS_COLOR.md` — 3-agent deep research against the locked palette. Outcome: matte-only law disqualifies glossy Roma Urban/Coral/Verona; **Legrand Myrius NextGen** confirmed as the only compliant system (converging with BUDGET_SPEC R-Switch winner): Charcoal Grey modules default, Ice Graphite/Charcoal kitchen, Pearl Champagne hero-board accent only, NO wood-print plates near Sonoma Oak, white allowed only on ceiling boards. Physical sheen samples (Ice Silk / Ice Graphite / Charcoal / Pearl Champagne) to be ordered before any bulk purchase. NOT yet a design lock — awaits sample approval like all material decisions.

## Next actions (suggested order)
1. Get site measure scheduled (unblocks everything).
2. Decide fate of untracked clutter: commit provenance-worthy items (site photos ARE register evidence — recommend committing them), gitignore scratch.
3. Corrected Ecru/Virgin White render set is now the default; Puddle/White Linen gallery twins remain clearly marked as legacy alternate.
4. Order Myrius NextGen finish samples (see switch colour note above) alongside laminate/paint samples.
5. Any new work → follow `_agents/PLAYBOOK.md`; update this file after.

## 2026-08-27 colour audit

Added `BIRLA_OPUS_COLOUR_SELECTION.md`. Official rendered swatches were visually checked for NN9088 Ecru Tint, WW0020 Virgin White, NN9059 Kala Ghoda museum, and NN9077 Old leaves underfoot. NN9505 was screened out as too light for black soot/grease contrast on a broad façade. Exterior product/tint and physical façade sample approval remain open.

Published on GitHub Pages after rebuild: gallery includes the exterior concept and `Bhadravati_FINAL_Interior_Design.pdf` now points to the 24-page V2 handoff. Live asset checks returned HTTP 200 for the page, exterior PNG, and PDF.

## 2026-08-27 corrected interior render set

Official Birla Opus swatches were visually inspected and cross-checked: NN9088 Ecru Tint `#E9E3D9` is the selected wall field and WW0020 Virgin White `#EDE9E2` the selected ceiling/trim. NN9074 Puddle of Grey + WW0005 White Linen remain legacy alternate only. A replacement 12-image living/kitchen/evening/bedroom/wardrobe set was generated, visually inspected, and stored in `Bhadravati_Interior_Design_V2/assets/img/corrected_ecru_virgin_white/`; the matching `docs/*_schemeB.png` gallery twins now reference that corrected set. V2 PDF rebuilt and verified at 24 pages.

Exterior replacement: official pages 104–105 were visually rechecked. Final visual concept uses NN9059 Kala Ghoda museum `#BEB2A1` / RGB 190,178,161 on broad walls; NN9077 Old leaves underfoot `#766C62` / RGB 118,108,98 on front bands/plinths and a lorry-facing side only after sample trial; conceptual NN9079 Dark tidings `#4F4A47` / RGB 79,74,71 on the thin roofline edge; roof is muted blue-grey with code UNKNOWN / SAMPLE-ONLY. Final concept image `docs/exterior_colour_concept_nn9059_nn9077_nn9079_blue_roof.png` is now the exterior visual reference. Studio Pose and Idria are historical/rejected only; no colour is fabrication-approved until physical samples are approved.

## 2026-08-27 final webpage + PDF QA

The client gallery now opens on the corrected NN9088 Ecru Tint + WW0020 Virgin White pair, keeps the corrected palette board visible for both URL toggles, uses real middle-dot labels, and has complete tab ARIA state plus section scroll offsets. Active floor-plan and axonometric SVG legends were reconciled to NN9088/WW0020/83661 Sonoma Oak. The three wiki SVG sources were UTF-8 cleaned and their PNGs regenerated; the wardrobe camera/exploded visuals now show 83661 Sonoma Oak rather than Idria.

V2 PDF was rebuilt and verified: 25 pages, unencrypted, no XML parser placeholders, no stale Idria wardrobe camera, no stale NN9074 IEQ wording, and no corrupted `?` glyphs. The deployed copy is `docs/Bhadravati_FINAL_Interior_Design.pdf`. All local HTML references resolve; scheme A and B full-page screenshots were visually inspected. These remain conceptual design-control outputs, not fabrication approval.

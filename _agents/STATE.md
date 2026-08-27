# STATE — live project tracker (update after every meaningful change)

**Last updated:** 2026-08-27 · by: Codex (industrial-premium colour audit)

## Project
Bhadravati Home — first-floor studio, Bhadravati, Karnataka. Envelope ~21×18 ft (~378 sq ft, plan_relationship_only).
Concept LOCKED: Warm Contemporary Minimalism — climate-resilient (Scheme A final: NN9074 + S1241 MT Latte + 84689 SU Idria Oak).

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
| 5 | Confirm exterior Birla Opus product/tint and approve physical NN9589 sample | Client/dealer input | Exterior paint order and end-to-end exterior QA |

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
`/Users/suhas/Storage/Research/modular-switches-2026/colors/FINDINGS_COLOR.md` — 3-agent deep research against the locked palette. Outcome: matte-only law disqualifies glossy Roma Urban/Coral/Verona; **Legrand Myrius NextGen** confirmed as the only compliant system (converging with BUDGET_SPEC R-Switch winner): Charcoal Grey modules default, Ice Graphite/Charcoal kitchen, Pearl Champagne hero-board accent only, NO wood-print plates near Idria Oak, white allowed only on ceiling boards. Physical sheen samples (Ice Silk / Ice Graphite / Charcoal / Pearl Champagne) to be ordered before any bulk purchase. NOT yet a design lock — awaits sample approval like all material decisions.

## Next actions (suggested order)
1. Get site measure scheduled (unblocks everything).
2. Decide fate of untracked clutter: commit provenance-worthy items (site photos ARE register evidence — recommend committing them), gitignore scratch.
3. When client picks paint scheme finally: retire the other scheme's gallery twins or mark clearly.
4. Order Myrius NextGen finish samples (see switch colour note above) alongside laminate/paint samples.
5. Any new work → follow `_agents/PLAYBOOK.md`; update this file after.

## 2026-08-27 colour audit

Added `BIRLA_OPUS_COLOUR_SELECTION.md`. Official rendered swatches were visually checked for NN9074 Puddle of Grey, NN9242 A Khadi Kurta, WW0005 White Linen, NN9564 Parisian Evenings, and NN9589 Studio Pose. Existing exterior concept boards were reviewed; NN9589 is the recommended exterior direction. Exterior product/tint and physical façade sample approval remain open.

Published on GitHub Pages after rebuild: gallery includes the exterior concept and `Bhadravati_FINAL_Interior_Design.pdf` now points to the 24-page V2 handoff. Live asset checks returned HTTP 200 for the page, exterior PNG, and PDF.

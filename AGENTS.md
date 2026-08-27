# AGENTS.md — Operating Manual for AI Agents

**Repo:** Bhadravati Home interior — design-control production repo (first-floor studio, ~21 ft × 18 ft, Bhadravati, Karnataka).
**Locked concept:** Warm Contemporary Minimalism — climate-resilient.
**Live site:** https://suhas-24.github.io/bhadravati-interior-final/ (auto-deploys from `docs/` on push to `main`).

This file tells any agent (Hermes, Claude Code, Codex, Cursor…) how to work here like a professional interior design studio without breaking the pipeline.

---

## 0. Prime rules — read before ANY action

1. **Authority hierarchy is law** (defined in `Bhadravati_Interior_Design_V2/SOURCE_OF_TRUTH.md`):
   signed site measure → `interior_dimension_control/dimension_register_v1` → V2 brief + `Bhadravati_Interior_Design_V2/source/design_tokens_v2.json` → prior PDFs/renders (**context only, never cut from them**).
2. **Never invent dimensions, SKUs, or prices.** Material codes must be catalogue-confirmed (evidence PNGs live in `Bhadravati_Interior_Design_V2/source/`). Flag gaps as `UNKNOWN` / `SAMPLE-ONLY`.
3. **Nothing here is fabrication-approved.** No output is a cut list until a signed site-measure sheet + physical sample approval exist.
4. **Do not move or rename** tracked dirs (`FINAL_DELIVERABLE/`, `Bhadravati_Interior_Design_V2/`, `docs/`, `.github/`) or legacy folders — governance docs cite them by name as provenance/audit trail.
5. **`docs/` deploys to GitHub Pages on every push to main.** Check the gallery builds before pushing.
6. **Stale paths:** older docs cite `/Users/suhas/Downloads/Interiors/…`; the repo now lives at `/Users/suhas/Storage/Personal/Interiors/`. Always use repo-relative paths.
7. **Vendor PDFs are huge (15–54 MB).** Read pre-extracted text in `processed_pdf_text/` and page images in `processed_pdf_images/` instead of opening the PDFs.

---

## 1. Repo map — where things live

| Path | What it is | Agent guidance |
|---|---|---|
| `Bhadravati_Interior_Design_V2/` | **Current governing package (V2)** — master brief, source of truth, design tokens, presentation boards 01–05, client PDF (19 pp), phase framework, QA checklist | **Start here** for any design question |
| `FINAL_DELIVERABLE/` | V1 handover (superseded for decisions) + machine locks in `coordination/*.json` (swatch, scheme B, dimension, wardrobe-door) + `design_tokens.json` | Locks still encode active constraints |
| `docs/` | Published GitHub Pages gallery — Scheme A + Scheme B render twins | Client-facing; CI-deployed; don't hand-edit renders here |
| `interior_dimension_control/` | K-01 (kitchen) / W-01 (wardrobe) dimension register + OCR pass script | **Only** dimension source until signed measure |
| `materials/` + root vendor PDFs | Century StarLine, Birla Opus, Advance, E3 EBT catalogs | Source catalogs; use extracted text for lookup |
| `processed_pdf_text/`, `processed_pdf_images/` | Pre-extracted catalog text + page JPGs (birla/, century/, e3/) | SKU/shade verification workspace |
| `research/` | Research essays ("The Resilient Indian Home…") | Reference material |
| `_qa_geometry_review/` | Page-by-page QA of earlier client PDFs (geometry errors caught) | **Read before re-rendering** — don't repeat fixed mistakes |
| `Bhadravati_Client_Visualization/`, `Bhadravati_Corrected_Renders/`, `Bhadravati_Corrected_Visualization/`, `Bhadravati_Professional_Interior_Design/`, `Bhadravati_Visual_Concept_Render/`, `Bhadravati_Final_Interior_Design_Brief/` | Aug-7 iteration history (legacy) | Provenance only — superseded |
| `interior_dimension_control/site_photos/` | Site photos — K-01 dimension evidence | Referenced by the dimension register |
| `Bhadravati_Interior_Design_V2/source/swatches/` | Physical swatch scans (80171, 83386, 83736, 844485, NN-9088) | Swatch reference for pixel QA |

---

## 2. Locked decisions — do not relitigate without client sign-off

- **Kitchen:** existing black granite retained; scope = **shutters only**. Base/drawers/loft in Century **S1241 MT Latte** only.
- **Hardware:** brushed stainless **recessed** pulls (J-pull/finger-pull). No projecting bar handles.
- **Wardrobe:** **3 doors** (single L + double R), leaf widths 457/457/458 mm inside 1372 mm clear. (Four-leaf option superseded — see `assets/04b_…_superseded.png`.)
- **Lighting:** 3000 K warm-neutral baseline. **Finishes:** matte / low-sheen.
- **Banned:** TV feature wall, island, L-kitchen flip, gold strips, slatted Japandi props, gloss/sparkle laminates.
- **Palette:** Corrected final = **NN9088 Ecru Tint + WW0020 Virgin White + S1241 MT Latte + 83661 SU Sonoma Oak**. NN9074 + WW0005 and 84689 SU Idria remain historical/legacy alternates only.
- **SKU verified:** **83661 SU Sonoma Oak** is the active wardrobe face; 84689 SU Idria Oak was catalogue-verified historically but is rejected for the current brief (see `IDRIA_REVALIDATION.md`).

---

## 3. Agent kit

| File | Purpose |
|---|---|
| `_agents/PLAYBOOK.md` | Step-by-step workflows: SKU verify, dimension change, new renders, PDF rebuild, publish, handover — each with its QA gate |
| `_agents/ROLE_PROMPTS.md` | Ready-to-use expert role prompts (space planner, materials lead, lighting designer, QA reviewer…) mapped to the project's phase framework |
| `_agents/STATE.md` | Live project state: what's locked, what's open, next actions — **update it after every meaningful change** |
| `_agents/work/` | Scratch space for agents (gitignored — safe for temp files) |

**Quick start by request type:**
- *"Is SKU X real?"* → PLAYBOOK W1 (catalogue verification)
- *"Change a dimension/finish"* → PLAYBOOK W2 → W4 (update sources → rebuild → QA)
- *"New render of Y"* → PLAYBOOK W3 (prompt conventions + image QA gates)
- *"Send the client the latest"* → PLAYBOOK W4 → W6 (verify → handover)
- *"What's the status?"* → `_agents/STATE.md` + `Bhadravati_Interior_Design_V2/PACKAGE_STATUS.md`

---

## 4. Change protocol (every design change)

1. Read `_agents/STATE.md` + relevant lock JSONs (`FINAL_DELIVERABLE/coordination/`).
2. Update the **source** (SoT / tokens / register) — never just the render.
3. Regenerate affected board/PDF (`Bhadravati_Interior_Design_V2/_build_pdf_v2.py`, verify with `_verify_pdf_v2.py`).
4. Pass the QA gates (PLAYBOOK §Gates): dimension reconciliation, swatch pixel QA, image QA, PDF verify.
5. Update `_agents/STATE.md` and `PACKAGE_STATUS.md`.
6. Commit with a descriptive message (repo convention: imperative, specific — see `git log`).

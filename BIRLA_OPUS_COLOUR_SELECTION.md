# Birla Opus colour selection — industrial-belt premium interior

**Status:** design-control record · exterior concept selected; final exterior product confirmation still required  
**Site:** Bhadravati, Karnataka · first-floor studio · approximately 21 ft × 18 ft (relationship-only until signed measure)

## Design intent

Warm Contemporary Minimalism with a richer, more composed presence in a dusty and smoke-affected industrial setting. The room should feel premium through proportion, matte depth, warm light, controlled contrast, and material quality—not through gloss, bright white, or decorative clutter.

## Verified colour system

| Role | Birla Opus shade | Digital representation | Use |
|---|---|---|---|
| Main interior walls | **NN9074 — Puddle of Grey** | `#B5AB9C` / RGB 181,171,156 | Living, kitchen, bedroom and study walls; mid-tone warm greige is more forgiving of soot than a stark light wall. |
| Dim-zone refinement | **NN9242 — A Khadi Kurta** | `#C7BAB0` / RGB 199,186,176 | Optional bath corridor / wardrobe surround where extra reflected light helps; not a new broad-wall default. |
| Ceilings | **WW0005 — White Linen** | `#EEEDE9` / RGB 238,237,233 | All ceilings; warm white keeps the premium palette soft under 3000 K. |
| Small accent (optional) | **GG7140 — Tender Buds** | `#9CAE91` / RGB 156,174,145 | At most one small wall; only after physical sample approval. |

The hex/RGB values above are the shade-card digital representations used by the existing project tokens. They are not a claim of monitor-independent paint accuracy; the shade code and physical sample remain the authority.

## Visual verification evidence

The actual rendered Birla Opus shade-card swatches were inspected, with code/name spatial association confirmed:

- `processed_pdf_images/birla/page_105.png` — NN9074 Puddle of Grey on the official “Neutrals: Browns & Greys” card.
- `processed_pdf_images/birla/page_114.png` — NN9242 A Khadi Kurta on the official “Neutrals: Browns & Greys (continued)” card.
- `processed_pdf_images/birla/page_002.png` — WW0005 White Linen on the official Whites card.

The existing swatch-pixel QA crops are retained under `Bhadravati_Interior_Design_V2/source/swatch_pixel_qa/`.

## Industrial-area application rules

1. Specify a Birla Opus washable, low-sheen/matt system; premium-value target is Calista Ever Wash (final product SKU and local price remain dealer verification items).
2. Use white-cement putty, tinted primer, and a stain-blocking spot primer on old soot marks before topcoat.
3. Keep the kitchen splash zone tiled; do not rely on painted plaster behind the hob.
4. Use closed storage, sealed window/door gaps, washable low-pile textiles, and a purifier/exhaust strategy to reduce deposition at source.
5. Clean with microfiber dusting monthly, gentle damp wiping quarterly at touch zones, and mild-soap washing twice yearly; no abrasive pads or bleach.
6. Preserve the locked material language: Century S1241 MT Latte kitchen shutters, 84689 SU Idria Oak wardrobe, retained black granite, recessed brushed-stainless pulls, and 3000 K lighting.

## Exterior concept — premium, smoke- and dust-aware

Two exterior concept boards are present in `interior_dimension_control/site_photos/` (27-Aug-2026):

- **NN9564 — Parisian Evenings** (`#9D9CA1`, RGB 157,156,161): visually verified on official shade-card page 132; cooler/lavender grey, acceptable but less connected to the warm interior materials.
- **NN9589 — Studio Pose** (`#80837D`, RGB 128,131,125): visually verified on official shade-card page 133; muted green-grey that coordinates with 84689 SU Idria Oak and matte black metal while remaining forgiving of soot streaks.

**Recommended exterior concept:** NN9589 Studio Pose as the broad wall field, with a restrained darker graphite/black band only where already expressed by the building (parapet/bands/grills/canopy), and a warm teak-toned door. Preserve the existing geometry, openings, drainage, canopy, grills, and signage. Do not add a decorative façade feature wall.

The boards are visual concepts, not proof of an exterior-product tint. Before painting, obtain the exact exterior Birla Opus product family available from the local dealer and test physical samples against the actual façade in sun, shade, and post-rain conditions. The shade code remains the identity; the interior shade-card RGB is a digital approximation, not an exterior paint certificate.

## Approval gate

This is a design-control recommendation, not fabrication or paint-order approval. Approve physical samples beside the retained granite, S1241 Latte, and 84689 Idria Oak under morning light, afternoon light, and 3000 K before bulk purchase.

## Validation record

- Static gallery reference check: PASS (HTML and image asset resolve).
- Local HTTP smoke test: PASS (`docs/index.html` and the exterior PNG returned successfully).
- Direct visual inspection: PASS for the exterior board and official shade-card renders.
- Automated browser screenshot: **NOT RUN** because the local Playwright runtime has no installed Chrome distribution; no claim of browser-render QA is made.

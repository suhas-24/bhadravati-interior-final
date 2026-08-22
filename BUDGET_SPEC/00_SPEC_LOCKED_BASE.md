# 00 — Spec Base: Environment Constraints & Locked Decisions

**Package:** Bhadravati Budget Build Spec (agent-researched buy list)
**Date:** 2026-08-22 · **Status:** DRAFT v0.1 — research tracks merging
**Relationship:** extends `Bhadravati_Interior_Design_V2/` governance. Changes NO locked decision. Fills the "street prices + exact SKUs" gap left open in `FINAL_DELIVERABLE/06_Budget_Phasing.md` ("₹ bands to be filled after local quotes").

---

## 1. Site environment (design drivers)

| Constraint | Source | Design response |
|---|---|---|
| Fine dust + soot deposition (industrial belt) | Client brief + SoT problems-solved | Mid-tone washable walls (no stark white); closed storage; sealed windows; low-pile textiles; purifier |
| Smoke smell / oily deposits | Client brief | Washable emulsion class ≥5000 scrubs; degrease-clean cadence; exhaust strategy review |
| Noise day/night | Client brief | Window seals + curtains + soft furnishings; realistic dB expectations documented |
| Vibrations (factories/trucks) | Client brief | Anti-vibration pads under appliances; rigid wardrobe fixing; no floating shelves over bed |
| Monsoon humidity ~85% | Climate knowledge | BWP/710 boards at wet risk, E1/E0 emission boards, matte finishes (hides water haze), ventilation |
| Hard water | SoT maintenance notes | Wipe-dry granite discipline; geyser tank chemistry choice; matte shutters not gloss |

## 2. Locked decisions carried forward (from V2 locks)

| Slot | Lock | Value |
|---|---|---|
| Walls | Birla Opus **NN9074 Puddle of Grey** | #B5AB9C warm greige, low-sheen washable |
| Ceiling | **WW0005 White Linen** | #EEEDE9 |
| Accent (optional, ≤1 wall) | **GG7140 Tender Buds** | #9CAE91 sage |
| Kitchen shutters | Century StarLine **S1241 MT Latte** | existing black granite retained; shutters only |
| Wardrobe shutters | Century **84689 SU Idria Oak** | 3 doors, leaf 457/457/458 mm in 1372 mm clear × 2286 H × ~488 D |
| TV cabinet accent | Century **80236 DW Slate Grey** | controlled low accent only |
| Hardware | brushed stainless recessed pulls | SS304 screws at wet risk |
| Lighting | 3000 K baseline, CRI≥90 where colour matters | matte diffusers |
| Banned | gloss/sparkle, gold strips, TV feature wall, island, L-flip, slat props | — |

All codes verified against `processed_pdf_text/birla_opus_shade_card_extracted.txt` (2,322-shade card, compiled 03-Aug-2026) and `processed_pdf_text/century_starline_extracted.txt`.

## 3. Brightness ladder for darker rooms (card-evidenced)

The client's own shade card recommends for **industrial areas**: ceilings WW0005/WW0020, walls NN9088/WW0120/NN9242. Measured brightness (L*≈ from RGB):

| Code | Name | Hex | L* approx | Use rule |
|---|---|---|---|---|
| NN9074 | Puddle of Grey | #B5AB9C | ~71 | LOCKED default — best soot-hiding mid-tone |
| NN9242 | A Khadi Kurta | #C7BAB0 | ~77 | **Factory-recommended industrial wall shade** — use instead of NN9074 in dim rooms (bath corridor, wardrobe surround) |
| NN9088 | Ecru Tint | #E9E3D9 | ~89 | Secondary/light option — stricter wipe schedule (shows dust faster) |
| WW0020 | Virgin White | #EDE9E2 | ~92 | Ceiling alternative to WW0005 |

Rule: physical samples approved under morning sun, afternoon sun, 3000 K evening before ordering (per `03_Palette_Materials.md` metamerism warning).

## 4. Paint system product ladder (from card system notes — pricing/chemistry under research)

| Tier | Product | Claimed class |
|---|---|---|
| Luxury | Birla Opus **One Pure Elegance Matt** | scuff & stain resistant, 7-yr warranty class |
| Premium | Birla Opus **Calista Ever Wash** | 5000+ washes, anti-fungal |
| Economy | Birla Opus **Style Color Smart** | anti-fungal, washable |
| Prep | One Pro Putty+Primer / Calista Pro White Primer | — |

Cross-brand comparison (Asian Paints Royale/Apex, Berger, JSW, Dulux) incoming from research track R-Paint.

## Research tracks in flight

| Track | Scope | Report file | State |
|---|---|---|---|
| R-Paint | Emulsions by series, VOC, scrub cycles, shades, human validation | `07_paint.md` | ✅ COMPLETE |
| R-Wood | Plywood/HDHMR grades, IS standards, formaldehyde classes, hardware, carcass spec | `02_wood_joinery.md` | ✅ COMPLETE |
| R-Light | LED fixtures/datasheets, wiring, MCB/RCCB/SPD surge plan, lux schedule | `03_electrical.md` | ✅ COMPLETE |
| R-Switch | Switchgear series/materials, BLDC fans, exhaust, geyser | `04_utilities.md` | ✅ COMPLETE |
| R-Envelope | Dust/noise/vibration defense, flooring, air purification | `05_envelope.md` | ✅ COMPLETE |
| R-Furniture | Sofa/mattress/bed/study/bedding by construction + real-user validation | `01_furniture.md` | ✅ COMPLETE |

Consolidated priced buy list: **`06_MASTER_BUY_LIST.md`** — Essential ≈₹2.9–3.6L · Recommended ≈₹3.9–4.9L · Premium ₹5.5L+.
Shared citation ledger: 40 sources (`~/.hermes/cache/citations/ledger.json`), Sources block rendered into 06.

# Engineered boards: Boilo, HDHMR, BWP, BWR, marine

**Role:** Engineered-board expert note (not a plywood-default sales sheet).  
**Date:** 2026-08-12  
**Status:** Research for specification. **Not a bid. Not a BIS certificate. Not a lab report.**  
**Job filter:** Bhadravati, Karnataka — monsoon humidity, termites, kitchen shutters + ~90 in wardrobe leaves.  
**Rule:** Manufacturer density, “BWP”, “FR”, and 15–25 year warranties are **claims** until the sheet stamp, mill test, and edge-seal process are in the job file.

---

## 0. Verdict in one page

| If you remember one thing | Why |
|---|---|
| **HDHMR is a trade name, not a BIS product class.** | BIS licences fibreboard as **IS 12406** MDF Grade 1 / Grade 2. “HDHMR / HDWR / HDFWR / Boilo” are mill brands sitting on or **beside** that standard. |
| **Boilo is HDF, not plywood.** Density **>1000 kg/m³** (mill). That is **outside** IS 12406’s 600–900 kg/m³ scope. | You cannot “ISI-mark Boilo as IS 12406 MDF” by density. You also cannot mark it as IS 710 marine ply. It is a **proprietary BWP-FR HDF**. |
| **“BWP plywood” ? marine plywood.** | Since **IS 303:2024**, general-purpose ply has grades **MR / BWR / BWP**. **IS 710:2024** is still **marine plywood** (wet bending, preservative retention, IS 848 BWP adhesive, craft/prolonged-moisture construction). |
| **IS 5509 is a fire-retardant *plywood* specification.** | Action Tesa says Boilo “confirming to IS:5509”. That is a **test-method borrow / manufacturer claim**, not a BIS licence that the sheet is fire-retardant plywood. Demand the **NABL/BIS test report** for *that SKU*. |
| **Open edges kill fibreboard.** | Faces are pressed and often waxed. **Cut edges are the sponge.** PVC/ABS with **PUR** (or proven hot-melt) on every cut, including hinge-cup walls and sink-base bottoms. PVA carpenter glue is not a seal. |
| **Independent 3–7 year Boilo diaries are scarce.** | Public English forums do not contain a named-SKU, Karnataka, year-5 kitchen sample. Density and FR are **not** a substitute for field life. |
| **Do not hang 90 in doors on Boilo by default.** | ~18–22 kg per 18 mm leaf vs ~13–16 kg for ply / HDHMR. Five cups still see a **sag tax**. Use Boilo on **kitchen shutters / wet boxes** in a **CNC** shop; use HDHMR or calibrated ply on tall leaves. |

**Default for this house (aligned with `BOARD_DECISION.md`):** kitchen shutters = **IS 710-stamped ply** *or* **Boilo 18 mm if CNC**; wardrobe 90 in = **calibrated BWP/710 ply** *or* **HDHMR/HDWR 18 mm CNC** — **not Boilo**.

---

## 1. First principles: what these boards actually are

### 1.1 How they are made (this decides failure mode)

| Family | Construction | Glue / process (typical India) | How it fails |
|---|---|---|---|
| **Plywood** | Cross-banded **veneers**. Strength is anisotropic (strong along face grain). | UF (MR), MUF/PF (BWR), **phenolic BWP-type IS 848** (BWP / marine). | **Delamination** at glue line; **core gaps / overlaps** at hinge cups; face telegraph under 0.8 mm laminate; edge wicking along veneer end-grain. |
| **Particle board (PB)** | Chips + resin, often three-layer. | Mostly UF. | **Disintegrates** when wet. Screw-holding collapses. Reject for wet or hinge-heavy work. |
| **MDF** | Defibrated **wood fibre** + resin, dry-process, hot-pressed. Homogeneous. | UF (interior Grade 2); **MUF + wax** (Grade 1 / “exterior” / HMR). | **Thickness swell** from cut edges; hinge-cup **crush** if density is low; formaldehyde if E2. |
| **HDF** | Same process as MDF, **higher compaction**. European shorthand: density **? ~800 kg/m³**. | Same resin families; more fibre per m³. | Same swell physics as MDF, slower if denser and better sealed. **Heavier.** |
| **HDHMR / HDWR / HDFWR** | Indian **marketing names** for high-density, moisture-resistant fibreboard. | Almost always **MUF + paraffin wax**, sold against **IS 12406 Grade 1**. | Not “waterproof”. **Edge swell** (“elephant edges”) in kitchens if banding fails. |
| **Boilo (Action Tesa)** | **BWP FR HDF** — mill says density **>1000 kg/m³**, surface **1180 kg/m³**, grey FR matrix. | Proprietary high-temp/high-pressure; FR additives in the mat (not a surface paint). | Still fibre. Still needs **edge seal**. Weight. Unproven 5–7 yr public diary. Category-error on IS 5509 / “BWP plywood” language. |

**Physics that does not care about the brand:**

1. **Water enters at the cut.** A pressed face is a crust. A sawn edge is open capillaries. Laminate on two faces with raw edges is a **moisture sandwich**.
2. **Swell is thickness-direction first.** Fibreboards swell more in thickness than in plane. Hinge cups ovalise; doors bind; ABS lifts.
3. **Density is not waterproofing.** Density raises hardness, screw withdrawal, and **weight**. Moisture resistance is **resin + wax + edge seal**. A dense UF board still fails in a sink leak.
4. **Plywood’s advantage is repair and anisotropy.** You can plane an edge, sister a rail, and the cross-band fights cupping. Its disadvantage is **voids** that a 35 mm cup will find.
5. **Fibreboard’s advantage is homogeneity and CNC.** No core gap at the cup. Routed profiles, membrane doors, 0.8 mm laminate without telegraph. Its disadvantage is **catastrophic edge swell** and **mass**.

### 1.2 Density bands (use as order-of-magnitude, then **weigh the sheet**)

| Material | Typical bulk density | 8×4 × **18 mm** sheet mass (calc.) | 8×4 × **19 mm** |
|---|---|---|---|
| Interior MDF (Grade 2) | ~650–750 kg/m³ | ~35–40 kg | ~37–42 kg |
| Greenpanel **HDWR** 12–19 mm (catalogue) | **825** kg/m³ | **~44 kg** | — |
| Action Tesa / VIR / Century **HDHMR** (claimed) | **>850** (often 850–900) | **~45–48 kg** | — |
| Good hardwood **ply** | ~550–750 (Club Prime SG **>0.69** ? 39 kg at 19 mm) | ~33–40 kg | **~37–42 kg** |
| **Boilo** (claimed bulk **>1000**; surface **1180**) | 1000–1100+ | **~54–59 kg** | — |

Volume of 8×4×18 mm ? **0.0535 m³**. Mass = density × volume. **Mic thickness and weigh one sheet at the yard.** Marketing “18 mm” is often 16.75–18.0 mm.

**90 in wardrobe leaf** (assume 2286 × 457 × 18 mm ? 0.0188 m³), **board only**, no laminate/hardware:

| Core | Leaf mass (approx.) |
|---|---|
| Ply ~700 kg/m³ | **~13 kg** |
| HDHMR ~850 | **~16 kg** |
| Boilo ~1050 | **~20 kg** |
| Boilo if bulk were 1180 | **~22 kg** |

Five Hettich Sensys cups on a 90 in leaf are designed for kitchen/wardrobe doors, not for treating mass as free. Extra **5–9 kg** vs ply is a **real sag and cup-wall fatigue** tax. That is why Boilo is a **kitchen-shutter / wet-box** board in a CNC shop, not a default tall-door board.

### 1.3 Thickness swell (what the tests actually do)

| Test | What it is | What it is **not** |
|---|---|---|
| **IS 848 BWP adhesive** (ply glue) | **Six** cycles: 8 h boil + 16 h dry at 65 °C. Knife test: wood failure ?50% to pass. | Proof that the **veneer** will not rot, or that **edges** are sealed. |
| **IS 848 BWR** | **Three** of those boil cycles. Standard text: joints survive weather “only a few years”; boiling water “for a limited period”. | “Kitchen-proof forever.” |
| **IS 848 MR** | **Three** cycles of **3 h at 60 °C** (not boiling) + dry. | Anything near a sink. |
| **IS 12406 accelerated water resistance** | Specimen brought to **boil for 2 hours**, cooled, then **internal bond** measured. Grade 1 must retain a **minimum IB** (low: e.g. 0.12 N/mm² class at 12–19 mm in mill tables). | Six-cycle plywood BWP. The board is allowed to **weaken**; it must not **fall apart**. |
| **IS 12406 24 h soak swell** | Thickness swell **max** (Grade 1, 12–19 mm): **8%** in Greenpanel’s published table. | A sealed cabinet. Unsealed edges in a monsoon kitchen will exceed lab coupons. |
| **Boilo “BWP HDF”** | Mill claim: bonding “unaffected even in boiling water”; lower absorption/swell than BWP ply. | An independent, published, third-party **coupon + 5-year install** dataset. |

**Honest translation:** Grade 1 MDF / HDHMR is **moisture-resistant furniture board**. Boilo is **sold as boiling-waterproof HDF**. Neither is a boat hull. **Marine ply (IS 710)** is the only Indian panel standard written for **prolonged moisture + preservative + wet bending**.

### 1.4 Hinge cups (35 mm)

| Substrate | Cup behaviour |
|---|---|
| **Gappy / alternate-core ply** | Cup lands on a void ? **tear-out** in 1–3 years of daily cycles. This is the Sainik/Ecotec field complaint, not a law of all ply. **Composed-core / calibrated marine** is the ply answer. |
| **Interior MDF (~700)** | Homogeneous but **soft**. Cup wall crushes; screws in the 35 mm cup **strip** if over-torqued. |
| **HDHMR / HDWR (~825–900)** | Best **CNC** cup: dense, no void. Needs **correct cup drill**, not a spade bit. Edge distance and **five cups on 90 in**. |
| **Boilo (>1000)** | Excellent cup **if** the shop has HDF tooling. Harder to drill; bits burn. Weight still loads the **hinge arm and carcass**. |

**Screws:** parallel-shank confirmat / dedicated HDF screws beat tapered wood screws in fibreboard. Pilot holes. Do not chase a stripped cup with a longer wood screw — **relocate or use a cup repair sleeve**.

### 1.5 CNC shop vs site carpenter

| | **CNC / factory edge** | **Site carpenter** |
|---|---|---|
| **Boilo / HDHMR** | Native habitat: nested cutting, **ABS/PVC PUR** banding, calibrated thickness, dust extraction, carbide. | High risk: handsaw fuzz, PVA banding, unsealed sink bottoms, hinge cups drilled by eye. |
| **Calibrated ply** | Also excellent. | **Native habitat.** Plane, lipping, repair. 0.8 mm laminate still wants a **calibrated** sheet. |
| **Rule for Bhadravati** | If the fabricator has **never** edged HDF, **do not experiment on the kitchen**. Write ply. | If they **are** a modular factory, HDHMR/Boilo is often **better** than economy ply. |

---

## 2. Standards dictionary (read the stamp, not the brochure)

### 2.1 IS 848:2006 — adhesives for plywood (the real BWP/BWR/MR)

Source: [IS 848 (2006) PDF](https://law.resource.org/pub/in/bis/S03/is.848.2006.pdf)

| Grade | Cycle | Pass idea (knife / wood failure) | Standard’s own honesty |
|---|---|---|---|
| **BWP** Boiling Water **Proof** | **6 ×** (8 h boil + 16 h @ 65 °C) | ?50% wood failure; 75% = excellent | Joints “highly resistant to weather, cold and boiling water, steam and dry heat” |
| **BWR** Boiling Water **Resistant** | **3 ×** same boil cycle | Same knife criteria | Survive weather “**only a few years**”; boiling water “**limited period**” |
| **MR** Moisture **Resistant** | **3 ×** (3 h @ **60 °C** water + 8 h dry) | Same | Cold water long; hot water limited; **fails in boiling water** |

**Hidden truth:** BWP/BWR/MR on a ply sheet is a **glue-line test**, not a species test, not a void test, not an edge-seal test.

### 2.2 IS 303:2024 — plywood for **general purposes**

- BIS product manual: [PM/IS 303 July 2024](https://www.bis.gov.in/wp-content/uploads/2024/07/PM-IS-303-_July-24.pdf)
- Compendium: [BIS plywood compendium](https://services.bis.gov.in/tmp/compendium_2025-06-02-04-13-12.pdf)
- Licence scope grades: **MR / BWR / BWP**. Appearance **AA / AB / BB**. Formaldehyde **E1 / E2**. Thicknesses listed include **15 / 19 mm** (yards still sell 16 / 18).

**2024 change that salespeople still get wrong:** BWP is now a **legal grade of interior/general-purpose plywood**. It is **not** automatically marine. Century’s own Sainik 710 footnote matches this: “Asli” BWP = **IS 303 BWP**.

Industry context: [Ply Reporter on BWP under IS 303](https://www.plyreporter.com/article/153905/the-new-bis-era-bwp-grade-comes-under-is-303).

### 2.3 IS 710:2024 — **marine plywood**

- Product manual: [PM/IS 710 July 2024](https://www.bis.gov.in/wp-content/uploads/2024/07/PM-IS-710-_July-24.pdf)
- Title: plywood for **marine and river craft, pontoons and the like**.
- Adhesive: **BWP type of IS 848** (manual, raw-material note).
- Extra vs IS 303 BWP (from 2010 text still widely used + 2024 manual tests): **wet bending**, **tensile**, **static bending**, **mycological**, **retention of preservative**. 2010 text: no glue **extenders**; fillers ?10% of solid content; pressure-impregnated preservative (e.g. CCA/CCB retention class). [IS 710:2010](https://law.resource.org/pub/in/bis/S03/is.710.2010.pdf)

**Kitchen implication:** a sheet that says **“710” in the brand name** (Sainik 710, Ecotec 710) can be **IS 303 BWP**. A sheet that is **marine** must show **IS 710** on the **ISI edge stamp** + CML. Photograph it.

### 2.4 IS 12406 — MDF (2003 and 2021)

- 2003 public copy: [IS 12406:2003](https://cracindia.in/admin/uploads/IS-12406.pdf)
- 2021 is the current certification target (mandatory QCO for general-purpose MDF). Scope cited by certifiers: density **600–900 kg/m³**. [Aleph / BIS IS 12406:2021](https://alephindia.in/isi-product/medium-density-fibre-boards-for-general-purpose.php)
- **Grade 1** vs **Grade 2:** Grade 1 is the moisture-resistant / higher-property class (Hazard Class 2 humidity in explainer literature). Grade 2 is interior-dry. [Global Omega summary](https://globalomega.com/blog/bis-certification-of-as-per-is-124062021/)
- Tests: density, moisture, MOR/MOE, IB, IB after **cyclic** *or* **2-hour boil AWR**, screw withdrawal, 24 h swell.

**HDHMR that is honest** will show **IS 12406 Grade 1** on the stamp — not “IS 710”.

**Boilo at >1000 kg/m³ is outside 600–900.** Treat it as a **proprietary HDF**, and ask which **standard and report** they actually hold (internal boil test, EN 622-5, flammability), not a fake 12406 mark.

### 2.5 IS 5509 — fire-retardant **plywood**

- Current: **IS 5509:2021**, third revision. [Archive listing](https://archive.org/details/gov.in.is.5509.2021)
- BIS compendium: FR chemicals on **plywood made to IS 303**; tests = **flammability, flame penetration, rate of burning**.

Action Tesa: Boilo “Fire retardant property confirming to IS:5509 Standard” — [Boilo product page](https://www.actiontesa.com/products/plain-boilo-bwp-hdf-boards/). They also claim ~101 min vs ~30 min flame appearance vs FR ply — [Tesa BWP/BWR/FR explainer](https://www.actiontesa.com/bwp-bwr-fire-retardant-making-sense-of-board-grades-in-india/).

**Expert read:** running IS 5509 **methods** on HDF coupons can be real. **Marking the board as IS 5509 plywood is a category error.** For a hospital/hotel spec, ask: *licence number, product name on the licence, and the test report.* Residential kitchens: FR is a **bonus**, not a reason to skip edge seal.

### 2.6 Other numbers that get thrown around

| Number | Actual title | Misuse |
|---|---|---|
| **IS 10701** | Structural plywood | Sold as “kitchen marine” |
| **IS 3087 / IS 12823** | Particle board / prelam PB | Cheap modular carcass |
| **IS 14587** | Prelaminated MDF (often cited with Century HDF) | Not a water grade by itself |
| **EN 622-5** | European dry-process MDF | Greenpanel cites it next to HDWR |
| **IS 5539 / IS 12120** | Preservative treatment of ply / panels | “Termite-proof” sticker without retention test |

---

## 3. Product dossiers (mill vs trade)

### 3.1 Action Tesa **Boilo** (BWP FR HDF)

**Official:** [Plain Boilo BWP HDF](https://www.actiontesa.com/products/plain-boilo-bwp-hdf-boards/) · [Applications](https://www.actiontesa.com/applications-for-action-tesas-boilo-boiling-water-proof-fr-hdf-board/) · [Brochure landing](https://www.actiontesa.com/brochure/boilo/) · [“Far better than BWP ply”](https://www.actiontesa.com/action-tesas-boilo-a-far-better-replacement-to-bwp-plywoods-fr-grade-plyboards/)

| Claim (mill) | Expert note |
|---|---|
| Density **>1000 kg/m³**; surface **1180 kg/m³** | Surface ? bulk. Weigh the sheet. Dent resistance is real; **mass is real**. |
| **BWP** + FR + borer + termite | BWP here is **HDF bonding**, not IS 710. Termite: **IPIRTI 1-year** certificate on the product page — not a 21-year biology test. |
| Homogeneous, **zero core gaps** | True vs veneer ply. This is the **hinge-cup** argument. |
| 8×6 available in 12 mm | Waste reduction for nested CNC. Confirm 18 mm sizes locally (8×4 is the yard default). |
| Grey colour | FR / high-density tell. Do not confuse with cheap green MDF dye. |
| “6× structural ply IS 10701 rigidity” | Marketing comparison. Do not spec Boilo as **structural plywood**. |
| Variants: **Plain** and **Prelam** | Prelam still needs **edge** banding. |

**Warranty in the wild:** dealers advertise **21 years** ([My Interio listing](https://www.myinterio.store/action-tesa-boilo-8mm-to-18mm-with-21-years-warranty-8x4-sheet-boilo-bwp-hdf-actionboilo)). Treat duration as **sales**; read **exclusions** (water, edges, installation). Modular-kitchen warranties routinely **exclude moisture swell** — [Kitchen Kaki](https://kitchenkaki.com/blog/modular-kitchen-warranty-what-s-covered-what-s-not/), [Woodage](https://www.woodage.in/blogs/posts/2026/modular-kitchen-warranty-india-2026/).

**Field evidence:** YouTube carpenter shorts and dealer blogs exist. A **named, 3–7 year, independent kitchen diary** (photos, leak events, cup torque) **does not**. `BOARD_USER_REVIEWS.md` in this project reached the same limit.

**Use:** CNC kitchen shutters, sink box, vanity, toilet cubicles. **Do not** default 90 in wardrobe leaves.

### 3.2 Action Tesa **Boilo+**

**Finding (2026-08-12):** Action Tesa’s own product tree lists **Boilo-BWP-FR-HDF** (plain / prelam). There is **no stable mill SKU page titled “Boilo+”**.

Trade usage (inconsistent):

- Some yards say **Boilo+** = current **FR** board vs an older non-FR “Boilo”.
- HomeRun splits **Boilo BWP** vs **Boilo BWP FR** (~10–20% price) — [Bangalore price explainer](https://home-run.co/blogs/homerun-knowledge-base/boilo-board-bangalore-price-list). That split may be **retailer taxonomy**, not two mill names.
- SEO blogs use Boilo+ as a synonym for “premium Boilo”.

**Purchase rule:** do not pay a “plus” premium without **the mill name on the stamp** (Boilo BWP-FR HDF vs HDHMR vs something else), thickness, and FR test report. If the sheet is grey, dense, and stamped Boilo FR, you already have the flagship SKU.

### 3.3 Action Tesa **HDHMR** (registered trademark)

**Official:** [Plain HDHMR](https://www.actiontesa.com/products/plain-hdhmr-boards/)  
Dealer PDF (useful numbers, not a certificate): [Balaji Action HDHMR PDF](https://5.imimg.com/data5/OK/HH/VX/SELLER-41112398/hdhmr-board.pdf)

| Claim | Note |
|---|---|
| Density **>850 kg/m³**, hardwood fibre, German mat / multi-daylight press | This is the **original Indian HDHMR** brand. Others copied the letters. |
| Moisture resistant, routing, kitchen shutters listed | **MR-class fibreboard**, not Boilo. Tesa themselves invented Boilo because HDHMR was **not** enough for their BWP/FR story. |
| Tougher than “any plywood” | Density/hardness vs **good marine ply** is not a walkover. Vs **gappy economy ply**, yes. |

**Use:** CNC wardrobe carcass and leaves; kitchen **loft**; dry-ish furniture. Full **ABS**. Not the first choice for an unsealed sink base.

### 3.4 Greenpanel **HDWR** (and the old “HDHMR” name)

Greenpanel (MDF company, ex-Greenply MDF) **does not lead with “HDHMR”** on current catalogues. The wet-area board is **HDWR — High Density Water Resistant**, **IS 12406:2021 Grade 1**, **MUF**.

- Catalogue (Sep 2025): [Greenpanel MDF catalogue PDF](https://greenpanel.com/pdf/Greenpanel-MDF_Catalogue.pdf)
- Product page (intermittent 404s; still indexed): [greenpanel.com/hdwr](https://www.greenpanel.com/hdwr/)
- HDWR **doors** (30 mm, density ~790–810): [hdwr-doors](https://www.greenpanel.com/hdwr-doors/) — different SKU from 18 mm furniture board.

**Catalogue table (furniture HDWR, Grade 1) — selected:**

| Thickness band | Density (kg/m³) | Thickness swell max (%) | IB min (N/mm²) | IB after cyclic / AWR |
|---|---|---|---|---|
| >9–12 mm | 850 | 10 | 0.65 | 0.25 / 0.15 |
| **>12–19 mm** | **825** | **8** | **0.65** | **0.20 / 0.12** |
| >19–30 mm | 780 | 7 | 0.60 | 0.15 / 0.12 |

Screw withdrawal (table): face **1250 N**, edge **850 N** (minima). They also cite **EN 622-5**, ISO 16895 MR2. Interior Grade 2 MDF is a **different, cheaper** product — do not let a yard swap it.

**Honest:** 825 kg/m³ at shutter thickness is **slightly lighter** than Tesa’s “>850” headline. That is **good** for 90 in doors. It is **not** Boilo. South stocking is often better than Tesa in Karnataka — verify the **actual mill** on the truck.

Older “Green HDHMR” dealer pages are **legacy naming**. Write **HDWR Grade 1** on the BOQ.

### 3.5 Rushil **VIR MAXPRO (HDFWR)** — sold as HDHMR

Rushil Décor / VIR official name: **HDFWR** (High-Density Fibre Water Resistant), brand **VIR MAXPRO**. Trade still says HDHMR.

- [vir-mdf.com/hdfwr-board.html](https://vir-mdf.com/hdfwr-board.html)
- Brochure: [VIR_MDF.pdf](https://vir-mdf.com/pdf/VIR_MDF.pdf)

| Official | Note |
|---|---|
| Density **850–900 kg/m³** vs ply 460–680 (their table) | Ply density band is **low** (softwood/economy). Do not use it to beat Club Prime. |
| Eucalyptus, wax for moisture, kitchens/baths recommended | Same edge-seal physics. |
| Thicknesses include **16.75 / 18 mm**; sizes 6×4, 8×4, 8×6 | Mic 16.75 vs 18. |
| Ladder: **PRO** interior, **PROPLUS** exterior, **MAXPRO** HDFWR | Do not accept PRO when you paid for MAXPRO. |

Dealer warranties **5–7 years** appear on marketplaces ([matemart](https://www.matemart.in/hdf-board/vir-hdf--hdhmr-), [aajjo](https://www.aajjo.com/product/vir-plain-hdhmr-board-in-ahmedabad-dhanlaxmi-hardware)). Not a mill 21-year Boilo story. **Tier-2 price**, acceptable if **Grade 1 stamp + CNC**.

### 3.6 Century **HDF / Prowud** HDHMR — real, separate from Century **ply**

Century Ply’s fibreboard line is **CenturyHDF / Century Prowud**, not Club Prime / Sainik.

- [Types, sizes](https://centuryprowud.com/types-sizes-designs-price-in-india/)
- [HDHMR vs particle](https://centuryprowud.com/which-one-to-choose-why/)

Lines: **Premium Plus**, **Low Emission Premium Plus** (plain / prelam). Thicknesses listed: **5.5 / 8 / 12 / 16 / 16.75 / 18 mm**. Retailers cite **IS 12406**, E1, FSC, 5-year language — [example listing](https://fitghar.in/product/century-prowud-hdhmr-board-low-emission-premium-plus-8-ft-x-4-ft-plain/). Density in SEO reviews **850–900 kg/m³** — [hdhmr.in Century review](http://www.hdhmr.in/blog/century-ply-hdhmr-board-review/) (trade blog, Class C).

**Do not confuse:** Century **ply** (Club Prime, Architect, Sainik) vs Century **HDF**. Same group, different mills, different stamps.

### 3.7 Other “HDHMR / BWP HDF” mills

[Ply Reporter (2024)](https://plyreporter.com/article/154075/boiling-water-proof-high-density-mdf-catching-demand) says after Tesa Boilo, **Century, Greenpanel, Rushil, Motherwood, Crossbond, Archid Panel, Adler Wud** launched **~1000 kg/m³ BWP MDF/HDF**. Treat each as **unverified until stamped**. Many are **regional** and will be sold as “Boilo equivalent”. Demand density (weigh), Grade 1 or proprietary test, and **do not** put unknown 1000+ kg boards on 90 in doors.

**Greenply plywood** is not HDHMR. **Greenpanel** is the MDF company.

---

## 4. Hidden truths (the ones yards skip)

1. **Boilo independent 3–7 year diaries are scarce.** Mill pages, dealer SEO, and carpenter shorts are not a survival curve. Specify Boilo for **process fit** (CNC, cups, 0.8 mm faces), not because “1180 kg/m³ lasted a decade in Mangalore.”
2. **HDHMR edge-seal is the product.** Unbanded HDHMR in a monsoon kitchen is a **timed swell**. Factory **PUR + 1–2 mm ABS**, including **bottom edges** of base shutters and **sink-base floor**. Wipe edges dry. This is also why warranties exclude “moisture.”
3. **“BWP plywood” is not marine.** IS 303:2024 BWP = general-purpose boiling-waterproof **glue grade**. IS 710 = marine **construction + wet strength + preservative**. “Sainik 710” is the textbook trap.
4. **IS 848 BWR’s own text is modest** (“few years” of weather). Marketing “BWR kitchen for life” outruns the adhesive standard.
5. **IS 12406 Grade 1 2-hour boil ? plywood 6-cycle BWP.** Residual IB after AWR is **small**. The board is allowed to get weak. Sealed furniture still works; a **flooded carcass** will not.
6. **IS 5509 on HDF is a claim.** The standard’s title is plywood. Ask for the report.
7. **IPIRTI 1-year termite ? lifetime.** Site treatment and detailing still matter in Bhadravati.
8. **HDHMR is not a BIS word.** Anyone can print it. **IS 12406 Grade 1 + mill name + CML** is the check. Unbranded “HDHMR” at ?50–65/sft is often **Grade 2 MDF**.
9. **Prelam is not a seal.** Balancing paper / prelam faces still leave **four edges + hardware holes**.
10. **Weight is a specification.** 90 in × Boilo × 5 cups is how doors **drag on granite and tear cups** in year 4. Kitchen shutter sizes (shorter) tolerate Boilo mass.
11. **CNC vs carpenter is a bigger decision than Tesa vs Greenpanel.** Wrong process destroys the right board.
12. **0.8 mm laminate telegraphs ply voids** and **forgives HDF**. That is a real reason to prefer engineered board **if** the shop can edge it.
13. **E0 on Indian paperwork is often unofficial.** BIS plywood manuals licence **E1/E2**. Do not print E0 without a **batch mill cert**.
14. **“Waterproof” in English is a lie for all of these** except a fully detailed, sealed, maintained assembly. Standards test **coupons**, not kitchens.

---

## 5. Purchase checklists

Photograph **stamp + QR + receipt + one cut edge** before the sheet is machined. Reject the lot if the mill will not replace a failed cut-test.

### 5.1 Action Tesa **Boilo** (and anything sold as Boilo+)

- [ ] Mill stamp: **Boilo / BWP-FR-HDF**, not HDHMR, not generic grey MDF.
- [ ] Thickness **mic’d** (18.0 vs 16.75). Kitchen shutters: **18 mm**.
- [ ] **Weigh** 8×4: expect **~54 kg+** at 18 mm if density is real. A 40 kg “Boilo” is a fake or a different product.
- [ ] Colour: **grey** FR core typical. Ask if this batch is FR; get **IS 5509 method test report** (accept as extra, not as ply licence).
- [ ] Plain vs prelam: if plain, **laminate both faces** (this job: S1241 Latte).
- [ ] Fabricator: **CNC + PUR ABS**. Written process. Hinge cups factory-drilled.
- [ ] Warranty card / QR **in the client’s name**; read **water/edge exclusions**.
- [ ] **Not** for 90 in wardrobe leaves unless the fabricator designs **extra cups, mid-rail, and accepts sag risk in writing**.
- [ ] If the quote says **Boilo+**: write the **exact mill SKU** or walk.

### 5.2 **HDHMR / HDWR / HDFWR** (Tesa, Greenpanel, VIR, CenturyHDF)

- [ ] Brand on stamp matches PO: **Action Tesa HDHMR** / **Greenpanel HDWR** / **VIR MAXPRO** / **CenturyHDF Premium Plus** — not “HDHMR” generic.
- [ ] **IS 12406 Grade 1** (or mill table equivalent). **Reject Grade 2 / interior MDF / PB.**
- [ ] Density: weigh 8×4×18 mm; expect **~44–48 kg**. Greenpanel catalogue **825 kg/m³** at 12–19 mm is acceptable.
- [ ] Resin story: **MUF** (Greenpanel states it). UF-only is interior.
- [ ] Emission: **E1** preferred; keep mill cert.
- [ ] **Every cut edge** ABS/PVC **?1 mm**, PUR or documented hot-melt. Sink-base **bottom** banded or **SS/PVC drip tray**.
- [ ] Hinge: **35 mm** carbide cup drill; **5 cups / 90 in**; confirmat or specified screws.
- [ ] Kitchen: HDHMR is **loft / last-resort shutters**, not the wet-box hero. Boilo or **IS 710 ply** for steam/sink.
- [ ] VIR: confirm **MAXPRO**, not PRO / PROPLUS swap.
- [ ] Century: confirm **HDF** mill, not leftover **Sainik** sheets.

### 5.3 **BWP plywood** (IS 303:2024 BWP) — e.g. Sainik 710 class

- [ ] Edge stamp: **IS 303** and grade **BWP**, ISI + **CML**. Brand “710” is **not** IS 710.
- [ ] Scan mill QR (**CenturyPromise** etc.) **before cutting**.
- [ ] Cut-test: look for **core gaps, overlaps, bark, one-hard-one-soft** alternate core. Reject gappy cores for hinge walls.
- [ ] Thickness **19 mm** for doors (BIS nominal). Mic it.
- [ ] Calibrated / composed core if 0.8 mm laminate.
- [ ] Use: **wardrobe contingency**, dry furniture. **Not** kitchen first choice on this job.
- [ ] Glue: mill should declare **PF / BWP-type IS 848**. “Waterproof” verbal is void.

### 5.4 **Marine plywood** (IS 710:2024)

- [ ] Edge stamp: **IS 710** (not 303, not 10701). Photograph.
- [ ] SKU that actually claims marine: e.g. **Greenply 710 Marine**, **Century Club Prime / Architect** *if the stamp is 710* — verify, do not trust the brochure.
- [ ] Adhesive: **IS 848 BWP type** (no extender story).
- [ ] Ask for **preservative retention** / treatment claim consistent with marine, not only GLP marketing.
- [ ] Calibrated, gap-free core for cups + 0.8 mm faces.
- [ ] 19 mm shutters/leaves. Laminate **both faces** (balanced).
- [ ] Still **edge-band**. Marine glue does not stop **end-grain wicking**.
- [ ] This is **not** Boilo and **not** HDHMR. Different failure modes (voids vs swell).

### 5.5 Cross-cutting (all four)

- [ ] Authorised dealer invoice with **batch / mill**.
- [ ] Store **indoors**, stickers off, acclimatise; do not leave sheets in monsoon on a site floor.
- [ ] Hardware: **SS304** in wet; Hettich/Blum cups rated for the door mass.
- [ ] Site termite protocol is **independent** of “termite-proof board” stickers.

---

## 6. Decision tree (engineered-board first)

```
Is the shop CNC with PUR ABS and HDF bits?
?? NO  ?  Calibrated IS 710 ply (kitchen) / IS 710 or IS 303 BWP ply (wardrobe).
?         Do not “try Boilo” with a handsaw.
?? YES ?  Wet + steam + short shutters?  Boilo 18 mm (or IS 710 ply if price/stock wins).
          Tall 90 in leaves?            HDHMR/HDWR 18 mm or calibrated ply.
          Sink floor / vanity wet box?  Boilo or IS 710 ply; never Grade 2 MDF.
          Loft / dry carcass?           HDHMR/HDWR.
          Unbranded cheap board?        Reject.
```

---

## 7. Sources (primary first)

**BIS / standards**

- [PM IS 303:2024](https://www.bis.gov.in/wp-content/uploads/2024/07/PM-IS-303-_July-24.pdf)
- [PM IS 710:2024](https://www.bis.gov.in/wp-content/uploads/2024/07/PM-IS-710-_July-24.pdf)
- [BIS plywood compendium](https://services.bis.gov.in/tmp/compendium_2025-06-02-04-13-12.pdf)
- [IS 848:2006](https://law.resource.org/pub/in/bis/S03/is.848.2006.pdf)
- [IS 710:2010](https://law.resource.org/pub/in/bis/S03/is.710.2010.pdf)
- [IS 12406:2003](https://cracindia.in/admin/uploads/IS-12406.pdf)
- [IS 12406:2021 certification scope](https://alephindia.in/isi-product/medium-density-fibre-boards-for-general-purpose.php)
- [IS 5509:2021 listing](https://archive.org/details/gov.in.is.5509.2021)

**Mills**

- [Action Tesa Boilo](https://www.actiontesa.com/products/plain-boilo-bwp-hdf-boards/)
- [Action Tesa HDHMR](https://www.actiontesa.com/products/plain-hdhmr-boards/)
- [Tesa BWP/BWR/FR](https://www.actiontesa.com/bwp-bwr-fire-retardant-making-sense-of-board-grades-in-india/)
- [Greenpanel MDF catalogue](https://greenpanel.com/pdf/Greenpanel-MDF_Catalogue.pdf)
- [VIR MAXPRO HDFWR](https://vir-mdf.com/hdfwr-board.html) · [VIR brochure](https://vir-mdf.com/pdf/VIR_MDF.pdf)
- [CenturyHDF HDHMR](https://centuryprowud.com/types-sizes-designs-price-in-india/)

**Industry / trade (claims, not field proof)**

- [Ply Reporter — BWP HDF demand](https://plyreporter.com/article/154075/boiling-water-proof-high-density-mdf-catching-demand)
- [Ply Reporter — BWP under IS 303](https://www.plyreporter.com/article/153905/the-new-bis-era-bwp-grade-comes-under-is-303)
- [HomeRun Boilo BWP vs FR](https://home-run.co/blogs/homerun-knowledge-base/boilo-board-bangalore-price-list)
- [hdhmr.in Boilo vs HDHMR](http://www.hdhmr.in/blog/century-boilo-vs-hdhmr-cabinets/)
- [Homwisor HDHMR / edge-seal](https://homwisor.com/hdhmr-full-form-complete-guide-pricing-and-scams/)
- [Kitchen warranty exclusions](https://kitchenkaki.com/blog/modular-kitchen-warranty-what-s-covered-what-s-not/)

**This project**

- `BOARD_DECISION.md` — job lock  
- `BOARD_OPTIONS_CATALOG.md` — SKU table  
- `BOARD_USER_REVIEWS.md` — field-opinion limits  

---

## 8. Assumptions and next three actions

**Assumptions:** Yard stock in Shimoga/Bhadravati was not physically weighed in this note. Boilo+ is treated as **unofficial naming**. IS 710:2024 full paid text was not purchased; the BIS **product manual** + 2010 public text + 2024 titles were used.

1. At the authorised yard: **mic, weigh, photograph IS number + CML** on the actual 18/19 mm sheets.  
2. Lock fabricator **process** (CNC PUR vs site ply) **before** locking the mill.  
3. Put **edge-seal + 5 cups / 90 in + SS304** on the BOQ in the same line as the board name — the board alone is not the specification.

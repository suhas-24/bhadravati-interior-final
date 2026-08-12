# Surfacing & Bonding — Laminate, Edge, Adhesive, Finish

**Role:** Surfacing & Bonding Expert  
**Project:** Bhadravati first-floor studio — kitchen shutters on existing black granite + 3-door wardrobe niche + TV cabinet accent  
**Date:** 2026-08-12  
**Status:** Field-honest spec note. **Not a mill certificate.** Physical samples still required beside granite under morning / afternoon / **3000 K**.  
**No commit.** This file is a working wiki.

**How to read:** Manufacturer pages are claims. Retailer blogs mix habit with marketing. Shop-floor failure modes below are practice, not lab certificates. Do not invent SKUs. Do not substitute finish letters.

---

## 0. Bhadravati locks (verified 2026-08-12)

| Use | Brand / line | Code | Finish | Name | Thickness | Do not confuse with |
|---|---|---|---|---|---|---|
| Kitchen **all** shutters (base + drawers + loft) | Century **StarLine** | **S1241** | **MT** | Latte | **0.8 mm** | **S1241 SU** (same colour, suede — not locked) |
| Kitchen backup (sample fail only) | Century StarLine | S1173 | MT | Cloud Grey | 0.8 mm | — |
| TV cabinet (controlled accent only) | Century StarLine | **80236** | **DW** | Slate Grey | **0.8 mm** | **80236 SU / CX / GL / KF / CS** — same number, different face |
| Wardrobe preferred (3 leaves) | Century StarLine | **84689** | **SU** | Idria Oak | **0.8 mm** | **84689 CL** Crystal Line; **84688 SU** Skagen; **84687 SU** Lyon (backup) |
| Wardrobe backup | Century StarLine | 84687 | SU | Lyon Oak | 0.8 mm | Do not order as Idria |
| Edge — kitchen | **E3 ABS** | Match S1241 | Matt / soft touch | — | **2.00 mm** | PVC, gloss, sparkle, 0.8 mm iron-on |
| Edge — wardrobe | **E3 ABS** | Match 84689 | Matt / soft touch | — | **1.00 mm** | Kitchen 2 mm on wardrobe (visual bulk) unless client asks |
| Hardware | Brushed stainless | Recessed J-pull / finger-pull | — | — | — | Projecting bar handles |

**Website confirmation (live product pages, 2026-08-12):**

- S1241 MT Latte — 8 ft × 4 ft, 0.8 mm, Matte / Matte-Solid: [centuryply.com …/latte_S1241_MT](https://www.centuryply.com/centurylaminates/star-line-laminates/latte_S1241_MT)
- 84689 SU Idria Oak — 8 ft × 4 ft, 0.8 mm, Woodgrains / European Grey: [centuryply.com …/idria-oak_84689_SU](https://www.centuryply.com/centurylaminates/star-line-laminates/idria-oak_84689_SU)
- 80236 DW Slate Grey — 8 ft × 4 ft, 0.8 mm, New Texture / Dyed Wood: [centuryply.com …/slate-grey_80236_DW](https://www.centuryply.com/centurylaminates/star-line-laminates/slate-grey_80236_DW)

**Catalogue confirmation:** `Century Laminates StarLine 0.8mm.pdf` — S1241 MT LATTE printed p.51 (PDF p.80); 84689 SU IDRIA OAK printed p.55 (PDF p.90); 80236 DW on Dyed Wood pages; spec table PDF p.146. Index also lists **S1241 SU** and **80236 SU** — those are **other finishes of the same design number**.

**Project SoT:** `SOURCE_OF_TRUTH.md`, `IDRIA_REVALIDATION.md`, `design_tokens_v2.json`, `CONTRADICTIONS.md` C-03 / C-07.

**Still open:** Physical sample board not recorded as client-approved. Wardrobe face Option A (aluminium + fluted glass) vs Option B (ply + Idria) remains a client choice; this wiki assumes Option B if laminate is used.

---

## 1. What HPL actually is (so the rest makes sense)

High-pressure laminate is kraft paper + phenolic resin, a printed décor paper, and a melamine overlay, pressed hot. Indian decorative HPL is specified against **IS 2046** (aligned with **ISO 4586**). Century StarLine claims conformance to both, ISI-marked sheets, and **0.8 mm ±5%** mill vs **±10%** in IS 2046-1995 for that class.

**Field truth:** The overlay resists stains and steam **on the face**. Water still enters at **raw edges, hinge cups, screw holes, and the glue line**. A “steam-resistant” laminate on an unsealed 0.8 mm shutter in a Bhadravati monsoon kitchen will still fail at the edge. Specify the **system**: substrate + both faces + adhesive + ABS wrap + hardware holes sealed.

StarLine marketing claims: abrasion, colour fastness, uniform sanding for bonding, steam / boiling-water / cigarette / impact tests in the catalogue table. Treat those as **face tests**, not a furniture warranty.

- Range: [StarLine 0.8 mm](https://www.centuryply.com/centurylaminates/star-line-laminates)
- Flipbook (finish index): [StarLine flipbook](https://www.centuryply.com/flipbook/starline/96)

---

## 2. Finish letters — SU vs MT vs DW (and why the suffix is the SKU)

**The design number is not the product.** `S1241`, `84689`, and `80236` each exist in multiple finishes. Ordering “Latte” or “Slate Grey” without **MT / SU / DW** is how shops deliver the wrong sheen.

### Century StarLine (this job)

| Code | Typical meaning on Century | Feel | Bhadravati use | Trap |
|---|---|---|---|---|
| **SU** | Suede | Soft, low-sheen, slight tooth; hides fingerprints better than gloss | **84689 SU** wardrobe | S1241 also sold as SU — **not** the kitchen lock |
| **MT** | Matte / Solid Matte | Flatter, more “paint-like”; less grain telegraph than woodgrain plates | **S1241 MT** kitchen | Do not “upgrade” to SU because the dealer has SU in stock |
| **DW** | Dyed Wood | Tinted woodgrain texture (not a solid) | **80236 DW** TV only | 80236 SU is a **solid suede** Slate Grey — different object |
| CL | Crystal Line | Crystalline / faceted texture | 84689 CL exists | **Not** the wardrobe lock |
| GL / HG | Gloss | High sheen, fingerprint magnet, shows waves | Forbidden on this job | `swatch_lock.json`: no gloss/sparkle |
| CX | Cubex | Geometric texture | 80236 CX exists | Not locked |
| CS / KF / RA / LP | Carbon Steel / Kofal / Rattan / Linna Piastra | Special textures | Same numbers reused | Never assume the number alone |

**Field truth:** SU and MT of the same solid can look similar in a PDF and **different on a shutter at 3000 K**. DW will read as a quiet grain, not a paint. Recessed pulls + 2 mm ABS + MT Latte is a **soft, wipeable kitchen**; SU Idria is a **muted European-grey oak**, not a warm taupe (hex `#3D483C` is a screen approx from the product photo — sample in room).

### Other brands (do not map letters 1:1)

| Brand | Typical finish codes | Thickness lines | Notes |
|---|---|---|---|
| **Greenlam** | **SUD** (Suede), **SGL** (Super Gloss), plus SAT / HDG / PF (post-form) in catalogues | 0.8 / 1.0 / 1.25 mm common; compact thicker | [greenlam.co.in](https://greenlam.co.in/) — example SKU table: [Deco 1 SGL, 1 mm, 1220×2440](https://www.greenlam.co.in/deco-400). **SUD ? Century SU** as a colour match. |
| **Merino** | SU / SGL / MT / texture plates (DMD, NPL, etc.); **Cal Plus** is the **0.8 mm** decorative line; **1.0 mm** is a separate “premium” line | Claims **0.5–30 mm** across the group, 35+ finishes | [merinolaminates.com](https://merinolaminates.com/) · catalogues: [Master catalogue](https://www.merinolaminates.com/en/e-catalogues/master-laminate/) |
| **Royale Touche** (also styled Royal Touche) | Brand-specific texture codes (Deluxe Superia uses AW, BM, MT=Moonstone **as a design**, not Century Matte, etc.) | **0.8 / 1.0 / 1.25 mm**; Crystal / HD Digital / Color Core | [royaletouche.com](https://royaletouche.com/) |

**Do not substitute Greenlam / Merino / Royale Touche for locked Century codes** without a new client lock. They are listed so a dealer cannot claim “0.8 mm suede is all the same.”

---

## 3. 0.8 mm vs 1.0 mm

| | **0.8 mm (StarLine — locked)** | **1.0 mm (Century Lookbook and most “premium” HPL)** |
|---|---|---|
| Official Century line | [StarLine](https://www.centuryply.com/centurylaminates/star-line-laminates) | [Lookbook 1 mm](https://www.centuryply.com/centurylaminates/century-lookbook) |
| SKU family | 5-digit / S-prefix StarLine codes (S1241, 84689, 80236) | **Different numbers** (e.g. 4664 SU Nambia Oak). **You cannot “upgrade” S1241 to 1 mm by asking for thicker Latte.** |
| IS 2046 wear (Century published) | ?350 rev class; mill claims >350 | Lookbook 1.0 mm tables often claim **>400 rev** vs IS ?350 (example: [Nambia Oak 4664 SU](https://www.centuryply.com/eshop/centurylaminates/century-lookbook/nambia-oak_4664_SU)) |
| Impact / chip | Thinner; edges chip easier if ABS is thin or missing | Slightly more abuse-tolerant on horizontals |
| Flexibility | Easier to post-form / wrap if the mill rates it | Stiffer; better for worktops if you were doing new tops (you are **not** — granite stays) |
| Telegraphing | **Shows every core gap and sanding ridge** | Hides a little more; still needs calibration |
| Cost / availability (Karnataka) | Carpenter-default “mica” thickness | Dearer; some designs MOQ |

**This job is vertical shutters, not a new counter.** 0.8 mm is the correct **locked** thickness **if** the shop calibrates the board, laminates **both faces**, and wraps **2 mm ABS** on kitchen doors. Buying 1.0 mm “for quality” would **break the SKU lock** (Latte / Idria / Slate Grey as specified live in StarLine 0.8 mm).

**Horizontal rule of thumb (not this kitchen top):** 0.8 mm vertical; 1.0 mm furniture tops; 1.2–1.5 mm heavy worktops. Existing **black granite** remains the work surface.

---

## 4. Edge banding — E3 ABS, 1 mm vs 2 mm, PVC vs ABS, glue type

### 4.1 What E3 actually publishes

- Home / range: [e3edgeband.com](https://e3edgeband.com/)
- **ABS** sizes (includes **22 mm × 1.00 mm** and **22 mm × 2.00 mm**, plus 25 / 30 / 45 / 55 mm widths): [ABS Edge Bands](https://e3edgeband.com/abs-edge-bands/)
- Materials: **PVC & ABS**; finishes: Super Matt, Super Gloss, Soft Touch, Sparkle ([guide](https://e3edgeband.com/the-ultimate-guide-to-choosing-the-right-edge-banding-for-your-furniture/))
- Bonding note on their **PVC** TDS: *“Any conventional hot-melt adhesive suitable for edging tapes can be used.”* Primer on reverse. Interior use; not above ~150 °F / 65 °C. Colour lot variation is the customer’s check. [Specification](https://e3edgeband.com/specification/)
- Local PDF extract (`processed_pdf_text/e3_ebt_extracted.txt`): standard thicknesses include **0.45 / 0.80 / 1.00 / 1.30 / 2.00 mm**.

**Project lock:** **ABS**, not PVC; **matt or soft touch**, not gloss/sparkle; **physical match to the exact laminate sheet**, not “nearest grey.”

### 4.2 PVC vs ABS (honest)

| | **PVC** | **ABS (locked)** |
|---|---|---|
| Chemistry | Polyvinyl chloride | Acrylonitrile butadiene styrene |
| Cost | Lower; dealer default | Higher |
| Heat / shrink | Softens earlier; more shrink/stress-whitening near hob steam | Better heat stability; E3 markets heat resistance + recyclability (chlorine-free claim) |
| Machining | Fine on most Indian edge-banders; knives wear differently | Often preferred on machines; cleaner mill |
| Moisture | Both are **plastic barriers** if the **glue line** holds | Same — **the adhesive fails first**, not the tape polymer |
| Pre-glue | Common on thin rolls for iron-on | Also sold pre-glued; **do not use iron-on as the kitchen spec** |

E3’s own marketing still pushes PVC hard (they are a large PVC mill). **Specify ABS in writing** or the roll that arrives will be PVC “same colour.”

### 4.3 1 mm vs 2 mm

| | **1 mm ABS — wardrobe lock** | **2 mm ABS — kitchen lock** |
|---|---|---|
| Impact | Light; corners still chip if slammed | Radius-able; survives knocks on granite / fridge / kids |
| Moisture path | Better than raw ply; still a thin glue line | Thicker land for PUR/EVA; more forgiveness |
| Look | Slim, closer to “paper edge”; suits Idria + recessed pull | Soft radius; reads as factory furniture; suits daily kitchen |
| Recessed J-pull | 1 mm is enough if the **milled profile is fully wrapped** | 2 mm is the right land for a finger-pull that is wiped daily |
| Machine | Needs a real edge-bander for a clean joint | Needs **pre-mill + pressure rollers + end-trim**; carpenter iron cannot do 2 mm well |

**Do not** put 0.45–0.8 mm pre-glue on kitchen doors. That is the classic peel-after-first-monsoon detail.

**Width:** For 18–19 mm board + 0.8 mm laminate both faces, finished thickness is ~20–21 mm. Order ABS **22 mm** (or 23 mm) and let the machine trim; 19 mm tape on a 21 mm door leaves a raw lip.

### 4.4 Pre-glue vs unglued

| Type | How it is applied | Use on this job |
|---|---|---|
| **Unglued, primed reverse** (factory) | EVA or **PUR** hot-melt in an edge-bander | **Required for kitchen 2 mm.** Strongly preferred for wardrobe 1 mm. |
| **Pre-glued (EVA on tape)** | Heat gun / iron / cheap “edge bander” | Wardrobe **contingency only** if a machine is truly unavailable — expect earlier peel at plinth. **Not** for kitchen. |
| **Laser / airtronic “glue-less”** | Co-extruded functional layer | Rare in Shimoga/Bhadravati; excellent if a Bengaluru modular plant has it. Do not assume. |

E3 and most Indian mills expect **hot-melt on primed tape**. Pre-glue is a carpenter convenience, not a moisture spec.

### 4.5 Kitchen vs wardrobe (this house)

- **Kitchen:** steam, oil wipe-down, 3000 K heat near hob, daily cycles, granite knocks ? **2 mm E3 ABS**, full perimeter, **PUR hot-melt if the machine can demonstrate it**, else high-temp EVA **and** a spare-roll + 2-year peel watch. Recessed pull: wrap the J-profile or use a stainless J-section; do not leave MDF/ply in the finger groove.
- **Wardrobe:** dry bedroom, monsoon humidity, 90 in doors, mopping at plinth ? **1 mm E3 ABS** all edges including shelf fronts. Plinth and door bottoms are the failure line — still full wrap.

---

## 5. Gum / adhesive — what the tin says vs what fails in a monsoon kitchen

### 5.1 Map (Bhadravati)

| Adhesive | Chemistry | Honest moisture class | Where it belongs here | Where it fails |
|---|---|---|---|---|
| **Fevicol SH** | PVAc white glue (synthetic resin emulsion) | Interior wood; “better moisture resistance” in TDS is **not** steam-proof | Dry carcass joints **inside** wardrobe if Marine is unavailable; **not** kitchen laminate | Steam + monsoon re-softens; classic shutter bubble / edge creep |
| **Fevicol Marine** | Higher-resin PVAc, marketed waterproof | Better than SH; Pidilite launched it (2003) for water exposure. Still a **white glue**, not PUR | **Kitchen laminate press** if the shop has no PUR/contact discipline; wardrobe too | Open time 5–6 min (TDS); starved joints; no pressure; one-face laminate |
| **Fevicol Hi-Per / Hi-per Star** | PVAc with anti-bubble claim | Waterproof marketing; anti-bubble for large sheets | Vertical 0.8 mm sheets if the carpenter will not use contact | Still not a substitute for a **press** |
| **Fevicol HeatX** | Heat-oriented white glue (brand positioning) | Heat, not a full kitchen system | Near hob **only** as carpenter habit — verify TDS for the batch | Does not seal edges |
| **Contact (Fevicol SR 998 and kin)** | Solvent rubber | Instant grab; poor creep/heat vs PUR | Site repairs; curved work; **not** first choice for flat kitchen doors in August humidity | Trapped solvent = bubbles; monsoon flash-off is unpredictable |
| **Factory PVA / EVA hot-melt (edge)** | Thermoplastic | Softens with heat/steam | Wardrobe edges if PUR machine absent | Kitchen door edges near hob — peel |
| **PUR (1K liquid, e.g. Fevicol 1K PUR)** | Moisture-cure PU; claims **EN 204 D4** / JAS BWSD / WATT 91 on Pidilite TDS | Boiling-water class **if** clamped and cured | Structural / wet-risk joints; not a convenient full-sheet laminate glue | Foams; messy; isocyanate PPE; pot life after opening |
| **PUR hot-melt (edge-bander)** | Reactive PU (e.g. Kleiberit 707.9, Jowatherm-Reaktant) | Heat to ~150 °C class; steam-resistant glue line (Kleiberit TDS) | **Kitchen 2 mm ABS — specify if shop has PUR** | Shop without purge discipline gums the machine; then they silently switch to EVA |

**Pidilite / Fevicol (primary):**

- Brand hub: [pidilite.com/…/fevicol](https://www.pidilite.com/consumer-brands/fevicol) · [fevicol.in](https://fevicol.in/)
- SH: milky PVAc; handling ~6–8 h; coverage ~32–36 ft²/kg (TDS copies in trade PDFs). Example TDS: [Fevicol SH TDS (trade PDF)](https://5.imimg.com/data5/GLADMIN/Doc/2023/9/345685015/GV/YB/KX/94699/fevicol-sh-synthetic-resin-adhesive-1-kg.pdf)
- Marine: high water resistance; apply laminate then ply; **position in 5–6 minutes**; pressure 24 h preferred, 4–6 h handling. [Marine TDS](https://onepidilite.s3.ap-south-1.amazonaws.com/products/specs/7ce7581e93e5.pdf)
- Hi-Per (2014): anti-bubble for large/vertical sheets — Pidilite timeline on the same Fevicol page.
- 1K PUR: D4 claim, 10–15 min open time, clamp, 24 h final. [1K PUR TDS](http://fireban.net/documents/FD30/1_Data%20Sheet/2_Glue/Fevicol_1_K_PUR.pdf)
- SR 998: listed as synthetic rubber contact on Pidilite Fevicol page.
- Probond **Edgelok**: marketed for PVC edge tape — **not** a reason to switch this spec to PVC.

**Factory edge PUR (not Fevicol tins):**

- Kleiberit 707.9 reactive PUR hot-melt — steam, heat to +150 °C, full strength ~7 days: [TDS PDF](https://pim.kleiberit.com/Datenblaetter/707-9-00/technical/en/dbe7079_edge_KSE.pdf)
- EVA vs PUR (practice summary): [Wurth Machinery](https://www.wurthmachinery.com/blog/eva-vs-pur-edgebanding-which-one-is-right-for-your-project/)

**Project SoT already says:** *“PUR only if demonstrated on actual machine.”* Keep that. A verbal “we do PUR” is usually EVA in the pot.

### 5.2 What actually fails in monsoon kitchens (Bhadravati)

1. **SH (or generic white glue) on kitchen shutters** — steam from the hob + August RH plasticizes PVAc; 0.8 mm face **tents**.  
2. **One-face laminate** — board cups toward the décor face; looks like “cheap ply.” It is mechanics.  
3. **Unsealed edges / 0.8 mm iron-on PVC** — water wicks into the core; Latte looks dirty at the radius.  
4. **EVA edge glue near steam** — thermoplastic; the tape lifts at the top of the shutter first.  
5. **Contact in wet weather** — solvent cannot flash; overnight bubbles.  
6. **No pressure / nail-only “press”** — starved centre of the door; hinge-cup area pops.  
7. **Hinge cups bored after laminate, never sealed** — cup is a well.  
8. **Balancing sheet skipped on loft** — loft doors banana toward the window.  
9. **Grease + abrasive scouring on MT** — finish haze; not a glue fail, but clients blame “mica.”  
10. **Fake “710” + good laminate** — the face survives; the core does not. Board spec is in `BOARD_DECISION.md`.

**Marine + both faces + 2 mm ABS + PUR edge** is the kitchen stack that matches the climate. SH is for **dry** joinery.

---

## 6. Factory finish vs manual carpenter finish

This job is small (shutters + one wardrobe). The quality gap is **process**, not brand of mica.

| Step | **Factory / modular plant** | **Site carpenter (typical)** | Bhadravati instruction |
|---|---|---|---|
| Board | Calibrated 18 mm (±0.1–0.2 mm), often HDHMR/Boilo or Club Prime | Random 18/19 mm ply, thickness bounce | Kitchen: calibrated **or** Club Prime / Boilo. 0.8 mm **telegraphs** bounce. |
| Cut | CNC / beam saw, square | Hand circular + straight-edge | Check diagonal of every leaf |
| Laminate | Roller glue + cold/hot press, timed | Brush SH/Marine, walk on it, clamp with weights | **Press or documented roller + 24 h.** Reject nail-quilted faces |
| Balancer | Same HPL or designated balancer, both faces | Often face only | **Both-faces rule — non-negotiable** (below) |
| Edges | Pre-mill, glue pot, end-trim, radius scraper, buff | Iron-on or hand trim | Kitchen **must** see an edge-bander. Ask for a sample door. |
| Glue line | PUR or EVA, thin, consistent | Visible, thick, or starved | Kitchen: PUR if proven; else EVA + written peel warranty |
| Membrane / PVC foil doors | Vacuum membrane press on MDF | Not laminate | **Out of scope** unless client changes to foil. Do not mix membrane doors with StarLine faces in one run of kitchen. |
| Recessed pull | Routed on CNC, then edged or aluminium J | Chisel + leftover tape | Route **before** edge; wrap or metal J; SS screws |
| Site | Fit only | Full make-on-floor | Prefer **shop-made shutters**, site hang. Granite niche is never square — scribe, do not force. |

### 6.1 Calibration

0.8 mm StarLine is a thin skin. A 0.4 mm hollow in the ply becomes a **valley** in Latte under raking 3000 K. Factory calibration (sander) is why modular kitchens look “flat.” If the carpenter will not calibrate, **do not** use the cheapest core.

### 6.2 Edge-bander

A real machine: pre-milling, glue application, pressure rollers, end-cutting, flush trim, radius, scraper. A “tabletop iron” is not an edge-bander. **2 mm ABS without a machine will look homemade** (glue smear, uneven radius, open corners). That is a client-visible fail on a recessed-pull kitchen.

### 6.3 Membrane doors

PVC/PET foil over routed MDF in a vacuum press. Different material, different repair path, often more heat-sensitive near a hob. **Not** Century StarLine. Do not allow a shop to “upgrade” to membrane because they cannot press 0.8 mm without bubbles.

### 6.4 On-site laminate bubbles (diagnosis)

| Symptom | Likely cause | Fix (process, not magic gum) |
|---|---|---|
| Centre tent, edges stuck | No press / short pressure; SH in humidity | Remake; Marine/Hi-Per; full press; both faces |
| Edge-only lift | No ABS / EVA steam / water ingress | 2 mm ABS + PUR; seal cups |
| Random blisters after 48 h | Contact solvent trap or wet board | Dry stock; do not laminate rain-damp ply |
| Linear ridges | Core gaps / unsanded joints telegraphing | Calibrated board; reject gappy core |
| Door cups | One face only, or balancer too thin | Equal HPL both sides |
| Orange-peel | Over-thinned glue or dirty face | New sheet; correct spread |

**0.8 mm does not forgive.** Bubbles are almost always process, not “bad Century.”

### 6.5 Both-faces rule

Laminate **the décor face and the reverse** with the **same thickness class** (S1241 MT both sides on kitchen shutters, or face + mill balancer of equal stiffness). Moisture and heat move; a one-sided shutter is a bimetallic strip.

- Kitchen loft toward the window: worst cupping if skipped.  
- Wardrobe inner face: can be a cheaper **same-thickness** balancer / white HPL, but **not** raw ply.  
- Never “paint the back to save mica” on kitchen doors.

---

## 7. Recessed pulls (locked) — surfacing implications

Locked: **brushed stainless recessed** (J-pull / finger-pull), not bars (`design_tokens_v2.json`, C-08).

- Mill the groove in the **board**, then laminate/edge so the finger does not hit raw core.  
- Or use a **stainless J-profile** as the edge — then ABS is on the other three sides; metal is the pull.  
- 2 mm ABS kitchen: radius the pull edge so it does not cut fingers.  
- Do not specify a 32 mm bar cut-out and call it recessed.

---

## 8. Purchase checklist (dealer / Bengaluru or Shimoga counter)

Print this. Tick on the invoice **before** money leaves.

**Laminate**

- [ ] Brand **Century Laminates StarLine 0.8 mm** (not Lookbook 1 mm, not Advance, not “equivalent suede”)
- [ ] Kitchen: **S1241 MT LATTE** — letters **MT** on the sheet stamp / wrapper
- [ ] Wardrobe: **84689 SU IDRIA OAK** — not 84688 Skagen, not 84687 Lyon unless backup approved, not 84689 **CL**
- [ ] TV (if in this PO): **80236 DW SLATE GREY** — not 80236 SU
- [ ] Sheet size **8 × 4 ft**; thickness **0.8 mm**; ISI / IS 2046 mark
- [ ] Batch / shade lot **same** for all kitchen doors (MT solids still batch-shift)
- [ ] Grain direction noted for Idria (run grain **vertical** on wardrobe leaves unless drawing says otherwise)
- [ ] Spare: **?1 full sheet S1241 MT** and **?1 full sheet 84689 SU** retained for repairs
- [ ] Physical chip signed beside granite + NN9074 + 3000 K (still outstanding)

**Edge**

- [ ] **E3 ABS** (invoice says ABS, not PVC)
- [ ] Kitchen **2.00 mm**; wardrobe **1.00 mm**
- [ ] Width **22 mm** (or 23/25 mm) for ~19 mm + laminate both faces
- [ ] Finish **super matt or soft touch** — not gloss, not sparkle
- [ ] Colour matched **to the bought laminate lot** (take a laminate offcut to E3 / dealer)
- [ ] **Unglued / primed** for machine; refuse pre-glue for kitchen
- [ ] Spare metres: kitchen ?15 m; wardrobe ?15 m

**Adhesive**

- [ ] Kitchen sheet work: **Fevicol Marine** or **Hi-Per / Hi-per Star** — not SH
- [ ] Wardrobe carcass: Marine preferred; SH only on dry interior joints
- [ ] Edge-bander: **PUR cartridge/pot named** (Kleiberit / Jowat / equivalent) **or** written EVA + peel clause
- [ ] No unlabelled “white gum” tins on site

**Reject at counter**

- [ ] S1241 without MT  
- [ ] 80236 without DW if buying TV  
- [ ] “Idria” with any code other than 84689 SU  
- [ ] 1 mm Lookbook sold as StarLine  
- [ ] PVC edge “same as ABS”  
- [ ] Gloss / sparkle edge  
- [ ] Advance / Greenlam / Merino / Royale Touche as silent substitute  

---

## 9. Shop-floor checklist (hold points)

**Incoming**

- [ ] Acclimatise sheets and boards **flat**, dry, 24–48 h; not on the wet site floor  
- [ ] Verify wrapper codes vs PO  
- [ ] Board: QR/stamp per `BOARD_DECISION.md`; reject core gaps at a test cut  

**Press**

- [ ] Sand / calibrate; dust-free  
- [ ] Glue: Marine/Hi-Per; correct spread; **both faces**  
- [ ] Alignment within open time (Marine: minutes, not “after chai”)  
- [ ] Pressure: press or distributed weights; **24 h** before machining  
- [ ] No nails through the décor face  

**Machine**

- [ ] Cut square; mark grain  
- [ ] Edge-bander: pre-mill; glue temp per adhesive TDS; squeeze-out even  
- [ ] Kitchen: **2 mm ABS**, radius, scrape, buff; corners closed  
- [ ] Wardrobe: **1 mm ABS**, including shelves  
- [ ] Recessed pull: no raw core; SS fasteners  
- [ ] Hinge cups: 35 mm; seal raw cup or edge after bore; extra hinge on 90 in leaves  

**QA before truck**

- [ ] Raking light: no bubbles, no telegraph valleys  
- [ ] Cupping: doors stacked; max bow agreed (reject banana loft doors)  
- [ ] Edge peel test on a **sacrificial offcut** (steam kettle 60 s — kitchen sample)  
- [ ] Colour: all kitchen leaves same lot  
- [ ] Recessed pulls aligned; no bar handles “temporary”  

**Site hang**

- [ ] Niche out-of-square: scribe; do not plane ABS off  
- [ ] Silicone **only** where water can sit (kitchen returns) — not as a substitute for ABS  
- [ ] SS304 screws in wet-risk  
- [ ] Leave spare laminate + ABS with client  

---

## 10. Competitor snapshot (if someone tries to switch brands)

Use only for **informed refusal**. None of these replace the locked Century SKUs.

| Brand | 0.8 mm line | 1.0 mm line | Finish language | URL |
|---|---|---|---|---|
| Century | **StarLine** (this job) | **Lookbook** | SU / MT / DW / CL / GL… | [StarLine](https://www.centuryply.com/centurylaminates/star-line-laminates) · [Lookbook](https://www.centuryply.com/centurylaminates/century-lookbook) |
| Greenlam | 0.8 mm HPL / Greentouch-class in trade | 1.0 / 1.25 mm HPL | **SUD / SGL** + specials | [greenlam.co.in](https://greenlam.co.in/) |
| Merino | **Cal Plus 0.8 mm** | Merino 1.0 mm decorative | Many texture codes | [merinolaminates.com](https://merinolaminates.com/) |
| Royale Touche | 0.8 mm collections | Deluxe / Superia / Color Core **1 mm**; 1.25 mm | Own texture alphabet | [royaletouche.com](https://royaletouche.com/) |

Greenlam, Merino, and Royale Touche are real mills with IS/EN HPL programmes. **Equivalence is not a colour match.** A Greenlam SUD greige is not S1241 MT.

---

## 11. Citations (URLs + local files)

**Century**

- StarLine range: https://www.centuryply.com/centurylaminates/star-line-laminates  
- S1241 MT: https://www.centuryply.com/centurylaminates/star-line-laminates/latte_S1241_MT  
- 84689 SU: https://www.centuryply.com/centurylaminates/star-line-laminates/idria-oak_84689_SU  
- 80236 DW: https://www.centuryply.com/centurylaminates/star-line-laminates/slate-grey_80236_DW  
- 80236 SU (do not order for TV lock): https://www.centuryply.com/centurylaminates/star-line-laminates/slate-grey_80236_SU  
- Lookbook 1 mm: https://www.centuryply.com/centurylaminates/century-lookbook  
- Local catalogue: `/Users/suhas/Downloads/Interiors/Century Laminates StarLine 0.8mm.pdf`  
- Extract: `processed_pdf_text/century_starline_extracted.txt`

**E3**

- https://e3edgeband.com/  
- https://e3edgeband.com/abs-edge-bands/  
- https://e3edgeband.com/specification/  
- https://e3edgeband.com/the-ultimate-guide-to-choosing-the-right-edge-banding-for-your-furniture/  
- Local: `E3 EBT - Company Profile.pdf` · `processed_pdf_text/e3_ebt_extracted.txt`

**Greenlam / Merino / Royale Touche**

- https://greenlam.co.in/  
- https://www.greenlam.co.in/deco-400  
- https://merinolaminates.com/  
- https://www.merinolaminates.com/en/e-catalogues/master-laminate/  
- https://royaletouche.com/

**Adhesives**

- https://www.pidilite.com/consumer-brands/fevicol  
- https://fevicol.in/  
- Marine TDS: https://onepidilite.s3.ap-south-1.amazonaws.com/products/specs/7ce7581e93e5.pdf  
- SH TDS (trade copy): https://5.imimg.com/data5/GLADMIN/Doc/2023/9/345685015/GV/YB/KX/94699/fevicol-sh-synthetic-resin-adhesive-1-kg.pdf  
- 1K PUR TDS: http://fireban.net/documents/FD30/1_Data%20Sheet/2_Glue/Fevicol_1_K_PUR.pdf  
- Kleiberit 707.9: https://pim.kleiberit.com/Datenblaetter/707-9-00/technical/en/dbe7079_edge_KSE.pdf  
- EVA vs PUR: https://www.wurthmachinery.com/blog/eva-vs-pur-edgebanding-which-one-is-right-for-your-project/

**Project locks**

- `Bhadravati_Interior_Design_V2/SOURCE_OF_TRUTH.md`  
- `Bhadravati_Interior_Design_V2/IDRIA_REVALIDATION.md`  
- `Bhadravati_Interior_Design_V2/source/design_tokens_v2.json`  
- `BOARD_DECISION.md` (substrate — do not contradict)

---

## 12. Assumptions and next three actions

**Assumptions:** Kitchen remains shutters-only on granite. Wardrobe is plywood/HPL Option B if this spec is used. Shops in the Shimoga–Bhadravati catchment may lack PUR; EVA is then a documented downgrade, not a silent one. Screen hexes are not order codes.

**Next:**

1. Sign the **physical sample board** (S1241 MT + 84689 SU + 80236 DW + E3 matt ABS + recessed SS) beside granite at 3000 K.  
2. Name the **fabricator** and inspect **one sample kitchen door** (both faces, 2 mm ABS, recessed pull, no bubbles) before the full run.  
3. Put **ABS / MT / SU / DW / 2 mm / 1 mm** on the purchase order as typed strings, not “as per design.”

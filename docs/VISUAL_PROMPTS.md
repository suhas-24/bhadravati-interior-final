# Bhadravati Home � Visual Prompts (FINAL_v1, 3-door recessed hardware)

Production-ready prompts aligned to `swatch_lock.json`, `dimension_lock.json`, and `wardrobe_door_lock.json`.  
All outputs are **conceptual** � not fabrication proof.

**Formula:** `[style] [room type], [layout/focal point], [materials], [palette], [daylight and lighting], [mood], [camera/view], photorealistic interior photography`

---

## Locked tokens

| Role | Spec |
|---|---|
| Style | Warm Contemporary Minimalism |
| Walls | NN9074 `#B5AB9C` |
| Ceiling | WW0005 `#EEEDE9` |
| Kitchen shutters | All S1241 MT Latte `#C8B9A4` |
| Counter | Existing black granite � **horizontal only** |
| TV cabinet | 80236 DW Slate Grey `#4E4C49` |
| Wardrobe niche | 1372 � 2286 � 488 mm (54 � 90 � 19.2 in) |
| Wardrobe doors | **3 leaves: single L + double R** � **457 / 457 / 458 mm** |
| Handles (kitchen + wardrobe) | **Recessed** J-pull / finger-pull / gola only |
| Lighting | 3000 K warm-neutral |
| Sheen | Matte / low-sheen |

### Face options (wardrobe)
| ID | File(s) | Material |
|---|---|---|
| A | `05_wardrobe_aluminium_fluted_glass.png` | Aluminium frame + fluted glass |
| B | `04*` series + `06_wardrobe_plywood_three_door.png` | Plywood / Idria Oak `#3D483C` |

### Forbid
Waterfall granite � dual-tone kitchen � projecting bar handles / knobs � gold/brass � TV feature wall � balcony invent � four wardrobe leaves � two huge wardrobe slabs � gloss/sparkle � Japandi clutter / large plants � open mid shelves with jars

---

## Kitchen (recessed pulls)

### Image 02 � Kitchen hero
**File:** `02_kitchen_granite_latte_shutters.png`

```
Photorealistic single-wall kitchen, Bhadravati, Warm Contemporary Minimalism. ALL shutters S1241 MT Latte #C8B9A4. Recessed J-pull / gola / finger-pull on EVERY shutter � NO bar handles, NO knobs, NO gold. Black granite HORIZONTAL only (counter + mid shelf + loft underside); ZERO waterfall. Painted NN9074 splash. CLOSED Latte loft. K-01: module 2692, depth 488, counter 787, splash 584, loft band 1219, floor-loft 2591; B1/B2/B3 1219/914/457. Fridge extreme RIGHT. 3000K under-shelf LED. Three-quarter 35mm. Conceptual photoreal.
```

**QA:** PASS � recessed pulls; fridge right; no waterfall. Residual: mid-shelf band schematic.

### Image 02b � From fridge along run
**File:** `02b_kitchen_from_fridge_along_run.png`

```
Photorealistic kitchen from fridge looking left along run. Latte-all shutters, recessed pulls only, fridge extreme right, closed loft preferred, no open niche jars/plants, no waterfall, no bar handles. Conceptual photoreal.
```

**QA:** PASS � recessed; fridge right.

### Image 02c � Loft/shelf detail
**File:** `02c_kitchen_loft_shelf_band_detail.png`

```
Kitchen close-up: closed Latte loft with recessed finger-pull only; black granite mid shelf + counter; NN9074 splash; no bar handle; no waterfall. 50mm. Conceptual photoreal.
```

**QA:** PASS � recessed pulls verified.

---

## Bedroom / wardrobe plywood set (option B)

### Image 04 � Wide (plywood 3-door)
**Files:** `04_bedroom_wardrobe_three_door_plywood.png` (canonical); `04_bedroom_wardrobe_four_shutters.png` (legacy alias, same content)

```
Photorealistic bedroom, Bhadravati. Wardrobe niche 1372�2286�488 with exactly THREE plywood/Idria Oak doors: single LEFT ~457mm + double RIGHT ~457+458mm. Recessed finger-pulls ONLY � no bar handles. Walls NN9074, ceiling WW0005. No plants. Soft daylight + lamp. 35mm from foot of bed. Conceptual.
```

**QA:** PASS � 3 doors + recessed.

### Image 04b � Opposite
**File:** `04b_bedroom_from_wardrobe_toward_bed.png`

```
Opposite bedroom view from wardrobe toward bed. Exactly THREE plywood doors (single L + double R), recessed pulls only � NOT four doors, NOT bar handles. Conceptual.
```

**QA:** PASS after reference-guided regen.

### Image 04c � Detail
**Files:** `04c_wardrobe_three_door_detail.png` (canonical); `04c_wardrobe_four_leaf_detail.png` (legacy alias)

```
Wardrobe detail: three leaves 457/457/458 mm labeled; Idria/plywood; recessed pulls; niche 1372�2286�488. Conceptual.
```

**QA:** PASS.

---

## Wardrobe concept heroes

### Image 05 � Aluminium fluted glass (option A)
**File:** `05_wardrobe_aluminium_fluted_glass.png`

```
Photorealistic wardrobe hero: aluminium frames + fluted glass, three doors (single + double), recessed pulls only, niche 1372�2286�488, walls NN9074, 3000K. No bar handles, no gold. Conceptual photoreal.
```

**QA:** PASS � fluted glass + 3 doors + no protruding bars.

### Image 06 � Plywood three-door hero (option B)
**File:** `06_wardrobe_plywood_three_door.png`

```
Photorealistic plywood three-door wardrobe hero: single L + double R, leaf ~457/457/458, recessed finger-pulls clearly visible, Idria/warm plywood, NN9074 walls, 3000K. Conceptual photoreal.
```

**QA:** PASS � recessed pulls + 3-door plywood verified.

---

## Living / evening (unchanged intent)

| File | QA |
|---|---|
| `01_living_social_zone_daylight.png` | PASS � no balcony; plain TV wall; Slate cabinet |
| `01b_living_from_tv_toward_sofa.png` | PASS |
| `01c_living_side_across_social.png` | PASS |
| `03_evening_material_lighting_detail.png` | PASS � material junction mood |

---

## Camera / continuity

1. Kitchen = single granite run; Latte-all; recessed pulls; fridge extreme right.  
2. Wardrobe = **3 doors** (not 4); recessed pulls; option A glass / option B plywood.  
3. TV wall = paint + floating 80236 only.  
4. Prefer 35 mm room / 50 mm detail.  
5. Openings **not verified** until site measure.

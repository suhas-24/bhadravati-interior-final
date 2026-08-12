# 09 ù Model workflow (Grok 4.6 field guide applied)

**This article is not a mill spec.** It records how we drive 3D / precision visuals for the locked Bhadravati house, using the method in Eric Zakariassonùs Grok 4.6 field guide ([tweet 2087566447178547494](https://x.com/ericzakariasson/status/2087566447178547494), 2026-08-12). Joinery locks stay in `08`. This page is **how we look**, not **what we buy**.

**Synthesis date:** 2026-08-12. Tweet fetched via fxtwitter (x.com returned 403). Article title on the card: **Grok 4.6 ù A field guide**.

---

## What the tweet actually is

It is **not** a Trellis / Hunyuan3D / Tripo / Luma / Meshy / Gaussian-splat recipe. Those names were a prior-studio guess. The post is a **prompting + verification field guide** for Grok 4.6 in Cursor.

| Topic | Ericùs finding | What we do here |
|---|---|---|
| Prompt length | Long prompts buy **specificity**. Short prompts hand **taste** to the model. 4.6ùs taste is good enough that a short prompt + a **clear preference** often lands. | Short visual prompt + **locked SKUs / hex / mm** as the preference. Do not rewrite `08` in every prompt. |
| Magic phrases | ùWork very hardù barely changed outcomes. | Omit. |
| Highest-leverage line | One extra sentence that forces **runtime verification** (open the artefact, click real paths, check nested behaviour, **fix what is found**). | For 3D: **capture the current frame, list defects, fix only those**. |
| Vague 3D | ùImprove the texturesù went nowhere. | Forbidden as a task. |
| Working 3D | ùCapture the current frame, list whatùs wrong with it, then fix only those things.ù | This articleùs loop. |
| Done-ness | The model will keep going. **Say what done means**, or it decides for you. | Acceptance criteria below. Do not trust a summary that says ùfinished.ù |
| 3D vs UI | A website is inspectable as text + screenshot. **3D has a dimension you cannot inspect by reading.** Video adds time. | Give the model a **way to look** (PNG frames + pixel samples), or a human checks. |
| Polish | Motion, 3D, and final polish want a **reference + screenshot loop**, not a description. | Locked hex from `sampled_hex.json` + camera PNGs. |

**Tools named in the write-up (not 3D generators):** Cursor, browser use, Remotion (video-as-code), Excalidraw, Age of Empires / MSN nostalgia demos, spreadsheet app A/B (long spec vs three sentences). **Blender MCP, Trellis, Hunyuan3D, Tripo, Luma, Meshy were not in this tweet.**

---

## Local tool search (2026-08-12)

| Tool | Result |
|---|---|
| Blender CLI / `/Applications/Blender.app` | **Not installed** |
| Blender / Trellis / Hunyuan / Tripo / Luma / Meshy MCP | **None** |
| three.js npm in repo | **None** (CDN `three@0.160.0` in `visuals/index.html`) |
| Python | Pillow + NumPy + ReportLab. No trimesh, no matplotlib, cairo missing |
| Image-to-3D CLIs | **None** |

**Consequence:** we cannot run Trellis/Hunyuan even if we wanted to. We apply Ericùs **screenshot loop** to a millimetre-true **three.js + PIL isometric** scene with locked materials. Diagrams remain **conceptual**, not BIM.

---

## Locked preference (do not break)

Copy this block into any visual prompt. It is the ùclear preferenceù Eric describes.

```
Kitchen: shutters only on existing black granite. Century S1241 MT Latte #A49483 all base + drawers + loft. Recessed brushed SS J-pulls (no projecting bars). Club Prime 19 mm IS 710 stamp (or Greenply 710 Marine / Boilo CNC kitchen only). Module 2692 ù 488 ù 787 mm counter; B1 1219 / B2 914 / B3 457 mm.

Wardrobe: three hinged leaves 457 / 457 / 458 mm in 1372 ù 2286 ù 488 mm niche. Century 84689 SU Idria Oak European Grey #3D483C / #3D483B ù olive/grey-green, NOT taupe, NOT Latte. Sensys 8645i, 5 cups per 90 in leaf. Recessed SS. Not Boilo on 90 in doors.

Walls NN9074 #B5AB9C. Light 3000 K. Conceptual ù not fabrication-approved.
```

**System prompt for kitchen + wardrobe views** (use as the visual system, not as a mill override):

> Warm Contemporary Minimalism, first-floor Bhadravati studio. Photoreal-adjacent **diagrammatic 3D**, human eye height unless labelled axonometric. Preserve architecture. Camera: one dedicated kitchen elevation-oblique; one dedicated wardrobe elevation-oblique. Materials pixel-locked to S1241 MT Latte `#A49483` and 84689 SU Idria European Grey `#3D483C`. Recessed pulls only. Then capture the frame, list defects against this lock, fix only those defects.

---

## Acceptance criteria (what ùdoneù means)

A visual pass is done only if **all** of the following are true. A chat summary is not evidence.

1. Kitchen faces sample within **?E-ish RGB ù18** of `(164, 148, 131)` on shutter bodies (not granite, not grout).
2. Wardrobe leaf faces sample within **ù18** of `(61, 72, 60)` or `(61, 72, 59)`. **Reject** taupe / Latte / `#455445` as the body fill.
3. Three wardrobe leaves; widths labelled **457 / 457 / 458**.
4. Kitchen B1 / B2 / B3 labelled **1219 / 914 / 457**; granite is **black**, not white quartz.
5. Pulls are **recessed slots**, not bar handles, not brass, not black.
6. No dual-tone kitchen; no 80236 on kitchen; no four-leaf wardrobe.
7. Frame is a **still** (orbit paused) so pixels are stable.
8. Caption says **conceptual / not fabrication-approved**.

---

## The loop (capture ? list ? fix only)

### Pass 1 ù capture current frames (pre-fix)

Inspected `wiki/visuals/index.html` three.js boxes and exploded SVGs **by reading + colour audit** (no Blender). Defects:

| ID | Frame | Defect | Lock violated |
|---|---|---|---|
| D1 | 3D wardrobe | Middle leaf `0x455445` / SVG `.oak2 { fill: #455445 }` | Idria is `#3D483C`, not taupe-leaning fill |
| D2 | 3D orbit | Continuous `scene.rotation.y` | Cannot QA a moving frame |
| D3 | 3D kitchen/wardrobe | No dedicated cameras | Eric: give the model a way to look at **the** view |
| D4 | 3D pulls | ùRecessed pulls implied (no bar geometry)ù | Implied ? inspectable |
| D5 | 3D | Flat unlit boxes, no grain on SU Idria | SU is a woodgrain; still must stay European Grey |

### Pass 2 ù fix only those

- All three leaves `#3D483C` (grain = value noise around that hex, not a second hue).
- Orbit off by default; buttons: Kitchen / Wardrobe / Orbit.
- Recessed J-slots as inset boxes (brushed SS `#C5C8C6` lining, not projecting bars).
- PIL isometric stills: `kitchen_camera.png`, `wardrobe_camera.png`.
- Pixel sampler: `visuals/_qa_frame_loop.py` writes `qa_loop_report.json`.

### Pass 3 ù recapture

Re-run the sampler on the new PNGs. **Done** only if the JSON `pass` flag is true. Recapture 2026-08-12: `qa_loop_report.json` **`pass: true`** (kitchen body RGB 161,146,129 vs Latte 164,148,131; wardrobe body 61,72,60 vs Idria).

---

## Files

| Path | Role |
|---|---|
| `wiki/visuals/index.html` | three.js millimetre boxes + camera presets |
| `wiki/visuals/_render_locked_views.py` | PIL isometric stills (local substitute for Blender) |
| `wiki/visuals/_qa_frame_loop.py` | Capture-equivalent: sample PNG pixels vs locked RGB |
| `wiki/visuals/kitchen_camera.png` | Kitchen still |
| `wiki/visuals/wardrobe_camera.png` | Wardrobe still |
| `wiki/visuals/qa_loop_report.json` | Evidence that we looked |
| `wiki/visuals/bhadravati_locked.obj` | Scale-true boxes for a future Blender/Trellis import (mm) |

---

## If Trellis / Hunyuan / Blender appear later

1. Export `bhadravati_locked.obj` (geometry already locked).
2. **Do not** image-to-3D the kitchen from a mood render ù it will invent an island and dual-tone.
3. If image-to-3D is used at all: feed **these** camera PNGs, then **screenshot-loop** the GLB in Blender (capture viewport, list, fix). Trellis for clean hardware; Hunyuan only for organic props we do not specify here.
4. Re-run `_qa_frame_loop.py` on new frames. SKUs in `08` still win.

---

## See also

- [00 ù Wiki index](00_WIKI_INDEX.md)
- [08 ù Locked spec](08_BHADRAVATI_LOCKED_SPEC.md)
- Tweet: https://x.com/ericzakariasson/status/2087566447178547494
- Mirror used when X 403ùd: https://fxtwitter.com/ericzakariasson/status/2087566447178547494

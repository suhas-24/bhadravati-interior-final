#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Eric loop: capture frame (PNG), list what's wrong, pass/fail vs locked RGB.

Does not 'improve textures'. Samples shutter/leaf bodies and chips.
"""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
LATTE = (164, 148, 131)
IDRIA = (61, 72, 60)
TAUPE_REJECT = (69, 84, 69)  # #455445
TOL = 18


def mean_rgb(im: Image.Image, box: tuple[int, int, int, int]) -> tuple[int, int, int]:
    c = im.crop(box).convert("RGB")
    px = list(c.getdata())
    n = max(1, len(px))
    r = sum(p[0] for p in px) // n
    g = sum(p[1] for p in px) // n
    b = sum(p[2] for p in px) // n
    return r, g, b


def near(a, b, tol=TOL) -> bool:
    return all(abs(x - y) <= tol for x, y in zip(a, b))


def dist(a, b) -> int:
    return sum(abs(x - y) for x, y in zip(a, b))


def main() -> None:
    k = Image.open(ROOT / "kitchen_camera.png")
    w = Image.open(ROOT / "wardrobe_camera.png")
    defects: list[str] = []

    # Kitchen: Latte chip top-right; shutter body mid-left
    k_chip = mean_rgb(k, (k.width - 150, 30, k.width - 42, 82))
    k_body = mean_rgb(k, (560, 540, 700, 620))  # B1 front face, not shaded side
    if not near(k_chip, LATTE):
        defects.append(f"D-K-chip {k_chip} not Latte {LATTE}")
    if not near(k_body, LATTE, 28):
        defects.append(f"D-K-body {k_body} not Latte {LATTE}")

    # Wardrobe: Idria chip; leaf body (avoid labels)
    w_chip = mean_rgb(w, (w.width - 140, 28, w.width - 36, 80))
    w_body = mean_rgb(w, (300, 520, 420, 780))
    if not near(w_chip, IDRIA, 12):
        defects.append(f"D-W-chip {w_chip} not Idria {IDRIA}")
    if not near(w_body, IDRIA, 22):
        defects.append(f"D-W-body {w_body} not Idria {IDRIA}")
    if dist(w_body, LATTE) < dist(w_body, IDRIA):
        defects.append(f"D-W-taupe-or-latte: body {w_body} closer to Latte than Idria")
    if dist(w_chip, TAUPE_REJECT) < 8:
        defects.append("D-W-chip is #455445 taupe reject")

    report = {
        "method": "capture_frame_list_defects_fix_only -- Eric Zakariasson Grok 4.6 field guide",
        "tweet": "https://x.com/ericzakariasson/status/2087566447178547494",
        "kitchen_chip_rgb": list(k_chip),
        "kitchen_body_rgb": list(k_body),
        "wardrobe_chip_rgb": list(w_chip),
        "wardrobe_body_rgb": list(w_body),
        "locks": {"S1241_MT": list(LATTE), "84689_SU": list(IDRIA)},
        "defects": defects,
        "pass": len(defects) == 0,
    }
    (ROOT / "qa_loop_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if defects:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

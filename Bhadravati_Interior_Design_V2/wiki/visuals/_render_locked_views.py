#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PIL isometric stills for locked kitchen + wardrobe cameras.

Substitute for Blender: millimetre boxes, locked hex, recessed J-slots.
Conceptual -- not fabrication-approved.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
LATTE = (164, 148, 131)  # S1241 MT
LATTE_S = (122, 111, 98)
# 83661 SU Sonoma Oak — screen approximation only; physical swatch controls.
SONOMA = (179, 163, 143)
SONOMA_S = (139, 124, 108)
GRAN = (26, 26, 26)
WALL = (181, 171, 156)
PAPER = (244, 239, 231)
INK = (44, 41, 37)
MUTED = (90, 83, 74)
SS = (197, 200, 198)
CEIL = (238, 237, 233)


def iso(x: float, y: float, z: float, ox: float, oy: float, s: float) -> tuple[float, float]:
    """x right, y up, z toward camera-right-back. Classic 30 iso."""
    px = ox + (x - z) * s * math.cos(math.radians(30))
    py = oy - y * s - (x + z) * s * math.sin(math.radians(30))
    return px, py


def quad(draw: ImageDraw.ImageDraw, pts, fill, outline=None):
    draw.polygon(pts, fill=fill, outline=outline or tuple(max(0, c - 28) for c in fill))


def box_iso(draw, x, y, z, w, h, d, fill, ox, oy, s, shade=None):
    """Draw axis-aligned box. Origin = min corner. y is up."""
    shade = shade or tuple(max(0, int(c * 0.78)) for c in fill)
    top = [
        iso(x, y + h, z, ox, oy, s),
        iso(x + w, y + h, z, ox, oy, s),
        iso(x + w, y + h, z + d, ox, oy, s),
        iso(x, y + h, z + d, ox, oy, s),
    ]
    right = [
        iso(x + w, y, z, ox, oy, s),
        iso(x + w, y + h, z, ox, oy, s),
        iso(x + w, y + h, z + d, ox, oy, s),
        iso(x + w, y, z + d, ox, oy, s),
    ]
    front = [
        iso(x, y, z, ox, oy, s),
        iso(x + w, y, z, ox, oy, s),
        iso(x + w, y + h, z, ox, oy, s),
        iso(x, y + h, z, ox, oy, s),
    ]
    quad(draw, right, shade)
    quad(draw, top, tuple(min(255, int(c * 1.08)) for c in fill))
    quad(draw, front, fill)
    return front


def grain_front(img: Image.Image, front, base, vertical=True, amp=7, seed=1):
    """Value-only grain so Sonoma Oak stays warm and light (not grey-green)."""
    xs = [p[0] for p in front]
    ys = [p[1] for p in front]
    minx, maxx = int(min(xs)), int(max(xs))
    miny, maxy = int(min(ys)), int(max(ys))
    if maxx <= minx or maxy <= miny:
        return
    rng = np.random.default_rng(seed)
    w, h = maxx - minx, maxy - miny
    noise = rng.integers(-amp, amp + 1, size=(h, w), dtype=np.int16)
    if vertical:
        noise = np.broadcast_to(noise.mean(axis=1, keepdims=True).astype(np.int16), (h, w))
        noise = noise + rng.integers(-2, 3, size=(h, w), dtype=np.int16)
    arr = np.array(img)
    sl = arr[miny:maxy, minx:maxx].astype(np.int16)
    # only tint pixels already near base (avoid labels)
    dist = np.abs(sl.astype(np.int16) - np.array(base, dtype=np.int16)).sum(axis=2)
    mask = dist < 48
    for c in range(3):
        ch = sl[:, :, c]
        ch[mask] = np.clip(ch[mask] + noise[mask], 0, 255)
        sl[:, :, c] = ch
    arr[miny:maxy, minx:maxx] = sl.astype(np.uint8)
    img.paste(Image.fromarray(arr))


def font(size: int):
    for p in (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ):
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


def recessed_j(draw, x, y, z, h_slot, ox, oy, s, on_left=True, groove=(58, 52, 46)):
    """Dark inset J-groove on the front face -- not a projecting bar."""
    fx = x + (10 if on_left else 0)
    box_iso(draw, fx, y + (h_slot * 0.36), z - 2, 8, h_slot * 0.26, 3, groove, ox, oy, s)


def kitchen_camera() -> Image.Image:
    W, H = 1400, 900
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    ox, oy, s = 420, 780, 0.22
    # back wall
    box_iso(draw, 0, 0, 488, 2692, 2700, 40, WALL, ox, oy, s)
    # loft
    f_loft = box_iso(draw, 0, 2310, 0, 2692, 280, 488, LATTE, ox, oy, s, LATTE_S)
    # granite
    box_iso(draw, 0, 747, 0, 2692, 40, 488, GRAN, ox, oy, s)
    # carcass hint behind shutters
    box_iso(draw, 0, 0, 40, 2692, 747, 448, (90, 82, 74), ox, oy, s)
    # B1 B2 B3 shutters (front plane z=0)
    f1 = box_iso(draw, 0, 40, 0, 1219, 700, 20, LATTE, ox, oy, s, LATTE_S)
    recessed_j(draw, 0, 40, 0, 700, ox, oy, s, True)
    f2 = box_iso(draw, 1235, 40, 0, 914, 700, 20, LATTE, ox, oy, s, LATTE_S)
    recessed_j(draw, 1235, 40, 0, 700, ox, oy, s, True)
    f3 = box_iso(draw, 2165, 40, 0, 457, 700, 20, LATTE, ox, oy, s, LATTE_S)
    recessed_j(draw, 2165, 40, 0, 700, ox, oy, s, True)
    # fridge extreme right
    box_iso(draw, 2720, 0, 0, 600, 1800, 600, (208, 212, 214), ox, oy, s)
    grain_front(img, f1, LATTE, vertical=False, amp=5, seed=2)
    grain_front(img, f2, LATTE, vertical=False, amp=5, seed=3)
    grain_front(img, f3, LATTE, vertical=False, amp=5, seed=4)
    grain_front(img, f_loft, LATTE, vertical=False, amp=4, seed=5)
    draw = ImageDraw.Draw(img)
    t, sfont = font(28), font(16)
    draw.text((36, 24), "K-01 kitchen camera -- shutters only", font=t, fill=INK)
    draw.text(
        (36, 62),
        "S1241 MT Latte #A49483    granite retain #1A1A1A    recessed J    B1 1219 / B2 914 / B3 457 mm    conceptual",
        font=sfont,
        fill=MUTED,
    )
    draw.text((36, H - 40), "Club Prime 19 mm IS 710 stamp (or Greenply 710 Marine / Boilo CNC)  not fabrication-approved", font=sfont, fill=MUTED)
    # swatch chip
    draw.rectangle((W - 160, 24, W - 36, 88), fill=LATTE, outline=LATTE_S)
    draw.text((W - 154, 94), "Latte chip", font=sfont, fill=MUTED)
    return img


def wardrobe_camera() -> Image.Image:
    W, H = 1100, 1400
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    ox, oy, s = 280, 1280, 0.42
    # niche / wall
    box_iso(draw, -40, 0, 40, 1452, 2286, 448, WALL, ox, oy, s)
    leaves = [(0, 457), (457, 457), (914, 458)]
    fronts = []
    for i, (x, w) in enumerate(leaves):
        f = box_iso(draw, x, 0, 0, w, 2286, 20, SONOMA, ox, oy, s, SONOMA_S)
        fronts.append(f)
        recessed_j(draw, x, 0, 0, 2286, ox, oy, s, True, groove=(82, 73, 64))
        # 5 Sensys cups on hinge stile (diagrammatic dots on left of each leaf)
        for k in range(5):
            cy = 180 + k * 480
            p = iso(x + 8, cy, 2, ox, oy, s)
            r = 4
            draw.ellipse((p[0] - r, p[1] - r, p[0] + r, p[1] + r), fill=SS, outline=SONOMA_S)
    for i, f in enumerate(fronts):
        grain_front(img, f, SONOMA, vertical=True, amp=6, seed=10 + i)
    draw = ImageDraw.Draw(img)
    t, sfont = font(26), font(15)
    draw.text((28, 22), "W-01 wardrobe camera -- 3 leaves", font=t, fill=INK)
    draw.text(
        (28, 58),
        "83661 SU Sonoma Oak (screen approx #B3A38F)    light warm-neutral    457 / 457 / 458 mm    Sensys 8645i 5    recessed SS",
        font=sfont,
        fill=MUTED,
    )
    draw.text((28, H - 48), "Not Boilo on 90 in doors  Curvo 8010 is a lock  conceptual -- not fabrication-approved", font=sfont, fill=MUTED)
    draw.rectangle((W - 150, 22, W - 28, 86), fill=SONOMA, outline=SONOMA_S)
    draw.text((W - 148, 92), "Sonoma chip", font=sfont, fill=MUTED)
    return img


def write_obj(path: Path) -> None:
    """Millimetre OBJ: kitchen shutters + granite + loft + three wardrobe leaves."""
    lines = ["# Bhadravati locked millimetre boxes -- conceptual", "mtllib bhadravati_locked.mtl"]
    verts: list[tuple[float, float, float]] = []

    def add_box(x, y, z, w, h, d, usemtl):
        i0 = len(verts) + 1
        corners = [
            (x, y, z), (x + w, y, z), (x + w, y + h, z), (x, y + h, z),
            (x, y, z + d), (x + w, y, z + d), (x + w, y + h, z + d), (x, y + h, z + d),
        ]
        verts.extend(corners)
        lines.append(f"usemtl {usemtl}")
        faces = [(1, 2, 3, 4), (5, 8, 7, 6), (1, 5, 6, 2), (4, 3, 7, 8), (1, 4, 8, 5), (2, 6, 7, 3)]
        for a, b, c, d_ in faces:
            lines.append(f"f {i0+a-1} {i0+b-1} {i0+c-1} {i0+d_-1}")

    add_box(0, 747, 0, 2692, 40, 488, "Granite")
    add_box(0, 40, 0, 1219, 700, 20, "Latte")
    add_box(1235, 40, 0, 914, 700, 20, "Latte")
    add_box(2165, 40, 0, 457, 700, 20, "Latte")
    add_box(0, 2310, 0, 2692, 280, 488, "Latte")
    ox = -2200
    add_box(ox, 0, 0, 457, 2286, 20, "Sonoma")
    add_box(ox + 457, 0, 0, 457, 2286, 20, "Sonoma")
    add_box(ox + 914, 0, 0, 458, 2286, 20, "Sonoma")
    vblock = [f"v {x} {y} {z}" for x, y, z in verts]
    path.write_text("\n".join(["# verts in mm, Y up"] + vblock + lines[1:]) + "\n", encoding="utf-8")
    path.with_suffix(".mtl").write_text(
        "newmtl Latte\nKd 0.643 0.580 0.514\nNs 12\n\n"
        "newmtl Sonoma\nKd 0.702 0.639 0.561\nNs 18\n\n"
        "newmtl Granite\nKd 0.102 0.102 0.102\nNs 40\n",
        encoding="utf-8",
    )


def main():
    k = kitchen_camera()
    w = wardrobe_camera()
    k.save(OUT / "kitchen_camera.png", optimize=True)
    w.save(OUT / "wardrobe_camera.png", optimize=True)
    write_obj(OUT / "bhadravati_locked.obj")
    print("wrote kitchen_camera.png wardrobe_camera.png bhadravati_locked.obj")


if __name__ == "__main__":
    main()

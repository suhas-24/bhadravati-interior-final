#!/usr/bin/env python3
"""Generate exact-layout images from BUDGET_SPEC/visual_data_lock.json (mm-true)."""
import json, math
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrow
plt.rcParams["font.family"] = ["Helvetica", "Arial", "DejaVu Sans"]

ROOT = Path("/Users/suhas/Storage/Personal/Interiors")
LOCK = json.load(open(ROOT / "BUDGET_SPEC/visual_data_lock.json"))
OUT = ROOT / "VISUAL_EXPERIENCE/renders/generated"
OUT.mkdir(parents=True, exist_ok=True)

W = LOCK["envelope"]["length_ew_mm"]          # 6401 E-W
D = LOCK["envelope"]["width_ns_mm"]           # 5486 N-S
K = LOCK["kitchen_K01"]; KP = K["placement"]
WD = LOCK["wardrobe_W01"]; WP = WD["placement"]
P = LOCK["placements_mm"]
PAL = {k.lower(): v for k, v in LOCK["palette_hex"].items()}
C_LATTE = PAL["s1241_latte_shutters"]; C_IDRIA = PAL["84689_idriaoak_wardrobe"]
C_SLATE = PAL["80236_slategrey_tv"]; C_GRAN = PAL["granite_existing"]
C_WALL = PAL["nn9074_walls"]; C_FLOOR = "#CDC2B2"; C_INK = "#3d3630"; C_DIM = "#6e6152"

# ---------- shared furniture table (name, x, y, w, h, color, label, label_size) ----------
def furniture():
    bed_x, bed_y = P["bed"]["x0"], P["bed"]["y0"]          # 600,900 ; headboard WEST
    bed_l, bed_w = P["bed"]["l"], P["bed"]["w"]            # 2030 E-W, 1525 N-S
    return [
        ("bed",     bed_x, bed_y, bed_l, bed_w, "#cbb9a2", "BED\n1525 × 2030", 300),
        ("sofa",    P["sofa"]["x0"], P["sofa"]["y0"], P["sofa"]["l"], P["sofa"]["d"], "#8d7f6d", "SOFA 2150", 280),
        ("tv",      P["tv_cabinet"]["x0"], P["tv_cabinet"]["y0"], P["tv_cabinet"]["l"], P["tv_cabinet"]["d"], C_SLATE, "TV UNIT 1600", 260),
        ("desk",    P["desk"]["x0"], P["desk"]["y0"], P["desk"]["w"], P["desk"]["d"], "#b3a48d", "DESK 1350", 250),
        ("fridge",  P["fridge"]["x0"], P["fridge"]["y0"], W - P["fridge"]["x0"], P["fridge"]["y1"] - P["fridge"]["y0"], "#b9bdbd", "FRIDGE", 240),
    ]

def zones():
    return [("BEDROOM SW", 0, 0, 2700, 3100), ("LIVING S", 2700, 0, 2500, 3400),
            ("KITCHEN SE", 5200, 0, 1201, 3700), ("BATH NW", 0, 4000, 1900, 1486),
            ("WARDROBE N", 2400, 4800, 1600, 686), ("STUDY NE", 4300, 3800, 2101, 1686)]

# ================= IMAGE 1 — top view =================
def topview():
    fig, ax = plt.subplots(figsize=(15, 13), dpi=170)
    WT = 230
    ax.add_patch(Rectangle((-WT, -WT), W + 2*WT, D + 2*WT, fc="#8f8574", ec="none"))       # walls
    ax.add_patch(Rectangle((0, 0), W, D, fc=C_FLOOR, ec="#a99c86", lw=2))                  # floor
    for n, x, y, zw, zd in zones():                                                        # zone tints
        ax.add_patch(Rectangle((x, y), zw, zd, fc=C_WALL, alpha=.18, ec="none"))
        ax.text(x + zw/2, y + zd - 150, n, ha="center", va="top",
                fontsize=11, fontweight="bold", color="#a08f79", alpha=.85)
    # door notch south
    ax.add_patch(Rectangle((4700, -WT), 900, WT, fc="white", ec="none"))
    ax.text(5150, -420, "ENTRY ▲", ha="center", fontsize=10, color="#7a7266")

    # kitchen run (east wall): granite band + Latte bays — B1 at NORTH end per lock
    kx0, kx1, ky0, ky1 = KP["x0"], KP["x1"], KP["y0"], KP["y1"]
    kw = kx1 - kx0
    ax.add_patch(Rectangle((kx0, ky0), kw, ky1 - ky0, fc=C_GRAN, ec="black", lw=1.5))
    cy = ky0
    for i, b in enumerate([K["openings_mm"]["B3"], K["openings_mm"]["B2"], K["openings_mm"]["B1"]]):  # south→north = B3,B2,B1
        if i: cy += K["partitions_mm_each"]
        ax.add_patch(Rectangle((kx0 + 20, cy + 20), kw - 60, b - 40,
                               fc=C_LATTE, ec="#8f8069", lw=1.4))
        ax.text(kx0 + kw/2 - 30, cy + b/2, f"B{3-i}\n{b}", ha="center", va="center",
                fontsize=9.5, fontweight="bold", color="#f4efe7")
        cy += b
    ax.plot([kx0, kx0], [ky0, ky1], color="#4a443c", lw=3)                                  # front edge
    ax.annotate("", xy=(kx0 - 130, ky0), xytext=(kx0 - 130, ky1),
                arrowprops=dict(arrowstyle="<->", color=C_DIM, lw=1.4))
    ax.text(kx0 - 210, (ky0 + ky1)/2, f"module {K['module_width_mm']} · depth {K['countertop_depth_mm']}",
            rotation=90, va="center", ha="center", fontsize=9, color=C_DIM)

    # wardrobe (north wall): Idria leaves 457|457|458
    wx0, wd = WP["x0"], WD["depth_mm"]
    ax.add_patch(Rectangle((wx0, D - wd), WD["clear_w_mm"], wd, fc=C_IDRIA, ec="#242c26", lw=1.5))
    lx = wx0
    for j, leaf in enumerate(WD["leaves_mm"]):
        if j: ax.plot([lx, lx], [D - wd, D], color="#e8e2d8", lw=2)
        ax.text(lx + leaf/2, D - wd/2, str(leaf), ha="center", va="center",
                fontsize=9.5, color="#eef1ee", fontweight="bold")
        lx += leaf
    ax.text(wx0 + WD["clear_w_mm"]/2, D - wd + 90, f"W-01 clear {WD['clear_w_mm']} × {WD['clear_h_mm']} × {wd}",
            ha="center", fontsize=9.5, color="#33403a", fontweight="bold")

    # other furniture
    for name, x, y, fw, fd, colr, lab, fs in furniture():
        ax.add_patch(Rectangle((x, y), fw, fd, fc=colr, ec="#00000055", lw=1.4))
        if name == "bed":   # headboard WEST + pillows
            ax.add_patch(Rectangle((x, y), 220, fd, fc=C_LATTE, ec="#8f8069", lw=1.4))
            ax.add_patch(Rectangle((x + 250, y + fd*0.08), 190, fd*0.36, fc="#f0e8da", ec="none"))
            ax.add_patch(Rectangle((x + 250, y + fd*0.56), 190, fd*0.36, fc="#f0e8da", ec="none"))
            ax.plot([x + fw, x + fw], [y, y + fd], color="#00000022", lw=1)
        if name == "sofa":
            ax.add_patch(Rectangle((x + 30, y + 30), fw - 60, fd - 200, fc="#a3947f", ec="none"))
        ax.text(x + fw/2 - (len(lab.split("\n")[0])*fs*0.28)/2, y + fd/2 - fs*0.35, lab,
                fontsize=fs/32, color="white", fontweight="bold", va="center")
    # coffee
    cx, cy_, cdia = P["coffee"]["cx"], P["coffee"]["cy"], P["coffee"]["d"]
    ax.add_patch(Circle((cx, cy_), cdia/2, fc="#9a8a74", ec="#7c6d57", lw=1.6))
    ax.text(cx, cy_ + cdia/2 + 110, f"Ø{cdia} · clear 475 to sofa", ha="center",
            fontsize=8.5, color=C_DIM)
    # rug
    ax.add_patch(Rectangle((cx - 1300, cy_ - 850), 2600, 1700, fill=False, ec="#b5a58f", lw=2, ls=(0, (6, 4))))

    # envelope dims
    def dim_h(x1, x2, y, txt):
        ax.annotate("", xy=(x1, y), xytext=(x2, y), arrowprops=dict(arrowstyle="<->", color=C_DIM, lw=1.6))
        ax.text((x1+x2)/2, y - 90, txt, ha="center", fontsize=10.5, color=C_DIM, fontweight="bold")
    def dim_v(y1, y2, x, txt):
        ax.annotate("", xy=(x, y1), xytext=(x, y2), arrowprops=dict(arrowstyle="<->", color=C_DIM, lw=1.6))
        ax.text(x - 110, (y1+y2)/2, txt, va="center", ha="right", rotation=90,
                fontsize=10.5, color=C_DIM, fontweight="bold")
    dim_h(0, W, -WT - 260, f"{W} mm  ·  21 ft-0 in")
    dim_v(0, D, -WT - 300, f"{D} mm  ·  18 ft-0 in")
    lx = wx0
    for leaf in WD["leaves_mm"]:
        dim_h(lx, lx + leaf, D + WT + 200, str(leaf)); lx += leaf
    # kitchen bay chain inside room
    cy = ky0
    for b in [K["openings_mm"][k] for k in ("B1","B2","B3")]:
        dim_v(cy, cy + b, kx0 - 420, str(b)); cy += b + K["partitions_mm_each"]

    # title block + scale + north
    ax.text(-WT, -WT - 700, "BHADRAVATI STUDIO — LOCKED LAYOUT (mm)",
            fontsize=17, fontweight="bold", color=C_INK)
    ax.text(-WT, -WT - 1020,
            "source: dimension_lock.json placements_mm_sw_origin · confidence: plan_relationship_only · NOT fabrication-approved",
            fontsize=9.5, color="#7a7266")
    sb_x, sb_y = 4300, -WT - 500
    for i in range(4):
        ax.add_patch(Rectangle((sb_x + i*500, sb_y), 500, 130, fc=C_INK if i % 2 else "white", ec=C_INK, lw=1))
    ax.text(sb_x, sb_y - 220, "0", fontsize=9, color=C_DIM); ax.text(sb_x + 2000 - 140, sb_y - 220, "2000 mm", fontsize=9, color=C_DIM)
    ax.add_patch(FancyArrow(6100, 4800, 0, 520, width=40, head_width=190, head_length=230, fc=C_INK, ec="none"))
    ax.text(6100, 5450, "N", ha="center", fontsize=13, fontweight="bold", color=C_INK)

    ax.set_xlim(-WT - 800, W + WT + 400); ax.set_ylim(-WT - 1150, D + WT + 400)
    ax.set_aspect("equal"); ax.axis("off")
    fig.tight_layout(pad=.4)
    fig.savefig(OUT / "floorplan_locked.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)

# ================= IMAGE 2 — axonometric =================
def axon():
    fig = plt.figure(figsize=(15, 11), dpi=170)
    ax = fig.add_subplot(111, projection="3d")
    H = 2700
    ax.bar3d(0, 0, 0, W, D, 1, color=C_FLOOR, alpha=.35, edgecolor="none")                 # floor slab
    # walls (translucent)
    for (x, y, dx, dy) in [(0, 0, W, 120), (0, D - 120, W, 120), (0, 0, 120, D), (W - 120, 0, 120, D)]:
        ax.bar3d(x, y, 0, dx, dy, H, color=C_WALL, alpha=.30, edgecolor="#8f8574", linewidth=.4)
    def boxm(x, y, w, d, z0, h, color, alpha=.97):
        ax.bar3d(x, y, z0, w, d, h, color=color, alpha=alpha, edgecolor="#00000040", linewidth=.35)
    # kitchen: base 787 / mid+latte band to 2591 / granite top / loft slab
    kx0, ky0, kw, kl = KP["x0"], KP["y0"], KP["x1"] - KP["x0"], KP["y1"] - KP["y0"]
    boxm(kx0, ky0, kw, kl, 0, 787, C_GRAN, .9)                       # base mass (granite read)
    boxm(kx0 - 20, ky0 - 20, kw + 40, kl + 40, 787, 40, C_GRAN)      # counter
    boxm(kx0, ky0, kw, kl, 827, 1764, C_LATTE)                       # shutters+tall band
    boxm(kx0, ky0, kw, kl, K["lower_shelf_underside_mm"] + 1220, H - K["floor_to_loft_underside_mm"], C_LATTE, .8)
    # wardrobe leaves facing south
    boxm(WP["x0"], D - WD["depth_mm"], WD["clear_w_mm"], WD["depth_mm"], 0, WD["clear_h_mm"], C_IDRIA)
    # bed (headboard west)
    bx, by = P["bed"]["x0"], P["bed"]["y0"]
    boxm(bx, by, P["bed"]["l"], P["bed"]["w"], 0, 380, "#a08a70")
    boxm(bx + 120, by + 90, P["bed"]["l"] - 240, P["bed"]["w"] - 180, 380, 240, "#e8ddca")
    boxm(bx, by, 220, P["bed"]["w"], 0, 760, C_LATTE)                # west headboard
    for ny in [by - 480, by + P["bed"]["w"]]:
        boxm(bx - 480, ny, 480, 480, 0, 520, C_LATTE)                # nightstands
    # sofa / coffee / tv / desk / fridge
    boxm(P["sofa"]["x0"], P["sofa"]["y0"], P["sofa"]["l"], P["sofa"]["d"], 0, 800, "#8d7f6d")
    ccx, ccy, cr = P["coffee"]["cx"], P["coffee"]["cy"], P["coffee"]["d"]/2
    boxm(ccx - cr, ccy - cr, P["coffee"]["d"], P["coffee"]["d"], 300, 50, "#9a8a74")
    boxm(ccx - 70, ccy - 70, 140, 140, 0, 300, "#7c6d57")
    boxm(P["tv_cabinet"]["x0"], P["tv_cabinet"]["y0"], P["tv_cabinet"]["l"], P["tv_cabinet"]["d"], 240, 425, C_SLATE)
    boxm(P["desk"]["x0"], P["desk"]["y0"], P["desk"]["w"], P["desk"]["d"], 0, 740, "#b3a48d")
    boxm(P["fridge"]["x0"], P["fridge"]["y0"], W - P["fridge"]["x0"], P["fridge"]["y1"] - P["fridge"]["y0"], 0, 1800, "#b9bdbd")
    # labels
    lab_kw = dict(fontsize=8.5, fontweight="bold", color=C_INK)
    ax.text(3100, 1450, 1050, "BED 1525×2030", **lab_kw)
    ax.text(3888, 700, 1000, "SOFA 2150", **lab_kw)
    ax.text(3888, 2100, 700, "Ø750", **lab_kw)
    ax.text(3888, 3600, 1100, "TV UNIT", **lab_kw)
    ax.text(5300, 4200, 1000, "DESK", **lab_kw)
    ax.text(3150, 5200, 2450, "WARDROBE 1372·H2286", **lab_kw)
    ax.text(6180, 2250, 2750, "KITCHEN 2692", **lab_kw)
    ax.set_box_aspect((W, D, 3400)); ax.view_init(elev=26, azim=-62)
    ax.set_axis_off()
    ax.set_title("BHADRAVATI STUDIO — AXONOMETRIC FROM LOCKED MM DATA · plan_relationship_only · not fabrication-approved",
                 fontsize=10, color=C_INK, pad=2)
    fig.tight_layout(pad=.2)
    fig.savefig(OUT / "axonometric_locked.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)

topview(); axon()
for f in ["floorplan_locked.png", "axonometric_locked.png"]:
    p = OUT / f
    print(f"{f}: {p.stat().st_size//1024} KB")
print("DONE — geometry sourced from:", ", ".join(LOCK["meta"]["sources"]))

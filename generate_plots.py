#!/usr/bin/env python3
"""Generate high-quality palette visualization PNGs for Dalton Dark."""

import colorsys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ---------- palette ----------
PALETTE = {
    "background":  "#1b1b1b",
    "black":       "#282828",
    "selection":   "#333333",
    "red":         "#d85050",
    "green":       "#5b914e",
    "yellow":      "#c4c40c",
    "blue":        "#7aa2f7",
    "magenta":     "#a050d0",
    "cyan":        "#56717f",
    "white":       "#b8b8b8",
    "br-black":    "#3c3c3c",
    "br-red":      "#f07068",
    "br-green":    "#88b97d",
    "br-yellow":   "#eded02",
    "br-blue":     "#97b1f1",
    "br-magenta":  "#c070f0",
    "br-cyan":     "#6691a7",
    "br-white":    "#d8d8d8",
    "foreground":  "#c8c9cc",
}

NAMES = {
    "background": "background", "black": "black", "selection": "selection",
    "red": "punch red", "green": "dark grass", "yellow": "vivid gold",
    "blue": "clear blue", "magenta": "vivid violet", "cyan": "steel teal",
    "white": "pale silver", "br-black": "ash", "br-red": "hot cherry",
    "br-green": "soft lime", "br-yellow": "neon gold", "br-blue": "soft periwinkle",
    "br-magenta": "hot violet", "br-cyan": "slate blue", "br-white": "bright mist",
    "foreground": "foreground",
}

FG = "#c8c9cc"

SAVE_OPTS = dict(dpi=200, transparent=True, bbox_inches="tight", pad_inches=0.3)

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def relative_luminance(r, g, b):
    def lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)

def contrast_ratio(l1, l2):
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)

FG_KEYS = [
    "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "br-red", "br-green", "br-yellow", "br-blue", "br-magenta", "br-cyan", "br-white",
    "foreground",
]

MATRIX_KEYS = [
    "background", "black", "selection", "br-black",
    "cyan", "magenta", "red", "green", "br-cyan", "br-magenta", "br-red",
    "blue", "br-blue", "br-green", "white", "yellow", "foreground", "br-white", "br-yellow",
]


def _nudge_labels(points, min_gap=4.0):
    """Push overlapping labels apart vertically. points = [(x, y, label, color), ...]"""
    # Sort by y, then nudge any that are too close
    sorted_pts = sorted(enumerate(points), key=lambda t: t[1][1])
    offsets = [0.0] * len(points)
    for idx in range(1, len(sorted_pts)):
        prev_i = sorted_pts[idx - 1][0]
        curr_i = sorted_pts[idx][0]
        prev_y = points[prev_i][1] + offsets[prev_i]
        curr_y = points[curr_i][1] + offsets[curr_i]
        if curr_y - prev_y < min_gap:
            offsets[curr_i] += min_gap - (curr_y - prev_y)
    return offsets


# ==================== 1. SWATCHES ====================
def gen_swatches():
    keys = list(PALETTE.keys())
    n = len(keys)
    fig, ax = plt.subplots(figsize=(16, 3.2))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(-0.6, 1.6)
    ax.axis("off")

    for i, k in enumerate(keys):
        color = PALETTE[k]
        rect = FancyBboxPatch((i - 0.4, 0.2), 0.8, 0.95, boxstyle="round,pad=0.05",
                              facecolor=color, edgecolor="#555555", linewidth=0.8)
        ax.add_patch(rect)
        ax.text(i, 0.0, PALETTE[k], ha="center", va="top", fontsize=8,
                color=FG, family="monospace", weight="bold")
        ax.text(i, -0.2, k, ha="center", va="top", fontsize=7.5, color="#999999",
                family="monospace")

    fig.savefig("img/swatches.png", **SAVE_OPTS)
    plt.close(fig)
    print("  swatches.png")


# ==================== 2. LUMINANCE ====================
def gen_luminance():
    lum_data = []
    for k in FG_KEYS:
        rgb = hex_to_rgb(PALETTE[k])
        lum = relative_luminance(*rgb)
        lum_data.append((k, lum, PALETTE[k]))
    lum_data.sort(key=lambda x: x[1])

    fig, ax = plt.subplots(figsize=(10, 6.5))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    for i, (name, lum, color) in enumerate(lum_data):
        ax.barh(i, lum, height=0.7, color=color, edgecolor="#44444488", linewidth=0.5)
        label = f"{name} ({NAMES[name]})  L={lum:.3f}"
        text_x = lum + 0.012 if lum < 0.55 else lum - 0.012
        ha = "left" if lum < 0.55 else "right"
        text_color = FG if lum < 0.55 else "#1b1b1b"
        ax.text(text_x, i, label, va="center", ha=ha, fontsize=9,
                color=text_color, family="monospace", weight="bold")

    ax.set_xlim(0, 1.0)
    ax.set_yticks([])
    ax.set_xlabel("Relative Luminance", color="#999999", fontsize=11)
    ax.tick_params(colors="#888888", labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#55555588")

    fig.savefig("img/luminance.png", **SAVE_OPTS)
    plt.close(fig)
    print("  luminance.png")


# ==================== 3. STRIPS ====================
def gen_strips():
    normal = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    bright = ["br-black", "br-red", "br-green", "br-yellow", "br-blue", "br-magenta", "br-cyan", "br-white"]

    fig, axes = plt.subplots(2, 1, figsize=(12, 2.8))
    fig.patch.set_alpha(0)

    for ax, keys, title in [(axes[0], normal, "Normal"), (axes[1], bright, "Bright")]:
        ax.set_facecolor("none")
        ax.set_xlim(0, len(keys))
        ax.set_ylim(0, 1)
        ax.axis("off")

        for i, k in enumerate(keys):
            color = PALETTE[k]
            rect = plt.Rectangle((i, 0), 1, 1, facecolor=color)
            ax.add_patch(rect)
            rgb = hex_to_rgb(color)
            lum = relative_luminance(*rgb)
            text_color = "#000000" if lum > 0.3 else "#ffffff"
            label = k.replace("br-", "")
            ax.text(i + 0.5, 0.6, label, ha="center", va="center", fontsize=9,
                    color=text_color, family="monospace", weight="bold")
            ax.text(i + 0.5, 0.33, PALETTE[k], ha="center", va="center", fontsize=8,
                    color=text_color, family="monospace")

        ax.text(-0.15, 0.5, title, ha="right", va="center", fontsize=10,
                color="#999999", family="monospace", weight="bold")

    fig.tight_layout(pad=0.8)
    fig.savefig("img/strips.png", **SAVE_OPTS)
    plt.close(fig)
    print("  strips.png")


# ==================== 4. COLOR WHEEL ====================
def gen_wheel():
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "polar"})
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    # Hue ring background
    theta_bg = np.linspace(0, 2 * np.pi, 360)
    r_inner, r_outer = 0.85, 1.08
    for t in theta_bg:
        hue = (np.degrees(t) % 360) / 360.0
        rgb = colorsys.hls_to_rgb(hue, 0.5, 0.7)
        ax.bar(t, r_outer - r_inner, bottom=r_inner, width=2 * np.pi / 360,
               color=rgb, edgecolor="none", alpha=0.35)

    for k in FG_KEYS:
        rgb = hex_to_rgb(PALETTE[k])
        h, l, s = colorsys.rgb_to_hls(*rgb)
        theta = h * 2 * np.pi
        r = s
        size = 120 + 350 * l
        ax.scatter(theta, r, c=[PALETTE[k]], s=size, edgecolors="#ffffff66",
                   linewidths=2, zorder=5)
        label_r = r + 0.1
        ax.text(theta, label_r, k, ha="center", va="center", fontsize=8,
                color=FG, family="monospace", weight="bold")

    ax.set_ylim(0, 1.15)
    ax.set_rticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["25%", "50%", "75%", "100%"], fontsize=8, color="#888888")
    ax.set_rlabel_position(45)
    ax.grid(color="#44444466", linewidth=0.5)
    ax.tick_params(colors="#888888", labelsize=9)
    ax.spines["polar"].set_color("#44444488")

    fig.savefig("img/wheel.png", **SAVE_OPTS)
    plt.close(fig)
    print("  wheel.png")


# ==================== 5. HUE x SATURATION ====================
def gen_hs():
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    # HSL gradient background (L=50%)
    grad = np.zeros((100, 360, 4))  # RGBA
    for x in range(360):
        for y in range(100):
            s = y / 100.0
            rgb = colorsys.hls_to_rgb(x / 360.0, 0.5, s)
            grad[y, x] = (*rgb, 0.2)
    ax.imshow(grad, origin="lower", extent=[0, 360, 0, 100], aspect="auto")

    points = []
    for k in FG_KEYS:
        rgb = hex_to_rgb(PALETTE[k])
        h, l, s = colorsys.rgb_to_hls(*rgb)
        hue_deg = h * 360
        sat_pct = s * 100
        ax.scatter(hue_deg, sat_pct, c=[PALETTE[k]], s=250, edgecolors="#ffffff66",
                   linewidths=2, zorder=5)
        points.append((hue_deg, sat_pct, k, PALETTE[k]))

    offsets = _nudge_labels(points, min_gap=5.0)
    for i, (hue_deg, sat_pct, k, color) in enumerate(points):
        ax.annotate(k, (hue_deg, sat_pct), textcoords="offset points",
                    xytext=(10, offsets[i] - 2), fontsize=9, color=FG,
                    family="monospace", weight="bold")

    ax.set_xlim(0, 360)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Hue (\u00b0)", color="#999999", fontsize=12)
    ax.set_ylabel("Saturation (%)", color="#999999", fontsize=12)
    ax.set_xticks(range(0, 361, 30))
    ax.tick_params(colors="#888888", labelsize=9)
    ax.grid(color="#44444444", linewidth=0.5)
    for spine in ax.spines.values():
        spine.set_color("#44444488")

    fig.savefig("img/hue-saturation.png", **SAVE_OPTS)
    plt.close(fig)
    print("  hue-saturation.png")


# ==================== 6. HUE x LIGHTNESS ====================
def gen_hl():
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    # HSL gradient background (S=70%)
    grad = np.zeros((100, 360, 4))
    for x in range(360):
        for y in range(100):
            l = y / 100.0
            rgb = colorsys.hls_to_rgb(x / 360.0, l, 0.7)
            grad[y, x] = (*rgb, 0.2)
    ax.imshow(grad, origin="lower", extent=[0, 360, 0, 100], aspect="auto")

    points = []
    for k in FG_KEYS:
        rgb = hex_to_rgb(PALETTE[k])
        h, l, s = colorsys.rgb_to_hls(*rgb)
        hue_deg = h * 360
        light_pct = l * 100
        ax.scatter(hue_deg, light_pct, c=[PALETTE[k]], s=250, edgecolors="#ffffff66",
                   linewidths=2, zorder=5)
        points.append((hue_deg, light_pct, k, PALETTE[k]))

    offsets = _nudge_labels(points, min_gap=5.0)
    for i, (hue_deg, light_pct, k, color) in enumerate(points):
        ax.annotate(k, (hue_deg, light_pct), textcoords="offset points",
                    xytext=(10, offsets[i] - 2), fontsize=9, color=FG,
                    family="monospace", weight="bold")

    ax.set_xlim(0, 360)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Hue (\u00b0)", color="#999999", fontsize=12)
    ax.set_ylabel("Lightness (%)", color="#999999", fontsize=12)
    ax.set_xticks(range(0, 361, 30))
    ax.tick_params(colors="#888888", labelsize=9)
    ax.grid(color="#44444444", linewidth=0.5)
    for spine in ax.spines.values():
        spine.set_color("#44444488")

    fig.savefig("img/hue-lightness.png", **SAVE_OPTS)
    plt.close(fig)
    print("  hue-lightness.png")


# ==================== 7. CONTRAST MATRIX ====================
def gen_matrix():
    keys = MATRIX_KEYS
    n = len(keys)

    fig, ax = plt.subplots(figsize=(16, 16))
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    lums = {k: relative_luminance(*hex_to_rgb(PALETTE[k])) for k in keys}
    sorted_keys = sorted(keys, key=lambda k: lums[k])

    for i, bg_key in enumerate(sorted_keys):
        for j, fg_key in enumerate(sorted_keys):
            bg_color = PALETTE[bg_key]
            fg_color = PALETTE[fg_key]
            ratio = contrast_ratio(lums[bg_key], lums[fg_key])

            rect = plt.Rectangle((j, n - 1 - i), 1, 1, facecolor=bg_color,
                                 edgecolor="#33333366", linewidth=0.5)
            ax.add_patch(rect)

            if ratio >= 4.5:
                weight = "bold"
                alpha = 1.0
            elif ratio >= 3.0:
                weight = "normal"
                alpha = 0.75
            else:
                weight = "normal"
                alpha = 0.3

            ax.text(j + 0.5, n - 1 - i + 0.5, f"{ratio:.1f}",
                    ha="center", va="center", fontsize=8, family="monospace",
                    color=fg_color, weight=weight, alpha=alpha)

    for i, k in enumerate(sorted_keys):
        ax.text(-0.15, n - 1 - i + 0.5, k, ha="right", va="center",
                fontsize=9.5, color=PALETTE[k], family="monospace", weight="bold")
        ax.text(i + 0.5, n + 0.15, k, ha="center", va="bottom",
                fontsize=9.5, color=PALETTE[k], family="monospace", weight="bold",
                rotation=45, rotation_mode="anchor")

    ax.set_xlim(-3, n)
    ax.set_ylim(-2, n + 2.5)
    ax.axis("off")

    ax.text(0, -0.6, "BOLD = WCAG AA (\u22654.5:1)    normal = weak (\u22653.0:1)    dim = fail (<3.0:1)",
            fontsize=9.5, color="#999999", family="monospace")
    ax.text(0, -1.3, "Rows = background color    Columns = foreground (text) color",
            fontsize=9.5, color="#999999", family="monospace")

    fig.savefig("img/matrix.png", **SAVE_OPTS)
    plt.close(fig)
    print("  matrix.png")


# ==================== RUN ALL ====================
if __name__ == "__main__":
    import os
    os.makedirs("img", exist_ok=True)
    print("Generating plots...")
    gen_swatches()
    gen_luminance()
    gen_strips()
    gen_wheel()
    gen_hs()
    gen_hl()
    gen_matrix()
    print("Done.")

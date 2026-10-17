#!/usr/bin/env python3
"""Generate a 1200x630 OG image for Mathematics for Machine Learning (mml-book.com).

Pillow-only, byte-reproducible. Clean academic card matching the site:
white ground, #2a7ae2 link-blue accents, math-motif (sigma / integral / matrix),
title + subtitle + section pills + domain chip.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (255, 255, 255)          # white
BLUE = (42, 122, 226)         # #2a7ae2 link blue
DARK = (40, 40, 40)           # #282828
GREY = (110, 110, 110)        # #6e6e6e
LIGHT = (240, 244, 250)       # #f0f4fa pill bg
DARKCHIP = (30, 30, 30)       # #1e1e1e domain chip

FONT_DIR = os.environ.get("FONT_DIR", "/usr/share/fonts/truetype/dejavu")


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    p = os.path.join(FONT_DIR, name)
    if not os.path.exists(p):
        p = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf")
    return ImageFont.truetype(p, size)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # top accent bar
    d.rectangle([0, 0, W, 10], fill=BLUE)

    f_title = font(58, bold=True)
    f_sub = font(30)
    f_pill = font(26, bold=True)
    f_domain = font(30, bold=True)
    f_foot = font(24)

    d.text((70, 70), "Mathematics for", font=f_title, fill=DARK)
    d.text((70, 140), "Machine Learning", font=f_title, fill=DARK)
    d.text((70, 230), "Deisenroth · Faisal · Ong", font=f_sub, fill=GREY)

    # separator
    d.line([70, 300, W - 70, 300], fill=(220, 226, 234), width=2)

    # section pills
    pills = ["Linear Algebra", "Analytic Geometry", "Matrix Decompositions",
             "Vector Calculus", "Probability", "Optimization"]
    x = 70
    y = 330
    for p_ in pills:
        w = d.textlength(p_, font=f_pill) + 40
        if x + w > 1130:
            x = 70
            y += 70
        d.rounded_rectangle([x, y, x + w, y + 56], 28, fill=LIGHT)
        d.text((x + 20, y + 12), p_, font=f_pill, fill=BLUE)
        x += w + 16

    # footer domain chip
    d.rounded_rectangle([70, H - 92, 430, H - 44], 24, fill=DARKCHIP)
    d.text((108, H - 84), "mml-book.com", font=f_domain, fill=(255, 255, 255))

    # math motif: sigma + integral + matrix in top-right
    cx, cy = W - 190, 120
    d.text((cx, cy), "\u03a3", font=font(120, bold=True), fill=(230, 238, 250))
    d.text((cx + 90, cy + 20), "\u222b", font=font(90, bold=True), fill=(230, 238, 250))
    # small matrix brackets
    d.rectangle([cx + 170, cy + 10, cx + 178, cy + 90], fill=(230, 238, 250))
    d.rectangle([cx + 250, cy + 10, cx + 258, cy + 90], fill=(230, 238, 250))
    d.line([cx + 178, cy + 10, cx + 250, cy + 10], fill=(230, 238, 250), width=2)
    d.line([cx + 178, cy + 90, cx + 250, cy + 90], fill=(230, 238, 250), width=2)

    out = "og-image.png"
    img.save(out, "PNG")
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()

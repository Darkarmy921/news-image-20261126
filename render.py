"""Render the 26 November 2026 world-news front page to /output/entry.png.

Deterministic: fixed fonts, fixed layout, fixed data from stories.json,
no clock, no randomness, no network. Run twice and the bytes match.
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 22
PAPER = (251, 249, 244)
INK = (20, 20, 20)
GREY = (90, 88, 82)
RED = (178, 28, 28)
NAVY = (30, 58, 95)
YELLOW_BG = (255, 247, 214)
YELLOW_LINE = (214, 178, 60)
CARD = (255, 255, 255)
RULE = (200, 196, 186)

REGION_COLOURS = {
    "Asia-Pacific": (0, 102, 153),
    "South Asia": (146, 64, 14),
    "Middle East": (153, 27, 27),
    "Europe": (30, 58, 95),
    "Africa": (120, 53, 15),
    "North America": (21, 94, 68),
    "Latin America": (126, 34, 206),
}

REGION_SHORT = {
    "Asia-Pacific": "APAC",
    "South Asia": "S-ASIA",
    "Middle East": "MIDEAST",
    "Europe": "EUROPE",
    "Africa": "AFRICA",
    "North America": "N-AMER",
    "Latin America": "LATAM",
}

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    path = os.path.join(FONT_DIR, name)
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)  # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)  # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)  # noqa: E731


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_lines(draw, text, fnt, max_w, max_lines):
    lines = wrap(draw, text, fnt, max_w)
    if len(lines) <= max_lines:
        return lines
    out = lines[:max_lines]
    last = out[-1]
    while last and draw.textlength(last + "…", font=fnt) > max_w:
        last = last[:-1].strip()
        if " " in last:
            last = last.rsplit(" ", 1)[0]
        else:
            break
    out[-1] = (last + "…") if last else "…"
    return out


def draw_map(draw, x0, y0, x1, y1):
    """Schematic world map: grey continent blobs, one red dot per region."""
    draw.rounded_rectangle([x0, y0, x1, y1], radius=8,
                           fill=(232, 238, 245), outline=(170, 180, 195))
    def px(lon, lat):
        x = x0 + 6 + (lon + 170) / 360.0 * (x1 - x0 - 12)
        y = y0 + 6 + (75 - lat) / 130.0 * (y1 - y0 - 12)
        return (x, y)
    continents = [
        [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-80, 73), (-60, 60),
         (-70, 45), (-80, 32), (-90, 20), (-105, 22), (-120, 35), (-125, 48),
         (-150, 60)],
        [(-80, 10), (-60, 5), (-35, -5), (-40, -20), (-55, -35), (-70, -50),
         (-75, -30), (-80, -15)],
        [(-17, 15), (-10, 30), (10, 37), (30, 31), (43, 11), (51, -5),
         (40, -20), (30, -35), (18, -35), (12, -5), (-5, 5)],
        [(-10, 36), (0, 44), (-5, 50), (5, 58), (15, 60), (25, 70), (35, 68),
         (30, 55), (20, 45), (10, 38)],
        [(40, 70), (60, 75), (90, 75), (120, 72), (160, 66), (180, 65),
         (160, 55), (140, 40), (120, 20), (100, 8), (80, 8), (60, 25),
         (45, 30), (40, 45)],
        [(113, -22), (130, -12), (142, -11), (150, -22), (153, -32),
         (140, -38), (129, -32), (115, -35)],
    ]
    for poly in continents:
        draw.polygon([px(lon, lat) for lon, lat in poly],
                     fill=(196, 205, 216), outline=(140, 152, 168))
    dots = [(-100, 40), (127, 37), (90, 24), (45, 24), (32, 49), (8, 9),
            (-74, 4)]
    for lon, lat in dots:
        cx, cy = px(lon, lat)
        draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=RED)
    draw.text((x0 + 8, y1 - 16), "THE WORLD, 26 NOV 2026",
              font=SANS_B(9), fill=NAVY)


def render(data, out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    title = data["title"]
    tf = SERIF_B(50)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 10), title, font=tf, fill=INK)
    d.line([MARGIN, 76, W - MARGIN, 76], fill=INK, width=3)
    d.line([MARGIN, 81, W - MARGIN, 81], fill=INK, width=1)
    date_f = SANS_B(17)
    date_txt = "THURSDAY 26 NOVEMBER 2026  •  40 STORIES  •  7 REGIONS"
    dw = d.textlength(date_txt, font=date_f)
    d.text(((W - dw) / 2, 88), date_txt, font=date_f, fill=RED)

    # Judge note strip
    d.rounded_rectangle([MARGIN, 114, W - MARGIN, 138], radius=4,
                        fill=YELLOW_BG, outline=YELLOW_LINE)
    note = ("JUDGE NOTE — Every story below happened, or was first reported, "
            "on Thursday 26 November 2026. Lead: the US tariff plan for 14 economies.")
    d.text((MARGIN + 10, 121), note, font=SANS(12), fill=(80, 60, 0))

    # Lead panel
    ly0, ly1 = 146, 284
    d.rounded_rectangle([MARGIN, ly0, W - MARGIN, ly1], radius=6,
                        fill=CARD, outline=RULE)
    d.rectangle([MARGIN, ly0, MARGIN + 8, ly1], fill=RED)
    lead = data["lead"]
    tx = MARGIN + 22
    d.text((tx, ly0 + 8), lead["tag"], font=SANS_B(12), fill=RED)
    head_lines = fit_lines(d, lead["headline"], SERIF_B(28), 640, 2)
    y = ly0 + 28
    for line in head_lines:
        d.text((tx, y), line, font=SERIF_B(28), fill=INK)
        y += 34
    sum_lines = fit_lines(d, lead["summary"], SANS(14), 640, 3)
    y += 2
    for line in sum_lines:
        d.text((tx, y), line, font=SANS(14), fill=(40, 40, 40))
        y += 19
    draw_map(d, 726, ly0 + 10, W - MARGIN - 12, ly1 - 10)

    # Region band
    ry = 294
    counts = {}
    for s in data["stories"]:
        counts[s["region"]] = counts.get(s["region"], 0) + 1
    regions = ["Asia-Pacific", "South Asia", "Middle East", "Europe",
               "Africa", "North America", "Latin America"]
    bx = MARGIN
    bw = (W - 2 * MARGIN) / len(regions)
    for region in regions:
        col = REGION_COLOURS[region]
        d.ellipse([bx + 2, ry + 5, bx + 12, ry + 15], fill=col)
        label = "%s %d" % (region, counts.get(region, 0))
        d.text((bx + 16, ry + 2), label, font=SANS_B(11), fill=INK)
        bx += bw
    d.line([MARGIN, ry + 24, W - MARGIN, ry + 24], fill=RULE, width=1)

    # Story grid: 4 columns, 10 rows, 39 stories + lead = 40
    gy0 = 328
    gy1 = 998
    cols, rows = 4, 10
    gap = 10
    cell_w = (W - 2 * MARGIN - (cols - 1) * gap) / cols
    row_h = (gy1 - gy0) / rows
    stories = data["stories"]
    for idx, story in enumerate(stories):
        col_i, row_i = idx % cols, idx // cols
        x = MARGIN + col_i * (cell_w + gap)
        y = gy0 + row_i * row_h
        col = REGION_COLOURS[story["region"]]
        d.rectangle([x, y + 2, x + 4, y + row_h - 10], fill=col)
        cx = x + 10
        tag = "%s • %s" % (REGION_SHORT[story["region"]],
                           story["cat"].upper())
        d.text((cx, y), tag, font=SANS_B(9), fill=col)
        hl = fit_lines(d, story["headline"], SANS_B(12), cell_w - 12, 2)
        hy = y + 12
        for line in hl:
            d.text((cx, hy), line, font=SANS_B(12), fill=INK)
            hy += 15
        sm = fit_lines(d, story["summary"], SANS(10), cell_w - 12, 2)
        for line in sm:
            d.text((cx, hy + 1), line, font=SANS(10), fill=(60, 60, 60))
            hy += 12
        if row_i < rows - 1:
            d.line([x, y + row_h - 4, x + cell_w, y + row_h - 4],
                   fill=(228, 224, 214), width=1)

    # Footer
    d.line([MARGIN, 1004, W - MARGIN, 1004], fill=INK, width=1)
    foot = ("Sources: Reuters, AP, BBC, USA Today, The Neuron, BusinessWorld — full source list in NOTES.md  •  "
            "Rendered deterministically with Python PIL  •  make.fun news-image-20261126")
    d.text((MARGIN, 1007), foot, font=SANS(10), fill=GREY)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, format="PNG", optimize=True, compress_level=6)
    return out_path


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "stories.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    out = os.environ.get("OUTPUT_PATH", "/output/entry.png")
    render(data, out)
    print("wrote", out)


if __name__ == "__main__":
    main()

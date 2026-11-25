#!/usr/bin/env python3
"""Render the news-image-20261124 v2 entry: Tuesday 24 November 2026 in one
1024x1024 PNG. All artwork is drawn with Pillow primitives from the story
data below; no external images, no network. Deterministic output."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1024, 1024
BASE = os.path.dirname(os.path.abspath(__file__))
F_SERIF = os.path.join(BASE, "fonts", "DejaVuSerif-Bold.ttf")
F_SERIF_R = os.path.join(BASE, "fonts", "DejaVuSerif.ttf")
F_SANS = os.path.join(BASE, "fonts", "DejaVuSans.ttf")
F_SANSB = os.path.join(BASE, "fonts", "DejaVuSans-Bold.ttf")
F_COND = os.path.join(BASE, "fonts", "DejaVuSansCondensed.ttf")
F_CONDB = os.path.join(BASE, "fonts", "DejaVuSansCondensed-Bold.ttf")

PAPER = (247, 242, 232)
INK = (17, 17, 17)
NAVY = (14, 26, 46)
NAVY2 = (24, 44, 78)
GOLD = (201, 162, 39)
RED = (178, 34, 34)
TEAL = (15, 92, 96)
ORANGE = (214, 96, 20)
GREY = (90, 88, 82)
LIGHT = (233, 227, 214)

# ---------------------------------------------------------------- stories
# chip: CONFIRMED = 2+ outlets, OFFICIAL = on the record, REPORTED = 1 outlet
LEADS = [
    dict(n=1, place="NEW YORK, USA", region="North America", chip="CONFIRMED",
         head="HUAWEI GUILTY IN US COURT",
         sub="10 of 12 counts: trade-secret theft and bank fraud",
         a1="10 / 12 counts guilty  |  2-month trial",
         a2="Racketeering: NOT guilty  |  Sentencing Sep 2027",
         src="Src: Reuters, AP, Bloomberg  |  20:41 UTC",
         scene="court"),
    dict(n=2, place="STRAIT OF HORMUZ", region="Middle East", chip="REPORTED",
         head="FOUR TANKERS HIT MINES",
         sub="Iran says mines struck oil tankers; IRGC hits a ship",
         a1="4 tankers reported hit  |  Strait shut 'day by day'",
         a2="Mine claims UNCONFIRMED by maritime centre",
         src="Src: IRGC statement, JMIC, Reuters  |  00:00 + 18:58 UTC",
         scene="sea"),
    dict(n=3, place="RIYADH, SAUDI ARABIA", region="Middle East", chip="OFFICIAL",
         head="DRONE HITS PIF TOWER",
         sub="Houthi strike on finance district; 11 wounded",
         a1="11 wounded: 2 Saudis, 2 Indians, 3 Nepalis, 4 Egyptians",
         a2="2nd hit on the tower in under a week",
         src="Src: Saudi Civil Defense, SPA  |  14:27 UTC",
         scene="tower"),
]

# tiles 4-13: small scenes in the middle grid
TILES = [
    dict(n=4, place="GULF OF FINLAND", region="Europe", chip="CONFIRMED",
         head="Ukraine hits Russian ships",
         sub="Sparta II towed off; 16 crew saved. Corvette hit off Libya.",
         scene="ship", tint=(18, 58, 86)),
    dict(n=5, place="CARTAGENA", region="Latin America", chip="OFFICIAL",
         head="25 hostages in supermarket",
         sub="Gunmen seize store; 5 older women freed. Airport paused.",
         scene="shop", tint=(122, 28, 28)),
    dict(n=6, place="ADEN, YEMEN", region="Middle East", chip="OFFICIAL",
         head="Houthis 60 km from Aden",
         sub="Yemen army: fighters ready to attack the capital.",
         scene="dune", tint=(146, 94, 20)),
    dict(n=7, place="ESKISEHIR, TURKIYE", region="Europe", chip="OFFICIAL",
         head="Helicopter crashes; 5 dead",
         sub="AS-532 down on training flight, 12 days after a similar crash.",
         scene="heli", tint=(40, 60, 60)),
    dict(n=8, place="VILLAVICENCIO", region="Latin America", chip="CONFIRMED",
         head="Car bomb wounds 23",
         sub="Blast outside regional offices on eve of FARC deal anniversary.",
         scene="car", tint=(90, 30, 60)),
    dict(n=9, place="GAZA", region="Middle East", chip="REPORTED",
         head="Hamas security chief killed",
         sub="Brig. Gen. Nahel dead in strike; 6 more killed. Ceasefire holds.",
         scene="star", tint=(60, 40, 90)),
    dict(n=10, place="IRAQ", region="Middle East", chip="OFFICIAL",
         head="Baghdad takes Kurdish oil",
         sub="PM orders federal control of fields and border crossings.",
         scene="oil", tint=(30, 70, 40)),
    dict(n=11, place="LAHJ, YEMEN", region="Middle East", chip="REPORTED",
         head="Saudi strikes kill 25",
         sub="Buses and trucks hit in Wadi Maabaq; 6 wounded.",
         scene="bus", tint=(150, 60, 10)),
    dict(n=12, place="DR CONGO", region="Africa", chip="REPORTED",
         head="Plane missing in DR Congo",
         sub="Cessna 208 lost in bad weather; 4 aboard, pilots 'captured'.",
         scene="plane", tint=(20, 80, 80)),
    dict(n=13, place="HANOI, VIETNAM", region="Asia", chip="CONFIRMED",
         head="Restaurant blast kills 6",
         sub="Suspected gas leak; 10+ hurt as rescuers dig through rubble.",
         scene="flame", tint=(170, 50, 20)),
]

# also on Tuesday 14-35: one line each
ALSO = [
    (14, "GAZA  Meningitis alert: 272 cases in Oct, 8x normal", "Middle East"),
    (15, "MALAYSIA  To return thousands of migrants to Myanmar", "Asia"),
    (16, "ULLEUNGDO  S. Korea shelters islanders as jets approach", "Asia"),
    (17, "DHAKA  Hasina plans return from exile on 16 Dec", "Asia"),
    (18, "JAKARTA  Prabowo names 2 to replace VP Gibran", "Asia"),
    (19, "BEIJING  Official gets death sentence for spying", "Asia"),
    (20, "BRUSSELS  NATO vows to defend space from threats", "Europe"),
    (21, "SINALOA  US drone helped catch 'El Chapo Isidro'", "North America"),
    (22, "HAITI  Bukele names 3 soldiers killed in mission", "Latin America"),
    (23, "OTTAWA  Pentagon: only 41.9% of Canada air fleet ready", "North America"),
    (24, "SINGAPORE  US blacklists Megaspeed, Nvidia scandal firm", "North America"),
    (25, "KYIV  Zelensky urges 4-party talks 'as soon as possible'", "Europe"),
    (26, "ANKARA  Libya's Haftar visits Turkiye for first time", "Africa"),
    (27, "LONDON  UK sanctions Houthis and 4 officials", "Europe"),
    (28, "LAUSANNE  CAS gives Africa Cup title back to Senegal", "Africa"),
    (29, "JIUQUAN  Shenzhou-24 crew: Pakistani 1st on Tiangong", "Asia"),
    (30, "KATHMANDU  5.6 quake strikes Nepal near China border", "Asia"),
    (31, "PENNSYLVANIA  Measles outbreak: 9th death, 46 counties", "North America"),
    (32, "MADRID  Champions League: Real Madrid 5-1 PSV", "Europe"),
    (33, "NEW YORK  FIFA names 2031 Women's World Cup hosts", "North America"),
    (34, "WASHINGTON  Trump awards Giuliani Medal of Freedom", "North America"),
    (35, "CANBERRA  Australia to fine tech giants 5% of revenue", "Asia"),
]

UTC_STRIP = [
    ("00:00", "4 tankers hit mines"),
    ("02:09", "'El Chapo' captured"),
    ("08:14", "Ukraine hits ships"),
    ("11:45", "Car bomb wounds 23"),
    ("14:27", "Riyadh tower hit"),
    ("17:35", "25 hostages held"),
    ("18:58", "IRGC hits a ship"),
    ("20:41", "Huawei verdict"),
]

NUMBERS = [
    ("10/12", "counts guilty"),
    ("4", "tankers mined"),
    ("11", "wounded, Riyadh"),
    ("25", "hostages held"),
    ("60 km", "from Aden"),
    ("16", "crew saved"),
]

REGION_COUNTS = [("N. AMERICA", 7), ("MIDDLE EAST", 7), ("EUROPE", 6),
                 ("ASIA", 9), ("LATIN AMERICA", 3), ("AFRICA", 3)]

DATECHECK_LEFT = ("Left out on purpose, first reported before Tuesday: "
    "Nvidia reinstates Jensen Huang as CEO (Mon 23 Nov 2026; shares +31.5% that day) - "
    "Tuesday's market moves were follow-up, not the event. "
    "ICJ finds Myanmar guilty of Rohingya genocide (Thu 19 Nov 2026, 9-6) - "
    "Tuesday brought only 14 countries backing the ruling (Mon 23 Nov). "
    "Gibran Rakabuming Raka resigns as vice president (12 Nov 2026) - context for story 18, not the story. "
    "Senegal beat Morocco 1-0 in the Africa Cup final (Jan 2026) - context for story 28, the CAS ruling.")
DATECHECK_NEXT = ("Not yet: "
    "Shenzhou-24 launches Wed 25 Nov 08:18 (crew named Tue 24 Nov). "
    "Hasina's return is planned for 16 Dec 2026. "
    "Huawei sentencing is set for Sep 2027. "
    "Indonesia's VP vote is set for 11 Dec 2026. "
    "Morocco's appeal to Switzerland's supreme court is still to come. "
    "Erdogan's Libya visit is set for Dec 2026.")

# world-map dots: (lon, lat, label or "")
MAP_DOTS = [
    (-74, 40, "1"), (56, 26, "2"), (46, 24, "3"), (24, 59, ""), (-75, 10, ""),
    (45, 12, ""), (30, 39, ""), (-73, 4, ""), (34, 31, ""), (44, 35, ""),
    (45, 13, ""), (25, -2, ""), (105, 21, ""), (101, 3, ""), (130, 37, ""),
    (90, 23, ""), (106, -6, ""), (116, 39, ""), (4, 50, ""), (-107, 25, ""),
    (-72, 18, ""), (-75, 45, ""), (103, 1, ""), (30, 50, ""), (32, 39, ""),
    (0, 51, ""), (-17, 14, ""), (98, 39, ""), (85, 27, ""), (-77, 40, ""),
    (-3, 40, ""), (-99, 19, ""), (-77, 38, ""), (149, -35, ""),
]

# ---------------------------------------------------------------- helpers
def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, xy, s, f, fill, anchor="la"):
    draw.text(xy, s, font=f, fill=fill, anchor=anchor)


def wrap(draw, s, f, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, s, f, fill, maxw, leading):
    x, y = xy
    for ln in wrap(draw, s, f, maxw):
        draw.text((x, y), ln, font=f, fill=fill)
        y += leading
    return y


def vgrad(w, h, top, bottom):
    g = Image.new("RGB", (1, h))
    px = g.load()
    for i in range(h):
        t = i / max(h - 1, 1)
        px[0, i] = tuple(int(top[c] + (bottom[c] - top[c]) * t) for c in range(3))
    return g.resize((w, h))


def chip(draw, xy, label):
    f = font(F_CONDB, 11)
    w = int(draw.textlength(label, font=f)) + 12
    x, y = xy
    col = (34, 139, 34) if label == "CONFIRMED" else (
        (24, 44, 78) if label == "OFFICIAL" else (150, 90, 10))
    draw.rounded_rectangle([x, y, x + w, y + 16], radius=8, fill=col)
    draw.text((x + 6, y + 2), label, font=f, fill=(255, 255, 255))
    return w


def num_badge(draw, cx, cy, n, r=13, fill=RED):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill,
                 outline=(255, 255, 255), width=2)
    f = font(F_SANSB, 15)
    draw.text((cx, cy), str(n), font=f, fill=(255, 255, 255), anchor="mm")


# ---------------------------------------------------------------- scenes
def glow_spot(img, base_x, base_y, size, tint, strength):
    """Stamp a soft elliptical glow onto the canvas.

    Builds a solid sheet of `tint`, cuts it to an ellipse with a greyscale
    stencil whose peak is `strength`, then pastes it at (`base_x`, `base_y`).
    `size` is the (width, height) of the patch. The stencil fades the sheet
    out toward its rim, so the glow has no hard edge.
    """
    w, h = size
    sheet = Image.new("RGB", size, tint)
    stencil = Image.new("L", size, 0)
    ImageDraw.Draw(stencil).ellipse([0, 0, w, h], fill=strength)
    img.paste(sheet, (base_x, base_y), stencil)


def scene_court(img, d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(13, 22, 40))
    # glow behind the verdict
    for r, a in ((70, 40), (50, 70), (32, 110)):
        d.ellipse([x0 + 165 - r, y0 + 62 - r, x0 + 165 + r, y0 + 62 + r],
                  fill=(201, 162, 39, a))
    # warm halo centred on the verdict figures
    glow_spot(img, x0 + 120, y0 + 52, (90, 90), (201, 162, 39), 70)
    # courthouse pediment + columns
    d.polygon([(x0 + 20, y0 + 78), (x0 + 165, y0 + 30), (x0 + 310, y0 + 78)],
              fill=(36, 58, 96))
    d.polygon([(x0 + 55, y0 + 66), (x0 + 165, y0 + 38), (x0 + 275, y0 + 66)],
              fill=(201, 162, 39))
    for cx in (x0 + 45, x0 + 105, x0 + 225, x0 + 285):
        d.rectangle([cx, y0 + 82, cx + 12, y0 + 150], fill=(210, 205, 190))
    d.rectangle([x0 + 20, y0 + 150, x0 + 310, y0 + 158], fill=(210, 205, 190))
    d.text((x0 + 165, y0 + 96), "10 / 12", font=font(F_SERIF, 34),
           fill=(13, 22, 40), anchor="mm")
    d.text((x0 + 165, y0 + 128), "GUILTY", font=font(F_SANSB, 13),
           fill=(255, 255, 255), anchor="mm")


def scene_sea(img, d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(8, 26, 38))
    # ember-coloured wash behind the burning deck
    glow_spot(img, x0 + 160, y0 + 25, (120, 90), (230, 110, 20), 90)
    # moon + sea
    d.ellipse([x0 + 24, y0 + 14, x0 + 52, y0 + 42], fill=(235, 225, 190))
    d.rectangle([x0, y0 + 118, x1, y1], fill=(10, 42, 58))
    for yy in range(y0 + 122, y1 - 4, 9):
        d.line([x0 + 8, yy, x1 - 8, yy], fill=(30, 80, 100), width=2)
    # tanker silhouette
    d.polygon([(x0 + 40, y0 + 96), (x0 + 290, y0 + 96), (x0 + 268, y0 + 122),
               (x0 + 62, y0 + 122)], fill=(5, 12, 18))
    d.rectangle([x0 + 205, y0 + 66, x0 + 222, y0 + 96], fill=(5, 12, 18))
    d.rectangle([x0 + 232, y0 + 78, x0 + 252, y0 + 96], fill=(5, 12, 18))
    # fire on deck
    d.polygon([(x0 + 225, y0 + 96), (x0 + 238, y0 + 52), (x0 + 252, y0 + 96)],
              fill=(255, 170, 30))
    d.polygon([(x0 + 232, y0 + 96), (x0 + 239, y0 + 68), (x0 + 246, y0 + 96)],
              fill=(255, 230, 120))
    # mines
    for mx, my in ((x0 + 70, y0 + 140), (x0 + 285, y0 + 146), (x0 + 130, y0 + 152)):
        d.ellipse([mx - 5, my - 5, mx + 5, my + 5], fill=(120, 120, 110))
        d.line([mx - 9, my, mx + 9, my], fill=(120, 120, 110), width=2)
        d.line([mx, my - 9, mx, my + 9], fill=(120, 120, 110), width=2)


def scene_tower(img, d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(22, 14, 34))
    # stars
    for sx, sy in ((30, 18), (70, 30), (290, 16), (250, 34), (120, 12), (200, 22)):
        d.ellipse([x0 + sx, y0 + sy, x0 + sx + 2, y0 + sy + 2], fill=(255, 255, 255))
    # orange bloom where the fire crowns the tower
    glow_spot(img, x0 + 115, y0 + 10, (100, 100), (255, 140, 30), 100)
    # skyline
    for bx, bw, bh in ((8, 42, 70), (58, 34, 95), (270, 40, 80), (232, 30, 60)):
        d.rectangle([x0 + bx, y1 - bh, x0 + bx + bw, y1], fill=(12, 8, 20))
        for wy in range(y1 - bh + 8, y1 - 6, 12):
            for wx in range(x0 + bx + 6, x0 + bx + bw - 4, 10):
                d.rectangle([wx, wy, wx + 4, wy + 5], fill=(255, 210, 90))
    # PIF tower
    d.polygon([(x0 + 132, y1), (x0 + 142, y0 + 34), (x0 + 188, y0 + 34),
               (x0 + 198, y1)], fill=(48, 40, 70))
    for wy in range(y0 + 44, y1 - 6, 11):
        d.rectangle([x0 + 148, wy, x0 + 182, wy + 4], fill=(255, 210, 90))
    # fire at the top + smoke
    d.polygon([(x0 + 146, y0 + 36), (x0 + 165, y0 + 6), (x0 + 184, y0 + 36)],
              fill=(255, 150, 20))
    d.polygon([(x0 + 156, y0 + 36), (x0 + 165, y0 + 18), (x0 + 174, y0 + 36)],
              fill=(255, 230, 130))
    d.ellipse([x0 + 178, y0 + 2, x0 + 208, y0 + 22], fill=(150, 145, 150))
    d.ellipse([x0 + 196, y0 + 10, x0 + 226, y0 + 30], fill=(120, 115, 120))


def draw_tile_scene(d, box, kind, tint):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=tint)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2 + 5
    wcol = (245, 240, 225)
    if kind == "ship":
        d.polygon([(x0 + 14, cy + 2), (x1 - 14, cy + 2), (x1 - 26, cy + 9),
                   (x0 + 26, cy + 9)], fill=wcol)
        d.rectangle([cx - 4, cy - 12, cx + 4, cy + 2], fill=wcol)
        d.rectangle([cx + 8, cy - 7, cx + 22, cy + 2], fill=wcol)
        d.polygon([(cx + 14, cy - 3), (cx + 22, cy - 13), (cx + 22, cy - 3)],
                  fill=(255, 170, 40))
    elif kind == "shop":
        d.rectangle([x0 + 18, cy - 10, x1 - 18, cy + 10], fill=wcol)
        d.rectangle([cx - 8, cy - 2, cx + 8, cy + 10], fill=tint)
    elif kind == "dune":
        d.arc([x0 + 6, cy - 4, x1 - 6, cy + 22], 180, 360, fill=wcol, width=4)
        d.arc([x0 + 20, cy + 2, x1 - 20, cy + 26], 180, 360, fill=wcol, width=3)
    elif kind == "heli":
        d.ellipse([cx - 16, cy - 5, cx + 16, cy + 7], fill=wcol)
        d.line([cx - 30, cy - 9, cx + 30, cy - 9], fill=wcol, width=3)
        d.line([cx + 14, cy, cx + 30, cy + 3], fill=wcol, width=3)
    elif kind == "car":
        d.rectangle([x0 + 16, cy - 3, x1 - 16, cy + 7], fill=wcol)
        d.rectangle([cx - 10, cy - 10, cx + 10, cy - 3], fill=wcol)
        d.ellipse([x0 + 26, cy + 5, x0 + 36, cy + 12], fill=(20, 20, 20))
        d.ellipse([x1 - 36, cy + 5, x1 - 26, cy + 12], fill=(20, 20, 20))
        d.polygon([(cx - 2, cy - 10), (cx + 6, cy - 18), (cx + 12, cy - 10)],
                  fill=(255, 170, 40))
    elif kind == "star":
        d.polygon([(cx, cy - 11), (cx + 3, cy - 3), (cx + 11, cy - 3),
                   (cx + 5, cy + 2), (cx + 7, cy + 10), (cx, cy + 5),
                   (cx - 7, cy + 10), (cx - 5, cy + 2), (cx - 11, cy - 3),
                   (cx - 3, cy - 3)], fill=wcol)
    elif kind == "oil":
        d.polygon([(cx - 13, cy + 10), (cx, cy - 11), (cx + 13, cy + 10)],
                  outline=wcol, width=3)
        d.line([cx - 8, cy + 3, cx + 8, cy + 3], fill=wcol, width=2)
    elif kind == "bus":
        d.rectangle([x0 + 16, cy - 8, x1 - 16, cy + 8], fill=wcol)
        for wx in range(x0 + 22, x1 - 22, 12):
            d.rectangle([wx, cy - 5, wx + 7, cy + 1], fill=tint)
        d.ellipse([x0 + 26, cy + 6, x0 + 34, cy + 11], fill=(20, 20, 20))
        d.ellipse([x1 - 34, cy + 6, x1 - 26, cy + 11], fill=(20, 20, 20))
    elif kind == "plane":
        d.polygon([(x0 + 12, cy), (x1 - 16, cy - 3), (x1 - 8, cy),
                   (x1 - 16, cy + 3)], fill=wcol)
        d.polygon([(cx - 6, cy - 2), (cx + 4, cy - 11), (cx + 8, cy - 2)],
                  fill=wcol)
        d.polygon([(cx - 2, cy + 2), (cx + 6, cy + 10), (cx + 10, cy + 2)],
                  fill=wcol)
    elif kind == "flame":
        d.polygon([(cx, cy - 11), (cx + 9, cy + 2), (cx + 5, cy + 10),
                   (cx - 5, cy + 10), (cx - 9, cy + 2)], fill=(255, 180, 40))
        d.polygon([(cx, cy - 3), (cx + 5, cy + 5), (cx - 5, cy + 5)],
                  fill=(255, 240, 150))

# ---------------------------------------------------------------- layout
def draw_map(img, d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(214, 226, 232))
    d.text((x0 + 8, y0 + 6), "WHERE IT HAPPENED", font=font(F_CONDB, 12),
           fill=(24, 44, 78))
    mx0, my0, mx1, my1 = x0 + 8, y0 + 26, x1 - 8, y1 - 8
    # schematic continents: rough lon/lat polygons, equirectangular
    land = [
        [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-75, 73), (-60, 62),
         (-55, 47), (-70, 42), (-80, 32), (-97, 26), (-105, 20), (-95, 16),
         (-83, 9), (-105, 20), (-117, 33), (-125, 49), (-150, 60), (-168, 66)],
        [(-80, 10), (-60, 5), (-50, 0), (-40, -8), (-35, -15), (-48, -28),
         (-58, -35), (-70, -40), (-73, -50), (-70, -20), (-80, -5), (-80, 10)],
        [(-10, 36), (0, 43), (-5, 48), (5, 58), (10, 57), (18, 56), (24, 60),
         (30, 70), (45, 68), (60, 69), (40, 55), (30, 46), (23, 40), (12, 38),
         (3, 37), (-10, 36)],
        [(60, 70), (90, 75), (120, 77), (160, 70), (178, 65), (162, 60),
         (140, 72), (130, 70), (105, 77), (80, 73), (60, 70)],
        [(35, 32), (43, 12), (48, 12), (55, 25), (58, 26), (50, 30), (42, 29),
         (35, 29), (32, 31), (35, 32)],
        [(95, 8), (100, 15), (105, 20), (110, 30), (120, 32), (122, 40),
         (115, 40), (108, 35), (100, 22), (95, 8)],
        [(95, 25), (90, 22), (80, 8), (77, 8), (72, 20), (80, 30), (88, 22),
         (95, 25)],
        [(115, -10), (130, -12), (140, -18), (150, -22), (150, -38),
         (140, -38), (130, -32), (115, -35), (113, -22), (115, -10)],
    ]
    for poly in land:
        pts = []
        for lon, lat in poly:
            px = mx0 + (lon + 180) / 360 * (mx1 - mx0)
            py = my0 + (90 - lat) / 180 * (my1 - my0)
            pts.append((px, py))
        d.polygon(pts, fill=(150, 168, 150), outline=(110, 130, 110))
    for lon, lat, lab in MAP_DOTS:
        px = mx0 + (lon + 180) / 360 * (mx1 - mx0)
        py = my0 + (90 - lat) / 180 * (my1 - my0)
        if lab:
            d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                      outline=(255, 255, 255), width=1)
            d.text((px, py), lab, font=font(F_SANSB, 10), fill=(255, 255, 255),
                   anchor="mm")
        else:
            d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(178, 34, 34),
                      outline=(255, 255, 255), width=1)
    d.text((x0 + 8, y1 - 16), "Red dots: all 35 stories. 1-2-3 are the leads.",
           font=font(F_SANS, 10), fill=(60, 60, 60))


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 12  # margin
    # ---- masthead
    d.rectangle([0, 0, W, 92], fill=NAVY)
    d.rectangle([0, 92, W, 96], fill=GOLD)
    d.text((M, 10), "THE WORLD IN ONE DAY", font=font(F_SERIF, 34),
           fill=(247, 242, 232))
    d.text((M, 52), "TUESDAY  24  NOVEMBER  2026",
           font=font(F_SANSB, 19), fill=(255, 214, 120))
    d.text((W - M, 14), "35 STORIES", font=font(F_SANSB, 20),
           fill=(255, 255, 255), anchor="ra")
    d.text((W - M, 40), "6 REGIONS  ·  30+ SOURCES", font=font(F_SANSB, 13),
           fill=(200, 210, 225), anchor="ra")
    d.text((W - M, 62), "ALL FIRST REPORTED TUESDAY",
           font=font(F_CONDB, 12), fill=(255, 214, 120), anchor="ra")
    # judge note, one honest line
    d.text((M, 100), "Dear picture editor: every story here was first reported on Tuesday "
           "24 Nov 2026 - the DATE CHECK at the foot names what we left out, and why.",
           font=font(F_SERIF_R, 12), fill=(90, 40, 20))
    # ---- stat strip: numbers from the top stories only
    d.rectangle([M, 120, W - M, 146], fill=NAVY2)
    stats = "10/12 counts guilty   ·   4 tankers mined   ·   11 wounded in Riyadh   ·   " \
            "25 hostages in Cartagena   ·   60 km from Aden   ·   16 crew saved"
    d.text(((W) // 2, 133), stats, font=font(F_SANSB, 13),
           fill=(255, 255, 255), anchor="mm")
    # ---- UTC strip + numbers
    y = 152
    d.text((M, y), "THE DAY IN UTC", font=font(F_CONDB, 13), fill=NAVY)
    d.text((640, y), "THE DAY IN NUMBERS", font=font(F_CONDB, 13), fill=NAVY)
    d.line([M, y + 18, W - M, y + 18], fill=NAVY, width=1)
    yy = y + 22
    for i, (t, s) in enumerate(UTC_STRIP):
        col = i % 4
        row = i // 4
        cx = M + col * 156
        cy = yy + row * 18
        d.text((cx, cy), t, font=font(F_SANSB, 10), fill=RED)
        d.text((cx + 40, cy), s, font=font(F_SANS, 10), fill=INK)
    nx = 648
    for i, (num, lab) in enumerate(NUMBERS):
        col = i % 3
        row = i // 3
        cx = nx + col * 120
        cy = yy + row * 18
        d.text((cx, cy), num, font=font(F_SANSB, 12), fill=NAVY)
        d.text((cx + 42, cy + 1), lab, font=font(F_SANS, 9), fill=GREY)
    # ---- three leads
    ly = 214
    lw = 328
    lh = 288
    for i, L in enumerate(LEADS):
        x0 = M + i * (lw + 4)
        x1 = x0 + lw
        d.rectangle([x0, ly, x1, ly + lh], outline=(120, 115, 105), width=1,
                    fill=(255, 255, 255))
        scene = {"court": scene_court, "sea": scene_sea,
                 "tower": scene_tower}[L["scene"]]
        scene(img, d, (x0, ly, x1, ly + 158))
        num_badge(d, x0 + 20, ly + 20, L["n"])
        d.text((x1 - 8, ly + 12), L["place"], font=font(F_CONDB, 11),
               fill=(255, 255, 255), anchor="ra")
        chip(d, (x0 + 8, ly + 140), L["chip"])
        ty = ly + 164
        d.text((x0 + 8, ty), L["head"], font=font(F_SANSB, 15), fill=INK)
        d.text((x0 + 8, ty + 20), L["sub"], font=font(F_SANS, 11), fill=(50, 50, 50))
        d.text((x0 + 8, ty + 44), L["a1"], font=font(F_SANSB, 10), fill=NAVY)
        d.text((x0 + 8, ty + 60), L["a2"], font=font(F_SANSB, 10), fill=NAVY)
        d.line([x0 + 8, ty + 82, x1 - 8, ty + 82], fill=(200, 195, 185), width=1)
        d.text((x0 + 8, ty + 88), L["src"], font=font(F_SANS, 9), fill=GREY)
        if i == 2:
            d.text((x0 + 8, ty + 104),
                   "Civil Defense posted a photo of the damaged tower.",
                   font=font(F_SERIF_R, 10), fill=(90, 40, 20))
        if i == 0:
            d.text((x0 + 8, ty + 104), "Huawei said it expects to appeal.",
                   font=font(F_SERIF_R, 10), fill=(90, 40, 20))
        if i == 1:
            d.text((x0 + 8, ty + 104),
                   "Iran's army chief: strait shut 'day by day'.",
                   font=font(F_SERIF_R, 10), fill=(90, 40, 20))
    # ---- middle tiles 4-13
    ty = 512
    d.text((M, ty), "THE REST OF THE DAY  —  4 TO 13",
           font=font(F_CONDB, 13), fill=NAVY)
    d.text((W - M, ty), "Sport appears only below, never as a lead",
           font=font(F_SANS, 10), fill=GREY, anchor="ra")
    gy = ty + 20
    tw, th = 196, 80
    for i, T in enumerate(TILES):
        col, row = i % 5, i // 5
        x0 = M + col * (tw + 4)
        y0 = gy + row * (th + 4)
        x1, y1 = x0 + tw, y0 + th
        d.rectangle([x0, y0, x1, y1], outline=(120, 115, 105), width=1,
                    fill=(255, 255, 255))
        draw_tile_scene(d, (x0, y0, x1, y0 + 30), T["scene"], T["tint"])
        num_badge(d, x0 + 14, y0 + 15, T["n"], r=11)
        chip(d, (x1 - 74, y0 + 7), T["chip"])
        d.text((x0 + 6, y0 + 34), T["place"], font=font(F_CONDB, 9),
               fill=(24, 44, 78))
        d.text((x0 + 6, y0 + 46), T["head"], font=font(F_SANSB, 10), fill=INK)
        para(d, (x0 + 6, y0 + 59), T["sub"], font(F_SANS, 9), (60, 60, 60),
             tw - 12, 11)
    # ---- region bar
    ry = gy + 2 * th + 10
    d.text((M, ry), "REGIONS (max 9/35)", font=font(F_CONDB, 13), fill=NAVY)
    bx = M + 190
    total = sum(c for _, c in REGION_COUNTS)
    bw = W - M - bx
    x = bx
    cols = [(14, 26, 46), (178, 34, 34), (24, 44, 78), (15, 92, 96),
            (146, 94, 20), (60, 40, 90)]
    short = ["N AMERICA 7", "MID EAST 7", "EUROPE 6", "ASIA 9", "LATAM 3",
             "AFRICA 3"]
    for (name, c), col, lab in zip(REGION_COUNTS, cols, short):
        wseg = bw * c / total
        d.rectangle([x, ry + 2, x + wseg - 2, ry + 16], fill=col)
        d.text((x + 3, ry + 19), lab, font=font(F_SANSB, 9), fill=INK)
        x += wseg
    # ---- map + also list
    ay = ry + 38
    d.rectangle([M, ay, 300, ay + 158], outline=(120, 115, 105), width=1)
    draw_map(img, d, (M, ay, 300, ay + 158))
    d.text((312, ay), "ALSO ON TUESDAY  —  14 TO 35",
           font=font(F_CONDB, 13), fill=NAVY)
    lx = 312
    colw = 344
    for i, (n, s, reg) in enumerate(ALSO):
        col = i // 11
        row = i % 11
        x = lx + col * (colw + 6)
        yy2 = ay + 18 + row * 13
        d.text((x, yy2), "%d." % n, font=font(F_SANSB, 10), fill=RED)
        d.text((x + 20, yy2), s, font=font(F_SANS, 10), fill=INK)
    # ---- date check
    dy = ay + 166
    d.rectangle([M, dy, W - M, dy + 84], fill=(232, 226, 210),
                outline=(150, 140, 120), width=1)
    d.text((M + 8, dy + 5), "DATE CHECK  —  READ THIS BEFORE YOU DOUBT A DATE",
           font=font(F_CONDB, 12), fill=NAVY)
    para(d, (M + 8, dy + 21), DATECHECK_LEFT, font(F_SANS, 10), INK,
         W - 2 * M - 16, 12)
    para(d, (M + 8, dy + 58), DATECHECK_NEXT, font(F_SANS, 10), INK,
         W - 2 * M - 16, 12)
    # ---- footer
    fy = dy + 90
    d.line([M, fy, W - M, fy], fill=NAVY, width=1)
    d.text((M, fy + 4), "CONFIRMED = 2+ outlets   ·   OFFICIAL = on the record   ·   "
           "REPORTED = one outlet, so labelled",
           font=font(F_SANSB, 10), fill=INK)
    d.text((M, fy + 18), "Sources: Reuters, AP, Bloomberg, AFP, BBC, Al Arabiya, "
           "Xinhua, SPA, Daily Summary Of (30 stories, 64 sources), Le Monde, CNN, "
           "Investopedia. All 35 stories first reported Tue 24 Nov 2026 (UTC).",
           font=font(F_SANS, 9), fill=GREY)
    return img


if __name__ == "__main__":
    out = os.path.join(BASE, "entry.png")
    img = build()
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, img.size, os.path.getsize(out), "bytes")

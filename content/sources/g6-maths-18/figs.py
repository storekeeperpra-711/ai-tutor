"""Pictures for the chapter 9 practice lessons (Symmetry): parallel lines with
a transversal, flat shapes, block letters, solids in a simple 3-D view, and
squared grids with a mirror line or a centre of turning. Everything is worked
out here (turns and flips with complex numbers, angles with math.cos/sin) so
the picture always matches the numbers, and the counts of mirror lines and
the orders of turning symmetry are checked by really flipping and turning.

Screen coordinates: x goes right and y goes DOWN, so a clockwise turn on the
screen is a positive angle. Coordinates are rounded to 1 decimal."""
import cmath
import math

from common import T

FULL = 360


def r1(v):
    return round(v + 0.0, 1) + 0.0


def xy(p):
    return (p.real, p.imag) if isinstance(p, complex) else (p[0], p[1])


def pt(p):
    x, y = xy(p)
    return [r1(x), r1(y)]


def seg(a, b, dashed=False):
    item = {"kind": "line", "from": pt(a), "to": pt(b)}
    if dashed:
        item["style"] = "dashed"
    return item


def poly(points, fill=False, dashed=False):
    item = {"kind": "polygon", "points": [pt(p) for p in points]}
    if fill:
        item["fill"] = True
    if dashed:
        item["style"] = "dashed"
    return item


def label(at, text):
    return {"kind": "label", "at": pt(at), "text": text}


def dot(at):
    return {"kind": "point", "at": pt(at)}


def circ(c, radius, fill=False):
    item = {"kind": "circle", "center": pt(c), "radius": r1(radius)}
    if fill:
        item["fill"] = True
    return item


def fig(w, h, en, ur, items):
    """A figure block; checks that everything is inside the box and labels keep 2.5% from the edge."""
    margin = 0.025 * max(w, h)
    for it in items:
        reach = it.get("radius", 0)
        pts = [*it.get("points", []), *(it[k] for k in ("from", "to", "center", "at") if k in it)]
        for x, y in pts:
            assert reach <= x <= w - reach and reach <= y <= h - reach, (en, it)
            if it["kind"] == "label":
                assert margin <= x <= w - margin and margin <= y <= h - margin, (en, it)
    return {"width": w, "height": h, "alt": T(en, ur), "items": items}


def with_fig(step, figure):
    step["figure"] = figure
    return step


# ---------- turning and flipping ----------

def polar(c, radius, deg):
    """A point `radius` from c, `deg` degrees clockwise on screen from +x."""
    return c + radius * cmath.exp(1j * math.radians(deg))


def regular(n, c, radius, start=-90):
    return [polar(c, radius, start + k * FULL / n) for k in range(n)]


def turn(z, c, deg):
    """Turn z about c by deg degrees clockwise on screen."""
    return c + (z - c) * cmath.exp(1j * math.radians(deg))


def mirror(z, c, deg):
    """Reflect z in the line through c at angle deg."""
    return c + cmath.exp(2j * math.radians(deg)) * (z - c).conjugate()


def key(z):
    return (round(z.real, 3) + 0.0, round(z.imag, 3) + 0.0)


def shape_key(pieces):
    return frozenset(frozenset(key(z) for z in p) for p in pieces)


def order(pieces, c):
    """How many turns (whole degrees, up to a full turn) fit the drawing onto itself."""
    start = shape_key(pieces)
    return sum(shape_key([[turn(z, c, d) for z in p] for p in pieces]) == start
               for d in range(1, FULL + 1))


def lines(pieces, c):
    """How many mirror lines through c (every half degree) fit the drawing onto itself."""
    start = shape_key(pieces)
    return sum(shape_key([[mirror(z, c, d / 2) for z in p] for p in pieces]) == start
               for d in range(0, 360))


def closed_pieces(points):
    """A closed shape as pieces (its sides, each a pair of corners)."""
    return [[points[i], points[(i + 1) % len(points)]] for i in range(len(points))]


def stroke_items(pieces, dashed=False):
    return [seg(a, b, dashed) for a, b in pieces]


def mirror_line(c, deg, half):
    d = cmath.exp(1j * math.radians(deg))
    return seg(c - half * d, c + half * d, dashed=True)


C = complex(50, 32)

# Block capital letters as strokes in a box 20 wide and 28 tall, centred on c.
LETTER_PATHS = {
    "H": [[(-10, -14), (-10, 14)], [(10, -14), (10, 14)], [(-10, 0), (10, 0)]],
    "A": [[(-10, 14), (0, -14), (10, 14)], [(-5, 2), (5, 2)]],
    "T": [[(-10, -14), (10, -14)], [(0, -14), (0, 14)]],
    "M": [[(-10, 14), (-10, -14), (0, 2), (10, -14), (10, 14)]],
    "N": [[(-10, 14), (-10, -14), (10, 14), (10, -14)]],
    "Z": [[(-10, -14), (10, -14), (-10, 14), (10, 14)]],
    "E": [[(10, -14), (-10, -14), (-10, 14), (10, 14)], [(-10, 0), (6, 0)]],
    "S": [[(10, -14), (-10, -14), (-10, 0), (10, 0), (10, 14), (-10, 14)]],
    "X": [[(-10, -14), (10, 14)], [(10, -14), (-10, 14)]],
    "F": [[(10, -14), (-10, -14), (-10, 14)], [(-10, 0), (6, 0)]],
}


def letter_pieces(name, c=0j, s=1.0):
    out = []
    for path in LETTER_PATHS[name]:
        pts = [c + complex(x * s, y * s) for x, y in path]
        out += [[pts[i], pts[i + 1]] for i in range(len(pts) - 1)]
    return out


def letter_items(name, c, s=1.0):
    return stroke_items(letter_pieces(name, c, s))


def letter_symmetry(name):
    """(lines of symmetry, order of rotational symmetry) of a block letter."""
    c = 0j
    return lines(letter_pieces(name), c), order(letter_pieces(name), c)


# ---------- solids in a simple view ----------

def ellipse_pts(c, rx, ry, a0=0, a1=360, n=24):
    return [c + complex(rx * math.cos(math.radians(a0 + (a1 - a0) * k / n)),
                        ry * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]


def path_items(points, dashed=False):
    return [seg(points[i], points[i + 1], dashed) for i in range(len(points) - 1)]


def cylinder(c, rx=20, ry=6, h=44):
    """Top ellipse, front half of the bottom edge (solid), back half (dashed), two sides."""
    top, bot = c - complex(0, h / 2), c + complex(0, h / 2)
    return ([poly(ellipse_pts(top, rx, ry)[:-1])]
            + path_items(ellipse_pts(bot, rx, ry, 0, 180, 12))
            + path_items(ellipse_pts(bot, rx, ry, 180, 360, 12), dashed=True)
            + [seg(top - rx, bot - rx), seg(top + rx, bot + rx)])


def cone(c, rx=20, ry=6, h=48):
    apex, base = c - complex(0, h / 2), c + complex(0, h / 2)
    return (path_items(ellipse_pts(base, rx, ry, 0, 180, 12))
            + path_items(ellipse_pts(base, rx, ry, 180, 360, 12), dashed=True)
            + [seg(apex, base - rx), seg(apex, base + rx)])


def sphere(c, radius=24):
    return [circ(c, radius)] + path_items(ellipse_pts(c, radius, radius * 0.28, 0, 180, 12)) \
        + path_items(ellipse_pts(c, radius, radius * 0.28, 180, 360, 12), dashed=True)


def hemisphere(c, radius=24):
    """A bowl standing on its round side: flat circle face on top, curved below."""
    return (path_items(ellipse_pts(c, radius, radius * 0.28))
            + path_items(ellipse_pts(c, radius, radius, 0, 180, 18)))


def cuboid(front_tl, w, h, depth=(10, -7)):
    """Oblique cuboid: front rectangle with its top-left corner at front_tl; the back goes up and right."""
    a = front_tl
    b, d = a + w, a + complex(0, h)
    c = a + complex(w, h)
    o = complex(*depth)
    items = [poly([a, b, c, d]), seg(a, a + o), seg(b, b + o), seg(c, c + o),
             seg(a + o, b + o), seg(b + o, c + o),
             seg(d, d + o, dashed=True), seg(d + o, c + o, dashed=True), seg(a + o, d + o, dashed=True)]
    return items


# ---------- squared grids ----------

class Grid:
    """A squared grid of cols x rows squares, each u wide, with pad around it.
    g.at(col, row) is the pixel of a grid corner (row counts down from the top)."""

    def __init__(self, cols, rows, u=10, pad=8):
        self.cols, self.rows, self.u, self.pad = cols, rows, u, pad
        self.w, self.h = cols * u + 2 * pad, rows * u + 2 * pad

    def at(self, col, row):
        return complex(self.pad + col * self.u, self.pad + row * self.u)

    def lines(self):
        items = [seg(self.at(c, 0), self.at(c, self.rows)) for c in range(self.cols + 1)]
        return items + [seg(self.at(0, r), self.at(self.cols, r)) for r in range(self.rows + 1)]

    def vmirror(self, col):
        return seg(self.at(col, -0.6), self.at(col, self.rows + 0.6), dashed=True)

    def hmirror(self, row):
        return seg(self.at(-0.6, row), self.at(self.cols + 0.6, row), dashed=True)

    def shape(self, cells, fill=True):
        return poly([self.at(c, r) for c, r in cells], fill=fill)

    def figure(self, en, ur, items):
        return fig(self.w, self.h, en, ur, self.lines() + items)


def reflect_cells(cells, axis, value):
    """Reflect grid points in the vertical line col = value ('v') or the horizontal line row = value ('h')."""
    if axis == "v":
        return [(2 * value - c, r) for c, r in cells]
    return [(c, 2 * value - r) for c, r in cells]


def turn_cells(cells, centre, quarter_turns):
    """Turn grid points about centre by quarter_turns x 90 degrees clockwise on screen."""
    cc = complex(*centre)
    out = []
    for c, r in cells:
        z = turn(complex(c, r), cc, 90 * quarter_turns)
        out.append((round(z.real), round(z.imag)))
        assert abs(z.real - out[-1][0]) < 1e-9 and abs(z.imag - out[-1][1]) < 1e-9
    return out


# ---------- parallel lines cut by a transversal ----------

LINE = 180
W, H = 120, 80
Y = {"l": 22, "m": 56}
MID_X = 60          # the transversal crosses half-way between l and m here
REACH = 16          # how far the transversal goes past each line
ARC_R = 7
LABEL_R = 16


def corner_size(theta, corner):
    return theta if corner in ("tr", "bl") else LINE - theta


def corner_arc(theta, corner):
    """(start, sweep) of the angle in this corner."""
    return {"tr": (360 - theta, theta),
            "tl": (180, 180 - theta),
            "bl": (180 - theta, theta),
            "br": (0, 180 - theta)}[corner]




def crossing(theta, line):
    """Where the transversal meets line l or m."""
    y = Y[line]
    mid_y = (Y["l"] + Y["m"]) / 2
    # Going up the transversal (y smaller) moves x by +1/tan(theta) per unit.
    x = MID_X + (mid_y - y) / math.tan(math.radians(theta))
    return [r1(x), y]


CORNER_EN = {"tr": "above line {L}, right of the transversal",
             "tl": "above line {L}, left of the transversal",
             "bl": "below line {L}, left of the transversal",
             "br": "below line {L}, right of the transversal"}
CORNER_UR = {"tr": "لکیر {L} کے اوپر، قاطع کے دائیں",
             "tl": "لکیر {L} کے اوپر، قاطع کے بائیں",
             "bl": "لکیر {L} کے نیچے، قاطع کے بائیں",
             "br": "لکیر {L} کے نیچے، قاطع کے دائیں"}


TILT = 12
TILT_SLOPE = math.tan(math.radians(TILT))


def transversal_figure(theta, marks, parallel=True):
    """marks: list of (line, corner, label). Draws an arc and a label in
    each marked corner."""
    assert 40 <= theta <= 140
    items = []
    for name in ("l", "m"):
        y = Y[name]
        if not parallel and name == "m":
            # tilt m about its crossing point so the two lines clearly meet
            cx = crossing(theta, "m")[0]
            dy = TILT_SLOPE * (W - 4 - cx), TILT_SLOPE * (cx - 4)
            items.append({"kind": "line", "from": [4, r1(y + dy[1])], "to": [W - 4, r1(y - dy[0])]})
        else:
            items.append({"kind": "line", "from": [4, y], "to": [W - 4, y]})
        if parallel:
            # a small arrow head on each line: the usual mark for parallel lines
            items.append({"kind": "line", "from": [16, y - 3], "to": [20, y]})
            items.append({"kind": "line", "from": [16, y + 3], "to": [20, y]})
        items.append({"kind": "label", "at": [W - 8, y - 6], "text": name})
    t = math.radians(theta)
    top, bottom = crossing(theta, "l"), crossing(theta, "m")
    up = [r1(top[0] + REACH / math.tan(t)), Y["l"] - REACH]
    down = [r1(bottom[0] - REACH / math.tan(t)), Y["m"] + REACH]
    items.append({"kind": "line", "from": down, "to": up})
    items += [{"kind": "point", "at": top}, {"kind": "point", "at": bottom}]
    en_parts, ur_parts = [], []
    for line, corner, text in marks:
        c = crossing(theta, line)
        start, sweep = corner_arc(theta, corner)
        assert sweep == corner_size(theta, corner)
        if not parallel and line == "m":
            # m is tilted up to the right by TILT degrees: corners above it shrink
            assert corner == "tr"
            sweep -= TILT
        items.append({"kind": "arc", "center": c, "radius": ARC_R, "start": start % 360, "sweep": sweep})
        mid = math.radians(start + sweep / 2)
        at = [r1(c[0] + LABEL_R * math.cos(mid)), r1(c[1] + LABEL_R * math.sin(mid))]
        assert 4 <= at[0] <= W - 4 and 4 <= at[1] <= H - 4, at
        items.append({"kind": "label", "at": at, "text": text})
        en_parts.append(f"angle {text} is {CORNER_EN[corner].format(L=line)}")
        ur_parts.append(f"زاویہ {text} {CORNER_UR[corner].format(L=line)} ہے")
    for it in items:
        for k in ("from", "to", "at", "center"):
            if k in it:
                x, y = it[k]
                rr = it.get("radius", 0)
                assert rr <= x <= W - rr and rr <= y <= H - rr, it
    if parallel:
        en = "Two parallel lines, l on top and m below, are crossed by a slanting line (the transversal)."
        ur = "دو متوازی لکیریں، اوپر l اور نیچے m، ایک ترچھی لکیر (قاطع) سے کٹتی ہیں۔"
    else:
        en = "Two lines l and m that are not parallel are crossed by a slanting line."
        ur = "دو لکیریں l اور m جو متوازی نہیں، ایک ترچھی لکیر سے کٹتی ہیں۔"
    if en_parts:
        en += " Marked: " + "; ".join(en_parts) + "."
        ur += " نشان لگے ہیں: " + "؛ ".join(ur_parts) + "۔"
    return {"width": W, "height": H, "alt": T(en, ur), "items": items}


def angle_figure(theta, given_line, given_corner, given, unknown_line, unknown_corner, letter):
    assert corner_size(theta, given_corner) == given
    return transversal_figure(theta, [(given_line, given_corner, f"{given}°"),
                                      (unknown_line, unknown_corner, letter)])


def theta_for(corner, size):
    """The drawing angle THETA that makes this corner the stated size."""
    th = size if corner in ("tr", "bl") else LINE - size
    assert corner_size(th, corner) == size
    return th



def theta_for(corner, size):
    """The drawing angle THETA that makes this corner the stated size."""
    th = size if corner in ("tr", "bl") else LINE - size
    assert corner_size(th, corner) == size
    return th

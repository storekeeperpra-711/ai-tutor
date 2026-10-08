"""Pictures for the Solids unit: boxes (cubes and cuboids) drawn in a simple
3-D (oblique) view, boxes filled with unit cubes, and nets laid flat, built
as lesson "figure" blocks.

The oblique view: the front face is drawn as it is (a rectangle), and the
depth goes back up and to the right at 30 degrees, drawn half as long, so
the top and the right side show as shaded parallelograms. The three edges
that meet at the hidden back-bottom-left corner are dashed.

Every figure is W wide, close to the size the app paints it on a phone,
so the 16 px labels keep their room. Coordinates are rounded to 1 decimal.
"""
import math

from common import T

W = 300
PAD = 8            # room round the drawing (labels keep 2.5% of the box)
CHAR = 9.6         # a label letter is about this wide
TALL = 16          # and this tall
MAX_ITEMS = 60
DX = 0.5 * math.cos(math.radians(30))   # one unit of depth goes this far right
DY = 0.5 * math.sin(math.radians(30))   # and this far up


def r1(v):
    return round(v + 0.0, 1)


def pt(x, y):
    return [r1(x), r1(y)]


def line(a, b, dashed=False):
    item = {"kind": "line", "from": pt(*a), "to": pt(*b)}
    if dashed:
        item["style"] = "dashed"
    return item


def poly(points, fill=False, dashed=False):
    item = {"kind": "polygon", "points": [pt(*p) for p in points]}
    if fill:
        item["fill"] = True
    if dashed:
        item["style"] = "dashed"
    return item


def label(at, text):
    return {"kind": "label", "at": pt(*at), "text": text}


def point(at):
    return {"kind": "point", "at": pt(*at)}


def circle(center, radius, fill=False):
    item = {"kind": "circle", "center": pt(*center), "radius": r1(radius)}
    if fill:
        item["fill"] = True
    return item


def cm(n):
    return f"{n}cm"


def label_box(text):
    return len(text) * CHAR / 2, TALL / 2


# ---------- moving and placing groups of items ----------

def extent(items):
    """The smallest box round all the items, letters of the labels included."""
    xs, ys = [], []
    for it in items:
        if it["kind"] == "label":
            hw, hh = label_box(it["text"])
            x, y = it["at"]
            xs += [x - hw, x + hw]
            ys += [y - hh, y + hh]
        elif it["kind"] == "circle":
            (x, y), rr = it["center"], it["radius"]
            xs += [x - rr, x + rr]
            ys += [y - rr, y + rr]
        else:
            for p in [*it.get("points", []), *(it[k] for k in ("from", "to", "at") if k in it)]:
                xs.append(p[0])
                ys.append(p[1])
    return min(xs), min(ys), max(xs), max(ys)


def shift(items, dx, dy):
    out = []
    for it in items:
        it = dict(it)
        if "points" in it:
            it["points"] = [pt(x + dx, y + dy) for x, y in it["points"]]
        for k in ("from", "to", "at", "center"):
            if k in it:
                it[k] = pt(it[k][0] + dx, it[k][1] + dy)
        out.append(it)
    return out


def row(groups, gap=24, bottom=True):
    """Groups side by side, gap apart, standing on one base line."""
    out, x = [], 0
    boxes = [extent(g) for g in groups]
    base = max(b[3] for b in boxes)
    for g, (x0, y0, x1, y1) in zip(groups, boxes):
        out += shift(g, x - x0, (base - y1) if bottom else -y0)
        x += x1 - x0 + gap
    return out


def figure(alt_en, alt_ur, items):
    """Centre the items in a box W wide (as tall as they need)."""
    assert len(items) <= MAX_ITEMS, (alt_en, len(items))
    x0, y0, x1, y1 = extent(items)
    assert x1 - x0 <= W - 2 * PAD, (alt_en, x1 - x0)
    height = y1 - y0 + 2 * PAD
    items = shift(items, (W - (x1 - x0)) / 2 - x0, PAD - y0)
    for it in items:
        if it["kind"] == "label":
            hw, hh = label_box(it["text"])
            x, y = it["at"]
            assert x - hw >= 0 and x + hw <= W and y - hh >= 0 and y + hh <= height, it
    return {"width": W, "height": r1(height), "alt": T(alt_en, alt_ur), "items": items}


# ---------- a box in 3-D ----------

class Box:
    """A cuboid `length` long (left to right), `depth` wide (going back) and
    `height` high, drawn s units per cm. The front-bottom-left corner is at
    (0, 0); y goes down on the screen, so up is negative."""

    def __init__(self, length, depth, height, s):
        self.l, self.d, self.h, self.s = length, depth, height, s

    def p(self, i, j, k):
        """The screen point i along, j back and k up."""
        s = self.s
        return (s * (i + DX * j), -s * (k + DY * j))

    def faces(self, open_top=False):
        l, d, h, p = self.l, self.d, self.h, self.p
        front = [p(0, 0, 0), p(l, 0, 0), p(l, 0, h), p(0, 0, h)]
        top = [p(0, 0, h), p(l, 0, h), p(l, d, h), p(0, d, h)]
        side = [p(l, 0, 0), p(l, d, 0), p(l, d, h), p(l, 0, h)]
        return [poly(front), poly(top, fill=not open_top), poly(side, fill=True)]

    def hidden(self):
        l, d, h, p = self.l, self.d, self.h, self.p
        back = p(0, d, 0)
        return [line(back, p(0, 0, 0), True), line(back, p(l, d, 0), True), line(back, p(0, d, h), True)]

    def grid(self, cell=1, faces="fts"):
        """Lines that split the visible faces into cell × cell squares."""
        l, d, h, p = self.l, self.d, self.h, self.p
        steps = lambda n: [cell * m for m in range(1, round(n / cell))]
        items = []
        if "f" in faces:
            items += [line(p(i, 0, 0), p(i, 0, h)) for i in steps(l)]
            items += [line(p(0, 0, k), p(l, 0, k)) for k in steps(h)]
        if "t" in faces:
            items += [line(p(i, 0, h), p(i, d, h)) for i in steps(l)]
            items += [line(p(0, j, h), p(l, j, h)) for j in steps(d)]
        if "s" in faces:
            items += [line(p(l, j, 0), p(l, j, h)) for j in steps(d)]
            items += [line(p(l, 0, k), p(l, d, k)) for k in steps(h)]
        return items

    def labels(self, lt=None, dt=None, ht=None):
        """Length under the front, height left of it, depth beside the
        bottom edge of the right side."""
        l, d, h, p = self.l, self.d, self.h, self.p
        items = []
        if lt:
            a, b = p(0, 0, 0), p(l, 0, 0)
            items.append(label(((a[0] + b[0]) / 2, a[1] + 4 + TALL / 2), lt))
        if ht:
            a, b = p(0, 0, 0), p(0, 0, h)
            items.append(label((a[0] - 5 - label_box(ht)[0], (a[1] + b[1]) / 2), ht))
        if dt:
            a, b = p(l, 0, 0), p(l, d, 0)
            nx, ny = 0.5, math.sqrt(3) / 2      # out from the edge, down and right
            off = 3 + nx * label_box(dt)[0] + ny * label_box(dt)[1]
            items.append(label(((a[0] + b[0]) / 2 + nx * off, (a[1] + b[1]) / 2 + ny * off), dt))
        return items

    def open_inside(self):
        """For a box with no lid: the inside back-left corner, seen through
        the open top down to the front edge."""
        l, d, h, p = self.l, self.d, self.h, self.p
        a = p(0, d, h)
        # The inside corner runs straight down from a until the front top edge hides it.
        return [line(a, (a[0], p(0, 0, h)[1]))]

    def corners(self):
        l, d, h, p = self.l, self.d, self.h, self.p
        return [point(p(i, j, k)) for i in (0, l) for j in (0, d) for k in (0, h)]


def fit(length, depth, height, max_w=220, max_h=130, max_s=None):
    """Units per cm so the box (without labels) fits max_w by max_h."""
    s = min(max_w / (length + DX * depth), max_h / (height + DY * depth))
    return min(s, max_s) if max_s else s


def box_items(length, depth, height, *, labels=True, grid=None, hidden=True, max_w=220, max_h=130, max_s=None,
              open_top=False, texts=None):
    """A labelled box. grid: cell size (in cm) of the unit cubes drawn on its faces."""
    b = Box(length, depth, height, fit(length, depth, height, max_w, max_h, max_s))
    items = b.faces(open_top=open_top)
    if grid:
        items += b.grid(grid)
    if open_top:
        items += b.open_inside()
    if hidden and not open_top:
        items += b.hidden()
    elif hidden:
        items += b.hidden()[:2]  # the back-bottom edges; the back-left edge is seen through the top
    if labels:
        lt, dt, ht = texts or (cm(length), cm(depth), cm(height))
        items += b.labels(lt, dt, ht)
    return items, b


def water(b, frac=0.75):
    """Water in a tank up to frac of its height, seen through the front."""
    w = b.h * frac
    return poly([b.p(0, 0, 0), b.p(b.l, 0, 0), b.p(b.l, 0, w), b.p(0, 0, w)], fill=True)


# ---------- alt text ----------

def box_alt(length, depth, height, what_en="A box", what_ur="ایک ڈبہ", grid=None, extra_en="", extra_ur=""):
    en = (f"{what_en} drawn in 3-D, {length} cm long, {depth} cm wide and {height} cm high; "
          f"the three lengths are labelled on its edges. The front is a rectangle, the top and the right side are shaded, "
          f"and the hidden edges at the back are dashed.")
    ur = (f"{what_ur} تین رخی (3-D) شکل میں، {length} سینٹی میٹر لمبا، {depth} سینٹی میٹر چوڑا اور {height} سینٹی میٹر اونچا؛ "
          f"تینوں لمبائیاں کناروں پر لکھی ہیں۔ سامنے کا رخ مستطیل ہے، اوپر اور دائیں رخ پر رنگ ہے، "
          f"اور پیچھے کے چھپے ہوئے کنارے ڈیش والی لکیروں سے دکھائے گئے ہیں۔")
    if grid:
        en += f" Its faces are split into {grid} cm squares, showing the {grid} cm cubes that fill it."
        ur += f" اس کی سطحوں پر {grid} سینٹی میٹر کے خانے بنے ہیں، جو اسے بھرنے والے {grid} سینٹی میٹر کے مکعب دکھاتے ہیں۔"
    if extra_en:
        en += " " + extra_en
        ur += " " + extra_ur
    return en, ur


def cube_alt(side, what_en="A cube", what_ur="ایک مکعب", grid=None, extra_en="", extra_ur=""):
    en = (f"{what_en} drawn in 3-D with all its sides {side} cm long; its length, width and height are each labelled {side} cm. "
          f"The front is a square, the top and the right side are shaded, and the hidden edges at the back are dashed.")
    ur = (f"{what_ur} تین رخی (3-D) شکل میں، جس کا ہر ضلع {side} سینٹی میٹر ہے؛ لمبائی، چوڑائی اور اونچائی تینوں پر {side} سینٹی میٹر لکھا ہے۔ "
          f"سامنے کا رخ مربع ہے، اوپر اور دائیں رخ پر رنگ ہے، اور پیچھے کے چھپے ہوئے کنارے ڈیش والی لکیروں سے دکھائے گئے ہیں۔")
    if grid:
        en += f" Its faces are split into 1 cm squares: {side} rows of {side} on each face."
        ur += f" اس کی سطحوں پر 1 سینٹی میٹر کے خانے بنے ہیں: ہر سطح پر {side} کی {side} قطاریں۔"
    if extra_en:
        en += " " + extra_en
        ur += " " + extra_ur
    return en, ur


def box_fig(length, depth, height, what_en="A box", what_ur="ایک ڈبہ", grid=None, **kw):
    items, _ = box_items(length, depth, height, grid=grid, **kw)
    return figure(*box_alt(length, depth, height, what_en, what_ur, grid), items)


def cube_fig(side, what_en="A cube", what_ur="ایک مکعب", grid=None, **kw):
    items, _ = box_items(side, side, side, grid=grid, **kw)
    return figure(*cube_alt(side, what_en, what_ur, grid), items)


# ---------- nets ----------

def net_items(length, width, height, s, texts=None, cell=None):
    """The net of a length × width × height box laid flat: a row of four
    faces (side, front, side, back), with the top above the front and the
    bottom below it. texts: what to write in the l×w, l×h and w×h faces.
    The top and bottom are shaded. cell: draw unit squares on every face."""
    l, w, h = length * s, width * s, height * s
    xs = [0, w, w + l, 2 * w + l]
    widths = [w, l, w, l]
    faces = [((xs[i], w), widths[i], h, "lh" if widths[i] == l else "wh") for i in range(4)]
    faces += [((w, 0), l, w, "lw"), ((w, w + h), l, w, "lw")]
    items, inside = [], []
    for (x, y), fw, fh, kind in faces:
        items.append(poly([(x, y), (x + fw, y), (x + fw, y + fh), (x, y + fh)], fill=(kind == "lw")))
        if cell:
            c = cell * s
            n_x, n_y = round(fw / c), round(fh / c)
            inside += [line((x + c * m, y), (x + c * m, y + fh)) for m in range(1, n_x)]
            inside += [line((x, y + c * m), (x + fw, y + c * m)) for m in range(1, n_y)]
        if texts and texts.get(kind):
            inside.append(label((x + fw / 2, y + fh / 2), texts[kind]))
    return items + inside


# ---------- the steps ----------

def with_figures(lesson, figures):
    """Attach each figure to the step with that id (main steps, question
    bank and review), and check every figure found its step."""
    used = set()
    steps = list(lesson["steps"])
    steps += [q["step"] for qs in lesson["question_bank"].values() for q in qs]
    steps += [q["step"] for q in lesson.get("review_questions", [])]
    for step in steps:
        if step["id"] in figures:
            assert step["type"] != "sim", step["id"]
            step["figure"] = figures[step["id"]]
            used.add(step["id"])
    assert used == set(figures), set(figures) - used
    return lesson

"""Pictures for the Sets unit: ovals holding the elements of a set, letter
tiles for the letters of a word, number lines and number grids, boxes for
subsets, and Venn diagrams (two overlapping circles, the overlap or the
union shaded, a rectangle for U) built as lesson "figure" blocks.

Every figure is drawn in a box 300 wide, close to the size the app paints
it on a phone, so the 16 px labels keep their room. Coordinates are
rounded to 1 decimal place. Labels are numbers, single letters or short
sets like {a, b}; the alt text names what each letter stands for.
`figure` checks that no two labels overlap and that every label keeps
clear of the edge.
"""
import math

from common import T

W = 300
MAX_ITEMS = 60
CHAR = 9.6         # about how wide one label character is
LABEL_H = 16       # about how tall a label is
EDGE = 0.025 * W   # labels keep this far from the edge (the validator's rule)


def r1(v):
    return round(v + 0.0, 1)


def pt(x, y):
    return [r1(x), r1(y)]


def line(a, b, dashed=False):
    item = {"kind": "line", "from": pt(*a), "to": pt(*b)}
    if dashed:
        item["style"] = "dashed"
    return item


def label(at, text):
    text = str(text)
    assert 1 <= len(text) <= 6, text
    return {"kind": "label", "at": pt(*at), "text": text}


def point(at):
    return {"kind": "point", "at": pt(*at)}


def arc(center, radius, start, sweep):
    return {"kind": "arc", "center": pt(*center), "radius": r1(radius), "start": start, "sweep": sweep}


def poly(points, fill=False, dashed=False):
    item = {"kind": "polygon", "points": [pt(*p) for p in points]}
    if fill:
        item["fill"] = True
    if dashed:
        item["style"] = "dashed"
    return item


def rect(x0, y0, x1, y1, fill=False, dashed=False):
    return poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill, dashed)


def circle(center, radius, fill=False, dashed=False):
    item = {"kind": "circle", "center": pt(*center), "radius": r1(radius)}
    if fill:
        item["fill"] = True
    if dashed:
        item["style"] = "dashed"
    return item


def width_of(text):
    return len(str(text).replace(" ", "")) * CHAR + str(text).count(" ") * 4


def check_labels(items, width, height):
    """No two labels overlap, and each keeps clear of the edge."""
    boxes = []
    for it in items:
        if it["kind"] != "label":
            continue
        x, y = it["at"]
        w = width_of(it["text"])
        margin = 0.025 * max(width, height)
        assert margin <= x - w / 2 + 2 and x + w / 2 - 2 <= width - margin, ("label off the side", it["text"], x)
        assert margin <= y and y <= height - margin, ("label off the top or bottom", it["text"], y)
        boxes.append((x - w / 2, y - LABEL_H / 2, x + w / 2, y + LABEL_H / 2, it["text"]))
    for i, a in enumerate(boxes):
        for b in boxes[i + 1:]:
            apart = a[2] <= b[0] + 1 or b[2] <= a[0] + 1 or a[3] <= b[1] + 1 or b[3] <= a[1] + 1
            assert apart, ("labels overlap", a[4], b[4])


def figure(width, height, alt_en, alt_ur, items):
    assert len(items) <= MAX_ITEMS, (alt_en, len(items))
    check_labels(items, width, height)
    return {"width": r1(width), "height": r1(height), "alt": T(alt_en, alt_ur), "items": items}


def attach(lesson, figures):
    """Put each figure on the step with that id (main steps, question bank
    and review questions); every id must exist."""
    steps = list(lesson["steps"])
    steps += [q["step"] for qs in lesson["question_bank"].values() for q in qs]
    steps += [q["step"] for q in lesson.get("review_questions", [])]
    by_id = {s["id"]: s for s in steps}
    for sid, fig in figures.items():
        assert sid in by_id, sid
        assert by_id[sid]["type"] != "sim", sid
        by_id[sid]["figure"] = fig


def arrow_right(x0, x1, y):
    return [line((x0, y), (x1, y)), line((x1 - 7, y - 5), (x1, y)), line((x1 - 7, y + 5), (x1, y))]


def ordered(elems):
    """Numbers smallest first; letters keep the given order."""
    elems = list(elems)
    return sorted(elems) if all(isinstance(e, int) for e in elems) else elems


def en_list(xs):
    xs = [str(x) for x in xs]
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


def ur_list(xs):
    xs = [str(x) for x in xs]
    return xs[0] if len(xs) == 1 else "، ".join(xs[:-1]) + " اور " + xs[-1]


# ---------- a set as an oval ----------

def oval(cx, cy, rx, ry, fill=False, dashed=False):
    pts = [(cx + rx * math.cos(2 * math.pi * k / 32), cy + ry * math.sin(2 * math.pi * k / 32)) for k in range(32)]
    return poly(pts, fill, dashed)


def inside_oval(x, y, cx, cy, rx, ry, w):
    """A label of width w at (x, y) stays inside the oval with room to spare."""
    return all(((px - cx) / rx) ** 2 + ((py - cy) / ry) ** 2 <= 0.92
               for px in (x - w / 2 - 2, x + w / 2 + 2) for py in (y - 8, y + 8))


def grid_places(cx, cy, n, cols, dx=26, dy=22):
    rows = math.ceil(n / cols) if n else 0
    places = []
    for i in range(n):
        r, c = divmod(i, cols)
        in_row = min(cols, n - r * cols)
        places.append((cx + (c - (in_row - 1) / 2) * dx, cy + (r - (rows - 1) / 2) * dy))
    return places


def set_oval(cx, cy, elems, *, name=None, rx=None, ry=None, cols=None, dx=26, dy=22, fill=False, dashed=False):
    """An oval holding the elements (written in a grid), its name just
    above its top left. Returns (items, rx, ry)."""
    elems = list(elems)
    n = len(elems)
    cols = cols or (n if n <= 3 else math.ceil(n / 2) if n <= 8 else math.ceil(n / 3))
    rows = math.ceil(n / cols) if n else 1
    widest = max([width_of(e) for e in elems] + [CHAR])
    dx = max(dx, widest + 8)
    rx = rx or max(30, (cols - 1) * dx / 2 + widest / 2 + 22)
    ry = ry or max(24, (rows - 1) * dy / 2 + 26)
    items = [oval(cx, cy, rx, ry, fill, dashed)]
    for e, (x, y) in zip(elems, grid_places(cx, cy, n, cols, dx, dy)):
        assert inside_oval(x, y, cx, cy, rx, ry, width_of(e)), (e, x, y)
        items.append(label((x, y), e))
    if name:
        a = math.radians(-135)
        items.append(label((cx + (rx + 6) * math.cos(a) - 4, cy + (ry + 6) * math.sin(a) - 2), name))
    return items, rx, ry


def oval_figure(elems, alt_en, alt_ur, *, name=None, outside=(), height=None, **kw):
    """One set as an oval in the middle, its name at the top left.
    outside: elements written to the right of the oval (not in the set)."""
    probe, rx, ry = set_oval(0, 0, elems, **kw)
    height = height or 2 * ry + (44 if name else 24)
    cy = height / 2 + (8 if name else 0)
    cx = W / 2 - (30 if outside else 0)
    items, rx, ry = set_oval(cx, cy, elems, name=name, **kw)
    for i, e in enumerate(outside):
        x = cx + rx + 30
        y = cy + (i - (len(outside) - 1) / 2) * 24
        items.append(label((x, y), e))
    return figure(W, height, alt_en, alt_ur, items)


def two_ovals(a, b, alt_en, alt_ur, *, names=("A", "B"), between=None, match=False, cols=None, height=None):
    """Two sets side by side as ovals. between: a label between them (like
    '='). match: a line from each element of a to the element of b at the
    same place (one-to-one matching)."""
    a, b = list(a), list(b)
    kw = {"cols": cols} if cols else {}
    if match:
        kw = {"cols": 1, "dy": 22}
    _, rxa, rya = set_oval(0, 0, a, **kw)
    _, rxb, ryb = set_oval(0, 0, b, **kw)
    ry = max(rya, ryb)
    height = height or 2 * ry + 44
    cy = height / 2 + 8
    gap = 70 if (between or match) else 50
    total = 2 * rxa + gap + 2 * rxb
    if total > W - 30 and not match and cols != 2:
        return two_ovals(a, b, alt_en, alt_ur, names=names, between=between, cols=2, height=height)
    assert total <= W - 30, total
    ca = (W - total) / 2 + rxa
    cb = ca + rxa + gap + rxb
    ia, _, _ = set_oval(ca, cy, a, name=names[0], ry=ry, **kw)
    ib, _, _ = set_oval(cb, cy, b, name=names[1], ry=ry, **kw)
    items = ia + ib
    if between:
        items.append(label(((ca + rxa + cb - rxb) / 2, cy), between))
    if match:
        assert len(a) == len(b)
        for (xa, ya), ea, eb in zip(grid_places(ca, cy, len(a), 1), a, b):
            items.append(line((xa + width_of(ea) / 2 + 6, ya), (cb - width_of(eb) / 2 - 6, ya)))
    return figure(W, height, alt_en, alt_ur, items)


# ---------- letters of a word, number lines, number grids ----------

def letter_tiles(word, alt_en, alt_ur, *, size=28, gap=6):
    """One square tile for each letter of the word, in order (repeats too)."""
    n = len(word)
    total = n * size + (n - 1) * gap
    assert total <= W - 20, word
    x = (W - total) / 2
    items = []
    for ch in word:
        items += [rect(x, 10, x + size, 10 + size), label((x + size / 2, 10 + size / 2), ch)]
        x += size + gap
    return figure(W, size + 20, alt_en, alt_ur, items)


def number_line(lo, hi, alt_en, alt_ur, *, ring=(), arrow=False, margin=24):
    """A number line with a tick and a number at every whole number from lo
    to hi. ring: numbers with a circle round them. arrow: the line goes on
    past hi with an arrow (it never ends)."""
    right = W - margin - (34 if arrow else 0)
    unit = (right - margin) / (hi - lo)
    assert unit >= width_of(hi) + 3, (lo, hi)
    y = 22
    items = [line((margin - 8, y), (right + 8, y))]
    if arrow:
        items += arrow_right(right + 8, W - margin + 6, y)[1:] + [line((right + 8, y), (W - margin + 6, y))]
    for v in range(lo, hi + 1):
        x = margin + (v - lo) * unit
        items += [line((x, y - 5), (x, y + 5)), label((x, y + 19), v)]
        if v in ring:
            items.append(circle((x, y + 19), 11))
    return figure(W, 50, alt_en, alt_ur, items)


def number_grid(lo, hi, alt_en, alt_ur, *, per_row=10, size=26, ring=()):
    """Numbers lo to hi in square boxes, per_row to a row."""
    values = list(range(lo, hi + 1))
    rows = math.ceil(len(values) / per_row)
    x0 = (W - per_row * size) / 2
    items = []
    for i, v in enumerate(values):
        r, c = divmod(i, per_row)
        x, y = x0 + c * size, 8 + r * size
        items += [rect(x, y, x + size, y + size), label((x + size / 2, y + size / 2), v)]
        if v in ring:
            items.append(circle((x + size / 2, y + size / 2), size / 2 - 1))
    return figure(W, rows * size + 16, alt_en, alt_ur, items)


# ---------- subsets ----------

def set_boxes(texts, alt_en, alt_ur, *, dashed=()):
    """A row of boxes, each holding a small set written like {a, b}."""
    n = len(texts)
    widths = [max(width_of(t), 2 * CHAR) + 16 for t in texts]
    gap = 12
    total = sum(widths) + (n - 1) * gap
    assert total <= W - 16, texts
    x = (W - total) / 2
    items = []
    for i, (t, bw) in enumerate(zip(texts, widths)):
        items += [rect(x, 10, x + bw, 44, dashed=i in dashed), label((x + bw / 2, 27), t)]
        x += bw + gap
    return figure(W, 54, alt_en, alt_ur, items)


def doubling_chain(sizes, alt_en, alt_ur):
    """For each set size k: k dots (the elements) above a box holding 2^k
    (how many subsets), with '×2' between the boxes."""
    n = len(sizes)
    bw, gap = 40, 30
    total = n * bw + (n - 1) * gap
    x = (W - total) / 2
    items = []
    for i, k in enumerate(sizes):
        cx = x + bw / 2
        for j in range(k):
            items.append(circle((cx + (j - (k - 1) / 2) * 9, 16), 3, fill=True))
        items += [rect(x, 30, x + bw, 62), label((cx, 46), 2 ** k)]
        if i < n - 1:
            items.append(label((x + bw + gap / 2, 76), "×2"))
            items += arrow_right(x + bw + 3, x + bw + gap - 3, 46)
        x += bw + gap
    return figure(W, 88, alt_en, alt_ur, items)


def sweets_box(n, alt_en, alt_ur):
    """A box holding n sweets (filled circles), each with a small number."""
    gap = 40
    total = (n - 1) * gap
    x0 = (W - total) / 2
    items = [rect(x0 - 34, 12, x0 + total + 34, 62)]
    for i in range(n):
        items += [circle((x0 + i * gap, 37), 13), label((x0 + i * gap, 37), i + 1)]
    return figure(W, 74, alt_en, alt_ur, items)


# ---------- Venn diagrams ----------

R = 52          # circle radius
D = 34          # half the distance between the two centres


def lens(ca, cb, r):
    """The overlap of two equal circles side by side, as a polygon."""
    d = (cb[0] - ca[0]) / 2
    h = math.sqrt(r * r - d * d)
    t = math.degrees(math.atan2(h, d))
    pts = [(cb[0] + r * math.cos(math.radians(180 - t + 2 * t * k / 16)),
            cb[1] + r * math.sin(math.radians(180 - t + 2 * t * k / 16))) for k in range(17)]
    pts += [(ca[0] + r * math.cos(math.radians(-t + 2 * t * k / 16)),
             ca[1] + r * math.sin(math.radians(-t + 2 * t * k / 16))) for k in range(1, 16)]
    return poly(pts, fill=True)


def region_places(x, cy, n, dy=20):
    cols = 1 if n <= 3 else 2
    return grid_places(x, cy, n, cols, dx=22, dy=dy)


def venn(alt_en, alt_ur, *, a_only=(), both=(), b_only=(), outside=(), names=("A", "B"),
         shade=None, universe=None, height=None, cx=None, r=R, d=D, check=True):
    """Two overlapping circles. Each region's labels (elements or counts)
    are written in its middle. shade: 'both' fills the overlap, 'union'
    fills both circles. universe: a label for a rectangle round
    everything (like 'U' or a total); outside: labels between the circles
    and the rectangle (bottom right)."""
    cx = W / 2 if cx is None else cx
    top_room = 30
    height = height or 2 * r + top_room + 12 + (8 if universe is not None else 0)
    cy = top_room + r + (4 if universe is not None else 0)
    ca, cb = (cx - d, cy), (cx + d, cy)
    items = []
    if universe is not None:
        items.append(rect(10, 6, W - 10, height - 6))
        items.append(label((24 + width_of(universe) / 2 - CHAR / 2, 20), universe))
    if shade == "union":
        items += [circle(ca, r, fill=True), circle(cb, r, fill=True)]
    else:
        items += [circle(ca, r), circle(cb, r)]
        if shade == "both":
            items.append(lens(ca, cb, r))
    places = []
    places += [(e, p) for e, p in zip(a_only, region_places(cx - d - r / 2 + 2, cy, len(a_only)))]
    places += [(e, p) for e, p in zip(both, region_places(cx, cy, len(both)))]
    places += [(e, p) for e, p in zip(b_only, region_places(cx + d + r / 2 - 2, cy, len(b_only)))]
    for i, e in enumerate(outside):
        places.append((e, (cx + d + r + 22 + i * 26, cy + r - 4)))
    if check:
        for e, (x, y) in places:
            for (c, members) in ((ca, list(a_only) + list(both)), (cb, list(b_only) + list(both))):
                dist = math.dist((x, y), c)
                if e in members:
                    assert dist <= r - 10, (e, dist)
                else:
                    assert dist >= r + 6, (e, dist)
    items += [label(p, e) for e, p in places]
    # names above the top left of A and the top right of B
    na, nb = names
    a = math.radians(-128)
    items.append(label((ca[0] + (r + 8) * math.cos(a) - width_of(na) / 2 + 4, ca[1] + (r + 8) * math.sin(a)), na))
    b = math.radians(-52)
    items.append(label((cb[0] + (r + 8) * math.cos(b) + width_of(nb) / 2 - 4, cb[1] + (r + 8) * math.sin(b)), nb))
    return figure(W, height, alt_en, alt_ur, items)


def two_venns(alt_en, alt_ur):
    """Two small Venn diagrams side by side: on the left both circles are
    shaded (the union), on the right only the overlap (the intersection)."""
    r, d = 34, 22
    cy = 62
    items = []
    for cx, shade in ((78, "union"), (222, "both")):
        ca, cb = (cx - d, cy), (cx + d, cy)
        if shade == "union":
            items += [circle(ca, r, fill=True), circle(cb, r, fill=True)]
        else:
            items += [circle(ca, r), circle(cb, r), lens(ca, cb, r)]
        items += [label((ca[0] - r * 0.75, cy - r - 6), "A"), label((cb[0] + r * 0.75, cy - r - 6), "B")]
    return figure(W, 108, alt_en, alt_ur, items)

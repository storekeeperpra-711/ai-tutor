"""Pictures for the Factors and Multiples unit: dot arrays for factor
pairs and square numbers, factor trees, jumps on a number line for
multiples, Venn circles for common factors and shared primes, number
grids for primes, and rectangles for HCF × LCM, built as lesson "figure"
blocks.

Every figure is drawn in a box 300 wide, close to the size the app paints
it on a phone, so the 16 px labels keep their room. Coordinates are
rounded to 1 decimal place. Labels are numbers, short products like 3×4,
or "?"; the alt text says what each one stands for.
"""
import math

from common import T, is_prime

W = 300
MAX_ITEMS = 60
CHAR = 9.6         # about how wide one label character is
LABEL_H = 16       # about how tall a label is


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


def figure(width, height, alt_en, alt_ur, items):
    assert len(items) <= MAX_ITEMS, (alt_en, len(items))
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


def shift(items, dx, dy=0):
    """The same items moved by (dx, dy)."""
    out = []
    for it in items:
        it = dict(it)
        for k in ("from", "to", "center", "at"):
            if k in it:
                it[k] = pt(it[k][0] + dx, it[k][1] + dy)
        if "points" in it:
            it["points"] = [pt(x + dx, y + dy) for x, y in it["points"]]
        out.append(it)
    return out


def en_list(xs):
    return ", ".join(str(x) for x in xs)


def ur_list(xs):
    return "، ".join(str(x) for x in xs)


def times(*xs):
    return "×".join(str(x) for x in xs)


# ---------- dot arrays ----------

GAP = 14           # distance between dots in an array
DOT = 4.5


def dot_array(x0, y0, rows, cols, *, gap=GAP, r=DOT, fill=True, dashed_last=0, extra=0):
    """rows × cols dots, the first at (x0, y0). dashed_last: that many of
    the last dots are dashed (missing). extra: dashed dots in one more row
    (left over)."""
    items = []
    n = rows * cols
    for k in range(n):
        i, j = divmod(k, cols)
        missing = k >= n - dashed_last
        items.append(circle((x0 + j * gap, y0 + i * gap), r, fill=fill and not missing, dashed=missing))
    for j in range(extra):
        items.append(circle((x0 + j * gap, y0 + rows * gap), r, dashed=True))
    return items


def arrays_figure(arrays, alt_en, alt_ur, *, gap=GAP, space=30):
    """Dot arrays side by side (wrapping onto a new line when there is no
    room), each with its text under it. arrays = [dict(rows, cols, text,
    dashed_last=0, extra=0, fill=True)]."""
    lines, cur, cur_w = [], [], 0
    for a in arrays:
        w = max((a["cols"] - 1) * gap, len(str(a["text"])) * CHAR)
        if cur and cur_w + space + w > W - 24:
            lines.append(cur)
            cur, cur_w = [], 0
        cur_w += (space if cur else 0) + w
        cur.append((a, w))
    lines.append(cur)
    items, y = [], 14
    for ln in lines:
        total = sum(w for _, w in ln) + space * (len(ln) - 1)
        x = (W - total) / 2
        tall = max(a["rows"] + (1 if a.get("extra") else 0) for a, _ in ln)
        for a, w in ln:
            dots_w = (a["cols"] - 1) * gap
            x0 = x + (w - dots_w) / 2
            items += dot_array(x0, y, a["rows"], a["cols"], gap=gap, fill=a.get("fill", True),
                               dashed_last=a.get("dashed_last", 0), extra=a.get("extra", 0))
            items.append(label((x + w / 2, y + (tall - 1) * gap + 20), a["text"]))
            x += w + space
        y += (tall - 1) * gap + 46
    return figure(W, y - 14, alt_en, alt_ur, items)


def side_array(rows, cols, alt_en, alt_ur, *, top_text=None, left_text=None, gap=GAP):
    """One array with the number of dots in a row written above it and the
    number of rows written on its left."""
    w = (cols - 1) * gap
    x0 = (W - w) / 2
    y0 = 36
    items = dot_array(x0, y0, rows, cols, gap=gap)
    items.append(label((x0 + w / 2, 14), top_text if top_text is not None else cols))
    items.append(label((x0 - 22, y0 + (rows - 1) * gap / 2), left_text if left_text is not None else rows))
    return figure(W, y0 + (rows - 1) * gap + 16, alt_en, alt_ur, items)


def rainbow(n, pairs, alt_en, alt_ur):
    """The factors of n in a row, each pair that multiplies to n joined by
    an arc above (the outside pair is the biggest arc)."""
    fs = sorted({f for p in pairs for f in p})
    for a, b in pairs:
        assert a * b == n, (a, b, n)
    step = min(46, (W - 50) / (len(fs) - 1))
    x0 = (W - step * (len(fs) - 1)) / 2
    xs = {f: x0 + i * step for i, f in enumerate(fs)}
    biggest = max(abs(xs[b] - xs[a]) / 2 for a, b in pairs)
    y = biggest + 22
    items = []
    for a, b in pairs:
        # drawn as short lines, not an arc, so the picture can stop just under the numbers
        r = abs(xs[b] - xs[a]) / 2
        cx, cy = (xs[a] + xs[b]) / 2, y - 10
        k = 12 if r > 40 else 8
        ps = [(cx - r * math.cos(math.pi * i / k), cy - r * math.sin(math.pi * i / k)) for i in range(k + 1)]
        items += [line(ps[i], ps[i + 1]) for i in range(k)]
    for f in fs:
        items.append(label((xs[f], y), f))
    return figure(W, y + 16, alt_en, alt_ur, items)


# ---------- number grid ----------

def number_grid(lo, hi, alt_en, alt_ur, *, ring=(), cols=10):
    """The numbers lo to hi in a grid of cells; numbers in ring get a circle."""
    nums = list(range(lo, hi + 1))
    cols = min(cols, len(nums))
    rows = -(-len(nums) // cols)
    cw, ch = min(28, (W - 12) // cols), 30
    x0 = (W - cols * cw) / 2
    y0 = 8
    items = []
    assert len(nums) % cols == 0, (lo, hi, cols)
    for i in range(rows + 1):
        items.append(line((x0, y0 + i * ch), (x0 + cols * cw, y0 + i * ch)))
    for j in range(cols + 1):
        items.append(line((x0 + j * cw, y0), (x0 + j * cw, y0 + rows * ch)))
    for k, n in enumerate(nums):
        i, j = divmod(k, cols)
        c = (x0 + j * cw + cw / 2, y0 + i * ch + ch / 2)
        items.append(label(c, n))
        if n in ring:
            items.append(circle(c, 11.5))
    return figure(W, y0 * 2 + rows * ch, alt_en, alt_ur, items)


# ---------- factor trees ----------

def ladder(n, stop=None):
    """A factor tree that splits off the smallest prime each time:
    60 -> (60, (2,), (30, (2,), (15, (3,), (5,)))). It stops (leaving a
    leaf that is not split) when it reaches `stop`."""
    if is_prime(n) or n == stop or n == 1:
        return (n,)
    p = next(d for d in range(2, n + 1) if n % d == 0)
    return (n, (p,), ladder(n // p, stop))


LEAF = 40
LEVEL = 40


def _leaves(t):
    return 1 if len(t) == 1 else _leaves(t[1]) + _leaves(t[2])


def _depth(t):
    return 0 if len(t) == 1 else 1 + max(_depth(t[1]), _depth(t[2]))


def tree_items(t, x0, y0, *, ring_primes=True, leaf=LEAF):
    """A factor tree with its first leaf at x0 and root at y0. Branches to
    "?" are dashed. Numbers that are prime and end a branch get a circle.
    Returns (items, root x)."""
    items = []

    def place(node, left, depth):
        y = y0 + depth * LEVEL
        v = node[0]
        if len(node) == 1:
            x = left + leaf / 2
        else:
            a, b = node[1], node[2]
            if isinstance(v, int) and isinstance(a[0], int) and isinstance(b[0], int):
                assert a[0] * b[0] == v, node
            xa = place(a, left, depth + 1)
            xb = place(b, left + _leaves(a) * leaf, depth + 1)
            x = (xa + xb) / 2
            for xc, child in ((xa, a), (xb, b)):
                items.append(line((x, y + 10), (xc, y + LEVEL - 14), dashed=child == ("?",)))
        items.append(label((x, y), v))
        if ring_primes and len(node) == 1 and isinstance(v, int) and is_prime(v):
            items.append(circle((x, y), 13))
        return x

    x = place(t, x0, 0)
    return items, x


def tree_size(t, leaf=LEAF):
    return _leaves(t) * leaf, _depth(t) * LEVEL + 32


def tree_figure(t, alt_en, alt_ur, **kw):
    w, h = tree_size(t)
    items, _ = tree_items(t, (W - w) / 2, 20, **kw)
    return figure(W, h + 4, alt_en, alt_ur, items)


def two_trees(t1, t2, alt_en, alt_ur):
    """Two factor trees side by side."""
    leaf = min(LEAF, (W - 30) / (_leaves(t1) + _leaves(t2)))
    (w1, h1), (w2, h2) = tree_size(t1, leaf), tree_size(t2, leaf)
    gap = max(20, (W - w1 - w2) / 3)
    x1 = (W - w1 - w2 - gap) / 2
    items, _ = tree_items(t1, x1, 20, leaf=leaf)
    more, _ = tree_items(t2, x1 + w1 + gap, 20, leaf=leaf)
    return figure(W, max(h1, h2) + 4, alt_en, alt_ur, items + more)


def tree_words(t):
    """The splits of a factor tree in words, e.g. '60 splits into 2 and 30,
    30 into 2 and 15'."""
    en, ur = [], []

    def walk(node):
        if len(node) == 3:
            en.append(f"{node[0]} into {node[1][0]} and {node[2][0]}")
            ur.append(f"{node[0]} سے {node[1][0]} اور {node[2][0]}")
            walk(node[1])
            walk(node[2])

    walk(t)
    return "; ".join(en), "؛ ".join(ur)


def tree_alt(t, extra_en="", extra_ur=""):
    en, ur = tree_words(t)
    return (f"A factor tree for {t[0]}: {en}. The primes at the ends of the branches are circled.{extra_en}",
            f"{t[0]} کا اجزائے ضربی کا درخت: {ur}۔ شاخوں کے آخر میں مفرد اعداد کے گرد دائرہ ہے۔{extra_ur}")


def tree_fig(t, extra_en="", extra_ur=""):
    return tree_figure(t, *tree_alt(t, extra_en, extra_ur))


def two_trees_fig(a, b, stop_a=None, stop_b=None):
    t1, t2 = ladder(a, stop_a), ladder(b, stop_b)
    e1, u1 = tree_words(t1)
    e2, u2 = tree_words(t2)
    e1 = e1 or f"{a} is prime and stays as it is"
    u1 = u1 or f"{a} مفرد ہے اور ویسے ہی رہتا ہے"
    return two_trees(t1, t2,
                     f"Two factor trees side by side. Left, {a}: {e1}. Right, {b}: {e2}. The primes at the ends of the branches are circled.",
                     f"دو اجزائے ضربی کے درخت ساتھ ساتھ۔ بائیں، {a}: {u1}۔ دائیں، {b}: {u2}۔ شاخوں کے آخر میں مفرد اعداد کے گرد دائرہ ہے۔")


# ---------- jumps on number lines ----------

class JumpLine:
    """A number line from 0 to hi across the figure at height y."""

    def __init__(self, hi, y, *, left=24, right=W - 24):
        self.hi, self.y, self.left = hi, y, left
        self.unit = (right - left) / hi
        self.items = [line((left - 6, y), (right + 8, y))]

    def x(self, v):
        return self.left + v * self.unit

    def jumps(self, step, count, *, texts=None, numbers=True, arrows=False, ring=(), hide=()):
        """count jumps of `step` from 0, each an arc above the line, with a
        tick and its number under each landing point. texts: a label in
        each arc. hide: numbers written as '?'. ring: numbers circled."""
        y = self.y
        self.items.append(line((self.x(0), y - 5), (self.x(0), y + 5)))
        if numbers:
            self.items.append(label((self.x(0), y + 16), 0))
        for k in range(count):
            a, b = k * step, (k + 1) * step
            xa, xb = self.x(a), self.x(b)
            r = (xb - xa) / 2
            self.items.append(arc(((xa + xb) / 2, y), r, 180, 180))
            self.items.append(line((xb, y - 5), (xb, y + 5)))
            if arrows:
                self.items += [line((xb - 4, y - 8), (xb, y - 1)), line((xb + 4, y - 8), (xb, y - 1))]
            if texts and texts[k] is not None:
                self.items.append(label(((xa + xb) / 2, y - r + 10 if r > 26 else y - r - 10), texts[k]))
            if b in hide:
                self.items.append(label((xb, y + 16), "?"))
            elif numbers:
                self.items.append(label((xb, y + 16), b))
            if b in ring:
                self.items.append(circle((xb, y + 16), 13))


def multiples_line(step, count, alt_en, alt_ur, *, shown=None, hide=(), counts=True):
    """count jumps of `step` from 0 on one line. shown: which landing
    numbers are written (others are only ticks); hide: written as '?'.
    counts: number the jumps 1, 2, 3 … above them."""
    hi = step * count
    unit = (W - 48) / hi
    r = step * unit / 2
    y = r + (30 if counts and r <= 26 else 14)
    ln = JumpLine(hi, y)
    ln.jumps(step, count, texts=[k + 1 for k in range(count)] if counts else None,
             numbers=False, arrows=True)
    shown = [0] + [step * (k + 1) for k in range(count)] if shown is None else shown
    for v in shown:
        ln.items.append(label((ln.x(v), y + 16), v))
    for v in hide:
        ln.items.append(label((ln.x(v), y + 16), "?"))
    # the app checks an arc's whole circle stays inside the box
    return figure(W, max(y + 30, y + r + 1), alt_en, alt_ur, ln.items)


def multiples_rows(a, b, hi, alt_en, alt_ur, *, ring=True, count_a=None, count_b=None):
    """Two number lines from 0 to hi, one above the other: jumps of a on
    the top line and jumps of b on the bottom one, the landing numbers
    under each. ring: circle the numbers both lines land on. count_a,
    count_b: draw only that many jumps."""
    count_a = hi // a if count_a is None else count_a
    count_b = hi // b if count_b is None else count_b
    unit = (W - 48) / hi
    ra, rb = a * unit / 2, b * unit / 2
    common = [v for v in range(a, hi + 1, a) if v % b == 0 and v <= a * count_a and v <= b * count_b] if ring else []
    y1 = ra + 26
    y2 = y1 + 16 + 14 + rb + 22
    top = JumpLine(hi, y1)
    top.jumps(a, count_a, texts=[f"+{a}"] + [None] * (count_a - 1), ring=common)
    bottom = JumpLine(hi, y2)
    bottom.jumps(b, count_b, texts=[f"+{b}"] + [None] * (count_b - 1), ring=common)
    # the app checks an arc's whole circle stays inside the box
    return figure(W, max(y2 + 30, y2 + rb + 1), alt_en, alt_ur, top.items + bottom.items)


# ---------- Venn circles ----------

def venn(left, both, right, names, alt_en, alt_ur, *, ring=()):
    """Two overlapping circles: the numbers only in the first, in both, and
    only in the second, each in its own part; the name of each circle above
    it. ring: numbers in the middle part that get a circle."""
    r, cy = 70, 100
    c1, c2 = (W / 2 - 38, cy), (W / 2 + 38, cy)
    items = [circle(c1, r), circle(c2, r),
             label((c1[0] - 20, cy - r - 12), names[0]), label((c2[0] + 20, cy - r - 12), names[1])]

    def column(xs, xc, ring_these=()):
        n = len(xs)
        cols = 1 if n <= 3 else 2
        per = -(-n // cols)
        for k, v in enumerate(xs):
            j, i = divmod(k, per)
            x = xc + (j - (cols - 1) / 2) * 30
            y = cy + (i - (per - 1) / 2) * 26
            items.append(label((x, y), v))
            if v in ring_these:
                items.append(circle((x, y), 13))

    column(left, c1[0] - 34)
    column(both, W / 2, ring)
    column(right, c2[0] + 34)
    return figure(W, cy + r + 6, alt_en, alt_ur, items)


# ---------- rectangles with the same area ----------

def area_rects(rects, alt_en, alt_ur, *, max_w=190, max_h=160, min_h=0):
    """Rectangles one under the other, drawn to the same scale. Each is a
    dict: h, w (the sides, used for the size), and optional h_text, w_text
    (what is written by each side, default the number) and area (written in
    the middle). The width is written above and the height on the left."""
    s = min(max_w / max(r["w"] for r in rects), (max_h - 34 * len(rects)) / sum(r["h"] for r in rects))
    items, y = [], 26
    x0 = 52
    for r in rects:
        hh, ww = max(r["h"] * s, min_h), r["w"] * s
        items.append(rect(x0, y, x0 + ww, y + hh))
        items.append(label((x0 + ww / 2, y - 11), r.get("w_text", r["w"])))
        items.append(label((x0 - 18, y + hh / 2), r.get("h_text", r["h"])))
        if r.get("area") is not None:
            text = str(r["area"])
            if hh >= 22 and ww >= len(text) * CHAR + 12:
                items.append(label((x0 + ww / 2, y + hh / 2), text))
            else:
                # too thin: write it just after the rectangle
                assert x0 + ww + 10 + len(text) * CHAR <= W - 10, r
                items.append(label((x0 + ww + 8 + len(text) * CHAR / 2, y + hh / 2), text))
        y += hh + 34
    return figure(W, y - 20, alt_en, alt_ur, items)


# ---------- groups of dots (two kinds) ----------

def dot_block(x0, y0, n, cols, *, gap=GAP, r=DOT, fill=True):
    """n dots in rows of cols, the first at (x0, y0)."""
    return [circle((x0 + (k % cols) * gap, y0 + (k // cols) * gap), r, fill=fill) for k in range(n)]


def dot_groups(groups, alt_en, alt_ur, *, side=True, gap=GAP, r=DOT):
    """Blocks of dots, each (n, cols, fill, text): side by side with the
    text above each block (side=True), or one under the other with the
    text on the left."""
    items = []
    if side:
        widths = [(cols - 1) * gap for _, cols, _, _ in groups]
        space = 40
        x = (W - sum(widths) - space * (len(groups) - 1)) / 2
        tall = 0
        for (n, cols, fill, text), w in zip(groups, widths):
            items.append(label((x + w / 2, 14), text))
            items += dot_block(x, 38, n, cols, gap=gap, r=r, fill=fill)
            tall = max(tall, -(-n // cols))
            x += w + space
        return figure(W, 38 + (tall - 1) * gap + 14, alt_en, alt_ur, items)
    widest = max((cols - 1) * gap for _, cols, _, _ in groups)
    x = (W - widest) / 2 + 14
    y = 14
    for n, cols, fill, text in groups:
        rows = -(-n // cols)
        items.append(label((x - 30, y + (rows - 1) * gap / 2), text))
        items += dot_block(x, y, n, cols, gap=gap, r=r, fill=fill)
        y += (rows - 1) * gap + 24
    return figure(W, y - 10, alt_en, alt_ur, items)


# ---------- word problems ----------

def bars_figure(values, alt_en, alt_ur, *, fills=None, max_w=220):
    """Bars one under the other, as long as each value (like ropes), with
    the value written after each bar."""
    s = max_w / max(values)
    items, y = [], 14
    for i, v in enumerate(values):
        items.append(rect(20, y, 20 + v * s, y + 20, fill=True if fills is None else fills[i]))
        items.append(label((20 + v * s + 10 + len(str(v)) * CHAR / 2, y + 10), v))
        y += 36
    return figure(W, y - 2, alt_en, alt_ur, items)


def floor_figure(width, length, alt_en, alt_ur, *, max_w=200, max_h=140):
    """A rectangle `length` across and `width` down, drawn to scale, with
    each side written beside it."""
    s = min(max_w / length, max_h / width)
    x0 = (W - length * s) / 2 + 10
    y0 = 30
    items = [rect(x0, y0, x0 + length * s, y0 + width * s),
             label((x0 + length * s / 2, y0 - 13), length),
             label((x0 - 20, y0 + width * s / 2), width)]
    return figure(W, y0 + width * s + 12, alt_en, alt_ur, items)


def pack_items(x0, y0, n, cols, *, gap=12, r=4, sticks=False):
    """One pack: a box round n dots (or upright sticks) in rows of cols.
    Returns (items, width, height)."""
    rows = -(-n // cols)
    w, h = (cols - 1) * gap + 20, (rows - 1) * gap + (28 if sticks else 20)
    items = [rect(x0, y0, x0 + w, y0 + h)]
    for k in range(n):
        i, j = divmod(k, cols)
        x, y = x0 + 10 + j * gap, y0 + 10 + i * gap
        if sticks:
            items.append(line((x, y - 4), (x, y + 12 + 0 * i)))
        else:
            items.append(circle((x, y), r, fill=True))
    return items, w, h


def packs_figure(packs, alt_en, alt_ur):
    """Packs side by side, each (n, cols, sticks) with n written above."""
    sizes = []
    for n, cols, sticks in packs:
        _, w, h = pack_items(0, 0, n, cols, sticks=sticks)
        sizes.append((w, h))
    space = 50
    x = (W - sum(w for w, _ in sizes) - space * (len(packs) - 1)) / 2
    items = []
    for (n, cols, sticks), (w, h) in zip(packs, sizes):
        more, _, _ = pack_items(x, 36, n, cols, sticks=sticks)
        items += more + [label((x + w / 2, 18), n)]
        x += w + space
    return figure(W, 36 + max(h for _, h in sizes) + 10, alt_en, alt_ur, items)


def hcf_lcm_panels(alt_en, alt_ur):
    """Two small pictures with no numbers. Left (HCF): two bars cut into
    equal pieces with nothing left over. Right (LCM): jumps of two sizes on
    two lines that land together, the meeting point circled."""
    items = []
    piece = 38
    for row, n in enumerate((2, 3)):
        y = 34 + row * 46
        items.append(rect(16, y, 16 + n * piece, y + 18, fill=True))
        for k in range(1, n):
            items.append(line((16 + k * piece, y - 4), (16 + k * piece, y + 22), dashed=True))
    items.append(line((W / 2, 8), (W / 2, 102), dashed=True))
    x0, unit = 172, 18
    for row, (step, count) in enumerate(((2, 3), (3, 2))):
        y = 44 + row * 46
        items.append(line((x0 - 4, y), (x0 + 6 * unit + 10, y)))
        for k in range(count):
            a, b = x0 + k * step * unit, x0 + (k + 1) * step * unit
            items.append(arc(((a + b) / 2, y), (b - a) / 2, 180, 180))
        items.append(circle((x0 + 6 * unit, y), 6))
    return figure(W, 90 + 3 * unit / 2 + 1, alt_en, alt_ur, items)

"""Pictures for the Data Handling unit: tally marks, tables, bar graphs,
double bar graphs, pie charts, levelling counters for the mean, number
cards for the median and dot plots, built as lesson "figure" blocks.

Every figure is drawn in a box 300 wide, close to the size the app paints
it on a phone, so the 16 px labels keep their room. Coordinates are
rounded to 1 decimal place. Labels are numbers or one or two letters; the
alt text names what each letter stands for.
"""
import math

from common import T

W = 300
MAX_ITEMS = 60
CHAR = 9.6         # about how wide one label character is


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


def arrow_right(x0, x1, y):
    return [line((x0, y), (x1, y)), line((x1 - 7, y - 5), (x1, y)), line((x1 - 7, y + 5), (x1, y))]


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


# ---------- tally marks ----------

STROKE = 7         # gap between upright strokes
GATE_GAP = 12      # gap between two groups


def tally_width(n):
    gates, rest = divmod(n, 5)
    parts = [3 * STROKE] * gates + ([(rest - 1) * STROKE] if rest else [])
    return sum(parts) + GATE_GAP * (len(parts) - 1) if parts else 0


def tally_marks(x, y, n, h=22):
    """Tally strokes for n starting at x, from y (top) to y + h: each fifth
    stroke goes across the four before it. Returns (items, group centres)."""
    items, centres = [], []
    gates, rest = divmod(n, 5)
    for g in range(gates):
        for i in range(4):
            items.append(line((x + i * STROKE, y), (x + i * STROKE, y + h)))
        items.append(line((x - 3, y + h - 4), (x + 3 * STROKE + 3, y + 4)))
        centres.append((x + 1.5 * STROKE, 5))
        x += 3 * STROKE + GATE_GAP
    if rest:
        for i in range(rest):
            items.append(line((x + i * STROKE, y), (x + i * STROKE, y + h)))
        centres.append((x + (rest - 1) * STROKE / 2, rest))
    return items, centres


def tally_figure(n, alt_en, alt_ur, parts=False):
    """A row of tally marks for n, centred. parts: write each group's size
    under it and the total at the end."""
    w = tally_width(n) + (40 if parts else 0)
    x0 = (W - w) / 2
    items, centres = tally_marks(x0, 12, n)
    height = 46
    if parts:
        for cx, size in centres:
            items.append(label((cx, 50), size))
        items.append(label((x0 + tally_width(n) + 26, 23), f"={n}"))
        height = 66
    return figure(W, height, alt_en, alt_ur, items)


def table_figure(rows, alt_en, alt_ur, *, tallies=True, counts=True, name_w=46):
    """A frequency table: a short name for each row, its tally marks and its
    count. rows = [(name, count)]."""
    count_w, row_h = 44, 32
    tally_w = max(tally_width(c) for _, c in rows) + 24 if tallies else 0
    width = name_w + tally_w + (count_w if counts else 0)
    x0, y0 = (W - width) / 2, 6
    y1 = y0 + row_h * len(rows)
    items = [rect(x0, y0, x0 + width, y1)]
    for i in range(1, len(rows)):
        items.append(line((x0, y0 + i * row_h), (x0 + width, y0 + i * row_h)))
    xs = [x0 + name_w] + ([x0 + name_w + tally_w] if tallies and counts else [])
    for x in xs:
        items.append(line((x, y0), (x, y1)))
    for i, (name, c) in enumerate(rows):
        yc = y0 + i * row_h + row_h / 2
        items.append(label((x0 + name_w / 2, yc), name))
        if tallies:
            marks, _ = tally_marks(x0 + name_w + 12, yc - 9, c, h=18)
            items += marks
        if counts:
            items.append(label((x0 + width - count_w / 2, yc), c))
    return figure(W, y1 + 6, alt_en, alt_ur, items)


# ---------- bar graphs ----------

def bar_graph(values, cats, alt_en, alt_ur, *, top, step, square=None, legend=None, numbers=True,
              height=170, bar_text=None, fills=None, mean_line=None, mean_text=None, grid=(),
              missing=None, width=W):
    """A bar graph: y axis from 0 to top with a number every `step`, one bar
    per value with its short name under it.

    square: draw each bar as a stack of squares, each standing for `square`.
    legend: write "□ = legend" in the top right (a small square and "=n").
    numbers: write the numbers up the axis (False when the question is to
    work them out from the squares).
    bar_text: text above each bar (or None for no text).
    fills: which bars are filled (default all).
    mean_line: draw a dashed line at that value across the graph.
    grid: values with a dashed line across (for "the 20 line").
    missing: index of a bar drawn as "?" with no bar.
    """
    widest = max(len(str(v)) for v in range(0, top + 1, step)) if numbers else 0
    ax = 18 + widest * CHAR if numbers else 20
    y0 = height - 26                       # the axis line
    ytop = 30 if legend is not None or mean_text or bar_text else 18
    unit = (y0 - ytop) / top
    right = width - 14
    slot = (right - ax) / len(values)
    bw = min(slot * 0.6, 40)
    items = [line((ax, y0), (right, y0)), line((ax, y0), (ax, ytop - 8))]
    if numbers:
        for v in range(0, top + 1, step):
            y = y0 - v * unit
            items += [line((ax - 4, y), (ax, y)), label((ax - 8 - len(str(v)) * CHAR / 2, y), v)]
    for v in grid:
        items.append(line((ax, y0 - v * unit), (right, y0 - v * unit), dashed=True))
    for i, v in enumerate(values):
        cx = ax + slot * (i + 0.5)
        x0, x1 = cx - bw / 2, cx + bw / 2
        filled = True if fills is None else fills[i]
        if i == missing:
            items.append(label((cx, y0 - 14), "?"))
        elif square:
            assert v % square == 0, (v, square)
            for k in range(v // square):
                items.append(rect(x0, y0 - (k + 1) * square * unit, x1, y0 - k * square * unit, fill=filled))
        elif v:
            items.append(rect(x0, y0 - v * unit, x1, y0, fill=filled))
        if cats:
            items.append(label((cx, y0 + 14), cats[i]))
        if bar_text and bar_text[i] is not None:
            ty = y0 - v * unit - 11
            if mean_line is not None and abs(ty - (y0 - mean_line * unit)) < 10:
                ty = y0 - v * unit + 12          # inside the bar, clear of the dashed line
            items.append(label((cx, ty), bar_text[i]))
    if mean_line is not None:
        y = y0 - mean_line * unit
        items.append(line((ax, y), (right, y), dashed=True))
        if mean_text:
            items.append(label((right - 14, y - 11), mean_text))
    if legend is not None:
        s = min(square * unit, 16) if square else 12
        lx = right - 30 - len(f"={legend}") * CHAR / 2
        items += [rect(lx - s, 8, lx, 8 + s, fill=True), label((lx + 6 + len(f"={legend}") * CHAR / 2, 8 + s / 2), f"={legend}")]
    return figure(width, height, alt_en, alt_ur, items)


def squares_bar(n, unit_value, cat, alt_en, alt_ur):
    """One bar of n squares, with the key '□ = unit_value' beside it."""
    side = min(16, 130 / n)
    height = n * side + 40
    x0 = 110
    y0 = height - 26
    items = [line((60, y0), (240, y0))]
    for k in range(n):
        items.append(rect(x0, y0 - (k + 1) * side, x0 + 36, y0 - k * side, fill=True))
    items.append(label((x0 + 18, y0 + 14), cat))
    text = f"={unit_value}"
    items += [rect(190, 14, 190 + side, 14 + side, fill=True),
              label((190 + side + 6 + len(text) * CHAR / 2, 14 + side / 2), text)]
    return figure(W, height, alt_en, alt_ur, items)


def double_bar_graph(groups, cats, alt_en, alt_ur, *, top, step, keys=("B", "G"), height=180):
    """Two bars side by side for each group: the first filled, the second
    empty. groups = [(a, b)]. A key at the top says which is which."""
    widest = len(str(top))
    ax = 18 + widest * CHAR
    y0 = height - 26
    ytop = 34
    unit = (y0 - ytop) / top
    right = W - 12
    slot = (right - ax) / len(groups)
    bw = min(slot * 0.32, 30)
    items = [line((ax, y0), (right, y0)), line((ax, y0), (ax, ytop - 8))]
    for v in range(0, top + 1, step):
        y = y0 - v * unit
        items += [line((ax - 4, y), (ax, y)), label((ax - 8 - len(str(v)) * CHAR / 2, y), v)]
    for i, (a, b) in enumerate(groups):
        cx = ax + slot * (i + 0.5)
        items += [rect(cx - bw - 1, y0 - a * unit, cx - 1, y0, fill=True),
                  rect(cx + 1, y0 - b * unit, cx + bw + 1, y0)]
        items.append(label((cx, y0 + 14), cats[i]))
    kx = right - 100
    items += [rect(kx, 8, kx + 12, 20, fill=True), label((kx + 24, 14), keys[0]),
              rect(kx + 50, 8, kx + 62, 20), label((kx + 74, 14), keys[1])]
    return figure(W, height, alt_en, alt_ur, items)


# ---------- pie charts ----------

def _on(c, r, deg):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] + r * math.sin(math.radians(deg)))


def pie_chart(slices, alt_en, alt_ur, *, fill=(), r=72, height=172):
    """A pie chart: slices = [(angle, name, angle_text)], drawn clockwise
    from the top. Each slice gets its name and angle text inside it (either
    may be None). fill: which slices are shaded."""
    assert sum(a for a, _, _ in slices) == 360, slices
    c = (W / 2, height / 2)
    items = [circle(c, r)]
    start = -90
    for i, (a, name, text) in enumerate(slices):
        if i in fill:
            pts = [c] + [_on(c, r, start + a * k / 24) for k in range(25)]
            items.append(poly(pts, fill=True))
        items.append(line(c, _on(c, r, start)))
        mid = start + a / 2
        far = 0.58 if a >= 90 else 0.66
        lx, ly = _on(c, r * far, mid)
        if name and text:
            items += [label((lx, ly - 9), name), label((lx, ly + 9), text)]
        elif name or text:
            items.append(label((lx, ly), name or text))
        start += a
    items.append(point(c))
    return figure(W, height, alt_en, alt_ur, items)


# ---------- the mean: levelling counters ----------

DOT = 14   # distance between counters


def counter_columns(x0, y0, counts, *, hollow=None, gap=26):
    """Columns of counters standing on y0, one column per count. hollow:
    {column: how many counters at its top are drawn dashed (they move)}."""
    items = []
    hollow = hollow or {}
    for i, n in enumerate(counts):
        x = x0 + i * gap
        for k in range(n):
            moving = k >= n - hollow.get(i, 0)
            items.append(circle((x, y0 - DOT / 2 - k * DOT), 5.5, fill=not moving, dashed=moving))
    return items


def levelling_figure(before, alt_en, alt_ur):
    """Counters before and after sharing out fairly: columns `before`, an
    arrow, and every column at the mean. The counters that move are dashed."""
    n = len(before)
    m = sum(before) // len(before)
    assert m * n == sum(before)
    tallest = max(before)
    gap = 30
    panel = (n - 1) * gap
    y0 = tallest * DOT + 14
    lx = 28
    rx = W - 28 - panel
    moved_out = {i: v - m for i, v in enumerate(before) if v > m}
    moved_in = {i: m - v for i, v in enumerate(before) if v < m}
    items = counter_columns(lx, y0, before, hollow=moved_out, gap=gap)
    items.append(line((lx - 12, y0 - m * DOT), (lx + panel + 12, y0 - m * DOT), dashed=True))
    items += counter_columns(rx, y0, [m] * n, hollow=moved_in, gap=gap)
    mid = (lx + panel + rx) / 2
    items += arrow_right(mid - 18, mid + 18, y0 - m * DOT / 2)
    for i, v in enumerate(before):
        items.append(label((lx + i * gap, y0 + 14), v))
        items.append(label((rx + i * gap, y0 + 14), m))
    return figure(W, y0 + 28, alt_en, alt_ur, items)


def columns_figure(values, alt_en, alt_ur):
    """Columns of counters for each value, with the value under each."""
    gap = 32
    n = len(values)
    x0 = (W - (n - 1) * gap) / 2
    y0 = max(values) * DOT + 12
    items = counter_columns(x0, y0, values, gap=gap)
    for i, v in enumerate(values):
        items.append(label((x0 + i * gap, y0 + 14), v))
    return figure(W, y0 + 28, alt_en, alt_ur, items)


# ---------- number cards (median) ----------

CARD = 30


def cards(xc, y, values, *, ring=(), gap=8):
    """A row of number cards centred on xc, top at y. ring: positions
    with a circle drawn round the card."""
    n = len(values)
    total = n * CARD + (n - 1) * gap
    x = xc - total / 2
    items, centres = [], []
    for i, v in enumerate(values):
        cx = x + CARD / 2
        items += [rect(x, y, x + CARD, y + CARD), label((cx, y + CARD / 2), v)]
        if i in ring:
            items.append(circle((cx, y + CARD / 2), CARD / 2 + 6))
        centres.append(cx)
        x += CARD + gap
    return items, centres


def height_bars(values, alt_en, alt_ur, *, height=150, ring=(), texts=True):
    """Bars as tall as each value, in the order given, the value above each
    (like children standing in a line). ring: bars drawn empty."""
    n = len(values)
    slot = min(48, (W - 40) / n)
    bw = slot * 0.6
    x0 = (W - slot * n) / 2
    y0 = height - 10
    unit = (y0 - 34) / max(values)
    items = [line((x0 - 6, y0), (x0 + slot * n + 6, y0))]
    for i, v in enumerate(values):
        cx = x0 + slot * (i + 0.5)
        items.append(rect(cx - bw / 2, y0 - v * unit, cx + bw / 2, y0, fill=i not in ring))
        if texts:
            items.append(label((cx, y0 - v * unit - 12), v))
    return figure(W, height, alt_en, alt_ur, items)


# ---------- number lines and dot plots ----------

class Line:
    """A number line from lo to hi across the figure at height y."""

    def __init__(self, lo, hi, y, *, margin=22, width=W):
        self.lo, self.hi, self.y = lo, hi, y
        self.left, self.unit = margin, (width - 2 * margin) / (hi - lo)
        self.items = [line((self.x(lo) - 6, y), (self.x(hi) + 6, y))]

    def x(self, v):
        return self.left + (v - self.lo) * self.unit

    def ticks(self, values, labelled=None, size=5):
        labelled = values if labelled is None else labelled
        for v in values:
            self.items.append(line((self.x(v), self.y - size), (self.x(v), self.y + size)))
        for v in labelled:
            self.items.append(label((self.x(v), self.y + 18), v))

    def stacks(self, data, gap=13, radius=5):
        """A dot plot: one dot above the line for each value, repeats stacked."""
        seen = {}
        for v in data:
            k = seen.get(v, 0)
            seen[v] = k + 1
            self.items.append(circle((self.x(v), self.y - 11 - k * gap), radius, fill=True))

    def dots(self, data, *, texts=True, radius=6):
        """One dot on the line for each value, its number above it; labels
        that would touch are lifted onto a second row."""
        placed = []
        for v in sorted(data):
            self.items.append(circle((self.x(v), self.y), radius, fill=True))
            if texts:
                w = len(str(v)) * CHAR
                row = 0
                while any(r == row and abs(self.x(v) - px) < (w + pw) / 2 + 2 for px, pw, r in placed):
                    row += 1
                placed.append((self.x(v), w, row))
                self.items.append(label((self.x(v), self.y - 16 - row * 17), v))
        return max((r for _, _, r in placed), default=0)


# ---------- practice sets ----------

def with_fig(step, figure):
    step["figure"] = figure
    return step


def hbar_graph(values, cats, alt_en, alt_ur, *, top, step, width=W):
    """A horizontal bar graph: bars run to the right from the side axis, a
    short name (one or two letters or a number) for each at the left, and
    a number every `step` along the bottom."""
    row, ax, right = 30, 44, width - 16
    n = len(values)
    y0 = 14 + n * row
    unit = (right - ax) / top
    items = [line((ax, y0), (right, y0)), line((ax, y0), (ax, 8))]
    for v in range(0, top + 1, step):
        x = ax + v * unit
        items += [line((x, y0), (x, y0 + 4)), label((x, y0 + 16), v)]
    for i, v in enumerate(values):
        yc = 14 + i * row + row / 2
        items.append(label((ax - 16, yc), cats[i]))
        if v:
            items.append(rect(ax, yc - 9, ax + v * unit, yc + 9, fill=True))
    return figure(width, y0 + 28, alt_en, alt_ur, items)

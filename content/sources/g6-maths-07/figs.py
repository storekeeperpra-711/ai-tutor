"""Pictures for the Introduction to Algebra unit, built as lesson "figure"
blocks: bags of marbles (a bag stands for an unknown number, a marble for
1), algebra tiles (a tall tile for a letter, a small square for 1, dashed
for a minus), balance scales for equations, bar models for word problems,
number cards and tables for sequences, and matchstick and dot patterns.

Every figure is drawn in a box 300 wide, close to the size the app paints
it on a phone, so the 16 px labels keep their room. Coordinates are
rounded to 1 decimal place. Labels are numbers, letters or short terms
like 3x; the alt text says what each letter stands for. `figure` checks
that no two labels overlap and that every label keeps clear of the edge.
"""
import math

from common import T

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
    text = str(text).replace("-", "−")
    assert 1 <= len(text) <= 6, text
    return {"kind": "label", "at": pt(*at), "text": text}


def point(at):
    return {"kind": "point", "at": pt(*at)}


def arc(center, radius, start, sweep, dashed=False):
    item = {"kind": "arc", "center": pt(*center), "radius": r1(radius), "start": start, "sweep": sweep}
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
    return len(str(text)) * CHAR


def check_labels(items, width, height):
    """No two labels overlap, and each keeps clear of the edge."""
    boxes = []
    margin = 0.025 * max(width, height)
    for it in items:
        if it["kind"] != "label":
            continue
        x, y = it["at"]
        w = width_of(it["text"])
        assert margin <= x - w / 2 + 2 and x + w / 2 - 2 <= width - margin, ("label off the side", it["text"], x)
        assert margin <= y <= height - margin, ("label off the top or bottom", it["text"], y)
        boxes.append((x - w / 2, y - LABEL_H / 2, x + w / 2, y + LABEL_H / 2, it["text"]))
    for i, a in enumerate(boxes):
        for b in boxes[i + 1:]:
            apart = a[2] <= b[0] + 1 or b[2] <= a[0] + 1 or a[3] <= b[1] + 1 or b[3] <= a[1] + 1
            assert apart, ("labels overlap", a[4], b[4])


def check_inside(items, width, height):
    for it in items:
        reach = it.get("radius", 0)
        pts = [*it.get("points", []), *(it[k] for k in ("from", "to", "center", "at") if k in it)]
        for x, y in pts:
            assert reach <= x <= width - reach and reach <= y <= height - reach, (it, width, height)


def figure(width, height, alt_en, alt_ur, items):
    assert len(items) <= MAX_ITEMS, (alt_en, len(items))
    check_labels(items, width, height)
    check_inside(items, width, height)
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


def arrow_down(x, y0, y1):
    return [line((x, y0), (x, y1)), line((x - 5, y1 - 7), (x, y1)), line((x + 5, y1 - 7), (x, y1))]


def en_list(xs):
    xs = [str(x) for x in xs]
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


def ur_list(xs):
    xs = [str(x) for x in xs]
    return xs[0] if len(xs) == 1 else "، ".join(xs[:-1]) + " اور " + xs[-1]


def term_text(coef, var, first=True):
    """3x, x, −x, 5, −2; with first=False a + goes in front of a positive term."""
    body = var if (var and abs(coef) == 1) else f"{abs(coef)}{var}"
    sign = "−" if coef < 0 else ("" if first else "+")
    return sign + body


def expr_text(terms):
    return " ".join(term_text(c, v, i == 0) if i == 0 else ("− " if c < 0 else "+ ") + term_text(abs(c), v)
                    for i, (c, v) in enumerate(terms))


# ---------- a strip of things in a row (bags, marbles, words) ----------

BAG_W, BAG_H = 30, 36
MARBLE = 5.5
PITCH = 14         # distance between marbles


def bag(cx, yb, letter=None, dashed=False):
    """A sack standing on yb (its bottom), with the letter written on it."""
    w, h = BAG_W, BAG_H
    shape = [(-0.42, 0), (0.42, 0), (0.5, -0.2), (0.46, -0.5), (0.25, -0.72), (0.13, -0.8),
             (0.27, -1), (-0.27, -1), (-0.13, -0.8), (-0.25, -0.72), (-0.46, -0.5), (-0.5, -0.2)]
    items = [poly([(cx + a * w, yb + b * h) for a, b in shape], dashed=dashed),
             line((cx - 0.15 * w, yb - 0.8 * h), (cx + 0.15 * w, yb - 0.8 * h))]
    if letter:
        items.append(label((cx, yb - 0.36 * h), letter))
    return items


def marble_grid(x0, yb, n, cols=5, dashed=False, fill=True):
    """n marbles in rows of `cols`, the bottom row resting on yb, from x0."""
    items = []
    for i in range(n):
        r, c = divmod(i, cols)
        items.append(circle((x0 + MARBLE + c * PITCH, yb - MARBLE - r * PITCH), MARBLE, fill=fill and not dashed, dashed=dashed))
    return items


def marbles_width(n, cols=5):
    return (min(n, cols) - 1) * PITCH + 2 * MARBLE


def strip(tokens, yb, *, gap=10, width=W):
    """Things in a row, centred, standing on yb. Tokens:
    ('bag', letter), ('bags', k, letter), ('marbles', n), ('dmarbles', n)
    for dashed marbles (taken away), ('text', s) for a label, ('box', s) for a
    small box with s in it."""
    parts = []
    for tok in tokens:
        kind = tok[0]
        if kind == "bag":
            parts.append((BAG_W, lambda x, t=tok: bag(x + BAG_W / 2, yb, t[1])))
        elif kind == "bags":
            k = tok[1]
            w = k * BAG_W + (k - 1) * 6
            parts.append((w, lambda x, t=tok: sum((bag(x + BAG_W / 2 + i * (BAG_W + 6), yb, t[2]) for i in range(t[1])), [])))
        elif kind in ("marbles", "dmarbles"):
            n = tok[1]
            cols = tok[2] if len(tok) > 2 else 5
            parts.append((marbles_width(n, cols), lambda x, t=tok, c=cols: marble_grid(x, yb, t[1], c, dashed=t[0] == "dmarbles")))
        elif kind == "text":
            parts.append((width_of(tok[1]), lambda x, t=tok: [label((x + width_of(t[1]) / 2, yb - 12), t[1])]))
        else:
            raise ValueError(kind)
    total = sum(w for w, _ in parts) + gap * (len(parts) - 1)
    assert total <= width - 16, total
    x = (width - total) / 2
    items = []
    for w, draw in parts:
        items += draw(x)
        x += w + gap
    return items


def strip_figure(tokens, alt_en, alt_ur, *, height=None):
    tall = max([BAG_H if t[0] in ("bag", "bags") else 0 for t in tokens] +
               [math.ceil(t[1] / (t[2] if len(t) > 2 else 5)) * PITCH for t in tokens if t[0] in ("marbles", "dmarbles")] + [20])
    height = height or tall + 20
    return figure(W, height, alt_en, alt_ur, strip(tokens, height - 10))


# ---------- algebra tiles ----------

TILE_W, TILE_H, UNIT = 12, 34, 12
TILE_PITCH = 15


def tile(x, yb, var, letters, dashed=False):
    """One tile with its left side at x and bottom at yb: a tall filled tile
    for the first letter, a tall empty tile for the second, a small filled
    square for 1. A minus tile is dashed and not filled."""
    if var:
        first = var == letters[0]
        return rect(x, yb - TILE_H, x + TILE_W, yb, fill=first and not dashed, dashed=dashed)
    return rect(x, yb - UNIT, x + UNIT, yb, fill=not dashed, dashed=dashed)


def group_width(n):
    return (n - 1) * TILE_PITCH + TILE_W


def tile_row(segments, yb, letters, *, width=W, names=True, gap=12):
    """A row of tile groups, centred, standing on yb. segments: ('terms',
    [(coef, var), ...]) each term a group of |coef| tiles named above
    (like 3x); ('bracket', [...]) the same inside round brackets; ('op', s)
    a sign between; ('cross', [...]) tiles crossed out (taken away)."""
    pieces = []        # (width, draw(x) -> items)
    for seg in segments:
        kind = seg[0]
        if kind == "op":
            pieces.append((width_of(seg[1]), lambda x, s=seg[1]: [label((x + width_of(s) / 2, yb - 17), s)]))
            continue
        terms = seg[1]
        dashed_all = kind == "cross"
        inner = sum(group_width(abs(c)) for c, _ in terms) + gap * (len(terms) - 1)
        pad = 12 if kind == "bracket" else 0

        def draw(x, terms=terms, kind=kind, inner=inner, pad=pad, dashed_all=dashed_all):
            items = []
            gx = x + pad
            for i, (c, v) in enumerate(terms):
                for k in range(abs(c)):
                    items.append(tile(gx + k * TILE_PITCH, yb, v, letters, dashed=dashed_all or c < 0))
                if names:
                    top = yb - (TILE_H if v else UNIT) - 11
                    items.append(label((gx + group_width(abs(c)) / 2, top), term_text(c, v, i == 0)))
                gx += group_width(abs(c)) + gap
            if kind == "bracket":
                mid = yb - TILE_H / 2 - 8
                rad = 28
                items.append(arc((x + rad, mid), rad, 140, 80))
                items.append(arc((x + 2 * pad + inner - rad, mid), rad, -40, 80))
            if kind == "cross":
                items.append(line((x - 3, yb + 3), (x + inner + 3, yb - TILE_H - 3)))
            return items
        pieces.append((inner + 2 * pad, draw))
    total = sum(w for w, _ in pieces) + 10 * (len(pieces) - 1)
    assert total <= width - 14, (segments, total)
    x = (width - total) / 2
    items = []
    for w, draw in pieces:
        items += draw(x)
        x += w + 10
    return items


def tiles_figure(rows, letters, alt_en, alt_ur, *, names=True, between=None):
    """Rows of tile groups (see tile_row), one under the other.
    between: a label drawn between rows (like '='), or an arrow ('arrow')."""
    row_h = TILE_H + 32
    height = row_h * len(rows) + 8 + (22 * (len(rows) - 1) if between else 0)
    items = []
    y = 8
    for i, row in enumerate(rows):
        if i and between:
            if between == "arrow":
                items += arrow_down(W / 2, y + 2, y + 20)
            else:
                items.append(label((W / 2, y + 11), between))
            y += 22
        items += tile_row(row, y + row_h - 6, letters, names=names)
        y += row_h
    return figure(W, height, alt_en, alt_ur, items)


def tiles_en(letters):
    first = f"a tall shaded tile stands for {letters[0]}"
    second = f", a tall empty tile for {letters[1]}" if len(letters) > 1 else ""
    return f"({first}{second}, a small shaded square for 1, and a dashed tile is taken away)"


def tiles_ur(letters):
    first = f"لمبی رنگی ٹائل {letters[0]} ہے"
    second = f"، لمبی خالی ٹائل {letters[1]}" if len(letters) > 1 else ""
    return f"({first}{second}، چھوٹا رنگا مربع 1 ہے، اور ڈیش والی ٹائل نکالی جاتی ہے)"


# ---------- a balance scale ----------

def unit_grid(cx, yb, n, *, cols=5, dashed_from=None, size=11, gap=3):
    """n unit squares in rows of cols, centred on cx, bottom row on yb.
    The squares from index dashed_from on are dashed (taken away)."""
    cols = min(cols, n) if n else 1
    w = cols * size + (cols - 1) * gap
    items = []
    for i in range(n):
        r, c = divmod(i, cols)
        x = cx - w / 2 + c * (size + gap)
        y = yb - (r + 1) * size - r * gap
        dashed = dashed_from is not None and i >= dashed_from
        items.append(rect(x, y, x + size, y + size, fill=not dashed, dashed=dashed))
    return items


def side_width(tokens, cols=5):
    w = 0
    for tok in tokens:
        if tok[0] == "bags":
            w += tok[1] * BAG_W + (tok[1] - 1) * 4 + 8
        elif tok[0] in ("units",):
            c = min(tok[2] if len(tok) > 2 else cols, tok[1])
            w += c * 14 + 8
    return w - 8


def side(tokens, cx, yb):
    """Bags and unit squares standing on a pan, centred on cx.
    ('bags', k, letter), ('units', n[, cols[, dashed_from]])."""
    total = side_width(tokens)
    x = cx - total / 2
    items = []
    for tok in tokens:
        if tok[0] == "bags":
            for i in range(tok[1]):
                items += bag(x + BAG_W / 2, yb, tok[2])
                x += BAG_W + 4
            x += 4
        else:
            n = tok[1]
            cols = tok[2] if len(tok) > 2 else 5
            dashed_from = tok[3] if len(tok) > 3 else None
            c = min(cols, n)
            items += unit_grid(x + (c * 14 - 3) / 2, yb, n, cols=cols, dashed_from=dashed_from)
            x += c * 14 + 8
    return items


def balance(left, right, alt_en, alt_ur, *, under=None, cols=5):
    """A level balance: a beam on a stand, with a pan at each end and the
    left and right things standing on the pans. under: a label under the
    stand (like 'x=7')."""
    def tall(tokens):
        h = 0
        for tok in tokens:
            if tok[0] == "bags":
                h = max(h, BAG_H)
            else:
                c = tok[2] if len(tok) > 2 else cols
                rows = math.ceil(tok[1] / min(c, tok[1]))
                h = max(h, rows * 14)
        return h
    top = max(tall(left), tall(right)) + 10
    pan_y = top + 4
    beam_y = pan_y + 14
    foot = beam_y + 34
    height = foot + (30 if under else 8)
    lx, rx = 78, 222
    items = [line((30, beam_y), (270, beam_y)),
             poly([(150, beam_y), (136, foot), (164, foot)]),
             line((110, foot), (190, foot))]
    for cx in (lx, rx):
        items += [line((cx - 54, pan_y), (cx + 54, pan_y)), line((cx, pan_y), (cx, beam_y))]
    items += side(left, lx, pan_y)
    items += side(right, rx, pan_y)
    if under:
        items.append(label((150, foot + 16), under))
    return figure(W, height, alt_en, alt_ur, items)


# ---------- bar models ----------

def bar_model(rows, alt_en, alt_ur, *, total=None, total_value=None, names=None, bar_h=28, width=250):
    """Bars of boxes, one row under the other, all on the same scale.
    rows: [[(value, text, dashed), ...], ...]. total: a label over a bracket
    above the first row, spanning total_value (default the first row).
    names: a short label at the left of each row."""
    scale_max = max(total_value or 0, max(sum(v for v, _, _ in row) for row in rows))
    left = 24 if names else 0
    unit = (width - left) / scale_max
    x0 = (W - width) / 2 + left
    y = 34 if total else 8
    items = []
    if total:
        span = (total_value or sum(v for v, _, _ in rows[0])) * unit
        items += [line((x0, y - 8), (x0, y - 14)), line((x0, y - 14), (x0 + span, y - 14)),
                  line((x0 + span, y - 14), (x0 + span, y - 8)),
                  label((x0 + span / 2, y - 24), total)]
    for i, row in enumerate(rows):
        x = x0
        for v, text, dashed in row:
            items.append(rect(x, y, x + v * unit, y + bar_h, dashed=dashed))
            if text is not None:
                assert width_of(text) <= v * unit - 2, (text, v * unit)
                items.append(label((x + v * unit / 2, y + bar_h / 2), text))
            x += v * unit
        if names:
            items.append(label((x0 - 16, y + bar_h / 2), names[i]))
        y += bar_h + 10
    return figure(W, y, alt_en, alt_ur, items)


# ---------- sequences ----------

CARD = 34


def number_cards(values, alt_en, alt_ur, *, jumps=None):
    """A row of number cards with a curved jump between each pair; jumps:
    a label over each jump (or None for plain jumps)."""
    n = len(values)
    gap = 18
    total = n * CARD + (n - 1) * gap
    assert total <= W - 16
    x = (W - total) / 2
    top = 52 if jumps else 32
    items = []
    for i, v in enumerate(values):
        items += [rect(x, top, x + CARD, top + CARD), label((x + CARD / 2, top + CARD / 2), v)]
        if i < n - 1:
            a, b = x + CARD / 2, x + CARD + gap + CARD / 2
            rad = (b - a) / 2
            items.append(arc(((a + b) / 2, top + 2), rad, 200, 140))
            if jumps:
                items.append(label(((a + b) / 2, top - rad - 10), jumps[i]))
        x += CARD + gap
    return figure(W, top + CARD + 10, alt_en, alt_ur, items)


def seq_table(positions, terms, alt_en, alt_ur, *, heads=("n", "T")):
    """A two-row table: the positions on top, the terms under them."""
    n = len(positions)
    head_w = 30
    cell = min(44, (W - 24 - head_w) / n)
    width = head_w + n * cell
    x0 = (W - width) / 2
    h = 28
    items = [rect(x0, 8, x0 + width, 8 + 2 * h), line((x0, 8 + h), (x0 + width, 8 + h)),
             line((x0 + head_w, 8), (x0 + head_w, 8 + 2 * h)),
             label((x0 + head_w / 2, 8 + h / 2), heads[0]), label((x0 + head_w / 2, 8 + 1.5 * h), heads[1])]
    for i, (p, t) in enumerate(zip(positions, terms)):
        cx = x0 + head_w + (i + 0.5) * cell
        if i:
            items.append(line((x0 + head_w + i * cell, 8), (x0 + head_w + i * cell, 8 + 2 * h)))
        items += [label((cx, 8 + h / 2), p), label((cx, 8 + 1.5 * h), t)]
    return figure(W, 2 * h + 16, alt_en, alt_ur, items)


def matchsticks(counts, alt_en, alt_ur, *, texts=None, side=18):
    """Rows of matchstick squares: for each k in counts, k squares in a row
    (made of 3k + 1 sticks), with a text under each (or none)."""
    widths = [k * side for k in counts]
    gap = 22
    total = sum(widths) + gap * (len(counts) - 1)
    assert total <= W - 16
    x = (W - total) / 2
    top = 12
    items = []
    for k, w in zip(counts, widths):
        for i in range(k + 1):
            items.append(line((x + i * side, top), (x + i * side, top + side)))
        for i in range(k):
            items += [line((x + i * side, top), (x + (i + 1) * side, top)),
                      line((x + i * side, top + side), (x + (i + 1) * side, top + side))]
        if texts:
            items.append(label((x + w / 2, top + side + 16), texts.pop(0)))
        x += w + gap
    return figure(W, top + side + (32 if texts is not None else 12), alt_en, alt_ur, items)


def dot_squares(sizes, alt_en, alt_ur, *, sp=12):
    """For each k: a k by k square of dots, side by side."""
    widths = [(k - 1) * sp for k in sizes]
    gap = 34
    total = sum(widths) + gap * (len(sizes) - 1)
    x = (W - total) / 2
    big = max(widths)
    items = []
    for k, w in zip(sizes, widths):
        for r in range(k):
            for c in range(k):
                items.append(circle((x + c * sp, 12 + big - (k - 1 - r) * sp), 4, fill=True))
        x += w + gap
    assert len(items) <= MAX_ITEMS
    return figure(W, big + 24, alt_en, alt_ur, items)


# ---------- shapes ----------

def square_sides(text, alt_en, alt_ur, *, inside=None):
    s = 80
    x0, y0 = (W - s) / 2, 26
    items = [rect(x0, y0, x0 + s, y0 + s),
             label((x0 + s / 2, y0 - 12), text), label((x0 + s / 2, y0 + s + 12), text),
             label((x0 - 8 - width_of(text) / 2, y0 + s / 2), text),
             label((x0 + s + 8 + width_of(text) / 2, y0 + s / 2), text)]
    if inside:
        items.append(label((x0 + s / 2, y0 + s / 2), inside))
    return figure(W, y0 + s + 26, alt_en, alt_ur, items)


def triangle_sides(texts, alt_en, alt_ur):
    """A triangle with a label beside each side: left, right, bottom."""
    a, b, c = (150, 14), (70, 116), (230, 116)
    items = [poly([a, b, c])]
    left, right, bottom = texts
    items += [label(((a[0] + b[0]) / 2 - 12 - width_of(left) / 2, (a[1] + b[1]) / 2), left),
              label(((a[0] + c[0]) / 2 + 12 + width_of(right) / 2, (a[1] + c[1]) / 2), right),
              label((150, 132), bottom)]
    return figure(W, 144, alt_en, alt_ur, items)


def term_boxes(texts, alt_en, alt_ur):
    """Each term of an expression in its own box, in a row."""
    widths = [width_of(t) + 16 for t in texts]
    gap = 10
    total = sum(widths) + gap * (len(texts) - 1)
    x = (W - total) / 2
    items = []
    for t, w in zip(texts, widths):
        items += [rect(x, 10, x + w, 44), label((x + w / 2, 27), t)]
        x += w + gap
    return figure(W, 54, alt_en, alt_ur, items)


def dot_array(rows, cols, alt_en, alt_ur, *, sp=13):
    w = (cols - 1) * sp
    x0 = (W - w) / 2
    items = [circle((x0 + c * sp, 12 + r * sp), 4, fill=True) for r in range(rows) for c in range(cols)]
    return figure(W, 24 + (rows - 1) * sp, alt_en, alt_ur, items)


# ---------- fruit, eggs, pens ----------

def mango(cx, cy, dashed=False):
    return circle((cx, cy), 8, fill=not dashed, dashed=dashed)


def banana(cx, cy, dashed=False):
    """A banana: a thin crescent made of two arcs."""
    return [arc((cx, cy - 14), 16, 35, 110, dashed), arc((cx, cy - 20), 18, 50, 80, dashed)]


def egg_box(x, y, eggs=6):
    items = [rect(x, y, x + 52, y + 36)]
    for i in range(eggs):
        r, c = divmod(i, 3)
        items.append(circle((x + 10 + c * 16, y + 10 + r * 16), 5.5))
    return items


def pen(cx, yb, letter):
    items = [rect(cx - 5, yb - 50, cx + 5, yb - 10), poly([(cx - 5, yb - 10), (cx + 5, yb - 10), (cx, yb)])]
    items.append(label((cx, yb - 62), letter))
    return items

"""Pictures for the Ratio and Proportion unit, built as lesson "figure" blocks:
counters (filled and hollow dots) for ratios, bar models (strips of equal
boxes), double number lines for proportion and the unitary method, clock
faces for the 24-hour clock and roads for speed.

Every figure is about 300 to 340 wide, close to the size the app paints it
on a phone, so the 16 px labels keep their room. Coordinates are rounded to
1 decimal place.
"""
import math

from common import T

MAX_ITEMS = 60
ARROW = 6


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


def poly(points, fill=False, dashed=False):
    item = {"kind": "polygon", "points": [pt(*p) for p in points]}
    if fill:
        item["fill"] = True
    if dashed:
        item["style"] = "dashed"
    return item


def rect(x, y, w, h, fill=False, dashed=False):
    return poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], fill, dashed)


def circle(center, radius, fill=False):
    item = {"kind": "circle", "center": pt(*center), "radius": r1(radius)}
    if fill:
        item["fill"] = True
    return item


def arc(center, radius, start, sweep):
    return {"kind": "arc", "center": pt(*center), "radius": r1(radius), "start": start, "sweep": sweep}


def label_width(text):
    return 9.6 * len(str(text))


MIN_WIDTH = 300


def shift(items, dx):
    for it in items:
        for k in ("from", "to", "center", "at"):
            if k in it:
                it[k] = pt(it[k][0] + dx, it[k][1])
        if "points" in it:
            it["points"] = [pt(x + dx, y) for x, y in it["points"]]
    return items


def figure(width, height, alt_en, alt_ur, items):
    """A figure block; a narrow drawing is centred in a box MIN_WIDTH wide
    so it is not blown up on the screen."""
    assert len(items) <= MAX_ITEMS, (alt_en, len(items))
    if width < MIN_WIDTH:
        shift(items, (MIN_WIDTH - width) / 2)
        width = MIN_WIDTH
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
        by_id[sid]["figure"] = fig


def arrow_h(y, x0, x1):
    d = 1 if x1 > x0 else -1
    return [line((x0, y), (x1, y)),
            line((x1 - d * ARROW * 1.3, y - ARROW * 0.8), (x1, y)),
            line((x1 - d * ARROW * 1.3, y + ARROW * 0.8), (x1, y))]


def bracket_h(x0, x1, y, text=None, above=True):
    """A measuring line from x0 to x1 with end marks; its text above or below."""
    items = [line((x0, y), (x1, y)), line((x0, y - 5), (x0, y + 5)), line((x1, y - 5), (x1, y + 5))]
    if text:
        items.append(label(((x0 + x1) / 2, y - 13 if above else y + 14), text))
    return items


def bracket_v(x, y0, y1, text=None):
    """A vertical measuring line with end marks, its text to the right."""
    items = [line((x, y0), (x, y1)), line((x - 5, y0), (x + 5, y0)), line((x - 5, y1), (x + 5, y1))]
    if text:
        items.append(label((x + 8 + label_width(text) / 2, (y0 + y1) / 2), text))
    return items


# ---------- counters: filled dots for one thing, hollow dots for the other ----------

DOT_R = 7
DOT_SP = 20


def counters(rows, alt_en, alt_ur, *, sp=DOT_SP, r=DOT_R, extra=None, breaks=()):
    """rows: list of (count, filled, right_text). One row of dots each,
    with its count (or "?") written after the row. extra(x_end, ys) may
    return more items (for example a ratio written beside the rows)."""
    x0, y0, row_h = 16 + r, 18 + r, 2 * r + 14
    widest = max(n for n, _, _ in rows)
    x_text = x0 + (widest - 1) * sp + r + 12
    items, ys = [], []
    y = y0
    for i, (n, filled, text) in enumerate(rows):
        if i in breaks:
            items.append(line((16, y - row_h / 2), (x_text, y - row_h / 2), dashed=True))
            y += 12
        ys.append(y)
        items += [circle((x0 + k * sp, y), r, fill=filled) for k in range(n)]
        if text:
            items.append(label((x_text + label_width(text) / 2, y), text))
        y += row_h
    width = x_text + max(label_width(t or "") for _, _, t in rows) + 14
    if extra:
        more, width = extra(x_text + max(label_width(t or "") for _, _, t in rows), ys, width)
        items += more
    return figure(width, ys[-1] + r + 18, alt_en, alt_ur, items)


def ratio_beside(text):
    """For counters(extra=...): a bracket joining the rows and the ratio after it."""
    def extra(x_end, ys, width):
        x = x_end + 14
        items = [line((x, ys[0]), (x, ys[-1])), line((x - 5, ys[0]), (x, ys[0])), line((x - 5, ys[-1]), (x, ys[-1]))]
        items.append(label((x + 10 + label_width(text) / 2, (ys[0] + ys[-1]) / 2), text))
        return items, x + 10 + label_width(text) + 14
    return extra


def grouped_counters(rows, alt_en, alt_ur, *, a, b, sp=14, r=5, side_texts=None):
    """Each row holds `groups` copies of a group: a filled dots over b hollow
    dots, with a dashed box round each group. rows: list of (groups, text);
    the text goes after the row. side_texts: (filled, hollow) numbers
    written at the left of a single row."""
    x_left = 14 + (max(label_width(t) for t in side_texts) + 8 if side_texts else 0)
    gw = max(a, b) * sp + 4          # a group box's width
    gh = 2 * sp + 6
    gap = 8
    items = []
    widest = max(g for g, _ in rows)
    x_text = x_left + widest * (gw + gap) + 4
    y = 12
    for groups, text in rows:
        for g in range(groups):
            gx = x_left + g * (gw + gap)
            items.append(rect(gx, y, gw, gh, dashed=True))
            for k in range(a):
                items.append(circle((gx + 2 + sp / 2 + k * sp, y + 3 + sp / 2), r, fill=True))
            for k in range(b):
                items.append(circle((gx + 2 + sp / 2 + k * sp, y + 3 + 1.5 * sp), r))
        if text:
            items.append(label((x_text + label_width(text) / 2, y + gh / 2), text))
        if side_texts:
            items.append(label((14 + label_width(side_texts[0]) / 2, y + 3 + sp / 2), side_texts[0]))
            items.append(label((14 + label_width(side_texts[1]) / 2, y + 3 + 1.5 * sp), side_texts[1]))
        y += gh + 10
    width = x_text + max(label_width(t or "") for _, t in rows) + 14
    return figure(width, y + 2, alt_en, alt_ur, items)


# ---------- bar models: strips of equal boxes ----------

def bars(rows, alt_en, alt_ur, *, box=40, box_h=26, total=None, over=None, under=None, left=None):
    """rows: list of (boxes, inside, right_text, filled). inside is the text
    in every box (or a list, one per box, or None). right_text goes after
    the strip. total: text on a bracket at the right joining all rows.
    over: text on a bracket above the first row. under: text under each
    box of the first row (like "1kg"). left: a text before each row."""
    x0 = 16 + (max(label_width(t) for t in left) + 10 if left else 0)
    y = 16 + (28 if over else 0)
    gap = 12 + (18 if under else 0)
    widest = max(n for n, *_ in rows)
    x_right = x0 + widest * box
    items, ys = [], []
    for i, (n, inside, right, filled) in enumerate(rows):
        ys.append(y)
        for k in range(n):
            items.append(rect(x0 + k * box, y, box, box_h, fill=filled))
            text = inside[k] if isinstance(inside, list) else inside
            if text:
                items.append(label((x0 + (k + 0.5) * box, y + box_h / 2), text))
            if under and i == 0:
                items.append(label((x0 + (k + 0.5) * box, y + box_h + 14), under))
        if right:
            items.append(label((x0 + n * box + 10 + label_width(right) / 2, y + box_h / 2), right))
        if left:
            items.append(label((16 + label_width(left[i]) / 2, y + box_h / 2), left[i]))
        y += box_h + gap
    bottom = y - gap + (18 if under else 0)
    width = max(x0 + n * box + (10 + label_width(rt) if rt else 0) for n, _, rt, _ in rows) + 16
    if total:
        xb = width + 6
        items += bracket_v(xb, ys[0], ys[-1] + box_h, total)
        width = xb + 8 + label_width(total) + 16
    if over:
        n0 = rows[0][0]
        items += bracket_h(x0, x0 + n0 * box, ys[0] - 10, over)
    return figure(width, bottom + 14, alt_en, alt_ur, items)


def part_whole(values, texts, total_text, alt_en, alt_ur, *, width=300, box_h=30):
    """One strip split into parts as wide as values (the first part shaded),
    each part's text inside it and the whole on a bracket above."""
    x0, x1, y = 16, width - 16, 44
    whole = sum(values)
    items = bracket_h(x0, x1, y - 12, total_text)
    x = x0
    for i, (v, t) in enumerate(zip(values, texts)):
        w = (x1 - x0) * v / whole
        items.append(rect(x, y, w, box_h, fill=(i == 0)))
        items.append(label((x + w / 2, y + box_h / 2), t))
        x += w
    return figure(width, y + box_h + 14, alt_en, alt_ur, items)


# ---------- double number lines ----------

def double_line(a, b, n, marks, alt_en, alt_ur, *, tags=None, ticks=True, width=320, arrows=None):
    """Two number lines, one over the other: tick k stands for k × a on the
    top line and k × b on the bottom line (k = 0 .. n). marks: {k: (top
    text, bottom text)}; marked ticks get dots joined by a dashed line.
    tags: (top, bottom) short unit names written at the left.
    arrows: list of (k_from, k_to, text) drawn as jumps above the top line."""
    left = 16 + (max(label_width(t) for t in tags) + 10 if tags else 0)
    left = max(left, 22)
    right = width - 22
    unit = (right - left) / n
    top = 46 if arrows else 30
    y_top, y_bot = top + 16, top + 66

    def x(k):
        return left + k * unit

    items = [line((left, y_top), (right + 10, y_top)), line((left, y_bot), (right + 10, y_bot))]
    ks = range(n + 1) if ticks else sorted(set([0]) | set(marks))
    for k in ks:
        items += [line((x(k), y_top - 5), (x(k), y_top + 5)), line((x(k), y_bot - 5), (x(k), y_bot + 5))]
    for k in sorted(set([0]) | set(marks)):
        t, bt = marks.get(k, ("0", "0"))
        if k in marks and k != 0:
            items += [line((x(k), y_top + 8), (x(k), y_bot - 8), dashed=True),
                      point((x(k), y_top)), point((x(k), y_bot))]
        items += [label((x(k), y_top - 14), t), label((x(k), y_bot + 16), bt)]
    for tag, y in zip(tags or (), (y_top, y_bot)):
        if tag:
            items.append(label((16 + label_width(tag) / 2, y), tag))
    for k0, k1, text in arrows or []:
        xa, xb = x(k0), x(k1)
        h = min(abs(xb - xa) / 2, 18)
        cy = y_top - 24
        items += [arc((xa + h, cy), h, 180, 90), line((xa + h, cy - h), (xb - h, cy - h)), arc((xb - h, cy), h, 270, 90),
                  line((xb - 5, cy - 7), (xb, cy)), line((xb + 5, cy - 7), (xb, cy))]
        items.append(label(((xa + xb) / 2, cy - h - 10), text))
    return figure(width, y_bot + 30, alt_en, alt_ur, items)


# ---------- clocks ----------

def clock(hour, minute, ampm, display, alt_en, alt_ur):
    """A 12-hour clock face showing hour:minute, am/pm written under it, an
    arrow to a digital 24-hour display showing `display` (or "?")."""
    cx, cy, R = 82, 82, 64
    items = [circle((cx, cy), R)]
    for h in range(12):
        ang = math.radians(h * 30 - 90)
        items.append(line((cx + (R - 7) * math.cos(ang), cy + (R - 7) * math.sin(ang)),
                          (cx + R * math.cos(ang), cy + R * math.sin(ang))))
        num = 12 if h == 0 else h
        items.append(label((cx + (R - 18) * math.cos(ang), cy + (R - 18) * math.sin(ang)), str(num)))
    m_ang = math.radians(minute * 6 - 90)
    h_ang = math.radians((hour % 12) * 30 + minute * 0.5 - 90)
    items += [line((cx, cy), (cx + (R - 28) * math.cos(m_ang), cy + (R - 28) * math.sin(m_ang))),
              line((cx, cy), (cx + (R - 42) * math.cos(h_ang), cy + (R - 42) * math.sin(h_ang))),
              point((cx, cy)),
              label((cx, cy + R + 18), ampm)]
    dx, dy, dw, dh = 214, cy - 22, 92, 44
    items += arrow_h(cy, cx + R + 10, dx - 8)
    items += [rect(dx, dy, dw, dh, fill=True), label((dx + dw / 2, cy), display)]
    return figure(320, cy + R + 34, alt_en, alt_ur, items)


def day_line(alt_en, alt_ur):
    """The 24 hours of a day from midnight on a line, the afternoon and
    night half shaded: 24-hour times above, 12-hour times below."""
    left, right, y = 30, 290, 46
    unit = (right - left) / 24
    items = [rect(left + 12 * unit, y - 9, 12 * unit, 18, fill=True), line((left, y), (right, y))]
    for h in range(25):
        size = 7 if h % 6 == 0 else 4
        items.append(line((left + h * unit, y - size), (left + h * unit, y + size)))
    for h, top, bottom in ((0, "00:00", "12am"), (6, "06:00", "6am"), (12, "12:00", "12pm"), (18, "18:00", "6pm")):
        items += [label((left + h * unit, y - 22), top), label((left + h * unit, y + 24), bottom)]
    items.append(label((right, y + 24), "12am"))
    return figure(320, y + 44, alt_en, alt_ur, items)


def time_line(start, end, alt_en, alt_ur, *, jumps=True):
    """A line of hours from start's hour to the hour after end, the start
    and end times marked, and jumps: to the next whole hour, whole hours,
    then the minutes left over. start and end are (hour, minute)."""
    h0, h1 = start[0], end[0] + 1
    left, right, y = 22, 298, 62
    unit = (right - left) / (h1 - h0)

    def x(h, m=0):
        return left + (h - h0 + m / 60) * unit

    items = [line((left, y), (right, y))]
    for h in range(h0, h1 + 1):
        items += [line((x(h), y - 5), (x(h), y + 5)), label((x(h), y + 17), str(h))]
    for (h, m) in (start, end):
        items += [circle((x(h, m), y), 6, fill=True), label((x(h, m), y + 40), f"{h:02d}:{m:02d}")]
        items.append(line((x(h, m), y + 9), (x(h, m), y + 28), dashed=True))
    if jumps:
        stops = [(start, (h0 + 1, 0), f"{60 - start[1]}"),
                 ((h0 + 1, 0), (end[0], 0), f"{end[0] - h0 - 1}h"),
                 ((end[0], 0), end, f"{end[1]}")]
        for (a, b, text) in stops:
            xa, xb = x(*a), x(*b)
            hh = min((xb - xa) / 2, 16)
            items += [arc((xa + hh, y - 8), hh, 180, 90), line((xa + hh, y - 8 - hh), (xb - hh, y - 8 - hh)),
                      arc((xb - hh, y - 8), hh, 270, 90)]
            items.append(label(((xa + xb) / 2, y - 8 - hh - 11), text))
    return figure(320, y + 58, alt_en, alt_ur, items)


# ---------- roads ----------

def road(total, pieces, alt_en, alt_ur, *, piece_text=None, times=None, total_text=None, shown=None, width=320):
    """A road `total` long (drawn to scale) cut into `pieces` equal pieces.
    piece_text: written on each piece (str, or list). times: written above
    each piece end (like "1h"). total_text on a bracket under the road.
    shown: draw only the first `shown` pieces' marks (the rest is unknown)."""
    left, right = 16, width - 16
    y0, y1 = 44, 74
    unit = (right - left) / total
    step = total / pieces
    items = [line((left, y0), (right, y0)), line((left, y1), (right, y1)),
             line((left, (y0 + y1) / 2), (right, (y0 + y1) / 2), dashed=True)]
    # a small car at the start
    items += [rect(left + 4, y0 - 20, 30, 12, fill=True), circle((left + 11, y0 - 5), 4, fill=True),
              circle((left + 27, y0 - 5), 4, fill=True)]
    items.append(line((left, y0 - 6), (left, y1 + 6)))
    count = pieces if shown is None else shown
    for k in range(1, count + 1):
        xk = left + k * step * unit
        items.append(line((xk, y0 - 6), (xk, y1 + 6)))
        if times:
            items.append(label((xk, y0 - 16) if xk - left > 50 else (xk, y0 - 16), times[k - 1]))
    for k in range(count):
        text = piece_text[k] if isinstance(piece_text, list) else piece_text
        if text:
            items.append(label((left + (k + 0.5) * step * unit, y1 + 16), text))
    bottom = y1 + 26
    if total_text:
        items += bracket_h(left, right, bottom + 6, total_text, above=False)
        bottom += 36
    return figure(width, bottom + 6, alt_en, alt_ur, items)


def scale_bars(rows, alt_en, alt_ur, *, width=320, bar_h=20):
    """Bars drawn to scale: rows of (length, text, filled, ticks_every).
    The longest bar fills the width; text goes after the bar (or above
    its right end when the bar is the longest); ticks_every marks the bar
    in equal pieces."""
    longest = max(r[0] for r in rows)
    left = 16
    text_room = max(label_width(r[1]) for r in rows) + 14
    unit = (width - left - text_room - 10) / longest
    items, y = [], 16
    for length, text, filled, every in rows:
        w = length * unit
        items.append(rect(left, y, w, bar_h, fill=filled))
        if every:
            for k in range(every, length, every):
                items.append(line((left + k * unit, y), (left + k * unit, y + bar_h * 0.5)))
        items.append(label((left + w + 10 + label_width(text) / 2, y + bar_h / 2), text))
        y += bar_h + 16
    return figure(width, y, alt_en, alt_ur, items)


# ---------- flags (width to length 2 : 3) ----------

def flag(x, y, w, l, *, grid=None, w_text=None, l_text=None):
    """A flag l long and w wide with its top-left corner at (x, y): a
    shaded rectangle, a crescent-like circle on it, and grid=(rows, cols)
    lines cutting it into equal squares. w_text is written left of it,
    l_text under it."""
    items = [rect(x, y, l, w, fill=True)]
    if grid:
        rows, cols = grid
        items += [line((x + l * c / cols, y), (x + l * c / cols, y + w)) for c in range(1, cols)]
        items += [line((x, y + w * r / rows), (x + l, y + w * r / rows)) for r in range(1, rows)]
    if w_text:
        items.append(label((x - 8 - label_width(w_text) / 2, y + w / 2), w_text))
    if l_text:
        items.append(label((x + l / 2, y + w + 14), l_text))
    return items


def two_flags(small, big, alt_en, alt_ur):
    """A small flag and a big flag side by side, bottoms lined up.
    small, big: dicts with w, l (drawn size) and flag() keywords."""
    gap = 26
    xs = 16 + label_width(small.get("w_text") or "") + 8
    xb = xs + small["l"] + gap + label_width(big.get("w_text") or "") + 8
    base = 14 + big["w"]
    items = flag(xs, base - small["w"], small["w"], small["l"], **{k: v for k, v in small.items() if k not in ("w", "l")})
    items += flag(xb, base - big["w"], big["w"], big["l"], **{k: v for k, v in big.items() if k not in ("w", "l")})
    return figure(xb + big["l"] + 16, base + 30, alt_en, alt_ur, items)


# ---------- shadows ----------

def shadows(pole, pole_shadow, tree_shadow, alt_en, alt_ur, *, scale=6, tree_text="?"):
    """A pole and a tree standing on the ground, each with its shadow on
    the ground to its right and a dashed sun ray from its top to the end of
    its shadow. The tree's height follows from the same pole : shadow ratio."""
    tree = pole * tree_shadow / pole_shadow
    yg = 26 + tree * scale
    xp, xt = 56, 166
    items = [line((16, yg), (304, yg))]
    # the pole
    items += [rect(xp - 2, yg - pole * scale, 4, pole * scale, fill=True),
              rect(xp, yg - 3, pole_shadow * scale, 3, fill=True),
              line((xp, yg - pole * scale), (xp + pole_shadow * scale, yg), dashed=True),
              label((xp - 26, yg - pole * scale / 2), f"{pole}m"),
              label((xp + pole_shadow * scale / 2, yg + 16), f"{pole_shadow}m")]
    # the tree: trunk and a round top, as tall as `tree`
    top = yg - tree * scale
    rr = 18
    items += [rect(xt - 4, top + rr, 8, tree * scale - rr, fill=True), circle((xt, top + rr), rr, fill=True),
              rect(xt, yg - 3, tree_shadow * scale, 3, fill=True),
              line((xt, top), (xt + tree_shadow * scale, yg), dashed=True),
              line((xt - rr - 10, top), (xt - rr - 10, yg)), line((xt - rr - 15, top), (xt - rr - 5, top)),
              label((xt - rr - 26, yg - tree * scale / 2), tree_text),
              label((xt + tree_shadow * scale / 2, yg + 16), f"{tree_shadow}m")]
    return figure(320, yg + 32, alt_en, alt_ur, items)

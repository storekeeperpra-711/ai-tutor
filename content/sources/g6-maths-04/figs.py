"""Pictures for the Integers unit: number lines with jumps, thermometers,
lifts and area models, built as lesson "figure" blocks.

Every figure is drawn in a box about 300 wide, which is close to the size
the app paints it on a phone, so the 16 px labels keep their room.
Coordinates are rounded to 1 decimal place.
"""
from common import T, signed

W = 300            # figure width
MARGIN = 16        # room left and right of a number line
TICK = 5           # half a tick mark
LABEL_DY = 17      # number labels sit this far below the axis
HOP = 30           # the tallest a jump arc gets (longer jumps get a flat top)
ARROW = 6          # arrowhead size
MAX_ITEMS = 60


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
    return {"kind": "label", "at": pt(*at), "text": text}


def point(at):
    return {"kind": "point", "at": pt(*at)}


def arc(center, radius, start, sweep):
    return {"kind": "arc", "center": pt(*center), "radius": r1(radius), "start": start, "sweep": sweep}


def poly(points, fill=False):
    item = {"kind": "polygon", "points": [pt(*p) for p in points]}
    if fill:
        item["fill"] = True
    return item


def circle(center, radius, fill=False):
    item = {"kind": "circle", "center": pt(*center), "radius": r1(radius)}
    if fill:
        item["fill"] = True
    return item


def figure(width, height, alt_en, alt_ur, items):
    assert len(items) <= MAX_ITEMS, (alt_en, len(items))
    return {"width": r1(width), "height": r1(height), "alt": T(alt_en, alt_ur), "items": items}


def label_width(text):
    return 9.6 * len(text)


# ---------- horizontal number line ----------

class NumberLine:
    """A number line from lo to hi across the figure, its axis at height y.

    keys: numbers that are always labelled; other numbers are labelled
    every `every` steps when there is room. hide: numbers whose label is
    replaced (for example by "?")."""

    def __init__(self, lo, hi, y, *, keys=(), every=None, hide=(), ticks_every=1, width=W):
        self.lo, self.hi, self.y = lo, hi, y
        self.unit = (width - 2 * MARGIN) / (hi - lo)
        if every is None:
            # The same gap between all the numbers, wide enough for the widest.
            widest = max(label_width(signed(n)) for n in range(lo, hi + 1))
            every = next(k for k in (1, 2, 5, 10, 20, 50, 100) if k * self.unit >= widest + 6)
        self.items = [line((self.x(lo) - 8, y), (self.x(hi) + 8, y))]
        for n in range(lo, hi + 1):
            if (n - lo) % ticks_every == 0 or n in keys or n == 0:
                self.items.append(line((self.x(n), y - TICK), (self.x(n), y + TICK)))
        shown = [n for n in keys if lo <= n <= hi and n not in hide]
        if 0 not in hide and lo <= 0 <= hi and 0 not in shown:
            shown.append(0)
        for n in range(lo, hi + 1):
            if n in shown or n in hide or n % every:
                continue
            near_key = any(abs(n - m) < min(every, 2) for m in list(keys) + list(hide))
            if not near_key and all(self.fits(n, m) for m in shown + list(hide)):
                shown.append(n)
        for n in sorted(shown):
            self.items.append(label((self.x(n), y + LABEL_DY), signed(n)))

    def fits(self, n, m):
        """Labels of n and m do not run into each other."""
        room = (label_width(signed(n)) + label_width(signed(m))) / 2 + 6
        return abs(self.x(n) - self.x(m)) >= room

    def x(self, n):
        return MARGIN + (n - self.lo) * self.unit

    def mark(self, n, text=None):
        """A dot on n; text replaces its number label below (for "?")."""
        self.items += [circle((self.x(n), self.y), 7, fill=True), point((self.x(n), self.y))]
        if text:
            self.items.append(label((self.x(n), self.y + LABEL_DY), text))

    def jump(self, a, b, text=None, height=None):
        """An arc above the line from a to b with an arrowhead where it lands,
        and its size (e.g. +3) written above."""
        xa, xb, y = self.x(a), self.x(b), self.y
        half = abs(xb - xa) / 2
        h = height or min(half, HOP)
        left, right = min(xa, xb), max(xa, xb)
        if half <= h + 0.05:
            self.items.append(arc(((xa + xb) / 2, y), half, 180, 180))
            h = half
        else:
            self.items += [arc((left + h, y), h, 180, 90),
                           line((left + h, y - h), (right - h, y - h)),
                           arc((right - h, y), h, 270, 90)]
        tip = y - 8  # just above the dot where the jump lands
        self.items += [line((xb - ARROW * 0.8, tip - ARROW * 1.3), (xb, tip)),
                       line((xb + ARROW * 0.8, tip - ARROW * 1.3), (xb, tip))]
        if text:
            self.items.append(label(((xa + xb) / 2, y - h - 11), text))
        return h

    def bracket(self, a, b, text=None, above=True, off=14):
        """A dashed measuring line from a to b (a distance), with end marks."""
        yb = self.y - off if above else self.y + off + 14
        xa, xb = self.x(a), self.x(b)
        self.items += [line((xa, yb), (xb, yb), dashed=True),
                       line((xa, yb - 5), (xa, yb + 5)), line((xb, yb - 5), (xb, yb + 5))]
        if text:
            self.items.append(label(((xa + xb) / 2, yb - 12 if above else yb + 13), text))


def number_line_figure(alt_en, alt_ur, lines, height):
    items = []
    for nl in lines:
        items += nl.items
    return figure(W, height, alt_en, alt_ur, items)


def chain_line(lo, hi, moves, y, *, keys=(), every=None, end_text=None, start_dot=True, text_of=None, height=None, ticks_every=1,
               stop_labels=True):
    """A number line with a chain of moves: moves = [start, step1, step2, ...].
    The last landing point gets a dot, and end_text (like "?") in place of
    its number when given."""
    start, steps = moves[0], moves[1:]
    stops = [start]
    for st in steps:
        stops.append(stops[-1] + st)
    end = stops[-1]
    hide = (end,) if end_text else ()
    stop_keys = tuple(stops[:-1]) if stop_labels else (start,)
    nl = NumberLine(lo, hi, y, keys=tuple(keys) + stop_keys + (() if end_text else (end,)), every=every, hide=hide, ticks_every=ticks_every)
    h = height or chain_height(lo, hi, moves)
    if start_dot:
        nl.mark(start)
    for a, st in zip(stops, steps):
        nl.jump(a, a + st, (text_of or signed_change)(st), height=h)
    nl.mark(end, end_text)
    return nl


def chain_height(lo, hi, moves):
    """Every jump gets the same height, so a chain of jumps looks even."""
    unit = (W - 2 * MARGIN) / (hi - lo)
    return min(max(abs(st) for st in moves[1:]) * unit / 2, HOP)


def jumps_figure(lo, hi, moves, alt_en, alt_ur, **kw):
    """One number line with a chain of jumps (see chain_line)."""
    y = chain_height(lo, hi, moves) + 26
    nl = chain_line(lo, hi, moves, y, **kw)
    return figure(W, y + LABEL_DY + 14, alt_en, alt_ur, nl.items)


def chains_figure(lo, hi, chains, alt_en, alt_ur, *, end_texts=None, every=None, ticks_every=1):
    """Several number lines, one under the other, each with its chain of jumps."""
    items, y = [], 0
    for i, moves in enumerate(chains):
        y += chain_height(lo, hi, moves) + 26
        nl = chain_line(lo, hi, moves, y, end_text=end_texts[i] if end_texts else None, every=every,
                        ticks_every=ticks_every)
        items += nl.items
        y += LABEL_DY + 12
    return figure(W, y + 10, alt_en, alt_ur, items)


def signed_change(n):
    return f"+{n}" if n > 0 else signed(n)


# ---------- vertical scales: thermometers, sea level, lifts ----------

class Vertical:
    """A vertical number scale: n = hi at y=top, n = lo at y=bottom, the line at x."""

    def __init__(self, lo, hi, x, top, bottom):
        self.lo, self.hi, self.xx, self.top, self.bottom = lo, hi, x, top, bottom

    def y(self, n):
        return self.bottom - (n - self.lo) * (self.bottom - self.top) / (self.hi - self.lo)


def thermometer(cx, lo, hi, value, top, bottom, *, ticks_every=1, keys=(), every=None, show_value=True, value_text=None):
    """A thermometer at cx: tube from lo to hi, liquid up to value.
    Tick marks to the right, numbers right of them."""
    v = Vertical(lo, hi, cx, top, bottom)
    tube_top, tube_bottom = v.y(hi) - 8, v.y(lo) + 6
    bulb = (cx, tube_bottom + 11)
    items = [poly([(cx - 7, tube_top), (cx + 7, tube_top), (cx + 7, tube_bottom), (cx - 7, tube_bottom)]),
             circle(bulb, 12, fill=True),
             poly([(cx - 3.5, v.y(value)), (cx + 3.5, v.y(value)), (cx + 3.5, bulb[1]), (cx - 3.5, bulb[1])], fill=True)]
    for n in range(lo, hi + 1):
        if (n - lo) % ticks_every == 0 or n in keys or n == 0:
            long = 6 if n == 0 else 4
            items.append(line((cx + 7, v.y(n)), (cx + 7 + long, v.y(n))))
    shown = set(keys) | {0}
    if show_value:
        shown.add(value)
    if every:
        for n in range(lo, hi + 1):
            if n % every == 0 and all(abs(v.y(n) - v.y(m)) >= 19 for m in shown):
                shown.add(n)
    for n in sorted(shown):
        if lo <= n <= hi:
            text = value_text if (n == value and value_text) else signed(n)
            items.append(label((cx + 32, v.y(n)), text))
    return items, v


def arrow_v(x, y0, y1):
    """A straight vertical arrow from y0 to y1."""
    d = 1 if y1 > y0 else -1
    return [line((x, y0), (x, y1)),
            line((x - ARROW * 0.8, y1 - d * ARROW * 1.3), (x, y1)),
            line((x + ARROW * 0.8, y1 - d * ARROW * 1.3), (x, y1))]


def arrow_h(y, x0, x1):
    d = 1 if x1 > x0 else -1
    return [line((x0, y), (x1, y)),
            line((x1 - d * ARROW * 1.3, y - ARROW * 0.8), (x1, y)),
            line((x1 - d * ARROW * 1.3, y + ARROW * 0.8), (x1, y))]


def bracket_v(x, y0, y1, text=None, side=1):
    """A dashed vertical measuring line with end marks; its text to one side."""
    items = [line((x, y0), (x, y1), dashed=True), line((x - 5, y0), (x + 5, y0)), line((x - 5, y1), (x + 5, y1))]
    if text:
        items.append(label((x + side * (6 + label_width(text) / 2), (y0 + y1) / 2), text))
    return items


def building(floors_lo, floors_hi, *, lift=None, top=14, floor_h=24, x0=110, x1=230, label_x=80, labels=None, ground_extra=True):
    """A building cut open: one box per floor (floors_hi at the top), the
    ground floor 0 marked by the ground line. lift: floor where the lift
    car (a shaded box) is. Returns (items, y_of_floor_middle, bottom)."""
    items = []
    n = floors_hi - floors_lo + 1

    def y_mid(f):
        return top + (floors_hi - f) * floor_h + floor_h / 2

    for f in range(floors_lo, floors_hi + 1):
        y_top = top + (floors_hi - f) * floor_h
        items.append(poly([(x0, y_top), (x1, y_top), (x1, y_top + floor_h), (x0, y_top + floor_h)]))
        if labels is None or f in labels:
            items.append(label((label_x, y_mid(f)), signed(f)))
    ground_y = top + (floors_hi - 0) * floor_h + floor_h
    if ground_extra:
        items.append(line((20, ground_y), (W - 20, ground_y), dashed=True))
    if lift is not None:
        ly = y_mid(lift)
        items.append(poly([(x0 + 8, ly - 8), (x0 + 26, ly - 8), (x0 + 26, ly + 8), (x0 + 8, ly + 8)], fill=True))
    return items, y_mid, top + n * floor_h


# ---------- bars and area models ----------

def area_model(parts, side, inside, alt_en, alt_ur, *, height=70):
    """A rectangle `side` tall split into widths in `parts` (numbers);
    inside[i] is written in part i (or None)."""
    total = sum(parts)
    x0, x1, y0 = 46, W - 16, 32
    min_w = 58
    widths = [max(min_w, (x1 - x0) * p / total) for p in parts]
    scale = (x1 - x0) / sum(widths)
    widths = [w * scale for w in widths]
    items = []
    x = x0
    for i, (p, w) in enumerate(zip(parts, widths)):
        items.append(poly([(x, y0), (x + w, y0), (x + w, y0 + height), (x, y0 + height)], fill=True))
        items.append(label((x + w / 2, y0 - 14), signed(p)))
        if inside[i]:
            items.append(label((x + w / 2, y0 + height / 2), inside[i]))
        x += w
    items.append(label((x0 - 22, y0 + height / 2), signed(side)))
    return figure(W, y0 + height + 12, alt_en, alt_ur, items)


def bar_pattern(unders, ys, alt_en, alt_ur, *, unit=10, caption=None):
    """Bars for a pattern: bar i is ys[i] tall (up for positive, down for
    negative) from a base line, with its value at its end. unders[i] is
    written in a row under all the bars; caption (if any) starts that row."""
    hi = max(max(ys), 0)
    lo = min(min(ys), 0)
    base = 30 + hi * unit
    left = 10 + (label_width(caption) + 14 if caption else 0)
    gap = (W - 10 - left) / len(ys)
    items = [line((left, base), (W - 10, base))]
    row = base - lo * unit + (34 if lo < 0 else 20)
    for i, (u, yv) in enumerate(zip(unders, ys)):
        cx = left + gap * (i + 0.5)
        if yv:
            items.append(poly([(cx - 11, base), (cx + 11, base), (cx + 11, base - yv * unit), (cx - 11, base - yv * unit)], fill=True))
        end = base - yv * unit + (14 if yv < 0 else -14)
        items.append(label((cx, end), signed(yv)))
        items.append(label((cx, row), u))
    if caption:
        items.append(label((12 + label_width(caption) / 2, row), caption))
    return figure(W, row + 16, alt_en, alt_ur, items)


def vertical_line(lo, hi, x, top, bottom, *, keys=(), ticks_every=1, hide=()):
    """A vertical number line (up is positive) with numbers to its left."""
    v = Vertical(lo, hi, x, top, bottom)
    items = [line((x, v.y(hi) - 6), (x, v.y(lo) + 6))]
    for n in range(lo, hi + 1):
        if (n - lo) % ticks_every == 0 or n in keys or n == 0:
            items.append(line((x - 4, v.y(n)), (x + 4, v.y(n))))
    for n in sorted(set(keys) | {0}):
        if lo <= n <= hi and n not in hide:
            items.append(label((x - 8 - label_width(signed(n)) / 2, v.y(n)), signed(n)))
    return items, v


def with_figure(step, fig):
    """Add a figure to a step made by a helper (number_question and so on)."""
    step["figure"] = fig
    return step


def two_thermometers(lo, hi, a, b, alt_en, alt_ur, *, every=5, ticks_every=None, under=None, height=210):
    """Two thermometers side by side showing a and b; under: their captions."""
    top, bottom = 22, height - 62
    ia, _ = thermometer(80, lo, hi, a, top, bottom, ticks_every=ticks_every or every, keys=(a,), every=every)
    ib, v = thermometer(200, lo, hi, b, top, bottom, ticks_every=ticks_every or every, keys=(b,), every=every)
    items = ia + ib
    if under:
        cap_y = bottom + 6 + 11 + 12 + 16
        items += [label((80, cap_y), under[0]), label((200, cap_y), under[1])]
    return figure(W, height, alt_en, alt_ur, items), v


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


def thermometer_move(lo, hi, start, change, alt_en, alt_ur, *, every=5, height=220):
    """A thermometer showing start, and an arrow beside it for the change
    (up for warmer, down for colder) ending at a question mark."""
    top, bottom = 22, height - 40
    items, v = thermometer(110, lo, hi, start, top, bottom, ticks_every=1, keys=(start,), every=every)
    end = start + change
    ax = 200
    items += [line((110 + 54, v.y(start)), (ax - 6, v.y(start)), dashed=True)]
    items += arrow_v(ax, v.y(start), v.y(end))
    items.append(label((ax + 30, (v.y(start) + v.y(end)) / 2), signed_change(change)))
    items.append(label((ax, v.y(end) + (-12 if change > 0 else 12)), "?"))
    return figure(W, height, alt_en, alt_ur, items)


def gap_thermometer(lo, hi, high, low, alt_en, alt_ur, *, every=5, height=240):
    """A thermometer whose liquid reaches `high`, with `low` marked lower
    down and a dashed measuring line between them marked "?"."""
    items, v = thermometer(110, lo, hi, high, 22, height - 40, ticks_every=1, keys=(high, low), every=every)
    for n in (high, low):
        items.append(line((168, v.y(n)), (214, v.y(n)), dashed=True))
    items += bracket_v(222, v.y(high), v.y(low), "?")
    return figure(W, height, alt_en, alt_ur, items)

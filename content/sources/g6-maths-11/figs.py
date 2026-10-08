"""Pictures for the Percentages unit, built as lesson "figure" blocks:
hundred grids, strip (bar) models for a percent of an amount, percentage
bars (an amount scale on top, 0%-100% underneath) and before/after bars
for a percentage increase or decrease.

Every figure is drawn in a box 300 wide, close to the size the app paints
it on a phone, so the 16 px labels keep their room. Coordinates are
rounded to 1 decimal place.
"""
from math import gcd

from common import T

W = 300
MAX_ITEMS = 60
X0, X1 = 24, 276      # left and right end of strips and bars


def r1(v):
    return round(float(v) + 0.0, 1)


def pt(x, y):
    return [r1(x), r1(y)]


def line(a, b, dashed=False):
    item = {"kind": "line", "from": pt(*a), "to": pt(*b)}
    if dashed:
        item["style"] = "dashed"
    return item


def label(at, text):
    return {"kind": "label", "at": pt(*at), "text": text}


def rect(x0, y0, x1, y1, fill=False, dashed=False):
    item = {"kind": "polygon", "points": [pt(x0, y0), pt(x1, y0), pt(x1, y1), pt(x0, y1)]}
    if fill:
        item["fill"] = True
    if dashed:
        item["style"] = "dashed"
    return item


def figure(height, alt_en, alt_ur, items, width=W):
    assert len(items) <= MAX_ITEMS, (alt_en, len(items))
    return {"width": r1(width), "height": r1(height), "alt": T(alt_en, alt_ur), "items": items}


def label_width(text):
    return 9.6 * len(text)


def fit(x, text):
    """x moved in, if needed, so the whole label stays inside the picture."""
    half = label_width(text) / 2 + 3
    return min(max(x, half), W - half)


def spread(marks, y, gap=6, drop=16):
    """Labels at (x, text) on one row, placed in the order given; a label
    that would run into one already placed moves down a row."""
    items, placed = [], []
    for x, text in marks:
        x = fit(x, text)
        yy = y
        while any(py == yy and abs(x - px) < (label_width(text) + label_width(pt_)) / 2 + gap
                  for px, pt_, py in placed):
            yy += drop
        items.append(label((x, yy), text))
        placed.append((x, text, yy))
    return items


# ---------- a grid of 100 small squares ----------

def grid_items(n, x0, y0, size):
    """A 10 x 10 grid with the first n squares shaded, row by row from the
    top. Shaded blocks are drawn as polygons under the grid lines."""
    c = size / 10
    rows, rest = divmod(int(n), 10)
    items = []
    if rows:
        items.append(rect(x0, y0, x0 + size, y0 + rows * c, fill=True))
    if rest:
        items.append(rect(x0, y0 + rows * c, x0 + rest * c, y0 + (rows + 1) * c, fill=True))
    items.append(rect(x0, y0, x0 + size, y0 + size))
    for i in range(1, 10):
        items.append(line((x0 + i * c, y0), (x0 + i * c, y0 + size)))
        items.append(line((x0, y0 + i * c), (x0 + size, y0 + i * c)))
    return items


def hundred_grid(n, alt_en, alt_ur, shaded_text=None, rest_text=None):
    """One grid of 100 squares with n shaded. shaded_text is written to the
    right of the shaded rows, rest_text to the right of the rows left white."""
    x0, y0, size = 30, 12, 190
    c = size / 10
    items = grid_items(n, x0, y0, size)
    n = int(n)
    rows = n // 10
    lx = x0 + size + 40
    if shaded_text:
        y = y0 + (rows * c / 2 if rows else c / 2)
        items.append(label((lx, y), shaded_text))
    if rest_text:
        top = -(-n // 10)  # first row with no shaded square
        y = y0 + (top + (10 - top) / 2) * c if top < 10 else y0 + 9.5 * c
        items.append(label((lx, y), rest_text))
    return figure(y0 + size + 12, alt_en, alt_ur, items)


def two_grids(a, b, text_a, text_b, alt_en, alt_ur):
    """Two grids of 100 side by side with a and b shaded; a label under each."""
    size, y0 = 120, 10
    items = grid_items(a, 22, y0, size) + grid_items(b, 158, y0, size)
    items += [label((22 + size / 2, y0 + size + 16), text_a), label((158 + size / 2, y0 + size + 16), text_b)]
    return figure(y0 + size + 30, alt_en, alt_ur, items)


def battery(percent, alt_en, alt_ur):
    """A phone battery split into quarters, charged up to percent."""
    x0, x1, y0, y1 = 30, 250, 20, 90
    xf = x0 + (x1 - x0) * percent / 100
    items = [rect(x0, y0, xf, y1, fill=True), rect(x0, y0, x1, y1), rect(x1, 42, x1 + 14, 68, fill=True)]
    for q in (1, 2, 3):
        x = x0 + (x1 - x0) * q / 4
        items.append(line((x, y0), (x, y1), dashed=True))
    items.append(label(((x0 + xf) / 2, (y0 + y1) / 2), f"{percent}%"))
    return figure(110, alt_en, alt_ur, items)


# ---------- strip (bar) model: a percent of an amount ----------

def strip(whole, parts, shaded, alt_en, alt_ur, *, ask="shaded", inside=None, under=(), half=False):
    """A strip for the whole amount (labelled above, with a bracket), cut
    into `parts` equal parts with the first `shaded` parts shaded (and half
    of the next one when half=True). ask: put "?" on the "shaded" part, on
    the "rest", or nowhere (None). inside: a text written in every part.
    under: (fraction of the way along, text) marks under the strip, like
    (0, "0%"), (1, "100%")."""
    y_top, y_bot = 36, 76
    part = (X1 - X0) / parts
    end = X0 + part * (shaded + (0.5 if half else 0))
    items = [label(((X0 + X1) / 2, 13), whole),
             line((X0, 26), (X1, 26)), line((X0, 22), (X0, 30)), line((X1, 22), (X1, 30))]
    if end > X0:
        items.append(rect(X0, y_top, end, y_bot, fill=True))
    items.append(rect(X0, y_top, X1, y_bot))
    asked = {"shaded": (X0, end), "rest": (end, X1)}.get(ask)
    for i in range(1, parts):
        x = X0 + i * part
        if asked and asked[0] < x < asked[1]:
            # Short marks only, so the question mark in the middle is clear.
            items += [line((x, y_top), (x, y_top + 9)), line((x, y_bot - 9), (x, y_bot))]
        else:
            items.append(line((x, y_top), (x, y_bot)))
    if half:
        x = X0 + part * (shaded + 0.5)
        items.append(line((x, y_top), (x, y_bot), dashed=True))
    if inside:
        for i in range(parts):
            items.append(label((X0 + (i + 0.5) * part, (y_top + y_bot) / 2), inside))
    if ask == "shaded":
        items.append(label(((X0 + end) / 2, (y_top + y_bot) / 2), "?"))
    elif ask == "rest":
        items.append(label(((end + X1) / 2, (y_top + y_bot) / 2), "?"))
    marks = []
    for f, text in sorted(under, key=lambda m: m[0] not in (0, 1)):
        x = X0 + (X1 - X0) * f
        items.append(line((x, y_bot), (x, y_bot + 6)))
        marks.append((x, text))
    under_labels = spread(marks, y_bot + 18)
    for (x, _), lab in zip(marks, under_labels):
        if lab["at"][1] > y_bot + 18:  # moved down a row: a line leads to it
            items.append(line((x, y_bot + 6), (x, lab["at"][1] - 9)))
    items += under_labels
    low = max([y_bot - 4] + [it["at"][1] for it in items if it["kind"] == "label"])
    return figure(low + 14, alt_en, alt_ur, items)


# ---------- percentage bar: amounts on top, percents underneath ----------

def scale_bar(shade, top, bottom, alt_en, alt_ur, *, pieces=None, shade_from=0):
    """A bar from 0 to 1 shaded from shade_from to shade (fractions of the
    way along), with a scale above and one below: top and bottom are lists
    of (fraction of the way along, text). The bar is cut into `pieces`
    equal pieces when given."""
    y_top, y_bot = 34, 64
    xs = lambda f: X0 + (X1 - X0) * f
    items = []
    if shade > shade_from:
        items.append(rect(xs(shade_from), y_top, xs(shade), y_bot, fill=True))
    items.append(rect(X0, y_top, X1, y_bot))
    if pieces:
        for i in range(1, pieces):
            items.append(line((xs(i / pieces), y_top), (xs(i / pieces), y_bot)))
    for f in sorted({f for f, _ in top}):
        items.append(line((xs(f), y_top - 6), (xs(f), y_top)))
    for f in sorted({f for f, _ in bottom}):
        items.append(line((xs(f), y_bot), (xs(f), y_bot + 6)))
    # Labels above have no room to move up, so one that would clash moves
    # sideways instead; labels below move down a row.
    items += place_row([(xs(f), t) for f, t in top], 18)
    ends_first = sorted(bottom, key=lambda m: m[0] not in (0, 1))
    under = spread([(xs(f), t) for f, t in ends_first], y_bot + 16)
    for (f, _), lab in zip(ends_first, under):
        if lab["at"][1] > y_bot + 16:  # moved down a row: a line leads to it
            items.append(line((xs(f), y_bot + 6), (xs(f), lab["at"][1] - 9)))
    items += under
    low = max(it["at"][1] for it in items if it["kind"] == "label")
    return figure(low + 14, alt_en, alt_ur, items)


def percent_bar(part, whole, alt_en, alt_ur, *, top=None, bottom=None, divide=True):
    """A bar for the whole, shaded up to the part. Above it the amounts 0,
    part and whole; below it 0%, the part's percent (when given) and 100%.
    top replaces the part's amount label (for example with "?"). The bar
    is cut into equal pieces when that makes at most 25 of them."""
    f = part / whole
    pieces = whole // gcd(part, whole)
    bottom_marks = [(0, "0%"), (1, "100%")] + ([(f, bottom)] if bottom else [])
    return scale_bar(f, [(0, "0"), (f, top or str(part)), (1, str(whole))], bottom_marks, alt_en, alt_ur,
                     pieces=pieces if divide and pieces <= 25 else None)


def place_row(marks, y, gap=4):
    """Labels on one row; a label that would run into the one after it is
    pushed left (never past the one before it)."""
    marks = sorted(marks, key=lambda m: m[0])
    xs = [fit(*m) for m in marks]
    for i in range(len(marks) - 2, -1, -1):
        need = (label_width(marks[i][1]) + label_width(marks[i + 1][1])) / 2 + gap
        if xs[i + 1] - xs[i] < need:
            xs[i] = xs[i + 1] - need
    return [label((x, y), m[1]) for x, m in zip(xs, marks)]


# ---------- before and after bars: percentage increase and decrease ----------

def change_bars(old, new, alt_en, alt_ur, *, old_text, new_text, change_text=None, pct_text=None,
                quarters=False):
    """Two bars drawn to the same scale: the old amount (shaded) and, under
    it, the new amount. For an increase the extra piece is added on the end
    (not shaded); for a decrease the piece taken away is drawn dashed.
    old_text / new_text sit above the bars, pct_text to the right of the
    new bar and change_text under the piece that changed."""
    big = max(old, new)
    unit = (210 - X0) / big
    xo, xn = X0 + old * unit, X0 + new * unit
    a1, a2, b1, b2 = 24, 50, 82, 108
    items = [rect(X0, a1, xo, a2, fill=True)]
    if quarters:
        for q in (1, 2, 3):
            items.append(line((X0 + (xo - X0) * q / 4, a1), (X0 + (xo - X0) * q / 4, a2)))
    items.append(label(((X0 + xo) / 2, 13), old_text))
    if new >= old:
        items += [rect(X0, b1, xo, b2, fill=True), rect(xo, b1, xn, b2)]
        base = xo
    else:
        items += [rect(X0, b1, xn, b2, fill=True), rect(xn, b1, xo, b2, dashed=True)]
        base = xn
    lo, hi = sorted((xo, xn))
    items.append(line((xo, a2), (xo, b1), dashed=True))
    items.append(label(((X0 + base) / 2, b1 - 11), new_text))
    if pct_text:
        items.append(label((fit(hi + 10 + label_width(pct_text) / 2, pct_text), (b1 + b2) / 2), pct_text))
    if change_text:
        items.append(label(((lo + hi) / 2, b2 + 15), change_text))
    return figure(b2 + (30 if change_text else 12), alt_en, alt_ur, items)


def bars(old, new, *, unit="", ask="pct", quarters=False, show_change=None):
    """Before and after bars from old to new, drawn to the same scale. ask:
    which of "new" (the new amount) or "pct" (the percentage change) is
    the question mark; the other numbers are written on the picture."""
    old, new = int(old), int(new)
    up = new > old
    diff = abs(new - old)
    assert diff * 100 % old == 0
    pct = diff * 100 // old
    sign = "+" if up else "−"
    pre, post = ("Rs", "") if unit == "Rs" else ("", unit)
    txt = lambda n: f"{pre}{n}{post}"
    words_en = lambda n: f"Rs {n}" if unit == "Rs" else f"{n} {unit}".strip()
    words_ur = lambda n: f"{n} روپے" if unit == "Rs" else (f"{n} کلو" if unit == "kg" else str(n))
    new_text = "?" if ask == "new" else txt(new)
    pct_text = "?" if ask == "pct" else f"{sign}{pct}%"
    if show_change is None:
        show_change = ask != "new"
    change_text = f"{sign}{diff}" if show_change else None
    en = f"Two bars drawn to the same scale. The top bar, shaded, is the old amount, {words_en(old)}"
    ur = f"ایک ہی پیمانے پر بنی دو پٹیاں۔ اوپر والی رنگی ہوئی پٹی پرانی مقدار ہے، {words_ur(old)}"
    if quarters:
        en += ", cut into 4 equal parts"
        ur += "، جو 4 برابر حصوں میں بٹی ہے"
    if up:
        en += f". The bottom bar is the same bar with an extra piece added on the end, marked {pct_text} on its right"
        ur += f"۔ نیچے والی پٹی وہی پٹی ہے جس کے آخر میں ایک اضافی ٹکڑا جوڑا گیا ہے، اس کے دائیں طرف {pct_text} لکھا ہے"
    else:
        en += f". In the bottom bar a piece at the end is taken away (drawn dashed), marked {pct_text} on its right"
        ur += f"۔ نیچے والی پٹی میں آخر سے ایک ٹکڑا نکال دیا گیا ہے (ڈیش والی لکیروں سے بنا)، اس کے دائیں طرف {pct_text} لکھا ہے"
    if change_text:
        en += f", with {change_text} under it"
        ur += f"، اور اس کے نیچے {change_text}"
    if ask == "new":
        en += ". The new amount is a question mark."
        ur += "۔ نئی مقدار پر سوالیہ نشان ہے۔"
    else:
        en += f". The new amount is {words_en(new)}."
        ur += f"۔ نئی مقدار {words_ur(new)} ہے۔"
    if pct_text == "?":
        en = en.replace("marked ?", "marked with a question mark")
        ur = ur.replace("اس کے دائیں طرف ? لکھا ہے", "اس کے دائیں طرف سوالیہ نشان ہے")
    return change_bars(old, new, en, ur, old_text=txt(old), new_text=new_text, change_text=change_text,
                       pct_text=pct_text, quarters=quarters)


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

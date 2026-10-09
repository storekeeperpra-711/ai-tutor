"""Pictures for the Linear Equations unit: balance scales with boxes (the
unknown) and small weights of 1, bar models where two rows of the same
length stand for the two sides of an equation, bags (groups) for brackets
and "put the number in place of the letter" rows, built as lesson "figure"
blocks.

Every figure is drawn in a box 300 wide, close to the size the app paints
it on a phone, so the 16 px labels keep their room. Coordinates are
rounded to 1 decimal place. The alt text is written by the helpers from
the same numbers that are drawn, so the words and the picture agree.
"""
from common import T, solves

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


def arrow_down(x, y0, y1):
    return [line((x, y0), (x, y1)), line((x - 4, y1 - 6), (x, y1)), line((x + 4, y1 - 6), (x, y1))]


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
        assert "figure" not in by_id[sid], sid
        by_id[sid]["figure"] = fig


def step_says(lesson, sid, *texts):
    """Check that the step's English words contain each text (the equation
    the picture is drawn from), so the picture and the step use the same
    numbers."""
    steps = list(lesson["steps"])
    steps += [q["step"] for qs in lesson["question_bank"].values() for q in qs]
    steps += [q["step"] for q in lesson.get("review_questions", [])]
    step = next(s for s in steps if s["id"] == sid)
    words = " ".join(step[k]["en"] for k in ("prompt", "text", "task") if k in step)
    if "character" in step:
        words += " " + step["character"]["say"]["en"]
    for t in texts:
        assert t in words, (sid, t)


def en_list(xs):
    xs = [str(x) for x in xs]
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


def ur_list(xs):
    xs = [str(x) for x in xs]
    return xs[0] if len(xs) == 1 else "، ".join(xs[:-1]) + " اور " + xs[-1]


# ---------- balance scale ----------

BOX = 24          # a box standing for the unknown
UNIT_R = 7        # a small weight of 1
ROW_W = 122       # room on one pan (the pan top is 124 wide)


class Side:
    """What stands on one pan: `boxes` boxes marked `letter` (or marked
    `box_text` once a number is put in), `units` small weights of 1 (the
    last `gone` of them dashed, being taken away), and a big weight marked
    `block`."""

    def __init__(self, boxes=0, letter="x", units=0, block=None, box_text=None, gone=0):
        assert units <= 10 and gone <= units
        self.boxes, self.letter, self.units, self.block = boxes, letter, units, block
        self.box_text, self.gone = box_text, gone

    def tokens(self):
        out = [("box", self.box_text or self.letter, False)] * self.boxes
        if self.block is not None:
            out.append(("block", str(self.block), False))
        out += [("unit", "", k >= self.units - self.gone) for k in range(self.units)]
        return out

    def describe(self):
        en, ur = [], []
        if self.boxes:
            mark = self.box_text or self.letter
            if self.box_text:
                en.append(f"{self.boxes} box{'es' if self.boxes > 1 else ''} marked {mark} (the number put in for {self.letter})")
                ur.append(f"{mark} لکھے {self.boxes} ڈبے ({self.letter} کی جگہ رکھا گیا عدد)")
            else:
                en.append(f"{self.boxes} box{'es' if self.boxes > 1 else ''} marked {mark}, each box is the unknown {mark}")
                ur.append(f"{mark} لکھے {self.boxes} ڈبے، ہر ڈبہ نامعلوم {mark} ہے")
        if self.block is not None:
            en.append(f"a big weight marked {self.block}")
            ur.append(f"{self.block} لکھا ایک بڑا وزن")
        if self.units:
            en.append(f"{self.units} small weight{'s' if self.units > 1 else ''} of 1")
            ur.append(f"1 کے {self.units} چھوٹے وزن")
        e, u = "; ".join(en), "؛ ".join(ur)
        if self.gone:
            e += f" ({self.gone} of the small weights are dashed: they are taken away)"
            u += f" ({self.gone} چھوٹے وزن ڈیش والے ہیں: انہیں ہٹایا جا رہا ہے)"
        return e, u


def _size(kind, text):
    if kind == "box":
        return BOX, BOX
    if kind == "unit":
        return 2 * UNIT_R, 2 * UNIT_R
    return 16 + len(text) * CHAR, 28


def _rows(tokens):
    """Rows from the bottom up: the boxes first, then the big weight, then
    the small weights, each kind on rows of its own, split evenly (at most
    4 boxes or 6 small weights in a row)."""
    rows = []
    for kind, most in (("box", 4), ("block", 1), ("unit", 6)):
        mine = [t for t in tokens if t[0] == kind]
        if not mine:
            continue
        n = -(-len(mine) // most)
        size = -(-len(mine) // n)
        rows += [mine[i:i + size] for i in range(0, len(mine), size)]
    for r in rows:
        assert sum(_size(*t[:2])[0] for t in r) + 5 * (len(r) - 1) <= ROW_W, r
    return rows


def _row_h(row):
    return max(_size(*t[:2])[1] for t in row) + 6


def _draw_tokens(cx, base, tokens):
    items = []
    y = base
    for row in _rows(tokens):
        h = _row_h(row) - 6
        widths = [_size(*t[:2])[0] for t in row]
        x = cx - (sum(widths) + 5 * (len(row) - 1)) / 2
        for (kind, text, dashed), tw in zip(row, widths):
            if kind == "unit":
                items.append(circle((x + UNIT_R, y - UNIT_R - 1), UNIT_R, fill=not dashed, dashed=dashed))
            else:
                th = _size(kind, text)[1]
                items += [rect(x, y - th, x + tw, y, fill=kind == "block"), label((x + tw / 2, y - th / 2), text)]
            x += tw + 5
        y -= h + 6
    return items


def balance(left, right, alt_en="", alt_ur="", *, pre=None):
    """A level balance scale: Side `left` on the left pan and Side `right`
    on the right pan, with = between them. The alt text is written from the
    two sides; `pre` = (en, ur) is said first."""
    lt, rt = left.tokens(), right.tokens()
    stack = max(sum(_row_h(r) for r in _rows(t)) for t in (lt, rt))
    P = 12 + stack                         # top of the pans
    B = P + 24                             # the beam
    items = []
    for cx, toks in ((78, lt), (222, rt)):
        items += [poly([(cx - 62, P), (cx + 62, P), (cx + 52, P + 8), (cx - 52, P + 8)], fill=True),
                  line((cx, P + 8), (cx, B))]
        items += _draw_tokens(cx, P - 1, toks)
    items += [line((78, B), (222, B)), poly([(150, B), (130, B + 32), (170, B + 32)], fill=True),
              line((112, B + 32), (188, B + 32)), label((150, P - 12), "=")]
    le, lu = left.describe()
    re_, ru = right.describe()
    en = f"A level balance scale. On the left pan: {le}. On the right pan: {re_}."
    ur = f"ایک برابر ترازو۔ بائیں پلڑے میں: {lu}۔ دائیں پلڑے میں: {ru}۔"
    if pre:
        en, ur = pre[0] + " " + en, pre[1] + " " + ur
    if alt_en:
        en, ur = en + " " + alt_en, ur + " " + alt_ur
    return figure(W, B + 40, en, ur, items)


def balance_eq(a, letter, b, c, sol, **kw):
    """The balance for a·letter + b = c: a boxes and b small weights (a big
    weight when b > 10) on the left, a big weight c on the right. Checks
    that sol solves the equation."""
    eq = (f"{a if a > 1 else ''}{letter}" + (f" + {b}" if b else "") + f" = {c}")
    assert solves(eq, **{letter: sol}), eq
    left = Side(a, letter, units=b) if b <= 10 else Side(a, letter, block=b)
    return balance(left, Side(block=c), **kw), eq


# ---------- bar models ----------

ROW_H = 30
ROW_GAP = 12


def bars(rows, alt_en, alt_ur, *, groups=(), splits=()):
    """A bar model. rows = [[(size, text, style), ...], ...]; every row
    starts at the same left edge and is drawn to the same scale, so rows of
    equal total are equally long (the two sides of an equation). style:
    "" plain, "f" shaded, "d" dashed (taken away). groups = [(row, first
    part, last part + 1, text)]: a bracket under those parts with the text
    under it (text may be None). splits = [(row, part, n)]: dashed lines
    cutting that part into n equal pieces."""
    left, span = 20, W - 40
    unit = span / max(sum(p[0] for p in r) for r in rows)
    items, y = [], 10
    for ri, row in enumerate(rows):
        x = left
        edges = [x]
        for size, text, style in row:
            w = size * unit
            assert w >= len(str(text)) * CHAR + 8, (text, w)
            items.append(rect(x, y, x + w, y + ROW_H, fill=style == "f", dashed=style == "d"))
            if text != "":
                items.append(label((x + w / 2, y + ROW_H / 2), text))
            x += w
            edges.append(x)
        for r, p, n in splits:
            if r == ri:
                w = (edges[p + 1] - edges[p]) / n
                for k in range(1, n):
                    items.append(line((edges[p] + k * w, y), (edges[p] + k * w, y + ROW_H), dashed=True))
        y += ROW_H
        mine = [g for g in groups if g[0] == ri]
        for _, a, b, text in mine:
            x0, x1 = edges[a] + 3, edges[b] - 3
            items += [line((x0, y + 4), (x0, y + 10)), line((x0, y + 10), (x1, y + 10)), line((x1, y + 4), (x1, y + 10))]
            if text:
                items.append(label(((x0 + x1) / 2, y + 22), text))
        if mine:
            y += 30 if any(g[3] for g in mine) else 12
        y += ROW_GAP
    return figure(W, y - ROW_GAP + 10, alt_en, alt_ur, items)


def two_rows_alt(top, bottom, *, pre=("", ""), dashed=None):
    """Alt text for a two-row bar model: the parts of each row, in order."""
    en = f"{pre[0]} A bar model with two rows of the same length. Top row: {en_list(top)}. Bottom row: {en_list(bottom)}.".strip()
    ur = f"{pre[1]} دو برابر لمبی قطاروں والا پٹی ماڈل۔ اوپر کی قطار: {ur_list(top)}۔ نیچے کی قطار: {ur_list(bottom)}۔".strip()
    if dashed:
        en += f" The part {dashed} is dashed: it was taken away."
        ur += f" {dashed} والا حصہ ڈیش والا ہے: اسے نکالا گیا تھا۔"
    return en, ur


def plus_bar(a, letter, b, c, sol, *, pre=("", ""), top_text=None, sizes=None):
    """a·letter + b = c: the top row is c, the bottom row is a parts marked
    letter and a part b. Part lengths use the solution so the rows line
    up; nothing shows its value."""
    eq = (f"{a if a > 1 else ''}{letter}" + (f" + {b}" if b else "") + f" = {c}")
    assert solves(eq, **{letter: sol}), eq
    bottom = [(sol, letter, "f")] * a + ([(b, b, "")] if b else [])
    top = [(c, top_text or c, "")]
    en, ur = two_rows_alt([top_text or c], [letter] * a + ([b] if b else []), pre=pre)
    return bars([top, bottom], en, ur), eq


def minus_bar(a, letter, b, c, sol, *, pre=("", "")):
    """a·letter − b = c: the top row is a parts marked letter, the bottom
    row is c and a dashed part b (taken away)."""
    eq = f"{a if a > 1 else ''}{letter} − {b} = {c}"
    assert solves(eq, **{letter: sol}), eq
    top = [(sol, letter, "f")] * a
    bottom = [(c, c, ""), (b, b, "d")]
    en, ur = two_rows_alt([letter] * a, [c, b], pre=pre, dashed=b)
    return bars([top, bottom], en, ur), eq


# ---------- bags for brackets ----------

def bags(n, letter, k, alt_en, alt_ur, *, total=None):
    """n bags (dashed boxes), each holding a box marked letter and k small
    circles; `total` written after the last bag as "=total"."""
    cols = -(-k // 3)
    bw = 8 + BOX + 6 + cols * 16 + 6
    gap = 10
    tail = (len(f"={total}") * CHAR + 12) if total is not None else 0
    width = n * bw + (n - 1) * gap + tail
    assert width <= W - 12, width
    x = (W - width) / 2
    top, h = 12, 3 * 16 + 14
    items = []
    for _ in range(n):
        items.append(rect(x, top, x + bw, top + h, dashed=True))
        bx = x + 8
        items += [rect(bx, top + h / 2 - BOX / 2, bx + BOX, top + h / 2 + BOX / 2, fill=True),
                  label((bx + BOX / 2, top + h / 2), letter)]
        for i in range(k):
            c, r = divmod(i, 3)
            items.append(circle((bx + BOX + 6 + 8 + c * 16, top + 15 + r * 16), 6.5))
        x += bw + gap
    if total is not None:
        items.append(label((x - gap + tail / 2 + 2, top + h / 2), f"={total}"))
    return figure(W, top + h + 12, alt_en, alt_ur, items)


# ---------- put the number in place of the letter ----------

def put_in(expr, tokens, letter, val, *, pre=("", "")):
    """The top row is the expression expr drawn as boxes marked letter and short
    texts (like "+2"); arrows go down to the bottom row, where every box
    holds the number val."""
    def widths():
        return [BOX + 4 if t == letter else len(t) * CHAR + 8 for t in tokens]
    ws = widths()
    gap = 6
    x = (W - sum(ws) - gap * (len(ws) - 1)) / 2
    y0, y1 = 10, 72
    items = []
    for t, w in zip(tokens, ws):
        cx = x + w / 2
        if t == letter:
            items += [rect(x + 2, y0, x + 2 + BOX, y0 + BOX, fill=True), label((cx, y0 + BOX / 2), letter)]
            items += arrow_down(cx, y0 + BOX + 4, y1 - 4)
            items += [rect(x + 2, y1, x + 2 + BOX, y1 + BOX), label((cx, y1 + BOX / 2), val)]
        else:
            items += [label((cx, y0 + BOX / 2), t), label((cx, y1 + BOX / 2), t)]
        x += w + gap
    n = tokens.count(letter)
    shown = expr
    en = (f"{pre[0]} Top row: {shown} drawn with {n} shaded box{'es' if n > 1 else ''} for {letter}. "
          f"Arrows point down to the bottom row, the same but each box now holds {val}.").strip()
    ur = (f"{pre[1]} اوپر کی قطار: {shown}، جس میں {letter} کی جگہ {n} رنگین ڈبے ہیں۔ "
          f"تیر نیچے کی قطار کی طرف ہیں، جو ویسی ہی ہے مگر ہر ڈبے میں اب {val} ہے۔").strip()
    return figure(W, y1 + BOX + 10, en, ur, items)


def bracket_bar(n, letter, b, c, sol, *, minus=False, pre=("", ""), middle=False):
    """n(letter + b) = c, or n(letter − b) = c with minus: the top row is c,
    the bottom row n equal groups. A plus group is drawn as a part letter
    and a part b with a bracket under it marked letter+b (one part marked
    letter+b when b is too thin to label); a minus group is one part
    marked letter−b. middle: a row of n parts c ÷ n between them (divide
    both sides by n)."""
    sign = "−" if minus else "+"
    eq = f"{n}({letter} {sign} {b}) = {c}"
    assert solves(eq, **{letter: sol}), eq
    group = sol - b if minus else sol + b
    assert group * n == c
    name = f"{letter}{sign}{b}"
    unit = (W - 40) / c
    split = not minus and b * unit >= len(str(b)) * CHAR + 8
    rows, groups = [[(c, c, "")]], ()
    if middle:
        rows.append([(group, group, "")] * n)
    if split:
        rows.append([(sol, letter, "f"), (b, b, "")] * n)
        groups = [(len(rows) - 1, 2 * k, 2 * k + 2, name) for k in range(n)]
        parts_en = f"{n} equal groups; each group is a part {letter} and a part {b}, with a bracket under it marked {letter} {sign} {b}"
        parts_ur = f"{n} برابر گروہ؛ ہر گروہ میں ایک حصہ {letter} اور ایک حصہ {b} ہے، اور نیچے قوس پر {letter} {sign} {b} لکھا ہے"
    else:
        rows.append([(group, name, "f")] * n)
        parts_en = f"{n} equal parts, each marked {letter} {sign} {b}"
        parts_ur = f"{n} برابر حصے، ہر ایک پر {letter} {sign} {b} لکھا ہے"
    en = f"{pre[0]} A bar model for {eq}. Top row: {c}.".strip()
    ur = f"{pre[1]} {eq} کا پٹی ماڈل۔ اوپر کی قطار: {c}۔".strip()
    if middle:
        en += f" Middle row, the same length: {n} parts of {group} ({c} ÷ {n})."
        ur += f" درمیانی قطار، اتنی ہی لمبی: {group} کے {n} حصے ({c} ÷ {n})۔"
    en += f" Bottom row, the same length: {parts_en}."
    ur += f" نیچے کی قطار، اتنی ہی لمبی: {parts_ur}۔"
    return bars(rows, en, ur, groups=groups), eq


def rate_bar(rate, letter, fixed, total, sol, *, pre=("", ""), show=False):
    """rate·letter + fixed = total (a fixed charge plus so much for each):
    the top row is total, the bottom row the fixed part and one shaded part
    marked rate·letter. show: cut the shaded part into sol pieces of rate
    each, with a bracket under them marked rate·letter (for a worked
    example)."""
    eq = f"{rate}{letter} + {fixed} = {total}"
    assert solves(eq, **{letter: sol}), eq
    name = f"{rate}{letter}"
    en = f"{pre[0]} A bar model with two rows of the same length. Top row: {total}. Bottom row: {fixed}, then a shaded part {name}.".strip()
    ur = f"{pre[1]} دو برابر لمبی قطاروں والا پٹی ماڈل۔ اوپر کی قطار: {total}۔ نیچے کی قطار: {fixed}، پھر ایک رنگین حصہ {name}۔".strip()
    if show:
        rows = [[(total, total, "")], [(fixed, fixed, "")] + [(rate, "", "f")] * sol]
        en += f" The shaded part is cut into {sol} equal pieces of {rate}, with a bracket under them marked {name}."
        ur += f" رنگین حصہ {rate} کے {sol} برابر ٹکڑوں میں بٹا ہے، اور ان کے نیچے قوس پر {name} لکھا ہے۔"
        return bars(rows, en, ur, groups=[(1, 1, 1 + sol, name)]), eq
    return bars([[(total, total, "")], [(fixed, fixed, ""), (rate * sol, name, "f")]], en, ur), eq


def loose(a, letter, b, *, pre=("", "")):
    """An expression a·letter + b drawn as a boxes marked letter, a + and b
    small weights of 1, with no balance and no = (nothing to solve)."""
    items = []
    gap = 6
    width = a * BOX + (a - 1) * gap + 30 + b * 2 * UNIT_R + (b - 1) * gap
    x = (W - width) / 2
    y = 16
    for _ in range(a):
        items += [rect(x, y, x + BOX, y + BOX, fill=True), label((x + BOX / 2, y + BOX / 2), letter)]
        x += BOX + gap
    items.append(label((x + 9, y + BOX / 2), "+"))
    x += 30
    for _ in range(b):
        items.append(circle((x + UNIT_R, y + BOX / 2), UNIT_R, fill=True))
        x += 2 * UNIT_R + gap
    en = f"{pre[0]} {a} shaded boxes marked {letter}, a + sign and {b} small circles of 1. There is no = sign and no balance.".strip()
    ur = f"{pre[1]} {letter} لکھے {a} رنگین ڈبے، + کا نشان اور 1 کے {b} چھوٹے دائرے۔ نہ = کا نشان ہے نہ ترازو۔".strip()
    return figure(W, y + BOX + 16, en, ur, items)

"""Pictures for the Simplification unit: an expression with the order of
its steps drawn under it (each step a numbered bracket with its result),
groups of counters for "× before +", fraction bars for "of", bar models
for word problems and number lines for rounding, built as lesson "figure"
blocks.

Every figure is drawn in a box 300 wide, close to the size the app paints
it on a phone, so the 16 px labels keep their room. Coordinates are
rounded to 1 decimal place. The numbers in an expression picture are
worked out here from the same expression the step shows (checked against
the step's text), never typed twice.
"""
from decimal import Decimal as D
from fractions import Fraction as F

from common import T, dec

W = 300
MAX_ITEMS = 60
CHAR = 9.6         # about how wide one label character is


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
    text = str(text)
    assert 1 <= len(text) <= 6, text
    return {"kind": "label", "at": pt(*at), "text": text}


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


def step_text(lesson, sid):
    """The English prompt or text of a step, to check a picture against."""
    steps = list(lesson["steps"])
    steps += [q["step"] for qs in lesson["question_bank"].values() for q in qs]
    steps += [q["step"] for q in lesson.get("review_questions", [])]
    s = next(s for s in steps if s["id"] == sid)
    return (s.get("prompt") or s.get("text") or s.get("task"))["en"]


def en_list(xs):
    return ", ".join(str(x) for x in xs)


def ur_list(xs):
    return "، ".join(str(x) for x in xs)


def show(v):
    """A number as children write it: 3, 8.5, 1/2."""
    if isinstance(v, F):
        return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"
    if isinstance(v, D):
        return dec(v)
    return str(v)


def frac_items(x, y, v):
    """A fraction drawn the school way: numerator, a short line, denominator."""
    w = max(len(str(v.numerator)), len(str(v.denominator))) * CHAR + 4
    return [label((x, y - 10), v.numerator), line((x - w / 2, y), (x + w / 2, y)), label((x, y + 10), v.denominator)]


def num_items(x, y, v):
    if isinstance(v, F) and v.denominator != 1:
        return frac_items(x, y, v)
    return [label((x, y), show(v))]


def num_width(v):
    if isinstance(v, F) and v.denominator != 1:
        return max(len(str(v.numerator)), len(str(v.denominator))) * CHAR + 4
    return len(show(v)) * CHAR


# ---------- expressions and the order of their steps ----------

class N:
    """A number in an expression."""

    def __init__(self, value):
        self.value = value


class Op:
    """a op b, optionally inside brackets ('(', '{' or '[')."""

    def __init__(self, a, op, b, bracket=None):
        self.a, self.op, self.b, self.bracket = a, op, b, bracket

    @property
    def value(self):
        a, b = self.a.value, self.b.value
        if self.op == "+":
            return a + b
        if self.op == "−":
            return a - b
        if self.op in ("×", "of"):
            return a * b
        if self.op == "÷":
            q = F(a) / F(b) if not isinstance(a, D) else a / b
            return q
        raise ValueError(self.op)


def n(v):
    return v if isinstance(v, (N, Op)) else N(v)


def op(a, o, b):
    return Op(n(a), o, n(b))


def br(node, kind="("):
    node.bracket = kind
    return node


CLOSE = {"(": ")", "{": "}", "[": "]"}


def tokens(node):
    """The expression as tokens: (text or Fraction, node or None)."""
    if isinstance(node, N):
        return [(node.value, node)]
    inner = tokens(node.a) + [(node.op, None)] + tokens(node.b)
    if node.bracket:
        inner = [(node.bracket, None)] + inner + [(CLOSE[node.bracket], None)]
    return inner


def text_of(node):
    """The expression as the lesson writes it: 50 − {6 × (3 + 2)}."""
    out = ""
    for t, _ in tokens(node):
        s = show(t) if not isinstance(t, str) else t
        if out and not out.endswith(("(", "{", "[")) and s not in (")", "}", "]"):
            out += " "
        out += s
    return out


def order(node):
    """The operations in the order BODMAS does them (inside first, then
    left to right as the tree is built)."""
    if isinstance(node, N):
        return []
    return order(node.a) + order(node.b) + [node]


def inner_brackets(node):
    """How many bracketed parts sit inside this one."""
    if isinstance(node, N):
        return 0
    return sum((1 if isinstance(c, Op) and c.bracket else 0) + inner_brackets(c) for c in (node.a, node.b))


def plain(v):
    """A result as an int when it is whole."""
    if isinstance(v, F) and v.denominator == 1:
        return int(v)
    if isinstance(v, D) and v == v.to_integral_value():
        return int(v)
    return v


def steps_figure(expr, alt_en, alt_ur, *, results=True, boxes=True, prompt=None):
    """The expression in a row; under it, one numbered bracket for each
    step in the order it is done, with that step's result under it
    (or '?' when results=False). Brackets in the expression get a dashed
    box round them (boxes=True). prompt: the step's text, which must
    contain the expression exactly."""
    if prompt is not None:
        assert text_of(expr) in prompt, (text_of(expr), prompt)
    toks = tokens(expr)
    has_frac = any(isinstance(t, F) and t.denominator != 1 for t, _ in toks)
    widths = []
    for t, _ in toks:
        if isinstance(t, str):
            widths.append(13 if t in "(){}[]" else (len(t) * CHAR + 14 if t == "of" else 22))
        else:
            widths.append(num_width(t) + 8)
    total = sum(widths)
    assert total <= W - 30, text_of(expr)
    x = (W - total) / 2
    y0 = 24 if has_frac else 16
    items, spans, pos = [], {}, []
    for (t, node), w in zip(toks, widths):
        cx = x + w / 2
        pos.append((x, x + w))
        items += num_items(cx, y0, t) if not isinstance(t, str) else [label((cx, y0), t)]
        x += w

    # where each node's tokens start and end
    def span(node, i):
        if isinstance(node, N):
            spans[node] = (i, i)
            return i + 1
        start = i
        if node.bracket:
            i += 1
        i = span(node.a, i)
        i += 1
        i = span(node.b, i)
        if node.bracket:
            i += 1
        spans[node] = (start, i - 1)
        return i

    span(expr, 0)
    steps = order(expr)
    row_h = 40
    nest = max([inner_brackets(nd) for nd in steps if nd.bracket] or [0])
    boxed = boxes and any(nd.bracket for nd in steps)
    y0 += 4 * nest if boxed else 0
    top = y0 + (20 if has_frac else 12) + (6 + 4 * nest if boxed else 0)
    for k, node in enumerate(steps):
        i, j = spans[node]
        if node.bracket:
            if boxes:
                pad = 1 + 4 * inner_brackets(node)
                half = 21 if has_frac else 11
                items.append(rect(pos[i][0] - pad, y0 - half - pad, pos[j][1] + pad, y0 + half + pad, dashed=True))
            i, j = i + 1, j - 1
        x0, x1 = pos[i][0] + 3, pos[j][1] - 3
        y = top + 6 + k * row_h
        items += [line((x0, y - 6), (x0, y)), line((x0, y), (x1, y)), line((x1, y - 6), (x1, y))]
        cx = (x0 + x1) / 2
        v = plain(node.value)
        ry = y + 18
        if results:
            items += num_items(cx, ry, v)
            half = num_width(v) / 2
        else:
            items.append(label((cx, ry), "?"))
            half = CHAR / 2
        items += [circle((cx - half - 17, ry), 9), label((cx - half - 17, ry), k + 1)]
    height = top + 6 + (len(steps) - 1) * row_h + 18 + (14 if results and isinstance(plain(expr.value), F) else 0) + 16
    return figure(W, height, alt_en, alt_ur, items)


def steps_alt(expr, results=True):
    """Alt text for steps_figure, in English and Urdu."""
    steps = order(expr)
    en, ur = [], []
    for k, node in enumerate(steps, start=1):
        part = text_of(Op(node.a, node.op, node.b))
        if results:
            en.append(f"step {k}, under {part}, gives {show(plain(node.value))}")
            ur.append(f"قدم {k}، {part} کے نیچے، جواب {show(plain(node.value))}")
        else:
            en.append(f"step {k} is under {part}, with a question mark")
            ur.append(f"قدم {k}، {part} کے نیچے، سوالیہ نشان کے ساتھ")
    boxed = any(node.bracket for node in steps)
    box_en = " The brackets have a dashed box round them." if boxed else ""
    box_ur = " قوسین کے گرد ڈیش والا خانہ ہے۔" if boxed else ""
    return (f"The expression {text_of(expr)} with numbered brackets under it showing the order of the steps: " + "; ".join(en) + "." + box_en,
            f"عبارت {text_of(expr)}، اس کے نیچے نمبر والی بریکٹیں جو قدموں کی ترتیب دکھاتی ہیں: " + "؛ ".join(ur) + "۔" + box_ur)


def steps_fig(expr, prompt=None, results=True):
    return steps_figure(expr, *steps_alt(expr, results), results=results, prompt=prompt)


def two_steps_figs(e1, e2, alt_en, alt_ur):
    """Two expression pictures one under the other, with their results."""
    f1 = steps_figure(e1, "", "")
    f2 = steps_figure(e2, "", "")
    items = list(f1["items"])
    dy = f1["height"] + 6
    items.append(line((20, dy - 3), (W - 20, dy - 3), dashed=True))
    for it in f2["items"]:
        it = dict(it)
        for k in ("from", "to", "center", "at"):
            if k in it:
                it[k] = pt(it[k][0], it[k][1] + dy)
        if "points" in it:
            it["points"] = [pt(x, y + dy) for x, y in it["points"]]
        items.append(it)
    return figure(W, dy + f2["height"], alt_en, alt_ur, items)


# ---------- groups of counters ----------

def groups_figure(singles, groups, each, alt_en, alt_ur):
    """`singles` loose counters, a + sign, then `groups` rings each holding
    `each` counters (so groups × each)."""
    gap, r = 13, 4.5
    cols = each if each <= 3 else -(-each // 2)
    rows = -(-each // cols)
    ring_w = (cols - 1) * gap + 22
    ring_h = (rows - 1) * gap + 22
    loose_w = (singles - 1) * gap
    total = loose_w + 40 + groups * ring_w + (groups - 1) * 8
    x = (W - total) / 2
    yc = 14 + ring_h / 2
    items = [circle((x + k * gap, yc), r, fill=True) for k in range(singles)]
    x += loose_w + 20
    items.append(label((x, yc), "+"))
    x += 20
    for g in range(groups):
        items.append(rect(x, yc - ring_h / 2, x + ring_w, yc + ring_h / 2, dashed=True))
        for k in range(each):
            i, j = divmod(k, cols)
            items.append(circle((x + 11 + j * gap, yc - ring_h / 2 + 11 + i * gap), r, fill=True))
        x += ring_w + 8
    return figure(W, ring_h + 28, alt_en, alt_ur, items)


# ---------- bars: fractions and bar models ----------

def bar_model(segments, alt_en, alt_ur, *, left=20, width=W - 40, total_text=None, split=None, shade=(), parts=None,
              split_from=0, under=()):
    """A bar made of segments (value, text, dashed) side by side, as long as
    their values, with each text inside. total_text: written above the
    whole bar with a bracket. split: a second bar under the first, just as
    long, cut into `split` equal parts (dashed), with parts[k] written in
    part k (None for nothing); the parts in shade are filled. split_from:
    the second bar starts under this value instead (to split only the rest).
    under: (from, to, text) brackets drawn under the bar with their text."""
    total = sum(v for v, _, _ in segments)
    s = width / total
    y0 = 40 if total_text is not None else 14
    bh = 32
    items = []
    x = left
    for v, text, dashed in segments:
        items.append(rect(x, y0, x + v * s, y0 + bh, dashed=dashed))
        if text is not None:
            items.append(label((x + v * s / 2, y0 + bh / 2), text))
        x += v * s
    if total_text is not None:
        items += [line((left, y0 - 8), (left, y0 - 14)), line((left, y0 - 14), (left + width, y0 - 14)),
                  line((left + width, y0 - 14), (left + width, y0 - 8)), label((left + width / 2, y0 - 26), total_text)]
    h = y0 + bh + 12
    for a, b, text in under:
        xa, xb, yb = left + a * s, left + b * s, y0 + bh + 14
        items += [line((xa, yb - 6), (xa, yb)), line((xa, yb), (xb, yb)), line((xb, yb - 6), (xb, yb)),
                  label(((xa + xb) / 2, yb + 13), text)]
        h = yb + 28
    if split:
        y1 = y0 + bh + 14
        start = left + split_from * s
        pw = (left + width - start) / split
        for k in range(split):
            items.append(rect(start + k * pw, y1, start + (k + 1) * pw, y1 + bh, fill=k in shade, dashed=k not in shade))
            if parts and parts[k] is not None:
                items.append(label((start + (k + 0.5) * pw, y1 + bh / 2), parts[k]))
        h = y1 + bh + 12
    return figure(W, h, alt_en, alt_ur, items)


def frac_bar(frac, whole, alt_en, alt_ur, *, part_texts=True, shaded_text=None):
    """frac of whole: a bar for whole cut into frac.denominator equal parts,
    frac.numerator of them shaded; each part's size inside it (part_texts),
    whole written above, and shaded_text under the shaded parts."""
    k = frac.denominator
    part = F(whole) / k
    s = W - 60
    x0, y0, bh = 30, 40, 32
    items = []
    for i in range(frac.numerator):
        items.append(rect(x0 + i * s / k, y0, x0 + (i + 1) * s / k, y0 + bh, fill=True))
    items.append(rect(x0, y0, x0 + s, y0 + bh))
    for i in range(1, k):
        items.append(line((x0 + i * s / k, y0), (x0 + i * s / k, y0 + bh)))
    if part_texts:
        for i in range(k):
            items.append(label((x0 + (i + 0.5) * s / k, y0 + bh / 2), show(part)))
    items += [line((x0, y0 - 8), (x0, y0 - 14)), line((x0, y0 - 14), (x0 + s, y0 - 14)),
              line((x0 + s, y0 - 14), (x0 + s, y0 - 8)), label((x0 + s / 2, y0 - 26), show(whole))]
    h = y0 + bh + 12
    if shaded_text is not None:
        xs = x0 + frac.numerator * s / k
        items += [line((x0, y0 + bh + 8), (x0, y0 + bh + 14)), line((x0, y0 + bh + 14), (xs, y0 + bh + 14)),
                  line((xs, y0 + bh + 8), (xs, y0 + bh + 14)), label(((x0 + xs) / 2, y0 + bh + 28), shaded_text)]
        h += 30
    return figure(W, h, alt_en, alt_ur, items)


# ---------- rounding on a number line ----------

def round_lines(rows, alt_en, alt_ur, *, arrows=False):
    """One short number line per row = (value, lo, hi): lo, the halfway
    mark (dashed) and hi written under it, small ticks for each tenth of
    the gap, and the value as a dot with its number above. arrows: an
    arrow from the value to the end it rounds to."""
    items = []
    y = 40
    left, right = 40, W - 40
    for value, lo, hi in rows:
        value, lo, hi = D(str(value)), D(str(lo)), D(str(hi))
        assert lo < value < hi
        unit = (right - left) / float(hi - lo)

        def x(v):
            return left + float(v - lo) * unit

        mid = (lo + hi) / 2
        items.append(line((left - 8, y), (right + 8, y)))
        for k in range(11):
            v = lo + (hi - lo) * k / 10
            size = 7 if k in (0, 10) else 3
            items.append(line((x(v), y - size), (x(v), y + size)))
        items.append(line((x(mid), y - 12), (x(mid), y + 8), dashed=True))
        for v in (lo, mid, hi):
            if v != value:          # the value is written above already
                items.append(label((x(v), y + 18), dec(v)))
        items.append(circle((x(value), y), 5, fill=True))
        items.append(label((x(value), y - 24), dec(value)))
        if arrows:
            to = hi if value >= mid else lo
            a, b = x(value), x(to)
            sign = 1 if b > a else -1
            yy = y - 10
            items += [line((a + sign * 7, yy), (b, yy)), line((b - sign * 6, yy - 4), (b, yy)), line((b - sign * 6, yy + 4), (b, yy))]
        y += 70
    return figure(W, y - 70 + 32, alt_en, alt_ur, items)


def round_alt(rows, arrows=False):
    en, ur = [], []
    for value, lo, hi in rows:
        mid = (D(str(lo)) + D(str(hi))) / 2
        to = hi if D(str(value)) >= mid else lo
        a_en = f", with an arrow to {dec(to)}" if arrows else ""
        a_ur = f"، اور ایک تیر {dec(to)} کی طرف" if arrows else ""
        on_mid = D(str(value)) == mid
        en.append(f"a number line from {dec(lo)} to {dec(hi)} with the halfway mark {dec(mid)} dashed, and {dec(value)} marked as a dot" + (" right on the halfway mark" if on_mid else "") + a_en)
        ur.append(f"{dec(lo)} سے {dec(hi)} تک عددی لکیر، درمیانی نشان {dec(mid)} ڈیش والا، اور {dec(value)} ایک نقطے سے دکھایا گیا" + (" جو ٹھیک درمیانی نشان پر ہے" if on_mid else "") + a_ur)
    return ("Rounding: " + "; ".join(en) + ".", "قریب ترین عدد تک لانا: " + "؛ ".join(ur) + "۔")


def round_fig(rows, arrows=False):
    return round_lines(rows, *round_alt(rows, arrows), arrows=arrows)

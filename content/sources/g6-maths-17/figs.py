"""Pictures for the Probability unit: dice faces, coins, bags of balls,
spinners, letter cards, grids of tickets or children, the two-coin table
and the 0 to 1 likelihood line, built as lesson "figure" blocks.

Every figure is drawn in a box 300 wide, close to the size the app paints
it on a phone, so the 16 px labels keep their room. Coordinates are
rounded to 1 decimal place. The pictures are drawn from the same sample
spaces (lists of outcomes) that the steps count, and the alt text is
written from them too, so the words and the picture agree. Colours are
shown by a letter on each ball (and a shaded ball for the first colour);
the alt text says which letter is which colour.
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
    """Check that the step's English words contain each text, so the
    picture and the step tell the same story."""
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


def _on(c, r, deg):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] + r * math.sin(math.radians(deg)))


# ---------- dice ----------

PIPS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)],
        4: [(-1, -1), (1, -1), (-1, 1), (1, 1)], 5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)],
        6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}


def die_face(x, y, s, n):
    """A dice face with n pips (dark dots), top left corner (x, y), side s."""
    items = [rect(x, y, x + s, y + s)]
    c, d = (x + s / 2, y + s / 2), s * 0.28
    for i, j in PIPS[n]:
        items.append(point((c[0] + i * d, c[1] + j * d)))
    return items


def dice_faces(faces, *, ring=(), pre=("", "")):
    """A row of dice faces; the faces in `ring` have a dashed box round
    them."""
    s, gap = 40, 8
    x = (W - len(faces) * s - (len(faces) - 1) * gap) / 2
    items = []
    for n in faces:
        items += die_face(x, 14, s, n)
        if n in ring:
            items.append(rect(x - 3, 11, x + s + 3, 14 + s + 3, dashed=True))
        x += s + gap
    en = f"{pre[0]} {len(faces)} dice faces in a row, showing {en_list(faces)} dots.".strip()
    ur = f"{pre[1]} پانسے کے {len(faces)} رخ ایک قطار میں، جن پر {ur_list(faces)} نقطے ہیں۔".strip()
    if ring:
        en += f" The faces {en_list(sorted(ring))} have a dashed box round them."
        ur += f" {ur_list(sorted(ring))} والے رخوں کے گرد ڈیش والا ڈبہ ہے۔"
    return figure(W, 14 + s + 14, en, ur, items)


def dice_cube(pre=("", "")):
    """One dice drawn as a cube: 5 dots on the front, 3 on top and 2 on
    the side (opposite faces of a dice add up to 7, so these three can be
    seen together)."""
    s, d = 64, 22
    x, y = (W - s - d) / 2, 10 + d
    items = die_face(x, y, s, 5)
    top = [(x, y), (x + d, y - d), (x + s + d, y - d), (x + s, y)]
    side = [(x + s, y), (x + s + d, y - d), (x + s + d, y + s - d), (x + s, y + s)]
    items += [poly(top), poly(side)]

    def on(face, u, v):          # u, v in 0..1 across a slanted face
        a, b, _, dd = face
        return (a[0] + u * (dd[0] - a[0]) + v * (b[0] - a[0]), a[1] + u * (dd[1] - a[1]) + v * (b[1] - a[1]))
    for u, v in ((0.25, 0.25), (0.5, 0.5), (0.75, 0.75)):
        items.append(point(on(top, u, v)))
    for u, v in ((0.3, 0.3), (0.7, 0.7)):
        cx, cy = on([(x + s, y + s), (x + s + d, y + s - d), None, (x + s, y)], u, v)
        items.append(point((cx, cy)))
    en = f"{pre[0]} One dice drawn as a cube. The front shows 5 dots, the top 3 dots and the side 2 dots.".strip()
    ur = f"{pre[1]} ایک پانسہ، مکعب کی شکل میں۔ سامنے 5 نقطے، اوپر 3 نقطے اور پہلو پر 2 نقطے ہیں۔".strip()
    return figure(W, y + s + 10, en, ur, items)


# ---------- coins ----------

def coin(c, text, r=22):
    return [circle(c, r), circle(c, r - 4), label(c, text)]


def coins_row(texts, alt_en, alt_ur, *, ring=(), toss=False):
    """Coins in a row, each with its text (H, T or a rupee value). ring:
    positions with a dashed circle round the coin. toss: a curved arc
    above each coin (it is spinning in the air)."""
    r, gap = 22, 30
    x = (W - len(texts) * 2 * r - (len(texts) - 1) * gap) / 2 + r
    y = 52 if toss else 32
    items = []
    for i, t in enumerate(texts):
        items += coin((x, y), t, r)
        if i in ring:
            items.append(circle((x, y), r + 6, dashed=True))
        if toss:
            items.append(arc((x, y), r + 14, 200, 140))
        x += 2 * r + gap
    return figure(W, y + r + 14, alt_en, alt_ur, items)


def coin_table(alt_en, alt_ur, *, cells=True):
    """The table for tossing two coins: the first coin down the side (H, T
    on coins), the second coin across the top, and each outcome in its
    cell."""
    c, x0, y0 = 54, 96, 52
    items = []
    for i, t in enumerate("HT"):
        items += coin((x0 + c * i + c / 2, y0 - 26), t, 16)
        items += coin((x0 - 26, y0 + c * i + c / 2), t, 16)
    items.append(rect(x0, y0, x0 + 2 * c, y0 + 2 * c))
    items += [line((x0 + c, y0), (x0 + c, y0 + 2 * c)), line((x0, y0 + c), (x0 + 2 * c, y0 + c))]
    if cells:
        for i, a in enumerate("HT"):
            for j, b in enumerate("HT"):
                items.append(label((x0 + c * j + c / 2, y0 + c * i + c / 2), a + b))
    return figure(W, y0 + 2 * c + 12, alt_en, alt_ur, items)


# ---------- bags of balls ----------

def bag(outcomes, key, *, pre=("", ""), per_row=5, x_center=W / 2, items_only=False, top=14):
    """A jar holding one ball per outcome, in the order of `key`.
    key = {outcome: (letter, colour_en, colour_ur)}; the first colour is
    shaded. Each ball has its letter on it."""
    r, gap = 11, 26
    n = len(outcomes)
    assert all(o in key for o in outcomes)
    # each colour starts a new row, so the balls of one colour are easy to count
    places = []
    for k in key:
        c = outcomes.count(k)
        size = -(-c // -(-c // per_row))       # split evenly: 9 is 5 + 4, 6 is 3 + 3
        places += [[k] * min(size, c - i) for i in range(0, c, size)]
    rows = len(places)
    inner = per_row * gap
    x0 = x_center - inner / 2 - 8
    x1 = x_center + inner / 2 + 8
    neck = 12
    bottom = top + neck + rows * gap + 20
    items = [poly([(x0 + 18, top), (x0 + 18, top + neck), (x0, top + neck + 10), (x0, bottom),
                   (x1, bottom), (x1, top + neck + 10), (x1 - 18, top + neck), (x1 - 18, top)])]
    first = next(iter(key))
    for row, balls_in_row in enumerate(places):
        for col, o in enumerate(balls_in_row):
            cx = x_center - inner / 2 + gap / 2 + col * gap
            cy = bottom - 6 - gap / 2 - row * gap
            items += [circle((cx, cy), r, fill=o == first), label((cx, cy), key[o][0])]
    we, wu = bag_words(outcomes, key)
    en = f"{pre[0]} A jar with {we}".strip()
    ur = f"{pre[1]} ایک مرتبان جس میں {wu}".strip()
    if items_only:
        return items, bottom
    return figure(W, bottom + 12, en, ur, items)


def bag_words(outcomes, key):
    """'10 balls: 3 marked R (red), ... The red balls are shaded.'"""
    first = next(iter(key))
    counts = [(outcomes.count(k), *key[k]) for k in key]
    en = (f"{len(outcomes)} balls: " + en_list([f"{c} marked {l} ({ce})" for c, l, ce, _ in counts])
          + f". The {key[first][1]} balls are shaded.")
    ur = (f"{len(outcomes)} گیندیں ہیں: " + ur_list([f"{l} والی {c} ({cu})" for c, l, _, cu in counts])
          + f"۔ {key[first][2]} گیندیں رنگین ہیں۔")
    return en, ur


def two_bags(a, b, key, names=("A", "B"), pre=("", "")):
    """Two jars side by side with a letter under each."""
    ia, ba = bag(a, key, per_row=4, x_center=78, items_only=True)
    ib, bb = bag(b, key, per_row=4, x_center=222, items_only=True)
    bottom = max(ba, bb)
    if ba != bb:     # stand both jars on the same shelf
        shift = bb - ba
        lo = ia if ba < bb else ib
        for it in lo:
            for k in ("center", "at"):
                if k in it:
                    it[k] = pt(it[k][0], it[k][1] + abs(shift))
            if "points" in it:
                it["points"] = [pt(x, y + abs(shift)) for x, y in it["points"]]
    items = ia + ib + [label((78, bottom + 16), names[0]), label((222, bottom + 16), names[1])]
    (ea, ua), (eb, ub) = bag_words(a, key), bag_words(b, key)
    en = f"{pre[0]} Two jars. Jar {names[0]}, on the left, has {ea} Jar {names[1]}, on the right, has {eb}".strip()
    ur = f"{pre[1]} دو مرتبان۔ بائیں مرتبان {names[0]} میں {ua} دائیں مرتبان {names[1]} میں {ub}".strip()
    return figure(W, bottom + 30, en, ur, items)


# ---------- spinners ----------

def spinner(parts, *, shade=(), pre=("", ""), what_en=None, what_ur=None):
    """A spinner of len(parts) equal parts, each with its text, drawn
    clockwise from the top. shade: the parts (by position) that are
    shaded. A pointer arrow from the middle. A text of None leaves that
    part empty; then what_en / what_ur must say what the parts are."""
    n = len(parts)
    rr, c = 66, (W / 2, 80)
    items = []
    for i in range(n):
        start = -90 + 360 * i / n
        if i in shade:
            pts = [c] + [_on(c, rr, start + 360 / n * k / 12) for k in range(13)]
            items.append(poly(pts, fill=True))
    items.append(circle(c, rr))
    for i, t in enumerate(parts):
        start = -90 + 360 * i / n
        items.append(line(c, _on(c, rr, start)))
        if t is not None:
            items.append(label(_on(c, rr * 0.7, start + 180 / n), t))
    tip = _on(c, rr * 0.42, -90 + 360 / n * 0.5 + 360 / n)   # points into the second part
    ang = math.degrees(math.atan2(tip[1] - c[1], tip[0] - c[0]))
    items += [line(c, tip), line(tip, _on(tip, 8, ang + 150)), line(tip, _on(tip, 8, ang - 150)), point(c)]
    en = (f"{pre[0]} A spinner with {n} equal parts, "
          + (what_en or f"marked {en_list(parts)}") + ". An arrow points out from the middle.").strip()
    ur = (f"{pre[1]} ایک گھومنے والا چکر جس کے {n} برابر حصے ہیں، "
          + (what_ur or f"جن پر {ur_list(parts)} لکھا ہے") + "۔ درمیان سے ایک تیر باہر کی طرف ہے۔").strip()
    return figure(W, 160, en, ur, items)


# ---------- cards and grids ----------

def cards(letters, *, pre=("", "")):
    """A row of cards, one letter on each."""
    w, h, gap = 28, 38, 6
    n = len(letters)
    x = (W - n * w - (n - 1) * gap) / 2
    items = []
    for t in letters:
        items += [rect(x, 12, x + w, 12 + h), label((x + w / 2, 12 + h / 2), t)]
        x += w + gap
    en = f"{pre[0]} {n} cards in a row: {en_list(list(letters))}.".strip()
    ur = f"{pre[1]} {n} کارڈ ایک قطار میں: {ur_list(list(letters))}۔".strip()
    return figure(W, 12 + h + 12, en, ur, items)


def grid(outcomes, marked, *, cols=10, shape="ticket", pre=("", ""), what_en="", what_ur=""):
    """One small ticket (or person) per outcome in a grid, the ones equal
    to `marked` shaded and first."""
    n = len(outcomes)
    order = sorted(outcomes, key=lambda o: o != marked)
    rows = -(-n // cols)
    if shape == "ticket":
        cw, ch, w, h = 26, 20, 20, 13
    else:
        cw, ch, w, h = 26, 22, 14, 14
    x0 = (W - cols * cw) / 2
    items = []
    for i, o in enumerate(order):
        row, col = divmod(i, cols)
        cx, cy = x0 + col * cw + cw / 2, 12 + row * ch + ch / 2
        if shape == "ticket":
            items.append(rect(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, fill=o == marked))
        else:
            items.append(circle((cx, cy), w / 2, fill=o == marked))
    k = outcomes.count(marked)
    en = f"{pre[0]} {n} small {'tickets' if shape == 'ticket' else 'circles'} in rows of {cols}; the first {k} are shaded{what_en}.".strip()
    ur = f"{pre[1]} {n} چھوٹے {'ٹکٹ' if shape == 'ticket' else 'دائرے'}، {cols} کی قطاروں میں؛ پہلے {k} رنگین ہیں{what_ur}۔".strip()
    return figure(W, 12 + rows * ch + 12, en, ur, items)


# ---------- the likelihood line ----------

def likelihood_line(alt_en, alt_ur, *, marks=()):
    """A line from 0 (impossible) to 1 (certain) with a taller tick at
    the middle (an even chance) and small ticks at the quarters. marks =
    [(value, letter)]: a dot on the line with its letter above."""
    x0, x1, y = 30, 270, 44
    items = [line((x0, y), (x1, y))]
    for k in range(5):
        x = x0 + (x1 - x0) * k / 4
        size = 12 if k in (0, 2, 4) else 6
        items.append(line((x, y - size), (x, y + size)))
    items += [label((x0, y + 26), "0"), label((x1, y + 26), "1")]
    for v, t in marks:
        x = x0 + (x1 - x0) * float(v)
        items += [circle((x, y), 5, fill=True), label((x, y - 24), t)]
    return figure(W, y + 42, alt_en, alt_ur, items)


NAMES = {"red": ("R", "red", "سرخ"), "blue": ("B", "blue", "نیلی"), "green": ("G", "green", "سبز"),
         "mango": ("M", "mango", "آم والی"), "strawberry": ("S", "strawberry", "اسٹرابیری والی"),
         "orange": ("O", "orange", "مالٹے والی"), "lemon": ("L", "lemon", "لیموں والی")}


def key(*names):
    """The key for bag(): the letter and colour words of each name, in
    this order (the first is shaded)."""
    return {n: NAMES[n] for n in names}


def with_fig(step, figure):
    step["figure"] = figure
    return step

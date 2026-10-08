import cmath
import math

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SY_SHAPES, SY_LINES, SY_LINE_SYMMETRY, SY_ROTATIONAL)

SKILL = SY_ROTATIONAL
FULL = 360


# ---------- geometry helpers (screen coordinates: y goes down) ----------

def r1(v):
    return round(v + 0.0, 1) + 0.0


def pt(z):
    return [r1(z.real), r1(z.imag)]


def polar(c, radius, deg):
    """A point `radius` from c, `deg` degrees clockwise on screen from +x."""
    return c + radius * cmath.exp(1j * math.radians(deg))


def regular(n, c, radius, start=-90):
    return [polar(c, radius, start + k * FULL / n) for k in range(n)]


def turn(z, c, deg):
    """Turn z about c by deg degrees clockwise on screen."""
    return c + (z - c) * cmath.exp(1j * math.radians(deg))


def mirror(z, c, deg):
    """Reflect z in the line through c at angle deg."""
    return c + cmath.exp(2j * math.radians(deg)) * (z - c).conjugate()


def key(z):
    return (round(z.real, 3) + 0.0, round(z.imag, 3) + 0.0)


def shape_key(pieces):
    """A drawing as a set of pieces; each piece is a set of its corners."""
    return frozenset(frozenset(key(z) for z in p) for p in pieces)


def order(pieces, c):
    """How many turns (of whole degrees, up to a full turn) fit the drawing onto itself."""
    start = shape_key(pieces)
    return sum(shape_key([[turn(z, c, d) for z in p] for p in pieces]) == start
               for d in range(1, FULL + 1))


def lines(pieces, c):
    """How many mirror lines through c (every half degree) fit the drawing onto itself."""
    start = shape_key(pieces)
    return sum(shape_key([[mirror(z, c, d / 2) for z in p] for p in pieces]) == start
               for d in range(0, 360))


def poly(points, fill=True, **extra):
    item = {"kind": "polygon", "points": [pt(z) for z in points]}
    if fill:
        item["fill"] = True
    item.update(extra)
    return item


def segs(pieces):
    return [{"kind": "line", "from": pt(a), "to": pt(b)} for a, b in pieces]


def centre_mark(c):
    return {"kind": "point", "at": pt(c)}


# ---------- the shapes ----------

C = complex(50, 32)
TRIANGLE = regular(3, C, 26)
SQUARE = regular(4, C, 26, start=-45)
HEXAGON = regular(6, C, 26, start=0)
RECT = [C + complex(-36, -18), C + complex(36, -18), C + complex(36, 18), C + complex(-36, 18)]


def pinwheel(c, radius):
    """A paper pinwheel (phirki): four blades, each a triangle bent to one side."""
    return [[c, polar(c, radius, a), polar(c, radius * 0.55, a + 50)] for a in (-90, 0, 90, 180)]


PIN = pinwheel(C, 28)


def letter(name, c, s):
    """Block capital letters as line segments around centre c, half-height 1.5 s."""
    P = lambda x, y: c + complex(x * s, y * s)
    if name == "Z":
        path = [P(-1, -1.5), P(1, -1.5), P(-1, 1.5), P(1, 1.5)]
    elif name == "S":
        path = [P(1, -1.5), P(-1, -1.5), P(-1, 0), P(1, 0), P(1, 1.5), P(-1, 1.5)]
    elif name == "A":
        path = [P(-1, 1.5), P(0, -1.5), P(1, 1.5)]
        return list(zip(path, path[1:])) + [(P(-0.5, 0), P(0.5, 0))]
    return list(zip(path, path[1:]))


def pieces_of(segments):
    return [list(s) for s in segments]


# Orders and lines of symmetry, worked out by turning and flipping.
assert order([TRIANGLE], C) == 3 and lines([TRIANGLE], C) == 3
assert order([SQUARE], C) == 4 and lines([SQUARE], C) == 4
assert order([RECT], C) == 2 and lines([RECT], C) == 2
assert order([HEXAGON], C) == 6 and lines([HEXAGON], C) == 6
assert order(PIN, C) == 4 and lines(PIN, C) == 0
Z_ORDER = order(pieces_of(letter("Z", C, 14)), C)
S_ORDER = order(pieces_of(letter("S", C, 14)), C)
A_ORDER = order(pieces_of(letter("A", C, 14)), C)
assert (Z_ORDER, S_ORDER, A_ORDER) == (2, 2, 1)
assert lines(pieces_of(letter("S", C, 14)), C) == 0
assert lines(pieces_of(letter("Z", C, 14)), C) == 0

# Smallest turn that fits = 360 ÷ order.
S4 = order([TRIANGLE], C)
assert S4 == 3 and FULL // S4 == 120
S5 = FULL // order([RECT], C)
assert S5 == 180 and FULL // order([SQUARE], C) == 90
S6 = Z_ORDER
assert S6 == 2
S8 = order([HEXAGON], C)
assert S8 == 6 and FULL // S8 == 60
S2 = lines([SQUARE], C)
assert S2 == 4

# ---------- the flag on a grid of dots (s7) ----------

U = 8          # grid spacing
FLAG_POLE = [0j, complex(0, -2)]
FLAG_CLOTH = [complex(0, -2), complex(2, -2), complex(2, -1), complex(0, -1)]


def flag_panel(c, deg=0, flip=False, tag=None):
    """Draw the flag about grid centre c, turned deg clockwise (or flipped top-to-bottom after turning)."""
    def place(z):
        w = turn(z, 0, deg)
        if flip:
            w = w.conjugate()
        return c + U * w
    items = [{"kind": "point", "at": pt(c + U * complex(i, j))} for i in (-2, 0, 2) for j in (-2, 0, 2)]
    items.append({"kind": "line", "from": pt(place(FLAG_POLE[0])), "to": pt(place(FLAG_POLE[1]))})
    items.append(poly([place(z) for z in FLAG_CLOTH]))
    if tag:
        items.append({"kind": "label", "at": pt(c + complex(0, 3 * U)), "text": tag})
    return items, shape_key([[place(z) - c for z in FLAG_POLE], [place(z) - c for z in FLAG_CLOTH]])


ORIG, k0 = flag_panel(complex(90, 22))
PA, ka = flag_panel(complex(22, 84), 90, tag="A")            # quarter turn clockwise (right)
PB, kb = flag_panel(complex(67, 84), -90, tag="B")           # quarter turn anticlockwise
PC, kc = flag_panel(complex(112, 84), 180, tag="C")          # half turn
PD, kd = flag_panel(complex(157, 84), 90, flip=True, tag="D")  # turned then flipped
assert len({k0, ka, kb, kc, kd}) == 5
# A really is a quarter turn clockwise of the original: turning the original's pieces by 90° gives A.
assert ka == shape_key([[turn(complex(*p), 0, 90) for p in piece] for piece in k0])
assert kb == shape_key([[turn(complex(*p), 0, -90) for p in piece] for piece in k0])
# D is not any turn of the original.
assert all(kd != shape_key([[turn(complex(*p), 0, d) for p in piece] for piece in k0]) for d in range(0, 360, 90))
FLAG_FIGURE = {
    "width": 180, "height": 116,
    "alt": T("Five pictures, each on a square of 9 dots. At the top is a flag: its pole goes up from the middle dot and the flag sticks out to the right at the top. Below are four choices. A: the pole points right from the middle dot and the flag hangs down from its end. B: the pole points left and the flag is above its end. C: the pole points down and the flag is to the left at the bottom. D: the pole points right and the flag is above its end.",
             "پانچ تصویریں، ہر ایک 9 نقطوں کے مربع جال پر۔ اوپر ایک جھنڈا ہے: اس کا ڈنڈا درمیانی نقطے سے اوپر جاتا ہے اور جھنڈا اوپر دائیں طرف نکلا ہے۔ نیچے چار جواب ہیں۔ A: ڈنڈا درمیانی نقطے سے دائیں طرف ہے اور جھنڈا اس کے سرے سے نیچے لٹکا ہے۔ B: ڈنڈا بائیں طرف ہے اور جھنڈا اس کے سرے کے اوپر ہے۔ C: ڈنڈا نیچے کی طرف ہے اور جھنڈا نیچے بائیں طرف ہے۔ D: ڈنڈا دائیں طرف ہے اور جھنڈا اس کے سرے کے اوپر ہے۔"),
    "items": ORIG + PA + PB + PC + PD,
}
assert len(FLAG_FIGURE["items"]) <= 60   # the schema's limit

# ---------- unit test numbers ----------

U1 = 6                     # faces of a cube (a Ludo dice)
assert U1 == 6
U2 = 65                    # corresponding angle on parallel lines
assert U2 != 180 - 65 and 180 - U2 == 115
U3 = lines([RECT], C)      # lines of symmetry of a rectangle
assert U3 == 2
U4 = FULL // order([SQUARE], C)
assert U4 == 90
# review
R1 = FULL // 45            # a floor pattern that fits every 45°
assert R1 == 8
# clock hand on 12: a quarter turn anticlockwise points to 9, clockwise to 3
HOUR = FULL // 12
R2 = 12 - 90 // HOUR
assert R2 == 9 and 90 // HOUR == 3

# ---------- small figures ----------

def fig(alt_en, alt_ur, items, w=100, h=64):
    return {"width": w, "height": h, "alt": T(alt_en, alt_ur), "items": items}


def turn_arc(c, radius):
    return {"kind": "arc", "center": pt(c), "radius": radius, "start": -60, "sweep": 90, "style": "dashed"}


PIN_FIG = fig("A paper pinwheel with four blades around a dot in the middle. Each blade is a triangle bent the same way round.",
              "ایک کاغذی پھرکی جس کے درمیان میں ایک نقطہ اور اس کے گرد چار پَر ہیں۔ ہر پَر ایک مثلث ہے، سب ایک ہی طرف مڑے ہوئے۔",
              [poly(b) for b in PIN] + [centre_mark(C)])

SQUARE_FIG = fig("A square with a dot at its centre, the centre of rotation, and a dashed curved arrow-line showing a turn around it.",
                 "ایک مربع جس کے بیچ میں ایک نقطہ ہے، یہ مرکزِ گردش ہے، اور اس کے گرد گھومنے کو دکھاتی ڈیش والی خمدار لکیر۔",
                 [poly(SQUARE), centre_mark(C), turn_arc(C, 10)])

TRI_FIG = fig("An equilateral triangle (all sides equal) with a dot at its centre.",
              "ایک مساوی الاضلاع مثلث (سب اضلاع برابر) جس کے بیچ میں ایک نقطہ ہے۔",
              [poly(TRIANGLE), centre_mark(C)])

RECT_FIG = fig("A rectangle, longer than it is tall, with a dot at its centre.",
               "ایک مستطیل، جو اونچائی سے زیادہ لمبی ہے، اور اس کے بیچ میں ایک نقطہ ہے۔",
               [poly(RECT), centre_mark(C)])

Z_FIG = fig("A capital letter Z with a dot at its middle.",
            "انگریزی کا بڑا حرف Z جس کے درمیان میں ایک نقطہ ہے۔",
            segs(letter("Z", C, 14)) + [centre_mark(C)])

HEX_FIG = fig("A regular hexagon: six equal sides and six equal angles, like one cell of a honeycomb, with a dot at its centre.",
              "ایک باقاعدہ مسدس: چھ برابر اضلاع اور چھ برابر زاویے، شہد کے چھتے کے ایک خانے کی طرح، بیچ میں ایک نقطہ۔",
              [poly(HEXAGON), centre_mark(C)])

S_FIG = fig("A capital letter S drawn with straight lines, with a dot at its middle.",
            "سیدھی لکیروں سے بنا انگریزی کا بڑا حرف S جس کے درمیان میں ایک نقطہ ہے۔",
            segs(letter("S", C, 14)) + [centre_mark(C)])

A_FIG = fig("A capital letter A with a dot at its middle.",
            "انگریزی کا بڑا حرف A جس کے درمیان میں ایک نقطہ ہے۔",
            segs(letter("A", C, 14)) + [centre_mark(C)])

# Four letters in a row for the last test question.
ROW = []
for i, name in enumerate(["S", "Z", "A", "N"]):
    cc = complex(25 + 50 * i, 30)
    if name == "N":
        P = lambda x, y, cc=cc: cc + complex(x * 10, y * 10)
        segments = [(P(-1, 1.5), P(-1, -1.5)), (P(-1, -1.5), P(1, 1.5)), (P(1, 1.5), P(1, -1.5))]
    else:
        segments = letter(name, cc, 10)
    if name == "N":
        assert order(pieces_of(segments), cc) == 2
    ROW += segs(segments) + [{"kind": "label", "at": pt(cc + complex(0, 26)), "text": str(i + 1)}]
LETTERS_FIG = fig("Four capital letters in a row, numbered 1 to 4: S, Z, A and N.",
                  "ایک قطار میں چار بڑے انگریزی حروف، 1 سے 4 تک نمبر کے ساتھ: S، Z، A اور N۔",
                  ROW, w=200, h=64)

# Parallel lines cut by a transversal, 65° marked at the top crossing.
P1, P2 = complex(10, 18), complex(150, 18)
Q1, Q2 = complex(10, 52), complex(150, 52)
COT = 1 / math.tan(math.radians(U2))
X1 = complex(90, 18)                       # the slanting line rises to the right at 65°
X2 = X1 + complex(-34 * COT, 34)
TA, TB = X1 + complex(14 * COT, -14), X2 + complex(-18 * COT, 18)
PAR_FIG = fig("Two parallel horizontal lines l and m are cut by a slanting line. At the top crossing, the angle above line l on the right of the slanting line is 65°. At the bottom crossing, the angle in the same position, above line m on the right, is marked x.",
              "دو متوازی افقی لکیریں l اور m ایک ترچھی لکیر سے کٹتی ہیں۔ اوپر والے نقطۂ تقاطع پر لکیر l کے اوپر، ترچھی لکیر کے دائیں طرف کا زاویہ 65° ہے۔ نیچے والے نقطۂ تقاطع پر اسی جگہ کا زاویہ، لکیر m کے اوپر دائیں طرف، x ہے۔",
              [{"kind": "line", "from": pt(P1), "to": pt(P2)},
               {"kind": "line", "from": pt(Q1), "to": pt(Q2)},
               {"kind": "line", "from": pt(TA), "to": pt(TB)},
               {"kind": "arc", "center": pt(X1), "radius": 7, "start": -U2, "sweep": U2},
               {"kind": "arc", "center": pt(X2), "radius": 7, "start": -U2, "sweep": U2},
               {"kind": "label", "at": pt(X1 + complex(18, -7)), "text": "65°"},
               {"kind": "label", "at": pt(X2 + complex(14, -6)), "text": "x"},
               {"kind": "label", "at": [155, 12], "text": "l"},
               {"kind": "label", "at": [155, 46], "text": "m"}],
              w=164, h=74)

CUBE_FIG = fig("A cube, like a Ludo dice, drawn with its front square face, its top face and its right side face showing.",
               "ایک مکعب، لُڈو کے ڈائس کی طرح، جس کا سامنے والا مربع رُخ، اوپر والا رُخ اور دائیں طرف کا رُخ نظر آ رہا ہے۔",
               [poly([complex(30, 24), complex(60, 24), complex(60, 54), complex(30, 54)]),
                poly([complex(30, 24), complex(42, 12), complex(72, 12), complex(60, 24)], fill=False),
                poly([complex(60, 24), complex(72, 12), complex(72, 42), complex(60, 54)], fill=False)])

lesson = {
 "id": "g6-maths-18-rotational-symmetry",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise rotational symmetry, find the centre and order of rotational symmetry of shapes and letters, and turn a shape through 90° and 180° clockwise and anticlockwise.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Rotational symmetry", "گردشی تشاکل"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": SY_LINE_SYMMETRY}, {"skill": SY_LINES}, {"skill": SY_SHAPES}],
 "misconceptions": [
   {"id": "order_zero", "description": "Says a shape with no rotational symmetry has order 0 (it has order 1: it fits once, after a full turn)."},
   {"id": "clock_direction", "description": "Confuses clockwise with anticlockwise when turning a shape."},
   {"id": "counts_lines", "description": "Counts the lines of symmetry instead of the turns that fit the shape onto itself."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_order_meaning", "type": "recall", "step": {
     "id": "qb_order_meaning", "type": "choice",
     "prompt": T("What does the order of rotational symmetry tell us?", "گردشی تشاکل کا درجہ ہمیں کیا بتاتا ہے؟"),
     "options": [
       opt("turns", "How many times the shape fits onto itself in one full turn.", "ایک پورے چکر میں شکل کتنی بار خود پر بالکل بیٹھتی ہے۔", True,
           "Yes! Count the fits as you turn it all the way round.", "جی ہاں! پورا گھماتے ہوئے گنیں کہ کتنی بار بیٹھتی ہے۔"),
       opt("lines", "How many lines of symmetry the shape has.", "شکل کے کتنے خطِ تشاکل ہیں۔", False,
           "That is line symmetry. The order counts turns, not fold lines.", "یہ خطی تشاکل ہے۔ درجہ موڑنے کی لکیریں نہیں، چکر گنتا ہے۔", "counts_lines"),
       opt("sides", "How many sides the shape has.", "شکل کے کتنے اضلاع ہیں۔", False,
           "A rectangle has 4 sides but order 2. Count the fits in a full turn.", "مستطیل کے 4 اضلاع ہیں لیکن درجہ 2۔ پورے چکر میں بیٹھنے کی تعداد گنیں۔"),
     ]}},
   {"id": "qb_pinwheel", "type": "apply", "step": dict(number_question(
     "qb_pinwheel",
     T("Bilal's paper pinwheel (phirki) has 4 blades. What is its order of rotational symmetry?", "بلال کی کاغذی پھرکی کے 4 پَر ہیں۔ اس کے گردشی تشاکل کا درجہ کیا ہے؟"),
     order(PIN, C),
     T("Turn it a quarter turn at a time. When does it look the same?", "اسے ایک ایک چوتھائی چکر گھمائیں۔ کب یہ ویسی ہی لگتی ہے؟"),
     T("Right! It fits after every quarter turn: order 4.", "درست! یہ ہر چوتھائی چکر کے بعد بیٹھتی ہے: درجہ 4"),
     T("Each quarter turn moves every blade to the next blade's place: 4 fits, order 4.", "ہر چوتھائی چکر ہر پَر کو اگلے پَر کی جگہ لے جاتا ہے: 4 بار، درجہ 4"),
     common_wrong=[wrong(0, "The bent blades give no lines of symmetry, but the pinwheel still turns onto itself 4 times: order 4.", "مڑے پَروں کی وجہ سے کوئی خطِ تشاکل نہیں، لیکن پھرکی پھر بھی 4 بار خود پر بیٹھتی ہے: درجہ 4", "counts_lines"),
                   wrong(1, "It fits after a quarter turn, not only after a full turn: order 4.", "یہ چوتھائی چکر کے بعد بھی بیٹھتی ہے، صرف پورے چکر پر نہیں: درجہ 4")],
     qtype=None), figure=PIN_FIG)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "figure": A_FIG,
     "prompt": T("Sana says the letter A has rotational symmetry of order 0. What went wrong?", "ثنا کہتی ہے حرف A کے گردشی تشاکل کا درجہ 0 ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("one", "The order is 1: A only fits onto itself after a full turn.", "درجہ 1 ہے: A صرف پورے چکر کے بعد خود پر بیٹھتا ہے۔", True,
           "Yes! Every shape fits once in a full turn, so the smallest order is 1.", "جی ہاں! ہر شکل پورے چکر میں ایک بار بیٹھتی ہے، اس لیے سب سے چھوٹا درجہ 1 ہے۔"),
       opt("two", "The order is 2: A looks the same after a half turn.", "درجہ 2 ہے: آدھے چکر کے بعد A ویسا ہی لگتا ہے۔", False,
           "After a half turn A is upside down. It only fits after a full turn: order 1.", "آدھے چکر کے بعد A الٹا ہو جاتا ہے۔ یہ صرف پورے چکر پر بیٹھتا ہے: درجہ 1"),
       opt("nothing", "Nothing. No rotational symmetry means order 0.", "کوئی غلطی نہیں۔ گردشی تشاکل نہ ہو تو درجہ 0۔", False,
           "A full turn always brings a shape back, so we count 1, not 0.", "پورا چکر شکل کو ہمیشہ واپس لے آتا ہے، اس لیے ہم 1 گنتے ہیں، 0 نہیں۔", "order_zero"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_order", "front": T("Order of rotational symmetry?", "گردشی تشاکل کا درجہ؟"),
    "back": T("How many times a shape fits onto itself in one full turn. Square 4, equilateral triangle 3, rectangle 2.",
              "ایک پورے چکر میں شکل کتنی بار خود پر بیٹھتی ہے۔ مربع 4، مساوی الاضلاع مثلث 3، مستطیل 2۔")},
   {"id": "f_one", "front": T("A shape with no rotational symmetry has order?", "جس شکل میں گردشی تشاکل نہ ہو اس کا درجہ؟"),
    "back": T("1, never 0. Like the letter A: it fits only after a full turn.", "1، کبھی 0 نہیں۔ جیسے حرف A: یہ صرف پورے چکر کے بعد بیٹھتا ہے۔")},
 ],
 "home_tasks": [{"id": "h_trace", "text": T(
   "Cut a square, a rectangle and a letter Z out of card. Lay each one on paper and trace round it. Put a pencil point on its centre and turn the card slowly. Count how many times it fits exactly on its outline before it gets back to the start. Then make a paper pinwheel (phirki) and count its order too.",
   "گتے سے ایک مربع، ایک مستطیل اور حرف Z کاٹیں۔ ہر ایک کو کاغذ پر رکھ کر اس کے گرد لکیر کھینچیں۔ اس کے مرکز پر پنسل کی نوک رکھیں اور گتے کو آہستہ آہستہ گھمائیں۔ گنیں کہ شروع کی جگہ پر واپس آنے تک یہ کتنی بار اپنے خاکے پر بالکل بیٹھتا ہے۔ پھر ایک کاغذی پھرکی بنائیں اور اس کا درجہ بھی گنیں۔")}],
 "glossary": [T("Rotational symmetry", "گردشی تشاکل"), T("Centre of rotation", "مرکزِ گردش"),
              T("Order of rotational symmetry", "گردشی تشاکل کا درجہ"),
              T("Clockwise", "گھڑی کی سوئیوں کی سمت"), T("Anticlockwise", "گھڑی کی سوئیوں کی مخالف سمت"),
              T("Quarter turn", "چوتھائی چکر"), T("Half turn", "آدھا چکر")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "figure": PIN_FIG,
    "character": say("curious", "Spin a paper phirki on the rooftop. Stop it after a little turn: it looks exactly the same! How?",
                     "چھت پر کاغذ کی پھرکی گھمائیں۔ تھوڑا سا گھوم کر روکیں: یہ بالکل ویسی ہی لگتی ہے! کیسے؟"),
    "text": T("Today we learn about shapes that look the same after a turn. This is the last lesson of the Symmetry unit, so it ends with a short unit test. First, a quick check.",
              "آج ہم ایسی شکلوں کے بارے میں سیکھیں گے جو گھمانے کے بعد ویسی ہی لگتی ہیں۔ یہ تشاکل کے باب کا آخری سبق ہے، اس لیے آخر میں باب کا ایک چھوٹا ٹیسٹ ہے۔ پہلے ایک چھوٹا سا سوال۔")},
   dict(number_question(
     "s2_foundation",
     T("How many lines of symmetry does a square have?", "مربع کے کتنے خطِ تشاکل ہوتے ہیں؟"),
     S2,
     T("Fold it down the middle both ways, and also corner to corner.", "اسے درمیان سے دونوں طرف تہہ کریں، اور کونے سے کونے تک بھی۔"),
     T("Right! 2 through the middles of the sides and 2 along the diagonals: 4.", "درست! 2 اضلاع کے درمیان سے اور 2 وتروں پر: 4"),
     T("A square has 4 lines of symmetry: across, down and both diagonals.", "مربع کے 4 خطِ تشاکل ہیں: افقی، عمودی اور دونوں وتر۔"),
     common_wrong=[wrong(2, "Don't forget the two diagonals: 4 lines.", "دونوں وتر نہ بھولیں: 4 لکیریں۔")],
     qtype="recall", skill=SY_LINE_SYMMETRY), figure=fig(
       "A square with a dot at its centre.", "ایک مربع جس کے بیچ میں ایک نقطہ ہے۔", [poly(SQUARE), centre_mark(C)])),
   {"id": "s3_rule", "type": "explain",
    "figure": SQUARE_FIG,
    "character": say("happy", "Turn it, count the fits. A full turn always counts as one, so the smallest order is 1!",
                     "گھمائیں اور گنیں کہ کتنی بار بیٹھتی ہے۔ پورا چکر ہمیشہ ایک گنا جاتا ہے، اس لیے سب سے چھوٹا درجہ 1 ہے!"),
    "text": T("A shape has rotational symmetry if it looks exactly the same after turning it less than a full turn about its centre. That fixed point is the centre of rotation. The order of rotational symmetry is how many times the shape fits onto itself in one full turn (360°). A square fits after every quarter turn (90°), so its order is 4. A shape that only fits after a full turn has order 1: it has no rotational symmetry. A turn can go clockwise (the way a clock's hands move) or anticlockwise (the other way).",
              "اگر کسی شکل کو اس کے مرکز کے گرد پورے چکر سے کم گھمانے پر وہ بالکل ویسی ہی لگے تو اس میں گردشی تشاکل (rotational symmetry) ہے۔ وہ ٹھہرا ہوا نقطہ مرکزِ گردش (centre of rotation) ہے۔ گردشی تشاکل کا درجہ (order) یہ ہے کہ ایک پورے چکر (360°) میں شکل کتنی بار خود پر بالکل بیٹھتی ہے۔ مربع ہر چوتھائی چکر (90°) کے بعد بیٹھتا ہے، اس لیے اس کا درجہ 4 ہے۔ جو شکل صرف پورے چکر کے بعد بیٹھے اس کا درجہ 1 ہے: اس میں گردشی تشاکل نہیں۔ گھمانا گھڑی کی سوئیوں کی سمت (clockwise) یا اس کی مخالف سمت (anticlockwise) ہو سکتا ہے۔")},
   dict(number_question(
     "s4_triangle",
     T("What is the order of rotational symmetry of an equilateral triangle?", "مساوی الاضلاع مثلث کے گردشی تشاکل کا درجہ کیا ہے؟"),
     S4,
     T("Each corner can move to where the next corner was.", "ہر کونا اگلے کونے کی جگہ جا سکتا ہے۔"),
     T("Right! It fits after every 120°: order 3.", "درست! یہ ہر 120° کے بعد بیٹھتی ہے: درجہ 3"),
     T("It fits 3 times in a full turn (every 360 ÷ 3 = 120°): order 3.", "یہ پورے چکر میں 3 بار بیٹھتی ہے (ہر 360 ÷ 3 = 120°): درجہ 3"),
     common_wrong=[wrong(120, "120° is the size of each turn. The order counts the fits: 3.", "120° ہر بار کا گھماؤ ہے۔ درجہ بیٹھنے کی تعداد ہے: 3"),
                   wrong(1, "It fits after 120°, before a full turn, so the order is more than 1: 3.", "یہ پورے چکر سے پہلے 120° پر بیٹھ جاتی ہے، اس لیے درجہ 1 سے زیادہ ہے: 3")]),
     figure=TRI_FIG),
   dict(number_question(
     "s5_rectangle",
     T("Ali turns a rectangle about its centre. What is the smallest turn, in degrees, that makes it fit onto itself?", "علی ایک مستطیل کو اس کے مرکز کے گرد گھماتا ہے۔ کم از کم کتنے درجے گھمانے پر یہ خود پر بیٹھتی ہے؟"),
     S5,
     T("Try a quarter turn first. Is the long side still lying flat?", "پہلے چوتھائی چکر آزمائیں۔ کیا لمبا ضلع اب بھی لیٹا ہوا ہے؟"),
     T("Right! A half turn, 180°. It fits twice in a full turn: order 2.", "درست! آدھا چکر، 180°۔ یہ پورے چکر میں دو بار بیٹھتی ہے: درجہ 2"),
     T("After 90° the rectangle stands up tall, so it doesn't fit. After 180° it fits: order 2.", "90° کے بعد مستطیل کھڑی ہو جاتی ہے، اس لیے نہیں بیٹھتی۔ 180° کے بعد بیٹھتی ہے: درجہ 2"),
     common_wrong=[wrong(90, "That works for a square. After 90° a rectangle stands up tall. It fits after 180°.", "یہ مربع کے لیے ہے۔ 90° کے بعد مستطیل کھڑی ہو جاتی ہے۔ یہ 180° پر بیٹھتی ہے۔"),
                   wrong(360, "Less than a full turn works too: a half turn, 180°.", "پورے چکر سے کم پر بھی بیٹھتی ہے: آدھا چکر، 180°")]),
     figure=RECT_FIG),
   dict(number_question(
     "s6_letter_z",
     T("Look at the letter Z. What is its order of rotational symmetry?", "حرف Z کو دیکھیں۔ اس کے گردشی تشاکل کا درجہ کیا ہے؟"),
     S6,
     T("Turn your book upside down. Does Z still look like Z?", "اپنی کتاب الٹی کریں۔ کیا Z اب بھی Z لگتا ہے؟"),
     T("Right! Z fits after a half turn and after a full turn: order 2.", "درست! Z آدھے چکر اور پورے چکر کے بعد بیٹھتا ہے: درجہ 2"),
     T("Upside down, Z is still Z. That is 2 fits in a full turn: order 2.", "الٹا کرنے پر بھی Z، Z ہی رہتا ہے۔ پورے چکر میں 2 بار: درجہ 2"),
     common_wrong=[wrong(0, "Z has no lines of symmetry, but it still turns onto itself after a half turn: order 2.", "Z کا کوئی خطِ تشاکل نہیں، لیکن آدھے چکر پر یہ خود پر بیٹھ جاتا ہے: درجہ 2", "counts_lines"),
                   wrong(1, "Z fits after a half turn too, not only a full turn: order 2.", "Z آدھے چکر پر بھی بیٹھتا ہے، صرف پورے چکر پر نہیں: درجہ 2")]),
     figure=Z_FIG),
   {"id": "s7_flag", "type": "choice", "question_type": "apply",
    "figure": FLAG_FIGURE,
    "prompt": T("Hamza turns the flag at the top a quarter turn (90°) clockwise about the bottom of its pole. Which picture shows the result?",
                "حمزہ اوپر والے جھنڈے کو اس کے ڈنڈے کے نچلے سرے کے گرد گھڑی کی سوئیوں کی سمت چوتھائی چکر (90°) گھماتا ہے۔ کون سی تصویر نتیجہ دکھاتی ہے؟"),
    "options": [
      opt("a", "A", "A", True,
          "Yes! The pole turns from pointing up to pointing right, and the flag swings down with it.", "جی ہاں! ڈنڈا اوپر سے دائیں طرف گھومتا ہے، اور جھنڈا اس کے ساتھ نیچے آ جاتا ہے۔"),
      opt("b", "B", "B", False,
          "That is a quarter turn anticlockwise. Clockwise, the top of the pole moves to the right: A.", "یہ گھڑی کی مخالف سمت چوتھائی چکر ہے۔ گھڑی کی سمت ڈنڈے کا اوپر والا سرا دائیں جاتا ہے: A", "clock_direction"),
      opt("c", "C", "C", False,
          "That is a half turn (180°): the pole points down. A quarter turn points it right: A.", "یہ آدھا چکر (180°) ہے: ڈنڈا نیچے ہو گیا۔ چوتھائی چکر سے یہ دائیں ہوتا ہے: A"),
      opt("d", "D", "D", False,
          "The pole points right, but the flag is on the wrong side: D is turned and flipped. A turn never flips: A.", "ڈنڈا دائیں ہے، لیکن جھنڈا غلط طرف ہے: D گھما کر پلٹا گیا ہے۔ گھمانے میں پلٹنا نہیں ہوتا: A"),
    ]},
   dict(number_question(
     "s8_hexagon",
     T("A floor tile is a regular hexagon (6 equal sides). What is its order of rotational symmetry?", "فرش کی ایک ٹائل باقاعدہ مسدس (6 برابر اضلاع) ہے۔ اس کے گردشی تشاکل کا درجہ کیا ہے؟"),
     S8,
     T("Each corner can move to where the next corner was. How many corners?", "ہر کونا اگلے کونے کی جگہ جا سکتا ہے۔ کتنے کونے ہیں؟"),
     T("Right! It fits after every 60°: order 6.", "درست! یہ ہر 60° کے بعد بیٹھتی ہے: درجہ 6"),
     T("6 corners, so it fits 6 times in a full turn (every 60°): order 6.", "6 کونے، تو یہ پورے چکر میں 6 بار بیٹھتی ہے (ہر 60°): درجہ 6"),
     common_wrong=[wrong(60, "60° is the size of each turn. Count the fits: 6.", "60° ہر بار کا گھماؤ ہے۔ بیٹھنے کی تعداد گنیں: 6"),
                   wrong(3, "It fits after every 60°, not every 120°: 6 times.", "یہ ہر 60° پر بیٹھتی ہے، ہر 120° پر نہیں: 6 بار۔")]),
     figure=HEX_FIG),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "figure": S_FIG,
    "prompt": T("Bilal says: 'The letter S has no line of symmetry, so it has no rotational symmetry.' What went wrong?",
                "بلال کہتا ہے: 'حرف S کا کوئی خطِ تشاکل نہیں، اس لیے اس میں گردشی تشاکل بھی نہیں۔' کیا غلطی ہوئی؟"),
    "options": [
      opt("turns", "Lines and turns are different. S fits after a half turn, so its order is 2.", "لکیریں اور چکر الگ ہیں۔ S آدھے چکر پر بیٹھتا ہے، اس لیے اس کا درجہ 2 ہے۔", True,
          "Yes! Turn S upside down and it is still S.", "جی ہاں! S کو الٹا کریں تو یہ پھر بھی S ہے۔"),
      opt("zero", "He is right, and the order of S is 0.", "وہ ٹھیک ہے، اور S کا درجہ 0 ہے۔", False,
          "The order is never 0, and S does fit after a half turn: order 2.", "درجہ کبھی 0 نہیں ہوتا، اور S آدھے چکر پر بیٹھتا ہے: درجہ 2", "order_zero"),
      opt("nothing", "Nothing. No lines of symmetry means no rotational symmetry.", "کوئی غلطی نہیں۔ خطِ تشاکل نہ ہو تو گردشی تشاکل بھی نہیں۔", False,
          "A shape can turn onto itself without any fold line. S fits after 180°: order 2.", "شکل بغیر کسی تہہ کی لکیر کے بھی گھوم کر بیٹھ سکتی ہے۔ S، 180° پر بیٹھتا ہے: درجہ 2", "counts_lines"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "figure": A_FIG,
    "character": say("curious", "Sana says the letter A has order 0. I think it is 1. Who is right, and why? Can you teach me?",
                     "ثنا کہتی ہے حرف A کا درجہ 0 ہے۔ میرے خیال میں 1 ہے۔ کون ٹھیک ہے، اور کیوں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the order of rotational symmetry never 0?",
              "اپنے الفاظ میں بتائیں: گردشی تشاکل کا درجہ کبھی 0 کیوں نہیں ہوتا؟"),
    "key_idea": "The order counts how many times a shape fits onto itself in one full turn. After a full turn (360°) every shape is back where it started, so it always fits at least once. A shape like A with no rotational symmetry has order 1.",
    "levels": {
      "got_it": "Says that after a full turn every shape is back in its place, so it fits at least once and the order is at least 1.",
      "partly": "Says the answer is 1 but does not link it to the full turn, or mentions the full turn without saying it counts as one fit.",
      "not_yet": "Gives no reason, says 0, or confuses it with lines of symmetry."},
    "keywords": [
      ["full turn", "360", "پورا چکر", "poora chakkar"],
      ["back", "same place", "start", "واپس", "wapas"],
      ["once", "1", "one", "ایک", "aik"]],
    "fallback_feedback": {
      "got_it": T("Well explained! A full turn always brings the shape back, so it fits at least once: order 1.", "بہت خوب! پورا چکر شکل کو ہمیشہ واپس لے آتا ہے، تو یہ کم از کم ایک بار بیٹھتی ہے: درجہ 1"),
      "partly": T("Good start! Now say what happens to any shape after a full turn of 360°.", "اچھی شروعات! اب بتائیں 360° کے پورے چکر کے بعد کسی بھی شکل کا کیا ہوتا ہے۔"),
      "not_yet": T("Turn the letter A all the way round, 360°. Is it back in its place? That counts as one fit.", "حرف A کو پورا 360° گھمائیں۔ کیا یہ اپنی جگہ پر واپس آ گیا؟ یہ ایک بار بیٹھنا گنا جاتا ہے۔")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Symmetry unit. You can do it!",
                     "ٹیسٹ کا وقت! تشاکل کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on 2-D and 3-D shapes, parallel lines, line symmetry and rotational symmetry. Take your time.",
              "اس چھوٹے ٹیسٹ میں دو اور تین ابعادی شکلوں، متوازی لکیروں، خطی تشاکل اور گردشی تشاکل کے سوال ہیں۔ آرام سے کریں۔")},
   dict(number_question(
     "u1_cube",
     T("Test 1: A Ludo dice is a cube. How many faces does it have?", "ٹیسٹ 1: لُڈو کا ڈائس ایک مکعب ہے۔ اس کے کتنے رُخ ہیں؟"),
     U1,
     T("It has a number from 1 to 6 on each face.", "اس کے ہر رُخ پر 1 سے 6 تک ایک عدد ہوتا ہے۔"),
     T("Right! 6 square faces.", "درست! 6 مربع رُخ۔"),
     T("A cube has 6 faces: top, bottom, front, back, left and right.", "مکعب کے 6 رُخ ہیں: اوپر، نیچے، آگے، پیچھے، بائیں اور دائیں۔"),
     common_wrong=[wrong(3, "You can only see 3 faces at once. There are 3 more hidden: 6.", "ایک وقت میں صرف 3 رُخ نظر آتے ہیں۔ 3 اور چھپے ہیں: 6"),
                   wrong(8, "8 is the number of corners (vertices). Faces: 6.", "8 کونوں (راس) کی تعداد ہے۔ رُخ: 6"),
                   wrong(12, "12 is the number of edges. Faces: 6.", "12 کناروں کی تعداد ہے۔ رُخ: 6")],
     skill=SY_SHAPES), figure=CUBE_FIG),
   dict(number_question(
     "u2_parallel",
     T("Test 2: Lines l and m are parallel. A slanting line cuts them. The angle at the top crossing is 65°. What is angle x, in the same position at the bottom crossing?",
       "ٹیسٹ 2: لکیریں l اور m متوازی ہیں۔ ایک ترچھی لکیر انہیں کاٹتی ہے۔ اوپر والے نقطۂ تقاطع پر زاویہ 65° ہے۔ نیچے والے نقطۂ تقاطع پر اسی جگہ کا زاویہ x کتنا ہے؟"),
     U2,
     T("Angles in the same position on parallel lines (corresponding angles) are equal.", "متوازی لکیروں پر ایک ہی جگہ کے زاویے (متناظر زاویے) برابر ہوتے ہیں۔"),
     T("Right! Corresponding angles are equal: 65°.", "درست! متناظر زاویے برابر ہوتے ہیں: 65°"),
     T("x is in the same position as 65°, so x = 65°.", "x، 65° والی جگہ پر ہے، اس لیے x = 65°"),
     common_wrong=[wrong(115, "115° is the angle next to it on the line. Corresponding angles are equal: 65°.", "115° لکیر پر اس کے ساتھ والا زاویہ ہے۔ متناظر زاویے برابر ہیں: 65°")],
     skill=SY_LINES), figure=PAR_FIG),
   dict(number_question(
     "u3_rectangle_lines",
     T("Test 3: How many lines of symmetry does a rectangle (not a square) have?", "ٹیسٹ 3: مستطیل (جو مربع نہ ہو) کے کتنے خطِ تشاکل ہیں؟"),
     U3,
     T("Fold a rectangle of paper corner to corner. Do the halves match?", "کاغذ کی مستطیل کو کونے سے کونے تک تہہ کریں۔ کیا دونوں آدھے ملتے ہیں؟"),
     T("Right! One across the middle and one down the middle: 2.", "درست! ایک افقی درمیان سے اور ایک عمودی درمیان سے: 2"),
     T("A rectangle has 2 lines of symmetry. The diagonals are not lines of symmetry.", "مستطیل کے 2 خطِ تشاکل ہیں۔ وتر خطِ تشاکل نہیں ہیں۔"),
     common_wrong=[wrong(4, "The diagonals don't work for a rectangle: the halves don't match. Only 2.", "مستطیل میں وتر کام نہیں کرتے: آدھے نہیں ملتے۔ صرف 2")],
     skill=SY_LINE_SYMMETRY), figure=RECT_FIG),
   dict(number_question(
     "u4_square_turn",
     T("Test 4: What is the smallest turn, in degrees, that fits a square onto itself?", "ٹیسٹ 4: مربع کو خود پر بٹھانے کے لیے کم از کم کتنے درجے کا گھماؤ چاہیے؟"),
     U4,
     T("A square has order 4. Share 360° into 4 turns.", "مربع کا درجہ 4 ہے۔ 360° کو 4 حصوں میں بانٹیں۔"),
     T("Right! A quarter turn, 90°.", "درست! چوتھائی چکر، 90°"),
     T("360 ÷ 4 = 90°: a quarter turn.", "360 ÷ 4 = 90°: چوتھائی چکر۔"),
     common_wrong=[wrong(180, "A half turn works, but a quarter turn (90°) already fits.", "آدھا چکر بھی چلتا ہے، لیکن چوتھائی چکر (90°) پر ہی بیٹھ جاتا ہے۔"),
                   wrong(45, "After 45° the square stands on a corner, like a diamond. It fits after 90°.", "45° کے بعد مربع کونے پر کھڑا ہو جاتا ہے۔ یہ 90° پر بیٹھتا ہے۔")],
     skill=SY_ROTATIONAL), figure=SQUARE_FIG),
   {"id": "u5_letters", "type": "choice", "skill": SY_ROTATIONAL,
    "figure": LETTERS_FIG,
    "prompt": T("Test 5: Which letter has NO rotational symmetry (order 1)?", "ٹیسٹ 5: کس حرف میں کوئی گردشی تشاکل نہیں (درجہ 1)؟"),
    "options": [
      opt("s", "1 (S)", "1 (S)", False,
          "S upside down is still S: order 2. Look at A.", "S الٹا بھی S ہے: درجہ 2۔ A کو دیکھیں۔"),
      opt("z", "2 (Z)", "2 (Z)", False,
          "Z upside down is still Z: order 2. Look at A.", "Z الٹا بھی Z ہے: درجہ 2۔ A کو دیکھیں۔"),
      opt("a", "3 (A)", "3 (A)", True,
          "Yes! A upside down is not A. It only fits after a full turn: order 1.", "جی ہاں! A الٹا A نہیں رہتا۔ یہ صرف پورے چکر پر بیٹھتا ہے: درجہ 1"),
      opt("n", "4 (N)", "4 (N)", False,
          "N upside down is still N: order 2. Look at A.", "N الٹا بھی N ہے: درجہ 2۔ A کو دیکھیں۔"),
    ]},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Symmetry unit complete! Now spot the turns in pinwheels, tiles and truck art all around you.",
                     "تشاکل کا باب مکمل! اب اپنے ارد گرد پھرکیوں، ٹائلوں اور ٹرک آرٹ میں چکر ڈھونڈیں۔"),
    "text": T("A shape has rotational symmetry if it looks the same after less than a full turn about its centre of rotation. The order is how many times it fits onto itself in one full turn: square 4, equilateral triangle 3, rectangle 2, regular hexagon 6, letters S and Z 2. A shape with no rotational symmetry, like A, has order 1, never 0. The smallest turn that fits is 360° ÷ order. Clockwise is the way a clock's hands move; anticlockwise is the other way. Count turns, not lines of symmetry.",
              "اگر کوئی شکل اپنے مرکزِ گردش کے گرد پورے چکر سے کم گھمانے پر ویسی ہی لگے تو اس میں گردشی تشاکل ہے۔ درجہ یہ ہے کہ پورے چکر میں شکل کتنی بار خود پر بیٹھتی ہے: مربع 4، مساوی الاضلاع مثلث 3، مستطیل 2، باقاعدہ مسدس 6، حروف S اور Z کا 2۔ جس شکل میں گردشی تشاکل نہ ہو، جیسے A، اس کا درجہ 1 ہے، کبھی 0 نہیں۔ سب سے چھوٹا گھماؤ 360° ÷ درجہ ہے۔ گھڑی کی سوئیوں کی سمت کلاک وائز ہے؛ مخالف سمت اینٹی کلاک وائز۔ چکر گنیں، خطِ تشاکل نہیں۔"),
    "points": [T("Order = fits in one full turn.", "درجہ = پورے چکر میں بیٹھنے کی تعداد۔"),
               T("No rotational symmetry: order 1.", "گردشی تشاکل نہیں: درجہ 1۔"),
               T("Smallest turn = 360° ÷ order.", "سب سے چھوٹا گھماؤ = 360° ÷ درجہ۔")]},
 ],
 "review_questions": [
   {"id": "r_rangoli", "type": "apply", "skill": SKILL, "step": number_question(
     "r_rangoli",
     T("A floor pattern for Eid looks exactly the same after every 45° turn. What is its order of rotational symmetry?", "عید کے لیے فرش کا ایک نقش ہر 45° گھمانے پر بالکل ویسا ہی لگتا ہے۔ اس کے گردشی تشاکل کا درجہ کیا ہے؟"),
     R1,
     T("How many 45° turns make 360°?", "کتنے 45° کے گھماؤ 360° بناتے ہیں؟"),
     T("Right! 360 ÷ 45 = 8.", "درست! 360 ÷ 45 = 8"),
     T("360 ÷ 45 = 8 fits in a full turn: order 8.", "360 ÷ 45 = 8 بار پورے چکر میں: درجہ 8"),
     common_wrong=[wrong(45, "45° is the size of each turn. Count the turns: 360 ÷ 45 = 8.", "45° ہر بار کا گھماؤ ہے۔ چکر گنیں: 360 ÷ 45 = 8"),
                   wrong(4, "That would be every 90°. Every 45° gives 8.", "یہ ہر 90° پر ہوتا۔ ہر 45° سے 8")],
     qtype=None)},
   {"id": "r_clock", "type": "apply", "skill": SKILL, "step": number_question(
     "r_clock",
     T("A clock hand points to 12. It turns a quarter turn (90°) anticlockwise. Which number does it point to now?", "گھڑی کی سوئی 12 پر ہے۔ یہ گھڑی کی مخالف سمت چوتھائی چکر (90°) گھومتی ہے۔ اب یہ کس عدد پر ہے؟"),
     R2,
     T("Anticlockwise is backwards: 12, 11, 10, …", "مخالف سمت پیچھے کی طرف ہے: 12، 11، 10، …"),
     T("Right! Back 3 hours: 9.", "درست! 3 گھنٹے پیچھے: 9"),
     T("A quarter turn is 3 hours. Going backwards from 12 gives 9.", "چوتھائی چکر 3 گھنٹے ہے۔ 12 سے پیچھے جائیں تو 9"),
     common_wrong=[wrong(3, "3 is a quarter turn clockwise. Anticlockwise goes the other way: 9.", "3 گھڑی کی سمت چوتھائی چکر ہے۔ مخالف سمت دوسری طرف: 9", "clock_direction"),
                   wrong(6, "6 is a half turn. A quarter turn anticlockwise reaches 9.", "6 آدھا چکر ہے۔ مخالف سمت چوتھائی چکر 9 پر پہنچتا ہے۔")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Symmetry unit (PCTB Mathematics 6, Sub-domain 9). No textbook text or exercises were used.",
   "Every order and smallest turn in this lesson (square, triangle, rectangle, hexagon, pinwheel, letters S, Z, A, N) and the four flag pictures in s7 were checked in the script by turning the drawn shapes in Python.",
   "Stress that the order is never 0: a shape with no rotational symmetry has order 1. Some books say 'order 0'; we follow the usual convention of order 1.",
   "The pinwheel and the letters S and Z show that a shape can have rotational symmetry with no line of symmetry, so turns and lines must be counted separately.",
   "The unit test (u1 to u5) covers 2-D and 3-D shapes, parallel lines and a transversal (corresponding angles), line symmetry and rotational symmetry.",
   "Urdu terms to check: گردشی تشاکل (rotational symmetry), مرکزِ گردش (centre of rotation), گردشی تشاکل کا درجہ (order), خطِ تشاکل (line of symmetry), گھڑی کی سوئیوں کی سمت / مخالف سمت (clockwise / anticlockwise), متناظر زاویے (corresponding angles), پھرکی (pinwheel).",
   "The numbers and pictures were worked out in content/sources/g6-maths-18/rotational_symmetry.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

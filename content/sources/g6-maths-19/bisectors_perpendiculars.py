import math

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SY_LINES, CO_BISECTORS)

SKILL = CO_BISECTORS
RIGHT = 90


def r1(v):
    return round(v, 1)


def arc_toward(center, target, radius, spread=30):
    """A short compass arc centred on `center`, drawn across `target`."""
    cx, cy = center
    ang = math.degrees(math.atan2(target[1] - cy, target[0] - cx))
    return {"kind": "arc", "center": [r1(cx), r1(cy)], "radius": radius,
            "start": r1((ang - spread / 2) % 360), "sweep": spread, "style": "dashed"}


def crossings(a, b, radius):
    """Where two circles of the same radius round a and b meet (above, below)."""
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    half = math.dist(a, b) / 2
    assert radius > half, "the compass must open more than half of AB"
    h = math.sqrt(radius ** 2 - half ** 2)
    ux, uy = (b[0] - a[0]) / (2 * half), (b[1] - a[1]) / (2 * half)
    up = (r1(mx + uy * h), r1(my - ux * h))
    down = (r1(mx - uy * h), r1(my + ux * h))
    return up, down


def right_mark(x, y, size=4):
    """A small right-angle box above and to the right of (x, y)."""
    return [{"kind": "line", "from": [x, y - size], "to": [x + size, y - size]},
            {"kind": "line", "from": [x + size, y - size], "to": [x + size, y]}]


# --- the finished construction (s3, s4) ---
A, B, RAD = (30, 35), (70, 35), 28
P, Q = crossings(A, B, RAD)
assert P[0] == Q[0] == 50 and P[1] < 35 < Q[1]
assert math.isclose(math.dist(A, P), math.dist(B, P), abs_tol=0.2)
CONSTRUCTION = {
  "width": 100, "height": 70,
  "alt": T("Line segment AB with its midpoint M. Dashed compass arcs from A and from B cross above AB at P and below AB at Q. A dashed line joins P and Q and cuts AB at M, with a small square showing a right angle.",
           "قطعۂ خط AB اور اس کا درمیانی نقطہ M۔ A اور B سے پرکار کی ڈیش والی قوسیں AB کے اوپر P پر اور نیچے Q پر ملتی ہیں۔ ڈیش والی لکیر P اور Q کو ملاتی ہے اور AB کو M پر کاٹتی ہے، اور ایک چھوٹا مربع زاویہ قائمہ دکھاتا ہے۔"),
  "items": [
    {"kind": "line", "from": list(A), "to": list(B)},
    arc_toward(A, P, RAD), arc_toward(A, Q, RAD), arc_toward(B, P, RAD), arc_toward(B, Q, RAD),
    {"kind": "line", "from": [50, 8], "to": [50, 62], "style": "dashed"},
    *right_mark(50, 35),
    {"kind": "point", "at": list(A)}, {"kind": "point", "at": list(B)},
    {"kind": "point", "at": list(P)}, {"kind": "point", "at": list(Q)}, {"kind": "point", "at": [50, 35]},
    {"kind": "label", "at": [24, 35], "text": "A"}, {"kind": "label", "at": [76, 35], "text": "B"},
    {"kind": "label", "at": [56, 12], "text": "P"}, {"kind": "label", "at": [56, 58], "text": "Q"},
    {"kind": "label", "at": [45, 41], "text": "M"},
  ]}

# --- s1: a segment of a given length ---
SEGMENT = {
  "width": 100, "height": 36,
  "alt": T("A straight line segment from point A to point B, 6 cm long.",
           "نقطہ A سے نقطہ B تک ایک سیدھا قطعۂ خط، جس کی لمبائی 6 سینٹی میٹر ہے۔"),
  "items": [
    {"kind": "line", "from": [15, 18], "to": [85, 18]},
    {"kind": "point", "at": [15, 18]}, {"kind": "point", "at": [85, 18]},
    {"kind": "label", "at": [9, 18], "text": "A"}, {"kind": "label", "at": [91, 18], "text": "B"},
    {"kind": "label", "at": [50, 28], "text": "6 cm"},
  ]}

# --- s5: compass opened less than half of AB, arcs do not meet ---
SA, SB, SMALL = (25, 30), (75, 30), 15
assert SMALL < math.dist(SA, SB) / 2
TOO_SMALL = {
  "width": 100, "height": 60,
  "alt": T("Line segment AB. A short dashed arc is drawn from A and another from B, but the compass was opened less than half of AB, so the two arcs stop before the middle and leave a gap. They do not cross.",
           "قطعۂ خط AB۔ A سے ایک چھوٹی ڈیش والی قوس اور B سے دوسری قوس لگائی گئی، لیکن پرکار AB کے آدھے سے کم کھولا گیا، اس لیے دونوں قوسیں درمیان سے پہلے رک جاتی ہیں اور خالی جگہ رہ جاتی ہے۔ وہ آپس میں نہیں ملتیں۔"),
  "items": [
    {"kind": "line", "from": list(SA), "to": list(SB)},
    {"kind": "arc", "center": list(SA), "radius": SMALL, "start": 300, "sweep": 120, "style": "dashed"},
    {"kind": "arc", "center": list(SB), "radius": SMALL, "start": 120, "sweep": 120, "style": "dashed"},
    {"kind": "point", "at": list(SA)}, {"kind": "point", "at": list(SB)},
    {"kind": "label", "at": [19, 30], "text": "A"}, {"kind": "label", "at": [81, 30], "text": "B"},
    {"kind": "label", "at": [50, 22], "text": "?"},
  ]}

# --- s6: AB = 10 cm, each half ---
AB6 = 10
S6 = AB6 // 2
assert S6 == 5 and S6 * 2 == AB6
HALVES = {
  "width": 100, "height": 50,
  "alt": T("Line segment AB, 10 cm long, with its midpoint M. A dashed perpendicular bisector goes through M. The part from A to M is marked with a question mark.",
           "10 سینٹی میٹر لمبا قطعۂ خط AB اور اس کا درمیانی نقطہ M۔ ڈیش والا عمودی ناصف M سے گزرتا ہے۔ A سے M تک کے حصے پر سوالیہ نشان ہے۔"),
  "items": [
    {"kind": "line", "from": [10, 25], "to": [90, 25]},
    {"kind": "line", "from": [50, 5], "to": [50, 45], "style": "dashed"},
    *right_mark(50, 25),
    {"kind": "point", "at": [10, 25]}, {"kind": "point", "at": [90, 25]}, {"kind": "point", "at": [50, 25]},
    {"kind": "label", "at": [5, 25], "text": "A"}, {"kind": "label", "at": [95, 25], "text": "B"},
    {"kind": "label", "at": [45, 31], "text": "M"},
    {"kind": "label", "at": [30, 18], "text": "?"},
    {"kind": "label", "at": [72, 40], "text": "10 cm"},
  ]}

# --- s7: perpendicular from a point outside a line ---
OP, LINE_Y, OR = (50, 30), 45, 22
dx = math.sqrt(OR ** 2 - (LINE_Y - OP[1]) ** 2)
C, D = (r1(OP[0] - dx), LINE_Y), (r1(OP[0] + dx), LINE_Y)
_, FOOT2 = crossings(C, D, OR)
assert FOOT2[0] == 50 and FOOT2[1] > LINE_Y
S7 = RIGHT
OUTSIDE = {
  "width": 100, "height": 75,
  "alt": T("A straight line l with point P above it. Dashed arcs from P cut the line at C and D. Dashed arcs from C and D cross below the line. A dashed line from P through that crossing meets l. The angle where it meets l is marked with a question mark.",
           "سیدھی لکیر l اور اس کے اوپر نقطہ P۔ P سے ڈیش والی قوسیں لکیر کو C اور D پر کاٹتی ہیں۔ C اور D سے ڈیش والی قوسیں لکیر کے نیچے ملتی ہیں۔ P سے اس ملنے کی جگہ تک ڈیش والی لکیر l سے ملتی ہے۔ جہاں یہ l سے ملتی ہے وہاں کے زاویے پر سوالیہ نشان ہے۔"),
  "items": [
    {"kind": "line", "from": [5, LINE_Y], "to": [95, LINE_Y]},
    arc_toward(OP, C, OR), arc_toward(OP, D, OR),
    arc_toward(C, FOOT2, OR), arc_toward(D, FOOT2, OR),
    {"kind": "line", "from": list(OP), "to": [50, 70], "style": "dashed"},
    {"kind": "point", "at": list(OP)}, {"kind": "point", "at": list(C)}, {"kind": "point", "at": list(D)},
    {"kind": "label", "at": [56, 26], "text": "P"},
    {"kind": "label", "at": [C[0] - 3, 51], "text": "C"}, {"kind": "label", "at": [D[0] + 3, 51], "text": "D"},
    {"kind": "label", "at": [92, 40], "text": "l"},
    {"kind": "label", "at": [58, 40], "text": "?"},
  ]}

# --- s8: a point on the perpendicular bisector is equally far from A and B ---
AB8, PA8 = 10, 7
S8 = PA8
assert S8 == 7 and AB8 - PA8 == 3 and 2 * PA8 == 14
EQUAL = {
  "width": 100, "height": 60,
  "alt": T("Line segment AB with a dashed perpendicular bisector. Point P is on the bisector above AB. Lines join P to A and P to B. PA is marked 7 and PB is marked with a question mark.",
           "قطعۂ خط AB اور ڈیش والا عمودی ناصف۔ نقطہ P ناصف پر AB کے اوپر ہے۔ P کو A سے اور P کو B سے لکیریں ملاتی ہیں۔ PA پر 7 لکھا ہے اور PB پر سوالیہ نشان ہے۔"),
  "items": [
    {"kind": "line", "from": [20, 50], "to": [80, 50]},
    {"kind": "line", "from": [50, 5], "to": [50, 57], "style": "dashed"},
    {"kind": "line", "from": [50, 15], "to": [20, 50]},
    {"kind": "line", "from": [50, 15], "to": [80, 50]},
    *right_mark(50, 50),
    {"kind": "point", "at": [20, 50]}, {"kind": "point", "at": [80, 50]}, {"kind": "point", "at": [50, 15]},
    {"kind": "label", "at": [14, 50], "text": "A"}, {"kind": "label", "at": [86, 50], "text": "B"},
    {"kind": "label", "at": [56, 11], "text": "P"},
    {"kind": "label", "at": [29, 29], "text": "7"}, {"kind": "label", "at": [71, 29], "text": "?"},
  ]}

# --- s9: a slanting line through the midpoint ---
SLANT = {
  "width": 100, "height": 60,
  "alt": T("Line segment AB with its midpoint M. A dashed line goes through M but slants across AB; it does not make a right angle with AB.",
           "قطعۂ خط AB اور اس کا درمیانی نقطہ M۔ ڈیش والی لکیر M سے گزرتی ہے لیکن AB پر ترچھی ہے؛ یہ AB کے ساتھ زاویہ قائمہ نہیں بناتی۔"),
  "items": [
    {"kind": "line", "from": [20, 30], "to": [80, 30]},
    {"kind": "line", "from": [35, 5], "to": [65, 55], "style": "dashed"},
    {"kind": "point", "at": [20, 30]}, {"kind": "point", "at": [80, 30]}, {"kind": "point", "at": [50, 30]},
    {"kind": "label", "at": [14, 30], "text": "A"}, {"kind": "label", "at": [86, 30], "text": "B"},
    {"kind": "label", "at": [57, 35], "text": "M"},
  ]}


# --- s11: three small drawings, only number 2 is a perpendicular bisector ---
def panel(i, kind):
    ox = 50 * i
    left, right, mid = ox + 8, ox + 42, ox + 25
    items = [{"kind": "line", "from": [left, 35], "to": [right, 35]},
             {"kind": "point", "at": [left, 35]}, {"kind": "point", "at": [right, 35]},
             {"kind": "label", "at": [mid, 5], "text": str(i + 1)}]
    if kind == "slant":
        items.append({"kind": "line", "from": [ox + 15, 12], "to": [ox + 35, 58], "style": "dashed"})
    elif kind == "true":
        items += [{"kind": "line", "from": [mid, 12], "to": [mid, 58], "style": "dashed"}, *right_mark(mid, 35, 3)]
    else:
        items += [{"kind": "line", "from": [ox + 16, 12], "to": [ox + 16, 58], "style": "dashed"}, *right_mark(ox + 16, 35, 3)]
    return items


PANELS = {
  "width": 150, "height": 62,
  "alt": T("Three drawings, numbered 1, 2 and 3, each with a line segment and a dashed line. In 1 the dashed line goes through the middle of the segment but slants. In 2 the dashed line goes through the middle of the segment at a right angle. In 3 the dashed line makes a right angle but crosses the segment near its left end, not the middle.",
           "تین شکلیں، نمبر 1، 2 اور 3، ہر ایک میں ایک قطعۂ خط اور ایک ڈیش والی لکیر ہے۔ 1 میں ڈیش والی لکیر قطعے کے درمیان سے گزرتی ہے لیکن ترچھی ہے۔ 2 میں ڈیش والی لکیر قطعے کے درمیان سے زاویہ قائمہ پر گزرتی ہے۔ 3 میں ڈیش والی لکیر زاویہ قائمہ بناتی ہے لیکن قطعے کو بائیں سرے کے قریب کاٹتی ہے، درمیان سے نہیں۔"),
  "items": [*panel(0, "slant"), *panel(1, "true"), *panel(2, "off")]}

# question bank and review
QB = 12 // 2
assert QB == 6
R1 = 14 // 2
assert R1 == 7
R2 = 9
assert R2 == 9 and 16 - 9 == 7

lesson = {
 "id": "g6-maths-19-bisectors-and-perpendiculars",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Construct a line segment of given length, its perpendicular bisector, and a perpendicular to a line from a point on it and from a point outside it, using a ruler and compasses.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Perpendicular bisectors and perpendiculars", "عمودی ناصف اور عمود"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": SY_LINES}],
 "misconceptions": [
   {"id": "compass_too_small", "description": "Opens the compass to less than half of AB, so the arcs from A and B do not meet."},
   {"id": "any_bisector_perpendicular", "description": "Thinks any line through the midpoint is a perpendicular bisector, even if it is not at 90°."},
   {"id": "nearer_one_end", "description": "Thinks a point on the perpendicular bisector is nearer to one end of the segment than the other."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("What does the perpendicular bisector of AB do?", "AB کا عمودی ناصف کیا کرتا ہے؟"),
     "options": [
       opt("both", "Cuts AB into two equal parts at 90°", "AB کو 90° پر دو برابر حصوں میں کاٹتا ہے", True,
           "Yes! Equal halves and a right angle, both together.", "جی ہاں! برابر حصے اور زاویہ قائمہ، دونوں ساتھ۔"),
       opt("halves", "Cuts AB into two equal parts at any angle", "AB کو کسی بھی زاویے پر دو برابر حصوں میں کاٹتا ہے", False,
           "That is just a bisector. A perpendicular bisector must also be at 90°.", "یہ صرف ناصف ہے۔ عمودی ناصف کو 90° پر بھی ہونا چاہیے۔", "any_bisector_perpendicular"),
       opt("right", "Meets AB at 90° anywhere along it", "AB سے کہیں بھی 90° پر ملتا ہے", False,
           "It must also go through the middle of AB.", "اسے AB کے درمیان سے بھی گزرنا چاہیے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("AB is 12 cm. Its perpendicular bisector cuts it at M. How long is AM, in cm?", "AB کی لمبائی 12 سینٹی میٹر ہے۔ اس کا عمودی ناصف اسے M پر کاٹتا ہے۔ AM کتنے سینٹی میٹر ہے؟"),
     QB,
     T("M is the middle of AB: 12 ÷ 2.", "M، AB کا درمیان ہے: 12 ÷ 2"),
     T("Right! 6 cm.", "درست! 6 سینٹی میٹر"),
     T("The bisector cuts AB in half: 12 ÷ 2 = 6 cm.", "ناصف AB کو آدھا کرتا ہے: 12 ÷ 2 = 6 سینٹی میٹر"),
     common_wrong=[wrong(12, "12 cm is all of AB. AM is half: 6 cm.", "12 پورا AB ہے۔ AM آدھا ہے: 6 سینٹی میٹر")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("AB is 8 cm. Ayesha opens her compass to 3 cm and draws arcs from A and from B, but the arcs never cross. What went wrong?",
                 "AB کی لمبائی 8 سینٹی میٹر ہے۔ عائشہ پرکار 3 سینٹی میٹر کھول کر A اور B سے قوسیں لگاتی ہے، لیکن قوسیں آپس میں نہیں ملتیں۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("more", "3 cm is less than half of 8 cm. She must open it more than 4 cm.", "3 سینٹی میٹر، 8 کے آدھے سے کم ہے۔ اسے پرکار 4 سے زیادہ کھولنا چاہیے۔", True,
           "Yes! Each arc must reach past the middle so they can cross.", "جی ہاں! ہر قوس کو درمیان سے آگے پہنچنا چاہیے تاکہ وہ مل سکیں۔"),
       opt("change", "She should change the compass between A and B.", "اسے A اور B کے درمیان پرکار بدل دینا چاہیے۔", False,
           "Keep the same opening for both. The problem is that 3 cm is too small.", "دونوں کے لیے ایک ہی کھلاؤ رکھیں۔ مسئلہ یہ ہے کہ 3 سینٹی میٹر بہت کم ہے۔"),
       opt("nothing", "Nothing. Arcs never cross.", "کوئی غلطی نہیں۔ قوسیں کبھی نہیں ملتیں۔", False,
           "They do cross if the compass opens more than half of AB, more than 4 cm.", "اگر پرکار AB کے آدھے، یعنی 4 سے زیادہ کھلے تو وہ ملتی ہیں۔", "compass_too_small"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_bisector", "front": T("What is a perpendicular bisector?", "عمودی ناصف کیا ہے؟"),
    "back": T("A line that cuts a segment into two equal parts at 90°.", "وہ لکیر جو قطعۂ خط کو 90° پر دو برابر حصوں میں کاٹے۔")},
   {"id": "f_compass", "front": T("How wide should the compass open?", "پرکار کتنا کھولنا چاہیے؟"),
    "back": T("More than half of AB, the same for both arcs.", "AB کے آدھے سے زیادہ، دونوں قوسوں کے لیے ایک جیسا۔")},
 ],
 "home_tasks": [{"id": "h_construct", "text": T(
   "On paper, draw AB = 8 cm with a ruler. Open your compass more than 4 cm and draw arcs from A and from B, above and below AB. Join the two crossing points. No compass? Tie a string to a pencil, hold the other end on A, and draw the arcs; keep the same string length for B. Now fold the paper so A lands exactly on B. The fold should lie on your line and cross AB at a right angle.",
   "کاغذ پر پیمانے سے 8 سینٹی میٹر کا AB بنائیں۔ پرکار 4 سے زیادہ کھولیں اور A اور B سے، AB کے اوپر اور نیچے قوسیں لگائیں۔ ملنے والے دونوں نقطوں کو ملا دیں۔ پرکار نہیں ہے؟ پنسل سے دھاگا باندھیں، دوسرا سرا A پر پکڑیں اور قوس بنائیں؛ B کے لیے دھاگے کی لمبائی وہی رکھیں۔ اب کاغذ ایسے موڑیں کہ A بالکل B پر آ جائے۔ تہ آپ کی لکیر پر آنی چاہیے اور AB کو زاویہ قائمہ پر کاٹنا چاہیے۔")}],
 "glossary": [T("Perpendicular bisector", "عمودی ناصف"), T("Bisector", "ناصف"), T("Perpendicular", "عمود"),
              T("Pair of compasses", "پرکار"), T("Arc", "قوس"), T("Line segment", "قطعۂ خط"), T("Midpoint", "درمیانی نقطہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Bilal wants to tie the kite string exactly in the middle of a stick, at a right angle. How can he find that spot without guessing?",
                     "بلال پتنگ کی ڈور ڈنڈی کے بالکل درمیان میں، زاویہ قائمہ پر باندھنا چاہتا ہے۔ وہ اندازے کے بغیر وہ جگہ کیسے ڈھونڈے؟"),
    "figure": SEGMENT,
    "text": T("Today we construct lines with three tools: a ruler for straight lines and lengths, a pair of compasses for arcs, and a protractor for checking angles. First we draw a line segment AB of a given length, like 6 cm, with the ruler. Then we find its middle and a line at 90° through it.",
              "آج ہم تین اوزاروں سے لکیریں بنائیں گے: سیدھی لکیر اور لمبائی کے لیے پیمانہ (ruler)، قوس کے لیے پرکار (pair of compasses)، اور زاویے جانچنے کے لیے زاویہ پیما (protractor)۔ پہلے پیمانے سے دی گئی لمبائی کا قطعۂ خط (line segment) AB بنائیں، جیسے 6 سینٹی میٹر۔ پھر اس کا درمیان اور اس سے 90° پر گزرنے والی لکیر ڈھونڈیں گے۔")},
   number_question(
     "s2_foundation",
     T("Two perpendicular lines meet. What angle do they make, in degrees?", "دو عمودی لکیریں ملتی ہیں۔ وہ کتنے درجے کا زاویہ بناتی ہیں؟"),
     RIGHT,
     T("Think of the corner of a page.", "کاپی کے صفحے کے کونے کے بارے میں سوچیں۔"),
     T("Right! Perpendicular lines meet at 90°.", "درست! عمودی لکیریں 90° پر ملتی ہیں۔"),
     T("Perpendicular lines meet at a right angle, 90°.", "عمودی لکیریں زاویہ قائمہ، 90° پر ملتی ہیں۔"),
     common_wrong=[wrong(180, "180° is a straight line. Perpendicular lines make a right angle: 90°.", "180° سیدھی لکیر ہے۔ عمودی لکیریں زاویہ قائمہ بناتی ہیں: 90°"),
                   wrong(45, "45° is half a right angle. Perpendicular means 90°.", "45° زاویہ قائمہ کا آدھا ہے۔ عمودی کا مطلب 90° ہے۔")],
     qtype="recall", skill=SY_LINES),
   {"id": "s3_construct", "type": "explain",
    "character": say("happy", "Same compass opening from A and from B. That is the whole secret!", "A اور B سے پرکار کا ایک جیسا کھلاؤ۔ یہی سارا راز ہے!"),
    "figure": CONSTRUCTION,
    "text": T("A bisector cuts a line segment into two equal parts. A perpendicular bisector (right bisector) does more: it cuts AB into two equal parts AND makes 90° with it. To construct it: 1. Draw AB with a ruler. 2. Open the compass more than half of AB. Put the point on A and draw arcs above and below AB. 3. Without changing the opening, do the same from B. 4. Join the two crossing points P and Q with a ruler. PQ cuts AB at its midpoint M at 90°. To draw a perpendicular from a point P to a line, draw arcs from P that cut the line at C and D (if P is on the line, C and D are on either side of it), then construct the perpendicular bisector of CD.",
              "ناصف (bisector) قطعۂ خط کو دو برابر حصوں میں کاٹتا ہے۔ عمودی ناصف (perpendicular bisector) اس سے زیادہ کرتا ہے: یہ AB کو دو برابر حصوں میں کاٹتا ہے اور اس کے ساتھ 90° بھی بناتا ہے۔ اسے بنانے کا طریقہ: 1۔ پیمانے سے AB کھینچیں۔ 2۔ پرکار AB کے آدھے سے زیادہ کھولیں۔ نوک A پر رکھ کر AB کے اوپر اور نیچے قوسیں (arcs) لگائیں۔ 3۔ کھلاؤ بدلے بغیر یہی B سے کریں۔ 4۔ ملنے والے دونوں نقطوں P اور Q کو پیمانے سے ملا دیں۔ PQ، AB کو اس کے درمیانی نقطے M پر 90° پر کاٹتا ہے۔ کسی نقطے P سے لکیر پر عمود (perpendicular) بنانے کے لیے P سے قوسیں لگائیں جو لکیر کو C اور D پر کاٹیں (اگر P لکیر پر ہو تو C اور D اس کے دونوں طرف ہوں گے)، پھر CD کا عمودی ناصف بنائیں۔")},
   {"id": "s4_order", "type": "choice",
    "figure": CONSTRUCTION,
    "prompt": T("Which order of steps constructs the perpendicular bisector of AB?", "کس ترتیب سے AB کا عمودی ناصف بنتا ہے؟"),
    "options": [
      opt("join_first", "Join P and Q; draw AB; draw arcs from A; draw arcs from B", "P اور Q ملائیں؛ AB کھینچیں؛ A سے قوسیں؛ B سے قوسیں", False,
          "P and Q don't exist yet! They come from the arcs. Draw AB first.", "P اور Q ابھی موجود ہی نہیں! یہ قوسوں سے بنتے ہیں۔ پہلے AB کھینچیں۔"),
      opt("right_order", "Draw AB; arcs from A; arcs from B with the same opening; join P and Q", "AB کھینچیں؛ A سے قوسیں؛ اسی کھلاؤ سے B سے قوسیں؛ P اور Q ملائیں", True,
          "Yes! Segment, arcs, arcs, then join the crossings.", "جی ہاں! قطعہ، قوسیں، قوسیں، پھر ملنے کے نقطے ملائیں۔"),
      opt("arcs_first", "Draw arcs from A and B; then draw AB; then join P and Q", "A اور B سے قوسیں؛ پھر AB کھینچیں؛ پھر P اور Q ملائیں", False,
          "You need A and B on the paper before you can put the compass on them. Draw AB first.", "پرکار رکھنے سے پہلے کاغذ پر A اور B ہونے چاہییں۔ پہلے AB کھینچیں۔"),
    ]},
   {"id": "s5_why_half", "type": "choice",
    "figure": TOO_SMALL,
    "prompt": T("Hira's arcs from A and B did not meet. Why must the compass open more than half of AB?", "حرا کی A اور B والی قوسیں نہیں ملیں۔ پرکار AB کے آدھے سے زیادہ کیوں کھلنا چاہیے؟"),
    "options": [
      opt("reach", "So each arc reaches past the middle of AB and the two arcs can cross", "تاکہ ہر قوس AB کے درمیان سے آگے پہنچے اور دونوں قوسیں مل سکیں", True,
          "Yes! Less than half and the arcs stop short of each other, like in the picture.", "جی ہاں! آدھے سے کم ہو تو قوسیں ایک دوسرے سے پہلے رک جاتی ہیں، جیسے تصویر میں۔"),
      opt("neat", "So the drawing looks neater", "تاکہ شکل زیادہ صاف لگے", False,
          "It is not about looks. With less than half, the arcs cannot meet at all.", "بات خوبصورتی کی نہیں۔ آدھے سے کم ہو تو قوسیں مل ہی نہیں سکتیں۔", "compass_too_small"),
      opt("any", "It doesn't matter; any opening works", "کوئی فرق نہیں؛ کوئی بھی کھلاؤ چلے گا", False,
          "Look at the picture: the arcs left a gap. The opening must be more than half of AB.", "تصویر دیکھیں: قوسوں میں خالی جگہ رہ گئی۔ کھلاؤ AB کے آدھے سے زیادہ ہونا چاہیے۔", "compass_too_small"),
    ]},
   dict(number_question(
     "s6_half",
     T("AB is 10 cm. Its perpendicular bisector cuts AB at M. How long is AM, in cm?", "AB کی لمبائی 10 سینٹی میٹر ہے۔ اس کا عمودی ناصف AB کو M پر کاٹتا ہے۔ AM کتنے سینٹی میٹر ہے؟"),
     S6,
     T("M is the midpoint, so AM is half of 10.", "M درمیانی نقطہ ہے، تو AM، 10 کا آدھا ہے۔"),
     T("Right! 5 cm, and MB is 5 cm too.", "درست! 5 سینٹی میٹر، اور MB بھی 5 ہے۔"),
     T("The bisector cuts AB into two equal parts: 10 ÷ 2 = 5 cm.", "ناصف AB کو دو برابر حصوں میں کاٹتا ہے: 10 ÷ 2 = 5 سینٹی میٹر"),
     common_wrong=[wrong(AB6, "10 cm is the whole of AB. Each half is 10 ÷ 2 = 5 cm.", "10 پورا AB ہے۔ ہر آدھا 10 ÷ 2 = 5 ہے۔"),
                   wrong(AB6 * 2, "Bisect means cut in half, not double: 5 cm.", "ناصف کا مطلب آدھا کرنا ہے، دگنا نہیں: 5 سینٹی میٹر")]),
     figure=HALVES),
   dict(number_question(
     "s7_angle",
     T("Sana draws a perpendicular from P to line l, as in the picture. What angle does it make with l, in degrees?", "ثنا نے تصویر کی طرح P سے لکیر l پر عمود بنایا۔ یہ l کے ساتھ کتنے درجے کا زاویہ بناتا ہے؟"),
     S7,
     T("Perpendicular means it meets the line at a right angle.", "عمود کا مطلب ہے لکیر سے زاویہ قائمہ پر ملنا۔"),
     T("Right! 90°. Check it with a protractor.", "درست! 90°۔ زاویہ پیما سے جانچ لیں۔"),
     T("A perpendicular always makes 90° with the line.", "عمود ہمیشہ لکیر کے ساتھ 90° بناتا ہے۔"),
     common_wrong=[wrong(180, "180° is a straight line. A perpendicular makes 90°.", "180° سیدھی لکیر ہے۔ عمود 90° بناتا ہے۔"),
                   wrong(45, "The construction gives a right angle, not 45°: 90°.", "یہ بناوٹ زاویہ قائمہ دیتی ہے، 45° نہیں: 90°")]),
     figure=OUTSIDE),
   dict(number_question(
     "s8_equal",
     T("AB is 10 cm. Point P is on the perpendicular bisector of AB, and P is 7 cm from A. How far is P from B, in cm?", "AB کی لمبائی 10 سینٹی میٹر ہے۔ نقطہ P، AB کے عمودی ناصف پر ہے اور A سے 7 سینٹی میٹر دور ہے۔ P، B سے کتنے سینٹی میٹر دور ہے؟"),
     S8,
     T("The arcs from A and B had the same radius. What does that tell you about P?", "A اور B سے قوسوں کا رداس ایک جیسا تھا۔ اس سے P کے بارے میں کیا پتا چلتا ہے؟"),
     T("Right! 7 cm. Every point on the perpendicular bisector is the same distance from A and B.", "درست! 7 سینٹی میٹر۔ عمودی ناصف کا ہر نقطہ A اور B سے برابر فاصلے پر ہوتا ہے۔"),
     T("A point on the perpendicular bisector is equally far from both ends: 7 cm.", "عمودی ناصف کا نقطہ دونوں سروں سے برابر دور ہوتا ہے: 7 سینٹی میٹر"),
     common_wrong=[wrong(AB8 - PA8, "10 − 7 does not work here. P is on the bisector, so PB = PA = 7 cm.", "یہاں 10 − 7 نہیں چلتا۔ P ناصف پر ہے، اس لیے PB = PA = 7 سینٹی میٹر", "nearer_one_end"),
                   wrong(2 * PA8, "P is not twice as far from B. It is equally far: 7 cm.", "P، B سے دگنا دور نہیں۔ برابر دور ہے: 7 سینٹی میٹر", "nearer_one_end")]),
     figure=EQUAL),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "figure": SLANT,
    "prompt": T("Usman marks the midpoint M of AB and draws a slanting line through it. He says it is the perpendicular bisector. What went wrong?",
                "عثمان AB کا درمیانی نقطہ M لگاتا ہے اور اس سے ترچھی لکیر کھینچتا ہے۔ وہ کہتا ہے یہ عمودی ناصف ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("not_90", "It bisects AB but is not at 90°, so it is not perpendicular.", "یہ AB کو آدھا کرتی ہے لیکن 90° پر نہیں، اس لیے عمودی نہیں۔", True,
          "Yes! A perpendicular bisector needs both: the middle AND 90°.", "جی ہاں! عمودی ناصف کو دونوں چاہییں: درمیان بھی اور 90° بھی۔"),
      opt("not_middle", "It doesn't go through the middle of AB.", "یہ AB کے درمیان سے نہیں گزرتی۔", False,
          "It does go through M, the middle. The problem is the angle: it is not 90°.", "یہ درمیان M سے گزرتی ہے۔ مسئلہ زاویے کا ہے: یہ 90° نہیں۔"),
      opt("nothing", "Nothing. Any line through the midpoint is a perpendicular bisector.", "کوئی غلطی نہیں۔ درمیانی نقطے سے گزرنے والی ہر لکیر عمودی ناصف ہے۔", False,
          "Many lines pass through M, but only one makes 90° with AB.", "M سے بہت سی لکیریں گزرتی ہیں، لیکن صرف ایک AB سے 90° بناتی ہے۔", "any_bisector_perpendicular"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is every point on the perpendicular bisector the same distance from A and from B? Can you teach me?",
                     "عمودی ناصف کا ہر نقطہ A اور B سے برابر فاصلے پر کیوں ہوتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "figure": CONSTRUCTION,
    "task": T("In your own words: why is a point on the perpendicular bisector of AB equally far from A and B?",
              "اپنے الفاظ میں بتائیں: AB کے عمودی ناصف کا نقطہ A اور B سے برابر دور کیوں ہوتا ہے؟"),
    "key_idea": "The crossing points come from arcs of the same radius drawn from A and from B, so they are equally far from both. Folding the paper so A lands on B makes a fold along the perpendicular bisector: the two sides match, so any point on the fold is the same distance from A and B.",
    "levels": {
      "got_it": "Says the arcs from A and B had the same radius (same compass opening), or that folding A onto B puts the two halves on top of each other, so distances to A and B match.",
      "partly": "Says the line is in the middle or is a mirror line, without linking it to equal arcs or matching halves.",
      "not_yet": "Gives no reason, or says one end is nearer."},
    "keywords": [
      ["same", "equal", "radius", "opening", "ایک جیسا", "برابر", "رداس", "کھلاؤ", "barabar"],
      ["fold", "mirror", "match", "تہ", "موڑ", "عکس", "mor"],
      ["arc", "compass", "قوس", "پرکار", "parkar"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Same compass opening from A and B, so the crossing points are equally far from both.", "بہت خوب! A اور B سے پرکار کا ایک جیسا کھلاؤ، اس لیے ملنے کے نقطے دونوں سے برابر دور ہیں۔"),
      "partly": T("Good start! Now say how the same compass opening, or folding A onto B, makes the distances equal.", "اچھی شروعات! اب بتائیں کہ پرکار کا ایک جیسا کھلاؤ، یا A کو B پر موڑنا، فاصلے برابر کیسے کرتا ہے۔"),
      "not_yet": T("Think: the arcs from A and B used the same compass opening. What does that say about P?", "سوچیں: A اور B کی قوسیں پرکار کے ایک ہی کھلاؤ سے بنیں۔ اس سے P کے بارے میں کیا پتا چلتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_which", "type": "choice",
    "figure": PANELS,
    "prompt": T("Which drawing shows a perpendicular bisector of the segment?", "کس شکل میں قطعۂ خط کا عمودی ناصف ہے؟"),
    "options": [
      opt("fig_1", "Drawing 1", "شکل 1", False,
          "It goes through the middle but slants. It is not at 90°.", "یہ درمیان سے گزرتی ہے لیکن ترچھی ہے۔ 90° پر نہیں۔", "any_bisector_perpendicular"),
      opt("fig_2", "Drawing 2", "شکل 2", True,
          "Yes! Through the middle and at a right angle.", "جی ہاں! درمیان سے اور زاویہ قائمہ پر۔"),
      opt("fig_3", "Drawing 3", "شکل 3", False,
          "It is at 90°, but it does not cut the segment into two equal parts.", "یہ 90° پر ہے، لیکن قطعے کو دو برابر حصوں میں نہیں کاٹتی۔"),
    ]},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Middle and 90°, made with one compass opening. Well done!", "درمیان اور 90°، پرکار کے ایک کھلاؤ سے۔ شاباش!"),
    "figure": CONSTRUCTION,
    "text": T("A perpendicular bisector cuts a line segment into two equal parts at 90°. Open the compass more than half of AB, draw arcs from A and from B with the same opening, and join the crossing points. Every point on it is equally far from A and B. A perpendicular from a point to a line is made the same way, using the two points where your arcs cut the line. Check by folding or with a protractor.",
              "عمودی ناصف قطعۂ خط کو 90° پر دو برابر حصوں میں کاٹتا ہے۔ پرکار AB کے آدھے سے زیادہ کھولیں، ایک ہی کھلاؤ سے A اور B سے قوسیں لگائیں، اور ملنے کے نقطے ملا دیں۔ اس کا ہر نقطہ A اور B سے برابر دور ہوتا ہے۔ کسی نقطے سے لکیر پر عمود بھی اسی طرح بنتا ہے، ان دو نقطوں سے جہاں قوسیں لکیر کو کاٹتی ہیں۔ کاغذ موڑ کر یا زاویہ پیما سے جانچیں۔"),
    "points": [T("Equal halves and 90°.", "برابر حصے اور 90°۔"),
               T("Compass: more than half of AB.", "پرکار: AB کے آدھے سے زیادہ۔"),
               T("Points on it: equally far from A and B.", "اس کے نقطے: A اور B سے برابر دور۔")]},
 ],
 "review_questions": [
   {"id": "r_half", "type": "apply", "skill": SKILL, "step": number_question(
     "r_half",
     T("AB is 14 cm. Its perpendicular bisector cuts it at M. How long is MB, in cm?", "AB کی لمبائی 14 سینٹی میٹر ہے۔ اس کا عمودی ناصف اسے M پر کاٹتا ہے۔ MB کتنے سینٹی میٹر ہے؟"),
     R1,
     T("14 ÷ 2.", "14 ÷ 2"),
     T("Right! 7 cm.", "درست! 7 سینٹی میٹر"),
     T("M is the middle: 14 ÷ 2 = 7 cm.", "M درمیان ہے: 14 ÷ 2 = 7 سینٹی میٹر"),
     common_wrong=[wrong(14, "14 cm is all of AB. MB is half: 7 cm.", "14 پورا AB ہے۔ MB آدھا ہے: 7 سینٹی میٹر")],
     qtype=None)},
   {"id": "r_equal", "type": "apply", "skill": SKILL, "step": number_question(
     "r_equal",
     T("AB is 16 cm. A point on the perpendicular bisector of AB is 9 cm from B. How far is it from A, in cm?", "AB کی لمبائی 16 سینٹی میٹر ہے۔ AB کے عمودی ناصف پر ایک نقطہ B سے 9 سینٹی میٹر دور ہے۔ یہ A سے کتنا دور ہے؟"),
     R2,
     T("Points on the perpendicular bisector are equally far from A and B.", "عمودی ناصف کے نقطے A اور B سے برابر دور ہوتے ہیں۔"),
     T("Right! 9 cm.", "درست! 9 سینٹی میٹر"),
     T("Same distance from both ends: 9 cm.", "دونوں سروں سے برابر فاصلہ: 9 سینٹی میٹر"),
     common_wrong=[wrong(7, "16 − 9 does not work here. It is equally far from both: 9 cm.", "یہاں 16 − 9 نہیں چلتا۔ دونوں سے برابر دور ہے: 9 سینٹی میٹر", "nearer_one_end")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Geometrical Constructions unit. No textbook text or exercises were used.",
   "The app cannot see real drawings, so practice checks the reasoning behind the construction (order of steps, why the compass opens more than half of AB, equal halves, 90°, equal distances). The home task is the real construction; ask students to show the folded paper or the arcs in class.",
   "The figures are drawn by the app from coordinates worked out in the script; the arcs are placed where the circles really cross.",
   "Perpendiculars from a point on a line and from a point outside it are taught as the same idea: arcs from the point cut the line at C and D, then construct the perpendicular bisector of CD.",
   "Urdu terms to check: عمودی ناصف (perpendicular bisector), ناصف (bisector), عمود (perpendicular), پرکار (pair of compasses), زاویہ پیما (protractor), پیمانہ (ruler), قوس (arc), قطعۂ خط (line segment), درمیانی نقطہ (midpoint).",
   "The numbers and figures were worked out in content/sources/g6-maths-19/bisectors_perpendiculars.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

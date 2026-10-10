"""Practice set for Exercise 9.3 of the book: lines of symmetry of shapes and
letters, completing a shape across a mirror line on a grid, the order of
rotational symmetry, and turning a point about a centre on a grid. The
questions are new; only the kinds of question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    SY_SHAPES, SY_LINE_SYMMETRY, SY_ROTATIONAL)
from figs import (fig, with_fig, poly, label, dot, seg, regular, polar, order, lines, closed_pieces, stroke_items,
                  letter_items, letter_symmetry, letter_pieces, mirror_line, Grid, reflect_cells, turn_cells, C, FULL)

SKILL = EX_SKILL["9.3"]

# ---------- shapes, checked by really flipping and turning ----------
PENTAGON = regular(5, C, 26)
OCTAGON = regular(8, C, 26, start=-22.5)
HEXAGON = regular(6, C, 26, start=0)
SQUARE = regular(4, C, 26, start=-45)
TRIANGLE = regular(3, C, 26)
PARALLELOGRAM = [C + complex(-34, -16), C + complex(14, -16), C + complex(34, 16), C + complex(-14, 16)]
PIN = [[C, polar(C, 28, a), polar(C, 28 * 0.55, a + 50)] for a in (-90, 0, 90, 180)]

assert (lines(closed_pieces(PENTAGON), C), order(closed_pieces(PENTAGON), C)) == (5, 5)
assert (lines(closed_pieces(OCTAGON), C), order(closed_pieces(OCTAGON), C)) == (8, 8)
assert (lines(closed_pieces(HEXAGON), C), order(closed_pieces(HEXAGON), C)) == (6, 6)
assert (lines(closed_pieces(SQUARE), C), order(closed_pieces(SQUARE), C)) == (4, 4)
assert (lines(closed_pieces(TRIANGLE), C), order(closed_pieces(TRIANGLE), C)) == (3, 3)
assert (lines(closed_pieces(PARALLELOGRAM), C), order(closed_pieces(PARALLELOGRAM), C)) == (0, 2)
assert (lines(PIN, C), order(PIN, C)) == (0, 4)

# q2: lines of symmetry of a regular pentagon
Q2 = lines(closed_pieces(PENTAGON), C)
assert Q2 == 5 and 2 * Q2 == 10
# q3: letters A H N E F: how many have no line of symmetry
ROW = "AHNEF"
LET = {k: letter_symmetry(k) for k in ROW}
assert LET == {"A": (1, 1), "H": (2, 2), "N": (0, 2), "E": (1, 1), "F": (0, 1)}
Q3 = sum(1 for k in ROW if LET[k][0] == 0)
assert Q3 == 2 and sum(1 for k in ROW if LET[k][0] == 1) == 2 and len(ROW) == 5
# q7: order of the pinwheel
Q7 = order(PIN, C)
assert Q7 == 4
# q8: smallest turn of a regular octagon
Q8 = FULL // order(closed_pieces(OCTAGON), C)
assert Q8 == 45 and FULL // 8 == 45 and 8 * 45 == FULL
# q13: a fan with 3 equal blades
Q13 = FULL // 3
assert Q13 == 120 and 3 * 120 == FULL

# ---------- grids ----------
# q4: vertical mirror at column 6; a triangle on the left; Q is its corner farthest from the mirror
G1 = Grid(12, 6)
MIRROR_COL = 6
TRI = [(4, 1), (1, 4), (4, 5)]
Q_PT = max(TRI, key=lambda p: MIRROR_COL - p[0])
assert Q_PT == (1, 4)
Q_IMG = reflect_cells([Q_PT], "v", MIRROR_COL)[0]
Q4 = Q_IMG[0] - MIRROR_COL
assert Q_IMG == (11, 4) and Q4 == 5 and MIRROR_COL - Q_PT[0] == 5 and Q_IMG[0] - Q_PT[0] == 10
# the image triangle really is the mirror picture of the original
assert sorted(reflect_cells(TRI, "v", MIRROR_COL)) == [(8, 1), (8, 5), (11, 4)]

# q5: horizontal mirror at row 3; R is 2 squares above it
G2 = Grid(8, 6)
MIRROR_ROW = 3
R_PT = (4, 1)
assert MIRROR_ROW - R_PT[1] == 2
R_IMG = reflect_cells([R_PT], "h", MIRROR_ROW)[0]
Q5 = R_IMG[1] - R_PT[1]
assert R_IMG == (4, 5) and Q5 == 4 and R_IMG[1] - MIRROR_ROW == 2 and MIRROR_ROW == 3

# q6: a staircase of unit squares left of the mirror (cells by lower-left corner)
G3 = Grid(12, 6)
STAIRS = [(3, 4)] + [(4, 3), (4, 4)] + [(5, 2), (5, 3), (5, 4)]
IMG = [(2 * MIRROR_COL - 1 - c, r) for c, r in STAIRS]    # a cell spans [c, c+1]
assert IMG == [(8, 4), (7, 3), (7, 4), (6, 2), (6, 3), (6, 4)]
assert not set(STAIRS) & set(IMG)
Q6 = len(STAIRS) + len(IMG)
assert len(STAIRS) == 1 + 2 + 3 == 6 and Q6 == 12

# q9, q10: turning about O at grid point (4, 3)
G4 = Grid(8, 6)
O = (4, 3)
A9 = (7, 3)
A9_IMG = turn_cells([A9], O, 1)[0]      # a quarter turn clockwise
assert A9_IMG == (4, 6) and A9_IMG[1] - O[1] == 3 and A9_IMG[0] == O[0]      # 3 squares below O
assert turn_cells([A9], O, 3)[0] == (4, 0)                                    # anticlockwise: 3 above O
assert turn_cells([A9], O, 2)[0] == (1, 3)                                    # half turn: 3 left of O
A10 = (7, 1)
A10_IMG = turn_cells([A10], O, 2)[0]       # a half turn
assert A10_IMG == (1, 5)
Q10 = O[0] - A10_IMG[0]
assert Q10 == 3 and A10[0] - O[0] == 3 and O[1] - A10[1] == 2 and A10_IMG[1] - O[1] == 2 and 2 * 3 == 6

# bank and review
QB1 = lines(closed_pieces(TRIANGLE), C)
assert QB1 == 3
QB2 = order(closed_pieces(HEXAGON), C)
assert QB2 == 6
QB3 = FULL // 5
assert QB3 == 72 and 5 * 72 == FULL
R1 = letter_symmetry("H")[0]
assert R1 == 2
R2 = FULL // order(closed_pieces(HEXAGON), C)
assert R2 == 60

# ---------- figures ----------
F_PENT = fig(100, 64,
    "A regular pentagon: five equal sides and five equal corners. No lines are drawn on it.",
    "ایک باقاعدہ پانچ ضلعی شکل: پانچ برابر اضلاع اور پانچ برابر کونے۔ اس پر کوئی لکیر نہیں۔",
    [poly(PENTAGON, fill=True)])
LETTER_ITEMS = []
for i, k in enumerate(ROW):
    LETTER_ITEMS += letter_items(k, complex(22 + 34 * i, 22))
    LETTER_ITEMS.append(label((22 + 34 * i, 48), str(i + 1)))
F_LETTERS = fig(176, 56,
    "Five capital letters drawn with straight strokes, numbered 1 to 5: A, H, N, E and F. Each letter is taller than it is wide.",
    "سیدھی لکیروں سے بنے پانچ بڑے انگریزی حروف، 1 سے 5 تک نمبر: A، H، N، E اور F۔ ہر حرف چوڑائی سے زیادہ اونچا ہے۔",
    LETTER_ITEMS)
F_TRI_MIRROR = G1.figure(
    "A squared grid 12 squares wide and 6 tall. A dashed mirror line goes down the middle. On the left is a triangle with a corner marked Q, the corner farthest from the mirror line, 5 squares away from it.",
    "12 خانے چوڑا اور 6 خانے اونچا چوکور جال۔ بیچ میں اوپر سے نیچے ڈیش والی آئینہ لکیر ہے۔ بائیں طرف ایک مثلث ہے جس کا ایک کونا Q نشان زد ہے، جو آئینہ لکیر سے سب سے دور، 5 خانے کے فاصلے پر ہے۔",
    [G1.vmirror(MIRROR_COL), G1.shape(TRI), dot(G1.at(*Q_PT)), label(G1.at(Q_PT[0] - 0.1, Q_PT[1] - 0.7), "Q")])
F_HMIRROR = G2.figure(
    "A squared grid 8 squares wide and 6 tall. A dashed mirror line goes across it, 3 squares from the top. Point R is 2 squares above the mirror line.",
    "8 خانے چوڑا اور 6 خانے اونچا چوکور جال۔ اس پر افقی ڈیش والی آئینہ لکیر اوپر سے 3 خانے نیچے ہے۔ نقطہ R آئینہ لکیر سے 2 خانے اوپر ہے۔",
    [G2.hmirror(MIRROR_ROW), dot(G2.at(*R_PT)), label(G2.at(R_PT[0] + 0.7, R_PT[1] - 0.5), "R")])
F_STAIRS = G3.figure(
    "A squared grid 12 squares wide and 6 tall. A dashed mirror line goes down the middle. On the left, 6 squares are shaded in a staircase: 1 square in the first column, 2 in the next and 3 in the one beside the mirror line. The right side is empty.",
    "12 خانے چوڑا اور 6 خانے اونچا چوکور جال۔ بیچ میں اوپر سے نیچے ڈیش والی آئینہ لکیر ہے۔ بائیں طرف 6 خانے سیڑھی کی شکل میں رنگے ہیں: پہلے کالم میں 1، اگلے میں 2 اور آئینہ لکیر کے ساتھ والے میں 3۔ دائیں طرف خالی ہے۔",
    [G3.vmirror(MIRROR_COL)] + [poly([G3.at(c, r), G3.at(c + 1, r), G3.at(c + 1, r + 1), G3.at(c, r + 1)], fill=True) for c, r in STAIRS])
F_PIN = fig(100, 64,
    "A paper pinwheel with four blades around a dot in the middle. Each blade is a triangle bent the same way round.",
    "چار پروں والی کاغذ کی پھرکی، بیچ میں ایک نقطہ ہے۔ ہر پر ایک مثلث ہے جو ایک ہی طرف مڑا ہوا ہے۔",
    [poly(p, fill=True) for p in PIN] + [dot(C)])
F_OCT = fig(100, 64,
    "A regular octagon: eight equal sides and eight equal corners, like a stop sign, with a dot at its centre.",
    "ایک باقاعدہ آٹھ ضلعی شکل: آٹھ برابر اضلاع اور آٹھ برابر کونے، رکنے کے نشان کی طرح، مرکز پر ایک نقطہ ہے۔",
    [poly(OCTAGON, fill=True), dot(C)])
F_TURN9 = G4.figure(
    "A squared grid 8 squares wide and 6 tall. The centre of turning O is a dot in the middle. Point A is a dot 3 squares to the right of O on the same row.",
    "8 خانے چوڑا اور 6 خانے اونچا چوکور جال۔ گردش کا مرکز O درمیان میں ایک نقطہ ہے۔ نقطہ A اسی صف میں O سے 3 خانے دائیں ہے۔",
    [dot(G4.at(*O)), label(G4.at(O[0] - 0.1, O[1] - 0.7), "O"), dot(G4.at(*A9)), label(G4.at(A9[0] - 0.1, A9[1] - 0.7), "A")])
F_TURN10 = G4.figure(
    "A squared grid 8 squares wide and 6 tall. The centre of turning O is a dot in the middle. Point A is a dot 3 squares to the right of O and 2 squares above it.",
    "8 خانے چوڑا اور 6 خانے اونچا چوکور جال۔ گردش کا مرکز O درمیان میں ایک نقطہ ہے۔ نقطہ A، O سے 3 خانے دائیں اور 2 خانے اوپر ہے۔",
    [dot(G4.at(*O)), label(G4.at(O[0] - 0.1, O[1] + 0.7), "O"), dot(G4.at(*A10)), label(G4.at(A10[0] - 0.1, A10[1] - 0.7), "A")])
F_PARA = fig(100, 64,
    "A parallelogram, slanting to the right, with a dot at its centre. No lines are drawn on it.",
    "ایک متوازی الاضلاع جو دائیں طرف جھکا ہوا ہے، مرکز پر ایک نقطہ ہے۔ اس پر کوئی لکیر نہیں۔",
    [poly(PARALLELOGRAM, fill=True), dot(C)])
F_N = fig(100, 64,
    "The capital letter N drawn with straight strokes, with a dot at its middle.",
    "سیدھی لکیروں سے بنا بڑا انگریزی حرف N، بیچ میں ایک نقطہ ہے۔",
    letter_items("N", C, 1.0) + [dot(C)])

lesson = practice_lesson(
 "9.3", script="exercise_9_3.py",
 title=T("Exercise 9.3 practice: symmetry", "مشق 9.3 کی پریکٹس: تشاکل"),
 outcome="Find the lines of symmetry of shapes and letters, complete a shape across a mirror line on a grid, give the order of rotational symmetry and turn a point about a centre.",
 prerequisites=[SY_SHAPES, SY_LINE_SYMMETRY, SY_ROTATIONAL],
 misconceptions=[
   {"id": "counts_double", "description": "Counts each line of symmetry twice, or counts both halves of the fold."},
   {"id": "no_line_no_symmetry", "description": "Thinks a shape with no line of symmetry has no symmetry at all and forgets rotational symmetry."},
   {"id": "mirror_distance", "description": "Gives the distance between a point and its image as the distance to the mirror line, or the other way round."},
   {"id": "only_original", "description": "Counts only the original shape and forgets its mirror image."},
   {"id": "turn_direction", "description": "Turns the wrong way (clockwise and anticlockwise swapped) or moves the point to the wrong side of the centre."},
   {"id": "swaps_distances", "description": "After a turn, keeps the sideways and up-down distances in the wrong places."},
   {"id": "parallelogram_lines", "description": "Gives a parallelogram 2 lines of symmetry, like a rectangle."},
   {"id": "order_for_angle", "description": "Gives the order of rotational symmetry when the smallest angle of turn is asked, or the other way round."},
 ],
 steps=[
   practice_intro("9.3",
     "Here you find lines of symmetry, complete shapes across a mirror line, give the order of rotational symmetry, and turn points about a centre.",
     "اس میں آپ تشاکل کی لکیریں ڈھونڈیں گے، آئینہ لکیر کے پار شکلیں مکمل کریں گے، گردشی تشاکل کا درجہ بتائیں گے، اور ایک مرکز کے گرد نقطے گھمائیں گے۔",
     "Exercise 9.3 is about symmetry. Ready?", "مشق 9.3 تشاکل کے بارے میں ہے۔ تیار؟"),
   ch("q1_fold", ("When does a shape have a line of symmetry?", "کسی شکل میں تشاکل کی لکیر کب ہوتی ہے؟"),
      ("When folding along the line makes the two halves match exactly.", "جب لکیر پر تہہ کرنے سے دونوں حصے بالکل ایک دوسرے پر آ جائیں۔", "Yes! The line works like a mirror.", "جی ہاں! لکیر آئینے کی طرح کام کرتی ہے۔"),
      [("When the line cuts the shape into two pieces.", "جب لکیر شکل کو دو ٹکڑوں میں کاٹ دے۔", "Any line can cut a shape in two. The halves must match.", "کوئی بھی لکیر شکل کو دو ٹکڑوں میں کاٹ سکتی ہے۔ دونوں حصے برابر ہونے چاہییں۔", "counts_double"),
       ("When the shape looks the same after it is turned.", "جب شکل گھمانے کے بعد ویسی ہی لگے۔", "That is rotational symmetry. A line of symmetry is about folding.", "یہ گردشی تشاکل ہے۔ تشاکل کی لکیر تہہ کرنے کے بارے میں ہے۔", "no_line_no_symmetry"),
       ("When the line goes from corner to corner.", "جب لکیر کونے سے کونے تک جائے۔", "A corner-to-corner line is a diagonal. It is a line of symmetry only for some shapes, such as a square.", "کونے سے کونے کی لکیر وتر ہے۔ وہ صرف کچھ شکلوں، جیسے مربع، کی تشاکل کی لکیر ہوتی ہے۔", "parallelogram_lines")],
      0, qtype="recall"),
   with_fig(nq("q2_pentagon", ("How many lines of symmetry does the regular pentagon in the picture have?", "تصویر والی باقاعدہ پانچ ضلعی شکل کی تشاکل کی کتنی لکیریں ہیں؟"), Q2,
      ("Each line goes from a corner to the middle of the opposite side.", "ہر لکیر ایک کونے سے سامنے والے ضلع کے درمیان تک جاتی ہے۔"),
      ("Right! One for each corner: 5 lines of symmetry.", "درست! ہر کونے کے لیے ایک: تشاکل کی 5 لکیریں۔"), ("A regular shape has as many lines as sides: 5.", "باقاعدہ شکل میں اضلاع کے برابر لکیریں ہوتی ہیں: 5"),
      [(10, "That counts each line twice, once from each end. There are 5.", "یہ ہر لکیر کو دو بار گنتا ہے، ہر سرے سے ایک بار۔ لکیریں 5 ہیں۔", "counts_double"),
       (1, "There is more than one fold. A regular pentagon has 5.", "ایک سے زیادہ تہیں ہیں۔ باقاعدہ پانچ ضلعی شکل کی 5 ہیں۔", "counts_double")], qtype="recall"), F_PENT),
   with_fig(nq("q3_letters", ("How many of the five letters in the picture have no line of symmetry?", "تصویر کے پانچ حروف میں سے کتنے حروف میں تشاکل کی کوئی لکیر نہیں؟"), Q3,
      ("Try folding each letter. Which ones never match?", "ہر حرف کو تہہ کر کے دیکھیں۔ کون سے کبھی نہیں ملتے؟"),
      ("Right! N and F have no line of symmetry. A and E have 1 and H has 2.", "درست! N اور F میں تشاکل کی کوئی لکیر نہیں۔ A اور E میں 1 اور H میں 2 ہیں۔"), ("A, E and H can be folded to match; N and F cannot: 2.", "A، E اور H تہہ کرنے سے مل جاتے ہیں؛ N اور F نہیں: 2"),
      [(1, "Only one? Check N and F: neither folds to match, so 2.", "صرف ایک؟ N اور F دیکھیں: دونوں تہہ کرنے سے نہیں ملتے، تو 2", "counts_double"),
       (3, "A, E and H do fold to match. Only N and F do not: 2.", "A، E اور H تہہ کرنے سے ملتے ہیں۔ صرف N اور F نہیں ملتے: 2", "counts_double")], qtype="recall"), F_LETTERS),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "A reflection is a flip. A rotation is a turn about a centre.", "عکس پلٹنا ہے۔ گردش مرکز کے گرد گھومنا ہے۔"),
    "text": T("Reflection: a point and its image are the same distance from the mirror line, on opposite sides. The distance between them is twice the distance to the mirror. Rotational symmetry: a shape fits onto itself when turned about its centre by less than a full turn. The order is how many times it fits in one full turn (360°), and the smallest turn is 360° ÷ order. A quarter turn is 90° and a half turn is 180°. Clockwise is the way a clock's hands go. A shape can have rotational symmetry and no line of symmetry, like a parallelogram.",
              "عکس: نقطہ اور اس کا عکس آئینہ لکیر سے ایک جتنے فاصلے پر، مخالف رخوں پر ہوتے ہیں۔ ان کے درمیان فاصلہ آئینہ لکیر تک فاصلے کا دگنا ہوتا ہے۔ گردشی تشاکل: شکل اپنے مرکز کے گرد پورے چکر سے کم گھمانے پر اپنے اوپر بیٹھ جاتی ہے۔ درجہ یہ ہے کہ ایک پورے چکر (360°) میں وہ کتنی بار بیٹھتی ہے، اور سب سے چھوٹا چکر 360° ÷ درجہ ہوتا ہے۔ چوتھائی چکر 90° اور آدھا چکر 180° ہے۔ گھڑی کی سوئیوں کی سمت گھڑی کی سوئیاں چلتی ہیں۔ شکل میں گردشی تشاکل ہو سکتا ہے مگر تشاکل کی لکیر نہیں، جیسے متوازی الاضلاع۔")},
   with_fig(nq("q4_mirror_distance", ("The triangle is reflected in the mirror line. Corner Q is 5 squares from the mirror line. How many squares from the mirror line is Q's image, on the other side?", "مثلث کا آئینہ لکیر میں عکس لیا جاتا ہے۔ کونا Q آئینہ لکیر سے 5 خانے دور ہے۔ دوسری طرف Q کا عکس آئینہ لکیر سے کتنے خانے دور ہے؟"), Q4,
      ("A point and its image are the same distance from the mirror.", "نقطہ اور اس کا عکس آئینہ لکیر سے برابر فاصلے پر ہوتے ہیں۔"),
      ("Right! The image is also 5 squares from the mirror line.", "درست! عکس بھی آئینہ لکیر سے 5 خانے دور ہے۔"), ("Same distance, other side: 5.", "برابر فاصلہ، دوسری طرف: 5"),
      [(10, "10 is the distance between Q and its image. The question asks the distance from the mirror: 5.", "10، Q اور اس کے عکس کے درمیان فاصلہ ہے۔ سوال آئینہ لکیر سے فاصلہ پوچھتا ہے: 5", "mirror_distance"),
       (6, "6 is the column of the mirror line. The image is 5 squares from it.", "6 آئینہ لکیر کا کالم ہے۔ عکس اس سے 5 خانے دور ہے۔", "mirror_distance")]), F_TRI_MIRROR),
   with_fig(nq("q5_between", ("Point R is 2 squares above the mirror line. R' is its reflection. How many squares apart are R and R'?", "نقطہ R آئینہ لکیر سے 2 خانے اوپر ہے۔ R' اس کا عکس ہے۔ R اور R' کے درمیان کتنے خانوں کا فاصلہ ہے؟"), Q5,
      ("R' is 2 squares below the mirror line. Add the two distances.", "R' آئینہ لکیر سے 2 خانے نیچے ہے۔ دونوں فاصلے جمع کریں۔"),
      ("Right! 2 + 2 = 4 squares.", "درست! 2 + 2 = 4 خانے"), ("2 above the line and 2 below: 4 apart.", "لکیر سے 2 اوپر اور 2 نیچے: درمیان 4"),
      [(2, "2 is the distance to the mirror only. R' is on the other side too: 4.", "2 صرف آئینہ لکیر تک فاصلہ ہے۔ R' دوسری طرف بھی ہے: 4", "mirror_distance"),
       (3, "3 is the row of the mirror line. Add the two distances, 2 + 2: 4.", "3 آئینہ لکیر کی صف ہے۔ دونوں فاصلے جمع کریں، 2 + 2: 4", "mirror_distance")]), F_HMIRROR),
   with_fig(nq("q6_complete", ("The shaded staircase is reflected in the mirror line to complete the shape. How many squares are shaded in the whole picture?", "سیڑھی کے رنگے ہوئے خانوں کا آئینہ لکیر میں عکس لے کر شکل مکمل کی جاتی ہے۔ پوری تصویر میں کتنے خانے رنگے ہوں گے؟"), Q6,
      ("The image has the same number of squares. Count the original first.", "عکس میں خانوں کی تعداد وہی ہوتی ہے۔ پہلے اصل کو گنیں۔"),
      ("Right! 6 + 6 = 12 squares.", "درست! 6 + 6 = 12 خانے"), ("The staircase has 1 + 2 + 3 = 6 squares, and so does its image: 12.", "سیڑھی میں 1 + 2 + 3 = 6 خانے ہیں، اور اس کے عکس میں بھی: 12"),
      [(6, "That counts only the original. The mirror image has 6 more: 12.", "یہ صرف اصل کو گنتا ہے۔ آئینے کے عکس میں 6 اور ہیں: 12", "only_original")]), F_STAIRS),
   with_fig(nq("q7_order", ("How many times does the pinwheel fit onto itself in one full turn about its centre dot (the order of rotational symmetry)?", "پھرکی اپنے مرکز کے نقطے کے گرد ایک پورے چکر میں کتنی بار اپنے اوپر بیٹھتی ہے (گردشی تشاکل کا درجہ)؟"), Q7,
      ("Turn it a quarter at a time and see when it looks the same.", "اسے چوتھائی چوتھائی گھمائیں اور دیکھیں کب ویسی ہی لگتی ہے۔"),
      ("Right! It looks the same after every quarter turn: order 4.", "درست! ہر چوتھائی چکر کے بعد ویسی ہی لگتی ہے: درجہ 4"), ("4 blades, 4 matching positions: 4.", "4 پر، 4 ملتی جلتی حالتیں: 4"),
      [(0, "A pinwheel has no line of symmetry, but it does fit when turned: order 4.", "پھرکی میں تشاکل کی لکیر نہیں، لیکن گھمانے پر وہ بیٹھتی ہے: درجہ 4", "no_line_no_symmetry"),
       (90, "90° is the smallest turn. The order is how many fit in 360°: 4.", "90° سب سے چھوٹا چکر ہے۔ درجہ یہ ہے کہ 360° میں کتنے آتے ہیں: 4", "order_for_angle")]), F_PIN),
   with_fig(nq("q8_angle", ("A regular octagon has rotational symmetry of order 8. What is the smallest angle, in degrees, that it can be turned through to fit onto itself?", "باقاعدہ آٹھ ضلعی شکل کا گردشی تشاکل کا درجہ 8 ہے۔ اسے کم از کم کتنے ڈگری گھمانے سے وہ اپنے اوپر بیٹھ جاتی ہے؟"), Q8,
      ("Smallest turn = 360° ÷ order.", "سب سے چھوٹا چکر = 360° ÷ درجہ"),
      ("Right! 360° ÷ 8 = 45°.", "درست! 360° ÷ 8 = 45°"), ("360 ÷ 8 = 45.", "360 ÷ 8 = 45"),
      [(8, "8 is the order. The angle is 360° ÷ 8 = 45°.", "8 درجہ ہے۔ زاویہ 360° ÷ 8 = 45° ہے۔", "order_for_angle"),
       (90, "90° would fit a square. Divide 360° by 8: 45°.", "90° مربع کے لیے ہوتا۔ 360° کو 8 سے تقسیم کریں: 45°", "order_for_angle")]), F_OCT),
   with_fig(ch("q9_quarter", ("Point A is turned a quarter turn (90°) clockwise about O. Where does it land?", "نقطہ A کو O کے گرد چوتھائی چکر (90°) گھڑی کی سوئیوں کی سمت میں گھمایا جاتا ہے۔ وہ کہاں پہنچتا ہے؟"),
      ("3 squares below O", "O سے 3 خانے نیچے", "Yes! Like the hand of a clock going from 3 o'clock to 6 o'clock.", "جی ہاں! جیسے گھڑی کی سوئی 3 بجے سے 6 بجے کی طرف جاتی ہے۔"),
      [("3 squares above O", "O سے 3 خانے اوپر", "That is a quarter turn anticlockwise.", "یہ گھڑی کی سوئیوں کی مخالف سمت میں چوتھائی چکر ہے۔", "turn_direction"),
       ("3 squares to the left of O", "O سے 3 خانے بائیں", "That is a half turn, 180°.", "یہ آدھا چکر، 180°، ہے۔", "turn_direction"),
       ("Where it is now, 3 squares to the right of O", "جہاں ہے وہیں، O سے 3 خانے دائیں", "A quarter turn moves it.", "چوتھائی چکر اسے ہلاتا ہے۔", "turn_direction")],
      0), F_TURN9),
   with_fig(nq("q10_half_turn", ("Point A is 3 squares right of O and 2 squares above it. After a half turn (180°) about O, how many squares to the left of O is its image?", "نقطہ A، O سے 3 خانے دائیں اور 2 خانے اوپر ہے۔ O کے گرد آدھے چکر (180°) کے بعد اس کا عکس O سے کتنے خانے بائیں ہے؟"), Q10,
      ("A half turn sends a point to the opposite side of O, the same distances away.", "آدھا چکر نقطے کو O کی مخالف طرف، اتنے ہی فاصلوں پر بھیجتا ہے۔"),
      ("Right! The image is 3 squares left of O and 2 squares below it.", "درست! عکس O سے 3 خانے بائیں اور 2 خانے نیچے ہے۔"), ("3 right becomes 3 left, 2 up becomes 2 down.", "3 دائیں، 3 بائیں بن جاتے ہیں، 2 اوپر، 2 نیچے بن جاتے ہیں۔"),
      [(2, "2 is the up-down distance. The sideways distance stays 3: 3 squares left.", "2 اوپر نیچے کا فاصلہ ہے۔ دائیں بائیں کا فاصلہ 3 ہی رہتا ہے: 3 خانے بائیں", "swaps_distances"),
       (6, "6 is the distance between A and its image, side to side. From O it is 3.", "6، A اور اس کے عکس کے درمیان دائیں بائیں کا فاصلہ ہے۔ O سے وہ 3 ہے۔", "mirror_distance")]), F_TURN10),
   with_fig(ch("q11_find_error", ("Zara says a parallelogram has 2 lines of symmetry, like a rectangle. What went wrong?", "زارا کہتی ہے متوازی الاضلاع کی تشاکل کی 2 لکیریں ہیں، مستطیل کی طرح۔ کیا غلطی ہوئی؟"),
      ("A parallelogram has no line of symmetry. It only has rotational symmetry of order 2.", "متوازی الاضلاع کی تشاکل کی کوئی لکیر نہیں۔ اس میں صرف درجہ 2 کا گردشی تشاکل ہے۔", "Yes! Folding it never matches the halves, but a half turn fits it onto itself.", "جی ہاں! تہہ کرنے سے حصے کبھی نہیں ملتے، لیکن آدھا چکر اسے اپنے اوپر بٹھا دیتا ہے۔"),
      [("Nothing. A parallelogram has 2 lines of symmetry.", "کوئی غلطی نہیں۔ متوازی الاضلاع کی تشاکل کی 2 لکیریں ہیں۔", "Fold it along a diagonal or through the middle: the halves do not match.", "اسے وتر پر یا درمیان سے تہہ کریں: حصے نہیں ملتے۔", "parallelogram_lines"),
       ("A parallelogram has 4 lines of symmetry.", "متوازی الاضلاع کی تشاکل کی 4 لکیریں ہیں۔", "Only a square has 4. A parallelogram has none.", "صرف مربع کی 4 ہوتی ہیں۔ متوازی الاضلاع کی کوئی نہیں۔", "parallelogram_lines")],
      0, qtype="find_error"), F_PARA),
   with_fig(ch("q12_find_error_n", ("Ali says the letter N has no symmetry at all, because no fold makes it match. What went wrong?", "علی کہتا ہے حرف N میں کوئی تشاکل ہے ہی نہیں، کیونکہ کوئی تہہ اسے ملاتی نہیں۔ کیا غلطی ہوئی؟"),
      ("N has no line of symmetry, but a half turn fits it onto itself: rotational symmetry of order 2.", "N میں تشاکل کی لکیر نہیں، مگر آدھا چکر اسے اپنے اوپر بٹھا دیتا ہے: درجہ 2 کا گردشی تشاکل۔", "Yes! Symmetry can be turning as well as folding.", "جی ہاں! تشاکل گھمانے سے بھی ہو سکتا ہے، تہہ کرنے سے ہی نہیں۔"),
      [("Nothing. A shape without a line of symmetry has no symmetry.", "کوئی غلطی نہیں۔ جس شکل میں تشاکل کی لکیر نہ ہو اس میں تشاکل نہیں ہوتا۔", "Turn N upside down: it looks the same. That is symmetry.", "N کو الٹا کریں: وہ ویسا ہی لگتا ہے۔ یہ تشاکل ہے۔", "no_line_no_symmetry"),
       ("N has 2 lines of symmetry, like H.", "N کی تشاکل کی 2 لکیریں ہیں، H کی طرح۔", "Folding N never matches the halves.", "N کو تہہ کرنے سے حصے کبھی نہیں ملتے۔", "counts_double")],
      1, qtype="find_error"), F_N),
   nq("q13_fan", ("A ceiling fan has 3 identical blades, equally spaced. What is the smallest angle, in degrees, it can turn through so that it looks the same?", "چھت کے پنکھے کے 3 ایک جیسے پر ہیں، برابر فاصلے پر۔ وہ کم از کم کتنے ڈگری گھومے تو ویسا ہی لگے؟"), Q13,
      ("The order is 3. Smallest turn = 360° ÷ 3.", "درجہ 3 ہے۔ سب سے چھوٹا چکر = 360° ÷ 3"),
      ("Right! 360° ÷ 3 = 120°.", "درست! 360° ÷ 3 = 120°"), ("Three equal turns make 360°: 120° each.", "تین برابر چکر مل کر 360° بناتے ہیں: ہر ایک 120°"),
      [(3, "3 is the order. The angle is 360° ÷ 3 = 120°.", "3 درجہ ہے۔ زاویہ 360° ÷ 3 = 120° ہے۔", "order_for_angle"),
       (60, "60° would be for 6 blades. 360° ÷ 3 = 120°.", "60° 6 پروں کے لیے ہوتا۔ 360° ÷ 3 = 120°", "order_for_angle")]),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can find both kinds of symmetry.", "شاباش! آپ دونوں قسم کے تشاکل ڈھونڈ سکتے ہیں۔"),
    "text": T("A line of symmetry folds a shape so the halves match; a regular shape has as many lines as sides. A point and its image are the same distance from the mirror, on opposite sides. Rotational symmetry: the order is how many times a shape fits onto itself in one full turn, and the smallest turn is 360° ÷ order. A shape can have rotational symmetry without a line of symmetry.",
              "تشاکل کی لکیر شکل کو یوں تہہ کرتی ہے کہ حصے مل جائیں؛ باقاعدہ شکل میں اضلاع کے برابر لکیریں ہوتی ہیں۔ نقطہ اور اس کا عکس آئینہ لکیر سے برابر فاصلے پر، مخالف رخوں پر ہوتے ہیں۔ گردشی تشاکل: درجہ یہ ہے کہ ایک پورے چکر میں شکل کتنی بار اپنے اوپر بیٹھتی ہے، اور سب سے چھوٹا چکر 360° ÷ درجہ ہے۔ شکل میں تشاکل کی لکیر کے بغیر بھی گردشی تشاکل ہو سکتا ہے۔"),
    "points": [T("Image: same distance from the mirror, other side.", "عکس: آئینہ لکیر سے برابر فاصلہ، دوسری طرف۔"),
               T("Smallest turn = 360° ÷ order.", "سب سے چھوٹا چکر = 360° ÷ درجہ")]},
 ],
 bank=[
   {"id": "qb_triangle_lines", "type": "recall", "step": nq("qb_triangle_lines", ("How many lines of symmetry does an equilateral triangle have?", "مساوی الاضلاع مثلث کی تشاکل کی کتنی لکیریں ہیں؟"), QB1,
      ("One from each corner.", "ہر کونے سے ایک۔"),
      ("Right! 3 lines of symmetry.", "درست! تشاکل کی 3 لکیریں۔"), ("3 corners, 3 lines.", "3 کونے، 3 لکیریں۔"),
      [(1, "That is an isosceles triangle. An equilateral triangle has 3.", "یہ مساوی الساقین مثلث ہے۔ مساوی الاضلاع مثلث کی 3 ہیں۔", "counts_double")], qtype=None)},
   {"id": "qb_hexagon_order", "type": "recall", "step": nq("qb_hexagon_order", ("What is the order of rotational symmetry of a regular hexagon?", "باقاعدہ مسدس کے گردشی تشاکل کا درجہ کیا ہے؟"), QB2,
      ("A regular shape has an order equal to its number of sides.", "باقاعدہ شکل کا درجہ اس کے اضلاع کی تعداد کے برابر ہوتا ہے۔"),
      ("Right! Order 6.", "درست! درجہ 6"), ("6 sides, order 6.", "6 اضلاع، درجہ 6"),
      [(60, "60° is the smallest turn. The order is 6.", "60° سب سے چھوٹا چکر ہے۔ درجہ 6 ہے۔", "order_for_angle")], qtype=None)},
   {"id": "qb_five", "type": "apply", "step": nq("qb_five", ("A shape has rotational symmetry of order 5. What is the smallest angle, in degrees, it can be turned through to fit onto itself?", "ایک شکل کے گردشی تشاکل کا درجہ 5 ہے۔ اسے کم از کم کتنے ڈگری گھمانے سے وہ اپنے اوپر بیٹھتی ہے؟"), QB3,
      ("360° ÷ 5.", "360° ÷ 5"),
      ("Right! 360° ÷ 5 = 72°.", "درست! 360° ÷ 5 = 72°"), ("360 ÷ 5 = 72.", "360 ÷ 5 = 72"),
      [(5, "5 is the order. The angle is 360° ÷ 5 = 72°.", "5 درجہ ہے۔ زاویہ 360° ÷ 5 = 72° ہے۔", "order_for_angle")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error", ("Hina says a regular hexagon has rotational symmetry of order 60. What went wrong?", "حنا کہتی ہے باقاعدہ مسدس کے گردشی تشاکل کا درجہ 60 ہے۔ کیا غلطی ہوئی؟"),
      ("60° is the smallest turn. The order is how many times it fits in a full turn: 360° ÷ 60° = 6.", "60° سب سے چھوٹا چکر ہے۔ درجہ یہ ہے کہ پورے چکر میں کتنی بار بیٹھتا ہے: 360° ÷ 60° = 6", "Yes! The order is 6.", "جی ہاں! درجہ 6 ہے۔"),
      [("Nothing. The order is 60.", "کوئی غلطی نہیں۔ درجہ 60 ہے۔", "60 is the angle in degrees, not the order.", "60 ڈگری میں زاویہ ہے، درجہ نہیں۔", "order_for_angle"),
       ("The order is 360.", "درجہ 360 ہے۔", "360° is a full turn. The order is how many fits it has: 6.", "360° پورا چکر ہے۔ درجہ یہ ہے کہ کتنی بار بیٹھتا ہے: 6", "order_for_angle")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_h_lines", "type": "recall", "step": nq("r_h_lines", ("How many lines of symmetry does the capital letter H have?", "بڑے انگریزی حرف H کی تشاکل کی کتنی لکیریں ہیں؟"), R1,
      ("One up-down and one across.", "ایک اوپر نیچے اور ایک آر پار۔"),
      ("Right! 2 lines of symmetry.", "درست! تشاکل کی 2 لکیریں۔"), ("Fold H down the middle, and across the middle: 2.", "H کو بیچ سے اوپر نیچے اور بیچ سے آر پار تہہ کریں: 2"),
      [(1, "H folds both ways: 2.", "H دونوں طرح تہہ ہوتا ہے: 2", "counts_double")], qtype=None)},
   {"id": "r_hexagon_turn", "type": "apply", "step": nq("r_hexagon_turn", ("What is the smallest angle, in degrees, a regular hexagon can be turned through to fit onto itself?", "باقاعدہ مسدس کو کم از کم کتنے ڈگری گھمانے سے وہ اپنے اوپر بیٹھتا ہے؟"), R2,
      ("360° ÷ 6.", "360° ÷ 6"),
      ("Right! 360° ÷ 6 = 60°.", "درست! 360° ÷ 6 = 60°"), ("360 ÷ 6 = 60.", "360 ÷ 6 = 60"),
      [(6, "6 is the order. The angle is 360° ÷ 6 = 60°.", "6 درجہ ہے۔ زاویہ 360° ÷ 6 = 60° ہے۔", "order_for_angle")], qtype=None)},
 ],
 glossary=[T("Line of symmetry", "تشاکل کی لکیر"), T("Mirror line", "آئینہ لکیر"), T("Reflection", "عکس"),
           T("Rotational symmetry", "گردشی تشاکل"), T("Order of rotational symmetry", "گردشی تشاکل کا درجہ"), T("Centre of rotation", "مرکزِ گردش"),
           T("Clockwise", "گھڑی کی سوئیوں کی سمت"), T("Half turn", "آدھا چکر")],
 flashcards=[
   {"id": "f_turn", "front": T("How do you find the smallest turn from the order?", "درجے سے سب سے چھوٹا چکر کیسے نکالتے ہیں؟"),
    "back": T("Divide 360° by the order. Order 4 gives 90°.", "360° کو درجے سے تقسیم کریں۔ درجہ 4 سے 90° ملتا ہے۔")},
   {"id": "f_mirror", "front": T("Where is the image of a point in a mirror line?", "آئینہ لکیر میں نقطے کا عکس کہاں ہوتا ہے؟"),
    "back": T("The same distance from the mirror line, on the other side.", "آئینہ لکیر سے برابر فاصلے پر، دوسری طرف۔")},
 ],
 home_task={"id": "h_symmetry", "text": T(
   "Cut out a paper pinwheel, a square and a rectangle. Fold each to find its lines of symmetry. Then turn each about its centre to find its order of rotational symmetry, and write down both numbers.",
   "کاغذ کی ایک پھرکی، ایک مربع اور ایک مستطیل کاٹیں۔ ہر ایک کو تہہ کر کے تشاکل کی لکیریں ڈھونڈیں۔ پھر ہر ایک کو اس کے مرکز کے گرد گھما کر گردشی تشاکل کا درجہ ڈھونڈیں، اور دونوں عدد لکھیں۔")},
 notes=["Covers lines of symmetry of a regular shape and of letters (q1 to q3, q11), reflecting a point and a shape on a grid (q4 to q6), the order of rotational symmetry and the smallest turn (q7, q8, q13), turning a point about a centre on a grid (q9, q10) and a letter with only rotational symmetry (q12).",
        "Each wrong answer is a real mistake: each line counted twice, rotational symmetry forgotten when there is no line, the distance to the mirror mixed with the distance between point and image, the mirror image forgotten, the turn the wrong way, and the order mixed with the angle.",
        "Counts and orders were checked in figs.py by really flipping and turning the drawn shapes. Urdu terms to check: تشاکل کی لکیر, آئینہ لکیر, عکس, گردشی تشاکل, گردشی تشاکل کا درجہ, آدھا چکر, گھڑی کی سوئیوں کی سمت, all as in the existing Symmetry lessons. پھرکی (pinwheel) is as in the rotational symmetry lesson; باقاعدہ پانچ ضلعی شکل and باقاعدہ آٹھ ضلعی شکل (regular pentagon, octagon) are new, so a teacher should confirm them."],
 minutes=20,
)

write(lesson)

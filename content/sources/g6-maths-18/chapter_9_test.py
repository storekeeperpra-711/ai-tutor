"""Chapter 9 test (Symmetry), set out like the book's review exercise and a
board paper: multiple choice, short questions, then longer problems. The
questions are new; only the kinds of question follow the book."""
from common import (T, say, nq, ch, write, book_ref, REVIEW, CHAPTER_9_TEST, CH9_PREREQS)
from figs import (fig, with_fig, label, dot, regular, order, lines, closed_pieces, letter_items, letter_symmetry,
                  transversal_figure, theta_for, corner_size, Grid, reflect_cells, C, FULL, LINE)

SKILL = CHAPTER_9_TEST


def mcq(id, en, ur, right, wrongs, pos):
    return ch(id, ("MCQ: " + en, "کثیر انتخابی: " + ur), right, wrongs, pos, qtype="exam_style")


def short(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Short question: " + en, "مختصر سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_q(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


# (faces, edges, vertices)
SOLIDS = {"cube": (6, 12, 8), "cylinder": (3, 2, 0), "cone": (2, 1, 1), "sphere": (1, 0, 0), "hemisphere": (2, 1, 0)}
# MCQs
assert [k for k, v in SOLIDS.items() if v[1:] == (0, 0)] == ["sphere"]
assert [k for k, v in SOLIDS.items() if v == (2, 1, 1)] == ["cone"]
M3_TH = theta_for("tr", 65)
M3 = corner_size(M3_TH, "tr")
assert M3 == 65 and LINE - 65 == 115 and 90 - 65 == 25 and 360 - 65 == 295
M3_FIG = transversal_figure(M3_TH, [("l", "tr", "65°"), ("m", "tr", "x")])
# a line perpendicular to one of two parallel lines is perpendicular to the other
M4 = corner_size(theta_for("tr", 90), "tr")
assert M4 == 90
RECT = [C + complex(-36, -18), C + complex(36, -18), C + complex(36, 18), C + complex(-36, 18)]
M5 = lines(closed_pieces(RECT), C)
assert M5 == 2 and order(closed_pieces(RECT), C) == 2
M6 = FULL // 6
assert M6 == 60 and 6 * 60 == FULL
# short questions
S1 = 4 * (10 + 7 + 5)
assert S1 == 88 and 10 + 7 + 5 == 22 and 10 * 7 * 5 == 350 and 12 * 10 == 120
S2 = (LINE - 60) // 3
assert S2 == 40 and 2 * S2 + S2 + 60 == LINE and 2 * S2 == 80 and S2 + 60 == 100
S2_TH = theta_for("bl", 2 * S2)
assert corner_size(S2_TH, "tl") == S2 + 60
S2_FIG = transversal_figure(S2_TH, [("l", "bl", "2x"), ("m", "tl", "x+60")])
S3_GRID = Grid(12, 4)
S3_P = (2, 2)
S3_MIRROR = 6
S3_IMG = reflect_cells([S3_P], "v", S3_MIRROR)[0]
S3 = S3_IMG[0] - S3_P[0]
assert S3_IMG == (10, 2) and S3 == 8 and S3_MIRROR - S3_P[0] == 4
S3_FIG = S3_GRID.figure(
    "A squared grid 12 squares wide and 4 tall. A dashed mirror line goes down the middle. Point P is 4 squares to the left of the mirror line.",
    "12 خانے چوڑا اور 4 خانے اونچا چوکور جال۔ بیچ میں اوپر سے نیچے ڈیش والی آئینہ لکیر ہے۔ نقطہ P آئینہ لکیر سے 4 خانے بائیں ہے۔",
    [S3_GRID.vmirror(S3_MIRROR), dot(S3_GRID.at(*S3_P)), label(S3_GRID.at(S3_P[0], S3_P[1] - 0.7), "P")])
S4 = FULL // 24
assert S4 == 15 and 15 * 24 == FULL and len(regular(15, C, 20)) == 15 and 360 // 15 == 24
# long questions
WORD = "MATH"
L1_LINES = {k: letter_symmetry(k)[0] for k in WORD}
assert L1_LINES == {"M": 1, "A": 1, "T": 1, "H": 2}
L1 = sum(L1_LINES.values())
assert L1 == 5 and 4 * 2 == 8
L1_ITEMS = []
for i, k in enumerate(WORD):
    L1_ITEMS += letter_items(k, complex(22 + 34 * i, 22))
L1_FIG = fig(144, 44,
    "The four capital letters M, A, T and H in a row, drawn with straight strokes. Each letter is taller than it is wide.",
    "چار بڑے انگریزی حروف M، A، T اور H ایک قطار میں، سیدھی لکیروں سے بنے ہوئے۔ ہر حرف چوڑائی سے زیادہ اونچا ہے۔",
    L1_ITEMS)
L2_X = (50 + 10) // 2
assert 3 * L2_X - 10 == L2_X + 50 and L2_X == 30
L2 = L2_X + 50
assert L2 == 80 and 3 * L2_X - 10 == 80 and LINE - L2 == 100
L2_TH = theta_for("br", L2)          # l bottom-right and m top-left are alternate angles
assert corner_size(L2_TH, "br") == L2 == corner_size(L2_TH, "tl")
L2_FIG = transversal_figure(L2_TH, [("l", "br", "3x−10"), ("m", "tl", "x+50")])
L3_EDGES = 12 * 9
L3 = L3_EDGES * 2
assert L3_EDGES == 108 and L3 == 216 and SOLIDS["cube"][1] == 12 and 9 * 9 * 9 == 729 and 8 * 9 == 72
L4_STEP = FULL // 5
L4 = 216 // L4_STEP
assert L4_STEP == 72 and L4 == 3 and 216 % L4_STEP == 0 and 216 // 5 == 43
# question bank and review
QB1 = SOLIDS["cube"][0]
assert QB1 == 6
QB2 = 180 - 115
assert QB2 == 65
QB3 = lines(closed_pieces(regular(4, C, 26, start=-45)), C)
assert QB3 == 4
R1 = SOLIDS["cylinder"][1]
assert R1 == 2
R2 = order(closed_pieces(regular(5, C, 26)), C)
assert R2 == 5

lesson = {
 "id": "g6-maths-18-chapter-9-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 9: 2-D and 3-D shapes and their faces, edges and vertices, parallel, intersecting and perpendicular lines, the angles a transversal makes, and reflective and rotational symmetry.",
                      "textbook": book_ref("Review Exercise 9")}],
 "skills": [SKILL],
 "title": T("Chapter 9 test: Symmetry", "باب 9 کا ٹیسٹ: تشاکل"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in CH9_PREREQS],
 "misconceptions": [
   {"id": "solid_parts_mix", "description": "Mixes up faces, edges and vertices of a solid, or does not count a curved surface as a face."},
   {"id": "edges_miscount", "description": "Counts too few edges, such as only the visible ones, or only one of each length."},
   {"id": "angle_rule_mix", "description": "Uses 180° minus the angle where the angles are equal, or equal where they add to 180°."},
   {"id": "lines_counted_wrong", "description": "Gives a rectangle 4 lines of symmetry (its diagonals), or counts each line twice."},
   {"id": "order_for_angle", "description": "Mixes up the order of rotational symmetry and the smallest angle of turn."},
   {"id": "mirror_distance", "description": "Gives the distance to the mirror line when the distance between the point and its image is asked."},
   {"id": "half_not_found", "description": "Sets up or solves the equation from the angle rule wrongly, or gives x when the angle is asked."},
   {"id": "answer_is_other_quantity", "description": "Stops at a middle step, such as the length of ribbon, and gives it as the answer."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_cube_faces", "type": "exam_style", "step": nq(
     "qb_exam_cube_faces", ("How many faces does a cube have?", "مکعب کی کتنی سطحیں ہیں؟"), QB1,
     ("Top, bottom, front, back, left, right.", "اوپر، نیچے، سامنے، پیچھے، بائیں، دائیں۔"),
     ("Correct: 6 faces.", "درست: 6 سطحیں"), ("2 + 2 + 2 = 6.", "2 + 2 + 2 = 6"),
     [(12, "12 is the number of edges. Faces: 6.", "12 کناروں کی تعداد ہے۔ سطحیں: 6", "solid_parts_mix")], qtype=None)},
   {"id": "qb_exam_cointerior", "type": "exam_style", "step": nq(
     "qb_exam_cointerior", ("Parallel lines are cut by a transversal. One co-interior angle is 115°. Find the other, in degrees.", "متوازی لکیریں ایک قاطع سے کٹتی ہیں۔ ایک ہم اندرونی زاویہ 115° ہے۔ دوسرا ڈگری میں نکالیں۔"), QB2,
     ("Co-interior angles add up to 180°.", "ہم اندرونی زاویوں کا مجموعہ 180° ہوتا ہے۔"),
     ("Correct: 180° − 115° = 65°.", "درست: 180° − 115° = 65°"), ("115 + x = 180, so x = 65.", "115 + x = 180، تو x = 65"),
     [(115, "That makes them equal. They add up to 180°: 65°.", "یہ انہیں برابر بناتا ہے۔ ان کا مجموعہ 180° ہے: 65°", "angle_rule_mix")], qtype=None)},
   {"id": "qb_exam_square_lines", "type": "exam_style", "step": nq(
     "qb_exam_square_lines", ("How many lines of symmetry does a square have?", "مربع کی تشاکل کی کتنی لکیریں ہیں؟"), QB3,
     ("Two through the middles of the sides and two diagonals.", "دو اضلاع کے درمیان سے اور دو وتر۔"),
     ("Correct: 4 lines of symmetry.", "درست: تشاکل کی 4 لکیریں"), ("2 across and down, 2 diagonals: 4.", "2 آر پار اور اوپر نیچے، 2 وتر: 4"),
     [(2, "A square folds along its diagonals too: 4.", "مربع وتر پر بھی تہہ ہوتا ہے: 4", "lines_counted_wrong")], qtype=None)},
 ]},
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 9 in your maths book in your notebook, setting out the working the way this test's answers do: write the rule you use, put in the numbers, work out the answer with its unit or degrees. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 9 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں: جو اصول استعمال کریں وہ لکھیں، اعداد رکھیں، اور جواب اکائی یا ڈگری کے ساتھ نکالیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Model answer", "نمونہ جواب"), T("Review exercise", "اعادی مشق")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 9 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook, then the final answer). The questions are new, not the book's. Write the unit with every answer in your notebook: degrees, cm or rupees.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 9 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوالات (کاپی میں پورا کام، پھر آخری جواب)۔ سوال نئے ہیں، کتاب کے نہیں۔ اپنی کاپی میں ہر جواب کے ساتھ اکائی لکھیں: ڈگری، سینٹی میٹر یا روپے۔")},
   mcq("m1_no_edges", "Which solid has no edge and no vertex?", "کس ٹھوس شکل کا نہ کوئی کنارہ ہے نہ کوئی راس؟",
       ("Sphere", "کرہ", "Correct: a sphere is one smooth curved surface.", "درست: کرہ ایک ہموار خمدار سطح ہے۔"),
       [("Cone", "مخروط", "A cone has 1 edge and 1 vertex.", "مخروط کا 1 کنارہ اور 1 راس ہے۔", "solid_parts_mix"),
        ("Cylinder", "اسطوانہ", "A cylinder has 2 edges.", "اسطوانے کے 2 کنارے ہیں۔", "solid_parts_mix"),
        ("Hemisphere", "نصف کرہ", "A hemisphere has 1 edge, where the flat circle meets the curved surface.", "نصف کرہ کا 1 کنارہ ہے، جہاں چپٹا دائرہ خمدار سطح سے ملتا ہے۔", "solid_parts_mix")], 1),
   mcq("m2_cone", "A cone has:", "مخروط میں ہوتے ہیں:",
       ("2 faces, 1 edge, 1 vertex", "2 سطحیں، 1 کنارہ، 1 راس", "Correct: a flat base, a curved side, the rim of the base, and the tip.", "درست: چپٹا قاعدہ، خمدار پہلو، قاعدے کا گھیرا، اور نوک۔"),
       [("3 faces, 2 edges, 0 vertices", "3 سطحیں، 2 کنارے، 0 راس", "That is a cylinder.", "یہ اسطوانہ ہے۔", "solid_parts_mix"),
        ("1 face, 0 edges, 0 vertices", "1 سطح، 0 کنارے، 0 راس", "That is a sphere.", "یہ کرہ ہے۔", "solid_parts_mix"),
        ("2 faces, 1 edge, 0 vertices", "2 سطحیں، 1 کنارہ، 0 راس", "That is a hemisphere. A cone has a tip, a vertex.", "یہ نصف کرہ ہے۔ مخروط کی نوک ہے، یعنی راس۔", "solid_parts_mix")], 0),
   with_fig(mcq("m3_corresponding", "Lines l and m are parallel. The angle on l is 65° and x is its corresponding angle on m. Then x is:", "لکیریں l اور m متوازی ہیں۔ l پر زاویہ 65° ہے اور x، m پر اس کا متناظرہ زاویہ ہے۔ تو x ہے:",
       ("65°", "65°", "Correct: corresponding angles between parallel lines are equal.", "درست: متوازی لکیروں کے درمیان متناظرہ زاویے برابر ہوتے ہیں۔"),
       [("115°", "115°", "That is 180° − 65°. Corresponding angles are equal.", "یہ 180° − 65° ہے۔ متناظرہ زاویے برابر ہوتے ہیں۔", "angle_rule_mix"),
        ("25°", "25°", "That is 90° − 65°. The rule uses equal angles, not 90°.", "یہ 90° − 65° ہے۔ اصول برابر زاویوں کا ہے، 90° کا نہیں۔", "angle_rule_mix"),
        ("295°", "295°", "That is 360° − 65°. Corresponding angles are equal.", "یہ 360° − 65° ہے۔ متناظرہ زاویے برابر ہوتے ہیں۔", "angle_rule_mix")], 2), M3_FIG),
   mcq("m4_perp_parallel", "Lines l and m are parallel. A line p is perpendicular to l. Then p is:", "لکیریں l اور m متوازی ہیں۔ لکیر p، l پر عمودی ہے۔ تو p، m پر:",
       ("perpendicular to m too", "m پر بھی عمودی ہے", "Correct: corresponding angles are equal, so the 90° at l is 90° at m.", "درست: متناظرہ زاویے برابر ہیں، تو l پر 90° کا زاویہ m پر بھی 90° ہے۔"),
       [("parallel to m", "m کے متوازی ہے", "p crosses l, so it crosses m too. It cannot be parallel to m.", "p، l کو کاٹتی ہے، تو m کو بھی کاٹے گی۔ وہ m کے متوازی نہیں ہو سکتی۔", "angle_rule_mix"),
        ("at 45° to m", "m پر 45° پر ہے", "The angle at m equals the 90° at l.", "m پر زاویہ l کے 90° کے برابر ہے۔", "angle_rule_mix"),
        ("at 180° to m", "m پر 180° پر ہے", "180° is a straight line. The angle is 90°.", "180° سیدھی لکیر ہے۔ زاویہ 90° ہے۔", "angle_rule_mix")], 0),
   mcq("m5_rectangle", "A rectangle that is not a square has how many lines of symmetry?", "جو مستطیل مربع نہ ہو اس کی تشاکل کی کتنی لکیریں ہیں؟",
       ("2", "2", "Correct: one up-down and one across through the middle.", "درست: ایک اوپر نیچے اور ایک آر پار، بیچ سے۔"),
       [("4", "4", "The diagonals are not lines of symmetry for a rectangle.", "مستطیل کے لیے وتر تشاکل کی لکیریں نہیں ہوتے۔", "lines_counted_wrong"),
        ("1", "1", "It folds two ways, not one.", "یہ دو طرح تہہ ہوتی ہے، ایک نہیں۔", "lines_counted_wrong"),
        ("0", "0", "A rectangle does fold to match, two ways.", "مستطیل تہہ ہو کر مل جاتی ہے، دو طرح۔", "lines_counted_wrong")], 3),
   mcq("m6_order_angle", "A shape has rotational symmetry of order 6. The smallest angle it can be turned through to fit onto itself is:", "ایک شکل کے گردشی تشاکل کا درجہ 6 ہے۔ اسے کم از کم جتنا گھمانے سے وہ اپنے اوپر بیٹھتی ہے وہ زاویہ ہے:",
       ("60°", "60°", "Correct: 360° ÷ 6 = 60°.", "درست: 360° ÷ 6 = 60°"),
       [("6°", "6°", "6 is the order. The angle is 360° ÷ 6.", "6 درجہ ہے۔ زاویہ 360° ÷ 6 ہے۔", "order_for_angle"),
        ("30°", "30°", "30° would be for order 12.", "30° درجہ 12 کے لیے ہوتا۔", "order_for_angle"),
        ("90°", "90°", "90° would be for order 4.", "90° درجہ 4 کے لیے ہوتا۔", "order_for_angle")], 1),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   short("q1_frame", "A wire frame is made along all the edges of a cuboid that is 10 cm long, 7 cm wide and 5 cm high. Find the length of wire, in cm.", "ایک تار کا ڈھانچہ مکعب نما کے سب کناروں پر بنایا جاتا ہے جو 10 سینٹی میٹر لمبا، 7 سینٹی میٹر چوڑا اور 5 سینٹی میٹر اونچا ہے۔ تار کی لمبائی سینٹی میٹر میں نکالیں۔",
      S1, ("4 edges of each length: 4 × (10 + 7 + 5).", "ہر لمبائی کے 4 کنارے: 4 × (10 + 7 + 5)"),
      ("Correct: 4 × 22 = 88 cm.", "درست: 4 × 22 = 88 سینٹی میٹر"),
      ("Model answer: a cuboid has 4 edges of each length. Wire = 4 × (10 + 7 + 5) = 4 × 22 = 88 cm.", "نمونہ جواب: مکعب نما کے ہر لمبائی کے 4 کنارے ہوتے ہیں۔ تار = 4 × (10 + 7 + 5) = 4 × 22 = 88 سینٹی میٹر"),
      [(22, "That is one of each length. There are 4 of each: 88.", "یہ ہر لمبائی کا ایک ایک ہے۔ ہر ایک کے 4 ہیں: 88", "edges_miscount"),
       (350, "That is the volume, 10 × 7 × 5. Wire goes along the edges: 88.", "یہ حجم ہے، 10 × 7 × 5۔ تار کناروں پر لگتا ہے: 88", "edges_miscount")]),
   with_fig(short("q2_cointerior_x", "Lines l and m are parallel. Two co-interior angles are 2x° and (x + 60)°. Find x.", "لکیریں l اور m متوازی ہیں۔ دو ہم اندرونی زاویے 2x° اور (x + 60)° ہیں۔ x نکالیں۔",
      S2, ("2x + (x + 60) = 180.", "2x + (x + 60) = 180"),
      ("Correct: 3x + 60 = 180, 3x = 120, x = 40.", "درست: 3x + 60 = 180، 3x = 120، x = 40"),
      ("Model answer: co-interior angles add up to 180°, so 2x + x + 60 = 180, 3x = 120, x = 40. Check: 80° + 100° = 180°.", "نمونہ جواب: ہم اندرونی زاویوں کا مجموعہ 180° ہے، تو 2x + x + 60 = 180، 3x = 120، x = 40۔ جانچ: 80° + 100° = 180°"),
      [(80, "80 is the angle 2x. The question asks for x: 40.", "80 زاویہ 2x ہے۔ سوال x پوچھتا ہے: 40", "half_not_found"),
       (60, "That forgets the 2x. 3x = 180 − 60 = 120, so x = 40.", "یہ 2x بھول جاتا ہے۔ 3x = 180 − 60 = 120، تو x = 40", "half_not_found")]), S2_FIG),
   with_fig(short("q3_image", "Point P is 4 squares to the left of the vertical mirror line. How many squares apart are P and its image P'?", "نقطہ P عمودی آئینہ لکیر سے 4 خانے بائیں ہے۔ P اور اس کے عکس P' کے درمیان کتنے خانوں کا فاصلہ ہے؟",
      S3, ("P' is 4 squares on the other side. Add both distances.", "P' دوسری طرف 4 خانے پر ہے۔ دونوں فاصلے جمع کریں۔"),
      ("Correct: 4 + 4 = 8 squares.", "درست: 4 + 4 = 8 خانے"),
      ("Model answer: P' is also 4 squares from the mirror, on the other side. Distance PP' = 4 + 4 = 8 squares.", "نمونہ جواب: P' بھی آئینہ لکیر سے 4 خانے دور، دوسری طرف ہے۔ فاصلہ PP' = 4 + 4 = 8 خانے"),
      [(4, "4 is the distance to the mirror only. Add the other side: 8.", "4 صرف آئینہ لکیر تک فاصلہ ہے۔ دوسری طرف بھی جمع کریں: 8", "mirror_distance"),
       (12, "That adds 4 and 8. The mirror is 4 from P and P' is 4 from the mirror: 8.", "یہ 4 اور 8 جمع کرتا ہے۔ آئینہ لکیر P سے 4 اور P' آئینہ لکیر سے 4 پر ہے: 8", "mirror_distance")]), S3_FIG),
   short("q4_sides", "A regular polygon has rotational symmetry. The smallest angle it can be turned through to fit onto itself is 24°. How many sides does it have?", "ایک باقاعدہ کثیر الاضلاع میں گردشی تشاکل ہے۔ اسے کم از کم 24° گھمانے سے وہ اپنے اوپر بیٹھتا ہے۔ اس کے کتنے اضلاع ہیں؟",
      S4, ("Order = 360° ÷ smallest turn. A regular polygon's order is its number of sides.", "درجہ = 360° ÷ سب سے چھوٹا چکر۔ باقاعدہ کثیر الاضلاع کا درجہ اس کے اضلاع کی تعداد ہے۔"),
      ("Correct: 360 ÷ 24 = 15 sides.", "درست: 360 ÷ 24 = 15 اضلاع"),
      ("Model answer: order = 360° ÷ 24° = 15. A regular polygon with order 15 has 15 sides.", "نمونہ جواب: درجہ = 360° ÷ 24° = 15۔ درجہ 15 والے باقاعدہ کثیر الاضلاع کے 15 اضلاع ہوتے ہیں۔"),
      [(24, "24° is the angle. The number of sides is 360 ÷ 24 = 15.", "24° زاویہ ہے۔ اضلاع کی تعداد 360 ÷ 24 = 15 ہے۔", "order_for_angle"),
       (336, "That is 360 − 24. Divide: 360 ÷ 24 = 15.", "یہ 360 − 24 ہے۔ تقسیم کریں: 360 ÷ 24 = 15", "order_for_angle")]),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write the rule and full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں اصول اور پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   with_fig(long_q("l1_math", "Find the total number of lines of symmetry in all the letters of the word MATH, drawn in the picture.", "تصویر میں دیے گئے لفظ MATH کے سب حروف کی تشاکل کی لکیریں کل کتنی ہیں؟",
      L1, ("Fold each letter: M, A, T, H. Add up the lines.", "ہر حرف تہہ کر کے دیکھیں: M، A، T، H۔ لکیریں جمع کریں۔"),
      ("Correct: 1 + 1 + 1 + 2 = 5 lines of symmetry.", "درست: 1 + 1 + 1 + 2 = تشاکل کی 5 لکیریں"),
      ("Model answer: M has 1 (down the middle), A has 1, T has 1, H has 2 (down and across). Total = 1 + 1 + 1 + 2 = 5.", "نمونہ جواب: M کی 1 (بیچ سے اوپر نیچے)، A کی 1، T کی 1، H کی 2 (اوپر نیچے اور آر پار)۔ کل = 1 + 1 + 1 + 2 = 5"),
      [(4, "That gives H only 1 line. H folds down the middle and across the middle: 5.", "یہ H کی صرف 1 لکیر گنتا ہے۔ H بیچ سے اوپر نیچے اور آر پار تہہ ہوتا ہے: 5", "lines_counted_wrong"),
       (8, "That gives every letter 2 lines. Only H has 2: 5.", "یہ ہر حرف کی 2 لکیریں گنتا ہے۔ صرف H کی 2 ہیں: 5", "lines_counted_wrong")]), L1_FIG),
   with_fig(long_q("l2_alternate", "Lines l and m are parallel. The alternate angles shown are (3x − 10)° and (x + 50)°. Find the size of each of these angles, in degrees.", "لکیریں l اور m متوازی ہیں۔ دکھائے گئے متبادلہ زاویے (3x − 10)° اور (x + 50)° ہیں۔ ان میں سے ہر زاویے کی پیمائش ڈگری میں نکالیں۔",
      L2, ("Alternate angles are equal: 3x − 10 = x + 50. Find x, then the angle.", "متبادلہ زاویے برابر ہیں: 3x − 10 = x + 50۔ x نکالیں، پھر زاویہ۔"),
      ("Correct: 2x = 60, x = 30, and the angle is 30 + 50 = 80°.", "درست: 2x = 60، x = 30، اور زاویہ 30 + 50 = 80°"),
      ("Model answer: alternate angles are equal, so 3x − 10 = x + 50, 2x = 60, x = 30. Each angle = 30 + 50 = 80°. Check: 3 × 30 − 10 = 80.", "نمونہ جواب: متبادلہ زاویے برابر ہیں، تو 3x − 10 = x + 50، 2x = 60، x = 30۔ ہر زاویہ = 30 + 50 = 80°۔ جانچ: 3 × 30 − 10 = 80"),
      [(30, "30 is x. The question asks for the angle: 80°.", "30، x ہے۔ سوال زاویہ پوچھتا ہے: 80°", "answer_is_other_quantity"),
       (100, "That is 180° − 80°. Alternate angles are equal, so each is 80°.", "یہ 180° − 80° ہے۔ متبادلہ زاویے برابر ہیں، تو ہر ایک 80° ہے۔", "angle_rule_mix")]), L2_FIG),
   long_q("l3_ribbon", "A gift box is a cube with a side of 9 cm. A ribbon is stuck along all its edges. The ribbon costs Rs 2 for each centimetre. Find the cost of the ribbon, in rupees.", "تحفے کا ایک ڈبہ مکعب ہے جس کا ضلع 9 سینٹی میٹر ہے۔ ایک فیتہ اس کے سب کناروں پر چپکایا جاتا ہے۔ فیتے کی قیمت فی سینٹی میٹر 2 روپے ہے۔ فیتے کی لاگت روپوں میں نکالیں۔",
      L3, ("A cube has 12 edges. Length of ribbon first, then × 2.", "مکعب کے 12 کنارے ہوتے ہیں۔ پہلے فیتے کی لمبائی، پھر × 2"),
      ("Correct: ribbon 12 × 9 = 108 cm, cost 108 × 2 = Rs 216.", "درست: فیتہ 12 × 9 = 108 سینٹی میٹر، لاگت 108 × 2 = 216 روپے"),
      ("Model answer: a cube has 12 equal edges. Length = 12 × 9 = 108 cm. Cost = 108 × 2 = Rs 216.", "نمونہ جواب: مکعب کے 12 برابر کنارے ہوتے ہیں۔ لمبائی = 12 × 9 = 108 سینٹی میٹر۔ لاگت = 108 × 2 = 216 روپے"),
      [(108, "108 cm is the length of ribbon. Multiply by Rs 2: 216.", "108 سینٹی میٹر فیتے کی لمبائی ہے۔ 2 روپے سے ضرب دیں: 216", "answer_is_other_quantity"),
       (144, "That counts only 8 edges. A cube has 12: 216.", "یہ صرف 8 کنارے گنتا ہے۔ مکعب کے 12 ہوتے ہیں: 216", "edges_miscount")]),
   long_q("l4_toy", "A star-shaped toy has rotational symmetry of order 5. It is turned about its centre through 216°. It then looks exactly as it did at the start. How many of its smallest matching turns is this?", "ستارے کی شکل کے کھلونے کے گردشی تشاکل کا درجہ 5 ہے۔ اسے اس کے مرکز کے گرد 216° گھمایا جاتا ہے۔ اس کے بعد وہ بالکل پہلے جیسا لگتا ہے۔ یہ اس کے سب سے چھوٹے ملتے ہوئے چکروں میں سے کتنے ہیں؟",
      L4, ("Smallest turn = 360° ÷ 5. Then 216° ÷ that.", "سب سے چھوٹا چکر = 360° ÷ 5۔ پھر 216° ÷ وہ"),
      ("Correct: smallest turn 72°, and 216 ÷ 72 = 3.", "درست: سب سے چھوٹا چکر 72°، اور 216 ÷ 72 = 3"),
      ("Model answer: smallest turn = 360° ÷ 5 = 72°. Number of turns = 216° ÷ 72° = 3.", "نمونہ جواب: سب سے چھوٹا چکر = 360° ÷ 5 = 72°۔ چکروں کی تعداد = 216° ÷ 72° = 3"),
      [(72, "72° is the smallest turn. The question asks how many of them make 216°: 3.", "72° سب سے چھوٹا چکر ہے۔ سوال پوچھتا ہے کتنے مل کر 216° بنتے ہیں: 3", "answer_is_other_quantity"),
       (43, "That divides 216 by 5. Divide by the smallest turn, 72: 3.", "یہ 216 کو 5 سے تقسیم کرتا ہے۔ سب سے چھوٹے چکر، 72، سے تقسیم کریں: 3", "order_for_angle")]),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 9 test. Well done!", "آپ نے باب 9 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: a cuboid or cube has 6 faces, 12 edges and 8 vertices; a cone 2, 1, 1; a cylinder 3, 2, 0; a sphere 1, 0, 0. Between parallel lines, corresponding and alternate angles are equal and co-interior angles add up to 180°; vertically opposite angles are always equal. A point and its image are the same distance from the mirror line. The smallest turn of rotational symmetry is 360° ÷ order.",
              "امتحان میں: مکعب نما یا مکعب کی 6 سطحیں، 12 کنارے اور 8 راس ہوتے ہیں؛ مخروط کی 2، 1، 1؛ اسطوانے کی 3، 2، 0؛ کرہ کی 1، 0، 0۔ متوازی لکیروں کے درمیان متناظرہ اور متبادلہ زاویے برابر ہوتے ہیں اور ہم اندرونی زاویوں کا مجموعہ 180° ہوتا ہے؛ راسی زاویے ہمیشہ برابر ہوتے ہیں۔ نقطہ اور اس کا عکس آئینہ لکیر سے برابر فاصلے پر ہوتے ہیں۔ گردشی تشاکل کا سب سے چھوٹا چکر 360° ÷ درجہ ہے۔"),
    "points": [T("Rule, numbers, answer with its unit.", "اصول، اعداد، اکائی کے ساتھ جواب۔"),
               T("Equation for x: write it, solve it, then answer the question asked.", "x کی مساوات: لکھیں، حل کریں، پھر پوچھا گیا جواب دیں۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_cyl_edges", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_cyl_edges", ("How many edges does a cylinder have?", "اسطوانے کے کتنے کنارے ہیں؟"), R1,
     ("The rim of the top and the rim of the bottom.", "اوپر کا گھیرا اور نیچے کا گھیرا۔"),
     ("Correct: 2 edges.", "درست: 2 کنارے"), ("One circle on top and one at the bottom: 2.", "ایک دائرہ اوپر اور ایک نیچے: 2"),
     [(3, "3 is the number of faces. Edges: 2.", "3 سطحوں کی تعداد ہے۔ کنارے: 2", "solid_parts_mix")], qtype=None)},
   {"id": "r_exam_pentagon_order", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_pentagon_order", ("What is the order of rotational symmetry of a regular pentagon?", "باقاعدہ پانچ ضلعی شکل کے گردشی تشاکل کا درجہ کیا ہے؟"), R2,
     ("A regular shape's order equals its number of sides.", "باقاعدہ شکل کا درجہ اس کے اضلاع کی تعداد کے برابر ہوتا ہے۔"),
     ("Correct: order 5.", "درست: درجہ 5"), ("5 sides, order 5.", "5 اضلاع، درجہ 5"),
     [(72, "72° is the smallest turn. The order is 5.", "72° سب سے چھوٹا چکر ہے۔ درجہ 5 ہے۔", "order_for_angle")], qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 9 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.symmetry.chapter_9_test), with the skills of the Symmetry unit, the Solids unit and the Angles unit as prerequisites, and is mastered with exam_style questions, like the chapter 5 to 8 tests.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), all as in the earlier chapter tests; the solid, angle and symmetry words come from the existing lessons. باقاعدہ کثیر الاضلاع (regular polygon) is new, so a teacher should confirm it.",
   "The numbers were worked out in content/sources/g6-maths-18/chapter_9_test.py; counts of lines and orders of symmetry were checked by flipping and turning the drawn shapes in figs.py. Edit the script, not this file.",
 ],
 "review": REVIEW,
}

write(lesson)

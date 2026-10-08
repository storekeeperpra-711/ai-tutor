from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, AREA_RECTANGLE, SO_PARTS)

SKILL = SO_PARTS

# A cuboid (and a cube) has 6 faces, 12 edges and 8 corners.
FACES, EDGES, CORNERS = 6, 12, 8
# Edges: 4 round the top, 4 round the bottom, 4 standing up.
assert 4 + 4 + 4 == EDGES
# Corners: 4 on top, 4 on the bottom.
assert 4 + 4 == CORNERS
# Faces: top and bottom, front and back, left and right.
assert 2 + 2 + 2 == FACES

# s2: area of a 6 cm by 4 cm rectangle
S2 = 6 * 4
assert S2 == 24
# s8: total faces on 3 separate dice
S8 = 3 * FACES
assert S8 == 18
# s11: a box with no lid has one face fewer
S11 = FACES - 1
assert S11 == 5
# review: faces on 2 separate matchboxes
R2 = 2 * FACES
assert R2 == 12

# ---------- figures ----------
from figs import Box, fit, figure, row, box_items, point, line, poly, circle, with_figures

# Everyday boxes in cm (only their shapes are drawn, not their sizes).
MATCHBOX = (5, 3, 2)
BRICK = (20, 10, 7)
DICE = 2


def plain_box(l, d, h, max_w=150, max_h=90, open_top=False):
    items, b = box_items(l, d, h, labels=False, max_w=max_w, max_h=max_h, open_top=open_top)
    return items, b


def dice(size_w=80, dots=5):
    """A cube with dots on its front face, like a dice."""
    items, b = plain_box(DICE, DICE, DICE, max_w=size_w, max_h=size_w)
    q = DICE / 4
    spots = {1: [(2, 2)], 3: [(1, 3), (2, 2), (3, 1)], 5: [(1, 1), (1, 3), (2, 2), (3, 1), (3, 3)]}[dots]
    items += [circle(b.p(q * a, 0, q * c), b.s * 0.22, fill=True) for a, c in spots]
    return items


HIDDEN_EN = "The hidden edges at the back are dashed."
HIDDEN_UR = "پیچھے کے چھپے ہوئے کنارے ڈیش والی لکیروں سے دکھائے گئے ہیں۔"

F_HOOK = figure(
    "Three solids side by side: a matchbox and a long brick, both cuboids with rectangle faces, and a dice, a cube with a square front face showing five dots. "
    "Each is drawn in 3-D: the front, a shaded top and a shaded right side.",
    "تین ٹھوس اشکال ساتھ ساتھ: ماچس کی ڈبیا اور لمبی اینٹ، دونوں مکعب نما جن کی سطحیں مستطیل ہیں، اور پانسہ، یعنی مکعب جس کی سامنے والی مربع سطح پر پانچ نقطے ہیں۔ "
    "ہر ایک تین رخی (3-D) شکل میں ہے: سامنے کا رخ، اوپر اور دائیں رخ پر رنگ۔",
    row([plain_box(*MATCHBOX, max_w=74, max_h=70)[0], plain_box(*BRICK, max_w=118, max_h=70)[0], dice(60)], gap=16))


def parts_fig():
    """A cuboid with its 8 corners marked and its hidden edges dashed."""
    items, b = box_items(*MATCHBOX, labels=False, max_w=200, max_h=120)
    items += b.corners()
    return figure(
        "A cuboid drawn in 3-D. Its front face is a rectangle and its top and right side are shaded, so 3 faces can be seen; "
        "the other 3 (back, bottom and left) are hidden. Its edges are the lines where two faces meet: 4 round the top, 4 round the bottom "
        "and 4 standing up. A dot marks each of its 8 corners, 4 on top and 4 on the bottom. The 3 edges at the hidden back corner are dashed.",
        "ایک مکعب نما تین رخی (3-D) شکل میں۔ سامنے کی سطح مستطیل ہے اور اوپر اور دائیں رخ پر رنگ ہے، تو 3 سطحیں نظر آتی ہیں؛ "
        "باقی 3 (پیچھے، نیچے اور بائیں) چھپی ہیں۔ کنارے وہ لکیریں ہیں جہاں دو سطحیں ملتی ہیں: 4 اوپر، 4 نیچے اور 4 کھڑے۔ "
        "اس کے 8 کونوں میں سے ہر ایک پر نقطہ ہے، 4 اوپر اور 4 نیچے۔ چھپے ہوئے پچھلے کونے کے 3 کنارے ڈیش والی لکیروں سے ہیں۔",
        items)


def solid_fig(dims, en, ur, max_w=200, max_h=120):
    items, _ = box_items(*dims, labels=False, max_w=max_w, max_h=max_h)
    return figure(en + " " + HIDDEN_EN, ur + " " + HIDDEN_UR, items)


F_PARTS = parts_fig()
F_MATCHBOX = solid_fig(MATCHBOX, "A matchbox, a cuboid, drawn in 3-D: its front face, its shaded top and its shaded right side can be seen.",
                       "ماچس کی ڈبیا، ایک مکعب نما، تین رخی (3-D) شکل میں: اس کی سامنے والی سطح، رنگی ہوئی اوپر والی اور دائیں سطح نظر آتی ہیں۔")
F_DICE = figure("A dice, a cube, drawn in 3-D: its square front face with five dots, its shaded top and its shaded right side. " + HIDDEN_EN,
                "ایک پانسہ، یعنی مکعب، تین رخی (3-D) شکل میں: اس کی سامنے والی مربع سطح جس پر پانچ نقطے ہیں، اوپر اور دائیں رخ پر رنگ۔ " + HIDDEN_UR,
                dice(120))
F_BRICK = solid_fig(BRICK, "A brick, a long cuboid, drawn in 3-D: its front face, its shaded top and its shaded right side can be seen.",
                    "ایک اینٹ، لمبا مکعب نما، تین رخی (3-D) شکل میں: اس کی سامنے والی سطح، رنگی ہوئی اوپر والی اور دائیں سطح نظر آتی ہیں۔", max_w=230)
F_THREE_DICE = figure(f"{S8 // FACES} dice lying apart in a row, each a cube drawn in 3-D with dots on its front. On each dice only 3 faces can be seen. " + HIDDEN_EN,
                      f"{S8 // FACES} پانسے ایک قطار میں الگ الگ، ہر ایک مکعب تین رخی (3-D) شکل میں، سامنے نقطے۔ ہر پانسے کی صرف 3 سطحیں نظر آتی ہیں۔ " + HIDDEN_UR,
                      row([dice(64, 1), dice(64, 3), dice(64, 5)], gap=26))


def no_lid_fig():
    """A shoe box with its lid lifted off and floating above it."""
    l, d, h = 6, 4, 2.5
    items, b = box_items(l, d, h, labels=False, max_w=200, max_h=100, open_top=True)
    lift = -b.s * 2.2
    lid = [b.p(0, 0, h), b.p(l, 0, h), b.p(l, d, h), b.p(0, d, h)]
    items.append(poly([(x, y + lift) for x, y in lid], fill=True))
    return figure("A shoe box drawn in 3-D with its lid lifted off. The lid, a shaded flat rectangle, floats above the box, and the top of the box is open. "
                  "The front, the right side, the back, the left side and the bottom are still there. The two hidden edges along the bottom at the back are dashed.",
                  "جوتوں کا ڈبہ تین رخی (3-D) شکل میں، جس کا ڈھکن اتار دیا گیا ہے۔ ڈھکن، ایک رنگی ہوئی چپٹی مستطیل، ڈبے کے اوپر ہوا میں ہے، اور ڈبے کا اوپر والا حصہ کھلا ہے۔ "
                  "سامنے، دایاں، پیچھے، بایاں رخ اور نیچے کی سطح ابھی موجود ہیں۔ پیچھے نیچے کے دو چھپے ہوئے کنارے ڈیش والی لکیروں سے ہیں۔",
                  items)


F_NO_LID = no_lid_fig()
F_CUBE = figure("A cube drawn in 3-D: its square front face, its shaded top and its shaded right side. " + HIDDEN_EN,
                "ایک مکعب تین رخی (3-D) شکل میں: اس کی سامنے والی مربع سطح، اوپر اور دائیں رخ پر رنگ۔ " + HIDDEN_UR,
                plain_box(2, 2, 2, max_w=120, max_h=120)[0])
F_TEA = solid_fig((4, 3, 6), "A tall box of tea, a cuboid, drawn in 3-D: its front face, its shaded top and its shaded right side can be seen.",
                  "چائے کا اونچا ڈبہ، ایک مکعب نما، تین رخی (3-D) شکل میں: اس کی سامنے والی سطح، رنگی ہوئی اوپر والی اور دائیں سطح نظر آتی ہیں۔", max_h=140)
F_BOOK = solid_fig((6, 8, 1), "A book lying flat, a thin cuboid, drawn in 3-D: its front edge face, its large shaded top and its shaded right side can be seen.",
                   "میز پر رکھی ایک کتاب، پتلا مکعب نما، تین رخی (3-D) شکل میں: اس کی سامنے والی پتلی سطح، رنگی ہوئی بڑی اوپر والی سطح اور دائیں سطح نظر آتی ہیں۔")
F_TWO_BOXES = figure(f"{R2 // FACES} matchboxes lying apart, each a cuboid drawn in 3-D with its front, its shaded top and its shaded right side. " + HIDDEN_EN,
                     f"{R2 // FACES} ماچس کی ڈبیاں الگ الگ، ہر ایک مکعب نما تین رخی (3-D) شکل میں: سامنے، اوپر اور دائیں رخ پر رنگ۔ " + HIDDEN_UR,
                     row([plain_box(*MATCHBOX, max_w=110, max_h=80)[0], plain_box(*MATCHBOX, max_w=110, max_h=80)[0]], gap=40))

FIGS = {
    "s1_hook": F_HOOK, "s3_parts": F_PARTS, "s4_faces": F_MATCHBOX, "s5_edges": F_DICE, "s7_corners": F_BRICK,
    "s8_three_dice": F_THREE_DICE, "s11_no_lid": F_NO_LID, "qb_corners": F_CUBE, "qb_apply": F_TEA,
    "qb_find_error": F_DICE, "r_edges": F_BOOK, "r_two_boxes": F_TWO_BOXES,
}


lesson = {
 "id": "g6-maths-14-solids",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Name cubes and cuboids and count their faces, edges and corners (vertices).", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Cubes and cuboids", "مکعب اور مکعب نما"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": AREA_RECTANGLE}],
 "misconceptions": [
   {"id": "counts_visible_only", "description": "Counts only the faces, edges or corners that can be seen from one side."},
   {"id": "mixes_parts", "description": "Mixes up faces, edges and corners."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_corners", "type": "recall", "step": number_question(
     "qb_corners",
     T("How many corners (vertices) does a cube have?", "مکعب کے کتنے کونے (راس) ہوتے ہیں؟"),
     CORNERS,
     T("4 on top and 4 on the bottom.", "4 اوپر اور 4 نیچے۔"),
     T("Right! 8 corners.", "درست! 8 کونے"),
     T("4 on top + 4 on the bottom = 8.", "4 اوپر + 4 نیچے = 8"),
     common_wrong=[wrong(4, "There are 4 on top and 4 more on the bottom: 8.", "4 اوپر ہیں اور 4 مزید نیچے: 8", "counts_visible_only"),
                   wrong(6, "6 is the number of faces. A cube has 8 corners.", "6 سطحوں کی تعداد ہے۔ مکعب کے 8 کونے ہیں۔", "mixes_parts")],
     qtype=None)},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A box of tea is a cuboid. How many edges does it have?", "چائے کا ڈبہ مکعب نما ہے۔ اس کے کتنے کنارے ہیں؟"),
     EDGES,
     T("4 round the top, 4 round the bottom, 4 standing up.", "4 اوپر، 4 نیچے، 4 کھڑے۔"),
     T("Right! 12 edges.", "درست! 12 کنارے"),
     T("4 + 4 + 4 = 12.", "4 + 4 + 4 = 12"),
     common_wrong=[wrong(8, "8 is the number of corners. A cuboid has 12 edges.", "8 کونوں کی تعداد ہے۔ مکعب نما کے 12 کنارے ہیں۔", "mixes_parts")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Zain looks at a dice on the table and says, \"A cube has 3 faces.\" What is wrong?", "زین میز پر رکھے پانسے کو دیکھ کر کہتا ہے، \"مکعب کی 3 سطحیں ہوتی ہیں۔\" کیا غلطی ہے؟"),
     "options": [
       opt("hidden", "He counted only the faces he can see. A cube has 6 faces.", "اس نے صرف وہ سطحیں گنیں جو نظر آتی ہیں۔ مکعب کی 6 سطحیں ہیں۔", True,
           "Yes! The bottom and the back faces are hidden.", "جی ہاں! نیچے اور پیچھے کی سطحیں چھپی ہوئی ہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Some faces are hidden from view. A dice has 6 faces, numbered 1 to 6.", "کچھ سطحیں نظر سے چھپی ہیں۔ پانسے کی 6 سطحیں ہیں، 1 سے 6 تک۔", "counts_visible_only"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_cuboid", "front": T("Cuboid: faces, edges, corners?", "مکعب نما: سطحیں، کنارے، کونے؟"),
    "back": T("6 faces, 12 edges, 8 corners.", "6 سطحیں، 12 کنارے، 8 کونے۔")},
   {"id": "f_cube", "front": T("What makes a cube special?", "مکعب میں خاص کیا ہے؟"),
    "back": T("All 6 faces are equal squares.", "اس کی تمام 6 سطحیں برابر مربع ہیں۔")},
 ],
 "home_tasks": [{"id": "h_hunt", "text": T(
   "Find three cuboids at home, like a matchbox, a brick or a book. For one of them, touch and count its faces, edges and corners.",
   "گھر میں تین مکعب نما چیزیں ڈھونڈیں، جیسے ماچس کی ڈبیا، اینٹ یا کتاب۔ ان میں سے ایک کی سطحیں، کنارے اور کونے چھو کر گنیں۔")}],
 "glossary": [T("Cube", "مکعب"), T("Cuboid", "مکعب نما"), T("Face", "سطح"), T("Edge", "کنارہ"), T("Corner (vertex)", "کونا (راس)")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A matchbox, a brick and a dice. What shape are they, and how many sides do they have?",
                     "ماچس کی ڈبیا، اینٹ اور پانسہ۔ ان کی شکل کیا ہے، اور ان کے کتنے رخ ہیں؟"),
    "text": T("Today we look at solid shapes. First, a quick area check.", "آج ہم ٹھوس اشکال دیکھیں گے۔ پہلے رقبے کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("A rectangle is 6 cm long and 4 cm wide. What is its area, in cm²?", "ایک مستطیل 6 سینٹی میٹر لمبا اور 4 سینٹی میٹر چوڑا ہے۔ اس کا رقبہ کتنے مربع سینٹی میٹر ہے؟"),
     S2,
     T("Area = length × width.", "رقبہ = لمبائی × چوڑائی"),
     T("Right! 24 cm².", "درست! 24 مربع سینٹی میٹر"),
     T("6 × 4 = 24.", "6 × 4 = 24"),
     common_wrong=[wrong(20, "20 cm is the perimeter. Area = 6 × 4 = 24.", "20 سینٹی میٹر احاطہ ہے۔ رقبہ = 6 × 4 = 24")],
     qtype="recall", skill=AREA_RECTANGLE),
   {"id": "s3_parts", "type": "explain",
    "character": say("happy", "Flat sides are faces. Where two faces meet is an edge. Where edges meet is a corner.", "چپٹے رخ سطحیں ہیں۔ جہاں دو سطحیں ملیں وہ کنارہ ہے۔ جہاں کنارے ملیں وہ کونا ہے۔"),
    "text": T("A matchbox and a brick are cuboids: every face is a rectangle. A dice is a cube: every face is the same square. Both have 6 faces (top and bottom, front and back, left and right), 12 edges (4 round the top, 4 round the bottom, 4 standing up) and 8 corners, also called vertices (4 on top, 4 on the bottom).",
              "ماچس کی ڈبیا اور اینٹ مکعب نما ہیں: ہر سطح مستطیل ہے۔ پانسہ مکعب ہے: ہر سطح ایک جیسا مربع ہے۔ دونوں کی 6 سطحیں (اوپر اور نیچے، آگے اور پیچھے، دائیں اور بائیں)، 12 کنارے (4 اوپر، 4 نیچے، 4 کھڑے) اور 8 کونے یعنی راس (4 اوپر، 4 نیچے) ہوتے ہیں۔")},
   number_question(
     "s4_faces",
     T("A matchbox is a cuboid. How many faces does it have?", "ماچس کی ڈبیا مکعب نما ہے۔ اس کی کتنی سطحیں ہیں؟"),
     FACES,
     T("Top and bottom, front and back, left and right.", "اوپر اور نیچے، آگے اور پیچھے، دائیں اور بائیں۔"),
     T("Right! 6 faces.", "درست! 6 سطحیں"),
     T("2 + 2 + 2 = 6.", "2 + 2 + 2 = 6"),
     common_wrong=[wrong(4, "Don't forget the top and bottom: 6 faces.", "اوپر اور نیچے نہ بھولیں: 6 سطحیں", "counts_visible_only"),
                   wrong(3, "Some faces are hidden. A cuboid has 6.", "کچھ سطحیں چھپی ہیں۔ مکعب نما کی 6 ہیں۔", "counts_visible_only")]),
   number_question(
     "s5_edges",
     T("A dice is a cube. How many edges does it have?", "پانسہ مکعب ہے۔ اس کے کتنے کنارے ہیں؟"),
     EDGES,
     T("4 round the top, 4 round the bottom, 4 standing up.", "4 اوپر، 4 نیچے، 4 کھڑے۔"),
     T("Right! 12 edges.", "درست! 12 کنارے"),
     T("4 + 4 + 4 = 12.", "4 + 4 + 4 = 12"),
     common_wrong=[wrong(8, "8 is the number of corners. A cube has 12 edges.", "8 کونوں کی تعداد ہے۔ مکعب کے 12 کنارے ہیں۔", "mixes_parts"),
                   wrong(6, "6 is the number of faces. A cube has 12 edges.", "6 سطحوں کی تعداد ہے۔ مکعب کے 12 کنارے ہیں۔", "mixes_parts")]),
   {"id": "s6_face_shape", "type": "choice",
    "prompt": T("What shape is each face of a cube?", "مکعب کی ہر سطح کس شکل کی ہوتی ہے؟"),
    "options": [
      opt("square", "A square", "مربع", True, "Yes! All 6 faces are equal squares.", "جی ہاں! تمام 6 سطحیں برابر مربع ہیں۔"),
      opt("rectangle", "A long rectangle", "لمبا مستطیل", False, "That is a cuboid like a brick. A cube has square faces.", "یہ اینٹ جیسا مکعب نما ہے۔ مکعب کی سطحیں مربع ہیں۔"),
      opt("triangle", "A triangle", "مثلث", False, "A cube has no triangles. Its faces are squares.", "مکعب میں کوئی مثلث نہیں۔ اس کی سطحیں مربع ہیں۔"),
    ]},
   number_question(
     "s7_corners",
     T("A brick is a cuboid. How many corners does it have?", "اینٹ مکعب نما ہے۔ اس کے کتنے کونے ہیں؟"),
     CORNERS,
     T("4 on top and 4 on the bottom.", "4 اوپر اور 4 نیچے۔"),
     T("Right! 8 corners.", "درست! 8 کونے"),
     T("4 + 4 = 8.", "4 + 4 = 8"),
     common_wrong=[wrong(4, "There are 4 more on the bottom: 8.", "4 مزید نیچے ہیں: 8", "counts_visible_only"),
                   wrong(12, "12 is the number of edges. A brick has 8 corners.", "12 کناروں کی تعداد ہے۔ اینٹ کے 8 کونے ہیں۔", "mixes_parts")]),
   number_question(
     "s8_three_dice",
     T("Bilal has 3 dice, lying apart on the table. How many faces are there on all 3 dice?", "بلال کے پاس 3 پانسے ہیں جو میز پر الگ الگ پڑے ہیں۔ تینوں پانسوں کی کل کتنی سطحیں ہیں؟"),
     S8,
     T("Each dice has 6 faces.", "ہر پانسے کی 6 سطحیں ہیں۔"),
     T("Right! 3 × 6 = 18.", "درست! 3 × 6 = 18"),
     T("3 × 6 = 18.", "3 × 6 = 18"),
     common_wrong=[wrong(9, "Count every face, even the hidden ones: 3 × 6 = 18.", "ہر سطح گنیں، چھپی ہوئی بھی: 3 × 6 = 18", "counts_visible_only")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hina says, \"A cuboid has 4 faces: front, back, left and right.\" What did she miss?", "حنا کہتی ہے، \"مکعب نما کی 4 سطحیں ہیں: آگے، پیچھے، دائیں اور بائیں۔\" وہ کیا بھول گئی؟"),
    "options": [
      opt("top_bottom", "The top and the bottom. A cuboid has 6 faces.", "اوپر اور نیچے۔ مکعب نما کی 6 سطحیں ہیں۔", True,
          "Yes! Top and bottom are faces too.", "جی ہاں! اوپر اور نیچے بھی سطحیں ہیں۔"),
      opt("edges", "She should count edges instead.", "اسے کنارے گننے چاہییں۔", False,
          "The question is about faces. She missed the top and the bottom.", "سوال سطحوں کا ہے۔ وہ اوپر اور نیچے بھول گئی۔", "mixes_parts"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Look above and below the box: 2 more faces, so 6.", "ڈبے کے اوپر اور نیچے دیکھیں: 2 سطحیں مزید، تو 6", "counts_visible_only"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "How can we be sure a cube has 12 edges without losing count? Can you teach me?",
                     "ہم گنتی بھولے بغیر کیسے یقین کریں کہ مکعب کے 12 کنارے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: explain a way to count the 12 edges of a cube.", "اپنے الفاظ میں بتائیں: مکعب کے 12 کنارے گننے کا ایک طریقہ۔"),
    "key_idea": "Count the edges in groups: 4 edges go round the top face, 4 go round the bottom face, and 4 stand up joining top to bottom. 4 + 4 + 4 = 12.",
    "levels": {
      "got_it": "Counts in groups: 4 round the top, 4 round the bottom and 4 standing up, making 12.",
      "partly": "Says 4 + 4 + 4 or 3 groups, without saying where the groups are.",
      "not_yet": "Gives no method."},
    "keywords": [
      ["top", "upper", "اوپر"],
      ["bottom", "lower", "نیچے"],
      ["standing", "up", "side", "کھڑے", "درمیان"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 4 on top, 4 on the bottom, 4 standing up.", "بہت خوب! 4 اوپر، 4 نیچے، 4 کھڑے۔"),
      "partly": T("Good start! Now say where each group of 4 edges is.", "اچھی شروعات! اب بتائیں 4 کناروں کا ہر گروپ کہاں ہے۔"),
      "not_yet": T("Look at the top face of a dice. How many edges go round it? Now the bottom?", "پانسے کی اوپر والی سطح دیکھیں۔ اس کے گرد کتنے کنارے ہیں؟ اب نیچے والی؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_no_lid",
     T("A shoe box has its lid taken off. How many faces does the open box have now?", "جوتوں کے ڈبے کا ڈھکن اتار دیا گیا۔ کھلے ڈبے کی اب کتنی سطحیں ہیں؟"),
     S11,
     T("A closed box has 6 faces. The lid was one of them.", "بند ڈبے کی 6 سطحیں ہیں۔ ڈھکن ان میں سے ایک تھا۔"),
     T("Right! 6 − 1 = 5.", "درست! 6 − 1 = 5"),
     T("6 faces − the lid = 5.", "6 سطحیں − ڈھکن = 5"),
     common_wrong=[wrong(6, "The lid is gone, so one face fewer: 5.", "ڈھکن ہٹ گیا، تو ایک سطح کم: 5"),
                   wrong(4, "Only the top is gone. The bottom is still there: 5.", "صرف اوپر والی ہٹی ہے۔ نیچے والی موجود ہے: 5", "counts_visible_only")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Six faces, twelve edges, eight corners. You know your boxes!", "چھ سطحیں، بارہ کنارے، آٹھ کونے۔ آپ ڈبوں کو جان گئے!"),
    "text": T("Cubes and cuboids both have 6 faces, 12 edges and 8 corners (vertices). A cuboid's faces are rectangles; a cube's faces are equal squares. Count hidden faces too.",
              "مکعب اور مکعب نما دونوں کی 6 سطحیں، 12 کنارے اور 8 کونے (راس) ہوتے ہیں۔ مکعب نما کی سطحیں مستطیل ہیں؛ مکعب کی سطحیں برابر مربع ہیں۔ چھپی ہوئی سطحیں بھی گنیں۔"),
    "points": [T("6 faces, 12 edges, 8 corners.", "6 سطحیں، 12 کنارے، 8 کونے۔"),
               T("Cube: all faces are squares.", "مکعب: تمام سطحیں مربع۔")]},
 ],
 "review_questions": [
   {"id": "r_edges", "type": "apply", "skill": SKILL, "step": number_question(
     "r_edges",
     T("A book is a cuboid. How many edges does it have?", "کتاب مکعب نما ہے۔ اس کے کتنے کنارے ہیں؟"),
     EDGES,
     T("4 + 4 + 4.", "4 + 4 + 4"),
     T("Right! 12.", "درست! 12"),
     T("4 round the top, 4 round the bottom, 4 standing up: 12.", "4 اوپر، 4 نیچے، 4 کھڑے: 12"),
     common_wrong=[wrong(8, "8 is the number of corners. A cuboid has 12 edges.", "8 کونوں کی تعداد ہے۔ مکعب نما کے 12 کنارے ہیں۔", "mixes_parts")],
     qtype=None)},
   {"id": "r_two_boxes", "type": "apply", "skill": SKILL, "step": number_question(
     "r_two_boxes",
     T("How many faces are there on 2 separate matchboxes?", "2 الگ ماچس کی ڈبیوں کی کل کتنی سطحیں ہیں؟"),
     R2,
     T("Each matchbox has 6 faces.", "ہر ڈبیا کی 6 سطحیں ہیں۔"),
     T("Right! 2 × 6 = 12.", "درست! 2 × 6 = 12"),
     T("2 × 6 = 12.", "2 × 6 = 12"),
     common_wrong=[wrong(6, "That is for one matchbox. Two have 12.", "یہ ایک ڈبیا کی ہیں۔ دو کی 12 ہیں۔")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Solids unit. No textbook text or exercises were used.",
   "Solids are drawn in a simple 3-D view (figs.py): front face, shaded top and side, hidden edges dashed. They are also linked to everyday objects children can hold: a matchbox, a brick, a dice.",
   "Urdu terms to check: مکعب (cube), مکعب نما (cuboid), سطح (face), کنارہ (edge), راس (vertex).",
   "The numbers were worked out in content/sources/g6-maths-14/solids.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(with_figures(lesson, FIGS))

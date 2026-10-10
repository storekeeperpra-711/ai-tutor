"""Practice set for Exercise 9.1 of the book: naming the 3-D shape of everyday
objects, telling 1-D, 2-D and 3-D figures apart, and counting faces, edges and
vertices. The questions are new; only the kinds of question follow the book."""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL, SO_PARTS, SY_SHAPES)
from figs import fig, with_fig, regular, poly, cylinder, cone, cuboid, C

SKILL = EX_SKILL["9.1"]

# (faces, edges, vertices) of each solid. A curved surface counts as a face and
# the circle where a curved surface meets a flat one counts as an edge.
CUBOID_FACES = 2 + 2 + 2                      # top/bottom, front/back, left/right
CUBOID_EDGES = 4 + 4 + 4                      # round the top, round the bottom, standing up
CUBOID_VERTS = 4 + 4
SOLIDS = {
    "cube": (6, 12, 8), "cuboid": (CUBOID_FACES, CUBOID_EDGES, CUBOID_VERTS),
    "cylinder": (2 + 1, 2, 0), "cone": (1 + 1, 1, 1), "sphere": (1, 0, 0), "hemisphere": (1 + 1, 1, 0),
}
assert SOLIDS["cube"] == SOLIDS["cuboid"] == (6, 12, 8)
# Exactly one solid has 1 edge and 1 vertex.
assert [k for k, v in SOLIDS.items() if v[1:] == (1, 1)] == ["cone"]
assert [k for k, v in SOLIDS.items() if v[1:] == (0, 0)] == ["sphere"]

# q4: flat faces of a cylinder
Q4 = 2
assert SOLIDS["cylinder"][0] - 1 == Q4
# q5: vertices of a cone
Q5 = SOLIDS["cone"][2]
assert Q5 == 1
# q6: faces of a cone
Q6 = SOLIDS["cone"][0]
assert Q6 == 2 and 1 + 1 == Q6
# q7: edges of a cuboid (matchbox); only 9 can be seen
Q7 = SOLIDS["cuboid"][1]
assert Q7 == 12 and 12 - 3 == 9 and SOLIDS["cuboid"][2] == 8 and SOLIDS["cuboid"][0] == 6
# q8: sides of a regular hexagon
Q8 = len(regular(6, C, 26, start=0))
assert Q8 == 6
# q9: four separate dice, vertices altogether
Q9 = 4 * SOLIDS["cube"][2]
assert Q9 == 32 and 4 * SOLIDS["cube"][0] == 24 and SOLIDS["cube"][2] == 8
# q10: wire frame of a cuboid 6 cm by 4 cm by 3 cm: 4 edges of each length
Q10 = 4 * (6 + 4 + 3)
assert Q10 == 52 and 6 + 4 + 3 == 13 and 2 * (6 + 4 + 3) == 26 and 6 * 4 * 3 == 72
# q11 (find error): hemisphere has 1 flat and 1 curved face
assert SOLIDS["hemisphere"][0] == 2
# q12 (find error): cone vertices 1, not 2
assert SOLIDS["cone"][2] == 1 and SOLIDS["cone"][1] == 1
# bank and review
QB1 = SOLIDS["sphere"][0]
assert QB1 == 1
QB2 = SOLIDS["cylinder"][1]
assert QB2 == 2
QB3 = 2 * SOLIDS["cube"][0]
assert QB3 == 12 and SOLIDS["cube"][0] == 6
R1 = 2 * SOLIDS["cuboid"][2]
assert R1 == 16 and SOLIDS["cuboid"][2] == 8
R2 = SOLIDS["hemisphere"][0]
assert R2 == 2

F_CYL = fig(100, 70,
    "A tin shaped like a cylinder: a flat circle on top, a curved side, and a flat circle at the bottom. The hidden back half of the bottom edge is dashed.",
    "اسطوانے کی شکل کا ایک ڈبہ: اوپر چپٹا دائرہ، خمدار پہلو، اور نیچے چپٹا دائرہ۔ نیچے کے کنارے کا چھپا ہوا پچھلا نصف ڈیش والی لکیر سے دکھایا ہے۔",
    cylinder(complex(50, 36)))
F_CONE = fig(100, 70,
    "An ice-cream cone shape: a sharp tip at the top, a curved side, and a flat round base at the bottom. The hidden back half of the base edge is dashed.",
    "آئس کریم کون جیسی شکل: اوپر نوک دار سرا، خمدار پہلو، اور نیچے چپٹا گول قاعدہ۔ قاعدے کے کنارے کا چھپا ہوا پچھلا نصف ڈیش والی لکیر سے دکھایا ہے۔",
    cone(complex(50, 36)))
F_MATCH = fig(100, 70,
    "A matchbox shape, a cuboid, drawn in 3-D: a front rectangle, a top and a right side. The three hidden edges at the back are dashed.",
    "ماچس کی ڈبیا جیسی شکل، یعنی مکعب نما، تین رخی (3-D) انداز میں: سامنے مستطیل، اوپر اور دائیں پہلو۔ پیچھے کے تین چھپے کنارے ڈیش والی لکیروں سے دکھائے ہیں۔",
    cuboid(complex(18, 26), 56, 34, depth=(22, -16)))
F_HEX = fig(100, 64,
    "A flat hexagon drawn on paper: a closed figure with straight sides, like a floor tile.",
    "کاغذ پر بنا ہوا چپٹا مسدس: سیدھے اضلاع والی بند شکل، فرش کی ٹائل کی طرح۔",
    [poly(regular(6, C, 26, start=0), fill=True)])

lesson = practice_lesson(
 "9.1", script="exercise_9_1.py",
 title=T("Exercise 9.1 practice: 2-D and 3-D shapes", "مشق 9.1 کی پریکٹس: 2-D اور 3-D اشکال"),
 outcome="Name the 3-D shape of everyday objects, tell 1-D, 2-D and 3-D figures apart, and count the faces, edges and vertices of solids.",
 prerequisites=[SO_PARTS, SY_SHAPES],
 misconceptions=[
   {"id": "flat_is_3d", "description": "Calls a flat figure drawn on paper a 3-D shape, or a round flat figure a sphere."},
   {"id": "curved_not_a_face", "description": "Does not count a curved surface as a face, so gives a cylinder 2 faces and a cone 1."},
   {"id": "edge_vertex_mix", "description": "Mixes up edges and vertices, for example counts the edge of a cone's base as a vertex."},
   {"id": "hidden_edges", "description": "Counts only the edges that can be seen in the picture and skips the hidden ones."},
   {"id": "shape_by_roundness", "description": "Names a solid from one feature, such as being round, and mixes up cylinder, cone and sphere."},
   {"id": "wrong_count_unit", "description": "Counts faces when vertices are asked, or the other way round, or multiplies by the wrong number."},
 ],
 steps=[
   practice_intro("9.1",
     "Here you name the 3-D shape of everyday objects, tell flat figures from solids, and count faces, edges and vertices.",
     "اس میں آپ روزمرہ چیزوں کی 3-D شکل کا نام بتائیں گے، چپٹی اشکال اور ٹھوس اشکال میں فرق کریں گے، اور سطحیں، کنارے اور راس گنیں گے۔",
     "Exercise 9.1 is about shapes. Ready?", "مشق 9.1 اشکال کے بارے میں ہے۔ تیار؟"),
   ch("q1_tin", ("A tin of ghee has a flat round top, a flat round bottom and a curved side. Which solid is it shaped like?", "گھی کے ڈبے کا اوپر اور نیچے چپٹا گول ہے اور پہلو خمدار ہے۔ یہ کس ٹھوس شکل جیسا ہے؟"),
      ("Cylinder", "اسطوانہ", "Yes! Two flat circles joined by one curved surface make a cylinder.", "جی ہاں! دو چپٹے دائرے اور ایک خمدار سطح مل کر اسطوانہ بناتے ہیں۔"),
      [("Cone", "مخروط", "A cone comes to a point at the top. This tin has a flat top.", "مخروط اوپر سے نوک دار ہوتا ہے۔ اس ڈبے کا اوپر چپٹا ہے۔", "shape_by_roundness"),
       ("Sphere", "کرہ", "A sphere is round all over, with no flat part.", "کرہ ہر طرف سے گول ہوتا ہے، اس میں کوئی چپٹا حصہ نہیں۔", "shape_by_roundness"),
       ("Cuboid", "مکعب نما", "A cuboid has only flat faces. This tin has a curved side.", "مکعب نما کی سب سطحیں چپٹی ہوتی ہیں۔ اس ڈبے کا پہلو خمدار ہے۔", "shape_by_roundness")],
      1, qtype="recall"),
   ch("q2_sphere", ("Which of these things is shaped like a sphere?", "ان میں سے کون سی چیز کرہ جیسی ہے؟"),
      ("A marble", "کانچ کی گولی", "Yes! A marble is round all over, like a sphere.", "جی ہاں! کانچ کی گولی ہر طرف سے گول ہے، کرہ کی طرح۔"),
      [("A brick", "اینٹ", "A brick has flat faces and corners: it is a cuboid.", "اینٹ کی سطحیں چپٹی اور کونے ہوتے ہیں: یہ مکعب نما ہے۔", "shape_by_roundness"),
       ("A road safety cone", "سڑک کا حفاظتی مخروط", "That is a cone: pointed at the top, flat at the bottom.", "یہ مخروط ہے: اوپر سے نوک دار، نیچے سے چپٹا۔", "shape_by_roundness"),
       ("A sheet of paper", "کاغذ کا ورق", "A sheet of paper is a flat 2-D figure.", "کاغذ کا ورق چپٹی 2-D شکل ہے۔", "flat_is_3d")],
      2, qtype="recall"),
   ch("q3_dimensions", ("Which of these is a 1-D figure?", "ان میں سے کون سی 1-D شکل ہے؟"),
      ("A line segment", "قطعہ خط", "Yes! A line segment has only length.", "جی ہاں! قطعہ خط کی صرف لمبائی ہوتی ہے۔"),
      [("A square", "مربع", "A square is flat with length and width: 2-D.", "مربع چپٹا ہوتا ہے، لمبائی اور چوڑائی کے ساتھ: 2-D۔", "flat_is_3d"),
       ("A cube", "مکعب", "A cube is solid: length, width and height: 3-D.", "مکعب ٹھوس ہے: لمبائی، چوڑائی اور اونچائی: 3-D۔", "flat_is_3d"),
       ("A circle", "دائرہ", "A circle drawn on paper is flat: 2-D.", "کاغذ پر بنا دائرہ چپٹا ہے: 2-D۔", "flat_is_3d")],
      0, qtype="recall"),
   {"id": "s_idea", "type": "explain",
    "character": say("thinking", "Count the faces, edges and vertices of a solid one kind at a time.", "ٹھوس شکل کی سطحیں، کنارے اور راس ایک ایک قسم کر کے گنیں۔"),
    "text": T("A face is a flat or curved surface. An edge is a line where two faces meet (a circle counts too). A vertex is a corner point. Cube and cuboid: 6 faces, 12 edges, 8 vertices. Cylinder: 3 faces (2 flat, 1 curved), 2 edges, 0 vertices. Cone: 2 faces, 1 edge, 1 vertex. Sphere: 1 face, 0 edges, 0 vertices. Hemisphere: 2 faces, 1 edge, 0 vertices. Hidden edges at the back count too.",
              "سطح چپٹی یا خمدار ہو سکتی ہے۔ کنارہ وہ لکیر ہے جہاں دو سطحیں ملتی ہیں (دائرہ بھی کنارہ گنا جاتا ہے)۔ راس کونے کا نقطہ ہے۔ مکعب اور مکعب نما: 6 سطحیں، 12 کنارے، 8 راس۔ اسطوانہ: 3 سطحیں (2 چپٹی، 1 خمدار)، 2 کنارے، 0 راس۔ مخروط: 2 سطحیں، 1 کنارہ، 1 راس۔ کرہ: 1 سطح، 0 کنارے، 0 راس۔ نصف کرہ: 2 سطحیں، 1 کنارہ، 0 راس۔ پیچھے کے چھپے ہوئے کنارے بھی گنے جاتے ہیں۔")},
   with_fig(nq("q4_cyl_flat", ("How many flat faces does the cylinder in the picture have?", "تصویر والے اسطوانے کی کتنی چپٹی سطحیں ہیں؟"), Q4,
      ("Look at the top and the bottom.", "اوپر اور نیچے دیکھیں۔"),
      ("Right! The top and the bottom: 2 flat faces (and 1 curved face).", "درست! اوپر اور نیچے: 2 چپٹی سطحیں (اور 1 خمدار سطح)۔"), ("The two flat circles are the top and the bottom.", "دو چپٹے دائرے اوپر اور نیچے ہیں۔"),
      [(3, "3 is all the faces. The curved side is not flat, so 2 are flat.", "3 کل سطحیں ہیں۔ خمدار پہلو چپٹا نہیں، تو 2 چپٹی ہیں۔", "wrong_count_unit"),
       (1, "That counts only the curved side. The top and bottom are flat faces too: 2.", "یہ صرف خمدار پہلو گنتا ہے۔ اوپر اور نیچے بھی چپٹی سطحیں ہیں: 2", "curved_not_a_face")], qtype="recall"), F_CYL),
   with_fig(nq("q5_cone_vertex", ("How many vertices (corners) does the cone in the picture have?", "تصویر والے مخروط کے کتنے راس (کونے) ہیں؟"), Q5,
      ("A vertex is a sharp point. Where is the cone sharp?", "راس نوک دار نقطہ ہوتا ہے۔ مخروط کہاں نوک دار ہے؟"),
      ("Right! Only the tip at the top is a vertex.", "درست! صرف اوپر کی نوک راس ہے۔"), ("The round edge of the base is smooth, with no sharp point. Only the tip counts.", "قاعدے کا گول کنارہ ہموار ہے، اس میں نوک دار نقطہ نہیں۔ صرف اوپر کی نوک گنی جاتی ہے۔"),
      [(2, "The edge of the base is a curved edge, not a vertex. Only the tip is a vertex: 1.", "قاعدے کا کنارہ خمدار کنارہ ہے، راس نہیں۔ صرف نوک راس ہے: 1", "edge_vertex_mix"),
       (0, "The tip at the top is a vertex: 1.", "اوپر کی نوک راس ہے: 1", "edge_vertex_mix")], qtype="recall"), F_CONE),
   with_fig(nq("q6_cone_faces", ("How many faces does the same cone have, counting the curved side?", "اسی مخروط کی کتنی سطحیں ہیں، خمدار پہلو سمیت؟"), Q6,
      ("One flat base and one curved side.", "ایک چپٹا قاعدہ اور ایک خمدار پہلو۔"),
      ("Right! 1 flat base + 1 curved surface = 2 faces.", "درست! 1 چپٹا قاعدہ + 1 خمدار سطح = 2 سطحیں"), ("The base is 1 face and the curved side is 1 face: 2.", "قاعدہ 1 سطح ہے اور خمدار پہلو 1 سطح: 2"),
      [(1, "That counts only the flat base. A curved surface is a face too: 2.", "یہ صرف چپٹا قاعدہ گنتا ہے۔ خمدار سطح بھی سطح ہے: 2", "curved_not_a_face"),
       (3, "A cone has just one flat base and one curved side: 2.", "مخروط کا صرف ایک چپٹا قاعدہ اور ایک خمدار پہلو ہوتا ہے: 2", "wrong_count_unit")], qtype="recall"), F_CONE),
   with_fig(nq("q7_matchbox_edges", ("How many edges does a matchbox have in all, counting the hidden ones?", "ماچس کی ڈبیا کے کل کتنے کنارے ہیں، چھپے ہوئے بھی گن کر؟"), Q7,
      ("4 round the top, 4 round the bottom, 4 standing up.", "4 اوپر کے گرد، 4 نیچے کے گرد، 4 کھڑے۔"),
      ("Right! 4 + 4 + 4 = 12 edges.", "درست! 4 + 4 + 4 = 12 کنارے"), ("Top 4, bottom 4, and 4 going up: 12.", "اوپر 4، نیچے 4، اور 4 اوپر جاتے ہوئے: 12"),
      [(9, "That counts only the 9 edges you can see. The 3 dashed ones count too: 12.", "یہ صرف 9 نظر آنے والے کنارے گنتا ہے۔ 3 ڈیش والے بھی گنے جاتے ہیں: 12", "hidden_edges"),
       (8, "8 is the number of vertices (corners). Edges are the lines: 12.", "8 راس (کونوں) کی تعداد ہے۔ کنارے لکیریں ہیں: 12", "edge_vertex_mix"),
       (6, "6 is the number of faces. Edges are the lines: 12.", "6 سطحوں کی تعداد ہے۔ کنارے لکیریں ہیں: 12", "wrong_count_unit")]), F_MATCH),
   with_fig(nq("q8_hexagon", ("How many sides does the flat figure in the picture have?", "تصویر والی چپٹی شکل کے کتنے اضلاع ہیں؟"), Q8,
      ("Go round the shape and count the straight sides.", "شکل کے گرد چل کر سیدھے اضلاع گنیں۔"),
      ("Right! It is a hexagon, with 6 sides.", "درست! یہ مسدس ہے، اس کے 6 اضلاع ہیں۔"), ("Count each straight side once: 6.", "ہر سیدھے ضلع کو ایک بار گنیں: 6"),
      [(5, "That misses one side. Count again: 6.", "ایک ضلع رہ گیا۔ دوبارہ گنیں: 6", "wrong_count_unit"),
       (8, "Too many. A hexagon has 6 sides.", "بہت زیادہ۔ مسدس کے 6 اضلاع ہوتے ہیں۔", "wrong_count_unit")], qtype="recall"), F_HEX),
   nq("q9_dice", ("A shop has 4 dice (cubes) on a shelf, not touching. How many vertices (corners) do they have altogether?", "ایک دکان میں شیلف پر 4 پانسے (مکعب) الگ الگ رکھے ہیں۔ ان کے کل کتنے راس (کونے) ہیں؟"), Q9,
      ("One cube has 8 vertices. Multiply by 4.", "ایک مکعب کے 8 راس ہوتے ہیں۔ 4 سے ضرب دیں۔"),
      ("Right! 4 × 8 = 32 vertices.", "درست! 4 × 8 = 32 راس"), ("Each die has 8 corners, and 4 × 8 = 32.", "ہر پانسے کے 8 کونے ہیں، اور 4 × 8 = 32"),
      [(24, "That is the faces, 4 × 6. Vertices: 4 × 8 = 32.", "یہ سطحیں ہیں، 4 × 6۔ راس: 4 × 8 = 32", "wrong_count_unit"),
       (8, "That is the vertices of one die. There are 4 dice: 32.", "یہ ایک پانسے کے راس ہیں۔ پانسے 4 ہیں: 32", "wrong_count_unit")]),
   nq("q10_wire", ("A wire frame of a cuboid is made along all its 12 edges. The cuboid is 6 cm long, 4 cm wide and 3 cm high. What length of wire is needed, in cm?", "مکعب نما کا تار کا ڈھانچہ اس کے سب 12 کناروں پر بنایا جاتا ہے۔ مکعب نما 6 سینٹی میٹر لمبا، 4 سینٹی میٹر چوڑا اور 3 سینٹی میٹر اونچا ہے۔ کتنے سینٹی میٹر تار چاہیے؟"), Q10,
      ("There are 4 edges of each length: 4 × (6 + 4 + 3).", "ہر لمبائی کے 4 کنارے ہیں: 4 × (6 + 4 + 3)"),
      ("Right! 4 × 13 = 52 cm of wire.", "درست! 4 × 13 = 52 سینٹی میٹر تار"), ("6 + 4 + 3 = 13, and there are 4 of each: 4 × 13 = 52.", "6 + 4 + 3 = 13، اور ہر ایک کے 4 ہیں: 4 × 13 = 52"),
      [(26, "That counts each length only twice. There are 4 edges of each length: 52.", "یہ ہر لمبائی صرف دو بار گنتا ہے۔ ہر لمبائی کے 4 کنارے ہیں: 52", "hidden_edges"),
       (13, "That is one of each. Multiply by 4: 52.", "یہ ہر ایک کا ایک ایک ہے۔ 4 سے ضرب دیں: 52", "hidden_edges"),
       (72, "That is the volume, 6 × 4 × 3. Wire goes along the edges: 52.", "یہ حجم ہے، 6 × 4 × 3۔ تار کناروں پر لگتا ہے: 52", "wrong_count_unit")]),
   ch("q11_find_error", ("Hamza says a hemisphere (half a ball) has no flat face, because a ball is round. What went wrong?", "حمزہ کہتا ہے نصف کرہ (آدھی گیند) کی کوئی چپٹی سطح نہیں، کیونکہ گیند گول ہوتی ہے۔ کیا غلطی ہوئی؟"),
      ("Cutting the ball makes a flat circle, so a hemisphere has 1 flat and 1 curved face: 2 faces.", "گیند کاٹنے سے چپٹا دائرہ بنتا ہے، تو نصف کرہ کی 1 چپٹی اور 1 خمدار سطح ہے: کل 2 سطحیں۔", "Yes! The cut makes a flat circle.", "جی ہاں! کاٹنے سے چپٹا دائرہ بنتا ہے۔"),
      [("Nothing. A hemisphere has only 1 curved face.", "کوئی غلطی نہیں۔ نصف کرہ کی صرف 1 خمدار سطح ہے۔", "The cut side is flat, so there is a second face.", "کٹا ہوا رخ چپٹا ہے، تو ایک اور سطح ہے۔", "curved_not_a_face"),
       ("A hemisphere has 3 flat faces.", "نصف کرہ کی 3 چپٹی سطحیں ہیں۔", "It has just one flat circle.", "اس کا صرف ایک چپٹا دائرہ ہے۔", "shape_by_roundness")],
      0, qtype="find_error"),
   ch("q12_find_error_cone", ("Mina says a cone has 2 vertices: the tip, and the round edge of its base. What went wrong?", "مینا کہتی ہے مخروط کے 2 راس ہیں: نوک، اور قاعدے کا گول کنارہ۔ کیا غلطی ہوئی؟"),
      ("The round edge of the base is an edge, not a vertex. A cone has 1 vertex, the tip.", "قاعدے کا گول کنارہ کنارہ ہے، راس نہیں۔ مخروط کا 1 راس ہے، یعنی نوک۔", "Yes! A vertex is a sharp corner point.", "جی ہاں! راس نوک دار کونے کا نقطہ ہوتا ہے۔"),
      [("Nothing. A cone has 2 vertices.", "کوئی غلطی نہیں۔ مخروط کے 2 راس ہیں۔", "A smooth round edge has no sharp point to count.", "ہموار گول کنارے میں گننے کے لیے نوک دار نقطہ نہیں ہوتا۔", "edge_vertex_mix"),
       ("A cone has no vertices.", "مخروط کا کوئی راس نہیں۔", "The tip is a vertex.", "نوک راس ہے۔", "edge_vertex_mix")],
      1, qtype="find_error"),
   ch("q13_which_solid", ("Which solid has exactly 1 edge and 1 vertex?", "کس ٹھوس شکل کا بالکل 1 کنارہ اور 1 راس ہے؟"),
      ("Cone", "مخروط", "Yes! The base circle is its 1 edge and the tip is its 1 vertex.", "جی ہاں! قاعدے کا دائرہ اس کا 1 کنارہ اور نوک اس کا 1 راس ہے۔"),
      [("Cylinder", "اسطوانہ", "A cylinder has 2 edges and no vertex.", "اسطوانے کے 2 کنارے ہیں اور کوئی راس نہیں۔", "edge_vertex_mix"),
       ("Hemisphere", "نصف کرہ", "A hemisphere has 1 edge but no vertex.", "نصف کرہ کا 1 کنارہ ہے مگر کوئی راس نہیں۔", "edge_vertex_mix"),
       ("Sphere", "کرہ", "A sphere has no edges and no vertices.", "کرہ کے نہ کنارے ہیں نہ راس۔", "edge_vertex_mix")],
      2),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can name solids and count their parts.", "شاباش! آپ ٹھوس اشکال کے نام بتا سکتے ہیں اور ان کے حصے گن سکتے ہیں۔"),
    "text": T("1-D: only length (a line segment). 2-D: flat, with length and width (square, circle, hexagon). 3-D: solid, with length, width and height. Cube and cuboid: 6 faces, 12 edges, 8 vertices. Cylinder: 3 faces, 2 edges, 0 vertices. Cone: 2 faces, 1 edge, 1 vertex. Sphere: 1 face, 0 edges, 0 vertices. Hemisphere: 2 faces, 1 edge, 0 vertices. Count the hidden edges too.",
              "1-D: صرف لمبائی (قطعہ خط)۔ 2-D: چپٹی، لمبائی اور چوڑائی کے ساتھ (مربع، دائرہ، مسدس)۔ 3-D: ٹھوس، لمبائی، چوڑائی اور اونچائی کے ساتھ۔ مکعب اور مکعب نما: 6 سطحیں، 12 کنارے، 8 راس۔ اسطوانہ: 3 سطحیں، 2 کنارے، 0 راس۔ مخروط: 2 سطحیں، 1 کنارہ، 1 راس۔ کرہ: 1 سطح، 0 کنارے، 0 راس۔ نصف کرہ: 2 سطحیں، 1 کنارہ، 0 راس۔ چھپے ہوئے کنارے بھی گنیں۔"),
    "points": [T("Curved surfaces are faces too.", "خمدار سطحیں بھی سطحیں ہیں۔"),
               T("A vertex is a sharp point; a round rim is an edge.", "راس نوک دار نقطہ ہے؛ گول کنارہ کنارہ ہے۔")]},
 ],
 bank=[
   {"id": "qb_sphere_faces", "type": "recall", "step": nq("qb_sphere_faces", ("How many faces does a sphere have?", "کرہ کی کتنی سطحیں ہیں؟"), QB1,
      ("One curved surface all round.", "ہر طرف ایک خمدار سطح۔"),
      ("Right! A sphere has 1 curved face.", "درست! کرہ کی 1 خمدار سطح ہے۔"), ("It is one smooth surface: 1.", "یہ ایک ہموار سطح ہے: 1"),
      [(0, "A curved surface counts as a face: 1.", "خمدار سطح بھی سطح گنی جاتی ہے: 1", "curved_not_a_face")], qtype=None)},
   {"id": "qb_cyl_edges", "type": "recall", "step": nq("qb_cyl_edges", ("How many edges does a cylinder have?", "اسطوانے کے کتنے کنارے ہیں؟"), QB2,
      ("Where the flat circles meet the curved side.", "جہاں چپٹے دائرے خمدار پہلو سے ملتے ہیں۔"),
      ("Right! The top rim and the bottom rim: 2 edges.", "درست! اوپر کا گھیرا اور نیچے کا گھیرا: 2 کنارے"), ("One circle on top and one at the bottom: 2.", "ایک دائرہ اوپر اور ایک نیچے: 2"),
      [(3, "3 is the number of faces. The edges are the 2 circles: 2.", "3 سطحوں کی تعداد ہے۔ کنارے 2 دائرے ہیں: 2", "wrong_count_unit")], qtype=None)},
   {"id": "qb_cube_faces", "type": "apply", "step": nq("qb_cube_faces", ("Two dice (cubes) are on a table, not touching. How many faces do they have altogether?", "میز پر دو پانسے (مکعب) الگ الگ رکھے ہیں۔ ان کی کل کتنی سطحیں ہیں؟"), QB3,
      ("One cube has 6 faces. Two cubes: 2 × 6.", "ایک مکعب کی 6 سطحیں ہیں۔ دو مکعب: 2 × 6"),
      ("Right! 2 × 6 = 12 faces.", "درست! 2 × 6 = 12 سطحیں"), ("6 faces on each die: 12.", "ہر پانسے کی 6 سطحیں: 12"),
      [(6, "That is one die. There are 2: 12.", "یہ ایک پانسہ ہے۔ پانسے 2 ہیں: 12", "wrong_count_unit"),
       (16, "16 is the vertices of 2 dice. Faces: 12.", "16، دو پانسوں کے راس ہیں۔ سطحیں: 12", "wrong_count_unit")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error", ("Sana says a sphere has 1 edge, because it is round all over. What went wrong?", "ثنا کہتی ہے کرہ کا 1 کنارہ ہے، کیونکہ وہ ہر طرف سے گول ہے۔ کیا غلطی ہوئی؟"),
      ("A sphere is one smooth surface with no line where two faces meet, so it has 0 edges.", "کرہ ایک ہموار سطح ہے جس میں دو سطحوں کے ملنے کی کوئی لکیر نہیں، تو اس کے 0 کنارے ہیں۔", "Yes! An edge needs two faces to meet.", "جی ہاں! کنارے کے لیے دو سطحوں کا ملنا ضروری ہے۔"),
      [("Nothing. A sphere has 1 edge all round the middle.", "کوئی غلطی نہیں۔ کرہ کے بیچ میں گرد 1 کنارہ ہے۔", "The middle is not an edge: nothing meets there.", "بیچ کا حصہ کنارہ نہیں: وہاں کچھ نہیں ملتا۔", "edge_vertex_mix"),
       ("A sphere has 2 edges, one on top and one at the bottom.", "کرہ کے 2 کنارے ہیں، ایک اوپر ایک نیچے۔", "A sphere has no top or bottom edge.", "کرہ کا اوپر یا نیچے کوئی کنارہ نہیں۔", "edge_vertex_mix")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_cuboid_vertices", "type": "apply", "step": nq("r_cuboid_vertices", ("Two matchboxes (cuboids) lie apart on a shelf. How many vertices (corners) do they have altogether?", "الماری میں دو ماچس کی ڈبیاں (مکعب نما) الگ الگ رکھی ہیں۔ ان کے کل کتنے راس (کونے) ہیں؟"), R1,
      ("One cuboid has 8 vertices. Two cuboids: 2 × 8.", "ایک مکعب نما کے 8 راس ہیں۔ دو مکعب نما: 2 × 8"),
      ("Right! 2 × 8 = 16 vertices.", "درست! 2 × 8 = 16 راس"), ("Each matchbox has 8 corners: 16.", "ہر ڈبیا کے 8 کونے ہیں: 16"),
      [(8, "That is one matchbox. There are 2: 16.", "یہ ایک ڈبیا ہے۔ ڈبیاں 2 ہیں: 16", "wrong_count_unit"),
       (24, "24 is the edges of 2 matchboxes. Vertices: 16.", "24، دو ڈبیوں کے کنارے ہیں۔ راس: 16", "edge_vertex_mix")], qtype=None)},
   {"id": "r_hemisphere_faces", "type": "recall", "step": nq("r_hemisphere_faces", ("How many faces does a hemisphere have?", "نصف کرہ کی کتنی سطحیں ہیں؟"), R2,
      ("One flat circle and one curved surface.", "ایک چپٹا دائرہ اور ایک خمدار سطح۔"),
      ("Right! 1 flat + 1 curved = 2 faces.", "درست! 1 چپٹی + 1 خمدار = 2 سطحیں"), ("The flat circle and the curved bowl: 2.", "چپٹا دائرہ اور خمدار پیالہ: 2"),
      [(1, "That misses the flat circle. A hemisphere has 2 faces.", "یہ چپٹا دائرہ چھوڑ دیتا ہے۔ نصف کرہ کی 2 سطحیں ہیں۔", "curved_not_a_face")], qtype=None)},
 ],
 glossary=[T("Face", "سطح"), T("Edge", "کنارہ"), T("Vertex", "راس"), T("Cylinder", "اسطوانہ"), T("Cone", "مخروط"),
           T("Sphere", "کرہ"), T("Hemisphere", "نصف کرہ"), T("Cuboid", "مکعب نما"), T("Curved surface", "خمدار سطح")],
 flashcards=[
   {"id": "f_cone", "front": T("Faces, edges and vertices of a cone?", "مخروط کی سطحیں، کنارے اور راس؟"),
    "back": T("2 faces (1 flat, 1 curved), 1 edge, 1 vertex.", "2 سطحیں (1 چپٹی، 1 خمدار)، 1 کنارہ، 1 راس۔")},
   {"id": "f_cuboid", "front": T("Faces, edges and vertices of a cuboid?", "مکعب نما کی سطحیں، کنارے اور راس؟"),
    "back": T("6 faces, 12 edges, 8 vertices.", "6 سطحیں، 12 کنارے، 8 راس۔")},
 ],
 home_task={"id": "h_objects", "text": T(
   "Find six things at home, such as a tin, a ball, a brick, a cap or a dice. Write the name of each one's 3-D shape. For two of them, count the faces, edges and vertices.",
   "گھر میں چھ چیزیں ڈھونڈیں، جیسے ڈبہ، گیند، اینٹ، ٹوپی یا پانسہ۔ ہر ایک کی 3-D شکل کا نام لکھیں۔ دو چیزوں کی سطحیں، کنارے اور راس گنیں۔")},
 notes=["Covers naming the 3-D shape of objects (q1, q2), 1-D, 2-D and 3-D figures (q3, q8), faces, edges and vertices of a cylinder, cone, cuboid, cube and hemisphere (q4 to q7, q11 to q13) and two word problems built on them (q9, q10).",
        "Each wrong answer is a real mistake: a curved surface not counted as a face, the base rim of a cone counted as a vertex, hidden edges skipped, faces counted for vertices, and a solid named from one feature such as roundness.",
        "Urdu terms to check: سطح (face), کنارہ (edge), راس (vertex), اسطوانہ, مخروط, کرہ, نصف کرہ, مکعب نما, خمدار سطح and مسدس (hexagon), all as in the existing Symmetry and Solids lessons. کانچ کی گولی (marble) and سڑک کا حفاظتی مخروط (road safety cone) are new, so a teacher should confirm them."],
 minutes=16,
)

write(lesson)

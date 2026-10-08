import math

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SO_PARTS, SY_SHAPES)

SKILL = SY_SHAPES

# Surfaces, edges and vertices of the solids in this lesson.
# Curved surfaces count as surfaces; an edge is where two surfaces meet;
# a vertex is a point where edges meet (or the tip of a cone).
SOLIDS = {
    "cube": (6, 12, 8),
    "cuboid": (6, 12, 8),
    "cylinder": (3, 2, 0),
    "cone": (2, 1, 1),
    "sphere": (1, 0, 0),
    "hemisphere": (2, 1, 0),
}
FACES, EDGES, VERTS = 0, 1, 2

# Polygons: sides = vertices.
HOUSE = 5      # square with a triangle roof, outline only
KITE = 4       # rooftop kite (patang) outline
HEXAGON = 6


def r(v):
    return round(v, 1)


def ellipse_pts(cx, cy, rx, ry, a0=0, a1=360, n=24):
    """Points on an ellipse, angles in degrees, y down (0..180 is the front/lower half)."""
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append([r(cx + rx * math.cos(a)), r(cy + ry * math.sin(a))])
    return pts


def segments(pts, dashed=False):
    items = []
    for p, q in zip(pts, pts[1:]):
        it = {"kind": "line", "from": p, "to": q}
        if dashed:
            it["style"] = "dashed"
        items.append(it)
    return items


def regular(cx, cy, rad, n, start=-90):
    return [[r(cx + rad * math.cos(math.radians(start + 360 * k / n))),
             r(cy + rad * math.sin(math.radians(start + 360 * k / n)))] for k in range(n)]


def cuboid_items(x, y, w, h, dx, dy):
    """Front rectangle at (x, y), back rectangle shifted by (dx, -dy); hidden edges dashed."""
    f = [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]
    b = [[r(px + dx), r(py - dy)] for px, py in f]
    items = [{"kind": "polygon", "points": f}]
    items += [{"kind": "line", "from": b[0], "to": b[1]},
              {"kind": "line", "from": b[1], "to": b[2]}]
    items += [{"kind": "line", "from": b[2], "to": b[3], "style": "dashed"},
              {"kind": "line", "from": b[3], "to": b[0], "style": "dashed"}]
    items += [{"kind": "line", "from": f[0], "to": b[0]},
              {"kind": "line", "from": f[1], "to": b[1]},
              {"kind": "line", "from": f[2], "to": b[2]},
              {"kind": "line", "from": f[3], "to": b[3], "style": "dashed"}]
    return items


def cylinder_items(cx, top, bottom, rx, ry):
    items = [{"kind": "polygon", "points": ellipse_pts(cx, top, rx, ry)[:-1]}]
    items += [{"kind": "line", "from": [r(cx - rx), top], "to": [r(cx - rx), bottom]},
              {"kind": "line", "from": [r(cx + rx), top], "to": [r(cx + rx), bottom]}]
    items += segments(ellipse_pts(cx, bottom, rx, ry, 0, 180, 8))
    items += segments(ellipse_pts(cx, bottom, rx, ry, 180, 360, 8), dashed=True)
    return items


def cone_items(cx, apex_y, base_y, rx, ry):
    items = [{"kind": "line", "from": [cx, apex_y], "to": [r(cx - rx), base_y]},
             {"kind": "line", "from": [cx, apex_y], "to": [r(cx + rx), base_y]},
             {"kind": "point", "at": [cx, apex_y]}]
    items += segments(ellipse_pts(cx, base_y, rx, ry, 0, 180, 8))
    items += segments(ellipse_pts(cx, base_y, rx, ry, 180, 360, 8), dashed=True)
    return items


def hemisphere_items(cx, base_y, rad, ry):
    items = [{"kind": "arc", "center": [cx, base_y], "radius": rad, "start": 180, "sweep": 180}]
    items += segments(ellipse_pts(cx, base_y, rad, ry, 0, 180, 8))
    items += segments(ellipse_pts(cx, base_y, rad, ry, 180, 360, 8), dashed=True)
    return items


def with_figure(step, figure):
    step["figure"] = figure
    return step


# --- numbers, worked out and checked ---
S2 = SOLIDS["cube"][FACES]
assert S2 == 6 and SOLIDS["cube"][EDGES] == 12 and SOLIDS["cube"][VERTS] == 8
S5 = HOUSE
assert S5 == 5 and S5 + 1 == 6 and S5 - 1 == 4     # 6 counts the dashed guide; 4 counts only the square
S6 = SOLIDS["cylinder"][EDGES]
assert S6 == 2 and SOLIDS["cylinder"][FACES] == 3
S7 = SOLIDS["cone"][VERTS]
assert S7 == 1 and SOLIDS["cone"][EDGES] == 1 and SOLIDS["cone"][FACES] == 2
S8 = SOLIDS["cylinder"][FACES]
flat_only = S8 - 1
assert S8 == 3 and flat_only == 2
S11 = SOLIDS["hemisphere"][FACES]
assert S11 == 2 and S11 - 1 == 1 and SOLIDS["hemisphere"][VERTS] == 0
QB = SOLIDS["cone"][EDGES]
assert QB == 1
R1 = KITE
assert R1 == 4 and R1 * 2 == 8
assert SOLIDS["sphere"][VERTS] == 0 and SOLIDS["sphere"][EDGES] == 0


# --- figures ---
FIG_HOOK = {
  "width": 120, "height": 70,
  "alt": T("Three things: a straight kite string drawn as a line from A to B, a kite drawn flat as a four-sided shape, and a cricket ball drawn as a round ball.",
           "تین چیزیں: پتنگ کی تنی ہوئی ڈور A سے B تک ایک لکیر، پتنگ چار اضلاع والی چپٹی شکل، اور کرکٹ کی گیند ایک گول گیند۔"),
  "items": [
    {"kind": "line", "from": [6, 60], "to": [34, 12]},
    {"kind": "point", "at": [6, 60]}, {"kind": "point", "at": [34, 12]},
    {"kind": "label", "at": [10, 66], "text": "A"}, {"kind": "label", "at": [30, 6], "text": "B"},
    {"kind": "polygon", "points": [[62, 8], [76, 30], [62, 62], [48, 30]], "fill": True},
    {"kind": "circle", "center": [100, 36], "radius": 14, "fill": True},
  ] + segments(ellipse_pts(100, 36, 14, 4, 0, 180, 10)),
}

FIG_TYPES = {
  "width": 150, "height": 64,
  "alt": T("Three shapes side by side. Left, labelled 1-D: a line segment AB, which has only length. Middle, labelled 2-D: a flat triangle, which has length and breadth. Right, labelled 3-D: a cuboid drawn as a front rectangle joined to a back rectangle; the hidden edges at the back are dashed. It has length, breadth and height.",
           "تین اشکال ساتھ ساتھ۔ بائیں، 1-D: قطعہ خط AB، جس کی صرف لمبائی ہے۔ درمیان، 2-D: چپٹی مثلث، جس کی لمبائی اور چوڑائی ہے۔ دائیں، 3-D: مکعب نما، آگے کا مستطیل پیچھے کے مستطیل سے جڑا ہوا؛ پیچھے کے چھپے کنارے نقطہ دار ہیں۔ اس کی لمبائی، چوڑائی اور اونچائی ہے۔"),
  "items": [
    {"kind": "line", "from": [6, 30], "to": [40, 30]},
    {"kind": "point", "at": [6, 30]}, {"kind": "point", "at": [40, 30]},
    {"kind": "label", "at": [6, 22], "text": "A"}, {"kind": "label", "at": [40, 22], "text": "B"},
    {"kind": "label", "at": [23, 56], "text": "1-D"},
    {"kind": "polygon", "points": [[55, 44], [90, 44], [70, 12]], "fill": True},
    {"kind": "label", "at": [72, 56], "text": "2-D"},
  ] + cuboid_items(104, 20, 28, 24, 12, 10) + [
    {"kind": "label", "at": [124, 56], "text": "3-D"},
  ],
}

FIG_HOUSE = {
  "width": 80, "height": 76,
  "alt": T("A flat house shape: a square with a triangle roof on top, drawn as one outline. A dashed guide line shows where the square and the roof meet; it is not a side of the shape.",
           "ایک چپٹی گھر جیسی شکل: مربع جس کے اوپر مثلث چھت ہے، ایک ہی بیرونی خاکے میں۔ ایک نقطہ دار رہنما لکیر دکھاتی ہے کہ مربع اور چھت کہاں ملتے ہیں؛ یہ شکل کا ضلع نہیں۔"),
  "items": [
    {"kind": "polygon", "points": [[16, 70], [64, 70], [64, 34], [40, 8], [16, 34]], "fill": True},
    {"kind": "line", "from": [16, 34], "to": [64, 34], "style": "dashed"},
  ],
}
assert len(FIG_HOUSE["items"][0]["points"]) == HOUSE

FIG_CYL = {
  "width": 70, "height": 80,
  "alt": T("A cylinder standing up, like a ghee tin. The top is a flat circle drawn as an oval. Two straight side lines go down to the bottom circle. The back half of the bottom circle is dashed because it is hidden.",
           "کھڑا ہوا اسطوانہ، گھی کے ڈبے کی طرح۔ اوپر چپٹا دائرہ بیضوی شکل میں بنا ہے۔ دو سیدھی لکیریں نیچے والے دائرے تک جاتی ہیں۔ نیچے والے دائرے کا پچھلا آدھا حصہ چھپا ہے اس لیے نقطہ دار ہے۔"),
  "items": cylinder_items(35, 14, 66, 24, 7),
}

FIG_CONE = {
  "width": 70, "height": 80,
  "alt": T("A cone, like an ice-cream cone turned upside down. It has a pointed tip at the top marked with a dot, two straight slanting lines going down, and a round base drawn as an oval with its hidden back half dashed.",
           "مخروط، الٹی رکھی آئس کریم کون کی طرح۔ اوپر نوکیلی چوٹی پر نقطہ ہے، دو ترچھی سیدھی لکیریں نیچے آتی ہیں، اور گول قاعدہ بیضوی شکل میں ہے جس کا چھپا پچھلا آدھا حصہ نقطہ دار ہے۔"),
  "items": cone_items(35, 8, 64, 24, 7),
}

FIG_CIRCLE = {
  "width": 80, "height": 60,
  "alt": T("A circle drawn in a notebook, shaded in. It is flat on the page.",
           "کاپی میں بنا ہوا ایک دائرہ، اندر سے رنگا ہوا۔ یہ صفحے پر چپٹا ہے۔"),
  "items": [
    {"kind": "polygon", "points": [[4, 6], [76, 6], [76, 54], [4, 54]]},
    {"kind": "circle", "center": [40, 30], "radius": 16, "fill": True},
  ],
}

FIG_HEMI = {
  "width": 80, "height": 74,
  "alt": T("Half a ball (a hemisphere) resting on its flat side: a curved dome on top and a flat round base drawn as an oval, with the hidden back half of the base dashed.",
           "آدھی گیند (نصف کرہ) اپنی چپٹی طرف پر رکھی ہے: اوپر خمدار گنبد اور نیچے چپٹا گول قاعدہ بیضوی شکل میں، جس کا چھپا پچھلا آدھا حصہ نقطہ دار ہے۔"),
  "items": hemisphere_items(40, 40, 28, 8),
}

FIG_KITE = {
  "width": 70, "height": 80,
  "alt": T("A rooftop kite (patang) drawn flat: a four-sided shape, wide in the middle and pointed at the top and bottom, with a dot at each corner.",
           "چھت پر اڑنے والی پتنگ چپٹی بنی ہے: چار اضلاع والی شکل، درمیان سے چوڑی اور اوپر نیچے سے نوکیلی، ہر کونے پر نقطہ۔"),
  "items": [{"kind": "polygon", "points": [[35, 6], [60, 30], [35, 74], [10, 30]], "fill": True}]
           + [{"kind": "point", "at": p} for p in [[35, 6], [60, 30], [35, 74], [10, 30]]],
}
assert len(FIG_KITE["items"][0]["points"]) == KITE

FIG_SOLIDS = {
  "width": 150, "height": 64,
  "alt": T("Three solids side by side: a cylinder with a flat circle on top and bottom, a cone with a pointed tip, and a cube drawn as two squares joined at the corners with hidden edges dashed.",
           "تین ٹھوس اشکال ساتھ ساتھ: اسطوانہ جس کے اوپر اور نیچے چپٹے دائرے ہیں، نوکیلی چوٹی والا مخروط، اور مکعب جو کونوں سے جڑے دو مربعوں کی شکل میں ہے، چھپے کنارے نقطہ دار۔"),
  "items": cylinder_items(22, 12, 52, 16, 5) + cone_items(70, 8, 52, 16, 5) + cuboid_items(104, 24, 26, 26, 12, 10),
}


lesson = {
 "id": "g6-maths-18-1d-2d-3d-shapes",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Tell 1-D, 2-D and 3-D shapes apart by their dimensions, and describe 2-D shapes by their sides and vertices and 3-D shapes by their surfaces, edges and vertices.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("1-D, 2-D and 3-D shapes", "1-D، 2-D اور 3-D اشکال"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": SO_PARTS}],
 "misconceptions": [
   {"id": "flat_is_3d", "description": "Thinks a flat shape drawn on paper, such as a circle, is 3-D because it looks round like a ball."},
   {"id": "curved_surface", "description": "Treats curved surfaces like flat faces: leaves the curved surface out of the count, or gives a sphere or cylinder corners (vertices) like a cube."},
   {"id": "edge_vertex_mix", "description": "Confuses edges (lines where two surfaces meet) with vertices (corner points)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_dims", "type": "recall", "step": {
     "id": "qb_dims", "type": "choice",
     "prompt": T("A 3-D shape has which measurements?", "3-D شکل کی کون سی پیمائشیں ہوتی ہیں؟"),
     "options": [
       opt("lbh", "Length, breadth and height", "لمبائی، چوڑائی اور اونچائی", True,
           "Yes! Three dimensions, so it is 3-D.", "جی ہاں! تین ابعاد، اس لیے 3-D۔"),
       opt("lb", "Length and breadth only", "صرف لمبائی اور چوڑائی", False,
           "That is a flat 2-D shape. A 3-D shape also has height.", "یہ چپٹی 2-D شکل ہے۔ 3-D شکل کی اونچائی بھی ہوتی ہے۔", "flat_is_3d"),
       opt("l", "Length only", "صرف لمبائی", False,
           "Only length is 1-D, like a line segment.", "صرف لمبائی 1-D ہے، جیسے قطعہ خط۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("How many edges does a cone have?", "مخروط کے کتنے کنارے ہوتے ہیں؟"),
     QB,
     T("An edge is where two surfaces meet. Where does the curved surface meet the flat base?", "کنارہ وہاں ہوتا ہے جہاں دو سطحیں ملیں۔ خمدار سطح چپٹے قاعدے سے کہاں ملتی ہے؟"),
     T("Right! 1 curved edge round the base.", "درست! قاعدے کے گرد 1 خمدار کنارہ۔"),
     T("A cone has 1 edge: the circle where the curved surface meets the base.", "مخروط کا 1 کنارہ ہے: وہ دائرہ جہاں خمدار سطح قاعدے سے ملتی ہے۔"),
     common_wrong=[wrong(0, "A curved edge is still an edge. The circle round the base is 1 edge.", "خمدار کنارہ بھی کنارہ ہے۔ قاعدے کے گرد دائرہ 1 کنارہ ہے۔", "curved_surface"),
                   wrong(2, "The tip is a vertex, not an edge. A cone has 1 edge.", "چوٹی راس ہے، کنارہ نہیں۔ مخروط کا 1 کنارہ ہے۔", "edge_vertex_mix")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Bilal looks at a ludo dice (a cube) and says: \"It has 8 edges and 12 vertices.\" What went wrong?",
                 "بلال لوڈو کا پانسہ (مکعب) دیکھ کر کہتا ہے: \"اس کے 8 کنارے اور 12 راس ہیں۔\" کیا غلطی ہوئی؟"),
     "options": [
       opt("swap", "He swapped them: a cube has 12 edges and 8 vertices.", "اس نے الٹ دیا: مکعب کے 12 کنارے اور 8 راس ہیں۔", True,
           "Yes! Edges are the lines, vertices are the corner points.", "جی ہاں! کنارے لکیریں ہیں، راس کونے کے نقطے ہیں۔"),
       opt("faces", "A cube has 6 edges.", "مکعب کے 6 کنارے ہیں۔", False,
           "6 is the number of faces. A cube has 12 edges and 8 vertices.", "6 سطحوں کی تعداد ہے۔ مکعب کے 12 کنارے اور 8 راس ہیں۔"),
       opt("nothing", "Nothing, he is right.", "کوئی غلطی نہیں، وہ درست ہے۔", False,
           "Count the corners: 4 on top and 4 below makes 8 vertices. The 12 are edges.", "کونے گنیں: 4 اوپر اور 4 نیچے، 8 راس۔ 12 کنارے ہیں۔", "edge_vertex_mix"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_dims", "front": T("1-D, 2-D, 3-D: what does each have?", "1-D، 2-D، 3-D: ہر ایک کی کیا ہوتا ہے؟"),
    "back": T("1-D: length (a line segment). 2-D: length and breadth (a triangle). 3-D: length, breadth and height (a brick).",
              "1-D: لمبائی (قطعہ خط)۔ 2-D: لمبائی اور چوڑائی (مثلث)۔ 3-D: لمبائی، چوڑائی اور اونچائی (اینٹ)۔")},
   {"id": "f_curved", "front": T("Surfaces, edges, vertices of a cylinder and a cone?", "اسطوانہ اور مخروط کی سطحیں، کنارے، راس؟"),
    "back": T("Cylinder: 3 surfaces, 2 edges, 0 vertices. Cone: 2 surfaces, 1 edge, 1 vertex.",
              "اسطوانہ: 3 سطحیں، 2 کنارے، 0 راس۔ مخروط: 2 سطحیں، 1 کنارہ، 1 راس۔")},
 ],
 "home_tasks": [{"id": "h_sort", "text": T(
   "Find 6 things at home (a thread, a coin, a matchbox, a ball, a glass, a picture in a book) and sort them into 1-D, 2-D and 3-D. Then draw a cube: draw a square, draw a second square a little up and to the right, and join their corners with a ruler. Make the hidden edges dashed.",
   "گھر میں 6 چیزیں ڈھونڈیں (دھاگا، سکہ، ماچس کی ڈبیا، گیند، گلاس، کتاب کی کوئی تصویر) اور انہیں 1-D، 2-D اور 3-D میں بانٹیں۔ پھر مکعب بنائیں: ایک مربع بنائیں، اس سے تھوڑا اوپر اور دائیں دوسرا مربع بنائیں، اور فٹے سے ان کے کونے جوڑ دیں۔ چھپے کنارے نقطہ دار بنائیں۔")}],
 "glossary": [T("Dimension", "بُعد"), T("Line segment", "قطعہ خط"), T("Cylinder", "اسطوانہ"), T("Cone", "مخروط"),
              T("Sphere", "کرہ"), T("Hemisphere", "نصف کرہ"), T("Curved surface", "خمدار سطح"), T("Vertex", "راس")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A kite string, a kite and a cricket ball. One is a line, one is flat, one is solid. Can you tell which?",
                     "پتنگ کی ڈور، پتنگ اور کرکٹ کی گیند۔ ایک لکیر ہے، ایک چپٹی ہے، ایک ٹھوس ہے۔ بتا سکتے ہیں کون سی کیا ہے؟"),
    "figure": FIG_HOOK,
    "text": T("Today we sort shapes into 1-D, 2-D and 3-D, and count their sides, surfaces, edges and vertices. First, a quick check on solids.",
              "آج ہم اشکال کو 1-D، 2-D اور 3-D میں بانٹیں گے، اور ان کے اضلاع، سطحیں، کنارے اور راس گنیں گے۔ پہلے ٹھوس اشکال پر ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("A ludo dice is a cube. How many faces does it have?", "لوڈو کا پانسہ مکعب ہے۔ اس کی کتنی سطحیں ہیں؟"),
     S2,
     T("Top and bottom, front and back, left and right.", "اوپر اور نیچے، آگے اور پیچھے، دائیں اور بائیں۔"),
     T("Right! 6 faces, one for each number 1 to 6.", "درست! 6 سطحیں، 1 سے 6 تک ہر عدد کے لیے ایک۔"),
     T("A cube has 6 faces: top, bottom, front, back, left, right.", "مکعب کی 6 سطحیں ہیں: اوپر، نیچے، آگے، پیچھے، دائیں، بائیں۔"),
     common_wrong=[wrong(3, "You can see only 3 at once. Turn it over: there are 6.", "ایک وقت میں صرف 3 نظر آتی ہیں۔ پلٹ کر دیکھیں: 6 ہیں۔"),
                   wrong(8, "8 is the number of corners (vertices). Faces: 6.", "8 کونوں (راس) کی تعداد ہے۔ سطحیں: 6۔"),
                   wrong(12, "12 is the number of edges. Faces: 6.", "12 کناروں کی تعداد ہے۔ سطحیں: 6۔")],
     qtype="recall", skill=SO_PARTS),
   {"id": "s3_dimensions", "type": "explain",
    "character": say("happy", "Count the measurements: one for a line, two for flat, three for solid!", "پیمائشیں گنیں: لکیر کی ایک، چپٹی کی دو، ٹھوس کی تین!"),
    "figure": FIG_TYPES,
    "text": T("A 1-D (one-dimensional) shape has only length, like a line segment or a thread pulled tight. A 2-D shape is flat: it has length and breadth, like a triangle, square, rectangle or circle drawn on paper. We describe it by its sides and vertices (corners). A 3-D shape is a solid: it has length, breadth and height, like a cube, cuboid, cylinder, sphere, hemisphere or cone. We describe it by its surfaces, edges and vertices. Some surfaces are curved: a cylinder has 2 flat circles and 1 curved surface.",
              "1-D (یک بعدی) شکل کی صرف لمبائی ہوتی ہے، جیسے قطعہ خط یا تنا ہوا دھاگا۔ 2-D شکل چپٹی ہوتی ہے: اس کی لمبائی اور چوڑائی ہوتی ہے، جیسے کاغذ پر بنی مثلث، مربع، مستطیل یا دائرہ۔ ہم اسے اس کے اضلاع اور راس (کونوں) سے بیان کرتے ہیں۔ 3-D شکل ٹھوس ہوتی ہے: اس کی لمبائی، چوڑائی اور اونچائی ہوتی ہے، جیسے مکعب، مکعب نما، اسطوانہ، کرہ، نصف کرہ یا مخروط۔ ہم اسے اس کی سطحوں، کناروں اور راسوں سے بیان کرتے ہیں۔ کچھ سطحیں خمدار ہوتی ہیں: اسطوانے کے 2 چپٹے دائرے اور 1 خمدار سطح ہوتی ہے۔")},
   {"id": "s4_sort", "type": "choice", "question_type": "apply",
    "prompt": T("Which of these is a 3-D shape?", "ان میں سے کون سی 3-D شکل ہے؟"),
    "options": [
      opt("brick", "A brick", "ایک اینٹ", True,
          "Yes! A brick has length, breadth and height. It is a cuboid.", "جی ہاں! اینٹ کی لمبائی، چوڑائی اور اونچائی ہے۔ یہ مکعب نما ہے۔"),
      opt("circle", "A circle drawn on paper", "کاغذ پر بنا دائرہ", False,
          "A drawn circle is flat: length and breadth only. It is 2-D.", "بنا ہوا دائرہ چپٹا ہے: صرف لمبائی اور چوڑائی۔ یہ 2-D ہے۔", "flat_is_3d"),
      opt("thread", "A thread pulled tight", "تنا ہوا دھاگا", False,
          "A tight thread is like a line segment: length only. It is 1-D.", "تنا ہوا دھاگا قطعہ خط جیسا ہے: صرف لمبائی۔ یہ 1-D ہے۔"),
    ]},
   with_figure(number_question(
     "s5_sides",
     T("This flat house shape is drawn on paper. How many sides does it have? (The dashed line is only a guide.)",
       "یہ چپٹی گھر جیسی شکل کاغذ پر بنی ہے۔ اس کے کتنے اضلاع ہیں؟ (نقطہ دار لکیر صرف رہنما ہے۔)"),
     S5,
     T("Go round the outline and count each straight side once.", "باہر کے خاکے کے گرد چلیں اور ہر سیدھا ضلع ایک بار گنیں۔"),
     T("Right! 5 sides, and so 5 vertices too.", "درست! 5 اضلاع، اور اس لیے 5 راس بھی۔"),
     T("Bottom, two walls and two roof sides: 5 sides.", "نیچے، دو دیواریں اور چھت کے دو اضلاع: 5 اضلاع۔"),
     common_wrong=[wrong(6, "The dashed line is inside the shape, not a side. Count the outline: 5.", "نقطہ دار لکیر شکل کے اندر ہے، ضلع نہیں۔ خاکہ گنیں: 5۔"),
                   wrong(4, "Don't stop at the square: the roof adds 2 sides, not 1. Total 5.", "مربع پر نہ رکیں: چھت 2 اضلاع جوڑتی ہے۔ کل 5۔")]),
     FIG_HOUSE),
   with_figure(number_question(
     "s6_cyl_edges",
     T("A ghee tin is a cylinder. How many edges does it have?", "گھی کا ڈبہ اسطوانہ ہے۔ اس کے کتنے کنارے ہیں؟"),
     S6,
     T("An edge is where two surfaces meet. Look at the top and the bottom rims.", "کنارہ وہاں ہے جہاں دو سطحیں ملیں۔ اوپر اور نیچے کے کنارے دیکھیں۔"),
     T("Right! 2 curved edges: one round the top, one round the bottom.", "درست! 2 خمدار کنارے: ایک اوپر کے گرد، ایک نیچے کے گرد۔"),
     T("The curved side meets the top circle and the bottom circle: 2 edges.", "خمدار سطح اوپر والے اور نیچے والے دائرے سے ملتی ہے: 2 کنارے۔"),
     common_wrong=[wrong(0, "Curved edges still count. The top rim and bottom rim are 2 edges.", "خمدار کنارے بھی گنے جاتے ہیں۔ اوپر اور نیچے کے کنارے 2 ہیں۔", "curved_surface"),
                   wrong(3, "3 is the number of surfaces. Edges are where they meet: 2.", "3 سطحوں کی تعداد ہے۔ کنارے وہاں ہیں جہاں وہ ملیں: 2۔")]),
     FIG_CYL),
   with_figure(number_question(
     "s7_cone_vertex",
     T("An ice-cream cone is shaped like a cone. How many vertices does a cone have?", "آئس کریم کون مخروط جیسی ہے۔ مخروط کے کتنے راس ہوتے ہیں؟"),
     S7,
     T("A vertex is a sharp point. Look for the pointed tip.", "راس نوکیلا نقطہ ہے۔ نوکیلی چوٹی ڈھونڈیں۔"),
     T("Right! 1 vertex, the tip.", "درست! 1 راس، چوٹی۔"),
     T("The only sharp point is the tip: 1 vertex. The round base has an edge but no corners.", "واحد نوکیلا نقطہ چوٹی ہے: 1 راس۔ گول قاعدے کا کنارہ ہے لیکن کونے نہیں۔"),
     common_wrong=[wrong(0, "The pointed tip is a vertex: 1.", "نوکیلی چوٹی راس ہے: 1۔"),
                   wrong(2, "The circle round the base is an edge, not a vertex. Only the tip: 1.", "قاعدے کا دائرہ کنارہ ہے، راس نہیں۔ صرف چوٹی: 1۔", "edge_vertex_mix")]),
     FIG_CONE),
   with_figure(number_question(
     "s8_cyl_surfaces",
     T("Look at the cylinder again. How many surfaces does it have, flat and curved together?", "اسطوانہ پھر دیکھیں۔ اس کی کتنی سطحیں ہیں، چپٹی اور خمدار ملا کر؟"),
     S8,
     T("Top, bottom, and the part that wraps round.", "اوپر، نیچے، اور وہ حصہ جو گرد لپٹا ہے۔"),
     T("Right! 2 flat circles and 1 curved surface: 3.", "درست! 2 چپٹے دائرے اور 1 خمدار سطح: 3۔"),
     T("2 flat circles + 1 curved surface = 3 surfaces.", "2 چپٹے دائرے + 1 خمدار سطح = 3 سطحیں۔"),
     common_wrong=[wrong(flat_only, "That counts only the flat circles. Add the curved surface: 3.", "یہ صرف چپٹے دائرے ہیں۔ خمدار سطح جوڑیں: 3۔", "curved_surface"),
                   wrong(6, "A cylinder is not a cuboid. It has 2 flat circles and 1 curved surface: 3.", "اسطوانہ مکعب نما نہیں۔ اس کے 2 چپٹے دائرے اور 1 خمدار سطح ہے: 3۔", "curved_surface")]),
     FIG_CYL),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "figure": FIG_CIRCLE,
    "prompt": T("Hamza draws this circle in his notebook and says: \"It is round like a cricket ball, so it is 3-D.\" What went wrong?",
                "حمزہ اپنی کاپی میں یہ دائرہ بنا کر کہتا ہے: \"یہ کرکٹ کی گیند کی طرح گول ہے، اس لیے 3-D ہے۔\" کیا غلطی ہوئی؟"),
    "options": [
      opt("flat", "The drawn circle is flat: it has no height. It is 2-D. A ball is a sphere, which is 3-D.", "بنا ہوا دائرہ چپٹا ہے: اس کی اونچائی نہیں۔ یہ 2-D ہے۔ گیند کرہ ہے جو 3-D ہے۔", True,
          "Yes! Round is not the test. Height is.", "جی ہاں! گول ہونا پیمانہ نہیں۔ اونچائی ہے۔"),
      opt("onedim", "A circle is 1-D because it is a curved line.", "دائرہ 1-D ہے کیونکہ یہ خمدار لکیر ہے۔", False,
          "The circle covers a flat space with length and breadth. It is 2-D.", "دائرہ لمبائی اور چوڑائی والی چپٹی جگہ گھیرتا ہے۔ یہ 2-D ہے۔"),
      opt("nothing", "Nothing, he is right.", "کوئی غلطی نہیں، وہ درست ہے۔", False,
          "Can you pick the drawing up off the page? It has no height, so it is 2-D.", "کیا آپ تصویر صفحے سے اٹھا سکتے ہیں؟ اس کی اونچائی نہیں، اس لیے 2-D ہے۔", "flat_is_3d"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "A coin and a circle drawn on paper look the same from above. Why is the coin 3-D but the drawing 2-D?",
                     "اوپر سے سکہ اور کاغذ پر بنا دائرہ ایک جیسے لگتے ہیں۔ سکہ 3-D اور تصویر 2-D کیوں ہے؟"),
    "task": T("In your own words: why is a coin a 3-D shape but a circle drawn on paper a 2-D shape?",
              "اپنے الفاظ میں بتائیں: سکہ 3-D شکل کیوں ہے جبکہ کاغذ پر بنا دائرہ 2-D شکل؟"),
    "key_idea": "A coin has thickness (height) as well as length and breadth, so it is a very short cylinder, a 3-D solid. A drawn circle is flat on the page with only length and breadth, so it is 2-D.",
    "levels": {
      "got_it": "Says the coin has thickness or height (a third measurement) and the drawn circle has only length and breadth / is flat.",
      "partly": "Says the coin is thick or solid, or the drawing is flat, but not both.",
      "not_yet": "Gives no reason, or says it is because of the shape or size."},
    "keywords": [
      ["thick", "height", "thickness", "موٹا", "موٹائی", "اونچائی", "motai"],
      ["flat", "paper", "چپٹا", "کاغذ", "chapta"],
      ["three", "solid", "تین", "ٹھوس", "cylinder", "اسطوانہ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The coin has thickness, a third measurement, so it is a short cylinder.", "بہت خوب! سکے کی موٹائی ہے، تیسری پیمائش، اس لیے یہ چھوٹا سا اسطوانہ ہے۔"),
      "partly": T("Good start! Now compare both: what does the coin have that the drawing does not?", "اچھی شروعات! اب دونوں کا موازنہ کریں: سکے میں کیا ہے جو تصویر میں نہیں؟"),
      "not_yet": T("Stand a coin on its edge. Can you do that with a drawing? Think about thickness.", "سکے کو کنارے پر کھڑا کریں۔ کیا تصویر کے ساتھ ایسا ہو سکتا ہے؟ موٹائی کے بارے میں سوچیں۔")},
    "limit_per_day": 3, "max_attempts": 2},
   with_figure(number_question(
     "s11_hemisphere",
     T("Cut a cricket ball in half and you get a hemisphere. How many surfaces does a hemisphere have?", "کرکٹ کی گیند آدھی کاٹیں تو نصف کرہ بنتا ہے۔ نصف کرہ کی کتنی سطحیں ہیں؟"),
     S11,
     T("One surface is where you cut. The other is the round dome.", "ایک سطح وہاں ہے جہاں کاٹا۔ دوسری گول گنبد ہے۔"),
     T("Right! 1 flat circle and 1 curved surface: 2.", "درست! 1 چپٹا دائرہ اور 1 خمدار سطح: 2۔"),
     T("1 flat surface + 1 curved surface = 2 surfaces.", "1 چپٹی سطح + 1 خمدار سطح = 2 سطحیں۔"),
     common_wrong=[wrong(1, "Don't forget the flat face from the cut. 1 curved + 1 flat = 2.", "کاٹنے سے بنی چپٹی سطح نہ بھولیں۔ 1 خمدار + 1 چپٹی = 2۔", "curved_surface")]),
     FIG_HEMI),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Line, flat, solid: 1-D, 2-D, 3-D. And curved surfaces count too! Well done!", "لکیر، چپٹی، ٹھوس: 1-D، 2-D، 3-D۔ اور خمدار سطحیں بھی گنی جاتی ہیں! شاباش!"),
    "figure": FIG_SOLIDS,
    "text": T("1-D shapes have length only. 2-D shapes are flat with length and breadth, and we count their sides and vertices. 3-D shapes are solids with length, breadth and height, and we count their surfaces, edges and vertices. Edges are lines where surfaces meet; vertices are corner points. Curved surfaces and curved edges count too.",
              "1-D اشکال کی صرف لمبائی ہوتی ہے۔ 2-D اشکال چپٹی ہوتی ہیں، لمبائی اور چوڑائی کے ساتھ، اور ہم ان کے اضلاع اور راس گنتے ہیں۔ 3-D اشکال ٹھوس ہوتی ہیں، لمبائی، چوڑائی اور اونچائی کے ساتھ، اور ہم ان کی سطحیں، کنارے اور راس گنتے ہیں۔ کنارے وہ لکیریں ہیں جہاں سطحیں ملتی ہیں؛ راس کونے کے نقطے ہیں۔ خمدار سطحیں اور خمدار کنارے بھی گنے جاتے ہیں۔"),
    "points": [T("Cylinder: 3 surfaces, 2 edges, 0 vertices.", "اسطوانہ: 3 سطحیں، 2 کنارے، 0 راس۔"),
               T("Cone: 2 surfaces, 1 edge, 1 vertex.", "مخروط: 2 سطحیں، 1 کنارہ، 1 راس۔"),
               T("Sphere: 1 curved surface, no edges, no vertices.", "کرہ: 1 خمدار سطح، کوئی کنارہ نہیں، کوئی راس نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_kite", "type": "apply", "skill": SKILL, "step": with_figure(number_question(
     "r_kite",
     T("This rooftop kite is drawn flat on paper. How many vertices does it have?", "چھت کی یہ پتنگ کاغذ پر چپٹی بنی ہے۔ اس کے کتنے راس ہیں؟"),
     R1,
     T("Count the corner dots.", "کونوں کے نقطے گنیں۔"),
     T("Right! 4 vertices, and 4 sides too.", "درست! 4 راس، اور 4 اضلاع بھی۔"),
     T("Top, bottom, left and right corners: 4 vertices.", "اوپر، نیچے، بائیں اور دائیں کونے: 4 راس۔"),
     common_wrong=[wrong(8, "Count each corner once: 4 vertices. Sides and vertices are not added.", "ہر کونا ایک بار گنیں: 4 راس۔ اضلاع اور راس جمع نہیں کرتے۔")],
     qtype=None), FIG_KITE)},
   {"id": "r_sphere", "type": "recall", "skill": SKILL, "step": {
     "id": "r_sphere", "type": "choice",
     "prompt": T("A cricket ball is a sphere. Which is true?", "کرکٹ کی گیند کرہ ہے۔ کون سی بات درست ہے؟"),
     "options": [
       opt("one", "1 curved surface, no edges, no vertices", "1 خمدار سطح، کوئی کنارہ نہیں، کوئی راس نہیں", True,
           "Yes! It is curved all over, with nothing sharp.", "جی ہاں! یہ ہر طرف سے خمدار ہے، کچھ نوکیلا نہیں۔"),
       opt("cube", "6 faces, 12 edges, 8 vertices", "6 سطحیں، 12 کنارے، 8 راس", False,
           "That is a cube. A sphere has 1 curved surface and no edges or vertices.", "یہ مکعب ہے۔ کرہ کی 1 خمدار سطح ہے اور کوئی کنارہ یا راس نہیں۔", "curved_surface"),
       opt("flat", "It is 2-D because it is round", "یہ 2-D ہے کیونکہ گول ہے", False,
           "A ball has height too. It is a 3-D solid.", "گیند کی اونچائی بھی ہے۔ یہ 3-D ٹھوس ہے۔"),
     ]}},
 ],
 "teacher_notes": [
   "Written fresh for the Symmetry unit. No textbook text or exercises were used.",
   "The test for each kind of shape is the number of measurements: length (1-D), length and breadth (2-D), length, breadth and height (3-D). Round versus straight is not the test, which is why the coin and the drawn circle are compared.",
   "Solids are drawn with straight lines and ovals made of short segments; hidden edges and hidden halves of circles are dashed. Remind children that the dashed lines are edges we cannot see from the front.",
   "We use 'surface' for both flat and curved surfaces (some books say a cylinder has 2 faces and 1 curved surface). Edges are where two surfaces meet, so curved rims count as edges.",
   "Urdu terms to check: بُعد (dimension), قطعہ خط (line segment), اسطوانہ (cylinder), مخروط (cone), کرہ (sphere), نصف کرہ (hemisphere), خمدار سطح (curved surface), راس (vertex), کنارہ (edge).",
   "The numbers and figures were worked out in content/sources/g6-maths-18/shapes_2d_3d.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

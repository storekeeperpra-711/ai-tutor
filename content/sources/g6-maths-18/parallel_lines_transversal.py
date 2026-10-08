import math

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SY_LINES, AN_PAIRS, AN_LINE)

SKILL = SY_LINES
LINE = 180

# ---------------------------------------------------------------------------
# Figures: two horizontal parallel lines l (top) and m (bottom), cut by a
# slanted transversal. THETA is the angle in the top-right corner at each
# crossing (between the part of the transversal going up and the line going
# right). The four corners at a crossing are:
#   tr, bl -> THETA        tl, br -> 180 - THETA
# Arc starts are clockwise from +x on screen (y goes down).
# ---------------------------------------------------------------------------
W, H = 120, 80
Y = {"l": 22, "m": 56}
MID_X = 60          # the transversal crosses half-way between l and m here
REACH = 16          # how far the transversal goes past each line
ARC_R = 7
LABEL_R = 16


def corner_size(theta, corner):
    return theta if corner in ("tr", "bl") else LINE - theta


def corner_arc(theta, corner):
    """(start, sweep) of the angle in this corner."""
    return {"tr": (360 - theta, theta),
            "tl": (180, 180 - theta),
            "bl": (180 - theta, theta),
            "br": (0, 180 - theta)}[corner]


def r1(v):
    return round(v, 1)


def crossing(theta, line):
    """Where the transversal meets line l or m."""
    y = Y[line]
    mid_y = (Y["l"] + Y["m"]) / 2
    # Going up the transversal (y smaller) moves x by +1/tan(theta) per unit.
    x = MID_X + (mid_y - y) / math.tan(math.radians(theta))
    return [r1(x), y]


CORNER_EN = {"tr": "above line {L}, right of the transversal",
             "tl": "above line {L}, left of the transversal",
             "bl": "below line {L}, left of the transversal",
             "br": "below line {L}, right of the transversal"}
CORNER_UR = {"tr": "لکیر {L} کے اوپر، قاطع کے دائیں",
             "tl": "لکیر {L} کے اوپر، قاطع کے بائیں",
             "bl": "لکیر {L} کے نیچے، قاطع کے بائیں",
             "br": "لکیر {L} کے نیچے، قاطع کے دائیں"}


TILT = 12
TILT_SLOPE = math.tan(math.radians(TILT))


def transversal_figure(theta, marks, parallel=True):
    """marks: list of (line, corner, label). Draws an arc and a label in
    each marked corner."""
    assert 40 <= theta <= 140
    items = []
    for name in ("l", "m"):
        y = Y[name]
        if not parallel and name == "m":
            # tilt m about its crossing point so the two lines clearly meet
            cx = crossing(theta, "m")[0]
            dy = TILT_SLOPE * (W - 4 - cx), TILT_SLOPE * (cx - 4)
            items.append({"kind": "line", "from": [4, r1(y + dy[1])], "to": [W - 4, r1(y - dy[0])]})
        else:
            items.append({"kind": "line", "from": [4, y], "to": [W - 4, y]})
        if parallel:
            # a small arrow head on each line: the usual mark for parallel lines
            items.append({"kind": "line", "from": [16, y - 3], "to": [20, y]})
            items.append({"kind": "line", "from": [16, y + 3], "to": [20, y]})
        items.append({"kind": "label", "at": [W - 8, y - 6], "text": name})
    t = math.radians(theta)
    top, bottom = crossing(theta, "l"), crossing(theta, "m")
    up = [r1(top[0] + REACH / math.tan(t)), Y["l"] - REACH]
    down = [r1(bottom[0] - REACH / math.tan(t)), Y["m"] + REACH]
    items.append({"kind": "line", "from": down, "to": up})
    items += [{"kind": "point", "at": top}, {"kind": "point", "at": bottom}]
    en_parts, ur_parts = [], []
    for line, corner, text in marks:
        c = crossing(theta, line)
        start, sweep = corner_arc(theta, corner)
        assert sweep == corner_size(theta, corner)
        if not parallel and line == "m":
            # m is tilted up to the right by TILT degrees: corners above it shrink
            assert corner == "tr"
            sweep -= TILT
        items.append({"kind": "arc", "center": c, "radius": ARC_R, "start": start % 360, "sweep": sweep})
        mid = math.radians(start + sweep / 2)
        at = [r1(c[0] + LABEL_R * math.cos(mid)), r1(c[1] + LABEL_R * math.sin(mid))]
        assert 4 <= at[0] <= W - 4 and 4 <= at[1] <= H - 4, at
        items.append({"kind": "label", "at": at, "text": text})
        en_parts.append(f"angle {text} is {CORNER_EN[corner].format(L=line)}")
        ur_parts.append(f"زاویہ {text} {CORNER_UR[corner].format(L=line)} ہے")
    for it in items:
        for k in ("from", "to", "at", "center"):
            if k in it:
                x, y = it[k]
                rr = it.get("radius", 0)
                assert rr <= x <= W - rr and rr <= y <= H - rr, it
    if parallel:
        en = "Two parallel lines, l on top and m below, are crossed by a slanting line (the transversal)."
        ur = "دو متوازی لکیریں، اوپر l اور نیچے m، ایک ترچھی لکیر (قاطع) سے کٹتی ہیں۔"
    else:
        en = "Two lines l and m that are not parallel are crossed by a slanting line."
        ur = "دو لکیریں l اور m جو متوازی نہیں، ایک ترچھی لکیر سے کٹتی ہیں۔"
    if en_parts:
        en += " Marked: " + "; ".join(en_parts) + "."
        ur += " نشان لگے ہیں: " + "؛ ".join(ur_parts) + "۔"
    return {"width": W, "height": H, "alt": T(en, ur), "items": items}


def angle_figure(theta, given_line, given_corner, given, unknown_line, unknown_corner, letter):
    assert corner_size(theta, given_corner) == given
    return transversal_figure(theta, [(given_line, given_corner, f"{given}°"),
                                      (unknown_line, unknown_corner, letter)])


def theta_for(corner, size):
    """The drawing angle THETA that makes this corner the stated size."""
    th = size if corner in ("tr", "bl") else LINE - size
    assert corner_size(th, corner) == size
    return th


# --- the numbers -----------------------------------------------------------
# s5: vertically opposite at line m: tl = 125 -> br = ?
S5_TH = theta_for("tl", 125)
S5 = corner_size(S5_TH, "br")
assert S5 == 125 and LINE - 125 == 55
# s6: corresponding: l tr = 65 -> m tr = ?
S6_TH = theta_for("tr", 65)
S6 = corner_size(S6_TH, "tr")
assert S6 == 65 and LINE - 65 == 115
# s7: alternate: l br = 110 -> m tl = ?
S7_TH = theta_for("br", 110)
S7 = corner_size(S7_TH, "tl")
assert S7 == 110 and LINE - 110 == 70
# s8: co-interior: l bl = 65 -> m tl = ?
S8_TH = theta_for("bl", 65)
S8 = corner_size(S8_TH, "tl")
assert S8 == 115 and S8 + 65 == LINE and 90 - 65 == 25
# s9: co-interior: l br = 110 -> m tr = 70 (not 110)
S9_TH = theta_for("br", 110)
S9 = corner_size(S9_TH, "tr")
assert S9 == 70 and S9 + 110 == LINE
# s11: straight line then corresponding: l tr = 72 -> m tl = ?
S11_TH = theta_for("tr", 72)
S11 = corner_size(S11_TH, "tl")
assert S11 == 108 and corner_size(S11_TH, "tl") + 72 == LINE and 360 - 72 == 288
# question bank: co-interior l br = 105 -> m tr = 75
QB_TH = theta_for("br", 105)
QB = corner_size(QB_TH, "tr")
assert QB == 75 and QB + 105 == LINE
# review: alternate l bl = 48 -> m tr; corresponding l tl = 128 -> m tl
R1_TH = theta_for("bl", 48)
R1 = corner_size(R1_TH, "tr")
assert R1 == 48 and LINE - 48 == 132
R2_TH = theta_for("tl", 128)
R2 = corner_size(R2_TH, "tl")
assert R2 == 128 and LINE - 128 == 52

# s3: all eight angles numbered 1-8 (theta 65): 2, 3, 6, 7 are 65°; 1, 4, 5, 8 are 115°.
S3_TH = 65
NUMBERED = [("l", "tl", "1"), ("l", "tr", "2"), ("l", "bl", "3"), ("l", "br", "4"),
            ("m", "tl", "5"), ("m", "tr", "6"), ("m", "bl", "7"), ("m", "br", "8")]
S3_FIG = transversal_figure(S3_TH, NUMBERED)
S3_FIG["alt"] = T(
    "Two parallel lines, l on top and m below, are crossed by a slanting transversal. At line l the four angles are numbered 1 (top left), 2 (top right), 3 (bottom left), 4 (bottom right). At line m they are numbered the same way: 5, 6, 7, 8.",
    "دو متوازی لکیریں، اوپر l اور نیچے m، ایک ترچھے قاطع سے کٹتی ہیں۔ لکیر l پر چار زاویوں کے نمبر 1 (اوپر بائیں)، 2 (اوپر دائیں)، 3 (نیچے بائیں)، 4 (نیچے دائیں) ہیں۔ لکیر m پر اسی طرح 5، 6، 7، 8 ہیں۔")
sizes = {n: corner_size(S3_TH, c) for _, c, n in NUMBERED}
assert sizes["2"] == sizes["6"] and sizes["3"] == sizes["6"] and sizes["3"] + sizes["5"] == LINE
assert sizes["1"] == sizes["4"]

# s4: two lines crossing at a right angle, with the square mark.
P_C = [60, 40]
S4_FIG = {"width": W, "height": H,
          "alt": T("Two straight lines p and q cross at one point. One goes across and one goes straight up and down. A small square in the corner where they meet marks a right angle.",
                   "دو سیدھی لکیریں p اور q ایک نقطے پر ملتی ہیں۔ ایک افقی ہے اور ایک سیدھی اوپر نیچے۔ ملنے کی جگہ کونے میں چھوٹا مربع قائمہ زاویہ ظاہر کرتا ہے۔"),
          "items": [
              {"kind": "line", "from": [12, 40], "to": [108, 40]},
              {"kind": "line", "from": [60, 6], "to": [60, 74]},
              {"kind": "polygon", "points": [[60, 40], [67, 40], [67, 33], [60, 33]]},
              {"kind": "point", "at": P_C},
              {"kind": "label", "at": [104, 34], "text": "p"},
              {"kind": "label", "at": [66, 10], "text": "q"},
          ]}

# Plain parallel lines for the hook (no marks).
S1_FIG = transversal_figure(65, [])

lesson = {
 "id": "g6-maths-18-parallel-lines-and-transversal",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise parallel, intersecting and perpendicular lines, and use vertically opposite angles and the angles made when a transversal crosses two parallel lines (corresponding, alternate and co-interior angles) to find unknown angles.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Parallel lines and transversals", "متوازی لکیریں اور قاطع"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": AN_PAIRS}, {"skill": AN_LINE}],
 "misconceptions": [
   {"id": "not_parallel_equal", "description": "Thinks corresponding (or alternate) angles are equal even when the two lines are not parallel."},
   {"id": "cointerior_wrong_total", "description": "Adds co-interior angles to 90°, or thinks co-interior angles are equal instead of adding to 180°."},
   {"id": "alt_cointerior_mixup", "description": "Mixes up alternate angles (equal, on opposite sides of the transversal) with co-interior angles (same side, add to 180°)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_cointerior", "type": "recall", "step": {
     "id": "qb_cointerior", "type": "choice",
     "prompt": T("A transversal crosses two parallel lines. The two co-interior angles (same side, between the lines) add up to how many degrees?",
                 "ایک قاطع دو متوازی لکیروں کو کاٹتا ہے۔ دو ہم اندرونی زاویوں (ایک ہی طرف، لکیروں کے درمیان) کا مجموعہ کتنے درجے ہوتا ہے؟"),
     "options": [
       opt("d180", "180°", "180°", True, "Yes! Co-interior angles add up to 180°.", "جی ہاں! ہم اندرونی زاویوں کا مجموعہ 180° ہوتا ہے۔"),
       opt("d90", "90°", "90°", False, "Not 90°. Together they make a straight angle: 180°.", "90° نہیں۔ مل کر یہ مستقیم زاویہ بناتے ہیں: 180°۔", "cointerior_wrong_total"),
       opt("equal", "They are equal, so there is no fixed total.", "یہ برابر ہوتے ہیں، کوئی مقررہ مجموعہ نہیں۔", False,
           "Alternate angles are equal. Co-interior angles add up to 180°.", "متبادلہ زاویے برابر ہوتے ہیں۔ ہم اندرونی زاویوں کا مجموعہ 180° ہے۔", "alt_cointerior_mixup"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": dict(number_question(
     "qb_apply",
     T("Lines l and m are parallel. The marked angle is 105°. Angle x is on the same side of the transversal, between the lines. Find x.",
       "لکیریں l اور m متوازی ہیں۔ نشان والا زاویہ 105° ہے۔ زاویہ x قاطع کی اسی طرف، لکیروں کے درمیان ہے۔ x معلوم کریں۔"),
     QB,
     T("Co-interior angles add up to 180°.", "ہم اندرونی زاویوں کا مجموعہ 180° ہے۔"),
     T("Right! 180 − 105 = 75°.", "درست! 180 − 105 = 75°"),
     T("They are co-interior: 180 − 105 = 75°.", "یہ ہم اندرونی ہیں: 180 − 105 = 75°"),
     common_wrong=[wrong(105, "Equal would be alternate angles. These are on the same side, so they add to 180°: 75°.", "برابر تو متبادلہ زاویے ہوتے ہیں۔ یہ ایک ہی طرف ہیں، مجموعہ 180°: 75°", "alt_cointerior_mixup")],
     qtype=None), figure=angle_figure(QB_TH, "l", "br", 105, "m", "tr", "x"))},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "figure": transversal_figure(70, [("l", "tr", "70°"), ("m", "tr", "x")], parallel=False),
     "prompt": T("Lines l and m are NOT parallel. Sana says x is a corresponding angle to 70°, so x = 70°. What went wrong?",
                 "لکیریں l اور m متوازی نہیں ہیں۔ ثنا کہتی ہے x، 70° کا متناظرہ زاویہ ہے، اس لیے x = 70°۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("parallel", "Corresponding angles are only equal when the lines are parallel. Here we can't say x = 70°.", "متناظرہ زاویے صرف متوازی لکیروں پر برابر ہوتے ہیں۔ یہاں x = 70° نہیں کہہ سکتے۔", True,
           "Yes! The rule needs parallel lines.", "جی ہاں! یہ اصول متوازی لکیروں کے لیے ہے۔"),
       opt("add", "x should be 180 − 70 = 110°.", "x کو 180 − 70 = 110° ہونا چاہیے۔", False,
           "That is not a rule here either. Without parallel lines we can't find x from 70°.", "یہ بھی یہاں اصول نہیں۔ متوازی لکیروں کے بغیر 70° سے x نہیں نکلتا۔"),
       opt("nothing", "Nothing, corresponding angles are always equal.", "کوئی غلطی نہیں، متناظرہ زاویے ہمیشہ برابر ہوتے ہیں۔", False,
           "Only for parallel lines. When lines tilt towards each other, the angles change.", "صرف متوازی لکیروں کے لیے۔ لکیریں ایک دوسرے کی طرف جھکیں تو زاویے بدل جاتے ہیں۔", "not_parallel_equal"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_equal", "front": T("Parallel lines and a transversal: which angle pairs are equal?", "متوازی لکیریں اور قاطع: کون سے زاویوں کے جوڑے برابر ہوتے ہیں؟"),
    "back": T("Corresponding angles, alternate angles and vertically opposite angles.", "متناظرہ زاویے، متبادلہ زاویے اور راسی زاویے۔")},
   {"id": "f_cointerior", "front": T("Co-interior angles add up to?", "ہم اندرونی زاویوں کا مجموعہ؟"),
    "back": T("180°. If one is 65°, the other is 115°.", "180°۔ اگر ایک 65° ہے تو دوسرا 115°۔")},
 ],
 "home_tasks": [{"id": "h_ruler", "text": T(
   "Draw a line along one edge of your ruler, then along the other edge: two parallel lines. Draw a slanting line across both. Number the 8 angles like in the lesson and measure them with a protractor. Which ones are equal? Which pairs add up to 180°?",
   "اپنی رولر کے ایک کنارے کے ساتھ لکیر کھینچیں، پھر دوسرے کنارے کے ساتھ: دو متوازی لکیریں۔ دونوں کو کاٹتی ایک ترچھی لکیر کھینچیں۔ سبق کی طرح 8 زاویوں کے نمبر لگائیں اور چاندے سے ناپیں۔ کون سے برابر ہیں؟ کون سے جوڑوں کا مجموعہ 180° ہے؟")}],
 "glossary": [T("Parallel lines", "متوازی لکیریں"), T("Perpendicular lines", "عمودی لکیریں"), T("Intersecting lines", "قطع کرنے والی لکیریں"),
              T("Transversal", "قاطع"), T("Vertically opposite angles", "راسی زاویے"), T("Corresponding angles", "متناظرہ زاویے"),
              T("Alternate angles", "متبادلہ زاویے"), T("Co-interior angles", "ہم اندرونی زاویے")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Railway tracks run side by side and never meet. Now a road crosses them. What angles does it make?",
                     "ریل کی پٹڑیاں ساتھ ساتھ چلتی ہیں اور کبھی نہیں ملتیں۔ اب ایک سڑک انہیں کاٹتی ہے۔ یہ کون سے زاویے بناتی ہے؟"),
    "figure": S1_FIG,
    "text": T("Today we look at lines that never meet, lines that cross, and the angles a slanting line makes when it crosses two parallel lines. First, a quick check.",
              "آج ہم ایسی لکیریں دیکھیں گے جو کبھی نہیں ملتیں، جو ایک دوسرے کو کاٹتی ہیں، اور وہ زاویے جو ایک ترچھی لکیر دو متوازی لکیروں کو کاٹ کر بناتی ہے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Angles that sit together on a straight line add up to how many degrees?", "سیدھی لکیر پر ساتھ ساتھ زاویوں کا مجموعہ کتنے درجے ہوتا ہے؟"),
     LINE,
     T("A straight line is half a turn.", "سیدھی لکیر آدھا چکر ہے۔"),
     T("Right! 180°. We will use this a lot today.", "درست! 180°۔ آج ہم یہ بہت استعمال کریں گے۔"),
     T("Angles on a straight line add up to 180°.", "سیدھی لکیر پر زاویوں کا مجموعہ 180° ہے۔"),
     common_wrong=[wrong(360, "360° is a full turn. A straight line is half: 180°.", "360° پورا چکر ہے۔ سیدھی لکیر آدھا ہے: 180°"),
                   wrong(90, "90° is a right angle. A straight line is two of them: 180°.", "90° قائمہ زاویہ ہے۔ سیدھی لکیر ان میں سے دو ہے: 180°")],
     qtype="recall", skill=AN_LINE),
   {"id": "s3_rules", "type": "explain",
    "character": say("happy", "Same place, same size. Opposite sides inside, same size. Same side inside, add to 180!",
                     "ایک جیسی جگہ، ایک جیسا سائز۔ اندر الٹی طرف، برابر۔ اندر ایک ہی طرف، مجموعہ 180!"),
    "figure": S3_FIG,
    "text": T("Parallel lines (∥) stay the same distance apart and never meet, like the two rails of a track: we write l ∥ m. Intersecting lines cross at a point. Perpendicular lines cross at a right angle, 90°. When two lines cross, the angles opposite each other are equal: these are vertically opposite angles (1 and 4, 2 and 3). A line that crosses two parallel lines is a transversal. Corresponding angles sit in the same place at each crossing, so they are equal (2 and 6). Alternate angles are between the lines on opposite sides of the transversal, and they are equal too (3 and 6, 4 and 5). Co-interior angles are between the lines on the same side, and they add up to 180° (3 and 5, 4 and 6).",
              "متوازی لکیریں (∥) ہمیشہ برابر فاصلے پر رہتی ہیں اور کبھی نہیں ملتیں، جیسے پٹڑی کی دو ریلیں: ہم لکھتے ہیں l ∥ m۔ قطع کرنے والی لکیریں ایک نقطے پر ایک دوسرے کو کاٹتی ہیں۔ عمودی لکیریں قائمہ زاویے، 90°، پر کاٹتی ہیں۔ جب دو لکیریں کاٹتی ہیں تو آمنے سامنے کے زاویے برابر ہوتے ہیں: یہ راسی زاویے ہیں (1 اور 4، 2 اور 3)۔ جو لکیر دو متوازی لکیروں کو کاٹے وہ قاطع ہے۔ متناظرہ زاویے ہر کٹاؤ پر ایک ہی جگہ ہوتے ہیں، اس لیے برابر ہیں (2 اور 6)۔ متبادلہ زاویے لکیروں کے درمیان قاطع کی الٹی طرف ہوتے ہیں، یہ بھی برابر ہیں (3 اور 6، 4 اور 5)۔ ہم اندرونی زاویے لکیروں کے درمیان قاطع کی ایک ہی طرف ہوتے ہیں، ان کا مجموعہ 180° ہے (3 اور 5، 4 اور 6)۔")},
   {"id": "s4_name_lines", "type": "choice", "question_type": "recall",
    "figure": S4_FIG,
    "prompt": T("Look at lines p and q. How are they related?", "لکیریں p اور q دیکھیں۔ ان کا آپس میں کیا تعلق ہے؟"),
    "options": [
      opt("perpendicular", "Perpendicular: they cross at 90°.", "عمودی: یہ 90° پر کاٹتی ہیں۔", True,
          "Yes! The little square shows a right angle.", "جی ہاں! چھوٹا مربع قائمہ زاویہ دکھاتا ہے۔"),
      opt("parallel", "Parallel: they never meet.", "متوازی: یہ کبھی نہیں ملتیں۔", False,
          "They do meet, in the middle. Parallel lines never meet.", "یہ تو درمیان میں مل رہی ہیں۔ متوازی لکیریں کبھی نہیں ملتیں۔"),
      opt("just_intersecting", "Intersecting, but not at a right angle.", "قطع کرنے والی، لیکن قائمہ زاویے پر نہیں۔", False,
          "They do intersect, but look at the square mark: the angle is 90°, so they are perpendicular.", "یہ کاٹتی تو ہیں، مگر مربع کا نشان دیکھیں: زاویہ 90° ہے، اس لیے یہ عمودی ہیں۔"),
    ]},
   dict(number_question(
     "s5_vertically_opposite",
     T("Two lines cross at a point on m. One angle is 125°. Angle a is opposite it at the same crossing. Find a.",
       "دو لکیریں m پر ایک نقطے پر کاٹتی ہیں۔ ایک زاویہ 125° ہے۔ زاویہ a اسی کٹاؤ پر اس کے آمنے سامنے ہے۔ a معلوم کریں۔"),
     S5,
     T("Vertically opposite angles are equal.", "راسی زاویے برابر ہوتے ہیں۔"),
     T("Right! a = 125°.", "درست! a = 125°"),
     T("Opposite angles at a crossing are equal: a = 125°.", "کٹاؤ پر آمنے سامنے کے زاویے برابر ہیں: a = 125°"),
     common_wrong=[wrong(55, "55° is the angle next to it on the straight line. The opposite angle is equal: 125°.", "55° تو سیدھی لکیر پر ساتھ والا زاویہ ہے۔ آمنے سامنے والا برابر ہے: 125°")]),
     figure=angle_figure(S5_TH, "m", "tl", 125, "m", "br", "a")),
   dict(number_question(
     "s6_corresponding",
     T("l ∥ m. The angle at line l is 65°. Angle x is in the same place at line m. Find x.",
       "l ∥ m۔ لکیر l پر زاویہ 65° ہے۔ زاویہ x لکیر m پر اسی جگہ ہے۔ x معلوم کریں۔"),
     S6,
     T("Corresponding angles are equal.", "متناظرہ زاویے برابر ہوتے ہیں۔"),
     T("Right! x = 65°. Slide the top crossing down onto m and the angles match.", "درست! x = 65°۔ اوپر والے کٹاؤ کو نیچے m پر کھسکائیں تو زاویے ایک جیسے ہیں۔"),
     T("They are corresponding angles, so x = 65°.", "یہ متناظرہ زاویے ہیں، اس لیے x = 65°"),
     common_wrong=[wrong(115, "115° would be the angle next to it. Corresponding angles are equal: 65°.", "115° ساتھ والا زاویہ ہوتا۔ متناظرہ زاویے برابر ہیں: 65°")]),
     figure=angle_figure(S6_TH, "l", "tr", 65, "m", "tr", "x")),
   dict(number_question(
     "s7_alternate",
     T("l ∥ m. The angle below l is 110°. Angle b is above m, between the lines, on the other side of the transversal. Find b.",
       "l ∥ m۔ l کے نیچے زاویہ 110° ہے۔ زاویہ b لکیروں کے درمیان m کے اوپر، قاطع کی دوسری طرف ہے۔ b معلوم کریں۔"),
     S7,
     T("Between the lines, opposite sides: alternate angles. They are equal.", "لکیروں کے درمیان، الٹی طرف: متبادلہ زاویے۔ یہ برابر ہوتے ہیں۔"),
     T("Right! b = 110°. Alternate angles make a Z shape.", "درست! b = 110°۔ متبادلہ زاویے Z کی شکل بناتے ہیں۔"),
     T("They are alternate angles, so b = 110°.", "یہ متبادلہ زاویے ہیں، اس لیے b = 110°"),
     common_wrong=[wrong(70, "Adding to 180° is for co-interior angles (same side). These are on opposite sides, so they are equal: 110°.", "180° مجموعہ ہم اندرونی (ایک ہی طرف) کے لیے ہے۔ یہ الٹی طرف ہیں، اس لیے برابر: 110°", "alt_cointerior_mixup")]),
     figure=angle_figure(S7_TH, "l", "br", 110, "m", "tl", "b")),
   dict(number_question(
     "s8_cointerior",
     T("l ∥ m. The angle below l is 65°. Angle y is above m, between the lines, on the same side of the transversal. Find y.",
       "l ∥ m۔ l کے نیچے زاویہ 65° ہے۔ زاویہ y لکیروں کے درمیان m کے اوپر، قاطع کی اسی طرف ہے۔ y معلوم کریں۔"),
     S8,
     T("Same side, between the lines: co-interior angles add up to 180°.", "ایک ہی طرف، لکیروں کے درمیان: ہم اندرونی زاویوں کا مجموعہ 180° ہے۔"),
     T("Right! 180 − 65 = 115°. Co-interior angles make a C shape.", "درست! 180 − 65 = 115°۔ ہم اندرونی زاویے C کی شکل بناتے ہیں۔"),
     T("Co-interior angles add up to 180°: 180 − 65 = 115°.", "ہم اندرونی زاویوں کا مجموعہ 180° ہے: 180 − 65 = 115°"),
     common_wrong=[wrong(65, "Co-interior angles are not equal. They add up to 180°: 115°.", "ہم اندرونی زاویے برابر نہیں ہوتے۔ ان کا مجموعہ 180° ہے: 115°", "cointerior_wrong_total"),
                   wrong(25, "Co-interior angles add up to 180°, not 90°: 180 − 65 = 115°.", "ہم اندرونی زاویوں کا مجموعہ 180° ہے، 90° نہیں: 180 − 65 = 115°", "cointerior_wrong_total")]),
     figure=angle_figure(S8_TH, "l", "bl", 65, "m", "tl", "y")),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "figure": angle_figure(S9_TH, "l", "br", 110, "m", "tr", "x"),
    "prompt": T("l ∥ m. The angle below l is 110°. Angle x is above m on the same side of the transversal. Bilal says x = 110° because the angles are equal. What went wrong?",
                "l ∥ m۔ l کے نیچے زاویہ 110° ہے۔ زاویہ x قاطع کی اسی طرف m کے اوپر ہے۔ بلال کہتا ہے x = 110° کیونکہ زاویے برابر ہیں۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("cointerior", "They are co-interior, so they add up to 180°: x = 70°.", "یہ ہم اندرونی ہیں، مجموعہ 180°: x = 70°", True,
          "Yes! Same side between the lines means they add to 180°.", "جی ہاں! لکیروں کے درمیان ایک ہی طرف ہوں تو مجموعہ 180° ہوتا ہے۔"),
      opt("ninety", "They add up to 90°, so x can't be found.", "ان کا مجموعہ 90° ہے، اس لیے x نہیں نکلتا۔", False,
          "Co-interior angles add up to 180°, not 90°: x = 70°.", "ہم اندرونی زاویوں کا مجموعہ 180° ہے، 90° نہیں: x = 70°", "cointerior_wrong_total"),
      opt("nothing", "Nothing. They are alternate angles, so they are equal.", "کوئی غلطی نہیں۔ یہ متبادلہ زاویے ہیں، اس لیے برابر ہیں۔", False,
          "Alternate angles are on opposite sides. These are on the same side: co-interior, x = 70°.", "متبادلہ زاویے الٹی طرف ہوتے ہیں۔ یہ ایک ہی طرف ہیں: ہم اندرونی، x = 70°", "alt_cointerior_mixup"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "If corresponding angles are equal, why do co-interior angles add up to 180°? Can you teach me?",
                     "اگر متناظرہ زاویے برابر ہیں تو ہم اندرونی زاویوں کا مجموعہ 180° کیوں ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "figure": S3_FIG,
    "task": T("Use the numbered picture. Explain why angles 3 and 5 add up to 180°.",
              "نمبر والی تصویر استعمال کریں۔ بتائیں زاویے 3 اور 5 کا مجموعہ 180° کیوں ہے۔"),
    "key_idea": "Angle 5 equals angle 1 because they are corresponding angles. Angles 1 and 3 sit together on the straight line l, so they add up to 180°. So angles 3 and 5 also add up to 180°.",
    "levels": {
      "got_it": "Links angle 5 to an equal angle at line l (corresponding 1, or uses alternate/vertically opposite) and says that angle and angle 3 lie on a straight line, so 180°.",
      "partly": "Mentions the straight line (180°) or an equal angle, but not both steps.",
      "not_yet": "Gives no reason, or just repeats the rule."},
    "keywords": [
      ["corresponding", "equal", "same", "متناظرہ", "برابر", "barabar"],
      ["straight", "line", "180", "سیدھی", "لکیر", "seedhi"],
      ["angle 1", "1 and 3", "5 and 1", "زاویہ 1"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Angle 5 equals angle 1, and 1 and 3 make a straight line.", "بہت خوب! زاویہ 5 زاویہ 1 کے برابر ہے، اور 1 اور 3 سیدھی لکیر بناتے ہیں۔"),
      "partly": T("Good start! Use both ideas: angle 5 equals angle 1, and angles 1 and 3 lie on a straight line.", "اچھی شروعات! دونوں باتیں استعمال کریں: زاویہ 5 زاویہ 1 کے برابر ہے، اور 1 اور 3 سیدھی لکیر پر ہیں۔"),
      "not_yet": T("Find an angle at line l equal to angle 5. What do it and angle 3 add up to on the straight line?", "لکیر l پر زاویہ 5 کے برابر زاویہ ڈھونڈیں۔ سیدھی لکیر پر اس کا اور زاویہ 3 کا مجموعہ کیا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   dict(number_question(
     "s11_two_steps",
     T("l ∥ m. The angle above l, right of the transversal, is 72°. Angle z is above m, left of the transversal. Find z.",
       "l ∥ m۔ l کے اوپر، قاطع کے دائیں زاویہ 72° ہے۔ زاویہ z لکیر m کے اوپر، قاطع کے بائیں ہے۔ z معلوم کریں۔"),
     S11,
     T("The angle in the same place at m is 72° (corresponding). z sits next to it on line m.", "m پر اسی جگہ زاویہ 72° ہے (متناظرہ)۔ z لکیر m پر اس کے ساتھ ہے۔"),
     T("Right! 180 − 72 = 108°.", "درست! 180 − 72 = 108°"),
     T("Corresponding angle at m is 72°, and z is on a straight line with it: 180 − 72 = 108°.", "m پر متناظرہ زاویہ 72° ہے، اور z اس کے ساتھ سیدھی لکیر پر ہے: 180 − 72 = 108°"),
     common_wrong=[wrong(72, "72° is the angle next to z. z is on a straight line with it: 180 − 72 = 108°.", "72° تو z کے ساتھ والا زاویہ ہے۔ z اس کے ساتھ سیدھی لکیر پر ہے: 180 − 72 = 108°"),
                   wrong(288, "That used 360°. A straight line is 180°: 108°.", "اس میں 360° لیا۔ سیدھی لکیر 180° ہے: 108°")]),
     figure=angle_figure(S11_TH, "l", "tr", 72, "m", "tl", "z")),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Corresponding and alternate: equal. Co-interior: 180. Well done!", "متناظرہ اور متبادلہ: برابر۔ ہم اندرونی: 180۔ شاباش!"),
    "figure": S3_FIG,
    "text": T("Parallel lines never meet; perpendicular lines meet at 90°. Vertically opposite angles are equal. When a transversal crosses two parallel lines: corresponding angles are equal (F shape), alternate angles are equal (Z shape), and co-interior angles add up to 180° (C shape). These rules only work when the lines are parallel.",
              "متوازی لکیریں کبھی نہیں ملتیں؛ عمودی لکیریں 90° پر ملتی ہیں۔ راسی زاویے برابر ہوتے ہیں۔ جب قاطع دو متوازی لکیروں کو کاٹے: متناظرہ زاویے برابر (F شکل)، متبادلہ زاویے برابر (Z شکل)، اور ہم اندرونی زاویوں کا مجموعہ 180° (C شکل)۔ یہ اصول صرف متوازی لکیروں پر لاگو ہوتے ہیں۔"),
    "points": [T("Corresponding and alternate angles are equal.", "متناظرہ اور متبادلہ زاویے برابر ہیں۔"),
               T("Co-interior angles add up to 180°.", "ہم اندرونی زاویوں کا مجموعہ 180° ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_alternate", "type": "apply", "skill": SKILL, "step": dict(number_question(
     "r_alternate",
     T("l ∥ m. The angle below l, left of the transversal, is 48°. Angle x is above m, right of the transversal. Find x.",
       "l ∥ m۔ l کے نیچے، قاطع کے بائیں زاویہ 48° ہے۔ زاویہ x لکیر m کے اوپر، قاطع کے دائیں ہے۔ x معلوم کریں۔"),
     R1,
     T("Between the lines, opposite sides: alternate angles.", "لکیروں کے درمیان، الٹی طرف: متبادلہ زاویے۔"),
     T("Right! x = 48°.", "درست! x = 48°"),
     T("Alternate angles are equal: x = 48°.", "متبادلہ زاویے برابر ہیں: x = 48°"),
     common_wrong=[wrong(132, "Alternate angles are equal, they don't add to 180°: 48°.", "متبادلہ زاویے برابر ہوتے ہیں، ان کا مجموعہ 180° نہیں: 48°", "alt_cointerior_mixup")],
     qtype=None), figure=angle_figure(R1_TH, "l", "bl", 48, "m", "tr", "x"))},
   {"id": "r_corresponding", "type": "apply", "skill": SKILL, "step": dict(number_question(
     "r_corresponding",
     T("l ∥ m. The angle above l, left of the transversal, is 128°. Angle a is in the same place at m. Find a.",
       "l ∥ m۔ l کے اوپر، قاطع کے بائیں زاویہ 128° ہے۔ زاویہ a لکیر m پر اسی جگہ ہے۔ a معلوم کریں۔"),
     R2,
     T("Same place at each crossing: corresponding angles.", "ہر کٹاؤ پر ایک ہی جگہ: متناظرہ زاویے۔"),
     T("Right! a = 128°.", "درست! a = 128°"),
     T("Corresponding angles are equal: a = 128°.", "متناظرہ زاویے برابر ہیں: a = 128°"),
     common_wrong=[wrong(52, "52° is the angle next to it. Corresponding angles are equal: 128°.", "52° ساتھ والا زاویہ ہے۔ متناظرہ زاویے برابر ہیں: 128°")],
     qtype=None), figure=angle_figure(R2_TH, "l", "tl", 128, "m", "tl", "a"))},
 ],
 "teacher_notes": [
   "Written fresh for the Symmetry unit (Sub-domain 9). No textbook text or exercises were used.",
   "Every figure is drawn by parallel_lines_transversal.py from the angle in the question, so the slant of the transversal in the picture matches the stated angle.",
   "The F, Z and C shapes are memory aids only; ask children to name the angle pair and say why (same place, opposite sides between the lines, same side between the lines).",
   "Stress that the transversal rules need parallel lines; the question-bank find-error item shows lines that are not parallel.",
   "Urdu terms to check: متوازی لکیریں (parallel lines), عمودی لکیریں (perpendicular lines), قطع کرنے والی لکیریں (intersecting lines), قاطع (transversal), راسی زاویے (vertically opposite angles), متناظرہ زاویے (corresponding angles), متبادلہ زاویے (alternate angles), ہم اندرونی زاویے (co-interior angles).",
   "The numbers and figures were worked out in content/sources/g6-maths-18/parallel_lines_transversal.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

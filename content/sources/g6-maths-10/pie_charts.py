from common import (T, opt, say, wrong, number_question, table_text, write,
                    BOOK, REVIEW, DH_BAR_GRAPHS, DH_PIE_CHARTS)
from figs import pie_chart, double_bar_graph, squares_bar, attach

SKILL = DH_PIE_CHARTS
WHOLE = 360


def count_from_angle(angle, total):
    """How many a slice stands for: (angle ÷ 360) × total."""
    assert (angle * total) % WHOLE == 0, (angle, total)
    return angle * total // WHOLE


def angle_of(part, total):
    """A slice's angle: (part ÷ total) × 360."""
    assert (part * WHOLE) % total == 0, (part, total)
    return part * WHOLE // total


# Slices and double bars, written as text in the steps and drawn in the pictures.
SPORTS = [(("Cricket", "کرکٹ"), 180), (("Hockey", "ہاکی"), 90), (("Football", "فٹ بال"), 90)]
SPORTS_EN, SPORTS_UR = table_text(SPORTS, "°", "°")
assert sum(a for _, a in SPORTS) == WHOLE
CLASSES = [("Class 6", "جماعت 6", 20, 25), ("Class 7", "جماعت 7", 18, 22), ("Class 8", "جماعت 8", 24, 19)]
CLASSES_EN = "; ".join(f"{en}: boys {b}, girls {g}" for en, _, b, g in CLASSES)
CLASSES_UR = "؛ ".join(f"{ur}: لڑکے {b}، لڑکیاں {g}" for _, ur, b, g in CLASSES)

# s2: bar graph, each square stands for 5, bar 6 squares tall
S2 = 6 * 5
assert S2 == 30 and 6 + 5 == 11
# s4: 40 children, hockey slice 90°
S4 = count_from_angle(90, 40)
assert S4 == 10 and S4 * 4 == 40
# s5: 15 of 60 children chose mango -> angle
S5 = angle_of(15, 60)
assert S5 == 90
# s6: 12 of 36 children walk to school -> angle
S6 = angle_of(12, 36)
assert S6 == 120 and WHOLE // 12 == 30
# s7: Class 6, how many more girls than boys
S7 = 25 - 20
assert S7 == 5 and 25 + 20 == 45
# s8: the class with more boys than girls
MORE_BOYS = [en for en, _, b, g in CLASSES if b > g]
assert MORE_BOYS == ["Class 8"]
# s9: 180° of 40 children is 20, not 180
assert count_from_angle(180, 40) == 20
# s11: missing slice
S11 = WHOLE - (150 + 120)
assert S11 == 90 and 150 + 120 == 270
# question bank and review
QB = count_from_angle(120, 24)
assert QB == 8
assert 25 - 20 == 5 and 25 + 20 == 45
R1 = count_from_angle(180, 60)
assert R1 == 30
R2 = 14 - 9
assert R2 == 5 and 14 + 9 == 23

lesson = {
 "id": "g6-maths-10-pie-charts-and-multiple-bar-graphs",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Read and work out the angles of a pie chart, where the whole circle is 360°, and compare two sets of data on a multiple bar graph.", "textbook": BOOK}],
 "skills": [SKILL],
 "title": T("Pie charts and multiple bar graphs", "دائری نقشہ (پائی چارٹ) اور دوہرے بار گراف"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": DH_BAR_GRAPHS}],
 "misconceptions": [
   {"id": "angle_as_count", "description": "Reads a slice's angle in degrees as the number of people or things it stands for."},
   {"id": "not_360", "description": "Thinks the whole circle is 100 or 180 instead of 360 degrees."},
   {"id": "adds_for_difference", "description": "Adds the two bars of a pair when the question asks how many more."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_whole", "type": "recall", "step": {
     "id": "qb_whole", "type": "choice",
     "prompt": T("How many degrees make the whole circle of a pie chart?", "پائی چارٹ کا پورا دائرہ کتنے درجے کا ہوتا ہے؟"),
     "options": [
       opt("d360", "360°", "360°", True, "Yes! The whole circle is 360° and stands for all the data.", "جی ہاں! پورا دائرہ 360° ہے اور سارا مواد دکھاتا ہے۔"),
       opt("d100", "100°", "100°", False, "A full turn is 360°, not 100°.", "ایک پورا چکر 360° ہے، 100° نہیں۔", "not_360"),
       opt("d180", "180°", "180°", False, "180° is only half the circle. The whole is 360°.", "180° صرف آدھا دائرہ ہے۔ پورا 360° ہے۔", "not_360"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A pie chart shows 24 children. One slice is 120°. How many children does it stand for?", "ایک پائی چارٹ 24 بچے دکھاتا ہے۔ ایک ٹکڑا 120° کا ہے۔ یہ کتنے بچوں کو ظاہر کرتا ہے؟"),
     QB,
     T("120° is what part of 360°?", "120°، 360° کا کتنا حصہ ہے؟"),
     T("Right! 8 children.", "درست! 8 بچے"),
     T("120° is one third of 360°, and one third of 24 is 8.", "120°، 360° کا تیسرا حصہ ہے، اور 24 کا تیسرا حصہ 8 ہے۔"),
     common_wrong=[wrong(120, "120 is the angle, not the number of children. 120° is a third of the circle: 24 ÷ 3 = 8.", "120 زاویہ ہے، بچوں کی تعداد نہیں۔ 120° دائرے کا تیسرا حصہ ہے: 24 ÷ 3 = 8", "angle_as_count")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A double bar graph shows Class 6: boys 20, girls 25. Ahmed says there are 45 more girls than boys. What went wrong?", "ایک دوہرا بار گراف دکھاتا ہے جماعت 6: لڑکے 20، لڑکیاں 25۔ احمد کہتا ہے لڑکیاں لڑکوں سے 45 زیادہ ہیں۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("subtract", "He added. 'How many more' means 25 − 20 = 5.", "اس نے جمع کیا۔ 'کتنے زیادہ' یعنی 25 − 20 = 5", True,
           "Yes! 45 is how many children in all.", "جی ہاں! 45 کل بچوں کی تعداد ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "45 is the total. The difference is 25 − 20 = 5.", "45 کل ہے۔ فرق 25 − 20 = 5 ہے۔", "adds_for_difference"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_angle", "front": T("Angle of a slice?", "ٹکڑے کا زاویہ؟"),
    "back": T("(part ÷ total) × 360°. 15 out of 60: a quarter, so 90°.", "(حصہ ÷ کل) × 360°۔ 60 میں سے 15: چوتھائی، یعنی 90°")},
   {"id": "f_half", "front": T("Half and quarter of a pie chart?", "پائی چارٹ کا آدھا اور چوتھائی؟"),
    "back": T("Half = 180°. Quarter = 90°. Whole = 360°.", "آدھا = 180°۔ چوتھائی = 90°۔ پورا = 360°")},
 ],
 "home_tasks": [{"id": "h_survey", "text": T(
   "Ask 4 people at home whether they like tea or milk best. Draw a circle and split it into 4 equal slices, one for each person, and colour them by drink. Each slice is 90°. How many degrees is tea?",
   "گھر میں 4 لوگوں سے پوچھیں کہ انہیں چائے پسند ہے یا دودھ۔ ایک دائرہ بنائیں اور اسے 4 برابر ٹکڑوں میں بانٹیں، ہر شخص کا ایک، اور مشروب کے حساب سے رنگ کریں۔ ہر ٹکڑا 90° ہے۔ چائے کتنے درجے ہے؟")}],
 "glossary": [T("Pie chart", "دائری نقشہ (پائی چارٹ)"), T("Slice", "ٹکڑا"), T("Angle", "زاویہ"), T("Degree", "درجہ"),
              T("Multiple (double) bar graph", "دوہرا بار گراف")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Imagine a round roti cut into pieces, one piece for each sport. The biggest piece shows the favourite!",
                     "سوچیں ایک گول روٹی ٹکڑوں میں کٹی ہے، ہر کھیل کا ایک ٹکڑا۔ سب سے بڑا ٹکڑا پسندیدہ کھیل دکھاتا ہے!"),
    "text": T("Today we read pie charts, like the one in the picture, and double bar graphs. First, a quick check.",
              "آج ہم پائی چارٹ، جیسے تصویر والا، اور دوہرے بار گراف پڑھیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("On a bar graph, each square stands for 5 children. A bar is 6 squares tall. How many children does it show?", "ایک بار گراف میں ہر خانہ 5 بچوں کو ظاہر کرتا ہے۔ ایک ستون 6 خانے اونچا ہے۔ یہ کتنے بچے دکھاتا ہے؟"),
     S2,
     T("6 squares, 5 each.", "6 خانے، ہر ایک 5"),
     T("Right! 30 children.", "درست! 30 بچے"),
     T("6 × 5 = 30.", "6 × 5 = 30"),
     common_wrong=[wrong(6, "Each square is 5 children: 6 × 5 = 30.", "ہر خانہ 5 بچے ہے: 6 × 5 = 30"),
                   wrong(11, "Multiply, don't add: 6 × 5 = 30.", "جمع نہیں، ضرب: 6 × 5 = 30")],
     qtype="recall", skill=DH_BAR_GRAPHS),
   {"id": "s3_pie", "type": "explain",
    "character": say("happy", "The whole circle is all the data, and it is 360°. Half is 180°, a quarter is 90°.",
                     "پورا دائرہ سارا مواد ہے، اور یہ 360° ہے۔ آدھا 180°، چوتھائی 90°۔"),
    "text": T("A pie chart is a circle split into slices. The whole circle stands for all the data and measures 360°. A bigger share gets a bigger slice. Angle of a slice = (part ÷ total) × 360. To read a slice, go the other way: a 90° slice is a quarter of the circle, so it is a quarter of the total. A multiple (double) bar graph puts two bars side by side for each group, such as boys and girls in each class, so you can compare them.",
              "پائی چارٹ ایک دائرہ ہے جو ٹکڑوں میں بٹا ہوتا ہے۔ پورا دائرہ سارا مواد دکھاتا ہے اور 360° کا ہوتا ہے۔ بڑے حصے کا ٹکڑا بڑا ہوتا ہے۔ ٹکڑے کا زاویہ = (حصہ ÷ کل) × 360۔ ٹکڑا پڑھنے کے لیے الٹا چلیں: 90° کا ٹکڑا دائرے کا چوتھائی ہے، تو یہ کل کا چوتھائی ہے۔ دوہرے بار گراف میں ہر گروہ کے دو ستون ساتھ ساتھ ہوتے ہیں، جیسے ہر جماعت کے لڑکے اور لڑکیاں، تاکہ آپ موازنہ کر سکیں۔")},
   number_question(
     "s4_quarter",
     T(f"A pie chart shows the favourite sport of 40 children: {SPORTS_EN}. How many children chose hockey?", f"ایک پائی چارٹ 40 بچوں کا پسندیدہ کھیل دکھاتا ہے: {SPORTS_UR}۔ کتنے بچوں نے ہاکی چنی؟"),
     S4,
     T("90° is a quarter of 360°.", "90°، 360° کا چوتھائی ہے۔"),
     T("Right! 10 children.", "درست! 10 بچے"),
     T("A quarter of 40 is 40 ÷ 4 = 10.", "40 کا چوتھائی 40 ÷ 4 = 10 ہے۔"),
     common_wrong=[wrong(90, "90 is the angle, not the children. 90° is a quarter: 40 ÷ 4 = 10.", "90 زاویہ ہے، بچے نہیں۔ 90° چوتھائی ہے: 40 ÷ 4 = 10", "angle_as_count")]),
   number_question(
     "s5_angle",
     T("In a class of 60 children, 15 chose mango as their favourite fruit. What angle should the mango slice have, in degrees?", "60 بچوں کی جماعت میں 15 نے آم کو پسندیدہ پھل چنا۔ آم کے ٹکڑے کا زاویہ کتنے درجے ہونا چاہیے؟"),
     S5,
     T("15 out of 60 is what part? Take that part of 360.", "60 میں سے 15 کتنا حصہ ہے؟ 360 کا اتنا حصہ لیں۔"),
     T("Right! 90°.", "درست! 90°"),
     T("15 ÷ 60 is a quarter, and a quarter of 360 is 90.", "15 ÷ 60 چوتھائی ہے، اور 360 کا چوتھائی 90 ہے۔"),
     common_wrong=[wrong(15, "15 is the number of children. Their slice is 15 out of 60 of 360°: 90°.", "15 بچوں کی تعداد ہے۔ ان کا ٹکڑا 360° کا 60 میں سے 15 حصہ ہے: 90°", "angle_as_count")]),
   number_question(
     "s6_angle",
     T("36 children were asked how they come to school. 12 walk. What is the angle of the 'walk' slice, in degrees?", "36 بچوں سے پوچھا گیا کہ وہ سکول کیسے آتے ہیں۔ 12 پیدل آتے ہیں۔ 'پیدل' والے ٹکڑے کا زاویہ کتنے درجے ہے؟"),
     S6,
     T("(12 ÷ 36) × 360.", "(12 ÷ 36) × 360"),
     T("Right! 120°.", "درست! 120°"),
     T("12 out of 36 is one third, and a third of 360 is 120.", "36 میں سے 12 تیسرا حصہ ہے، اور 360 کا تیسرا حصہ 120 ہے۔"),
     common_wrong=[wrong(12, "12 is the number of children. A third of 360° is 120°.", "12 بچوں کی تعداد ہے۔ 360° کا تیسرا حصہ 120° ہے۔", "angle_as_count"),
                   wrong(30, "That is 360 ÷ 12. Use the part of the total: 12 ÷ 36 is a third, so 120°.", "یہ 360 ÷ 12 ہے۔ کل کا حصہ لیں: 12 ÷ 36 تیسرا حصہ ہے، تو 120°")]),
   number_question(
     "s7_double",
     T(f"A double bar graph shows children in each class: {CLASSES_EN}. In Class 6, how many more girls are there than boys?", f"ایک دوہرا بار گراف ہر جماعت کے بچے دکھاتا ہے: {CLASSES_UR}۔ جماعت 6 میں لڑکیاں لڑکوں سے کتنی زیادہ ہیں؟"),
     S7,
     T("Take the shorter bar from the taller one.", "اونچے ستون میں سے چھوٹا نفی کریں۔"),
     T("Right! 5 more girls.", "درست! 5 لڑکیاں زیادہ"),
     T("25 − 20 = 5.", "25 − 20 = 5"),
     common_wrong=[wrong(45, "That adds them. 'How many more' is 25 − 20 = 5.", "یہ جمع ہے۔ 'کتنے زیادہ' یعنی 25 − 20 = 5", "adds_for_difference")]),
   {"id": "s8_more_boys", "type": "choice", "question_type": "apply",
    "prompt": T(f"Same graph: {CLASSES_EN}. In which class are there more boys than girls?", f"وہی گراف: {CLASSES_UR}۔ کس جماعت میں لڑکے لڑکیوں سے زیادہ ہیں؟"),
    "options": [
      opt("class_8", "Class 8", "جماعت 8", True, "Yes! Boys 24, girls 19: the boys' bar is taller.", "جی ہاں! لڑکے 24، لڑکیاں 19: لڑکوں کا ستون اونچا ہے۔"),
      opt("class_6", "Class 6", "جماعت 6", False, "In Class 6 the girls' bar is taller: 25 against 20.", "جماعت 6 میں لڑکیوں کا ستون اونچا ہے: 25 بمقابلہ 20۔"),
      opt("class_7", "Class 7", "جماعت 7", False, "In Class 7 the girls' bar is taller: 22 against 18.", "جماعت 7 میں لڑکیوں کا ستون اونچا ہے: 22 بمقابلہ 18۔"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T(f"A pie chart of 40 children shows {SPORTS_EN}. Zain says 180 children chose cricket. What went wrong?", f"40 بچوں کا ایک پائی چارٹ دکھاتا ہے {SPORTS_UR}۔ زین کہتا ہے 180 بچوں نے کرکٹ چنی۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("angle", "180° is an angle, not children. It is half the circle, so half of 40: 20.", "180° زاویہ ہے، بچے نہیں۔ یہ آدھا دائرہ ہے، تو 40 کا آدھا: 20", True,
          "Yes! Only 40 children were asked, so it can't be 180.", "جی ہاں! صرف 40 بچوں سے پوچھا گیا، تو 180 نہیں ہو سکتے۔"),
      opt("quarter", "180° is a quarter, so it is 10 children.", "180° چوتھائی ہے، تو 10 بچے ہیں۔", False,
          "A quarter is 90°. 180° is half: 20 children.", "چوتھائی 90° ہے۔ 180° آدھا ہے: 20 بچے", "not_360"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "There are only 40 children! 180° is half the circle: 20.", "بچے صرف 40 ہیں! 180° آدھا دائرہ ہے: 20", "angle_as_count"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why does a 90° slice stand for a quarter of the children? Can you teach me?",
                     "90° کا ٹکڑا بچوں کا چوتھائی کیوں ظاہر کرتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why does a 90° slice of a pie chart stand for a quarter of the total?", "اپنے الفاظ میں بتائیں: پائی چارٹ کا 90° والا ٹکڑا کل کا چوتھائی کیوں ظاہر کرتا ہے؟"),
    "key_idea": "The whole circle is 360° and stands for all the data. 90° is a quarter of 360°, so the slice is a quarter of the circle and stands for a quarter of the total.",
    "levels": {
      "got_it": "Says the whole circle is 360° (all the data) and 90° is a quarter of 360°, so the slice is a quarter of the total.",
      "partly": "Mentions 360° or a quarter, without linking the angle to the share of the data.",
      "not_yet": "Gives no reason, or just repeats the rule."},
    "keywords": [
      ["360", "whole", "circle", "پورا", "دائرہ"],
      ["quarter", "four", "چوتھائی", "چار"],
      ["total", "all", "data", "کل", "سب"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 90° is a quarter of 360°, so it is a quarter of the data.", "بہت خوب! 90°، 360° کا چوتھائی ہے، تو یہ مواد کا چوتھائی ہے۔"),
      "partly": T("Good start! Now say how 90° compares with the whole 360°.", "اچھی شروعات! اب بتائیں 90° کا پورے 360° سے کیا تعلق ہے۔"),
      "not_yet": T("Think of a round roti cut into 4 equal pieces. How many degrees is each piece?", "ایک گول روٹی سوچیں جو 4 برابر ٹکڑوں میں کٹی ہے۔ ہر ٹکڑا کتنے درجے کا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_missing",
     T("A pie chart shows what families cooked for dinner: Rice 150°, Roti 120°, Daal is the last slice. What is the angle of the Daal slice, in degrees?", "ایک پائی چارٹ دکھاتا ہے خاندانوں نے رات کو کیا پکایا: چاول 150°، روٹی 120°، دال آخری ٹکڑا ہے۔ دال کے ٹکڑے کا زاویہ کتنے درجے ہے؟"),
     S11,
     T("All the slices together make 360°.", "سب ٹکڑے مل کر 360° بنتے ہیں۔"),
     T("Right! 90°.", "درست! 90°"),
     T("150 + 120 = 270, and 360 − 270 = 90.", "150 + 120 = 270، اور 360 − 270 = 90"),
     common_wrong=[wrong(270, "270 is the two slices you know. Take it from 360: 90°.", "270 معلوم دو ٹکڑے ہیں۔ اسے 360 میں سے نفی کریں: 90°")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can read pie charts and double bar graphs now!", "اب آپ پائی چارٹ اور دوہرے بار گراف پڑھ سکتے ہیں!"),
    "text": T("A pie chart is a circle of 360° that stands for all the data. Angle of a slice = (part ÷ total) × 360. Half the circle is 180°, a quarter is 90°. A slice's angle is not the number of things: work out what part of 360° it is, then take that part of the total. A double bar graph shows two bars side by side; subtract to find how many more.",
              "پائی چارٹ 360° کا دائرہ ہے جو سارا مواد دکھاتا ہے۔ ٹکڑے کا زاویہ = (حصہ ÷ کل) × 360۔ آدھا دائرہ 180°، چوتھائی 90°۔ ٹکڑے کا زاویہ چیزوں کی تعداد نہیں: دیکھیں یہ 360° کا کتنا حصہ ہے، پھر کل کا اتنا حصہ لیں۔ دوہرے بار گراف میں دو ستون ساتھ ساتھ ہوتے ہیں؛ کتنے زیادہ کے لیے نفی کریں۔"),
    "points": [T("Whole circle = 360° = all the data.", "پورا دائرہ = 360° = سارا مواد۔"),
               T("Angle = (part ÷ total) × 360.", "زاویہ = (حصہ ÷ کل) × 360۔"),
               T("Double bars: subtract to compare.", "دوہرے ستون: موازنے کے لیے نفی کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_half", "type": "apply", "skill": SKILL, "step": number_question(
     "r_half",
     T("A pie chart shows 60 people. One slice is 180°. How many people does it stand for?", "ایک پائی چارٹ 60 لوگ دکھاتا ہے۔ ایک ٹکڑا 180° کا ہے۔ یہ کتنے لوگوں کو ظاہر کرتا ہے؟"),
     R1,
     T("180° is half the circle.", "180° آدھا دائرہ ہے۔"),
     T("Right! 30 people.", "درست! 30 لوگ"),
     T("Half of 60 is 30.", "60 کا آدھا 30 ہے۔"),
     common_wrong=[wrong(180, "180 is the angle. Half of 60 is 30.", "180 زاویہ ہے۔ 60 کا آدھا 30 ہے۔", "angle_as_count")],
     qtype=None)},
   {"id": "r_double", "type": "apply", "skill": SKILL, "step": number_question(
     "r_double",
     T("A double bar graph of fruit sold on Monday shows apples 14, oranges 9. How many more apples than oranges were sold?", "پیر کو بکنے والے پھلوں کا دوہرا بار گراف دکھاتا ہے سیب 14، مالٹے 9۔ مالٹوں سے کتنے زیادہ سیب بکے؟"),
     R2,
     T("Subtract the shorter bar.", "چھوٹا ستون نفی کریں۔"),
     T("Right! 5 more.", "درست! 5 زیادہ"),
     T("14 − 9 = 5.", "14 − 9 = 5"),
     common_wrong=[wrong(23, "That adds them. 14 − 9 = 5.", "یہ جمع ہے۔ 14 − 9 = 5", "adds_for_difference")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Data Handling unit. No textbook text or exercises were used.",
   "Pie charts and double bar graphs are drawn as pictures (slices marked with a short letter and their angle; boys' bars filled, girls' bars empty) and also written in words in each step (e.g. Cricket: 180°, Hockey: 90°, Football: 90°; Class 6: boys 20, girls 25). Drawing them on the board helps.",
   "All slices are simple fractions of the circle (half, quarter, third), so every answer is a whole number.",
   "Urdu terms to check: دائری نقشہ / پائی چارٹ (pie chart), ٹکڑا (slice), زاویہ (angle), درجہ (degree), دوہرا بار گراف (multiple/double bar graph).",
   "The numbers were worked out in content/sources/g6-maths-10/pie_charts.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
SPORT_SLICES = [(a, en[0], f"{a}°") for (en, _), a in SPORTS]      # C, H, F
SPORT_EN = "C (cricket) 180°, half the circle; H (hockey) 90°, a quarter; F (football) 90°, a quarter"
SPORT_UR = "C (کرکٹ) 180°، آدھا دائرہ؛ H (ہاکی) 90°، چوتھائی؛ F (فٹ بال) 90°، چوتھائی"


def sports_pie(shade=None):
    i = [n for _, n, _ in SPORT_SLICES].index(shade) if shade else None
    extra_en = f" The {dict(C='cricket', H='hockey', F='football')[shade]} slice is shaded." if shade else ""
    extra_ur = f" {dict(C='کرکٹ', H='ہاکی', F='فٹ بال')[shade]} والا ٹکڑا رنگا ہوا ہے۔" if shade else ""
    return pie_chart(SPORT_SLICES, f"A pie chart of favourite sports: {SPORT_EN}.{extra_en}",
                     f"پسندیدہ کھیلوں کا پائی چارٹ: {SPORT_UR}۔{extra_ur}", fill=(i,) if shade else ())


def classes_graph():
    return double_bar_graph([(b, g) for _, _, b, g in CLASSES], [en.split()[1] for en, _, _, _ in CLASSES],
        "A double bar graph with a scale from 0 to 25 in 5s. For each class two bars stand side by side: a filled bar for boys (B) and an empty bar for girls (G). "
        "Class 6: boys 20, girls 25. Class 7: boys 18, girls 22. Class 8: boys 24, girls 19. The classes are written as 6, 7 and 8 under the bars.",
        "دوہرا بار گراف، پیمانہ 0 سے 25 تک، 5 کے وقفے سے۔ ہر جماعت کے دو ستون ساتھ ساتھ ہیں: لڑکوں (B) کا بھرا ہوا ستون اور لڑکیوں (G) کا خالی ستون۔ "
        "جماعت 6: لڑکے 20، لڑکیاں 25۔ جماعت 7: لڑکے 18، لڑکیاں 22۔ جماعت 8: لڑکے 24، لڑکیاں 19۔ جماعتیں ستونوں کے نیچے 6، 7 اور 8 لکھی ہیں۔",
        top=25, step=5)


def one_slice(angle):
    return pie_chart([(angle, None, f"{angle}°"), (WHOLE - angle, None, None)],
                     f"A pie chart with one shaded slice marked {angle}°; the rest of the circle is not shaded.",
                     f"ایک پائی چارٹ جس میں ایک رنگا ہوا ٹکڑا {angle}° کا ہے؛ باقی دائرہ رنگا ہوا نہیں۔", fill=(0,))


attach(lesson, {
    "s1_hook": sports_pie(),
    "s2_foundation": squares_bar(6, 5, "C", "One bar made of 6 squares stacked up. A key beside it shows one square = 5.",
                                 "6 خانوں سے بنا ایک ستون۔ ساتھ کی کلید دکھاتی ہے: ایک خانہ = 5۔"),
    "s3_pie": sports_pie("H"),
    "s4_quarter": sports_pie("H"),
    "s7_double": classes_graph(),
    "s8_more_boys": classes_graph(),
    "s9_find_error": sports_pie("C"),
    "s11_missing": pie_chart([(150, "Ri", "150°"), (120, "Ro", "120°"), (S11, "D", "?")],
        "A pie chart of dinners: Ri (rice) 150°, Ro (roti) 120°, and the last slice D (daal) is shaded and marked with a question mark.",
        "رات کے کھانوں کا پائی چارٹ: Ri (چاول) 150°، Ro (روٹی) 120°، اور آخری ٹکڑا D (دال) رنگا ہوا ہے اور اس پر سوالیہ نشان ہے۔", fill=(2,)),
    "qb_apply": one_slice(120),
    "qb_find_error": double_bar_graph([(20, 25)], ["6"],
        "A double bar graph for Class 6 with a scale from 0 to 25 in 5s: a filled bar for boys (B) at 20 and an empty bar for girls (G) at 25, side by side.",
        "جماعت 6 کا دوہرا بار گراف، پیمانہ 0 سے 25 تک، 5 کے وقفے سے: لڑکوں (B) کا بھرا ہوا ستون 20 پر اور لڑکیوں (G) کا خالی ستون 25 پر، ساتھ ساتھ۔",
        top=25, step=5),
    "r_half": one_slice(180),
    "r_double": double_bar_graph([(14, 9)], ["Mo"],
        "A double bar graph of fruit sold on Monday (Mo) with a scale from 0 to 15 in 5s: a filled bar for apples (A) at 14 and an empty bar for oranges (O) at 9, side by side.",
        "پیر (Mo) کو بکنے والے پھلوں کا دوہرا بار گراف، پیمانہ 0 سے 15 تک، 5 کے وقفے سے: سیبوں (A) کا بھرا ہوا ستون 14 پر اور مالٹوں (O) کا خالی ستون 9 پر، ساتھ ساتھ۔",
        top=15, step=5, keys=("A", "O")),
})
write(lesson)

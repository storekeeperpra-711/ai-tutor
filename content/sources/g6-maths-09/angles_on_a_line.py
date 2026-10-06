from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, AN_TYPES, AN_LINE)

SKILL = AN_LINE
LINE, POINT = 180, 360


def missing(total, *known):
    m = total - sum(known)
    assert 0 < m < total, (total, known)
    return m


# s4: a line split into 130 and ?
S4 = missing(LINE, 130)
assert S4 == 50 and POINT - 130 == 230
# s5: three angles on a line
S5 = missing(LINE, 40, 75)
assert S5 == 65 and 40 + 75 == 115 and POINT - 115 == 245
# s6: around a point
S6 = missing(POINT, 100, 150)
assert S6 == 110 and 100 + 150 == 250
# s7: four equal angles around a point
S7 = POINT // 4
assert S7 == 90 and 4 * S7 == POINT and LINE // 4 == 45
# s8: x + x + 40 on a line
S8 = missing(LINE, 40) // 2
assert S8 == 70 and S8 + S8 + 40 == LINE and missing(LINE, 40) == 140
# s9: 70 on a line; 290 uses the full turn by mistake
assert missing(LINE, 70) == 110 and POINT - 70 == 290
# s11: four angles around a point, one is a right angle
S11 = missing(POINT, 90, 120, 85)
assert S11 == 65 and missing(POINT, 120, 85) == 155
# question bank and review
QB = missing(LINE, 75)
assert QB == 105 and POINT - 75 == 285
R1 = missing(LINE, 145)
assert R1 == 35 and POINT - 145 == 215
R2 = missing(POINT, 200, 95)
assert R2 == 65 and 200 + 95 == 295

lesson = {
 "id": "g6-maths-09-angles-on-a-line",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find missing angles using: angles on a straight line add up to 180°, and angles around a point add up to 360°.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Angles on a line and around a point", "سیدھی لکیر پر اور نقطے کے گرد زاویے"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": AN_TYPES}],
 "misconceptions": [
   {"id": "line_is_360", "description": "Uses 360° for angles on a straight line."},
   {"id": "point_is_180", "description": "Uses 180° for angles around a point."},
   {"id": "adds_known", "description": "Adds the known angles instead of taking them away from the total."},
   {"id": "forgets_an_angle", "description": "Leaves one known angle (often the right angle) out of the sum."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_point", "type": "recall", "step": {
     "id": "qb_point", "type": "choice",
     "prompt": T("The angles around a point add up to how many degrees?", "نقطے کے گرد زاویوں کا مجموعہ کتنے درجے ہوتا ہے؟"),
     "options": [
       opt("full", "360°", "360°", True, "Yes! Around a point is a full turn, 360°.", "جی ہاں! نقطے کے گرد پورا چکر ہے، 360°۔"),
       opt("half", "180°", "180°", False, "180° is a straight line, half a turn. Around a point is 360°.", "180° سیدھی لکیر، آدھا چکر ہے۔ نقطے کے گرد 360°۔", "point_is_180"),
       opt("quarter", "90°", "90°", False, "90° is a quarter turn. All the way around is 360°.", "90° چوتھائی چکر ہے۔ پورا گرد 360°۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Two angles sit on a straight line. One is 75°. What is the other, in degrees?", "سیدھی لکیر پر دو زاویے ہیں۔ ایک 75° ہے۔ دوسرا کتنے درجے ہے؟"),
     QB,
     T("180 − 75.", "180 − 75"),
     T("Right! 105°.", "درست! 105°"),
     T("180 − 75 = 105°.", "180 − 75 = 105°"),
     common_wrong=[wrong(285, "That used 360°. A straight line is 180°: 180 − 75 = 105.", "اس میں 360° لیا۔ سیدھی لکیر 180° ہے: 180 − 75 = 105", "line_is_360")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Three angles meet at a point: 120°, 140° and a missing one. Zara says the missing angle is 180 − 120 − 140. What went wrong?",
                 "ایک نقطے پر تین زاویے ملتے ہیں: 120°، 140° اور ایک نامعلوم۔ زارا کہتی ہے نامعلوم زاویہ 180 − 120 − 140 ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("full", "Around a point is 360°, not 180°. 360 − 120 − 140 = 100°.", "نقطے کے گرد 360° ہے، 180° نہیں۔ 360 − 120 − 140 = 100°", True,
           "Yes! 180° is only for a straight line.", "جی ہاں! 180° صرف سیدھی لکیر کے لیے ہے۔"),
       opt("add", "She should add: 120 + 140 = 260°.", "اسے جمع کرنا چاہیے: 120 + 140 = 260°", False,
           "Take the known angles away from 360°: 100°.", "معلوم زاویے 360° سے نفی کریں: 100°", "adds_known"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "180 − 120 − 140 is less than zero! Around a point use 360°: 100°.", "180 − 120 − 140 صفر سے کم ہے! نقطے کے گرد 360° لیں: 100°", "point_is_180"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_line", "front": T("Angles on a straight line add up to?", "سیدھی لکیر پر زاویوں کا مجموعہ؟"),
    "back": T("180°. If one is 130°, the other is 50°.", "180°۔ اگر ایک 130° ہے تو دوسرا 50°۔")},
   {"id": "f_point", "front": T("Angles around a point add up to?", "نقطے کے گرد زاویوں کا مجموعہ؟"),
    "back": T("360°, a full turn.", "360°، پورا چکر۔")},
 ],
 "home_tasks": [{"id": "h_roti", "text": T(
   "Cut a roti or a paper circle into 4 pieces from the middle (not all the same size). The angles at the middle add up to 360°. Lay two pieces with straight edges together on a line: those angles make 180°.",
   "روٹی یا کاغذ کے دائرے کو درمیان سے 4 ٹکڑوں میں کاٹیں (سب برابر نہ ہوں)۔ درمیان کے زاویوں کا مجموعہ 360° ہے۔ سیدھے کناروں والے دو ٹکڑے ایک لکیر پر رکھیں: وہ زاویے 180° بناتے ہیں۔")}],
 "glossary": [T("Straight line", "سیدھی لکیر"), T("Point", "نقطہ"), T("Full turn", "پورا چکر"), T("Missing angle", "نامعلوم زاویہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Cut a roti into slices from the middle. All the slice corners together make a full turn! How many degrees is that?",
                     "روٹی کو درمیان سے ٹکڑوں میں کاٹیں۔ سب ٹکڑوں کے کونے مل کر پورا چکر بناتے ہیں! یہ کتنے درجے ہے؟"),
    "text": T("Today we find missing angles on a straight line and around a point. First, a quick check.",
              "آج ہم سیدھی لکیر پر اور نقطے کے گرد نامعلوم زاویے نکالیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many degrees is a straight angle?", "مستقیم زاویہ کتنے درجے کا ہوتا ہے؟"),
     LINE,
     T("Half of a full turn.", "پورے چکر کا آدھا"),
     T("Right! 180°.", "درست! 180°"),
     T("A straight angle is 180°.", "مستقیم زاویہ 180° ہے۔"),
     common_wrong=[wrong(90, "90° is a right angle. A straight angle is two of them: 180°.", "90° قائمہ زاویہ ہے۔ مستقیم ان میں سے دو ہے: 180°"),
                   wrong(360, "360° is a full turn. A straight angle is half: 180°.", "360° پورا چکر ہے۔ مستقیم آدھا ہے: 180°")],
     qtype="recall", skill=AN_TYPES),
   {"id": "s3_rules", "type": "explain",
    "character": say("happy", "Two numbers to remember: 180 for a line, 360 for a point!", "دو عدد یاد رکھیں: لکیر کے لیے 180، نقطے کے لیے 360!"),
    "text": T("Angles that sit together on a straight line add up to 180°. Angles that go all the way around a point add up to 360°. To find a missing angle, take the known angles away from 180° or 360°.",
              "سیدھی لکیر پر ساتھ ساتھ زاویوں کا مجموعہ 180° ہوتا ہے۔ نقطے کے پورے گرد زاویوں کا مجموعہ 360° ہوتا ہے۔ نامعلوم زاویہ نکالنے کے لیے معلوم زاویے 180° یا 360° سے نفی کریں۔")},
   number_question(
     "s4_line",
     T("A straight line is split into two angles. One is 130°. What is the other, in degrees?", "ایک سیدھی لکیر دو زاویوں میں تقسیم ہے۔ ایک 130° ہے۔ دوسرا کتنے درجے ہے؟"),
     S4,
     T("180 − 130.", "180 − 130"),
     T("Right! 50°. Check: 130 + 50 = 180.", "درست! 50°۔ جانچ: 130 + 50 = 180"),
     T("180 − 130 = 50°.", "180 − 130 = 50°"),
     common_wrong=[wrong(230, "That used 360°. A straight line is 180°: 50°.", "اس میں 360° لیا۔ سیدھی لکیر 180° ہے: 50°", "line_is_360")]),
   number_question(
     "s5_three",
     T("Three angles sit on a straight line: 40°, 75° and a missing one. What is the missing angle?", "سیدھی لکیر پر تین زاویے ہیں: 40°، 75° اور ایک نامعلوم۔ نامعلوم زاویہ کتنا ہے؟"),
     S5,
     T("40 + 75 = 115. Then 180 − 115.", "40 + 75 = 115۔ پھر 180 − 115"),
     T("Right! 65°.", "درست! 65°"),
     T("180 − 115 = 65°.", "180 − 115 = 65°"),
     common_wrong=[wrong(115, "115 is the two known angles. Take it from 180: 65°.", "115 دو معلوم زاویے ہیں۔ 180 سے نفی کریں: 65°", "adds_known"),
                   wrong(245, "That used 360°. On a line use 180°: 65°.", "اس میں 360° لیا۔ لکیر پر 180° لیں: 65°", "line_is_360")]),
   number_question(
     "s6_point",
     T("Three angles meet around a point: 100°, 150° and a missing one. What is the missing angle?", "ایک نقطے کے گرد تین زاویے ملتے ہیں: 100°، 150° اور ایک نامعلوم۔ نامعلوم زاویہ کتنا ہے؟"),
     S6,
     T("Around a point: 360 − 100 − 150.", "نقطے کے گرد: 360 − 100 − 150"),
     T("Right! 110°.", "درست! 110°"),
     T("100 + 150 = 250, and 360 − 250 = 110°.", "100 + 150 = 250، اور 360 − 250 = 110°"),
     common_wrong=[wrong(250, "250 is the two known angles. Take it from 360: 110°.", "250 دو معلوم زاویے ہیں۔ 360 سے نفی کریں: 110°", "adds_known")]),
   number_question(
     "s7_equal",
     T("Four equal angles meet around a point. How big is each one?", "ایک نقطے کے گرد چار برابر زاویے ملتے ہیں۔ ہر ایک کتنا بڑا ہے؟"),
     S7,
     T("360 ÷ 4.", "360 ÷ 4"),
     T("Right! 90°: four right angles, like a plus sign.", "درست! 90°: چار قائمہ زاویے، جمع کے نشان کی طرح۔"),
     T("360 ÷ 4 = 90°.", "360 ÷ 4 = 90°"),
     common_wrong=[wrong(45, "That used 180°. Around a point is 360°: 360 ÷ 4 = 90°.", "اس میں 180° لیا۔ نقطے کے گرد 360° ہے: 360 ÷ 4 = 90°", "point_is_180")]),
   number_question(
     "s8_two_equal",
     T("On a straight line there is a 40° angle and two equal angles. How big is each equal angle?", "سیدھی لکیر پر ایک 40° کا زاویہ اور دو برابر زاویے ہیں۔ ہر برابر زاویہ کتنا ہے؟"),
     S8,
     T("180 − 40 = 140. Share it between two.", "180 − 40 = 140۔ اسے دو میں بانٹیں۔"),
     T("Right! 70°. Check: 70 + 70 + 40 = 180.", "درست! 70°۔ جانچ: 70 + 70 + 40 = 180"),
     T("180 − 40 = 140, and 140 ÷ 2 = 70°.", "180 − 40 = 140، اور 140 ÷ 2 = 70°"),
     common_wrong=[wrong(140, "That is both equal angles together. Each is 140 ÷ 2 = 70°.", "یہ دونوں برابر زاویے مل کر ہیں۔ ہر ایک 140 ÷ 2 = 70°")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Two angles sit on a straight line. One is 70°. Usman says the other is 360 − 70 = 290°. What went wrong?",
                "سیدھی لکیر پر دو زاویے ہیں۔ ایک 70° ہے۔ عثمان کہتا ہے دوسرا 360 − 70 = 290° ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("line", "A straight line is 180°. 180 − 70 = 110°.", "سیدھی لکیر 180° ہے۔ 180 − 70 = 110°", True,
          "Yes! 360° is for a full turn around a point.", "جی ہاں! 360° نقطے کے گرد پورے چکر کے لیے ہے۔"),
      opt("add", "He should add: 70 + 70 = 140°.", "اسے جمع کرنا چاہیے: 70 + 70 = 140°", False,
          "The two angles needn't be equal. 180 − 70 = 110°.", "دونوں زاویوں کا برابر ہونا ضروری نہیں۔ 180 − 70 = 110°"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "290° is more than a straight line! 180 − 70 = 110°.", "290° تو سیدھی لکیر سے بھی زیادہ ہے! 180 − 70 = 110°", "line_is_360"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do the angles on a straight line always add up to 180°? Can you teach me?",
                     "سیدھی لکیر پر زاویوں کا مجموعہ ہمیشہ 180° کیوں ہوتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do angles on a straight line add up to 180°?",
              "اپنے الفاظ میں بتائیں: سیدھی لکیر پر زاویوں کا مجموعہ 180° کیوں ہوتا ہے؟"),
    "key_idea": "A straight line is half a turn, a straight angle of 180°. The angles on it just split that half turn into parts, so together they still make 180°.",
    "levels": {
      "got_it": "Says a straight line is a straight angle or half a turn (180°), and the angles on it are parts of it.",
      "partly": "Says a straight line is 180° without saying the angles are its parts, or the reverse.",
      "not_yet": "Gives no reason, or says it is just the rule."},
    "keywords": [
      ["half", "straight angle", "آدھا", "مستقیم", "aadha"],
      ["turn", "360", "چکر", "chakkar"],
      ["parts", "split", "together", "حصے", "مل کر", "hissay"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The angles are just parts of one straight angle, 180°.", "بہت خوب! یہ زاویے ایک مستقیم زاویے، 180°، کے حصے ہیں۔"),
      "partly": T("Good start! Now say how the angles on the line are parts of the straight angle.", "اچھی شروعات! اب بتائیں لکیر کے زاویے مستقیم زاویے کے حصے کیسے ہیں۔"),
      "not_yet": T("A straight line is half a turn. How many degrees is half of 360°? The angles share that.", "سیدھی لکیر آدھا چکر ہے۔ 360° کا آدھا کتنا ہے؟ زاویے اسی کو بانٹتے ہیں۔")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_four",
     T("Four angles meet around a point: a right angle (90°), 120°, 85° and a missing one. What is the missing angle?",
       "ایک نقطے کے گرد چار زاویے ملتے ہیں: ایک قائمہ زاویہ (90°)، 120°، 85° اور ایک نامعلوم۔ نامعلوم زاویہ کتنا ہے؟"),
     S11,
     T("90 + 120 + 85 = 295. Then 360 − 295.", "90 + 120 + 85 = 295۔ پھر 360 − 295"),
     T("Right! 65°.", "درست! 65°"),
     T("360 − 295 = 65°.", "360 − 295 = 65°"),
     common_wrong=[wrong(155, "Don't forget the right angle: 360 − 90 − 120 − 85 = 65°.", "قائمہ زاویہ نہ بھولیں: 360 − 90 − 120 − 85 = 65°", "forgets_an_angle")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "180 for a line, 360 for a point. Well done!", "لکیر کے لیے 180، نقطے کے لیے 360۔ شاباش!"),
    "text": T("Angles on a straight line add up to 180°. Angles around a point add up to 360°. To find a missing angle, add the known ones and take the sum away from 180° or 360°. Check by adding them all back up.",
              "سیدھی لکیر پر زاویوں کا مجموعہ 180° ہے۔ نقطے کے گرد زاویوں کا مجموعہ 360° ہے۔ نامعلوم زاویے کے لیے معلوم زاویے جمع کریں اور 180° یا 360° سے نفی کریں۔ سب کو دوبارہ جمع کر کے جانچیں۔"),
    "points": [T("Straight line: 180°.", "سیدھی لکیر: 180°۔"),
               T("Around a point: 360°.", "نقطے کے گرد: 360°۔")]},
 ],
 "review_questions": [
   {"id": "r_line", "type": "apply", "skill": SKILL, "step": number_question(
     "r_line",
     T("Two angles sit on a straight line. One is 145°. What is the other?", "سیدھی لکیر پر دو زاویے ہیں۔ ایک 145° ہے۔ دوسرا کتنا ہے؟"),
     R1,
     T("180 − 145.", "180 − 145"),
     T("Right! 35°.", "درست! 35°"),
     T("180 − 145 = 35°.", "180 − 145 = 35°"),
     common_wrong=[wrong(215, "Use 180° for a line: 35°.", "لکیر کے لیے 180° لیں: 35°", "line_is_360")],
     qtype=None)},
   {"id": "r_point", "type": "apply", "skill": SKILL, "step": number_question(
     "r_point",
     T("Three angles meet around a point: 200°, 95° and a missing one. What is the missing angle?", "ایک نقطے کے گرد تین زاویے ہیں: 200°، 95° اور ایک نامعلوم۔ نامعلوم زاویہ کتنا ہے؟"),
     R2,
     T("360 − 200 − 95.", "360 − 200 − 95"),
     T("Right! 65°.", "درست! 65°"),
     T("200 + 95 = 295, and 360 − 295 = 65°.", "200 + 95 = 295، اور 360 − 295 = 65°"),
     common_wrong=[wrong(295, "Take the known angles from 360: 65°.", "معلوم زاویے 360 سے نفی کریں: 65°", "adds_known")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Angles unit. No textbook text or exercises were used.",
   "The two totals are tied to turns: a straight line is half a turn (180°), all the way round is a full turn (360°). The most common slip is using the wrong total, so several wrong answers catch it.",
   "Urdu terms to check: سیدھی لکیر (straight line), نقطہ (point), پورا چکر (full turn), نامعلوم زاویہ (missing angle).",
   "The numbers were worked out in content/sources/g6-maths-09/angles_on_a_line.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

from common import (T, opt, say, wrong, number_question, kind_of, kind_question, write,
                    REF, REVIEW, PA_TRIANGLE, AN_TYPES)

SKILL = AN_TYPES

# s4, s5, s7: one angle of each kind the lesson names
assert kind_of(35) == "acute" and kind_of(120) == "obtuse" and kind_of(250) == "reflex"
# s6: a straight angle is two right angles
S6 = 180 // 90
assert S6 == 2 and 90 * S6 == 180
# s8: at 3 o'clock the hands are a quarter turn apart; each hour is 360 / 12 = 30 degrees
S8 = 3 * (360 // 12)
assert S8 == 90 and kind_of(S8) == "right"
# s9: 180 is straight, not obtuse
assert kind_of(180) == "straight"
# s11: at 6 o'clock the hands point opposite ways
S11 = 6 * (360 // 12)
assert S11 == 180 and kind_of(S11) == "straight"
# question bank and review
assert kind_of(160) == "obtuse" and kind_of(89) == "acute" and kind_of(300) == "reflex"
assert kind_of(95) == "obtuse"

TYPE_MIS = {"acute": "big_is_acute", "right": "near_90_is_right"}

lesson = {
 "id": "g6-maths-09-types-of-angles",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Name acute, right, obtuse, straight and reflex angles from their size in degrees.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Types of angles", "زاویوں کی اقسام"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": PA_TRIANGLE}],
 "misconceptions": [
   {"id": "straight_is_obtuse", "description": "Calls a 180° angle obtuse instead of straight."},
   {"id": "big_is_acute", "description": "Mixes up acute and obtuse, calling a wide angle acute."},
   {"id": "near_90_is_right", "description": "Calls any angle close to 90° a right angle."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_right", "type": "recall", "step": {
     "id": "qb_right", "type": "choice",
     "prompt": T("How many degrees is a right angle?", "قائمہ زاویہ کتنے درجے کا ہوتا ہے؟"),
     "options": [
       opt("ninety", "90°", "90°", True, "Yes! A right angle is a square corner, 90°.", "جی ہاں! قائمہ زاویہ چوکور کونا ہے، 90°۔"),
       opt("hundred", "100°", "100°", False, "A right angle is exactly 90°.", "قائمہ زاویہ بالکل 90° ہوتا ہے۔"),
       opt("oneeighty", "180°", "180°", False, "180° is a straight angle. A right angle is half of it: 90°.", "180° مستقیم زاویہ ہے۔ قائمہ اس کا آدھا ہے: 90°۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": kind_question(
     "qb_apply", 160,
     T("What kind of angle is 160°?", "160° کس قسم کا زاویہ ہے؟"),
     qtype=None, mis=TYPE_MIS)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Hina says 95° is a right angle because it is close to 90°. What went wrong?", "حنا کہتی ہے 95° قائمہ زاویہ ہے کیونکہ یہ 90° کے قریب ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("exact", "A right angle is exactly 90°. 95° is obtuse.", "قائمہ زاویہ بالکل 90° ہوتا ہے۔ 95° منفرجہ ہے۔", True,
           "Yes! Even 1° more than 90° makes it obtuse.", "جی ہاں! 90° سے 1° زیادہ بھی منفرجہ ہے۔"),
       opt("acute", "95° is acute.", "95° حادہ ہے۔", False,
           "Acute is less than 90°. 95° is more, so it is obtuse.", "حادہ 90° سے کم ہوتا ہے۔ 95° زیادہ ہے، اس لیے منفرجہ ہے۔", "big_is_acute"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Right angles are exactly 90°. 95° is obtuse.", "قائمہ زاویہ بالکل 90° ہوتا ہے۔ 95° منفرجہ ہے۔", "near_90_is_right"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_kinds", "front": T("The five kinds of angle?", "زاویوں کی پانچ اقسام؟"),
    "back": T("Acute (less than 90°), right (90°), obtuse (90° to 180°), straight (180°), reflex (180° to 360°).",
              "حادہ (90° سے کم)، قائمہ (90°)، منفرجہ (90° سے 180°)، مستقیم (180°)، منعکس (180° سے 360°)۔")},
   {"id": "f_turn", "front": T("How many degrees in a full turn?", "پورے چکر میں کتنے درجے؟"),
    "back": T("360°. Half a turn is 180°, a quarter turn is 90°.", "360°۔ آدھا چکر 180°، چوتھائی چکر 90°۔")},
 ],
 "home_tasks": [{"id": "h_hunt", "text": T(
   "Go on an angle hunt at home. Find one right angle (a book corner), one acute angle and one obtuse angle (an open door or scissors). Tell someone at home what kind each one is.",
   "گھر میں زاویے تلاش کریں۔ ایک قائمہ زاویہ (کتاب کا کونا)، ایک حادہ اور ایک منفرجہ زاویہ (کھلا دروازہ یا قینچی) ڈھونڈیں۔ گھر والوں کو بتائیں ہر ایک کس قسم کا ہے۔")}],
 "glossary": [T("Angle", "زاویہ"), T("Degree", "درجہ"), T("Acute angle", "حادہ زاویہ"), T("Right angle", "قائمہ زاویہ"),
              T("Obtuse angle", "منفرجہ زاویہ"), T("Straight angle", "مستقیم زاویہ"), T("Reflex angle", "منعکس زاویہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Open a door a little, then wider, then all the way. The turn gets bigger! That turn is an angle.",
                     "دروازہ تھوڑا کھولیں، پھر زیادہ، پھر پورا۔ گھماؤ بڑا ہوتا جاتا ہے! یہ گھماؤ زاویہ ہے۔"),
    "text": T("An angle measures how far something turns. We measure it in degrees (°). A full turn is 360°. First, a quick check.",
              "زاویہ بتاتا ہے کوئی چیز کتنا گھومی۔ ہم اسے درجوں (°) میں ناپتے ہیں۔ پورا چکر 360° ہے۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": PA_TRIANGLE,
    "prompt": T("In the triangle lesson, the height met the base at a square corner. What is that corner called?",
                "مثلث کے سبق میں اونچائی قاعدے سے چوکور کونے پر ملی۔ اس کونے کو کیا کہتے ہیں؟"),
    "options": [
      opt("right", "A right angle", "قائمہ زاویہ", True, "Yes! A square corner is a right angle.", "جی ہاں! چوکور کونا قائمہ زاویہ ہے۔"),
      opt("slant", "A slanted side", "ترچھا ضلع", False, "The height is not slanted. It meets the base at a right angle.", "اونچائی ترچھی نہیں۔ یہ قاعدے سے قائمہ زاویے پر ملتی ہے۔"),
      opt("base", "The base", "قاعدہ", False, "The base is a side. The square corner is a right angle.", "قاعدہ ایک ضلع ہے۔ چوکور کونا قائمہ زاویہ ہے۔"),
    ]},
   {"id": "s3_kinds", "type": "explain",
    "character": say("happy", "Five kinds of angle, and the right angle, 90°, is the one to compare with!",
                     "زاویوں کی پانچ اقسام، اور قائمہ زاویہ، 90°، سے موازنہ کریں!"),
    "text": T("Acute: less than 90° (a narrow opening). Right: exactly 90° (a square corner). Obtuse: between 90° and 180° (wider than a corner). Straight: exactly 180° (a straight line). Reflex: between 180° and 360° (more than half a turn).",
              "حادہ: 90° سے کم (تنگ کھلاؤ)۔ قائمہ: بالکل 90° (چوکور کونا)۔ منفرجہ: 90° اور 180° کے درمیان (کونے سے زیادہ کھلا)۔ مستقیم: بالکل 180° (سیدھی لکیر)۔ منعکس: 180° اور 360° کے درمیان (آدھے چکر سے زیادہ)۔")},
   kind_question("s4_acute", 35, T("What kind of angle is 35°?", "35° کس قسم کا زاویہ ہے؟"), mis=TYPE_MIS),
   kind_question("s5_obtuse", 120, T("A door is opened 120°. What kind of angle is that?", "دروازہ 120° کھولا گیا۔ یہ کس قسم کا زاویہ ہے؟"), mis=TYPE_MIS),
   number_question(
     "s6_two_rights",
     T("How many right angles make one straight angle?", "کتنے قائمہ زاویے مل کر ایک مستقیم زاویہ بناتے ہیں؟"),
     S6,
     T("A straight angle is 180°. A right angle is 90°.", "مستقیم زاویہ 180° ہے۔ قائمہ زاویہ 90° ہے۔"),
     T("Right! 90° + 90° = 180°.", "درست! 90° + 90° = 180°"),
     T("180 ÷ 90 = 2 right angles.", "180 ÷ 90 = 2 قائمہ زاویے"),
     common_wrong=[wrong(4, "Four right angles make a full turn, 360°. A straight angle is 180°: two.", "چار قائمہ زاویے پورا چکر، 360°، بناتے ہیں۔ مستقیم 180° ہے: دو۔")]),
   kind_question("s7_reflex", 250, T("What kind of angle is 250°?", "250° کس قسم کا زاویہ ہے؟"), mis=TYPE_MIS),
   number_question(
     "s8_clock",
     T("A clock shows 3 o'clock. How many degrees apart are the two hands? (Each hour mark is 30° apart.)",
       "گھڑی 3 بجا رہی ہے۔ دونوں سوئیوں کے درمیان کتنے درجے ہیں؟ (ہر گھنٹے کا نشان 30° کے فاصلے پر ہے۔)"),
     S8,
     T("3 hour marks, 30° each.", "3 گھنٹے کے نشان، ہر ایک 30°"),
     T("Right! 90°, a right angle.", "درست! 90°، قائمہ زاویہ"),
     T("3 × 30° = 90°.", "3 × 30° = 90°"),
     common_wrong=[wrong(3, "3 is the hour. Each hour is 30°: 3 × 30 = 90°.", "3 گھنٹہ ہے۔ ہر گھنٹہ 30°: 3 × 30 = 90°"),
                   wrong(15, "That is minutes. Use degrees: 3 × 30 = 90°.", "یہ منٹ ہیں۔ درجے لیں: 3 × 30 = 90°")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal says 180° is an obtuse angle because it is more than 90°. What went wrong?",
                "بلال کہتا ہے 180° منفرجہ زاویہ ہے کیونکہ یہ 90° سے زیادہ ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("straight", "180° is exactly a straight line, so it is a straight angle.", "180° بالکل سیدھی لکیر ہے، اس لیے مستقیم زاویہ ہے۔", True,
          "Yes! Obtuse angles are less than 180°. Exactly 180° is straight.", "جی ہاں! منفرجہ زاویہ 180° سے کم ہوتا ہے۔ بالکل 180° مستقیم ہے۔"),
      opt("reflex", "180° is reflex.", "180° منعکس ہے۔", False,
          "Reflex is more than 180°. Exactly 180° is straight.", "منعکس 180° سے زیادہ ہوتا ہے۔ بالکل 180° مستقیم ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Obtuse stops before 180°. 180° is a straight angle.", "منفرجہ 180° سے پہلے رک جاتا ہے۔ 180° مستقیم زاویہ ہے۔", "straight_is_obtuse"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Is 100° acute or obtuse? How can you tell? Can you teach me?",
                     "100° حادہ ہے یا منفرجہ؟ آپ کیسے بتاتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: is 100° acute or obtuse, and how do you know?",
              "اپنے الفاظ میں بتائیں: 100° حادہ ہے یا منفرجہ، اور آپ کو کیسے پتا؟"),
    "key_idea": "100° is obtuse because it is more than a right angle (90°) but less than a straight angle (180°). Acute angles are less than 90°.",
    "levels": {
      "got_it": "Says 100° is obtuse and compares it with 90° (and ideally 180°).",
      "partly": "Says obtuse without comparing with 90°, or compares correctly but names the wrong type.",
      "not_yet": "Says acute, or gives no reason."},
    "keywords": [
      ["obtuse", "منفرجہ", "munfarja"],
      ["90", "right", "قائمہ", "qaima"],
      ["more", "bigger", "greater", "زیادہ", "بڑا", "zyada"]],
    "fallback_feedback": {
      "got_it": T("Well explained! More than 90° but less than 180° means obtuse.", "بہت خوب! 90° سے زیادہ لیکن 180° سے کم کا مطلب منفرجہ۔"),
      "partly": T("Good start! Now compare 100° with a right angle, 90°.", "اچھی شروعات! اب 100° کا موازنہ قائمہ زاویے، 90°، سے کریں۔"),
      "not_yet": T("Is 100° bigger or smaller than a square corner, 90°? Acute angles are smaller than 90°.", "کیا 100° چوکور کونے، 90°، سے بڑا ہے یا چھوٹا؟ حادہ زاویے 90° سے چھوٹے ہوتے ہیں۔")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_six",
     T("A clock shows 6 o'clock. How many degrees apart are the two hands?", "گھڑی 6 بجا رہی ہے۔ دونوں سوئیوں کے درمیان کتنے درجے ہیں؟"),
     S11,
     T("6 hour marks, 30° each.", "6 گھنٹے کے نشان، ہر ایک 30°"),
     T("Right! 180°, a straight angle: the hands make a straight line.", "درست! 180°، مستقیم زاویہ: سوئیاں سیدھی لکیر بناتی ہیں۔"),
     T("6 × 30° = 180°.", "6 × 30° = 180°"),
     common_wrong=[wrong(6, "6 is the hour. Each hour is 30°: 6 × 30 = 180°.", "6 گھنٹہ ہے۔ ہر گھنٹہ 30°: 6 × 30 = 180°"),
                   wrong(30, "That is one hour. Six hours: 6 × 30 = 180°.", "یہ ایک گھنٹہ ہے۔ چھ گھنٹے: 6 × 30 = 180°")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can name every angle now!", "اب آپ ہر زاویے کا نام بتا سکتے ہیں!"),
    "text": T("Compare every angle with 90° and 180°. Less than 90°: acute. Exactly 90°: right. Between 90° and 180°: obtuse. Exactly 180°: straight. More than 180°: reflex. A full turn is 360°.",
              "ہر زاویے کا موازنہ 90° اور 180° سے کریں۔ 90° سے کم: حادہ۔ بالکل 90°: قائمہ۔ 90° اور 180° کے درمیان: منفرجہ۔ بالکل 180°: مستقیم۔ 180° سے زیادہ: منعکس۔ پورا چکر 360° ہے۔"),
    "points": [T("Right angle = 90°, straight angle = 180°.", "قائمہ = 90°، مستقیم = 180°۔"),
               T("Full turn = 360°.", "پورا چکر = 360°۔")]},
 ],
 "review_questions": [
   {"id": "r_acute", "type": "apply", "skill": SKILL, "step": kind_question(
     "r_acute", 89, T("What kind of angle is 89°?", "89° کس قسم کا زاویہ ہے؟"), qtype=None, mis=TYPE_MIS)},
   {"id": "r_reflex", "type": "recall", "skill": SKILL, "step": kind_question(
     "r_reflex", 300, T("What kind of angle is 300°?", "300° کس قسم کا زاویہ ہے؟"), qtype=None, mis=TYPE_MIS)},
 ],
 "teacher_notes": [
   "Written fresh for the Angles unit. No textbook text or exercises were used.",
   "There are no pictures yet, so every angle is given in degrees or as a clock or door. Doors, book corners and clock hands make the sizes concrete; the home task is an angle hunt.",
   "Urdu terms to check: زاویہ (angle), درجہ (degree), حادہ (acute), قائمہ (right), منفرجہ (obtuse), مستقیم (straight), منعکس (reflex).",
   "The numbers were worked out in content/sources/g6-maths-09/angle_types.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

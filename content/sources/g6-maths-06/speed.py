from fractions import Fraction as F

from common import (T, opt, say, wrong, number_question, write,
                    BOOK, REVIEW, RATIO_RATE)

SKILL = "maths.ratio.speed"


def whole(x):
    x = F(x)
    assert x.denominator == 1, x
    return int(x)


def kmh_to_ms(v):
    """km/h to m/s: × 1000 m, ÷ 3600 s (the same as × 5/18)."""
    return whole(F(v) * 1000 / 3600)


def ms_to_kmh(v):
    return whole(F(v) * 3600 / 1000)


# s2: 150 km in 3 hours
S2 = whole(F(150, 3))
assert S2 == 50
# s4: 60 km/h for 4 hours (dividing: 15)
S4 = 60 * 4
assert S4 == 240
# s5: 300 km at 75 km/h (multiplying: 22,500)
S5 = whole(F(300, 75))
assert S5 == 4
# s7: 36 km/h in m/s (only km to m: 36,000)
S7 = kmh_to_ms(36)
assert S7 == 10 and kmh_to_ms(36) == whole(F(36) * F(5, 18))
# s8: 20 m/s in km/h (only seconds to minutes: 1,200)
S8 = ms_to_kmh(20)
assert S8 == 72 and 20 * 60 == 1200
# s9: 54 km/h is 15 m/s
assert kmh_to_ms(54) == 15
# s10: cheetah 30 m/s = 108 km/h, faster than a car at 90 km/h
assert ms_to_kmh(30) == 108 > 90
# s11: 18 km/h in m/s
S11 = kmh_to_ms(18)
assert S11 == 5
# question bank: 72 km/h in m/s
QB = kmh_to_ms(72)
assert QB == 20
# review: 45 km/h for 2 hours; 25 m/s in km/h
R1 = 45 * 2
assert R1 == 90
R2 = ms_to_kmh(25)
assert R2 == 90

lesson = {
 "id": "g6-maths-06-speed",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Use speed = distance ÷ time to find speed, distance or time, and change speeds between km/h and m/s.", "textbook": f"{BOOK}, Speed, distance and time"}],
 "skills": [SKILL],
 "title": T("Speed, distance and time", "رفتار، فاصلہ اور وقت"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": RATIO_RATE}],
 "misconceptions": [
   {"id": "wrong_operation", "description": "Divides when the distance is needed, or multiplies when the time is needed."},
   {"id": "half_conversion", "description": "Changes only the kilometres or only the hours when converting km/h and m/s."},
   {"id": "formula_upside_down", "description": "Writes time = speed ÷ distance."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_formula", "type": "recall", "step": {
     "id": "qb_formula", "type": "choice",
     "prompt": T("Speed = …", "رفتار = …"),
     "options": [
       opt("d_over_t", "distance ÷ time", "فاصلہ ÷ وقت", True, "Yes! Like km per hour.", "جی ہاں! جیسے کلومیٹر فی گھنٹہ۔"),
       opt("t_over_d", "time ÷ distance", "وقت ÷ فاصلہ", False, "Upside down. km per hour is km ÷ hours.", "اُلٹا ہے۔ کلومیٹر فی گھنٹہ یعنی کلومیٹر ÷ گھنٹے۔", "formula_upside_down"),
       opt("d_times_t", "distance × time", "فاصلہ × وقت", False, "Speed is distance for each hour: divide.", "رفتار ہر گھنٹے کا فاصلہ ہے: تقسیم کریں۔", "wrong_operation"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A car goes at 72 km/h. What is its speed in m/s?", "ایک گاڑی 72 کلومیٹر فی گھنٹہ کی رفتار سے چلتی ہے۔ اس کی رفتار میٹر فی سیکنڈ میں کیا ہے؟"),
     QB,
     T("× 1000, then ÷ 3600 (or × 5/18).", "× 1000، پھر ÷ 3600 (یا × 5/18)"),
     T("Right! 72 × 5 ÷ 18 = 20 m/s.", "درست! 72 × 5 ÷ 18 = 20 میٹر فی سیکنڈ"),
     T("72,000 m in 3,600 s: 72,000 ÷ 3,600 = 20.", "3,600 سیکنڈ میں 72,000 میٹر: 72,000 ÷ 3,600 = 20"),
     common_wrong=[wrong(72000, "That changes only km to m. Also ÷ 3600 for seconds: 20.", "یہ صرف کلومیٹر کو میٹر بناتا ہے۔ سیکنڈ کے لیے ÷ 3600 بھی: 20", "half_conversion")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Sana wants the time for 200 km at 50 km/h. She writes time = 50 ÷ 200. What is wrong?", "ثنا 50 کلومیٹر فی گھنٹہ پر 200 کلومیٹر کا وقت نکالنا چاہتی ہے۔ وہ لکھتی ہے وقت = 50 ÷ 200۔ کیا غلطی ہے؟"),
     "options": [
       opt("flip", "Time = distance ÷ speed = 200 ÷ 50 = 4 hours.", "وقت = فاصلہ ÷ رفتار = 200 ÷ 50 = 4 گھنٹے", True,
           "Yes! How many 50s fit in 200?", "جی ہاں! 200 میں 50 کتنی بار آتا ہے؟"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "50 ÷ 200 is a quarter: far too short. 200 ÷ 50 = 4 hours.", "50 ÷ 200 چوتھائی ہے: بہت کم۔ 200 ÷ 50 = 4 گھنٹے", "formula_upside_down"),
       opt("times", "She should multiply: 10,000 hours.", "اسے ضرب دینی چاہیے: 10,000 گھنٹے", False,
           "Multiplying speed by distance means nothing here. 200 ÷ 50 = 4.", "رفتار کو فاصلے سے ضرب کا یہاں کوئی مطلب نہیں۔ 200 ÷ 50 = 4", "wrong_operation"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_triangle", "front": T("Speed, distance, time?", "رفتار، فاصلہ، وقت؟"),
    "back": T("speed = distance ÷ time; distance = speed × time; time = distance ÷ speed.", "رفتار = فاصلہ ÷ وقت؛ فاصلہ = رفتار × وقت؛ وقت = فاصلہ ÷ رفتار")},
   {"id": "f_convert", "front": T("km/h to m/s?", "کلومیٹر فی گھنٹہ سے میٹر فی سیکنڈ؟"),
    "back": T("× 1000 ÷ 3600, which is × 5/18: 36 km/h = 10 m/s.", "× 1000 ÷ 3600، یعنی × 5/18: 36 کلومیٹر فی گھنٹہ = 10 میٹر فی سیکنڈ")},
 ],
 "home_tasks": [{"id": "h_walk", "text": T(
   "Walk 100 steps and ask someone to time you in seconds. If one step is about half a metre, how many metres per second did you walk?",
   "100 قدم چلیں اور کسی سے سیکنڈ میں وقت نوٹ کروائیں۔ اگر ایک قدم تقریباً آدھا میٹر ہو تو آپ کتنے میٹر فی سیکنڈ چلے؟")}],
 "glossary": [T("Speed", "رفتار"), T("Distance", "فاصلہ"), T("km/h (kilometres per hour)", "کلومیٹر فی گھنٹہ"), T("m/s (metres per second)", "میٹر فی سیکنڈ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A cheetah runs at 30 metres per second. A car goes 90 km per hour. Which is faster?",
                     "چیتا 30 میٹر فی سیکنڈ دوڑتا ہے۔ گاڑی 90 کلومیٹر فی گھنٹہ چلتی ہے۔ کون تیز ہے؟"),
    "text": T("Today we find speed, distance and time, and change km/h to m/s. First, a rate.", "آج ہم رفتار، فاصلہ اور وقت نکالیں گے، اور کلومیٹر فی گھنٹہ کو میٹر فی سیکنڈ میں بدلیں گے۔ پہلے ایک شرح۔")},
   number_question(
     "s2_foundation",
     T("A van goes 150 km in 3 hours. How many km per hour is that?", "ایک وین 3 گھنٹوں میں 150 کلومیٹر چلتی ہے۔ یہ کتنے کلومیٹر فی گھنٹہ ہیں؟"),
     S2,
     T("Divide by the hours.", "گھنٹوں سے تقسیم کریں۔"),
     T("Right! 50 km/h.", "درست! 50 کلومیٹر فی گھنٹہ"),
     T("150 ÷ 3 = 50 km per hour.", "150 ÷ 3 = 50 کلومیٹر فی گھنٹہ"),
     common_wrong=[wrong(450, "Divide, don't multiply: 150 ÷ 3 = 50.", "ضرب نہیں، تقسیم کریں: 150 ÷ 3 = 50", "wrong_operation")],
     qtype="recall", skill=RATIO_RATE),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Speed is a rate: distance for each hour or each second. One rule gives all three!", "رفتار ایک شرح ہے: ہر گھنٹے یا ہر سیکنڈ کا فاصلہ۔ ایک اصول سے تینوں!"),
    "text": T("Speed = distance ÷ time. So distance = speed × time, and time = distance ÷ speed. Speed can be in km/h or in m/s. To change km/h to m/s: 1 km = 1000 m and 1 hour = 3600 s, so multiply by 1000 and divide by 3600 (the same as × 5/18): 36 km/h = 10 m/s. To change m/s to km/h, multiply by 3600 and divide by 1000 (× 18/5).",
              "رفتار = فاصلہ ÷ وقت۔ اس لیے فاصلہ = رفتار × وقت، اور وقت = فاصلہ ÷ رفتار۔ رفتار کلومیٹر فی گھنٹہ (km/h) یا میٹر فی سیکنڈ (m/s) میں ہو سکتی ہے۔ km/h کو m/s میں بدلنے کے لیے: 1 کلومیٹر = 1000 میٹر اور 1 گھنٹہ = 3600 سیکنڈ، تو 1000 سے ضرب دیں اور 3600 سے تقسیم کریں (یعنی × 5/18): 36 km/h = 10 m/s۔ m/s کو km/h میں بدلنے کے لیے 3600 سے ضرب اور 1000 سے تقسیم کریں (× 18/5)۔")},
   number_question(
     "s4_distance",
     T("A car drives at 60 km/h for 4 hours. How far does it go, in km?", "ایک گاڑی 4 گھنٹے 60 کلومیٹر فی گھنٹہ کی رفتار سے چلتی ہے۔ وہ کتنے کلومیٹر جاتی ہے؟"),
     S4,
     T("60 km each hour, for 4 hours.", "ہر گھنٹے 60 کلومیٹر، 4 گھنٹے تک۔"),
     T("Right! 60 × 4 = 240 km.", "درست! 60 × 4 = 240 کلومیٹر"),
     T("distance = speed × time = 60 × 4 = 240.", "فاصلہ = رفتار × وقت = 60 × 4 = 240"),
     common_wrong=[wrong(15, "For distance, multiply: 60 × 4 = 240.", "فاصلے کے لیے ضرب دیں: 60 × 4 = 240", "wrong_operation")]),
   number_question(
     "s5_time",
     T("Lahore to Islamabad on the motorway is about 300 km. A bus goes at 75 km/h. How many hours does it take?", "موٹروے پر لاہور سے اسلام آباد تقریباً 300 کلومیٹر ہے۔ ایک بس 75 کلومیٹر فی گھنٹہ چلتی ہے۔ کتنے گھنٹے لگیں گے؟"),
     S5,
     T("How many 75s make 300?", "300 میں 75 کتنی بار آتا ہے؟"),
     T("Right! 300 ÷ 75 = 4 hours.", "درست! 300 ÷ 75 = 4 گھنٹے"),
     T("time = distance ÷ speed = 300 ÷ 75 = 4.", "وقت = فاصلہ ÷ رفتار = 300 ÷ 75 = 4"),
     common_wrong=[wrong(22500, "For time, divide: 300 ÷ 75 = 4.", "وقت کے لیے تقسیم کریں: 300 ÷ 75 = 4", "wrong_operation")]),
   {"id": "s6_units", "type": "choice",
    "prompt": T("To change km/h to m/s we use two facts. Which pair is right?", "km/h کو m/s میں بدلنے کے لیے ہم دو حقائق استعمال کرتے ہیں۔ کون سی جوڑی درست ہے؟"),
    "options": [
      opt("right", "1 km = 1000 m and 1 hour = 3600 s", "1 کلومیٹر = 1000 میٹر اور 1 گھنٹہ = 3600 سیکنڈ", True,
          "Yes! 60 minutes × 60 seconds = 3600 seconds.", "جی ہاں! 60 منٹ × 60 سیکنڈ = 3600 سیکنڈ"),
      opt("sixty", "1 km = 1000 m and 1 hour = 60 s", "1 کلومیٹر = 1000 میٹر اور 1 گھنٹہ = 60 سیکنڈ", False,
          "60 seconds is a minute. An hour is 60 × 60 = 3600 s.", "60 سیکنڈ ایک منٹ ہے۔ گھنٹہ 60 × 60 = 3600 سیکنڈ", "half_conversion"),
      opt("hundred", "1 km = 100 m and 1 hour = 3600 s", "1 کلومیٹر = 100 میٹر اور 1 گھنٹہ = 3600 سیکنڈ", False,
          "A kilometre is 1000 metres.", "ایک کلومیٹر 1000 میٹر کا ہے۔"),
    ]},
   number_question(
     "s7_to_ms",
     T("Change 36 km/h to m/s.", "36 کلومیٹر فی گھنٹہ کو میٹر فی سیکنڈ میں بدلیں۔"),
     S7,
     T("36 × 1000 ÷ 3600, or 36 × 5 ÷ 18.", "36 × 1000 ÷ 3600، یا 36 × 5 ÷ 18"),
     T("Right! 10 m/s.", "درست! 10 میٹر فی سیکنڈ"),
     T("36,000 m in 3,600 s: 36,000 ÷ 3,600 = 10.", "3,600 سیکنڈ میں 36,000 میٹر: 36,000 ÷ 3,600 = 10"),
     common_wrong=[wrong(36000, "That changes km to m only. Also ÷ 3600 for the seconds: 10.", "یہ صرف کلومیٹر کو میٹر بناتا ہے۔ سیکنڈ کے لیے ÷ 3600 بھی: 10", "half_conversion")]),
   number_question(
     "s8_to_kmh",
     T("Change 20 m/s to km/h.", "20 میٹر فی سیکنڈ کو کلومیٹر فی گھنٹہ میں بدلیں۔"),
     S8,
     T("20 × 3600 ÷ 1000, or 20 × 18 ÷ 5.", "20 × 3600 ÷ 1000، یا 20 × 18 ÷ 5"),
     T("Right! 72 km/h.", "درست! 72 کلومیٹر فی گھنٹہ"),
     T("In an hour: 20 × 3600 = 72,000 m = 72 km.", "ایک گھنٹے میں: 20 × 3600 = 72,000 میٹر = 72 کلومیٹر"),
     common_wrong=[wrong(1200, "× 60 gives metres per minute. An hour is 3600 s: 72,000 m = 72 km.", "× 60 سے میٹر فی منٹ ملتا ہے۔ گھنٹہ 3600 سیکنڈ: 72,000 میٹر = 72 کلومیٹر", "half_conversion")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal changes 54 km/h to m/s. He writes 54 × 1000 = 54,000 m/s. What is wrong?", "بلال 54 km/h کو m/s میں بدلتا ہے۔ وہ لکھتا ہے 54 × 1000 = 54,000 m/s۔ کیا غلطی ہے؟"),
    "options": [
      opt("seconds", "He forgot to divide by 3600 for the seconds: 15 m/s.", "وہ سیکنڈ کے لیے 3600 سے تقسیم کرنا بھول گیا: 15 m/s", True,
          "Yes! 54,000 ÷ 3600 = 15.", "جی ہاں! 54,000 ÷ 3600 = 15"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "54,000 m/s is faster than a rocket! Divide by 3600: 15 m/s.", "54,000 m/s تو راکٹ سے بھی تیز ہے! 3600 سے تقسیم کریں: 15 m/s", "half_conversion"),
      opt("hundred", "He should multiply by 100.", "اسے 100 سے ضرب دینی چاہیے۔", False,
          "1 km is 1000 m, that part is right. He forgot ÷ 3600: 15.", "1 کلومیٹر 1000 میٹر ہے، یہ ٹھیک ہے۔ وہ ÷ 3600 بھول گیا: 15"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "30 is smaller than 90, so the car wins? But the units are different! Help me compare.",
                     "30، 90 سے چھوٹا ہے، تو گاڑی جیتی؟ مگر اکائیاں مختلف ہیں! موازنہ کرنے میں مدد کریں۔"),
    "task": T("A cheetah runs at 30 m/s. A car goes at 90 km/h. Which is faster? Explain how you compared them.", "چیتا 30 m/s کی رفتار سے دوڑتا ہے۔ گاڑی 90 km/h کی رفتار سے چلتی ہے۔ کون تیز ہے؟ بتائیں آپ نے موازنہ کیسے کیا۔"),
    "key_idea": "Change to the same unit first. 30 m/s × 18/5 = 108 km/h, which is more than 90 km/h, so the cheetah is faster. (Or 90 km/h = 25 m/s, less than 30 m/s.)",
    "levels": {
      "got_it": "Changes one speed to the other unit (108 km/h or 25 m/s) and says the cheetah is faster.",
      "partly": "Says the cheetah is faster without converting, or converts but makes a slip.",
      "not_yet": "Says the car is faster because 90 > 30, or gives no reason."},
    "keywords": [
      ["108"],
      ["25"],
      ["same unit", "convert", "change", "بدل", "ایک جیسی"],
      ["cheetah", "چیتا"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Same units first: the cheetah wins.", "بہت خوب! پہلے ایک جیسی اکائیاں: چیتا جیتا۔"),
      "partly": T("Good start! Now change 30 m/s into km/h to prove it.", "اچھی شروعات! اب ثابت کرنے کے لیے 30 m/s کو km/h میں بدلیں۔"),
      "not_yet": T("m/s and km/h are different units. Change 30 m/s to km/h first.", "m/s اور km/h مختلف اکائیاں ہیں۔ پہلے 30 m/s کو km/h میں بدلیں۔")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_cyclist",
     T("Hamza cycles to school at 18 km/h. What is his speed in m/s?", "حمزہ 18 km/h کی رفتار سے سائیکل پر اسکول جاتا ہے۔ اس کی رفتار m/s میں کیا ہے؟"),
     S11,
     T("18 × 5 ÷ 18.", "18 × 5 ÷ 18"),
     T("Right! 5 m/s.", "درست! 5 میٹر فی سیکنڈ"),
     T("18,000 m in 3,600 s: 18,000 ÷ 3,600 = 5.", "3,600 سیکنڈ میں 18,000 میٹر: 18,000 ÷ 3,600 = 5"),
     common_wrong=[wrong(18000, "Also divide by 3600 for the seconds: 5.", "سیکنڈ کے لیے 3600 سے تقسیم بھی کریں: 5", "half_conversion"),
                   wrong(300, "÷ 60 gives metres per minute. Divide by 3600: 5 m/s.", "÷ 60 سے میٹر فی منٹ ملتا ہے۔ 3600 سے تقسیم کریں: 5 m/s", "half_conversion")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Speed, distance and time, and both units. You're up to speed!", "رفتار، فاصلہ اور وقت، اور دونوں اکائیاں۔ آپ نے سب سیکھ لیا!"),
    "text": T("speed = distance ÷ time, distance = speed × time, time = distance ÷ speed. km/h to m/s: × 1000 ÷ 3600 (× 5/18). m/s to km/h: × 3600 ÷ 1000 (× 18/5). Compare speeds only in the same unit.",
              "رفتار = فاصلہ ÷ وقت، فاصلہ = رفتار × وقت، وقت = فاصلہ ÷ رفتار۔ km/h سے m/s: × 1000 ÷ 3600 (× 5/18)۔ m/s سے km/h: × 3600 ÷ 1000 (× 18/5)۔ رفتاروں کا موازنہ صرف ایک جیسی اکائی میں کریں۔"),
    "points": [T("speed = distance ÷ time", "رفتار = فاصلہ ÷ وقت"),
               T("km/h × 5/18 = m/s", "km/h × 5/18 = m/s")]},
 ],
 "review_questions": [
   {"id": "r_distance", "type": "apply", "skill": SKILL, "step": number_question(
     "r_distance",
     T("A rickshaw goes at 45 km/h for 2 hours. How many km does it go?", "ایک رکشہ 2 گھنٹے 45 km/h کی رفتار سے چلتا ہے۔ وہ کتنے کلومیٹر جاتا ہے؟"),
     R1,
     T("distance = speed × time.", "فاصلہ = رفتار × وقت"),
     T("Right! 45 × 2 = 90 km.", "درست! 45 × 2 = 90 کلومیٹر"),
     T("45 × 2 = 90.", "45 × 2 = 90"),
     common_wrong=[wrong(22, "For distance, multiply: 45 × 2 = 90.", "فاصلے کے لیے ضرب دیں: 45 × 2 = 90", "wrong_operation")],
     qtype=None)},
   {"id": "r_convert", "type": "apply", "skill": SKILL, "step": number_question(
     "r_convert",
     T("Change 25 m/s to km/h.", "25 m/s کو km/h میں بدلیں۔"),
     R2,
     T("25 × 18 ÷ 5.", "25 × 18 ÷ 5"),
     T("Right! 90 km/h.", "درست! 90 km/h"),
     T("25 × 3600 = 90,000 m = 90 km in an hour.", "25 × 3600 = 90,000 میٹر = ایک گھنٹے میں 90 کلومیٹر"),
     common_wrong=[wrong(1500, "× 60 gives metres per minute. × 3600 ÷ 1000 = 90.", "× 60 سے میٹر فی منٹ ملتا ہے۔ × 3600 ÷ 1000 = 90", "half_conversion")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh after matching the app with PCTB Mathematics 6 (Sub-domain 4 includes speed in km/h and m/s). No textbook text or exercises were used.",
   "Every speed chosen converts to a whole number, so children can work with × 5/18 or with × 1000 ÷ 3600.",
   "Urdu terms to check: رفتار (speed), فاصلہ (distance), کلومیٹر فی گھنٹہ, میٹر فی سیکنڈ.",
   "The numbers were worked out in content/sources/g6-maths-06/speed.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import attach, road


def hours(n, unit="h"):
    return [f"{k}{unit}" for k in range(1, n + 1)]


attach(lesson, {
  "s1_hook": road(
    90, 3,
    "A road cut into 3 equal pieces of 30 m each. The marks above say 1s, 2s and 3s: the cheetah runs 30 m in every second.",
    "سڑک 30، 30 میٹر کے 3 برابر ٹکڑوں میں بٹی ہوئی۔ اوپر کے نشانوں پر 1s، 2s اور 3s لکھا ہے: چیتا ہر سیکنڈ میں 30 میٹر دوڑتا ہے۔",
    piece_text="30m", times=hours(3, "s")),
  "s2_foundation": road(
    150, 3,
    "A road 150 km long, marked with a bracket under it, cut into 3 equal pieces. The marks above say 1h, 2h and 3h; each piece has a question mark.",
    "150 کلومیٹر لمبی سڑک، نیچے قوس کے ساتھ، 3 برابر ٹکڑوں میں بٹی ہوئی۔ اوپر کے نشانوں پر 1h، 2h اور 3h لکھا ہے؛ ہر ٹکڑے پر سوالیہ نشان ہے۔",
    piece_text="?", times=hours(3), total_text="150km"),
  "s3_rule": road(
    36 * 3, 3,
    "At 36 km/h a car goes 36 km in each hour: a road cut into 3 pieces of 36 km, marked 1h, 2h and 3h above, 108 km in all.",
    "36 کلومیٹر فی گھنٹہ کی رفتار سے گاڑی ہر گھنٹے میں 36 کلومیٹر جاتی ہے: سڑک 36 کلومیٹر کے 3 ٹکڑوں میں بٹی ہوئی، اوپر 1h، 2h اور 3h، کل 108 کلومیٹر۔",
    piece_text="36km", times=hours(3), total_text=f"{36 * 3}km"),
  "s4_distance": road(
    S4, 4,
    "A road cut into 4 equal pieces of 60 km, marked 1h, 2h, 3h and 4h above. The bracket under the whole road has a question mark.",
    "سڑک 60 کلومیٹر کے 4 برابر ٹکڑوں میں بٹی ہوئی، اوپر 1h، 2h، 3h اور 4h۔ پوری سڑک کے نیچے قوس پر سوالیہ نشان ہے۔",
    piece_text="60km", times=hours(4), total_text="?"),
  "s5_time": road(
    300, 300 // 75,
    "A road 300 km long, marked with a bracket under it. Only the first piece is marked: 75 km, gone in 1h. How many such pieces fit in the road?",
    "300 کلومیٹر لمبی سڑک، نیچے قوس کے ساتھ۔ صرف پہلا ٹکڑا دکھایا گیا ہے: 75 کلومیٹر، 1h میں۔ سڑک میں ایسے کتنے ٹکڑے آتے ہیں؟",
    piece_text=["75km"], times=["1h"], total_text="300km", shown=1),
  "r_distance": road(
    R1, 2,
    "A road cut into 2 equal pieces of 45 km, marked 1h and 2h above. The bracket under the whole road has a question mark.",
    "سڑک 45 کلومیٹر کے 2 برابر ٹکڑوں میں بٹی ہوئی، اوپر 1h اور 2h۔ پوری سڑک کے نیچے قوس پر سوالیہ نشان ہے۔",
    piece_text="45km", times=hours(2), total_text="?"),
})
write(lesson)

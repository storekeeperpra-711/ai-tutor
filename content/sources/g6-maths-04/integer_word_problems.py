from common import (T, opt, say, wrong, signed, number_question, write,
                    REF, REVIEW, INT_MEANING, INT_ADD, INT_SUBTRACT, INT_MULTIPLY,
                    INT_WORD_PROBLEMS)

SKILL = INT_WORD_PROBLEMS
S = signed

# s1, s5: quiz, +5 for right, −2 for wrong. Ayesha: 6 right, 4 wrong.
QUIZ = 6 * 5 + 4 * -2
assert QUIZ == 22 and 6 * 5 + 4 * 2 == 38
# s2: foundation
assert 2 - -5 == 7
# s4: lift from basement −2 up 5 floors.
LIFT = -2 + 5
assert LIFT == 3 and -2 - 5 == -7
# s6: Skardu −9 °C at night, 4 °C at noon: the rise.
RISE = 4 - -9
assert RISE == 13 and 9 - 4 == 5
# s7: temperature falls 12 degrees in 4 hours, steadily: change each hour.
PER_HOUR = -12 // 4
assert PER_HOUR == -3
# s8: Bilal: floor −5 to floor 3.
FLOORS = 3 - -5
assert FLOORS == 8 and 3 + -5 == -2
# s9: diver at −15 m, kite at 20 m.
GAP = 20 - -15
assert GAP == 35
# Unit test.
assert -9 < -4                  # u1
U2 = -7 + 4
assert U2 == -3                  # u2
U3 = -2 - 9
assert U3 == -11                 # u3
U4 = -4 * -6
assert U4 == 24                  # u4
U5 = -35 // 7
assert U5 == -5 and 7 * U5 == -35  # u5
# Question bank and review.
assert 1 - -6 == 7 and -1 * 6 == -6
ACCOUNT = 500 - 800
assert ACCOUNT == -300
SUB = -40 + 15
assert SUB == -25
MATCH = 3 * 4 + 2 * -3
assert MATCH == 6


lesson = {
 "id": "g6-maths-04-integer-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems with integers (temperature, floors, depth, money and scores), choosing the right operation.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Integer word problems", "صحیح اعداد کے عملی سوالات"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": INT_MEANING}, {"skill": INT_ADD}, {"skill": INT_SUBTRACT}, {"skill": INT_MULTIPLY}],
 "misconceptions": [
   {"id": "difference_as_digits", "description": "Finds the gap between a negative and a positive number by subtracting the digits: from −9 to 4 is 5."},
   {"id": "penalty_added", "description": "Adds a penalty or loss as if it were a gain."},
   {"id": "wrong_operation", "description": "Picks the wrong operation for the story, like adding when the story asks for a difference."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_operation", "type": "recall", "step": {
     "id": "qb_operation", "type": "choice",
     "prompt": T("It is −6 °C in the morning and 1 °C at noon. Which sum tells you how much warmer noon is?", "صبح −6 ڈگری اور دوپہر کو 1 ڈگری ہے۔ کون سا سوال بتاتا ہے کہ دوپہر کتنی زیادہ گرم ہے؟"),
     "options": [
       opt("sub", "1 − (−6)", "1 − (−6)", True, "Yes! A difference is a subtraction: 1 − (−6) = 7 degrees.", "جی ہاں! فرق تفریق ہے: 1 − (−6) = 7 ڈگری۔"),
       opt("add", "1 + (−6)", "1 + (−6)", False, "That gives −5. 'How much warmer' is a difference: 1 − (−6).", "اس سے −5 آتا ہے۔ \"کتنا زیادہ گرم\" فرق ہے: 1 − (−6)", "wrong_operation"),
       opt("mul", "1 × (−6)", "1 × (−6)", False, "Nothing is repeated here. 'How much warmer' is a difference: 1 − (−6).", "یہاں کچھ دہرایا نہیں جا رہا۔ \"کتنا زیادہ گرم\" فرق ہے: 1 − (−6)", "wrong_operation"),
     ]}},
   {"id": "qb_account", "type": "apply", "step": number_question(
     "qb_account",
     T("Kamran has Rs 500 in his school savings card. He buys a uniform for Rs 800, and the school lets him owe the rest. Work out 500 − 800 to show his balance.",
       "کامران کے اسکول بچت کارڈ میں 500 روپے ہیں۔ وہ 800 روپے کی وردی خریدتا ہے، اور اسکول باقی رقم ادھار کر دیتا ہے۔ اس کا بقایا دکھانے کے لیے 500 − 800 حل کریں۔"),
     ACCOUNT,
     T("He spends more than he has, so the balance goes below 0.", "وہ اپنی رقم سے زیادہ خرچ کرتا ہے، اس لیے بقایا 0 سے نیچے چلا جاتا ہے۔"),
     T(f"Right! 500 − 800 = {S(ACCOUNT)}: he owes Rs 300.", f"درست! 500 − 800 = {S(ACCOUNT)}: اس پر 300 روپے ادھار ہیں۔"),
     T(f"800 − 500 = 300, and he spent more than he had, so {S(ACCOUNT)}.", f"800 − 500 = 300، اور اس نے اپنی رقم سے زیادہ خرچ کیا، اس لیے {S(ACCOUNT)}"),
     common_wrong=[wrong(300, "He owes the money, so the balance is negative: −300.", "اس پر ادھار ہے، اس لیے بقایا منفی ہے: −300")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A submarine is at −40 m. It rises 15 m. Saad says it is now at −55 m. What went wrong?", "ایک آبدوز −40 میٹر پر ہے۔ یہ 15 میٹر اوپر آتی ہے۔ سعد کہتا ہے اب یہ −55 میٹر پر ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("up", "Rising means going UP, towards 0: −40 + 15 = −25.", "اوپر آنے کا مطلب 0 کی طرف جانا ہے: −40 + 15 = −25", True,
           "Yes! It is still under water, but nearer the top: −25 m.", "جی ہاں! یہ ابھی بھی پانی کے نیچے ہے، مگر اوپر کے قریب: −25 میٹر۔"),
       opt("pos", "It should be 25 m.", "یہ 25 میٹر ہونا چاہیے۔", False,
           "It rose only 15 m from 40 m deep, so it is still below sea level: −25.", "یہ 40 میٹر گہرائی سے صرف 15 میٹر اوپر آئی، اس لیے ابھی بھی سطح سمندر سے نیچے ہے: −25"),
       opt("nothing", "Nothing. 40 + 15 = 55.", "کوئی غلطی نہیں۔ 40 + 15 = 55", False,
           "Going deeper would be −55. Rising goes towards 0: −25.", "مزید گہرائی میں جانا −55 ہوتا۔ اوپر آنا 0 کی طرف جانا ہے: −25", "wrong_operation"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_choose", "front": T("How do you choose the operation in an integer story?", "صحیح اعداد کی کہانی میں عمل کیسے چنتے ہیں؟"),
    "back": T("A change: add (up is +, down is −). How far apart or how much warmer: subtract. The same change again and again: multiply. Shared equally: divide.",
              "تبدیلی: جمع کریں (اوپر +، نیچے −)۔ کتنا دور یا کتنا زیادہ گرم: تفریق کریں۔ ایک ہی تبدیلی بار بار: ضرب دیں۔ برابر بانٹنا: تقسیم کریں۔")},
   {"id": "f_gap", "front": T("How far is it from −9 to 4?", "−9 سے 4 تک کتنا فاصلہ ہے؟"),
    "back": T("4 − (−9) = 13: 9 up to zero, then 4 more.", "4 − (−9) = 13: صفر تک 9، پھر 4 مزید۔")},
 ],
 "home_tasks": [{"id": "h_story", "text": T(
   "Make up your own integer story about the weather, a lift or money. Write the sum and the answer, then ask someone at home to solve it.",
   "موسم، لفٹ یا پیسوں کے بارے میں صحیح اعداد کی اپنی ایک کہانی بنائیں۔ سوال اور جواب لکھیں، پھر گھر میں کسی سے حل کروائیں۔")}],
 "glossary": [T("Balance", "بقایا"), T("Sea level", "سطح سمندر"), T("Basement", "تہہ خانہ"), T("Penalty", "جرمانہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "In a class quiz you get 5 points for a right answer and lose 2 points for a wrong one. Can your score go below zero?",
      "جماعت کے کوئز میں درست جواب پر 5 نمبر ملتے ہیں اور غلط جواب پر 2 نمبر کٹتے ہیں۔ کیا آپ کا اسکور صفر سے نیچے جا سکتا ہے؟"),
    "text": T("Integers are everywhere: scores, lifts, the weather, money and the sea. Today we solve stories with them. First, a quick check.",
              "صحیح اعداد ہر جگہ ہیں: اسکور، لفٹ، موسم، پیسے اور سمندر۔ آج ہم ان سے کہانیاں حل کریں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Work out 2 − (−5)", "حل کریں: 2 − (−5)"),
     7,
     T("Subtracting −5 is adding 5.", "−5 تفریق کرنا 5 جمع کرنا ہے۔"),
     T("Right! 2 − (−5) = 7.", "درست! 2 − (−5) = 7"),
     T("2 − (−5) = 2 + 5 = 7.", "2 − (−5) = 2 + 5 = 7"),
     common_wrong=[wrong(-3, "That is 2 − 5. Subtracting −5 is adding 5: 7.", "یہ 2 − 5 ہے۔ −5 تفریق کرنا 5 جمع کرنا ہے: 7")],
     qtype="recall", skill=INT_SUBTRACT),
   {"id": "s3_which_operation", "type": "explain",
    "character": say("thinking", "First decide what the story is asking. Then choose the operation.", "پہلے سمجھیں کہ کہانی کیا پوچھ رہی ہے۔ پھر عمل چنیں۔"),
    "text": T("A change (going up, going down, getting warmer or colder): add, with up as + and down as −. How far apart, or how much warmer: subtract. The same change again and again: multiply. A change shared equally: divide.",
              "تبدیلی (اوپر جانا، نیچے جانا، گرم یا ٹھنڈا ہونا): جمع کریں، اوپر + اور نیچے −۔ کتنا دور، یا کتنا زیادہ گرم: تفریق کریں۔ ایک ہی تبدیلی بار بار: ضرب دیں۔ تبدیلی برابر بانٹی گئی: تقسیم کریں۔")},
   number_question(
     "s4_lift",
     T("In a shopping mall, the ground floor is 0 and the car park is floor −2. Amna gets in the lift at the car park and goes up 5 floors. Which floor is she on?",
       "ایک شاپنگ مال میں زمینی منزل 0 ہے اور گاڑیوں کی پارکنگ منزل −2 ہے۔ آمنہ پارکنگ سے لفٹ میں بیٹھتی ہے اور 5 منزلیں اوپر جاتی ہے۔ وہ کس منزل پر ہے؟"),
     LIFT,
     T("Up is +: work out −2 + 5.", "اوپر + ہے: −2 + 5 حل کریں۔"),
     T(f"Right! −2 + 5 = {LIFT}. She is on floor {LIFT}.", f"درست! −2 + 5 = {LIFT}۔ وہ منزل {LIFT} پر ہے۔"),
     T(f"From −2, go up 5: −1, 0, 1, 2, 3. Floor {LIFT}.", f"−2 سے 5 اوپر جائیں: −1، 0، 1، 2، 3۔ منزل {LIFT}۔"),
     common_wrong=[wrong(-7, "She went UP, so add 5: −2 + 5 = 3.", "وہ اوپر گئی، اس لیے 5 جمع کریں: −2 + 5 = 3", "wrong_operation"),
                   wrong(5, "She started at −2, not at 0. −2 + 5 = 3.", "اس نے 0 سے نہیں، −2 سے شروع کیا۔ −2 + 5 = 3")]),
   number_question(
     "s5_quiz",
     T("Back to the quiz: +5 for each right answer, −2 for each wrong one. Ayesha gets 6 right and 4 wrong. What is her score?",
       "واپس کوئز پر: ہر درست جواب پر +5، ہر غلط پر −2۔ عائشہ کے 6 جواب درست اور 4 غلط ہیں۔ اس کا اسکور کیا ہے؟"),
     QUIZ,
     T("6 × 5 for the right answers, 4 × (−2) for the wrong ones. Then add.", "درست جوابوں کے لیے 6 × 5، غلط کے لیے 4 × (−2)۔ پھر جمع کریں۔"),
     T(f"Right! 30 + (−8) = {QUIZ}.", f"درست! 30 + (−8) = {QUIZ}"),
     T(f"6 × 5 = 30 and 4 × (−2) = −8. 30 + (−8) = {QUIZ}.", f"6 × 5 = 30 اور 4 × (−2) = −8۔ 30 + (−8) = {QUIZ}"),
     common_wrong=[wrong(38, "The wrong answers take points AWAY: 4 × (−2) = −8, so 30 − 8.", "غلط جواب نمبر کاٹتے ہیں: 4 × (−2) = −8، اس لیے 30 − 8", "penalty_added"),
                   wrong(30, "Don't forget the 4 wrong answers: they take away 8 points.", "4 غلط جواب نہ بھولیں: یہ 8 نمبر کاٹتے ہیں۔")]),
   number_question(
     "s6_skardu",
     T("In Skardu it is −9 °C at night and 4 °C at noon. How many degrees warmer is noon?",
       "سکردو میں رات کو −9 ڈگری اور دوپہر کو 4 ڈگری ہے۔ دوپہر کتنی ڈگری زیادہ گرم ہے؟"),
     RISE,
     T("How much warmer is a difference: 4 − (−9).", "کتنا زیادہ گرم فرق ہے: 4 − (−9)"),
     T(f"Right! 4 − (−9) = {RISE} degrees.", f"درست! 4 − (−9) = {RISE} ڈگری۔"),
     T(f"From −9 up to 0 is 9 degrees, then 4 more: 4 − (−9) = {RISE}.", f"−9 سے 0 تک 9 ڈگری، پھر 4 مزید: 4 − (−9) = {RISE}"),
     common_wrong=[wrong(5, "That is 9 − 4. Count 9 up to zero, then 4 more: 13.", "یہ 9 − 4 ہے۔ صفر تک 9 گنیں، پھر 4 مزید: 13", "difference_as_digits")]),
   number_question(
     "s7_per_hour",
     T("In the evening the temperature falls 12 degrees in 4 hours, the same each hour. Write the change each hour as an integer.",
       "شام کو 4 گھنٹوں میں درجہ حرارت 12 ڈگری گرتا ہے، ہر گھنٹے برابر۔ ہر گھنٹے کی تبدیلی کو صحیح عدد کی شکل میں لکھیں۔"),
     PER_HOUR,
     T("Falling 12 is −12. Share it over 4 hours.", "12 گرنا −12 ہے۔ اسے 4 گھنٹوں میں بانٹیں۔"),
     T(f"Right! (−12) ÷ 4 = {S(PER_HOUR)}: it falls 3 degrees each hour.", f"درست! (−12) ÷ 4 = {S(PER_HOUR)}: ہر گھنٹے 3 ڈگری گرتا ہے۔"),
     T(f"Falling is negative: (−12) ÷ 4 = {S(PER_HOUR)}.", f"گرنا منفی ہے: (−12) ÷ 4 = {S(PER_HOUR)}"),
     common_wrong=[wrong(3, "The temperature is falling, so the change is negative: −3.", "درجہ حرارت گر رہا ہے، اس لیے تبدیلی منفی ہے: −3"),
                   wrong(-48, "Shared equally means divide: (−12) ÷ 4.", "برابر بانٹنے کا مطلب تقسیم ہے: (−12) ÷ 4", "wrong_operation")]),
   {"id": "s8_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A building has floors from −5 (the lowest basement) to 3. Bilal says the lift travels 2 floors from the bottom to the top, because −5 + 3 = −2. What went wrong?",
                "ایک عمارت میں منزلیں −5 (سب سے نیچے کا تہہ خانہ) سے 3 تک ہیں۔ بلال کہتا ہے لفٹ نیچے سے اوپر تک 2 منزلیں جاتی ہے، کیونکہ −5 + 3 = −2۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("sub", "How far apart is a difference: 3 − (−5) = 8 floors.", "کتنا فاصلہ فرق ہے: 3 − (−5) = 8 منزلیں۔", True,
          "Yes! 5 floors up to the ground, then 3 more: 8.", "جی ہاں! زمینی منزل تک 5 منزلیں، پھر 3 مزید: 8"),
      opt("two", "Nothing. The answer is 2 floors.", "کوئی غلطی نہیں۔ جواب 2 منزلیں ہے۔", False,
          "Count them: −4, −3, −2, −1, 0, 1, 2, 3 is 8 floors up.", "گنیں: −4، −3، −2، −1، 0، 1، 2، 3 یعنی 8 منزلیں اوپر۔", "wrong_operation"),
      opt("minus8", "It should be −8.", "یہ −8 ہونا چاہیے۔", False,
          "A distance is never negative. The lift goes 8 floors.", "فاصلہ کبھی منفی نہیں ہوتا۔ لفٹ 8 منزلیں جاتی ہے۔"),
    ]},
   {"id": "s9_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "A diver is at −15 m and a kite is 20 m above the sea. My friend says they are 5 m apart. Help!",
                     "ایک غوطہ خور −15 میٹر پر ہے اور ایک پتنگ سمندر سے 20 میٹر اوپر ہے۔ میرا دوست کہتا ہے یہ 5 میٹر دور ہیں۔ مدد کریں!"),
    "task": T("In your own words: how far apart are the diver (−15 m) and the kite (20 m), and why?",
              "اپنے الفاظ میں بتائیں: غوطہ خور (−15 میٹر) اور پتنگ (20 میٹر) کتنے دور ہیں، اور کیوں؟"),
    "key_idea": "They are on opposite sides of sea level, so add the two distances: 15 m down to the water plus 20 m up = 35 m. That is 20 − (−15) = 35. The friend did 20 − 15.",
    "levels": {
      "got_it": "Says 35 m, explaining 15 below plus 20 above sea level, or 20 − (−15) = 20 + 15.",
      "partly": "Says 35 with no reason, or explains that they are on different sides of sea level without the total.",
      "not_yet": "Agrees with 5, gives another answer, or no reason."},
    "keywords": [
      ["35", "thirty-five", "پینتیس", "paintees", "۳۵"],
      ["sea level", "zero", "0", "سطح", "صفر", "sifar"],
      ["add", "plus", "+", "جمع", "jama"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 15 m up to the sea, then 20 m more: 35 m. That is 20 − (−15).",
                  "بہت خوب سمجھایا! سمندر تک 15 میٹر، پھر 20 میٹر مزید: 35 میٹر۔ یعنی 20 − (−15)"),
      "partly": T("Good start! Now count: how far from the diver up to sea level, and from sea level up to the kite?", "اچھی شروعات! اب گنیں: غوطہ خور سے سطح سمندر تک کتنا، اور سطح سمندر سے پتنگ تک کتنا؟"),
      "not_yet": T("Picture it: the diver is under the water and the kite is in the sky. How far is each one from the sea's surface?",
                   "تصور کریں: غوطہ خور پانی کے نیچے ہے اور پتنگ آسمان میں۔ ہر ایک سمندر کی سطح سے کتنا دور ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s10_gap",
     T("So how many metres apart are the diver and the kite?", "تو غوطہ خور اور پتنگ کتنے میٹر دور ہیں؟"),
     GAP,
     T("Work out 20 − (−15).", "20 − (−15) حل کریں۔"),
     T(f"Right! 20 − (−15) = {GAP} m.", f"درست! 20 − (−15) = {GAP} میٹر۔"),
     T(f"15 m up to the sea, then 20 m more: {GAP} m.", f"سمندر تک 15 میٹر، پھر 20 میٹر مزید: {GAP} میٹر۔"),
     common_wrong=[wrong(5, "That is 20 − 15. They are on opposite sides of sea level: 15 + 20.", "یہ 20 − 15 ہے۔ یہ سطح سمندر کے مخالف طرف ہیں: 15 + 20", "difference_as_digits")]),
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Integers unit. You can do it!", "ٹیسٹ کا وقت! صحیح اعداد کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has one question on each part of the unit: comparing, adding, subtracting, multiplying and dividing. Think about the sign of each answer.",
              "اس چھوٹے ٹیسٹ میں باب کے ہر حصے سے ایک سوال ہے: موازنہ، جمع، تفریق، ضرب اور تقسیم۔ ہر جواب کی علامت کا سوچیں۔")},
   {"id": "u1_compare", "type": "choice", "question_type": "recall", "skill": INT_MEANING,
    "prompt": T("Test 1: Which is colder, −9 °C or −4 °C?", "ٹیسٹ 1: کون زیادہ ٹھنڈا ہے، −9 ڈگری یا −4 ڈگری؟"),
    "options": [
      opt("m9", S(-9) + " °C", S(-9) + " ڈگری", True, "Yes! −9 is further left, so it is smaller and colder.", "جی ہاں! −9 زیادہ بائیں ہے، اس لیے چھوٹا اور زیادہ ٹھنڈا ہے۔"),
      opt("m4", S(-4) + " °C", S(-4) + " ڈگری", False, "−4 is to the right of −9, so −4 is warmer.", "−4، −9 کے دائیں طرف ہے، اس لیے −4 زیادہ گرم ہے۔"),
    ]},
   number_question(
     "u2_add",
     T("Test 2: Work out −7 + 4", "ٹیسٹ 2: حل کریں: −7 + 4"),
     U2,
     T("Different signs: 7 − 4, and −7 is further from 0.", "مختلف علامتیں: 7 − 4، اور −7 صفر سے زیادہ دور ہے۔"),
     T(f"Right! −7 + 4 = {U2}.", f"درست! −7 + 4 = {U2}"),
     T(f"7 − 4 = 3, and −7 is further from 0: {U2}.", f"7 − 4 = 3، اور −7 صفر سے زیادہ دور ہے: {U2}"),
     common_wrong=[wrong(3, "−7 is further from 0, so the answer is negative: −3.", "−7 صفر سے زیادہ دور ہے، اس لیے جواب منفی ہے: −3"),
                   wrong(-11, "Different signs: subtract, don't add. 7 − 4 = 3.", "مختلف علامتیں: جمع نہیں، تفریق کریں۔ 7 − 4 = 3")],
     qtype="apply", skill=INT_ADD),
   number_question(
     "u3_subtract",
     T("Test 3: Work out −2 − 9", "ٹیسٹ 3: حل کریں: −2 − 9"),
     U3,
     T("Add the opposite: −2 + (−9).", "مخالف جمع کریں: −2 + (−9)"),
     T(f"Right! −2 − 9 = {U3}.", f"درست! −2 − 9 = {U3}"),
     T(f"−2 + (−9): same signs, 2 + 9 = 11, keep the minus: {U3}.", f"−2 + (−9): ایک جیسی علامتیں، 2 + 9 = 11، منفی رکھیں: {U3}"),
     common_wrong=[wrong(-7, "Subtracting 9 moves 9 to the left from −2, past −7: −11.", "9 تفریق کرنے سے −2 سے بائیں جاتے ہیں: −11"),
                   wrong(7, "That is −2 + 9. Subtracting 9 moves left: −11.", "یہ −2 + 9 ہے۔ 9 تفریق کرنے سے بائیں جاتے ہیں: −11")],
     qtype="apply", skill=INT_SUBTRACT),
   number_question(
     "u4_multiply",
     T("Test 4: Work out (−4) × (−6)", "ٹیسٹ 4: حل کریں: (−4) × (−6)"),
     U4,
     T("4 × 6 = 24. Same signs.", "4 × 6 = 24۔ ایک جیسی علامتیں۔"),
     T(f"Right! (−4) × (−6) = {U4}.", f"درست! (−4) × (−6) = {U4}"),
     T(f"4 × 6 = 24, and same signs give a positive answer: {U4}.", f"4 × 6 = 24، اور ایک جیسی علامتوں کا جواب مثبت ہوتا ہے: {U4}"),
     common_wrong=[wrong(-24, "Same signs give a positive answer: 24.", "ایک جیسی علامتوں کا جواب مثبت ہوتا ہے: 24"),
                   wrong(-10, "That adds them. Multiply: 4 × 6 = 24.", "یہ جمع ہے۔ ضرب دیں: 4 × 6 = 24")],
     qtype="apply", skill=INT_MULTIPLY),
   number_question(
     "u5_divide",
     T("Test 5: Work out (−35) ÷ 7", "ٹیسٹ 5: حل کریں: (−35) ÷ 7"),
     U5,
     T("35 ÷ 7 = 5. Different signs.", "35 ÷ 7 = 5۔ مختلف علامتیں۔"),
     T(f"Right! (−35) ÷ 7 = {U5}.", f"درست! (−35) ÷ 7 = {U5}"),
     T(f"35 ÷ 7 = 5, and different signs give a negative answer: {U5}.", f"35 ÷ 7 = 5، اور مختلف علامتوں کا جواب منفی ہوتا ہے: {U5}"),
     common_wrong=[wrong(5, "Different signs give a negative answer: −5.", "مختلف علامتوں کا جواب منفی ہوتا ہے: −5")],
     qtype="recall", skill=INT_MULTIPLY),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You finished the whole Integers unit. Shabash!", "آپ نے صحیح اعداد کا پورا باب مکمل کر لیا۔ شاباش!"),
    "text": T("In an integer story, decide what is asked. A change: add (up +, down −). How far apart or how much warmer: subtract. The same change again and again: multiply. Shared equally: divide. Then check that the sign makes sense.",
              "صحیح اعداد کی کہانی میں سمجھیں کہ کیا پوچھا گیا ہے۔ تبدیلی: جمع (اوپر +، نیچے −)۔ کتنا دور یا کتنا زیادہ گرم: تفریق۔ ایک ہی تبدیلی بار بار: ضرب۔ برابر بانٹنا: تقسیم۔ پھر دیکھیں کہ علامت سمجھ میں آتی ہے۔"),
    "points": [T("From −9 to 4 is 13, not 5.", "−9 سے 4 تک 13 ہے، 5 نہیں۔"),
               T("A distance is never negative.", "فاصلہ کبھی منفی نہیں ہوتا۔")]},
 ],
 "review_questions": [
   {"id": "r_submarine", "type": "apply", "skill": SKILL, "step": number_question(
     "r_submarine",
     T("A submarine is at −40 m. It rises 15 m. Where is it now, in metres?", "ایک آبدوز −40 میٹر پر ہے۔ یہ 15 میٹر اوپر آتی ہے۔ اب یہ کتنے میٹر پر ہے؟"),
     SUB,
     T("Rising is +: −40 + 15.", "اوپر آنا + ہے: −40 + 15"),
     T(f"Right! −40 + 15 = {SUB}.", f"درست! −40 + 15 = {SUB}"),
     T(f"40 − 15 = 25, and −40 is further from 0: {SUB}.", f"40 − 15 = 25، اور −40 صفر سے زیادہ دور ہے: {SUB}"),
     common_wrong=[wrong(-55, "Rising goes up, towards 0: −40 + 15 = −25.", "اوپر آنا 0 کی طرف جانا ہے: −40 + 15 = −25", "wrong_operation"),
                   wrong(25, "It is still under water, so the answer is negative: −25.", "یہ ابھی بھی پانی کے نیچے ہے، اس لیے جواب منفی ہے: −25")],
     qtype=None)},
   {"id": "r_match", "type": "apply", "skill": SKILL, "step": number_question(
     "r_match",
     T("In a game you get +4 for a win and −3 for a loss. Hassan wins 3 games and loses 2. What is his score?", "ایک کھیل میں جیت پر +4 اور ہار پر −3 ملتے ہیں۔ حسن 3 کھیل جیتتا ہے اور 2 ہارتا ہے۔ اس کا اسکور کیا ہے؟"),
     MATCH,
     T("3 × 4 for the wins, 2 × (−3) for the losses. Then add.", "جیت کے لیے 3 × 4، ہار کے لیے 2 × (−3)۔ پھر جمع کریں۔"),
     T(f"Right! 12 + (−6) = {MATCH}.", f"درست! 12 + (−6) = {MATCH}"),
     T(f"3 × 4 = 12 and 2 × (−3) = −6. 12 + (−6) = {MATCH}.", f"3 × 4 = 12 اور 2 × (−3) = −6۔ 12 + (−6) = {MATCH}"),
     common_wrong=[wrong(18, "Losses take points away: 12 − 6.", "ہار سے نمبر کٹتے ہیں: 12 − 6", "penalty_added")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Integers unit. No textbook text or exercises were used. Temperatures and amounts are made up for the sums.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-04. Fix the names and curriculum_refs if the unit differs.",
   "Urdu terms to check: بقایا (balance), تہہ خانہ (basement), سطح سمندر (sea level).",
   "The lesson teaches choosing the operation (s3) before solving.",
   "s11 to u5 are a short unit test, one question per earlier lesson. Each u-step is tagged with that lesson's skill (meaning, add, subtract, multiply_divide), so it counts as practice for that skill rather than for word problems.",
   "The numbers were worked out in content/sources/g6-maths-04/integer_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

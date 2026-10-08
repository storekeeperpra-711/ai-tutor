from common import (T, opt, say, wrong, signed, number_question, write,
                    REVIEW, BOOK_INTEGERS, INT_MEANING, INT_ABSOLUTE)

SKILL = INT_ABSOLUTE

# s1, s3: Skardu −7 °C and Multan 7 °C are both 7 degrees from zero.
SKARDU, MULTAN = -7, 7
assert abs(SKARDU) == abs(MULTAN) == 7

# s2: foundation compare.
assert 2 > -3

# s4: |−7|; the common wrong answer keeps the sign.
S4 = abs(-7)
assert S4 == 7 and -7 != S4

# s5: |0|; common wrong answer 1.
S5 = abs(0)
assert S5 == 0 and 1 != S5

# s6: the integers with absolute value 5.
S6 = sorted(n for n in range(-10, 11) if abs(n) == 5)
assert S6 == [-5, 5]

# s7: a lift goes 4 floors below the ground floor: floor −4, 4 floors away.
FLOOR = -4
S7 = abs(FLOOR)
assert S7 == 4 and FLOOR != S7

# s8: −9 has the bigger absolute value, but 3 is the greater integer.
assert abs(-9) > abs(3) and 3 > -9

# s9: |−8| > |2| but −8 < 2.
assert abs(-8) > abs(2) and -8 < 2

# s11: order by absolute value, smallest first.
S11 = sorted([-8, 2, -3, 5], key=abs)
assert S11 == [2, -3, 5, -8]
assert sorted([-8, 2, -3, 5]) == [-8, -3, 2, 5]  # the order by value (a wrong option)

# Question bank.
QB_RECALL = abs(-4)
assert QB_RECALL == 4
OWED = -150
QB_APPLY = abs(OWED)
assert QB_APPLY == 150 and OWED != QB_APPLY
assert abs(0) == 0

# Review questions.
R1 = abs(-15)
assert R1 == 15 and -15 != R1
assert abs(-6) > abs(2) and 2 > -6

lesson = {
 "id": "g6-maths-04-absolute-value",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Understand the absolute value of an integer as its distance from 0 on the number line, find it, and tell ordering by absolute value apart from ordering by value.", "textbook": BOOK_INTEGERS}],
 "skills": [SKILL],
 "title": T("Absolute value", "مطلق قیمت"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": INT_MEANING}],
 "misconceptions": [
   {"id": "keeps_sign", "description": "Thinks the absolute value of a negative number is still negative, e.g. |−7| = −7."},
   {"id": "bigger_abs_bigger", "description": "Thinks a bigger absolute value means a bigger integer, so −9 > 3."},
   {"id": "zero_abs", "description": "Thinks |0| is 1, or that 0 has no absolute value."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_abs_four", "type": "recall", "step": {
     "id": "qb_abs_four", "type": "choice",
     "prompt": T("What is |−4|?", "|−4| کیا ہے؟"),
     "options": [
       opt("four", str(QB_RECALL), str(QB_RECALL), True,
           "Yes! −4 is 4 steps from 0, so |−4| = 4.", "جی ہاں! −4، 0 سے 4 قدم دور ہے، اس لیے |−4| = 4"),
       opt("minus_4", signed(-4), signed(-4), False,
           "A distance is never negative. −4 is 4 steps from 0, so |−4| = 4.", "فاصلہ کبھی منفی نہیں ہوتا۔ −4، 0 سے 4 قدم دور ہے، اس لیے |−4| = 4", "keeps_sign"),
       opt("zero", "0", "0", False,
           "Only 0 is 0 steps from 0. −4 is 4 steps away.", "صرف 0 ہی 0 سے 0 قدم دور ہے۔ −4، 4 قدم دور ہے۔"),
     ]}},
   {"id": "qb_owed", "type": "apply", "step": number_question(
     "qb_owed",
     T("Zara's bank balance is −150 rupees: she owes the shop money. How many rupees does she owe? Type the absolute value.",
       "زارا کا حساب −150 روپے ہے: اس نے دکان کے پیسے دینے ہیں۔ اس پر کتنے روپے ادھار ہیں؟ مطلق قیمت لکھیں۔"),
     QB_APPLY,
     T("How far is −150 from 0?", "−150، 0 سے کتنا دور ہے؟"),
     T("Right! |−150| = 150, so she owes Rs 150.", "درست! |−150| = 150، اس لیے اس پر 150 روپے ادھار ہیں۔"),
     T("The minus sign shows she owes money. The amount is the distance from 0: |−150| = 150.", "منفی کی علامت بتاتی ہے کہ ادھار ہے۔ رقم 0 سے فاصلہ ہے: |−150| = 150"),
     common_wrong=[wrong(OWED, "The amount owed is a distance from 0, so it is not negative: 150.", "ادھار کی رقم 0 سے فاصلہ ہے، اس لیے منفی نہیں: 150", "keeps_sign")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Hina says |0| = 1, because every absolute value must be at least 1. Is she right?",
                 "حنا کہتی ہے |0| = 1، کیونکہ ہر مطلق قیمت کم از کم 1 ہونی چاہیے۔ کیا وہ درست ہے؟"),
     "options": [
       opt("no", "No. 0 is 0 steps from 0, so |0| = 0.", "نہیں۔ 0، 0 سے 0 قدم دور ہے، اس لیے |0| = 0", True,
           "Right! The absolute value of 0 is 0.", "درست! 0 کی مطلق قیمت 0 ہے۔"),
       opt("yes", "Yes. An absolute value cannot be 0.", "ہاں۔ مطلق قیمت 0 نہیں ہو سکتی۔", False,
           "Absolute value is distance from 0. From 0 to 0 you move no steps, so |0| = 0.", "مطلق قیمت 0 سے فاصلہ ہے۔ 0 سے 0 تک کوئی قدم نہیں، اس لیے |0| = 0", "zero_abs"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_meaning", "front": T("What is the absolute value of an integer?", "کسی صحیح عدد کی مطلق قیمت کیا ہے؟"),
    "back": T("Its distance from 0 on the number line. It is never negative: |−7| = 7, |7| = 7, |0| = 0.",
              "عددی خط پر 0 سے اس کا فاصلہ۔ یہ کبھی منفی نہیں ہوتی: |−7| = 7، |7| = 7، |0| = 0")},
   {"id": "f_compare", "front": T("|−9| is bigger than |3|. Is −9 bigger than 3?", "|−9|، |3| سے بڑا ہے۔ کیا −9، 3 سے بڑا ہے؟"),
    "back": T("No! −9 is further from 0, but it is to the left of 3, so −9 < 3.", "نہیں! −9، 0 سے زیادہ دور ہے، لیکن 3 کے بائیں طرف ہے، اس لیے −9 < 3")},
 ],
 "home_tasks": [{"id": "h_lift", "text": T(
   "Find a lift, a staircase or a building plan with floors below the ground floor (a basement), or ask an adult about one. Write each floor as an integer, then write how many floors it is from the ground floor using absolute value.",
   "کوئی لفٹ، سیڑھیاں یا عمارت کا نقشہ تلاش کریں جس میں زمینی منزل سے نیچے منزلیں ہوں (تہہ خانہ)، یا کسی بڑے سے پوچھیں۔ ہر منزل کو صحیح عدد کی شکل میں لکھیں، پھر مطلق قیمت سے لکھیں کہ وہ زمینی منزل سے کتنی منزلیں دور ہے۔")}],
 "glossary": [T("Absolute value", "مطلق قیمت"), T("Distance", "فاصلہ"), T("Integer", "صحیح عدد"), T("Number line", "عددی خط"), T("Negative", "منفی")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Skardu is −7 °C and Multan is 7 °C. One is cold, one is warm, but both are 7 degrees away from zero!",
      "سکردو میں −7 ڈگری اور ملتان میں 7 ڈگری ہے۔ ایک ٹھنڈا، ایک گرم، مگر دونوں صفر سے 7 ڈگری دور ہیں!"),
    "text": T("Today we measure how far a number is from zero. First, a quick check.",
              "آج ہم ناپیں گے کہ کوئی عدد صفر سے کتنا دور ہے۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": INT_MEANING,
    "prompt": T("Which is greater, −3 or 2?", "کون سا بڑا ہے، −3 یا 2؟"),
    "options": [
      opt("two", "2", "2", True, "Yes! 2 is to the right of −3 on the number line.", "جی ہاں! عددی خط پر 2، −3 کے دائیں طرف ہے۔"),
      opt("minus_3", signed(-3), signed(-3), False, "−3 is to the left of 0, and 2 is to the right, so 2 is greater.", "−3، 0 کے بائیں طرف ہے اور 2 دائیں طرف، اس لیے 2 بڑا ہے۔"),
    ]},
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "Absolute value is just counting steps to zero!", "مطلق قیمت بس صفر تک قدم گننا ہے!"),
    "text": T("The absolute value of a number is its distance from 0 on the number line. We write it with two bars: |−7| means \"the absolute value of −7\". −7 is 7 steps from 0, so |−7| = 7. 7 is also 7 steps from 0, so |7| = 7. And |0| = 0. A distance is never negative, so an absolute value is never negative.",
              "کسی عدد کی مطلق قیمت عددی خط پر 0 سے اس کا فاصلہ ہے۔ ہم اسے دو لکیروں کے درمیان لکھتے ہیں: |−7| کا مطلب ہے \"−7 کی مطلق قیمت\"۔ −7، 0 سے 7 قدم دور ہے، اس لیے |−7| = 7۔ 7 بھی 0 سے 7 قدم دور ہے، اس لیے |7| = 7۔ اور |0| = 0۔ فاصلہ کبھی منفی نہیں ہوتا، اس لیے مطلق قیمت کبھی منفی نہیں ہوتی۔")},
   number_question(
     "s4_abs_seven",
     T("What is |−7|?", "|−7| کیا ہے؟"),
     S4,
     T("Count the steps from −7 to 0.", "−7 سے 0 تک قدم گنیں۔"),
     T("Yes! −7 is 7 steps from 0, so |−7| = 7.", "جی ہاں! −7، 0 سے 7 قدم دور ہے، اس لیے |−7| = 7"),
     T("Absolute value is the distance from 0. −7 is 7 steps away, so |−7| = 7.", "مطلق قیمت 0 سے فاصلہ ہے۔ −7، 7 قدم دور ہے، اس لیے |−7| = 7"),
     common_wrong=[wrong(-7, "A distance cannot be negative. Drop the minus sign: |−7| = 7.", "فاصلہ منفی نہیں ہو سکتا۔ منفی کی علامت ہٹا دیں: |−7| = 7", "keeps_sign")]),
   number_question(
     "s5_abs_zero",
     T("What is |0|?", "|0| کیا ہے؟"),
     S5,
     T("How many steps is it from 0 to 0?", "0 سے 0 تک کتنے قدم ہیں؟"),
     T("Right! 0 is no steps from 0, so |0| = 0.", "درست! 0، 0 سے کوئی قدم دور نہیں، اس لیے |0| = 0"),
     T("You do not move at all from 0 to 0, so the distance is 0: |0| = 0.", "0 سے 0 تک آپ بالکل نہیں چلتے، اس لیے فاصلہ 0 ہے: |0| = 0"),
     common_wrong=[wrong(1, "From 0 to 0 you take no steps, not 1. |0| = 0.", "0 سے 0 تک کوئی قدم نہیں، 1 نہیں۔ |0| = 0", "zero_abs")]),
   {"id": "s6_two_numbers", "type": "choice", "question_type": "apply",
    "prompt": T("Which two integers have an absolute value of 5?", "کن دو صحیح اعداد کی مطلق قیمت 5 ہے؟"),
    "options": [
      opt("both", "5 and −5", "5 اور −5", True,
          "Yes! Both are 5 steps from 0, one on each side.", "جی ہاں! دونوں 0 سے 5 قدم دور ہیں، ایک ایک طرف۔"),
      opt("zero_five", "0 and 5", "0 اور 5", False,
          "|0| = 0, not 5. Look 5 steps to the left of 0 too.", "|0| = 0 ہے، 5 نہیں۔ 0 سے 5 قدم بائیں طرف بھی دیکھیں۔", "zero_abs"),
      opt("only_five", "Only 5", "صرف 5", False,
          "−5 is also 5 steps from 0, on the left side. So |−5| = 5 too.", "−5 بھی 0 سے 5 قدم دور ہے، بائیں طرف۔ اس لیے |−5| = 5 بھی ہے۔", "keeps_sign"),
    ]},
   number_question(
     "s7_lift",
     T("A lift goes down to floor −4, below the ground floor (0). How many floors is it from the ground floor?",
       "ایک لفٹ نیچے منزل −4 پر جاتی ہے، زمینی منزل (0) سے نیچے۔ یہ زمینی منزل سے کتنی منزلیں دور ہے؟"),
     S7,
     T("Count the floors from −4 up to 0.", "−4 سے اوپر 0 تک منزلیں گنیں۔"),
     T("Yes! |−4| = 4, so it is 4 floors away.", "جی ہاں! |−4| = 4، اس لیے یہ 4 منزلیں دور ہے۔"),
     T("Floor −4 is 4 floors below 0. The distance is |−4| = 4.", "منزل −4، 0 سے 4 منزلیں نیچے ہے۔ فاصلہ |−4| = 4 ہے۔"),
     common_wrong=[wrong(FLOOR, "−4 is the floor number. The number of floors away is a distance: 4.", "−4 منزل کا نمبر ہے۔ کتنی منزلیں دور ہے، یہ فاصلہ ہے: 4", "keeps_sign")]),
   {"id": "s8_value_vs_abs", "type": "choice", "question_type": "apply",
    "prompt": T("|−9| = 9 and |3| = 3. Which integer is greater, −9 or 3?", "|−9| = 9 اور |3| = 3۔ کون سا صحیح عدد بڑا ہے، −9 یا 3؟"),
    "options": [
      opt("three", "3", "3", True,
          "Yes! 3 is to the right of −9, so 3 > −9, even though −9 is further from 0.", "جی ہاں! 3، −9 کے دائیں طرف ہے، اس لیے 3 > −9، حالانکہ −9، 0 سے زیادہ دور ہے۔"),
      opt("minus_9", signed(-9), signed(-9), False,
          "−9 is further from 0, but it is on the left, so it is smaller. −9 °C is much colder than 3 °C.", "−9، 0 سے زیادہ دور ہے، لیکن بائیں طرف ہے، اس لیے چھوٹا ہے۔ −9 ڈگری، 3 ڈگری سے بہت ٹھنڈا ہے۔", "bigger_abs_bigger"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Usman says −8 > 2, because |−8| = 8 and 8 is more than 2. What went wrong?",
                "عثمان کہتا ہے −8 > 2، کیونکہ |−8| = 8 اور 8، 2 سے زیادہ ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("distance", "He compared distances from 0, not the numbers. −8 is to the left of 2, so −8 < 2.",
          "اس نے 0 سے فاصلوں کا موازنہ کیا، اعداد کا نہیں۔ −8، 2 کے بائیں طرف ہے، اس لیے −8 < 2", True,
          "Yes! Bigger absolute value means further from 0, not greater.", "جی ہاں! بڑی مطلق قیمت کا مطلب 0 سے زیادہ دور ہے، بڑا عدد نہیں۔"),
      opt("nothing", "Nothing. The bigger absolute value is the bigger number.", "کوئی غلطی نہیں۔ بڑی مطلق قیمت والا عدد بڑا ہے۔", False,
          "That only works for positive numbers. −8 is on the left of 2, so it is smaller.", "یہ صرف مثبت اعداد کے لیے درست ہے۔ −8، 2 کے بائیں طرف ہے، اس لیے چھوٹا ہے۔", "bigger_abs_bigger"),
      opt("abs_wrong", "|−8| should be −8.", "|−8| کو −8 ہونا چاہیے۔", False,
          "|−8| = 8 is correct: a distance is never negative. The mistake is in the comparison.", "|−8| = 8 درست ہے: فاصلہ کبھی منفی نہیں ہوتا۔ غلطی موازنے میں ہے۔", "keeps_sign"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? Why is |−6| equal to 6 and not −6?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ |−6| برابر 6 کیوں ہے، −6 کیوں نہیں؟"),
    "task": T("In your own words: why is |−6| = 6 and not −6? You can use a number line, a lift or the weather.",
              "اپنے الفاظ میں بتائیں: |−6| = 6 کیوں ہے، −6 کیوں نہیں؟ آپ عددی خط، لفٹ یا موسم کی مثال دے سکتے ہیں۔"),
    "key_idea": "Absolute value is the distance from 0. −6 is 6 steps from 0 on the number line, and a distance is never negative, so |−6| = 6.",
    "levels": {
      "got_it": "Says absolute value is the distance (or number of steps) from 0, that −6 is 6 away from 0, and that a distance cannot be negative.",
      "partly": "Says |−6| = 6 or mentions distance or steps, but does not link it to the distance from 0.",
      "not_yet": "Says |−6| is −6, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["distance", "far", "away", "steps", "فاصلہ", "دور", "قدم", "fasla", "door", "qadam"],
      ["zero", "0", "صفر", "sifar"],
      ["never negative", "not negative", "positive", "منفی نہیں", "مثبت", "manfi nahi", "musbat"]],
    "fallback_feedback": {
      "got_it": T("Well explained! −6 is 6 steps from 0, and a distance is never negative, so |−6| = 6.",
                  "بہت خوب سمجھایا! −6، 0 سے 6 قدم دور ہے، اور فاصلہ کبھی منفی نہیں ہوتا، اس لیے |−6| = 6"),
      "partly": T("Good start! Now say what absolute value measures: the distance from where?", "اچھی شروعات! اب بتائیں کہ مطلق قیمت کیا ناپتی ہے: کہاں سے فاصلہ؟"),
      "not_yet": T("Think: if you walk from −6 to 0 on the number line, how many steps do you take? Can that be negative?",
                   "سوچیں: اگر آپ عددی خط پر −6 سے 0 تک چلیں، تو کتنے قدم لیں گے؟ کیا یہ منفی ہو سکتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_order_abs", "type": "choice", "question_type": "apply",
    "prompt": T("Order −8, 2, −3, 5 by absolute value, from closest to 0 to furthest from 0.",
                "−8، 2، −3، 5 کو مطلق قیمت کے لحاظ سے ترتیب دیں، 0 کے سب سے قریب سے سب سے دور تک۔"),
    "options": [
      opt("by_abs", "2, −3, 5, −8", "2، −3، 5، −8", True,
          "Yes! Their absolute values are 2, 3, 5, 8.", "جی ہاں! ان کی مطلق قیمتیں 2، 3، 5، 8 ہیں۔"),
      opt("by_value", "−8, −3, 2, 5", "−8، −3، 2، 5", False,
          "That is the order by value, smallest to greatest. Here we want distance from 0: 2, 3, 5, 8.", "یہ قیمت کے لحاظ سے چھوٹے سے بڑے کی ترتیب ہے۔ یہاں 0 سے فاصلہ چاہیے: 2، 3، 5، 8"),
      opt("negatives_first", "−3, −8, 2, 5", "−3، −8، 2، 5", False,
          "Ignore the signs and look at the distances: |2| = 2 is the smallest, |−8| = 8 the biggest.", "علامتیں چھوڑ کر فاصلے دیکھیں: |2| = 2 سب سے چھوٹا ہے، |−8| = 8 سب سے بڑا۔"),
    ]},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can measure how far any integer is from zero!", "اب آپ ناپ سکتے ہیں کہ کوئی بھی صحیح عدد صفر سے کتنا دور ہے!"),
    "text": T("The absolute value of a number is its distance from 0, written with two bars. It is never negative: |−7| = 7, |7| = 7, |0| = 0. A bigger absolute value means further from 0, not a greater number: |−9| > |3|, but −9 < 3.",
              "کسی عدد کی مطلق قیمت 0 سے اس کا فاصلہ ہے، جو دو لکیروں کے درمیان لکھی جاتی ہے۔ یہ کبھی منفی نہیں ہوتی: |−7| = 7، |7| = 7، |0| = 0۔ بڑی مطلق قیمت کا مطلب 0 سے زیادہ دور ہے، بڑا عدد نہیں: |−9| > |3|، لیکن −9 < 3"),
    "points": [T("Floor −4 is |−4| = 4 floors below the ground floor.", "منزل −4، زمینی منزل سے |−4| = 4 منزلیں نیچے ہے۔"),
               T("5 and −5 both have absolute value 5.", "5 اور −5 دونوں کی مطلق قیمت 5 ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_abs_fifteen", "type": "apply", "skill": SKILL, "step": number_question(
     "r_abs_fifteen",
     T("A diver is at −15 m, below sea level (0). How many metres is she from the surface?",
       "ایک غوطہ خور −15 میٹر پر ہے، سطح سمندر (0) سے نیچے۔ وہ سطح سے کتنے میٹر دور ہے؟"),
     R1,
     T("Find |−15|: the distance from 0.", "|−15| معلوم کریں: 0 سے فاصلہ۔"),
     T("Right! |−15| = 15 m.", "درست! |−15| = 15 میٹر۔"),
     T("The distance from 0 is the absolute value: |−15| = 15.", "0 سے فاصلہ مطلق قیمت ہے: |−15| = 15"),
     common_wrong=[wrong(-15, "A distance is never negative: 15 m.", "فاصلہ کبھی منفی نہیں ہوتا: 15 میٹر۔", "keeps_sign")],
     qtype=None)},
   {"id": "r_compare", "type": "recall", "skill": SKILL, "step": {
     "id": "r_compare", "type": "choice",
     "prompt": T("|−6| is bigger than |2|. Which integer is greater, −6 or 2?", "|−6|، |2| سے بڑا ہے۔ کون سا صحیح عدد بڑا ہے، −6 یا 2؟"),
     "options": [
       opt("two", "2", "2", True, "Yes! 2 is to the right of −6.", "جی ہاں! 2، −6 کے دائیں طرف ہے۔"),
       opt("minus_6", signed(-6), signed(-6), False, "−6 is further from 0, but on the left, so it is smaller.", "−6، 0 سے زیادہ دور ہے، لیکن بائیں طرف، اس لیے چھوٹا ہے۔", "bigger_abs_bigger"),
     ]}},
 ],
 "teacher_notes": [
   "Written fresh for the Integers sub-domain. No textbook text or exercises were used.",
   "Absolute value is written with two bars, |−7|. Check that the bars display clearly in both languages on the device.",
   "Urdu terms to check against the Punjab textbook: مطلق قیمت (absolute value), فاصلہ (distance), صحیح عدد (integer), عددی خط (number line), منفی (negative), مثبت (positive).",
   "Typed negative answers accept the keyboard minus and the − sign. The common wrong answers catch a child who keeps the minus sign (−7 for |−7|) or gives 1 for |0|.",
   "Temperatures, floors and money amounts are made-up examples, not real readings.",
   "The numbers were worked out in content/sources/g6-maths-04/absolute_value.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

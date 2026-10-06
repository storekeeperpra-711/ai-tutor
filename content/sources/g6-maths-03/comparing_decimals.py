from common import (T, D, opt, say, wrong, dec, number_question, decimal_line, write,
                    REF, REVIEW, DEC_PLACE_VALUE, DEC_COMPARE)

SKILL = DEC_COMPARE

# s1, s4, s10: 1.5 kg against 1.25 kg
assert D("1.5") > D("1.25") and D("1.5") == D("1.50")
# s6
assert D("0.4") > D("0.38")
# s7
ORDER = sorted([D("0.7"), D("0.07"), D("0.17"), D("0.71")])
assert ORDER == [D("0.07"), D("0.17"), D("0.7"), D("0.71")]
# s8: halfway between 0.3 and 0.4
S8 = (D("0.3") + D("0.4")) / 2
assert S8 == D("0.35") and D("0.3") < S8 < D("0.4")
# s9
assert D("0.1") > D("0.09")
# s11
S11 = max([D("2.6"), D("2.06"), D("2.66")])
assert S11 == D("2.66")
# question bank and review
QB = min(D("0.8"), D("0.75"))
assert QB == D("0.75")
R1 = max(D("3.09"), D("3.1"))
assert R1 == D("3.1")
R2 = min([D("5.5"), D("5.05"), D("5.45")])
assert R2 == D("5.05")

lesson = {
 "id": "g6-maths-03-comparing-decimals",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Compare and order decimals using place value and the number line.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Comparing and ordering decimals", "اعشاریہ اعداد کا موازنہ اور ترتیب"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": DEC_PLACE_VALUE}],
 "misconceptions": [
   {"id": "longer_is_bigger", "description": "Thinks a decimal with more digits is bigger: 1.25 > 1.5."},
   {"id": "shorter_is_bigger", "description": "Thinks a decimal with fewer digits is always bigger, or that hundredths beat tenths."},
   {"id": "compare_after_point", "description": "Compares the digits after the point as whole numbers: 0.09 > 0.1 because 9 > 1."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_first", "type": "recall", "step": {
     "id": "qb_first", "type": "choice",
     "prompt": T("To compare 4.62 and 4.7, which digits decide it?", "4.62 اور 4.7 کا موازنہ کرنے کے لیے کون سے ہندسے فیصلہ کرتے ہیں؟"),
     "options": [
       opt("tenths", "The tenths: 6 and 7, so 4.7 is bigger.", "دسویں: 6 اور 7، اس لیے 4.7 بڑا ہے۔", True, "Yes! The ones are the same, so look at the tenths.", "جی ہاں! اکائیاں ایک جیسی ہیں، اس لیے دسویں دیکھیں۔"),
       opt("last", "The last digits: 2 and 7.", "آخری ہندسے: 2 اور 7", False, "Compare place by place from the left. After the ones, look at the tenths: 6 and 7.", "بائیں سے مقام بہ مقام موازنہ کریں۔ اکائیوں کے بعد دسویں دیکھیں: 6 اور 7"),
       opt("count", "The number of digits: 4.62 has more.", "ہندسوں کی تعداد: 4.62 میں زیادہ ہیں۔", False, "More digits doesn't mean bigger. Compare the tenths: 7 > 6.", "زیادہ ہندسوں کا مطلب بڑا نہیں۔ دسویں کا موازنہ کریں: 7 > 6", "longer_is_bigger"),
     ]}},
   {"id": "qb_smaller", "type": "apply", "step": number_question(
     "qb_smaller",
     T("Which is smaller, 0.8 or 0.75? Type it.", "کون سا چھوٹا ہے، 0.8 یا 0.75؟ لکھیں۔"),
     QB,
     T("Write 0.8 as 0.80, then compare.", "0.8 کو 0.80 لکھیں، پھر موازنہ کریں۔"),
     T("Right! 0.75 < 0.80.", "درست! 0.75 < 0.80"),
     T("0.8 = 0.80, and 75 hundredths is less than 80 hundredths. So 0.75 is smaller.", "0.8 = 0.80، اور 75 سوواں، 80 سوویں سے کم ہے۔ اس لیے 0.75 چھوٹا ہے۔"),
     common_wrong=[wrong(D("0.8"), "0.8 = 0.80, which is more than 0.75.", "0.8 = 0.80، جو 0.75 سے زیادہ ہے۔", "longer_is_bigger")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Hamid says 2.35 is bigger than 2.4, because 35 is bigger than 4. What went wrong?", "حامد کہتا ہے 2.35، 2.4 سے بڑا ہے، کیونکہ 35، 4 سے بڑا ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("tenths", "Compare the tenths: 4 > 3, so 2.4 is bigger.", "دسویں کا موازنہ کریں: 4 > 3، اس لیے 2.4 بڑا ہے۔", True,
           "Yes! 2.4 = 2.40, and 40 hundredths beats 35 hundredths.", "جی ہاں! 2.4 = 2.40، اور 40 سوواں، 35 سوویں سے زیادہ ہے۔"),
       opt("nothing", "Nothing. 35 > 4.", "کوئی غلطی نہیں۔ 35 > 4", False,
           "The digits after the point are not whole numbers. 2.4 = 2.40 > 2.35.", "اعشاریہ کے بعد کے ہندسے مکمل اعداد نہیں ہیں۔ 2.4 = 2.40 > 2.35", "compare_after_point"),
       opt("equal", "They are equal.", "یہ برابر ہیں۔", False,
           "2.40 and 2.35 are different: 2.4 is bigger.", "2.40 اور 2.35 مختلف ہیں: 2.4 بڑا ہے۔"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_compare", "front": T("How do you compare two decimals?", "دو اعشاریہ اعداد کا موازنہ کیسے کرتے ہیں؟"),
    "back": T("Line up the points. Compare place by place from the left: ones, tenths, hundredths. Add zeros to make them the same length: 1.5 = 1.50 > 1.25.",
              "نقطے ایک سیدھ میں رکھیں۔ بائیں سے مقام بہ مقام موازنہ کریں: اکائیاں، دسواں، سوواں۔ برابر لمبائی کے لیے صفر لگائیں: 1.5 = 1.50 > 1.25")},
   {"id": "f_trap", "front": T("Which is bigger, 0.1 or 0.09?", "کون سا بڑا ہے، 0.1 یا 0.09؟"),
    "back": T("0.1, because 0.1 = 0.10 and 10 hundredths > 9 hundredths.", "0.1، کیونکہ 0.1 = 0.10 اور 10 سوواں > 9 سوواں")},
 ],
 "home_tasks": [{"id": "h_labels", "text": T(
   "Find 3 packets or bottles at home with decimal weights or volumes on them (like 1.5 L or 0.25 kg). Write them in order from smallest to biggest.",
   "گھر میں 3 پیکٹ یا بوتلیں ڈھونڈیں جن پر اعشاریہ میں وزن یا مقدار لکھی ہو (جیسے 1.5 لیٹر یا 0.25 کلوگرام)۔ انہیں چھوٹے سے بڑے کی ترتیب میں لکھیں۔")}],
 "glossary": [T("Greater than (>)", "بڑا (>)"), T("Less than (<)", "چھوٹا (<)"), T("Order", "ترتیب")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "One bag of sugar weighs 1.5 kg and another weighs 1.25 kg. Hira says 1.25 is heavier because 25 is more than 5. Is she right?",
      "چینی کا ایک تھیلا 1.5 کلوگرام اور دوسرا 1.25 کلوگرام ہے۔ حرا کہتی ہے 1.25 زیادہ بھاری ہے کیونکہ 25، 5 سے زیادہ ہے۔ کیا وہ درست ہے؟"),
    "text": T("Today we learn to compare and order decimals. First, a quick check on place value.", "آج ہم اعشاریہ اعداد کا موازنہ اور ترتیب سیکھیں گے۔ پہلے مقامی قیمت کا ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": DEC_PLACE_VALUE,
    "prompt": T("In 1.25, what is the value of the 2?", "1.25 میں 2 کی قیمت کیا ہے؟"),
    "options": [
      opt("tenths", "2 tenths (0.2)", "2 دسواں (0.2)", True, "Yes! The first place after the point is tenths.", "جی ہاں! اعشاریہ کے بعد پہلا مقام دسواں ہے۔"),
      opt("hundredths", "2 hundredths (0.02)", "2 سوواں (0.02)", False, "Hundredths is the second place, where the 5 is.", "سوواں دوسرا مقام ہے، جہاں 5 ہے۔"),
      opt("twenty", "20", "20", False, "The 2 is after the point, so it is less than 1.", "2 اعشاریہ کے بعد ہے، اس لیے ایک سے کم ہے۔"),
    ]},
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "Line up the points, then compare from the left!", "نقطے ایک سیدھ میں رکھیں، پھر بائیں سے موازنہ کریں!"),
    "text": T("Compare place by place from the left: ones first, then tenths, then hundredths. 1.5 and 1.25 have the same ones (1). Tenths: 5 against 2, so 1.5 is bigger. It helps to add a zero so both have the same number of places: 1.50 and 1.25. A zero at the end does not change a decimal.",
              "بائیں سے مقام بہ مقام موازنہ کریں: پہلے اکائیاں، پھر دسواں، پھر سوواں۔ 1.5 اور 1.25 کی اکائیاں ایک جیسی ہیں (1)۔ دسواں: 5 اور 2، اس لیے 1.5 بڑا ہے۔ دونوں کے برابر مقام کرنے کے لیے صفر لگانا مددگار ہے: 1.50 اور 1.25۔ آخر میں صفر لگانے سے اعشاریہ نہیں بدلتا۔")},
   {"id": "s4_sugar", "type": "choice", "question_type": "apply",
    "prompt": T("So which bag of sugar is heavier?", "تو چینی کا کون سا تھیلا زیادہ بھاری ہے؟"),
    "options": [
      opt("big", "1.5 kg", "1.5 کلوگرام", True, "Yes! 1.50 > 1.25. Hira was wrong.", "جی ہاں! 1.50 > 1.25۔ حرا غلط تھی۔"),
      opt("long", "1.25 kg", "1.25 کلوگرام", False, "More digits doesn't mean heavier. Compare tenths: 5 > 2.", "زیادہ ہندسوں کا مطلب زیادہ بھاری نہیں۔ دسویں کا موازنہ کریں: 5 > 2", "longer_is_bigger"),
    ]},
   {"id": "s5_number_line", "type": "explain",
    "character": say("thinking", "On a number line, the bigger number is further right.", "عددی خط پر بڑا عدد زیادہ دائیں ہوتا ہے۔"),
    "text": T("Between 1 and 2 there are tenths: 1.1, 1.2, 1.3 … 1.9. 1.25 is halfway between 1.2 and 1.3. 1.5 is further right, so it is bigger.",
              "1 اور 2 کے درمیان دسواں ہیں: 1.1، 1.2، 1.3 … 1.9۔ 1.25، 1.2 اور 1.3 کے بالکل درمیان ہے۔ 1.5 زیادہ دائیں ہے، اس لیے بڑا ہے۔")},
   {"id": "s6_compare", "type": "choice", "question_type": "apply",
    "prompt": T("Which is greater, 0.4 or 0.38?", "کون سا بڑا ہے، 0.4 یا 0.38؟"),
    "options": [
      opt("right", "0.4", "0.4", True, "Yes! 0.4 = 0.40, and 40 hundredths > 38 hundredths.", "جی ہاں! 0.4 = 0.40، اور 40 سوواں > 38 سوواں۔"),
      opt("wrong", "0.38", "0.38", False, "Compare tenths: 4 > 3. So 0.4 is greater.", "دسویں کا موازنہ کریں: 4 > 3۔ اس لیے 0.4 بڑا ہے۔", "longer_is_bigger"),
    ]},
   {"id": "s7_order", "type": "choice", "question_type": "apply",
    "prompt": T("Put in order from smallest to greatest: 0.7, 0.07, 0.17, 0.71", "چھوٹے سے بڑے کی ترتیب میں رکھیں: 0.7، 0.07، 0.17، 0.71"),
    "options": [
      opt("right", "0.07, 0.17, 0.7, 0.71", "0.07، 0.17، 0.7، 0.71", True, "Yes! As hundredths: 7, 17, 70, 71.", "جی ہاں! سوویں میں: 7، 17، 70، 71"),
      opt("length", "0.7, 0.07, 0.17, 0.71", "0.7، 0.07، 0.17، 0.71", False, "Write them all with two places: 0.70, 0.07, 0.17, 0.71. Now order them.", "سب کو دو مقام کے ساتھ لکھیں: 0.70، 0.07، 0.17، 0.71۔ اب ترتیب دیں۔", "shorter_is_bigger"),
      opt("digits", "0.07, 0.7, 0.17, 0.71", "0.07، 0.7، 0.17، 0.71", False, "0.7 = 0.70, which is bigger than 0.17.", "0.7 = 0.70، جو 0.17 سے بڑا ہے۔", "compare_after_point"),
    ]},
   decimal_line(
     "s8_between",
     T("This line goes from 0 to 1 in steps of 0.05. Put the marker on the number halfway between 0.3 and 0.4. Press Check.", "یہ خط 0 سے 1 تک 0.05 کے قدموں میں ہے۔ نشان کو 0.3 اور 0.4 کے بالکل درمیان والے عدد پر رکھیں۔ \"جانچیں\" دبائیں۔"),
     S8, 
     T("Think in hundredths: 0.30 and 0.40. What is halfway?", "سوویں میں سوچیں: 0.30 اور 0.40۔ درمیان میں کیا ہے؟"),
     T("Yes! 0.35 is between 0.3 and 0.4.", "جی ہاں! 0.35، 0.3 اور 0.4 کے درمیان ہے۔"),
     T("0.30 and 0.40: halfway is 0.35.", "0.30 اور 0.40: درمیان 0.35 ہے۔"),
     step="0.05",
     common_wrong=[wrong("0.4", "That is the end, 0.4. Go back one step to halfway: 0.35.", "یہ آخر ہے، 0.4۔ ایک قدم پیچھے درمیان میں جائیں: 0.35")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal says 0.09 is greater than 0.1, because 9 is greater than 1. What went wrong?", "بلال کہتا ہے 0.09، 0.1 سے بڑا ہے، کیونکہ 9، 1 سے بڑا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("tenths", "Compare tenths: 0.1 has 1 tenth, 0.09 has 0 tenths. So 0.1 is greater.", "دسویں کا موازنہ کریں: 0.1 میں 1 دسواں، 0.09 میں 0 دسواں۔ اس لیے 0.1 بڑا ہے۔", True,
          "Yes! 0.1 = 0.10, and 10 hundredths > 9 hundredths.", "جی ہاں! 0.1 = 0.10، اور 10 سوواں > 9 سوواں۔"),
      opt("nothing", "Nothing. 9 > 1.", "کوئی غلطی نہیں۔ 9 > 1", False,
          "The 9 is hundredths but the 1 is a tenth. 0.1 = 0.10 > 0.09.", "9 سوواں ہے مگر 1 دسواں ہے۔ 0.1 = 0.10 > 0.09", "compare_after_point"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Hira still thinks 1.25 kg is heavier than 1.5 kg. Can you help her?",
                     "حرا اب بھی سمجھتی ہے 1.25 کلوگرام، 1.5 کلوگرام سے زیادہ بھاری ہے۔ کیا آپ اس کی مدد کر سکتے ہیں؟"),
    "task": T("In your own words: why is 1.5 greater than 1.25?", "اپنے الفاظ میں بتائیں: 1.5، 1.25 سے بڑا کیوں ہے؟"),
    "key_idea": "The ones are the same. In the tenths place, 1.5 has 5 tenths and 1.25 has only 2 tenths, so 1.5 is greater. Writing 1.5 as 1.50 shows 50 hundredths against 25 hundredths.",
    "levels": {
      "got_it": "Compares the tenths (5 against 2), or writes 1.5 as 1.50 and compares 50 with 25 hundredths.",
      "partly": "Says 1.5 is greater without a place-value reason, or mentions adding a zero without comparing.",
      "not_yet": "Agrees 1.25 is greater, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["tenths", "دسواں", "daswan", "5 > 2", "5 and 2"],
      ["1.50", "zero", "صفر", "sifar", "50"],
      ["hundredths", "سوواں", "sauwan"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 1.5 has 5 tenths but 1.25 has only 2, so 1.5 is greater: 1.50 > 1.25.",
                  "بہت خوب سمجھایا! 1.5 میں 5 دسواں ہیں مگر 1.25 میں صرف 2، اس لیے 1.5 بڑا ہے: 1.50 > 1.25"),
      "partly": T("Good start! Now compare the tenths digit of each number.", "اچھی شروعات! اب ہر عدد کا دسویں والا ہندسہ دیکھیں۔"),
      "not_yet": T("Write 1.5 as 1.50. Now compare 1.50 and 1.25 place by place.", "1.5 کو 1.50 لکھیں۔ اب 1.50 اور 1.25 کا مقام بہ مقام موازنہ کریں۔")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_greatest",
     T("Which is the greatest: 2.6, 2.06 or 2.66? Type it.", "سب سے بڑا کون سا ہے: 2.6، 2.06 یا 2.66؟ لکھیں۔"),
     S11,
     T("Write them all with two places: 2.60, 2.06, 2.66.", "سب کو دو مقام کے ساتھ لکھیں: 2.60، 2.06، 2.66"),
     T("Right! 2.66 is the greatest.", "درست! 2.66 سب سے بڑا ہے۔"),
     T("2.60, 2.06, 2.66: the tenths tie at 6 for two of them, then 6 hundredths beats 0. So 2.66.", "2.60، 2.06، 2.66: دو میں دسواں 6 ہے، پھر 6 سوواں، 0 سے زیادہ ہے۔ اس لیے 2.66"),
     common_wrong=[wrong(D("2.6"), "2.6 = 2.60, which is less than 2.66.", "2.6 = 2.60، جو 2.66 سے کم ہے۔", "shorter_is_bigger"),
                   wrong(D("2.06"), "2.06 has 0 tenths, so it is the smallest.", "2.06 میں 0 دسواں ہیں، اس لیے یہ سب سے چھوٹا ہے۔")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can compare any decimals now!", "اب آپ کسی بھی اعشاریہ کا موازنہ کر سکتے ہیں!"),
    "text": T("Line up the decimal points and compare place by place from the left: ones, tenths, hundredths. Add zeros at the end to make the same number of places. More digits does not mean bigger: 1.5 > 1.25 and 0.1 > 0.09.",
              "اعشاری نقطے ایک سیدھ میں رکھیں اور بائیں سے مقام بہ مقام موازنہ کریں: اکائیاں، دسواں، سوواں۔ برابر مقام کے لیے آخر میں صفر لگائیں۔ زیادہ ہندسوں کا مطلب بڑا نہیں: 1.5 > 1.25 اور 0.1 > 0.09"),
    "points": [T("1.5 = 1.50", "1.5 = 1.50"), T("On a number line, bigger is further right.", "عددی خط پر بڑا عدد زیادہ دائیں ہوتا ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_greater", "type": "apply", "skill": SKILL, "step": number_question(
     "r_greater",
     T("Which is greater, 3.09 or 3.1? Type it.", "کون سا بڑا ہے، 3.09 یا 3.1؟ لکھیں۔"),
     R1,
     T("Compare the tenths: 0 and 1.", "دسویں کا موازنہ کریں: 0 اور 1"),
     T("Right! 3.1 = 3.10 > 3.09.", "درست! 3.1 = 3.10 > 3.09"),
     T("3.1 has 1 tenth and 3.09 has 0 tenths, so 3.1 is greater.", "3.1 میں 1 دسواں اور 3.09 میں 0 دسواں، اس لیے 3.1 بڑا ہے۔"),
     common_wrong=[wrong(D("3.09"), "9 hundredths is less than 1 tenth (10 hundredths). 3.1 is greater.", "9 سوواں، 1 دسویں (10 سوویں) سے کم ہے۔ 3.1 بڑا ہے۔", "compare_after_point")],
     qtype=None)},
   {"id": "r_smallest", "type": "apply", "skill": SKILL, "step": number_question(
     "r_smallest",
     T("Which is the smallest: 5.5, 5.05 or 5.45? Type it.", "سب سے چھوٹا کون سا ہے: 5.5، 5.05 یا 5.45؟ لکھیں۔"),
     R2,
     T("Write them with two places: 5.50, 5.05, 5.45.", "دو مقام کے ساتھ لکھیں: 5.50، 5.05، 5.45"),
     T("Right! 5.05 has 0 tenths, so it is the smallest.", "درست! 5.05 میں 0 دسواں ہیں، اس لیے یہ سب سے چھوٹا ہے۔"),
     T("5.50, 5.05, 5.45: tenths 5, 0, 4. The smallest is 5.05.", "5.50، 5.05، 5.45: دسواں 5، 0، 4۔ سب سے چھوٹا 5.05"),
     common_wrong=[wrong(D("5.5"), "5.5 = 5.50, the greatest of the three.", "5.5 = 5.50، تینوں میں سب سے بڑا۔", "shorter_is_bigger")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Decimals unit. No textbook text or exercises were used.",
   "The key method is lining up the points and adding zeros so both numbers have the same number of places.",
   "Urdu terms to check: ترتیب (order), موازنہ (compare).",
   "The number-line step uses the native number_line sim from 0 to 1 in steps of 0.05 with decimal labels.",
   "The numbers were worked out in content/sources/g6-maths-03/comparing_decimals.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

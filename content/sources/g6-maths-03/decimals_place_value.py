from fractions import Fraction as F

from common import (T, D, opt, say, wrong, dec, number_question, decimal_line, write,
                    REF, REVIEW, FRACTIONS_EQUIVALENT, DEC_PLACE_VALUE)

SKILL = DEC_PLACE_VALUE


def as_fraction(d):
    return F(str(d))


# s2: 3/10 = 30/100
assert F(3, 10) == F(30, 100) != F(3, 100)
# s4: 7 tenths
assert as_fraction(D("0.7")) == F(7, 10)
# s5: the 4 in 2.45 is 4 tenths
assert str(D("2.45")).split(".")[1][0] == "4"
# s6: 6/100
S6 = D(6) / 100
assert S6 == D("0.06") and as_fraction(S6) == F(6, 100)
# s7: 3 + 2/10 + 5/100
S7 = 3 + D(2) / 10 + D(5) / 100
assert S7 == D("3.25")
# s8: 3/4 = 75/100
S8 = D(3) / 4
assert S8 == D("0.75") and F(3, 4) == F(75, 100)
# s9: 0.5 = 5/10, not 5/100
assert as_fraction(D("0.5")) == F(5, 10) != F(5, 100)
# s10: 0.5 = 0.50
assert D("0.5") == D("0.50")
# s11: 35 cm in metres
S11 = D(35) / 100
assert S11 == D("0.35")
# question bank and review
QB = D(9) / 10
assert QB == D("0.9")
R1 = D(48) / 100
assert R1 == D("0.48")
R2 = D(2) / 5
assert R2 == D("0.4") and F(2, 5) == F(4, 10)


lesson = {
 "id": "g6-maths-03-decimals-and-place-value",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Understand tenths and hundredths, read and write decimals, and change simple fractions to decimals.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Decimals and place value", "اعشاریہ اور مقامی قیمت"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": FRACTIONS_EQUIVALENT}],
 "misconceptions": [
   {"id": "tenths_hundredths", "description": "Mixes up tenths and hundredths: writes 6/100 as 0.6."},
   {"id": "decimal_as_whole", "description": "Reads the digits after the point as a whole number: thinks 0.35 means 35."},
   {"id": "fraction_digits", "description": "Writes a fraction as a decimal by putting its digits after the point: 3/4 = 0.34."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_digit", "type": "recall", "step": {
     "id": "qb_digit", "type": "choice",
     "prompt": T("In 5.83, what is the value of the 3?", "5.83 میں 3 کی قیمت کیا ہے؟"),
     "options": [
       opt("hundredths", "3 hundredths (0.03)", "3 سوواں (0.03)", True, "Yes! The second place after the point is hundredths.", "جی ہاں! اعشاریہ کے بعد دوسرا مقام سوواں ہے۔"),
       opt("tenths", "3 tenths (0.3)", "3 دسواں (0.3)", False, "The first place after the point is tenths; that is the 8. The 3 is in the hundredths place.", "اعشاریہ کے بعد پہلا مقام دسواں ہے؛ وہاں 8 ہے۔ 3 سوویں کے مقام پر ہے۔", "tenths_hundredths"),
       opt("ones", "3 ones", "3 اکائیاں", False, "The ones digit is 5, before the point. The 3 is after the point.", "اکائی کا ہندسہ 5 ہے، اعشاریہ سے پہلے۔ 3 اعشاریہ کے بعد ہے۔", "decimal_as_whole"),
     ]}},
   {"id": "qb_write", "type": "apply", "step": number_question(
     "qb_write",
     T("Write 9/10 as a decimal.", "9/10 کو اعشاریہ میں لکھیں۔"),
     QB,
     T("9 tenths: one place after the point.", "9 دسواں: اعشاریہ کے بعد ایک مقام۔"),
     T("Right! 9/10 = 0.9.", "درست! 9/10 = 0.9"),
     T("Tenths go in the first place after the point: 9/10 = 0.9.", "دسواں اعشاریہ کے بعد پہلے مقام پر آتا ہے: 9/10 = 0.9"),
     common_wrong=[wrong(D("0.09"), "0.09 is 9 hundredths. 9 tenths is 0.9.", "0.09 نو سوواں ہے۔ 9 دسواں 0.9 ہے۔", "tenths_hundredths"),
                   wrong(D("9.1"), "The 9 is tenths, so it goes after the point: 0.9.", "9 دسواں ہے، اس لیے اعشاریہ کے بعد آئے گا: 0.9", "fraction_digits")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Ahmad wrote 7/100 as 0.7. What went wrong?", "احمد نے 7/100 کو 0.7 لکھا۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("place", "7 hundredths goes in the second place: 0.07.", "7 سوواں دوسرے مقام پر آتا ہے: 0.07", True,
           "Yes! 0.7 is 7 tenths, which is 70 hundredths.", "جی ہاں! 0.7 سات دسواں ہے، یعنی 70 سوواں۔"),
       opt("nothing", "Nothing. 7/100 = 0.7.", "کوئی غلطی نہیں۔ 7/100 = 0.7", False,
           "0.7 is 7/10. Hundredths need two places after the point: 0.07.", "0.7 سات دسواں ہے۔ سوویں کے لیے اعشاریہ کے بعد دو مقام چاہییں: 0.07", "tenths_hundredths"),
       opt("big", "It should be 7.100.", "یہ 7.100 ہونا چاہیے۔", False,
           "7/100 is less than 1, so it starts with 0: 0.07.", "7/100 ایک سے کم ہے، اس لیے یہ 0 سے شروع ہوگا: 0.07", "fraction_digits"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_places", "front": T("What are the places after the decimal point?", "اعشاریہ کے بعد کون سے مقام ہیں؟"),
    "back": T("First tenths, then hundredths. In 2.45: 4 tenths and 5 hundredths.", "پہلے دسواں، پھر سوواں۔ 2.45 میں: 4 دسواں اور 5 سوواں۔")},
   {"id": "f_fraction", "front": T("3/4 as a decimal?", "3/4 اعشاریہ میں؟"),
    "back": T("0.75, because 3/4 = 75/100.", "0.75، کیونکہ 3/4 = 75/100")},
 ],
 "home_tasks": [{"id": "h_ruler", "text": T(
   "Use a ruler to measure 3 things at home in centimetres, like a pencil or a spoon. Write each length in metres as a decimal (for example 15 cm = 0.15 m).",
   "گھر میں 3 چیزیں، جیسے پنسل یا چمچ، فٹے سے سینٹی میٹر میں ناپیں۔ ہر لمبائی کو میٹر میں اعشاریہ کی شکل میں لکھیں (مثلاً 15 سینٹی میٹر = 0.15 میٹر)۔")}],
 "glossary": [T("Decimal", "اعشاریہ"), T("Decimal point", "اعشاری نقطہ"), T("Tenths", "دسواں حصہ"), T("Hundredths", "سوواں حصہ"), T("Place value", "مقامی قیمت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "My pencil is longer than 7 cm but shorter than 8 cm. How can we write its length exactly?",
      "میری پنسل 7 سینٹی میٹر سے لمبی مگر 8 سینٹی میٹر سے چھوٹی ہے۔ ہم اس کی ٹھیک لمبائی کیسے لکھیں؟"),
    "text": T("We need numbers between the whole numbers. They are called decimals. First, a quick check on fractions.",
              "ہمیں مکمل اعداد کے درمیان کے اعداد چاہییں۔ انہیں اعشاریہ کہتے ہیں۔ پہلے کسروں کا ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": FRACTIONS_EQUIVALENT,
    "prompt": T("Which fraction is equal to 3/10?", "کون سی کسر 3/10 کے برابر ہے؟"),
    "options": [
      opt("right", "30/100", "30/100", True, "Yes! Multiply the top and bottom by 10.", "جی ہاں! شمار کنندہ اور نسب نما دونوں کو 10 سے ضرب دیں۔"),
      opt("small", "3/100", "3/100", False, "3/100 is ten times smaller. Multiply the top by 10 too: 30/100.", "3/100 دس گنا چھوٹا ہے۔ اوپر والے کو بھی 10 سے ضرب دیں: 30/100"),
      opt("flip", "10/3", "10/3", False, "That is turned upside down. 3/10 = 30/100.", "یہ الٹا ہے۔ 3/10 = 30/100"),
    ]},
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "The decimal point separates whole numbers from parts of one.", "اعشاری نقطہ مکمل اعداد کو ایک کے حصوں سے الگ کرتا ہے۔"),
    "text": T("Cut 1 into 10 equal parts: each part is one tenth, 1/10 = 0.1. So 7/10 = 0.7. Cut 1 into 100 parts: each is one hundredth, 1/100 = 0.01. In 2.45, the 2 is ones, the 4 is tenths and the 5 is hundredths. My pencil is 7.3 cm: 7 whole cm and 3 tenths.",
              "1 کو 10 برابر حصوں میں کاٹیں: ہر حصہ ایک دسواں ہے، 1/10 = 0.1۔ اس لیے 7/10 = 0.7۔ 1 کو 100 حصوں میں کاٹیں: ہر حصہ ایک سوواں ہے، 1/100 = 0.01۔ 2.45 میں 2 اکائیاں، 4 دسواں اور 5 سوواں ہیں۔ میری پنسل 7.3 سینٹی میٹر ہے: 7 پورے سینٹی میٹر اور 3 دسواں۔")},
   decimal_line(
     "s4_place",
     T("This line goes from 0 to 1 in tenths. Put the marker on 0.7. Press Check.", "یہ خط 0 سے 1 تک دسویں حصوں میں ہے۔ نشان کو 0.7 پر رکھیں۔ \"جانچیں\" دبائیں۔"),
     "0.7",
     T("Count 7 tenths from 0.", "0 سے 7 دسواں گنیں۔"),
     T("Yes! 0.7 is 7 tenths of the way from 0 to 1.", "جی ہاں! 0.7، 0 سے 1 تک کا 7 دسواں راستہ ہے۔"),
     T("0.1, 0.2, 0.3 … count 7 steps: 0.7.", "0.1، 0.2، 0.3 … 7 قدم گنیں: 0.7"),
     common_wrong=[wrong("0.3", "That is 3 tenths. Count 7 steps from 0.", "یہ 3 دسواں ہے۔ 0 سے 7 قدم گنیں۔")]),
   {"id": "s5_digit", "type": "choice", "question_type": "recall",
    "prompt": T("In 2.45, what is the value of the 4?", "2.45 میں 4 کی قیمت کیا ہے؟"),
    "options": [
      opt("tenths", "4 tenths (0.4)", "4 دسواں (0.4)", True, "Yes! The first place after the point is tenths.", "جی ہاں! اعشاریہ کے بعد پہلا مقام دسواں ہے۔"),
      opt("hundredths", "4 hundredths (0.04)", "4 سوواں (0.04)", False, "Hundredths is the second place, where the 5 is. The 4 is tenths.", "سوواں دوسرا مقام ہے، جہاں 5 ہے۔ 4 دسواں ہے۔", "tenths_hundredths"),
      opt("forty", "40", "40", False, "The 4 is after the point, so it is less than 1: 4 tenths.", "4 اعشاریہ کے بعد ہے، اس لیے ایک سے کم ہے: 4 دسواں۔", "decimal_as_whole"),
    ]},
   number_question(
     "s6_hundredths",
     T("Write 6/100 as a decimal.", "6/100 کو اعشاریہ میں لکھیں۔"),
     S6,
     T("Hundredths need two places after the point.", "سوویں کے لیے اعشاریہ کے بعد دو مقام چاہییں۔"),
     T("Right! 6/100 = 0.06.", "درست! 6/100 = 0.06"),
     T("No tenths, 6 hundredths: 0.06.", "کوئی دسواں نہیں، 6 سوواں: 0.06"),
     common_wrong=[wrong(D("0.6"), "0.6 is 6 tenths. 6 hundredths needs a 0 in the tenths place: 0.06.", "0.6 چھ دسواں ہے۔ 6 سوویں کے لیے دسویں کے مقام پر 0 لگائیں: 0.06", "tenths_hundredths"),
                   wrong(6, "6/100 is much less than 1: 0.06.", "6/100 ایک سے بہت کم ہے: 0.06", "decimal_as_whole")]),
   number_question(
     "s7_expanded",
     T("Write 3 + 2/10 + 5/100 as one decimal.", "3 + 2/10 + 5/100 کو ایک اعشاریہ عدد میں لکھیں۔"),
     S7,
     T("3 ones, 2 tenths, 5 hundredths.", "3 اکائیاں، 2 دسواں، 5 سوواں۔"),
     T(f"Right! {dec(S7)}.", f"درست! {dec(S7)}"),
     T(f"Ones before the point, then tenths, then hundredths: {dec(S7)}.", f"اکائیاں اعشاریہ سے پہلے، پھر دسواں، پھر سوواں: {dec(S7)}"),
     common_wrong=[wrong(325, "The 2 and the 5 are parts of 1, so they go after the point: 3.25.", "2 اور 5 ایک کے حصے ہیں، اس لیے اعشاریہ کے بعد آئیں گے: 3.25", "decimal_as_whole")]),
   number_question(
     "s8_three_quarters",
     T("Write 3/4 as a decimal. Hint: make the bottom 100.", "3/4 کو اعشاریہ میں لکھیں۔ اشارہ: نسب نما کو 100 بنائیں۔"),
     S8,
     T("4 × 25 = 100, so 3/4 = 75/100.", "4 × 25 = 100، اس لیے 3/4 = 75/100"),
     T("Right! 3/4 = 75/100 = 0.75.", "درست! 3/4 = 75/100 = 0.75"),
     T("Multiply top and bottom by 25: 3/4 = 75/100 = 0.75.", "اوپر اور نیچے کو 25 سے ضرب دیں: 3/4 = 75/100 = 0.75"),
     common_wrong=[wrong(D("0.34"), "The digits of a fraction don't go straight after the point. Make the bottom 100: 75/100 = 0.75.", "کسر کے ہندسے سیدھے اعشاریہ کے بعد نہیں لکھے جاتے۔ نسب نما 100 بنائیں: 75/100 = 0.75", "fraction_digits"),
                   wrong(D("3.4"), "3/4 is less than 1. Make the bottom 100: 0.75.", "3/4 ایک سے کم ہے۔ نسب نما 100 بنائیں: 0.75", "fraction_digits")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Zara says 0.5 means 5/100. What went wrong?", "زارا کہتی ہے 0.5 کا مطلب 5/100 ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("tenths", "The 5 is in the tenths place, so 0.5 = 5/10, which is half.", "5 دسویں کے مقام پر ہے، اس لیے 0.5 = 5/10، یعنی آدھا۔", True,
          "Yes! 5/100 would be 0.05.", "جی ہاں! 5/100 تو 0.05 ہوتا۔"),
      opt("nothing", "Nothing. 0.5 = 5/100.", "کوئی غلطی نہیں۔ 0.5 = 5/100", False,
          "One place after the point is tenths: 0.5 = 5/10.", "اعشاریہ کے بعد ایک مقام دسواں ہے: 0.5 = 5/10", "tenths_hundredths"),
      opt("five", "0.5 means 5.", "0.5 کا مطلب 5 ہے۔", False,
          "0.5 is less than 1: it is half of 1.", "0.5 ایک سے کم ہے: یہ 1 کا آدھا ہے۔", "decimal_as_whole"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "My friend says 0.50 is bigger than 0.5 because it has more digits. Is that right?",
                     "میرا دوست کہتا ہے 0.50، 0.5 سے بڑا ہے کیونکہ اس میں زیادہ ہندسے ہیں۔ کیا یہ درست ہے؟"),
    "task": T("In your own words: are 0.5 and 0.50 equal? Explain why, using tenths and hundredths.",
              "اپنے الفاظ میں بتائیں: کیا 0.5 اور 0.50 برابر ہیں؟ دسویں اور سوویں حصوں سے سمجھائیں۔"),
    "key_idea": "They are equal: 0.5 is 5 tenths, and 5 tenths is the same as 50 hundredths, which is 0.50. A zero at the end after the point does not change the value.",
    "levels": {
      "got_it": "Says they are equal, because 5 tenths = 50 hundredths (or 5/10 = 50/100), or because the end zero adds no tenths or hundredths.",
      "partly": "Says they are equal but gives no reason, or mentions tenths without linking them to hundredths.",
      "not_yet": "Says 0.50 is bigger, gives no answer, or the reasoning is wrong."},
    "keywords": [
      ["equal", "same", "برابر", "ایک جیسے", "barabar"],
      ["tenths", "hundredths", "دسواں", "سوواں", "daswan", "sauwan"],
      ["50/100", "5/10", "zero", "صفر", "sifar"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 5 tenths is the same as 50 hundredths, so 0.5 = 0.50.",
                  "بہت خوب سمجھایا! 5 دسواں، 50 سوویں کے برابر ہے، اس لیے 0.5 = 0.50"),
      "partly": T("Good start! Now say how many hundredths are in 5 tenths.", "اچھی شروعات! اب بتائیں کہ 5 دسویں میں کتنے سوواں ہیں۔"),
      "not_yet": T("Think: 0.5 is 5/10 and 0.50 is 50/100. Are 5/10 and 50/100 equal?",
                   "سوچیں: 0.5 یعنی 5/10 اور 0.50 یعنی 50/100۔ کیا 5/10 اور 50/100 برابر ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_metres",
     T("1 metre is 100 centimetres. A pencil is 35 cm long. Write its length in metres as a decimal.", "1 میٹر میں 100 سینٹی میٹر ہوتے ہیں۔ ایک پنسل 35 سینٹی میٹر لمبی ہے۔ اس کی لمبائی میٹر میں اعشاریہ کی شکل میں لکھیں۔"),
     S11,
     T("35 cm is 35/100 of a metre.", "35 سینٹی میٹر، ایک میٹر کا 35/100 ہے۔"),
     T("Right! 35 cm = 0.35 m.", "درست! 35 سینٹی میٹر = 0.35 میٹر"),
     T("35/100 m = 0.35 m.", "35/100 میٹر = 0.35 میٹر"),
     common_wrong=[wrong(D("3.5"), "3.5 m is longer than 3 metres! 35 cm is less than 1 m: 0.35.", "3.5 میٹر تو 3 میٹر سے بھی لمبا ہے! 35 سینٹی میٹر ایک میٹر سے کم ہے: 0.35", "tenths_hundredths"),
                   wrong(35, "That is in centimetres. In metres it is 35/100 = 0.35.", "یہ سینٹی میٹر میں ہے۔ میٹر میں یہ 35/100 = 0.35 ہے۔", "decimal_as_whole")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can read and write decimals!", "اب آپ اعشاریہ پڑھ اور لکھ سکتے ہیں!"),
    "text": T("The first place after the decimal point is tenths, the second is hundredths. 0.7 = 7/10, 0.06 = 6/100, 2.45 = 2 + 4/10 + 5/100. To change a fraction to a decimal, make the bottom 10 or 100: 3/4 = 75/100 = 0.75.",
              "اعشاریہ کے بعد پہلا مقام دسواں ہے، دوسرا سوواں۔ 0.7 = 7/10، 0.06 = 6/100، 2.45 = 2 + 4/10 + 5/100۔ کسر کو اعشاریہ میں بدلنے کے لیے نسب نما 10 یا 100 بنائیں: 3/4 = 75/100 = 0.75"),
    "points": [T("0.5 = 0.50: a zero at the end changes nothing.", "0.5 = 0.50: آخر میں صفر سے کچھ نہیں بدلتا۔"),
               T("0.6 is 6 tenths; 0.06 is 6 hundredths.", "0.6 چھ دسواں ہے؛ 0.06 چھ سوواں۔")]},
 ],
 "review_questions": [
   {"id": "r_hundredths", "type": "apply", "skill": SKILL, "step": number_question(
     "r_hundredths",
     T("Write 48/100 as a decimal.", "48/100 کو اعشاریہ میں لکھیں۔"),
     R1,
     T("Two places after the point for hundredths.", "سوویں کے لیے اعشاریہ کے بعد دو مقام۔"),
     T("Right! 48/100 = 0.48.", "درست! 48/100 = 0.48"),
     T("48 hundredths = 0.48.", "48 سوواں = 0.48"),
     common_wrong=[wrong(D("4.8"), "4.8 is more than 4! 48/100 is less than 1: 0.48.", "4.8 تو 4 سے زیادہ ہے! 48/100 ایک سے کم ہے: 0.48", "tenths_hundredths")],
     qtype=None)},
   {"id": "r_fifths", "type": "apply", "skill": SKILL, "step": number_question(
     "r_fifths",
     T("Write 2/5 as a decimal. Hint: make the bottom 10.", "2/5 کو اعشاریہ میں لکھیں۔ اشارہ: نسب نما 10 بنائیں۔"),
     R2,
     T("5 × 2 = 10, so 2/5 = 4/10.", "5 × 2 = 10، اس لیے 2/5 = 4/10"),
     T("Right! 2/5 = 4/10 = 0.4.", "درست! 2/5 = 4/10 = 0.4"),
     T("Multiply top and bottom by 2: 4/10 = 0.4.", "اوپر اور نیچے کو 2 سے ضرب دیں: 4/10 = 0.4"),
     common_wrong=[wrong(D("0.25"), "The digits of a fraction don't go after the point. 2/5 = 4/10 = 0.4.", "کسر کے ہندسے اعشاریہ کے بعد نہیں لکھے جاتے۔ 2/5 = 4/10 = 0.4", "fraction_digits"),
                   wrong(D("2.5"), "2/5 is less than 1. 2/5 = 4/10 = 0.4.", "2/5 ایک سے کم ہے۔ 2/5 = 4/10 = 0.4", "fraction_digits")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Decimals unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-03. Fix the names and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: اعشاریہ (decimal), اعشاری نقطہ (decimal point), دسواں حصہ (tenths), سوواں حصہ (hundredths), مقامی قیمت (place value).",
   "The number-line step uses the native number_line sim with decimal labels from 0 to 1 in tenths.",
   "The numbers were worked out in content/sources/g6-maths-03/decimals_place_value.py with exact Decimal arithmetic; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

from common import (T, D, opt, say, wrong, dec, number_question, write,
                    REF, REVIEW, DEC_ADD_SUBTRACT, DEC_MULTIPLY_DIVIDE)

SKILL = DEC_MULTIPLY_DIVIDE


def places(x):
    return max(0, -D(x).normalize().as_tuple().exponent) if D(x) != D(x).to_integral_value() else 0


# s1, s2: 4 bottles of 1.5 L
S2 = D("1.5") * 4
assert S2 == D("1.5") + D("1.5") + D("1.5") + D("1.5") == 6
# s3, s4, s5: × 10, × 100, ÷ 10
assert D("3.45") * 10 == D("34.5") and D("3.45") * 100 == 345 and D("6.2") / 10 == D("0.62")
S4 = D("0.75") * 100
assert S4 == 75
S5 = D("48.6") / 10
assert S5 == D("4.86")
# s6, s7: whole × decimal: multiply as whole numbers, then count places
assert 4 * 15 == 60 and D("1.5") * 4 == D("6.0")
S7 = 3 * D("2.4")
assert S7 == D("7.2") and 3 * 24 == 72
# s8: 0.3 × 0.2 has 1 + 1 = 2 places
S8 = D("0.3") * D("0.2")
assert S8 == D("0.06") and places("0.3") + places("0.2") == 2
# s9: 0.4 × 0.5 = 0.20, not 0.02
S9 = D("0.4") * D("0.5")
assert S9 == D("0.2") and 4 * 5 == 20
# s10: smaller than both
assert S8 < D("0.3") and S8 < D("0.2")
# s11: 7.5 ÷ 3
S11 = D("7.5") / 3
assert S11 == D("2.5")
# question bank and review
assert D("5.2") * 100 == 520
QB = 6 * D("0.7")
assert QB == D("4.2")
R1 = D("2.36") * 10
assert R1 == D("23.6")
R2 = D("9.6") / 4
assert R2 == D("2.4")


lesson = {
 "id": "g6-maths-03-multiplying-and-dividing-decimals",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Multiply and divide decimals by 10 and 100, multiply decimals, and divide a decimal by a whole number.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Multiplying and dividing decimals", "اعشاریہ اعداد کی ضرب اور تقسیم"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": DEC_ADD_SUBTRACT}],
 "misconceptions": [
   {"id": "add_a_zero", "description": "Multiplies by 10 by writing a 0 at the end: 0.75 × 10 = 0.750."},
   {"id": "point_count", "description": "Puts the decimal point in the wrong place after multiplying: 0.3 × 0.2 = 0.6."},
   {"id": "drop_point", "description": "Leaves the decimal point out of the answer: 3 × 2.4 = 72."},
   {"id": "lost_zero", "description": "Drops the zero of a product like 20 before counting places: 0.4 × 0.5 = 0.02."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_hundred", "type": "recall", "step": {
     "id": "qb_hundred", "type": "choice",
     "prompt": T("What is 5.2 × 100?", "5.2 × 100 کتنا ہے؟"),
     "options": [
       opt("right", "520", "520", True, "Yes! × 100 moves each digit two places left.", "جی ہاں! 100 سے ضرب ہر ہندسے کو دو مقام بائیں لے جاتی ہے۔"),
       opt("zeros", "5.200", "5.200", False, "Zeros at the end of a decimal change nothing. Move the digits two places: 520.", "اعشاریہ کے آخر میں صفر لگانے سے کچھ نہیں بدلتا۔ ہندسے دو مقام ہٹائیں: 520", "add_a_zero"),
       opt("one", "52", "52", False, "That is × 10. For × 100 move two places: 520.", "یہ 10 سے ضرب ہے۔ 100 کے لیے دو مقام ہٹائیں: 520"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Work out 6 × 0.7", "حل کریں: 6 × 0.7"),
     QB,
     T("6 × 7 = 42, and there is 1 decimal place.", "6 × 7 = 42، اور ایک اعشاری مقام ہے۔"),
     T(f"Right! 6 × 0.7 = {dec(QB)}.", f"درست! 6 × 0.7 = {dec(QB)}"),
     T(f"6 × 7 = 42. One decimal place: {dec(QB)}.", f"6 × 7 = 42۔ ایک اعشاری مقام: {dec(QB)}"),
     common_wrong=[wrong(42, "Count the decimal places: 0.7 has one, so the answer has one: 4.2.", "اعشاری مقام گنیں: 0.7 میں ایک ہے، اس لیے جواب میں ایک ہوگا: 4.2", "drop_point"),
                   wrong(D("0.42"), "0.7 has only one decimal place, so the answer has one: 4.2.", "0.7 میں صرف ایک اعشاری مقام ہے، اس لیے جواب میں ایک ہوگا: 4.2", "point_count")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Rida wrote 0.75 × 10 = 0.750. What went wrong?", "ردا نے لکھا 0.75 × 10 = 0.750۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("move", "Adding a zero at the end changes nothing. Move the digits one place left: 7.5.", "آخر میں صفر لگانے سے کچھ نہیں بدلتا۔ ہندسے ایک مقام بائیں ہٹائیں: 7.5", True,
           "Yes! 0.750 is still 0.75. × 10 gives 7.5.", "جی ہاں! 0.750 اب بھی 0.75 ہے۔ 10 سے ضرب کا جواب 7.5 ہے۔"),
       opt("nothing", "Nothing. Times 10 adds a zero.", "کوئی غلطی نہیں۔ 10 سے ضرب ایک صفر لگاتی ہے۔", False,
           "That only works for whole numbers. For decimals, move the digits: 7.5.", "یہ صرف مکمل اعداد کے لیے ہے۔ اعشاریہ میں ہندسے ہٹائیں: 7.5", "add_a_zero"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_ten", "front": T("× 10, × 100, ÷ 10 with decimals?", "اعشاریہ کو 10 اور 100 سے ضرب، 10 سے تقسیم؟"),
    "back": T("× 10: digits move 1 place left (3.45 → 34.5). × 100: 2 places (345). ÷ 10: 1 place right (6.2 → 0.62).",
              "× 10: ہندسے 1 مقام بائیں (3.45 → 34.5)۔ × 100: 2 مقام (345)۔ ÷ 10: 1 مقام دائیں (6.2 → 0.62)")},
   {"id": "f_places", "front": T("0.3 × 0.2 = ?", "0.3 × 0.2 = ؟"),
    "back": T("0.06. 3 × 2 = 6, and 1 + 1 = 2 decimal places.", "0.06۔ 3 × 2 = 6، اور 1 + 1 = 2 اعشاری مقام۔")},
 ],
 "home_tasks": [{"id": "h_milk", "text": T(
   "Find something at home sold in decimals, like a 1.5 L bottle or a 0.5 kg packet. How much would 4 of them be? How much is one tenth of it?",
   "گھر میں کوئی ایسی چیز ڈھونڈیں جو اعشاریہ میں بکتی ہو، جیسے 1.5 لیٹر کی بوتل یا 0.5 کلوگرام کا پیکٹ۔ ایسی 4 چیزیں کتنی ہوں گی؟ اس کا دسواں حصہ کتنا ہے؟")}],
 "glossary": [T("Product", "حاصل ضرب"), T("Decimal places", "اعشاری مقام"), T("Quotient", "حاصل تقسیم")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "One bottle holds 1.5 litres of water. How much do 4 bottles hold?",
      "ایک بوتل میں 1.5 لیٹر پانی آتا ہے۔ 4 بوتلوں میں کتنا آئے گا؟"),
    "text": T("Today we multiply and divide decimals. First, a quick check on adding.", "آج ہم اعشاریہ اعداد کی ضرب اور تقسیم کریں گے۔ پہلے جمع کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Work out 1.5 + 1.5 + 1.5 + 1.5", "حل کریں: 1.5 + 1.5 + 1.5 + 1.5"),
     S2,
     T("Two 1.5s make 3.", "دو 1.5 مل کر 3 بنتے ہیں۔"),
     T("Right! 4 bottles hold 6 litres. That is 4 × 1.5 = 6.", "درست! 4 بوتلوں میں 6 لیٹر آتا ہے۔ یعنی 4 × 1.5 = 6"),
     T("1.5 + 1.5 = 3, and 3 + 3 = 6.", "1.5 + 1.5 = 3، اور 3 + 3 = 6"),
     common_wrong=[wrong(D("4.2"), "Add the tenths too: 5 tenths × 4 = 20 tenths = 2. So 4 + 2 = 6.", "دسویں بھی جمع کریں: 5 دسواں × 4 = 20 دسواں = 2۔ اس لیے 4 + 2 = 6")],
     qtype="recall", skill=DEC_ADD_SUBTRACT),
   {"id": "s3_tens", "type": "explain",
    "character": say("happy", "Multiplying by 10 makes every digit worth ten times more!", "10 سے ضرب ہر ہندسے کی قیمت دس گنا کر دیتی ہے!"),
    "text": T("× 10: every digit moves one place to the left. 3.45 × 10 = 34.5. × 100: two places. 3.45 × 100 = 345. ÷ 10: every digit moves one place to the right. 6.2 ÷ 10 = 0.62. Writing a zero at the end of a decimal does NOT multiply it by 10: 0.750 is still 0.75.",
              "10 سے ضرب: ہر ہندسہ ایک مقام بائیں جاتا ہے۔ 3.45 × 10 = 34.5۔ 100 سے ضرب: دو مقام۔ 3.45 × 100 = 345۔ 10 سے تقسیم: ہر ہندسہ ایک مقام دائیں جاتا ہے۔ 6.2 ÷ 10 = 0.62۔ اعشاریہ کے آخر میں صفر لکھنے سے وہ 10 سے ضرب نہیں ہوتا: 0.750 اب بھی 0.75 ہے۔")},
   number_question(
     "s4_times_100",
     T("Work out 0.75 × 100", "حل کریں: 0.75 × 100"),
     S4,
     T("Move each digit two places to the left.", "ہر ہندسے کو دو مقام بائیں ہٹائیں۔"),
     T("Right! 0.75 × 100 = 75.", "درست! 0.75 × 100 = 75"),
     T("0.75 → 7.5 (× 10) → 75 (× 100).", "0.75 → 7.5 (× 10) → 75 (× 100)"),
     common_wrong=[wrong(D("7.5"), "That is × 10. For × 100 move two places: 75.", "یہ 10 سے ضرب ہے۔ 100 کے لیے دو مقام ہٹائیں: 75"),
                   wrong(D("0.75"), "Writing zeros at the end doesn't change 0.75. Move the digits: 75.", "آخر میں صفر لکھنے سے 0.75 نہیں بدلتا۔ ہندسے ہٹائیں: 75", "add_a_zero")]),
   number_question(
     "s5_divide_10",
     T("Work out 48.6 ÷ 10", "حل کریں: 48.6 ÷ 10"),
     S5,
     T("Move each digit one place to the right.", "ہر ہندسے کو ایک مقام دائیں ہٹائیں۔"),
     T(f"Right! 48.6 ÷ 10 = {dec(S5)}.", f"درست! 48.6 ÷ 10 = {dec(S5)}"),
     T(f"The 4 tens become 4 ones, the 8 ones become 8 tenths, the 6 tenths become 6 hundredths: {dec(S5)}.", f"4 دہائیاں 4 اکائیاں بن جاتی ہیں، 8 اکائیاں 8 دسواں، 6 دسواں 6 سوواں: {dec(S5)}"),
     common_wrong=[wrong(486, "Dividing makes it smaller, not bigger. Move the digits right: 4.86.", "تقسیم سے عدد چھوٹا ہوتا ہے، بڑا نہیں۔ ہندسے دائیں ہٹائیں: 4.86")]),
   {"id": "s6_count_places", "type": "explain",
    "character": say("thinking", "Multiply like whole numbers, then count the decimal places!", "مکمل اعداد کی طرح ضرب دیں، پھر اعشاری مقام گنیں!"),
    "text": T("To work out 4 × 1.5: forget the point and do 4 × 15 = 60. 1.5 has 1 decimal place, so the answer has 1: 6.0 = 6. For 0.3 × 0.2: 3 × 2 = 6. Each number has 1 decimal place: 1 + 1 = 2 places, so the answer is 0.06.",
              "4 × 1.5 کے لیے: نقطہ بھول جائیں اور 4 × 15 = 60 کریں۔ 1.5 میں 1 اعشاری مقام ہے، اس لیے جواب میں 1 ہوگا: 6.0 = 6۔ 0.3 × 0.2 کے لیے: 3 × 2 = 6۔ ہر عدد میں 1 اعشاری مقام ہے: 1 + 1 = 2 مقام، اس لیے جواب 0.06 ہے۔")},
   number_question(
     "s7_whole_times",
     T("Work out 3 × 2.4", "حل کریں: 3 × 2.4"),
     S7,
     T("3 × 24 = 72. How many decimal places?", "3 × 24 = 72۔ کتنے اعشاری مقام ہیں؟"),
     T(f"Right! 3 × 2.4 = {dec(S7)}.", f"درست! 3 × 2.4 = {dec(S7)}"),
     T(f"3 × 24 = 72, and 2.4 has 1 decimal place: {dec(S7)}.", f"3 × 24 = 72، اور 2.4 میں 1 اعشاری مقام ہے: {dec(S7)}"),
     common_wrong=[wrong(72, "Put the point back: 2.4 has 1 decimal place, so 7.2.", "نقطہ واپس لگائیں: 2.4 میں 1 اعشاری مقام ہے، اس لیے 7.2", "drop_point"),
                   wrong(D("6.4"), "Multiply the whole 2.4, not just the 2: 3 × 2.4 = 7.2.", "صرف 2 نہیں، پورا 2.4 ضرب دیں: 3 × 2.4 = 7.2")]),
   number_question(
     "s8_dec_times_dec",
     T("Work out 0.3 × 0.2", "حل کریں: 0.3 × 0.2"),
     S8,
     T("3 × 2 = 6. Count the decimal places in both numbers.", "3 × 2 = 6۔ دونوں اعداد کے اعشاری مقام گنیں۔"),
     T(f"Right! 0.3 × 0.2 = {dec(S8)}.", f"درست! 0.3 × 0.2 = {dec(S8)}"),
     T(f"3 × 2 = 6, and 1 + 1 = 2 decimal places: {dec(S8)}.", f"3 × 2 = 6، اور 1 + 1 = 2 اعشاری مقام: {dec(S8)}"),
     common_wrong=[wrong(D("0.6"), "Count the places in BOTH numbers: 1 + 1 = 2. So 0.06.", "دونوں اعداد کے مقام گنیں: 1 + 1 = 2۔ اس لیے 0.06", "point_count")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Ali wrote 0.4 × 0.5 = 0.02. What went wrong?", "علی نے لکھا 0.4 × 0.5 = 0.02۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("zero", "4 × 5 = 20, not 2. With 2 decimal places, 0.20 = 0.2.", "4 × 5 = 20 ہے، 2 نہیں۔ 2 اعشاری مقام کے ساتھ 0.20 = 0.2", True,
          "Yes! Keep the 0 of 20 until you have placed the point.", "جی ہاں! نقطہ لگانے تک 20 کا 0 رکھیں۔"),
      opt("places", "There should be only 1 decimal place: 2.0.", "صرف 1 اعشاری مقام ہونا چاہیے: 2.0", False,
          "Each number has 1 place, so 2 in all. The mistake is 4 × 5 = 20, not 2: 0.20.", "ہر عدد میں 1 مقام، کل 2۔ غلطی یہ ہے کہ 4 × 5 = 20 ہے، 2 نہیں: 0.20", "point_count"),
      opt("nothing", "Nothing. 4 × 5 has 2 decimal places.", "کوئی غلطی نہیں۔ 4 × 5 میں 2 اعشاری مقام ہیں۔", False,
          "The places are right, but 4 × 5 = 20: 0.20 = 0.2.", "مقام درست ہیں، مگر 4 × 5 = 20: 0.20 = 0.2", "lost_zero"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("surprised", "Wait! 0.3 × 0.2 = 0.06, and that is smaller than both numbers. I thought multiplying makes numbers bigger!",
                     "رکیں! 0.3 × 0.2 = 0.06، اور یہ دونوں اعداد سے چھوٹا ہے۔ میں سمجھتا تھا ضرب سے اعداد بڑے ہوتے ہیں!"),
    "task": T("In your own words: why is 0.3 × 0.2 smaller than 0.3?", "اپنے الفاظ میں بتائیں: 0.3 × 0.2، 0.3 سے چھوٹا کیوں ہے؟"),
    "key_idea": "0.2 is less than 1, so 0.3 × 0.2 means taking only part (2 tenths) of 0.3, which is less than 0.3. Multiplying by a number less than 1 makes a number smaller.",
    "levels": {
      "got_it": "Explains that 0.2 is less than 1, so multiplying by it takes only a part (2 tenths) of 0.3, which is smaller.",
      "partly": "Says multiplying by something less than 1 makes it smaller, without saying why, or only shows the working.",
      "not_yet": "Says the answer must be wrong, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["less than 1", "less than one", "ایک سے کم", "ek se kam", "smaller than 1"],
      ["part", "of", "حصہ", "hissa"],
      ["tenths", "دسواں", "daswan", "2/10"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 0.2 is less than 1, so 0.3 × 0.2 is only 2 tenths of 0.3, which is smaller.",
                  "بہت خوب سمجھایا! 0.2 ایک سے کم ہے، اس لیے 0.3 × 0.2 صرف 0.3 کا 2 دسواں حصہ ہے، جو چھوٹا ہے۔"),
      "partly": T("Good start! Now say what 'times 0.2' means: how much of 0.3 do we take?", "اچھی شروعات! اب بتائیں کہ '0.2 سے ضرب' کا کیا مطلب ہے: ہم 0.3 کا کتنا حصہ لیتے ہیں؟"),
      "not_yet": T("Think: 0.3 × 1 = 0.3. Is 0.2 more or less than 1? So is the answer more or less than 0.3?",
                   "سوچیں: 0.3 × 1 = 0.3۔ کیا 0.2 ایک سے زیادہ ہے یا کم؟ تو جواب 0.3 سے زیادہ ہوگا یا کم؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_share",
     T("Three friends share 7.5 kg of rice equally. How many kg does each get?", "تین دوست 7.5 کلوگرام چاول برابر بانٹتے ہیں۔ ہر ایک کو کتنے کلوگرام ملیں گے؟"),
     S11,
     T("Divide 7.5 by 3. Keep the point in the same place.", "7.5 کو 3 سے تقسیم کریں۔ نقطہ اسی جگہ رکھیں۔"),
     T(f"Right! 7.5 ÷ 3 = {dec(S11)} kg each.", f"درست! 7.5 ÷ 3 = {dec(S11)} کلوگرام ہر ایک کو۔"),
     T(f"75 ÷ 3 = 25, and 7.5 has 1 decimal place: {dec(S11)}. Check: 3 × 2.5 = 7.5.", f"75 ÷ 3 = 25، اور 7.5 میں 1 اعشاری مقام ہے: {dec(S11)}۔ جانچ: 3 × 2.5 = 7.5"),
     common_wrong=[wrong(25, "Each friend can't get more than 7.5 kg! Put the point back: 2.5.", "ہر دوست کو 7.5 کلوگرام سے زیادہ نہیں مل سکتا! نقطہ واپس لگائیں: 2.5", "drop_point")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can multiply and divide decimals now!", "اب آپ اعشاریہ کی ضرب اور تقسیم کر سکتے ہیں!"),
    "text": T("× 10 or × 100: move the digits 1 or 2 places left. ÷ 10: 1 place right. To multiply decimals, multiply like whole numbers, then give the answer as many decimal places as both numbers together. To divide by a whole number, keep the point in the same place.",
              "10 یا 100 سے ضرب: ہندسے 1 یا 2 مقام بائیں ہٹائیں۔ 10 سے تقسیم: 1 مقام دائیں۔ اعشاریہ کی ضرب کے لیے مکمل اعداد کی طرح ضرب دیں، پھر جواب میں اتنے اعشاری مقام رکھیں جتنے دونوں اعداد میں مل کر ہیں۔ مکمل عدد سے تقسیم میں نقطہ اسی جگہ رکھیں۔"),
    "points": [T("0.3 × 0.2 = 0.06", "0.3 × 0.2 = 0.06"), T("Multiplying by a number less than 1 makes it smaller.", "ایک سے کم عدد سے ضرب دینے پر عدد چھوٹا ہو جاتا ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_ten", "type": "recall", "skill": SKILL, "step": number_question(
     "r_ten",
     T("Work out 2.36 × 10", "حل کریں: 2.36 × 10"),
     R1,
     T("Move each digit one place to the left.", "ہر ہندسے کو ایک مقام بائیں ہٹائیں۔"),
     T(f"Right! 2.36 × 10 = {dec(R1)}.", f"درست! 2.36 × 10 = {dec(R1)}"),
     T(f"The 2 ones become 2 tens, the 3 tenths become 3 ones: {dec(R1)}.", f"2 اکائیاں 2 دہائیاں، 3 دسواں 3 اکائیاں بن جاتے ہیں: {dec(R1)}"),
     common_wrong=[wrong(D("2.360"), "A zero at the end changes nothing. Move the digits: 23.6.", "آخر میں صفر سے کچھ نہیں بدلتا۔ ہندسے ہٹائیں: 23.6", "add_a_zero")],
     qtype=None)},
   {"id": "r_divide", "type": "apply", "skill": SKILL, "step": number_question(
     "r_divide",
     T("Work out 9.6 ÷ 4", "حل کریں: 9.6 ÷ 4"),
     R2,
     T("96 ÷ 4 = 24. Keep 1 decimal place.", "96 ÷ 4 = 24۔ ایک اعشاری مقام رکھیں۔"),
     T(f"Right! 9.6 ÷ 4 = {dec(R2)}.", f"درست! 9.6 ÷ 4 = {dec(R2)}"),
     T(f"96 ÷ 4 = 24, so 9.6 ÷ 4 = {dec(R2)}. Check: 4 × 2.4 = 9.6.", f"96 ÷ 4 = 24، اس لیے 9.6 ÷ 4 = {dec(R2)}۔ جانچ: 4 × 2.4 = 9.6"),
     common_wrong=[wrong(24, "Put the point back: 9.6 ÷ 4 is less than 9.6, so 2.4.", "نقطہ واپس لگائیں: 9.6 ÷ 4، 9.6 سے کم ہے، اس لیے 2.4", "drop_point")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Decimals unit. No textbook text or exercises were used.",
   "The lesson says digits move (not that the point moves) for × 10 and ÷ 10; both ways are common, so check the Punjab textbook's wording.",
   "Division is only by whole numbers here; dividing by a decimal can come later.",
   "Urdu terms to check: اعشاری مقام (decimal places), حاصل ضرب (product), حاصل تقسیم (quotient).",
   "The numbers were worked out in content/sources/g6-maths-03/multiplying_dividing_decimals.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

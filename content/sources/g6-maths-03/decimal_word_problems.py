from common import (T, D, opt, say, wrong, dec, number_question, write,
                    REF, REVIEW, DEC_PLACE_VALUE, DEC_COMPARE, DEC_ADD_SUBTRACT,
                    DEC_MULTIPLY_DIVIDE, DEC_WORD_PROBLEMS)

SKILL = DEC_WORD_PROBLEMS

# s2: foundation
S2 = D("2.5") * 4
assert S2 == 10 and 2 * 4 + D("0.5") == D("8.5")
# s4: 1.25 km + 0.8 km; lining up the last digits gives 1.33
S4 = D("1.25") + D("0.8")
assert S4 == D("2.05") and D(125) / 100 + D(8) / 100 == D("1.33")
# s1, s5: long jump 3.5 m against 3.45 m
S5 = D("3.5") - D("3.45")
assert S5 == D("0.05") and D("3.5") > D("3.45")
# s6: 5 suits of 2.4 m
S6 = 5 * D("2.4")
assert S6 == 12 and 5 * 2 + D("0.4") == D("10.4")
# s7: 12.6 L into 6 jugs
S7 = D("12.6") / 6
assert S7 == D("2.1")
# s8: 5 kg flour, 0.75 kg a day for 3 days
USED = 3 * D("0.75")
S8 = 5 - USED
assert USED == D("2.25") and S8 == D("2.75") and 5 - D("0.75") == D("4.25")
# s9: 2 m ribbon in 4 equal pieces
S9 = D(2) / 4
assert S9 == D("0.5") and 2 * 4 == 8
# s10: estimate 4.9 × 3 ≈ 5 × 3 = 15
assert D("4.9") * 3 == D("14.7") and abs(D("14.7") - 15) < 1
# Unit test.
assert str(D("3.07")).split(".")[1][1] == "7"            # u1: 7 hundredths
U2 = max(D("0.6"), D("0.56"), D("0.065"))
assert U2 == D("0.6")                                    # u2
U3 = 8 - D("2.75")
assert U3 == D("5.25") and (8 - 2) + D("0.75") == D("6.75")  # u3
U4 = D("0.6") * D("0.4")
assert U4 == D("0.24")                                   # u4
U5 = D("14.4") / 6
assert U5 == D("2.4")                                    # u5
# Question bank and review.
QB = D("1.75") + D("2.5")
assert QB == D("4.25")
R1 = 4 * D("0.35")
assert R1 == D("1.4")
R2 = D("20") - D("12.85")
assert R2 == D("7.15")


lesson = {
 "id": "g6-maths-03-decimal-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems with decimals (lengths, weights and volumes), choosing the operation and checking with an estimate.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Decimal word problems", "اعشاریہ کے عملی سوالات"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": DEC_PLACE_VALUE}, {"skill": DEC_COMPARE}, {"skill": DEC_ADD_SUBTRACT}, {"skill": DEC_MULTIPLY_DIVIDE}],
 "misconceptions": [
   {"id": "wrong_operation", "description": "Picks the wrong operation for the story, like multiplying when the story shares equally."},
   {"id": "one_step_only", "description": "Stops after the first step of a two-step problem."},
   {"id": "no_estimate", "description": "Accepts an answer that is far from a quick estimate, like 4.9 × 3 = 1.47."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_operation", "type": "recall", "step": {
     "id": "qb_operation", "type": "choice",
     "prompt": T("4.8 litres of milk is poured equally into 4 glasses. Which sum finds how much is in each glass?", "4.8 لیٹر دودھ 4 گلاسوں میں برابر ڈالا جاتا ہے۔ کون سا سوال بتاتا ہے کہ ہر گلاس میں کتنا ہے؟"),
     "options": [
       opt("div", "4.8 ÷ 4", "4.8 ÷ 4", True, "Yes! Sharing equally is dividing: 1.2 litres each.", "جی ہاں! برابر بانٹنا تقسیم ہے: ہر ایک میں 1.2 لیٹر۔"),
       opt("mul", "4.8 × 4", "4.8 × 4", False, "That would be 4 times as much milk. Sharing is dividing.", "اس سے دودھ 4 گنا ہو جاتا۔ بانٹنا تقسیم ہے۔", "wrong_operation"),
       opt("sub", "4.8 − 4", "4.8 − 4", False, "Nothing is taken away. Share equally: divide.", "کچھ کم نہیں کیا جا رہا۔ برابر بانٹیں: تقسیم کریں۔", "wrong_operation"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A recipe needs 1.75 kg of potatoes and 2.5 kg of onions. How many kg is that in all?", "ایک ترکیب میں 1.75 کلوگرام آلو اور 2.5 کلوگرام پیاز چاہییں۔ کل کتنے کلوگرام ہیں؟"),
     QB,
     T("Add: 1.75 + 2.50.", "جمع کریں: 1.75 + 2.50"),
     T(f"Right! {dec(QB)} kg.", f"درست! {dec(QB)} کلوگرام۔"),
     T(f"1.75 + 2.50 = {dec(QB)}.", f"1.75 + 2.50 = {dec(QB)}"),
     common_wrong=[wrong(D("2.00"), "Line up the points: 1.75 + 2.50.", "نقطے سیدھ میں رکھیں: 1.75 + 2.50")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Kamran worked out 4.9 × 3 = 1.47. How can you tell quickly that it is wrong?", "کامران نے 4.9 × 3 = 1.47 حل کیا۔ آپ جلدی کیسے بتا سکتے ہیں کہ یہ غلط ہے؟"),
     "options": [
       opt("estimate", "4.9 is about 5, and 5 × 3 = 15. 1.47 is far too small.", "4.9 تقریباً 5 ہے، اور 5 × 3 = 15۔ 1.47 بہت چھوٹا ہے۔", True,
           "Yes! The answer is 14.7: the point was put in the wrong place.", "جی ہاں! جواب 14.7 ہے: نقطہ غلط جگہ لگا تھا۔"),
       opt("cant", "You can't tell without working it out again.", "دوبارہ حل کیے بغیر نہیں بتا سکتے۔", False,
           "A quick estimate tells you: about 5 × 3 = 15.", "ایک فوری اندازہ بتا دیتا ہے: تقریباً 5 × 3 = 15", "no_estimate"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_choose", "front": T("How do you choose the operation in a decimal story?", "اعشاریہ کی کہانی میں عمل کیسے چنتے ہیں؟"),
    "back": T("Putting together: add. How much more or left: subtract. Equal groups: multiply. Sharing equally: divide. Then estimate to check.",
              "اکٹھا کرنا: جمع۔ کتنا زیادہ یا باقی: تفریق۔ برابر گروہ: ضرب۔ برابر بانٹنا: تقسیم۔ پھر اندازے سے جانچیں۔")},
   {"id": "f_estimate", "front": T("Why estimate?", "اندازہ کیوں لگائیں؟"),
    "back": T("To catch a decimal point in the wrong place: 4.9 × 3 is about 15, so 14.7 makes sense and 1.47 does not.", "غلط جگہ لگا نقطہ پکڑنے کے لیے: 4.9 × 3 تقریباً 15 ہے، اس لیے 14.7 درست لگتا ہے اور 1.47 نہیں۔")},
 ],
 "home_tasks": [{"id": "h_story", "text": T(
   "Make up a decimal story about cooking, shopping or travel. Write the sum and the answer, then ask someone at home to solve it.",
   "کھانا پکانے، خریداری یا سفر کے بارے میں اعشاریہ کی ایک کہانی بنائیں۔ سوال اور جواب لکھیں، پھر گھر میں کسی سے حل کروائیں۔")}],
 "glossary": [T("Estimate", "اندازہ"), T("Total", "کل"), T("Each", "ہر ایک")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "On sports day, Sara jumps 3.5 m and Hina jumps 3.45 m. Who wins, and by how much?",
      "کھیلوں کے دن سارہ 3.5 میٹر اور حنا 3.45 میٹر چھلانگ لگاتی ہیں۔ کون جیتتا ہے، اور کتنے فرق سے؟"),
    "text": T("Decimals are everywhere: lengths, weights, litres and times. Today we solve stories with them. First, a quick check.",
              "اعشاریہ ہر جگہ ہیں: لمبائی، وزن، لیٹر اور وقت۔ آج ہم ان سے کہانیاں حل کریں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Work out 2.5 × 4", "حل کریں: 2.5 × 4"),
     S2,
     T("25 × 4 = 100, with 1 decimal place.", "25 × 4 = 100، ایک اعشاری مقام کے ساتھ۔"),
     T("Right! 2.5 × 4 = 10.", "درست! 2.5 × 4 = 10"),
     T("25 × 4 = 100. One decimal place: 10.0 = 10.", "25 × 4 = 100۔ ایک اعشاری مقام: 10.0 = 10"),
     common_wrong=[wrong(D("8.5"), "Multiply the 0.5 too: 0.5 × 4 = 2. So 8 + 2 = 10.", "0.5 کو بھی ضرب دیں: 0.5 × 4 = 2۔ اس لیے 8 + 2 = 10"),
                   wrong(100, "Put the point back: one decimal place, so 10.", "نقطہ واپس لگائیں: ایک اعشاری مقام، اس لیے 10")],
     qtype="recall", skill=DEC_MULTIPLY_DIVIDE),
   {"id": "s3_which_operation", "type": "explain",
    "character": say("thinking", "Read the story, choose the operation, then estimate to check!", "کہانی پڑھیں، عمل چنیں، پھر اندازے سے جانچیں!"),
    "text": T("Putting amounts together: add. How much more, or how much is left: subtract. Equal groups: multiply. Sharing equally: divide. Then estimate with whole numbers: 4.9 × 3 is about 5 × 3 = 15. If your answer is far from the estimate, check the decimal point.",
              "مقداریں اکٹھی کرنا: جمع۔ کتنا زیادہ، یا کتنا باقی: تفریق۔ برابر گروہ: ضرب۔ برابر بانٹنا: تقسیم۔ پھر مکمل اعداد سے اندازہ لگائیں: 4.9 × 3 تقریباً 5 × 3 = 15۔ اگر جواب اندازے سے بہت دور ہو تو اعشاری نقطہ دیکھیں۔")},
   number_question(
     "s4_walk",
     T("Ahmed walks 1.25 km to school and then 0.8 km to the tuition centre. How many km does he walk in all?", "احمد اسکول تک 1.25 کلومیٹر اور پھر ٹیوشن سینٹر تک 0.8 کلومیٹر پیدل چلتا ہے۔ وہ کل کتنے کلومیٹر چلتا ہے؟"),
     S4,
     T("Add, lining up the points: 1.25 + 0.80.", "نقطے سیدھ میں رکھ کر جمع کریں: 1.25 + 0.80"),
     T(f"Right! {dec(S4)} km.", f"درست! {dec(S4)} کلومیٹر۔"),
     T(f"1.25 + 0.80 = {dec(S4)}. Estimate: about 1 + 1 = 2.", f"1.25 + 0.80 = {dec(S4)}۔ اندازہ: تقریباً 1 + 1 = 2"),
     common_wrong=[wrong(D("1.33"), "The 8 is 8 tenths, not 8 hundredths. Write 0.80 and line up the points.", "8 آٹھ دسواں ہے، آٹھ سوواں نہیں۔ 0.80 لکھیں اور نقطے سیدھ میں رکھیں۔")]),
   number_question(
     "s5_long_jump",
     T("Back to sports day: Sara jumped 3.5 m and Hina 3.45 m. By how many metres did Sara win?", "واپس کھیلوں کے دن پر: سارہ نے 3.5 میٹر اور حنا نے 3.45 میٹر چھلانگ لگائی۔ سارہ کتنے میٹر سے جیتی؟"),
     S5,
     T("How much more: subtract 3.50 − 3.45.", "کتنا زیادہ: تفریق کریں 3.50 − 3.45"),
     T(f"Right! Sara won by {dec(S5)} m, just 5 cm.", f"درست! سارہ {dec(S5)} میٹر سے جیتی، صرف 5 سینٹی میٹر۔"),
     T(f"3.50 − 3.45 = {dec(S5)}.", f"3.50 − 3.45 = {dec(S5)}"),
     common_wrong=[wrong(D("0.4"), "Write 3.5 as 3.50 first, then subtract: 3.50 − 3.45 = 0.05.", "پہلے 3.5 کو 3.50 لکھیں، پھر تفریق کریں: 3.50 − 3.45 = 0.05")]),
   number_question(
     "s6_tailor",
     T("A tailor needs 2.4 m of cloth for one suit. How many metres does he need for 5 suits?", "ایک درزی کو ایک سوٹ کے لیے 2.4 میٹر کپڑا چاہیے۔ 5 سوٹوں کے لیے کتنے میٹر چاہییں؟"),
     S6,
     T("5 equal groups of 2.4: multiply.", "2.4 کے 5 برابر گروہ: ضرب دیں۔"),
     T(f"Right! 5 × 2.4 = {dec(S6)} m.", f"درست! 5 × 2.4 = {dec(S6)} میٹر۔"),
     T(f"5 × 24 = 120, with 1 decimal place: 12.0 = {dec(S6)}.", f"5 × 24 = 120، ایک اعشاری مقام کے ساتھ: 12.0 = {dec(S6)}"),
     common_wrong=[wrong(D("10.4"), "Multiply the 0.4 too: 5 × 0.4 = 2. So 10 + 2 = 12.", "0.4 کو بھی ضرب دیں: 5 × 0.4 = 2۔ اس لیے 10 + 2 = 12"),
                   wrong(D("7.4"), "Equal groups means multiply, not add.", "برابر گروہ کا مطلب ضرب ہے، جمع نہیں۔", "wrong_operation")]),
   number_question(
     "s7_juice",
     T("12.6 litres of juice is poured equally into 6 jugs. How many litres are in each jug?", "12.6 لیٹر جوس 6 جگوں میں برابر ڈالا جاتا ہے۔ ہر جگ میں کتنے لیٹر ہیں؟"),
     S7,
     T("Sharing equally: divide 12.6 by 6.", "برابر بانٹنا: 12.6 کو 6 سے تقسیم کریں۔"),
     T(f"Right! {dec(S7)} litres each.", f"درست! ہر ایک میں {dec(S7)} لیٹر۔"),
     T(f"126 ÷ 6 = 21, so 12.6 ÷ 6 = {dec(S7)}. Check: 6 × 2.1 = 12.6.", f"126 ÷ 6 = 21، اس لیے 12.6 ÷ 6 = {dec(S7)}۔ جانچ: 6 × 2.1 = 12.6"),
     common_wrong=[wrong(21, "One jug can't hold more than all the juice! 12.6 ÷ 6 = 2.1.", "ایک جگ میں سارے جوس سے زیادہ نہیں آ سکتا! 12.6 ÷ 6 = 2.1"),
                   wrong(D("75.6"), "Sharing makes each part smaller: divide, don't multiply.", "بانٹنے سے ہر حصہ چھوٹا ہوتا ہے: تقسیم کریں، ضرب نہیں۔", "wrong_operation")]),
   number_question(
     "s8_two_steps",
     T("Ammi has 5 kg of flour. She uses 0.75 kg each day for 3 days. How many kg are left?", "امی کے پاس 5 کلوگرام آٹا ہے۔ وہ 3 دن تک ہر روز 0.75 کلوگرام استعمال کرتی ہیں۔ کتنے کلوگرام باقی ہیں؟"),
     S8,
     T("Two steps: first 3 × 0.75, then take that from 5.", "دو قدم: پہلے 3 × 0.75، پھر اسے 5 میں سے تفریق کریں۔"),
     T(f"Right! She used {dec(USED)} kg, so {dec(S8)} kg are left.", f"درست! انہوں نے {dec(USED)} کلوگرام استعمال کیا، اس لیے {dec(S8)} کلوگرام باقی ہے۔"),
     T(f"3 × 0.75 = {dec(USED)}. 5.00 − {dec(USED)} = {dec(S8)}.", f"3 × 0.75 = {dec(USED)}۔ 5.00 − {dec(USED)} = {dec(S8)}"),
     common_wrong=[wrong(D("4.25"), "That is only one day. She uses 0.75 kg on each of 3 days.", "یہ صرف ایک دن ہے۔ وہ 3 دن ہر روز 0.75 کلوگرام استعمال کرتی ہیں۔", "one_step_only"),
                   wrong(USED, f"{dec(USED)} kg is what she used. The question asks what is left.", f"{dec(USED)} کلوگرام استعمال ہوا۔ سوال یہ ہے کہ کتنا باقی ہے۔", "one_step_only")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A 2 m ribbon is cut into 4 equal pieces. Hira says each piece is 8 m long. What went wrong?", "2 میٹر کا فیتہ 4 برابر ٹکڑوں میں کاٹا جاتا ہے۔ حرا کہتی ہے ہر ٹکڑا 8 میٹر لمبا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("divide", "She multiplied. Cutting into equal pieces is dividing: 2 ÷ 4 = 0.5 m.", "اس نے ضرب دی۔ برابر ٹکڑوں میں کاٹنا تقسیم ہے: 2 ÷ 4 = 0.5 میٹر", True,
          "Yes! A piece can't be longer than the whole ribbon.", "جی ہاں! ایک ٹکڑا پورے فیتے سے لمبا نہیں ہو سکتا۔"),
      opt("two", "Each piece should be 2 m.", "ہر ٹکڑا 2 میٹر ہونا چاہیے۔", False,
          "2 m is the whole ribbon. Share it into 4: 0.5 m.", "2 میٹر پورا فیتہ ہے۔ اسے 4 میں بانٹیں: 0.5 میٹر", "wrong_operation"),
      opt("nothing", "Nothing. 2 × 4 = 8.", "کوئی غلطی نہیں۔ 2 × 4 = 8", False,
          "8 m is longer than the whole ribbon! Cutting into pieces is dividing.", "8 میٹر تو پورے فیتے سے لمبا ہے! ٹکڑوں میں کاٹنا تقسیم ہے۔", "wrong_operation"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "My friend got 4.9 × 3 = 1.47. How can we check quickly, without doing it again?",
                     "میرے دوست کا جواب 4.9 × 3 = 1.47 آیا۔ ہم دوبارہ حل کیے بغیر جلدی کیسے جانچیں؟"),
    "task": T("In your own words: how can an estimate show that 4.9 × 3 = 1.47 is wrong? What is the right answer?",
              "اپنے الفاظ میں بتائیں: اندازہ کیسے دکھاتا ہے کہ 4.9 × 3 = 1.47 غلط ہے؟ درست جواب کیا ہے؟"),
    "key_idea": "4.9 is close to 5, and 5 × 3 = 15, so the answer must be close to 15. 1.47 is far too small: the decimal point is in the wrong place. The answer is 14.7.",
    "levels": {
      "got_it": "Rounds 4.9 to 5 and estimates 15, says 1.47 is too small (point in the wrong place), and gives 14.7.",
      "partly": "Gives the estimate or the right answer 14.7, but not both, or doesn't explain why 1.47 is wrong.",
      "not_yet": "Agrees with 1.47, gives no estimate, or the reasoning is wrong."},
    "keywords": [
      ["5", "about", "round", "تقریباً", "taqreeban", "andaza", "اندازہ"],
      ["15", "پندرہ", "pandrah"],
      ["14.7", "point", "نقطہ", "nuqta"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 4.9 × 3 is about 5 × 3 = 15, so 1.47 is far too small. The answer is 14.7.",
                  "بہت خوب سمجھایا! 4.9 × 3 تقریباً 5 × 3 = 15 ہے، اس لیے 1.47 بہت چھوٹا ہے۔ جواب 14.7 ہے۔"),
      "partly": T("Good start! Round 4.9 to a whole number. What is the estimate, and is 1.47 close to it?", "اچھی شروعات! 4.9 کو مکمل عدد بنائیں۔ اندازہ کیا ہے، اور کیا 1.47 اس کے قریب ہے؟"),
      "not_yet": T("Think: 4.9 is close to which whole number? What is that number times 3?",
                   "سوچیں: 4.9 کس مکمل عدد کے قریب ہے؟ اس عدد کو 3 سے ضرب دیں تو کیا آتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Decimals unit. You can do it!", "ٹیسٹ کا وقت! اعشاریہ کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on each part of the unit: place value, comparing, adding and subtracting, multiplying and dividing. Line up the points and check your decimal places.",
              "اس چھوٹے ٹیسٹ میں باب کے ہر حصے سے سوال ہیں: مقامی قیمت، موازنہ، جمع اور تفریق، ضرب اور تقسیم۔ نقطے سیدھ میں رکھیں اور اعشاری مقام جانچیں۔")},
   {"id": "u1_place", "type": "choice", "question_type": "recall", "skill": DEC_PLACE_VALUE,
    "prompt": T("Test 1: In 3.07, what is the value of the 7?", "ٹیسٹ 1: 3.07 میں 7 کی قیمت کیا ہے؟"),
    "options": [
      opt("hundredths", "7 hundredths (0.07)", "7 سوواں (0.07)", True, "Yes! The 7 is in the second place after the point.", "جی ہاں! 7 اعشاریہ کے بعد دوسرے مقام پر ہے۔"),
      opt("tenths", "7 tenths (0.7)", "7 دسواں (0.7)", False, "The tenths digit is 0. The 7 is hundredths.", "دسویں کا ہندسہ 0 ہے۔ 7 سوواں ہے۔"),
      opt("seven", "7", "7", False, "The 7 is after the point, so it is less than 1.", "7 اعشاریہ کے بعد ہے، اس لیے ایک سے کم ہے۔"),
    ]},
   number_question(
     "u2_compare",
     T("Test 2: Which is the greatest: 0.6, 0.56 or 0.065? Type it.", "ٹیسٹ 2: سب سے بڑا کون سا ہے: 0.6، 0.56 یا 0.065؟ لکھیں۔"),
     U2,
     T("Write them with three places: 0.600, 0.560, 0.065.", "تین مقام کے ساتھ لکھیں: 0.600، 0.560، 0.065"),
     T("Right! 0.6 has the most tenths.", "درست! 0.6 میں سب سے زیادہ دسواں ہیں۔"),
     T("Compare tenths: 6, 5, 0. So 0.6 is the greatest.", "دسویں کا موازنہ کریں: 6، 5، 0۔ اس لیے 0.6 سب سے بڑا ہے۔"),
     common_wrong=[wrong(D("0.065"), "More digits doesn't mean bigger. 0.065 has 0 tenths.", "زیادہ ہندسوں کا مطلب بڑا نہیں۔ 0.065 میں 0 دسواں ہیں۔"),
                   wrong(D("0.56"), "0.6 = 0.60, which is more than 0.56.", "0.6 = 0.60، جو 0.56 سے زیادہ ہے۔")],
     qtype="recall", skill=DEC_COMPARE),
   number_question(
     "u3_subtract",
     T("Test 3: Work out 8 − 2.75", "ٹیسٹ 3: حل کریں: 8 − 2.75"),
     U3,
     T("Write 8.00 − 2.75.", "8.00 − 2.75 لکھیں۔"),
     T(f"Right! 8 − 2.75 = {dec(U3)}.", f"درست! 8 − 2.75 = {dec(U3)}"),
     T(f"8.00 − 2.75 = {dec(U3)}. Check: {dec(U3)} + 2.75 = 8.", f"8.00 − 2.75 = {dec(U3)}۔ جانچ: {dec(U3)} + 2.75 = 8"),
     common_wrong=[wrong(D("6.75"), "Take away the 0.75 too: 8.00 − 2.75 = 5.25.", "0.75 بھی تفریق کریں: 8.00 − 2.75 = 5.25")],
     qtype="apply", skill=DEC_ADD_SUBTRACT),
   number_question(
     "u4_multiply",
     T("Test 4: Work out 0.6 × 0.4", "ٹیسٹ 4: حل کریں: 0.6 × 0.4"),
     U4,
     T("6 × 4 = 24. How many decimal places?", "6 × 4 = 24۔ کتنے اعشاری مقام؟"),
     T(f"Right! 0.6 × 0.4 = {dec(U4)}.", f"درست! 0.6 × 0.4 = {dec(U4)}"),
     T(f"6 × 4 = 24, and 1 + 1 = 2 decimal places: {dec(U4)}.", f"6 × 4 = 24، اور 1 + 1 = 2 اعشاری مقام: {dec(U4)}"),
     common_wrong=[wrong(D("2.4"), "Count the places in both numbers: 2. So 0.24.", "دونوں اعداد کے مقام گنیں: 2۔ اس لیے 0.24")],
     qtype="apply", skill=DEC_MULTIPLY_DIVIDE),
   number_question(
     "u5_divide",
     T("Test 5: Work out 14.4 ÷ 6", "ٹیسٹ 5: حل کریں: 14.4 ÷ 6"),
     U5,
     T("144 ÷ 6 = 24. Keep 1 decimal place.", "144 ÷ 6 = 24۔ ایک اعشاری مقام رکھیں۔"),
     T(f"Right! 14.4 ÷ 6 = {dec(U5)}.", f"درست! 14.4 ÷ 6 = {dec(U5)}"),
     T(f"144 ÷ 6 = 24, so 14.4 ÷ 6 = {dec(U5)}. Check: 6 × 2.4 = 14.4.", f"144 ÷ 6 = 24، اس لیے 14.4 ÷ 6 = {dec(U5)}۔ جانچ: 6 × 2.4 = 14.4"),
     common_wrong=[wrong(24, "Put the point back: the answer is less than 14.4. So 2.4.", "نقطہ واپس لگائیں: جواب 14.4 سے کم ہے۔ اس لیے 2.4")],
     qtype="recall", skill=DEC_MULTIPLY_DIVIDE),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You finished the whole Decimals unit. Shabash!", "آپ نے اعشاریہ کا پورا باب مکمل کر لیا۔ شاباش!"),
    "text": T("In a decimal story, decide what is asked. Putting together: add. How much more or left: subtract. Equal groups: multiply. Sharing equally: divide. Some stories need two steps. Always estimate with whole numbers to check the decimal point.",
              "اعشاریہ کی کہانی میں سمجھیں کہ کیا پوچھا گیا ہے۔ اکٹھا کرنا: جمع۔ کتنا زیادہ یا باقی: تفریق۔ برابر گروہ: ضرب۔ برابر بانٹنا: تقسیم۔ کچھ کہانیوں میں دو قدم ہوتے ہیں۔ اعشاری نقطہ جانچنے کے لیے ہمیشہ مکمل اعداد سے اندازہ لگائیں۔"),
    "points": [T("4.9 × 3 ≈ 15, so the answer is 14.7.", "4.9 × 3 ≈ 15، اس لیے جواب 14.7 ہے۔"),
               T("A piece is never longer than the whole.", "ایک ٹکڑا کبھی پورے سے لمبا نہیں ہوتا۔")]},
 ],
 "review_questions": [
   {"id": "r_bottles", "type": "apply", "skill": SKILL, "step": number_question(
     "r_bottles",
     T("A small bottle holds 0.35 litres. How many litres do 4 bottles hold?", "ایک چھوٹی بوتل میں 0.35 لیٹر آتا ہے۔ 4 بوتلوں میں کتنے لیٹر آئیں گے؟"),
     R1,
     T("4 equal groups: 4 × 0.35.", "4 برابر گروہ: 4 × 0.35"),
     T(f"Right! 4 × 0.35 = {dec(R1)} litres.", f"درست! 4 × 0.35 = {dec(R1)} لیٹر۔"),
     T(f"4 × 35 = 140, with 2 decimal places: 1.40 = {dec(R1)}.", f"4 × 35 = 140، دو اعشاری مقام کے ساتھ: 1.40 = {dec(R1)}"),
     common_wrong=[wrong(D("14"), "Two decimal places: 1.40 = 1.4. Estimate: 4 × about 0.3 is about 1.2.", "دو اعشاری مقام: 1.40 = 1.4۔ اندازہ: 4 × تقریباً 0.3 تقریباً 1.2 ہے۔", "no_estimate")],
     qtype=None)},
   {"id": "r_change", "type": "apply", "skill": SKILL, "step": number_question(
     "r_change",
     T("A water tank holds 20 litres. 12.85 litres are used. How many litres are left?", "پانی کی ٹینکی میں 20 لیٹر آتا ہے۔ 12.85 لیٹر استعمال ہو گیا۔ کتنے لیٹر باقی ہیں؟"),
     R2,
     T("How much is left: 20.00 − 12.85.", "کتنا باقی: 20.00 − 12.85"),
     T(f"Right! {dec(R2)} litres are left.", f"درست! {dec(R2)} لیٹر باقی ہیں۔"),
     T(f"20.00 − 12.85 = {dec(R2)}. Check: {dec(R2)} + 12.85 = 20.", f"20.00 − 12.85 = {dec(R2)}۔ جانچ: {dec(R2)} + 12.85 = 20"),
     common_wrong=[wrong(D("8.85"), "Take away the 0.85 too: 20.00 − 12.85 = 7.15.", "0.85 بھی تفریق کریں: 20.00 − 12.85 = 7.15")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Decimals unit. No textbook text or exercises were used. Lengths, weights and volumes are made up for the sums; money is left out because rupee prices are now mostly whole numbers.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-03. Fix the names and curriculum_refs if the unit differs.",
   "The lesson teaches choosing the operation (s3) and checking with a whole-number estimate (s10).",
   "s11 to u5 are a short unit test. Each u-step is tagged with an earlier lesson's skill (place_value, compare, add_subtract, multiply_divide), so it counts as practice for that skill rather than for word problems.",
   "The numbers were worked out in content/sources/g6-maths-03/decimal_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

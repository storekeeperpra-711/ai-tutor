from common import (D, T, opt, say, wrong, number_question, write,
                    REF, REVIEW, DEC_ADD_SUBTRACT, DEC_MULTIPLY_DIVIDE, PL_BILLS)

SKILL = PL_BILLS

# s2: 3 x Rs 45.50
S2 = 3 * D("45.50")
assert S2 == D("136.50")
# s4: 2 kg sugar at Rs 160 a kg
S4 = 2 * 160
assert S4 == 320
# s5: bill: 2 kg sugar at 160, 3 packets biscuits at 35, 1 litre milk at 220
S5 = 2 * 160 + 3 * 35 + 1 * 220
assert S5 == 645
# s6: paid Rs 1000 for that bill
assert 1000 - S5 == 355
# s7: 4 notebooks at Rs 85.50, paid with Rs 500
S7 = 500 - 4 * D("85.50")
assert 4 * D("85.50") == 342 and S7 == 158
# s8: bill Rs 1235, paid with a 1000 note and a 500 note
S8 = 1000 + 500 - 1235
assert S8 == 265
# s9: 3 pens at 25 and 2 erasers at 15 is 105, not 25 + 15 = 40
assert 3 * 25 + 2 * 15 == 105 and 25 + 15 == 40
# s11: 1.5 kg tomatoes at 120, 0.5 kg ginger at 600, paid Rs 500
S11_BILL = D("1.5") * 120 + D("0.5") * 600
assert S11_BILL == 480
S11 = 500 - S11_BILL
assert S11 == 20
# question bank and review
QB = 200 - 5 * 30
assert QB == 50
R1 = 3 * 140
assert R1 == 420
R2 = 1000 - 785
assert R2 == 215

lesson = {
 "id": "g6-maths-12-bills-and-change",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Read and make a simple shop bill, find the total, and work out the change.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Bills and change", "بل اور بقایا"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": DEC_ADD_SUBTRACT}, {"skill": DEC_MULTIPLY_DIVIDE}],
 "misconceptions": [
   {"id": "forgets_quantity", "description": "Adds the rate of each item and forgets to multiply by how many were bought."},
   {"id": "total_as_change", "description": "Gives the bill total when the question asks for the change."},
   {"id": "change_wrong_way", "description": "Adds the bill to the money paid instead of taking it away."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("How do you find the change?", "بقایا کیسے نکالتے ہیں؟"),
     "options": [
       opt("minus", "Money given − bill total", "دی گئی رقم − بل کا کل", True,
           "Yes! Change is what comes back.", "جی ہاں! بقایا وہ ہے جو واپس آتا ہے۔"),
       opt("plus", "Money given + bill total", "دی گئی رقم + بل کا کل", False,
           "Change is smaller than the money given. Take the bill away.", "بقایا دی گئی رقم سے کم ہوتا ہے۔ بل نفی کریں۔", "change_wrong_way"),
       opt("total", "It is the bill total", "یہ بل کا کل ہے", False,
           "The total is what you pay. The change is what is left over.", "کل وہ ہے جو آپ دیتے ہیں۔ بقایا وہ ہے جو بچ جاتا ہے۔", "total_as_change"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Zara buys 5 eggs at Rs 30 each and pays with a Rs 200 note. How much change does she get, in rupees?", "زارا 30 روپے فی انڈا کے حساب سے 5 انڈے خریدتی ہے اور 200 روپے کا نوٹ دیتی ہے۔ اسے کتنے روپے بقایا ملے گا؟"),
     QB,
     T("Bill: 5 × 30. Then 200 − bill.", "بل: 5 × 30۔ پھر 200 − بل"),
     T("Right! Rs 50.", "درست! 50 روپے"),
     T("Bill = 150. Change = 200 − 150 = 50.", "بل = 150۔ بقایا = 200 − 150 = 50"),
     common_wrong=[wrong(150, "Rs 150 is the bill. Change: 200 − 150 = 50.", "150 روپے بل ہے۔ بقایا: 200 − 150 = 50", "total_as_change"),
                   wrong(170, "5 eggs cost 5 × 30 = 150, not 30. Change: 50.", "5 انڈے 5 × 30 = 150 کے ہیں، 30 کے نہیں۔ بقایا: 50", "forgets_quantity")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A bill has 3 pens at Rs 25 and 2 erasers at Rs 15. Bilal writes the total as 25 + 15 = Rs 40. What is wrong?", "ایک بل میں 25 روپے کے 3 قلم اور 15 روپے کے 2 ربڑ ہیں۔ بلال کل 25 + 15 = 40 روپے لکھتا ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("qty", "He forgot how many: 3 × 25 + 2 × 15 = Rs 105.", "وہ تعداد بھول گیا: 3 × 25 + 2 × 15 = 105 روپے", True,
           "Yes! Multiply each rate by how many, then add.", "جی ہاں! ہر قیمت کو تعداد سے ضرب دیں، پھر جمع کریں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "There are 3 pens and 2 erasers, not one of each.", "3 قلم اور 2 ربڑ ہیں، ہر ایک کا ایک نہیں۔", "forgets_quantity"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_line", "front": T("Amount for one line of a bill?", "بل کی ایک لائن کی رقم؟"),
    "back": T("Quantity × rate", "تعداد × قیمت فی عدد")},
   {"id": "f_change", "front": T("Change?", "بقایا؟"),
    "back": T("Money given − bill total", "دی گئی رقم − بل کا کل")},
 ],
 "home_tasks": [{"id": "h_bill", "text": T(
   "Next time someone at home goes shopping, ask to see the bill, or write one together. Check each line (quantity × rate), check the total, and work out the change from the note they paid with.",
   "اگلی بار جب گھر میں کوئی خریداری کرے تو بل دیکھنے کو کہیں، یا مل کر ایک بل بنائیں۔ ہر لائن جانچیں (تعداد × قیمت)، کل جانچیں، اور دیے گئے نوٹ سے بقایا نکالیں۔")}],
 "glossary": [T("Bill", "بل"), T("Rate", "قیمت فی عدد"), T("Total", "کل"), T("Change", "بقایا")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "At the shop, Ammi pays with a Rs 1000 note. How do we check the bill and the change?",
                     "دکان پر امی 1000 روپے کا نوٹ دیتی ہیں۔ ہم بل اور بقایا کیسے جانچیں؟"),
    "text": T("Today we read bills and work out change. First, a quick decimal check.", "آج ہم بل پڑھیں گے اور بقایا نکالیں گے۔ پہلے اعشاریہ کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("3 × Rs 45.50 = ? rupees", "3 × 45.50 روپے = ? روپے"),
     S2,
     T("3 × 45 = 135, and 3 × 0.50 = 1.50.", "3 × 45 = 135، اور 3 × 0.50 = 1.50"),
     T("Right! Rs 136.50.", "درست! 136.50 روپے"),
     T("135 + 1.50 = 136.50.", "135 + 1.50 = 136.50"),
     common_wrong=[wrong(D("135.50"), "Multiply the paisa too: 3 × 0.50 = 1.50, so 136.50.", "پیسے بھی ضرب دیں: 3 × 0.50 = 1.50، تو 136.50")],
     qtype="recall", skill=DEC_MULTIPLY_DIVIDE),
   {"id": "s3_bill", "type": "explain",
    "character": say("happy", "Each line: how many times the rate. Then add the lines. Then the change.", "ہر لائن: تعداد ضرب قیمت۔ پھر لائنیں جمع کریں۔ پھر بقایا۔"),
    "text": T("A bill lists each item, how many (quantity), the price of one (rate) and the amount for that line: quantity × rate. Add all the lines to get the total. If you pay with a note, change = money given − total.",
              "بل میں ہر چیز، اس کی تعداد، ایک کی قیمت اور اس لائن کی رقم ہوتی ہے: تعداد × قیمت۔ تمام لائنیں جمع کرنے سے کل بنتا ہے۔ اگر آپ نوٹ دیں تو بقایا = دی گئی رقم − کل۔")},
   number_question(
     "s4_sugar",
     T("Sugar costs Rs 160 a kg. What is the amount for 2 kg, in rupees?", "چینی 160 روپے فی کلو ہے۔ 2 کلو کی رقم کتنے روپے ہے؟"),
     S4,
     T("Quantity × rate: 2 × 160.", "تعداد × قیمت: 2 × 160"),
     T("Right! Rs 320.", "درست! 320 روپے"),
     T("2 × 160 = 320.", "2 × 160 = 320"),
     common_wrong=[wrong(160, "Rs 160 is for 1 kg. For 2 kg: 2 × 160 = 320.", "160 روپے 1 کلو کے ہیں۔ 2 کلو: 2 × 160 = 320", "forgets_quantity")]),
   number_question(
     "s5_total",
     T("A bill has: 2 kg sugar at Rs 160 a kg, 3 packets of biscuits at Rs 35 each, and 1 litre of milk at Rs 220. What is the total, in rupees?", "ایک بل میں ہے: 160 روپے فی کلو کے حساب سے 2 کلو چینی، 35 روپے فی پیکٹ کے حساب سے 3 پیکٹ بسکٹ، اور 220 روپے کا 1 لیٹر دودھ۔ کل کتنے روپے ہیں؟"),
     S5,
     T("Lines: 320, 3 × 35 = 105, and 220. Add them.", "لائنیں: 320، 3 × 35 = 105، اور 220۔ انہیں جمع کریں۔"),
     T("Right! Rs 645.", "درست! 645 روپے"),
     T("320 + 105 + 220 = 645.", "320 + 105 + 220 = 645"),
     common_wrong=[wrong(415, "Multiply each rate by its quantity first: 320 + 105 + 220 = 645.", "پہلے ہر قیمت کو تعداد سے ضرب دیں: 320 + 105 + 220 = 645", "forgets_quantity")]),
   {"id": "s6_change", "type": "choice",
    "prompt": T("That bill comes to Rs 645. Ammi pays with a Rs 1000 note. What is the change?", "وہ بل 645 روپے بنتا ہے۔ امی 1000 روپے کا نوٹ دیتی ہیں۔ بقایا کتنا ہے؟"),
    "options": [
      opt("355", "Rs 355", "355 روپے", True, "Yes! 1000 − 645 = 355.", "جی ہاں! 1000 − 645 = 355"),
      opt("455", "Rs 455", "455 روپے", False, "Check the subtraction: 1000 − 645 = 355.", "نفی دوبارہ دیکھیں: 1000 − 645 = 355"),
      opt("1645", "Rs 1645", "1645 روپے", False, "Change is taken away, not added: 1000 − 645 = 355.", "بقایا نفی سے نکلتا ہے، جمع سے نہیں: 1000 − 645 = 355", "change_wrong_way"),
    ]},
   number_question(
     "s7_notebooks",
     T("Ahmed buys 4 notebooks at Rs 85.50 each. He pays with a Rs 500 note. How much change does he get, in rupees?", "احمد 85.50 روپے فی کاپی کے حساب سے 4 کاپیاں خریدتا ہے۔ وہ 500 روپے کا نوٹ دیتا ہے۔ اسے کتنے روپے بقایا ملے گا؟"),
     S7,
     T("Bill: 4 × 85.50. Then 500 − bill.", "بل: 4 × 85.50۔ پھر 500 − بل"),
     T("Right! Rs 158.", "درست! 158 روپے"),
     T("4 × 85.50 = 342. 500 − 342 = 158.", "4 × 85.50 = 342۔ 500 − 342 = 158"),
     common_wrong=[wrong(342, "Rs 342 is the bill. Change: 500 − 342 = 158.", "342 روپے بل ہے۔ بقایا: 500 − 342 = 158", "total_as_change"),
                   wrong(D("414.50"), "That is for one notebook. 4 cost 342, so the change is 158.", "یہ ایک کاپی کا ہے۔ 4 کی قیمت 342 ہے، تو بقایا 158 ہے۔", "forgets_quantity")]),
   number_question(
     "s8_two_notes",
     T("A bill comes to Rs 1235. Abbu pays with one Rs 1000 note and one Rs 500 note. How much change does he get, in rupees?", "ایک بل 1235 روپے بنتا ہے۔ ابو 1000 روپے کا ایک نوٹ اور 500 روپے کا ایک نوٹ دیتے ہیں۔ انہیں کتنے روپے بقایا ملے گا؟"),
     S8,
     T("Money given: 1000 + 500 = 1500.", "دی گئی رقم: 1000 + 500 = 1500"),
     T("Right! Rs 265.", "درست! 265 روپے"),
     T("1500 − 1235 = 265.", "1500 − 1235 = 265"),
     common_wrong=[wrong(235, "He gave 1500, not 1000 + 1000. 1500 − 1235 = 265.", "انہوں نے 1500 دیے۔ 1500 − 1235 = 265")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A bill has 3 pens at Rs 25 each and 2 erasers at Rs 15 each. The shop boy writes, \"Total: 25 + 15 = Rs 40.\" What went wrong?", "ایک بل میں 25 روپے فی قلم کے حساب سے 3 قلم اور 15 روپے فی ربڑ کے حساب سے 2 ربڑ ہیں۔ دکان کا لڑکا لکھتا ہے، \"کل: 25 + 15 = 40 روپے۔\" کیا غلطی ہوئی؟"),
    "options": [
      opt("qty", "He forgot the quantities. 3 × 25 + 2 × 15 = Rs 105.", "وہ تعداد بھول گیا۔ 3 × 25 + 2 × 15 = 105 روپے", True,
          "Yes! Each line is quantity × rate.", "جی ہاں! ہر لائن تعداد × قیمت ہے۔"),
      opt("add", "He should have multiplied: 25 × 15.", "اسے ضرب دینی چاہیے تھی: 25 × 15", False,
          "Different items are added, but each rate is first multiplied by its quantity.", "مختلف چیزیں جمع ہوتی ہیں، لیکن پہلے ہر قیمت کو اس کی تعداد سے ضرب دی جاتی ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "There are 3 pens and 2 erasers, not one of each. The total is Rs 105.", "3 قلم اور 2 ربڑ ہیں، ہر ایک کا ایک نہیں۔ کل 105 روپے ہے۔", "forgets_quantity"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why can't we just add the prices on a bill? Can you teach me?",
                     "ہم بل پر قیمتیں سیدھی جمع کیوں نہیں کر سکتے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we multiply each rate by the quantity before adding the lines of a bill?", "اپنے الفاظ میں بتائیں: بل کی لائنیں جمع کرنے سے پہلے ہم ہر قیمت کو تعداد سے ضرب کیوں دیتے ہیں؟"),
    "key_idea": "The rate is the price of one item. If you buy 3 pens, you pay for 3 pens, so the line amount is 3 × the rate. Only then do we add the lines together for the total.",
    "levels": {
      "got_it": "Says the rate is the price of only one item, so for many items you multiply by how many, then add the lines.",
      "partly": "Says you multiply, without saying the rate is for one item.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["one", "each", "ایک", "فی"],
      ["how many", "quantity", "تعداد", "کتنے"],
      ["multiply", "times", "ضرب", "گنا"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The rate is for one, so we multiply by how many.", "بہت خوب! قیمت ایک کی ہے، اس لیے تعداد سے ضرب دیتے ہیں۔"),
      "partly": T("Good start! Now say what the rate is the price of.", "اچھی شروعات! اب بتائیں قیمت فی عدد کس چیز کی قیمت ہے۔"),
      "not_yet": T("One pen costs Rs 25. You buy 3 pens. Do you pay Rs 25 or more?", "ایک قلم 25 روپے کا ہے۔ آپ 3 قلم خریدتے ہیں۔ آپ 25 روپے دیں گے یا زیادہ؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_vegetables",
     T("At the sabzi stall, Saima buys 1.5 kg of tomatoes at Rs 120 a kg and 0.5 kg of ginger at Rs 600 a kg. She pays with a Rs 500 note. How much change does she get, in rupees?", "سبزی کی ریڑھی پر صائمہ 120 روپے فی کلو کے حساب سے 1.5 کلو ٹماٹر اور 600 روپے فی کلو کے حساب سے 0.5 کلو ادرک خریدتی ہے۔ وہ 500 روپے کا نوٹ دیتی ہے۔ اسے کتنے روپے بقایا ملے گا؟"),
     S11,
     T("1.5 × 120 = 180 and 0.5 × 600 = 300.", "1.5 × 120 = 180 اور 0.5 × 600 = 300"),
     T("Right! Rs 20.", "درست! 20 روپے"),
     T("Bill = 180 + 300 = 480. Change = 500 − 480 = 20.", "بل = 180 + 300 = 480۔ بقایا = 500 − 480 = 20"),
     common_wrong=[wrong(480, "Rs 480 is the bill. Change: 500 − 480 = 20.", "480 روپے بل ہے۔ بقایا: 500 − 480 = 20", "total_as_change")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can check any shop bill yourself!", "اب آپ دکان کا کوئی بھی بل خود جانچ سکتے ہیں!"),
    "text": T("Each line of a bill is quantity × rate. Add the lines to get the total. Change = money given − total. Always check the bill before you pay.",
              "بل کی ہر لائن تعداد × قیمت ہے۔ لائنیں جمع کرنے سے کل بنتا ہے۔ بقایا = دی گئی رقم − کل۔ پیسے دینے سے پہلے ہمیشہ بل جانچیں۔"),
    "points": [T("Line = quantity × rate.", "لائن = تعداد × قیمت۔"),
               T("Change = money given − total.", "بقایا = دی گئی رقم − کل۔")]},
 ],
 "review_questions": [
   {"id": "r_line", "type": "apply", "skill": SKILL, "step": number_question(
     "r_line",
     T("Flour costs Rs 140 a kg. What is the amount for 3 kg, in rupees?", "آٹا 140 روپے فی کلو ہے۔ 3 کلو کی رقم کتنے روپے ہے؟"),
     R1,
     T("3 × 140.", "3 × 140"),
     T("Right! Rs 420.", "درست! 420 روپے"),
     T("3 × 140 = 420.", "3 × 140 = 420"),
     common_wrong=[wrong(140, "Rs 140 is for 1 kg. 3 × 140 = 420.", "140 روپے 1 کلو کے ہیں۔ 3 × 140 = 420", "forgets_quantity")],
     qtype=None)},
   {"id": "r_change", "type": "apply", "skill": SKILL, "step": number_question(
     "r_change",
     T("A bill comes to Rs 785. You pay with a Rs 1000 note. How much change do you get, in rupees?", "ایک بل 785 روپے بنتا ہے۔ آپ 1000 روپے کا نوٹ دیتے ہیں۔ آپ کو کتنے روپے بقایا ملے گا؟"),
     R2,
     T("1000 − 785.", "1000 − 785"),
     T("Right! Rs 215.", "درست! 215 روپے"),
     T("1000 − 785 = 215.", "1000 − 785 = 215"),
     common_wrong=[wrong(225, "Check the subtraction: 1000 − 785 = 215.", "نفی دوبارہ دیکھیں: 1000 − 785 = 215")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Profit and Loss unit. No textbook text or exercises were used.",
   "Prices are round and close to everyday Pakistani shop prices; they are for practice, not exact current prices.",
   "Urdu terms to check: بل (bill), قیمت فی عدد (rate), بقایا (change).",
   "The numbers were worked out in content/sources/g6-maths-12/bills_and_change.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

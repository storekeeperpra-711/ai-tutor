from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, PC_OF_AMOUNT, PL_PERCENT, PL_SELLING_PRICE, percent_of)

SKILL = PL_SELLING_PRICE

# s2: 10% of 350
S2 = percent_of(10, 350)
assert S2 == 35
# s4: CP 400, 10% profit -> SP 440
S4 = 400 + percent_of(10, 400)
assert S4 == 440
# s5: CP 600, 20% loss -> SP 480
S5 = 600 - percent_of(20, 600)
assert S5 == 480
# s6: CP 200, 25% profit -> SP 250
assert 200 + percent_of(25, 200) == 250
# s7: CP 1500, 12% profit -> SP 1680
S7 = 1500 + percent_of(12, 1500)
assert S7 == 1680
# s8: CP 80, 5% loss -> SP 76
S8 = 80 - percent_of(5, 80)
assert S8 == 76
# s9: CP 500, 10% profit is SP 550, not 510
assert 500 + percent_of(10, 500) == 550
# s11: crate of eggs CP 600, 15% profit -> SP 690
S11 = 600 + percent_of(15, 600)
assert S11 == 690
# question bank and review
QB = 200 + percent_of(30, 200)
assert QB == 260
R1 = 900 - percent_of(10, 900)
assert R1 == 810
R2 = 120 + percent_of(50, 120)
assert R2 == 180

lesson = {
 "id": "g6-maths-12-selling-price",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the selling price when the cost price and the profit or loss percent are given.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Finding the selling price", "قیمتِ فروخت معلوم کرنا"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": PL_PERCENT}, {"skill": PC_OF_AMOUNT}],
 "misconceptions": [
   {"id": "adds_percent_as_rupees", "description": "Adds the percent as rupees (10% profit on Rs 500 gives Rs 510)."},
   {"id": "stops_at_profit", "description": "Finds the profit or loss in rupees and gives that as the selling price."},
   {"id": "wrong_direction", "description": "Adds a loss or takes away a profit."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("An item is sold at a loss. How do you find the selling price?", "ایک چیز نقصان پر بیچی جاتی ہے۔ قیمتِ فروخت کیسے نکالتے ہیں؟"),
     "options": [
       opt("minus", "Cost price − the loss", "قیمتِ خرید − نقصان", True,
           "Yes! With a loss, you get back less than the cost price.", "جی ہاں! نقصان میں قیمتِ خرید سے کم واپس ملتا ہے۔"),
       opt("plus", "Cost price + the loss", "قیمتِ خرید + نقصان", False,
           "Adding would make it a profit. A loss is taken away.", "جمع کرنے سے نفع بن جائے گا۔ نقصان نفی کیا جاتا ہے۔", "wrong_direction"),
       opt("loss", "The selling price is the loss", "قیمتِ فروخت نقصان کے برابر ہے", False,
           "The loss is only the part lost. Take it away from the cost price.", "نقصان صرف گیا ہوا حصہ ہے۔ اسے قیمتِ خرید سے نفی کریں۔", "stops_at_profit"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A chair costs Rs 200. It is sold at a 30% profit. What is the selling price, in rupees?", "ایک کرسی 200 روپے کی ہے۔ اسے 30% نفع پر بیچا جاتا ہے۔ قیمتِ فروخت کتنے روپے ہے؟"),
     QB,
     T("30% of 200 = 60. Then 200 + 60.", "200 کا 30% = 60۔ پھر 200 + 60"),
     T("Right! Rs 260.", "درست! 260 روپے"),
     T("Profit = 60. SP = 200 + 60 = 260.", "نفع = 60۔ قیمتِ فروخت = 200 + 60 = 260"),
     common_wrong=[wrong(60, "Rs 60 is the profit. Add it: 200 + 60 = 260.", "60 روپے نفع ہے۔ اسے جمع کریں: 200 + 60 = 260", "stops_at_profit"),
                   wrong(230, "30% is not Rs 30. 30% of 200 = 60, so 260.", "30%، 30 روپے نہیں ہے۔ 200 کا 30% = 60، تو 260", "adds_percent_as_rupees")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A kettle costs Rs 500 and is sold at a 10% profit. Faisal says the selling price is Rs 510. What is wrong?", "ایک کیتلی 500 روپے کی ہے اور 10% نفع پر بیچی جاتی ہے۔ فیصل کہتا ہے قیمتِ فروخت 510 روپے ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("percent", "10% of 500 is Rs 50, not Rs 10. The selling price is Rs 550.", "500 کا 10%، 50 روپے ہے، 10 نہیں۔ قیمتِ فروخت 550 روپے ہے۔", True,
           "Yes! Work out the percent of the cost price first.", "جی ہاں! پہلے قیمتِ خرید کی فیصد نکالیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "10% means 10 out of every 100. On Rs 500 that is Rs 50.", "10% یعنی ہر 100 میں سے 10۔ 500 روپے پر یہ 50 روپے ہے۔", "adds_percent_as_rupees"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_sp_profit", "front": T("Selling price with a profit?", "نفع کے ساتھ قیمتِ فروخت؟"),
    "back": T("Cost price + (profit % of cost price)", "قیمتِ خرید + (قیمتِ خرید کا نفع %)")},
   {"id": "f_sp_loss", "front": T("Selling price with a loss?", "نقصان کے ساتھ قیمتِ فروخت؟"),
    "back": T("Cost price − (loss % of cost price)", "قیمتِ خرید − (قیمتِ خرید کا نقصان %)")},
 ],
 "home_tasks": [{"id": "h_price_tag", "text": T(
   "Pretend you run a small shop. Pick three things from home and guess what they cost. If you want a 20% profit on each, what price would you sell them for?",
   "فرض کریں آپ کی ایک چھوٹی سی دکان ہے۔ گھر سے تین چیزیں چنیں اور اندازہ لگائیں کہ ان کی قیمتِ خرید کیا ہے۔ اگر آپ ہر ایک پر 20% نفع چاہیں تو آپ انہیں کتنے میں بیچیں گے؟")}],
 "glossary": [T("Selling price", "قیمتِ فروخت"), T("Profit percent", "نفع کی فیصد"), T("Loss percent", "نقصان کی فیصد")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A shopkeeper buys a fan for Rs 400 and wants a 10% profit. What price tag should he put on it?",
                     "ایک دکاندار 400 روپے کا پنکھا خریدتا ہے اور 10% نفع چاہتا ہے۔ وہ اس پر کون سی قیمت لکھے؟"),
    "text": T("Today we use a percent to find the selling price. First, a quick percent check.", "آج ہم فیصد سے قیمتِ فروخت نکالیں گے۔ پہلے فیصد کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("What is 10% of Rs 350, in rupees?", "350 روپے کا 10% کتنے روپے ہے؟"),
     S2,
     T("10% means divide by 10.", "10% یعنی 10 سے تقسیم کریں۔"),
     T("Right! Rs 35.", "درست! 35 روپے"),
     T("350 ÷ 10 = 35.", "350 ÷ 10 = 35"),
     common_wrong=[wrong(10, "Not Rs 10. 10% of 350 = 350 ÷ 10 = 35.", "10 روپے نہیں۔ 350 کا 10% = 350 ÷ 10 = 35")],
     qtype="recall", skill=PC_OF_AMOUNT),
   {"id": "s3_two_steps", "type": "explain",
    "character": say("happy", "Two steps: find the percent of the cost price, then add or take away.", "دو قدم: قیمتِ خرید کی فیصد نکالیں، پھر جمع یا نفی کریں۔"),
    "text": T("Step 1: find the profit or loss in rupees: percent × cost price ÷ 100. Step 2: for a profit, selling price = cost price + profit. For a loss, selling price = cost price − loss. Example: Rs 400 with 10% profit: 10% of 400 = 40, so SP = 440.",
              "قدم 1: روپوں میں نفع یا نقصان نکالیں: فیصد × قیمتِ خرید ÷ 100۔ قدم 2: نفع ہو تو قیمتِ فروخت = قیمتِ خرید + نفع۔ نقصان ہو تو قیمتِ فروخت = قیمتِ خرید − نقصان۔ مثال: 400 روپے پر 10% نفع: 400 کا 10% = 40، تو قیمتِ فروخت = 440")},
   number_question(
     "s4_fan",
     T("A fan costs Rs 400. It is sold at a 10% profit. What is the selling price, in rupees?", "ایک پنکھا 400 روپے کا ہے۔ اسے 10% نفع پر بیچا جاتا ہے۔ قیمتِ فروخت کتنے روپے ہے؟"),
     S4,
     T("10% of 400 = 40. Then 400 + 40.", "400 کا 10% = 40۔ پھر 400 + 40"),
     T("Right! Rs 440.", "درست! 440 روپے"),
     T("Profit = 40. SP = 400 + 40 = 440.", "نفع = 40۔ قیمتِ فروخت = 400 + 40 = 440"),
     common_wrong=[wrong(40, "Rs 40 is the profit. Add it: 400 + 40 = 440.", "40 روپے نفع ہے۔ اسے جمع کریں: 400 + 40 = 440", "stops_at_profit"),
                   wrong(410, "10% is not Rs 10. 10% of 400 = 40, so 440.", "10%، 10 روپے نہیں ہے۔ 400 کا 10% = 40، تو 440", "adds_percent_as_rupees"),
                   wrong(360, "It's a profit, so add: 400 + 40 = 440.", "یہ نفع ہے، تو جمع کریں: 400 + 40 = 440", "wrong_direction")]),
   number_question(
     "s5_phone",
     T("An old phone costs Rs 600. It is sold at a 20% loss. What is the selling price, in rupees?", "ایک پرانا فون 600 روپے کا ہے۔ اسے 20% نقصان پر بیچا جاتا ہے۔ قیمتِ فروخت کتنے روپے ہے؟"),
     S5,
     T("20% of 600 = 120. Then 600 − 120.", "600 کا 20% = 120۔ پھر 600 − 120"),
     T("Right! Rs 480.", "درست! 480 روپے"),
     T("Loss = 120. SP = 600 − 120 = 480.", "نقصان = 120۔ قیمتِ فروخت = 600 − 120 = 480"),
     common_wrong=[wrong(720, "It's a loss, so take away: 600 − 120 = 480.", "یہ نقصان ہے، تو نفی کریں: 600 − 120 = 480", "wrong_direction"),
                   wrong(120, "Rs 120 is the loss. 600 − 120 = 480.", "120 روپے نقصان ہے۔ 600 − 120 = 480", "stops_at_profit")]),
   {"id": "s6_choose", "type": "choice",
    "prompt": T("A pair of shoes costs Rs 200 and is sold at a 25% profit. What is the selling price?", "جوتوں کا ایک جوڑا 200 روپے کا ہے اور 25% نفع پر بیچا جاتا ہے۔ قیمتِ فروخت کیا ہے؟"),
    "options": [
      opt("250", "Rs 250", "250 روپے", True, "Yes! 25% of 200 = 50, and 200 + 50 = 250.", "جی ہاں! 200 کا 25% = 50، اور 200 + 50 = 250"),
      opt("225", "Rs 225", "225 روپے", False, "25% is not Rs 25. 25% of 200 = 50.", "25%، 25 روپے نہیں ہے۔ 200 کا 25% = 50", "adds_percent_as_rupees"),
      opt("150", "Rs 150", "150 روپے", False, "It's a profit, so add 50: 250.", "یہ نفع ہے، تو 50 جمع کریں: 250", "wrong_direction"),
    ]},
   number_question(
     "s7_cycle",
     T("A sewing machine costs Rs 1500. It is sold at a 12% profit. What is the selling price, in rupees?", "ایک سلائی مشین 1500 روپے کی ہے۔ اسے 12% نفع پر بیچا جاتا ہے۔ قیمتِ فروخت کتنے روپے ہے؟"),
     S7,
     T("12% of 1500 = 12 × 1500 ÷ 100.", "1500 کا 12% = 12 × 1500 ÷ 100"),
     T("Right! Rs 1680.", "درست! 1680 روپے"),
     T("12 × 15 = 180. SP = 1500 + 180 = 1680.", "12 × 15 = 180۔ قیمتِ فروخت = 1500 + 180 = 1680"),
     common_wrong=[wrong(180, "Rs 180 is the profit. 1500 + 180 = 1680.", "180 روپے نفع ہے۔ 1500 + 180 = 1680", "stops_at_profit"),
                   wrong(1512, "12% is not Rs 12. 12% of 1500 = 180, so 1680.", "12%، 12 روپے نہیں ہے۔ 1500 کا 12% = 180، تو 1680", "adds_percent_as_rupees")]),
   number_question(
     "s8_pencil_box",
     T("A pencil box costs Rs 80. It is sold at a 5% loss. What is the selling price, in rupees?", "ایک پنسل باکس 80 روپے کا ہے۔ اسے 5% نقصان پر بیچا جاتا ہے۔ قیمتِ فروخت کتنے روپے ہے؟"),
     S8,
     T("5% of 80 = 4. Then 80 − 4.", "80 کا 5% = 4۔ پھر 80 − 4"),
     T("Right! Rs 76.", "درست! 76 روپے"),
     T("Loss = 4. SP = 80 − 4 = 76.", "نقصان = 4۔ قیمتِ فروخت = 80 − 4 = 76"),
     common_wrong=[wrong(75, "5% is not Rs 5. 5% of 80 = 4, so 76.", "5%، 5 روپے نہیں ہے۔ 80 کا 5% = 4، تو 76", "adds_percent_as_rupees"),
                   wrong(84, "It's a loss, so take away: 80 − 4 = 76.", "یہ نقصان ہے، تو نفی کریں: 80 − 4 = 76", "wrong_direction")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A kettle costs Rs 500 and is sold at a 10% profit. Asma says, \"500 + 10 = Rs 510.\" What went wrong?", "ایک کیتلی 500 روپے کی ہے اور 10% نفع پر بیچی جاتی ہے۔ عاصمہ کہتی ہے، \"500 + 10 = 510 روپے۔\" کیا غلطی ہوئی؟"),
    "options": [
      opt("percent", "She added 10 rupees, not 10%. 10% of 500 = 50, so Rs 550.", "اس نے 10 روپے جمع کیے، 10% نہیں۔ 500 کا 10% = 50، تو 550 روپے۔", True,
          "Yes! Find the percent of the cost price first.", "جی ہاں! پہلے قیمتِ خرید کی فیصد نکالیں۔"),
      opt("subtract", "She should take away: 500 − 10 = 490.", "اسے نفی کرنا چاہیے: 500 − 10 = 490", False,
          "It's a profit, so adding is right. The mistake is adding Rs 10 instead of 10%.", "یہ نفع ہے، تو جمع درست ہے۔ غلطی 10% کی جگہ 10 روپے جمع کرنا ہے۔", "wrong_direction"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "10% of Rs 500 is Rs 50, not Rs 10.", "500 روپے کا 10%، 50 روپے ہے، 10 نہیں۔", "adds_percent_as_rupees"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is a 10% profit on Rs 500 not Rs 510? Can you teach me?",
                     "500 روپے پر 10% نفع 510 روپے کیوں نہیں ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we find 10% of the cost price before adding it?", "اپنے الفاظ میں بتائیں: جمع کرنے سے پہلے ہم قیمتِ خرید کا 10% کیوں نکالتے ہیں؟"),
    "key_idea": "A percent is a part of an amount, not a number of rupees. 10% means 10 out of every 100, so on Rs 500 it is 5 lots of 10 = Rs 50. That profit in rupees is what we add to the cost price.",
    "levels": {
      "got_it": "Says 10% means 10 out of every 100, so on Rs 500 the profit is Rs 50, and that is what gets added.",
      "partly": "Says you must find the percent first, without saying why 10% is not 10 rupees.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["100", "every", "hundred", "سو"],
      ["50", "fifty", "پچاس"],
      ["part", "of", "حصہ", "کا"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 10% of Rs 500 is Rs 50, so the selling price is Rs 550.", "بہت خوب! 500 روپے کا 10%، 50 روپے ہے، تو قیمتِ فروخت 550 روپے ہے۔"),
      "partly": T("Good start! Now say how much 10% of Rs 500 is in rupees.", "اچھی شروعات! اب بتائیں 500 روپے کا 10% کتنے روپے ہے۔"),
      "not_yet": T("10% means 10 out of every 100. How many 100s are there in 500?", "10% یعنی ہر 100 میں سے 10۔ 500 میں کتنے 100 ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_eggs",
     T("A shopkeeper buys a crate of eggs for Rs 600. He wants a 15% profit on the crate. For how many rupees should he sell the whole crate?", "ایک دکاندار انڈوں کی پیٹی 600 روپے میں خریدتا ہے۔ وہ پیٹی پر 15% نفع چاہتا ہے۔ اسے پوری پیٹی کتنے روپے میں بیچنی چاہیے؟"),
     S11,
     T("15% of 600 = 15 × 6.", "600 کا 15% = 15 × 6"),
     T("Right! Rs 690.", "درست! 690 روپے"),
     T("Profit = 90. SP = 600 + 90 = 690.", "نفع = 90۔ قیمتِ فروخت = 600 + 90 = 690"),
     common_wrong=[wrong(90, "Rs 90 is the profit. 600 + 90 = 690.", "90 روپے نفع ہے۔ 600 + 90 = 690", "stops_at_profit"),
                   wrong(615, "15% is not Rs 15. 15% of 600 = 90, so 690.", "15%، 15 روپے نہیں ہے۔ 600 کا 15% = 90، تو 690", "adds_percent_as_rupees")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can put a fair price tag on anything!", "اب آپ کسی بھی چیز پر مناسب قیمت لکھ سکتے ہیں!"),
    "text": T("First find the profit or loss in rupees: percent × cost price ÷ 100. Then for a profit add it to the cost price; for a loss take it away. A percent is never just that many rupees.",
              "پہلے روپوں میں نفع یا نقصان نکالیں: فیصد × قیمتِ خرید ÷ 100۔ پھر نفع ہو تو قیمتِ خرید میں جمع کریں؛ نقصان ہو تو نفی کریں۔ فیصد کبھی بھی اتنے ہی روپے نہیں ہوتی۔"),
    "points": [T("Profit: SP = CP + profit.", "نفع: قیمتِ فروخت = قیمتِ خرید + نفع۔"),
               T("Loss: SP = CP − loss.", "نقصان: قیمتِ فروخت = قیمتِ خرید − نقصان۔")]},
 ],
 "review_questions": [
   {"id": "r_loss", "type": "apply", "skill": SKILL, "step": number_question(
     "r_loss",
     T("A cupboard costs Rs 900. It is sold at a 10% loss. What is the selling price, in rupees?", "ایک الماری 900 روپے کی ہے۔ اسے 10% نقصان پر بیچا جاتا ہے۔ قیمتِ فروخت کتنے روپے ہے؟"),
     R1,
     T("10% of 900 = 90. Then 900 − 90.", "900 کا 10% = 90۔ پھر 900 − 90"),
     T("Right! Rs 810.", "درست! 810 روپے"),
     T("900 − 90 = 810.", "900 − 90 = 810"),
     common_wrong=[wrong(990, "It's a loss, so take away: 900 − 90 = 810.", "یہ نقصان ہے، تو نفی کریں: 900 − 90 = 810", "wrong_direction")],
     qtype=None)},
   {"id": "r_profit", "type": "apply", "skill": SKILL, "step": number_question(
     "r_profit",
     T("A cricket ball costs Rs 120. It is sold at a 50% profit. What is the selling price, in rupees?", "ایک کرکٹ گیند 120 روپے کی ہے۔ اسے 50% نفع پر بیچا جاتا ہے۔ قیمتِ فروخت کتنے روپے ہے؟"),
     R2,
     T("50% is half: 60. Then 120 + 60.", "50% یعنی آدھا: 60۔ پھر 120 + 60"),
     T("Right! Rs 180.", "درست! 180 روپے"),
     T("120 + 60 = 180.", "120 + 60 = 180"),
     common_wrong=[wrong(170, "50% is not Rs 50. Half of 120 = 60, so 180.", "50%، 50 روپے نہیں ہے۔ 120 کا آدھا = 60، تو 180", "adds_percent_as_rupees")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Profit and Loss unit. No textbook text or exercises were used.",
   "The main error targeted is adding the percent as rupees (10% on Rs 500 gives Rs 510).",
   "The numbers were worked out in content/sources/g6-maths-12/selling_price.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

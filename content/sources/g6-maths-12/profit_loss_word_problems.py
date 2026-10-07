from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, PL_MEANING, PL_PERCENT, PL_SELLING_PRICE, PL_BILLS, PL_WORD_PROBLEMS,
                    percent_of, as_percent)

SKILL = PL_WORD_PROBLEMS

# s2: CP 350, SP 420
S2 = 420 - 350
assert S2 == 70
# s4: 12 notebooks at Rs 50, each sold at Rs 60
S4_CP = 12 * 50
S4 = 12 * 60 - S4_CP
assert S4_CP == 600 and S4 == 120
# s5: profit percent on that
S5 = as_percent(S4, S4_CP)
assert S5 == 20
# s6: 2 dozen bananas at Rs 100 a dozen, sold at Rs 10 each
assert 2 * 12 * 10 - 2 * 100 == 40
# s7: fridge bought for 8000, Rs 1000 on repair, sold for 10800
S7_CP = 8000 + 1000
S7 = 10800 - S7_CP
assert S7 == 1800
# s8: profit percent on the full cost
S8 = as_percent(S7, S7_CP)
assert S8 == 20
# s9: bicycle 3000 + repair 500, sold 4000: profit 500, not 1000
assert 4000 - (3000 + 500) == 500 and 4000 - 3000 == 1000
# unit test
U1 = 750 - 600
assert U1 == 150
U2 = as_percent(360 - 300, 300)
assert U2 == 20
U3 = 800 - percent_of(15, 800)
assert U3 == 680
U4 = 1000 - 3 * 220
assert U4 == 340
U5 = 20 * 15 - 20 * 12
assert U5 == 60
# question bank and review
QB = 10 * 75 - 10 * 60
assert QB == 150
R1 = 2400 - 5 * 400
assert R1 == 400
R2 = as_percent(R1, 5 * 400)
assert R2 == 20

lesson = {
 "id": "g6-maths-12-profit-loss-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems on profit and loss, including buying in bulk and extra costs such as repairs.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Profit and loss word problems", "نفع اور نقصان کے عملی سوال"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": PL_SELLING_PRICE}, {"skill": PL_PERCENT}, {"skill": PL_BILLS}, {"skill": PL_MEANING}],
 "misconceptions": [
   {"id": "forgets_extra_cost", "description": "Leaves out extra costs like repairs or transport from the cost price."},
   {"id": "one_item_only", "description": "Works with the price of one item when many were bought and sold."},
   {"id": "rupees_as_percent", "description": "Gives the profit in rupees when the question asks for the percent."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("A trader buys a cart for Rs 5000 and pays Rs 500 to bring it home. What is the cost price?", "ایک تاجر 5000 روپے میں ریڑھی خریدتا ہے اور اسے گھر لانے کے 500 روپے دیتا ہے۔ قیمتِ خرید کیا ہے؟"),
     "options": [
       opt("5500", "Rs 5500", "5500 روپے", True,
           "Yes! Every rupee spent to get it ready to sell is part of the cost price.", "جی ہاں! بیچنے کے لیے تیار کرنے پر خرچ ہر روپیہ قیمتِ خرید کا حصہ ہے۔"),
       opt("5000", "Rs 5000", "5000 روپے", False,
           "The Rs 500 was spent too, so the cost price is Rs 5500.", "500 روپے بھی خرچ ہوئے، تو قیمتِ خرید 5500 روپے ہے۔", "forgets_extra_cost"),
       opt("4500", "Rs 4500", "4500 روپے", False,
           "Extra costs are added, not taken away: Rs 5500.", "اضافی خرچ جمع ہوتا ہے، نفی نہیں: 5500 روپے"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A vendor buys 10 kg of potatoes at Rs 60 a kg and sells them at Rs 75 a kg. What is the profit, in rupees?", "ایک ریڑھی والا 60 روپے فی کلو کے حساب سے 10 کلو آلو خریدتا ہے اور 75 روپے فی کلو بیچتا ہے۔ نفع کتنے روپے ہے؟"),
     QB,
     T("CP = 10 × 60, SP = 10 × 75.", "قیمتِ خرید = 10 × 60، قیمتِ فروخت = 10 × 75"),
     T("Right! Rs 150.", "درست! 150 روپے"),
     T("750 − 600 = 150.", "750 − 600 = 150"),
     common_wrong=[wrong(15, "Rs 15 is the profit on 1 kg. On 10 kg: 150.", "15 روپے 1 کلو پر نفع ہے۔ 10 کلو پر: 150", "one_item_only")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Kashif buys a motorbike for Rs 40000, spends Rs 5000 on repairs and sells it for Rs 50000. He says his profit is Rs 10000. What is wrong?", "کاشف 40000 روپے میں موٹر سائیکل خریدتا ہے، 5000 روپے مرمت پر لگاتا ہے اور 50000 روپے میں بیچتا ہے۔ وہ کہتا ہے اس کا نفع 10000 روپے ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("repair", "He forgot the repairs. Cost price = 45000, so profit = Rs 5000.", "وہ مرمت بھول گیا۔ قیمتِ خرید = 45000، تو نفع = 5000 روپے", True,
           "Yes! The repair money is part of the cost price.", "جی ہاں! مرمت کے پیسے قیمتِ خرید کا حصہ ہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "He spent Rs 45000 in all, so the profit is only Rs 5000.", "اس نے کل 45000 روپے خرچ کیے، تو نفع صرف 5000 روپے ہے۔", "forgets_extra_cost"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_extra", "front": T("Repairs or transport?", "مرمت یا کرایہ؟"),
    "back": T("Add them to the cost price.", "انہیں قیمتِ خرید میں جمع کریں۔")},
   {"id": "f_bulk", "front": T("Many items bought and sold?", "بہت سی چیزیں خریدیں اور بیچیں؟"),
    "back": T("Find the total CP and total SP first.", "پہلے کل قیمتِ خرید اور کل قیمتِ فروخت نکالیں۔")},
 ],
 "home_tasks": [{"id": "h_stall", "text": T(
   "Plan a small stall for a school fair. Choose one thing to sell, like lemonade glasses. Guess what you would spend on everything you need, choose a selling price, and work out your profit and profit percent if you sell 30.",
   "سکول میلے کے لیے ایک چھوٹے سٹال کا منصوبہ بنائیں۔ بیچنے کے لیے ایک چیز چنیں، جیسے شکنجبین کے گلاس۔ اندازہ لگائیں کہ ضرورت کی ہر چیز پر کتنا خرچ ہوگا، قیمتِ فروخت چنیں، اور 30 بیچنے پر نفع اور نفع کی فیصد نکالیں۔")}],
 "glossary": [T("Repair", "مرمت"), T("Total cost price", "کل قیمتِ خرید"), T("Total selling price", "کل قیمتِ فروخت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Uncle Rashid fixes old fridges and sells them. How does he know if his work pays?",
                     "رشید چچا پرانے فریج ٹھیک کر کے بیچتے ہیں۔ انہیں کیسے پتا چلے کہ ان کا کام فائدہ مند ہے؟"),
    "text": T("Today we solve real profit and loss problems. First, a quick check.", "آج ہم نفع اور نقصان کے اصل زندگی کے سوال حل کریں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Bought for Rs 350, sold for Rs 420. What is the profit, in rupees?", "350 روپے میں خریدا، 420 روپے میں بیچا۔ نفع کتنے روپے ہے؟"),
     S2,
     T("SP − CP.", "قیمتِ فروخت − قیمتِ خرید"),
     T("Right! Rs 70.", "درست! 70 روپے"),
     T("420 − 350 = 70.", "420 − 350 = 70"),
     common_wrong=[wrong(420, "Rs 420 is the selling price. Profit: 420 − 350 = 70.", "420 روپے قیمتِ فروخت ہے۔ نفع: 420 − 350 = 70")],
     qtype="recall", skill=PL_MEANING),
   {"id": "s3_steps", "type": "explain",
    "character": say("thinking", "Count every rupee spent, and every rupee earned. Then compare.", "خرچ ہونے والا ہر روپیہ اور کمایا ہوا ہر روپیہ گنیں۔ پھر موازنہ کریں۔"),
    "text": T("1) Find the total cost price: everything paid, including repairs or transport. 2) Find the total selling price: everything received. 3) Profit or loss = the difference. 4) For a percent, divide by the total cost price and × 100.",
              "1) کل قیمتِ خرید نکالیں: سب کچھ جو ادا کیا، مرمت یا کرایہ سمیت۔ 2) کل قیمتِ فروخت نکالیں: سب کچھ جو ملا۔ 3) نفع یا نقصان = فرق۔ 4) فیصد کے لیے کل قیمتِ خرید سے تقسیم کریں اور × 100 کریں۔")},
   number_question(
     "s4_notebooks",
     T("A shopkeeper buys 12 notebooks at Rs 50 each and sells each one for Rs 60. What is the total profit, in rupees?", "ایک دکاندار 50 روپے فی کاپی کے حساب سے 12 کاپیاں خریدتا ہے اور ہر ایک 60 روپے میں بیچتا ہے۔ کل نفع کتنے روپے ہے؟"),
     S4,
     T("CP = 12 × 50, SP = 12 × 60.", "قیمتِ خرید = 12 × 50، قیمتِ فروخت = 12 × 60"),
     T("Right! Rs 120.", "درست! 120 روپے"),
     T("720 − 600 = 120.", "720 − 600 = 120"),
     common_wrong=[wrong(10, "Rs 10 is the profit on one notebook. On 12: 120.", "10 روپے ایک کاپی پر نفع ہے۔ 12 پر: 120", "one_item_only")]),
   number_question(
     "s5_percent",
     T("He spent Rs 600 on the 12 notebooks and made Rs 120 profit. What is his profit percent? Type just the number.", "اس نے 12 کاپیوں پر 600 روپے خرچ کیے اور 120 روپے نفع کمایا۔ نفع کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S5,
     T("120 ÷ 600 × 100.", "120 ÷ 600 × 100"),
     T("Right! 20%.", "درست! 20%"),
     T("120 ÷ 600 × 100 = 20.", "120 ÷ 600 × 100 = 20"),
     common_wrong=[wrong(120, "Rs 120 is the profit in rupees. 120 ÷ 600 × 100 = 20%.", "120 روپے نفع ہے۔ 120 ÷ 600 × 100 = 20%", "rupees_as_percent")]),
   {"id": "s6_bananas", "type": "choice",
    "prompt": T("Nadia buys 2 dozen bananas at Rs 100 a dozen and sells them at Rs 10 each. What happens?", "نادیہ 100 روپے فی درجن کے حساب سے 2 درجن کیلے خریدتی ہے اور 10 روپے فی کیلا بیچتی ہے۔ کیا ہوتا ہے؟"),
    "options": [
      opt("profit", "A profit of Rs 40", "40 روپے نفع", True, "Yes! CP = 200, SP = 24 × 10 = 240.", "جی ہاں! قیمتِ خرید = 200، قیمتِ فروخت = 24 × 10 = 240"),
      opt("loss", "A loss of Rs 40", "40 روپے نقصان", False, "SP = 240 is more than CP = 200, so it is a profit.", "قیمتِ فروخت 240، قیمتِ خرید 200 سے زیادہ ہے، تو یہ نفع ہے۔"),
      opt("neither", "No profit and no loss", "نہ نفع نہ نقصان", False, "2 dozen is 24 bananas: 24 × 10 = 240, more than 200.", "2 درجن یعنی 24 کیلے: 24 × 10 = 240، جو 200 سے زیادہ ہے۔", "one_item_only"),
    ]},
   number_question(
     "s7_fridge",
     T("Rashid buys an old fridge for Rs 8000, spends Rs 1000 on repairs, and sells it for Rs 10800. What is his profit, in rupees?", "رشید 8000 روپے میں پرانا فریج خریدتا ہے، 1000 روپے مرمت پر لگاتا ہے، اور اسے 10800 روپے میں بیچتا ہے۔ اس کا نفع کتنے روپے ہے؟"),
     S7,
     T("Cost price = 8000 + 1000.", "قیمتِ خرید = 8000 + 1000"),
     T("Right! Rs 1800.", "درست! 1800 روپے"),
     T("CP = 9000. 10800 − 9000 = 1800.", "قیمتِ خرید = 9000۔ 10800 − 9000 = 1800"),
     common_wrong=[wrong(2800, "Add the repairs to the cost: 9000. Profit: 10800 − 9000 = 1800.", "مرمت قیمت میں جمع کریں: 9000۔ نفع: 10800 − 9000 = 1800", "forgets_extra_cost")]),
   number_question(
     "s8_fridge_percent",
     T("Rashid's fridge cost him Rs 9000 in all and he made Rs 1800 profit. What is his profit percent? Type just the number.", "رشید کو فریج کل 9000 روپے کا پڑا اور اس نے 1800 روپے نفع کمایا۔ نفع کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S8,
     T("1800 ÷ 9000 × 100.", "1800 ÷ 9000 × 100"),
     T("Right! 20%.", "درست! 20%"),
     T("1800 ÷ 9000 × 100 = 20.", "1800 ÷ 9000 × 100 = 20"),
     common_wrong=[wrong(1800, "Rs 1800 is the profit in rupees. 1800 ÷ 9000 × 100 = 20%.", "1800 روپے نفع ہے۔ 1800 ÷ 9000 × 100 = 20%", "rupees_as_percent")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Imran buys a bicycle for Rs 3000, spends Rs 500 on new tyres, and sells it for Rs 4000. He says, \"4000 − 3000 = Rs 1000 profit.\" What went wrong?", "عمران 3000 روپے میں سائیکل خریدتا ہے، 500 روپے نئے ٹائروں پر لگاتا ہے، اور اسے 4000 روپے میں بیچتا ہے۔ وہ کہتا ہے، \"4000 − 3000 = 1000 روپے نفع۔\" کیا غلطی ہوئی؟"),
    "options": [
      opt("tyres", "He forgot the tyres. CP = 3500, so the profit is Rs 500.", "وہ ٹائر بھول گیا۔ قیمتِ خرید = 3500، تو نفع 500 روپے ہے۔", True,
          "Yes! Money spent to get it ready is part of the cost.", "جی ہاں! تیار کرنے پر خرچ ہونے والی رقم قیمت کا حصہ ہے۔"),
      opt("loss", "It is a loss of Rs 500.", "یہ 500 روپے نقصان ہے۔", False,
          "SP 4000 is still more than CP 3500, so it is a profit of Rs 500.", "قیمتِ فروخت 4000، قیمتِ خرید 3500 سے زیادہ ہے، تو یہ 500 روپے نفع ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "He spent Rs 3500 in all, not Rs 3000.", "اس نے کل 3500 روپے خرچ کیے، 3000 نہیں۔", "forgets_extra_cost"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why does the repair money count as part of the cost price? Can you teach me?",
                     "مرمت کے پیسے قیمتِ خرید میں کیوں گنے جاتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we add repair or transport costs to the cost price?", "اپنے الفاظ میں بتائیں: ہم مرمت یا کرایے کا خرچ قیمتِ خرید میں کیوں جمع کرتے ہیں؟"),
    "key_idea": "Profit is the money you have at the end compared with all the money you spent. Repairs and transport are money spent to be able to sell, so leaving them out would make the profit look bigger than it really is.",
    "levels": {
      "got_it": "Says repairs or transport are money spent, so they are part of what it cost, and leaving them out makes the profit look too big.",
      "partly": "Says they are money spent, without saying what happens to the profit if they are left out.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["spent", "paid", "money", "خرچ", "ادا", "پیسے"],
      ["cost", "قیمت", "خرید"],
      ["bigger", "too much", "wrong", "real", "زیادہ", "اصل"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Every rupee spent counts, or the profit looks too big.", "بہت خوب! خرچ ہونے والا ہر روپیہ گنا جاتا ہے، ورنہ نفع زیادہ لگتا ہے۔"),
      "partly": T("Good start! Now say what would happen to the profit if we left the repairs out.", "اچھی شروعات! اب بتائیں اگر مرمت چھوڑ دیں تو نفع کا کیا ہوگا۔"),
      "not_yet": T("Imran spent Rs 3000 and then Rs 500 more. How much did he spend in all?", "عمران نے 3000 روپے اور پھر 500 روپے مزید خرچ کیے۔ کل کتنا خرچ کیا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Profit and loss unit. You can do it!",
                     "ٹیسٹ کا وقت! نفع اور نقصان کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on profit and loss, profit percent, the selling price, bills and change, and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں نفع اور نقصان، نفع کی فیصد، قیمتِ فروخت، بل اور بقایا، اور ایک اصل زندگی کا سوال ہے۔ آرام سے کریں۔")},
   number_question(
     "u1_loss",
     T("Test 1: A school bag is bought for Rs 750 and sold for Rs 600. What is the loss, in rupees?", "ٹیسٹ 1: ایک سکول بیگ 750 روپے میں خریدا اور 600 روپے میں بیچا گیا۔ نقصان کتنے روپے ہے؟"),
     U1,
     T("CP − SP.", "قیمتِ خرید − قیمتِ فروخت"),
     T("Right! Rs 150.", "درست! 150 روپے"),
     T("750 − 600 = 150.", "750 − 600 = 150"),
     common_wrong=[wrong(600, "Rs 600 is the selling price. Loss: 750 − 600 = 150.", "600 روپے قیمتِ فروخت ہے۔ نقصان: 750 − 600 = 150")],
     qtype="recall", skill=PL_MEANING),
   number_question(
     "u2_percent",
     T("Test 2: A clock is bought for Rs 300 and sold for Rs 360. What is the profit percent? Type just the number.", "ٹیسٹ 2: ایک گھڑیال 300 روپے میں خریدا اور 360 روپے میں بیچا گیا۔ نفع کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     U2,
     T("Profit = 60. Then 60 ÷ 300 × 100.", "نفع = 60۔ پھر 60 ÷ 300 × 100"),
     T("Right! 20%.", "درست! 20%"),
     T("60 ÷ 300 × 100 = 20.", "60 ÷ 300 × 100 = 20"),
     common_wrong=[wrong(60, "Rs 60 is the profit in rupees. 60 ÷ 300 × 100 = 20%.", "60 روپے نفع ہے۔ 60 ÷ 300 × 100 = 20%", "rupees_as_percent")],
     qtype="apply", skill=PL_PERCENT),
   number_question(
     "u3_selling_price",
     T("Test 3: A table costs Rs 800. It is sold at a 15% loss. What is the selling price, in rupees?", "ٹیسٹ 3: ایک میز 800 روپے کی ہے۔ اسے 15% نقصان پر بیچا جاتا ہے۔ قیمتِ فروخت کتنے روپے ہے؟"),
     U3,
     T("15% of 800 = 120. Then 800 − 120.", "800 کا 15% = 120۔ پھر 800 − 120"),
     T("Right! Rs 680.", "درست! 680 روپے"),
     T("800 − 120 = 680.", "800 − 120 = 680"),
     common_wrong=[wrong(920, "It's a loss, so take away: 800 − 120 = 680.", "یہ نقصان ہے، تو نفی کریں: 800 − 120 = 680"),
                   wrong(785, "15% is not Rs 15. 15% of 800 = 120, so 680.", "15%، 15 روپے نہیں ہے۔ 800 کا 15% = 120، تو 680")],
     qtype="apply", skill=PL_SELLING_PRICE),
   number_question(
     "u4_change",
     T("Test 4: Rice costs Rs 220 a kg. Ali buys 3 kg and pays with a Rs 1000 note. How much change does he get, in rupees?", "ٹیسٹ 4: چاول 220 روپے فی کلو ہیں۔ علی 3 کلو خریدتا ہے اور 1000 روپے کا نوٹ دیتا ہے۔ اسے کتنے روپے بقایا ملے گا؟"),
     U4,
     T("Bill: 3 × 220. Then 1000 − bill.", "بل: 3 × 220۔ پھر 1000 − بل"),
     T("Right! Rs 340.", "درست! 340 روپے"),
     T("3 × 220 = 660. 1000 − 660 = 340.", "3 × 220 = 660۔ 1000 − 660 = 340"),
     common_wrong=[wrong(660, "Rs 660 is the bill. Change: 1000 − 660 = 340.", "660 روپے بل ہے۔ بقایا: 1000 − 660 = 340"),
                   wrong(780, "3 kg cost 3 × 220 = 660, not 220. Change: 340.", "3 کلو 3 × 220 = 660 کے ہیں، 220 کے نہیں۔ بقایا: 340")],
     qtype="apply", skill=PL_BILLS),
   number_question(
     "u5_pens",
     T("Test 5: A shopkeeper buys 20 pens at Rs 12 each and sells all of them at Rs 15 each. What is the profit, in rupees?", "ٹیسٹ 5: ایک دکاندار 12 روپے فی قلم کے حساب سے 20 قلم خریدتا ہے اور سب 15 روپے فی قلم بیچتا ہے۔ نفع کتنے روپے ہے؟"),
     U5,
     T("CP = 20 × 12, SP = 20 × 15.", "قیمتِ خرید = 20 × 12، قیمتِ فروخت = 20 × 15"),
     T("Right! Rs 60.", "درست! 60 روپے"),
     T("300 − 240 = 60.", "300 − 240 = 60"),
     common_wrong=[wrong(3, "Rs 3 is the profit on one pen. On 20: 60.", "3 روپے ایک قلم پر نفع ہے۔ 20 پر: 60", "one_item_only")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Profit and loss unit complete! You think like a smart shopkeeper now.", "نفع اور نقصان کا باب مکمل! اب آپ ایک سمجھدار دکاندار کی طرح سوچتے ہیں۔"),
    "text": T("Find the total cost price, including extra costs like repairs or transport. Find the total selling price for all the items. The difference is the profit or loss. For a percent, divide by the total cost price and × 100.",
              "کل قیمتِ خرید نکالیں، مرمت یا کرایے جیسے اضافی خرچ سمیت۔ تمام چیزوں کی کل قیمتِ فروخت نکالیں۔ فرق نفع یا نقصان ہے۔ فیصد کے لیے کل قیمتِ خرید سے تقسیم کریں اور × 100 کریں۔"),
    "points": [T("Extra costs go into the cost price.", "اضافی خرچ قیمتِ خرید میں جاتا ہے۔"),
               T("Many items: use totals.", "بہت سی چیزیں: کل استعمال کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_shirts", "type": "apply", "skill": SKILL, "step": number_question(
     "r_shirts",
     T("A trader buys 5 shirts at Rs 400 each and sells all 5 for Rs 2400 in total. What is the profit, in rupees?", "ایک تاجر 400 روپے فی قمیض کے حساب سے 5 قمیضیں خریدتا ہے اور پانچوں کل 2400 روپے میں بیچتا ہے۔ نفع کتنے روپے ہے؟"),
     R1,
     T("CP = 5 × 400.", "قیمتِ خرید = 5 × 400"),
     T("Right! Rs 400.", "درست! 400 روپے"),
     T("2400 − 2000 = 400.", "2400 − 2000 = 400"),
     common_wrong=[wrong(2000, "Rs 2000 is the cost price. Profit: 2400 − 2000 = 400.", "2000 روپے قیمتِ خرید ہے۔ نفع: 2400 − 2000 = 400")],
     qtype=None)},
   {"id": "r_shirts_percent", "type": "apply", "skill": SKILL, "step": number_question(
     "r_shirts_percent",
     T("The trader spent Rs 2000 on the shirts and made Rs 400 profit. What is the profit percent? Type just the number.", "تاجر نے قمیضوں پر 2000 روپے خرچ کیے اور 400 روپے نفع کمایا۔ نفع کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     R2,
     T("400 ÷ 2000 × 100.", "400 ÷ 2000 × 100"),
     T("Right! 20%.", "درست! 20%"),
     T("400 ÷ 2000 × 100 = 20.", "400 ÷ 2000 × 100 = 20"),
     common_wrong=[wrong(400, "Rs 400 is the profit in rupees. 400 ÷ 2000 × 100 = 20%.", "400 روپے نفع ہے۔ 400 ÷ 2000 × 100 = 20%", "rupees_as_percent")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Profit and Loss unit. No textbook text or exercises were used.",
   "The five-question unit test at the end covers every lesson of the unit.",
   "Urdu terms to check: مرمت (repair), کل قیمتِ خرید (total cost price).",
   "The numbers were worked out in content/sources/g6-maths-12/profit_loss_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

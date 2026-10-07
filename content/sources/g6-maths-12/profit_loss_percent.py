from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, PC_FIND, PL_MEANING, PL_PERCENT, as_percent)

SKILL = PL_PERCENT

# s2: 30 out of 120 as a percent
S2 = as_percent(30, 120)
assert S2 == 25
# s4: CP 200, SP 250 -> profit 50 -> 25%
S4 = as_percent(250 - 200, 200)
assert S4 == 25
# s5: CP 400, SP 340 -> loss 60 -> 15%
S5 = as_percent(400 - 340, 400)
assert S5 == 15
# s7: CP 500, SP 600 -> 20%
S7 = as_percent(600 - 500, 500)
assert S7 == 20
# s8: bicycle CP 2000, SP 1500 -> loss 25%
S8 = as_percent(2000 - 1500, 2000)
assert S8 == 25
# s9: CP 80, SP 100: profit 20 is 25% of CP, not 20% of SP
assert as_percent(20, 80) == 25 and as_percent(20, 100) == 20
# s11: shop A CP 100 profit 20 (20%); shop B CP 400 profit 60 -> 15%
assert as_percent(20, 100) == 20
S11 = as_percent(60, 400)
assert S11 == 15
# question bank and review
QB = as_percent(60 - 50, 50)
assert QB == 20
R1 = as_percent(250 - 200, 250)
assert R1 == 20
R2 = as_percent(200 - 160, 160)
assert R2 == 25

lesson = {
 "id": "g6-maths-12-profit-loss-percent",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the profit or loss as a percentage of the cost price.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Profit and loss percent", "نفع اور نقصان کی فیصد"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": PL_MEANING}, {"skill": PC_FIND}],
 "misconceptions": [
   {"id": "percent_of_sp", "description": "Divides the profit or loss by the selling price instead of the cost price."},
   {"id": "rupees_as_percent", "description": "Gives the profit in rupees as the percent (Rs 50 profit = 50%)."},
   {"id": "bigger_is_better", "description": "Thinks the bigger profit in rupees is always the better deal, without comparing percents."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("How do you find the profit percent?", "نفع کی فیصد کیسے نکالتے ہیں؟"),
     "options": [
       opt("of_cp", "Profit ÷ cost price × 100", "نفع ÷ قیمتِ خرید × 100", True,
           "Yes! The percent is always of the cost price.", "جی ہاں! فیصد ہمیشہ قیمتِ خرید کی ہوتی ہے۔"),
       opt("of_sp", "Profit ÷ selling price × 100", "نفع ÷ قیمتِ فروخت × 100", False,
           "We compare the profit with what was paid: the cost price.", "ہم نفع کا موازنہ ادا کی گئی رقم یعنی قیمتِ خرید سے کرتے ہیں۔", "percent_of_sp"),
       opt("rupees", "The profit in rupees is the percent", "روپوں میں نفع ہی فیصد ہے", False,
           "Rupees are not a percent. Divide by the cost price and × 100.", "روپے فیصد نہیں ہیں۔ قیمتِ خرید سے تقسیم کریں اور × 100 کریں۔", "rupees_as_percent"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A toy costs Rs 50 and is sold for Rs 60. What is the profit percent? Type just the number.", "ایک کھلونا 50 روپے کا خریدا اور 60 روپے میں بیچا گیا۔ نفع کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     QB,
     T("Profit = 10. Then 10 ÷ 50 × 100.", "نفع = 10۔ پھر 10 ÷ 50 × 100"),
     T("Right! 20%.", "درست! 20%"),
     T("Profit 10. 10 ÷ 50 × 100 = 20%.", "نفع 10۔ 10 ÷ 50 × 100 = 20%"),
     common_wrong=[wrong(10, "Rs 10 is the profit in rupees. 10 ÷ 50 × 100 = 20%.", "10 روپے نفع ہے۔ 10 ÷ 50 × 100 = 20%", "rupees_as_percent")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A lamp costs Rs 80 and is sold for Rs 100. Kamran says the profit percent is 20 ÷ 100 × 100 = 20%. What is wrong?", "ایک لیمپ 80 روپے کا خریدا اور 100 روپے میں بیچا گیا۔ کامران کہتا ہے نفع 20 ÷ 100 × 100 = 20% ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("use_cp", "He divided by the selling price. It should be 20 ÷ 80 × 100 = 25%.", "اس نے قیمتِ فروخت سے تقسیم کیا۔ 20 ÷ 80 × 100 = 25% ہونا چاہیے۔", True,
           "Yes! The percent is of the cost price.", "جی ہاں! فیصد قیمتِ خرید کی ہوتی ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Look at what he divided by: Rs 100 is the selling price.", "دیکھیں اس نے کس سے تقسیم کیا: 100 روپے قیمتِ فروخت ہے۔", "percent_of_sp"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_profit_percent", "front": T("Profit percent?", "نفع کی فیصد؟"),
    "back": T("Profit ÷ cost price × 100", "نفع ÷ قیمتِ خرید × 100")},
   {"id": "f_loss_percent", "front": T("Loss percent?", "نقصان کی فیصد؟"),
    "back": T("Loss ÷ cost price × 100", "نقصان ÷ قیمتِ خرید × 100")},
 ],
 "home_tasks": [{"id": "h_deal", "text": T(
   "Think of something your family bought and later sold, or ask a shopkeeper about one item. Work out the profit or loss, then the percent of the cost price.",
   "کسی ایسی چیز کے بارے میں سوچیں جو آپ کے گھر والوں نے خریدی اور بعد میں بیچی، یا کسی دکاندار سے ایک چیز کے بارے میں پوچھیں۔ نفع یا نقصان نکالیں، پھر قیمتِ خرید کی فیصد۔")}],
 "glossary": [T("Profit percent", "نفع کی فیصد"), T("Loss percent", "نقصان کی فیصد"), T("Cost price", "قیمتِ خرید")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Ali makes Rs 20 on a Rs 100 toy. Sara makes Rs 60 on a Rs 400 bag. Who did better?",
                     "علی 100 روپے کے کھلونے پر 20 روپے کماتا ہے۔ سارہ 400 روپے کے بیگ پر 60 روپے۔ کس نے بہتر کیا؟"),
    "text": T("Rupees alone don't tell us. A percent lets us compare. First, a quick percent check.", "صرف روپے یہ نہیں بتاتے۔ فیصد سے ہم موازنہ کر سکتے ہیں۔ پہلے فیصد کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("What percent is 30 of 120? Type just the number.", "30، 120 کا کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S2,
     T("30 ÷ 120, then × 100.", "30 ÷ 120، پھر × 100"),
     T("Right! 25%.", "درست! 25%"),
     T("30/120 = 1/4 = 25%.", "30/120 = 1/4 = 25%"),
     common_wrong=[wrong(30, "30 out of 120 is not 30%. 30 ÷ 120 × 100 = 25.", "120 میں سے 30، 30% نہیں ہے۔ 30 ÷ 120 × 100 = 25")],
     qtype="recall", skill=PC_FIND),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Always compare with the cost price: the money you put in.", "ہمیشہ قیمتِ خرید سے موازنہ کریں: وہ رقم جو آپ نے لگائی۔"),
    "text": T("Profit percent = profit ÷ cost price × 100. Loss percent = loss ÷ cost price × 100. Example: bought for Rs 200, sold for Rs 250. Profit = 50. 50 ÷ 200 × 100 = 25%.",
              "نفع کی فیصد = نفع ÷ قیمتِ خرید × 100۔ نقصان کی فیصد = نقصان ÷ قیمتِ خرید × 100۔ مثال: 200 روپے میں خریدا، 250 میں بیچا۔ نفع = 50۔ 50 ÷ 200 × 100 = 25%")},
   number_question(
     "s4_profit_percent",
     T("A shirt is bought for Rs 200 and sold for Rs 250. What is the profit percent? Type just the number.", "ایک قمیض 200 روپے میں خریدی اور 250 روپے میں بیچی گئی۔ نفع کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S4,
     T("Profit = 50. Then 50 ÷ 200 × 100.", "نفع = 50۔ پھر 50 ÷ 200 × 100"),
     T("Right! 25%.", "درست! 25%"),
     T("50 ÷ 200 × 100 = 25.", "50 ÷ 200 × 100 = 25"),
     common_wrong=[wrong(50, "Rs 50 is the profit in rupees. 50 ÷ 200 × 100 = 25%.", "50 روپے نفع ہے۔ 50 ÷ 200 × 100 = 25%", "rupees_as_percent"),
                   wrong(20, "Divide by the cost price (200), not the selling price (250).", "قیمتِ خرید (200) سے تقسیم کریں، قیمتِ فروخت (250) سے نہیں۔", "percent_of_sp")]),
   number_question(
     "s5_loss_percent",
     T("A school bag is bought for Rs 400 and sold for Rs 340. What is the loss percent? Type just the number.", "ایک سکول بیگ 400 روپے میں خریدا اور 340 روپے میں بیچا گیا۔ نقصان کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S5,
     T("Loss = 400 − 340 = 60. Then 60 ÷ 400 × 100.", "نقصان = 400 − 340 = 60۔ پھر 60 ÷ 400 × 100"),
     T("Right! 15%.", "درست! 15%"),
     T("60 ÷ 400 × 100 = 15.", "60 ÷ 400 × 100 = 15"),
     common_wrong=[wrong(60, "Rs 60 is the loss in rupees. 60 ÷ 400 × 100 = 15%.", "60 روپے نقصان ہے۔ 60 ÷ 400 × 100 = 15%", "rupees_as_percent")]),
   {"id": "s6_which_price", "type": "choice",
    "prompt": T("Profit percent and loss percent are always worked out from which price?", "نفع اور نقصان کی فیصد ہمیشہ کس قیمت سے نکالی جاتی ہے؟"),
    "options": [
      opt("cp", "The cost price", "قیمتِ خرید", True, "Yes! The money that was put in.", "جی ہاں! وہ رقم جو لگائی گئی۔"),
      opt("sp", "The selling price", "قیمتِ فروخت", False, "No, we compare with what was paid: the cost price.", "نہیں، ہم ادا کی گئی رقم یعنی قیمتِ خرید سے موازنہ کرتے ہیں۔", "percent_of_sp"),
      opt("100", "Always Rs 100", "ہمیشہ 100 روپے", False, "We divide by the cost price, then × 100.", "ہم قیمتِ خرید سے تقسیم کرتے ہیں، پھر × 100"),
    ]},
   number_question(
     "s7_watch",
     T("A watch is bought for Rs 500 and sold for Rs 600. What is the profit percent? Type just the number.", "ایک گھڑی 500 روپے میں خریدی اور 600 روپے میں بیچی گئی۔ نفع کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S7,
     T("Profit = 100. Then 100 ÷ 500 × 100.", "نفع = 100۔ پھر 100 ÷ 500 × 100"),
     T("Right! 20%.", "درست! 20%"),
     T("100 ÷ 500 × 100 = 20.", "100 ÷ 500 × 100 = 20"),
     common_wrong=[wrong(100, "Rs 100 is the profit in rupees. 100 ÷ 500 × 100 = 20%.", "100 روپے نفع ہے۔ 100 ÷ 500 × 100 = 20%", "rupees_as_percent")]),
   number_question(
     "s8_bicycle",
     T("Usman bought a bicycle for Rs 2000 and sold it for Rs 1500. What is his loss percent? Type just the number.", "عثمان نے سائیکل 2000 روپے میں خریدی اور 1500 روپے میں بیچی۔ اس کا نقصان کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S8,
     T("Loss = 500. Then 500 ÷ 2000 × 100.", "نقصان = 500۔ پھر 500 ÷ 2000 × 100"),
     T("Right! 25%.", "درست! 25%"),
     T("500 ÷ 2000 × 100 = 25.", "500 ÷ 2000 × 100 = 25"),
     common_wrong=[wrong(33, "Divide by the cost price (2000), not 1500: 500 ÷ 2000 × 100 = 25.", "1500 نہیں، قیمتِ خرید (2000) سے تقسیم کریں: 500 ÷ 2000 × 100 = 25", "percent_of_sp")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A lamp is bought for Rs 80 and sold for Rs 100. Hina says, \"Profit 20, so 20 ÷ 100 × 100 = 20%.\" What went wrong?", "ایک لیمپ 80 روپے میں خریدا اور 100 روپے میں بیچا گیا۔ حنا کہتی ہے، \"نفع 20، تو 20 ÷ 100 × 100 = 20%۔\" کیا غلطی ہوئی؟"),
    "options": [
      opt("use_cp", "She divided by the selling price. It should be 20 ÷ 80 × 100 = 25%.", "اس نے قیمتِ فروخت سے تقسیم کیا۔ 20 ÷ 80 × 100 = 25% ہونا چاہیے۔", True,
          "Yes! Always divide by the cost price.", "جی ہاں! ہمیشہ قیمتِ خرید سے تقسیم کریں۔"),
      opt("profit", "The profit is not Rs 20.", "نفع 20 روپے نہیں ہے۔", False,
          "The profit is right: 100 − 80 = 20. The mistake is dividing by 100.", "نفع درست ہے: 100 − 80 = 20۔ غلطی 100 سے تقسیم کرنا ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Rs 100 is the selling price. Divide by the cost price, 80.", "100 روپے قیمتِ فروخت ہے۔ قیمتِ خرید 80 سے تقسیم کریں۔", "percent_of_sp"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Ali made Rs 20 and Sara made Rs 60. Why might Ali have done better? Can you teach me?",
                     "علی نے 20 روپے اور سارہ نے 60 روپے کمائے۔ علی نے بہتر کیوں کیا ہو سکتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we use a percent of the cost price to compare two deals, and not just the rupees?", "اپنے الفاظ میں بتائیں: دو سودوں کا موازنہ کرنے کے لیے ہم صرف روپے کے بجائے قیمتِ خرید کی فیصد کیوں استعمال کرتے ہیں؟"),
    "key_idea": "Deals start with different amounts of money. A percent of the cost price shows how much was earned for every 100 rupees put in, so deals of different sizes can be compared fairly. Ali: 20 on 100 is 20%; Sara: 60 on 400 is 15%.",
    "levels": {
      "got_it": "Says the cost prices are different, and a percent shows the profit for every 100 rupees spent, so it is a fair comparison.",
      "partly": "Says percent is fairer, without linking it to the different cost prices.",
      "not_yet": "Gives no reason, or says the bigger rupee profit is always better."},
    "keywords": [
      ["cost", "spent", "paid", "خرید", "خرچ", "لگائی"],
      ["100", "every", "hundred", "سو"],
      ["fair", "compare", "different", "موازنہ", "مختلف"]],
    "fallback_feedback": {
      "got_it": T("Well explained! A percent shows the profit for every Rs 100 put in.", "بہت خوب! فیصد ہر 100 روپے پر نفع دکھاتی ہے۔"),
      "partly": T("Good start! Now say why the different cost prices matter.", "اچھی شروعات! اب بتائیں کہ مختلف قیمتِ خرید کیوں اہم ہے۔"),
      "not_yet": T("Ali spent Rs 100 and Sara spent Rs 400. For every Rs 100 spent, how much did each earn?", "علی نے 100 روپے اور سارہ نے 400 روپے لگائے۔ ہر 100 روپے پر ہر ایک نے کتنا کمایا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_compare",
     T("Ali makes Rs 20 profit on a toy that cost Rs 100: that is 20%. Sara makes Rs 60 profit on a bag that cost Rs 400. What is Sara's profit percent? Type just the number.", "علی 100 روپے کے کھلونے پر 20 روپے نفع کماتا ہے: یہ 20% ہے۔ سارہ 400 روپے کے بیگ پر 60 روپے نفع کماتی ہے۔ سارہ کا نفع کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S11,
     T("60 ÷ 400 × 100.", "60 ÷ 400 × 100"),
     T("Right! 15%, so Ali did better for the money he put in.", "درست! 15%، تو لگائی گئی رقم کے حساب سے علی نے بہتر کیا۔"),
     T("60 ÷ 400 × 100 = 15. Ali's 20% is better.", "60 ÷ 400 × 100 = 15۔ علی کا 20% بہتر ہے۔"),
     common_wrong=[wrong(60, "Rs 60 is the profit in rupees. 60 ÷ 400 × 100 = 15%.", "60 روپے نفع ہے۔ 60 ÷ 400 × 100 = 15%", "rupees_as_percent")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can compare any two deals fairly!", "اب آپ کسی بھی دو سودوں کا منصفانہ موازنہ کر سکتے ہیں!"),
    "text": T("Profit percent = profit ÷ cost price × 100. Loss percent = loss ÷ cost price × 100. Always divide by the cost price. A percent lets us compare deals of different sizes.",
              "نفع کی فیصد = نفع ÷ قیمتِ خرید × 100۔ نقصان کی فیصد = نقصان ÷ قیمتِ خرید × 100۔ ہمیشہ قیمتِ خرید سے تقسیم کریں۔ فیصد سے مختلف سائز کے سودوں کا موازنہ ہو سکتا ہے۔"),
    "points": [T("Find the profit or loss in rupees first.", "پہلے روپوں میں نفع یا نقصان نکالیں۔"),
               T("Then ÷ cost price × 100.", "پھر ÷ قیمتِ خرید × 100")]},
 ],
 "review_questions": [
   {"id": "r_loss", "type": "apply", "skill": SKILL, "step": number_question(
     "r_loss",
     T("A fan is bought for Rs 250 and sold for Rs 200. What is the loss percent? Type just the number.", "ایک پنکھا 250 روپے میں خریدا اور 200 روپے میں بیچا گیا۔ نقصان کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     R1,
     T("Loss = 50. Then 50 ÷ 250 × 100.", "نقصان = 50۔ پھر 50 ÷ 250 × 100"),
     T("Right! 20%.", "درست! 20%"),
     T("50 ÷ 250 × 100 = 20.", "50 ÷ 250 × 100 = 20"),
     common_wrong=[wrong(25, "Divide by the cost price (250), not 200: 50 ÷ 250 × 100 = 20.", "200 نہیں، قیمتِ خرید (250) سے تقسیم کریں: 50 ÷ 250 × 100 = 20", "percent_of_sp")],
     qtype=None)},
   {"id": "r_profit", "type": "apply", "skill": SKILL, "step": number_question(
     "r_profit",
     T("A book is bought for Rs 160 and sold for Rs 200. What is the profit percent? Type just the number.", "ایک کتاب 160 روپے میں خریدی اور 200 روپے میں بیچی گئی۔ نفع کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     R2,
     T("Profit = 40. Then 40 ÷ 160 × 100.", "نفع = 40۔ پھر 40 ÷ 160 × 100"),
     T("Right! 25%.", "درست! 25%"),
     T("40 ÷ 160 × 100 = 25.", "40 ÷ 160 × 100 = 25"),
     common_wrong=[wrong(20, "Divide by the cost price (160), not 200: 40 ÷ 160 × 100 = 25.", "200 نہیں، قیمتِ خرید (160) سے تقسیم کریں: 40 ÷ 160 × 100 = 25", "percent_of_sp")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Profit and Loss unit. No textbook text or exercises were used.",
   "The hook and s11 compare two deals to show why a percent of the cost price is used.",
   "Urdu terms to check: نفع کی فیصد (profit percent), نقصان کی فیصد (loss percent).",
   "The numbers were worked out in content/sources/g6-maths-12/profit_loss_percent.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

from common import (D, T, opt, say, wrong, number_question, write,
                    REF, REVIEW, DEC_ADD_SUBTRACT, PL_MEANING)

SKILL = PL_MEANING

# s2: Rs 12.50 + Rs 7.50
S2 = D("12.50") + D("7.50")
assert S2 == 20
# s4: mangoes CP 120, SP 150
S4 = 150 - 120
assert S4 == 30
# s5: bicycle CP 4500, SP 4200
S5 = 4500 - 4200
assert S5 == 300
# s7: 10 pens at Rs 15, all sold for Rs 200
S7 = 200 - 10 * 15
assert S7 == 50
# s8: profit 75, SP 400 -> CP
S8 = 400 - 75
assert S8 == 325 and S8 + 75 == 400
# s9: CP 600, SP 550 is a loss of 50
assert 550 < 600 and 600 - 550 == 50
# s11: crate CP 900, halves sold for 600 and 500
S11 = (600 + 500) - 900
assert S11 == 200
# question bank and review
QB = 310 - 250
assert QB == 60
R1 = 1200 - 1000
assert R1 == 200
R2 = 95 - 80
assert R2 == 15

lesson = {
 "id": "g6-maths-12-profit-and-loss",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Understand cost price and selling price, and work out the profit or loss in rupees.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Profit and loss", "نفع اور نقصان"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": DEC_ADD_SUBTRACT}],
 "misconceptions": [
   {"id": "profit_loss_swap", "description": "Calls it a profit when the selling price is less than the cost price, or the other way round."},
   {"id": "per_item_cost", "description": "Uses the price of one item as the cost price when many were bought."},
   {"id": "sp_as_profit", "description": "Gives the selling price as the profit, without taking away the cost price."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("When is there a profit?", "نفع کب ہوتا ہے؟"),
     "options": [
       opt("sp_more", "When the selling price is more than the cost price", "جب قیمتِ فروخت قیمتِ خرید سے زیادہ ہو", True,
           "Yes! Profit = selling price − cost price.", "جی ہاں! نفع = قیمتِ فروخت − قیمتِ خرید۔"),
       opt("cp_more", "When the cost price is more than the selling price", "جب قیمتِ خرید قیمتِ فروخت سے زیادہ ہو", False,
           "That is a loss: you got back less than you paid.", "یہ نقصان ہے: آپ کو ادا کیے سے کم واپس ملا۔", "profit_loss_swap"),
       opt("same", "When they are the same", "جب دونوں برابر ہوں", False,
           "Then there is no profit and no loss.", "تب نہ نفع ہے نہ نقصان۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A cap costs a shopkeeper Rs 250. He sells it for Rs 310. What is his profit, in rupees?", "ایک دکاندار کو ٹوپی 250 روپے کی پڑتی ہے۔ وہ اسے 310 روپے میں بیچتا ہے۔ اس کا نفع کتنے روپے ہے؟"),
     QB,
     T("Selling price − cost price.", "قیمتِ فروخت − قیمتِ خرید"),
     T("Right! Rs 60 profit.", "درست! 60 روپے نفع"),
     T("310 − 250 = 60.", "310 − 250 = 60"),
     common_wrong=[wrong(310, "Rs 310 is the selling price. Profit: 310 − 250 = 60.", "310 روپے قیمتِ فروخت ہے۔ نفع: 310 − 250 = 60", "sp_as_profit")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Nasir buys a phone cover for Rs 600 and sells it for Rs 550. He says he made a profit of Rs 50. What is wrong?", "ناصر فون کور 600 روپے میں خریدتا ہے اور 550 روپے میں بیچتا ہے۔ وہ کہتا ہے اسے 50 روپے نفع ہوا۔ کیا غلطی ہے؟"),
     "options": [
       opt("loss", "He sold it for less than he paid, so it is a loss of Rs 50.", "اس نے ادا کیے سے کم میں بیچا، تو یہ 50 روپے نقصان ہے۔", True,
           "Yes! Selling price below cost price means a loss.", "جی ہاں! قیمتِ فروخت قیمتِ خرید سے کم ہو تو نقصان ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "He got back Rs 550 for Rs 600 spent. That is a loss of Rs 50.", "600 روپے خرچ کر کے 550 واپس ملے۔ یہ 50 روپے نقصان ہے۔", "profit_loss_swap"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_profit", "front": T("Profit?", "نفع؟"),
    "back": T("Selling price − cost price, when you sell for more than you paid.", "قیمتِ فروخت − قیمتِ خرید، جب ادا کیے سے زیادہ میں بیچیں۔")},
   {"id": "f_loss", "front": T("Loss?", "نقصان؟"),
    "back": T("Cost price − selling price, when you sell for less than you paid.", "قیمتِ خرید − قیمتِ فروخت، جب ادا کیے سے کم میں بیچیں۔")},
 ],
 "home_tasks": [{"id": "h_shop", "text": T(
   "Ask someone at home, or a shopkeeper you know, about one thing they buy and sell, like a packet of biscuits. What do they pay for it, and what do they sell it for? Work out the profit.",
   "گھر میں کسی سے، یا کسی جاننے والے دکاندار سے، کسی ایسی چیز کے بارے میں پوچھیں جو وہ خریدتے اور بیچتے ہیں، جیسے بسکٹ کا پیکٹ۔ وہ اسے کتنے میں خریدتے ہیں اور کتنے میں بیچتے ہیں؟ نفع نکالیں۔")}],
 "glossary": [T("Cost price", "قیمتِ خرید"), T("Selling price", "قیمتِ فروخت"), T("Profit", "نفع"), T("Loss", "نقصان")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Bilal's uncle buys mangoes for Rs 120 a dozen and sells them for Rs 150. Did he earn money or lose it?",
                     "بلال کے چچا آم 120 روپے درجن خریدتے ہیں اور 150 روپے میں بیچتے ہیں۔ انہوں نے پیسے کمائے یا گنوائے؟"),
    "text": T("Today we learn about profit and loss. First, a quick check with rupees.", "آج ہم نفع اور نقصان سیکھیں گے۔ پہلے روپوں کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Rs 12.50 + Rs 7.50 = ? rupees", "12.50 روپے + 7.50 روپے = ? روپے"),
     S2,
     T("50 paisa + 50 paisa makes 1 rupee.", "50 پیسے + 50 پیسے سے 1 روپیہ بنتا ہے۔"),
     T("Right! Rs 20.", "درست! 20 روپے"),
     T("12.50 + 7.50 = 20.", "12.50 + 7.50 = 20"),
     common_wrong=[wrong(19, "Don't forget the 50 + 50 paisa: Rs 20.", "50 + 50 پیسے نہ بھولیں: 20 روپے")],
     qtype="recall", skill=DEC_ADD_SUBTRACT),
   {"id": "s3_cp_sp", "type": "explain",
    "character": say("happy", "Sell for more than you paid: profit! Sell for less: loss.", "ادا کیے سے زیادہ میں بیچیں: نفع! کم میں بیچیں: نقصان۔"),
    "text": T("The cost price (CP) is what you pay for something. The selling price (SP) is what you sell it for. If SP is more than CP, you make a profit: profit = SP − CP. If SP is less than CP, you make a loss: loss = CP − SP. If they are equal, there is no profit and no loss.",
              "قیمتِ خرید وہ ہے جو آپ کسی چیز کے لیے ادا کرتے ہیں۔ قیمتِ فروخت وہ ہے جس پر آپ اسے بیچتے ہیں۔ اگر قیمتِ فروخت قیمتِ خرید سے زیادہ ہو تو نفع ہوتا ہے: نفع = قیمتِ فروخت − قیمتِ خرید۔ اگر کم ہو تو نقصان: نقصان = قیمتِ خرید − قیمتِ فروخت۔ برابر ہوں تو نہ نفع نہ نقصان۔")},
   number_question(
     "s4_mangoes",
     T("Mangoes cost Rs 120 a dozen and are sold for Rs 150 a dozen. What is the profit on one dozen, in rupees?", "آم 120 روپے درجن کے خریدے اور 150 روپے درجن بیچے گئے۔ ایک درجن پر کتنے روپے نفع ہے؟"),
     S4,
     T("SP − CP.", "قیمتِ فروخت − قیمتِ خرید"),
     T("Right! Rs 30 profit.", "درست! 30 روپے نفع"),
     T("150 − 120 = 30.", "150 − 120 = 30"),
     common_wrong=[wrong(150, "Rs 150 is the selling price. Profit: 150 − 120 = 30.", "150 روپے قیمتِ فروخت ہے۔ نفع: 150 − 120 = 30", "sp_as_profit"),
                   wrong(270, "Take away, don't add: 150 − 120 = 30.", "جمع نہیں، نفی کریں: 150 − 120 = 30")]),
   number_question(
     "s5_bicycle",
     T("Hamid bought an old bicycle for Rs 4500 and later sold it for Rs 4200. What was his loss, in rupees?", "حامد نے پرانی سائیکل 4500 روپے میں خریدی اور بعد میں 4200 روپے میں بیچی۔ اسے کتنے روپے نقصان ہوا؟"),
     S5,
     T("CP − SP.", "قیمتِ خرید − قیمتِ فروخت"),
     T("Right! Rs 300 loss.", "درست! 300 روپے نقصان"),
     T("4500 − 4200 = 300.", "4500 − 4200 = 300"),
     common_wrong=[wrong(4200, "Rs 4200 is what he got. Loss: 4500 − 4200 = 300.", "4200 روپے اسے ملے۔ نقصان: 4500 − 4200 = 300", "sp_as_profit")]),
   {"id": "s6_neither", "type": "choice",
    "prompt": T("A watch is bought for Rs 800 and sold for Rs 800. What is it?", "ایک گھڑی 800 روپے میں خریدی اور 800 روپے میں بیچی گئی۔ یہ کیا ہے؟"),
    "options": [
      opt("neither", "No profit and no loss", "نہ نفع نہ نقصان", True, "Yes! SP = CP.", "جی ہاں! قیمتِ فروخت = قیمتِ خرید"),
      opt("profit", "A profit of Rs 800", "800 روپے نفع", False, "Rs 800 came back for Rs 800 spent: no profit.", "800 خرچ کر کے 800 واپس آئے: کوئی نفع نہیں۔", "sp_as_profit"),
      opt("loss", "A loss", "نقصان", False, "Nothing was lost: SP = CP.", "کچھ نہیں گیا: قیمتِ فروخت = قیمتِ خرید"),
    ]},
   number_question(
     "s7_pens",
     T("A shopkeeper buys 10 pens at Rs 15 each and sells all of them for Rs 200. What is the profit, in rupees?", "ایک دکاندار 15 روپے فی قلم کے حساب سے 10 قلم خریدتا ہے اور سب کو 200 روپے میں بیچتا ہے۔ نفع کتنے روپے ہے؟"),
     S7,
     T("Cost price of all 10: 10 × 15.", "تمام 10 کی قیمتِ خرید: 10 × 15"),
     T("Right! 200 − 150 = Rs 50.", "درست! 200 − 150 = 50 روپے"),
     T("CP = 10 × 15 = 150. Profit = 200 − 150 = 50.", "قیمتِ خرید = 10 × 15 = 150۔ نفع = 200 − 150 = 50"),
     common_wrong=[wrong(185, "Rs 15 is for one pen. All 10 cost Rs 150: profit 200 − 150 = 50.", "15 روپے ایک قلم کے ہیں۔ تمام 10 کے 150: نفع 200 − 150 = 50", "per_item_cost")]),
   number_question(
     "s8_find_cp",
     T("Sana sold a bag for Rs 400 and made a profit of Rs 75. What was the cost price, in rupees?", "ثنا نے ایک بیگ 400 روپے میں بیچا اور 75 روپے نفع کمایا۔ قیمتِ خرید کتنے روپے تھی؟"),
     S8,
     T("SP = CP + profit, so CP = SP − profit.", "قیمتِ فروخت = قیمتِ خرید + نفع، تو قیمتِ خرید = قیمتِ فروخت − نفع"),
     T("Right! Rs 325.", "درست! 325 روپے"),
     T("400 − 75 = 325. Check: 325 + 75 = 400.", "400 − 75 = 325۔ جانچ: 325 + 75 = 400"),
     common_wrong=[wrong(475, "With a profit, the cost price is less than Rs 400: 400 − 75 = 325.", "نفع ہو تو قیمتِ خرید 400 سے کم ہے: 400 − 75 = 325")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Rubina buys a dupatta for Rs 600 and sells it for Rs 550. She says, \"I made Rs 50 profit.\" What went wrong?", "روبینہ دوپٹہ 600 روپے میں خریدتی ہے اور 550 روپے میں بیچتی ہے۔ وہ کہتی ہے، \"مجھے 50 روپے نفع ہوا۔\" کیا غلطی ہوئی؟"),
    "options": [
      opt("loss", "She sold it for less than she paid. It is a loss of Rs 50.", "اس نے ادا کیے سے کم میں بیچا۔ یہ 50 روپے نقصان ہے۔", True,
          "Yes! SP is less than CP, so it is a loss.", "جی ہاں! قیمتِ فروخت کم ہے، اس لیے نقصان ہے۔"),
      opt("amount", "The profit should be Rs 550.", "نفع 550 روپے ہونا چاہیے۔", False,
          "Rs 550 is what she got. She spent Rs 600, so she lost Rs 50.", "550 روپے اسے ملے۔ اس نے 600 خرچ کیے، تو 50 روپے نقصان ہوا۔", "sp_as_profit"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "She got back less than she spent. That is a loss.", "اسے خرچ سے کم واپس ملا۔ یہ نقصان ہے۔", "profit_loss_swap"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is selling for less than you paid a loss, even though you still got money? Can you teach me?",
                     "ادا کیے سے کم میں بیچنا نقصان کیوں ہے، حالانکہ پیسے تو پھر بھی ملے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is it a loss when the selling price is less than the cost price?", "اپنے الفاظ میں بتائیں: جب قیمتِ فروخت قیمتِ خرید سے کم ہو تو نقصان کیوں ہوتا ہے؟"),
    "key_idea": "You first spent the cost price. Selling brings back only the selling price, which is less, so you end up with less money than you started with. The difference, CP − SP, is the loss.",
    "levels": {
      "got_it": "Says you spent more (the cost price) than you got back (the selling price), so you end with less money than before.",
      "partly": "Says the selling price is smaller, without saying you end with less money than you started with.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["spent", "paid", "cost", "خرچ", "ادا", "خرید"],
      ["got back", "less", "کم", "واپس"],
      ["started", "before", "lost", "پہلے", "گنوا"]],
    "fallback_feedback": {
      "got_it": T("Well explained! You get back less than you spent, so money is lost.", "بہت خوب! خرچ سے کم واپس ملتا ہے، اس لیے پیسے گئے۔"),
      "partly": T("Good start! Now compare the money you had before buying with the money you have after selling.", "اچھی شروعات! اب خریدنے سے پہلے اور بیچنے کے بعد کے پیسوں کا موازنہ کریں۔"),
      "not_yet": T("Start with Rs 600. Spend it on a dupatta, then sell the dupatta for Rs 550. How much do you have now?", "600 روپے سے شروع کریں۔ انہیں دوپٹے پر خرچ کریں، پھر دوپٹہ 550 میں بیچیں۔ اب آپ کے پاس کتنے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_crate",
     T("A fruit seller buys a crate of apples for Rs 900. He sells half the crate for Rs 600 and the other half for Rs 500. What is his profit, in rupees?", "ایک پھل فروش سیبوں کی پیٹی 900 روپے میں خریدتا ہے۔ وہ آدھی پیٹی 600 روپے میں اور باقی آدھی 500 روپے میں بیچتا ہے۔ اس کا نفع کتنے روپے ہے؟"),
     S11,
     T("Total selling price first: 600 + 500.", "پہلے کل قیمتِ فروخت: 600 + 500"),
     T("Right! 1100 − 900 = Rs 200.", "درست! 1100 − 900 = 200 روپے"),
     T("SP = 600 + 500 = 1100. Profit = 1100 − 900 = 200.", "قیمتِ فروخت = 600 + 500 = 1100۔ نفع = 1100 − 900 = 200"),
     common_wrong=[wrong(1100, "Rs 1100 is the total selling price. Profit: 1100 − 900 = 200.", "1100 روپے کل قیمتِ فروخت ہے۔ نفع: 1100 − 900 = 200", "sp_as_profit"),
                   wrong(100, "Add both halves first: 600 + 500 = 1100, then 1100 − 900 = 200.", "پہلے دونوں آدھے جمع کریں: 600 + 500 = 1100، پھر 1100 − 900 = 200")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can tell if a sale made money!", "اب آپ بتا سکتے ہیں کہ بیچنے سے پیسے کمائے یا نہیں!"),
    "text": T("Cost price (CP) is what you pay; selling price (SP) is what you sell for. SP more than CP: profit = SP − CP. SP less than CP: loss = CP − SP. When many things are bought, find the total cost price first.",
              "قیمتِ خرید وہ ہے جو آپ ادا کرتے ہیں؛ قیمتِ فروخت وہ ہے جس پر بیچتے ہیں۔ قیمتِ فروخت زیادہ ہو: نفع = قیمتِ فروخت − قیمتِ خرید۔ کم ہو: نقصان = قیمتِ خرید − قیمتِ فروخت۔ جب بہت سی چیزیں خریدی جائیں تو پہلے کل قیمتِ خرید نکالیں۔"),
    "points": [T("Profit = SP − CP.", "نفع = قیمتِ فروخت − قیمتِ خرید۔"),
               T("Loss = CP − SP.", "نقصان = قیمتِ خرید − قیمتِ فروخت۔")]},
 ],
 "review_questions": [
   {"id": "r_loss", "type": "apply", "skill": SKILL, "step": number_question(
     "r_loss",
     T("A goat is bought for Rs 1200 and sold for Rs 1000. What is the loss, in rupees?", "ایک بکری 1200 روپے میں خریدی اور 1000 روپے میں بیچی گئی۔ کتنے روپے نقصان ہوا؟"),
     R1,
     T("CP − SP.", "قیمتِ خرید − قیمتِ فروخت"),
     T("Right! Rs 200.", "درست! 200 روپے"),
     T("1200 − 1000 = 200.", "1200 − 1000 = 200"),
     common_wrong=[wrong(1000, "Rs 1000 is the selling price. Loss: 1200 − 1000 = 200.", "1000 روپے قیمتِ فروخت ہے۔ نقصان: 1200 − 1000 = 200", "sp_as_profit")],
     qtype=None)},
   {"id": "r_profit", "type": "apply", "skill": SKILL, "step": number_question(
     "r_profit",
     T("A notebook is bought for Rs 80 and sold for Rs 95. What is the profit, in rupees?", "ایک کاپی 80 روپے میں خریدی اور 95 روپے میں بیچی گئی۔ کتنے روپے نفع ہوا؟"),
     R2,
     T("SP − CP.", "قیمتِ فروخت − قیمتِ خرید"),
     T("Right! Rs 15.", "درست! 15 روپے"),
     T("95 − 80 = 15.", "95 − 80 = 15"),
     common_wrong=[wrong(95, "Rs 95 is the selling price. Profit: 95 − 80 = 15.", "95 روپے قیمتِ فروخت ہے۔ نفع: 95 − 80 = 15", "sp_as_profit")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Profit and Loss unit. No textbook text or exercises were used.",
   "Contexts are local trade: a fruit seller, a goat, a dupatta, a mango dozen.",
   "Urdu terms to check: قیمتِ خرید (cost price), قیمتِ فروخت (selling price), نفع (profit), نقصان (loss).",
   "The numbers were worked out in content/sources/g6-maths-12/profit_and_loss.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

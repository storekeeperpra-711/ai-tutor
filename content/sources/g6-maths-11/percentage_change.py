from common import (T, opt, say, wrong, number_question, write, percent_of,
                    as_percent, REVIEW, PC_OF_AMOUNT, PC_FIND)

SKILL = "maths.percent.change"
BOOK = "PCTB Mathematics 6 (SNC 2022), Sub-domain 4: Rate, Ratio and Percentage"


def increase(amount, p):
    return amount + percent_of(p, amount)


def decrease(amount, p):
    return amount - percent_of(p, amount)


def change(old, new):
    """Percentage increase (or decrease) from old to new."""
    return as_percent(abs(new - old), old)


# s2: 20% of 450
S2 = percent_of(20, 450)
assert S2 == 90
# s4: Rs 800 up 10% (just the increase: 80; adding 10: 810)
S4 = increase(800, 10)
assert S4 == 880 and percent_of(10, 800) == 80
# s5: Rs 1,200 with 25% off (the discount: 300; increased: 1,500)
S5 = decrease(1200, 25)
assert S5 == 900 and increase(1200, 25) == 1500
# s6: 500 to 550 students (dividing by 550 is not 10%)
assert change(500, 550) == 10 and as_percent(50, 550) != 10
# s7: fare Rs 40 to Rs 50 (dividing by the new fare: 20)
S7 = change(40, 50)
assert S7 == 25 and as_percent(10, 50) == 20
# s8: bag 25 kg to 20 kg (dividing by the new weight: 25)
S8 = change(25, 20)
assert S8 == 20 and as_percent(5, 20) == 25
# s9: 200 to 250 is 25%, not 50/250 = 20%
assert change(200, 250) == 25 and as_percent(50, 250) == 20
# s10: Rs 1,000 up 10% then down 10% is Rs 990
assert decrease(increase(1000, 10), 10) == 990
# s11: village of 2,000 grows by 15%
S11 = increase(2000, 15)
assert S11 == 2300
# question bank: Rs 600 down 5%; 20% off Rs 500
QB = decrease(600, 5)
assert QB == 570 and percent_of(5, 600) == 30
assert decrease(500, 20) == 400
# review: Rs 250 up 20%; 80 down to 60
R1 = increase(250, 20)
assert R1 == 300
R2 = change(80, 60)
assert R2 == 25

lesson = {
 "id": "g6-maths-11-percentage-change",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Increase or decrease an amount by a percentage, and find a percentage increase or decrease.", "textbook": f"{BOOK}, 4.3 Percentage (increase and decrease)"}],
 "skills": [SKILL],
 "title": T("Percentage increase and decrease", "فیصد اضافہ اور کمی"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": PC_OF_AMOUNT}, {"skill": PC_FIND}],
 "misconceptions": [
   {"id": "change_only", "description": "Gives only the increase or decrease, not the new amount."},
   {"id": "adds_the_number", "description": "Adds or subtracts the percentage number itself (800 + 10) instead of that percent of the amount."},
   {"id": "new_as_base", "description": "Divides the change by the new amount instead of the original amount."},
   {"id": "difference_as_percent", "description": "Gives the difference (Rs 10) as the percentage."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("Percentage increase = …", "فیصد اضافہ = …"),
     "options": [
       opt("original", "increase ÷ original amount × 100", "اضافہ ÷ اصل مقدار × 100", True,
           "Yes! Always compare with where you started.", "جی ہاں! ہمیشہ شروع کی مقدار سے موازنہ کریں۔"),
       opt("new", "increase ÷ new amount × 100", "اضافہ ÷ نئی مقدار × 100", False,
           "Divide by the ORIGINAL amount, not the new one.", "اصل مقدار سے تقسیم کریں، نئی سے نہیں۔", "new_as_base"),
       opt("difference", "new amount − original amount", "نئی مقدار − اصل مقدار", False,
           "That is the increase in rupees. Divide by the original and × 100 for the percent.", "یہ روپوں میں اضافہ ہے۔ فیصد کے لیے اصل سے تقسیم کریں اور 100 سے ضرب۔", "difference_as_percent"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A water bill of Rs 600 goes down by 5%. What is the new bill?", "600 روپے کا پانی کا بل 5% کم ہو جاتا ہے۔ نیا بل کتنا ہے؟"),
     QB,
     T("5% of 600 is 30. Take it away.", "600 کا 5% = 30۔ اسے تفریق کریں۔"),
     T("Right! 600 − 30 = Rs 570.", "درست! 600 − 30 = 570 روپے"),
     T("5% of 600 = 30, and 600 − 30 = 570.", "600 کا 5% = 30، اور 600 − 30 = 570"),
     common_wrong=[wrong(30, "30 is the decrease. The new bill is 600 − 30 = 570.", "30 کمی ہے۔ نیا بل 600 − 30 = 570", "change_only"),
                   wrong(595, "Take away 5% of 600 (30), not 5: 570.", "5 نہیں، 600 کا 5% (30) تفریق کریں: 570", "adds_the_number")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A bag costs Rs 500. In a sale it has 20% off. Ayesha says the sale price is Rs 480. What is wrong?", "ایک بستہ 500 روپے کا ہے۔ سیل میں 20% رعایت ہے۔ عائشہ کہتی ہے سیل کی قیمت 480 روپے ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("percent_of", "20% of 500 is 100, not 20: the price is 500 − 100 = Rs 400.", "500 کا 20% = 100، 20 نہیں: قیمت 500 − 100 = 400 روپے", True,
           "Yes! Find 20% of the price first.", "جی ہاں! پہلے قیمت کا 20% نکالیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "She took away 20 rupees, not 20%. 20% of 500 = 100: Rs 400.", "اس نے 20 روپے تفریق کیے، 20% نہیں۔ 500 کا 20% = 100: 400 روپے", "adds_the_number"),
       opt("add", "She should add: Rs 520.", "اسے جمع کرنا چاہیے: 520 روپے", False,
           "A sale makes the price go down: 500 − 100 = 400.", "سیل میں قیمت کم ہوتی ہے: 500 − 100 = 400"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_new", "front": T("Increase Rs 800 by 10%?", "800 روپے میں 10% اضافہ؟"),
    "back": T("10% of 800 = 80, so 800 + 80 = Rs 880.", "800 کا 10% = 80، تو 800 + 80 = 880 روپے")},
   {"id": "f_change", "front": T("Percentage change?", "فیصد تبدیلی؟"),
    "back": T("change ÷ ORIGINAL amount × 100.", "تبدیلی ÷ اصل مقدار × 100")},
 ],
 "home_tasks": [{"id": "h_prices", "text": T(
   "Ask someone at home what a litre of milk cost last year and what it costs now. Work out the percentage increase.",
   "گھر میں کسی سے پوچھیں کہ پچھلے سال ایک لیٹر دودھ کتنے کا تھا اور اب کتنے کا ہے۔ فیصد اضافہ نکالیں۔")}],
 "glossary": [T("Increase", "اضافہ"), T("Decrease", "کمی"), T("Original amount", "اصل مقدار"), T("Discount", "رعایت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Prices go up, sales bring them down. How do shopkeepers work out 10% more or 25% off?",
                     "قیمتیں بڑھتی ہیں، سیل انہیں کم کرتی ہے۔ دکاندار 10% زیادہ یا 25% رعایت کیسے نکالتے ہیں؟"),
    "text": T("Today we increase and decrease amounts by a percentage, and find the percentage change. First, a percentage of an amount.", "آج ہم مقداروں میں فیصد اضافہ اور کمی کریں گے، اور فیصد تبدیلی نکالیں گے۔ پہلے کسی مقدار کا فیصد۔")},
   number_question(
     "s2_foundation",
     T("What is 20% of 450?", "450 کا 20% کتنا ہے؟"),
     S2,
     T("10% of 450 is 45. Double it.", "450 کا 10% = 45۔ اسے دگنا کریں۔"),
     T("Right! 90.", "درست! 90"),
     T("10% of 450 = 45, so 20% = 90.", "450 کا 10% = 45، تو 20% = 90"),
     common_wrong=[wrong(45, "45 is 10%. 20% is double: 90.", "45 تو 10% ہے۔ 20% اس کا دگنا: 90")],
     qtype="recall", skill=PC_OF_AMOUNT),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Find the percent of the amount, then add it or take it away. Always start from the original!", "مقدار کا فیصد نکالیں، پھر جمع یا تفریق کریں۔ ہمیشہ اصل مقدار سے شروع کریں!"),
    "text": T("To increase Rs 800 by 10%: 10% of 800 = 80, so the new price is 800 + 80 = Rs 880. To decrease, take it away instead. To find the percentage change: change ÷ original amount × 100. A fare goes from Rs 40 to Rs 50: the change is 10, and 10 ÷ 40 × 100 = 25%. Always divide by the ORIGINAL amount.",
              "800 روپے میں 10% اضافہ: 800 کا 10% = 80، تو نئی قیمت 800 + 80 = 880 روپے۔ کمی کے لیے اسے تفریق کریں۔ فیصد تبدیلی نکالنے کے لیے: تبدیلی ÷ اصل مقدار × 100۔ کرایہ 40 سے 50 روپے ہو جاتا ہے: تبدیلی 10 ہے، اور 10 ÷ 40 × 100 = 25%۔ ہمیشہ اصل مقدار سے تقسیم کریں۔")},
   number_question(
     "s4_increase",
     T("A school bag costs Rs 800. The price goes up by 10%. What is the new price?", "ایک اسکول بیگ 800 روپے کا ہے۔ قیمت 10% بڑھ جاتی ہے۔ نئی قیمت کیا ہے؟"),
     S4,
     T("10% of 800, then add it on.", "800 کا 10%، پھر جمع کریں۔"),
     T("Right! 800 + 80 = Rs 880.", "درست! 800 + 80 = 880 روپے"),
     T("10% of 800 = 80, so 800 + 80 = 880.", "800 کا 10% = 80، تو 800 + 80 = 880"),
     common_wrong=[wrong(80, "80 is the increase. Add it: 800 + 80 = 880.", "80 اضافہ ہے۔ اسے جمع کریں: 800 + 80 = 880", "change_only"),
                   wrong(810, "Add 10% of 800 (80), not 10: 880.", "10 نہیں، 800 کا 10% (80) جمع کریں: 880", "adds_the_number")]),
   number_question(
     "s5_sale",
     T("A shirt costs Rs 1,200. In a sale it has 25% off. What is the sale price?", "ایک قمیض 1,200 روپے کی ہے۔ سیل میں 25% رعایت ہے۔ سیل کی قیمت کیا ہے؟"),
     S5,
     T("25% is a quarter. Take a quarter of 1,200 away.", "25% یعنی چوتھائی۔ 1,200 کا چوتھائی تفریق کریں۔"),
     T("Right! 1,200 − 300 = Rs 900.", "درست! 1,200 − 300 = 900 روپے"),
     T("25% of 1,200 = 300, so 1,200 − 300 = 900.", "1,200 کا 25% = 300، تو 1,200 − 300 = 900"),
     common_wrong=[wrong(300, "300 is the discount. The price is 1,200 − 300 = 900.", "300 رعایت ہے۔ قیمت 1,200 − 300 = 900", "change_only"),
                   wrong(1500, "'Off' means the price goes down: 1,200 − 300 = 900.", "'رعایت' یعنی قیمت کم ہوتی ہے: 1,200 − 300 = 900")]),
   {"id": "s6_students", "type": "choice",
    "prompt": T("A school had 500 students. Now it has 550. What is the percentage increase?", "ایک اسکول میں 500 طلبہ تھے۔ اب 550 ہیں۔ فیصد اضافہ کتنا ہے؟"),
    "options": [
      opt("ten", "10%", "10%", True, "Yes! 50 ÷ 500 × 100 = 10%.", "جی ہاں! 50 ÷ 500 × 100 = 10%"),
      opt("fifty", "50%", "50%", False, "50 is the number of new students. 50 ÷ 500 × 100 = 10%.", "50 نئے طلبہ کی تعداد ہے۔ 50 ÷ 500 × 100 = 10%", "difference_as_percent"),
      opt("nine", "about 9%", "تقریباً 9%", False, "Divide by the original 500, not 550: 10%.", "اصل 500 سے تقسیم کریں، 550 سے نہیں: 10%", "new_as_base"),
    ]},
   number_question(
     "s7_fare",
     T("A bus fare goes up from Rs 40 to Rs 50. What is the percentage increase? Type the number.", "بس کا کرایہ 40 سے 50 روپے ہو جاتا ہے۔ فیصد اضافہ کتنا ہے؟ عدد لکھیں۔"),
     S7,
     T("The increase is 10. Divide by the original 40, then × 100.", "اضافہ 10 ہے۔ اصل 40 سے تقسیم کریں، پھر × 100"),
     T("Right! 10 ÷ 40 × 100 = 25%.", "درست! 10 ÷ 40 × 100 = 25%"),
     T("Change 10, original 40: 10 ÷ 40 × 100 = 25.", "تبدیلی 10، اصل 40: 10 ÷ 40 × 100 = 25"),
     common_wrong=[wrong(20, "Divide by the original fare (40), not the new one: 25%.", "پرانے کرائے (40) سے تقسیم کریں، نئے سے نہیں: 25%", "new_as_base"),
                   wrong(10, "Rs 10 is the increase. As a percent: 10 ÷ 40 × 100 = 25.", "10 روپے اضافہ ہے۔ فیصد میں: 10 ÷ 40 × 100 = 25", "difference_as_percent")]),
   number_question(
     "s8_decrease",
     T("A sack of flour weighed 25 kg. After some was used, it weighs 20 kg. What is the percentage decrease?", "آٹے کی بوری 25 کلو کی تھی۔ کچھ استعمال کے بعد 20 کلو کی ہے۔ فیصد کمی کتنی ہے؟"),
     S8,
     T("The decrease is 5 kg. Divide by the original 25.", "کمی 5 کلو ہے۔ اصل 25 سے تقسیم کریں۔"),
     T("Right! 5 ÷ 25 × 100 = 20%.", "درست! 5 ÷ 25 × 100 = 20%"),
     T("Change 5, original 25: 5 ÷ 25 × 100 = 20.", "تبدیلی 5، اصل 25: 5 ÷ 25 × 100 = 20"),
     common_wrong=[wrong(25, "Divide by the original 25 kg, not 20: 20%.", "اصل 25 کلو سے تقسیم کریں، 20 سے نہیں: 20%", "new_as_base"),
                   wrong(5, "5 kg is the decrease. As a percent: 5 ÷ 25 × 100 = 20.", "5 کلو کمی ہے۔ فیصد میں: 5 ÷ 25 × 100 = 20", "difference_as_percent")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("A price goes from Rs 200 to Rs 250. Bilal writes 50 ÷ 250 × 100 = 20% increase. What is wrong?", "قیمت 200 سے 250 روپے ہو جاتی ہے۔ بلال لکھتا ہے 50 ÷ 250 × 100 = 20% اضافہ۔ کیا غلطی ہے؟"),
    "options": [
      opt("original", "Divide by the original Rs 200: 50 ÷ 200 × 100 = 25%.", "اصل 200 روپے سے تقسیم کریں: 50 ÷ 200 × 100 = 25%", True,
          "Yes! The change is compared with where it started.", "جی ہاں! تبدیلی کا موازنہ شروع کی مقدار سے ہوتا ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "250 is the new price. Use the original 200: 25%.", "250 نئی قیمت ہے۔ اصل 200 لیں: 25%", "new_as_base"),
      opt("fifty", "The answer is 50%.", "جواب 50% ہے۔", False,
          "Rs 50 is the change, not the percent: 50 ÷ 200 × 100 = 25%.", "50 روپے تبدیلی ہے، فیصد نہیں: 50 ÷ 200 × 100 = 25%", "difference_as_percent"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Up 10%, then down 10%. Surely we're back where we started? Can you check for me?",
                     "10% اوپر، پھر 10% نیچے۔ یقیناً ہم وہیں واپس آ گئے؟ کیا آپ جانچ سکتے ہیں؟"),
    "task": T("A price of Rs 1,000 goes up by 10%, then the new price goes down by 10%. Is it back to Rs 1,000? Explain.", "1,000 روپے کی قیمت 10% بڑھتی ہے، پھر نئی قیمت 10% کم ہوتی ہے۔ کیا یہ واپس 1,000 روپے ہو گئی؟ وضاحت کریں۔"),
    "key_idea": "Up 10%: 1,000 + 100 = 1,100. Down 10% of 1,100 is 110, so 1,100 − 110 = 990. It is not back to 1,000, because the second 10% is of a bigger amount.",
    "levels": {
      "got_it": "Works out 1,100, then 1,100 − 110 = 990, and says the second 10% is of the bigger amount (1,100).",
      "partly": "Says 'no' with 1,100 but not the second step, or gets 990 without a reason.",
      "not_yet": "Says it is back to 1,000, or gives no reason."},
    "keywords": [
      ["1100", "1,100"],
      ["110"],
      ["990"],
      ["bigger", "more", "new", "زیادہ", "نئی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 990, because the second 10% is of 1,100.", "بہت خوب! 990، کیونکہ دوسرا 10%، 1,100 کا ہے۔"),
      "partly": T("Good start! Now find 10% of 1,100 and take it away.", "اچھی شروعات! اب 1,100 کا 10% نکالیں اور تفریق کریں۔"),
      "not_yet": T("Work it out: 10% of 1,000 first. Then 10% of the new price.", "حساب کریں: پہلے 1,000 کا 10%۔ پھر نئی قیمت کا 10%۔")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_village",
     T("A village has 2,000 people. Its population increases by 15%. How many people live there now?", "ایک گاؤں میں 2,000 لوگ ہیں۔ آبادی 15% بڑھ جاتی ہے۔ اب وہاں کتنے لوگ رہتے ہیں؟"),
     S11,
     T("15% of 2,000 = 10% + 5% = 200 + 100.", "2,000 کا 15% = 10% + 5% = 200 + 100"),
     T("Right! 2,000 + 300 = 2,300.", "درست! 2,000 + 300 = 2,300"),
     T("15% of 2,000 = 300, so 2,000 + 300 = 2,300.", "2,000 کا 15% = 300، تو 2,000 + 300 = 2,300"),
     common_wrong=[wrong(300, "300 is the increase. Add it: 2,300.", "300 اضافہ ہے۔ اسے جمع کریں: 2,300", "change_only"),
                   wrong(2015, "Add 15% of 2,000 (300), not 15: 2,300.", "15 نہیں، 2,000 کا 15% (300) جمع کریں: 2,300", "adds_the_number")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Percent of the amount, then add or take away. And compare with the original!", "مقدار کا فیصد، پھر جمع یا تفریق۔ اور اصل سے موازنہ کریں!"),
    "text": T("To increase or decrease by a percentage, find that percentage of the amount, then add it or take it away. To find a percentage change, divide the change by the ORIGINAL amount and multiply by 100.",
              "فیصد اضافہ یا کمی کے لیے مقدار کا وہ فیصد نکالیں، پھر جمع یا تفریق کریں۔ فیصد تبدیلی کے لیے تبدیلی کو اصل مقدار سے تقسیم کریں اور 100 سے ضرب دیں۔"),
    "points": [T("New amount = original ± percent of it.", "نئی مقدار = اصل ± اس کا فیصد"),
               T("% change = change ÷ original × 100", "فیصد تبدیلی = تبدیلی ÷ اصل × 100")]},
 ],
 "review_questions": [
   {"id": "r_increase", "type": "apply", "skill": SKILL, "step": number_question(
     "r_increase",
     T("Increase Rs 250 by 20%.", "250 روپے میں 20% اضافہ کریں۔"),
     R1,
     T("20% of 250 is 50.", "250 کا 20% = 50"),
     T("Right! 250 + 50 = Rs 300.", "درست! 250 + 50 = 300 روپے"),
     T("20% of 250 = 50, so 250 + 50 = 300.", "250 کا 20% = 50، تو 250 + 50 = 300"),
     common_wrong=[wrong(50, "50 is the increase. Add it: 300.", "50 اضافہ ہے۔ اسے جمع کریں: 300", "change_only")],
     qtype=None)},
   {"id": "r_change", "type": "apply", "skill": SKILL, "step": number_question(
     "r_change",
     T("The number of mangoes on a tree goes from 80 to 60. What is the percentage decrease?", "ایک درخت پر آموں کی تعداد 80 سے 60 ہو جاتی ہے۔ فیصد کمی کتنی ہے؟"),
     R2,
     T("The decrease is 20. Divide by the original 80.", "کمی 20 ہے۔ اصل 80 سے تقسیم کریں۔"),
     T("Right! 20 ÷ 80 × 100 = 25%.", "درست! 20 ÷ 80 × 100 = 25%"),
     T("Change 20, original 80: 20 ÷ 80 × 100 = 25.", "تبدیلی 20، اصل 80: 20 ÷ 80 × 100 = 25"),
     common_wrong=[wrong(20, "20 is the decrease in mangoes. As a percent: 20 ÷ 80 × 100 = 25.", "20 آموں میں کمی ہے۔ فیصد میں: 20 ÷ 80 × 100 = 25", "difference_as_percent")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh after matching the app with PCTB Mathematics 6 (Sub-domain 4, percentage increase and decrease). No textbook text or exercises were used.",
   "Every answer is a whole number, so the percent sign is not typed.",
   "Urdu terms to check: فیصد اضافہ (percentage increase), فیصد کمی (percentage decrease), اصل مقدار (original amount), رعایت (discount).",
   "The numbers were worked out in content/sources/g6-maths-11/percentage_change.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

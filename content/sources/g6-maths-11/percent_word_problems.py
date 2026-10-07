from common import (D, T, opt, say, wrong, number_question, write,
                    REF, REVIEW, PC_MEANING, PC_CONVERT, PC_OF_AMOUNT, PC_FIND, PC_WORD_PROBLEMS,
                    percent_of, as_percent)

SKILL = PC_WORD_PROBLEMS

# s2: 10% of 250
S2 = percent_of(10, 250)
assert S2 == 25
# s4: Rs 800 shirt, 25% off -> sale price
S4 = 800 - percent_of(25, 800)
assert S4 == 600 and S4 == percent_of(75, 800)
# s5: Rs 200 pocket money rises by 10%
S5 = 200 + percent_of(10, 200)
assert S5 == 220
# s6: 600 children, 45% girls -> boys
S6 = 600 - percent_of(45, 600)
assert S6 == 330
# s7: Rs 400 down to Rs 340 -> percent off
S7 = as_percent(400 - 340, 400)
assert S7 == 15
# s8: saves 20% of Rs 1500 -> spends
S8 = 1500 - percent_of(20, 1500)
assert S8 == 1200
# s9: Rs 1000 shoes, 10% off -> pays 900, not 100
assert 1000 - percent_of(10, 1000) == 900
# unit test
U1 = 100 - 35
assert U1 == 65
U2 = D("0.08") * 100
assert U2 == 8
U3 = percent_of(30, 90)
assert U3 == 27
U4 = as_percent(21, 30)
assert U4 == 70
U5 = 250 - percent_of(20, 250)
assert U5 == 200
# question bank and review
QB = 300 - percent_of(10, 300)
assert QB == 270
R1 = 50 + percent_of(20, 50)
assert R1 == 60
R2 = as_percent(500 - 450, 500)
assert R2 == 10

lesson = {
 "id": "g6-maths-11-percent-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems with percentages: discounts, increases, savings and parts of a group.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Percentage word problems", "فیصد کے عملی سوال"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": PC_OF_AMOUNT}, {"skill": PC_FIND}, {"skill": PC_CONVERT}, {"skill": PC_MEANING}],
 "misconceptions": [
   {"id": "discount_as_price", "description": "Gives the discount (the money saved) when the question asks for the new price."},
   {"id": "percent_not_amount", "description": "Adds or takes away the percent number itself (Rs 200 + 10 instead of Rs 200 + 10% of 200)."},
   {"id": "wrong_group", "description": "Answers for the group named in the percent instead of the other group asked about."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_sale", "type": "recall", "step": {
     "id": "qb_sale", "type": "choice",
     "prompt": T("A shop gives 25% off. What fraction of the old price do you pay?", "دکان 25% رعایت دیتی ہے۔ آپ پرانی قیمت کا کتنا حصہ دیتے ہیں؟"),
     "options": [
       opt("75", "75%, three quarters", "75%، تین چوتھائی", True,
           "Yes! 100% − 25% = 75%.", "جی ہاں! 100% − 25% = 75%"),
       opt("25", "25%, one quarter", "25%، ایک چوتھائی", False,
           "25% is what you save. You pay the rest: 75%.", "25% آپ بچاتے ہیں۔ باقی آپ دیتے ہیں: 75%", "discount_as_price"),
       opt("all", "All of it", "ساری", False,
           "You get 25% off, so you pay 75%.", "آپ کو 25% رعایت ملتی ہے، تو آپ 75% دیتے ہیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A cricket ball costs Rs 300. It is sold at 10% off. What is the sale price, in rupees?", "کرکٹ بال 300 روپے کی ہے۔ یہ 10% رعایت پر بکتی ہے۔ سیل کی قیمت کتنے روپے ہے؟"),
     QB,
     T("10% of 300 is 30. Take it off.", "300 کا 10% یعنی 30۔ اسے کم کریں۔"),
     T("Right! Rs 270.", "درست! 270 روپے"),
     T("300 − 30 = 270.", "300 − 30 = 270"),
     common_wrong=[wrong(30, "Rs 30 is the discount. The sale price is 300 − 30 = 270.", "30 روپے رعایت ہے۔ سیل کی قیمت 300 − 30 = 270 ہے۔", "discount_as_price"),
                   wrong(290, "Take off 10% of 300 (Rs 30), not Rs 10: 270.", "300 کا 10% (30 روپے) کم کریں، 10 روپے نہیں: 270", "percent_not_amount")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A bag of rice weighed 50 kg. Its weight grows by 20%. Faisal says it now weighs 70 kg. What went wrong?", "چاول کی بوری 50 کلو تھی۔ اس کا وزن 20% بڑھتا ہے۔ فیصل کہتا ہے اب یہ 70 کلو ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("amount", "He added 20 kg. 20% of 50 is 10 kg, so it is 60 kg.", "اس نے 20 کلو جمع کیا۔ 50 کا 20% یعنی 10 کلو، تو یہ 60 کلو ہے۔", True,
           "Yes! Work out the percent of the amount first.", "جی ہاں! پہلے مقدار کا فیصد نکالیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "20% of 50 kg is 10 kg, not 20 kg. 50 + 10 = 60 kg.", "50 کلو کا 20% یعنی 10 کلو، 20 کلو نہیں۔ 50 + 10 = 60 کلو", "percent_not_amount"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_discount", "front": T("Sale price?", "سیل کی قیمت؟"),
    "back": T("Old price − discount. 25% off Rs 800: 800 − 200 = Rs 600.", "پرانی قیمت − رعایت۔ 800 پر 25% رعایت: 800 − 200 = 600 روپے")},
   {"id": "f_increase", "front": T("After an increase?", "اضافے کے بعد؟"),
    "back": T("Old amount + increase. Rs 200 up 10%: 200 + 20 = Rs 220.", "پرانی مقدار + اضافہ۔ 200 روپے میں 10% اضافہ: 200 + 20 = 220 روپے")},
 ],
 "home_tasks": [{"id": "h_shop", "text": T(
   "Imagine a sale at a shop near you: everything is 20% off. Choose three things your family buys and work out the sale price of each. How much would the family save altogether?",
   "سوچیں کہ قریب کی دکان پر سیل ہے: ہر چیز پر 20% رعایت۔ تین چیزیں چنیں جو آپ کا گھرانہ خریدتا ہے اور ہر ایک کی سیل کی قیمت نکالیں۔ گھرانہ کل کتنے پیسے بچائے گا؟")}],
 "glossary": [T("Discount", "رعایت"), T("Sale price", "سیل کی قیمت"), T("Increase", "اضافہ"), T("Save", "بچانا")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Eid sale! A shirt costs Rs 800 with 25% off. How much do we actually pay?",
                     "عید سیل! ایک قمیض 800 روپے کی ہے، 25% رعایت کے ساتھ۔ ہم اصل میں کتنے دیں گے؟"),
    "text": T("Today we use percents to solve real problems. First, a quick check.", "آج ہم فیصد سے اصل زندگی کے سوال حل کریں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("What is 10% of 250?", "250 کا 10% کیا ہے؟"),
     S2,
     T("Divide by 10.", "10 سے تقسیم کریں۔"),
     T("Right! 25.", "درست! 25"),
     T("250 ÷ 10 = 25.", "250 ÷ 10 = 25"),
     common_wrong=[wrong(240, "10% is a tenth, not 10 less: 25.", "10% دسواں حصہ ہے، 10 کم نہیں: 25")],
     qtype="recall", skill=PC_OF_AMOUNT),
   {"id": "s3_steps", "type": "explain",
    "character": say("thinking", "Read the question twice. Does it want the money saved, or the new price?", "سوال دو بار پڑھیں۔ کیا بچت پوچھی ہے، یا نئی قیمت؟"),
    "text": T("Most percent problems need two steps. 1) Find the percent of the amount (25% of 800 = 200). 2) Decide what to do with it: take it away for a discount (800 − 200 = 600), add it for an increase. To find what percent something changed by, use change ÷ old amount × 100. Always check what the question asks for.",
              "زیادہ تر فیصد کے سوالوں میں دو قدم ہوتے ہیں۔ 1) مقدار کا فیصد نکالیں (800 کا 25% = 200)۔ 2) فیصلہ کریں کہ اس کا کیا کرنا ہے: رعایت ہو تو نفی کریں (800 − 200 = 600)، اضافہ ہو تو جمع کریں۔ یہ معلوم کرنے کے لیے کہ کتنے فیصد تبدیلی ہوئی: تبدیلی ÷ پرانی مقدار × 100۔ ہمیشہ دیکھیں سوال کیا پوچھ رہا ہے۔")},
   number_question(
     "s4_shirt",
     T("A shirt costs Rs 800. In the Eid sale it is 25% off. What is the sale price, in rupees?", "ایک قمیض 800 روپے کی ہے۔ عید سیل میں اس پر 25% رعایت ہے۔ سیل کی قیمت کتنے روپے ہے؟"),
     S4,
     T("25% of 800 is a quarter: 200. Take it off.", "800 کا 25% یعنی چوتھائی: 200۔ اسے کم کریں۔"),
     T("Right! Rs 600.", "درست! 600 روپے"),
     T("800 − 200 = 600.", "800 − 200 = 600"),
     common_wrong=[wrong(200, "Rs 200 is the discount. The sale price is 800 − 200 = 600.", "200 روپے رعایت ہے۔ سیل کی قیمت 800 − 200 = 600 ہے۔", "discount_as_price"),
                   wrong(775, "Take off 25% of 800 (Rs 200), not Rs 25: 600.", "800 کا 25% (200 روپے) کم کریں، 25 روپے نہیں: 600", "percent_not_amount")]),
   number_question(
     "s5_pocket",
     T("Hira's weekly pocket money is Rs 200. It goes up by 10%. What is her new pocket money, in rupees?", "حرا کا ہفتہ وار جیب خرچ 200 روپے ہے۔ اس میں 10% اضافہ ہوتا ہے۔ نیا جیب خرچ کتنے روپے ہے؟"),
     S5,
     T("10% of 200 is 20. Add it on.", "200 کا 10% یعنی 20۔ اسے جمع کریں۔"),
     T("Right! Rs 220.", "درست! 220 روپے"),
     T("200 + 20 = 220.", "200 + 20 = 220"),
     common_wrong=[wrong(210, "Add 10% of 200 (Rs 20), not Rs 10: 220.", "200 کا 10% (20 روپے) جمع کریں، 10 روپے نہیں: 220", "percent_not_amount"),
                   wrong(20, "Rs 20 is the increase. New amount: 200 + 20 = 220.", "20 روپے اضافہ ہے۔ نئی رقم: 200 + 20 = 220")]),
   number_question(
     "s6_boys",
     T("A school has 600 children. 45% are girls. How many boys are there?", "ایک اسکول میں 600 بچے ہیں۔ 45% لڑکیاں ہیں۔ لڑکے کتنے ہیں؟"),
     S6,
     T("Boys are 100% − 45% = 55%. Or find the girls first and take them away.", "لڑکے 100% − 45% = 55% ہیں۔ یا پہلے لڑکیاں نکالیں اور نفی کریں۔"),
     T("Right! 330 boys.", "درست! 330 لڑکے"),
     T("Girls: 45% of 600 = 270. Boys: 600 − 270 = 330.", "لڑکیاں: 600 کا 45% = 270۔ لڑکے: 600 − 270 = 330"),
     common_wrong=[wrong(270, "270 are girls. Boys: 600 − 270 = 330.", "270 لڑکیاں ہیں۔ لڑکے: 600 − 270 = 330", "wrong_group"),
                   wrong(55, "55% are boys. 55% of 600 is 330.", "55% لڑکے ہیں۔ 600 کا 55% یعنی 330")]),
   number_question(
     "s7_percent_off",
     T("A fan's price drops from Rs 400 to Rs 340. What percent discount is that? Type just the number.", "پنکھے کی قیمت 400 روپے سے کم ہو کر 340 روپے ہو جاتی ہے۔ یہ کتنے فیصد رعایت ہے؟ صرف عدد لکھیں۔"),
     S7,
     T("The drop is Rs 60. What percent is 60 of 400?", "کمی 60 روپے ہے۔ 60، 400 کا کتنے فیصد ہے؟"),
     T("Right! 15% off.", "درست! 15% رعایت"),
     T("60 ÷ 400 × 100 = 15.", "60 ÷ 400 × 100 = 15"),
     common_wrong=[wrong(60, "Rs 60 is the drop in rupees. As a percent: 60 ÷ 400 × 100 = 15%.", "60 روپے کمی ہے۔ فیصد میں: 60 ÷ 400 × 100 = 15%"),
                   wrong(85, "85% is what you still pay. The discount is 15%.", "85% آپ اب بھی دیتے ہیں۔ رعایت 15% ہے۔", "discount_as_price")]),
   number_question(
     "s8_spend",
     T("Ali earns Rs 1500 from a holiday job. He saves 20% and spends the rest. How many rupees does he spend?", "علی چھٹیوں کے کام سے 1500 روپے کماتا ہے۔ وہ 20% بچاتا ہے اور باقی خرچ کرتا ہے۔ وہ کتنے روپے خرچ کرتا ہے؟"),
     S8,
     T("20% of 1500 is 300. The rest is spent.", "1500 کا 20% یعنی 300۔ باقی خرچ ہوتا ہے۔"),
     T("Right! Rs 1200.", "درست! 1200 روپے"),
     T("1500 − 300 = 1200.", "1500 − 300 = 1200"),
     common_wrong=[wrong(300, "Rs 300 is what he saves. He spends 1500 − 300 = 1200.", "300 روپے وہ بچاتا ہے۔ وہ 1500 − 300 = 1200 خرچ کرتا ہے۔", "wrong_group")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Shoes cost Rs 1000 with 10% off. Imran says he will pay Rs 100. What went wrong?", "جوتے 1000 روپے کے ہیں، 10% رعایت کے ساتھ۔ عمران کہتا ہے وہ 100 روپے دے گا۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("discount", "Rs 100 is the discount. He pays 1000 − 100 = Rs 900.", "100 روپے رعایت ہے۔ وہ 1000 − 100 = 900 روپے دے گا۔", True,
          "Yes! With 10% off you still pay 90%.", "جی ہاں! 10% رعایت پر آپ پھر بھی 90% دیتے ہیں۔"),
      opt("ten", "He should pay Rs 990.", "اسے 990 روپے دینے چاہییں۔", False,
          "10% of 1000 is Rs 100, not Rs 10. He pays Rs 900.", "1000 کا 10% یعنی 100 روپے، 10 نہیں۔ وہ 900 روپے دے گا۔", "percent_not_amount"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Rs 100 is only the money saved. He pays Rs 900.", "100 روپے صرف بچت ہے۔ وہ 900 روپے دے گا۔", "discount_as_price"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "With 25% off, why can we find the sale price by working out 75% of the old price? Can you teach me?",
                     "25% رعایت پر، پرانی قیمت کا 75% نکال کر سیل کی قیمت کیوں مل جاتی ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the price after 25% off the same as 75% of the old price?", "اپنے الفاظ میں بتائیں: 25% رعایت کے بعد قیمت پرانی قیمت کے 75% کے برابر کیوں ہے؟"),
    "key_idea": "The old price is 100%. Taking 25% off leaves 100% − 25% = 75% of the price, so the sale price is 75% of the old price.",
    "levels": {
      "got_it": "Says the whole price is 100%, and taking away 25% leaves 75%.",
      "partly": "Says 100 − 25 = 75, without linking it to the price.",
      "not_yet": "Gives no reason, or just repeats the rule."},
    "keywords": [
      ["100", "whole", "full", "پورا", "پوری"],
      ["left", "rest", "remain", "باقی"],
      ["75", "take away", "minus", "نفی", "کم"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The full price is 100%, and 25% off leaves 75%.", "بہت خوب! پوری قیمت 100% ہے، اور 25% رعایت کے بعد 75% بچتا ہے۔"),
      "partly": T("Good start! Now say what the 100% stands for.", "اچھی شروعات! اب بتائیں 100% کس چیز کو ظاہر کرتا ہے۔"),
      "not_yet": T("The full price is 100%. If 25% is taken off, what percent of the price is left to pay?", "پوری قیمت 100% ہے۔ اگر 25% کم ہو جائے تو قیمت کا کتنے فیصد دینا باقی ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Percentages unit. You can do it!",
                     "ٹیسٹ کا وقت! فیصد کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on what a percent means, changing decimals to percents, percent of an amount, finding the percentage and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں فیصد کا مطلب، اعشاریہ کو فیصد بنانا، مقدار کا فیصد، فیصد معلوم کرنا اور ایک اصل زندگی کا سوال ہے۔ آرام سے کریں۔")},
   number_question(
     "u1_rest",
     T("Test 1: 35% of a field is planted with wheat. What percent is not planted with wheat?", "ٹیسٹ 1: ایک کھیت کے 35% میں گندم لگی ہے۔ کتنے فیصد میں گندم نہیں لگی؟"),
     U1,
     T("The whole field is 100%.", "پورا کھیت 100% ہے۔"),
     T("Right! 65%.", "درست! 65%"),
     T("100 − 35 = 65.", "100 − 35 = 65"),
     common_wrong=[wrong(35, "35% has wheat. The rest: 100 − 35 = 65%.", "35% میں گندم ہے۔ باقی: 100 − 35 = 65%")],
     qtype="recall", skill=PC_MEANING),
   number_question(
     "u2_decimal",
     T("Test 2: Write 0.08 as a percent. Type just the number.", "ٹیسٹ 2: 0.08 کو فیصد میں لکھیں۔ صرف عدد لکھیں۔"),
     U2,
     T("Multiply by 100.", "100 سے ضرب دیں۔"),
     T("Right! 0.08 = 8%.", "درست! 0.08 = 8%"),
     T("0.08 × 100 = 8.", "0.08 × 100 = 8"),
     common_wrong=[wrong(80, "0.08 is 8 hundredths: 8%. 80% would be 0.8.", "0.08 یعنی 8 سوویں: 8%۔ 80% تو 0.8 ہوتا۔")],
     qtype="apply", skill=PC_CONVERT),
   number_question(
     "u3_amount",
     T("Test 3: Find 30% of 90.", "ٹیسٹ 3: 90 کا 30% معلوم کریں۔"),
     U3,
     T("10% of 90 is 9. 30% is three times that.", "90 کا 10% یعنی 9۔ 30% اس کا تین گنا ہے۔"),
     T("Right! 27.", "درست! 27"),
     T("10% = 9, so 30% = 27.", "10% = 9، تو 30% = 27"),
     common_wrong=[wrong(30, "30 is the percent. 30% of 90 is 27.", "30 فیصد ہے۔ 90 کا 30% یعنی 27"),
                   wrong(60, "That takes away 30. 30% of 90 is 3 × 9 = 27.", "یہ 30 کی نفی ہے۔ 90 کا 30% یعنی 3 × 9 = 27")],
     qtype="apply", skill=PC_OF_AMOUNT),
   number_question(
     "u4_find",
     T("Test 4: Sana gets 21 out of 30 in a test. What percent is that? Type just the number.", "ٹیسٹ 4: ثنا ٹیسٹ میں 30 میں سے 21 لیتی ہے۔ یہ کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     U4,
     T("21/30 = 7/10 = ?/100", "21/30 = 7/10 = ?/100"),
     T("Right! 70%.", "درست! 70%"),
     T("21/30 = 7/10 = 70/100 = 70%.", "21/30 = 7/10 = 70/100 = 70%"),
     common_wrong=[wrong(21, "21 out of 30 is not 21%. 21/30 = 70%.", "30 میں سے 21، 21% نہیں ہے۔ 21/30 = 70%")],
     qtype="apply", skill=PC_FIND),
   number_question(
     "u5_sale",
     T("Test 5: A school bag costs Rs 250. It is sold at 20% off. What is the sale price, in rupees?", "ٹیسٹ 5: اسکول بیگ 250 روپے کا ہے۔ یہ 20% رعایت پر بکتا ہے۔ سیل کی قیمت کتنے روپے ہے؟"),
     U5,
     T("20% of 250 is 50. Take it off.", "250 کا 20% یعنی 50۔ اسے کم کریں۔"),
     T("Right! Rs 200.", "درست! 200 روپے"),
     T("250 − 50 = 200.", "250 − 50 = 200"),
     common_wrong=[wrong(50, "Rs 50 is the discount. Sale price: 250 − 50 = 200.", "50 روپے رعایت ہے۔ سیل کی قیمت: 250 − 50 = 200", "discount_as_price"),
                   wrong(230, "Take off 20% of 250 (Rs 50), not Rs 20: 200.", "250 کا 20% (50 روپے) کم کریں، 20 روپے نہیں: 200", "percent_not_amount")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Percentages unit complete! You're ready for any sale in the bazaar.", "فیصد کا باب مکمل! اب آپ بازار کی ہر سیل کے لیے تیار ہیں۔"),
    "text": T("Percent problems usually take two steps: find the percent of the amount, then take it away (discount, savings spent) or add it on (increase). To find a percent change: change ÷ old amount × 100. Read carefully to see whether the question wants the part, the rest or the new total.",
              "فیصد کے سوال عموماً دو قدم لیتے ہیں: مقدار کا فیصد نکالیں، پھر اسے نفی کریں (رعایت، بچت کے بعد خرچ) یا جمع کریں (اضافہ)۔ فیصد تبدیلی نکالنے کے لیے: تبدیلی ÷ پرانی مقدار × 100۔ غور سے پڑھیں کہ سوال حصہ، باقی یا نیا کل پوچھ رہا ہے۔"),
    "points": [T("Discount: take it away. Increase: add it on.", "رعایت: نفی کریں۔ اضافہ: جمع کریں۔"),
               T("Check what the question asks for.", "دیکھیں سوال کیا پوچھ رہا ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_increase", "type": "apply", "skill": SKILL, "step": number_question(
     "r_increase",
     T("A goat weighed 50 kg. Its weight goes up by 20%. What does it weigh now, in kg?", "ایک بکری کا وزن 50 کلو تھا۔ اس کا وزن 20% بڑھ جاتا ہے۔ اب اس کا وزن کتنے کلو ہے؟"),
     R1,
     T("20% of 50 is 10. Add it on.", "50 کا 20% یعنی 10۔ اسے جمع کریں۔"),
     T("Right! 60 kg.", "درست! 60 کلو"),
     T("50 + 10 = 60.", "50 + 10 = 60"),
     common_wrong=[wrong(70, "Add 20% of 50 (10 kg), not 20 kg: 60.", "50 کا 20% (10 کلو) جمع کریں، 20 کلو نہیں: 60", "percent_not_amount")],
     qtype=None)},
   {"id": "r_percent_off", "type": "apply", "skill": SKILL, "step": number_question(
     "r_percent_off",
     T("A watch's price drops from Rs 500 to Rs 450. What percent discount is that? Type just the number.", "ایک گھڑی کی قیمت 500 روپے سے کم ہو کر 450 روپے ہو جاتی ہے۔ یہ کتنے فیصد رعایت ہے؟ صرف عدد لکھیں۔"),
     R2,
     T("The drop is Rs 50. What percent is 50 of 500?", "کمی 50 روپے ہے۔ 50، 500 کا کتنے فیصد ہے؟"),
     T("Right! 10% off.", "درست! 10% رعایت"),
     T("50 ÷ 500 × 100 = 10.", "50 ÷ 500 × 100 = 10"),
     common_wrong=[wrong(50, "Rs 50 is the drop in rupees. As a percent: 10%.", "50 روپے کمی ہے۔ فیصد میں: 10%")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Percentages unit. No textbook text or exercises were used.",
   "Contexts are everyday Pakistani ones (Eid sale, pocket money, holiday job). The five-question unit test at the end covers every lesson of the unit.",
   "Urdu terms to check: رعایت (discount), اضافہ (increase), سیل کی قیمت (sale price).",
   "The numbers were worked out in content/sources/g6-maths-11/percent_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

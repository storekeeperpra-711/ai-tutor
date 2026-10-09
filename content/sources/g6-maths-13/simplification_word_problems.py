from fractions import Fraction as F

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SM_ORDER, SM_BRACKETS, SM_FRACTIONS_DECIMALS, SM_ESTIMATE, SM_WORD_PROBLEMS,
                    round_to)
from figs import (attach, step_text, op, br, steps_fig, bar_model, round_fig, figure, rect, circle, label, W)

SKILL = SM_WORD_PROBLEMS

# s2: (12 + 8) / 4
S2 = (12 + 8) // 4
assert S2 == 5
# s4: 500 - 3 x 40 (forgetting the 3 gives 460)
S4 = 500 - 3 * 40
assert S4 == 380 and 500 - 40 == 460
# s5: 4 x 12 + 6 (bracketing it as 4 x (12 + 6) gives 72)
S5 = 4 * 12 + 6
assert S5 == 54 and 4 * (12 + 6) == 72
# qb: (250 + 150) / 4
assert (250 + 150) // 4 == 100
# s6: (120 + 60) / 3 = 60; 120 + 60 / 3 = 140
assert (120 + 60) // 3 == 60 and 120 + 60 // 3 == 140
# s7: 30 x 50 - 600
S7 = 30 * 50 - 600
assert S7 == 900
# s8: 1/4 of (300 + 100) (only the 300: 75 + 100 = 175)
assert (F(1, 4) * (300 + 100)).denominator == 1
S8 = int(F(1, 4) * (300 + 100))
assert S8 == 100 and F(1, 4) * 300 + 100 == 175
# s9: 5 x 8 - 3 = 37, not 5 x (8 - 3) = 25
assert 5 * 8 - 3 == 37 and 5 * (8 - 3) == 25
# unit test
U1 = 15 - 3 * 4
assert U1 == 3 and (15 - 3) * 4 == 48
U2 = (7 + 5) * 3
assert U2 == 36 and 7 + 5 * 3 == 22
assert (F(1, 2) * (14 + 6)).denominator == 1
U3 = int(F(1, 2) * (14 + 6))
assert U3 == 10 and F(1, 2) * 14 + 6 == 13
U4 = round_to(351, 100)
assert U4 == 400
U5 = 500 - 2 * 150
assert U5 == 200 and 500 - 150 == 350
# question bank and review
QB = 6 * 7 + 5
assert QB == 47 and 6 * (7 + 5) == 72
R1 = 3 * 90 + 30
assert R1 == 300 and 3 * (90 + 30) == 360
R2 = (400 - 100) // 3
assert R2 == 100 and 400 - 100 // 3 != R2

lesson = {
 "id": "g6-maths-13-simplification-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Write a number sentence for a real-life problem, using brackets where needed, and simplify it with BODMAS.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Simplification word problems", "مختصر کرنے کے عملی سوال"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": SM_ESTIMATE}, {"skill": SM_FRACTIONS_DECIMALS}, {"skill": SM_BRACKETS}, {"skill": SM_ORDER}],
 "misconceptions": [
   {"id": "missing_brackets", "description": "Leaves out brackets when a total must be found before sharing or multiplying."},
   {"id": "extra_brackets", "description": "Adds brackets where none are needed, changing what the story means."},
   {"id": "forgets_quantity", "description": "Uses the price of one item when several were bought."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_sentence", "type": "recall", "step": {
     "id": "qb_sentence", "type": "choice",
     "prompt": T("Nida has Rs 250 and Zain has Rs 150. They put it together and share it equally among 4 friends. Which number sentence fits?", "ندا کے پاس 250 اور زین کے پاس 150 روپے ہیں۔ وہ پیسے ملا کر 4 دوستوں میں برابر بانٹتے ہیں۔ کون سا عددی جملہ درست ہے؟"),
     "options": [
       opt("brackets", "(250 + 150) ÷ 4", "(250 + 150) ÷ 4", True,
           "Yes! Find the total first, then share it: Rs 100 each.", "جی ہاں! پہلے کل نکالیں، پھر بانٹیں: ہر ایک کو 100 روپے"),
       opt("no_brackets", "250 + 150 ÷ 4", "250 + 150 ÷ 4", False,
           "Without brackets only the Rs 150 is shared. All the money is shared: (250 + 150) ÷ 4.", "قوسین کے بغیر صرف 150 روپے بٹتے ہیں۔ سارے پیسے بٹتے ہیں: (250 + 150) ÷ 4", "missing_brackets"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A hall has 6 rows of 7 chairs, and 5 more chairs at the front. How many chairs are there?", "ایک ہال میں کرسیوں کی 6 قطاریں ہیں، ہر قطار میں 7، اور آگے 5 کرسیاں مزید۔ کل کتنی کرسیاں ہیں؟"),
     QB,
     T("6 × 7 + 5.", "6 × 7 + 5"),
     T("Right! 42 + 5 = 47.", "درست! 42 + 5 = 47"),
     T("6 × 7 = 42, then 42 + 5 = 47.", "6 × 7 = 42، پھر 42 + 5 = 47"),
     common_wrong=[wrong(72, "The 5 chairs are not in every row: 6 × 7 + 5 = 47.", "5 کرسیاں ہر قطار میں نہیں ہیں: 6 × 7 + 5 = 47", "extra_brackets")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("A goat costs Rs 400 and Rs 100 was paid. The rest is paid in 3 equal parts. Amna writes 400 − 100 ÷ 3. What is wrong?", "ایک بکری 400 روپے کی ہے اور 100 روپے دے دیے گئے۔ باقی 3 برابر قسطوں میں دینے ہیں۔ آمنہ 400 − 100 ÷ 3 لکھتی ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("brackets", "It needs brackets: (400 − 100) ÷ 3 = Rs 100.", "قوسین چاہییں: (400 − 100) ÷ 3 = 100 روپے", True,
           "Yes! Find what is left first, then divide.", "جی ہاں! پہلے باقی نکالیں، پھر تقسیم کریں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Without brackets, only the 100 is divided. The rest, 300, is shared: Rs 100.", "قوسین کے بغیر صرف 100 تقسیم ہوتا ہے۔ باقی 300 بٹتا ہے: 100 روپے", "missing_brackets"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_total_first", "front": T("Total, then share?", "پہلے کل، پھر بانٹنا؟"),
    "back": T("Use brackets: (a + b) ÷ n.", "قوسین لگائیں: (a + b) ÷ n")},
   {"id": "f_steps", "front": T("Solving a word problem?", "عملی سوال حل کرنا؟"),
    "back": T("Write the number sentence, simplify with BODMAS, then estimate to check.", "عددی جملہ لکھیں، BODMAS سے مختصر کریں، پھر اندازے سے جانچیں۔")},
 ],
 "home_tasks": [{"id": "h_story", "text": T(
   "Make up your own story for (20 + 10) ÷ 5, and another for 20 + 10 ÷ 5. Tell them to someone at home and ask them which story goes with which sentence.",
   "(20 + 10) ÷ 5 کے لیے اپنی کہانی بنائیں، اور 20 + 10 ÷ 5 کے لیے ایک اور۔ گھر میں کسی کو سنائیں اور پوچھیں کون سی کہانی کس جملے کی ہے۔")}],
 "glossary": [T("Number sentence", "عددی جملہ"), T("Word problem", "عملی سوال"), T("Total", "کل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Real problems don't come with brackets. We have to decide where they go!",
                     "اصل سوالوں میں قوسین لکھی نہیں ہوتیں۔ ہمیں خود فیصلہ کرنا پڑتا ہے کہ کہاں لگانی ہیں!"),
    "text": T("Today we turn stories into number sentences. First, a quick bracket check.", "آج ہم کہانیوں کو عددی جملوں میں بدلیں گے۔ پہلے قوسین کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Simplify: (12 + 8) ÷ 4", "مختصر کریں: (12 + 8) ÷ 4"),
     S2,
     T("Brackets first: 12 + 8.", "پہلے قوسین: 12 + 8"),
     T("Right! 20 ÷ 4 = 5.", "درست! 20 ÷ 4 = 5"),
     T("12 + 8 = 20, then 20 ÷ 4 = 5.", "12 + 8 = 20، پھر 20 ÷ 4 = 5"),
     common_wrong=[wrong(14, "Brackets first: 20 ÷ 4 = 5.", "پہلے قوسین: 20 ÷ 4 = 5")],
     qtype="recall", skill=SM_BRACKETS),
   {"id": "s3_steps", "type": "explain",
    "character": say("thinking", "Ask: what must I find first? If it's a total, it goes in brackets.", "پوچھیں: پہلے کیا نکالنا ہے؟ اگر کل ہے تو وہ قوسین میں جائے گا۔"),
    "text": T("1) Read the story and write a number sentence. 2) If a total or a difference must be found before you multiply or share, put it in brackets. 3) Simplify with BODMAS. 4) Estimate to check the answer makes sense.",
              "1) کہانی پڑھیں اور عددی جملہ لکھیں۔ 2) اگر ضرب یا بانٹنے سے پہلے کل یا فرق نکالنا ہو تو اسے قوسین میں رکھیں۔ 3) BODMAS سے مختصر کریں۔ 4) اندازے سے جانچیں کہ جواب درست لگتا ہے۔")},
   number_question(
     "s4_pens",
     T("Bilal has Rs 500. He buys 3 pens at Rs 40 each. How much money is left? (500 − 3 × 40)", "بلال کے پاس 500 روپے ہیں۔ وہ 40 روپے فی قلم کے حساب سے 3 قلم خریدتا ہے۔ کتنے پیسے بچے؟ (500 − 3 × 40)"),
     S4,
     T("3 × 40 first.", "پہلے 3 × 40"),
     T("Right! 500 − 120 = Rs 380.", "درست! 500 − 120 = 380 روپے"),
     T("3 × 40 = 120, then 500 − 120 = 380.", "3 × 40 = 120، پھر 500 − 120 = 380"),
     common_wrong=[wrong(460, "He bought 3 pens, not 1: 500 − 120 = 380.", "اس نے 3 قلم خریدے، 1 نہیں: 500 − 120 = 380", "forgets_quantity")]),
   number_question(
     "s5_mangoes",
     T("There are 4 boxes with 12 mangoes in each, and 6 loose mangoes. How many mangoes are there?", "4 پیٹیاں ہیں، ہر ایک میں 12 آم، اور 6 آم الگ۔ کل کتنے آم ہیں؟"),
     S5,
     T("4 × 12 + 6.", "4 × 12 + 6"),
     T("Right! 48 + 6 = 54.", "درست! 48 + 6 = 54"),
     T("4 × 12 = 48, then 48 + 6 = 54.", "4 × 12 = 48، پھر 48 + 6 = 54"),
     common_wrong=[wrong(72, "The 6 loose mangoes are not in every box: 4 × 12 + 6 = 54.", "6 الگ آم ہر پیٹی میں نہیں ہیں: 4 × 12 + 6 = 54", "extra_brackets")]),
   {"id": "s6_sentence", "type": "choice",
    "prompt": T("Two brothers have Rs 120 and Rs 60. They share all of it equally among 3 children. Which number sentence fits?", "دو بھائیوں کے پاس 120 اور 60 روپے ہیں۔ وہ سارے پیسے 3 بچوں میں برابر بانٹتے ہیں۔ کون سا عددی جملہ درست ہے؟"),
    "options": [
      opt("brackets", "(120 + 60) ÷ 3", "(120 + 60) ÷ 3", True, "Yes! Total first: 180 ÷ 3 = Rs 60 each.", "جی ہاں! پہلے کل: 180 ÷ 3 = ہر ایک کو 60 روپے"),
      opt("no_brackets", "120 + 60 ÷ 3", "120 + 60 ÷ 3", False, "That shares only the Rs 60. All the money is shared.", "یہ صرف 60 روپے بانٹتا ہے۔ سارے پیسے بٹتے ہیں۔", "missing_brackets"),
      opt("times", "(120 + 60) × 3", "(120 + 60) × 3", False, "Sharing means dividing, not multiplying.", "بانٹنے کا مطلب تقسیم ہے، ضرب نہیں۔"),
    ]},
   number_question(
     "s7_party",
     T("30 students each give Rs 50 for a class party. Rs 600 is spent on food. How much is left? (30 × 50 − 600)", "30 طالب علم کلاس پارٹی کے لیے 50، 50 روپے دیتے ہیں۔ 600 روپے کھانے پر خرچ ہوتے ہیں۔ کتنے بچے؟ (30 × 50 − 600)"),
     S7,
     T("30 × 50 first.", "پہلے 30 × 50"),
     T("Right! 1500 − 600 = Rs 900.", "درست! 1500 − 600 = 900 روپے"),
     T("30 × 50 = 1500, then 1500 − 600 = 900.", "30 × 50 = 1500، پھر 1500 − 600 = 900"),
     common_wrong=[wrong(1500, "Rs 1500 is what was collected. Take away 600: 900.", "1500 روپے جمع ہوئے۔ 600 نفی کریں: 900")]),
   number_question(
     "s8_savings",
     T("Sana gets Rs 300 from her uncle and Rs 100 from her aunt. She saves 1/4 of all of it. How much does she save? (1/4 of (300 + 100))", "ثنا کو چچا سے 300 روپے اور خالہ سے 100 روپے ملتے ہیں۔ وہ سارے پیسوں کا 1/4 بچاتی ہے۔ وہ کتنے بچاتی ہے؟ ((300 + 100) کا 1/4)"),
     S8,
     T("Total first: 300 + 100 = 400.", "پہلے کل: 300 + 100 = 400"),
     T("Right! 1/4 of 400 = Rs 100.", "درست! 400 کا 1/4 = 100 روپے"),
     T("300 + 100 = 400, then 400 ÷ 4 = 100.", "300 + 100 = 400، پھر 400 ÷ 4 = 100"),
     common_wrong=[wrong(175, "She saves 1/4 of all the money, not just the 300: 100.", "وہ سارے پیسوں کا 1/4 بچاتی ہے، صرف 300 کا نہیں: 100", "missing_brackets")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("There are 5 packets with 8 biscuits in each. Ali eats 3 biscuits. Hamza writes 5 × (8 − 3) = 25 biscuits left. What went wrong?", "5 پیکٹ ہیں، ہر ایک میں 8 بسکٹ۔ علی 3 بسکٹ کھاتا ہے۔ حمزہ لکھتا ہے 5 × (8 − 3) = 25 بسکٹ بچے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("extra", "The brackets mean 3 eaten from every packet. It should be 5 × 8 − 3 = 37.", "قوسین کا مطلب ہے ہر پیکٹ سے 3 کھائے۔ یہ 5 × 8 − 3 = 37 ہونا چاہیے۔", True,
          "Yes! Ali ate 3 in all, not 3 from each packet.", "جی ہاں! علی نے کل 3 کھائے، ہر پیکٹ سے 3 نہیں۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Ali ate only 3 biscuits in all, so 40 − 3 = 37.", "علی نے کل صرف 3 بسکٹ کھائے، تو 40 − 3 = 37", "extra_brackets"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "How do you know when a story needs brackets? Can you teach me?",
                     "آپ کو کیسے پتا چلتا ہے کہ کہانی میں قوسین چاہییں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why does sharing Rs 120 and Rs 60 among 3 children need brackets?", "اپنے الفاظ میں بتائیں: 120 اور 60 روپے 3 بچوں میں بانٹنے کے لیے قوسین کیوں چاہییں؟"),
    "key_idea": "All the money is shared, so the total (120 + 60) must be found before dividing. Without brackets, BODMAS divides first and only the Rs 60 would be shared.",
    "levels": {
      "got_it": "Says the total must be found first because all the money is shared, and without brackets only the 60 would be divided.",
      "partly": "Says you add first, without saying what would go wrong without brackets.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["total", "all", "together", "کل", "سارے"],
      ["first", "before", "پہلے"],
      ["divide", "share", "تقسیم", "بانٹ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Brackets make sure the total is shared, not just one part.", "بہت خوب! قوسین یقینی بناتی ہیں کہ کل بٹے، صرف ایک حصہ نہیں۔"),
      "partly": T("Good start! Now say what would happen without the brackets.", "اچھی شروعات! اب بتائیں قوسین کے بغیر کیا ہوتا۔"),
      "not_yet": T("Work out 120 + 60 ÷ 3 with BODMAS. Is all the money shared?", "BODMAS سے 120 + 60 ÷ 3 حل کریں۔ کیا سارے پیسے بٹے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Simplification unit. You can do it!",
                     "ٹیسٹ کا وقت! مختصر کرنے کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on the order of operations, brackets, fractions, rounding and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں عملیات کی ترتیب، قوسین، کسور، قریب ترین عدد اور ایک اصل زندگی کا سوال ہے۔ آرام سے کریں۔")},
   number_question(
     "u1_order",
     T("Test 1: Simplify 15 − 3 × 4", "ٹیسٹ 1: 15 − 3 × 4 مختصر کریں"),
     U1,
     T("× before −.", "× پہلے، − بعد میں۔"),
     T("Right! 15 − 12 = 3.", "درست! 15 − 12 = 3"),
     T("3 × 4 = 12, then 15 − 12 = 3.", "3 × 4 = 12، پھر 15 − 12 = 3"),
     common_wrong=[wrong(48, "That subtracts first. Multiply first: 15 − 12 = 3.", "یہ پہلے تفریق ہے۔ پہلے ضرب: 15 − 12 = 3")],
     qtype="recall", skill=SM_ORDER),
   number_question(
     "u2_brackets",
     T("Test 2: Simplify (7 + 5) × 3", "ٹیسٹ 2: (7 + 5) × 3 مختصر کریں"),
     U2,
     T("Brackets first.", "پہلے قوسین۔"),
     T("Right! 12 × 3 = 36.", "درست! 12 × 3 = 36"),
     T("7 + 5 = 12, then 12 × 3 = 36.", "7 + 5 = 12، پھر 12 × 3 = 36"),
     common_wrong=[wrong(22, "That ignores the brackets: 12 × 3 = 36.", "یہ قوسین نظر انداز کرتا ہے: 12 × 3 = 36")],
     qtype="apply", skill=SM_BRACKETS),
   number_question(
     "u3_of",
     T("Test 3: Simplify 1/2 of (14 + 6)", "ٹیسٹ 3: (14 + 6) کا 1/2 مختصر کریں"),
     U3,
     T("Brackets first: 20.", "پہلے قوسین: 20"),
     T("Right! Half of 20 = 10.", "درست! 20 کا آدھا = 10"),
     T("14 + 6 = 20, then 1/2 × 20 = 10.", "14 + 6 = 20، پھر 1/2 × 20 = 10"),
     common_wrong=[wrong(13, "'Of' applies to the whole bracket: half of 20 = 10.", "'کا' پوری قوسین پر لگتا ہے: 20 کا آدھا = 10")],
     qtype="apply", skill=SM_FRACTIONS_DECIMALS),
   number_question(
     "u4_round",
     T("Test 4: Round 351 to the nearest 100.", "ٹیسٹ 4: 351 کو قریب ترین 100 تک لائیں۔"),
     U4,
     T("Look at the tens digit: 5.", "دہائی کا ہندسہ دیکھیں: 5"),
     T("Right! 400.", "درست! 400"),
     T("The tens digit is 5, so round up: 400.", "دہائی کا ہندسہ 5 ہے، تو اوپر: 400"),
     common_wrong=[wrong(300, "The tens digit is 5, so round up: 400.", "دہائی کا ہندسہ 5 ہے، تو اوپر: 400"),
                   wrong(350, "That is the nearest 10. To the nearest 100: 400.", "یہ قریب ترین 10 ہے۔ قریب ترین 100 تک: 400")],
     qtype="apply", skill=SM_ESTIMATE),
   number_question(
     "u5_apples",
     T("Test 5: Ammi buys 2 kg of apples at Rs 150 a kg and pays with a Rs 500 note. How much change does she get? (500 − 2 × 150)", "ٹیسٹ 5: امی 150 روپے فی کلو کے حساب سے 2 کلو سیب خریدتی ہیں اور 500 روپے کا نوٹ دیتی ہیں۔ انہیں کتنا بقایا ملے گا؟ (500 − 2 × 150)"),
     U5,
     T("2 × 150 first.", "پہلے 2 × 150"),
     T("Right! 500 − 300 = Rs 200.", "درست! 500 − 300 = 200 روپے"),
     T("2 × 150 = 300, then 500 − 300 = 200.", "2 × 150 = 300، پھر 500 − 300 = 200"),
     common_wrong=[wrong(350, "She bought 2 kg, not 1: 500 − 300 = 200.", "انہوں نے 2 کلو خریدے، 1 نہیں: 500 − 300 = 200", "forgets_quantity")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Simplification unit complete! You can turn any story into maths now.", "مختصر کرنے کا باب مکمل! اب آپ کسی بھی کہانی کو ریاضی میں بدل سکتے ہیں۔"),
    "text": T("Write a number sentence for the story. If a total or difference must be found first, put it in brackets. Simplify with BODMAS, then estimate to check the answer makes sense.",
              "کہانی کا عددی جملہ لکھیں۔ اگر کل یا فرق پہلے نکالنا ہو تو اسے قوسین میں رکھیں۔ BODMAS سے مختصر کریں، پھر اندازے سے جانچیں کہ جواب درست لگتا ہے۔"),
    "points": [T("Total first? Use brackets.", "پہلے کل؟ قوسین لگائیں۔"),
               T("Then BODMAS, then check.", "پھر BODMAS، پھر جانچ۔")]},
 ],
 "review_questions": [
   {"id": "r_food", "type": "apply", "skill": SKILL, "step": number_question(
     "r_food",
     T("3 friends each pay Rs 90 for food, and they pay Rs 30 in all for drinks. What do they spend altogether? (3 × 90 + 30)", "3 دوست کھانے کے لیے 90، 90 روپے دیتے ہیں، اور مشروبات کے لیے کل 30 روپے۔ وہ کل کتنا خرچ کرتے ہیں؟ (3 × 90 + 30)"),
     R1,
     T("3 × 90 first.", "پہلے 3 × 90"),
     T("Right! 270 + 30 = Rs 300.", "درست! 270 + 30 = 300 روپے"),
     T("3 × 90 = 270, then 270 + 30 = 300.", "3 × 90 = 270، پھر 270 + 30 = 300"),
     common_wrong=[wrong(360, "The Rs 30 is for all of them, not each: 270 + 30 = 300.", "30 روپے سب کے لیے ہیں، ہر ایک کے نہیں: 270 + 30 = 300", "extra_brackets")],
     qtype=None)},
   {"id": "r_rest", "type": "apply", "skill": SKILL, "step": number_question(
     "r_rest",
     T("A goat costs Rs 400. Rs 100 is paid now and the rest in 3 equal parts. How much is each part? ((400 − 100) ÷ 3)", "ایک بکری 400 روپے کی ہے۔ 100 روپے ابھی دیے جاتے ہیں اور باقی 3 برابر قسطوں میں۔ ہر قسط کتنی ہے؟ ((400 − 100) ÷ 3)"),
     R2,
     T("Brackets first: 400 − 100.", "پہلے قوسین: 400 − 100"),
     T("Right! 300 ÷ 3 = Rs 100.", "درست! 300 ÷ 3 = 100 روپے"),
     T("400 − 100 = 300, then 300 ÷ 3 = 100.", "400 − 100 = 300، پھر 300 ÷ 3 = 100"),
     common_wrong=[wrong(300, "Rs 300 is what is left. Share it in 3 parts: 100.", "300 روپے باقی ہیں۔ 3 حصوں میں بانٹیں: 100")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Simplification unit. No textbook text or exercises were used.",
   "Most practice steps show the number sentence in brackets after the story, so children practise simplifying; the choice and find-the-mistake steps practise writing the sentence.",
   "The five-question unit test at the end covers every lesson of the unit.",
   "The numbers were worked out in content/sources/g6-maths-13/simplification_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
E2 = op(br(op(12, "+", 8)), "÷", 4)
assert E2.value == S2
MONEY, PENS, PEN_PRICE = 500, 3, 40
assert MONEY - PENS * PEN_PRICE == S4
BOXES, PER_BOX, LOOSE = 4, 12, 6
assert BOXES * PER_BOX + LOOSE == S5
STUDENTS, EACH, FOOD = 30, 50, 600
assert STUDENTS * EACH - FOOD == S7
UNCLE, AUNT, SAVE = 300, 100, F(1, 4)
assert SAVE * (UNCLE + AUNT) == S8
U4_ROW = (351, 300, 400)
assert round_to(351, 100) == U4 and U4_ROW[1] < 351 < U4_ROW[2]
NOTE, KG, APPLE_PRICE = 500, 2, 150
assert NOTE - KG * APPLE_PRICE == U5
ROWS, PER_ROW, FRONT = 6, 7, 5
assert ROWS * PER_ROW + FRONT == QB
FRIENDS, FOOD_EACH, DRINKS = 3, 90, 30
assert FRIENDS * FOOD_EACH + DRINKS == R1
GOAT, PAID, PARTS = 400, 100, 3
assert (GOAT - PAID) // PARTS == R2


def pens_bar(rest_text):
    return bar_model([(PEN_PRICE, None, False)] * PENS + [(MONEY - PENS * PEN_PRICE, rest_text, True)],
        f"A bar for Bilal's Rs {MONEY}, with {MONEY} written above it. It starts with {PENS} small parts, one for each pen, with {PENS}×{PEN_PRICE} written under them; the dashed part left over has {rest_text} in it.",
        f"بلال کے {MONEY} روپے کی ایک پٹی، اوپر {MONEY} لکھا ہے۔ شروع میں {PENS} چھوٹے حصے ہیں، ہر قلم کا ایک، ان کے نیچے {PENS}×{PEN_PRICE} لکھا ہے؛ باقی بچا ڈیش والا حصہ، اس میں {rest_text} لکھا ہے۔",
        total_text=MONEY, under=[(0, PENS * PEN_PRICE, f"{PENS}×{PEN_PRICE}")])


def mangoes():
    items = []
    bw, gap = 46, 10
    x = 10
    for _ in range(BOXES):
        items += [rect(x, 22, x + bw, 62), label((x + bw / 2, 42), PER_BOX)]
        x += bw + gap
    x += 8
    for k in range(LOOSE):
        items.append(circle((x + (k % 3) * 16, 34 + (k // 3) * 16), 6, fill=True))
    return figure(W, 82,
        f"{BOXES} boxes of mangoes, each with {PER_BOX} written on it, and {LOOSE} loose mangoes drawn as dots next to them.",
        f"آموں کے {BOXES} ڈبے، ہر ایک پر {PER_BOX} لکھا ہے، اور ساتھ {LOOSE} کھلے آم نقطوں کی صورت میں۔",
        items)


def chairs():
    gap = 15
    x0 = (W - (PER_ROW - 1) * gap) / 2
    fx = (W - (FRONT - 1) * gap) / 2
    items = [label((x0 - 30, 34), FRONT)]
    items += [circle((fx + k * gap, 34), 5, fill=True) for k in range(FRONT)]
    for i in range(ROWS):
        for j in range(PER_ROW):
            items.append(circle((x0 + j * gap, 64 + i * gap), 5))
    items += [label((x0 - 30, 64 + (ROWS - 1) * gap / 2), ROWS), label((W / 2, 64 + ROWS * gap + 6), PER_ROW)]
    return figure(W, 64 + ROWS * gap + 22,
        f"Chairs in a hall seen from above. Front: {FRONT} chairs as filled dots, with {FRONT} written on the left. Behind them: {ROWS} rows of {PER_ROW} chairs as empty dots, with {ROWS} written on the left and {PER_ROW} under the rows.",
        f"ہال کی کرسیاں اوپر سے۔ آگے: {FRONT} کرسیاں بھرے نقطے، بائیں طرف {FRONT} لکھا ہے۔ ان کے پیچھے: {PER_ROW} کرسیوں کی {ROWS} قطاریں خالی نقطے، بائیں طرف {ROWS} اور قطاروں کے نیچے {PER_ROW} لکھا ہے۔",
        items)


attach(lesson, {
    "s2_foundation": steps_fig(E2, prompt=step_text(lesson, "s2_foundation"), results=False),
    "s4_pens": pens_bar("?"),
    "s5_mangoes": mangoes(),
    "s7_party": bar_model([(FOOD, FOOD, False), (STUDENTS * EACH - FOOD, "?", True)],
        f"A bar for all the money collected, with 30×50 written above it. The first part, {FOOD}, is spent on food; the dashed part left over has a question mark.",
        f"جمع ہونے والے سارے پیسوں کی پٹی، اوپر 30×50 لکھا ہے۔ پہلا حصہ، {FOOD}، کھانے پر خرچ ہوا؛ باقی بچے ڈیش والے حصے میں سوالیہ نشان ہے۔",
        total_text=f"{STUDENTS}×{EACH}"),
    "s8_savings": bar_model([(UNCLE, UNCLE, False), (AUNT, AUNT, False)],
        f"A bar made of Rs {UNCLE} and Rs {AUNT} joined together. Under it is a bar just as long, cut into {SAVE.denominator} equal parts; the first part is shaded, with a question mark: the part Sana saves.",
        f"ایک پٹی جو {UNCLE} روپے اور {AUNT} روپے کو جوڑ کر بنی ہے۔ اس کے نیچے اتنی ہی لمبی پٹی ہے جو {SAVE.denominator} برابر حصوں میں کٹی ہے؛ پہلا حصہ رنگا ہوا ہے اور اس میں سوالیہ نشان ہے: جو ثنا بچاتی ہے۔",
        split=SAVE.denominator, shade=(0,), parts=["?"] + [None] * (SAVE.denominator - 1)),
    "u4_round": round_fig([U4_ROW]),
    "u5_apples": bar_model([(APPLE_PRICE, APPLE_PRICE, False)] * KG + [(NOTE - KG * APPLE_PRICE, "?", True)],
        f"A bar for the Rs {NOTE} note, with {NOTE} written above it. It starts with {KG} parts of {APPLE_PRICE}, one for each kg of apples; the dashed part left over, the change, has a question mark.",
        f"{NOTE} روپے کے نوٹ کی پٹی، اوپر {NOTE} لکھا ہے۔ شروع میں {APPLE_PRICE} کے {KG} حصے ہیں، ہر کلو سیب کا ایک؛ باقی بچے ڈیش والے حصے، یعنی بقایا، میں سوالیہ نشان ہے۔",
        total_text=NOTE),
    "s12_summary": pens_bar(str(S4)),
    "qb_apply": chairs(),
    "r_food": bar_model([(FOOD_EACH, FOOD_EACH, False)] * FRIENDS + [(DRINKS, DRINKS, False)],
        f"A bar made of {FRIENDS} parts of {FOOD_EACH}, one for each friend's food, and one small part of {DRINKS} for the drinks, with a question mark above the whole bar.",
        f"ایک پٹی جس میں {FOOD_EACH} کے {FRIENDS} حصے ہیں، ہر دوست کے کھانے کا ایک، اور مشروبات کا {DRINKS} کا ایک چھوٹا حصہ؛ پوری پٹی کے اوپر سوالیہ نشان ہے۔",
        total_text="?"),
    "r_rest": bar_model([(PAID, PAID, False), (GOAT - PAID, None, False)],
        f"A bar for the goat's price, with {GOAT} written above it. The first part, {PAID}, is paid now. Under the rest is a bar cut into {PARTS} equal dashed parts; the first has a question mark.",
        f"بکری کی قیمت کی پٹی، اوپر {GOAT} لکھا ہے۔ پہلا حصہ، {PAID}، ابھی ادا ہوا۔ باقی حصے کے نیچے ایک پٹی ہے جو {PARTS} برابر ڈیش والے حصوں میں کٹی ہے؛ پہلے میں سوالیہ نشان ہے۔",
        total_text=GOAT, split=PARTS, split_from=PAID, parts=["?"] + [None] * (PARTS - 1)),
})
write(lesson)

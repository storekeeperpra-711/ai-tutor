from common import (T, opt, say, wrong, number_question, write, solves,
                    REF, REVIEW, EQ_CHECK, EQ_FORMING, EQ_TWO_STEP, EQ_BRACKETS, EQ_WORD_PROBLEMS)

SKILL = EQ_WORD_PROBLEMS

# s2: 2x + 3 = 15 (stopping at 2x: 12)
S2 = (15 - 3) // 2
assert solves("2x + 3 = 15", x=S2) and S2 == 6
# s4: father's age 3x + 4 = 40 (stopping at 3x: 36)
S4 = (40 - 4) // 3
assert solves("3x + 4 = 40", x=S4) and S4 == 12
# s5: taxi 20k + 50 = 210 (adding the 50: 13)
S5 = (210 - 50) // 20
assert solves("20k + 50 = 210", k=S5) and S5 == 8 and (210 + 50) // 20 == 13
# s6: x - 30 = 45
assert solves("x − 30 = 45", x=75)
# s7: 4x + 6 = 54 (adding the 6: 15)
S7 = (54 - 6) // 4
assert solves("4x + 6 = 54", x=S7) and S7 == 12 and (54 + 6) // 4 == 15
# s8: 5(x + 3) = 40 (stopping at the bracket: 8)
S8 = 40 // 5 - 3
assert solves("5(x + 3) = 40", x=S8) and S8 == 5
# s9: 2x + 10 = 30 gives 10, not 20
assert solves("2x + 10 = 30", x=10) and 2 * 20 + 10 == 50
# unit test
U1 = [x for x in (3, 4, 5) if solves("7x − 4 = 24", x=x)]
assert U1 == [4]
U1 = U1[0]
U2 = 42 - 15
assert solves("x + 15 = 42", x=U2) and U2 == 27
U3 = (7 - 3) * 5
assert solves("x ÷ 5 + 3 = 7", x=U3) and U3 == 20
U4 = 24 // 4 + 2
assert solves("4(x − 2) = 24", x=U4) and U4 == 8
U5 = (275 - 100) // 25
assert solves("25d + 100 = 275", d=U5) and U5 == 7
# question bank and review
QB = (600 - 150) // 3
assert solves("3x + 150 = 600", x=QB) and QB == 150 and (600 + 150) // 3 == 250
R1 = (31 - 5) // 2
assert solves("2x + 5 = 31", x=R1) and R1 == 13
R2 = (40 - 4) // 6
assert solves("6x + 4 = 40", x=R2) and R2 == 6

lesson = {
 "id": "g6-maths-16-equation-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems by writing and solving a linear equation, then checking the answer in the story.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Equation word problems", "مساوات کے عملی سوال"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": EQ_BRACKETS}, {"skill": EQ_TWO_STEP}, {"skill": EQ_FORMING}, {"skill": EQ_CHECK}],
 "misconceptions": [
   {"id": "one_step_only", "description": "Stops after one step (finds 3x, or the bracket) and gives that as the answer."},
   {"id": "wrong_inverse", "description": "Adds a fixed charge instead of taking it away."},
   {"id": "wrong_equation", "description": "Writes the story the wrong way round, like 30 − x for 'spent 30'."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_check", "type": "recall", "step": {
     "id": "qb_check", "type": "choice",
     "prompt": T("You have solved an equation from a story. What should you do next?", "آپ نے کہانی سے بنی مساوات حل کر لی۔ اب کیا کرنا چاہیے؟"),
     "options": [
       opt("check", "Put the answer back into the story to check it", "جواب کو کہانی میں رکھ کر جانچیں", True,
           "Yes! If the story works, the answer is right.", "جی ہاں! اگر کہانی ٹھیک بیٹھے تو جواب درست ہے۔"),
       opt("stop", "Nothing, you are done", "کچھ نہیں، کام ختم", False,
           "Always check: put the answer back into the story.", "ہمیشہ جانچیں: جواب کو کہانی میں واپس رکھیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Zara buys 3 books at Rs x each and a bag for Rs 150. She pays Rs 600 in all. What does one book cost? (3x + 150 = 600)", "زارا x روپے فی کتاب کے حساب سے 3 کتابیں اور 150 روپے کا ایک بستہ خریدتی ہے۔ وہ کل 600 روپے دیتی ہے۔ ایک کتاب کتنے کی ہے؟ (3x + 150 = 600)"),
     QB,
     T("Take 150 away, then divide by 3.", "150 تفریق کریں، پھر 3 سے تقسیم۔"),
     T("Right! Rs 150.", "درست! 150 روپے"),
     T("600 − 150 = 450, then 450 ÷ 3 = 150.", "600 − 150 = 450، پھر 450 ÷ 3 = 150"),
     common_wrong=[wrong(250, "The bag cost is taken away, not added: 450 ÷ 3 = 150.", "بستے کی قیمت تفریق ہوتی ہے، جمع نہیں: 450 ÷ 3 = 150", "wrong_inverse"),
                   wrong(450, "That is the 3 books together. One book: 450 ÷ 3 = 150.", "یہ 3 کتابیں اکٹھی ہیں۔ ایک کتاب: 450 ÷ 3 = 150", "one_step_only")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("'Usman had some money, spent Rs 40 and has Rs 60 left.' He writes 40 − x = 60. What is wrong?", "'عثمان کے پاس کچھ پیسے تھے، اس نے 40 روپے خرچ کیے اور 60 روپے بچے۔' وہ لکھتا ہے 40 − x = 60۔ کیا غلطی ہے؟"),
     "options": [
       opt("order", "He started with x and took 40 away: x − 40 = 60, so x = 100.", "اس کے پاس x تھے اور 40 نکلے: x − 40 = 60، تو x = 100", True,
           "Yes! Start with what he had.", "جی ہاں! جو اس کے پاس تھا وہاں سے شروع کریں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "He spent 40 from his money x: x − 40 = 60.", "اس نے اپنے x پیسوں میں سے 40 خرچ کیے: x − 40 = 60", "wrong_equation"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_steps", "front": T("Word problem steps?", "عملی سوال کے قدم؟"),
    "back": T("Letter for the unknown, write the equation, solve, check in the story.", "نامعلوم کے لیے حرف، مساوات لکھیں، حل کریں، کہانی میں جانچیں۔")},
   {"id": "f_fixed", "front": T("Rs 50 plus Rs 20 per km = Rs 210?", "50 روپے جمع 20 روپے فی کلومیٹر = 210 روپے؟"),
    "back": T("20k + 50 = 210, so k = 8.", "20k + 50 = 210، تو k = 8")},
 ],
 "home_tasks": [{"id": "h_bill", "text": T(
   "Look at a bill at home with a fixed charge plus a charge per unit (a phone package or electricity). Make up an equation from it and solve it.",
   "گھر میں کوئی بل دیکھیں جس میں ایک مقررہ رقم اور فی یونٹ رقم ہو (فون پیکج یا بجلی)۔ اس سے ایک مساوات بنائیں اور حل کریں۔")}],
 "glossary": [T("Unknown", "نامعلوم"), T("Fixed charge", "مقررہ رقم"), T("Per", "فی")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A rickshaw ride cost Rs 210. How many kilometres was it? An equation can tell us!",
                     "رکشے کا کرایہ 210 روپے آیا۔ کتنے کلومیٹر کا سفر تھا؟ ایک مساوات بتا سکتی ہے!"),
    "text": T("Today we solve real problems by writing an equation. First, a quick two-step check.", "آج ہم مساوات لکھ کر اصل مسئلے حل کریں گے۔ پہلے دو قدمی مساوات کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Solve 2x + 3 = 15. What is x?", "2x + 3 = 15 حل کریں۔ x کیا ہے؟"),
     S2,
     T("Take 3 away, then divide by 2.", "3 تفریق کریں، پھر 2 سے تقسیم۔"),
     T("Right! x = 6.", "درست! x = 6"),
     T("15 − 3 = 12, then 12 ÷ 2 = 6.", "15 − 3 = 12، پھر 12 ÷ 2 = 6"),
     common_wrong=[wrong(12, "That is 2x. Divide by 2: x = 6.", "یہ 2x ہے۔ 2 سے تقسیم کریں: x = 6", "one_step_only")],
     qtype="recall", skill=EQ_TWO_STEP),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Letter, equation, solve, check. Four steps to crack any story!", "حرف، مساوات، حل، جانچ۔ ہر کہانی حل کرنے کے چار قدم!"),
    "text": T("1. Choose a letter for what you don't know. 2. Write an equation from the story. 3. Solve it. 4. Check the answer in the story and write it in words. Example: a rickshaw charges Rs 50, plus Rs 20 per km. The fare is Rs 210. 20k + 50 = 210, 20k = 160, k = 8 km. Check: 50 + 20 × 8 = 210.",
              "1۔ جو معلوم نہیں اس کے لیے حرف چنیں۔ 2۔ کہانی سے مساوات لکھیں۔ 3۔ حل کریں۔ 4۔ جواب کہانی میں جانچیں اور الفاظ میں لکھیں۔ مثال: رکشہ 50 روپے، جمع 20 روپے فی کلومیٹر لیتا ہے۔ کرایہ 210 روپے ہے۔ 20k + 50 = 210، 20k = 160، k = 8 کلومیٹر۔ جانچ: 50 + 20 × 8 = 210")},
   number_question(
     "s4_age",
     T("Ahmed is x years old. His father's age is 3 times Ahmed's age plus 4. His father is 40. How old is Ahmed? (3x + 4 = 40)", "احمد کی عمر x سال ہے۔ اس کے والد کی عمر احمد کی عمر کا 3 گنا جمع 4 ہے۔ والد 40 سال کے ہیں۔ احمد کتنے سال کا ہے؟ (3x + 4 = 40)"),
     S4,
     T("Take 4 away, then divide by 3.", "4 تفریق کریں، پھر 3 سے تقسیم۔"),
     T("Right! Ahmed is 12.", "درست! احمد 12 سال کا ہے۔"),
     T("40 − 4 = 36, then 36 ÷ 3 = 12. Check: 3 × 12 + 4 = 40.", "40 − 4 = 36، پھر 36 ÷ 3 = 12۔ جانچ: 3 × 12 + 4 = 40"),
     common_wrong=[wrong(36, "That is 3 times his age. Divide by 3: 12.", "یہ اس کی عمر کا 3 گنا ہے۔ 3 سے تقسیم کریں: 12", "one_step_only")]),
   number_question(
     "s5_rickshaw",
     T("A rickshaw charges Rs 50, plus Rs 20 for each km. A ride costs Rs 210. How many km was it? (20k + 50 = 210)", "رکشہ 50 روپے، جمع ہر کلومیٹر کے 20 روپے لیتا ہے۔ ایک سفر کا کرایہ 210 روپے ہے۔ سفر کتنے کلومیٹر تھا؟ (20k + 50 = 210)"),
     S5,
     T("Take the Rs 50 away first.", "پہلے 50 روپے تفریق کریں۔"),
     T("Right! 8 km.", "درست! 8 کلومیٹر"),
     T("210 − 50 = 160, then 160 ÷ 20 = 8.", "210 − 50 = 160، پھر 160 ÷ 20 = 8"),
     common_wrong=[wrong(13, "The Rs 50 is part of the fare, so take it away: 160 ÷ 20 = 8.", "50 روپے کرائے کا حصہ ہیں، تو تفریق کریں: 160 ÷ 20 = 8", "wrong_inverse"),
                   wrong(160, "That is the money for the km. Divide by 20: 8 km.", "یہ کلومیٹرز کے پیسے ہیں۔ 20 سے تقسیم کریں: 8 کلومیٹر", "one_step_only")]),
   {"id": "s6_which", "type": "choice",
    "prompt": T("Sara had x rupees. She spent Rs 30 and has Rs 45 left. Which equation fits?", "سارہ کے پاس x روپے تھے۔ اس نے 30 روپے خرچ کیے اور 45 روپے بچے۔ کون سی مساوات ٹھیک ہے؟"),
    "options": [
      opt("minus", "x − 30 = 45", "x − 30 = 45", True, "Yes! Then x = 75.", "جی ہاں! پھر x = 75"),
      opt("reverse", "30 − x = 45", "30 − x = 45", False, "She started with x and spent 30: x − 30 = 45.", "اس کے پاس x تھے اور 30 خرچ ہوئے: x − 30 = 45", "wrong_equation"),
      opt("plus", "x + 30 = 45", "x + 30 = 45", False, "Spending takes away: x − 30 = 45.", "خرچ کرنا یعنی نکالنا: x − 30 = 45", "wrong_equation"),
    ]},
   number_question(
     "s7_pencils",
     T("Hina has 4 boxes with x pencils in each, and 6 loose pencils. She has 54 pencils in all. How many are in each box? (4x + 6 = 54)", "حنا کے پاس 4 ڈبے ہیں، ہر ایک میں x پنسلیں، اور 6 کھلی پنسلیں۔ کل 54 پنسلیں ہیں۔ ہر ڈبے میں کتنی ہیں؟ (4x + 6 = 54)"),
     S7,
     T("Take the 6 loose ones away, then share by 4.", "6 کھلی پنسلیں تفریق کریں، پھر 4 پر تقسیم۔"),
     T("Right! 12 pencils in each box.", "درست! ہر ڈبے میں 12 پنسلیں"),
     T("54 − 6 = 48, then 48 ÷ 4 = 12.", "54 − 6 = 48، پھر 48 ÷ 4 = 12"),
     common_wrong=[wrong(15, "Take the loose pencils away, don't add: 48 ÷ 4 = 12.", "کھلی پنسلیں تفریق کریں، جمع نہیں: 48 ÷ 4 = 12", "wrong_inverse"),
                   wrong(48, "That is all 4 boxes. One box: 48 ÷ 4 = 12.", "یہ چاروں ڈبے ہیں۔ ایک ڈبہ: 48 ÷ 4 = 12", "one_step_only")]),
   number_question(
     "s8_sweets",
     T("5 children each get x toffees and 3 lollipops. 40 sweets are given out in all. How many toffees does each child get? (5(x + 3) = 40)", "5 بچوں میں سے ہر ایک کو x ٹافیاں اور 3 لولی پاپ ملتے ہیں۔ کل 40 مٹھائیاں بٹتی ہیں۔ ہر بچے کو کتنی ٹافیاں ملتی ہیں؟ (5(x + 3) = 40)"),
     S8,
     T("Divide by 5, then take 3 away.", "5 سے تقسیم کریں، پھر 3 تفریق۔"),
     T("Right! 5 toffees each.", "درست! ہر ایک کو 5 ٹافیاں"),
     T("40 ÷ 5 = 8 sweets each, and 8 − 3 = 5 toffees.", "40 ÷ 5 = 8 مٹھائیاں فی بچہ، اور 8 − 3 = 5 ٹافیاں"),
     common_wrong=[wrong(8, "8 is all the sweets each child gets. Take away the 3 lollipops: 5.", "8 ہر بچے کی کل مٹھائیاں ہیں۔ 3 لولی پاپ تفریق کریں: 5", "one_step_only")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal solves 2x + 10 = 30 for a story and gets x = 20. What went wrong?", "بلال ایک کہانی کی مساوات 2x + 10 = 30 حل کرکے x = 20 نکالتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("check", "Check: 2 × 20 + 10 = 50, not 30. The answer is x = 10.", "جانچ: 2 × 20 + 10 = 50، 30 نہیں۔ جواب x = 10 ہے۔", True,
          "Yes! 30 − 10 = 20, then 20 ÷ 2 = 10. He forgot to divide.", "جی ہاں! 30 − 10 = 20، پھر 20 ÷ 2 = 10۔ وہ تقسیم بھول گیا۔"),
      opt("add", "He should add 10: x = 40.", "اسے 10 جمع کرنا چاہیے: x = 40", False,
          "Undo + 10 by subtracting, then divide by 2: x = 10.", "+ 10 کو تفریق سے ختم کریں، پھر 2 سے تقسیم: x = 10", "wrong_inverse"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Check it: 2 × 20 + 10 = 50, not 30. He forgot to divide by 2.", "جانچیں: 2 × 20 + 10 = 50، 30 نہیں۔ وہ 2 سے تقسیم بھول گیا۔", "one_step_only"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why should we check our answer in the story? Can you teach me?",
                     "ہمیں جواب کہانی میں کیوں جانچنا چاہیے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is it a good idea to put your answer back into the story? Use the rickshaw (Rs 50 + Rs 20 per km = Rs 210) as an example.", "اپنے الفاظ میں بتائیں: جواب کو کہانی میں واپس رکھنا کیوں اچھا ہے؟ رکشے (50 روپے + 20 روپے فی کلومیٹر = 210 روپے) کی مثال لیں۔"),
    "key_idea": "Checking catches mistakes in writing or solving the equation. For the rickshaw, 8 km gives 50 + 20 × 8 = 210, which matches the fare, so 8 km is right. A wrong answer like 13 km gives 310, which doesn't match.",
    "levels": {
      "got_it": "Says checking catches mistakes and shows 50 + 20 × 8 = 210 (or a wrong answer failing).",
      "partly": "Says 'to see if it's right' without the example.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["mistake", "wrong", "right", "غلطی", "درست"],
      ["210"],
      ["8", "eight", "آٹھ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The story tells you if the answer works.", "بہت خوب! کہانی بتا دیتی ہے کہ جواب ٹھیک ہے یا نہیں۔"),
      "partly": T("Good start! Now show the check with the rickshaw numbers.", "اچھی شروعات! اب رکشے کے اعداد سے جانچ دکھائیں۔"),
      "not_yet": T("Try 8 km: what is 50 + 20 × 8? Does it match the fare?", "8 کلومیٹر آزمائیں: 50 + 20 × 8 کتنا ہے؟ کیا یہ کرائے کے برابر ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Linear equations unit. You can do it!",
                     "ٹیسٹ کا وقت! خطی مساوات کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on checking a solution, writing equations, two-step equations, brackets and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں حل کی جانچ، مساوات لکھنے، دو قدمی مساوات، قوسین اور ایک اصل زندگی کے سوال ہیں۔ آرام سے کریں۔")},
   number_question(
     "u1_check",
     T("Test 1: Which of 3, 4 or 5 is the solution of 7x − 4 = 24? Type it.", "ٹیسٹ 1: 3، 4 یا 5 میں سے کون سا 7x − 4 = 24 کا حل ہے؟ اسے لکھیں۔"),
     U1,
     T("Try each one in 7x − 4.", "ہر ایک کو 7x − 4 میں آزمائیں۔"),
     T("Right! 7 × 4 − 4 = 24.", "درست! 7 × 4 − 4 = 24"),
     T("7 × 4 = 28, 28 − 4 = 24.", "7 × 4 = 28، 28 − 4 = 24"),
     common_wrong=[wrong(3, "7 × 3 − 4 = 17, not 24. Try 4.", "7 × 3 − 4 = 17، 24 نہیں۔ 4 آزمائیں۔"),
                   wrong(5, "7 × 5 − 4 = 31, not 24. Try 4.", "7 × 5 − 4 = 31، 24 نہیں۔ 4 آزمائیں۔")],
     qtype="recall", skill=EQ_CHECK),
   number_question(
     "u2_forming",
     T("Test 2: A number plus 15 is 42. What is the number?", "ٹیسٹ 2: ایک عدد جمع 15 برابر 42۔ عدد کیا ہے؟"),
     U2,
     T("x + 15 = 42. Take 15 away.", "x + 15 = 42۔ 15 تفریق کریں۔"),
     T("Right! 27.", "درست! 27"),
     T("42 − 15 = 27.", "42 − 15 = 27"),
     common_wrong=[wrong(57, "Undo + 15 by subtracting: 42 − 15 = 27.", "+ 15 کو تفریق سے ختم کریں: 42 − 15 = 27", "wrong_inverse")],
     qtype="apply", skill=EQ_FORMING),
   number_question(
     "u3_two_step",
     T("Test 3: Solve x ÷ 5 + 3 = 7. What is x?", "ٹیسٹ 3: x ÷ 5 + 3 = 7 حل کریں۔ x کیا ہے؟"),
     U3,
     T("Take 3 away, then multiply by 5.", "3 تفریق کریں، پھر 5 سے ضرب۔"),
     T("Right! x = 20.", "درست! x = 20"),
     T("7 − 3 = 4, then 4 × 5 = 20.", "7 − 3 = 4، پھر 4 × 5 = 20"),
     common_wrong=[wrong(4, "That is x ÷ 5. Multiply by 5: x = 20.", "یہ x ÷ 5 ہے۔ 5 سے ضرب دیں: x = 20", "one_step_only"),
                   wrong(50, "Undo + 3 by subtracting 3: 4 × 5 = 20.", "+ 3 کو 3 تفریق کرکے ختم کریں: 4 × 5 = 20", "wrong_inverse")],
     qtype="apply", skill=EQ_TWO_STEP),
   number_question(
     "u4_brackets",
     T("Test 4: Solve 4(x − 2) = 24. What is x?", "ٹیسٹ 4: 4(x − 2) = 24 حل کریں۔ x کیا ہے؟"),
     U4,
     T("Divide by 4, then add 2.", "4 سے تقسیم کریں، پھر 2 جمع۔"),
     T("Right! x = 8.", "درست! x = 8"),
     T("24 ÷ 4 = 6, so x − 2 = 6, x = 8.", "24 ÷ 4 = 6، تو x − 2 = 6، x = 8"),
     common_wrong=[wrong(6, "That is x − 2. Add 2: x = 8.", "یہ x − 2 ہے۔ 2 جمع کریں: x = 8", "one_step_only"),
                   wrong(4, "Undo − 2 by adding 2: 6 + 2 = 8.", "− 2 کو 2 جمع کرکے ختم کریں: 6 + 2 = 8", "wrong_inverse")],
     qtype="apply", skill=EQ_BRACKETS),
   number_question(
     "u5_package",
     T("Test 5: A phone package costs Rs 100 to start, plus Rs 25 for each day. Ali paid Rs 275. How many days did he use it? (25d + 100 = 275)", "ٹیسٹ 5: فون پیکج شروع کرنے کے 100 روپے، جمع ہر دن کے 25 روپے ہیں۔ علی نے 275 روپے دیے۔ اس نے کتنے دن استعمال کیا؟ (25d + 100 = 275)"),
     U5,
     T("Take the Rs 100 away first.", "پہلے 100 روپے تفریق کریں۔"),
     T("Right! 7 days.", "درست! 7 دن"),
     T("275 − 100 = 175, then 175 ÷ 25 = 7.", "275 − 100 = 175، پھر 175 ÷ 25 = 7"),
     common_wrong=[wrong(15, "Take the Rs 100 away, don't add it: 175 ÷ 25 = 7.", "100 روپے تفریق کریں، جمع نہیں: 175 ÷ 25 = 7", "wrong_inverse"),
                   wrong(175, "That is the money for the days. Divide by 25: 7.", "یہ دنوں کے پیسے ہیں۔ 25 سے تقسیم کریں: 7", "one_step_only")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Linear equations unit complete! Stories turn into equations, and equations give answers.", "خطی مساوات کا باب مکمل! کہانیاں مساوات بنتی ہیں، اور مساوات جواب دیتی ہیں۔"),
    "text": T("Choose a letter for the unknown, write the equation from the story, solve it step by step, and check the answer in the story. Fixed amounts are taken away first; amounts 'per' or 'each' are divided last.",
              "نامعلوم کے لیے حرف چنیں، کہانی سے مساوات لکھیں، قدم بہ قدم حل کریں، اور جواب کہانی میں جانچیں۔ مقررہ رقم پہلے تفریق ہوتی ہے؛ 'فی' یا 'ہر ایک' والی رقم پر آخر میں تقسیم۔"),
    "points": [T("Letter, equation, solve, check.", "حرف، مساوات، حل، جانچ۔"),
               T("Take fixed amounts away first.", "مقررہ رقم پہلے تفریق کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_twice", "type": "apply", "skill": SKILL, "step": number_question(
     "r_twice",
     T("5 more than twice a number is 31. What is the number? (2x + 5 = 31)", "ایک عدد کے دگنے سے 5 زیادہ 31 ہے۔ عدد کیا ہے؟ (2x + 5 = 31)"),
     R1,
     T("Take 5 away, then divide by 2.", "5 تفریق کریں، پھر 2 سے تقسیم۔"),
     T("Right! 13.", "درست! 13"),
     T("31 − 5 = 26, then 26 ÷ 2 = 13.", "31 − 5 = 26، پھر 26 ÷ 2 = 13"),
     common_wrong=[wrong(26, "That is twice the number. Divide by 2: 13.", "یہ عدد کا دگنا ہے۔ 2 سے تقسیم کریں: 13", "one_step_only"),
                   wrong(18, "Undo + 5 by subtracting: 26 ÷ 2 = 13.", "+ 5 کو تفریق سے ختم کریں: 26 ÷ 2 = 13", "wrong_inverse")],
     qtype=None)},
   {"id": "r_packs", "type": "apply", "skill": SKILL, "step": number_question(
     "r_packs",
     T("A teacher has 6 packs of x chalks and 4 loose chalks: 40 chalks in all. How many chalks are in a pack? (6x + 4 = 40)", "استاد کے پاس x چاکوں والے 6 پیکٹ اور 4 کھلے چاک ہیں: کل 40 چاک۔ ایک پیکٹ میں کتنے چاک ہیں؟ (6x + 4 = 40)"),
     R2,
     T("Take the 4 loose chalks away, then divide by 6.", "4 کھلے چاک تفریق کریں، پھر 6 سے تقسیم۔"),
     T("Right! 6 chalks in a pack.", "درست! ایک پیکٹ میں 6 چاک"),
     T("40 − 4 = 36, then 36 ÷ 6 = 6.", "40 − 4 = 36، پھر 36 ÷ 6 = 6"),
     common_wrong=[wrong(36, "That is all 6 packs. One pack: 36 ÷ 6 = 6.", "یہ چھ پیکٹ ہیں۔ ایک پیکٹ: 36 ÷ 6 = 6", "one_step_only")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Linear Equations unit. No textbook text or exercises were used.",
   "Each story question shows its equation in brackets, so children practise solving; the choice and find-the-mistake steps practise writing the equation.",
   "The five-question unit test at the end covers every lesson of the unit.",
   "The numbers were worked out in content/sources/g6-maths-16/equation_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

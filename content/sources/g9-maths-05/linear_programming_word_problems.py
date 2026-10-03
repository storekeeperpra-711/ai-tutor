from common import T, opt, say, write, REF, REVIEW, corners, corner_text, region_sim, best, table, num, values, plane

SKILL = "maths.linear_programming.word_problems"

# Nadia the tailor: x shirts, y trousers a day.
TAILOR = ["x + 2y <= 10", "2x + y <= 14", "x >= 0", "y >= 0"]
PROFIT = "300x + 400y"
(pt, zt) = best(PROFIT, corners(TAILOR))
assert corner_text(corners(TAILOR)) == "(0, 0), (0, 5), (6, 2), (7, 0)"
assert (pt, zt) == ((6, 2), 2600), (pt, zt)
vals = dict(values(PROFIT, corners(TAILOR)))
assert vals[(7, 0)] == 2100 and vals[(0, 5)] == 2000
# Kamran's (7, 5) breaks the time limit.
assert not plane.parse_half_plane("x + 2y <= 10").contains((7, 5))

# Farmer for the question bank: x acres wheat, y acres maize.
FARM = ["x + y <= 8", "x + 3y <= 12", "x >= 0", "y >= 0"]
FARM_PROFIT = "5x + 9y"
(pf, zf) = best(FARM_PROFIT, corners(FARM))
assert corner_text(corners(FARM)) == "(0, 0), (0, 4), (6, 2), (8, 0)"
assert (pf, zf) == ((6, 2), 48), (pf, zf)

lesson = {
 "id": "g9-maths-05-linear-programming-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 9, "tier": "older",
 "curriculum_refs": [{"outcome": "Solve real-life problems with linear programming: write the constraints and objective function, then find the best solution.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Linear programming word problems", "خطی پروگرامنگ کے عملی سوالات"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": "maths.linear_programming.optimize"}],
 "misconceptions": [
   {"id": "mixed_up_numbers", "description": "Puts a number with the wrong variable when writing a constraint (2x + y instead of x + 2y)."},
   {"id": "sign_reading", "description": "Writes ≥ for 'at most' (or ≤ for 'at least')."},
   {"id": "forgets_non_negative", "description": "Leaves out x ≥ 0 and y ≥ 0."},
   {"id": "point_not_feasible", "description": "Chooses a point that breaks a constraint because it gives a bigger value."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["apply", "explain", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_farm_constraint", "type": "apply", "step": {
     "id": "qb_farm_constraint", "type": "text_check", "checker": "linear_inequality_2d", "expected": "x + 3y <= 12",
     "prompt": T("A farmer plants x acres of wheat and y acres of maize. Wheat needs 1 bag of fertiliser an acre, maize needs 3, and he has 12 bags. Write the fertiliser inequality.",
                 "ایک کسان x ایکڑ گندم اور y ایکڑ مکئی بوتا ہے۔ گندم کو فی ایکڑ کھاد کی 1 بوری چاہیے، مکئی کو 3، اور اس کے پاس 12 بوریاں ہیں۔ کھاد کی نامساوات لکھیں۔"),
     "hint": T("Bags used: 1 × x for wheat and 3 × y for maize. At most 12.", "استعمال ہونے والی بوریاں: گندم کے لیے 1 × x اور مکئی کے لیے 3 × y۔ زیادہ سے زیادہ 12۔"),
     "feedback_correct": T("Correct: x + 3y ≤ 12.", "درست: x + 3y ≤ 12۔"),
     "feedback_wrong": T("Bags used are x + 3y, and he has 12, so x + 3y ≤ 12.", "استعمال ہونے والی بوریاں x + 3y ہیں، اور اس کے پاس 12 ہیں، اس لیے x + 3y ≤ 12۔"),
     "common_wrong": [{"answer": "3x + y <= 12", "misconception_id": "mixed_up_numbers", "feedback": T("Maize needs 3 bags, so the 3 goes with y.", "مکئی کو 3 بوریاں چاہئیں، اس لیے 3، y کے ساتھ آئے گا۔")}]}},
   {"id": "qb_why_non_negative", "type": "explain", "step": {
     "id": "qb_why_non_negative", "type": "choice",
     "prompt": T("Why do word problems always add x ≥ 0 and y ≥ 0?", "عملی سوالات میں ہمیشہ x ≥ 0 اور y ≥ 0 کیوں شامل کرتے ہیں؟"),
     "options": [
       opt("a", "x and y count real things, like shirts or acres, and you can't have a negative number of them.", "x اور y اصل چیزیں گنتے ہیں، جیسے قمیضیں یا ایکڑ، اور ان کی منفی تعداد نہیں ہو سکتی۔", True,
           "Exactly! Without them the region would go off into negative numbers.", "بالکل! ان کے بغیر خطہ منفی اعداد میں چلا جاتا۔"),
       opt("b", "Because the textbook always does.", "کیونکہ کتاب میں ہمیشہ ہوتا ہے۔", False,
           "There is a real reason. What do x and y count?", "اس کی اصل وجہ ہے۔ x اور y کیا گنتے ہیں؟"),
       opt("c", "To make the answer bigger.", "جواب بڑا کرنے کے لیے۔", False,
           "They make the region smaller, not the answer bigger. Think about what a negative shirt would mean.", "یہ خطے کو چھوٹا کرتے ہیں، جواب بڑا نہیں۔ سوچیں منفی قمیض کا کیا مطلب ہو گا۔", "forgets_non_negative"),
     ]}},
   {"id": "qb_find_error_farm", "type": "find_error", "step": {
     "id": "qb_find_error_farm", "type": "choice",
     "prompt": T(f"With x + y ≤ 8, x + 3y ≤ 12, x ≥ 0, y ≥ 0 and profit 5x + 9y (thousand rupees), Saad says plant 0 acres of wheat and 8 of maize for 72. What is wrong?",
                 f"x + y ≤ 8، x + 3y ≤ 12، x ≥ 0، y ≥ 0 اور منافع 5x + 9y (ہزار روپے) کے ساتھ سعد کہتا ہے 0 ایکڑ گندم اور 8 ایکڑ مکئی سے 72۔ غلطی کیا ہے؟"),
     "options": [
       opt("a", f"(0, 8) breaks x + 3y ≤ 12: it needs 24 bags. The best corner is (6, 2), with profit {num(zf)}.", f"(0, 8)، x + 3y ≤ 12 کو توڑتا ہے: اسے 24 بوریاں چاہئیں۔ بہترین کونا (6, 2) ہے، منافع {num(zf)}۔", True,
           "Right! Only points in the feasible region are allowed.", "درست! صرف قابلِ عمل خطے کے نقطوں کی اجازت ہے۔"),
       opt("b", "Nothing: 72 is the biggest profit.", "کچھ نہیں: 72 سب سے زیادہ منافع ہے۔", False,
           "Check (0, 8) in x + 3y ≤ 12: 0 + 24 = 24.", "(0, 8) کو x + 3y ≤ 12 میں جانچیں: 0 + 24 = 24۔", "point_not_feasible"),
       opt("c", "He should plant only wheat.", "اسے صرف گندم بونی چاہیے۔", False,
           f"Only wheat, (8, 0), gives 40. Work out the profit at every corner.", f"صرف گندم، (8, 0)، سے 40 ملتا ہے۔ ہر کونے پر منافع نکالیں۔"),
     ]}},
 ]},
 "home_tasks": [{"id": "h_own_problem", "text": T(
   "Make up your own problem: a shopkeeper with limited money and space who sells two things. Write two constraints, x ≥ 0, y ≥ 0 and a profit function. Find the best plan. Ask someone at home to check your inequalities.",
   "اپنا سوال بنائیں: ایک دکاندار جس کے پاس پیسے اور جگہ محدود ہیں اور جو دو چیزیں بیچتا ہے۔ دو شرطیں، x ≥ 0، y ≥ 0 اور منافع کا تفاعل لکھیں۔ بہترین منصوبہ معلوم کریں۔ گھر میں کسی سے اپنی نامساوات جانچوائیں۔")}],
 "glossary": [T("Constraint", "قید (شرط)"), T("Profit", "منافع"), T("At most", "زیادہ سے زیادہ"), T("At least", "کم از کم"), T("Optimal solution", "بہترین حل")],
 "steps": [
   {"id": "s1_tailor", "type": "explain",
    "character": say("curious",
      "Nadia is a tailor in Faisalabad. She makes shirts and trousers. How many of each should she make to earn the most?",
      "نادیہ فیصل آباد میں درزن ہے۔ وہ قمیضیں اور پتلونیں بناتی ہے۔ سب سے زیادہ کمانے کے لیے وہ ہر ایک کی کتنی بنائے؟"),
    "text": T(
      "Each day she has at most 10 hours and at most 14 metres of cloth. A shirt takes 1 hour and 2 metres of cloth. A pair of trousers takes 2 hours and 1 metre. Her profit is Rs 300 on a shirt and Rs 400 on a pair of trousers. Let x be the number of shirts and y the number of trousers.",
      "ہر دن اس کے پاس زیادہ سے زیادہ 10 گھنٹے اور زیادہ سے زیادہ 14 میٹر کپڑا ہے۔ ایک قمیض میں 1 گھنٹہ اور 2 میٹر کپڑا لگتا ہے۔ ایک پتلون میں 2 گھنٹے اور 1 میٹر۔ اسے قمیض پر 300 روپے اور پتلون پر 400 روپے منافع ہوتا ہے۔ قمیضوں کی تعداد x اور پتلونوں کی تعداد y لیں۔")},
   {"id": "s2_time", "type": "choice", "question_type": "apply",
    "prompt": T("Which inequality says that Nadia has at most 10 hours?", "کون سی نامساوات کہتی ہے کہ نادیہ کے پاس زیادہ سے زیادہ 10 گھنٹے ہیں؟"),
    "options": [
      opt("right", "x + 2y ≤ 10", "x + 2y ≤ 10", True,
          "Yes! 1 hour for each shirt (x) and 2 hours for each pair of trousers (2y), at most 10.", "جی ہاں! ہر قمیض کا 1 گھنٹہ (x) اور ہر پتلون کے 2 گھنٹے (2y)، زیادہ سے زیادہ 10۔"),
      opt("mixed", "2x + y ≤ 10", "2x + y ≤ 10", False,
          "That gives shirts 2 hours. A shirt takes 1 hour; trousers take 2.", "اس میں قمیض کے 2 گھنٹے ہیں۔ قمیض میں 1 گھنٹہ لگتا ہے؛ پتلون میں 2۔", "mixed_up_numbers"),
      opt("sign", "x + 2y ≥ 10", "x + 2y ≥ 10", False,
          "'At most 10' means 10 or less, so ≤.", "'زیادہ سے زیادہ 10' کا مطلب 10 یا کم، اس لیے ≤۔", "sign_reading"),
    ]},
   {"id": "s3_cloth", "type": "text_check", "question_type": "apply", "checker": "linear_inequality_2d", "expected": "2x + y <= 14",
    "prompt": T("Now write the cloth inequality. (Type ≤ as <=.)", "اب کپڑے کی نامساوات لکھیں۔ (≤ کو <= لکھیں۔)"),
    "hint": T("A shirt takes 2 metres and trousers take 1 metre. She has at most 14 metres.", "قمیض میں 2 میٹر اور پتلون میں 1 میٹر لگتا ہے۔ اس کے پاس زیادہ سے زیادہ 14 میٹر ہیں۔"),
    "feedback_correct": T("Correct: 2x + y ≤ 14.", "درست: 2x + y ≤ 14۔"),
    "feedback_wrong": T("Cloth used: 2 metres for each shirt (2x) and 1 for each pair of trousers (y). So 2x + y ≤ 14.", "استعمال ہونے والا کپڑا: ہر قمیض کے 2 میٹر (2x) اور ہر پتلون کا 1 (y)۔ اس لیے 2x + y ≤ 14۔"),
    "common_wrong": [{"answer": "x + 2y <= 14", "misconception_id": "mixed_up_numbers", "feedback": T(
      "The numbers are swapped: shirts take 2 metres, so the 2 goes with x.", "اعداد الٹ گئے: قمیض میں 2 میٹر لگتا ہے، اس لیے 2، x کے ساتھ آئے گا۔")}]},
   {"id": "s4_non_negative", "type": "choice", "question_type": "explain",
    "prompt": T("What else must be true about x and y?", "x اور y کے بارے میں اور کیا درست ہونا چاہیے؟"),
    "options": [
      opt("right", "x ≥ 0 and y ≥ 0: she can't make a negative number of clothes.", "x ≥ 0 اور y ≥ 0: وہ کپڑوں کی منفی تعداد نہیں بنا سکتی۔", True,
          "Exactly! These are the non-negative constraints.", "بالکل! یہ غیر منفی شرطیں ہیں۔"),
      opt("equal", "x = y: she must make the same number of each.", "x = y: اسے دونوں برابر تعداد میں بنانے ہیں۔", False,
          "The story doesn't say that. She can make any mix that fits her time and cloth.", "کہانی یہ نہیں کہتی۔ وہ کوئی بھی ملاپ بنا سکتی ہے جو وقت اور کپڑے میں پورا آئے۔"),
      opt("nothing", "Nothing else.", "اور کچھ نہیں۔", False,
          "Could x be −2? A negative number of shirts makes no sense.", "کیا x، −2 ہو سکتا ہے؟ قمیضوں کی منفی تعداد کا کوئی مطلب نہیں۔", "forgets_non_negative"),
    ]},
   region_sim("s5_region", TAILOR,
     T("Here is Nadia's feasible region for x + 2y ≤ 10, 2x + y ≤ 14, x ≥ 0, y ≥ 0. Mark its corners; each shows her profit 300x + 400y.",
       "یہ نادیہ کا قابلِ عمل خطہ ہے: x + 2y ≤ 10، 2x + y ≤ 14، x ≥ 0، y ≥ 0۔ اس کے کونے نشان زد کریں؛ ہر ایک اس کا منافع 300x + 400y دکھاتا ہے۔"),
     T("4 corners. The slanted lines meet where x + 2y = 10 and 2x + y = 14 are both true.", "4 کونے۔ ترچھے خطوط وہاں ملتے ہیں جہاں x + 2y = 10 اور 2x + y = 14 دونوں درست ہوں۔"),
     T(f"Well done! {table(PROFIT, corners(TAILOR), 'profit')}.", f"شاباش! {table(PROFIT, corners(TAILOR), 'منافع')}۔"),
     T(f"The corners are {corner_text(corners(TAILOR))}. (6, 2) is where the two slanted lines meet: 6 + 4 = 10 and 12 + 2 = 14.",
       f"کونے {corner_text(corners(TAILOR))} ہیں۔ (6, 2) پر دونوں ترچھے خطوط ملتے ہیں: 6 + 4 = 10 اور 12 + 2 = 14۔"),
     x_max=8, y_max=7, objective=PROFIT),
   {"id": "s6_best_profit", "type": "number", "question_type": "apply", "checker": "numeric", "answer": int(zt),
    "unit": T("rupees", "روپے"),
    "prompt": T("What is the most profit Nadia can make in a day?", "نادیہ ایک دن میں زیادہ سے زیادہ کتنا منافع کما سکتی ہے؟"),
    "hint": T("Compare the profit at the four corners.", "چاروں کونوں پر منافع کا موازنہ کریں۔"),
    "feedback_correct": T(f"Correct! Rs {num(zt)}.", f"درست! {num(zt)} روپے۔"),
    "feedback_wrong": T(f"{table(PROFIT, corners(TAILOR), 'profit')}. The most is Rs {num(zt)}.", f"{table(PROFIT, corners(TAILOR), 'منافع')}۔ سب سے زیادہ {num(zt)} روپے ہے۔"),
    "common_wrong": [{"answer": 2100, "misconception_id": "point_not_feasible", "feedback": T(
      "2100 is for 7 shirts only. Check the corner where the two slanted lines meet.", "2100 صرف 7 قمیضوں کا ہے۔ وہ کونا جانچیں جہاں دونوں ترچھے خطوط ملتے ہیں۔")}]},
   {"id": "s7_how_many", "type": "choice", "question_type": "apply",
    "prompt": T("So what should Nadia make each day?", "تو نادیہ ہر دن کیا بنائے؟"),
    "options": [
      opt("right", "6 shirts and 2 pairs of trousers", "6 قمیضیں اور 2 پتلونیں", True,
          f"Yes! The corner (6, 2) gives Rs {num(zt)}, and uses exactly 10 hours and 14 metres.", f"جی ہاں! کونا (6, 2)، {num(zt)} روپے دیتا ہے، اور ٹھیک 10 گھنٹے اور 14 میٹر استعمال کرتا ہے۔"),
      opt("swapped", "2 shirts and 6 pairs of trousers", "2 قمیضیں اور 6 پتلونیں", False,
          "x is shirts and y is trousers, so (6, 2) means 6 shirts. Also, (2, 6) needs 14 hours.", "x قمیضیں اور y پتلونیں ہیں، اس لیے (6, 2) کا مطلب 6 قمیضیں۔ اور (2, 6) کے لیے 14 گھنٹے چاہئیں۔", "mixed_up_numbers"),
      opt("only_shirts", "7 shirts and no trousers", "7 قمیضیں اور کوئی پتلون نہیں", False,
          f"That gives Rs 2100. (6, 2) gives Rs {num(zt)}.", f"اس سے 2100 روپے ملتے ہیں۔ (6, 2) سے {num(zt)} روپے۔"),
    ]},
   {"id": "s8_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Kamran says Nadia should make 7 shirts and 5 pairs of trousers, because that gives Rs 4100. What is wrong?",
                "کامران کہتا ہے نادیہ 7 قمیضیں اور 5 پتلونیں بنائے، کیونکہ اس سے 4100 روپے ملتے ہیں۔ غلطی کیا ہے؟"),
    "options": [
      opt("right", "(7, 5) is not allowed: it needs 7 + 10 = 17 hours, but she only has 10.", "(7, 5) کی اجازت نہیں: اس کے لیے 7 + 10 = 17 گھنٹے چاہئیں، مگر اس کے پاس صرف 10 ہیں۔", True,
          "Right! A bigger profit means nothing if the plan breaks a constraint.", "درست! اگر منصوبہ کوئی شرط توڑے تو زیادہ منافع کا کوئی مطلب نہیں۔"),
      opt("sum", "The profit is wrong: it should be 300 + 400 = 700.", "منافع غلط ہے: 300 + 400 = 700 ہونا چاہیے۔", False,
          "His profit sum is right: 2100 + 2000 = 4100. Check the constraints.", "اس کا منافع کا حساب درست ہے: 2100 + 2000 = 4100۔ شرطیں جانچیں۔"),
      opt("nothing", "Nothing, more clothes means more profit.", "کچھ نہیں، زیادہ کپڑے زیادہ منافع۔", False,
          "Put (7, 5) into x + 2y ≤ 10.", "(7, 5) کو x + 2y ≤ 10 میں رکھیں۔", "point_not_feasible"),
    ]},
   {"id": "s9_explain_steps", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "task": T("Explain the steps you follow to solve a linear programming word problem, like Nadia's.",
              "نادیہ جیسے خطی پروگرامنگ کے عملی سوال کو حل کرنے کے مراحل سمجھائیں۔"),
    "key_idea": "Choose the variables (x and y), write each limit as an inequality plus x ≥ 0 and y ≥ 0, write the objective function (profit or cost), draw the feasible region, find its corners, work out the objective at each corner, and choose the biggest (or smallest). Then answer in words.",
    "levels": {
      "got_it": "Names variables, inequalities (constraints), the region and its corners, and checking the objective at the corners to pick the best.",
      "partly": "Mentions some steps, e.g. writing inequalities or checking corners, but leaves out key ones.",
      "not_yet": "Guesses or tries random numbers without inequalities or corners."},
    "keywords": [
      ["inequality", "constraint", "limit", "نامساوات", "شرط", "حد", "namasawat", "shart", "had"],
      ["corner", "vertex", "point", "کونا", "کونے", "نقطہ", "kona", "konay", "nuqta"],
      ["profit", "objective", "value", "best", "maximum", "منافع", "قیمت", "بہترین", "munafa", "qeemat", "behtareen"]],
    "fallback_feedback": {
      "got_it": T("Excellent! Variables, inequalities, region, corners, best value: that's the method.", "زبردست! متغیرات، نامساوات، خطہ، کونے، بہترین قیمت: یہی طریقہ ہے۔"),
      "partly": T("Good start! After writing the inequalities, how do you find the best plan?", "اچھا آغاز! نامساوات لکھنے کے بعد بہترین منصوبہ کیسے ڈھونڈتے ہیں؟"),
      "not_yet": T("Start like this: what are x and y? What limits does the story give?", "یوں شروع کریں: x اور y کیا ہیں؟ کہانی کیا حدیں بتاتی ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s10_summary", "type": "summary",
    "character": say("celebrating", "You solved a real business problem with maths!", "آپ نے ریاضی سے کاروبار کا اصل مسئلہ حل کر لیا!"),
    "text": T("1) Choose x and y. 2) Write each limit as an inequality, plus x ≥ 0 and y ≥ 0. 3) Write the profit or cost. 4) Draw the region and find its corners. 5) Work out the profit at each corner and choose the best. 6) Answer in words.",
              "1) x اور y چنیں۔ 2) ہر حد کو نامساوات کے طور پر لکھیں، ساتھ x ≥ 0 اور y ≥ 0۔ 3) منافع یا خرچ لکھیں۔ 4) خطہ بنائیں اور اس کے کونے معلوم کریں۔ 5) ہر کونے پر منافع نکالیں اور بہترین چنیں۔ 6) جواب الفاظ میں لکھیں۔"),
    "points": [T("'At most' means ≤, 'at least' means ≥.", "'زیادہ سے زیادہ' کا مطلب ≤، 'کم از کم' کا مطلب ≥۔"),
               T("Check your answer in every constraint before you write it.", "جواب لکھنے سے پہلے اسے ہر شرط میں جانچیں۔")]},
 ],
 "teacher_notes": [
   "Written fresh for Phase 8. No textbook text or exercises were copied.",
   "Urdu terms to check: قید / شرط (constraint), منافع (profit), درزن (tailor, female). Nadia's numbers keep every corner a whole number so the interactive can mark it.",
   "All corners and profits are worked out by a script (tools/plane.py) and checked by tools/validate_lessons.py.",
   "Board-exam practice for the whole unit is a separate practice set."],
 "review": REVIEW,
 "review_questions": [{"id": "r_farm_profit", "type": "apply", "skill": SKILL, "step": {
   "id": "r_farm_profit", "type": "number", "checker": "numeric", "answer": int(zf),
   "unit": T("thousand rupees", "ہزار روپے"),
   "prompt": T(f"A farmer's region has corners {corner_text(corners(FARM))}. Profit is 5x + 9y thousand rupees. What is the most profit?",
               f"ایک کسان کے خطے کے کونے {corner_text(corners(FARM))} ہیں۔ منافع 5x + 9y ہزار روپے ہے۔ زیادہ سے زیادہ منافع کیا ہے؟"),
   "hint": T("Work out 5x + 9y at each corner.", "ہر کونے پر 5x + 9y نکالیں۔"),
   "feedback_correct": T(f"Correct: {num(zf)} thousand rupees, at (6, 2).", f"درست: {num(zf)} ہزار روپے، (6, 2) پر۔"),
   "feedback_wrong": T(f"{table(FARM_PROFIT, corners(FARM), 'profit')}. The most is {num(zf)}.", f"{table(FARM_PROFIT, corners(FARM), 'منافع')}۔ سب سے زیادہ {num(zf)} ہے۔")}}],
}
write(lesson)

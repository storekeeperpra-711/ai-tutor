from common import T, opt, say, write, REF, REVIEW, corners, corner_text, region_sim, best, table, num, plane
from fractions import Fraction

SKILL = "maths.unit5.board_exam"

# Long question 1 (minimum).
L1 = ["x + y >= 3", "x <= 4", "y <= 4", "x >= 0", "y >= 0"]
Z1 = "2x + 3y"
(p1, z1) = best(Z1, corners(L1), biggest=False)
assert corner_text(corners(L1)) == "(0, 3), (0, 4), (3, 0), (4, 0), (4, 4)"
assert (p1, z1) == ((3, 0), 6), (p1, z1)

# Long question 2 (maximum, notebook).
L2 = ["x + y <= 6", "x + 3y <= 12", "x >= 0", "y >= 0"]
Z2 = "2x + 5y"
(p2, z2) = best(Z2, corners(L2))
assert corner_text(corners(L2)) == "(0, 0), (0, 4), (3, 3), (6, 0)"
assert (p2, z2) == ((3, 3), 21), (p2, z2)

# MCQ 2: which point satisfies 2x + y < 5.
H = plane.parse_half_plane("2x + y < 5")
assert H.contains((1, 2)) and not any(H.contains(p) for p in [(2, 1), (3, 0), (0, 5)])

# Bank: maximum of 4x + 3y on lesson 5's region.
LB = ["x + 2y <= 8", "x + y <= 6", "x >= 0", "y >= 0"]
ZB = "4x + 3y"
(pb, zb) = best(ZB, corners(LB))
assert (pb, zb) == ((6, 0), 24), (pb, zb)


def mcq(id, en, ur, options):
    return {"id": id, "type": "choice", "question_type": "exam_style", "prompt": T(en, ur), "options": options}


lesson = {
 "id": "g9-maths-05-board-exam-practice",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 9, "tier": "older",
 "curriculum_refs": [{"outcome": "Answer board-exam questions on linear equations, inequalities and linear programming, with working set out as examiners expect.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Unit 5 board-exam practice", "یونٹ 5: بورڈ امتحان کی تیاری"),
 "estimated_minutes": 25,
 "prerequisites": [
   {"skill": "maths.linear_equations.brackets_fractions"},
   {"skill": "maths.inequalities.one_variable"},
   {"skill": "maths.linear_programming.word_problems"}],
 "misconceptions": [
   {"id": "forgot_to_flip", "description": "Divides an inequality by a negative number without reversing the sign."},
   {"id": "boundary_point", "description": "Counts a point on the line of a strict (< or >) inequality as a solution."},
   {"id": "max_min_mixed", "description": "Gives the largest value when the question asks for the smallest."},
   {"id": "fraction_one_term", "description": "Multiplies only some terms when clearing fractions."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_max", "type": "exam_style", "step": {
     "id": "qb_exam_max", "type": "number", "checker": "numeric", "answer": int(zb),
     "prompt": T("Maximise z = 4x + 3y subject to x + 2y ≤ 8, x + y ≤ 6, x ≥ 0, y ≥ 0.", "z = 4x + 3y کو زیادہ سے زیادہ کریں، شرائط x + 2y ≤ 8، x + y ≤ 6، x ≥ 0، y ≥ 0۔"),
     "hint": T(f"The corners are {corner_text(corners(LB))}.", f"کونے {corner_text(corners(LB))} ہیں۔"),
     "feedback_correct": T(f"Correct: z = {num(zb)} at (6, 0).", f"درست: z = {num(zb)}، (6, 0) پر۔"),
     "feedback_wrong": T(f"{table(ZB, corners(LB))}. Maximum z = {num(zb)} at (6, 0).", f"{table(ZB, corners(LB))}۔ زیادہ سے زیادہ z = {num(zb)}، (6, 0) پر۔"),
     "common_wrong": [{"answer": 22, "feedback": T("22 is at (4, 2). Check (6, 0) too.", "22، (4, 2) پر ہے۔ (6, 0) بھی جانچیں۔")}]}},
   {"id": "qb_exam_solve", "type": "exam_style", "step": {
     "id": "qb_exam_solve", "type": "text_check", "checker": "linear_inequality", "expected": "2(x - 3) > 5x + 3", "multiline": True,
     "prompt": T("Solve 2(x − 3) > 5x + 3. Write each step on a new line.", "2(x − 3) > 5x + 3 حل کریں۔ ہر قدم نئی سطر میں لکھیں۔"),
     "hint": T("Open the bracket: 2x − 6 > 5x + 3. Then take 5x from both sides.", "قوس کھولیں: 2x − 6 > 5x + 3۔ پھر دونوں طرف سے 5x گھٹائیں۔"),
     "feedback_correct": T("Correct: x < −3.", "درست: x < −3۔"),
     "feedback_wrong": T("2x − 6 > 5x + 3, so −3x > 9, so x < −3 (flipped, dividing by −3).", "2x − 6 > 5x + 3، اس لیے −3x > 9، اس لیے x < −3 (−3 سے تقسیم پر علامت الٹی)۔")}},
 ]},
 "home_tasks": [{"id": "h_past_paper", "text": T(
   "Ask a teacher or an older student for a past BISE Grade 9 maths paper. Find the Unit 5 questions and answer them in your notebook, setting out the working like the model answers in this practice.",
   "کسی استاد یا بڑے طالب علم سے نویں جماعت ریاضی کا پرانا بورڈ پرچہ لیں۔ یونٹ 5 کے سوال ڈھونڈیں اور اپنی کاپی میں حل کریں، کام اس مشق کے نمونہ جوابات کی طرح لکھیں۔")}],
 "glossary": [T("Model answer", "نمونہ جواب"), T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"), T("Marks", "نمبر")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "Let's practise Unit 5 the way the board exam asks it. Write neatly and show every step!",
                     "آئیں یونٹ 5 کی مشق ویسے کریں جیسے بورڈ امتحان پوچھتا ہے۔ صاف لکھیں اور ہر قدم دکھائیں!"),
    "text": T(
      "The paper has three kinds of question: multiple choice (1 mark each, choose one answer), short questions (about 2 marks, a few lines of working), and long questions (4 marks or more, full working). In short and long questions, marks are for the working, not just the answer.",
      "پرچے میں تین طرح کے سوال ہوتے ہیں: کثیر انتخابی (ہر ایک کا 1 نمبر، ایک جواب چنیں)، مختصر سوال (تقریباً 2 نمبر، چند سطروں کا کام)، اور تفصیلی سوال (4 یا زیادہ نمبر، پورا کام)۔ مختصر اور تفصیلی سوالوں میں نمبر کام کے ہیں، صرف جواب کے نہیں۔")},
   mcq("m1_solve", "MCQ: The solution of 3x − 5 = 7 is:", "کثیر انتخابی: 3x − 5 = 7 کا حل ہے:", [
     opt("a", "x = 4", "x = 4", True, "Correct: 3x = 12, so x = 4.", "درست: 3x = 12، اس لیے x = 4۔"),
     opt("b", "x = 2/3", "x = 2/3", False, "That comes from 3x = 2. Add 5 to both sides first: 3x = 12.", "یہ 3x = 2 سے آتا ہے۔ پہلے دونوں طرف 5 جمع کریں: 3x = 12۔"),
     opt("c", "x = 12", "x = 12", False, "3x = 12; now divide by 3.", "3x = 12؛ اب 3 سے تقسیم کریں۔"),
     opt("d", "x = −4", "x = −4", False, "Check: 3 × (−4) − 5 = −17, not 7.", "جانچیں: 3 × (−4) − 5 = −17، نہ کہ 7۔"),
   ]),
   mcq("m2_flip", "MCQ: The solution of −2x > 6 is:", "کثیر انتخابی: −2x > 6 کا حل ہے:", [
     opt("a", "x < −3", "x < −3", True, "Correct: dividing by −2 flips > to <.", "درست: −2 سے تقسیم پر > بدل کر < ہو جاتا ہے۔"),
     opt("b", "x > −3", "x > −3", False, "You divided by −2, so the sign must flip.", "آپ نے −2 سے تقسیم کیا، اس لیے علامت الٹنی چاہیے۔", "forgot_to_flip"),
     opt("c", "x < 3", "x < 3", False, "6 ÷ (−2) = −3, not 3.", "6 ÷ (−2) = −3، نہ کہ 3۔"),
     opt("d", "x > 3", "x > 3", False, "Try x = 4: −8 > 6 is false.", "x = 4 آزمائیں: −8 > 6 غلط ہے۔"),
   ]),
   mcq("m3_point", "MCQ: Which point satisfies 2x + y < 5?", "کثیر انتخابی: کون سا نقطہ 2x + y < 5 پر پورا اترتا ہے؟", [
     opt("a", "(1, 2)", "(1, 2)", True, "Correct: 2 + 2 = 4, and 4 < 5.", "درست: 2 + 2 = 4، اور 4 < 5۔"),
     opt("b", "(2, 1)", "(2, 1)", False, "4 + 1 = 5, and 5 < 5 is false: the point is on the dashed line.", "4 + 1 = 5، اور 5 < 5 غلط ہے: نقطہ ٹوٹی لکیر پر ہے۔", "boundary_point"),
     opt("c", "(3, 0)", "(3, 0)", False, "6 + 0 = 6, which is not less than 5.", "6 + 0 = 6، جو 5 سے کم نہیں۔"),
     opt("d", "(0, 5)", "(0, 5)", False, "0 + 5 = 5, and 5 < 5 is false.", "0 + 5 = 5، اور 5 < 5 غلط ہے۔", "boundary_point"),
   ]),
   mcq("m4_names", "MCQ: In linear programming, x ≥ 0 and y ≥ 0 are called:", "کثیر انتخابی: خطی پروگرامنگ میں x ≥ 0 اور y ≥ 0 کہلاتے ہیں:", [
     opt("a", "non-negative constraints", "غیر منفی شرطیں", True, "Correct.", "درست۔"),
     opt("b", "the objective function", "مقصدی تفاعل", False, "The objective function is what you maximise or minimise, like z = 3x + 2y.", "مقصدی تفاعل وہ ہے جسے زیادہ یا کم کرتے ہیں، جیسے z = 3x + 2y۔"),
     opt("c", "the feasible region", "قابلِ عمل خطہ", False, "The feasible region is the area where all the constraints are true.", "قابلِ عمل خطہ وہ حصہ ہے جہاں سب شرطیں درست ہوں۔"),
     opt("d", "corner points", "کونے کے نقطے", False, "Corner points are where boundary lines meet.", "کونے کے نقطے وہاں ہیں جہاں حدی خطوط ملتے ہیں۔"),
   ]),
   mcq("m5_corner", "MCQ: The maximum or minimum of the objective function is found at:", "کثیر انتخابی: مقصدی تفاعل کی زیادہ سے زیادہ یا کم سے کم قیمت ملتی ہے:", [
     opt("a", "a corner point of the feasible region", "قابلِ عمل خطے کے کسی کونے پر", True, "Correct.", "درست۔"),
     opt("b", "the origin", "مبدا (0, 0) پر", False, "(0, 0) is only sometimes a corner, and only sometimes the best.", "(0, 0) صرف کبھی کبھی کونا ہوتا ہے، اور صرف کبھی کبھی بہترین۔"),
     opt("c", "the centre of the region", "خطے کے مرکز پر", False, "From the centre you can always move to a better point.", "مرکز سے ہمیشہ بہتر نقطے کی طرف جا سکتے ہیں۔"),
     opt("d", "any point of the region", "خطے کے کسی بھی نقطے پر", False, "Different points give different values; the best is at a corner.", "مختلف نقطے مختلف قیمتیں دیتے ہیں؛ بہترین کونے پر ہوتی ہے۔"),
   ]),
   {"id": "q1_fractions", "type": "text_check", "question_type": "exam_style", "checker": "linear_equation", "expected": "(x - 1)/3 = (x + 3)/5", "multiline": True,
    "prompt": T("Short question: Solve (x − 1)/3 = (x + 3)/5. Write each step on a new line.", "مختصر سوال: (x − 1)/3 = (x + 3)/5 حل کریں۔ ہر قدم نئی سطر میں لکھیں۔"),
    "hint": T("Multiply both sides by 15, the LCM of 3 and 5.", "دونوں طرف کو 15 سے ضرب دیں، جو 3 اور 5 کا ذو اضعاف اقل ہے۔"),
    "feedback_correct": T("Correct: x = 7. Check: (7 − 1)/3 = 2 and (7 + 3)/5 = 2.", "درست: x = 7۔ جانچ: (7 − 1)/3 = 2 اور (7 + 3)/5 = 2۔"),
    "feedback_wrong": T("Model answer: multiply by 15: 5(x − 1) = 3(x + 3). So 5x − 5 = 3x + 9. So 2x = 14. So x = 7.", "نمونہ جواب: 15 سے ضرب: 5(x − 1) = 3(x + 3)۔ پھر 5x − 5 = 3x + 9۔ پھر 2x = 14۔ پھر x = 7۔")},
   {"id": "q2_inequality", "type": "text_check", "question_type": "exam_style", "checker": "linear_inequality", "expected": "4 - 3x <= 13", "multiline": True,
    "prompt": T("Short question: Solve 4 − 3x ≤ 13. Write each step on a new line. (Type ≤ as <=.)", "مختصر سوال: 4 − 3x ≤ 13 حل کریں۔ ہر قدم نئی سطر میں لکھیں۔ (≤ کو <= لکھیں۔)"),
    "hint": T("Take 4 from both sides, then divide by −3 and flip the sign.", "دونوں طرف سے 4 گھٹائیں، پھر −3 سے تقسیم کریں اور علامت الٹیں۔"),
    "feedback_correct": T("Correct: x ≥ −3.", "درست: x ≥ −3۔"),
    "feedback_wrong": T("Model answer: 4 − 3x ≤ 13. Take 4 from both sides: −3x ≤ 9. Divide by −3 and reverse the sign: x ≥ −3.", "نمونہ جواب: 4 − 3x ≤ 13۔ دونوں طرف سے 4 گھٹائیں: −3x ≤ 9۔ −3 سے تقسیم کریں اور علامت الٹیں: x ≥ −3۔"),
    "common_wrong": [{"answer": "x <= -3", "misconception_id": "forgot_to_flip", "feedback": T("You divided by −3, so ≤ must turn into ≥.", "آپ نے −3 سے تقسیم کیا، اس لیے ≤ کو ≥ بننا چاہیے۔")}]},
   {"id": "q3_graph", "type": "sim", "question_type": "exam_style", "renderer": "native", "sim_id": "inequality_plane",
    "prompt": T("Short question: Graph x − 2y ≥ 4. Draw the line, choose solid or dashed, and shade the region.", "مختصر سوال: x − 2y ≥ 4 کا گراف بنائیں۔ خط بنائیں، سیدھی یا ٹوٹی لکیر چنیں، اور خطہ رنگیں۔"),
    "params": {"size": 5, "points": [[0, 0], [1, 1]]},
    "expected": {"result": "inequality", "checker": "linear_inequality_2d", "answer": "x - 2y >= 4"},
    "hint": T("The line goes through (4, 0) and (0, −2). Test (0, 0): 0 ≥ 4 is false.", "خط (4, 0) اور (0, −2) سے گزرتا ہے۔ (0, 0) آزمائیں: 0 ≥ 4 غلط ہے۔"),
    "feedback_correct": T("Correct! A solid line through (4, 0) and (0, −2), shaded away from (0, 0).", "درست! (4, 0) اور (0, −2) سے سیدھی لکیر، (0, 0) سے دور والی طرف رنگی ہوئی۔"),
    "feedback_wrong": T("Model answer: the line x − 2y = 4 goes through (4, 0) and (0, −2); ≥ means solid. (0, 0) gives 0 ≥ 4, false, so shade the side without (0, 0).", "نمونہ جواب: خط x − 2y = 4، (4, 0) اور (0, −2) سے گزرتا ہے؛ ≥ کا مطلب سیدھی لکیر۔ (0, 0) سے 0 ≥ 4، غلط، اس لیے وہ طرف رنگیں جس میں (0, 0) نہیں۔")},
   {"id": "q4_meet", "type": "text_check", "question_type": "exam_style", "checker": "points", "expected": "(3, 2)",
    "prompt": T("Short question: Find the point where 2x + y = 8 and x + y = 5 meet. Write it like (1, 2).", "مختصر سوال: وہ نقطہ معلوم کریں جہاں 2x + y = 8 اور x + y = 5 ملتے ہیں۔ (1, 2) کی طرح لکھیں۔"),
    "hint": T("Subtract the second equation from the first.", "پہلی مساوات میں سے دوسری گھٹائیں۔"),
    "feedback_correct": T("Correct: (3, 2).", "درست: (3, 2)۔"),
    "feedback_wrong": T("Model answer: subtracting gives x = 3. Then 3 + y = 5, so y = 2. The point is (3, 2).", "نمونہ جواب: تفریق سے x = 3۔ پھر 3 + y = 5، یعنی y = 2۔ نقطہ (3, 2) ہے۔")},
   {"id": "l1_layout", "type": "explain",
    "character": say("talking", "Long questions next. Here is how to set out a linear programming answer.", "اب تفصیلی سوال۔ خطی پروگرامنگ کا جواب ایسے لکھیں۔"),
    "text": T(
      "1) Write the constraints and change each to an equation to draw its line, with two points on it. 2) Draw all lines on one graph and shade the feasible region. 3) Find the corners (solve the equations where two lines meet). 4) Make a table of corners and the objective's value at each. 5) Write the answer: 'The minimum value is ... at (..., ...)'.",
      "1) شرطیں لکھیں اور ہر ایک کو مساوات بنا کر اس کے دو نقطوں سے خط بنائیں۔ 2) سب خطوط ایک گراف پر بنائیں اور قابلِ عمل خطہ رنگیں۔ 3) کونے معلوم کریں (جہاں دو خطوط ملیں، مساواتیں حل کریں)۔ 4) کونوں اور ہر ایک پر مقصدی تفاعل کی قیمت کا جدول بنائیں۔ 5) جواب لکھیں: 'کم سے کم قیمت ... ہے، (..., ...) پر'۔")},
   region_sim("l2_corners", L1,
     T("Long question: Minimise z = 2x + 3y subject to x + y ≥ 3, x ≤ 4, y ≤ 4, x ≥ 0, y ≥ 0. First, mark the corners of the feasible region.",
       "تفصیلی سوال: z = 2x + 3y کو کم سے کم کریں، شرائط x + y ≥ 3، x ≤ 4، y ≤ 4، x ≥ 0، y ≥ 0۔ پہلے قابلِ عمل خطے کے کونے نشان زد کریں۔"),
     T("The region has 5 corners. x + y ≥ 3 cuts off the corner at (0, 0).", "خطے کے 5 کونے ہیں۔ x + y ≥ 3، (0, 0) والا کونا کاٹ دیتا ہے۔"),
     T(f"Correct! {table(Z1, corners(L1))}.", f"درست! {table(Z1, corners(L1))}۔"),
     T(f"The corners are {corner_text(corners(L1))}. {table(Z1, corners(L1))}.", f"کونے {corner_text(corners(L1))} ہیں۔ {table(Z1, corners(L1))}۔"),
     x_max=5, y_max=5, objective=Z1, qtype="exam_style"),
   {"id": "l3_minimum", "type": "number", "question_type": "exam_style", "checker": "numeric", "answer": int(z1),
    "prompt": T("What is the minimum value of z = 2x + 3y?", "z = 2x + 3y کی کم سے کم قیمت کیا ہے؟"),
    "hint": T("Take the smallest value in your table.", "اپنے جدول میں سب سے چھوٹی قیمت لیں۔"),
    "feedback_correct": T(f"Correct! The minimum value is {num(z1)}, at (3, 0).", f"درست! کم سے کم قیمت {num(z1)} ہے، (3, 0) پر۔"),
    "feedback_wrong": T(f"Model answer: {table(Z1, corners(L1))}. The minimum value is {num(z1)} at (3, 0).", f"نمونہ جواب: {table(Z1, corners(L1))}۔ کم سے کم قیمت {num(z1)} ہے، (3, 0) پر۔"),
    "common_wrong": [{"answer": 20, "misconception_id": "max_min_mixed", "feedback": T("20 is the maximum. The question asks for the minimum.", "20 زیادہ سے زیادہ قیمت ہے۔ سوال کم سے کم مانگ رہا ہے۔")}]},
   {"id": "l4_notebook", "type": "photo_check", "question_type": "exam_style", "checker": "numeric", "expected": num(z2),
    "character": say("encouraging", "Last one: a full long question in your notebook, set out like the model answer.", "آخری سوال: پورا تفصیلی سوال اپنی کاپی میں، نمونہ جواب کی طرح۔"),
    "problem": T("Long question: Maximise z = 2x + 5y subject to x + y ≤ 6, x + 3y ≤ 12, x ≥ 0, y ≥ 0. Draw the graph, find the corners, make the table, and end with z = your answer. Then take a photo.",
                 "تفصیلی سوال: z = 2x + 5y کو زیادہ سے زیادہ کریں، شرائط x + y ≤ 6، x + 3y ≤ 12، x ≥ 0، y ≥ 0۔ گراف بنائیں، کونے معلوم کریں، جدول بنائیں، اور آخر میں z = آپ کا جواب لکھیں۔ پھر تصویر لیں۔"),
    "hint": T("The two slanted lines meet where x + y = 6 and x + 3y = 12: subtract to get 2y = 6.", "دونوں ترچھے خطوط وہاں ملتے ہیں جہاں x + y = 6 اور x + 3y = 12: تفریق سے 2y = 6۔"),
    "feedback_correct": T(f"Correct! The maximum is z = {num(z2)}, at (3, 3).", f"درست! زیادہ سے زیادہ z = {num(z2)}، (3, 3) پر۔"),
    "correct_working": T(f"Model answer: lines x + y = 6 through (6, 0) and (0, 6); x + 3y = 12 through (12, 0) and (0, 4). They meet at (3, 3). Corners: {corner_text(corners(L2))}. {table(Z2, corners(L2))}. The maximum value is z = {num(z2)} at (3, 3).",
                         f"نمونہ جواب: خط x + y = 6، (6, 0) اور (0, 6) سے؛ x + 3y = 12، (12, 0) اور (0, 4) سے۔ یہ (3, 3) پر ملتے ہیں۔ کونے: {corner_text(corners(L2))}۔ {table(Z2, corners(L2))}۔ زیادہ سے زیادہ قیمت z = {num(z2)}، (3, 3) پر۔"),
    "common_wrong": [{"answer": "20", "feedback": T("20 is at (0, 4). Did you find where the two slanted lines meet?", "20، (0, 4) پر ہے۔ کیا آپ نے دیکھا کہ دونوں ترچھے خطوط کہاں ملتے ہیں؟")}],
    "limit_per_day": 2, "max_attempts": 3},
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "Well done! Practise like this and the exam will feel easy.", "شاباش! ایسے مشق کریں تو امتحان آسان لگے گا۔"),
    "text": T("In the exam: show every step, check your answer by putting it back in, flip the sign when you multiply or divide an inequality by a negative number, and set out linear programming answers with a table of corners.",
              "امتحان میں: ہر قدم دکھائیں، جواب واپس رکھ کر جانچیں، نامساوات کو منفی عدد سے ضرب یا تقسیم کریں تو علامت الٹیں، اور خطی پروگرامنگ کے جواب کونوں کے جدول کے ساتھ لکھیں۔"),
    "points": [T("Label the axes and the lines on your graph.", "اپنے گراف پر محور اور خطوط کے نام لکھیں۔"),
               T("End with a sentence that answers the question.", "آخر میں ایک جملہ لکھیں جو سوال کا جواب دے۔")]},
 ],
 "teacher_notes": [
   "Written fresh for Phase 8 in the style of BISE Punjab Grade 9 papers (multiple choice, short and long questions). No past-paper questions were copied; please check that the marks and layout match your board's current paper.",
   "Every answer is checked by code: equations and inequalities line by line, graphs with the linear_inequality_2d checker, corners and objective values worked out by tools/plane.py. The notebook question checks the final value; the AI comments on the working.",
   "This practice set is offered after the unit's lessons (its prerequisites are the unit's skills).",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), ذو اضعاف اقل (LCM), مبدا (origin)."],
 "review": REVIEW,
 "review_questions": [{"id": "r_exam_min", "type": "exam_style", "skill": SKILL, "step": {
   "id": "r_exam_min", "type": "number", "checker": "numeric", "answer": int(z1),
   "prompt": T(f"The corners of a feasible region are {corner_text(corners(L1))}. Find the minimum of z = 2x + 3y.", f"ایک قابلِ عمل خطے کے کونے {corner_text(corners(L1))} ہیں۔ z = 2x + 3y کی کم سے کم قیمت معلوم کریں۔"),
   "hint": T("Work out 2x + 3y at each corner and take the smallest.", "ہر کونے پر 2x + 3y نکالیں اور سب سے چھوٹی لیں۔"),
   "feedback_correct": T(f"Correct: {num(z1)} at (3, 0).", f"درست: {num(z1)}، (3, 0) پر۔"),
   "feedback_wrong": T(f"{table(Z1, corners(L1))}. The minimum is {num(z1)}.", f"{table(Z1, corners(L1))}۔ کم سے کم {num(z1)} ہے۔")}}],
}
write(lesson)

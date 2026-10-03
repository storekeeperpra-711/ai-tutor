from common import T, opt, say, write, REF, REVIEW, corners, corner_text, region_sim, best, table, num, values

SKILL = "maths.linear_programming.optimize"

A = ["x + y <= 6", "x <= 4", "x >= 0", "y >= 0"]
ZA = "3x + 2y"
(pa, za) = best(ZA, corners(A))
assert (pa, za) == ((4, 2), 16)

B = ["x + y >= 2", "x <= 4", "y <= 3", "x >= 0", "y >= 0"]
ZB = "2x + 5y"
(pb, zb) = best(ZB, corners(B), biggest=False)
assert (pb, zb) == ((2, 0), 4), (pb, zb)

# Usman's mistake: z = x + 3y on region A.
ZU = "x + 3y"
(pu, zu) = best(ZU, corners(A))
assert (pu, zu) == ((0, 6), 18)
assert dict(values(ZU, corners(A)))[(4, 0)] == 4

# Notebook question.
N = ["x + y <= 5", "x <= 3", "x >= 0", "y >= 0"]
ZN = "5x + 4y"
(pn, zn) = best(ZN, corners(N))
assert (pn, zn) == ((3, 2), 23)

lesson = {
 "id": "g9-maths-05-linear-programming",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 9, "tier": "older",
 "curriculum_refs": [{"outcome": "Find the maximum or minimum value of a linear objective function over a feasible region, using its corner points.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Linear programming: the best corner", "خطی پروگرامنگ: بہترین کونا"),
 "estimated_minutes": 16,
 "prerequisites": [{"skill": "maths.inequalities.feasible_region"}],
 "misconceptions": [
   {"id": "farthest_point", "description": "Picks the corner farthest from the origin, or with the biggest x, instead of working out the objective at every corner."},
   {"id": "max_min_mixed", "description": "Gives the largest value when the question asks for the smallest (or the other way round)."},
   {"id": "inside_point", "description": "Thinks the best value can be at a point inside the region rather than at a corner."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["apply", "explain", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_max_value", "type": "apply", "step": {
     "id": "qb_max_value", "type": "number", "checker": "numeric", "answer": int(zn),
     "prompt": T(f"The corners of a region are {corner_text(corners(N))}. Find the maximum of z = 5x + 4y.", f"ایک خطے کے کونے {corner_text(corners(N))} ہیں۔ z = 5x + 4y کی زیادہ سے زیادہ قیمت معلوم کریں۔"),
     "hint": T("Work out 5x + 4y at each corner and pick the biggest.", "ہر کونے پر 5x + 4y نکالیں اور سب سے بڑی قیمت چنیں۔"),
     "feedback_correct": T(f"Correct: {num(zn)} at (3, 2).", f"درست: (3, 2) پر {num(zn)}۔"),
     "feedback_wrong": T(f"{table(ZN, corners(N))}. The biggest is {num(zn)}.", f"{table(ZN, corners(N))}۔ سب سے بڑی {num(zn)} ہے۔"),
     "common_wrong": [{"answer": 20, "misconception_id": "farthest_point", "feedback": T("20 is at (0, 5). Check (3, 2) too: 15 + 8.", "20، (0, 5) پر ہے۔ (3, 2) بھی جانچیں: 15 + 8۔")}]}},
   {"id": "qb_why_corner", "type": "explain", "step": {
     "id": "qb_why_corner", "type": "choice",
     "prompt": T("Why can't the largest value of z = 3x + 2y be at a point in the middle of the region?", "z = 3x + 2y کی سب سے بڑی قیمت خطے کے درمیان کسی نقطے پر کیوں نہیں ہو سکتی؟"),
     "options": [
       opt("a", "From a middle point you can always move right or up a little, and z gets bigger.", "درمیانی نقطے سے ہمیشہ تھوڑا دائیں یا اوپر جا سکتے ہیں، اور z بڑا ہو جاتا ہے۔", True,
           "Exactly! You keep going until you hit an edge, and then slide along it to a corner.", "بالکل! آپ کنارے تک جاتے ہیں، پھر اس کے ساتھ ساتھ کونے تک۔"),
       opt("b", "Because the middle point is always (0, 0).", "کیونکہ درمیانی نقطہ ہمیشہ (0, 0) ہوتا ہے۔", False,
           "The middle of the region isn't (0, 0). Think about moving a little from a point inside.", "خطے کا درمیان (0, 0) نہیں۔ سوچیں کہ اندر کے نقطے سے تھوڑا ہلیں تو کیا ہوتا ہے۔"),
       opt("c", "It can: the middle is often the best.", "ہو سکتی ہے: درمیان اکثر بہترین ہوتا ہے۔", False,
           "Try it: at (2, 1), z = 8. Move to (2, 2): z = 10. You could always do better.", "آزمائیں: (2, 1) پر z = 8۔ (2, 2) پر جائیں: z = 10۔ ہمیشہ بہتر ہو سکتا ہے۔", "inside_point"),
     ]}},
   {"id": "qb_find_error_min", "type": "find_error", "step": {
     "id": "qb_find_error_min", "type": "choice",
     "prompt": T(f"Asked for the minimum of z = 2x + 5y, with corners {corner_text(corners(B))}, Rabia answers 23. What went wrong?",
                 f"z = 2x + 5y کی کم سے کم قیمت پوچھی گئی، کونے {corner_text(corners(B))} ہیں، اور رابعہ کا جواب 23 ہے۔ غلطی کیا ہے؟"),
     "options": [
       opt("a", f"23 is the maximum. The minimum is {num(zb)}, at (2, 0).", f"23 زیادہ سے زیادہ قیمت ہے۔ کم سے کم {num(zb)} ہے، (2, 0) پر۔", True,
           "Right! Always read whether the question wants the biggest or the smallest.", "درست! ہمیشہ پڑھیں کہ سوال سب سے بڑی قیمت مانگ رہا ہے یا سب سے چھوٹی۔"),
       opt("b", "The minimum is 0, at (0, 0).", "کم سے کم 0 ہے، (0, 0) پر۔", False,
           "(0, 0) breaks x + y ≥ 2, so it isn't in the region.", "(0, 0)، x + y ≥ 2 کو توڑتا ہے، اس لیے خطے میں نہیں۔"),
       opt("c", "Nothing, 23 is right.", "کچھ نہیں، 23 درست ہے۔", False,
           "23 is at (4, 3). Is it the smallest value?", "23، (4, 3) پر ہے۔ کیا یہ سب سے چھوٹی قیمت ہے؟", "max_min_mixed"),
     ]}},
 ]},
 "home_tasks": [{"id": "h_best_buy", "text": T(
   "Think of a choice with limits at home, like buying apples and bananas with 200 rupees when the bag holds 10 fruits. Write the inequalities, find the corners, and decide which corner gives the most fruit or the most vitamins.",
   "گھر میں کسی ایسے انتخاب کا سوچیں جس پر حدیں ہوں، جیسے 200 روپے میں سیب اور کیلے خریدنا جبکہ تھیلے میں 10 پھل آتے ہیں۔ نامساوات لکھیں، کونے معلوم کریں، اور طے کریں کون سا کونا سب سے زیادہ پھل یا وٹامن دیتا ہے۔")}],
 "glossary": [T("Linear programming", "خطی پروگرامنگ"), T("Objective function", "مقصدی تفاعل"), T("Maximum", "زیادہ سے زیادہ (اعظم)"), T("Minimum", "کم سے کم (اقل)"), T("Optimal solution", "بہترین حل")],
 "steps": [
   {"id": "s1_best_choice", "type": "explain",
    "character": say("curious",
      "In the feasible region, every point is allowed. But which point is the best? That is linear programming!",
      "قابلِ عمل خطے میں ہر نقطے کی اجازت ہے۔ لیکن بہترین نقطہ کون سا ہے؟ یہی خطی پروگرامنگ ہے!"),
    "text": T(
      "We want to make a quantity, like profit z = 3x + 2y, as big as possible (or a cost as small as possible). This z is the objective function. The rule that makes it easy: the maximum and the minimum are always at a corner of the feasible region. So work out z at every corner and compare.",
      "ہم کسی مقدار، جیسے منافع z = 3x + 2y، کو زیادہ سے زیادہ (یا خرچ کو کم سے کم) کرنا چاہتے ہیں۔ یہ z مقصدی تفاعل ہے۔ کام آسان کرنے والا اصول: زیادہ سے زیادہ اور کم سے کم قیمت ہمیشہ قابلِ عمل خطے کے کسی کونے پر ہوتی ہے۔ اس لیے ہر کونے پر z نکالیں اور موازنہ کریں۔")},
   region_sim("s2_corners_with_z", A,
     T("Mark the corners of x + y ≤ 6, x ≤ 4, x ≥ 0, y ≥ 0. Each corner you mark shows z = 3x + 2y. Press Check when all are marked.",
       "x + y ≤ 6، x ≤ 4، x ≥ 0، y ≥ 0 کے کونے نشان زد کریں۔ ہر نشان زد کونا z = 3x + 2y دکھاتا ہے۔ سب نشان زد ہوں تو \"جانچیں\" دبائیں۔"),
     T("There are 4 corners, including (0, 0) and (4, 2).", "4 کونے ہیں، جن میں (0, 0) اور (4, 2) بھی ہیں۔"),
     T(f"Well done! {table(ZA, corners(A))}.", f"شاباش! {table(ZA, corners(A))}۔"),
     T(f"The corners are {corner_text(corners(A))}. {table(ZA, corners(A))}.", f"کونے {corner_text(corners(A))} ہیں۔ {table(ZA, corners(A))}۔"),
     x_max=7, y_max=7, objective=ZA),
   {"id": "s3_maximum", "type": "number", "question_type": "apply", "checker": "numeric", "answer": int(za),
    "prompt": T("What is the maximum value of z = 3x + 2y in this region?", "اس خطے میں z = 3x + 2y کی زیادہ سے زیادہ قیمت کیا ہے؟"),
    "hint": T("Compare z at the four corners and take the biggest.", "چاروں کونوں پر z کا موازنہ کریں اور سب سے بڑی لیں۔"),
    "feedback_correct": T(f"Correct! The maximum is {num(za)}, at (4, 2).", f"درست! زیادہ سے زیادہ {num(za)} ہے، (4, 2) پر۔"),
    "feedback_wrong": T(f"{table(ZA, corners(A))}. The biggest is {num(za)}, at (4, 2).", f"{table(ZA, corners(A))}۔ سب سے بڑی {num(za)} ہے، (4, 2) پر۔"),
    "common_wrong": [{"answer": 12, "misconception_id": "farthest_point", "feedback": T(
      "12 is z at (4, 0) and at (0, 6). Check every corner: what is z at (4, 2)?", "12، (4, 0) اور (0, 6) پر z ہے۔ ہر کونا جانچیں: (4, 2) پر z کیا ہے؟")}]},
   {"id": "s4_why_corners", "type": "choice", "question_type": "explain",
    "prompt": T("Why do we only need to check the corners, not every point in the region?", "ہمیں صرف کونے کیوں جانچنے ہیں، خطے کا ہر نقطہ کیوں نہیں؟"),
    "options": [
      opt("a", "Moving in a straight line changes z steadily, so the best value is at an end of an edge: a corner.", "سیدھی لائن میں چلنے سے z یکساں بدلتا ہے، اس لیے بہترین قیمت کسی کنارے کے سرے پر، یعنی کونے پر، ہوتی ہے۔", True,
          "Exactly! z keeps growing in one direction, so it is biggest where the region ends.", "بالکل! z ایک سمت میں بڑھتا رہتا ہے، اس لیے یہ وہاں سب سے بڑا ہے جہاں خطہ ختم ہوتا ہے۔"),
      opt("b", "Because corners are easy to calculate.", "کیونکہ کونوں کا حساب آسان ہے۔", False,
          "They are easy, but that isn't the reason. Think about what happens to z along an edge.", "آسان تو ہیں، مگر وجہ یہ نہیں۔ سوچیں کنارے کے ساتھ z کا کیا ہوتا ہے۔"),
      opt("c", "Because the region has no points inside.", "کیونکہ خطے کے اندر کوئی نقطہ نہیں۔", False,
          "There are lots of points inside, like (2, 1). They just can't beat the best corner.", "اندر بہت سے نقطے ہیں، جیسے (2, 1)۔ وہ بس بہترین کونے سے آگے نہیں جا سکتے۔", "inside_point"),
    ]},
   region_sim("s5_corners_for_min", B,
     T("A new region: x + y ≥ 2, x ≤ 4, y ≤ 3, x ≥ 0, y ≥ 0. Mark its corners; each shows z = 2x + 5y.",
       "نیا خطہ: x + y ≥ 2، x ≤ 4، y ≤ 3، x ≥ 0، y ≥ 0۔ اس کے کونے نشان زد کریں؛ ہر ایک z = 2x + 5y دکھاتا ہے۔"),
     T("x + y ≥ 2 cuts off the corner at (0, 0), so the region has 5 corners.", "x + y ≥ 2، (0, 0) والا کونا کاٹ دیتا ہے، اس لیے خطے کے 5 کونے ہیں۔"),
     T(f"Well done! {table(ZB, corners(B))}.", f"شاباش! {table(ZB, corners(B))}۔"),
     T(f"The corners are {corner_text(corners(B))}. (0, 0) is not in the region: 0 + 0 is less than 2.", f"کونے {corner_text(corners(B))} ہیں۔ (0, 0) خطے میں نہیں: 0 + 0، 2 سے کم ہے۔"),
     x_max=5, y_max=4, objective=ZB),
   {"id": "s6_minimum", "type": "number", "question_type": "apply", "checker": "numeric", "answer": int(zb),
    "prompt": T("What is the minimum value of z = 2x + 5y in this region?", "اس خطے میں z = 2x + 5y کی کم سے کم قیمت کیا ہے؟"),
    "hint": T("This time take the smallest value at the corners.", "اس بار کونوں پر سب سے چھوٹی قیمت لیں۔"),
    "feedback_correct": T(f"Correct! The minimum is {num(zb)}, at (2, 0).", f"درست! کم سے کم {num(zb)} ہے، (2, 0) پر۔"),
    "feedback_wrong": T(f"{table(ZB, corners(B))}. The smallest is {num(zb)}, at (2, 0).", f"{table(ZB, corners(B))}۔ سب سے چھوٹی {num(zb)} ہے، (2, 0) پر۔"),
    "common_wrong": [
      {"answer": 23, "misconception_id": "max_min_mixed", "feedback": T("23 is the biggest value. The question asks for the smallest.", "23 سب سے بڑی قیمت ہے۔ سوال سب سے چھوٹی مانگ رہا ہے۔")},
      {"answer": 0, "feedback": T("(0, 0) is not in this region: x + y ≥ 2 is false there.", "(0, 0) اس خطے میں نہیں: وہاں x + y ≥ 2 غلط ہے۔")}]},
   {"id": "s7_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("For the region x + y ≤ 6, x ≤ 4, x ≥ 0, y ≥ 0, Usman says z = x + 3y is biggest at (4, 0), because x is biggest there. What is wrong?",
                "خطہ x + y ≤ 6، x ≤ 4، x ≥ 0، y ≥ 0 کے لیے عثمان کہتا ہے کہ z = x + 3y، (4, 0) پر سب سے بڑا ہے، کیونکہ وہاں x سب سے بڑا ہے۔ غلطی کیا ہے؟"),
    "options": [
      opt("check_all", f"He didn't work out z at every corner. At (4, 0), z = 4, but at (0, 6), z = {num(zu)}.", f"اس نے ہر کونے پر z نہیں نکالا۔ (4, 0) پر z = 4، مگر (0, 6) پر z = {num(zu)}۔", True,
          "Right! y counts 3 times in z, so the corner with the most y wins here.", "درست! z میں y تین گنا گنا جاتا ہے، اس لیے یہاں سب سے زیادہ y والا کونا جیتتا ہے۔"),
      opt("inside", "The maximum is inside the region, not at a corner.", "زیادہ سے زیادہ قیمت خطے کے اندر ہے، کونے پر نہیں۔", False,
          "The maximum is always at a corner. The mistake is which corner.", "زیادہ سے زیادہ قیمت ہمیشہ کونے پر ہوتی ہے۔ غلطی یہ ہے کہ کون سا کونا۔", "inside_point"),
      opt("nothing", "Nothing, (4, 0) is right.", "کچھ نہیں، (4, 0) درست ہے۔", False,
          "Work out z = x + 3y at (0, 6).", "(0, 6) پر z = x + 3y نکالیں۔", "farthest_point"),
    ]},
   {"id": "s8_notebook", "type": "photo_check", "question_type": "apply", "checker": "numeric", "expected": num(zn),
    "character": say("encouraging", "Notebook time! Show every corner and its value, like in the exam.", "کاپی کا وقت! ہر کونا اور اس کی قیمت لکھیں، جیسے امتحان میں۔"),
    "problem": T("In your notebook, maximise z = 5x + 4y subject to x + y ≤ 5, x ≤ 3, x ≥ 0, y ≥ 0. Draw the region, list the corners with z at each, and end with z = your answer. Then take a photo.",
                 "اپنی کاپی میں z = 5x + 4y کو زیادہ سے زیادہ کریں، شرائط x + y ≤ 5، x ≤ 3، x ≥ 0، y ≥ 0 کے ساتھ۔ خطہ بنائیں، کونے اور ہر ایک پر z لکھیں، اور آخر میں z = آپ کا جواب لکھیں۔ پھر تصویر لیں۔"),
    "hint": T("The corners are where the lines meet: (0, 0), (3, 0), (3, 2) and (0, 5).", "کونے وہاں ہیں جہاں خطوط ملتے ہیں: (0, 0)، (3, 0)، (3, 2) اور (0, 5)۔"),
    "feedback_correct": T(f"Correct! The maximum is z = {num(zn)}, at (3, 2).", f"درست! زیادہ سے زیادہ z = {num(zn)}، (3, 2) پر۔"),
    "correct_working": T(f"Corners: {corner_text(corners(N))}. {table(ZN, corners(N))}. Maximum: z = {num(zn)} at (3, 2).",
                         f"کونے: {corner_text(corners(N))}۔ {table(ZN, corners(N))}۔ زیادہ سے زیادہ: z = {num(zn)}، (3, 2) پر۔"),
    "common_wrong": [{"answer": "20", "misconception_id": "farthest_point", "feedback": T("20 is at (0, 5). Did you check (3, 2)?", "20، (0, 5) پر ہے۔ کیا آپ نے (3, 2) جانچا؟")}],
    "limit_per_day": 2, "max_attempts": 3},
   {"id": "s9_summary", "type": "summary",
    "character": say("celebrating", "Now you can find the best choice with linear programming!", "اب آپ خطی پروگرامنگ سے بہترین انتخاب ڈھونڈ سکتے ہیں!"),
    "text": T("To find the maximum or minimum of an objective function: draw the feasible region, find its corners, work out the function at every corner, and pick the biggest or the smallest.",
              "مقصدی تفاعل کی زیادہ سے زیادہ یا کم سے کم قیمت کے لیے: قابلِ عمل خطہ بنائیں، اس کے کونے معلوم کریں، ہر کونے پر تفاعل کی قیمت نکالیں، اور سب سے بڑی یا سب سے چھوٹی چنیں۔"),
    "points": [T("Make a table of corners and values: it's easy to check and examiners like it.", "کونوں اور قیمتوں کا جدول بنائیں: جانچنا آسان ہے اور ممتحن اسے پسند کرتے ہیں۔"),
               T("Read the question again: maximum or minimum?", "سوال دوبارہ پڑھیں: زیادہ سے زیادہ یا کم سے کم؟")]},
 ],
 "teacher_notes": [
   "Written fresh for Phase 8. No textbook text or exercises were copied.",
   "Urdu terms to check against the PCTB book: خطی پروگرامنگ (linear programming), مقصدی تفاعل (objective function), زیادہ سے زیادہ / کم سے کم (maximum / minimum; the book may say اعظم / اقل).",
   "Every corner and value in this lesson is worked out by a script from the inequalities (tools/plane.py), not typed by hand. The feasible_region interactive shows the objective's value at each corner the student marks.",
   "The notebook step reads the student's photo; the code checks only the final value (z = 23), and the AI comments on the working.",
   "Next lesson: word problems (writing the inequalities from a story)."],
 "review": REVIEW,
 "review_questions": [{"id": "r_max", "type": "apply", "skill": SKILL, "step": {
   "id": "r_max", "type": "number", "checker": "numeric", "answer": int(zu),
   "prompt": T(f"The corners of a region are {corner_text(corners(A))}. Find the maximum of z = x + 3y.", f"ایک خطے کے کونے {corner_text(corners(A))} ہیں۔ z = x + 3y کی زیادہ سے زیادہ قیمت معلوم کریں۔"),
   "hint": T("Work out x + 3y at each corner.", "ہر کونے پر x + 3y نکالیں۔"),
   "feedback_correct": T(f"Correct: {num(zu)}, at (0, 6).", f"درست: {num(zu)}، (0, 6) پر۔"),
   "feedback_wrong": T(f"{table(ZU, corners(A))}. The biggest is {num(zu)}.", f"{table(ZU, corners(A))}۔ سب سے بڑی {num(zu)} ہے۔")}}],
}
write(lesson)

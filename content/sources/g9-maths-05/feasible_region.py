from common import T, opt, say, write, REF, REVIEW, corners, corner_text, region_sim

SKILL = "maths.inequalities.feasible_region"

A = ["x + y <= 6", "x <= 4", "x >= 0", "y >= 0"]
B = ["x + 2y <= 8", "x + y <= 6", "x >= 0", "y >= 0"]
C = ["2x + y <= 8", "y <= 4", "x >= 0", "y >= 0"]
assert corner_text(corners(A)) == "(0, 0), (0, 6), (4, 0), (4, 2)"
assert corner_text(corners(B)) == "(0, 0), (0, 4), (4, 2), (6, 0)"
assert corner_text(corners(C)) == "(0, 0), (0, 4), (2, 4), (4, 0)"

lesson = {
 "id": "g9-maths-05-feasible-region",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 9, "tier": "older",
 "curriculum_refs": [{"outcome": "Graph a system of linear inequalities in two variables, find the feasible region and its corner points.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("The feasible region and its corners", "قابلِ عمل خطہ اور اس کے کونے"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": "maths.inequalities.two_variable"}],
 "misconceptions": [
   {"id": "one_constraint_only", "description": "Checks a point in one inequality only instead of all of them."},
   {"id": "corner_outside", "description": "Takes a crossing point of two boundary lines as a corner even though it breaks another inequality."},
   {"id": "forgets_axes", "description": "Forgets the corners on the axes, such as (0, 0)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["apply", "explain", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_corners", "type": "apply", "step": region_sim("qb_corners", C,
     T("Mark every corner of the region for 2x + y ≤ 8, y ≤ 4, x ≥ 0, y ≥ 0, then press Check.", "2x + y ≤ 8، y ≤ 4، x ≥ 0، y ≥ 0 کے خطے کے سب کونے نشان زد کریں، پھر \"جانچیں\" دبائیں۔"),
     T("Where does 2x + y = 8 meet y = 4? Put y = 4 in: 2x + 4 = 8.", "2x + y = 8 اور y = 4 کہاں ملتے ہیں؟ y = 4 رکھیں: 2x + 4 = 8۔"),
     T(f"Correct: {corner_text(corners(C))}.", f"درست: {corner_text(corners(C))}۔"),
     T(f"The corners are {corner_text(corners(C))}. (2, 4) is where 2x + y = 8 meets y = 4.", f"کونے {corner_text(corners(C))} ہیں۔ (2, 4) وہاں ہے جہاں 2x + y = 8، y = 4 سے ملتا ہے۔"),
     x_max=6, y_max=8)},
   {"id": "qb_why_all", "type": "explain", "step": {
     "id": "qb_why_all", "type": "choice",
     "prompt": T("Why is the feasible region only the part where all the shadings overlap?", "قابلِ عمل خطہ صرف وہ حصہ کیوں ہے جہاں سب رنگ ایک دوسرے پر آتے ہیں؟"),
     "options": [
       opt("a", "Because a point must make every inequality true at the same time.", "کیونکہ نقطے کو سب نامساوات ایک ساتھ درست کرنی ہوتی ہیں۔", True,
           "Exactly! Breaking even one condition is not allowed.", "بالکل! ایک شرط توڑنا بھی منع ہے۔"),
       opt("b", "Because it is the biggest part of the graph.", "کیونکہ یہ گراف کا سب سے بڑا حصہ ہے۔", False,
           "Size doesn't matter. Think about what each inequality asks.", "سائز سے فرق نہیں پڑتا۔ سوچیں ہر نامساوات کیا مانگتی ہے۔"),
       opt("c", "Because a point only needs to make one inequality true.", "کیونکہ نقطے کو صرف ایک نامساوات درست کرنی ہوتی ہے۔", False,
           "Then Ayesha could study 10 hours just because 10 ≥ 0! All the conditions must hold.", "پھر تو عائشہ 10 گھنٹے پڑھ سکتی کیونکہ 10 ≥ 0! سب شرطیں پوری ہونی چاہئیں۔", "one_constraint_only"),
     ]}},
   {"id": "qb_find_error_corner", "type": "find_error", "step": {
     "id": "qb_find_error_corner", "type": "choice",
     "prompt": T("For x + 2y ≤ 8, x + y ≤ 6, x ≥ 0, y ≥ 0, Zain lists the corners (0, 0), (6, 0), (4, 2), (0, 6). What is wrong?",
                 "x + 2y ≤ 8، x + y ≤ 6، x ≥ 0، y ≥ 0 کے لیے زین کونے (0, 0)، (6, 0)، (4, 2)، (0, 6) لکھتا ہے۔ غلطی کیا ہے؟"),
     "options": [
       opt("a", "(0, 6) breaks x + 2y ≤ 8: 0 + 12 = 12. The corner on the y-axis is (0, 4).", "(0, 6)، x + 2y ≤ 8 کو توڑتا ہے: 0 + 12 = 12۔ y محور پر کونا (0, 4) ہے۔", True,
           "Right! A corner must make every inequality true.", "درست! کونے کو ہر نامساوات درست کرنی چاہیے۔"),
       opt("b", "(4, 2) is not a corner.", "(4, 2) کونا نہیں۔", False,
           "Check: 4 + 4 = 8 and 4 + 2 = 6. It is on both lines, so it is a corner.", "جانچیں: 4 + 4 = 8 اور 4 + 2 = 6۔ یہ دونوں خطوط پر ہے، اس لیے کونا ہے۔"),
       opt("c", "Nothing is wrong.", "کوئی غلطی نہیں۔", False,
           "Put (0, 6) into x + 2y ≤ 8.", "(0, 6) کو x + 2y ≤ 8 میں رکھیں۔", "corner_outside"),
     ]}},
 ]},
 "home_tasks": [{"id": "h_draw_region", "text": T(
   "On squared paper, draw x + y ≤ 5, x ≤ 3, x ≥ 0 and y ≥ 0 on one graph. Shade the feasible region and write down its corners. Check each corner in all four inequalities.",
   "خانوں والے کاغذ پر ایک ہی گراف میں x + y ≤ 5، x ≤ 3، x ≥ 0 اور y ≥ 0 بنائیں۔ قابلِ عمل خطہ رنگیں اور اس کے کونے لکھیں۔ ہر کونے کو چاروں نامساوات میں جانچیں۔")}],
 "glossary": [T("System of inequalities", "نامساوات کا نظام"), T("Feasible region", "قابلِ عمل خطہ"), T("Corner point", "کونے کا نقطہ"), T("Non-negative", "غیر منفی"), T("Constraint", "قید (شرط)")],
 "steps": [
   {"id": "s1_many_rules", "type": "explain",
    "character": say("curious",
      "Ayesha has at most 6 hours, and at most 4 hours can be maths. Now two rules must be true together!",
      "عائشہ کے پاس زیادہ سے زیادہ 6 گھنٹے ہیں، اور ریاضی زیادہ سے زیادہ 4 گھنٹے ہو سکتی ہے۔ اب دو اصول ایک ساتھ درست ہونے چاہئیں!"),
    "text": T(
      "x + y ≤ 6 and x ≤ 4. Hours can't be negative, so also x ≥ 0 and y ≥ 0 (the non-negative constraints). Drawn together, the part of the graph where all of them are true is called the feasible region. A point is in it only if it makes every inequality true.",
      "x + y ≤ 6 اور x ≤ 4۔ گھنٹے منفی نہیں ہو سکتے، اس لیے x ≥ 0 اور y ≥ 0 بھی (غیر منفی شرطیں)۔ سب کو ایک ساتھ بنائیں تو گراف کا وہ حصہ جہاں سب درست ہوں قابلِ عمل خطہ کہلاتا ہے۔ کوئی نقطہ اس میں تبھی ہے جب وہ ہر نامساوات کو درست کرے۔")},
   {"id": "s2_which_point", "type": "choice", "question_type": "apply",
    "prompt": T("Which point is in the feasible region of x + y ≤ 6, x ≤ 4, x ≥ 0, y ≥ 0?", "x + y ≤ 6، x ≤ 4، x ≥ 0، y ≥ 0 کے قابلِ عمل خطے میں کون سا نقطہ ہے؟"),
    "options": [
      opt("in", "(3, 2)", "(3, 2)", True,
          "Yes! 3 + 2 = 5 ≤ 6, 3 ≤ 4, and both are not negative.", "جی ہاں! 3 + 2 = 5 ≤ 6، 3 ≤ 4، اور دونوں منفی نہیں۔"),
      opt("too_much_maths", "(5, 1)", "(5, 1)", False,
          "5 + 1 = 6 is fine, but x = 5 breaks x ≤ 4. Every inequality must be true.", "5 + 1 = 6 ٹھیک ہے، مگر x = 5، x ≤ 4 کو توڑتا ہے۔ ہر نامساوات درست ہونی چاہیے۔", "one_constraint_only"),
      opt("negative", "(−1, 3)", "(−1, 3)", False,
          "x = −1 breaks x ≥ 0: Ayesha can't study for −1 hours!", "x = −1، x ≥ 0 کو توڑتا ہے: عائشہ −1 گھنٹے نہیں پڑھ سکتی!", "one_constraint_only"),
    ]},
   {"id": "s3_corners", "type": "explain",
    "character": say("talking", "The corners of the region are very important. Next lesson shows why!", "خطے کے کونے بہت اہم ہیں۔ اگلا سبق بتائے گا کیوں!"),
    "text": T(
      "The feasible region has straight edges, and its corners are where two boundary lines meet. Some corners are easy, on the axes, like (0, 0). For the others, solve the two line equations together. For example, x + y = 6 and x = 4 meet where 4 + y = 6, so y = 2: the corner is (4, 2).",
      "قابلِ عمل خطے کے کنارے سیدھے ہیں، اور اس کے کونے وہاں ہیں جہاں دو حدی خطوط ملتے ہیں۔ کچھ کونے آسان ہیں، محوروں پر، جیسے (0, 0)۔ باقی کے لیے دونوں خطوط کی مساواتیں ایک ساتھ حل کریں۔ مثلاً x + y = 6 اور x = 4 وہاں ملتے ہیں جہاں 4 + y = 6، یعنی y = 2: کونا (4, 2) ہے۔")},
   region_sim("s4_mark_corners", A,
     T("Here is the region for x + y ≤ 6, x ≤ 4, x ≥ 0, y ≥ 0. Tap each of its corners, then press Check.", "یہ x + y ≤ 6، x ≤ 4، x ≥ 0، y ≥ 0 کا خطہ ہے۔ اس کے ہر کونے پر ٹیپ کریں، پھر \"جانچیں\" دبائیں۔"),
     T("There are 4 corners. Don't forget (0, 0), and the corner where x + y = 6 meets x = 4.", "4 کونے ہیں۔ (0, 0) اور وہ کونا مت بھولیں جہاں x + y = 6، x = 4 سے ملتا ہے۔"),
     T(f"Well done! The corners are {corner_text(corners(A))}.", f"شاباش! کونے {corner_text(corners(A))} ہیں۔"),
     T(f"The corners are {corner_text(corners(A))}.", f"کونے {corner_text(corners(A))} ہیں۔"),
     x_max=7, y_max=7),
   {"id": "s5_solve_corner", "type": "text_check", "question_type": "apply", "checker": "points", "expected": "(4, 2)",
    "prompt": T("Where do the lines x + 2y = 8 and x + y = 6 meet? Write the point like (1, 2).", "خطوط x + 2y = 8 اور x + y = 6 کہاں ملتے ہیں؟ نقطہ (1, 2) کی طرح لکھیں۔"),
    "hint": T("Take the second equation from the first: (x + 2y) − (x + y) = 8 − 6, so y = 2.", "پہلی مساوات میں سے دوسری گھٹائیں: (x + 2y) − (x + y) = 8 − 6، یعنی y = 2۔"),
    "feedback_correct": T("Correct! (4, 2): 4 + 4 = 8 and 4 + 2 = 6.", "درست! (4, 2): 4 + 4 = 8 اور 4 + 2 = 6۔"),
    "feedback_wrong": T("Subtract: y = 2. Then x + 2 = 6, so x = 4. They meet at (4, 2).", "تفریق کریں: y = 2۔ پھر x + 2 = 6، یعنی x = 4۔ یہ (4, 2) پر ملتے ہیں۔"),
    "common_wrong": [{"answer": "(2, 4)", "feedback": T("x and y are swapped: (x, y) means x first. Check x + 2y with (2, 4): 2 + 8 = 10, not 8.", "x اور y الٹ گئے: (x, y) میں پہلے x آتا ہے۔ (2, 4) سے x + 2y جانچیں: 2 + 8 = 10، نہ کہ 8۔")}]},
   region_sim("s6_mark_corners", B,
     T("Now the region for x + 2y ≤ 8, x + y ≤ 6, x ≥ 0, y ≥ 0. Mark all its corners.", "اب x + 2y ≤ 8، x + y ≤ 6، x ≥ 0، y ≥ 0 کا خطہ۔ اس کے سب کونے نشان زد کریں۔"),
     T("You found one corner already: (4, 2). Where does each line meet the axes, inside the region?", "ایک کونا آپ ڈھونڈ چکے: (4, 2)۔ ہر خط محوروں سے کہاں ملتا ہے، خطے کے اندر؟"),
     T(f"Excellent! The corners are {corner_text(corners(B))}.", f"زبردست! کونے {corner_text(corners(B))} ہیں۔"),
     T(f"The corners are {corner_text(corners(B))}. (0, 6) is not one: it breaks x + 2y ≤ 8.", f"کونے {corner_text(corners(B))} ہیں۔ (0, 6) کونا نہیں: یہ x + 2y ≤ 8 کو توڑتا ہے۔"),
     x_max=9, y_max=7),
   {"id": "s7_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("For x + y ≤ 6, x ≤ 4, x ≥ 0, y ≥ 0, Hina says the corners are (0, 0), (4, 0), (0, 6) and (4, 6). What is wrong?",
                "x + y ≤ 6، x ≤ 4، x ≥ 0، y ≥ 0 کے لیے حنا کہتی ہے کونے (0, 0)، (4, 0)، (0, 6) اور (4, 6) ہیں۔ غلطی کیا ہے؟"),
    "options": [
      opt("outside", "(4, 6) breaks x + y ≤ 6. The real corner is (4, 2).", "(4, 6)، x + y ≤ 6 کو توڑتا ہے۔ اصل کونا (4, 2) ہے۔", True,
          "Right! 4 + 6 = 10. She drew a rectangle and forgot the slanted line.", "درست! 4 + 6 = 10۔ اس نے مستطیل بنا لیا اور ترچھا خط بھول گئی۔"),
      opt("origin", "(0, 0) is not a corner.", "(0, 0) کونا نہیں۔", False,
          "(0, 0) is where x = 0 meets y = 0, and it makes all four true.", "(0, 0) وہاں ہے جہاں x = 0، y = 0 سے ملتا ہے، اور یہ چاروں کو درست کرتا ہے۔", "forgets_axes"),
      opt("nothing", "Nothing, those are the corners.", "کوئی غلطی نہیں، یہی کونے ہیں۔", False,
          "Put (4, 6) into x + y ≤ 6.", "(4, 6) کو x + y ≤ 6 میں رکھیں۔", "corner_outside"),
    ]},
   {"id": "s8_explain_region", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "task": T("Explain how you would check whether a point, like (3, 4), is in the feasible region of several inequalities, and why.",
              "سمجھائیں کہ آپ کیسے جانچیں گے کہ کوئی نقطہ، جیسے (3, 4)، کئی نامساوات کے قابلِ عمل خطے میں ہے یا نہیں، اور کیوں۔"),
    "key_idea": "Put the point's x and y into every inequality. It is in the feasible region only if every inequality is true; if even one is false, it is outside. The feasible region is where all the conditions hold at the same time.",
    "levels": {
      "got_it": "Puts the point into each inequality and says it must make all of them true (one false is enough to be outside), because the region is where all conditions hold together.",
      "partly": "Says to put the point into the inequalities but not that all must be true, or checks only one.",
      "not_yet": "Judges by looking (e.g. 'near the origin') or gives no method."},
    "keywords": [
      ["put", "substitute", "check", "test", "رکھ", "آزما", "جانچ", "rakh", "check kar", "aazma"],
      ["every", "all", "each", "both", "سب", "ہر", "تمام", "sab", "har", "tamam"],
      ["true", "false", "satisfy", "درست", "غلط", "sahi", "ghalat", "durust"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Every inequality must be true for the point to be in the region.", "بہت خوب! نقطہ خطے میں تبھی ہے جب ہر نامساوات درست ہو۔"),
      "partly": T("Good start! Must the point satisfy one inequality, or all of them?", "اچھا آغاز! کیا نقطے کو ایک نامساوات پوری کرنی ہے، یا سب؟"),
      "not_yet": T("Try it: put (3, 4) into x + y ≤ 6. True or false? What does that mean for the region?", "آزمائیں: (3, 4) کو x + y ≤ 6 میں رکھیں۔ درست یا غلط؟ خطے کے لیے اس کا کیا مطلب ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s9_summary", "type": "summary",
    "character": say("celebrating", "Great work! You can find a feasible region and its corners.", "بہت اچھا! آپ قابلِ عمل خطہ اور اس کے کونے ڈھونڈ سکتے ہیں۔"),
    "text": T("Draw every inequality on one graph. The feasible region is where all of them are true. Its corners are where two boundary lines meet; check each corner in every inequality.",
              "ہر نامساوات ایک ہی گراف پر بنائیں۔ قابلِ عمل خطہ وہ ہے جہاں سب درست ہوں۔ اس کے کونے وہاں ہیں جہاں دو حدی خطوط ملتے ہیں؛ ہر کونے کو ہر نامساوات میں جانچیں۔"),
    "points": [T("x ≥ 0 and y ≥ 0 keep the region in the first quarter of the graph.", "x ≥ 0 اور y ≥ 0 خطے کو گراف کے پہلے حصے (ربع) میں رکھتے ہیں۔"),
               T("Not every crossing of two lines is a corner: it must be inside all the other inequalities too.", "دو خطوط کا ہر ملاپ کونا نہیں: اسے باقی سب نامساوات کے اندر بھی ہونا چاہیے۔")]},
 ],
 "teacher_notes": [
   "Written fresh for Phase 8. No textbook text or exercises were copied.",
   "Urdu terms to check against the PCTB book: قابلِ عمل خطہ (feasible region), کونے کا نقطہ (corner point; the book may say راس), غیر منفی شرطیں (non-negative constraints), قید (constraint).",
   "Corner steps use the new feasible_region interactive: the region is drawn from the inequalities, and the student taps the corners. tools/validate_lessons.py works out the corners from the inequalities and fails if the lesson's answer differs, so a typing mistake in a corner can't reach students.",
   "Next lesson: linear programming (the biggest or smallest value at a corner)."],
 "review": REVIEW,
 "review_questions": [{"id": "r_meet", "type": "apply", "skill": SKILL, "step": {
   "id": "r_meet", "type": "text_check", "checker": "points", "expected": "(3, 2)",
   "prompt": T("Where do the lines 2x + y = 8 and x + y = 5 meet? Write the point like (1, 2).", "خطوط 2x + y = 8 اور x + y = 5 کہاں ملتے ہیں؟ نقطہ (1, 2) کی طرح لکھیں۔"),
   "hint": T("Take the second equation from the first: x = 3.", "پہلی مساوات میں سے دوسری گھٹائیں: x = 3۔"),
   "feedback_correct": T("Correct: (3, 2). 6 + 2 = 8 and 3 + 2 = 5.", "درست: (3, 2)۔ 6 + 2 = 8 اور 3 + 2 = 5۔"),
   "feedback_wrong": T("Subtract: x = 3. Then 3 + y = 5, so y = 2. The point is (3, 2).", "تفریق کریں: x = 3۔ پھر 3 + y = 5، یعنی y = 2۔ نقطہ (3, 2) ہے۔")}}],
}
write(lesson)

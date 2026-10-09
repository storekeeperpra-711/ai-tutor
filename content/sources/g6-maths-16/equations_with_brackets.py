from common import (T, opt, say, wrong, number_question, write, solves,
                    REF, REVIEW, WN_PROPERTIES, EQ_TWO_STEP, EQ_BRACKETS)

SKILL = EQ_BRACKETS

# s2: 4 x (6 + 2) = 4 x 6 + 4 x 2 (multiplying only the 6: 26)
S2 = 4 * 6 + 4 * 2
assert S2 == 32 and 4 * 6 + 2 == 26
# s4: 3(x + 2) = 21 (stopping at x + 2: 7)
S4 = 21 // 3 - 2
assert solves("3(x + 2) = 21", x=S4) and S4 == 5
# s5: 2(y - 3) = 10 (stopping: 5; subtracting 3: 2)
S5 = 10 // 2 + 3
assert solves("2(y − 3) = 10", y=S5) and S5 == 8 and 10 // 2 - 3 == 2
# s6: 4(m + 1) = 4m + 4
assert all(solves("4(m + 1) = 4m + 4", m=m) for m in range(5))
# s7: 5(n + 4) = 35 (stopping: 7)
S7 = 35 // 5 - 4
assert solves("5(n + 4) = 35", n=S7) and S7 == 3
# s8: (x + 6) / 2 = 9 (ignoring brackets: x + 3 = 9 gives 6)
S8 = 9 * 2 - 6
assert solves("(x + 6) ÷ 2 = 9", x=S8) and S8 == 12 and solves("x + 6 ÷ 2 = 9", x=6)
# s9: 3(x + 5) = 27 gives x = 4
assert solves("3(x + 5) = 27", x=4) and solves("3x + 15 = 27", x=4)
# s11: 6(k - 2) = 30 (stopping: 5; subtracting: 3)
S11 = 30 // 6 + 2
assert solves("6(k − 2) = 30", k=S11) and S11 == 7
# question bank and review
QB = 42 // 7 - 1
assert solves("7(a + 1) = 42", a=QB) and QB == 5
assert solves("2(x + 4) = 14", x=3) and solves("2x + 8 = 14", x=3)
R1 = 18 // 2 - 5
assert solves("2(x + 5) = 18", x=R1) and R1 == 4
R2 = 12 // 3 + 1
assert solves("3(y − 1) = 12", y=R2) and R2 == 5

lesson = {
 "id": "g6-maths-16-equations-with-brackets",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve linear equations with brackets, like 3(x + 2) = 21, by dividing first or by multiplying out the brackets.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Equations with brackets", "قوسین والی مساوات"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": EQ_TWO_STEP}, {"skill": WN_PROPERTIES}],
 "misconceptions": [
   {"id": "stops_at_bracket", "description": "Finds the value of the bracket (like x + 2 = 7) and gives that as x."},
   {"id": "partial_expand", "description": "Multiplies only the first term: 3(x + 5) becomes 3x + 5."},
   {"id": "wrong_inverse", "description": "Undoes − 3 by subtracting 3 again, or ÷ by dividing."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_first", "type": "recall", "step": {
     "id": "qb_first", "type": "choice",
     "prompt": T("To solve 4(x + 3) = 20, a good first step is …", "4(x + 3) = 20 حل کرنے کا اچھا پہلا قدم ہے …"),
     "options": [
       opt("divide", "divide both sides by 4", "دونوں طرف کو 4 سے تقسیم", True,
           "Yes! x + 3 = 5, so x = 2.", "جی ہاں! x + 3 = 5، تو x = 2"),
       opt("subtract3", "subtract 3 from both sides", "دونوں طرف سے 3 تفریق", False,
           "The 3 is inside the bracket, multiplied by 4. Divide by 4 first.", "3 قوسین کے اندر ہے، 4 سے ضرب ہے۔ پہلے 4 سے تقسیم کریں۔"),
       opt("subtract4", "subtract 4 from both sides", "دونوں طرف سے 4 تفریق", False,
           "The 4 multiplies the bracket, so undo it by dividing.", "4 قوسین کو ضرب دیتا ہے، تو اسے تقسیم سے ختم کریں۔", "wrong_inverse"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Solve 7(a + 1) = 42. What is a?", "7(a + 1) = 42 حل کریں۔ a کیا ہے؟"),
     QB,
     T("Divide by 7, then subtract 1.", "7 سے تقسیم کریں، پھر 1 تفریق۔"),
     T("Right! a = 5.", "درست! a = 5"),
     T("42 ÷ 7 = 6, so a + 1 = 6, a = 5.", "42 ÷ 7 = 6، تو a + 1 = 6، a = 5"),
     common_wrong=[wrong(6, "That is a + 1. Subtract 1: a = 5.", "یہ a + 1 ہے۔ 1 تفریق کریں: a = 5", "stops_at_bracket")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Kamran multiplies out 2(x + 4) = 14 as 2x + 4 = 14. What is wrong?", "کامران 2(x + 4) = 14 کو 2x + 4 = 14 لکھتا ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("both", "Multiply both terms: 2x + 8 = 14, so x = 3.", "دونوں حصوں کو ضرب دیں: 2x + 8 = 14، تو x = 3", True,
           "Yes! The 2 multiplies the 4 too.", "جی ہاں! 2 چار کو بھی ضرب دیتا ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "The 2 multiplies everything in the bracket: 2x + 8 = 14.", "2 قوسین کی ہر چیز کو ضرب دیتا ہے: 2x + 8 = 14", "partial_expand"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_divide", "front": T("3(x + 2) = 21: quick way?", "3(x + 2) = 21: آسان طریقہ؟"),
    "back": T("Divide by 3: x + 2 = 7, so x = 5.", "3 سے تقسیم: x + 2 = 7، تو x = 5")},
   {"id": "f_expand", "front": T("3(x + 5) multiplied out?", "3(x + 5) کھول کر؟"),
    "back": T("3x + 15", "3x + 15")},
 ],
 "home_tasks": [{"id": "h_bags", "text": T(
   "Put the same number of spoons in 3 cups, then add 2 more spoons to each cup. If there are 21 spoons in all, how many were in each cup at first? Write 3(x + 2) = 21.",
   "3 کپوں میں برابر چمچ رکھیں، پھر ہر کپ میں 2 چمچ اور ڈالیں۔ اگر کل 21 چمچ ہوں تو شروع میں ہر کپ میں کتنے تھے؟ 3(x + 2) = 21 لکھیں۔")}],
 "glossary": [T("Brackets", "قوسین"), T("Multiply out", "قوسین کھولنا"), T("Equation", "مساوات")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "3 bags, each with x apples and 2 oranges. 21 fruits in all. How many apples in each bag?",
                     "3 تھیلے، ہر ایک میں x سیب اور 2 مالٹے۔ کل 21 پھل۔ ہر تھیلے میں کتنے سیب ہیں؟"),
    "text": T("That story is 3(x + 2) = 21. Today we solve equations with brackets. First, a quick check on multiplying a bracket.", "یہ کہانی 3(x + 2) = 21 ہے۔ آج ہم قوسین والی مساوات حل کریں گے۔ پہلے قوسین کو ضرب دینے کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Work out 4 × 6 + 4 × 2, which is the same as 4 × (6 + 2).", "4 × 6 + 4 × 2 نکالیں، جو 4 × (6 + 2) کے برابر ہے۔"),
     S2,
     T("24 + 8.", "24 + 8"),
     T("Right! 32.", "درست! 32"),
     T("4 × 6 = 24, 4 × 2 = 8, 24 + 8 = 32. And 4 × 8 = 32 too.", "4 × 6 = 24، 4 × 2 = 8، 24 + 8 = 32۔ اور 4 × 8 بھی 32 ہے۔"),
     common_wrong=[wrong(26, "Multiply the 2 by 4 as well: 24 + 8 = 32.", "2 کو بھی 4 سے ضرب دیں: 24 + 8 = 32", "partial_expand")],
     qtype="recall", skill=WN_PROPERTIES),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Two ways: divide first, or open the brackets. Both give the same answer!", "دو طریقے: پہلے تقسیم، یا قوسین کھولیں۔ دونوں کا جواب ایک!"),
    "text": T("Way 1, divide first: 3(x + 2) = 21. Divide both sides by 3: x + 2 = 7. Then x = 5. Way 2, open the brackets: 3(x + 2) = 3x + 6, so 3x + 6 = 21, 3x = 15, x = 5. When you open brackets, multiply EVERY term inside.",
              "طریقہ 1، پہلے تقسیم: 3(x + 2) = 21۔ دونوں طرف کو 3 سے تقسیم: x + 2 = 7۔ پھر x = 5۔ طریقہ 2، قوسین کھولیں: 3(x + 2) = 3x + 6، تو 3x + 6 = 21، 3x = 15، x = 5۔ قوسین کھولتے وقت اندر کی ہر چیز کو ضرب دیں۔")},
   number_question(
     "s4_divide_first",
     T("Solve 3(x + 2) = 21. What is x?", "3(x + 2) = 21 حل کریں۔ x کیا ہے؟"),
     S4,
     T("Divide by 3, then take away 2.", "3 سے تقسیم کریں، پھر 2 تفریق۔"),
     T("Right! x = 5.", "درست! x = 5"),
     T("21 ÷ 3 = 7, so x + 2 = 7, x = 5.", "21 ÷ 3 = 7، تو x + 2 = 7، x = 5"),
     common_wrong=[wrong(7, "That is x + 2. Take away 2: x = 5.", "یہ x + 2 ہے۔ 2 تفریق کریں: x = 5", "stops_at_bracket")]),
   number_question(
     "s5_minus",
     T("Solve 2(y − 3) = 10. What is y?", "2(y − 3) = 10 حل کریں۔ y کیا ہے؟"),
     S5,
     T("Divide by 2, then add 3.", "2 سے تقسیم کریں، پھر 3 جمع۔"),
     T("Right! y = 8.", "درست! y = 8"),
     T("10 ÷ 2 = 5, so y − 3 = 5, y = 8.", "10 ÷ 2 = 5، تو y − 3 = 5، y = 8"),
     common_wrong=[wrong(5, "That is y − 3. Add 3: y = 8.", "یہ y − 3 ہے۔ 3 جمع کریں: y = 8", "stops_at_bracket"),
                   wrong(2, "Undo − 3 by adding 3: 5 + 3 = 8.", "− 3 کو 3 جمع کرکے ختم کریں: 5 + 3 = 8", "wrong_inverse")]),
   {"id": "s6_expand", "type": "choice",
    "prompt": T("What is 4(m + 1) with the brackets opened?", "قوسین کھول کر 4(m + 1) کیا بنتا ہے؟"),
    "options": [
      opt("both", "4m + 4", "4m + 4", True, "Yes! 4 × m and 4 × 1.", "جی ہاں! 4 × m اور 4 × 1"),
      opt("first_only", "4m + 1", "4m + 1", False, "Multiply the 1 by 4 too: 4m + 4.", "1 کو بھی 4 سے ضرب دیں: 4m + 4", "partial_expand"),
      opt("add", "m + 4", "m + 4", False, "4 multiplies the m as well: 4m + 4.", "4 m کو بھی ضرب دیتا ہے: 4m + 4"),
    ]},
   number_question(
     "s7_plus",
     T("Solve 5(n + 4) = 35. What is n?", "5(n + 4) = 35 حل کریں۔ n کیا ہے؟"),
     S7,
     T("Divide by 5, then take away 4.", "5 سے تقسیم کریں، پھر 4 تفریق۔"),
     T("Right! n = 3.", "درست! n = 3"),
     T("35 ÷ 5 = 7, so n + 4 = 7, n = 3.", "35 ÷ 5 = 7، تو n + 4 = 7، n = 3"),
     common_wrong=[wrong(7, "That is n + 4. Take away 4: n = 3.", "یہ n + 4 ہے۔ 4 تفریق کریں: n = 3", "stops_at_bracket"),
                   wrong(11, "Undo + 4 by subtracting: 7 − 4 = 3.", "+ 4 کو تفریق سے ختم کریں: 7 − 4 = 3", "wrong_inverse")]),
   number_question(
     "s8_shared",
     T("Solve (x + 6) ÷ 2 = 9. What is x?", "(x + 6) ÷ 2 = 9 حل کریں۔ x کیا ہے؟"),
     S8,
     T("Multiply by 2 first, then take away 6.", "پہلے 2 سے ضرب دیں، پھر 6 تفریق۔"),
     T("Right! x = 12.", "درست! x = 12"),
     T("9 × 2 = 18, so x + 6 = 18, x = 12. Check: 18 ÷ 2 = 9.", "9 × 2 = 18، تو x + 6 = 18، x = 12۔ جانچ: 18 ÷ 2 = 9"),
     common_wrong=[wrong(6, "The whole bracket is divided by 2. Multiply by 2 first: x + 6 = 18, x = 12.", "پوری قوسین 2 سے تقسیم ہے۔ پہلے 2 سے ضرب دیں: x + 6 = 18، x = 12"),
                   wrong(18, "That is x + 6. Take away 6: x = 12.", "یہ x + 6 ہے۔ 6 تفریق کریں: x = 12", "stops_at_bracket")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hira opens the brackets in 3(x + 5) = 27 and writes 3x + 5 = 27. What went wrong?", "حرا 3(x + 5) = 27 کی قوسین کھول کر 3x + 5 = 27 لکھتی ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("both", "The 3 multiplies the 5 too: 3x + 15 = 27, so x = 4.", "3 پانچ کو بھی ضرب دیتا ہے: 3x + 15 = 27، تو x = 4", True,
          "Yes! Or divide first: x + 5 = 9, x = 4.", "جی ہاں! یا پہلے تقسیم: x + 5 = 9، x = 4"),
      opt("add", "It should be x + 8 = 27.", "یہ x + 8 = 27 ہونا چاہیے۔", False,
          "3 multiplies the bracket; it is not added: 3x + 15 = 27.", "3 قوسین کو ضرب دیتا ہے؛ جمع نہیں ہوتا: 3x + 15 = 27"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "She forgot 3 × 5. It is 3x + 15 = 27.", "وہ 3 × 5 بھول گئی۔ یہ 3x + 15 = 27 ہے۔", "partial_expand"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why can we divide both sides by 2 first in 2(x + 3) = 16? Can you teach me?",
                     "2(x + 3) = 16 میں ہم پہلے دونوں طرف کو 2 سے تقسیم کیوں کر سکتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: solve 2(x + 3) = 16 and explain why dividing by 2 first works.", "اپنے الفاظ میں بتائیں: 2(x + 3) = 16 حل کریں اور سمجھائیں کہ پہلے 2 سے تقسیم کیوں درست ہے۔"),
    "key_idea": "2(x + 3) means 2 lots of (x + 3). If 2 lots make 16, one lot is 16 ÷ 2 = 8. So x + 3 = 8 and x = 5. Dividing both sides by the same number keeps the equation balanced.",
    "levels": {
      "got_it": "Says 2 lots of (x + 3) make 16, so one lot is 8, then x = 5; or that doing the same to both sides keeps it balanced.",
      "partly": "Gets x = 5 without explaining why dividing first works.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["8", "eight", "آٹھ"],
      ["5", "five", "پانچ"],
      ["both sides", "balance", "دونوں طرف", "توازن"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Two lots make 16, so one lot is 8.", "بہت خوب! دو حصے 16، تو ایک حصہ 8"),
      "partly": T("Good start! Now say why dividing both sides is allowed.", "اچھی شروعات! اب بتائیں دونوں طرف تقسیم کرنا کیوں جائز ہے۔"),
      "not_yet": T("2(x + 3) means two lots of (x + 3). If two lots are 16, what is one lot?", "2(x + 3) یعنی (x + 3) کے دو حصے۔ اگر دو حصے 16 ہیں تو ایک حصہ کتنا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_minus_big",
     T("Solve 6(k − 2) = 30. What is k?", "6(k − 2) = 30 حل کریں۔ k کیا ہے؟"),
     S11,
     T("Divide by 6, then add 2.", "6 سے تقسیم کریں، پھر 2 جمع۔"),
     T("Right! k = 7.", "درست! k = 7"),
     T("30 ÷ 6 = 5, so k − 2 = 5, k = 7.", "30 ÷ 6 = 5، تو k − 2 = 5، k = 7"),
     common_wrong=[wrong(5, "That is k − 2. Add 2: k = 7.", "یہ k − 2 ہے۔ 2 جمع کریں: k = 7", "stops_at_bracket"),
                   wrong(3, "Undo − 2 by adding 2: 5 + 2 = 7.", "− 2 کو 2 جمع کرکے ختم کریں: 5 + 2 = 7", "wrong_inverse")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Brackets don't scare you any more. Divide first, or open them carefully!", "قوسین اب آپ کو نہیں ڈراتیں۔ پہلے تقسیم کریں، یا احتیاط سے کھولیں!"),
    "text": T("To solve a(x + b) = c: divide both sides by a, then undo the + b. Or open the brackets, multiplying every term inside, and solve the two-step equation. Check your answer at the end.",
              "a(x + b) = c حل کرنے کے لیے: دونوں طرف کو a سے تقسیم کریں، پھر + b ختم کریں۔ یا قوسین کھولیں، اندر کی ہر چیز کو ضرب دے کر، اور دو قدمی مساوات حل کریں۔ آخر میں جواب جانچیں۔"),
    "points": [T("Divide first, then undo + or −.", "پہلے تقسیم، پھر + یا − ختم کریں۔"),
               T("Opening brackets: multiply every term.", "قوسین کھولنا: ہر حصے کو ضرب دیں۔")]},
 ],
 "review_questions": [
   {"id": "r_plus", "type": "apply", "skill": SKILL, "step": number_question(
     "r_plus",
     T("Solve 2(x + 5) = 18. What is x?", "2(x + 5) = 18 حل کریں۔ x کیا ہے؟"),
     R1,
     T("Divide by 2, then take away 5.", "2 سے تقسیم کریں، پھر 5 تفریق۔"),
     T("Right! x = 4.", "درست! x = 4"),
     T("18 ÷ 2 = 9, so x + 5 = 9, x = 4.", "18 ÷ 2 = 9، تو x + 5 = 9، x = 4"),
     common_wrong=[wrong(9, "That is x + 5. Take away 5: x = 4.", "یہ x + 5 ہے۔ 5 تفریق کریں: x = 4", "stops_at_bracket")],
     qtype=None)},
   {"id": "r_minus", "type": "apply", "skill": SKILL, "step": number_question(
     "r_minus",
     T("Solve 3(y − 1) = 12. What is y?", "3(y − 1) = 12 حل کریں۔ y کیا ہے؟"),
     R2,
     T("Divide by 3, then add 1.", "3 سے تقسیم کریں، پھر 1 جمع۔"),
     T("Right! y = 5.", "درست! y = 5"),
     T("12 ÷ 3 = 4, so y − 1 = 4, y = 5.", "12 ÷ 3 = 4، تو y − 1 = 4، y = 5"),
     common_wrong=[wrong(4, "That is y − 1. Add 1: y = 5.", "یہ y − 1 ہے۔ 1 جمع کریں: y = 5", "stops_at_bracket"),
                   wrong(3, "Undo − 1 by adding 1: 4 + 1 = 5.", "− 1 کو 1 جمع کرکے ختم کریں: 4 + 1 = 5", "wrong_inverse")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Linear Equations unit. No textbook text or exercises were used.",
   "Both methods are shown; dividing first is quicker when the number outside divides the right side exactly, which it does in every question here.",
   "Urdu terms to check: قوسین (brackets), قوسین کھولنا (multiply out the brackets).",
   "The numbers were worked out in content/sources/g6-maths-16/equations_with_brackets.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

# ---------- pictures ----------
from figs import attach, step_says, bags, bars, bracket_bar, two_rows_alt

HOOK = 3, 2, 21        # 3 bags, each with x apples and 2 oranges: 21 fruits
assert solves(f"{HOOK[0]}(x + {HOOK[1]}) = {HOOK[2]}", x=S4)
s3_fig, s3_eq = bracket_bar(3, "x", 2, 21, S4, middle=True)
s4_fig, s4_eq = bracket_bar(3, "x", 2, 21, S4)
s5_fig, s5_eq = bracket_bar(2, "y", 3, 10, S5, minus=True)
s7_fig, s7_eq = bracket_bar(5, "n", 4, 35, S7)
s11_fig, s11_eq = bracket_bar(6, "k", 2, 30, S11, minus=True)
qf_fig, qf_eq = bracket_bar(4, "x", 3, 20, 2)
qa_fig, qa_eq = bracket_bar(7, "a", 1, 42, QB)
r1_fig, r1_eq = bracket_bar(2, "x", 5, 18, R1)
r2_fig, r2_eq = bracket_bar(3, "y", 1, 12, R2, minus=True)
S2_PARTS = 4, 6, 2     # 4 × (6 + 2)
assert S2 == S2_PARTS[0] * (S2_PARTS[1] + S2_PARTS[2])
S8_PARTS = 6, 2, 9     # (x + 6) ÷ 2 = 9
assert solves(f"(x + {S8_PARTS[0]}) ÷ {S8_PARTS[1]} = {S8_PARTS[2]}", x=S8)
for sid, eq in (("s1_hook", s4_eq), ("s3_rule", s3_eq), ("s4_divide_first", s4_eq), ("s5_minus", s5_eq),
                ("s7_plus", s7_eq), ("s11_minus_big", s11_eq), ("qb_first", qf_eq), ("qb_apply", qa_eq),
                ("r_plus", r1_eq), ("r_minus", r2_eq), ("s2_foundation", "4 × (6 + 2)"),
                ("s8_shared", "(x + 6) ÷ 2 = 9")):
    step_says(lesson, sid, eq)
n, a, b = S2_PARTS

attach(lesson, {
    "s1_hook": bags(HOOK[0], "x", HOOK[1],
        f"{HOOK[0]} bags drawn as dashed boxes. Each bag holds a shaded box marked x (the apples) and {HOOK[1]} small circles (the oranges). After the last bag: ={HOOK[2]}, the fruits in all.",
        f"{HOOK[0]} تھیلے، ڈیش والے ڈبوں کی شکل میں۔ ہر تھیلے میں x لکھا ایک رنگین ڈبہ (سیب) اور {HOOK[1]} چھوٹے دائرے (مالٹے) ہیں۔ آخری تھیلے کے بعد: ={HOOK[2]}، کل پھل۔",
        total=HOOK[2]),
    "s2_foundation": bars([[(a, a, "f"), (b, b, "")]] * n,
        f"{n} rows, one under the other, all the same. Each row is a shaded part {a} and a part {b}: {n} lots of ({a} + {b}). The shaded parts make {n} × {a} and the white parts {n} × {b}.",
        f"{n} قطاریں، ایک کے نیچے ایک، سب ایک جیسی۔ ہر قطار میں ایک رنگین حصہ {a} اور ایک حصہ {b} ہے: ({a} + {b}) کے {n} گنا۔ رنگین حصے {n} × {a} اور سفید حصے {n} × {b} بناتے ہیں۔"),
    "s3_rule": s3_fig,
    "s4_divide_first": s4_fig,
    "s5_minus": s5_fig,
    "s7_plus": s7_fig,
    "s8_shared": bars([[(S8, "x", "f"), (S8_PARTS[0], S8_PARTS[0], "")], [(S8_PARTS[2], S8_PARTS[2], "")] * S8_PARTS[1]],
        *two_rows_alt(["x", S8_PARTS[0]], [S8_PARTS[2]] * S8_PARTS[1],
                      pre=(f"(x + {S8_PARTS[0]}) shared into {S8_PARTS[1]} equal parts gives {S8_PARTS[2]} in each.",
                           f"(x + {S8_PARTS[0]}) کو {S8_PARTS[1]} برابر حصوں میں بانٹیں تو ہر حصے میں {S8_PARTS[2]} آتا ہے۔"))),
    "s11_minus_big": s11_fig,
    "qb_first": qf_fig,
    "qb_apply": qa_fig,
    "r_plus": r1_fig,
    "r_minus": r2_fig,
})
write(lesson)

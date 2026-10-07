from common import (T, opt, say, wrong, number_question, write, solves,
                    REF, REVIEW, ALG_EQUATIONS, EQ_FORMING, EQ_TWO_STEP)

SKILL = EQ_TWO_STEP

# s2: 3x = 18
S2 = 18 // 3
assert solves("3x = 18", x=S2) and S2 == 6 and 18 - 3 == 15
# s4: 2x + 5 = 17 (dividing first: (17 + 5) / 2 = 11)
S4 = (17 - 5) // 2
assert solves("2x + 5 = 17", x=S4) and S4 == 6 and (17 + 5) // 2 == 11
# s5: 3y - 4 = 11 (forgetting to divide: 15)
S5 = (11 + 4) // 3
assert solves("3y − 4 = 11", y=S5) and S5 == 5
# s6: 4m + 7 = 31: subtract 7 first
assert solves("4m + 7 = 31", m=6)
# s7: x/3 + 2 = 7 (forgetting x 3: 5)
S7 = (7 - 2) * 3
assert solves("x ÷ 3 + 2 = 7", x=S7) and S7 == 15
# s8: 5n - 6 = 29 (forgetting to divide: 35)
S8 = (29 + 6) // 5
assert solves("5n − 6 = 29", n=S8) and S8 == 7
# s9: 2x + 6 = 20 gives x = 7, not 4
assert solves("2x + 6 = 20", x=7) and 20 // 2 - 6 == 4
# s11: m/4 - 1 = 5 (forgetting x 4: 6; subtracting 1: 16)
S11 = (5 + 1) * 4
assert solves("m ÷ 4 − 1 = 5", m=S11) and S11 == 24 and (5 - 1) * 4 == 16
# question bank and review
QB = (45 - 3) // 6
assert solves("6k + 3 = 45", k=QB) and QB == 7 and 48 // 6 == 8
R1 = (21 - 1) // 4
assert solves("4a + 1 = 21", a=R1) and R1 == 5
R2 = (4 + 3) * 2
assert solves("x ÷ 2 − 3 = 4", x=R2) and R2 == 14 and (4 - 3) * 2 == 2

lesson = {
 "id": "g6-maths-16-two-step-equations",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve two-step linear equations (like 2x + 5 = 17 and x ÷ 3 + 2 = 7) by undoing the operations in reverse order.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Two-step equations", "دو قدمی مساوات"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": EQ_FORMING}, {"skill": ALG_EQUATIONS}],
 "misconceptions": [
   {"id": "divide_first", "description": "Divides before undoing the + or −, or divides only one term."},
   {"id": "one_step_only", "description": "Stops after the first step and forgets to undo the × or ÷."},
   {"id": "wrong_inverse", "description": "Undoes + by adding, or ÷ by dividing."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_first", "type": "recall", "step": {
     "id": "qb_first", "type": "choice",
     "prompt": T("To solve 3x + 2 = 14, what do you do first?", "3x + 2 = 14 حل کرنے کے لیے پہلے کیا کریں گے؟"),
     "options": [
       opt("subtract", "Subtract 2 from both sides", "دونوں طرف سے 2 تفریق", True,
           "Yes! 3x = 12, then x = 4.", "جی ہاں! 3x = 12، پھر x = 4"),
       opt("divide", "Divide both sides by 3", "دونوں طرف کو 3 سے تقسیم", False,
           "Undo the + 2 first, then the × 3.", "پہلے + 2 ختم کریں، پھر × 3", "divide_first"),
       opt("add", "Add 2 to both sides", "دونوں طرف 2 جمع", False,
           "Undo + 2 by subtracting 2, not adding.", "+ 2 کو 2 تفریق کرکے ختم کریں، جمع کرکے نہیں۔", "wrong_inverse"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Solve 6k + 3 = 45. What is k?", "6k + 3 = 45 حل کریں۔ k کیا ہے؟"),
     QB,
     T("Subtract 3, then divide by 6.", "3 تفریق کریں، پھر 6 سے تقسیم۔"),
     T("Right! k = 7.", "درست! k = 7"),
     T("45 − 3 = 42, then 42 ÷ 6 = 7.", "45 − 3 = 42، پھر 42 ÷ 6 = 7"),
     common_wrong=[wrong(8, "Undo + 3 by subtracting: 42 ÷ 6 = 7.", "+ 3 کو تفریق سے ختم کریں: 42 ÷ 6 = 7", "wrong_inverse"),
                   wrong(42, "That is 6k. Divide by 6: k = 7.", "یہ 6k ہے۔ 6 سے تقسیم کریں: k = 7", "one_step_only")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Sana solves 5x − 2 = 18. She writes 5x = 16, so x = 3.2. What is wrong?", "ثنا 5x − 2 = 18 حل کرتی ہے۔ وہ لکھتی ہے 5x = 16، تو x = 3.2۔ کیا غلطی ہے؟"),
     "options": [
       opt("add", "Undo − 2 by adding 2: 5x = 20, x = 4.", "− 2 کو 2 جمع کرکے ختم کریں: 5x = 20، x = 4", True,
           "Yes! Check: 5 × 4 − 2 = 18.", "جی ہاں! جانچ: 5 × 4 − 2 = 18"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Check: 5 × 3.2 − 2 = 14, not 18. Add 2 first: 5x = 20, x = 4.", "جانچ: 5 × 3.2 − 2 = 14، 18 نہیں۔ پہلے 2 جمع کریں: 5x = 20، x = 4", "wrong_inverse"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_order", "front": T("Two-step equation: first step?", "دو قدمی مساوات: پہلا قدم؟"),
    "back": T("Undo + or − first, then × or ÷.", "پہلے + یا − ختم کریں، پھر × یا ÷")},
   {"id": "f_divide", "front": T("Undo ÷ 3?", "÷ 3 کیسے ختم کریں؟"),
    "back": T("Multiply by 3.", "3 سے ضرب دیں۔")},
 ],
 "home_tasks": [{"id": "h_trick", "text": T(
   "Play 'think of a number' at home: someone doubles their number and adds 3, then tells you the answer. Use an equation to find their number.",
   "گھر میں 'ایک عدد سوچیں' کھیلیں: کوئی اپنا عدد دگنا کرکے 3 جمع کرے اور جواب بتائے۔ مساوات سے ان کا عدد معلوم کریں۔")}],
 "glossary": [T("Two-step", "دو قدمی"), T("Undo", "ختم کرنا / الٹ کرنا"), T("Both sides", "دونوں اطراف")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Putting on socks, then shoes. Taking them off, shoes come first! Equations work the same way.",
                     "پہلے جرابیں، پھر جوتے۔ اتارتے وقت پہلے جوتے! مساوات بھی ایسے ہی کام کرتی ہیں۔"),
    "text": T("Today we solve equations that need two steps. First, a quick one-step check.", "آج ہم ایسی مساوات حل کریں گے جن میں دو قدم لگتے ہیں۔ پہلے ایک قدم والا چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Solve 3x = 18. What is x?", "3x = 18 حل کریں۔ x کیا ہے؟"),
     S2,
     T("Divide both sides by 3.", "دونوں طرف کو 3 سے تقسیم کریں۔"),
     T("Right! x = 6.", "درست! x = 6"),
     T("18 ÷ 3 = 6.", "18 ÷ 3 = 6"),
     common_wrong=[wrong(15, "3x means 3 × x, so divide: 18 ÷ 3 = 6.", "3x یعنی 3 × x، تو تقسیم کریں: 18 ÷ 3 = 6"),
                   wrong(54, "Undo × 3 by dividing: 18 ÷ 3 = 6.", "× 3 کو تقسیم سے ختم کریں: 18 ÷ 3 = 6", "wrong_inverse")],
     qtype="recall", skill=ALG_EQUATIONS),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Undo the last thing first, like taking off shoes before socks!", "جو آخر میں ہوا اسے پہلے ختم کریں، جیسے جرابوں سے پہلے جوتے اتارنا!"),
    "text": T("In 2x + 5 = 17, x was multiplied by 2, then 5 was added. Undo in reverse order: first take 5 from both sides (2x = 12), then divide both sides by 2 (x = 6). Do the same to both sides each time. Check: 2 × 6 + 5 = 17.",
              "2x + 5 = 17 میں x کو 2 سے ضرب دی گئی، پھر 5 جمع ہوا۔ الٹی ترتیب سے ختم کریں: پہلے دونوں طرف سے 5 تفریق (2x = 12)، پھر دونوں طرف کو 2 سے تقسیم (x = 6)۔ ہر بار دونوں طرف ایک ہی کام کریں۔ جانچ: 2 × 6 + 5 = 17")},
   number_question(
     "s4_plus",
     T("Solve 2x + 5 = 17. What is x?", "2x + 5 = 17 حل کریں۔ x کیا ہے؟"),
     S4,
     T("Take 5 away first, then divide by 2.", "پہلے 5 تفریق کریں، پھر 2 سے تقسیم۔"),
     T("Right! x = 6.", "درست! x = 6"),
     T("17 − 5 = 12, then 12 ÷ 2 = 6.", "17 − 5 = 12، پھر 12 ÷ 2 = 6"),
     common_wrong=[wrong(11, "Undo + 5 by subtracting: 12 ÷ 2 = 6.", "+ 5 کو تفریق سے ختم کریں: 12 ÷ 2 = 6", "wrong_inverse"),
                   wrong(12, "That is 2x. Divide by 2: x = 6.", "یہ 2x ہے۔ 2 سے تقسیم کریں: x = 6", "one_step_only")]),
   number_question(
     "s5_minus",
     T("Solve 3y − 4 = 11. What is y?", "3y − 4 = 11 حل کریں۔ y کیا ہے؟"),
     S5,
     T("Add 4 first, then divide by 3.", "پہلے 4 جمع کریں، پھر 3 سے تقسیم۔"),
     T("Right! y = 5.", "درست! y = 5"),
     T("11 + 4 = 15, then 15 ÷ 3 = 5.", "11 + 4 = 15، پھر 15 ÷ 3 = 5"),
     common_wrong=[wrong(15, "That is 3y. Divide by 3: y = 5.", "یہ 3y ہے۔ 3 سے تقسیم کریں: y = 5", "one_step_only")]),
   {"id": "s6_first_step", "type": "choice",
    "prompt": T("To solve 4m + 7 = 31, what is the first step?", "4m + 7 = 31 حل کرنے کا پہلا قدم کیا ہے؟"),
    "options": [
      opt("subtract7", "Take 7 from both sides", "دونوں طرف سے 7 تفریق", True, "Yes! 4m = 24, then m = 6.", "جی ہاں! 4m = 24، پھر m = 6"),
      opt("divide4", "Divide both sides by 4", "دونوں طرف کو 4 سے تقسیم", False, "Undo the + 7 first. Then divide by 4.", "پہلے + 7 ختم کریں۔ پھر 4 سے تقسیم۔", "divide_first"),
      opt("add7", "Add 7 to both sides", "دونوں طرف 7 جمع", False, "Undo + 7 by subtracting 7.", "+ 7 کو 7 تفریق کرکے ختم کریں۔", "wrong_inverse"),
    ]},
   number_question(
     "s7_divide",
     T("Solve x ÷ 3 + 2 = 7. What is x?", "x ÷ 3 + 2 = 7 حل کریں۔ x کیا ہے؟"),
     S7,
     T("Take 2 away, then multiply by 3.", "2 تفریق کریں، پھر 3 سے ضرب۔"),
     T("Right! x = 15.", "درست! x = 15"),
     T("7 − 2 = 5, then 5 × 3 = 15. Check: 15 ÷ 3 + 2 = 7.", "7 − 2 = 5، پھر 5 × 3 = 15۔ جانچ: 15 ÷ 3 + 2 = 7"),
     common_wrong=[wrong(5, "That is x ÷ 3. Multiply by 3: x = 15.", "یہ x ÷ 3 ہے۔ 3 سے ضرب دیں: x = 15", "one_step_only"),
                   wrong(3, "Undo ÷ 3 by multiplying: 5 × 3 = 15.", "÷ 3 کو ضرب سے ختم کریں: 5 × 3 = 15", "wrong_inverse")]),
   number_question(
     "s8_minus_big",
     T("Solve 5n − 6 = 29. What is n?", "5n − 6 = 29 حل کریں۔ n کیا ہے؟"),
     S8,
     T("Add 6, then divide by 5.", "6 جمع کریں، پھر 5 سے تقسیم۔"),
     T("Right! n = 7.", "درست! n = 7"),
     T("29 + 6 = 35, then 35 ÷ 5 = 7.", "29 + 6 = 35، پھر 35 ÷ 5 = 7"),
     common_wrong=[wrong(35, "That is 5n. Divide by 5: n = 7.", "یہ 5n ہے۔ 5 سے تقسیم کریں: n = 7", "one_step_only")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Ahmed solves 2x + 6 = 20. He divides 20 by 2 to get x + 6 = 10, so x = 4. What went wrong?", "احمد 2x + 6 = 20 حل کرتا ہے۔ وہ 20 کو 2 سے تقسیم کرکے x + 6 = 10 لکھتا ہے، تو x = 4۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("subtract_first", "Take 6 away first: 2x = 14, so x = 7.", "پہلے 6 تفریق کریں: 2x = 14، تو x = 7", True,
          "Yes! He divided only part of the left side. Check: 2 × 7 + 6 = 20.", "جی ہاں! اس نے بائیں طرف کا صرف ایک حصہ تقسیم کیا۔ جانچ: 2 × 7 + 6 = 20"),
      opt("multiply", "He should multiply by 2: x = 40.", "اسے 2 سے ضرب دینی چاہیے: x = 40", False,
          "2x means × 2, so we divide. But take 6 away first: x = 7.", "2x یعنی × 2، تو تقسیم کریں۔ مگر پہلے 6 تفریق: x = 7", "wrong_inverse"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Check: 2 × 4 + 6 = 14, not 20. Take 6 away first: x = 7.", "جانچ: 2 × 4 + 6 = 14، 20 نہیں۔ پہلے 6 تفریق: x = 7", "divide_first"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we undo the + 5 before the × 2? Can you teach me?",
                     "ہم × 2 سے پہلے + 5 کیوں ختم کرتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: to solve 2x + 5 = 17, why do we take away 5 before dividing by 2?", "اپنے الفاظ میں بتائیں: 2x + 5 = 17 حل کرنے کے لیے ہم 2 سے تقسیم کرنے سے پہلے 5 کیوں تفریق کرتے ہیں؟"),
    "key_idea": "x was multiplied by 2 first and then 5 was added, so we undo in reverse order: take away the 5 (the last thing done), then divide by 2. Dividing first would have to divide the 5 too.",
    "levels": {
      "got_it": "Says we undo in reverse order (the + 5 was done last), or that dividing first would also have to divide the 5.",
      "partly": "Says 'take 5 first' without a reason.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["reverse", "last", "order", "الٹ", "آخر", "ترتیب"],
      ["undo", "ختم"],
      ["5", "five", "پانچ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Undo the last step first.", "بہت خوب! آخری قدم پہلے ختم کریں۔"),
      "partly": T("Good start! Now say why the order matters.", "اچھی شروعات! اب بتائیں ترتیب کیوں اہم ہے۔"),
      "not_yet": T("Which happened to x last: × 2 or + 5? Which should you undo first?", "x کے ساتھ آخر میں کیا ہوا: × 2 یا + 5؟ پہلے کسے ختم کرنا چاہیے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_quarter",
     T("Solve m ÷ 4 − 1 = 5. What is m?", "m ÷ 4 − 1 = 5 حل کریں۔ m کیا ہے؟"),
     S11,
     T("Add 1, then multiply by 4.", "1 جمع کریں، پھر 4 سے ضرب۔"),
     T("Right! m = 24.", "درست! m = 24"),
     T("5 + 1 = 6, then 6 × 4 = 24. Check: 24 ÷ 4 − 1 = 5.", "5 + 1 = 6، پھر 6 × 4 = 24۔ جانچ: 24 ÷ 4 − 1 = 5"),
     common_wrong=[wrong(16, "Undo − 1 by adding 1: 6 × 4 = 24.", "− 1 کو 1 جمع کرکے ختم کریں: 6 × 4 = 24", "wrong_inverse"),
                   wrong(6, "That is m ÷ 4. Multiply by 4: m = 24.", "یہ m ÷ 4 ہے۔ 4 سے ضرب دیں: m = 24", "one_step_only")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Two steps, reverse order, then check. You've got it!", "دو قدم، الٹی ترتیب، پھر جانچ۔ آپ سیکھ گئے!"),
    "text": T("To solve a two-step equation, undo in reverse order: first undo + or −, then undo × or ÷. Do the same to both sides, and check your answer in the equation.",
              "دو قدمی مساوات حل کرنے کے لیے الٹی ترتیب سے ختم کریں: پہلے + یا − ختم کریں، پھر × یا ÷۔ دونوں طرف ایک ہی کام کریں، اور جواب مساوات میں رکھ کر جانچیں۔"),
    "points": [T("First + or −, then × or ÷.", "پہلے + یا −، پھر × یا ÷"),
               T("Always check your answer.", "ہمیشہ جواب جانچیں۔")]},
 ],
 "review_questions": [
   {"id": "r_plus", "type": "apply", "skill": SKILL, "step": number_question(
     "r_plus",
     T("Solve 4a + 1 = 21. What is a?", "4a + 1 = 21 حل کریں۔ a کیا ہے؟"),
     R1,
     T("Subtract 1, then divide by 4.", "1 تفریق کریں، پھر 4 سے تقسیم۔"),
     T("Right! a = 5.", "درست! a = 5"),
     T("21 − 1 = 20, then 20 ÷ 4 = 5.", "21 − 1 = 20، پھر 20 ÷ 4 = 5"),
     common_wrong=[wrong(20, "That is 4a. Divide by 4: a = 5.", "یہ 4a ہے۔ 4 سے تقسیم کریں: a = 5", "one_step_only")],
     qtype=None)},
   {"id": "r_half", "type": "apply", "skill": SKILL, "step": number_question(
     "r_half",
     T("Solve x ÷ 2 − 3 = 4. What is x?", "x ÷ 2 − 3 = 4 حل کریں۔ x کیا ہے؟"),
     R2,
     T("Add 3, then multiply by 2.", "3 جمع کریں، پھر 2 سے ضرب۔"),
     T("Right! x = 14.", "درست! x = 14"),
     T("4 + 3 = 7, then 7 × 2 = 14.", "4 + 3 = 7، پھر 7 × 2 = 14"),
     common_wrong=[wrong(2, "Undo − 3 by adding 3: 7 × 2 = 14.", "− 3 کو 3 جمع کرکے ختم کریں: 7 × 2 = 14", "wrong_inverse"),
                   wrong(7, "That is x ÷ 2. Multiply by 2: x = 14.", "یہ x ÷ 2 ہے۔ 2 سے ضرب دیں: x = 14", "one_step_only")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Linear Equations unit. No textbook text or exercises were used.",
   "The Introduction to Algebra unit met two-step equations briefly; this lesson practises them fully, including ÷ (x ÷ 3 + 2 = 7).",
   "Urdu terms to check: دو قدمی مساوات (two-step equation), الٹی ترتیب (reverse order).",
   "The numbers were worked out in content/sources/g6-maths-16/two_step_equations.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

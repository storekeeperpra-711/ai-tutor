from common import (T, opt, say, wrong, number_question, write, value, solves,
                    REF, REVIEW, ALG_SUBSTITUTION, ALG_EQUATIONS, EQ_CHECK)

SKILL = EQ_CHECK

# s2: 3n + 2 when n = 4 (reading 3n as 34 gives 36)
S2 = value("3n + 2", n=4)
assert S2 == 14 and 34 + 2 == 36
# s4: 5y - 2 when y = 3 (reading 5y as 53 gives 51)
S4 = value("5y − 2", y=3)
assert S4 == 13 and 53 - 2 == 51
# s5: y = 3 solves 5y - 2 = 13
assert solves("5y − 2 = 13", y=3)
# s6: 4x = 28
assert solves("4x = 28", x=7) and not solves("4x = 28", x=24) and not solves("4x = 28", x=32)
# s7: which of 2, 3, 4 solves 3m + 1 = 13
S7 = [m for m in (2, 3, 4) if solves("3m + 1 = 13", m=m)]
assert S7 == [4] and value("3m + 1", m=3) == 10
S7 = S7[0]
# s8: x/2 + 5 when x = 6 (forgetting the + 5 gives 3)
S8 = value("x ÷ 2 + 5", x=6)
assert S8 == 8
# s9: x = 6 does solve 3x - 4 = 14 (reading 3x as 36 gives 32)
assert solves("3x − 4 = 14", x=6) and 36 - 4 == 32
# s11: which of 4, 5, 6 solves 4n + 3 = 23
S11 = [n for n in (4, 5, 6) if solves("4n + 3 = 23", n=n)]
assert S11 == [5] and value("4n + 3", n=4) == 19 and value("4n + 3", n=6) == 27
S11 = S11[0]
# question bank and review
QB = [x for x in (3, 4, 5) if solves("6x − 5 = 25", x=x)]
assert QB == [5] and value("6x − 5", x=4) == 19
QB = QB[0]
assert solves("2a + 1 = 9", a=4) and not solves("2a + 1 = 9", a=5)
R1 = value("2a + 7", a=6)
assert R1 == 19 and 26 + 7 == 33
R2 = [k for k in (7, 8, 9) if solves("5k − 10 = 30", k=k)]
assert R2 == [8]
R2 = R2[0]

lesson = {
 "id": "g6-maths-16-checking-solutions",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Check whether a number is a solution of a linear equation by putting it in place of the letter.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Checking a solution", "حل کی جانچ"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": ALG_EQUATIONS}, {"skill": ALG_SUBSTITUTION}],
 "misconceptions": [
   {"id": "joins_digits", "description": "Reads 3x with x = 6 as 36 instead of 3 × 6."},
   {"id": "one_side", "description": "Works out one side but does not compare it with the other side."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("A solution of an equation is a number that …", "مساوات کا حل وہ عدد ہے جو …"),
     "options": [
       opt("equal", "makes both sides equal", "دونوں اطراف کو برابر کر دے", True,
           "Yes! Put it in and both sides match.", "جی ہاں! اسے رکھیں تو دونوں اطراف برابر ہو جائیں۔"),
       opt("biggest", "is the biggest number in it", "اس میں سب سے بڑا عدد ہو", False,
           "No. It is the number that makes the left side equal the right side.", "نہیں۔ یہ وہ عدد ہے جو بائیں طرف کو دائیں طرف کے برابر کر دے۔", "one_side"),
       opt("right", "is on the right side", "دائیں طرف لکھا ہو", False,
           "The right side is just part of the equation. The solution makes both sides equal.", "دائیں طرف مساوات کا ایک حصہ ہے۔ حل دونوں اطراف کو برابر کرتا ہے۔", "one_side"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Which of 3, 4 or 5 is the solution of 6x − 5 = 25? Type it.", "3، 4 یا 5 میں سے کون سا 6x − 5 = 25 کا حل ہے؟ اسے لکھیں۔"),
     QB,
     T("Try each: 6 × 3 − 5, 6 × 4 − 5, 6 × 5 − 5.", "ہر ایک آزمائیں: 6 × 3 − 5، 6 × 4 − 5، 6 × 5 − 5"),
     T("Right! 6 × 5 − 5 = 25.", "درست! 6 × 5 − 5 = 25"),
     T("6 × 5 = 30, 30 − 5 = 25. Both sides are 25.", "6 × 5 = 30، 30 − 5 = 25۔ دونوں اطراف 25 ہیں۔"),
     common_wrong=[wrong(4, "6 × 4 − 5 = 19, not 25. Try 5: 30 − 5 = 25.", "6 × 4 − 5 = 19، 25 نہیں۔ 5 آزمائیں: 30 − 5 = 25", "one_side")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Rida checks a = 4 in 2a + 1 = 9. She writes 24 + 1 = 25, so 'not a solution'. What is wrong?", "ردا 2a + 1 = 9 میں a = 4 جانچتی ہے۔ وہ لکھتی ہے 24 + 1 = 25، تو 'حل نہیں'۔ کیا غلطی ہے؟"),
     "options": [
       opt("times", "2a means 2 × 4 = 8. 8 + 1 = 9, so a = 4 is a solution.", "2a یعنی 2 × 4 = 8۔ 8 + 1 = 9، تو a = 4 حل ہے۔", True,
           "Yes! A number next to a letter means multiply.", "جی ہاں! حرف کے ساتھ عدد یعنی ضرب۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "2a is 2 × a, not 24. 2 × 4 + 1 = 9: it is a solution.", "2a یعنی 2 × a، 24 نہیں۔ 2 × 4 + 1 = 9: یہ حل ہے۔", "joins_digits"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_solution", "front": T("Solution of an equation?", "مساوات کا حل؟"),
    "back": T("The number that makes both sides equal.", "وہ عدد جو دونوں اطراف کو برابر کرے۔")},
   {"id": "f_check", "front": T("How to check?", "جانچ کیسے؟"),
    "back": T("Put the number in, work out each side, compare.", "عدد رکھیں، ہر طرف حل کریں، موازنہ کریں۔")},
 ],
 "home_tasks": [{"id": "h_guess", "text": T(
   "Ask someone at home to think of a number, multiply it by 2 and add 5, and tell you the answer. Guess their number, then check it.",
   "گھر میں کسی سے کہیں کہ ایک عدد سوچیں، اسے 2 سے ضرب دیں اور 5 جمع کریں، اور آپ کو جواب بتائیں۔ ان کا عدد بوجھیں، پھر جانچیں۔")}],
 "glossary": [T("Solution", "حل"), T("Equation", "مساوات"), T("Side", "طرف")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Is 4 the answer to 2x + 3 = 11? How can we be sure?",
                     "کیا 2x + 3 = 11 کا جواب 4 ہے؟ ہم یقین کیسے کریں؟"),
    "text": T("Today we learn to check whether a number is the solution of an equation. First, a quick substitution check.", "آج ہم جانچنا سیکھیں گے کہ کوئی عدد مساوات کا حل ہے یا نہیں۔ پہلے قیمت رکھنے کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Find the value of 3n + 2 when n = 4.", "جب n = 4 ہو تو 3n + 2 کی قیمت معلوم کریں۔"),
     S2,
     T("3n means 3 × n.", "3n یعنی 3 × n"),
     T("Right! 3 × 4 + 2 = 14.", "درست! 3 × 4 + 2 = 14"),
     T("3 × 4 = 12, then 12 + 2 = 14.", "3 × 4 = 12، پھر 12 + 2 = 14"),
     common_wrong=[wrong(36, "3n is 3 × 4, not 34: 12 + 2 = 14.", "3n یعنی 3 × 4، 34 نہیں: 12 + 2 = 14", "joins_digits")],
     qtype="recall", skill=ALG_SUBSTITUTION),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Put the number in. If both sides match, it's the solution!", "عدد رکھیں۔ اگر دونوں اطراف برابر ہوں تو یہی حل ہے!"),
    "text": T("A solution is a number that makes both sides of the equation equal. To check: 1. Put the number in place of the letter. 2. Work out the left side. 3. Compare it with the right side. For 2x + 3 = 11 and x = 4: 2 × 4 + 3 = 11. Both sides are 11, so x = 4 is the solution.",
              "حل وہ عدد ہے جو مساوات کی دونوں اطراف کو برابر کر دے۔ جانچنے کے لیے: 1۔ حرف کی جگہ عدد رکھیں۔ 2۔ بائیں طرف حل کریں۔ 3۔ اسے دائیں طرف سے ملائیں۔ 2x + 3 = 11 اور x = 4 کے لیے: 2 × 4 + 3 = 11۔ دونوں اطراف 11 ہیں، تو x = 4 حل ہے۔")},
   number_question(
     "s4_left_side",
     T("Put y = 3 into 5y − 2. What do you get?", "5y − 2 میں y = 3 رکھیں۔ کیا ملتا ہے؟"),
     S4,
     T("5 × 3, then − 2.", "5 × 3، پھر − 2"),
     T("Right! 15 − 2 = 13.", "درست! 15 − 2 = 13"),
     T("5 × 3 = 15, then 15 − 2 = 13.", "5 × 3 = 15، پھر 15 − 2 = 13"),
     common_wrong=[wrong(51, "5y is 5 × 3, not 53: 15 − 2 = 13.", "5y یعنی 5 × 3، 53 نہیں: 15 − 2 = 13", "joins_digits")]),
   {"id": "s5_is_solution", "type": "choice",
    "prompt": T("So, is y = 3 a solution of 5y − 2 = 13?", "تو کیا y = 3 مساوات 5y − 2 = 13 کا حل ہے؟"),
    "options": [
      opt("yes", "Yes", "ہاں", True, "Yes! The left side is 13 and the right side is 13.", "جی ہاں! بائیں طرف 13 ہے اور دائیں طرف 13۔"),
      opt("no", "No", "نہیں", False, "The left side came to 13, the same as the right side. So yes.", "بائیں طرف 13 آیا، دائیں طرف جتنا۔ تو ہاں۔", "one_side"),
    ]},
   {"id": "s6_which", "type": "choice",
    "prompt": T("Which number is the solution of 4x = 28?", "کون سا عدد 4x = 28 کا حل ہے؟"),
    "options": [
      opt("seven", "7", "7", True, "Yes! 4 × 7 = 28.", "جی ہاں! 4 × 7 = 28"),
      opt("twenty_four", "24", "24", False, "4 × 24 = 96, not 28. Try 7: 4 × 7 = 28.", "4 × 24 = 96، 28 نہیں۔ 7 آزمائیں: 4 × 7 = 28"),
      opt("thirty_two", "32", "32", False, "4 × 32 = 128, not 28. Try 7: 4 × 7 = 28.", "4 × 32 = 128، 28 نہیں۔ 7 آزمائیں: 4 × 7 = 28"),
    ]},
   number_question(
     "s7_try",
     T("Which of 2, 3 or 4 is the solution of 3m + 1 = 13? Type it.", "2، 3 یا 4 میں سے کون سا 3m + 1 = 13 کا حل ہے؟ اسے لکھیں۔"),
     S7,
     T("Try each one: 3 × 2 + 1, 3 × 3 + 1, 3 × 4 + 1.", "ہر ایک آزمائیں: 3 × 2 + 1، 3 × 3 + 1، 3 × 4 + 1"),
     T("Right! 3 × 4 + 1 = 13.", "درست! 3 × 4 + 1 = 13"),
     T("3 × 4 = 12, 12 + 1 = 13. Both sides are 13.", "3 × 4 = 12، 12 + 1 = 13۔ دونوں اطراف 13 ہیں۔"),
     common_wrong=[wrong(3, "3 × 3 + 1 = 10, not 13. Try 4.", "3 × 3 + 1 = 10، 13 نہیں۔ 4 آزمائیں۔", "one_side"),
                   wrong(2, "3 × 2 + 1 = 7, not 13. Try 4.", "3 × 2 + 1 = 7، 13 نہیں۔ 4 آزمائیں۔", "one_side")]),
   number_question(
     "s8_divide",
     T("Put x = 6 into x ÷ 2 + 5. What do you get?", "x ÷ 2 + 5 میں x = 6 رکھیں۔ کیا ملتا ہے؟"),
     S8,
     T("6 ÷ 2 first, then + 5.", "پہلے 6 ÷ 2، پھر + 5"),
     T("Right! 3 + 5 = 8.", "درست! 3 + 5 = 8"),
     T("6 ÷ 2 = 3, then 3 + 5 = 8.", "6 ÷ 2 = 3، پھر 3 + 5 = 8"),
     common_wrong=[wrong(3, "That is 6 ÷ 2. Now add 5: 8.", "یہ 6 ÷ 2 ہے۔ اب 5 جمع کریں: 8")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Usman checks x = 6 in 3x − 4 = 14. He writes 36 − 4 = 32 and says 'no'. What went wrong?", "عثمان 3x − 4 = 14 میں x = 6 جانچتا ہے۔ وہ لکھتا ہے 36 − 4 = 32 اور کہتا ہے 'نہیں'۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("times", "3x means 3 × 6 = 18. 18 − 4 = 14, so x = 6 IS a solution.", "3x یعنی 3 × 6 = 18۔ 18 − 4 = 14، تو x = 6 حل ہے۔", True,
          "Yes! Multiply the number by 3; don't write 3 and 6 side by side.", "جی ہاں! عدد کو 3 سے ضرب دیں؛ 3 اور 6 ساتھ ساتھ نہ لکھیں۔"),
      opt("add", "He should add: 3 + 6 − 4 = 5.", "اسے جمع کرنا چاہیے: 3 + 6 − 4 = 5", False,
          "3x means 3 × x, not 3 + x: 18 − 4 = 14.", "3x یعنی 3 × x، 3 + x نہیں: 18 − 4 = 14"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "3x is 3 × 6 = 18, not 36. 18 − 4 = 14: it is a solution.", "3x یعنی 3 × 6 = 18، 36 نہیں۔ 18 − 4 = 14: یہ حل ہے۔", "joins_digits"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "How can you tell if a number is the solution, without solving? Can you teach me?",
                     "بغیر حل کیے کیسے پتا چلے کہ کوئی عدد حل ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: how do you check whether x = 5 is the solution of 2x + 1 = 11?", "اپنے الفاظ میں بتائیں: آپ کیسے جانچیں گے کہ x = 5 مساوات 2x + 1 = 11 کا حل ہے یا نہیں؟"),
    "key_idea": "Put 5 in place of x: 2 × 5 + 1 = 11. The left side equals the right side (11), so x = 5 is the solution. If the sides were different, it would not be.",
    "levels": {
      "got_it": "Puts 5 in for x, works out 2 × 5 + 1 = 11, and says the two sides are equal so it is the solution.",
      "partly": "Puts 5 in but doesn't compare the two sides, or compares without working it out.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["11", "eleven", "گیارہ"],
      ["equal", "same", "برابر"],
      ["side", "طرف"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Both sides came to 11.", "بہت خوب! دونوں اطراف 11 آئیں۔"),
      "partly": T("Good start! Now compare your answer with the right side.", "اچھی شروعات! اب اپنا جواب دائیں طرف سے ملائیں۔"),
      "not_yet": T("Put 5 where x is. What is 2 × 5 + 1? Is it 11?", "x کی جگہ 5 رکھیں۔ 2 × 5 + 1 کتنا ہے؟ کیا یہ 11 ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_think",
     T("Ali thinks of a number n. He says 4n + 3 = 23. Which of 4, 5 or 6 is his number?", "علی ایک عدد n سوچتا ہے۔ وہ کہتا ہے 4n + 3 = 23۔ 4، 5 یا 6 میں سے اس کا عدد کون سا ہے؟"),
     S11,
     T("Try each one in 4n + 3.", "ہر ایک کو 4n + 3 میں آزمائیں۔"),
     T("Right! 4 × 5 + 3 = 23.", "درست! 4 × 5 + 3 = 23"),
     T("4 × 5 = 20, 20 + 3 = 23.", "4 × 5 = 20، 20 + 3 = 23"),
     common_wrong=[wrong(4, "4 × 4 + 3 = 19, not 23. Try 5.", "4 × 4 + 3 = 19، 23 نہیں۔ 5 آزمائیں۔", "one_side"),
                   wrong(6, "4 × 6 + 3 = 27, not 23. Try 5.", "4 × 6 + 3 = 27، 23 نہیں۔ 5 آزمائیں۔", "one_side")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Put it in, work it out, compare. Now you can check any answer!", "رکھیں، حل کریں، موازنہ کریں۔ اب آپ کوئی بھی جواب جانچ سکتے ہیں!"),
    "text": T("A solution makes both sides of an equation equal. To check a number, put it in place of the letter, work out each side, and compare. A number next to a letter means multiply.",
              "حل مساوات کی دونوں اطراف کو برابر کرتا ہے۔ کسی عدد کو جانچنے کے لیے اسے حرف کی جگہ رکھیں، ہر طرف حل کریں، اور موازنہ کریں۔ حرف کے ساتھ عدد یعنی ضرب۔"),
    "points": [T("Both sides equal = solution.", "دونوں اطراف برابر = حل"),
               T("3x means 3 × x.", "3x یعنی 3 × x")]},
 ],
 "review_questions": [
   {"id": "r_value", "type": "apply", "skill": SKILL, "step": number_question(
     "r_value",
     T("Put a = 6 into 2a + 7. What do you get?", "2a + 7 میں a = 6 رکھیں۔ کیا ملتا ہے؟"),
     R1,
     T("2 × 6, then + 7.", "2 × 6، پھر + 7"),
     T("Right! 12 + 7 = 19.", "درست! 12 + 7 = 19"),
     T("2 × 6 = 12, 12 + 7 = 19.", "2 × 6 = 12، 12 + 7 = 19"),
     common_wrong=[wrong(33, "2a is 2 × 6, not 26: 12 + 7 = 19.", "2a یعنی 2 × 6، 26 نہیں: 12 + 7 = 19", "joins_digits")],
     qtype=None)},
   {"id": "r_which", "type": "apply", "skill": SKILL, "step": number_question(
     "r_which",
     T("Which of 7, 8 or 9 is the solution of 5k − 10 = 30? Type it.", "7، 8 یا 9 میں سے کون سا 5k − 10 = 30 کا حل ہے؟ اسے لکھیں۔"),
     R2,
     T("Try each one in 5k − 10.", "ہر ایک کو 5k − 10 میں آزمائیں۔"),
     T("Right! 5 × 8 − 10 = 30.", "درست! 5 × 8 − 10 = 30"),
     T("5 × 8 = 40, 40 − 10 = 30.", "5 × 8 = 40، 40 − 10 = 30"),
     common_wrong=[wrong(7, "5 × 7 − 10 = 25, not 30. Try 8.", "5 × 7 − 10 = 25، 30 نہیں۔ 8 آزمائیں۔", "one_side"),
                   wrong(9, "5 × 9 − 10 = 35, not 30. Try 8.", "5 × 9 − 10 = 35، 30 نہیں۔ 8 آزمائیں۔", "one_side")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Linear Equations unit. No textbook text or exercises were used.",
   "Checking by substitution is taught before more solving, so children can check every answer they find later in the unit.",
   "Urdu terms to check: مساوات (equation), حل (solution), طرف / اطراف (side / sides).",
   "The numbers were worked out in content/sources/g6-maths-16/checking_solutions.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

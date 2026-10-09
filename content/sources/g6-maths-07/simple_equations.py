from common import (T, opt, say, wrong, number_question, text_question, write, value,
                    REF, REVIEW, ALG_SUBSTITUTION, ALG_LIKE_TERMS, ALG_EQUATIONS)

SKILL = ALG_EQUATIONS


def solve(equation, letter):
    """The whole number from 0 to 100 that makes the equation true (only one may)."""
    left, right = equation.split("=")
    found = [n for n in range(0, 101) if value(left, **{letter: n}) == value(right, **{letter: n})]
    assert len(found) == 1, (equation, found)
    return found[0]


# s2
assert value("5y + 2y", y=3) == value("7y", y=3)
# s4 to s7
S4 = solve("x + 5 = 12", "x")
assert S4 == 7 and 12 + 5 == 17
S5 = solve("y - 4 = 9", "y")
assert S5 == 13 and 9 - 4 == 5
S6 = solve("3x = 18", "x")
assert S6 == 6 and 18 - 3 == 15 and 18 * 3 == 54
S7 = solve("m / 4 = 5", "m")
assert S7 == 20 and 5 + 4 == 9
# s8: 2x + 1 = 9 by working
assert solve("2x + 1 = 9", "x") == 4 and (9 + 1) / 2 == 5
# s9: x + 6 = 10
assert solve("x + 6 = 10", "x") == 4
# s11: 4n − 3 = 25
S11 = solve("4n - 3 = 25", "n")
assert S11 == 7 and (25 - 3) / 4 == 5.5
# question bank and review
assert solve("x + 3 = 10", "x") == 7
QB = solve("5k = 35", "k")
assert QB == 7 and 35 - 5 == 30
assert solve("n - 3 = 8", "n") == 11
R1 = solve("a + 9 = 15", "a")
assert R1 == 6
R2 = solve("6y = 42", "y")
assert R2 == 7


lesson = {
 "id": "g6-maths-07-simple-equations",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve simple one-step and two-step equations by doing the same to both sides, and check the answer.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Simple equations", "سادہ مساوات"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": ALG_SUBSTITUTION}, {"skill": ALG_LIKE_TERMS}],
 "misconceptions": [
   {"id": "same_operation", "description": "Does the operation in the equation instead of its opposite: x + 5 = 12 gives x = 17."},
   {"id": "wrong_inverse", "description": "Undoes multiplying by subtracting: 3x = 18 gives x = 15."},
   {"id": "two_step_order", "description": "In a two-step equation, divides before taking away the number: 2x + 1 = 9 gives x = 4.5 or 5."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_recall", "type": "recall", "step": {
     "id": "qb_recall", "type": "choice",
     "prompt": T("Which value of x makes x + 3 = 10 true?", "x کی کون سی قیمت x + 3 = 10 کو درست بناتی ہے؟"),
     "options": [
       opt("seven", "x = 7", "x = 7", True, "Yes! 7 + 3 = 10.", "جی ہاں! 7 + 3 = 10"),
       opt("thirteen", "x = 13", "x = 13", False, "13 + 3 = 16, not 10. Take 3 away: x = 7.", "13 + 3 = 16، نہ کہ 10۔ 3 گھٹائیں: x = 7", "same_operation"),
       opt("thirty", "x = 30", "x = 30", False, "30 + 3 = 33. Take 3 from 10: x = 7.", "30 + 3 = 33۔ 10 میں سے 3 گھٹائیں: x = 7"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Solve 5k = 35. What is k?", "5k = 35 حل کریں۔ k کتنا ہے؟"),
     QB,
     T("5 times what makes 35? Divide both sides by 5.", "5 ضرب کیا 35 بنتا ہے؟ دونوں طرف 5 سے تقسیم کریں۔"),
     T("Right! k = 7. Check: 5 × 7 = 35.", "درست! k = 7۔ جانچ: 5 × 7 = 35"),
     T("35 ÷ 5 = 7, so k = 7.", "35 ÷ 5 = 7، اس لیے k = 7"),
     common_wrong=[wrong(30, "5k means 5 × k, so divide, don't subtract: 35 ÷ 5 = 7.", "5k یعنی 5 × k، اس لیے تفریق نہیں تقسیم: 35 ÷ 5 = 7", "wrong_inverse"),
                   wrong(175, "Undo × 5 by dividing: 35 ÷ 5 = 7.", "× 5 کو تقسیم سے الٹیں: 35 ÷ 5 = 7", "same_operation")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Hina solves n − 3 = 8 and gets n = 5. What went wrong?", "حنا n − 3 = 8 حل کر کے n = 5 نکالتی ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("add", "She should add 3 to both sides: n = 11.", "اسے دونوں طرف 3 جمع کرنا چاہیے: n = 11", True,
           "Yes! Check: 11 − 3 = 8. And 5 − 3 = 2, not 8.", "جی ہاں! جانچ: 11 − 3 = 8۔ اور 5 − 3 = 2، نہ کہ 8"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Check: 5 − 3 = 2, not 8. Add 3 to both sides: n = 11.", "جانچیں: 5 − 3 = 2، نہ کہ 8۔ دونوں طرف 3 جمع کریں: n = 11", "same_operation"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_balance", "front": T("How do you solve an equation?", "مساوات کیسے حل کرتے ہیں؟"),
    "back": T("Keep it balanced: do the opposite operation to both sides. x + 5 = 12: take 5 from both sides, x = 7.", "توازن رکھیں: دونوں طرف الٹا عمل کریں۔ x + 5 = 12: دونوں طرف سے 5 گھٹائیں، x = 7")},
   {"id": "f_check", "front": T("How do you check an answer?", "جواب کیسے جانچیں؟"),
    "back": T("Put it back in. x = 7 in x + 5 = 12: 7 + 5 = 12. True!", "اسے واپس رکھیں۔ x + 5 = 12 میں x = 7: 7 + 5 = 12۔ درست!")},
 ],
 "home_tasks": [{"id": "h_mystery", "text": T(
   "Play 'think of a number' with someone at home: they think of a number, double it and add 3, and tell you the result. Write an equation like 2n + 3 = 17 and solve it to find their number.",
   "گھر میں کسی کے ساتھ 'کوئی عدد سوچو' کھیلیں: وہ عدد سوچیں، اسے دگنا کر کے 3 جمع کریں، اور نتیجہ بتائیں۔ 2n + 3 = 17 جیسی مساوات لکھ کر حل کریں اور ان کا عدد معلوم کریں۔")}],
 "glossary": [T("Equation", "مساوات"), T("Solve", "حل کرنا"), T("Both sides", "دونوں طرف")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "I'm thinking of a number. I add 5 and get 12. Can you find my number?",
                     "میں نے ایک عدد سوچا ہے۔ اس میں 5 جمع کیا تو 12 آیا۔ کیا آپ میرا عدد ڈھونڈ سکتے ہیں؟"),
    "text": T("We can write this as an equation: x + 5 = 12. Today we solve equations like this. First, a quick check.", "اسے ہم مساوات کی شکل میں لکھ سکتے ہیں: x + 5 = 12۔ آج ہم ایسی مساواتیں حل کریں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   text_question(
     "s2_foundation",
     T("Simplify 5y + 2y.", "5y + 2y کو مختصر کریں۔"),
     "7y",
     T("Same letter: add the numbers.", "ایک ہی حرف: اعداد جمع کریں۔"),
     T("Right! 7y.", "درست! 7y"),
     T("5y + 2y = 7y.", "5y + 2y = 7y"),
     accept=["7*y", "y7"],
     common_wrong=[wrong("7", "Keep the letter: 7y.", "حرف رکھیں: 7y")],
     qtype="recall", skill=ALG_LIKE_TERMS),
   {"id": "s3_balance", "type": "explain",
    "character": say("thinking", "An equation is like a balance. Keep both sides equal!", "مساوات ترازو کی طرح ہے۔ دونوں پلڑے برابر رکھیں!"),
    "text": T("x + 5 = 12 says both sides weigh the same. To get x alone, undo the + 5 by taking 5 from BOTH sides: x = 12 − 5 = 7. Undo + with −, − with +, × with ÷, and ÷ with ×. Then check: 7 + 5 = 12.",
              "x + 5 = 12 کہتی ہے دونوں طرف برابر ہیں۔ x کو اکیلا کرنے کے لیے + 5 کو الٹیں، دونوں طرف سے 5 گھٹا کر: x = 12 − 5 = 7۔ + کو − سے، − کو + سے، × کو ÷ سے، اور ÷ کو × سے الٹیں۔ پھر جانچیں: 7 + 5 = 12")},
   number_question(
     "s4_add",
     T("Solve x + 5 = 12. What is x?", "x + 5 = 12 حل کریں۔ x کتنا ہے؟"),
     S4,
     T("Take 5 from both sides.", "دونوں طرف سے 5 گھٹائیں۔"),
     T("Right! x = 7. Check: 7 + 5 = 12.", "درست! x = 7۔ جانچ: 7 + 5 = 12"),
     T("12 − 5 = 7, so x = 7.", "12 − 5 = 7، اس لیے x = 7"),
     common_wrong=[wrong(17, "Check: 17 + 5 = 22, not 12. Undo + 5 by taking 5 away: 7.", "جانچیں: 17 + 5 = 22، نہ کہ 12۔ + 5 کو 5 گھٹا کر الٹیں: 7", "same_operation")]),
   number_question(
     "s5_subtract",
     T("Solve y − 4 = 9. What is y?", "y − 4 = 9 حل کریں۔ y کتنا ہے؟"),
     S5,
     T("Undo − 4 by adding 4 to both sides.", "− 4 کو دونوں طرف 4 جمع کر کے الٹیں۔"),
     T("Right! y = 13. Check: 13 − 4 = 9.", "درست! y = 13۔ جانچ: 13 − 4 = 9"),
     T("9 + 4 = 13, so y = 13.", "9 + 4 = 13، اس لیے y = 13"),
     common_wrong=[wrong(5, "Check: 5 − 4 = 1, not 9. Add 4 to both sides: 13.", "جانچیں: 5 − 4 = 1، نہ کہ 9۔ دونوں طرف 4 جمع کریں: 13", "same_operation")]),
   number_question(
     "s6_times",
     T("Solve 3x = 18. What is x?", "3x = 18 حل کریں۔ x کتنا ہے؟"),
     S6,
     T("3x means 3 × x. Undo it by dividing both sides by 3.", "3x یعنی 3 × x۔ دونوں طرف 3 سے تقسیم کر کے الٹیں۔"),
     T("Right! x = 6. Check: 3 × 6 = 18.", "درست! x = 6۔ جانچ: 3 × 6 = 18"),
     T("18 ÷ 3 = 6, so x = 6.", "18 ÷ 3 = 6، اس لیے x = 6"),
     common_wrong=[wrong(15, "3x is 3 × x, so divide, don't subtract: 18 ÷ 3 = 6.", "3x یعنی 3 × x، اس لیے تفریق نہیں تقسیم: 18 ÷ 3 = 6", "wrong_inverse"),
                   wrong(54, "Undo × 3 by dividing: 18 ÷ 3 = 6.", "× 3 کو تقسیم سے الٹیں: 18 ÷ 3 = 6", "same_operation")]),
   number_question(
     "s7_divide",
     T("Solve m ÷ 4 = 5. What is m?", "m ÷ 4 = 5 حل کریں۔ m کتنا ہے؟"),
     S7,
     T("Undo ÷ 4 by multiplying both sides by 4.", "÷ 4 کو دونوں طرف 4 سے ضرب دے کر الٹیں۔"),
     T("Right! m = 20. Check: 20 ÷ 4 = 5.", "درست! m = 20۔ جانچ: 20 ÷ 4 = 5"),
     T("5 × 4 = 20, so m = 20.", "5 × 4 = 20، اس لیے m = 20"),
     common_wrong=[wrong(9, "Undo ÷ 4 by multiplying, not adding: 5 × 4 = 20.", "÷ 4 کو جمع سے نہیں، ضرب سے الٹیں: 5 × 4 = 20", "wrong_inverse"),
                   wrong(1, "Check: 1 ÷ 4 is not 5. Multiply: 5 × 4 = 20.", "جانچیں: 1 ÷ 4 پانچ نہیں۔ ضرب دیں: 5 × 4 = 20", "wrong_inverse")]),
   {"id": "s8_two_step", "type": "text_check", "question_type": "apply", "checker": "linear_equation",
    "expected": "2x + 1 = 9", "multiline": True,
    "character": say("encouraging", "Two steps now! Undo the + 1 first, then the × 2.", "اب دو قدم! پہلے + 1 کو الٹیں، پھر × 2 کو۔"),
    "prompt": T("Solve 2x + 1 = 9. Write each step on a new line, ending with x = your answer.", "2x + 1 = 9 حل کریں۔ ہر قدم نئی سطر میں لکھیں، اور آخر میں x = آپ کا جواب۔"),
    "hint": T("Take 1 from both sides: 2x = 8. Then divide both sides by 2.", "دونوں طرف سے 1 گھٹائیں: 2x = 8۔ پھر دونوں طرف 2 سے تقسیم کریں۔"),
    "feedback_correct": T("Well done! x = 4. Check: 2 × 4 + 1 = 9.", "شاباش! x = 4۔ جانچ: 2 × 4 + 1 = 9"),
    "feedback_wrong": T("2x + 1 = 9. Take 1 from both sides: 2x = 8. Divide both sides by 2: x = 4.", "2x + 1 = 9۔ دونوں طرف سے 1 گھٹائیں: 2x = 8۔ دونوں طرف 2 سے تقسیم کریں: x = 4"),
    "common_wrong": [wrong("x = 5", "Take the 1 away, don't add it: 2x = 8, so x = 4. Check: 2 × 5 + 1 = 11, not 9.", "1 جمع نہیں، گھٹائیں: 2x = 8، اس لیے x = 4۔ جانچ: 2 × 5 + 1 = 11، نہ کہ 9", "same_operation")]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Ahmed solves x + 6 = 10 and gets x = 16. What went wrong?", "احمد x + 6 = 10 حل کر کے x = 16 نکالتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("undo", "He added 6 instead of taking it away. x = 4.", "اس نے 6 گھٹانے کی بجائے جمع کیا۔ x = 4", True,
          "Yes! Check: 4 + 6 = 10. And 16 + 6 = 22.", "جی ہاں! جانچ: 4 + 6 = 10۔ اور 16 + 6 = 22"),
      opt("sixty", "He should multiply: x = 60.", "اسے ضرب دینی چاہیے: x = 60", False,
          "Check: 60 + 6 = 66, not 10. Take 6 away: x = 4.", "جانچیں: 60 + 6 = 66، نہ کہ 10۔ 6 گھٹائیں: x = 4"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Check: 16 + 6 = 22, not 10. x = 4.", "جانچیں: 16 + 6 = 22، نہ کہ 10۔ x = 4", "same_operation"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why must we do the same thing to BOTH sides of an equation? Can you teach me?",
                     "مساوات کے دونوں طرف ایک ہی کام کیوں کرنا ضروری ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we take 5 from both sides of x + 5 = 12, and not just one side?",
              "اپنے الفاظ میں بتائیں: x + 5 = 12 میں ہم دونوں طرف سے 5 کیوں گھٹاتے ہیں، صرف ایک طرف سے کیوں نہیں؟"),
    "key_idea": "The equals sign means both sides are the same amount, like a balance. Changing only one side breaks the balance, so whatever we do to one side we must do to the other.",
    "levels": {
      "got_it": "Explains that the two sides are equal (balanced) and changing only one side would make them unequal.",
      "partly": "Says we must keep it fair or balanced, without linking to the equals sign.",
      "not_yet": "Gives no reason, or says one side is enough."},
    "keywords": [
      ["equal", "same", "برابر", "barabar"],
      ["balance", "ترازو", "توازن", "tarazu"],
      ["both", "دونوں", "dono"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The two sides stay equal only if we change both the same way.", "بہت خوب! دونوں طرف تبھی برابر رہتے ہیں جب دونوں کو ایک جیسا بدلیں۔"),
      "partly": T("Good start! Now say what the = sign tells us about the two sides.", "اچھی شروعات! اب بتائیں = کا نشان دونوں طرف کے بارے میں کیا بتاتا ہے۔"),
      "not_yet": T("Think of a balance with x + 5 on one pan and 12 on the other. What happens if you take 5 off one pan only?", "ایک ترازو سوچیں جس کے ایک پلڑے میں x + 5 اور دوسرے میں 12 ہو۔ اگر صرف ایک پلڑے سے 5 اٹھائیں تو کیا ہوگا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_two_step",
     T("Solve 4n − 3 = 25. What is n?", "4n − 3 = 25 حل کریں۔ n کتنا ہے؟"),
     S11,
     T("Add 3 to both sides first: 4n = 28. Then divide by 4.", "پہلے دونوں طرف 3 جمع کریں: 4n = 28۔ پھر 4 سے تقسیم کریں۔"),
     T("Right! n = 7. Check: 4 × 7 − 3 = 25.", "درست! n = 7۔ جانچ: 4 × 7 − 3 = 25"),
     T("4n − 3 = 25, so 4n = 28 and n = 28 ÷ 4 = 7.", "4n − 3 = 25، تو 4n = 28 اور n = 28 ÷ 4 = 7"),
     common_wrong=[wrong(28, "That is 4n. Now divide by 4: n = 7.", "یہ 4n ہے۔ اب 4 سے تقسیم کریں: n = 7"),
                   wrong(5.5, "Add 3, don't take it away: 4n = 28, so n = 7.", "3 گھٹائیں نہیں، جمع کریں: 4n = 28، اس لیے n = 7", "same_operation")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can solve equations now!", "اب آپ مساوات حل کر سکتے ہیں!"),
    "text": T("An equation is a balance. To find the letter, undo each operation by doing the opposite to both sides: x + 5 = 12 gives x = 7; 3x = 18 gives x = 6. For two steps, undo the + or − first, then the × or ÷. Always check by putting the answer back in.",
              "مساوات ایک ترازو ہے۔ حرف معلوم کرنے کے لیے ہر عمل کو الٹیں، دونوں طرف الٹا عمل کر کے: x + 5 = 12 سے x = 7؛ 3x = 18 سے x = 6۔ دو قدم ہوں تو پہلے + یا − کو الٹیں، پھر × یا ÷ کو۔ ہمیشہ جواب واپس رکھ کر جانچیں۔"),
    "points": [T("Do the same to both sides.", "دونوں طرف ایک جیسا کریں۔"),
               T("Check: put your answer back into the equation.", "جانچیں: اپنا جواب مساوات میں واپس رکھیں۔")]},
 ],
 "review_questions": [
   {"id": "r_add", "type": "apply", "skill": SKILL, "step": number_question(
     "r_add",
     T("Solve a + 9 = 15. What is a?", "a + 9 = 15 حل کریں۔ a کتنا ہے؟"),
     R1,
     T("Take 9 from both sides.", "دونوں طرف سے 9 گھٹائیں۔"),
     T("Right! a = 6.", "درست! a = 6"),
     T("15 − 9 = 6, so a = 6.", "15 − 9 = 6، اس لیے a = 6"),
     common_wrong=[wrong(24, "Check: 24 + 9 = 33, not 15. Take 9 away: 6.", "جانچیں: 24 + 9 = 33، نہ کہ 15۔ 9 گھٹائیں: 6", "same_operation")],
     qtype=None)},
   {"id": "r_times", "type": "recall", "skill": SKILL, "step": number_question(
     "r_times",
     T("Solve 6y = 42. What is y?", "6y = 42 حل کریں۔ y کتنا ہے؟"),
     R2,
     T("Divide both sides by 6.", "دونوں طرف 6 سے تقسیم کریں۔"),
     T("Right! y = 7.", "درست! y = 7"),
     T("42 ÷ 6 = 7, so y = 7.", "42 ÷ 6 = 7، اس لیے y = 7"),
     common_wrong=[wrong(36, "6y is 6 × y, so divide: 42 ÷ 6 = 7.", "6y یعنی 6 × y، اس لیے تقسیم: 42 ÷ 6 = 7", "wrong_inverse")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Introduction to Algebra unit. No textbook text or exercises were used.",
   "Equations are taught as a balance: do the opposite operation to both sides, then check. Step s8 uses the same step-by-step working checker as the Grade 9 equations lesson.",
   "Urdu terms to check: مساوات (equation), حل کرنا (solve).",
   "The numbers were worked out in content/sources/g6-maths-07/simple_equations.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
import re

from figs import attach, balance, bar_model, tiles_figure, tiles_en, tiles_ur

BAL_EN = "(a bag stands for the unknown number, each small square for 1)"
BAL_UR = "(تھیلا نامعلوم عدد ہے، ہر چھوٹا مربع 1 ہے)"


def parts(equation):
    """'2x + 1 = 9' -> (2, 'x', 1, 9)."""
    m = re.fullmatch(r"(\d*)([a-z])(?: \+ (\d+))? = (\d+)", equation)
    k, letter, b, right = m.groups()
    return int(k or 1), letter, int(b or 0), int(right)


def scale(equation, *, take=False, under=None, cols=5, en_extra="", ur_extra=""):
    """A balance for an equation like 2x + 1 = 9: bags and squares on the
    left, squares on the right. take: the left squares, and as many on the
    right, are dashed (taken from both sides)."""
    k, letter, b, right = parts(equation)
    answer = solve(equation, letter)
    assert k * answer + b == right
    left = [("bags", k, letter)] + ([("units", b, min(cols, b), 0 if take else None)] if b else [])
    right_side = [("units", right, cols, right - b if take else None)]
    bags = f"{k} bags" if k > 1 else "a bag"
    bags_ur = f"{k} تھیلے" if k > 1 else "ایک تھیلا"
    squares = f" and {b} small squares" if b else ""
    squares_ur = f" اور {b} چھوٹے مربعے" if b else ""
    return balance(left, right_side,
        f"A level balance for {equation}. Left pan: {bags} marked {letter}{squares}. Right pan: {right} small squares. {BAL_EN}{en_extra}",
        f"{equation} کا برابر ترازو۔ بایاں پلڑا: {bags_ur} جن پر {letter} لکھا ہے{squares_ur}۔ دایاں پلڑا: {right} چھوٹے مربعے۔ {BAL_UR}{ur_extra}",
        under=under, cols=cols), answer


def boxes_bar(k, letter, total, en, ur, answer):
    """k equal boxes marked with the letter, with the total over them."""
    each = total // k
    assert each * k == total and each == answer
    return bar_model([[(each, letter, False)] * k], en, ur, total=str(total))


_, _, B3, _ = parts("x + 5 = 12")
S3_FIG, S3_X = scale("x + 5 = 12", take=True, under=f"x={S4}",
    en_extra=f" The {B3} squares on the left and {B3} of the squares on the right are dashed: they are taken away from both sides, leaving x = {S4}.",
    ur_extra=f" بائیں طرف کے {B3} مربعے اور دائیں طرف کے {B3} مربعے ڈیش والے ہیں: انہیں دونوں طرف سے نکالا گیا، باقی x = {S4} بچتا ہے۔")
assert S3_X == S4
K12, _, _, R12 = parts("3x = 18")
S12_FIG, S12_X = scale("3x = 18", cols=S6, under=f"x={S6}",
    en_extra=f" The {R12} squares are in {K12} rows of {S6}, one row for each bag, so x = {S6}.",
    ur_extra=f" {R12} مربعے {S6} کی {K12} قطاروں میں ہیں، ہر تھیلے کے لیے ایک قطار، اس لیے x = {S6}۔")
assert S12_X == S6

Y5, TAKE5 = S5, 4                     # s5: y − 4 = 9
assert Y5 - TAKE5 == 9
M7, PARTS7 = S7, 4                    # s7: m ÷ 4 = 5
assert M7 // PARTS7 == 5 and M7 % PARTS7 == 0
N11, TAKE11 = S11, 3                  # s11: 4n − 3 = 25
assert 4 * N11 - TAKE11 == 25
N_QB, TAKE_QB = solve("n - 3 = 8", "n"), 3
assert N_QB - TAKE_QB == 8

attach(lesson, {
    "s1_hook": scale("x + 5 = 12")[0],
    "s2_foundation": tiles_figure([[("terms", [(5, "y")]), ("op", "+"), ("terms", [(2, "y")])]], ("y",),
        f"Algebra tiles: a group of 5 y-tiles named 5y, a plus sign, and a group of 2 y-tiles named 2y. {tiles_en(('y',))}",
        f"الجبرا ٹائلیں: 5 ٹائلیں y کا گروہ جس کا نام 5y، جمع کا نشان، اور 2 ٹائلیں y کا گروہ جس کا نام 2y۔ {tiles_ur(('y',))}"),
    "s3_balance": S3_FIG,
    "s5_subtract": bar_model([[(Y5, "y", False)], [(Y5 - TAKE5, str(Y5 - TAKE5), False), (TAKE5, str(TAKE5), True)]],
        f"Two bars of the same length. The top bar is y. The bottom bar is split into {Y5 - TAKE5} and a dashed piece of {TAKE5}: taking {TAKE5} away from y leaves {Y5 - TAKE5}.",
        f"ایک جتنی لمبی دو پٹیاں۔ اوپر والی پٹی y ہے۔ نیچے والی پٹی {Y5 - TAKE5} اور {TAKE5} کے ڈیش والے ٹکڑے میں بٹی ہے: y میں سے {TAKE5} نکالیں تو {Y5 - TAKE5} بچتا ہے۔"),
    "s6_times": scale("3x = 18", cols=6)[0],
    "s7_divide": bar_model([[(M7, "m", False)], [(M7 // PARTS7, str(M7 // PARTS7), False)] * PARTS7],
        f"Two bars of the same length. The top bar is m. The bottom bar is m cut into {PARTS7} equal parts, each marked {M7 // PARTS7}: m ÷ {PARTS7} = {M7 // PARTS7}.",
        f"ایک جتنی لمبی دو پٹیاں۔ اوپر والی پٹی m ہے۔ نیچے والی پٹی m کے {PARTS7} برابر حصے ہیں، ہر ایک پر {M7 // PARTS7} لکھا ہے: m ÷ {PARTS7} = {M7 // PARTS7}۔"),
    "s8_two_step": scale("2x + 1 = 9")[0],
    "s9_find_error": scale("x + 6 = 10")[0],
    "s11_two_step": bar_model([[(N11, "n", False)] * 4, [(4 * N11 - TAKE11, str(4 * N11 - TAKE11), False), (TAKE11, str(TAKE11), True)]],
        f"Two bars of the same length. The top bar is 4 equal boxes marked n, which is 4n. The bottom bar is split into {4 * N11 - TAKE11} and a dashed piece of {TAKE11}: taking {TAKE11} from 4n leaves {4 * N11 - TAKE11}.",
        f"ایک جتنی لمبی دو پٹیاں۔ اوپر والی پٹی n والے 4 برابر خانے ہیں، یعنی 4n۔ نیچے والی پٹی {4 * N11 - TAKE11} اور {TAKE11} کے ڈیش والے ٹکڑے میں بٹی ہے: 4n میں سے {TAKE11} نکالیں تو {4 * N11 - TAKE11} بچتا ہے۔"),
    "s12_summary": S12_FIG,
    "qb_recall": scale("x + 3 = 10")[0],
    "qb_apply": boxes_bar(5, "k", 35,
        "A bar of 5 equal boxes, each marked k, with 35 over the whole bar: 5k = 35.",
        "5 برابر خانوں کی پٹی، ہر خانے پر k لکھا ہے، اور پوری پٹی کے اوپر 35: یعنی 5k = 35۔", QB),
    "qb_find_error": bar_model([[(N_QB, "n", False)], [(N_QB - TAKE_QB, str(N_QB - TAKE_QB), False), (TAKE_QB, str(TAKE_QB), True)]],
        f"Two bars of the same length. The top bar is n. The bottom bar is split into {N_QB - TAKE_QB} and a dashed piece of {TAKE_QB}: taking {TAKE_QB} from n leaves {N_QB - TAKE_QB}.",
        f"ایک جتنی لمبی دو پٹیاں۔ اوپر والی پٹی n ہے۔ نیچے والی پٹی {N_QB - TAKE_QB} اور {TAKE_QB} کے ڈیش والے ٹکڑے میں بٹی ہے: n میں سے {TAKE_QB} نکالیں تو {N_QB - TAKE_QB} بچتا ہے۔"),
    "r_add": scale("a + 9 = 15")[0],
    "r_times": boxes_bar(6, "y", 42,
        "A bar of 6 equal boxes, each marked y, with 42 over the whole bar: 6y = 42.",
        "6 برابر خانوں کی پٹی، ہر خانے پر y لکھا ہے، اور پوری پٹی کے اوپر 42: یعنی 6y = 42۔", R2),
})
write(lesson)

from common import (T, opt, say, wrong, number_question, text_question, write, value,
                    REF, REVIEW, ALG_VARIABLES, ALG_SUBSTITUTION, ALG_LIKE_TERMS, ALG_EQUATIONS, ALG_WORD_PROBLEMS)

SKILL = ALG_WORD_PROBLEMS


def solve(equation, letter):
    """The whole number from 0 to 200 that makes the equation true (only one may)."""
    left, right = equation.split("=")
    found = [n for n in range(0, 201) if value(left, **{letter: n}) == value(right, **{letter: n})]
    assert len(found) == 1, (equation, found)
    return found[0]


# s2
assert solve("x + 8 = 20", "x") == 12
# s4, s5: stickers
S5 = solve("s + 6 = 21", "s")
assert S5 == 15 and 21 + 6 == 27
# s6: 3 notebooks cost 135
S6 = solve("3n = 135", "n")
assert S6 == 45 and 135 - 3 == 132
# s7: Bilal's age doubled plus 4 is 30
S7 = solve("2a + 4 = 30", "a")
assert S7 == 13 and (30 + 4) // 2 == 17
# s8: Omar o, Ali o + 5, together 31
S8 = solve("o + o + 5 = 31", "o")
assert S8 == 13 and S8 + 5 == 18
# s9: a number take away 7 is 12
assert solve("n - 7 = 12", "n") == 19
# unit test
assert value("4t", t=3) == 12
U2 = value("5x - 2", x=3)
assert U2 == 13 and 53 - 2 == 51 and 5 * (3 - 2) == 5
assert all(value("6a + 2 + a", a=a) == value("7a + 2", a=a) for a in range(-5, 6))
assert value("6a + 2 + a", a=2) != value("9a", a=2)
U4 = solve("2x + 3 = 15", "x")
assert U4 == 6 and (15 + 3) // 2 == 9
U5 = solve("50 + 20k = 210", "k")
assert U5 == 8 and 210 // 20 == 10
# question bank and review
assert solve("4n = 28", "n") == 7
QB = solve("5p + 3 = 43", "p")
assert QB == 8 and 43 // 5 == 8 and (43 - 3) == 40
assert solve("2n + 5 = 25", "n") == 10 and value("2n + 5", n=15) == 35
R1 = solve("n + 15 = 40", "n")
assert R1 == 25
R2 = solve("7b = 84", "b")
assert R2 == 12


lesson = {
 "id": "g6-maths-07-algebra-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Write and solve simple equations for real-life problems, and check the answer in the story.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Algebra word problems", "الجبرا کے سوالات"),
 "estimated_minutes": 16,
 "prerequisites": [{"skill": ALG_EQUATIONS}, {"skill": ALG_VARIABLES}, {"skill": ALG_SUBSTITUTION}, {"skill": ALG_LIKE_TERMS}],
 "misconceptions": [
   {"id": "wrong_equation", "description": "Writes the wrong operation from the words: 'buys 6 more' as 6s, or 'take away 7' as 7 − n."},
   {"id": "same_operation", "description": "Solves by doing the operation in the equation instead of its opposite."},
   {"id": "answers_wrong_quantity", "description": "Finds a number but not the one the question asks for (Ali's marbles instead of Omar's)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_equation", "type": "recall", "step": {
     "id": "qb_equation", "type": "choice",
     "prompt": T("'A number times 4 is 28.' Which equation fits?", "'ایک عدد کا 4 گنا 28 ہے۔' کون سی مساوات درست ہے؟"),
     "options": [
       opt("times", "4n = 28", "4n = 28", True, "Yes! Times 4 is 4n. So n = 7.", "جی ہاں! 4 گنا یعنی 4n۔ تو n = 7"),
       opt("plus", "n + 4 = 28", "n + 4 = 28", False, "That is 4 more, not 4 times. 4n = 28.", "یہ 4 زیادہ ہے، 4 گنا نہیں۔ 4n = 28", "wrong_equation"),
       opt("minus", "n − 4 = 28", "n − 4 = 28", False, "That is 4 less. Times 4 is 4n = 28.", "یہ 4 کم ہے۔ 4 گنا یعنی 4n = 28", "wrong_equation"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Amna has 5 full packets of biscuits and 3 loose ones: 43 biscuits in all. How many are in each packet?", "آمنہ کے پاس بسکٹ کے 5 بھرے پیکٹ اور 3 کھلے بسکٹ ہیں: کل 43 بسکٹ۔ ہر پیکٹ میں کتنے ہیں؟"),
     QB,
     T("5p + 3 = 43. Take 3 away first.", "5p + 3 = 43۔ پہلے 3 گھٹائیں۔"),
     T("Right! 8 in each packet. Check: 5 × 8 + 3 = 43.", "درست! ہر پیکٹ میں 8۔ جانچ: 5 × 8 + 3 = 43"),
     T("5p + 3 = 43, so 5p = 40 and p = 8.", "5p + 3 = 43، تو 5p = 40 اور p = 8"),
     common_wrong=[wrong(40, "40 is all the biscuits in packets. Each packet: 40 ÷ 5 = 8.", "40 پیکٹوں کے سارے بسکٹ ہیں۔ ہر پیکٹ: 40 ÷ 5 = 8", "answers_wrong_quantity"),
                   wrong(9.2, "Take the 3 loose ones away first: 5p = 40, p = 8.", "پہلے 3 کھلے بسکٹ گھٹائیں: 5p = 40، p = 8", "same_operation")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Zain solves 2n + 5 = 25 and gets n = 15. What went wrong?", "زین 2n + 5 = 25 حل کر کے n = 15 نکالتا ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("check", "Check: 2 × 15 + 5 = 35, not 25. It should be n = 10.", "جانچ: 2 × 15 + 5 = 35، نہ کہ 25۔ n = 10 ہونا چاہیے۔", True,
           "Yes! 25 − 5 = 20, then 20 ÷ 2 = 10.", "جی ہاں! 25 − 5 = 20، پھر 20 ÷ 2 = 10"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Put it back in: 2 × 15 + 5 = 35. The answer is n = 10.", "واپس رکھیں: 2 × 15 + 5 = 35۔ جواب n = 10 ہے۔", "same_operation"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_steps", "front": T("How do you solve a word problem with algebra?", "الجبرا سے سوال کیسے حل کریں؟"),
    "back": T("1. Use a letter for the unknown. 2. Write an equation. 3. Solve it. 4. Check it in the story and answer in words.", "1۔ نامعلوم کے لیے حرف لیں۔ 2۔ مساوات لکھیں۔ 3۔ حل کریں۔ 4۔ کہانی میں جانچیں اور الفاظ میں جواب دیں۔")},
 ],
 "home_tasks": [{"id": "h_shop", "text": T(
   "Next time someone buys several of the same thing, note the total cost and how many. Write an equation like 4n = 260 and solve it to find the price of one. Check with the shopkeeper's price!",
   "اگلی بار جب کوئی ایک جیسی کئی چیزیں خریدے تو کل قیمت اور تعداد لکھ لیں۔ 4n = 260 جیسی مساوات لکھ کر ایک چیز کی قیمت نکالیں۔ دکاندار کی قیمت سے جانچیں!")}],
 "glossary": [T("Unknown", "نامعلوم"), T("Equation", "مساوات")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Three notebooks cost 135 rupees. How much is one? Algebra can answer questions like this!",
                     "تین کاپیاں 135 روپے کی ہیں۔ ایک کتنے کی ہے؟ الجبرا ایسے سوالوں کا جواب دے سکتا ہے!"),
    "text": T("Today we turn stories into equations and solve them. First, a quick check.", "آج ہم کہانیوں کو مساوات میں بدل کر حل کریں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Solve x + 8 = 20. What is x?", "x + 8 = 20 حل کریں۔ x کتنا ہے؟"),
     12,
     T("Take 8 from both sides.", "دونوں طرف سے 8 گھٹائیں۔"),
     T("Right! x = 12.", "درست! x = 12"),
     T("20 − 8 = 12, so x = 12.", "20 − 8 = 12، اس لیے x = 12"),
     common_wrong=[wrong(28, "Check: 28 + 8 = 36. Take 8 away: 12.", "جانچیں: 28 + 8 = 36۔ 8 گھٹائیں: 12")],
     qtype="recall", skill=ALG_EQUATIONS),
   {"id": "s3_steps", "type": "explain",
    "character": say("thinking", "Four steps: letter, equation, solve, check!", "چار قدم: حرف، مساوات، حل، جانچ!"),
    "text": T("1. Choose a letter for the number you don't know. 2. Turn the words into an equation. 3. Solve it. 4. Check the answer makes sense in the story, and answer in words.",
              "1۔ نامعلوم عدد کے لیے حرف چنیں۔ 2۔ الفاظ کو مساوات میں بدلیں۔ 3۔ اسے حل کریں۔ 4۔ جانچیں کہ جواب کہانی میں ٹھیک ہے، اور الفاظ میں جواب دیں۔")},
   {"id": "s4_write", "type": "choice", "question_type": "apply",
    "prompt": T("Ayesha has s stickers. She buys 6 more and now has 21. Which equation fits?", "عائشہ کے پاس s اسٹیکر ہیں۔ وہ 6 اور خریدتی ہے اور اب اس کے پاس 21 ہیں۔ کون سی مساوات درست ہے؟"),
    "options": [
      opt("plus", "s + 6 = 21", "s + 6 = 21", True, "Yes! 6 more means + 6.", "جی ہاں! 6 اور یعنی + 6"),
      opt("times", "6s = 21", "6s = 21", False, "6s means 6 times as many. She bought 6 more: s + 6 = 21.", "6s یعنی 6 گنا۔ اس نے 6 اور خریدے: s + 6 = 21", "wrong_equation"),
      opt("minus", "s − 6 = 21", "s − 6 = 21", False, "Buying adds stickers: s + 6 = 21.", "خریدنے سے اسٹیکر بڑھتے ہیں: s + 6 = 21", "wrong_equation"),
    ]},
   number_question(
     "s5_stickers",
     T("Solve s + 6 = 21. How many stickers did Ayesha have at first?", "s + 6 = 21 حل کریں۔ شروع میں عائشہ کے پاس کتنے اسٹیکر تھے؟"),
     S5,
     T("Take 6 from both sides.", "دونوں طرف سے 6 گھٹائیں۔"),
     T("Right! 15 stickers. Check: 15 + 6 = 21.", "درست! 15 اسٹیکر۔ جانچ: 15 + 6 = 21"),
     T("21 − 6 = 15 stickers.", "21 − 6 = 15 اسٹیکر"),
     common_wrong=[wrong(27, "Check: 27 + 6 = 33, not 21. Take 6 away: 15.", "جانچیں: 27 + 6 = 33، نہ کہ 21۔ 6 گھٹائیں: 15", "same_operation")]),
   number_question(
     "s6_notebooks",
     T("3 notebooks cost 135 rupees. Write 3n = 135 and find n, the price of one notebook.", "3 کاپیاں 135 روپے کی ہیں۔ 3n = 135 لکھیں اور n یعنی ایک کاپی کی قیمت معلوم کریں۔"),
     S6,
     T("Divide both sides by 3.", "دونوں طرف 3 سے تقسیم کریں۔"),
     T("Right! 45 rupees. Check: 3 × 45 = 135.", "درست! 45 روپے۔ جانچ: 3 × 45 = 135"),
     T("135 ÷ 3 = 45 rupees.", "135 ÷ 3 = 45 روپے"),
     common_wrong=[wrong(132, "3n is 3 × n, so divide: 135 ÷ 3 = 45.", "3n یعنی 3 × n، اس لیے تقسیم: 135 ÷ 3 = 45", "same_operation")]),
   number_question(
     "s7_age",
     T("Bilal doubles his age and adds 4. He gets 30. Write 2a + 4 = 30 and find his age a.", "بلال اپنی عمر دگنی کر کے 4 جمع کرتا ہے تو 30 آتا ہے۔ 2a + 4 = 30 لکھیں اور اس کی عمر a معلوم کریں۔"),
     S7,
     T("Take 4 from both sides first, then divide by 2.", "پہلے دونوں طرف سے 4 گھٹائیں، پھر 2 سے تقسیم کریں۔"),
     T("Right! Bilal is 13. Check: 2 × 13 + 4 = 30.", "درست! بلال 13 سال کا ہے۔ جانچ: 2 × 13 + 4 = 30"),
     T("2a = 30 − 4 = 26, so a = 13.", "2a = 30 − 4 = 26، اس لیے a = 13"),
     common_wrong=[wrong(17, "Take the 4 away, don't add it: 2a = 26, a = 13.", "4 جمع نہیں، گھٹائیں: 2a = 26، a = 13", "same_operation"),
                   wrong(26, "That is 2a, double his age. Halve it: 13.", "یہ 2a ہے، دگنی عمر۔ آدھا کریں: 13", "answers_wrong_quantity")]),
   number_question(
     "s8_together",
     T("Ali has 5 more marbles than Omar. Together they have 31. Call Omar's marbles o, so o + o + 5 = 31. How many does OMAR have?", "علی کے پاس عمر سے 5 کنچے زیادہ ہیں۔ دونوں کے پاس مل کر 31 ہیں۔ عمر کے کنچوں کو o کہیں، تو o + o + 5 = 31۔ عمر کے پاس کتنے ہیں؟"),
     S8,
     T("o + o is 2o. Then 2o + 5 = 31.", "o + o یعنی 2o۔ پھر 2o + 5 = 31"),
     T("Right! Omar has 13 and Ali has 18. Check: 13 + 18 = 31.", "درست! عمر کے 13 اور علی کے 18۔ جانچ: 13 + 18 = 31"),
     T("2o + 5 = 31, so 2o = 26 and o = 13.", "2o + 5 = 31، تو 2o = 26 اور o = 13"),
     common_wrong=[wrong(18, "18 is Ali's marbles. The question asks for Omar's: 13.", "18 علی کے کنچے ہیں۔ سوال عمر کے بارے میں ہے: 13", "answers_wrong_quantity"),
                   wrong(26, "That is 2o. Halve it: Omar has 13.", "یہ 2o ہے۔ آدھا کریں: عمر کے 13", "answers_wrong_quantity")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("'I think of a number and take away 7. I get 12.' Sana writes 7 − n = 12. What went wrong?", "'میں ایک عدد سوچ کر اس میں سے 7 گھٹاتی ہوں۔ 12 آتا ہے۔' ثنا 7 − n = 12 لکھتی ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("order", "Start with the number: n − 7 = 12, so n = 19.", "عدد سے شروع کریں: n − 7 = 12، تو n = 19", True,
          "Yes! Check: 19 − 7 = 12.", "جی ہاں! جانچ: 19 − 7 = 12"),
      opt("plus", "It should be n + 7 = 12.", "یہ n + 7 = 12 ہونا چاہیے۔", False,
          "Take away means −. Start with the number: n − 7 = 12.", "گھٹانا یعنی −۔ عدد سے شروع کریں: n − 7 = 12"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "7 − n takes the number from 7. It should be n − 7 = 12, so n = 19.", "7 − n میں عدد کو 7 سے گھٹاتے ہیں۔ یہ n − 7 = 12 ہونا چاہیے، تو n = 19", "wrong_equation"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why should we check our answer in the story, not just in the equation? Can you teach me?",
                     "ہمیں اپنا جواب صرف مساوات میں نہیں، کہانی میں بھی کیوں جانچنا چاہیے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is it good to check your answer in the story at the end?",
              "اپنے الفاظ میں بتائیں: آخر میں جواب کو کہانی میں جانچنا کیوں اچھا ہے؟"),
    "key_idea": "The equation might have been written wrongly, or we might have found a different quantity from the one asked. Putting the answer back into the story catches both mistakes and shows the answer makes sense.",
    "levels": {
      "got_it": "Explains that checking in the story catches a wrong equation or answering the wrong quantity, and shows the answer makes sense.",
      "partly": "Says checking finds mistakes, without saying which kind or why the story matters.",
      "not_yet": "Gives no reason, or says checking isn't needed."},
    "keywords": [
      ["check", "جانچ", "jaanch"],
      ["story", "question", "کہانی", "سوال", "sense", "ٹھیک"],
      ["wrong", "mistake", "غلط", "غلطی", "ghalti"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The story check catches a wrong equation or a wrong answer.", "بہت خوب! کہانی میں جانچ غلط مساوات یا غلط جواب پکڑ لیتی ہے۔"),
      "partly": T("Good start! Think of Ali and Omar: what mistake would the story check catch?", "اچھی شروعات! علی اور عمر کا سوچیں: کہانی میں جانچ کون سی غلطی پکڑتی؟"),
      "not_yet": T("Remember Ali and Omar: 18 solved the sum but answered about the wrong boy. How could we have spotted that?", "علی اور عمر یاد کریں: 18 بھی ایک جواب تھا مگر غلط لڑکے کا۔ ہم یہ کیسے پکڑ سکتے تھے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole algebra unit. You can do it!",
                     "ٹیسٹ کا وقت! الجبرا کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on writing expressions, substitution, like terms, equations and a word problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں عبارت لکھنے، قیمت رکھنے، یکساں رقوم، مساوات اور ایک کہانی والے سوال ہیں۔ آرام سے کریں۔")},
   text_question(
     "u1_write",
     T("Test 1: Write an expression for '4 times t'.", "ٹیسٹ 1: 't کا 4 گنا' کی عبارت لکھیں۔"),
     "4t",
     T("Number first, no × sign.", "عدد پہلے، × کے بغیر۔"),
     T("Right! 4t.", "درست! 4t"),
     T("4 × t = 4t.", "4 × t = 4t"),
     accept=["4*t", "t*4", "t4"],
     common_wrong=[wrong("t + 4", "That is 4 more. 4 times t is 4t.", "یہ 4 زیادہ ہے۔ t کا 4 گنا 4t ہے۔")],
     qtype="recall", skill=ALG_VARIABLES),
   number_question(
     "u2_substitute",
     T("Test 2: Find the value of 5x − 2 when x = 3.", "ٹیسٹ 2: جب x = 3 ہو تو 5x − 2 کی قیمت معلوم کریں۔"),
     U2,
     T("5 × 3 first, then take away 2.", "پہلے 5 × 3، پھر 2 گھٹائیں۔"),
     T("Right! 15 − 2 = 13.", "درست! 15 − 2 = 13"),
     T("5 × 3 = 15, then 15 − 2 = 13.", "5 × 3 = 15، پھر 15 − 2 = 13"),
     common_wrong=[wrong(51, "5x is 5 × x, not 53. 15 − 2 = 13.", "5x یعنی 5 × x، نہ کہ 53۔ 15 − 2 = 13"),
                   wrong(5, "Multiply first: 5 × 3 = 15, then − 2 = 13.", "پہلے ضرب: 5 × 3 = 15، پھر − 2 = 13")],
     qtype="apply", skill=ALG_SUBSTITUTION),
   text_question(
     "u3_simplify",
     T("Test 3: Simplify 6a + 2 + a.", "ٹیسٹ 3: 6a + 2 + a کو مختصر کریں۔"),
     "7a + 2",
     T("a on its own is 1a. The 2 stays.", "اکیلا a یعنی 1a۔ 2 ویسے ہی رہے گا۔"),
     T("Right! 7a + 2.", "درست! 7a + 2"),
     T("6a + a = 7a, and the 2 stays: 7a + 2.", "6a + a = 7a، اور 2 ویسے ہی: 7a + 2"),
     accept=["2 + 7a"],
     common_wrong=[wrong("9a", "2 has no letter, so it stays apart: 7a + 2.", "2 میں حرف نہیں، اس لیے الگ رہتا ہے: 7a + 2"),
                   wrong("6a + 2", "Don't forget the last a (1a): 7a + 2.", "آخری a نہ بھولیں (1a): 7a + 2")],
     qtype="apply", skill=ALG_LIKE_TERMS),
   number_question(
     "u4_equation",
     T("Test 4: Solve 2x + 3 = 15. What is x?", "ٹیسٹ 4: 2x + 3 = 15 حل کریں۔ x کتنا ہے؟"),
     U4,
     T("Take 3 from both sides, then divide by 2.", "دونوں طرف سے 3 گھٹائیں، پھر 2 سے تقسیم کریں۔"),
     T("Right! x = 6. Check: 2 × 6 + 3 = 15.", "درست! x = 6۔ جانچ: 2 × 6 + 3 = 15"),
     T("2x = 15 − 3 = 12, so x = 6.", "2x = 15 − 3 = 12، اس لیے x = 6"),
     common_wrong=[wrong(9, "Take the 3 away, don't add it: 2x = 12, x = 6.", "3 جمع نہیں، گھٹائیں: 2x = 12، x = 6"),
                   wrong(12, "That is 2x. Divide by 2: x = 6.", "یہ 2x ہے۔ 2 سے تقسیم کریں: x = 6")],
     qtype="apply", skill=ALG_EQUATIONS),
   number_question(
     "u5_taxi",
     T("Test 5: A taxi charges 50 rupees plus 20 rupees for each km. A ride costs 210 rupees. Write 50 + 20k = 210. How many km was the ride?", "ٹیسٹ 5: ٹیکسی 50 روپے اور ہر کلومیٹر کے 20 روپے لیتی ہے۔ ایک سفر 210 روپے کا ہوا۔ 50 + 20k = 210 لکھیں۔ سفر کتنے کلومیٹر کا تھا؟"),
     U5,
     T("Take 50 from both sides, then divide by 20.", "دونوں طرف سے 50 گھٹائیں، پھر 20 سے تقسیم کریں۔"),
     T("Right! 8 km. Check: 50 + 20 × 8 = 210.", "درست! 8 کلومیٹر۔ جانچ: 50 + 20 × 8 = 210"),
     T("20k = 210 − 50 = 160, so k = 8 km.", "20k = 210 − 50 = 160، اس لیے k = 8 کلومیٹر"),
     common_wrong=[wrong(160, "That is 20k, the cost of the km. Divide by 20: 8 km.", "یہ 20k ہے، کلومیٹر کی قیمت۔ 20 سے تقسیم کریں: 8 کلومیٹر", "answers_wrong_quantity"),
                   wrong(10, "Take away the 50 first: 160 ÷ 20 = 8.", "پہلے 50 گھٹائیں: 160 ÷ 20 = 8")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You finished the algebra unit! Well done!", "آپ نے الجبرا کا باب مکمل کر لیا! شاباش!"),
    "text": T("Use a letter for the unknown, turn the words into an equation, solve it by doing the same to both sides, then check in the story and answer the question that was asked.",
              "نامعلوم کے لیے حرف لیں، الفاظ کو مساوات میں بدلیں، دونوں طرف ایک جیسا کر کے حل کریں، پھر کہانی میں جانچیں اور وہی جواب دیں جو پوچھا گیا ہے۔"),
    "points": [T("'More' is +, 'less' or 'take away' is −, 'times' or 'each' is ×.", "'زیادہ' یعنی +، 'کم' یا 'گھٹانا' یعنی −، 'گنا' یا 'ہر ایک' یعنی ×"),
               T("Answer the question asked: Omar's marbles, not Ali's.", "وہی جواب دیں جو پوچھا گیا: عمر کے کنچے، علی کے نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_plus", "type": "apply", "skill": SKILL, "step": number_question(
     "r_plus",
     T("A number plus 15 is 40. What is the number?", "ایک عدد جمع 15 برابر 40 ہے۔ وہ عدد کیا ہے؟"),
     R1,
     T("n + 15 = 40. Take 15 from both sides.", "n + 15 = 40۔ دونوں طرف سے 15 گھٹائیں۔"),
     T("Right! 25.", "درست! 25"),
     T("40 − 15 = 25.", "40 − 15 = 25"),
     common_wrong=[wrong(55, "Check: 55 + 15 = 70. Take 15 away: 25.", "جانچیں: 55 + 15 = 70۔ 15 گھٹائیں: 25", "same_operation")],
     qtype=None)},
   {"id": "r_bags", "type": "recall", "skill": SKILL, "step": number_question(
     "r_bags",
     T("7 equal bags hold 84 mangoes. How many mangoes are in each bag?", "7 برابر تھیلوں میں 84 آم ہیں۔ ہر تھیلے میں کتنے آم ہیں؟"),
     R2,
     T("7b = 84. Divide both sides by 7.", "7b = 84۔ دونوں طرف 7 سے تقسیم کریں۔"),
     T("Right! 12 mangoes.", "درست! 12 آم"),
     T("84 ÷ 7 = 12.", "84 ÷ 7 = 12"),
     common_wrong=[wrong(77, "7b is 7 × b, so divide: 84 ÷ 7 = 12.", "7b یعنی 7 × b، اس لیے تقسیم: 84 ÷ 7 = 12", "same_operation")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Introduction to Algebra unit. No textbook text or exercises were used.",
   "Each problem follows four steps: letter, equation, solve, check in the story. Step s8 checks that the child answers the quantity asked for.",
   "Steps u1 to u5 are a short unit test; each is tagged with the skill of the lesson it comes from.",
   "The numbers were worked out in content/sources/g6-maths-07/algebra_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import attach, balance, bar_model, strip_figure

BAL_EN = "(a bag stands for the unknown number, each small square for 1)"
BAL_UR = "(تھیلا نامعلوم عدد ہے، ہر چھوٹا مربع 1 ہے)"


def bar(parts, total, en, ur):
    """One bar of boxes (value, text), with the total over it; the boxes
    must add up to the total."""
    assert sum(v for v, _ in parts) == total, (parts, total)
    return bar_model([[(v, t, False) for v, t in parts]], en, ur, total=str(total))


X2, ADD2, TOTAL2 = solve("x + 8 = 20", "x"), 8, 20
assert X2 + ADD2 == TOTAL2
MORE4, HAS4 = 6, 21                       # s4, s5: s + 6 = 21
assert S5 + MORE4 == HAS4
BOOKS, COST = 3, 135                      # s1, s6, s12: 3n = 135
assert BOOKS * S6 == COST
PLUS7, GOT7 = 4, 30                       # s7: 2a + 4 = 30
assert 2 * S7 + PLUS7 == GOT7
MORE8, TOGETHER8 = 5, 31                  # s8: o + o + 5 = 31
assert 2 * S8 + MORE8 == TOGETHER8
ADD_U4, TOTAL_U4 = 3, 15                  # u4: 2x + 3 = 15
assert 2 * U4 + ADD_U4 == TOTAL_U4
BASE5, PER_KM, FARE = 50, 20, 210         # u5: 50 + 20k = 210
assert BASE5 + PER_KM * U5 == FARE
PACKETS, LOOSE, BISCUITS = 5, 3, 43       # qb_apply: 5p + 3 = 43
assert PACKETS * QB + LOOSE == BISCUITS
N_QB = solve("2n + 5 = 25", "n")          # qb_find_error
assert 2 * N_QB + 5 == 25
PLUS_R1, TOTAL_R1 = 15, 40                # r_plus: n + 15 = 40
assert R1 + PLUS_R1 == TOTAL_R1
BAGS_R2, MANGOES = 7, 84                  # r_bags: 7b = 84
assert BAGS_R2 * R2 == MANGOES

NOTEBOOKS_EN = f"A bar of {BOOKS} equal boxes, one for each notebook, with {COST} rupees over the whole bar."
NOTEBOOKS_UR = f"{BOOKS} برابر خانوں کی پٹی، ہر کاپی کا ایک خانہ، اور پوری پٹی کے اوپر {COST} روپے۔"

attach(lesson, {
    "s1_hook": bar([(S6, "?")] * BOOKS, COST,
        NOTEBOOKS_EN + " Each box has a question mark: the price of one notebook.",
        NOTEBOOKS_UR + " ہر خانے پر سوالیہ نشان ہے: ایک کاپی کی قیمت۔"),
    "s2_foundation": balance([("bags", 1, "x"), ("units", ADD2, 4)], [("units", TOTAL2, 5)],
        f"A level balance for x + {ADD2} = {TOTAL2}. Left pan: a bag marked x and {ADD2} small squares. Right pan: {TOTAL2} small squares. {BAL_EN}",
        f"x + {ADD2} = {TOTAL2} کا برابر ترازو۔ بایاں پلڑا: ایک تھیلا جس پر x لکھا ہے اور {ADD2} چھوٹے مربعے۔ دایاں پلڑا: {TOTAL2} چھوٹے مربعے۔ {BAL_UR}"),
    "s4_write": strip_figure([("bag", "s"), ("text", "+"), ("marbles", MORE4, 3), ("text", "="), ("text", HAS4)],
        f"Ayesha's bag of stickers marked s, a plus sign, {MORE4} more stickers (circles), an equals sign and {HAS4}, how many she has now.",
        f"عائشہ کا اسٹیکروں کا تھیلا جس پر s لکھا ہے، جمع کا نشان، {MORE4} مزید اسٹیکر (دائرے)، برابر کا نشان اور {HAS4}، جتنے اب اس کے پاس ہیں۔"),
    "s5_stickers": bar([(S5, "s"), (MORE4, str(MORE4))], HAS4,
        f"A bar split into s (the stickers at first) and {MORE4} (the new ones), with {HAS4} over the whole bar: s + {MORE4} = {HAS4}.",
        f"ایک پٹی جو s (شروع کے اسٹیکر) اور {MORE4} (نئے) میں بٹی ہے، پوری پٹی کے اوپر {HAS4}: یعنی s + {MORE4} = {HAS4}۔"),
    "s6_notebooks": bar([(S6, "n")] * BOOKS, COST,
        NOTEBOOKS_EN + " Each box is marked n, the price of one notebook.",
        NOTEBOOKS_UR + " ہر خانے پر n لکھا ہے، ایک کاپی کی قیمت۔"),
    "s7_age": bar([(S7, "a"), (S7, "a"), (PLUS7, str(PLUS7))], GOT7,
        f"A bar of two equal boxes marked a (Bilal's age, doubled) and a small box of {PLUS7}, with {GOT7} over the whole bar: 2a + {PLUS7} = {GOT7}.",
        f"ایک پٹی جس میں a والے دو برابر خانے (بلال کی عمر کا دگنا) اور {PLUS7} کا چھوٹا خانہ ہے، پوری پٹی کے اوپر {GOT7}: یعنی 2a + {PLUS7} = {GOT7}۔"),
    "s8_together": bar([(S8, "o"), (S8, "o"), (MORE8, str(MORE8))], TOGETHER8,
        f"A bar for all the marbles: a box o for Omar's marbles, then a box o and a box {MORE8} for Ali's (he has {MORE8} more), with {TOGETHER8} over the whole bar: o + o + {MORE8} = {TOGETHER8}.",
        f"تمام کنچوں کی پٹی: عمر کے کنچوں کا خانہ o، پھر علی کے لیے خانہ o اور خانہ {MORE8} (اس کے پاس {MORE8} زیادہ ہیں)، پوری پٹی کے اوپر {TOGETHER8}: یعنی o + o + {MORE8} = {TOGETHER8}۔"),
    "u4_equation": balance([("bags", 2, "x"), ("units", ADD_U4, 3)], [("units", TOTAL_U4, 5)],
        f"A level balance for 2x + {ADD_U4} = {TOTAL_U4}. Left pan: 2 bags marked x and {ADD_U4} small squares. Right pan: {TOTAL_U4} small squares. {BAL_EN}",
        f"2x + {ADD_U4} = {TOTAL_U4} کا برابر ترازو۔ بایاں پلڑا: 2 تھیلے جن پر x لکھا ہے اور {ADD_U4} چھوٹے مربعے۔ دایاں پلڑا: {TOTAL_U4} چھوٹے مربعے۔ {BAL_UR}"),
    "u5_taxi": bar([(BASE5, str(BASE5)), (PER_KM * U5, f"{PER_KM}k")], FARE,
        f"A bar for the taxi fare: a box of {BASE5} rupees, then a box of {PER_KM}k rupees for the k km, with {FARE} over the whole bar: {BASE5} + {PER_KM}k = {FARE}.",
        f"ٹیکسی کے کرائے کی پٹی: {BASE5} روپے کا خانہ، پھر k کلومیٹر کے {PER_KM}k روپے کا خانہ، پوری پٹی کے اوپر {FARE}: یعنی {BASE5} + {PER_KM}k = {FARE}۔"),
    "s12_summary": bar([(S6, str(S6))] * BOOKS, COST,
        NOTEBOOKS_EN + f" Each box is {S6}: one notebook costs {S6} rupees, and {BOOKS} × {S6} = {COST}.",
        NOTEBOOKS_UR + f" ہر خانہ {S6} ہے: ایک کاپی {S6} روپے کی ہے، اور {BOOKS} × {S6} = {COST}۔"),
    "qb_apply": bar([(QB, "p")] * PACKETS + [(LOOSE, str(LOOSE))], BISCUITS,
        f"A bar of {PACKETS} equal boxes marked p (the biscuits in each packet) and a small box of {LOOSE} loose biscuits, with {BISCUITS} over the whole bar.",
        f"p والے {PACKETS} برابر خانوں (ہر پیکٹ کے بسکٹ) اور {LOOSE} کھلے بسکٹوں کے چھوٹے خانے کی پٹی، پوری پٹی کے اوپر {BISCUITS}۔"),
    "qb_find_error": bar([(N_QB, "n"), (N_QB, "n"), (5, "5")], 25,
        "A bar of two equal boxes marked n and a small box of 5, with 25 over the whole bar: 2n + 5 = 25.",
        "n والے دو برابر خانوں اور 5 کے چھوٹے خانے کی پٹی، پوری پٹی کے اوپر 25: یعنی 2n + 5 = 25۔"),
    "r_plus": bar([(R1, "?"), (PLUS_R1, str(PLUS_R1))], TOTAL_R1,
        f"A bar split into a box with a question mark (the number) and a box of {PLUS_R1}, with {TOTAL_R1} over the whole bar.",
        f"ایک پٹی جو سوالیہ نشان والے خانے (عدد) اور {PLUS_R1} کے خانے میں بٹی ہے، پوری پٹی کے اوپر {TOTAL_R1}۔"),
    "r_bags": bar([(R2, "?")] * BAGS_R2, MANGOES,
        f"A bar of {BAGS_R2} equal boxes, one for each bag, each with a question mark, and {MANGOES} mangoes over the whole bar.",
        f"{BAGS_R2} برابر خانوں کی پٹی، ہر تھیلے کا ایک خانہ، ہر ایک پر سوالیہ نشان، اور پوری پٹی کے اوپر {MANGOES} آم۔"),
})
write(lesson)

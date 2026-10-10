"""Chapter 7 test (Linear Expression and Equations), set out like the book's
review exercise and a board paper: multiple choice, short questions, then
longer problems. The questions are new; only the kinds of question follow
the book."""
from decimal import Decimal as D
from common import (T, say, nq, eq_q, ch, write, m, solves, solve, book_ref, REVIEW, CHAPTER_7_TEST,
                    EQ_RECOGNISE, EQ_CHECK, EQ_FORMING, EQ_TWO_STEP, EQ_BRACKETS, EQ_WORD_PROBLEMS,
                    ALG_SUBSTITUTION, ALG_EQUATIONS)

SKILL = CHAPTER_7_TEST


def mcq(id, en, ur, right, wrongs, pos):
    return ch(id, ("MCQ: " + en, "کثیر انتخابی: " + ur), right, wrongs, pos, qtype="exam_style")


def short(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Short question: " + en, "مختصر سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_q(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def short_eq(id, en, ur, forms, values, hint, good, bad, wrongs=()):
    return eq_q(id, ("Short question: " + en, "مختصر سوال: " + ur), forms, values, hint, good, bad, wrongs, qtype="exam_style")


def linear_one_variable(eq):
    letters = {c for c in eq if c.isalpha()}
    return "=" in eq and len(letters) == 1 and "²" not in eq


# MCQs
assert "=" in "4a + 1 = 13" and "=" not in "4a + 1" and solve("4a + 1 = 13", "a") == 3
assert solve("y + 7 = 19", "y") == 12 and not solves("7y = 19", y=12) and not solves("y − 7 = 19", y=12)
M3 = "2m − 5 = 9"
assert linear_one_variable(M3) and not any(linear_one_variable(w) for w in ["m² − 5 = 9", "2m − n = 9", "2m − 5"])
M4 = solve("2x + 3 = 15")
assert M4 == 6 and (15 + 3) // 2 == 9 and 15 - 3 == 12
M5 = solve("x − 7 = 12")
assert M5 == 19 and 12 - 7 == 5 and 12 * 7 == 84
M6 = solve("x ÷ 5 = 4")
assert M6 == 20 and 4 + 5 == 9 and 5 - 4 == 1
# short questions
S1 = solve("5x − 8 = 27")
assert S1 == 7 and 27 + 8 == 35 and 27 - 8 == 19 and not solves("5x − 8 = 27", x=19 // 5)
assert solve("2p + 9 = 31", "p") == 11 and not solves("2(p + 9) = 31", p=11) and not solves("2p − 9 = 31", p=11)
S3 = D("9.2") / 4
assert S3 == D("2.3") and 4 * S3 == D("9.2") and D("9.2") * 4 == D("36.8") and D("9.2") - 4 == D("5.2")
S4 = solve("3(x − 2) = 21")
assert S4 == 9 and 21 // 3 == 7 and 7 - 2 == 5
# long questions
L1X = solve("x + (x − 3) = 41")
L1 = L1X - 3
assert L1X == 22 and L1 == 19 and L1 + L1X == 41 and 41 + 3 == 44
L2X = solve("x + (x + 1) + (x + 2) + (x + 3) = 102")
L2 = L2X + 3
assert L2X == 24 and L2 == 27 and sum(range(L2X, L2X + 4)) == 102 and L2X + 2 == 26
L3P = solve("12x = 960")
L3 = 5 * L3P
assert L3P == 80 and L3 == 400 and 3 * L3P + 4 * L3P + 5 * L3P == 960 and 4 * L3P == 320
L4 = solve("3x − 18 = 63")
assert L4 == 27 and 3 * L4 - 18 == 63 and 63 + 18 == 81 and (63 - 18) // 3 == 15
# question bank and review
QB1 = solve("x + 15 = 40")
assert QB1 == 25 and 40 + 15 == 55
QB2 = solve("4x + 2 = 26")
assert QB2 == 6 and 26 - 2 == 24
QB3 = solve("x ÷ 3 = 7")
assert QB3 == 21 and 7 - 3 == 4
R1 = solve("3x − 4 = 14")
assert R1 == 6 and 14 - 4 == 10
R2 = solve("6x = 72")
assert R2 == 12 and 72 - 6 == 66

lesson = {
 "id": "g6-maths-16-chapter-7-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 7: equations and expressions, linear equations in one variable, forming equations from words, solving and checking them, and word problems.",
                      "textbook": book_ref("Review Exercise 7")}],
 "skills": [SKILL],
 "title": T("Chapter 7 test: Linear equations", "باب 7 کا ٹیسٹ: خطی مساوات"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in (EQ_RECOGNISE, EQ_CHECK, EQ_FORMING, EQ_TWO_STEP, EQ_BRACKETS, EQ_WORD_PROBLEMS, ALG_SUBSTITUTION, ALG_EQUATIONS)],
 "misconceptions": [
   {"id": "letter_means_equation", "description": "Thinks anything with a letter is an equation, even with no = sign."},
   {"id": "power_is_linear", "description": "Counts x² = 9 or an equation with two letters as a linear equation in one variable."},
   {"id": "wrong_operation", "description": "Writes 'more than' or 'increased by' as the wrong operation, or times as plus."},
   {"id": "wrong_inverse", "description": "Undoes an operation by repeating it or doing the wrong one."},
   {"id": "stops_early", "description": "Stops after the first step and gives that as the answer."},
   {"id": "order_of_steps", "description": "Divides or multiplies before dealing with the number added or subtracted."},
   {"id": "brackets_wrong", "description": "Puts brackets where the words don't need them, or forgets to multiply the whole bracket."},
   {"id": "answer_is_other_quantity", "description": "Finds the unknown but gives another quantity from the story."},
   {"id": "decimal_slip", "description": "Multiplies instead of dividing, or subtracts instead of dividing, with decimals."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_one", "type": "exam_style", "step": nq(
     "qb_exam_one", ("Solve x + 15 = 40.", "حل کریں x + 15 = 40"), QB1,
     ("Take 15 away from 40.", "40 میں سے 15 تفریق کریں۔"),
     ("Correct: x = 25.", "درست: x = 25"), ("40 − 15 = 25.", "40 − 15 = 25"),
     [(55, "That adds 15. Undo + 15 by taking 15 away: 25.", "یہ 15 جمع کرتا ہے۔ + 15 کو 15 تفریق کر کے ختم کریں: 25", "wrong_inverse")], qtype=None)},
   {"id": "qb_exam_two", "type": "exam_style", "step": nq(
     "qb_exam_two", ("Solve 4x + 2 = 26.", "حل کریں 4x + 2 = 26"), QB2,
     ("Take 2 away first, then divide by 4.", "پہلے 2 تفریق کریں، پھر 4 سے تقسیم کریں۔"),
     ("Correct: 4x = 24, so x = 6.", "درست: 4x = 24، تو x = 6"), ("26 − 2 = 24, then 24 ÷ 4 = 6.", "26 − 2 = 24، پھر 24 ÷ 4 = 6"),
     [(24, "4x = 24 is only the first step. Divide by 4: 6.", "4x = 24 صرف پہلا قدم ہے۔ 4 سے تقسیم کریں: 6", "stops_early")], qtype=None)},
   {"id": "qb_exam_div", "type": "exam_style", "step": nq(
     "qb_exam_div", ("Solve x ÷ 3 = 7.", "حل کریں x ÷ 3 = 7"), QB3,
     ("Undo ÷ 3 with × 3.", "÷ 3 کو × 3 سے ختم کریں۔"),
     ("Correct: x = 7 × 3 = 21.", "درست: x = 7 × 3 = 21"), ("7 × 3 = 21, and 21 ÷ 3 = 7.", "7 × 3 = 21، اور 21 ÷ 3 = 7"),
     [(4, "That takes 3 away. Undo ÷ 3 with × 3: 21.", "یہ 3 تفریق کرتا ہے۔ ÷ 3 کو × 3 سے ختم کریں: 21", "wrong_inverse")], qtype=None)},
 ]},
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 7 in your maths book in your notebook, setting out the working the way this test's answers do: write the equation, solve it step by step, and check. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 7 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں: مساوات لکھیں، قدم بہ قدم حل کریں، اور جانچیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Model answer", "نمونہ جواب"), T("Review exercise", "اعادی مشق")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 7 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook, then the answer). The questions are new, not the book's. Check every solution by putting it back into the equation.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 7 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوال (اپنی کاپی میں پورا کام، پھر جواب)۔ سوال نئے ہیں، کتاب والے نہیں۔ ہر حل کو مساوات میں واپس رکھ کر جانچیں۔")},
   mcq("m1_which", "Which of these is an equation?", "ان میں سے کون سی مساوات ہے؟",
       ("4a + 1 = 13", "4a + 1 = 13", "Correct: it has an = sign.", "درست: اس میں = کا نشان ہے۔"),
       [("4a + 1", "4a + 1", "No = sign: an expression.", "= کا نشان نہیں: الجبری جملہ۔", "letter_means_equation"),
        ("4a", "4a", "A letter with a number is an expression.", "حرف اور عدد الجبری جملہ ہے۔", "letter_means_equation"),
        ("a + 1 + 13", "a + 1 + 13", "Still no = sign: an expression.", "پھر بھی = کا نشان نہیں: الجبری جملہ۔", "letter_means_equation")], 0),
   mcq("m2_words", "Which equation says '7 more than a number y is 19'?", "کون سی مساوات کہتی ہے 'عدد y سے 7 زیادہ 19 ہے'؟",
       ("y + 7 = 19", "y + 7 = 19", "Correct: more than means add.", "درست: زیادہ یعنی جمع۔"),
       [("7y = 19", "7y = 19", "7y means 7 times y.", "7y یعنی y کا 7 گنا۔", "wrong_operation"),
        ("y − 7 = 19", "y − 7 = 19", "That is 7 LESS than y.", "یہ y سے 7 کم ہے۔", "wrong_operation"),
        ("7 − y = 19", "7 − y = 19", "That takes y away from 7.", "یہ 7 میں سے y تفریق کرتا ہے۔", "wrong_operation")], 2),
   mcq("m3_linear", "Which is a linear equation in one variable?", "ان میں سے کون سی ایک متغیر والی خطی مساوات ہے؟",
       (M3, M3, "Correct: one letter, power 1.", "درست: ایک حرف، طاقت 1۔"),
       [("m² − 5 = 9", "m² − 5 = 9", "m² has power 2.", "m² کی طاقت 2 ہے۔", "power_is_linear"),
        ("2m − n = 9", "2m − n = 9", "Two letters, m and n.", "دو حرف m اور n۔", "power_is_linear"),
        ("2m − 5", "2m − 5", "No = sign.", "= کا نشان نہیں۔", "letter_means_equation")], 1),
   mcq("m4_solution", "The solution of 2x + 3 = 15 is:", "2x + 3 = 15 کا حل ہے:",
       (str(M4), str(M4), "Correct: 2 × 6 + 3 = 15.", "درست: 2 × 6 + 3 = 15"),
       [("9", "9", "That adds 3: (15 + 3) ÷ 2. Take 3 away: 6.", "یہ 3 جمع کرتا ہے: (15 + 3) ÷ 2۔ 3 تفریق کریں: 6", "wrong_inverse"),
        ("12", "12", "2x = 12 is only the first step. Divide by 2: 6.", "2x = 12 صرف پہلا قدم ہے۔ 2 سے تقسیم کریں: 6", "stops_early"),
        ("18", "18", "Check: 2 × 18 + 3 = 39, not 15.", "جانچ: 2 × 18 + 3 = 39، 15 نہیں۔", "wrong_inverse")], 3),
   mcq("m5_one_step", "If x − 7 = 12, then x is:", "اگر x − 7 = 12 ہو تو x ہے:",
       (str(M5), str(M5), "Correct: 19 − 7 = 12.", "درست: 19 − 7 = 12"),
       [("5", "5", "That takes 7 from 12. Undo − 7 by adding 7: 19.", "یہ 12 میں سے 7 تفریق کرتا ہے۔ − 7 کو 7 جمع کر کے ختم کریں: 19", "wrong_inverse"),
        ("84", "84", "Do not multiply. Add 7: 19.", "ضرب نہ دیں۔ 7 جمع کریں: 19", "wrong_inverse"),
        ("−5", "−5", "Check: −5 − 7 = −12, not 12.", "جانچ: −5 − 7 = −12، 12 نہیں۔", "wrong_inverse")], 1),
   mcq("m6_divide", "If x ÷ 5 = 4, then x is:", "اگر x ÷ 5 = 4 ہو تو x ہے:",
       (str(M6), str(M6), "Correct: 20 ÷ 5 = 4.", "درست: 20 ÷ 5 = 4"),
       [("9", "9", "That adds 5. Undo ÷ 5 with × 5: 20.", "یہ 5 جمع کرتا ہے۔ ÷ 5 کو × 5 سے ختم کریں: 20", "wrong_inverse"),
        ("1", "1", "That takes 4 from 5. Multiply: 4 × 5 = 20.", "یہ 5 میں سے 4 تفریق کرتا ہے۔ ضرب دیں: 4 × 5 = 20", "wrong_inverse"),
        ("0.8", "0.8", "That divides 4 by 5. Undo ÷ 5 with × 5: 20.", "یہ 4 کو 5 سے تقسیم کرتا ہے۔ ÷ 5 کو × 5 سے ختم کریں: 20", "wrong_inverse")], 0),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   short("q1_two_step", "Solve 5x − 8 = 27.", "حل کریں 5x − 8 = 27", S1,
      ("Add 8 to both sides first, then divide by 5.", "پہلے دونوں طرف 8 جمع کریں، پھر 5 سے تقسیم کریں۔"),
      ("Correct: 5x = 35, so x = 7.", "درست: 5x = 35، تو x = 7"),
      ("Model answer: 5x − 8 = 27, so 5x = 27 + 8 = 35 and x = 35 ÷ 5 = 7. Check: 5 × 7 − 8 = 27.", "نمونہ جواب: 5x − 8 = 27، تو 5x = 27 + 8 = 35 اور x = 35 ÷ 5 = 7۔ جانچ: 5 × 7 − 8 = 27"),
      [(35, "5x = 35 is only the first step. Divide by 5: 7.", "5x = 35 صرف پہلا قدم ہے۔ 5 سے تقسیم کریں: 7", "stops_early"),
       (4, "That takes 8 away, but − 8 is undone by adding 8: x = 7.", "یہ 8 تفریق کرتا ہے، مگر − 8 کو 8 جمع کر کے ختم کرتے ہیں: x = 7", "wrong_inverse")]),
   short_eq("q2_build", "Write an equation: twice a number p, increased by 9, is 31.", "مساوات لکھیں: عدد p کا دگنا، 9 زیادہ، 31 ہے۔",
      ["2p + 9 = 31", "2 × p + 9 = 31", "31 = 2p + 9"], {"p": 11},
      ("Twice p is 2p. Then add 9.", "p کا دگنا 2p ہے۔ پھر 9 جمع کریں۔"),
      ("Correct: 2p + 9 = 31.", "درست: 2p + 9 = 31"),
      ("Model answer: twice p is 2p, increased by 9 is 2p + 9, and 'is 31' gives 2p + 9 = 31.", "نمونہ جواب: p کا دگنا 2p، 9 زیادہ 2p + 9، اور '31 ہے' سے 2p + 9 = 31"),
      [("2(p + 9) = 31", "Only 2p is increased by 9. Brackets would double the 9 too: 2p + 9 = 31.", "9 صرف 2p میں جمع ہوتا ہے۔ قوسین 9 کو بھی دگنا کرتی: 2p + 9 = 31", "brackets_wrong"),
       ("2p − 9 = 31", "'Increased' means add: 2p + 9 = 31.", "'زیادہ' یعنی جمع: 2p + 9 = 31", "wrong_operation")]),
   short("q3_decimal", "Solve 4x = 9.2.", "حل کریں 4x = 9.2", S3,
      ("Divide 9.2 by 4.", "9.2 کو 4 سے تقسیم کریں۔"),
      ("Correct: x = 9.2 ÷ 4 = 2.3.", "درست: x = 9.2 ÷ 4 = 2.3"),
      ("Model answer: x = 9.2 ÷ 4 = 2.3. Check: 4 × 2.3 = 9.2.", "نمونہ جواب: x = 9.2 ÷ 4 = 2.3۔ جانچ: 4 × 2.3 = 9.2"),
      [(D("36.8"), "That multiplies. Undo × 4 by dividing by 4: 2.3.", "یہ ضرب دیتا ہے۔ × 4 کو 4 سے تقسیم کر کے ختم کریں: 2.3", "decimal_slip"),
       (D("5.2"), "That takes 4 away. Undo × 4 by dividing: 2.3.", "یہ 4 تفریق کرتا ہے۔ × 4 کو تقسیم سے ختم کریں: 2.3", "decimal_slip")]),
   short("q4_brackets", "Solve 3(x − 2) = 21.", "حل کریں 3(x − 2) = 21", S4,
      ("Divide both sides by 3 first: x − 2 = 7.", "پہلے دونوں طرف 3 سے تقسیم کریں: x − 2 = 7"),
      ("Correct: x − 2 = 7, so x = 9. Check: 3 × (9 − 2) = 21.", "درست: x − 2 = 7، تو x = 9۔ جانچ: 3 × (9 − 2) = 21"),
      ("Model answer: 3(x − 2) = 21, so x − 2 = 7 and x = 9.", "نمونہ جواب: 3(x − 2) = 21، تو x − 2 = 7 اور x = 9"),
      [(7, "x − 2 = 7 is only the first step. Add 2: 9.", "x − 2 = 7 صرف پہلا قدم ہے۔ 2 جمع کریں: 9", "stops_early"),
       (5, "That takes 2 from 7, but − 2 is undone by adding 2: 9.", "یہ 7 میں سے 2 تفریق کرتا ہے، مگر − 2 کو 2 جمع کر کے ختم کرتے ہیں: 9", "wrong_inverse")]),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write the equation and full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں مساوات اور پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   long_q("l1_ages", "Rida is 3 years younger than Zain. The sum of their ages is 41. If Zain is x years old, then x + (x − 3) = 41. How old is Rida?", "ریدا زین سے 3 سال چھوٹی ہے۔ دونوں کی عمروں کا مجموعہ 41 ہے۔ اگر زین x سال کا ہے تو x + (x − 3) = 41۔ ریدا کتنے سال کی ہے؟", L1,
      ("2x − 3 = 41. Solve for x (Zain), then find Rida.", "2x − 3 = 41۔ x (زین) معلوم کریں، پھر ریدا کی عمر نکالیں۔"),
      ("Correct: Zain is 22, so Rida is 22 − 3 = 19.", "درست: زین 22 کا ہے، تو ریدا 22 − 3 = 19 کی ہے۔"),
      ("Model answer: 2x − 3 = 41, 2x = 44, x = 22. Rida is 22 − 3 = 19. Check: 22 + 19 = 41.", "نمونہ جواب: 2x − 3 = 41، 2x = 44، x = 22۔ ریدا 22 − 3 = 19 کی ہے۔ جانچ: 22 + 19 = 41"),
      [(22, "22 is Zain's age. The question asks for Rida: 19.", "22 زین کی عمر ہے۔ سوال ریدا کی عمر پوچھتا ہے: 19", "answer_is_other_quantity"),
       (44, "That is 41 + 3. To undo − 3, add 3 to get 2x = 44, then divide by 2 and take 3 for Rida: 19.", "یہ 41 + 3 ہے۔ − 3 کو ختم کرنے کے لیے 3 جمع کر کے 2x = 44 ملتا ہے، پھر 2 سے تقسیم کریں اور ریدا کے لیے 3 تفریق کریں: 19", "stops_early")]),
   long_q("l2_consecutive", "The sum of four consecutive numbers is 102. If the smallest is x, the numbers are x, x + 1, x + 2 and x + 3. What is the largest number?", "چار لگاتار اعداد کا مجموعہ 102 ہے۔ اگر سب سے چھوٹا x ہو تو اعداد x، x + 1، x + 2 اور x + 3 ہیں۔ سب سے بڑا عدد کیا ہے؟", L2,
      ("Add them: 4x + 6 = 102. Solve for x, then find the largest.", "جمع کریں: 4x + 6 = 102۔ x معلوم کریں، پھر سب سے بڑا عدد نکالیں۔"),
      ("Correct: x = 24, so the numbers are 24, 25, 26, 27 and the largest is 27.", "درست: x = 24، تو اعداد 24، 25، 26، 27 ہیں اور سب سے بڑا 27 ہے۔"),
      ("Model answer: 4x + 6 = 102, 4x = 96, x = 24. The largest is x + 3 = 27. Check: 24 + 25 + 26 + 27 = 102.", "نمونہ جواب: 4x + 6 = 102، 4x = 96، x = 24۔ سب سے بڑا x + 3 = 27 ہے۔ جانچ: 24 + 25 + 26 + 27 = 102"),
      [(24, "24 is the smallest number (x). The largest is x + 3 = 27.", "24 سب سے چھوٹا عدد (x) ہے۔ سب سے بڑا x + 3 = 27 ہے۔", "answer_is_other_quantity"),
       (26, "26 is the third number, x + 2. The largest is x + 3 = 27.", "26 تیسرا عدد x + 2 ہے۔ سب سے بڑا x + 3 = 27 ہے۔", "answer_is_other_quantity")]),
   long_q("l3_ratio", "Rs 960 is shared among Amna, Bushra and Chand in the ratio 3 : 4 : 5. There are 3 + 4 + 5 = 12 equal parts, so 12x = 960. How many rupees does Chand, with the largest share (5 parts), get?", "960 روپے آمنہ، بشریٰ اور چاند میں نسبت 3 : 4 : 5 سے تقسیم ہوتے ہیں۔ 3 + 4 + 5 = 12 برابر حصے ہیں، تو 12x = 960۔ چاند کو، جس کا حصہ سب سے بڑا (5 حصے) ہے، کتنے روپے ملتے ہیں؟", L3,
      ("Find one part, 960 ÷ 12, then multiply by 5.", "ایک حصہ معلوم کریں، 960 ÷ 12، پھر 5 سے ضرب دیں۔"),
      ("Correct: one part is Rs 80, so Chand gets 5 × 80 = Rs 400.", "درست: ایک حصہ 80 روپے ہے، تو چاند کو 5 × 80 = 400 روپے ملتے ہیں۔"),
      ("Model answer: 12x = 960, x = 80. Chand gets 5 × 80 = Rs 400. Check: 240 + 320 + 400 = 960.", "نمونہ جواب: 12x = 960، x = 80۔ چاند کو 5 × 80 = 400 روپے ملتے ہیں۔ جانچ: 240 + 320 + 400 = 960"),
      [(80, "Rs 80 is one part. Chand has 5 parts: 400.", "80 روپے ایک حصہ ہے۔ چاند کے 5 حصے ہیں: 400", "answer_is_other_quantity"),
       (320, "Rs 320 is Bushra's share (4 parts). Chand has 5 parts: 400.", "320 روپے بشریٰ کا حصہ ہے (4 حصے)۔ چاند کے 5 حصے ہیں: 400", "answer_is_other_quantity")]),
   long_q("l4_cricket", "Babar scored 18 runs less than three times the runs of Fawad. Babar scored 63. If Fawad scored x runs, then 3x − 18 = 63. How many runs did Fawad score?", "بابر نے فواد کے رنز کے تین گنا سے 18 رنز کم بنائے۔ بابر نے 63 رنز بنائے۔ اگر فواد نے x رنز بنائے تو 3x − 18 = 63۔ فواد نے کتنے رنز بنائے؟", L4,
      ("Add 18 to both sides first, then divide by 3.", "پہلے دونوں طرف 18 جمع کریں، پھر 3 سے تقسیم کریں۔"),
      ("Correct: 3x = 81, so x = 27. Check: 3 × 27 − 18 = 63.", "درست: 3x = 81، تو x = 27۔ جانچ: 3 × 27 − 18 = 63"),
      ("Model answer: 3x − 18 = 63, 3x = 63 + 18 = 81, x = 27.", "نمونہ جواب: 3x − 18 = 63، 3x = 63 + 18 = 81، x = 27"),
      [(81, "3x = 81 is only the first step. Divide by 3: 27.", "3x = 81 صرف پہلا قدم ہے۔ 3 سے تقسیم کریں: 27", "stops_early"),
       (15, "That takes 18 away. To undo − 18, add 18: 81, then 27.", "یہ 18 تفریق کرتا ہے۔ − 18 کو ختم کرنے کے لیے 18 جمع کریں: 81، پھر 27", "wrong_inverse")]),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 7 test. Well done!", "آپ نے باب 7 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: an equation has an = sign and an expression does not. A linear equation in one variable has one letter with power 1. Write words as an equation, call the unknown x, and undo the operations in reverse order: add or take away first, then divide or multiply. Check by putting the answer back, and answer what the question asks.",
              "امتحان میں: مساوات میں = کا نشان ہوتا ہے اور الجبری جملے میں نہیں۔ ایک متغیر والی خطی مساوات میں ایک حرف ہوتا ہے جس کی طاقت 1 ہو۔ الفاظ کو مساوات میں لکھیں، نامعلوم کو x کہیں، اور عملوں کو الٹی ترتیب سے ختم کریں: پہلے جمع یا تفریق، پھر تقسیم یا ضرب۔ جواب کو واپس رکھ کر جانچیں، اور وہی بتائیں جو سوال پوچھتا ہے۔"),
    "points": [T("Check an answer by putting it in the equation.", "جواب کو مساوات میں رکھ کر جانچیں۔"),
               T("Write the equation, the working, then the final answer.", "مساوات لکھیں، کام لکھیں، پھر آخری جواب۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_two", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_two", ("Solve 3x − 4 = 14.", "حل کریں 3x − 4 = 14"), R1,
     ("Add 4 to both sides, then divide by 3.", "دونوں طرف 4 جمع کریں، پھر 3 سے تقسیم کریں۔"),
     ("Correct: 3x = 18, so x = 6.", "درست: 3x = 18، تو x = 6"), ("14 + 4 = 18, then 18 ÷ 3 = 6.", "14 + 4 = 18، پھر 18 ÷ 3 = 6"),
     [(10, "That takes 4 away, but − 4 is undone by adding 4: 6.", "یہ 4 تفریق کرتا ہے، مگر − 4 کو 4 جمع کر کے ختم کرتے ہیں: 6", "wrong_inverse")], qtype=None)},
   {"id": "r_exam_one", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_one", ("Solve 6x = 72.", "حل کریں 6x = 72"), R2,
     ("Divide both sides by 6.", "دونوں طرف 6 سے تقسیم کریں۔"),
     ("Correct: x = 12.", "درست: x = 12"), ("72 ÷ 6 = 12.", "72 ÷ 6 = 12"),
     [(66, "That takes 6 away. Undo × 6 by dividing by 6: 12.", "یہ 6 تفریق کرتا ہے۔ × 6 کو 6 سے تقسیم کر کے ختم کریں: 12", "wrong_inverse")], qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 7 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.equations.chapter_7_test), with the chapter's equations skills as prerequisites, and is mastered with exam_style questions, like the chapter 5 and 6 tests.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), مساوات (equation), خطی مساوات (linear equation), حل (solution), نسبت (ratio). لگاتار اعداد (consecutive numbers) is new and should be confirmed by a teacher.",
   "The numbers were worked out in content/sources/g6-maths-16/chapter_7_test.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

write(lesson)

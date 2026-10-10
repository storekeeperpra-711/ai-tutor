"""Chapter 2 test (Integers), set out like the book's review exercise and a
board paper: multiple choice, short questions, then longer mixed problems.
The questions are new; only the kinds of question follow the book."""
from common import (T, opt, say, wrong, signed, number_question, choice_question, write, book_ref,
                    REVIEW, CHAPTER_TEST, INT_MEANING, INT_ABSOLUTE)

SKILL = CHAPTER_TEST


def mcq(id, en, ur, right, wrongs, pos):
    """A multiple choice question. right and each of wrongs are
    (en, ur, feedback_en, feedback_ur[, misconception]); the right one goes
    at index pos."""
    options = [opt("x", right[0], right[1], True, right[2], right[3])]
    for r in wrongs:
        options.append(opt("x", r[0], r[1], False, r[2], r[3], r[4] if len(r) > 4 else None))
    options.insert(pos, options.pop(0))
    for k, o in enumerate(options):
        o["id"] = "abcd"[k]
    return choice_question(id, T("MCQ: " + en, "کثیر انتخابی: " + ur), options, qtype="exam_style")


def short(id, en, ur, *args, **kw):
    return number_question(id, T("Short question: " + en, "مختصر سوال: " + ur), *args, qtype="exam_style", **kw)


def long_q(id, en, ur, *args, **kw):
    return number_question(id, T("Long question: " + en, "تفصیلی سوال: " + ur), *args, qtype="exam_style", **kw)


# MCQs
M1 = (-6, 0, 6, -0.5)
assert [n for n in M1 if n < 0 and n == int(n)] == [-6]
assert [n for n in M1 if n == 0] == [0]
M3 = -(-17)
assert M3 == 17 and -17 + M3 == 0
M4 = abs(-23)
assert M4 == 23 and 32 != M4
M5_SET = (-2, -15, 0, 9)
assert min(M5_SET) == -15 and min(M5_SET, key=abs) == 0
M6_SET = [3, -8, -1, 5]
M6 = sorted(M6_SET)
M6_DESC = sorted(M6_SET, reverse=True)
M6_ABS = sorted(M6_SET, key=abs)
assert M6 == [-8, -1, 3, 5] and M6_DESC == [5, 3, -1, -8] and M6_ABS == [-1, 3, 5, -8]
M7_SET = (6, -11, 9, -10)
assert max(M7_SET, key=abs) == -11 and max(M7_SET) == 9 and abs(-11) == 11
assert (-9 < -2) and not (-3 > 0) and not (abs(-5) < abs(4)) and not (-1 > 1)
# short questions
S1 = abs(-15) - abs(9)
assert S1 == 6 and -15 - 9 == -24 and 15 + 9 == 24
S2 = -800
assert S2 < 0
S3 = 6 - (-9)
assert S3 == 15 and 9 + 6 == 15 and 9 - 6 == 3
S4_ALL = [x for x in range(-10, 11) if -4 < x < 2]
S4 = len(S4_ALL)
assert S4_ALL == [-3, -2, -1, 0, 1] and S4 == 5 and len([x for x in range(-10, 11) if -4 <= x <= 2]) == 7
S5 = 2 - 7
assert S5 == -5 and 2 + 7 == 9 and 7 - 2 == 5
# long questions
L1_A = 5
L1_B = -L1_A
L1 = L1_A - L1_B
assert L1_B == -5 and L1 == 10 and -6 <= L1_B <= L1_A <= 8
L2_T = {"Murree": -6, "Quetta": -11, "Lahore": 4, "Karachi": 18, "Skardu": -14}
L2_ASC = sorted(L2_T.values())
L2 = L2_ASC[1]
assert L2_ASC == [-14, -11, -6, 4, 18] and L2 == -11
assert sorted(L2_T.values(), reverse=True)[1] == 4 and sorted(L2_T.values(), key=abs)[1] == -6
L3_VALUES = list(range(-4, 5))
L3 = sum(abs(n) for n in L3_VALUES)
assert L3 == 20 and sum(L3_VALUES) == 0 and 4 + 3 + 2 + 1 == 10
L4_ALL = [n for n in range(-30, 31) if abs(n) == 12 and n < -5]
assert L4_ALL == [-12]
L4 = L4_ALL[0]
assert [n for n in range(-30, 31) if abs(n) == 12] == [-12, 12]
# question bank
QB1 = abs(-19) + abs(-4)
assert QB1 == 23 and -19 + -4 == -23
QB2 = -(-8)
assert QB2 == 8
QB3_SET = (-7, 2, -13, 10)
QB3 = min(QB3_SET)
assert QB3 == -13 and max(QB3_SET, key=abs) == -13
# review
R1 = 12 - (-3)
assert R1 == 15 and 12 - 3 == 9
R2_SET = [-5, 7, -1, 0]
R2 = sorted(R2_SET, reverse=True)[1]
assert sorted(R2_SET, reverse=True) == [7, 0, -1, -5] and R2 == 0 and sorted(R2_SET)[1] == -1


lesson = {
 "id": "g6-maths-04-chapter-2-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 2: integers, opposites, the number line, ordering integers, and absolute value.",
                      "textbook": book_ref("Review Exercise 2")}],
 "skills": [SKILL],
 "title": T("Chapter 2 test: Integers", "باب 2 کا ٹیسٹ: صحیح اعداد"),
 "estimated_minutes": 22,
 "prerequisites": [{"skill": s} for s in (INT_MEANING, INT_ABSOLUTE)],
 "misconceptions": [
   {"id": "sign_ignored", "description": "Ignores the minus sign, writing a loss or a point left of 0 as a positive number."},
   {"id": "opposite_same", "description": "Thinks the opposite of a number is the number itself."},
   {"id": "zero_sign", "description": "Thinks 0 is positive or negative."},
   {"id": "bigger_digits", "description": "Thinks a negative number with bigger digits is greater: −9 > −2."},
   {"id": "sign_kept", "description": "Gives the absolute value with its minus sign: |−10| = −10."},
   {"id": "abs_order_mixed", "description": "Orders by value when absolute values are asked for, or the other way round."},
   {"id": "gap_miscount", "description": "Subtracts the numbers without their signs, or leaves out 0 when counting integers."},
   {"id": "one_value", "description": "Thinks only one integer has a given absolute value."},
   {"id": "stops_early", "description": "Finds a middle result but does not answer the question asked."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_abs", "type": "exam_style", "step": number_question(
     "qb_exam_abs",
     T("Find |−19| + |−4|.", "|−19| + |−4| معلوم کریں۔"),
     QB1,
     T("Take the absolute values first: 19 and 4.", "پہلے مطلق قیمتیں لیں: 19 اور 4"),
     T("Correct: 19 + 4 = 23.", "درست: 19 + 4 = 23"),
     T("|−19| = 19 and |−4| = 4, so 19 + 4 = 23.", "|−19| = 19 اور |−4| = 4، اس لیے 19 + 4 = 23"),
     common_wrong=[wrong(-23, "Absolute values are not negative: 19 + 4 = 23.", "مطلق قیمتیں منفی نہیں ہوتیں: 19 + 4 = 23", "sign_kept")],
     qtype=None)},
   {"id": "qb_exam_opposite", "type": "exam_style", "step": number_question(
     "qb_exam_opposite",
     T("Write the opposite of −8.", "−8 کا مخالف عدد لکھیں۔"),
     QB2,
     T("Same distance from 0, on the other side.", "0 سے اتنا ہی فاصلہ، دوسری طرف۔"),
     T("Correct: 8.", "درست: 8"),
     T("The opposite of −8 is 8.", "−8 کا مخالف عدد 8 ہے۔"),
     common_wrong=[wrong(-8, "That is the same number. The opposite is 8.", "یہ وہی عدد ہے۔ مخالف 8 ہے۔", "opposite_same")],
     qtype=None)},
   {"id": "qb_exam_smallest", "type": "exam_style", "step": number_question(
     "qb_exam_smallest",
     T("Which is the smallest of −7, 2, −13 and 10?", "−7، 2، −13 اور 10 میں سے سب سے چھوٹا کون سا ہے؟"),
     QB3,
     T("The smallest is furthest to the left on the number line.", "سب سے چھوٹا عددی خط پر سب سے بائیں ہوتا ہے۔"),
     T("Correct: −13.", "درست: −13"),
     T("−13 is furthest left, so it is the smallest.", "−13 سب سے بائیں ہے، اس لیے سب سے چھوٹا ہے۔"),
     common_wrong=[wrong(-7, "−7 is right of −13, so it is bigger. The smallest is −13.", "−7، −13 کے دائیں ہے، اس لیے بڑا ہے۔ سب سے چھوٹا −13 ہے۔", "bigger_digits")],
     qtype=None)},
 ]},
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 2 in your maths book in your notebook, setting out the working the way this test's answers do. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 2 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Absolute value", "مطلق قیمت"), T("Opposite", "مخالف عدد")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 2 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook). The questions are new, not the book's.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 2 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوال (پورا کام اپنی کاپی میں)۔ سوال نئے ہیں، کتاب والے نہیں۔")},
   mcq("m1_negative", "Which of these is a negative integer?", "ان میں سے کون سا منفی صحیح عدد ہے؟",
       ("−6", "−6", "Correct: −6 is an integer less than 0.", "درست: −6، 0 سے چھوٹا صحیح عدد ہے۔"),
       [("0", "0", "0 is neither positive nor negative.", "0 نہ مثبت ہے نہ منفی۔", "zero_sign"),
        ("6", "6", "6 is a positive integer.", "6 مثبت صحیح عدد ہے۔", "sign_ignored"),
        ("−½", "−½", "−½ is negative but it is not an integer.", "−½ منفی ہے مگر صحیح عدد نہیں۔")], 1),
   mcq("m2_neutral", "Which integer is neither positive nor negative?", "کون سا صحیح عدد نہ مثبت ہے نہ منفی؟",
       ("0", "0", "Correct: 0 is the neutral integer.", "درست: 0 غیر جانبدار صحیح عدد ہے۔"),
       [("1", "1", "1 is the smallest positive integer.", "1 سب سے چھوٹا مثبت صحیح عدد ہے۔"),
        ("−1", "−1", "−1 is the greatest negative integer.", "−1 سب سے بڑا منفی صحیح عدد ہے۔"),
        ("There is none.", "کوئی نہیں۔", "0 is neither positive nor negative.", "0 نہ مثبت ہے نہ منفی۔", "zero_sign")], 0),
   mcq("m3_opposite", "The opposite of −17 is:", "−17 کا مخالف عدد ہے:",
       (str(M3), str(M3), "Correct: −17 + 17 = 0.", "درست: −17 + 17 = 0"),
       [("−17", "−17", "That is the same number. The opposite is on the other side of 0.", "یہ وہی عدد ہے۔ مخالف عدد 0 کی دوسری طرف ہوتا ہے۔", "opposite_same"),
        ("0", "0", "0 is the middle point, not the opposite.", "0 درمیانی نقطہ ہے، مخالف نہیں۔"),
        ("71", "71", "71 only has the digits swapped. The opposite of −17 is 17.", "71 میں صرف ہندسے الٹے ہیں۔ −17 کا مخالف 17 ہے۔")], 3),
   mcq("m4_abs", "|−23| is equal to:", "|−23| برابر ہے:",
       (str(M4), str(M4), "Correct: −23 is 23 steps from 0.", "درست: −23، 0 سے 23 قدم دور ہے۔"),
       [("−23", "−23", "A distance is never negative.", "فاصلہ کبھی منفی نہیں ہوتا۔", "sign_kept"),
        ("0", "0", "Only |0| is 0.", "صرف |0| صفر ہے۔"),
        ("32", "32", "32 only has the digits swapped. |−23| = 23.", "32 میں صرف ہندسے الٹے ہیں۔ |−23| = 23", None)], 2),
   mcq("m5_smallest", "The smallest of −2, −15, 0 and 9 is:", "−2، −15، 0 اور 9 میں سب سے چھوٹا ہے:",
       ("−15", "−15", "Correct: −15 is furthest to the left.", "درست: −15 سب سے بائیں ہے۔"),
       [("−2", "−2", "−2 is right of −15, so it is bigger.", "−2، −15 کے دائیں ہے، اس لیے بڑا ہے۔", "bigger_digits"),
        ("0", "0", "0 is bigger than every negative number.", "0 ہر منفی عدد سے بڑا ہے۔"),
        ("9", "9", "9 is the biggest of the four.", "9 ان چاروں میں سب سے بڑا ہے۔")], 1),
   mcq("m6_ascending", "3, −8, −1, 5 in ascending order is:", "3، −8، −1، 5 صعودی ترتیب میں ہیں:",
       (", ".join(map(signed, M6)), ", ".join(map(signed, M6)), "Correct: smallest to biggest, left to right.", "درست: چھوٹے سے بڑے، بائیں سے دائیں۔"),
       [(", ".join(map(signed, M6_DESC)), ", ".join(map(signed, M6_DESC)), "That is descending order.", "یہ نزولی ترتیب ہے۔", "abs_order_mixed"),
        (", ".join(map(signed, M6_ABS)), ", ".join(map(signed, M6_ABS)), "That orders them by absolute value. Order them by value.", "یہ مطلق قیمت کی ترتیب ہے۔ قیمت کی ترتیب بنائیں۔", "abs_order_mixed"),
        ("−1, −8, 3, 5", "−1، −8، 3، 5", "−8 is smaller than −1, so it comes first.", "−8، −1 سے چھوٹا ہے، اس لیے پہلے آئے گا۔", "bigger_digits")], 0),
   mcq("m7_greatest_abs", "Which of 6, −11, 9 and −10 has the greatest absolute value?", "6، −11، 9 اور −10 میں سے کس کی مطلق قیمت سب سے زیادہ ہے؟",
       ("−11", "−11", "Correct: |−11| = 11 is the greatest.", "درست: |−11| = 11 سب سے بڑی ہے۔"),
       [("9", "9", "9 is the greatest number, but |−11| = 11 and |−10| = 10 are bigger than 9.", "9 سب سے بڑا عدد ہے، مگر |−11| = 11 اور |−10| = 10، 9 سے بڑی ہیں۔", "abs_order_mixed"),
        ("−10", "−10", "|−10| = 10, but |−11| = 11 is bigger.", "|−10| = 10، مگر |−11| = 11 بڑی ہے۔"),
        ("6", "6", "|6| = 6 is the smallest absolute value.", "|6| = 6 سب سے چھوٹی مطلق قیمت ہے۔")], 2),
   mcq("m8_true", "Which statement is true?", "کون سا بیان درست ہے؟",
       ("−9 < −2", "−9 < −2", "Correct: −9 is further left than −2.", "درست: −9، −2 سے زیادہ بائیں ہے۔"),
       [("−3 > 0", "−3 > 0", "Every negative number is less than 0.", "ہر منفی عدد 0 سے چھوٹا ہے۔"),
        ("|−5| < |4|", "|−5| < |4|", "|−5| = 5, which is more than |4| = 4.", "|−5| = 5، جو |4| = 4 سے زیادہ ہے۔", "sign_kept"),
        ("−1 > 1", "−1 > 1", "−1 is left of 1, so −1 < 1.", "−1، 1 کے بائیں ہے، اس لیے −1 < 1", "bigger_digits")], 3),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   short("q1_abs_diff", "Find |−15| − |9|.", "|−15| − |9| معلوم کریں۔",
     S1,
     T("Find each absolute value first: 15 and 9.", "پہلے ہر مطلق قیمت معلوم کریں: 15 اور 9"),
     T("Correct: 15 − 9 = 6.", "درست: 15 − 9 = 6"),
     T("Model answer: |−15| = 15 and |9| = 9, so 15 − 9 = 6.", "نمونہ جواب: |−15| = 15 اور |9| = 9، اس لیے 15 − 9 = 6"),
     common_wrong=[wrong(-24, "That uses −15 − 9. Take the absolute values first: 15 − 9 = 6.", "یہ −15 − 9 ہے۔ پہلے مطلق قیمتیں لیں: 15 − 9 = 6", "sign_kept")]),
   short("q2_withdraw", "A bank deposit is written as a positive integer. Write a withdrawal of Rs 800 as an integer.", "بینک میں رقم جمع کروانا مثبت صحیح عدد لکھا جاتا ہے۔ 800 روپے نکلوانے کو صحیح عدد میں لکھیں۔",
     S2,
     T("A withdrawal is the opposite of a deposit.", "رقم نکلوانا رقم جمع کروانے کا الٹ ہے۔"),
     T("Correct: −800.", "درست: −800"),
     T("Model answer: deposit is positive, so withdrawal is negative: −800.", "نمونہ جواب: جمع مثبت ہے، اس لیے نکلوانا منفی ہے: −800"),
     common_wrong=[wrong(800, "That would be a deposit. A withdrawal is negative: −800.", "یہ جمع ہوتا۔ نکلوانا منفی ہے: −800", "sign_ignored")]),
   short("q3_steps", "How many steps are there on the number line from −9 to 6?", "عددی خط پر −9 سے 6 تک کتنے قدم ہیں؟",
     S3,
     T("Steps from −9 to 0, then from 0 to 6.", "−9 سے 0 تک قدم، پھر 0 سے 6 تک۔"),
     T("Correct: 9 + 6 = 15.", "درست: 9 + 6 = 15"),
     T("Model answer: −9 to 0 is 9 steps, 0 to 6 is 6 steps, so 15 steps.", "نمونہ جواب: −9 سے 0 تک 9 قدم، 0 سے 6 تک 6 قدم، اس لیے 15 قدم۔"),
     common_wrong=[wrong(3, "That is 9 − 6. The numbers are on opposite sides of 0, so add: 15.", "یہ 9 − 6 ہے۔ اعداد 0 کے مخالف طرف ہیں، اس لیے جمع کریں: 15", "gap_miscount")]),
   short("q4_count", "How many integers x are there with −4 < x < 2?", "کتنے صحیح اعداد x ایسے ہیں کہ −4 < x < 2؟",
     S4,
     T("−4 and 2 are not included. List the integers between them, and include 0.", "−4 اور 2 شامل نہیں۔ ان کے بیچ کے صحیح اعداد لکھیں، اور 0 بھی شامل کریں۔"),
     T("Correct: −3, −2, −1, 0, 1.", "درست: −3، −2، −1، 0، 1"),
     T("Model answer: the integers are −3, −2, −1, 0, 1, which is 5.", "نمونہ جواب: صحیح اعداد −3، −2، −1، 0، 1 ہیں، یعنی 5"),
     common_wrong=[wrong(7, "That counts −4 and 2 as well. They are not included: 5.", "اس میں −4 اور 2 بھی گنے گئے ہیں۔ وہ شامل نہیں: 5", "gap_miscount"),
                   wrong(4, "Don't forget 0. The integers are −3, −2, −1, 0, 1: 5.", "0 کو نہ بھولیں۔ صحیح اعداد −3، −2، −1، 0، 1 ہیں: 5", "gap_miscount")]),
   short("q5_left", "Start at 2 on the number line and move 7 steps to the left. Which integer do you reach?", "عددی خط پر 2 سے شروع کریں اور 7 قدم بائیں جائیں۔ آپ کس صحیح عدد پر پہنچیں گے؟",
     S5,
     T("2 steps get you to 0. How many are left?", "2 قدم میں 0 پر پہنچتے ہیں۔ کتنے قدم باقی ہیں؟"),
     T("Correct: −5.", "درست: −5"),
     T("Model answer: 2 steps reach 0, and 5 more steps go past it to −5.", "نمونہ جواب: 2 قدم سے 0 پر، اور 5 قدم مزید آگے −5 پر۔"),
     common_wrong=[wrong(5, "That is 7 − 2 with the sign lost. You go past 0, so the answer is negative: −5.", "یہ علامت کھو کر 7 − 2 ہے۔ آپ 0 سے آگے جاتے ہیں، اس لیے جواب منفی ہے: −5", "sign_ignored"),
                   wrong(9, "That moved to the right. Left of 0 is negative: −5.", "یہ دائیں گیا۔ 0 کے بائیں منفی ہے: −5", "sign_ignored")]),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   long_q("l1_floors", "A building has floors from −6 (basement) to 8. Ali is on floor 5. Sana is on the floor that is the opposite of Ali's floor. How many floors apart are they?", "ایک عمارت کی منزلیں −6 (تہہ خانہ) سے 8 تک ہیں۔ علی منزل 5 پر ہے۔ ثنا اس منزل پر ہے جو علی کی منزل کی مخالف ہے۔ دونوں میں کتنی منزلوں کا فاصلہ ہے؟",
     L1,
     T("Find Sana's floor first. Then count the floors from her floor to Ali's.", "پہلے ثنا کی منزل معلوم کریں۔ پھر اس کی منزل سے علی کی منزل تک گنیں۔"),
     T("Correct: Sana is on −5, and 5 + 5 = 10.", "درست: ثنا −5 پر ہے، اور 5 + 5 = 10"),
     T("Model answer: the opposite of 5 is −5. From −5 to 0 is 5 floors and from 0 to 5 is 5 floors, so 10 floors apart.", "نمونہ جواب: 5 کا مخالف −5 ہے۔ −5 سے 0 تک 5 منزلیں اور 0 سے 5 تک 5 منزلیں، اس لیے 10 منزلوں کا فاصلہ۔"),
     common_wrong=[wrong(0, "The opposite of 5 is −5, not 5. They are 10 floors apart.", "5 کا مخالف −5 ہے، 5 نہیں۔ وہ 10 منزل دور ہیں۔", "opposite_same"),
                   wrong(5, "That is Ali's distance from 0 only. Add Sana's 5 floors: 10.", "یہ صرف علی کا 0 سے فاصلہ ہے۔ ثنا کی 5 منزلیں ملائیں: 10", "stops_early")]),
   long_q("l2_cities", "On a winter morning the temperatures are Murree −6, Quetta −11, Lahore 4, Karachi 18 and Skardu −14 degrees. Write them in ascending order. What is the second temperature in your list?", "سردیوں کی ایک صبح درجہ حرارت یہ ہیں: مری −6، کوئٹہ −11، لاہور 4، کراچی 18 اور سکردو −14 ڈگری۔ انہیں صعودی ترتیب میں لکھیں۔ آپ کی فہرست میں دوسرا درجہ حرارت کون سا ہے؟",
     L2,
     T("Ascending starts with the coldest, the smallest number.", "صعودی ترتیب سب سے ٹھنڈے، یعنی سب سے چھوٹے عدد سے شروع ہوتی ہے۔"),
     T("Correct: −14, −11, −6, 4, 18; the second is −11.", "درست: −14، −11، −6، 4، 18؛ دوسرا −11 ہے۔"),
     T("Model answer: the smallest is −14 (Skardu), then −11 (Quetta), −6, 4, 18. The second is −11.", "نمونہ جواب: سب سے چھوٹا −14 (سکردو) ہے، پھر −11 (کوئٹہ)، −6، 4، 18۔ دوسرا −11 ہے۔"),
     common_wrong=[wrong(4, "That is the second when listed from the biggest. Ascending starts with −14, so the second is −11.", "یہ بڑے سے شروع کرنے پر دوسرا ہے۔ صعودی ترتیب −14 سے شروع ہوتی ہے، اس لیے دوسرا −11 ہے۔", "abs_order_mixed"),
                   wrong(-6, "That is the second in order of absolute value (4, 6, 11 ...). By value the second is −11.", "یہ مطلق قیمت کی ترتیب (4، 6، 11 ...) میں دوسرا ہے۔ قیمت میں دوسرا −11 ہے۔", "abs_order_mixed")],
     ),
   long_q("l3_sum_abs", "Find the sum of the absolute values of all the integers from −4 to 4.", "−4 سے 4 تک تمام صحیح اعداد کی مطلق قیمتوں کا مجموعہ معلوم کریں۔",
     L3,
     T("List the integers, take each absolute value, then add. Don't forget 0.", "صحیح اعداد لکھیں، ہر مطلق قیمت لیں، پھر جمع کریں۔ 0 کو نہ بھولیں۔"),
     T("Correct: 2 × (1 + 2 + 3 + 4) = 20.", "درست: 2 × (1 + 2 + 3 + 4) = 20"),
     T("Model answer: 4+3+2+1+0+1+2+3+4 = 20, since −4 to −1 and 1 to 4 give the same absolute values.", "نمونہ جواب: 4+3+2+1+0+1+2+3+4 = 20، کیونکہ −4 سے −1 اور 1 سے 4 کی مطلق قیمتیں برابر ہیں۔"),
     common_wrong=[wrong(0, "That adds the integers with their signs. Absolute values are not negative: 20.", "یہ علامتوں کے ساتھ جمع ہے۔ مطلق قیمتیں منفی نہیں ہوتیں: 20", "sign_kept"),
                   wrong(10, "That is only one side, 1 + 2 + 3 + 4. The negative side gives another 10: 20.", "یہ صرف ایک طرف 1 + 2 + 3 + 4 ہے۔ منفی طرف مزید 10 دیتی ہے: 20", "stops_early")]),
   long_q("l4_who_am_i", "Who am I? My absolute value is 12, and I am less than −5.", "میں کون ہوں؟ میری مطلق قیمت 12 ہے، اور میں −5 سے چھوٹا ہوں۔",
     L4,
     T("Two integers have absolute value 12. Which one is less than −5?", "دو صحیح اعداد کی مطلق قیمت 12 ہے۔ ان میں سے کون −5 سے چھوٹا ہے؟"),
     T("Correct: −12.", "درست: −12"),
     T("Model answer: the integers with absolute value 12 are 12 and −12. 12 is greater than −5, but −12 is less than −5. So I am −12.", "نمونہ جواب: مطلق قیمت 12 والے صحیح اعداد 12 اور −12 ہیں۔ 12، −5 سے بڑا ہے، مگر −12، −5 سے چھوٹا ہے۔ اس لیے میں −12 ہوں۔"),
     common_wrong=[wrong(12, "12 is greater than −5. The other integer with absolute value 12 is −12.", "12، −5 سے بڑا ہے۔ مطلق قیمت 12 والا دوسرا صحیح عدد −12 ہے۔", "one_value")],
     ),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 2 test. Well done!", "آپ نے باب 2 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: a loss, a debt or a point below zero is negative; the opposite of a number is on the other side of 0; the smaller of two negative numbers has the bigger digits; and the absolute value is a distance, so it is never negative. When you order by absolute value, write the absolute values first.",
              "امتحان میں: نقصان، قرض یا صفر سے نیچے کا نقطہ منفی ہوتا ہے؛ عدد کا مخالف 0 کی دوسری طرف ہوتا ہے؛ دو منفی اعداد میں بڑے ہندسوں والا چھوٹا ہوتا ہے؛ اور مطلق قیمت فاصلہ ہے، اس لیے کبھی منفی نہیں ہوتی۔ مطلق قیمت کی ترتیب میں پہلے مطلق قیمتیں لکھیں۔"),
    "points": [T("Check an ordering by placing the numbers on a number line.", "ترتیب کو عددی خط پر اعداد رکھ کر جانچیں۔"),
               T("Between a negative and a positive number, count the steps to 0 on each side and add.", "منفی اور مثبت عدد کے بیچ، 0 تک ہر طرف کے قدم گن کر جمع کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_gap", "type": "exam_style", "skill": SKILL, "step": number_question(
     "r_exam_gap",
     T("How many steps are there on the number line from −3 to 12?", "عددی خط پر −3 سے 12 تک کتنے قدم ہیں؟"),
     R1,
     T("Steps from −3 to 0, then from 0 to 12.", "−3 سے 0 تک قدم، پھر 0 سے 12 تک۔"),
     T("Correct: 3 + 12 = 15.", "درست: 3 + 12 = 15"),
     T("−3 to 0 is 3 steps and 0 to 12 is 12 steps, so 15.", "−3 سے 0 تک 3 قدم اور 0 سے 12 تک 12 قدم، اس لیے 15"),
     common_wrong=[wrong(9, "That is 12 − 3. The numbers are on opposite sides of 0, so add: 15.", "یہ 12 − 3 ہے۔ اعداد 0 کے مخالف طرف ہیں، اس لیے جمع کریں: 15", "gap_miscount")],
     qtype=None)},
   {"id": "r_exam_order", "type": "exam_style", "skill": SKILL, "step": number_question(
     "r_exam_order",
     T("Arrange −5, 7, −1, 0 in descending order. Which number is the second?", "−5، 7، −1، 0 کو نزولی ترتیب میں لکھیں۔ دوسرا عدد کون سا ہے؟"),
     R2,
     T("Descending starts with the biggest.", "نزولی ترتیب سب سے بڑے سے شروع ہوتی ہے۔"),
     T("Correct: 7, 0, −1, −5; the second is 0.", "درست: 7، 0، −1، −5؛ دوسرا 0 ہے۔"),
     T("Descending: 7, 0, −1, −5. The second is 0.", "نزولی: 7، 0، −1، −5۔ دوسرا 0 ہے۔"),
     common_wrong=[wrong(-1, "That is the second in ascending order. Descending: 7, 0, ...", "یہ صعودی ترتیب میں دوسرا ہے۔ نزولی: 7، 0، ...", "abs_order_mixed")],
     qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 2 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
   "It has its own skill (maths.integers.chapter_2_test), with the unit's skills as prerequisites, and is mastered with exam_style questions, like g9-maths-05-board-exam-practice.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), غیر جانبدار صحیح عدد (neutral integer).",
   "The numbers were worked out in content/sources/g6-maths-04/chapter_2_test.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

write(lesson)

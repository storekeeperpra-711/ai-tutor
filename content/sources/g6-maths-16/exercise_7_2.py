"""Practice set for Exercise 7.2 of the book: pick out linear equations, build
equations from statements, solve one-variable equations (with fractions and
decimals) and check them, and solve word problems (ages, consecutive numbers,
sharing in a ratio, cricket scores). The questions are new; only the kinds of
question follow the book."""
from decimal import Decimal as D
from common import (T, say, nq, eq_q, ch, practice_lesson, practice_intro, write, solves, solve,
                    EX_SKILL, EQ_RECOGNISE, EQ_CHECK, EQ_FORMING, EQ_TWO_STEP, EQ_BRACKETS, EQ_WORD_PROBLEMS,
                    ALG_EQUATIONS)
import figs

SKILL = EX_SKILL["7.2"]


def linear_one_variable(eq):
    """An equation (has =), one letter only, with that letter to the power 1."""
    letters = {c for c in eq if c.isalpha()}
    return "=" in eq and len(letters) == 1 and "²" not in eq


# q1: which is a linear equation in one variable
Q1_RIGHT, Q1_WRONG = "3x + 1 = 10", ["x² = 9", "2x + y = 7", "5x + 3"]
assert linear_one_variable(Q1_RIGHT) and not any(linear_one_variable(w) for w in Q1_WRONG)
assert solve(Q1_RIGHT) == 3
# q2: count the linear equations in one variable
ITEMS2 = ["x + 4 = 9", "y² = 16", "2a − 3 = 7", "m + n = 5", "5k = 40"]
Q2 = len([e for e in ITEMS2 if linear_one_variable(e)])
assert Q2 == 3 and len([e for e in ITEMS2 if "=" in e]) == 5
# q3: x ÷ 4 = 6
Q3 = solve("x ÷ 4 = 6")
assert Q3 == 24 and 6 + 4 == 10 and 6 - 4 == 2
# q4: 4x + 5 = 29
Q4 = solve("4x + 5 = 29")
assert Q4 == 6 and 29 - 5 == 24 and 29 + 5 == 34
FIG4, EQ4 = figs.balance_eq(4, "x", 5, 29, Q4)
assert EQ4 == "4x + 5 = 29"
# q5: check x = 7 in 3x − 5 = 16
assert solve("3x − 5 = 16") == 7 and 3 * 7 - 5 == 16 and 7 - 5 != 16 and 3 * 7 + 5 != 16
# q6: x + 2.5 = 7.8
Q6 = D("7.8") - D("2.5")
assert Q6 == D("5.3") and Q6 + D("2.5") == D("7.8") and D("7.8") + D("2.5") == D("10.3")
# q7: half of a number, plus 3, is 8
Q7 = solve("x ÷ 2 + 3 = 8")
assert Q7 == 10 and (8 - 3) == 5 and 8 * 2 == 16 and 8 * 2 - 3 != Q7
# q8: 3 times k, decreased by 4, is 20 (k = 8)
assert solve("3k − 4 = 20", "k") == 8 and not solves("3(k − 4) = 20", k=8) and not solves("3k + 4 = 20", k=8)
# q9: 2x + 6 = 20 gives x = 7, not (20 + 6) ÷ 2 = 13
Q9 = solve("2x + 6 = 20")
assert Q9 == 7 and (20 + 6) // 2 == 13 and not solves("2x + 6 = 20", x=13)
# q10: Sara is x, Ali is x + 5, together 37
Q10 = solve("x + (x + 5) = 37")
assert Q10 == 16 and Q10 + 5 == 21 and 37 - 5 == 32
# q11: three consecutive numbers with sum 78
Q11 = solve("x + (x + 1) + (x + 2) = 78")
assert Q11 == 25 and Q11 + 1 == 26 and Q11 + 2 == 27
assert sum([Q11, Q11 + 1, Q11 + 2]) == 78
# q12: Rs 450 shared in the ratio 2 : 3, Sana gets the larger share
PART = solve("5x = 450")
Q12 = 3 * PART
assert PART == 90 and Q12 == 270 and 2 * PART == 180 and 2 * PART + Q12 == 450
# q13: batter scores 12 more than twice his partner's runs, 52 in all
Q13 = solve("2x + 12 = 52")
assert Q13 == 20 and 52 - 12 == 40 and 52 // 2 - 12 == 14 and 2 * Q13 + 12 == 52
# bank and review
QB = solve("5x = 45")
assert QB == 9 and 45 - 5 == 40
R1 = solve("2x + 3 = 11")
assert R1 == 4 and (11 - 3) == 8
R2 = solve("x + 9 = 31")
assert R2 == 22 and 31 + 9 == 40

lesson = practice_lesson(
 "7.2", script="exercise_7_2.py",
 title=T("Exercise 7.2 practice: solving linear equations", "مشق 7.2 کی پریکٹس: خطی مساوات حل کرنا"),
 outcome="Identify linear equations in one variable, build equations from statements, solve them (with fractions and decimals), check the solution, and solve word problems.",
 prerequisites=[EQ_RECOGNISE, EQ_CHECK, EQ_FORMING, EQ_TWO_STEP, EQ_BRACKETS, EQ_WORD_PROBLEMS, ALG_EQUATIONS],
 misconceptions=[
   {"id": "power_is_linear", "description": "Counts x² = 9 or an equation with two letters as a linear equation in one variable."},
   {"id": "wrong_inverse", "description": "Undoes an operation by repeating it or doing the wrong one, like adding 4 when the equation divides by 4."},
   {"id": "stops_early", "description": "Stops after the first step, like 4x = 24, and gives that as the answer."},
   {"id": "order_of_steps", "description": "Divides or multiplies before dealing with the number added or subtracted, so the answer is wrong."},
   {"id": "brackets_wrong", "description": "Puts brackets where the words don't need them, like 3(k − 4) for 'three times k, decreased by 4'."},
   {"id": "answer_is_other_quantity", "description": "Finds the unknown but gives another quantity from the story (Ali's age instead of Sara's, the middle number instead of the smallest)."},
   {"id": "check_wrong_side", "description": "Checks a solution with the wrong operation, or only compares it with a number in the equation."},
   {"id": "ratio_as_amount", "description": "Treats a ratio number (2 or 3) as the amount, or finds one part and stops."},
 ],
 steps=[
   practice_intro("7.2",
     "Here you pick out linear equations, build equations from statements, solve them (with fractions and decimals) and check them, and solve word problems about ages, consecutive numbers, sharing and cricket scores.",
     "اس میں آپ خطی مساواتیں پہچانیں گے، بیانات سے مساواتیں بنائیں گے، انھیں (کسروں اور اعشاریہ کے ساتھ) حل کر کے جانچیں گے، اور عمروں، لگاتار اعداد، تقسیم اور کرکٹ کے رنز کے سوال حل کریں گے۔",
     "Exercise 7.2 is about solving equations. Ready?", "مشق 7.2 مساوات حل کرنے کے بارے میں ہے۔ تیار؟"),
   ch("q1_linear", ("Which of these is a linear equation in one variable?", "ان میں سے کون سی ایک متغیر والی خطی مساوات ہے؟"),
      (Q1_RIGHT, Q1_RIGHT, "Yes! One letter, with power 1, and an = sign.", "جی ہاں! ایک حرف، طاقت 1، اور = کا نشان۔"),
      [(Q1_WRONG[0], Q1_WRONG[0], "x² has power 2, so it is not linear.", "x² کی طاقت 2 ہے، اس لیے یہ خطی نہیں۔", "power_is_linear"),
       (Q1_WRONG[1], Q1_WRONG[1], "It has two letters, x and y. Linear in one variable has only one letter.", "اس میں دو حرف x اور y ہیں۔ ایک متغیر والی خطی مساوات میں صرف ایک حرف ہوتا ہے۔", "power_is_linear"),
       (Q1_WRONG[2], Q1_WRONG[2], "No = sign, so it is an expression, not an equation.", "= کا نشان نہیں، اس لیے یہ الجبری جملہ ہے۔")],
      1, qtype="recall"),
   nq("q2_count", (f"How many of these are linear equations in one variable: {', '.join(ITEMS2)}?", f"ان میں سے کتنی ایک متغیر والی خطی مساواتیں ہیں: {', '.join(ITEMS2)}؟"), Q2,
      ("Each needs one letter only, with power 1.", "ہر ایک میں صرف ایک حرف اور طاقت 1 ہونی چاہیے۔"),
      ("Right! x + 4 = 9, 2a − 3 = 7 and 5k = 40: 3.", "درست! x + 4 = 9، 2a − 3 = 7 اور 5k = 40: 3"),
      ("y² = 16 has a power 2 and m + n = 5 has two letters. The other 3 are linear.", "y² = 16 میں طاقت 2 ہے اور m + n = 5 میں دو حرف ہیں۔ باقی 3 خطی ہیں۔"),
      [(5, "All five have = signs, but y² has power 2 and m + n has two letters: 3.", "پانچوں میں = ہے، مگر y² کی طاقت 2 ہے اور m + n میں دو حرف ہیں: 3", "power_is_linear"),
       (4, "y² = 16 is not linear, and neither is m + n = 5: 3.", "y² = 16 خطی نہیں، اور m + n = 5 بھی نہیں: 3", "power_is_linear")], qtype="recall"),
   nq("q3_divide", ("Solve the equation x ÷ 4 = 6.", "مساوات x ÷ 4 = 6 حل کریں۔"), Q3,
      ("x is divided by 4. Undo it by multiplying by 4.", "x کو 4 سے تقسیم کیا گیا ہے۔ اسے 4 سے ضرب دے کر ختم کریں۔"),
      ("Right! x = 6 × 4 = 24.", "درست! x = 6 × 4 = 24"), ("Undo ÷ 4 with × 4: 6 × 4 = 24, and 24 ÷ 4 = 6.", "÷ 4 کو × 4 سے ختم کریں: 6 × 4 = 24، اور 24 ÷ 4 = 6"),
      [(10, "That adds 4. Dividing is undone by multiplying: 24.", "یہ 4 جمع کرتا ہے۔ تقسیم کو ضرب سے ختم کرتے ہیں: 24", "wrong_inverse"),
       (2, "That takes 4 away. Undo ÷ 4 with × 4: 24.", "یہ 4 تفریق کرتا ہے۔ ÷ 4 کو × 4 سے ختم کریں: 24", "wrong_inverse")], qtype="recall"),
   nq("q4_two_step", ("Solve 4x + 5 = 29. Take away the 5 first, then divide.", "حل کریں 4x + 5 = 29۔ پہلے 5 تفریق کریں، پھر تقسیم کریں۔"), Q4,
      ("29 − 5 = 24, so 4x = 24.", "29 − 5 = 24، تو 4x = 24"),
      ("Right! 4x = 24, so x = 6. Check: 4 × 6 + 5 = 29.", "درست! 4x = 24، تو x = 6۔ جانچ: 4 × 6 + 5 = 29"),
      ("29 − 5 = 24, then 24 ÷ 4 = 6.", "29 − 5 = 24، پھر 24 ÷ 4 = 6"),
      [(24, "4x = 24 is only the first step. Divide by 4 too: 6.", "4x = 24 صرف پہلا قدم ہے۔ 4 سے تقسیم بھی کریں: 6", "stops_early"),
       (34, "To undo + 5, take 5 away, not add: 24, then 6.", "+ 5 کو ختم کرنے کے لیے 5 تفریق کریں، جمع نہیں: 24، پھر 6", "wrong_inverse")]),
   ch("q5_check", ("Mohsin solved 3x − 5 = 16 and got x = 7. Which check shows he is right?", "محسن نے 3x − 5 = 16 حل کر کے x = 7 پایا۔ کون سی جانچ دکھاتی ہے کہ وہ درست ہے؟"),
      ("3 × 7 − 5 = 21 − 5 = 16, which matches the right side.", "3 × 7 − 5 = 21 − 5 = 16، جو دائیں طرف کے برابر ہے۔", "Yes! Put 7 in place of x and both sides are 16.", "جی ہاں! x کی جگہ 7 رکھیں تو دونوں طرف 16 ہے۔"),
      [("7 − 5 = 2, which is not 16.", "7 − 5 = 2، جو 16 نہیں۔", "Put 7 into the whole left side, 3x − 5, not just x − 5.", "پوری بائیں طرف 3x − 5 میں 7 رکھیں، صرف x − 5 میں نہیں۔", "check_wrong_side"),
       ("3 × 7 + 5 = 26, which is not 16.", "3 × 7 + 5 = 26، جو 16 نہیں۔", "The equation has − 5, so the check uses − 5 too: 21 − 5 = 16.", "مساوات میں − 5 ہے، تو جانچ میں بھی − 5: 21 − 5 = 16", "check_wrong_side")],
      2),
   nq("q6_decimal", ("Solve x + 2.5 = 7.8.", "حل کریں x + 2.5 = 7.8"), Q6,
      ("Take 2.5 away from 7.8. Line up the decimal points.", "7.8 میں سے 2.5 تفریق کریں۔ اعشاریہ نقطے ایک سیدھ میں رکھیں۔"),
      ("Right! x = 7.8 − 2.5 = 5.3.", "درست! x = 7.8 − 2.5 = 5.3"), ("7.8 − 2.5 = 5.3, and 5.3 + 2.5 = 7.8.", "7.8 − 2.5 = 5.3، اور 5.3 + 2.5 = 7.8"),
      [(D("10.3"), "That adds 2.5. Undo + 2.5 by taking 2.5 away: 5.3.", "یہ 2.5 جمع کرتا ہے۔ + 2.5 کو 2.5 تفریق کر کے ختم کریں: 5.3", "wrong_inverse")]),
   nq("q7_fraction", ("Half of a number, plus 3, is 8. This is x ÷ 2 + 3 = 8. Find x.", "ایک عدد کا آدھا، جمع 3، 8 ہے۔ یہ x ÷ 2 + 3 = 8 ہے۔ x معلوم کریں۔"), Q7,
      ("Take away 3 first: x ÷ 2 = 5. Then multiply by 2.", "پہلے 3 تفریق کریں: x ÷ 2 = 5۔ پھر 2 سے ضرب دیں۔"),
      ("Right! x ÷ 2 = 5, so x = 10. Check: 10 ÷ 2 + 3 = 8.", "درست! x ÷ 2 = 5، تو x = 10۔ جانچ: 10 ÷ 2 + 3 = 8"),
      ("8 − 3 = 5, then 5 × 2 = 10.", "8 − 3 = 5، پھر 5 × 2 = 10"),
      [(5, "x ÷ 2 = 5 is only the first step. Multiply by 2: 10.", "x ÷ 2 = 5 صرف پہلا قدم ہے۔ 2 سے ضرب دیں: 10", "stops_early"),
       (16, "That multiplies 8 by 2 before taking away the 3. Take 3 away first: 10.", "یہ 3 تفریق کرنے سے پہلے 8 کو 2 سے ضرب دیتا ہے۔ پہلے 3 تفریق کریں: 10", "order_of_steps")]),
   eq_q("q8_build", ("Write an equation: 3 times a number k, decreased by 4, is 20.", "مساوات لکھیں: عدد k کا 3 گنا، 4 کم، 20 ہے۔"),
        ["3k − 4 = 20", "3 × k − 4 = 20", "20 = 3k − 4"], {"k": 8},
        ("3 times k is 3k. Then take away 4.", "k کا 3 گنا 3k ہے۔ پھر 4 تفریق کریں۔"),
        ("Right! 3k − 4 = 20.", "درست! 3k − 4 = 20"), ("3k, decreased by 4, is 3k − 4, and it equals 20.", "3k میں سے 4 کم یعنی 3k − 4، اور یہ 20 کے برابر ہے۔"),
        [("3(k − 4) = 20", "Only 3k is decreased by 4. Brackets would multiply the 4 as well: 3k − 4 = 20.", "4 صرف 3k میں سے کم ہوتا ہے۔ قوسین 4 کو بھی ضرب دیتی: 3k − 4 = 20", "brackets_wrong"),
         ("3k + 4 = 20", "'Decreased' means take away: 3k − 4 = 20.", "'کم' کا مطلب تفریق: 3k − 4 = 20", "wrong_inverse")]),
   ch("q9_find_error", ("Imran solves 2x + 6 = 20 like this: x = (20 + 6) ÷ 2 = 13. What went wrong?", "عمران 2x + 6 = 20 کو یوں حل کرتا ہے: x = (20 + 6) ÷ 2 = 13۔ کیا غلطی ہوئی؟"),
      ("He added 6. To undo + 6, take 6 away: 20 − 6 = 14, then 14 ÷ 2 = 7.", "اس نے 6 جمع کیا۔ + 6 کو ختم کرنے کے لیے 6 تفریق کریں: 20 − 6 = 14، پھر 14 ÷ 2 = 7", "Yes! Check: 2 × 13 + 6 = 32, not 20, but 2 × 7 + 6 = 20.", "جی ہاں! جانچ: 2 × 13 + 6 = 32، 20 نہیں، مگر 2 × 7 + 6 = 20"),
      [("Nothing. x = 13 is right.", "کوئی غلطی نہیں۔ x = 13 درست ہے۔", "Check it: 2 × 13 + 6 = 32, not 20.", "جانچیں: 2 × 13 + 6 = 32، 20 نہیں۔", "wrong_inverse"),
       ("He should not divide by 2.", "اسے 2 سے تقسیم نہیں کرنا چاہیے۔", "Dividing by 2 is right. The mistake is adding 6 instead of taking it away.", "2 سے تقسیم درست ہے۔ غلطی 6 تفریق کرنے کی جگہ جمع کرنا ہے۔", "order_of_steps")],
      0, qtype="find_error"),
   nq("q10_ages", ("Ali is 5 years older than Sara. Together their ages add up to 37. If Sara is x years old, then x + (x + 5) = 37. How old is Sara?", "علی سارہ سے 5 سال بڑا ہے۔ دونوں کی عمروں کا مجموعہ 37 ہے۔ اگر سارہ x سال کی ہے تو x + (x + 5) = 37۔ سارہ کتنے سال کی ہے؟"), Q10,
      ("x + x + 5 = 2x + 5 = 37. Solve for x.", "x + x + 5 = 2x + 5 = 37۔ x معلوم کریں۔"),
      ("Right! 2x = 32, so Sara is 16 (and Ali is 21).", "درست! 2x = 32، تو سارہ 16 سال کی ہے (اور علی 21 کا)۔"),
      ("2x + 5 = 37, so 2x = 32 and x = 16.", "2x + 5 = 37، تو 2x = 32 اور x = 16"),
      [(21, "21 is Ali's age. The question asks for Sara: 16.", "21 علی کی عمر ہے۔ سوال سارہ کی عمر پوچھتا ہے: 16", "answer_is_other_quantity"),
       (32, "That is 37 − 5, only the first step. Divide by 2: 16.", "یہ 37 − 5 ہے، صرف پہلا قدم۔ 2 سے تقسیم کریں: 16", "stops_early")]),
   nq("q11_consecutive", ("The sum of three consecutive numbers is 78. If the smallest is x, the numbers are x, x + 1 and x + 2. Find the smallest.", "تین لگاتار اعداد کا مجموعہ 78 ہے۔ اگر سب سے چھوٹا x ہو تو اعداد x، x + 1 اور x + 2 ہیں۔ سب سے چھوٹا عدد معلوم کریں۔"), Q11,
      ("x + (x + 1) + (x + 2) = 3x + 3 = 78.", "x + (x + 1) + (x + 2) = 3x + 3 = 78"),
      ("Right! 3x = 75, so x = 25. The numbers are 25, 26, 27.", "درست! 3x = 75، تو x = 25۔ اعداد 25، 26، 27 ہیں۔"),
      ("3x + 3 = 78, so 3x = 75 and x = 25.", "3x + 3 = 78، تو 3x = 75 اور x = 25"),
      [(26, "26 is the middle number. The question asks for the smallest: 25.", "26 درمیانی عدد ہے۔ سوال سب سے چھوٹا پوچھتا ہے: 25", "answer_is_other_quantity"),
       (27, "27 is the largest number. The smallest is x = 25.", "27 سب سے بڑا عدد ہے۔ سب سے چھوٹا x = 25 ہے۔", "answer_is_other_quantity")]),
   nq("q12_ratio", ("Rs 450 is shared between Hina and Sana in the ratio 2 : 3. There are 2 + 3 = 5 equal parts, so 5x = 450. How many rupees does Sana get (3 parts)?", "450 روپے حنا اور ثناء میں نسبت 2 : 3 سے تقسیم ہوتے ہیں۔ 2 + 3 = 5 برابر حصے ہیں، تو 5x = 450۔ ثناء کو (3 حصے) کتنے روپے ملتے ہیں؟"), Q12,
      ("First find one part: 450 ÷ 5.", "پہلے ایک حصہ معلوم کریں: 450 ÷ 5"),
      ("Right! One part is Rs 90, so Sana gets 3 × 90 = Rs 270.", "درست! ایک حصہ 90 روپے ہے، تو ثناء کو 3 × 90 = 270 روپے ملتے ہیں۔"),
      ("x = 450 ÷ 5 = 90. Sana gets 3 × 90 = 270.", "x = 450 ÷ 5 = 90۔ ثناء کو 3 × 90 = 270 ملتے ہیں۔"),
      [(90, "Rs 90 is one part. Sana has 3 parts: 270.", "90 روپے ایک حصہ ہے۔ ثناء کے 3 حصے ہیں: 270", "ratio_as_amount"),
       (180, "Rs 180 is Hina's share (2 parts). Sana's is 3 parts: 270.", "180 روپے حنا کا حصہ ہے (2 حصے)۔ ثناء کے 3 حصے ہیں: 270", "answer_is_other_quantity")]),
   nq("q13_cricket", ("A batter scored 12 more than twice the runs of his partner. He scored 52 runs. If his partner scored x runs, then 2x + 12 = 52. How many runs did the partner score?", "ایک بلے باز نے اپنے ساتھی کے رنز کے دگنے سے 12 زیادہ رنز بنائے۔ اس نے 52 رنز بنائے۔ اگر اس کے ساتھی نے x رنز بنائے تو 2x + 12 = 52۔ ساتھی نے کتنے رنز بنائے؟"), Q13,
      ("Take away 12 first, then divide by 2.", "پہلے 12 تفریق کریں، پھر 2 سے تقسیم کریں۔"),
      ("Right! 2x = 40, so x = 20. Check: 2 × 20 + 12 = 52.", "درست! 2x = 40، تو x = 20۔ جانچ: 2 × 20 + 12 = 52"),
      ("52 − 12 = 40, then 40 ÷ 2 = 20.", "52 − 12 = 40، پھر 40 ÷ 2 = 20"),
      [(40, "2x = 40 is only the first step. Divide by 2: 20.", "2x = 40 صرف پہلا قدم ہے۔ 2 سے تقسیم کریں: 20", "stops_early"),
       (14, "That divides 52 by 2 before taking away 12. Take 12 away first: 20.", "یہ 12 تفریق کرنے سے پہلے 52 کو 2 سے تقسیم کرتا ہے۔ پہلے 12 تفریق کریں: 20", "order_of_steps")]),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can solve and check equations.", "شاباش! آپ مساواتیں حل کر کے جانچ سکتے ہیں۔"),
    "text": T("A linear equation in one variable has one letter with power 1 and an = sign. Solve it by undoing the operations in reverse order, doing the same to both sides: take away or add first, then divide or multiply. Check by putting the answer back. For a word problem, call the unknown x, write the equation, solve it, and answer what the question asks (Sara's age, the smallest number, Sana's share).",
              "ایک متغیر والی خطی مساوات میں ایک حرف ہوتا ہے جس کی طاقت 1 ہو اور = کا نشان۔ اسے حل کرنے کے لیے عملوں کو الٹی ترتیب سے ختم کریں، دونوں طرف ایک ہی کام کریں: پہلے جمع یا تفریق، پھر تقسیم یا ضرب۔ جواب واپس رکھ کر جانچیں۔ لفظی سوال میں نامعلوم کو x کہیں، مساوات لکھیں، حل کریں، اور وہی بتائیں جو سوال پوچھتا ہے (سارہ کی عمر، سب سے چھوٹا عدد، ثناء کا حصہ)۔"),
    "points": [T("Undo the adding or taking away first.", "پہلے جمع یا تفریق کو ختم کریں۔"),
               T("Check by putting the answer in the equation.", "جواب کو مساوات میں رکھ کر جانچیں۔")]},
 ],
 bank=[
   {"id": "qb_both_sides", "type": "recall", "step": ch("qb_both_sides", ("When you solve an equation, what must you do to keep it balanced?", "مساوات حل کرتے وقت اسے برابر رکھنے کے لیے کیا کرنا چاہیے؟"),
      ("Do the same to both sides.", "دونوں طرف ایک ہی کام کریں۔", "Yes! Like a balance scale, both sides must change in the same way.", "جی ہاں! ترازو کی طرح دونوں طرف ایک ہی طرح تبدیلی ہونی چاہیے۔"),
      [("Change only the side with the letter.", "صرف حرف والی طرف بدلیں۔", "Then the two sides would no longer be equal.", "تب دونوں طرف برابر نہیں رہیں گی۔", "wrong_inverse"),
       ("Add to one side and take away from the other.", "ایک طرف جمع کریں اور دوسری طرف سے تفریق۔", "That unbalances it. Do the same to both sides.", "اس سے توازن بگڑ جاتا ہے۔ دونوں طرف ایک ہی کام کریں۔", "wrong_inverse")],
      1, qtype=None)},
   {"id": "qb_solve", "type": "apply", "step": nq("qb_solve", ("Solve 5x = 45.", "حل کریں 5x = 45"), QB,
      ("Undo × 5 by dividing by 5.", "× 5 کو 5 سے تقسیم کر کے ختم کریں۔"),
      ("Right! x = 9.", "درست! x = 9"), ("45 ÷ 5 = 9.", "45 ÷ 5 = 9"),
      [(40, "That takes 5 away. Undo × 5 by ÷ 5: 9.", "یہ 5 تفریق کرتا ہے۔ × 5 کو ÷ 5 سے ختم کریں: 9", "wrong_inverse")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Hira says x² = 16 is a linear equation in one variable. What went wrong?", "ہیرا کہتی ہے x² = 16 ایک متغیر والی خطی مساوات ہے۔ کیا غلطی ہوئی؟"),
      ("x has power 2. A linear equation has power 1 only.", "x کی طاقت 2 ہے۔ خطی مساوات میں صرف طاقت 1 ہوتی ہے۔", "Yes! x² is x × x, so it is not linear.", "جی ہاں! x² یعنی x × x، اس لیے یہ خطی نہیں۔"),
      [("Nothing. It has one letter and an = sign.", "کوئی غلطی نہیں۔ اس میں ایک حرف اور = کا نشان ہے۔", "The power matters too: linear means power 1.", "طاقت بھی اہم ہے: خطی کا مطلب طاقت 1۔", "power_is_linear"),
       ("It has no = sign.", "اس میں = کا نشان نہیں۔", "It does have =. The problem is the power 2.", "اس میں = ہے۔ مسئلہ طاقت 2 کا ہے۔")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_two_step", "type": "apply", "step": nq("r_two_step", ("Solve 2x + 3 = 11.", "حل کریں 2x + 3 = 11"), R1,
      ("Take 3 away first, then divide by 2.", "پہلے 3 تفریق کریں، پھر 2 سے تقسیم کریں۔"),
      ("Right! 2x = 8, so x = 4.", "درست! 2x = 8، تو x = 4"), ("11 − 3 = 8, then 8 ÷ 2 = 4.", "11 − 3 = 8، پھر 8 ÷ 2 = 4"),
      [(8, "2x = 8 is only the first step. Divide by 2: 4.", "2x = 8 صرف پہلا قدم ہے۔ 2 سے تقسیم کریں: 4", "stops_early")], qtype=None)},
   {"id": "r_one_step", "type": "apply", "step": nq("r_one_step", ("Solve x + 9 = 31.", "حل کریں x + 9 = 31"), R2,
      ("Take 9 away from 31.", "31 میں سے 9 تفریق کریں۔"),
      ("Right! x = 22.", "درست! x = 22"), ("31 − 9 = 22.", "31 − 9 = 22"),
      [(40, "That adds 9. Undo + 9 by taking 9 away: 22.", "یہ 9 جمع کرتا ہے۔ + 9 کو 9 تفریق کر کے ختم کریں: 22", "wrong_inverse")], qtype=None)},
 ],
 glossary=[T("Linear equation", "خطی مساوات"), T("Solution", "حل"), T("Check", "جانچ"), T("Consecutive numbers", "لگاتار اعداد"), T("Ratio", "نسبت")],
 flashcards=[
   {"id": "f_solve", "front": T("How do you solve 3x + 4 = 19?", "3x + 4 = 19 کیسے حل کرتے ہیں؟"),
    "back": T("Take 4 away: 3x = 15. Divide by 3: x = 5. Check: 3 × 5 + 4 = 19.", "4 تفریق کریں: 3x = 15۔ 3 سے تقسیم کریں: x = 5۔ جانچ: 3 × 5 + 4 = 19")},
   {"id": "f_linear", "front": T("What makes an equation linear in one variable?", "ایک متغیر والی مساوات خطی کب ہوتی ہے؟"),
    "back": T("One letter with power 1, like 2x − 3 = 7. Not x² = 9 and not x + y = 5.", "ایک حرف جس کی طاقت 1 ہو، جیسے 2x − 3 = 7۔ x² = 9 نہیں اور x + y = 5 بھی نہیں۔")},
 ],
 home_task={"id": "h_solve_at_home", "text": T(
   "Make up a number puzzle for someone at home: 'I think of a number, double it and add 5, and get 17.' Write it as an equation, solve it, and check by putting the number back. Then ask them to solve it without the equation.",
   "گھر میں کسی کے لیے عدد کی پہیلی بنائیں: 'میں ایک عدد سوچتا ہوں، اسے دگنا کر کے 5 جمع کرتا ہوں تو 17 آتا ہے۔' اسے مساوات میں لکھیں، حل کریں، اور عدد واپس رکھ کر جانچیں۔ پھر انھیں مساوات کے بغیر حل کرنے کو کہیں۔")},
 notes=["Covers picking out linear equations (q1, q2), solving one- and two-step equations with whole numbers, decimals and fractions (q3, q4, q6, q7), checking a solution (q5), building an equation (q8), finding a mistake (q9), and word problems about ages, consecutive numbers, sharing in a ratio and cricket scores (q10 to q13).",
        "Each wrong answer is a real mistake: the wrong inverse, stopping after the first step, dividing before taking away, brackets added by habit, and giving another quantity from the story (Ali's age, the middle number, Hina's share).",
        "Urdu terms to check: خطی مساوات (linear equation), حل (solution), جانچ (check), نسبت (ratio), رنز (runs). لگاتار اعداد (consecutive numbers) is new and should be confirmed by a teacher; the lesson also writes the sum as مجموعہ."],
 minutes=22,
)

figs.attach(lesson, {"q4_two_step": FIG4})
write(lesson)

"""Practice set for Exercise 3.3 of the book: simplify expressions with
BODMAS, nested brackets and a vinculum (bar), expressions with decimals,
fractions and mixed numbers, and multi-step word problems. The questions are
new; only the kinds of question follow the book."""
from fractions import Fraction as F
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    SM_ORDER, SM_BRACKETS, SM_FRACTIONS_DECIMALS, SM_WORD_PROBLEMS)

SKILL = EX_SKILL["3.3"]


def bar(text):
    """Draw a bar (vinculum) over a piece of text."""
    return "".join(c + "̅" if c != " " else c for c in text)


# q1, q2: operation order
Q1 = 8 + 6 * 3
assert Q1 == 26 and (8 + 6) * 3 == 42
Q2 = 30 - 12 // 3
assert Q2 == 26 and (30 - 12) // 3 == 6
# q3: brackets first
Q3 = 7 * (9 - 4) + 3
assert Q3 == 38 and 7 * 9 - 4 + 3 == 62
# q4: nested brackets, inside out
Q4 = 50 - (12 + (8 - 3))
assert Q4 == 33 and 50 - 12 + (8 - 3) == 43
# q5: vinculum 30 / (3 + 2) + 4
Q5 = 30 // (3 + 2) + 4
assert Q5 == 10 and 30 // 3 + 2 + 4 == 16 and 30 % 5 == 0
# q6: 100 - [30 + {20 - (5 + 3)}]
Q6 = 100 - (30 + (20 - (5 + 3)))
assert Q6 == 58 and 20 - (5 + 3) == 12 and 100 - 30 + 12 == 82
# q7: decimals 2.5 + 1.5 x 4
Q7 = F(5, 2) + F(3, 2) * 4
assert Q7 == F(17, 2) and float(Q7) == 8.5 and (F(5, 2) + F(3, 2)) * 4 == 16
# q8: decimals (7.2 - 3.6) / 0.9
Q8 = (F(72, 10) - F(36, 10)) / F(9, 10)
assert Q8 == 4 and F(72, 10) - F(36, 10) / F(9, 10) == F(16, 5) and float(F(16, 5)) == 3.2
# q9: fractions 1/2 + 1/4 x 2
Q9 = F(1, 2) + F(1, 4) * 2
assert Q9 == 1 and (F(1, 2) + F(1, 4)) * 2 == F(3, 2)
# q10: mixed numbers 2 1/2 x (1 1/5 + 4/5)
Q10 = F(5, 2) * (F(6, 5) + F(4, 5))
assert Q10 == 5 and F(5, 2) * F(6, 5) + F(4, 5) == F(19, 5) and float(F(19, 5)) == 3.8
# q11: change from Rs 200
Q11 = 200 - (3 * 45 + 2 * 18)
assert Q11 == 29 and 3 * 45 == 135 and 2 * 18 == 36 and 200 - 135 == 65
# q12: rope 12.5 m
Q12 = (F(25, 2) - 3 * F(5, 2)) / 2
assert Q12 == F(5, 2) and float(Q12) == 2.5 and F(25, 2) - 3 * F(5, 2) == 5
# q13 (find error): 5 + 3 x 4
assert 5 + 3 * 4 == 17 and (5 + 3) * 4 == 32
# bank and review
QB_REC = 9 + 4 * 2
assert QB_REC == 17 and (9 + 4) * 2 == 26
QB_APP = 48 // (4 + 2) - 3
assert 48 % 6 == 0 and QB_APP == 5 and 48 // 4 + 2 - 3 == 11
assert 20 - (6 - 2) == 16 and 20 - 6 - 2 == 12 and 20 - 6 + 2 == 16
R_REC = 18 - 6 // 2
assert R_REC == 15 and (18 - 6) // 2 == 6
R_APP = F(24, 10) * (5 - F(35, 10))
assert R_APP == F(18, 5) and float(R_APP) == 3.6 and F(24, 10) * 5 - F(35, 10) == F(85, 10)

lesson = practice_lesson(
 "3.3", script="exercise_3_3.py",
 title=T("Exercise 3.3 practice: BODMAS and brackets", "مشق 3.3 کی پریکٹس: بوڈ ماس اور بریکٹ"),
 outcome="Apply the BODMAS rule to simplify expressions with brackets, a bar, decimals and fractions, and solve multi-step word problems.",
 prerequisites=[SM_ORDER, SM_BRACKETS, SM_FRACTIONS_DECIMALS, SM_WORD_PROBLEMS],
 misconceptions=[
   {"id": "left_to_right", "description": "Works strictly left to right and ignores BODMAS: 8 + 6 × 3 = 42."},
   {"id": "skips_brackets", "description": "Ignores the brackets, or does the operation next to them before the brackets."},
   {"id": "bracket_sign", "description": "Removes a bracket after a minus sign without changing the signs inside."},
   {"id": "bar_ignored", "description": "Does not treat the terms under a bar as one bracket."},
   {"id": "decimal_order", "description": "Adds before multiplying in an expression with decimals or fractions."},
   {"id": "stops_early", "description": "Finds a middle result but does not finish the problem."},
 ],
 steps=[
   practice_intro("3.3",
     "Here you simplify expressions with brackets, a bar, decimals and fractions using the BODMAS rule, and solve word problems with several steps.",
     "اس میں آپ بوڈ ماس اصول سے بریکٹ، بار، اعشاریہ اور کسر والی عبارتیں سادہ کریں گے، اور کئی مراحل والے سوال حل کریں گے۔",
     "Exercise 3.3 is about BODMAS. Ready?",
     "مشق 3.3 بوڈ ماس کے بارے میں ہے۔ تیار؟"),
   nq("q1_order", ("Simplify 8 + 6 × 3.", "8 + 6 × 3 سادہ کریں۔"), Q1,
      ("Multiplication comes before addition.", "ضرب جمع سے پہلے آتی ہے۔"),
      ("Right! 6 × 3 = 18, then 8 + 18 = 26.", "درست! 6 × 3 = 18، پھر 8 + 18 = 26"),
      ("Multiply first: 6 × 3 = 18. Then add: 8 + 18 = 26.", "پہلے ضرب: 6 × 3 = 18۔ پھر جمع: 8 + 18 = 26"),
      [(42, "That works left to right: 8 + 6 = 14, then × 3. BODMAS says multiply first: 26.", "یہ بائیں سے دائیں چلتا ہے: 8 + 6 = 14، پھر × 3۔ بوڈ ماس کہتا ہے پہلے ضرب: 26", "left_to_right")],
      qtype="recall"),
   nq("q2_order", ("Simplify 30 − 12 ÷ 3.", "30 − 12 ÷ 3 سادہ کریں۔"), Q2,
      ("Division comes before subtraction.", "تقسیم تفریق سے پہلے آتی ہے۔"),
      ("Right! 12 ÷ 3 = 4, then 30 − 4 = 26.", "درست! 12 ÷ 3 = 4، پھر 30 − 4 = 26"),
      ("Divide first: 12 ÷ 3 = 4. Then subtract: 30 − 4 = 26.", "پہلے تقسیم: 12 ÷ 3 = 4۔ پھر تفریق: 30 − 4 = 26"),
      [(6, "That subtracts first: 30 − 12 = 18, then ÷ 3. Divide first: 26.", "یہ پہلے تفریق کرتا ہے: 30 − 12 = 18، پھر ÷ 3۔ پہلے تقسیم کریں: 26", "left_to_right")],
      qtype="recall"),
   {"id": "s_bodmas", "type": "explain",
    "character": say("thinking", "Brackets first, then of, division, multiplication, addition, subtraction.", "پہلے بریکٹ، پھر of، تقسیم، ضرب، جمع، تفریق۔"),
    "text": T(f"BODMAS gives the order: Brackets, Of, Division, Multiplication, Addition, Subtraction. Brackets are removed from the inside out: the bar first, then ( ), then {{ }}, then [ ]. A bar over some terms, like {bar('3 + 2')}, works as a bracket round them. A minus sign in front of a bracket changes every sign inside when the bracket is removed. With decimals and fractions the same order is used.",
              f"بوڈ ماس ترتیب بتاتا ہے: بریکٹ، of، تقسیم، ضرب، جمع، تفریق۔ بریکٹ اندر سے باہر کھولے جاتے ہیں: پہلے بار، پھر ( )، پھر {{ }}، پھر [ ]۔ کچھ اجزا کے اوپر بار، جیسے {bar('3 + 2')}، ان کے گرد بریکٹ کی طرح کام کرتا ہے۔ بریکٹ کے سامنے منفی علامت ہو تو بریکٹ ہٹاتے وقت اندر کی ہر علامت بدل جاتی ہے۔ اعشاریہ اور کسر کے ساتھ بھی یہی ترتیب چلتی ہے۔")},
   nq("q3_bracket", ("Simplify 7 × (9 − 4) + 3.", "7 × (9 − 4) + 3 سادہ کریں۔"), Q3,
      ("Work out the bracket first: 9 − 4.", "پہلے بریکٹ نکالیں: 9 − 4"),
      ("Right! 7 × 5 + 3 = 35 + 3 = 38.", "درست! 7 × 5 + 3 = 35 + 3 = 38"),
      ("Bracket: 9 − 4 = 5. Multiply: 7 × 5 = 35. Add: 35 + 3 = 38.", "بریکٹ: 9 − 4 = 5۔ ضرب: 7 × 5 = 35۔ جمع: 35 + 3 = 38"),
      [(62, "That multiplies 7 × 9 and ignores the bracket. Do 9 − 4 = 5 first: 38.", "یہ 7 × 9 کرتا ہے اور بریکٹ نظر انداز کرتا ہے۔ پہلے 9 − 4 = 5 کریں: 38", "skips_brackets")]),
   nq("q4_nested", ("Simplify 50 − {12 + (8 − 3)}.", "50 − {12 + (8 − 3)} سادہ کریں۔"), Q4,
      ("Start with the inner ( ): 8 − 3. Then the { }.", "اندر کے ( ) سے شروع کریں: 8 − 3۔ پھر { }"),
      ("Right! (8 − 3) = 5, {12 + 5} = 17, and 50 − 17 = 33.", "درست! (8 − 3) = 5، {12 + 5} = 17، اور 50 − 17 = 33"),
      ("Inside out: 8 − 3 = 5, then 12 + 5 = 17, then 50 − 17 = 33.", "اندر سے باہر: 8 − 3 = 5، پھر 12 + 5 = 17، پھر 50 − 17 = 33"),
      [(43, "The curly bracket still has to be worked out as a whole: 12 + 5 = 17, and 50 − 17 = 33.", "گھنگھریالے بریکٹ کو بھی پورا حل کرنا ہے: 12 + 5 = 17، اور 50 − 17 = 33", "skips_brackets")]),
   nq("q5_bar", (f"Simplify 30 ÷ {bar('3 + 2')} + 4. (The bar covers 3 + 2.)", f"30 ÷ {bar('3 + 2')} + 4 سادہ کریں۔ (بار 3 + 2 کے اوپر ہے۔)"), Q5,
      ("The bar works like a bracket: work out 3 + 2 first.", "بار بریکٹ کی طرح کام کرتا ہے: پہلے 3 + 2 نکالیں۔"),
      ("Right! 30 ÷ 5 = 6, then 6 + 4 = 10.", "درست! 30 ÷ 5 = 6، پھر 6 + 4 = 10"),
      ("Bar: 3 + 2 = 5. Divide: 30 ÷ 5 = 6. Add: 6 + 4 = 10.", "بار: 3 + 2 = 5۔ تقسیم: 30 ÷ 5 = 6۔ جمع: 6 + 4 = 10"),
      [(16, "That divides 30 by 3 only. The bar groups 3 + 2, so divide by 5: 10.", "یہ 30 کو صرف 3 سے تقسیم کرتا ہے۔ بار 3 + 2 کو اکٹھا کرتا ہے، اس لیے 5 سے تقسیم کریں: 10", "bar_ignored")]),
   nq("q6_three_brackets", ("Simplify 100 − [30 + {20 − (5 + 3)}].", "100 − [30 + {20 − (5 + 3)}] سادہ کریں۔"), Q6,
      ("Innermost first: (5 + 3). Then { }, then [ ].", "سب سے اندر پہلے: (5 + 3)۔ پھر { }، پھر [ ]"),
      ("Right! (5 + 3) = 8, {20 − 8} = 12, [30 + 12] = 42, and 100 − 42 = 58.", "درست! (5 + 3) = 8، {20 − 8} = 12، [30 + 12] = 42، اور 100 − 42 = 58"),
      ("Inside out: 8, then 12, then 42. Finally 100 − 42 = 58.", "اندر سے باہر: 8، پھر 12، پھر 42۔ آخر میں 100 − 42 = 58"),
      [(82, "A minus sign before [ ] applies to the whole bracket: 100 − 42, not 100 − 30 + 12. The answer is 58.", "[ ] سے پہلے کی منفی علامت پورے بریکٹ پر لگتی ہے: 100 − 42، نہ کہ 100 − 30 + 12۔ جواب 58 ہے۔", "bracket_sign")]),
   nq("q7_decimal", ("Simplify 2.5 + 1.5 × 4.", "2.5 + 1.5 × 4 سادہ کریں۔"), Q7,
      ("Multiply first: 1.5 × 4.", "پہلے ضرب: 1.5 × 4"),
      ("Right! 1.5 × 4 = 6, then 2.5 + 6 = 8.5.", "درست! 1.5 × 4 = 6، پھر 2.5 + 6 = 8.5"),
      ("1.5 × 4 = 6, and 2.5 + 6 = 8.5.", "1.5 × 4 = 6، اور 2.5 + 6 = 8.5"),
      [(16, "That adds 2.5 + 1.5 first. BODMAS says multiply first: 8.5.", "یہ پہلے 2.5 + 1.5 کرتا ہے۔ بوڈ ماس کہتا ہے پہلے ضرب: 8.5", "decimal_order")]),
   nq("q8_decimal_bracket", ("Simplify (7.2 − 3.6) ÷ 0.9.", "(7.2 − 3.6) ÷ 0.9 سادہ کریں۔"), Q8,
      ("Bracket first: 7.2 − 3.6. Then divide by 0.9.", "پہلے بریکٹ: 7.2 − 3.6۔ پھر 0.9 سے تقسیم کریں۔"),
      ("Right! 3.6 ÷ 0.9 = 4.", "درست! 3.6 ÷ 0.9 = 4"),
      ("Bracket: 7.2 − 3.6 = 3.6. Divide: 3.6 ÷ 0.9 = 4.", "بریکٹ: 7.2 − 3.6 = 3.6۔ تقسیم: 3.6 ÷ 0.9 = 4"),
      [(3.2, "That divides 3.6 by 0.9 first and ignores the bracket: 7.2 − 4 = 3.2. Bracket first: 4.", "یہ بریکٹ نظر انداز کر کے پہلے 3.6 ÷ 0.9 کرتا ہے: 7.2 − 4 = 3.2۔ پہلے بریکٹ: 4", "skips_brackets")]),
   nq("q9_fraction", ("Simplify ½ + ¼ × 2.", "½ + ¼ × 2 سادہ کریں۔"), Q9,
      ("Multiply first: ¼ × 2 = ½.", "پہلے ضرب: ¼ × 2 = ½"),
      ("Right! ½ + ½ = 1.", "درست! ½ + ½ = 1"),
      ("¼ × 2 = ½, and ½ + ½ = 1.", "¼ × 2 = ½، اور ½ + ½ = 1"),
      [(1.5, "That adds ½ + ¼ = ¾ first and then doubles it. Multiply first: 1.", "یہ پہلے ½ + ¼ = ¾ کر کے دگنا کرتا ہے۔ پہلے ضرب کریں: 1", "decimal_order")]),
   nq("q10_mixed", ("Simplify 2½ × (1⅕ + ⅘).", "2½ × (1⅕ + ⅘) سادہ کریں۔"), Q10,
      ("Bracket first: 1⅕ + ⅘ = 6/5 + 4/5.", "پہلے بریکٹ: 1⅕ + ⅘ = 6/5 + 4/5"),
      ("Right! The bracket is 2, and 2½ × 2 = 5.", "درست! بریکٹ 2 ہے، اور 2½ × 2 = 5"),
      ("Bracket: 6/5 + 4/5 = 10/5 = 2. Then 2½ × 2 = 5.", "بریکٹ: 6/5 + 4/5 = 10/5 = 2۔ پھر 2½ × 2 = 5"),
      [(3.8, "That multiplies 2½ × 1⅕ = 3 and then adds ⅘. The bracket comes first: 5.", "یہ 2½ × 1⅕ = 3 کر کے پھر ⅘ جمع کرتا ہے۔ بریکٹ پہلے آتا ہے: 5", "skips_brackets")]),
   nq("q11_shop", ("Bilal buys 3 notebooks at Rs 45 each and 2 pens at Rs 18 each. He pays with a Rs 200 note. How many rupees does he get back? (Write it as 200 − (3 × 45 + 2 × 18).)", "بلال 45 روپے والی 3 کاپیاں اور 18 روپے والے 2 قلم خریدتا ہے۔ وہ 200 روپے کا نوٹ دیتا ہے۔ اسے کتنے روپے واپس ملتے ہیں؟ (200 − (3 × 45 + 2 × 18) لکھیں۔)"), Q11,
      ("Inside the bracket: multiply, then add. Subtract from 200 last.", "بریکٹ کے اندر: ضرب، پھر جمع۔ آخر میں 200 سے گھٹائیں۔"),
      ("Right! 135 + 36 = 171, and 200 − 171 = 29.", "درست! 135 + 36 = 171، اور 200 − 171 = 29"),
      ("Notebooks 3 × 45 = 135, pens 2 × 18 = 36, total 171, change 200 − 171 = Rs 29.", "کاپیاں 3 × 45 = 135، قلم 2 × 18 = 36، کل 171، واپسی 200 − 171 = 29 روپے۔"),
      [(65, "That takes away the notebooks only. The pens cost money too: 200 − 171 = 29.", "یہ صرف کاپیاں گھٹاتا ہے۔ قلموں کی بھی قیمت ہے: 200 − 171 = 29", "stops_early")]),
   nq("q12_rope", ("A rope is 12.5 m long. Three pieces of 2.5 m each are cut from it, and the rest is shared equally by 2 children. How many metres does each child get? (Write it as (12.5 − 3 × 2.5) ÷ 2.)", "ایک رسی 12.5 میٹر لمبی ہے۔ اس سے 2.5 میٹر کے تین ٹکڑے کاٹے جاتے ہیں، اور باقی 2 بچوں میں برابر بانٹی جاتی ہے۔ ہر بچے کو کتنے میٹر ملتے ہیں؟ ((12.5 − 3 × 2.5) ÷ 2 لکھیں۔)"), Q12,
      ("In the bracket multiply first: 3 × 2.5. Then subtract, then divide by 2.", "بریکٹ میں پہلے ضرب: 3 × 2.5۔ پھر تفریق، پھر 2 سے تقسیم۔"),
      ("Right! 12.5 − 7.5 = 5, and 5 ÷ 2 = 2.5 m.", "درست! 12.5 − 7.5 = 5، اور 5 ÷ 2 = 2.5 میٹر"),
      ("3 × 2.5 = 7.5, 12.5 − 7.5 = 5 m left, and 5 ÷ 2 = 2.5 m each.", "3 × 2.5 = 7.5، 12.5 − 7.5 = 5 میٹر باقی، اور 5 ÷ 2 = 2.5 میٹر فی بچہ۔"),
      [(5, "That is the length left. It is shared by 2 children: 2.5 m each.", "یہ باقی لمبائی ہے۔ یہ 2 بچوں میں بانٹی جاتی ہے: ہر ایک کو 2.5 میٹر", "stops_early")]),
   ch("q13_find_error", ("Ahmed simplifies 5 + 3 × 4 like this: 5 + 3 = 8, then 8 × 4 = 32. What went wrong?", "احمد 5 + 3 × 4 یوں سادہ کرتا ہے: 5 + 3 = 8، پھر 8 × 4 = 32۔ کیا غلطی ہوئی؟"),
      ("He added before multiplying. By BODMAS 3 × 4 = 12 first, then 5 + 12 = 17.", "اس نے ضرب سے پہلے جمع کر دی۔ بوڈ ماس کے مطابق پہلے 3 × 4 = 12، پھر 5 + 12 = 17", "Yes! Multiplication comes before addition.", "جی ہاں! ضرب جمع سے پہلے آتی ہے۔"),
      [("Nothing. Working left to right is correct.", "کوئی غلطی نہیں۔ بائیں سے دائیں چلنا درست ہے۔", "Not here: BODMAS puts multiplication before addition.", "یہاں نہیں: بوڈ ماس ضرب کو جمع سے پہلے رکھتا ہے۔", "left_to_right"),
       ("He should have put a bracket round 5 + 3.", "اسے 5 + 3 کے گرد بریکٹ لگانا چاہیے تھا۔", "The question has no bracket. Without one, multiplication goes first.", "سوال میں بریکٹ نہیں۔ اس کے بغیر ضرب پہلے ہوتی ہے۔", "skips_brackets")],
      0, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You used BODMAS.", "شاباش! آپ نے بوڈ ماس استعمال کیا۔"),
    "text": T("BODMAS: Brackets, Of, Division, Multiplication, Addition, Subtraction. Remove brackets from the inside out, and treat a bar as a bracket. The same order works for decimals, fractions and mixed numbers. In a word problem, write the whole calculation with brackets, then simplify it.",
              "بوڈ ماس: بریکٹ، of، تقسیم، ضرب، جمع، تفریق۔ بریکٹ اندر سے باہر ہٹائیں، اور بار کو بریکٹ سمجھیں۔ یہی ترتیب اعشاریہ، کسر اور مخلوط اعداد کے ساتھ بھی چلتی ہے۔ لفظی سوال میں پورا حساب بریکٹ کے ساتھ لکھیں، پھر سادہ کریں۔"),
    "points": [T("Multiplication and division come before addition and subtraction.", "ضرب اور تقسیم جمع اور تفریق سے پہلے آتی ہیں۔"),
               T("A minus sign before a bracket applies to everything inside it.", "بریکٹ سے پہلے کی منفی علامت اس کے اندر ہر چیز پر لگتی ہے۔")]},
 ],
 bank=[
   {"id": "qb_order", "type": "recall", "step": nq("qb_order", ("Simplify 9 + 4 × 2.", "9 + 4 × 2 سادہ کریں۔"), QB_REC,
      ("Multiply first.", "پہلے ضرب۔"),
      ("Right! 9 + 8 = 17.", "درست! 9 + 8 = 17"), ("4 × 2 = 8, then 9 + 8 = 17.", "4 × 2 = 8، پھر 9 + 8 = 17"),
      [(26, "That adds first: 13 × 2. Multiply first: 17.", "یہ پہلے جمع کرتا ہے: 13 × 2۔ پہلے ضرب: 17", "left_to_right")], qtype=None)},
   {"id": "qb_bracket", "type": "apply", "step": nq("qb_bracket", ("Simplify 48 ÷ (4 + 2) − 3.", "48 ÷ (4 + 2) − 3 سادہ کریں۔"), QB_APP,
      ("Bracket first: 4 + 2. Then divide. Subtract last.", "پہلے بریکٹ: 4 + 2۔ پھر تقسیم۔ آخر میں تفریق۔"),
      ("Right! 48 ÷ 6 = 8, and 8 − 3 = 5.", "درست! 48 ÷ 6 = 8، اور 8 − 3 = 5"), ("Bracket 6, divide 8, subtract 3: 5.", "بریکٹ 6، تقسیم 8، تفریق 3: 5"),
      [(11, "That divides by 4 only and ignores the bracket: 5 is the answer.", "یہ صرف 4 سے تقسیم کرتا ہے اور بریکٹ نظر انداز کرتا ہے: جواب 5 ہے۔", "skips_brackets")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Sana simplifies 20 − (6 − 2) as 20 − 6 − 2 = 12. What went wrong?", "ثنا 20 − (6 − 2) کو 20 − 6 − 2 = 12 لکھ کر حل کرتی ہے۔ کیا غلطی ہوئی؟"),
      ("She did not work out the bracket first. (6 − 2) = 4, and 20 − 4 = 16.", "اس نے پہلے بریکٹ حل نہیں کیا۔ (6 − 2) = 4، اور 20 − 4 = 16", "Yes! Bracket first: 16. (Removing the bracket instead gives 20 − 6 + 2 = 16.)", "جی ہاں! پہلے بریکٹ: 16۔ (بریکٹ ہٹانے سے 20 − 6 + 2 = 16 ملتا ہے۔)"),
      [("Nothing. 12 is correct.", "کوئی غلطی نہیں۔ 12 درست ہے۔", "A minus before a bracket changes the signs inside: the answer is 16.", "بریکٹ سے پہلے منفی اندر کی علامتیں بدل دیتا ہے: جواب 16 ہے۔", "bracket_sign"),
       ("She should have added 20 and 6.", "اسے 20 اور 6 جمع کرنا چاہیے تھے۔", "Nothing in the question says to add 20 and 6.", "سوال میں 20 اور 6 جمع کرنے کا نہیں کہا۔")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_order", "type": "recall", "step": nq("r_order", ("Simplify 18 − 6 ÷ 2.", "18 − 6 ÷ 2 سادہ کریں۔"), R_REC,
      ("Divide first.", "پہلے تقسیم۔"),
      ("Right! 18 − 3 = 15.", "درست! 18 − 3 = 15"), ("6 ÷ 2 = 3, then 18 − 3 = 15.", "6 ÷ 2 = 3، پھر 18 − 3 = 15"),
      [(6, "That subtracts first. Divide first: 15.", "یہ پہلے تفریق کرتا ہے۔ پہلے تقسیم: 15", "left_to_right")], qtype=None)},
   {"id": "r_decimal", "type": "apply", "step": nq("r_decimal", ("Simplify 2.4 × (5 − 3.5).", "2.4 × (5 − 3.5) سادہ کریں۔"), R_APP,
      ("Bracket first: 5 − 3.5.", "پہلے بریکٹ: 5 − 3.5"),
      ("Right! 2.4 × 1.5 = 3.6.", "درست! 2.4 × 1.5 = 3.6"), ("5 − 3.5 = 1.5 and 2.4 × 1.5 = 3.6.", "5 − 3.5 = 1.5 اور 2.4 × 1.5 = 3.6"),
      [(8.5, "That multiplies 2.4 × 5 first and ignores the bracket. Bracket first: 3.6.", "یہ بریکٹ نظر انداز کر کے پہلے 2.4 × 5 کرتا ہے۔ پہلے بریکٹ: 3.6", "skips_brackets")], qtype=None)},
 ],
 glossary=[T("BODMAS", "بوڈ ماس"), T("Bracket", "بریکٹ"), T("Bar (vinculum)", "بار (خط)"), T("Simplify", "سادہ کرنا"), T("Mixed number", "مخلوط عدد")],
 flashcards=[
   {"id": "f_bodmas", "front": T("What does BODMAS stand for?", "بوڈ ماس کا کیا مطلب ہے؟"),
    "back": T("Brackets, Of, Division, Multiplication, Addition, Subtraction.", "بریکٹ، of، تقسیم، ضرب، جمع، تفریق۔")},
   {"id": "f_inside", "front": T("In which order are brackets removed?", "بریکٹ کس ترتیب سے ہٹاتے ہیں؟"),
    "back": T("Inside out: bar, then ( ), then { }, then [ ].", "اندر سے باہر: بار، پھر ( )، پھر { }، پھر [ ]۔")},
 ],
 home_task={"id": "h_shop", "text": T(
   "Pick three things from a shop and write their prices. Make up a purchase with different numbers of each, pay with a bigger note, and write the change as one expression with brackets. Simplify it with BODMAS.",
   "دکان سے تین چیزیں چنیں اور ان کی قیمتیں لکھیں۔ ہر ایک کی مختلف تعداد کی خریداری بنائیں، بڑے نوٹ سے ادائیگی کریں، اور واپسی کو بریکٹ والی ایک عبارت کے طور پر لکھیں۔ بوڈ ماس سے سادہ کریں۔")},
 notes=["Covers operation order (q1, q2, q13), single and nested brackets (q3, q4, q6), the bar or vinculum (q5), decimals (q7, q8), fractions and mixed numbers (q9, q10) and multi-step money and measurement problems (q11, q12).",
        "The bar is drawn with a combining overline over each character. Each wrong answer is a real mistake: working left to right, skipping the brackets, ignoring the bar, or stopping before the last step.",
        "Urdu terms to check: بوڈ ماس (BODMAS), بار / خط (bar, vinculum), سادہ کرنا (simplify), مخلوط عدد (mixed number)."],
 minutes=20,
)

write(lesson)

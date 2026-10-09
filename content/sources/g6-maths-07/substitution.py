from common import (T, opt, say, wrong, number_question, text_question, write, value,
                    REF, REVIEW, ALG_VARIABLES, ALG_SUBSTITUTION)

SKILL = ALG_SUBSTITUTION

# s4
S4 = value("x + 9", x=6)
assert S4 == 15
# s5: 3n + 2, n = 4; wrong: 34 + 2 (digit), 3 × (4 + 2) (adds first)
S5 = value("3n + 2", n=4)
assert S5 == 14 and 34 + 2 == 36 and 3 * (4 + 2) == 18
# s6: 5a − 3, a = 2
S6 = value("5a - 3", a=2)
assert S6 == 7 and 52 - 3 == 49 and 5 * (2 - 3) == -5
# s7: 2a + b, a = 3, b = 4
S7 = value("2a + b", a=3, b=4)
assert S7 == 10 and 2 * (3 + 4) == 14 and 23 + 4 == 27
# s8: perimeter of a square 4s, s = 9
S8 = value("4s", s=9)
assert S8 == 36 and 9 + 4 == 13
# s9: 2y with y = 5
assert value("2y", y=5) == 10
# s10: 3n, n = 4
assert value("3n", n=4) == 12
# s11: 10 − 2k, k = 3
S11 = value("10 - 2k", k=3)
assert S11 == 4 and (10 - 2) * 3 == 24
# question bank
QB = value("6 + 2c", c=7)
assert QB == 20 and (6 + 2) * 7 == 56
assert value("4m", m=5) == 20
assert value("2a + 1", a=3) == 7 and 2 * (3 + 1) == 8
# review
R1 = value("4p + 1", p=5)
assert R1 == 21 and 45 + 1 == 46
R2 = value("a*b", a=3, b=6)
assert R2 == 18 and 3 + 6 == 9


lesson = {
 "id": "g6-maths-07-substitution",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the value of an algebraic expression by putting numbers in place of the letters.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Putting numbers in (substitution)", "قیمت رکھنا"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": ALG_VARIABLES}],
 "misconceptions": [
   {"id": "letter_is_digit", "description": "Puts the number next to the digit: 3n with n = 4 becomes 34, not 3 × 4."},
   {"id": "adds_first", "description": "Adds or subtracts before multiplying: 3n + 2 with n = 4 becomes 3 × 6 = 18."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_recall", "type": "recall", "step": {
     "id": "qb_recall", "type": "choice",
     "prompt": T("If m = 5, what is 4m?", "اگر m = 5 ہو تو 4m کتنا ہے؟"),
     "options": [
       opt("twenty", "20", "20", True, "Yes! 4m means 4 × m = 4 × 5 = 20.", "جی ہاں! 4m یعنی 4 × m = 4 × 5 = 20"),
       opt("fortyfive", "45", "45", False, "m is not a digit. 4m means 4 × 5 = 20.", "m ہندسہ نہیں۔ 4m یعنی 4 × 5 = 20", "letter_is_digit"),
       opt("nine", "9", "9", False, "That is 4 + 5. 4m means 4 × 5 = 20.", "یہ 4 + 5 ہے۔ 4m یعنی 4 × 5 = 20"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find the value of 6 + 2c when c = 7.", "جب c = 7 ہو تو 6 + 2c کی قیمت معلوم کریں۔"),
     QB,
     T("Work out 2c first: 2 × 7.", "پہلے 2c نکالیں: 2 × 7"),
     T("Right! 6 + 14 = 20.", "درست! 6 + 14 = 20"),
     T("2c = 2 × 7 = 14, then 6 + 14 = 20.", "2c = 2 × 7 = 14، پھر 6 + 14 = 20"),
     common_wrong=[wrong(56, "Multiply before adding: 2 × 7 = 14, then 6 + 14 = 20.", "جمع سے پہلے ضرب: 2 × 7 = 14، پھر 6 + 14 = 20", "adds_first"),
                   wrong(33, "c is not a digit: 2c = 2 × 7 = 14, so 6 + 14 = 20.", "c ہندسہ نہیں: 2c = 2 × 7 = 14، تو 6 + 14 = 20", "letter_is_digit")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Asma says 2a + 1 = 8 when a = 3, because 3 + 1 = 4 and 2 × 4 = 8. What went wrong?", "اسماء کہتی ہے a = 3 پر 2a + 1 = 8، کیونکہ 3 + 1 = 4 اور 2 × 4 = 8۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("order", "She added first. Multiply first: 2 × 3 = 6, then 6 + 1 = 7.", "اس نے پہلے جمع کیا۔ پہلے ضرب: 2 × 3 = 6، پھر 6 + 1 = 7", True,
           "Yes! 2a means 2 × a, worked out before the + 1.", "جی ہاں! 2a یعنی 2 × a، جو + 1 سے پہلے نکالتے ہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "2a + 1 means (2 × a) + 1 = 6 + 1 = 7.", "2a + 1 یعنی (2 × a) + 1 = 6 + 1 = 7", "adds_first"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_sub", "front": T("How do you substitute?", "قیمت کیسے رکھتے ہیں؟"),
    "back": T("Put the number in place of the letter, then work it out. 3n + 2 with n = 4: 3 × 4 + 2 = 14.", "حرف کی جگہ عدد رکھیں، پھر حل کریں۔ n = 4 پر 3n + 2: 3 × 4 + 2 = 14")},
   {"id": "f_order", "front": T("3n + 2: which first?", "3n + 2: پہلے کیا؟"),
    "back": T("Multiply first (3 × n), then add 2.", "پہلے ضرب (3 × n)، پھر 2 جمع۔")},
 ],
 "home_tasks": [{"id": "h_fare", "text": T(
   "A rickshaw charges 50 rupees plus 20 rupees for each km: 50 + 20k. Work out the fare for 2 km, 5 km and 10 km. Which trips around your home would cost what?",
   "رکشہ 50 روپے اور ہر کلومیٹر کے 20 روپے لیتا ہے: 50 + 20k۔ 2، 5 اور 10 کلومیٹر کا کرایہ نکالیں۔ آپ کے گھر کے آس پاس کون سا سفر کتنے کا ہوگا؟")}],
 "glossary": [T("Substitute", "قیمت رکھنا"), T("Value of an expression", "عبارت کی قیمت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "A square's perimeter is 4s, where s is its side. What if the side is 9 cm? Let's find out!",
                     "مربع کا احاطہ 4s ہے، جہاں s اس کا ضلع ہے۔ اگر ضلع 9 سینٹی میٹر ہو تو؟ آئیں معلوم کریں!"),
    "text": T("When we know the number a letter stands for, we can find the value of the expression. First, a quick check.", "جب معلوم ہو کہ حرف کس عدد کی جگہ ہے تو ہم عبارت کی قیمت نکال سکتے ہیں۔ پہلے ایک چھوٹا سا سوال۔")},
   text_question(
     "s2_foundation",
     T("Write an expression for '7 more than t'.", "'t سے 7 زیادہ' کی عبارت لکھیں۔"),
     "t + 7",
     T("More than means add.", "زیادہ کا مطلب جمع۔"),
     T("Right! t + 7.", "درست! t + 7"),
     T("7 more than t is t + 7.", "t سے 7 زیادہ یعنی t + 7"),
     accept=["7 + t"],
     common_wrong=[wrong("7t", "7t means 7 × t. More than means add: t + 7.", "7t یعنی 7 × t۔ زیادہ کا مطلب جمع: t + 7")],
     qtype="recall", skill=ALG_VARIABLES),
   {"id": "s3_how", "type": "explain",
    "character": say("happy", "Swap the letter for its number, then work it out!", "حرف کی جگہ اس کا عدد رکھیں، پھر حل کریں!"),
    "text": T("This is called substitution. Remember 3n means 3 × n. So when n = 4, 3n + 2 = 3 × 4 + 2 = 12 + 2 = 14. Multiply first, then add or take away.",
              "اسے قیمت رکھنا کہتے ہیں۔ یاد رکھیں 3n یعنی 3 × n۔ تو جب n = 4 ہو، 3n + 2 = 3 × 4 + 2 = 12 + 2 = 14۔ پہلے ضرب، پھر جمع یا تفریق۔")},
   number_question(
     "s4_add",
     T("Find the value of x + 9 when x = 6.", "جب x = 6 ہو تو x + 9 کی قیمت معلوم کریں۔"),
     S4,
     T("Put 6 in place of x.", "x کی جگہ 6 رکھیں۔"),
     T("Right! 6 + 9 = 15.", "درست! 6 + 9 = 15"),
     T("x + 9 = 6 + 9 = 15.", "x + 9 = 6 + 9 = 15"),
     common_wrong=[wrong(54, "That is 6 × 9. x + 9 means add: 15.", "یہ 6 × 9 ہے۔ x + 9 میں جمع: 15")]),
   number_question(
     "s5_times_add",
     T("Find the value of 3n + 2 when n = 4.", "جب n = 4 ہو تو 3n + 2 کی قیمت معلوم کریں۔"),
     S5,
     T("3n means 3 × 4. Do that first.", "3n یعنی 3 × 4۔ پہلے یہ کریں۔"),
     T("Right! 12 + 2 = 14.", "درست! 12 + 2 = 14"),
     T("3 × 4 = 12, then 12 + 2 = 14.", "3 × 4 = 12، پھر 12 + 2 = 14"),
     common_wrong=[wrong(36, "3n is 3 × n, not 34. 3 × 4 + 2 = 14.", "3n یعنی 3 × n، نہ کہ 34۔ 3 × 4 + 2 = 14", "letter_is_digit"),
                   wrong(18, "Multiply before adding: 3 × 4 = 12, then + 2 = 14.", "جمع سے پہلے ضرب: 3 × 4 = 12، پھر + 2 = 14", "adds_first")]),
   number_question(
     "s6_times_subtract",
     T("Find the value of 5a − 3 when a = 2.", "جب a = 2 ہو تو 5a − 3 کی قیمت معلوم کریں۔"),
     S6,
     T("5 × 2 first, then take away 3.", "پہلے 5 × 2، پھر 3 گھٹائیں۔"),
     T("Right! 10 − 3 = 7.", "درست! 10 − 3 = 7"),
     T("5 × 2 = 10, then 10 − 3 = 7.", "5 × 2 = 10، پھر 10 − 3 = 7"),
     common_wrong=[wrong(49, "5a is 5 × a, not 52. 5 × 2 − 3 = 7.", "5a یعنی 5 × a، نہ کہ 52۔ 5 × 2 − 3 = 7", "letter_is_digit"),
                   wrong(10, "That is 5a. Now take away 3: 7.", "یہ 5a ہے۔ اب 3 گھٹائیں: 7")]),
   number_question(
     "s7_two_letters",
     T("Find the value of 2a + b when a = 3 and b = 4.", "جب a = 3 اور b = 4 ہو تو 2a + b کی قیمت معلوم کریں۔"),
     S7,
     T("2a = 2 × 3. Then add b.", "2a = 2 × 3۔ پھر b جمع کریں۔"),
     T("Right! 6 + 4 = 10.", "درست! 6 + 4 = 10"),
     T("2 × 3 = 6, then 6 + 4 = 10.", "2 × 3 = 6، پھر 6 + 4 = 10"),
     common_wrong=[wrong(14, "Only a is doubled: 2 × 3 + 4 = 10.", "صرف a دگنا ہوتا ہے: 2 × 3 + 4 = 10", "adds_first"),
                   wrong(27, "2a is 2 × a, not 23. 6 + 4 = 10.", "2a یعنی 2 × a، نہ کہ 23۔ 6 + 4 = 10", "letter_is_digit")]),
   number_question(
     "s8_square",
     T("Back to the square: its perimeter is 4s. Find the perimeter when s = 9 cm.", "واپس مربع پر: اس کا احاطہ 4s ہے۔ جب s = 9 سینٹی میٹر ہو تو احاطہ معلوم کریں۔"),
     S8,
     T("4s means 4 × 9.", "4s یعنی 4 × 9"),
     T("Right! 36 cm.", "درست! 36 سینٹی میٹر"),
     T("4 × 9 = 36 cm: four sides of 9 cm.", "4 × 9 = 36 سینٹی میٹر: 9 سینٹی میٹر کے چار ضلعے۔"),
     common_wrong=[wrong(13, "That is 4 + 9. A square has 4 sides of 9: 4 × 9 = 36.", "یہ 4 + 9 ہے۔ مربع کے 9 کے 4 ضلعے: 4 × 9 = 36"),
                   wrong(49, "4s is 4 × s, not 49. 4 × 9 = 36.", "4s یعنی 4 × s، نہ کہ 49۔ 4 × 9 = 36", "letter_is_digit")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Zara says that when y = 5, 2y = 25. What went wrong?", "زارا کہتی ہے جب y = 5 ہو تو 2y = 25۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("digit", "2y means 2 × y = 10, not the digits 2 and 5.", "2y یعنی 2 × y = 10، نہ کہ ہندسے 2 اور 5", True,
          "Yes! A number next to a letter means multiply.", "جی ہاں! حرف کے ساتھ لکھا عدد ضرب کا مطلب دیتا ہے۔"),
      opt("seven", "It should be 7.", "یہ 7 ہونا چاہیے۔", False,
          "7 is 2 + 5. 2y means 2 × 5 = 10.", "7 یعنی 2 + 5۔ 2y یعنی 2 × 5 = 10"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "2y is 2 × y. With y = 5 that is 10.", "2y یعنی 2 × y۔ y = 5 پر یہ 10 ہے۔", "letter_is_digit"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "When n = 4, why is 3n equal to 12 and not 34? Can you teach me?",
                     "جب n = 4 ہو تو 3n کا جواب 12 کیوں ہے، 34 کیوں نہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: when n = 4, why is 3n equal to 12 and not 34?",
              "اپنے الفاظ میں بتائیں: جب n = 4 ہو تو 3n کا جواب 12 کیوں ہے، 34 کیوں نہیں؟"),
    "key_idea": "In algebra, a number written next to a letter means multiply: 3n means 3 × n. So with n = 4 it is 3 × 4 = 12. 34 would be thirty-four, which is not what 3n means.",
    "levels": {
      "got_it": "Explains that 3n means 3 × n, so it is 3 × 4 = 12, and that writing the digits side by side gives a different number.",
      "partly": "Says 3n means multiply, or works out 12, without saying why 34 is wrong.",
      "not_yet": "Says 34 is right, or gives no reason."},
    "keywords": [
      ["multiply", "times", "×", "ضرب", "guna", "zarb"],
      ["3 × 4", "3 x 4", "12"],
      ["digit", "next to", "ہندسہ", "ساتھ"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 3n means 3 × n, so it's 3 × 4 = 12.", "بہت خوب! 3n یعنی 3 × n، تو یہ 3 × 4 = 12 ہے۔"),
      "partly": T("Good start! Now say why 34 is wrong: what does the 3 next to n mean?", "اچھی شروعات! اب بتائیں 34 کیوں غلط ہے: n کے ساتھ 3 کا کیا مطلب ہے؟"),
      "not_yet": T("Remember: 3n is short for 3 × n. What is 3 × 4?", "یاد کریں: 3n مختصر ہے 3 × n کا۔ 3 × 4 کتنا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_take_away",
     T("Find the value of 10 − 2k when k = 3.", "جب k = 3 ہو تو 10 − 2k کی قیمت معلوم کریں۔"),
     S11,
     T("Work out 2k = 2 × 3 first.", "پہلے 2k = 2 × 3 نکالیں۔"),
     T("Right! 10 − 6 = 4.", "درست! 10 − 6 = 4"),
     T("2 × 3 = 6, then 10 − 6 = 4.", "2 × 3 = 6، پھر 10 − 6 = 4"),
     common_wrong=[wrong(24, "Multiply first: 2 × 3 = 6, then 10 − 6 = 4.", "پہلے ضرب: 2 × 3 = 6، پھر 10 − 6 = 4", "adds_first"),
                   wrong(6, "That is 2k. Now take it from 10: 10 − 6 = 4.", "یہ 2k ہے۔ اب اسے 10 سے گھٹائیں: 10 − 6 = 4")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Great substituting!", "بہت خوب قیمتیں رکھیں!"),
    "text": T("To find the value of an expression, put each number in place of its letter. A number next to a letter means multiply, and multiplying comes before adding or taking away: 3n + 2 with n = 4 is 3 × 4 + 2 = 14.",
              "عبارت کی قیمت نکالنے کے لیے ہر حرف کی جگہ اس کا عدد رکھیں۔ حرف کے ساتھ عدد کا مطلب ضرب، اور ضرب جمع یا تفریق سے پہلے: n = 4 پر 3n + 2 = 3 × 4 + 2 = 14"),
    "points": [T("2y with y = 5 is 10, not 25.", "y = 5 پر 2y = 10، نہ کہ 25"),
               T("Multiply first, then add or take away.", "پہلے ضرب، پھر جمع یا تفریق۔")]},
 ],
 "review_questions": [
   {"id": "r_value", "type": "apply", "skill": SKILL, "step": number_question(
     "r_value",
     T("Find the value of 4p + 1 when p = 5.", "جب p = 5 ہو تو 4p + 1 کی قیمت معلوم کریں۔"),
     R1,
     T("4 × 5 first, then add 1.", "پہلے 4 × 5، پھر 1 جمع۔"),
     T("Right! 20 + 1 = 21.", "درست! 20 + 1 = 21"),
     T("4 × 5 = 20, then 20 + 1 = 21.", "4 × 5 = 20، پھر 20 + 1 = 21"),
     common_wrong=[wrong(46, "4p is 4 × p, not 45. 20 + 1 = 21.", "4p یعنی 4 × p، نہ کہ 45۔ 20 + 1 = 21", "letter_is_digit"),
                   wrong(24, "Multiply first: 4 × 5 = 20, then + 1 = 21.", "پہلے ضرب: 4 × 5 = 20، پھر + 1 = 21", "adds_first")],
     qtype=None)},
   {"id": "r_ab", "type": "recall", "skill": SKILL, "step": number_question(
     "r_ab",
     T("ab means a × b. Find ab when a = 3 and b = 6.", "ab یعنی a × b۔ جب a = 3 اور b = 6 ہو تو ab معلوم کریں۔"),
     R2,
     T("3 × 6.", "3 × 6"),
     T("Right! 18.", "درست! 18"),
     T("ab = 3 × 6 = 18.", "ab = 3 × 6 = 18"),
     common_wrong=[wrong(9, "That is a + b. ab means multiply: 18.", "یہ a + b ہے۔ ab میں ضرب: 18"),
                   wrong(36, "ab is a × b, not the digits 3 and 6. 3 × 6 = 18.", "ab یعنی a × b، نہ کہ ہندسے 3 اور 6۔ 3 × 6 = 18", "letter_is_digit")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Introduction to Algebra unit. No textbook text or exercises were used.",
   "Common wrong answers target the two classic slips: reading 3n as a two-digit number, and adding before multiplying.",
   "Urdu terms to check: قیمت رکھنا (substitute), عبارت کی قیمت (value of an expression).",
   "The numbers were worked out in content/sources/g6-maths-07/substitution.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import (attach, figure, strip, strip_figure, bar_model, square_sides, arrow_down,
                  label, W)

SIDE = 9                                     # s8: the square's side
assert value("4s", s=SIDE) == S8
TEN11, K11 = 10, 3                           # s11: 10 − 2k with k = 3
assert value("10 - 2k", k=K11) == S11 == TEN11 - 2 * K11
N3 = 4                                       # s3: 3n + 2 with n = 4
assert value("3n + 2", n=N3) == S5


def worked():
    """3n + 2 as bags, then each bag opened to show n marbles."""
    items = strip([("bags", 3, "n"), ("text", "+"), ("marbles", 2)], 46)
    items += arrow_down(W / 2, 54, 74)
    items.append(label((W / 2 + 30, 64), f"n={N3}"))
    items += strip([("marbles", N3, 2), ("marbles", N3, 2), ("marbles", N3, 2), ("text", "+"),
                    ("marbles", 2), ("text", "="), ("text", S5)], 116, gap=12)
    return figure(W, 124,
        f"Top: 3 bags marked n and 2 marbles, which is 3n + 2 (n is the number of marbles in each bag). An arrow down marked n={N3}. Bottom: each bag is opened and holds {N3} marbles, so 3 groups of {N3} marbles plus 2 marbles = {S5}.",
        f"اوپر: 3 تھیلے جن پر n لکھا ہے اور 2 کنچے، یعنی 3n + 2 (n ہر تھیلے کے کنچوں کی تعداد ہے)۔ نیچے کی طرف تیر جس پر n={N3} لکھا ہے۔ نیچے: ہر تھیلا کھلا ہے اور اس میں {N3} کنچے ہیں، تو {N3} کنچوں کے 3 گروہ جمع 2 کنچے = {S5}۔",
        items)


def bags_story(tokens, given, en, ur, answer=None, expr=None):
    """Bags and marbles for an expression, with the given values beside
    them. The expression the picture shows (bags of a letter count as that
    letter, marbles as 1, dashed marbles as −1) must give the step's answer."""
    if answer is not None:
        shown, sign = [], "+"
        for tok in tokens:
            if tok[0] == "text":
                sign = tok[1]
            elif tok[0] in ("bag", "bags"):
                k, letter = (1, tok[1]) if tok[0] == "bag" else (tok[1], tok[2])
                shown.append(f"{sign} {k}*{letter}")
            else:
                shown.append(f"{'-' if tok[0] == 'dmarbles' else sign} {tok[1]}")
        values = {g.split("=")[0]: int(g.split("=")[1]) for g in given}
        assert value(" ".join(shown).lstrip("+ "), **values) == answer, (shown, given)
    return strip_figure(tokens + [("text", g) for g in given], en, ur)


attach(lesson, {
    "s1_hook": square_sides("s",
        "A square with each of its four sides marked s, the length of a side.",
        "ایک مربع جس کے چاروں اطراف پر s لکھا ہے، یعنی ایک ضلع کی لمبائی۔"),
    "s3_how": worked(),
    "s4_add": bags_story([("bag", "x"), ("text", "+"), ("marbles", 9)], ["x=6"],
        "A bag marked x, a plus sign and 9 marbles, which is x + 9. Beside it: x=6, the bag holds 6 marbles.",
        "ایک تھیلا جس پر x لکھا ہے، جمع کا نشان اور 9 کنچے، یعنی x + 9۔ ساتھ میں: x=6، تھیلے میں 6 کنچے ہیں۔", S4),
    "s5_times_add": bags_story([("bags", 3, "n"), ("text", "+"), ("marbles", 2)], [f"n={N3}"],
        f"3 bags marked n, a plus sign and 2 marbles, which is 3n + 2. Beside it: n={N3}, each bag holds {N3} marbles.",
        f"3 تھیلے جن پر n لکھا ہے، جمع کا نشان اور 2 کنچے، یعنی 3n + 2۔ ساتھ میں: n={N3}، ہر تھیلے میں {N3} کنچے ہیں۔", S5),
    "s6_times_subtract": bags_story([("bags", 5, "a"), ("text", "−"), ("dmarbles", 3)], ["a=2"],
        "5 bags marked a, a minus sign and 3 dashed marbles to take away, which is 5a − 3. Beside it: a=2, each bag holds 2 marbles.",
        "5 تھیلے جن پر a لکھا ہے، تفریق کا نشان اور نکالنے کے لیے 3 ڈیش والے کنچے، یعنی 5a − 3۔ ساتھ میں: a=2، ہر تھیلے میں 2 کنچے ہیں۔", S6),
    "s7_two_letters": bags_story([("bags", 2, "a"), ("text", "+"), ("bag", "b")], ["a=3", "b=4"],
        "2 bags marked a, a plus sign and 1 bag marked b, which is 2a + b. Beside it: a=3 and b=4, the marbles in each kind of bag.",
        "2 تھیلے جن پر a لکھا ہے، جمع کا نشان اور 1 تھیلا جس پر b لکھا ہے، یعنی 2a + b۔ ساتھ میں: a=3 اور b=4، ہر قسم کے تھیلے کے کنچے۔", S7),
    "s8_square": square_sides("s",
        f"A square with each of its four sides marked s. Inside it: s={SIDE}, each side is {SIDE} cm.",
        f"ایک مربع جس کے چاروں اطراف پر s لکھا ہے۔ اس کے اندر: s={SIDE}، ہر ضلع {SIDE} سینٹی میٹر ہے۔", inside=f"s={SIDE}"),
    "s9_find_error": bags_story([("bags", 2, "y")], ["y=5"],
        "2 bags marked y, which is 2y. Beside them: y=5, each bag holds 5 marbles.",
        "2 تھیلے جن پر y لکھا ہے، یعنی 2y۔ ساتھ میں: y=5، ہر تھیلے میں 5 کنچے ہیں۔", value("2y", y=5)),
    "s11_take_away": bar_model([[(TEN11, str(TEN11), False)], [(S11, None, False), (K11, "k", True), (K11, "k", True)]],
        f"Two bars. The top bar is 10. The bottom bar is the same length, with two dashed pieces marked k taken away from its end: 10 − 2k. Here k is {K11}.",
        f"دو پٹیاں۔ اوپر والی پٹی 10 ہے۔ نیچے والی پٹی اتنی ہی لمبی ہے، اس کے آخر سے k والے دو ڈیش ٹکڑے نکالے گئے ہیں: 10 − 2k۔ یہاں k کی قیمت {K11} ہے۔"),
    "s12_summary": worked(),
    "qb_recall": bags_story([("bags", 4, "m")], ["m=5"],
        "4 bags marked m, which is 4m. Beside them: m=5, each bag holds 5 marbles.",
        "4 تھیلے جن پر m لکھا ہے، یعنی 4m۔ ساتھ میں: m=5، ہر تھیلے میں 5 کنچے ہیں۔", value("4m", m=5)),
    "qb_apply": bags_story([("marbles", 6, 3), ("text", "+"), ("bags", 2, "c")], ["c=7"],
        "6 marbles, a plus sign and 2 bags marked c, which is 6 + 2c. Beside them: c=7, each bag holds 7 marbles.",
        "6 کنچے، جمع کا نشان اور 2 تھیلے جن پر c لکھا ہے، یعنی 6 + 2c۔ ساتھ میں: c=7، ہر تھیلے میں 7 کنچے ہیں۔", QB),
    "qb_find_error": bags_story([("bags", 2, "a"), ("text", "+"), ("marbles", 1)], ["a=3"],
        "2 bags marked a, a plus sign and 1 marble, which is 2a + 1. Beside them: a=3, each bag holds 3 marbles.",
        "2 تھیلے جن پر a لکھا ہے، جمع کا نشان اور 1 کنچا، یعنی 2a + 1۔ ساتھ میں: a=3، ہر تھیلے میں 3 کنچے ہیں۔", value("2a + 1", a=3)),
    "r_value": bags_story([("bags", 4, "p"), ("text", "+"), ("marbles", 1)], ["p=5"],
        "4 bags marked p, a plus sign and 1 marble, which is 4p + 1. Beside them: p=5, each bag holds 5 marbles.",
        "4 تھیلے جن پر p لکھا ہے، جمع کا نشان اور 1 کنچا، یعنی 4p + 1۔ ساتھ میں: p=5، ہر تھیلے میں 5 کنچے ہیں۔", R1),
})
write(lesson)

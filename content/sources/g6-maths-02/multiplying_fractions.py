from common import (F, T, opt, say, wrong, frac, mixed, unsimplified, fraction_question, write,
                    REF, REVIEW, TIMES_TABLES, EQUIVALENT, MULTIPLY)

SKILL = MULTIPLY


def added(a: F, b: F) -> str:
    """The mistake from adding: 2/3 × 4/5 -> 6/8 (adds tops and bottoms)."""
    return unsimplified(a.numerator + b.numerator, a.denominator + b.denominator)


def kept_denominator(a: F, b: F) -> str:
    """The mistake: multiply the tops but keep one denominator (2/3 × 4/5 -> 8/5)."""
    return unsimplified(a.numerator * b.numerator, b.denominator)


def whole_into_both(n: int, x: F) -> str:
    """The mistake: 3 × 2/5 -> 6/15 (multiplies the top and the bottom by 3)."""
    return unsimplified(n * x.numerator, n * x.denominator)


def whole_part_only(n: int, whole: int, part: F) -> str:
    """The mistake: 3 × 2 1/4 -> 6 1/4 (multiplies only the whole number)."""
    return mixed(n * whole + part)


# s1, s3: a third of Ammi's 12 mangoes
MANGOES = 12
GIVEN = F(1, 3) * MANGOES
assert GIVEN == 4 and MANGOES // 3 == GIVEN
assert MANGOES * 3 == 36  # the "multiplying makes bigger" mistake

# s4, s5, s13: half of 6
HALF_OF_SIX = F(1, 2) * 6
assert HALF_OF_SIX == 3 and HALF_OF_SIX < 6

# s6, s7: Zara gets half of Ali's third of a paratha
ALI, SHARE = F(1, 3), F(1, 2)
ZARA = SHARE * ALI
assert ZARA == F(1, 6)
CUT = ZARA.denominator
assert CUT == 6 and ALI * CUT == 2 and ZARA * CUT == 1 and F(1, 2) * CUT == 3

# s8: two fractions
A8, B8 = F(2, 3), F(4, 5)
S8 = A8 * B8
assert S8 == F(8, 15)
assert kept_denominator(A8, B8) == "8/5" and added(A8, B8) == "6/8"

# s9: simplify before or after
A9, B9 = F(3, 4), F(2, 9)
S9 = A9 * B9
assert unsimplified(3 * 2, 4 * 9) == "6/36" and S9 == F(1, 6)
assert F(1, 2) * F(1, 3) == S9  # 3 and 9 both ÷ 3, 2 and 4 both ÷ 2 first
assert added(A9, B9) == "5/13" and kept_denominator(A9, B9) == "6/9"

# s10: multiplying by a fraction less than 1 makes 8 smaller
assert 8 * F(3, 4) == 6 < 8 < 8 * F(5, 4) == 10 < 8 * F(3, 2) == 12

# s11: a tailor's cloth: 3 suits of 2 1/4 metres
SUITS, PER_SUIT = 3, 2 + F(1, 4)
CLOTH = SUITS * PER_SUIT
assert CLOTH == F(27, 4) and mixed(CLOTH) == "6 3/4"
assert SUITS * 2 == 6 and SUITS * F(1, 4) == F(3, 4)
assert whole_part_only(SUITS, 2, F(1, 4)) == "6 1/4"

# s12: Sana's mistake
assert whole_into_both(3, F(2, 5)) == "6/15" and F(6, 15) == F(2, 5)
assert 3 * F(2, 5) == F(6, 5) and mixed(F(6, 5)) == "1 1/5"

# Question bank and review
QB = F(5, 6) * F(3, 10)
assert unsimplified(15, 60) == "15/60" and QB == F(1, 4)
assert kept_denominator(F(5, 6), F(3, 10)) == "15/10" and added(F(5, 6), F(3, 10)) == "8/16"
assert 2 * (2 + F(1, 2)) == 5 and whole_part_only(2, 2, F(1, 2)) == "4 1/2"
assert F(2, 3) * 12 == 8 and 12 // 3 == 4
assert F(1, 2) * F(4, 7) == F(2, 7) and kept_denominator(F(1, 2), F(4, 7)) == "4/7"

lesson = {
 "id": "g6-maths-02-multiplying-fractions",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find a fraction of a whole number, multiply fractions and mixed numbers (simplifying before or after), and know that multiplying by a fraction less than 1 gives a smaller answer.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Multiplying fractions", "کسور کی ضرب"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": EQUIVALENT}, {"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "multiply_makes_bigger", "description": "Believes multiplying always gives a bigger answer, so 1/2 × 6 must be more than 6."},
   {"id": "kept_denominator", "description": "Multiplies the numerators but keeps a denominator, as when adding (2/3 × 4/5 = 8/5)."},
   {"id": "add_tops_and_bottoms", "description": "Adds the numerators and the denominators instead of multiplying (2/3 × 4/5 = 6/8)."},
   {"id": "whole_into_both", "description": "Multiplies both the numerator and the denominator by the whole number (3 × 2/5 = 6/15, which is still 2/5)."},
   {"id": "whole_part_only", "description": "Multiplies only the whole-number part of a mixed number (3 × 2 1/4 = 6 1/4)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("How do you work out 2/3 × 4/5?", "2/3 × 4/5 کیسے حل کرتے ہیں؟"),
     "options": [
       opt("tops_bottoms", "Multiply the tops and multiply the bottoms: 8/15", "اوپر والوں کو ضرب دیں اور نیچے والوں کو ضرب دیں: 8/15", True,
           "Yes! 2 × 4 = 8 and 3 × 5 = 15, so 2/3 × 4/5 = 8/15.", "جی ہاں! 2 × 4 = 8 اور 3 × 5 = 15، اس لیے 2/3 × 4/5 = 8/15"),
       opt("common", "Find a common denominator first", "پہلے مشترک نسب نما نکالیں", False,
           "That is for adding and subtracting. To multiply, just multiply the tops and the bottoms.", "یہ جمع اور تفریق کے لیے ہے۔ ضرب میں صرف اوپر والوں اور نیچے والوں کو ضرب دیں۔"),
       opt("keep", "Multiply the tops and keep the bottom: 8/5", "اوپر والوں کو ضرب دیں اور نیچے والا وہی رکھیں: 8/5", False,
           "8/5 is more than 1, but 2/3 of 4/5 must be less than 4/5. Multiply the bottoms too.", "8/5 تو 1 سے زیادہ ہے، لیکن 4/5 کا 2/3 تو 4/5 سے کم ہونا چاہیے۔ نیچے والوں کو بھی ضرب دیں۔", "kept_denominator"),
     ]}},
   {"id": "qb_five_sixths", "type": "apply", "step": fraction_question(
     "qb_five_sixths",
     T("Work out 5/6 × 3/10. Give your answer in its simplest form.", "5/6 × 3/10 حل کریں۔ جواب سادہ ترین شکل میں لکھیں۔"),
     frac(QB),
     T("Multiply the tops and the bottoms, then simplify. Or simplify first: 5 and 10, 3 and 6.", "اوپر والوں اور نیچے والوں کو ضرب دیں، پھر سادہ کریں۔ یا پہلے سادہ کریں: 5 اور 10، 3 اور 6"),
     T("Right! 15/60 = 1/4. Simplifying first gives 1/2 × 1/2 = 1/4 too.", "درست! 15/60 = 1/4۔ پہلے سادہ کرنے سے بھی 1/2 × 1/2 = 1/4 آتا ہے۔"),
     T("5 × 3 = 15 and 6 × 10 = 60, so 15/60. 15 divides both: 15/60 = 1/4.", "5 × 3 = 15 اور 6 × 10 = 60، یعنی 15/60۔ 15 دونوں کو تقسیم کرتا ہے: 15/60 = 1/4"),
     common_wrong=[
       wrong(kept_denominator(F(5, 6), F(3, 10)), "Multiply the bottoms too: 6 × 10 = 60.", "نیچے والوں کو بھی ضرب دیں: 6 × 10 = 60", "kept_denominator"),
       wrong(added(F(5, 6), F(3, 10)), "You added the tops and the bottoms. To multiply, multiply them.", "آپ نے اوپر اور نیچے والے جمع کر دیے۔ ضرب میں انہیں ضرب دیں۔", "add_tops_and_bottoms")],
     qtype=None)},
   {"id": "qb_find_error_mixed", "type": "find_error", "step": {
     "id": "qb_find_error_mixed", "type": "choice",
     "prompt": T("Hamza says 2 × 2 1/2 = 4 1/2. What went wrong?", "حمزہ کہتا ہے 2 × 2 1/2 = 4 1/2۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("half", "He multiplied the 2 wholes but not the 1/2. 2 × 2 1/2 = 4 + 1 = 5.", "اس نے 2 پوروں کو ضرب دی لیکن 1/2 کو نہیں۔ 2 × 2 1/2 = 4 + 1 = 5", True,
           "Right! Two halves make 1 more, so the answer is 5. Or 2 × 5/2 = 10/2 = 5.", "درست! دو آدھے مل کر 1 اور بنتے ہیں، اس لیے جواب 5 ہے۔ یا 2 × 5/2 = 10/2 = 5"),
       opt("nothing", "Nothing, 2 × 2 = 4 and the 1/2 stays.", "کوئی غلطی نہیں، 2 × 2 = 4 اور 1/2 ویسے ہی رہتا ہے۔", False,
           "2 × 2 1/2 means two lots of 2 1/2. Two halves are there, not one.", "2 × 2 1/2 کا مطلب ہے 2 1/2 دو بار۔ اس میں دو آدھے ہیں، ایک نہیں۔", "whole_part_only"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_multiply_rule", "front": T("How do you multiply 2/3 × 4/5?", "2/3 × 4/5 کیسے ضرب دیتے ہیں؟"),
    "back": T("Multiply top × top and bottom × bottom: (2 × 4)/(3 × 5) = 8/15. No common denominator needed.", "اوپر × اوپر اور نیچے × نیچے: (2 × 4)/(3 × 5) = 8/15۔ مشترک نسب نما کی ضرورت نہیں۔")},
   {"id": "f_of_means_times", "front": T("What is 1/3 of 12?", "12 کا 1/3 کتنا ہے؟"),
    "back": T("'Of' means ×: 1/3 × 12 = 12 ÷ 3 = 4.", "'کا' کا مطلب ہے ×: 1/3 × 12 = 12 ÷ 3 = 4")},
   {"id": "f_smaller", "front": T("Does multiplying always make a number bigger?", "کیا ضرب سے عدد ہمیشہ بڑا ہو جاتا ہے؟"),
    "back": T("No! Multiplying by a fraction less than 1 makes it smaller: 1/2 × 6 = 3.", "نہیں! 1 سے کم کسر سے ضرب دینے پر عدد چھوٹا ہو جاتا ہے: 1/2 × 6 = 3")},
 ],
 "home_tasks": [{"id": "h_fold_half_third", "text": T(
   "Take a square of paper. Fold it into 3 equal strips and colour one strip: that is 1/3. Now fold the paper in half the other way. How much of the whole paper is half of your coloured strip? Open it and count the small pieces.",
   "کاغذ کا ایک چوکور ٹکڑا لیں۔ اسے 3 برابر پٹیوں میں تہہ کریں اور ایک پٹی رنگ دیں: یہ 1/3 ہے۔ اب کاغذ کو دوسری طرف سے آدھا تہہ کریں۔ رنگی ہوئی پٹی کا آدھا پورے کاغذ کا کتنا حصہ ہے؟ کھول کر چھوٹے ٹکڑے گنیں۔")}],
 "glossary": [T("Fraction", "کسر"), T("Numerator", "شمار کنندہ"), T("Denominator", "نسب نما"),
              T("Multiplication", "ضرب"), T("Product", "حاصل ضرب"), T("Simplest form", "سادہ ترین شکل"),
              T("Mixed number", "مخلوط عدد"), T("Improper fraction", "غیر واجب کسر")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", f"Ammi bought {MANGOES} mangoes and gave a third of them to our neighbours. How many mangoes did she give?",
                     f"امی نے {MANGOES} آم خریدے اور ان کا تہائی حصہ پڑوسیوں کو دے دیا۔ انہوں نے کتنے آم دیے؟"),
    "text": T("Today we multiply with fractions: a fraction of a number, and a fraction of a fraction. First, a quick check.",
              "آج ہم کسور کے ساتھ ضرب سیکھیں گے: کسی عدد کا کسری حصہ، اور کسی کسر کا کسری حصہ۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": EQUIVALENT,
    "prompt": T("What is 4/6 in its simplest form?", "4/6 کی سادہ ترین شکل کیا ہے؟"),
    "options": [
      opt("two_thirds", "2/3", "2/3", True,
          "Yes! 2 divides 4 and 6: 4/6 = 2/3.", "جی ہاں! 2، 4 اور 6 دونوں کو تقسیم کرتا ہے: 4/6 = 2/3"),
      opt("one_half", "1/2", "1/2", False,
          "1/2 = 3/6, not 4/6. Divide the top and the bottom by the same number.", "1/2 = 3/6 ہے، 4/6 نہیں۔ اوپر اور نیچے کو ایک ہی عدد سے تقسیم کریں۔"),
      opt("two_sixths", "2/6", "2/6", False,
          "Only the top was divided. Divide the bottom by 2 as well.", "صرف اوپر والا تقسیم ہوا۔ نیچے والے کو بھی 2 سے تقسیم کریں۔"),
    ]},
   {"id": "s3_third_of_twelve", "type": "number", "question_type": "apply",
    "prompt": T(f"Ammi shares {MANGOES} mangoes into 3 equal groups and gives one group away. How many mangoes is 1/3 of {MANGOES}?",
                f"امی {MANGOES} آموں کو 3 برابر حصوں میں بانٹتی ہیں اور ایک حصہ دے دیتی ہیں۔ {MANGOES} کا 1/3 کتنے آم ہیں؟"),
    "answer": int(GIVEN), "checker": "numeric",
    "hint": T(f"Share {MANGOES} into 3 equal groups: {MANGOES} ÷ 3.", f"{MANGOES} کو 3 برابر حصوں میں بانٹیں: {MANGOES} ÷ 3"),
    "feedback_correct": T(f"Right! {MANGOES} ÷ 3 = {GIVEN}. So 1/3 of {MANGOES} = 1/3 × {MANGOES} = {GIVEN} mangoes.", f"درست! {MANGOES} ÷ 3 = {GIVEN}۔ اس لیے {MANGOES} کا 1/3 = 1/3 × {MANGOES} = {GIVEN} آم۔"),
    "feedback_wrong": T(f"3 equal groups of {MANGOES} mangoes have {GIVEN} mangoes each. 1/3 of {MANGOES} = {GIVEN}.", f"{MANGOES} آموں کے 3 برابر حصوں میں ہر ایک میں {GIVEN} آم ہیں۔ {MANGOES} کا 1/3 = {GIVEN}"),
    "common_wrong": [wrong(MANGOES * 3, "That is 3 times 12! A third of the mangoes must be fewer than all 12.",
                           "یہ تو 12 کا 3 گنا ہے! آموں کا تہائی حصہ تو سارے 12 آموں سے کم ہونا چاہیے۔", "multiply_makes_bigger")]},
   {"id": "s4_predict", "type": "choice",
    "prompt": T("Guess first: Bilal says multiplying always makes a number bigger, so 1/2 × 6 is more than 6. Is he right?",
                "پہلے اندازہ لگائیں: بلال کہتا ہے کہ ضرب سے عدد ہمیشہ بڑا ہوتا ہے، اس لیے 1/2 × 6 چھ سے زیادہ ہے۔ کیا وہ درست ہے؟"),
    "options": [
      opt("yes", "Yes, multiplying always makes bigger", "ہاں، ضرب سے ہمیشہ بڑا ہوتا ہے", False,
          "That is true for whole numbers like 2 × 6. But 1/2 × 6 means half of 6. Is half of 6 more than 6?",
          "یہ 2 × 6 جیسے پورے اعداد کے لیے درست ہے۔ لیکن 1/2 × 6 کا مطلب ہے 6 کا آدھا۔ کیا 6 کا آدھا 6 سے زیادہ ہے؟", "multiply_makes_bigger"),
      opt("no", "No, 1/2 × 6 is less than 6", "نہیں، 1/2 × 6 چھ سے کم ہے", True,
          "Good thinking! 1/2 × 6 means half of 6, which is 3. That is less than 6.", "بہت خوب سوچا! 1/2 × 6 کا مطلب ہے 6 کا آدھا، یعنی 3۔ یہ 6 سے کم ہے۔"),
      opt("same", "It stays 6", "یہ 6 ہی رہتا ہے", False,
          "Only 1 × 6 stays 6. Half of 6 is less.", "صرف 1 × 6 چھ رہتا ہے۔ 6 کا آدھا اس سے کم ہے۔"),
    ]},
   {"id": "s5_see_it", "type": "explain",
    "character": say("talking", "'Of' means multiply! Half of 6 is 1/2 × 6.", "'کا' کا مطلب ہے ضرب! 6 کا آدھا یعنی 1/2 × 6"),
    "text": T("1/3 of 12 is the same as 1/3 × 12 = 12 ÷ 3 = 4. In the same way, 1/2 of 6 = 1/2 × 6 = 3. When you multiply by a fraction less than 1, you take only a part, so the answer is smaller than the number you started with. Multiplying makes bigger only when you multiply by more than 1.",
              "12 کا 1/3 وہی ہے جو 1/3 × 12 = 12 ÷ 3 = 4۔ اسی طرح 6 کا 1/2 = 1/2 × 6 = 3۔ جب آپ 1 سے کم کسر سے ضرب دیتے ہیں تو صرف ایک حصہ لیتے ہیں، اس لیے جواب شروع والے عدد سے چھوٹا آتا ہے۔ ضرب سے عدد صرف تب بڑا ہوتا ہے جب 1 سے زیادہ سے ضرب دیں۔")},
   {"id": "s6_part_of_part", "type": "sim", "question_type": "apply", "renderer": "native", "sim_id": "fraction_bars",
    "prompt": T(f"Ali has 1/3 of a paratha. He gives half of his piece to Zara. Use + to cut the paratha into {CUT} pieces. Ali's third is {int(ALI * CUT)} pieces. Tap only Zara's pieces, then press Check.",
                f"علی کے پاس پراٹھے کا 1/3 ہے۔ وہ اپنے ٹکڑے کا آدھا زارا کو دیتا ہے۔ + دبا کر پراٹھے کے {CUT} ٹکڑے کریں۔ علی کا تہائی {int(ALI * CUT)} ٹکڑے ہے۔ صرف زارا کے ٹکڑے چھوئیں، پھر \"جانچیں\" دبائیں۔"),
    "params": {"wholes": 1, "max_cut": 12},
    "expected": {"result": "pieces", "checker": "numeric", "answer": str(int(ZARA * CUT))},
    "hint": T(f"Ali's third is {int(ALI * CUT)} pieces. Half of {int(ALI * CUT)} pieces is how many?", f"علی کا تہائی {int(ALI * CUT)} ٹکڑے ہے۔ {int(ALI * CUT)} ٹکڑوں کا آدھا کتنے ٹکڑے ہے؟"),
    "feedback_correct": T(f"Yes! Zara gets 1 piece out of {CUT}: half of a third is 1/6 of the paratha.", f"جی ہاں! زارا کو {CUT} میں سے 1 ٹکڑا ملا: تہائی کا آدھا پراٹھے کا 1/6 ہے۔"),
    "feedback_wrong": T(f"Cut the paratha into {CUT}. Ali's third is 2 pieces; half of that is 1 piece. Zara gets 1/6 of the paratha.", f"پراٹھے کے {CUT} ٹکڑے کریں۔ علی کا تہائی 2 ٹکڑے ہے؛ اس کا آدھا 1 ٹکڑا ہے۔ زارا کو پراٹھے کا 1/6 ملا۔"),
    "common_wrong": [
      wrong(str(int(ALI * CUT)), "That is all of Ali's third. Zara gets only half of it.", "یہ تو علی کا پورا تہائی ہے۔ زارا کو اس کا صرف آدھا ملتا ہے۔"),
      wrong(str(int(F(1, 2) * CUT)), "That is half of the whole paratha. Zara gets half of Ali's third, not half of the paratha.", "یہ تو پورے پراٹھے کا آدھا ہے۔ زارا کو علی کے تہائی کا آدھا ملتا ہے، پورے پراٹھے کا نہیں۔"),
    ]},
   {"id": "s7_rule", "type": "explain",
    "character": say("happy", "Multiply top by top, and bottom by bottom!", "اوپر کو اوپر سے، اور نیچے کو نیچے سے ضرب دیں!"),
    "text": T("Half of a third is 1/2 × 1/3. Zara got 1 piece out of 6, so 1/2 × 1/3 = 1/6. We get it by multiplying the numerators and multiplying the denominators: (1 × 1)/(2 × 3) = 1/6. No common denominator is needed to multiply. Notice: 1/6 is smaller than both 1/2 and 1/3.",
              "تہائی کا آدھا یعنی 1/2 × 1/3۔ زارا کو 6 میں سے 1 ٹکڑا ملا، اس لیے 1/2 × 1/3 = 1/6۔ یہ شمار کنندوں کو آپس میں ضرب دینے اور نسب نماؤں کو آپس میں ضرب دینے سے آتا ہے: (1 × 1)/(2 × 3) = 1/6۔ ضرب کے لیے مشترک نسب نما کی ضرورت نہیں۔ دیکھیں: 1/6، 1/2 اور 1/3 دونوں سے چھوٹا ہے۔")},
   fraction_question(
     "s8_two_fractions",
     T("Work out 2/3 × 4/5.", "2/3 × 4/5 حل کریں۔"),
     frac(S8),
     T("Multiply the tops: 2 × 4. Multiply the bottoms: 3 × 5.", "اوپر والوں کو ضرب دیں: 2 × 4۔ نیچے والوں کو ضرب دیں: 3 × 5"),
     T("Right! (2 × 4)/(3 × 5) = 8/15.", "درست! (2 × 4)/(3 × 5) = 8/15"),
     T("2 × 4 = 8 on top and 3 × 5 = 15 at the bottom: 2/3 × 4/5 = 8/15.", "اوپر 2 × 4 = 8 اور نیچے 3 × 5 = 15: یعنی 2/3 × 4/5 = 8/15"),
     common_wrong=[
       wrong(kept_denominator(A8, B8), "You kept the 5 at the bottom. 8/5 is more than 1! Multiply the bottoms too: 3 × 5.",
             "آپ نے نیچے 5 ہی رہنے دیا۔ 8/5 تو 1 سے زیادہ ہے! نیچے والوں کو بھی ضرب دیں: 3 × 5", "kept_denominator"),
       wrong(added(A8, B8), "You added the tops and the bottoms. This time we multiply: 2 × 4 and 3 × 5.",
             "آپ نے اوپر اور نیچے والے جمع کر دیے۔ یہاں ضرب دینی ہے: 2 × 4 اور 3 × 5", "add_tops_and_bottoms"),
     ]),
   fraction_question(
     "s9_simplify",
     T("Work out 3/4 × 2/9. Give your answer in its simplest form. Tip: you can simplify before you multiply.",
       "3/4 × 2/9 حل کریں۔ جواب سادہ ترین شکل میں لکھیں۔ مشورہ: آپ ضرب سے پہلے بھی سادہ کر سکتے ہیں۔"),
     frac(S9),
     T("3 goes into 3 and 9; 2 goes into 2 and 4. Or multiply first to get 6/36, then simplify.", "3، 3 اور 9 میں پورا آتا ہے؛ 2، 2 اور 4 میں۔ یا پہلے ضرب دے کر 6/36 بنائیں، پھر سادہ کریں۔"),
     T("Well done! Simplify first: 1/2 × 1/3 = 1/6. Or after: 6/36 = 1/6. The same answer!", "شاباش! پہلے سادہ کریں: 1/2 × 1/3 = 1/6۔ یا بعد میں: 6/36 = 1/6۔ جواب ایک ہی ہے!"),
     T("3 × 2 = 6 and 4 × 9 = 36, so 6/36. 6 divides both: 6/36 = 1/6.", "3 × 2 = 6 اور 4 × 9 = 36، یعنی 6/36۔ 6 دونوں کو تقسیم کرتا ہے: 6/36 = 1/6"),
     common_wrong=[
       wrong(kept_denominator(A9, B9), "You kept the 9 at the bottom. Multiply the bottoms too: 4 × 9 = 36.",
             "آپ نے نیچے 9 ہی رہنے دیا۔ نیچے والوں کو بھی ضرب دیں: 4 × 9 = 36", "kept_denominator"),
       wrong(added(A9, B9), "You added the tops and the bottoms. Multiply them instead.",
             "آپ نے اوپر اور نیچے والے جمع کر دیے۔ انہیں ضرب دیں۔", "add_tops_and_bottoms"),
     ]),
   {"id": "s10_smaller", "type": "choice", "question_type": "recall",
    "prompt": T("Which answer is less than 8?", "کس کا جواب 8 سے کم ہے؟"),
    "options": [
      opt("three_quarters", "8 × 3/4", "8 × 3/4", True,
          "Yes! 3/4 is less than 1, so 8 × 3/4 = 6 is less than 8.", "جی ہاں! 3/4، 1 سے کم ہے، اس لیے 8 × 3/4 = 6، 8 سے کم ہے۔"),
      opt("five_quarters", "8 × 5/4", "8 × 5/4", False,
          "5/4 is more than 1, so 8 × 5/4 = 10 is more than 8.", "5/4، 1 سے زیادہ ہے، اس لیے 8 × 5/4 = 10، 8 سے زیادہ ہے۔", "multiply_makes_bigger"),
      opt("one_and_half", "8 × 1 1/2", "8 × 1 1/2", False,
          "1 1/2 is more than 1, so 8 × 1 1/2 = 12 is more than 8.", "1 1/2، 1 سے زیادہ ہے، اس لیے 8 × 1 1/2 = 12، 8 سے زیادہ ہے۔", "multiply_makes_bigger"),
    ]},
   fraction_question(
     "s11_tailor",
     T(f"A tailor needs {mixed(PER_SUIT)} metres of cloth for one shalwar kameez. How much cloth does he need for {SUITS} suits? Write a mixed number.",
       f"ایک درزی کو ایک شلوار قمیض کے لیے {mixed(PER_SUIT)} میٹر کپڑا چاہیے۔ {SUITS} سوٹوں کے لیے کتنا کپڑا چاہیے؟ مخلوط عدد لکھیں۔"),
     mixed(CLOTH),
     T(f"Change {mixed(PER_SUIT)} to quarters first: {mixed(PER_SUIT)} = {frac(PER_SUIT)}. Then multiply by {SUITS}.", f"پہلے {mixed(PER_SUIT)} کو چوتھائیوں میں بدلیں: {mixed(PER_SUIT)} = {frac(PER_SUIT)}۔ پھر {SUITS} سے ضرب دیں۔"),
     T(f"Right! {SUITS} × {frac(PER_SUIT)} = {frac(CLOTH)} = {mixed(CLOTH)} metres.", f"درست! {SUITS} × {frac(PER_SUIT)} = {frac(CLOTH)} = {mixed(CLOTH)} میٹر"),
     T(f"{mixed(PER_SUIT)} = {frac(PER_SUIT)}. {SUITS} × {frac(PER_SUIT)} = {frac(CLOTH)}, and 27 ÷ 4 = 6 remainder 3, so {mixed(CLOTH)} metres.",
       f"{mixed(PER_SUIT)} = {frac(PER_SUIT)}۔ {SUITS} × {frac(PER_SUIT)} = {frac(CLOTH)}، اور 27 ÷ 4 = 6 باقی 3، اس لیے {mixed(CLOTH)} میٹر۔"),
     common_wrong=[
       wrong(whole_part_only(SUITS, 2, F(1, 4)), "You multiplied the 2 metres but not the 1/4. 3 lots of 1/4 is 3/4, so add 3/4, not 1/4.",
             "آپ نے 2 میٹر کو ضرب دی لیکن 1/4 کو نہیں۔ 1/4 تین بار 3/4 بنتا ہے، اس لیے 3/4 جمع کریں، 1/4 نہیں۔", "whole_part_only"),
       wrong(frac(CLOTH), "The right amount, but please write it as a mixed number: 27 ÷ 4 = ? remainder ?",
             "مقدار درست ہے، لیکن اسے مخلوط عدد کی شکل میں لکھیں: 27 ÷ 4 = ? باقی ?"),
     ]),
   {"id": "s12_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Sana says 3 × 2/5 = 6/15. What went wrong?", "ثنا کہتی ہے 3 × 2/5 = 6/15۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("both", "She multiplied the top and the bottom by 3. Only the top: 3 × 2/5 = 6/5 = 1 1/5.", "اس نے اوپر اور نیچے دونوں کو 3 سے ضرب دی۔ صرف اوپر والے کو: 3 × 2/5 = 6/5 = 1 1/5", True,
          "Yes! 6/15 is the same as 2/5, so nothing was multiplied. 3 lots of 2 fifths are 6 fifths.", "جی ہاں! 6/15 تو 2/5 ہی کے برابر ہے، یعنی کچھ ضرب ہوا ہی نہیں۔ 2 پانچویں حصے تین بار 6 پانچویں حصے بنتے ہیں۔"),
      opt("nothing", "Nothing, 3 × 2 = 6 and 3 × 5 = 15.", "کوئی غلطی نہیں، 3 × 2 = 6 اور 3 × 5 = 15", False,
          "6/15 = 2/5, the number we started with. 3 × 2/5 must be 3 times as much.", "6/15 = 2/5، یعنی وہی عدد جس سے شروع کیا۔ 3 × 2/5 تو اس کا تین گنا ہونا چاہیے۔", "whole_into_both"),
      opt("bottom", "She should multiply only the bottom: 2/15.", "اسے صرف نیچے والے کو ضرب دینی چاہیے تھی: 2/15", False,
          "2/15 is smaller than 2/5! 3 = 3/1, so multiply the tops: 3 × 2 = 6, and the bottoms: 1 × 5 = 5.", "2/15 تو 2/5 سے بھی چھوٹا ہے! 3 = 3/1، اس لیے اوپر والے ضرب دیں: 3 × 2 = 6، اور نیچے والے: 1 × 5 = 5"),
    ]},
   {"id": "s13_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? I thought multiplying always makes a number bigger!",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ میں تو سمجھتا تھا کہ ضرب سے عدد ہمیشہ بڑا ہو جاتا ہے!"),
    "task": T("In your own words: why is 1/2 × 6 only 3, smaller than 6? Explain it to Bilal. You can use rotis or mangoes.",
              "اپنے الفاظ میں بتائیں: 1/2 × 6 کا جواب صرف 3 کیوں ہے، جو 6 سے چھوٹا ہے؟ بلال کو سمجھائیں۔ آپ روٹیوں یا آموں کی مثال دے سکتے ہیں۔"),
    "key_idea": "1/2 × 6 means half of 6, so we take only a part of the 6: 3. Multiplying by a fraction less than 1 gives an answer smaller than the number; it only makes bigger when the multiplier is more than 1.",
    "levels": {
      "got_it": "Says 1/2 × 6 means half of 6 (taking a part), gets 3, and/or says multiplying by a number less than 1 makes it smaller.",
      "partly": "Gives the answer 3 or says 'half of 6', but does not say why the answer is smaller than 6.",
      "not_yet": "Agrees that multiplying always makes bigger, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["half", "part", "آدھ", "حصہ", "aadh", "adh", "hissa", "hisa"],
      ["less than 1", "less than one", "less", "smaller", "کم", "چھوٹ", "kam", "chhot", "chot"],
      ["3", "three", "تین", "teen"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 1/2 × 6 means half of 6, so we take only a part: 3. A fraction less than 1 makes the answer smaller.",
                  "بہت خوب سمجھایا! 1/2 × 6 کا مطلب ہے 6 کا آدھا، یعنی ہم صرف ایک حصہ لیتے ہیں: 3۔ 1 سے کم کسر سے ضرب دینے پر جواب چھوٹا آتا ہے۔"),
      "partly": T("Good start! Now say why the answer is smaller: is 1/2 more or less than 1?",
                  "اچھی شروعات! اب بتائیں کہ جواب چھوٹا کیوں ہے: کیا 1/2، 1 سے زیادہ ہے یا کم؟"),
      "not_yet": T("Think of 6 rotis. If you eat half of them, how many do you eat? Is that more or less than 6?",
                   "سوچیں: 6 روٹیاں ہیں۔ اگر آپ ان کا آدھا کھائیں تو کتنی کھائیں گے؟ یہ 6 سے زیادہ ہے یا کم؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s14_summary", "type": "summary",
    "character": say("celebrating", "Now you can multiply fractions!", "اب آپ کسور کو ضرب دے سکتے ہیں!"),
    "text": T("'Of' means multiply: 1/3 of 12 = 1/3 × 12 = 4. To multiply fractions, multiply the numerators and multiply the denominators, then simplify (or simplify first). Change a mixed number to an improper fraction before multiplying. Multiplying by a fraction less than 1 makes a number smaller.",
              "'کا' کا مطلب ہے ضرب: 12 کا 1/3 = 1/3 × 12 = 4۔ کسور کو ضرب دینے کے لیے شمار کنندوں کو آپس میں اور نسب نماؤں کو آپس میں ضرب دیں، پھر سادہ کریں (یا پہلے سادہ کریں)۔ ضرب سے پہلے مخلوط عدد کو غیر واجب کسر میں بدلیں۔ 1 سے کم کسر سے ضرب دینے پر عدد چھوٹا ہو جاتا ہے۔"),
    "points": [T("1/2 × 1/3 = (1 × 1)/(2 × 3) = 1/6", "1/2 × 1/3 = (1 × 1)/(2 × 3) = 1/6"),
               T("3 × 2 1/4 = 3 × 9/4 = 27/4 = 6 3/4", "3 × 2 1/4 = 3 × 9/4 = 27/4 = 6 3/4"),
               T("1/2 × 6 = 3: smaller than 6!", "1/2 × 6 = 3: یہ 6 سے چھوٹا ہے!")]},
 ],
 "review_questions": [
   {"id": "r_two_thirds", "type": "apply", "skill": SKILL, "step": {
     "id": "r_two_thirds", "type": "number",
     "prompt": T("What is 2/3 of 12 rotis?", "12 روٹیوں کا 2/3 کتنی روٹیاں ہیں؟"),
     "answer": int(F(2, 3) * 12), "checker": "numeric",
     "hint": T("First find 1/3 of 12, then take 2 of those groups.", "پہلے 12 کا 1/3 نکالیں، پھر ایسے 2 حصے لیں۔"),
     "feedback_correct": T("Right! 1/3 of 12 is 4, so 2/3 of 12 is 8.", "درست! 12 کا 1/3 چار ہے، اس لیے 12 کا 2/3 آٹھ ہے۔"),
     "feedback_wrong": T("12 ÷ 3 = 4 rotis in each third. Two thirds: 2 × 4 = 8 rotis.", "ہر تہائی میں 12 ÷ 3 = 4 روٹیاں۔ دو تہائیاں: 2 × 4 = 8 روٹیاں۔"),
     "common_wrong": [wrong(12 // 3, "4 is only 1/3 of 12. Two thirds is two of those groups.", "4 تو 12 کا صرف 1/3 ہے۔ دو تہائیاں ایسے دو حصے ہیں۔")]}},
   {"id": "r_half_of_four_sevenths", "type": "apply", "skill": SKILL, "step": fraction_question(
     "r_half_of_four_sevenths",
     T("Work out 1/2 × 4/7. Give your answer in its simplest form.", "1/2 × 4/7 حل کریں۔ جواب سادہ ترین شکل میں لکھیں۔"),
     frac(F(1, 2) * F(4, 7)),
     T("Multiply the tops and the bottoms, then simplify.", "اوپر والوں اور نیچے والوں کو ضرب دیں، پھر سادہ کریں۔"),
     T("Right! 4/14 = 2/7. Half of 4 sevenths is 2 sevenths.", "درست! 4/14 = 2/7۔ 4 ساتویں حصوں کا آدھا 2 ساتویں حصے ہیں۔"),
     T("1 × 4 = 4 and 2 × 7 = 14, so 4/14 = 2/7.", "1 × 4 = 4 اور 2 × 7 = 14، یعنی 4/14 = 2/7"),
     common_wrong=[wrong(kept_denominator(F(1, 2), F(4, 7)), "4/7 is what we started with. Half of it must be smaller: multiply the bottoms too.",
                         "4/7 تو وہی ہے جس سے شروع کیا۔ اس کا آدھا چھوٹا ہونا چاہیے: نیچے والوں کو بھی ضرب دیں۔", "kept_denominator")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Fractions unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the file is named g6-maths-02 to sit with the other fractions lessons. Fix the name and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: ضرب (multiplication), حاصل ضرب (product), سادہ ترین شکل (simplest form), تہائی (third), and 'کا' used for 'of' (12 کا 1/3). Some books write 'of' as 'کا حصہ'.",
   "s11 multiplies a mixed number, which the mixed-numbers lesson teaches; the hint shows the change to an improper fraction, so maths.fractions.mixed_numbers is not listed as a prerequisite. Add it if students reach this lesson first.",
   "The fraction checker accepts any equal value: in s11, 27/4 is listed in common_wrong with feedback asking for a mixed number (it costs an attempt). Unsimplified answers like 6/36 in s9 get 'simplify it' and do not cost an attempt.",
   "Steps follow the lesson pattern: foundation check (s2), fraction of a number (s3), prediction (s4), symbolic (s5), concrete part of a part with the fraction bars (s6) then the rule (s7), practice (s8, s9), multiplying makes smaller (s10), mixed number (s11), find the error (s12), explain (s13).",
   "The answers and the common wrong answers were worked out with Python's fractions module in content/sources/g6-maths-02/multiplying_fractions.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

from math import gcd

from common import (F, T, opt, say, wrong, frac, unsimplified, fraction_question, write,
                    REF, REVIEW, UNIT_FRACTIONS, TIMES_TABLES, EQUIVALENT)

SKILL = EQUIVALENT

# Zara's half and Ali's two quarters (s1, s3, s4).
assert F(1, 2) == F(2, 4) == F(4, 8)
HALF_IN_QUARTERS = F(1, 2) * 4
assert HALF_IN_QUARTERS == 2

# s6: 2/3 = ?/12
GAP_TOP = F(2, 3) * 12
assert GAP_TOP == 8
GAP_ADDED = 2 + (12 - 3)  # adds 9 to the top as well as the bottom
assert GAP_ADDED == 11 and F(GAP_ADDED, 12) != F(2, 3)

# s7: 6/8 in lowest terms
assert gcd(6, 8) == 2 and F(6, 8) == F(3, 4)

# s8: 12/18 in lowest terms (one step: divide by 6; or 2 then 3)
assert gcd(12, 18) == 6
CHART = F(12, 18)
assert frac(CHART) == "2/3"
assert F(6, 9) == CHART  # half-way: still simplifiable

# s9: Hamza adds 1 to top and bottom of 1/2
assert F(1 + 1, 2 + 1) == F(2, 3) != F(1, 2)
assert F(1 * 2, 2 * 2) == F(1, 2)

# s11: which equals 3/5?
assert F(6, 10) == F(3, 5)
assert F(4, 6) != F(3, 5) and F(3, 10) != F(3, 5) and F(6, 5) != F(3, 5)

# Question bank and review.
assert F(10, 15) == F(2, 3) and gcd(10, 15) == 5
assert F(3, 4) == F(9, 12)
assert F(16, 20) == F(4, 5) and gcd(16, 20) == 4
assert F(8, 10) == F(4, 5)

lesson = {
 "id": "g6-maths-02-equivalent-fractions",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise and make equivalent fractions, and write a fraction in its simplest form (lowest terms).", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Equivalent fractions", "مساوی کسور"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": UNIT_FRACTIONS}, {"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "bigger_numbers_bigger", "description": "Thinks 2/4 is more than 1/2 because its numbers are bigger."},
   {"id": "add_same_number", "description": "Adds the same number to the numerator and the denominator (1/2 = 2/3) instead of multiplying or dividing."},
   {"id": "only_one_part", "description": "Multiplies or divides only the numerator, or only the denominator."},
   {"id": "not_fully_simplified", "description": "Stops simplifying too early (12/18 = 6/9), or does not know when a fraction is in its simplest form."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_what_is_equivalent", "type": "recall", "step": {
     "id": "qb_what_is_equivalent", "type": "choice",
     "prompt": T("What are equivalent fractions?", "مساوی کسور کسے کہتے ہیں؟"),
     "options": [
       opt("a", "Fractions that show the same amount, like 1/2 and 2/4.", "وہ کسور جو ایک جتنی مقدار دکھائیں، جیسے 1/2 اور 2/4۔", True,
           "Yes! Same amount, just cut into a different number of pieces.", "جی ہاں! مقدار ایک جتنی، بس ٹکڑوں کی تعداد مختلف۔"),
       opt("b", "Fractions with the same denominator, like 1/5 and 3/5.", "ایک جیسے نسب نما والی کسور، جیسے 1/5 اور 3/5۔", False,
           "1/5 and 3/5 have the same denominator, but 3/5 is more. Equivalent means the same amount.", "1/5 اور 3/5 کا نسب نما ایک ہے، لیکن 3/5 زیادہ ہے۔ مساوی کا مطلب ہے ایک جتنی مقدار۔"),
       opt("c", "Fractions with the same numerator, like 2/3 and 2/7.", "ایک جیسے شمار کنندہ والی کسور، جیسے 2/3 اور 2/7۔", False,
           "2/3 is much more than 2/7: sevenths are smaller pieces. Equivalent means the same amount.", "2/3 تو 2/7 سے بہت زیادہ ہے: ساتویں حصے چھوٹے ٹکڑے ہیں۔ مساوی کا مطلب ہے ایک جتنی مقدار۔"),
     ]}},
   {"id": "qb_simplify_ten_fifteenths", "type": "apply", "step": fraction_question(
     "qb_simplify_ten_fifteenths",
     T("Write 10/15 in its simplest form.", "10/15 کو سادہ ترین شکل میں لکھیں۔"),
     frac(F(10, 15)),
     T("Which number divides both 10 and 15?", "کون سا عدد 10 اور 15 دونوں کو تقسیم کرتا ہے؟"),
     T("Right! Divide both by 5: 10/15 = 2/3.", "درست! دونوں کو 5 سے تقسیم کریں: 10/15 = 2/3"),
     T("5 divides both: 10 ÷ 5 = 2 and 15 ÷ 5 = 3, so 10/15 = 2/3.", "5 دونوں کو تقسیم کرتا ہے: 10 ÷ 5 = 2 اور 15 ÷ 5 = 3، اس لیے 10/15 = 2/3"),
     common_wrong=[wrong("2/15", "You divided only the top. Divide the bottom by 5 too.", "آپ نے صرف اوپر والے عدد کو تقسیم کیا۔ نیچے والے کو بھی 5 سے تقسیم کریں۔", "only_one_part")],
     qtype=None)},
   {"id": "qb_find_error_add", "type": "find_error", "step": {
     "id": "qb_find_error_add", "type": "choice",
     "prompt": T("Sana says 3/4 = 5/6, because she added 2 to the top and 2 to the bottom. Is she right?", "ثنا کہتی ہے 3/4 = 5/6، کیونکہ اس نے اوپر اور نیچے دونوں میں 2 جمع کیے۔ کیا وہ درست ہے؟"),
     "options": [
       opt("no", "No. Adding changes the amount; she must multiply both by the same number, e.g. 3/4 = 9/12.", "نہیں۔ جمع کرنے سے مقدار بدل جاتی ہے؛ دونوں کو ایک ہی عدد سے ضرب دینی چاہیے، جیسے 3/4 = 9/12۔", True,
           "Right! 3/4 = 9/12 (multiply both by 3), but 5/6 is a different amount.", "درست! 3/4 = 9/12 (دونوں کو 3 سے ضرب)، لیکن 5/6 مختلف مقدار ہے۔"),
       opt("yes", "Yes. She did the same thing to the top and the bottom.", "ہاں۔ اس نے اوپر اور نیچے ایک جیسا کام کیا۔", False,
           "Doing the same thing only works for × and ÷. Adding 2 changes the amount.", "ایک جیسا کام صرف × اور ÷ سے ٹھیک رہتا ہے۔ 2 جمع کرنے سے مقدار بدل جاتی ہے۔", "add_same_number"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_make_equivalent", "front": T("How do you make an equivalent fraction?", "مساوی کسر کیسے بناتے ہیں؟"),
    "back": T("Multiply (or divide) the numerator and the denominator by the same number. 1/2 = 2/4 = 4/8", "شمار کنندہ اور نسب نما دونوں کو ایک ہی عدد سے ضرب (یا تقسیم) دیں۔ 1/2 = 2/4 = 4/8")},
   {"id": "f_simplest_form", "front": T("When is a fraction in its simplest form?", "کسر سادہ ترین شکل میں کب ہوتی ہے؟"),
    "back": T("When no number except 1 divides both the top and the bottom. 2/3 is simplest; 6/9 is not (3 divides both).", "جب 1 کے سوا کوئی عدد اوپر اور نیچے دونوں کو تقسیم نہ کرے۔ 2/3 سادہ ترین ہے؛ 6/9 نہیں (3 دونوں کو تقسیم کرتا ہے)۔")},
 ],
 "home_tasks": [{"id": "h_fold_paper", "text": T(
   "Fold a sheet of paper in half and colour one half. Now fold it in half again, and again. Count the pieces and the coloured pieces each time. Write the three fractions. Are they the same amount?",
   "کاغذ کو آدھا تہہ کریں اور ایک آدھا رنگ دیں۔ اب اسے پھر آدھا تہہ کریں، اور ایک بار پھر۔ ہر بار کل ٹکڑے اور رنگے ہوئے ٹکڑے گنیں۔ تینوں کسور لکھیں۔ کیا یہ ایک جتنی مقدار ہیں؟")}],
 "glossary": [T("Fraction", "کسر"), T("Numerator", "شمار کنندہ"), T("Denominator", "نسب نما"),
              T("Equivalent fractions", "مساوی کسور"), T("Simplest form (lowest terms)", "سادہ ترین شکل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Zara cut her roti into 2 pieces and ate 1. Ali cut his into 4 pieces and ate 2. Who ate more?",
      "زارا نے اپنی روٹی کے 2 ٹکڑے کیے اور 1 کھایا۔ علی نے اپنی روٹی کے 4 ٹکڑے کیے اور 2 کھائے۔ زیادہ کس نے کھایا؟"),
    "text": T("Both rotis are the same size. Let's find out together. First, a quick check.",
              "دونوں روٹیاں ایک جتنی ہیں۔ آئیں مل کر معلوم کریں۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": UNIT_FRACTIONS,
    "prompt": T("A paratha is cut into 4 equal pieces. Ayesha eats 3 of them. What fraction of the paratha did she eat?",
                "ایک پراٹھے کے 4 برابر ٹکڑے کیے گئے۔ عائشہ نے ان میں سے 3 کھائے۔ اس نے پراٹھے کا کتنا حصہ کھایا؟"),
    "options": [
      opt("three_quarters", "3/4", "3/4", True,
          "Yes! 3 of the 4 equal pieces: 3/4. The 3 on top is the numerator and the 4 below is the denominator.",
          "جی ہاں! 4 برابر ٹکڑوں میں سے 3: یعنی 3/4۔ اوپر والا 3 شمار کنندہ ہے اور نیچے والا 4 نسب نما۔"),
      opt("four_thirds", "4/3", "4/3", False,
          "The bottom number says how many equal pieces the paratha has (4). The top says how many she ate (3).",
          "نیچے والا عدد بتاتا ہے کہ پراٹھے کے کتنے برابر ٹکڑے ہیں (4)۔ اوپر والا بتاتا ہے کہ اس نے کتنے کھائے (3)۔"),
      opt("one_quarter", "1/4", "1/4", False,
          "1/4 is one piece. Ayesha ate 3 pieces.", "1/4 ایک ٹکڑا ہے۔ عائشہ نے 3 ٹکڑے کھائے۔"),
    ]},
   {"id": "s3_predict", "type": "choice",
    "prompt": T("Guess first: Zara ate 1/2 of her roti. Ali ate 2/4 of his. Who ate more?",
                "پہلے اندازہ لگائیں: زارا نے اپنی روٹی کا 1/2 کھایا۔ علی نے اپنی روٹی کا 2/4 کھایا۔ زیادہ کس نے کھایا؟"),
    "options": [
      opt("ali", "Ali: 2 and 4 are bigger numbers", "علی: 2 اور 4 بڑے عدد ہیں", False,
          "Many people think bigger numbers mean more roti. But Ali's pieces are smaller. Let's test it.",
          "بہت سے لوگ سمجھتے ہیں کہ بڑے عدد کا مطلب زیادہ روٹی ہے۔ لیکن علی کے ٹکڑے چھوٹے ہیں۔ آئیں جانچیں۔", "bigger_numbers_bigger"),
      opt("zara", "Zara: her piece is bigger", "زارا: اس کا ٹکڑا بڑا ہے", False,
          "Her one piece is bigger, but Ali ate two pieces. Let's test it.", "اس کا ایک ٹکڑا بڑا ہے، لیکن علی نے دو ٹکڑے کھائے۔ آئیں جانچیں۔"),
      opt("same", "They ate the same amount", "دونوں نے برابر کھایا", True,
          "Good thinking! Let's check it with a roti.", "بہت خوب سوچا! آئیں روٹی سے جانچیں۔"),
    ]},
   {"id": "s4_test_it", "type": "sim", "question_type": "apply", "renderer": "native", "sim_id": "fraction_bars",
    "prompt": T("Test your guess. Use + to cut the roti into 4 pieces. Then tap the pieces that make half the roti. Press Check.",
                "اپنا اندازہ آزمائیں۔ + دبا کر روٹی کے 4 ٹکڑے کریں۔ پھر وہ ٹکڑے چھوئیں جو آدھی روٹی بناتے ہیں۔ \"جانچیں\" دبائیں۔"),
    "params": {"wholes": 1, "max_cut": 8},
    "expected": {"result": "pieces", "checker": "numeric", "answer": frac(HALF_IN_QUARTERS)},
    "hint": T("Half the roti is the left side. How many quarters cover it?", "آدھی روٹی بائیں طرف کا حصہ ہے۔ کتنی چوتھائیاں اسے ڈھانپتی ہیں؟"),
    "feedback_correct": T("Yes! 2 quarters cover half the roti. So 2/4 = 1/2: Zara and Ali ate the same amount.",
                          "جی ہاں! 2 چوتھائیاں آدھی روٹی ڈھانپ لیتی ہیں۔ یعنی 2/4 = 1/2: زارا اور علی نے برابر کھایا۔"),
    "feedback_wrong": T("Cut the roti into 4. The 2 pieces on the left cover half of it, so 2/4 = 1/2.",
                        "روٹی کے 4 ٹکڑے کریں۔ بائیں طرف کے 2 ٹکڑے آدھی روٹی ڈھانپتے ہیں، یعنی 2/4 = 1/2"),
    "common_wrong": [wrong("1", "That is one quarter, 1/4. Half the roti is more than that.", "یہ ایک چوتھائی، یعنی 1/4 ہے۔ آدھی روٹی اس سے زیادہ ہے۔")]},
   {"id": "s5_see_it", "type": "explain",
    "character": say("happy", "Same amount of roti, just more pieces!", "روٹی اتنی ہی ہے، بس ٹکڑے زیادہ ہیں!"),
    "text": T("1/2 and 2/4 cover the same amount. Cut each quarter in half and you get 4/8, still the same. So 1/2 = 2/4 = 4/8. These are called equivalent fractions. To make one, multiply the numerator and the denominator by the same number: 1/2 = (1 × 2)/(2 × 2) = 2/4.",
              "1/2 اور 2/4 ایک جتنی جگہ ڈھانپتے ہیں۔ ہر چوتھائی کو آدھا کاٹیں تو 4/8 بنتا ہے، پھر بھی اتنا ہی۔ یعنی 1/2 = 2/4 = 4/8۔ انہیں مساوی کسور کہتے ہیں۔ مساوی کسر بنانے کے لیے شمار کنندہ اور نسب نما دونوں کو ایک ہی عدد سے ضرب دیں: 1/2 = (1 × 2)/(2 × 2) = 2/4")},
   {"id": "s6_fill_gap", "type": "number", "question_type": "apply",
    "prompt": T("Fill the gap: 2/3 = ?/12. What is the missing numerator?", "خالی جگہ پُر کریں: 2/3 = ?/12۔ غائب شمار کنندہ کیا ہے؟"),
    "answer": int(GAP_TOP), "checker": "numeric",
    "hint": T("3 × 4 = 12. Do the same to the top.", "3 × 4 = 12۔ اوپر والے عدد کے ساتھ بھی یہی کریں۔"),
    "feedback_correct": T("Right! 2/3 = (2 × 4)/(3 × 4) = 8/12.", "درست! 2/3 = (2 × 4)/(3 × 4) = 8/12"),
    "feedback_wrong": T("The bottom was multiplied by 4 (3 × 4 = 12), so multiply the top by 4 too: 2 × 4 = 8. 2/3 = 8/12.",
                        "نیچے والے عدد کو 4 سے ضرب دی گئی (3 × 4 = 12)، اس لیے اوپر والے کو بھی 4 سے ضرب دیں: 2 × 4 = 8۔ 2/3 = 8/12"),
    "common_wrong": [
      wrong(GAP_ADDED, "You added 9 to the top because 3 + 9 = 12. But we must multiply, not add: 3 × 4 = 12.",
            "آپ نے اوپر 9 جمع کیا کیونکہ 3 + 9 = 12۔ لیکن ہمیں ضرب دینی ہے، جمع نہیں: 3 × 4 = 12", "add_same_number"),
      wrong(2, "If the top stays 2, the pieces get smaller but you don't get more of them. Multiply the top by 4 too.",
            "اگر اوپر 2 ہی رہے تو ٹکڑے چھوٹے ہو جاتے ہیں مگر زیادہ نہیں ملتے۔ اوپر والے کو بھی 4 سے ضرب دیں۔", "only_one_part"),
    ]},
   {"id": "s7_simplest", "type": "explain",
    "character": say("thinking", "Can we go the other way, to fewer pieces?", "کیا ہم الٹی طرف جا کر کم ٹکڑے بنا سکتے ہیں؟"),
    "text": T("Yes: divide the numerator and the denominator by the same number. 6/8: 2 divides both, so 6/8 = (6 ÷ 2)/(8 ÷ 2) = 3/4. Now no number except 1 divides both 3 and 4, so 3/4 is in its simplest form (lowest terms).",
              "جی ہاں: شمار کنندہ اور نسب نما دونوں کو ایک ہی عدد سے تقسیم کریں۔ 6/8 میں 2 دونوں کو تقسیم کرتا ہے، اس لیے 6/8 = (6 ÷ 2)/(8 ÷ 2) = 3/4۔ اب 1 کے سوا کوئی عدد 3 اور 4 دونوں کو تقسیم نہیں کرتا، اس لیے 3/4 سادہ ترین شکل میں ہے۔")},
   fraction_question(
     "s8_simplify",
     T("Bilal coloured 12 of the 18 squares on his chart: 12/18. Write 12/18 in its simplest form.",
       "بلال نے اپنے چارٹ کے 18 خانوں میں سے 12 رنگے: 12/18۔ 12/18 کو سادہ ترین شکل میں لکھیں۔"),
     frac(CHART),
     T("Divide both by 2, then look again: can you divide by 3?", "دونوں کو 2 سے تقسیم کریں، پھر دوبارہ دیکھیں: کیا 3 سے تقسیم ہو سکتا ہے؟"),
     T("Well done! 12/18 = 6/9 = 2/3. You can also divide by 6 in one go.", "شاباش! 12/18 = 6/9 = 2/3۔ آپ ایک ہی بار میں 6 سے بھی تقسیم کر سکتے ہیں۔"),
     T("6 divides both 12 and 18: 12 ÷ 6 = 2 and 18 ÷ 6 = 3. So 12/18 = 2/3.", "6، 12 اور 18 دونوں کو تقسیم کرتا ہے: 12 ÷ 6 = 2 اور 18 ÷ 6 = 3۔ اس لیے 12/18 = 2/3"),
     common_wrong=[
       wrong(unsimplified(2, 18), "You divided only the top by 6. Divide the bottom by 6 too.", "آپ نے صرف اوپر والے عدد کو 6 سے تقسیم کیا۔ نیچے والے کو بھی 6 سے تقسیم کریں۔", "only_one_part"),
     ]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hamza says 1/2 = 2/3, because he added 1 to the top and 1 to the bottom. What went wrong?",
                "حمزہ کہتا ہے 1/2 = 2/3، کیونکہ اس نے اوپر بھی 1 جمع کیا اور نیچے بھی 1۔ اس سے کیا غلطی ہوئی؟"),
    "options": [
      opt("added", "Adding changes the amount. He should multiply both by the same number: 1/2 = 2/4.", "جمع کرنے سے مقدار بدل جاتی ہے۔ اسے دونوں کو ایک ہی عدد سے ضرب دینی چاہیے: 1/2 = 2/4", True,
          "Yes! 2/3 is more than 1/2. Multiplying both by 2 gives 2/4, the same amount as 1/2.", "جی ہاں! 2/3، 1/2 سے زیادہ ہے۔ دونوں کو 2 سے ضرب دینے سے 2/4 بنتا ہے، جو 1/2 کے برابر ہے۔"),
      opt("nothing", "Nothing. He did the same to the top and the bottom.", "کوئی غلطی نہیں۔ اس نے اوپر اور نیچے ایک جیسا کام کیا۔", False,
          "Check with a roti: 2 of 3 pieces is more than half. Doing the same only works with × and ÷.", "روٹی سے جانچیں: 3 میں سے 2 ٹکڑے آدھی سے زیادہ ہیں۔ ایک جیسا کام صرف × اور ÷ سے ٹھیک رہتا ہے۔", "add_same_number"),
      opt("top_only", "He should have changed only the top: 2/2.", "اسے صرف اوپر والا عدد بدلنا چاہیے تھا: 2/2", False,
          "2/2 is a whole roti! Change both numbers, by multiplying.", "2/2 تو پوری روٹی ہے! دونوں عدد بدلیں، ضرب دے کر۔", "only_one_part"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? 6/8 has bigger numbers, so isn't it more than 3/4?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ 6/8 میں عدد بڑے ہیں، تو کیا یہ 3/4 سے زیادہ نہیں؟"),
    "task": T("In your own words: why are 3/4 and 6/8 of a roti the same amount? Explain it to a friend.",
              "اپنے الفاظ میں بتائیں: روٹی کا 3/4 اور 6/8 ایک جتنی مقدار کیوں ہیں؟ کسی دوست کو سمجھائیں۔"),
    "key_idea": "6/8 is 3/4 with every piece cut in two: there are twice as many pieces, but each piece is half the size, so the amount is the same. In numbers, the numerator and the denominator are both multiplied by 2.",
    "levels": {
      "got_it": "Says the amount is the same because each quarter is cut into 2 smaller pieces (eighths), so there are twice as many pieces that are half the size; or that top and bottom are both multiplied by 2.",
      "partly": "Says they are the same, or mentions multiplying by 2 or more pieces, but does not link more pieces with smaller pieces.",
      "not_yet": "Says 6/8 is more because the numbers are bigger, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["same", "equal", "برابر", "ایک جتن", "اتنی", "barabar", "ek jitn", "utni", "itni"],
      ["piece", "cut", "smaller", "eighth", "ٹکڑ", "کاٹ", "چھوٹ", "آٹھو", "tukr", "tukd", "kaat", "chhot", "chot"],
      ["multiply", "double", "twice", "× 2", "x 2", "times 2", "ضرب", "دگن", "دو گنا", "zarb", "dugn", "do guna"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Each quarter is cut into 2 eighths: twice as many pieces, each half as big, so the same amount.",
                  "بہت خوب سمجھایا! ہر چوتھائی کے 2 آٹھویں حصے بنتے ہیں: ٹکڑے دگنے، مگر ہر ٹکڑا آدھا، اس لیے مقدار وہی رہی۔"),
      "partly": T("Good start! Now say what happens to the size of the pieces when there are twice as many.",
                  "اچھی شروعات! اب بتائیں کہ جب ٹکڑے دگنے ہو جائیں تو ہر ٹکڑے کا سائز کیا ہوتا ہے۔"),
      "not_yet": T("Think of a roti cut into 4, with 3 pieces eaten. Now cut every piece in half. How many pieces were eaten now? Did the amount change?",
                   "سوچیں: ایک روٹی کے 4 ٹکڑے ہیں اور 3 کھائے گئے۔ اب ہر ٹکڑے کو آدھا کاٹیں۔ اب کتنے ٹکڑے کھائے گئے؟ کیا مقدار بدلی؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_which_equal", "type": "choice", "question_type": "apply",
    "prompt": T("Which fraction is equal to 3/5?", "کون سی کسر 3/5 کے برابر ہے؟"),
    "options": [
      opt("six_tenths", "6/10", "6/10", True,
          "Yes! Both numbers are multiplied by 2: 3/5 = 6/10.", "جی ہاں! دونوں عدد 2 سے ضرب ہوئے: 3/5 = 6/10"),
      opt("four_sixths", "4/6", "4/6", False,
          "4/6 is 3/5 with 1 added to the top and the bottom. Adding changes the amount.", "4/6 میں 3/5 کے اوپر اور نیچے 1 جمع کیا گیا ہے۔ جمع کرنے سے مقدار بدل جاتی ہے۔", "add_same_number"),
      opt("three_tenths", "3/10", "3/10", False,
          "Only the bottom was multiplied by 2. The pieces got smaller, so 3/10 is less.", "صرف نیچے والے عدد کو 2 سے ضرب دی گئی۔ ٹکڑے چھوٹے ہو گئے، اس لیے 3/10 کم ہے۔", "only_one_part"),
      opt("six_fifths", "6/5", "6/5", False,
          "Only the top was multiplied by 2. 6/5 is more than a whole!", "صرف اوپر والے عدد کو 2 سے ضرب دی گئی۔ 6/5 تو ایک پورے سے بھی زیادہ ہے!", "only_one_part"),
    ]},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can find fractions that look different but are the same!",
                     "اب آپ ایسی کسور ڈھونڈ سکتے ہیں جو دیکھنے میں مختلف ہیں مگر برابر ہیں!"),
    "text": T("Equivalent fractions show the same amount with a different number of pieces. Multiply or divide the numerator and the denominator by the same number. A fraction is in its simplest form when no number except 1 divides both.",
              "مساوی کسور ایک جتنی مقدار کو مختلف تعداد کے ٹکڑوں میں دکھاتی ہیں۔ شمار کنندہ اور نسب نما دونوں کو ایک ہی عدد سے ضرب یا تقسیم کریں۔ کسر سادہ ترین شکل میں تب ہوتی ہے جب 1 کے سوا کوئی عدد دونوں کو تقسیم نہ کرے۔"),
    "points": [T("1/2 = 2/4 = 4/8", "1/2 = 2/4 = 4/8"),
               T("Never add the same number to the top and bottom: that changes the amount.", "اوپر اور نیچے ایک ہی عدد کبھی جمع نہ کریں: اس سے مقدار بدل جاتی ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_fill_gap", "type": "apply", "skill": SKILL, "step": {
     "id": "r_fill_gap", "type": "number",
     "prompt": T("Fill the gap: 3/4 = ?/12.", "خالی جگہ پُر کریں: 3/4 = ?/12"),
     "answer": int(F(3, 4) * 12), "checker": "numeric",
     "hint": T("What do you multiply 4 by to get 12?", "4 کو کس عدد سے ضرب دیں تو 12 بنتا ہے؟"),
     "feedback_correct": T("Yes! 3/4 = (3 × 3)/(4 × 3) = 9/12.", "جی ہاں! 3/4 = (3 × 3)/(4 × 3) = 9/12"),
     "feedback_wrong": T("4 × 3 = 12, so multiply the top by 3 too: 3 × 3 = 9. 3/4 = 9/12.", "4 × 3 = 12، اس لیے اوپر والے کو بھی 3 سے ضرب دیں: 3 × 3 = 9۔ 3/4 = 9/12"),
     "common_wrong": [wrong(3 + (12 - 4), "You added 8 because 4 + 8 = 12. Multiply instead: 4 × 3 = 12.", "آپ نے 8 جمع کیا کیونکہ 4 + 8 = 12۔ اس کے بجائے ضرب دیں: 4 × 3 = 12", "add_same_number")]}},
   {"id": "r_simplify", "type": "apply", "skill": SKILL, "step": fraction_question(
     "r_simplify",
     T("Write 16/20 in its simplest form.", "16/20 کو سادہ ترین شکل میں لکھیں۔"),
     frac(F(16, 20)),
     T("4 divides both 16 and 20.", "4، 16 اور 20 دونوں کو تقسیم کرتا ہے۔"),
     T("Right! 16/20 = 4/5.", "درست! 16/20 = 4/5"),
     T("Divide both by 4: 16 ÷ 4 = 4 and 20 ÷ 4 = 5. So 16/20 = 4/5.", "دونوں کو 4 سے تقسیم کریں: 16 ÷ 4 = 4 اور 20 ÷ 4 = 5۔ اس لیے 16/20 = 4/5"),
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Fractions unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the file is named g6-maths-02 to sit with the dividing-fractions lesson. Fix the name and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: مساوی کسور (equivalent fractions), سادہ ترین شکل (simplest form / lowest terms), شمار کنندہ (numerator), نسب نما (denominator), چوتھائی (quarter), آٹھواں حصہ (eighth).",
   "Steps follow the lesson pattern: foundation check (s2), prediction (s3), concrete with the fraction bars (s4) then symbolic (s5, s6), simplifying (s7, s8), find the error (s9), explain (s10), new numbers (s11).",
   "Typed fractions use the fraction checker with require_simplest: an equal but unsimplified answer (like 6/9) gets 'simplify it' and does not use up an attempt.",
   "The answers were worked out with Python's fractions module in content/sources/g6-maths-02/equivalent_fractions.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

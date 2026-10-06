from math import gcd

from common import (F, T, opt, say, wrong, ratio, simplest, same_ratio, ratio_question, write,
                    REF, REVIEW, EQUIVALENT_FRACTIONS, RATIO_MEANING, RATIO_EQUIVALENT)

SKILL = RATIO_EQUIVALENT

# Lemonade: Ali uses 2 glasses of lemon juice to 5 of water, Sara 4 to 10.
assert same_ratio(2, 5, 4, 10) and same_ratio(2, 5, 6, 15)

# s5: 3 : 4 = ? : 20
GAP = 3 * (20 // 4)
assert GAP == 15 and same_ratio(3, 4, GAP, 20)
GAP_ADDED = 3 + (20 - 4)
assert GAP_ADDED == 19 and not same_ratio(3, 4, GAP_ADDED, 20)

# s6: 12 : 18 in simplest form
assert gcd(12, 18) == 6 and simplest(12, 18) == (2, 3)

# s7: 8 : 12 in simplest form; 4 : 6 is half-way.
S7 = simplest(8, 12)
assert S7 == (2, 3) and same_ratio(4, 6, 8, 12) and gcd(4, 6) == 2

# s8: 25 : 15 in simplest form.
S8 = simplest(25, 15)
assert S8 == (5, 3)

# s9: Zain adds 2 to both numbers of 2 : 3.
assert not same_ratio(2, 3, 4, 5) and same_ratio(2, 3, 4, 6)

# s11: which equals 4 : 6?
assert same_ratio(4, 6, 2, 3)
assert not same_ratio(4, 6, 6, 8) and not same_ratio(4, 6, 6, 4) and not same_ratio(4, 6, 4, 12)

# Question bank and review.
assert simplest(10, 4) == (5, 2)
assert simplest(16, 24) == (2, 3)
assert 5 * (12 // 2) == 30 and same_ratio(5, 2, 30, 12)

lesson = {
 "id": "g6-maths-06-equivalent-ratios",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Make equivalent ratios by multiplying or dividing both terms by the same number, and write a ratio in its simplest form.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Equivalent ratios", "مساوی نسبتیں"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": RATIO_MEANING}, {"skill": EQUIVALENT_FRACTIONS}],
 "misconceptions": [
   {"id": "add_same_number", "description": "Adds the same number to both terms (2 : 3 = 4 : 5) instead of multiplying or dividing."},
   {"id": "bigger_numbers_more", "description": "Thinks 4 : 10 is a stronger or bigger mix than 2 : 5 because its numbers are bigger."},
   {"id": "not_fully_simplified", "description": "Stops simplifying too early (8 : 12 = 4 : 6)."},
   {"id": "order_swapped", "description": "Swaps the two terms while simplifying (25 : 15 = 3 : 5)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_how_equivalent", "type": "recall", "step": {
     "id": "qb_how_equivalent", "type": "choice",
     "prompt": T("How do you make a ratio equivalent to 3 : 7?", "3 : 7 کے مساوی نسبت کیسے بناتے ہیں؟"),
     "options": [
       opt("a", "Multiply both numbers by the same number, like 6 : 14.", "دونوں عدد کو ایک ہی عدد سے ضرب دیں، جیسے 6 : 14۔", True,
           "Yes! 3 × 2 = 6 and 7 × 2 = 14, so 3 : 7 = 6 : 14.", "جی ہاں! 3 × 2 = 6 اور 7 × 2 = 14، اس لیے 3 : 7 = 6 : 14"),
       opt("b", "Add the same number to both, like 5 : 9.", "دونوں میں ایک ہی عدد جمع کریں، جیسے 5 : 9۔", False,
           "Adding changes the comparison. Multiply or divide both by the same number.", "جمع کرنے سے موازنہ بدل جاتا ہے۔ دونوں کو ایک ہی عدد سے ضرب یا تقسیم کریں۔", "add_same_number"),
       opt("c", "Swap them round, like 7 : 3.", "انہیں الٹ دیں، جیسے 7 : 3۔", False,
           "7 : 3 is a different ratio: the order matters.", "7 : 3 ایک مختلف نسبت ہے: ترتیب اہم ہے۔", "order_swapped"),
     ]}},
   {"id": "qb_simplify", "type": "apply", "step": ratio_question(
     "qb_simplify",
     T("Write 10 : 4 in its simplest form.", "10 : 4 کو سادہ ترین شکل میں لکھیں۔"),
     *simplest(10, 4),
     T("Which number divides both 10 and 4?", "کون سا عدد 10 اور 4 دونوں کو تقسیم کرتا ہے؟"),
     T("Right! Divide both by 2: 10 : 4 = 5 : 2.", "درست! دونوں کو 2 سے تقسیم کریں: 10 : 4 = 5 : 2"),
     T("2 divides both: 10 ÷ 2 = 5 and 4 ÷ 2 = 2, so 10 : 4 = 5 : 2.", "2 دونوں کو تقسیم کرتا ہے: 10 ÷ 2 = 5 اور 4 ÷ 2 = 2، اس لیے 10 : 4 = 5 : 2"),
     common_wrong=[wrong("2:5", "Keep the order: 10 was first, so its part (5) stays first.", "ترتیب برقرار رکھیں: 10 پہلے تھا، اس لیے اس کا حصہ (5) پہلے رہے گا۔", "order_swapped")],
     qtype=None)},
   {"id": "qb_find_error_add", "type": "find_error", "step": {
     "id": "qb_find_error_add", "type": "choice",
     "prompt": T("Rida says 1 : 3 = 4 : 6, because she added 3 to both numbers. Is she right?", "ردا کہتی ہے 1 : 3 = 4 : 6، کیونکہ اس نے دونوں عدد میں 3 جمع کیا۔ کیا وہ درست ہے؟"),
     "options": [
       opt("no", "No. She must multiply both by the same number: 1 : 3 = 2 : 6.", "نہیں۔ اسے دونوں کو ایک ہی عدد سے ضرب دینی چاہیے: 1 : 3 = 2 : 6", True,
           "Right! 1 : 3 = 2 : 6 (both × 2). 4 : 6 is a different ratio.", "درست! 1 : 3 = 2 : 6 (دونوں × 2)۔ 4 : 6 ایک مختلف نسبت ہے۔"),
       opt("yes", "Yes. She did the same to both numbers.", "ہاں۔ اس نے دونوں عدد کے ساتھ ایک جیسا کام کیا۔", False,
           "Doing the same only works with × and ÷. Adding changes the ratio.", "ایک جیسا کام صرف × اور ÷ سے ٹھیک رہتا ہے۔ جمع کرنے سے نسبت بدل جاتی ہے۔", "add_same_number"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_equivalent", "front": T("How do you make an equivalent ratio?", "مساوی نسبت کیسے بناتے ہیں؟"),
    "back": T("Multiply or divide both numbers by the same number. 2 : 5 = 4 : 10 = 6 : 15", "دونوں عدد کو ایک ہی عدد سے ضرب یا تقسیم دیں۔ 2 : 5 = 4 : 10 = 6 : 15")},
   {"id": "f_simplest", "front": T("When is a ratio in its simplest form?", "نسبت سادہ ترین شکل میں کب ہوتی ہے؟"),
    "back": T("When no number except 1 divides both numbers. 2 : 3 is simplest; 8 : 12 is not (4 divides both).", "جب 1 کے سوا کوئی عدد دونوں کو تقسیم نہ کرے۔ 2 : 3 سادہ ترین ہے؛ 8 : 12 نہیں (4 دونوں کو تقسیم کرتا ہے)۔")},
 ],
 "home_tasks": [{"id": "h_sharbat", "text": T(
   "Make sharbat with an adult: 1 spoon of syrup to 4 spoons of water. Now make twice as much. How many spoons of each do you need? Does it taste the same?",
   "کسی بڑے کے ساتھ شربت بنائیں: 1 چمچ شربت اور 4 چمچ پانی۔ اب دگنا بنائیں۔ ہر ایک کے کتنے چمچ چاہییں؟ کیا ذائقہ ایک جیسا ہے؟")}],
 "glossary": [T("Ratio", "نسبت"), T("Equivalent ratios", "مساوی نسبتیں"), T("Simplest form", "سادہ ترین شکل"), T("Term (of a ratio)", "نسبت کا رکن")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Ali makes lemonade with 2 glasses of lemon juice and 5 of water. Sara uses 4 and 10. Whose lemonade is stronger?",
      "علی 2 گلاس لیموں کے رس اور 5 گلاس پانی سے لیمونیڈ بناتا ہے۔ سارہ 4 اور 10 استعمال کرتی ہے۔ کس کا لیمونیڈ زیادہ تیز ہے؟"),
    "text": T("Let's find out. First, a quick check.", "آئیں معلوم کریں۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": RATIO_MEANING,
    "prompt": T("A cake uses 2 cups of sugar and 5 cups of flour. What is the ratio of sugar to flour?",
                "ایک کیک میں 2 کپ چینی اور 5 کپ آٹا ڈلتا ہے۔ چینی اور آٹے کی نسبت کیا ہے؟"),
    "options": [
      opt("right", "2 : 5", "2 : 5", True, "Yes! Sugar first: 2 : 5.", "جی ہاں! چینی پہلے: 2 : 5"),
      opt("swapped", "5 : 2", "5 : 2", False, "That is flour to sugar. Sugar is named first.", "یہ آٹے اور چینی کی نسبت ہے۔ چینی پہلے آئی ہے۔", "order_swapped"),
      opt("whole", "2 : 7", "2 : 7", False, "7 is all the cups. Compare sugar with flour only.", "7 تمام کپ ہیں۔ چینی کا موازنہ صرف آٹے سے کریں۔"),
    ]},
   {"id": "s3_predict", "type": "choice",
    "prompt": T("Guess first: Ali uses 2 : 5 and Sara uses 4 : 10. Whose lemonade is stronger?",
                "پہلے اندازہ لگائیں: علی 2 : 5 اور سارہ 4 : 10 استعمال کرتی ہے۔ کس کا لیمونیڈ زیادہ تیز ہے؟"),
    "options": [
      opt("sara", "Sara's: she uses more lemon juice", "سارہ کا: وہ زیادہ لیموں کا رس ڈالتی ہے", False,
          "She uses more lemon, but also more water. Let's look closely.", "وہ لیموں زیادہ ڈالتی ہے، مگر پانی بھی زیادہ۔ آئیں غور سے دیکھیں۔", "bigger_numbers_more"),
      opt("ali", "Ali's: he uses less water", "علی کا: وہ کم پانی ڈالتا ہے", False,
          "He uses less water, but also less lemon. Let's look closely.", "وہ پانی کم ڈالتا ہے، مگر لیموں بھی کم۔ آئیں غور سے دیکھیں۔"),
      opt("same", "They taste the same", "دونوں کا ذائقہ ایک جیسا ہے", True,
          "Good thinking! Let's see why.", "بہت خوب سوچا! آئیں دیکھیں کیوں۔"),
    ]},
   {"id": "s4_see_it", "type": "explain",
    "character": say("happy", "Sara just made two jugs of Ali's lemonade!", "سارہ نے بس علی والے لیمونیڈ کے دو جگ بنائے!"),
    "text": T("Sara's 4 : 10 is Ali's 2 : 5 made twice: 2 × 2 = 4 and 5 × 2 = 10. For every 2 glasses of lemon there are still 5 of water, so they taste the same. 2 : 5, 4 : 10 and 6 : 15 are equivalent ratios. To make one, multiply (or divide) both numbers by the same number, just like equivalent fractions.",
              "سارہ کا 4 : 10، علی کا 2 : 5 دو بار بنایا ہوا ہے: 2 × 2 = 4 اور 5 × 2 = 10۔ ہر 2 گلاس لیموں کے مقابلے میں اب بھی 5 گلاس پانی ہے، اس لیے ذائقہ ایک جیسا ہے۔ 2 : 5، 4 : 10 اور 6 : 15 مساوی نسبتیں ہیں۔ مساوی نسبت بنانے کے لیے دونوں عدد کو ایک ہی عدد سے ضرب (یا تقسیم) دیں، بالکل مساوی کسور کی طرح۔")},
   {"id": "s5_fill_gap", "type": "number", "question_type": "apply",
    "prompt": T("Fill the gap: 3 : 4 = ? : 20. What is the missing number?", "خالی جگہ پُر کریں: 3 : 4 = ? : 20۔ غائب عدد کیا ہے؟"),
    "answer": GAP, "checker": "numeric",
    "hint": T("4 × 5 = 20. Do the same to the 3.", "4 × 5 = 20۔ 3 کے ساتھ بھی یہی کریں۔"),
    "feedback_correct": T(f"Right! 3 × 5 = {GAP}, so 3 : 4 = {GAP} : 20.", f"درست! 3 × 5 = {GAP}، اس لیے 3 : 4 = {GAP} : 20"),
    "feedback_wrong": T(f"4 was multiplied by 5 to make 20, so multiply 3 by 5 too: 3 × 5 = {GAP}.", f"20 بنانے کے لیے 4 کو 5 سے ضرب دی گئی، اس لیے 3 کو بھی 5 سے ضرب دیں: 3 × 5 = {GAP}"),
    "common_wrong": [
      wrong(GAP_ADDED, "You added 16 because 4 + 16 = 20. Multiply instead: 4 × 5 = 20.", "آپ نے 16 جمع کیا کیونکہ 4 + 16 = 20۔ اس کے بجائے ضرب دیں: 4 × 5 = 20", "add_same_number"),
      wrong(3, "If the 3 stays the same, the mix changes. Multiply it by 5 too.", "اگر 3 ویسا ہی رہے تو آمیزہ بدل جاتا ہے۔ اسے بھی 5 سے ضرب دیں۔"),
    ]},
   {"id": "s6_simplest", "type": "explain",
    "character": say("thinking", "Big numbers are hard to compare. Can we make them smaller?", "بڑے اعداد کا موازنہ مشکل ہے۔ کیا ہم انہیں چھوٹا کر سکتے ہیں؟"),
    "text": T("Yes: divide both numbers by the same number. 12 : 18: 6 divides both, so 12 : 18 = (12 ÷ 6) : (18 ÷ 6) = 2 : 3. Now no number except 1 divides both 2 and 3, so 2 : 3 is the simplest form. Keep the order: 12 was first, so 2 stays first.",
              "جی ہاں: دونوں عدد کو ایک ہی عدد سے تقسیم کریں۔ 12 : 18 میں 6 دونوں کو تقسیم کرتا ہے، اس لیے 12 : 18 = (12 ÷ 6) : (18 ÷ 6) = 2 : 3۔ اب 1 کے سوا کوئی عدد 2 اور 3 دونوں کو تقسیم نہیں کرتا، اس لیے 2 : 3 سادہ ترین شکل ہے۔ ترتیب برقرار رکھیں: 12 پہلے تھا، اس لیے 2 پہلے رہے گا۔")},
   ratio_question(
     "s7_simplify",
     T("A class has 8 girls and 12 boys. Write the ratio of girls to boys in its simplest form.", "ایک جماعت میں 8 لڑکیاں اور 12 لڑکے ہیں۔ لڑکیوں اور لڑکوں کی نسبت سادہ ترین شکل میں لکھیں۔"),
     *S7,
     T("Divide both by 2, then look again: can you divide by 2 once more?", "دونوں کو 2 سے تقسیم کریں، پھر دوبارہ دیکھیں: کیا ایک بار پھر 2 سے تقسیم ہو سکتا ہے؟"),
     T("Well done! 8 : 12 = 4 : 6 = 2 : 3. You can also divide by 4 in one go.", "شاباش! 8 : 12 = 4 : 6 = 2 : 3۔ آپ ایک ہی بار میں 4 سے بھی تقسیم کر سکتے ہیں۔"),
     T("4 divides both: 8 ÷ 4 = 2 and 12 ÷ 4 = 3. So 8 : 12 = 2 : 3.", "4 دونوں کو تقسیم کرتا ہے: 8 ÷ 4 = 2 اور 12 ÷ 4 = 3۔ اس لیے 8 : 12 = 2 : 3"),
     common_wrong=[
       wrong("4:6", "4 : 6 is equal, but 2 still divides both. Keep going.", "4 : 6 برابر ہے، لیکن 2 اب بھی دونوں کو تقسیم کرتا ہے۔ آگے بڑھیں۔", "not_fully_simplified"),
       wrong("3:2", "Keep the order: girls (8) came first, so their part stays first.", "ترتیب برقرار رکھیں: لڑکیاں (8) پہلے تھیں، اس لیے ان کا حصہ پہلے رہے گا۔", "order_swapped"),
     ]),
   ratio_question(
     "s8_simplify_bigger_first",
     T("A farmer has 25 goats and 15 cows. Write the ratio of goats to cows in its simplest form.", "ایک کسان کے پاس 25 بکریاں اور 15 گائیں ہیں۔ بکریوں اور گایوں کی نسبت سادہ ترین شکل میں لکھیں۔"),
     *S8,
     T("Which number divides both 25 and 15?", "کون سا عدد 25 اور 15 دونوں کو تقسیم کرتا ہے؟"),
     T("Right! Divide both by 5: 25 : 15 = 5 : 3.", "درست! دونوں کو 5 سے تقسیم کریں: 25 : 15 = 5 : 3"),
     T("5 divides both: 25 ÷ 5 = 5 and 15 ÷ 5 = 3. Goats first, so 5 : 3.", "5 دونوں کو تقسیم کرتا ہے: 25 ÷ 5 = 5 اور 15 ÷ 5 = 3۔ بکریاں پہلے، اس لیے 5 : 3"),
     common_wrong=[wrong("3:5", "The goats came first (25), so their part (5) stays first: 5 : 3.", "بکریاں (25) پہلے تھیں، اس لیے ان کا حصہ (5) پہلے رہے گا: 5 : 3", "order_swapped")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Zain says 2 : 3 = 4 : 5, because he added 2 to both numbers. What went wrong?",
                "زین کہتا ہے 2 : 3 = 4 : 5، کیونکہ اس نے دونوں عدد میں 2 جمع کیا۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("added", "Adding changes the ratio. He should multiply both: 2 : 3 = 4 : 6.", "جمع کرنے سے نسبت بدل جاتی ہے۔ اسے دونوں کو ضرب دینی چاہیے: 2 : 3 = 4 : 6", True,
          "Yes! 2 : 3 = 4 : 6 (both × 2). 4 : 5 is a different ratio.", "جی ہاں! 2 : 3 = 4 : 6 (دونوں × 2)۔ 4 : 5 ایک مختلف نسبت ہے۔"),
      opt("nothing", "Nothing. He did the same to both numbers.", "کوئی غلطی نہیں۔ اس نے دونوں عدد کے ساتھ ایک جیسا کام کیا۔", False,
          "Doing the same only works with × and ÷. 2 : 3 = 4 : 6, not 4 : 5.", "ایک جیسا کام صرف × اور ÷ سے ٹھیک رہتا ہے۔ 2 : 3 = 4 : 6، نہ کہ 4 : 5۔", "add_same_number"),
      opt("order", "He should have swapped them: 3 : 2.", "اسے انہیں الٹ دینا چاہیے تھا: 3 : 2", False,
          "Swapping makes a different ratio. Multiply both numbers by the same number.", "الٹنے سے مختلف نسبت بنتی ہے۔ دونوں عدد کو ایک ہی عدد سے ضرب دیں۔", "order_swapped"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? 4 : 10 has bigger numbers, so isn't Sara's lemonade stronger?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ 4 : 10 میں عدد بڑے ہیں، تو کیا سارہ کا لیمونیڈ زیادہ تیز نہیں؟"),
    "task": T("In your own words: why do Ali's 2 : 5 and Sara's 4 : 10 lemonade taste the same?",
              "اپنے الفاظ میں بتائیں: علی کا 2 : 5 اور سارہ کا 4 : 10 لیمونیڈ ایک جیسا کیوں لگتا ہے؟"),
    "key_idea": "Sara doubled both the lemon juice and the water (2 × 2 = 4, 5 × 2 = 10). For every 2 glasses of lemon there are still 5 of water, so the mix, and the taste, is the same.",
    "levels": {
      "got_it": "Says both amounts were multiplied by 2 (doubled), so there is still the same amount of water for each glass of lemon; or that 4 : 10 simplifies to 2 : 5.",
      "partly": "Says they are the same, or mentions doubling, but does not say that both the lemon and the water were doubled.",
      "not_yet": "Says Sara's is stronger because the numbers are bigger, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["same", "equal", "برابر", "ایک جیس", "barabar", "ek jais"],
      ["double", "twice", "× 2", "x 2", "times 2", "multiply", "دگن", "دو گنا", "ضرب", "dugn", "do guna", "zarb"],
      ["both", "water", "lemon", "دونوں", "پانی", "لیموں", "dono", "paani", "pani", "limo"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Sara doubled both the lemon and the water, so the mix stays 2 : 5.",
                  "بہت خوب سمجھایا! سارہ نے لیموں اور پانی دونوں دگنے کیے، اس لیے آمیزہ 2 : 5 ہی رہا۔"),
      "partly": T("Good start! Now say what happened to the lemon juice and to the water.",
                  "اچھی شروعات! اب بتائیں کہ لیموں کے رس اور پانی کے ساتھ کیا ہوا۔"),
      "not_yet": T("Think: if you pour Sara's jug into two equal jugs, how much lemon and water is in each one?",
                   "سوچیں: اگر سارہ کے جگ کو دو برابر جگوں میں ڈالیں تو ہر ایک میں کتنا لیموں اور پانی ہوگا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_which_equal", "type": "choice", "question_type": "apply",
    "prompt": T("Which ratio is equal to 4 : 6?", "کون سی نسبت 4 : 6 کے برابر ہے؟"),
    "options": [
      opt("two_three", "2 : 3", "2 : 3", True, "Yes! Both divided by 2: 4 : 6 = 2 : 3.", "جی ہاں! دونوں کو 2 سے تقسیم: 4 : 6 = 2 : 3"),
      opt("six_eight", "6 : 8", "6 : 8", False, "6 : 8 is 4 : 6 with 2 added to both. Adding changes the ratio.", "6 : 8 میں 4 : 6 کے دونوں عدد میں 2 جمع کیا گیا ہے۔ جمع کرنے سے نسبت بدل جاتی ہے۔", "add_same_number"),
      opt("six_four", "6 : 4", "6 : 4", False, "6 : 4 is the other way round. The order matters.", "6 : 4 الٹی ترتیب ہے۔ ترتیب اہم ہے۔", "order_swapped"),
      opt("four_twelve", "4 : 12", "4 : 12", False, "Only the second number was multiplied by 2. Change both.", "صرف دوسرے عدد کو 2 سے ضرب دی گئی۔ دونوں کو بدلیں۔"),
    ]},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can make ratios bigger or smaller and keep them the same!", "اب آپ نسبتوں کو بڑا یا چھوٹا کر کے بھی ویسا ہی رکھ سکتے ہیں!"),
    "text": T("Equivalent ratios compare in the same way: 2 : 5 = 4 : 10 = 6 : 15. Multiply or divide both numbers by the same number, and keep the order. A ratio is in its simplest form when no number except 1 divides both numbers.",
              "مساوی نسبتیں ایک ہی طرح موازنہ کرتی ہیں: 2 : 5 = 4 : 10 = 6 : 15۔ دونوں عدد کو ایک ہی عدد سے ضرب یا تقسیم دیں، اور ترتیب برقرار رکھیں۔ نسبت سادہ ترین شکل میں تب ہوتی ہے جب 1 کے سوا کوئی عدد دونوں کو تقسیم نہ کرے۔"),
    "points": [T("12 : 18 = 2 : 3 (both ÷ 6)", "12 : 18 = 2 : 3 (دونوں ÷ 6)"),
               T("Never add the same number to both: that changes the ratio.", "دونوں میں ایک ہی عدد کبھی جمع نہ کریں: اس سے نسبت بدل جاتی ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_simplify", "type": "apply", "skill": SKILL, "step": ratio_question(
     "r_simplify",
     T("Write 16 : 24 in its simplest form.", "16 : 24 کو سادہ ترین شکل میں لکھیں۔"),
     *simplest(16, 24),
     T("8 divides both 16 and 24.", "8، 16 اور 24 دونوں کو تقسیم کرتا ہے۔"),
     T("Right! 16 : 24 = 2 : 3.", "درست! 16 : 24 = 2 : 3"),
     T("Divide both by 8: 16 ÷ 8 = 2 and 24 ÷ 8 = 3. So 16 : 24 = 2 : 3.", "دونوں کو 8 سے تقسیم کریں: 16 ÷ 8 = 2 اور 24 ÷ 8 = 3۔ اس لیے 16 : 24 = 2 : 3"),
     common_wrong=[wrong("8:12", "8 : 12 is equal, but 4 still divides both. Keep going.", "8 : 12 برابر ہے، لیکن 4 اب بھی دونوں کو تقسیم کرتا ہے۔ آگے بڑھیں۔", "not_fully_simplified"),
                   wrong("4:6", "4 : 6 is equal, but 2 still divides both. Keep going.", "4 : 6 برابر ہے، لیکن 2 اب بھی دونوں کو تقسیم کرتا ہے۔ آگے بڑھیں۔", "not_fully_simplified")],
     qtype=None)},
   {"id": "r_fill_gap", "type": "apply", "skill": SKILL, "step": {
     "id": "r_fill_gap", "type": "number",
     "prompt": T("Fill the gap: 5 : 2 = ? : 12.", "خالی جگہ پُر کریں: 5 : 2 = ? : 12"),
     "answer": 30, "checker": "numeric",
     "hint": T("What do you multiply 2 by to get 12?", "2 کو کس عدد سے ضرب دیں تو 12 بنتا ہے؟"),
     "feedback_correct": T("Yes! Both × 6: 5 : 2 = 30 : 12.", "جی ہاں! دونوں × 6: 5 : 2 = 30 : 12"),
     "feedback_wrong": T("2 × 6 = 12, so multiply 5 by 6 too: 5 × 6 = 30.", "2 × 6 = 12، اس لیے 5 کو بھی 6 سے ضرب دیں: 5 × 6 = 30"),
     "common_wrong": [wrong(15, "You added 10 because 2 + 10 = 12. Multiply instead: 2 × 6 = 12.", "آپ نے 10 جمع کیا کیونکہ 2 + 10 = 12۔ اس کے بجائے ضرب دیں: 2 × 6 = 12", "add_same_number")]}},
 ],
 "teacher_notes": [
   "Written fresh for the Ratio and Proportion unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-06. Fix the names and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: مساوی نسبتیں (equivalent ratios), سادہ ترین شکل (simplest form), نسبت کا رکن (term of a ratio).",
   "Typed ratios use the text checker, which compares exactly: an equal but unsimplified ratio (like 4 : 6 for 8 : 12) has its own 'keep going' feedback but still counts as a wrong attempt.",
   "Steps: foundation (s2), prediction (s3), the idea (s4) and a missing number (s5), simplifying (s6 to s8), find the error (s9), explain (s10), new numbers (s11).",
   "The numbers were worked out in content/sources/g6-maths-06/equivalent_ratios.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
assert 15 == 5 + (12 - 2)
write(lesson)

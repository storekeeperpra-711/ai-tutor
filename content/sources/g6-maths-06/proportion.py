from common import (T, opt, say, wrong, same_ratio, missing_term, number_question, write,
                    REF, REVIEW, RATIO_EQUIVALENT, RATIO_PROPORTION)

SKILL = RATIO_PROPORTION

# The flag of Pakistan: width to length 2 : 3 (s1, s3, s8).
FLAG_W, FLAG_L = 2, 3
assert missing_term(FLAG_W, FLAG_L, 20) == 30
FLAG_8 = missing_term(FLAG_W, FLAG_L, 40)
assert FLAG_8 == 60
assert 3 + (40 - 2) == 41

# s3: extremes and means of 2 : 3 :: 20 : 30
assert 2 * 30 == 3 * 20 == 60

# s4: 3 : 4 :: 9 : 12 is a proportion (although 9 - 3 != 12 - 4).
assert same_ratio(3, 4, 9, 12) and 3 * 12 == 4 * 9 and 9 - 3 != 12 - 4

# s5: which is a proportion with 2 : 5?
assert same_ratio(2, 5, 6, 15) and not same_ratio(2, 5, 5, 8) and not same_ratio(2, 5, 5, 2)

# s6: 3 : 5 :: 12 : ?
S6 = missing_term(3, 5, 12)
assert S6 == 20

# s7: 4 : 7 :: 12 : ?
S7 = missing_term(4, 7, 12)
assert S7 == 21 and 7 + (12 - 4) == 15

# s9: Asma's 2 : 3 :: 4 : 5
assert not same_ratio(2, 3, 4, 5) and 2 * 5 != 3 * 4

# s11: ? : 6 :: 10 : 15
S11 = 6 * 10 // 15
assert S11 == 4 and same_ratio(S11, 6, 10, 15) and 10 - (15 - 6) == 1

# Question bank and review.
assert missing_term(5, 8, 15) == 24
assert missing_term(3, 2, 15) == 10
assert same_ratio(4, 10, 6, 15)

lesson = {
 "id": "g6-maths-06-proportion",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise a proportion as two equal ratios, written a : b :: c : d, check it with the product of the extremes and the means, and find a missing term.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Proportion", "تناسب"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": RATIO_EQUIVALENT}],
 "misconceptions": [
   {"id": "additive_thinking", "description": "Thinks two ratios are in proportion when both terms go up by the same amount (2 : 3 :: 4 : 5), or finds a missing term by adding instead of multiplying."},
   {"id": "extremes_means_mixed", "description": "Multiplies the wrong pairs: the first and second terms instead of the extremes (first and fourth) and the means (second and third)."},
   {"id": "order_swapped", "description": "Writes the second ratio the other way round (2 : 5 :: 5 : 2)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_extremes", "type": "recall", "step": {
     "id": "qb_extremes", "type": "choice",
     "prompt": T("In the proportion 1 : 4 :: 3 : 12, which numbers are the extremes?", "تناسب 1 : 4 :: 3 : 12 میں طرفین کون سے ہیں؟"),
     "options": [
       opt("a", "1 and 12 (the outside numbers)", "1 اور 12 (باہر والے عدد)", True,
           "Yes! The extremes are the first and last terms. 1 × 12 = 12 and the means give 4 × 3 = 12.", "جی ہاں! طرفین پہلا اور آخری رکن ہیں۔ 1 × 12 = 12 اور وسطین سے 4 × 3 = 12"),
       opt("b", "4 and 3 (the inside numbers)", "4 اور 3 (اندر والے عدد)", False,
           "4 and 3 are the means, in the middle. The extremes are on the outside: 1 and 12.", "4 اور 3 وسطین ہیں، درمیان میں۔ طرفین باہر ہیں: 1 اور 12", "extremes_means_mixed"),
       opt("c", "1 and 4 (the first ratio)", "1 اور 4 (پہلی نسبت)", False,
           "1 and 4 make the first ratio. The extremes are the first and the last terms: 1 and 12.", "1 اور 4 پہلی نسبت بناتے ہیں۔ طرفین پہلا اور آخری رکن ہیں: 1 اور 12", "extremes_means_mixed"),
     ]}},
   {"id": "qb_missing", "type": "apply", "step": number_question(
     "qb_missing",
     T("Find the missing term: 5 : 8 :: 15 : ?", "غائب رکن معلوم کریں: 5 : 8 :: 15 : ?"),
     missing_term(5, 8, 15),
     T("5 × 3 = 15. Do the same to the 8.", "5 × 3 = 15۔ 8 کے ساتھ بھی یہی کریں۔"),
     T("Right! 8 × 3 = 24, so 5 : 8 :: 15 : 24.", "درست! 8 × 3 = 24، اس لیے 5 : 8 :: 15 : 24"),
     T("5 was multiplied by 3 to make 15, so multiply 8 by 3: 24.", "15 بنانے کے لیے 5 کو 3 سے ضرب دی گئی، اس لیے 8 کو بھی 3 سے ضرب دیں: 24"),
     common_wrong=[wrong(18, "You added 10 because 5 + 10 = 15. Multiply instead: 5 × 3 = 15.", "آپ نے 10 جمع کیا کیونکہ 5 + 10 = 15۔ اس کے بجائے ضرب دیں: 5 × 3 = 15", "additive_thinking")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Danish says 1 : 2 :: 3 : 4 is a proportion, because both ratios go up by 1. Is he right?", "دانش کہتا ہے 1 : 2 :: 3 : 4 تناسب ہے، کیونکہ دونوں نسبتوں میں 1 کا فرق ہے۔ کیا وہ درست ہے؟"),
     "options": [
       opt("no", "No. 1 × 4 = 4 but 2 × 3 = 6, so the ratios are not equal.", "نہیں۔ 1 × 4 = 4 لیکن 2 × 3 = 6، اس لیے نسبتیں برابر نہیں۔", True,
           "Right! 1 : 2 means double; 3 : 4 is not double. 1 : 2 :: 3 : 6 would be a proportion.", "درست! 1 : 2 کا مطلب دگنا ہے؛ 3 : 4 دگنا نہیں۔ 1 : 2 :: 3 : 6 تناسب ہوتا۔"),
       opt("yes", "Yes. The gap is the same in both ratios.", "ہاں۔ دونوں نسبتوں میں فرق ایک جیسا ہے۔", False,
           "A ratio is about times, not gaps. Check: 1 × 4 = 4 but 2 × 3 = 6.", "نسبت گنا کا معاملہ ہے، فرق کا نہیں۔ جانچیں: 1 × 4 = 4 لیکن 2 × 3 = 6", "additive_thinking"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_proportion", "front": T("What is a proportion?", "تناسب کیا ہے؟"),
    "back": T("Two equal ratios. 2 : 3 :: 20 : 30, read \"2 is to 3 as 20 is to 30\".", "دو برابر نسبتیں۔ 2 : 3 :: 20 : 30، پڑھیں \"2 کی نسبت 3 سے وہی ہے جو 20 کی 30 سے\"۔")},
   {"id": "f_check", "front": T("How do you check a proportion?", "تناسب کو کیسے جانچتے ہیں؟"),
    "back": T("Product of the extremes = product of the means. 2 : 3 :: 20 : 30 → 2 × 30 = 60 and 3 × 20 = 60.", "طرفین کا حاصل ضرب = وسطین کا حاصل ضرب۔ 2 : 3 :: 20 : 30 ← 2 × 30 = 60 اور 3 × 20 = 60")},
 ],
 "home_tasks": [{"id": "h_flag", "text": T(
   "The flag of Pakistan has width to length 2 : 3. Draw a flag 4 boxes wide on squared paper. How many boxes long must it be? Draw it and colour it.",
   "پاکستان کے جھنڈے کی چوڑائی اور لمبائی کی نسبت 2 : 3 ہے۔ خانوں والے کاغذ پر 4 خانے چوڑا جھنڈا بنائیں۔ یہ کتنے خانے لمبا ہونا چاہیے؟ بنا کر رنگ کریں۔")}],
 "glossary": [T("Proportion", "تناسب"), T("Extremes", "طرفین"), T("Means", "وسطین"), T("Term", "رکن")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Every flag of Pakistan has the same shape: width to length 2 : 3. A school flag is 20 cm wide. How long is it?",
      "پاکستان کے ہر جھنڈے کی شکل ایک جیسی ہے: چوڑائی اور لمبائی 2 : 3۔ سکول کا جھنڈا 20 سینٹی میٹر چوڑا ہے۔ یہ کتنا لمبا ہے؟"),
    "text": T("Big flag or small flag, the ratio stays the same. Let's see how. First, a quick check.",
              "جھنڈا بڑا ہو یا چھوٹا، نسبت وہی رہتی ہے۔ آئیں دیکھیں کیسے۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": RATIO_EQUIVALENT,
    "prompt": T("Which ratio is equal to 2 : 3?", "کون سی نسبت 2 : 3 کے برابر ہے؟"),
    "options": [
      opt("four_six", "4 : 6", "4 : 6", True, "Yes! Both × 2: 2 : 3 = 4 : 6.", "جی ہاں! دونوں × 2: 2 : 3 = 4 : 6"),
      opt("three_four", "3 : 4", "3 : 4", False, "3 : 4 adds 1 to both. Adding changes the ratio.", "3 : 4 میں دونوں میں 1 جمع کیا گیا۔ جمع کرنے سے نسبت بدل جاتی ہے۔", "additive_thinking"),
      opt("three_two", "3 : 2", "3 : 2", False, "3 : 2 is the other way round.", "3 : 2 الٹی ترتیب ہے۔", "order_swapped"),
    ]},
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "Two equal ratios make a proportion!", "دو برابر نسبتیں مل کر تناسب بناتی ہیں!"),
    "text": T("The school flag is 20 cm wide and 30 cm long: 2 : 3 = 20 : 30 (both × 10). Two equal ratios make a proportion, written 2 : 3 :: 20 : 30 and read \"2 is to 3 as 20 is to 30\". The outside terms (2 and 30) are the extremes; the inside terms (3 and 20) are the means. In a proportion, extremes × extremes = means × means: 2 × 30 = 60 and 3 × 20 = 60.",
              "سکول کا جھنڈا 20 سینٹی میٹر چوڑا اور 30 سینٹی میٹر لمبا ہے: 2 : 3 = 20 : 30 (دونوں × 10)۔ دو برابر نسبتیں تناسب بناتی ہیں، 2 : 3 :: 20 : 30 لکھا اور \"2 کی نسبت 3 سے وہی ہے جو 20 کی 30 سے\" پڑھا جاتا ہے۔ باہر والے رکن (2 اور 30) طرفین ہیں؛ اندر والے (3 اور 20) وسطین۔ تناسب میں طرفین کا حاصل ضرب = وسطین کا حاصل ضرب: 2 × 30 = 60 اور 3 × 20 = 60")},
   {"id": "s4_check", "type": "choice", "question_type": "apply",
    "prompt": T("Is 3 : 4 :: 9 : 12 a proportion?", "کیا 3 : 4 :: 9 : 12 تناسب ہے؟"),
    "options": [
      opt("yes", "Yes: 3 × 12 = 36 and 4 × 9 = 36.", "ہاں: 3 × 12 = 36 اور 4 × 9 = 36", True,
          "Right! Extremes 3 × 12 = 36, means 4 × 9 = 36. Both ratios are 3 : 4 (9 : 12 is 3 : 4 × 3).", "درست! طرفین 3 × 12 = 36، وسطین 4 × 9 = 36۔ دونوں نسبتیں 3 : 4 ہیں (9 : 12 = 3 : 4 × 3)۔"),
      opt("gap", "No: 9 − 3 = 6 but 12 − 4 = 8.", "نہیں: 9 − 3 = 6 لیکن 12 − 4 = 8", False,
          "Ratios are about times, not gaps. 3 × 3 = 9 and 4 × 3 = 12, so they are equal.", "نسبت گنا کا معاملہ ہے، فرق کا نہیں۔ 3 × 3 = 9 اور 4 × 3 = 12، اس لیے برابر ہیں۔", "additive_thinking"),
      opt("pairs", "No: 3 × 4 = 12 but 9 × 12 = 108.", "نہیں: 3 × 4 = 12 لیکن 9 × 12 = 108", False,
          "Multiply the extremes (3 and 12) and the means (4 and 9), not each ratio.", "طرفین (3 اور 12) اور وسطین (4 اور 9) کو ضرب دیں، ہر نسبت کو نہیں۔", "extremes_means_mixed"),
    ]},
   {"id": "s5_which", "type": "choice", "question_type": "apply",
    "prompt": T("Which of these is a proportion?", "ان میں سے کون سا تناسب ہے؟"),
    "options": [
      opt("right", "2 : 5 :: 6 : 15", "2 : 5 :: 6 : 15", True, "Yes! 2 × 15 = 30 and 5 × 6 = 30.", "جی ہاں! 2 × 15 = 30 اور 5 × 6 = 30"),
      opt("added", "2 : 5 :: 5 : 8", "2 : 5 :: 5 : 8", False, "Both go up by 3, but 2 × 8 = 16 and 5 × 5 = 25. Not equal.", "دونوں میں 3 بڑھا، لیکن 2 × 8 = 16 اور 5 × 5 = 25۔ برابر نہیں۔", "additive_thinking"),
      opt("swapped", "2 : 5 :: 5 : 2", "2 : 5 :: 5 : 2", False, "5 : 2 is 2 : 5 the other way round, not the same ratio.", "5 : 2، 2 : 5 کی الٹی ترتیب ہے، ایک جیسی نسبت نہیں۔", "order_swapped"),
    ]},
   {"id": "s6_missing_explain", "type": "explain",
    "character": say("thinking", "What if one term is missing? We can find it!", "اگر ایک رکن غائب ہو تو؟ ہم اسے ڈھونڈ سکتے ہیں!"),
    "text": T(f"3 : 5 :: 12 : ?. Way 1: 3 × 4 = 12, so multiply 5 by 4 too: ? = {S6}. Way 2: extremes = means, so 3 × ? = 5 × 12 = 60, and ? = 60 ÷ 3 = {S6}. Check: 3 × {S6} = 60 and 5 × 12 = 60.",
              f"3 : 5 :: 12 : ?۔ پہلا طریقہ: 3 × 4 = 12، اس لیے 5 کو بھی 4 سے ضرب دیں: ? = {S6}۔ دوسرا طریقہ: طرفین = وسطین، اس لیے 3 × ? = 5 × 12 = 60، اور ? = 60 ÷ 3 = {S6}۔ جانچیں: 3 × {S6} = 60 اور 5 × 12 = 60")},
   number_question(
     "s7_missing",
     T("Find the missing term: 4 : 7 :: 12 : ?", "غائب رکن معلوم کریں: 4 : 7 :: 12 : ?"),
     S7,
     T("4 × 3 = 12. Do the same to the 7.", "4 × 3 = 12۔ 7 کے ساتھ بھی یہی کریں۔"),
     T(f"Right! 7 × 3 = {S7}. Check: 4 × {S7} = 84 and 7 × 12 = 84.", f"درست! 7 × 3 = {S7}۔ جانچیں: 4 × {S7} = 84 اور 7 × 12 = 84"),
     T(f"4 was multiplied by 3 to make 12, so multiply 7 by 3: {S7}.", f"12 بنانے کے لیے 4 کو 3 سے ضرب دی گئی، اس لیے 7 کو بھی 3 سے ضرب دیں: {S7}"),
     common_wrong=[wrong(15, "You added 8 because 4 + 8 = 12. Multiply instead: 4 × 3 = 12.", "آپ نے 8 جمع کیا کیونکہ 4 + 8 = 12۔ اس کے بجائے ضرب دیں: 4 × 3 = 12", "additive_thinking")]),
   number_question(
     "s8_flag",
     T("A big flag of Pakistan is 40 cm wide. Width to length is 2 : 3. How long is the flag, in cm?", "پاکستان کا ایک بڑا جھنڈا 40 سینٹی میٹر چوڑا ہے۔ چوڑائی اور لمبائی 2 : 3 ہے۔ جھنڈا کتنے سینٹی میٹر لمبا ہے؟"),
     FLAG_8,
     T("2 : 3 :: 40 : ?. What do you multiply 2 by to get 40?", "2 : 3 :: 40 : ?۔ 2 کو کس عدد سے ضرب دیں تو 40 بنتا ہے؟"),
     T(f"Right! 2 × 20 = 40, so 3 × 20 = {FLAG_8} cm.", f"درست! 2 × 20 = 40، اس لیے 3 × 20 = {FLAG_8} سینٹی میٹر۔"),
     T(f"2 : 3 :: 40 : ?. 2 × 20 = 40, so the length is 3 × 20 = {FLAG_8} cm.", f"2 : 3 :: 40 : ?۔ 2 × 20 = 40، اس لیے لمبائی 3 × 20 = {FLAG_8} سینٹی میٹر۔"),
     common_wrong=[wrong(41, "Adding 38 to both doesn't keep the shape. Multiply: 2 × 20 = 40.", "دونوں میں 38 جمع کرنے سے شکل نہیں رہتی۔ ضرب دیں: 2 × 20 = 40", "additive_thinking"),
                   wrong(80, "That doubles 40, but the ratio needs 3 parts for every 2: 40 ÷ 2 × 3.", "یہ 40 کا دگنا ہے، لیکن نسبت میں ہر 2 کے مقابلے میں 3 حصے ہیں: 40 ÷ 2 × 3")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Asma says 2 : 3 :: 4 : 5 is a proportion, because both ratios go up by 2. What went wrong?",
                "عاصمہ کہتی ہے 2 : 3 :: 4 : 5 تناسب ہے، کیونکہ دونوں نسبتوں میں 2 بڑھا۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("adding", "Adding doesn't keep a ratio. 2 × 5 = 10 but 3 × 4 = 12, so it is not a proportion.", "جمع کرنے سے نسبت برقرار نہیں رہتی۔ 2 × 5 = 10 لیکن 3 × 4 = 12، اس لیے یہ تناسب نہیں۔", True,
          "Yes! 2 : 3 :: 4 : 6 would be a proportion (both × 2).", "جی ہاں! 2 : 3 :: 4 : 6 تناسب ہوتا (دونوں × 2)۔"),
      opt("nothing", "Nothing. Both went up by the same amount.", "کوئی غلطی نہیں۔ دونوں برابر بڑھے۔", False,
          "Check the extremes and means: 2 × 5 = 10, 3 × 4 = 12. Not equal.", "طرفین اور وسطین جانچیں: 2 × 5 = 10، 3 × 4 = 12۔ برابر نہیں۔", "additive_thinking"),
      opt("order", "She should write 3 : 2 :: 5 : 4.", "اسے 3 : 2 :: 5 : 4 لکھنا چاہیے۔", False,
          "Turning both round doesn't help: 3 × 4 = 12 and 2 × 5 = 10, still not equal.", "دونوں کو الٹنے سے فرق نہیں پڑتا: 3 × 4 = 12 اور 2 × 5 = 10، پھر بھی برابر نہیں۔", "order_swapped"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? How do I know the 20 cm flag must be 30 cm long?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ مجھے کیسے پتا چلے کہ 20 سینٹی میٹر والا جھنڈا 30 سینٹی میٹر لمبا ہوگا؟"),
    "task": T("In your own words: why is 2 : 3 :: 20 : 30 a proportion?", "اپنے الفاظ میں بتائیں: 2 : 3 :: 20 : 30 تناسب کیوں ہے؟"),
    "key_idea": "20 : 30 is 2 : 3 with both terms multiplied by 10, so the two ratios are equal. You can also check that the product of the extremes (2 × 30 = 60) equals the product of the means (3 × 20 = 60).",
    "levels": {
      "got_it": "Says both terms of 2 : 3 were multiplied by 10 (so the ratios are equal), or checks that 2 × 30 = 3 × 20 = 60.",
      "partly": "Says the ratios are equal or mentions 10 or 60, but does not say that both terms were multiplied by the same number or which products match.",
      "not_yet": "Says because the numbers go up, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["10", "ten", "دس", "۱۰", "das"],
      ["multiply", "times", "×", "ضرب", "گنا", "zarb", "guna"],
      ["equal", "same", "60", "برابر", "ایک جیس", "barabar", "ek jais"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Both terms are × 10, so 2 : 3 = 20 : 30, and 2 × 30 = 3 × 20 = 60.",
                  "بہت خوب سمجھایا! دونوں رکن × 10 ہیں، اس لیے 2 : 3 = 20 : 30، اور 2 × 30 = 3 × 20 = 60"),
      "partly": T("Good start! Now say what both 2 and 3 were multiplied by.", "اچھی شروعات! اب بتائیں کہ 2 اور 3 دونوں کو کس عدد سے ضرب دی گئی۔"),
      "not_yet": T("Think: what do you multiply 2 by to get 20? Do you get 30 if you multiply 3 by the same number?",
                   "سوچیں: 2 کو کس عدد سے ضرب دیں تو 20 بنتا ہے؟ کیا 3 کو اسی عدد سے ضرب دینے پر 30 بنتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_missing_first",
     T("Find the missing term: ? : 6 :: 10 : 15", "غائب رکن معلوم کریں: ? : 6 :: 10 : 15"),
     S11,
     T("Extremes = means: ? × 15 = 6 × 10.", "طرفین = وسطین: ? × 15 = 6 × 10"),
     T(f"Right! ? × 15 = 60, so ? = 60 ÷ 15 = {S11}. And {S11} : 6 = 2 : 3 = 10 : 15.", f"درست! ? × 15 = 60، اس لیے ? = 60 ÷ 15 = {S11}۔ اور {S11} : 6 = 2 : 3 = 10 : 15"),
     T(f"Means: 6 × 10 = 60. So ? × 15 = 60, and ? = 60 ÷ 15 = {S11}.", f"وسطین: 6 × 10 = 60۔ اس لیے ? × 15 = 60، اور ? = 60 ÷ 15 = {S11}"),
     common_wrong=[wrong(1, "You subtracted 9 because 15 − 9 = 6. Use extremes = means instead.", "آپ نے 9 تفریق کیا کیونکہ 15 − 9 = 6۔ اس کے بجائے طرفین = وسطین استعمال کریں۔", "additive_thinking"),
                   wrong(9, "6 × 10 = 60, then 60 ÷ 15, not 15 − 6.", "6 × 10 = 60، پھر 60 ÷ 15، نہ کہ 15 − 6۔")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can check a proportion and find a missing term!", "اب آپ تناسب جانچ سکتے ہیں اور غائب رکن ڈھونڈ سکتے ہیں!"),
    "text": T("A proportion is two equal ratios, written a : b :: c : d. The extremes are a and d; the means are b and c. In a proportion, extremes × extremes = means × means. Use this to check a proportion or to find a missing term.",
              "تناسب دو برابر نسبتیں ہیں، a : b :: c : d لکھا جاتا ہے۔ a اور d طرفین ہیں؛ b اور c وسطین۔ تناسب میں طرفین کا حاصل ضرب = وسطین کا حاصل ضرب۔ اس سے تناسب جانچیں یا غائب رکن معلوم کریں۔"),
    "points": [T("2 : 3 :: 20 : 30 → 2 × 30 = 3 × 20 = 60", "2 : 3 :: 20 : 30 ← 2 × 30 = 3 × 20 = 60"),
               T("Ratios are about times, not gaps: 2 : 3 :: 4 : 5 is not a proportion.", "نسبت گنا کا معاملہ ہے، فرق کا نہیں: 2 : 3 :: 4 : 5 تناسب نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_missing", "type": "apply", "skill": SKILL, "step": number_question(
     "r_missing",
     T("Find the missing term: 3 : 2 :: 15 : ?", "غائب رکن معلوم کریں: 3 : 2 :: 15 : ?"),
     missing_term(3, 2, 15),
     T("3 × 5 = 15.", "3 × 5 = 15"),
     T("Right! 2 × 5 = 10, so 3 : 2 :: 15 : 10.", "درست! 2 × 5 = 10، اس لیے 3 : 2 :: 15 : 10"),
     T("3 × 5 = 15, so multiply 2 by 5 too: 10.", "3 × 5 = 15، اس لیے 2 کو بھی 5 سے ضرب دیں: 10"),
     common_wrong=[wrong(14, "You added 12 because 3 + 12 = 15. Multiply instead.", "آپ نے 12 جمع کیا کیونکہ 3 + 12 = 15۔ اس کے بجائے ضرب دیں۔", "additive_thinking")],
     qtype=None)},
   {"id": "r_check", "type": "recall", "skill": SKILL, "step": {
     "id": "r_check", "type": "choice",
     "prompt": T("Is 4 : 10 :: 6 : 15 a proportion?", "کیا 4 : 10 :: 6 : 15 تناسب ہے؟"),
     "options": [
       opt("yes", "Yes: 4 × 15 = 60 and 10 × 6 = 60.", "ہاں: 4 × 15 = 60 اور 10 × 6 = 60", True,
           "Right! Both ratios are 2 : 5.", "درست! دونوں نسبتیں 2 : 5 ہیں۔"),
       opt("no", "No: 4 × 10 = 40 but 6 × 15 = 90.", "نہیں: 4 × 10 = 40 لیکن 6 × 15 = 90", False,
           "Multiply the extremes (4, 15) and the means (10, 6): 60 and 60. It is a proportion.", "طرفین (4، 15) اور وسطین (10، 6) کو ضرب دیں: 60 اور 60۔ یہ تناسب ہے۔", "extremes_means_mixed"),
     ]}},
 ],
 "teacher_notes": [
   "Written fresh for the Ratio and Proportion unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-06. Fix the names and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: تناسب (proportion), طرفین (extremes), وسطین (means), رکن (term). The proportion sign :: is read \"کی نسبت ... سے وہی ہے جو\".",
   "The flag of Pakistan's width to length ratio is 2 : 3; the lesson uses it as the context.",
   "Two ways to find a missing term are taught: scaling (×) and extremes × extremes = means × means. Every missing term is a whole number.",
   "The numbers were worked out in content/sources/g6-maths-06/proportion.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import attach, double_line, two_flags

SMALL_FLAG = {"w": 40, "l": 60, "grid": (FLAG_W, FLAG_L), "w_text": str(FLAG_W), "l_text": str(FLAG_L)}
assert SMALL_FLAG["w"] * FLAG_L == SMALL_FLAG["l"] * FLAG_W

attach(lesson, {
  "s1_hook": two_flags(
    SMALL_FLAG, {"w": 100, "l": 150, "w_text": "20cm", "l_text": "?"},
    "Two flags of the same shape. The small one is cut into 2 rows of 3 equal squares: 2 wide and 3 long. The big school flag is 20 cm wide; its length is marked with a question mark.",
    "ایک ہی شکل کے دو جھنڈے۔ چھوٹا جھنڈا 3، 3 برابر مربعوں کی 2 قطاروں میں بٹا ہے: چوڑائی 2 اور لمبائی 3۔ سکول کا بڑا جھنڈا 20 سینٹی میٹر چوڑا ہے؛ اس کی لمبائی پر سوالیہ نشان ہے۔"),
  "s3_see_it": two_flags(
    SMALL_FLAG, {"w": 100, "l": 150, "grid": (FLAG_W, FLAG_L), "w_text": "20cm", "l_text": "30cm"},
    "Two flags of the same shape, each cut into 2 rows of 3 equal squares. The small one is 2 wide and 3 long. The big school flag is 20 cm wide and 30 cm long, each square 10 cm: 2 : 3 = 20 : 30.",
    "ایک ہی شکل کے دو جھنڈے، ہر ایک 3، 3 برابر مربعوں کی 2 قطاروں میں بٹا۔ چھوٹا 2 چوڑا اور 3 لمبا ہے۔ سکول کا بڑا جھنڈا 20 سینٹی میٹر چوڑا اور 30 سینٹی میٹر لمبا ہے، ہر مربع 10 سینٹی میٹر: 2 : 3 = 20 : 30"),
  "s6_missing_explain": double_line(
    3, 5, 12 // 3, {1: ("3", "5"), 12 // 3: ("12", str(S6))},
    f"A double number line. The top line has 3 and 12; the bottom line has 5 and {S6} under them. An arrow marked ×4 jumps from the first pair to the second.",
    f"دوہری عددی لکیر۔ اوپر کی لکیر پر 3 اور 12 ہیں؛ نیچے کی لکیر پر ان کے نیچے 5 اور {S6} ہیں۔ ×4 لکھا تیر پہلے جوڑے سے دوسرے جوڑے تک جاتا ہے۔",
    arrows=[(1, 12 // 3, "×4")]),
  "s7_missing": double_line(
    4, 7, 12 // 4, {1: ("4", "7"), 12 // 4: ("12", "?")},
    "A double number line for 4 : 7 :: 12 : ?. The top line has 4 and 12; the bottom line has 7 under the 4 and a question mark under the 12. An arrow marked ×3 jumps from 4 to 12.",
    "4 : 7 :: 12 : ? کی دوہری عددی لکیر۔ اوپر کی لکیر پر 4 اور 12 ہیں؛ نیچے کی لکیر پر 4 کے نیچے 7 اور 12 کے نیچے سوالیہ نشان ہے۔ ×3 لکھا تیر 4 سے 12 تک جاتا ہے۔",
    arrows=[(1, 12 // 4, "×3")]),
  "s8_flag": two_flags(
    {"w": 40, "l": 60, "w_text": str(FLAG_W), "l_text": str(FLAG_L)}, {"w": 100, "l": 150, "w_text": "40cm", "l_text": "?"},
    "Two flags of the same shape. The small one is 2 wide and 3 long. The big one is 40 cm wide; its length is marked with a question mark.",
    "ایک ہی شکل کے دو جھنڈے۔ چھوٹا 2 چوڑا اور 3 لمبا ہے۔ بڑا 40 سینٹی میٹر چوڑا ہے؛ اس کی لمبائی پر سوالیہ نشان ہے۔"),
  "s11_missing_first": double_line(
    2, 3, 5, {2: ("?", "6"), 5: ("10", "15")},
    "A double number line for ? : 6 :: 10 : 15, with equal steps. The bottom line has 6 and 15; above them the top line has a question mark and 10.",
    "? : 6 :: 10 : 15 کی دوہری عددی لکیر، برابر قدموں کے ساتھ۔ نیچے کی لکیر پر 6 اور 15 ہیں؛ ان کے اوپر، اوپر کی لکیر پر سوالیہ نشان اور 10 ہیں۔"),
  "qb_missing": double_line(
    5, 8, 15 // 5, {1: ("5", "8"), 15 // 5: ("15", "?")},
    "A double number line for 5 : 8 :: 15 : ?. The top line has 5 and 15; the bottom line has 8 under the 5 and a question mark under the 15. An arrow marked ×3 jumps from 5 to 15.",
    "5 : 8 :: 15 : ? کی دوہری عددی لکیر۔ اوپر کی لکیر پر 5 اور 15 ہیں؛ نیچے کی لکیر پر 5 کے نیچے 8 اور 15 کے نیچے سوالیہ نشان ہے۔ ×3 لکھا تیر 5 سے 15 تک جاتا ہے۔",
    arrows=[(1, 15 // 5, "×3")]),
  "r_missing": double_line(
    3, 2, 15 // 3, {1: ("3", "2"), 15 // 3: ("15", "?")},
    "A double number line for 3 : 2 :: 15 : ?. The top line has 3 and 15; the bottom line has 2 under the 3 and a question mark under the 15. An arrow marked ×5 jumps from 3 to 15.",
    "3 : 2 :: 15 : ? کی دوہری عددی لکیر۔ اوپر کی لکیر پر 3 اور 15 ہیں؛ نیچے کی لکیر پر 3 کے نیچے 2 اور 15 کے نیچے سوالیہ نشان ہے۔ ×5 لکھا تیر 3 سے 15 تک جاتا ہے۔",
    arrows=[(1, 15 // 3, "×5")]),
})
write(lesson)

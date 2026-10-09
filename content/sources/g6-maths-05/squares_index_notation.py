from math import prod

from common import (T, opt, say, wrong, number_question, write, prime_factors,
                    BOOK, REVIEW, FM_PRIMES, FM_INDEX)
from figs import attach, arrays_figure, side_array, ladder, tree_fig

SKILL = FM_INDEX

# s1: 16 marbles make a 4 by 4 square, 15 do not
SQUARES_100 = [n * n for n in range(1, 11)]
assert 16 in SQUARES_100 and 15 not in SQUARES_100
# s2: 72 = 2 × 2 × 2 × 3 × ?
S2 = 72 // (2 * 2 * 2 * 3)
assert S2 == 3 and prime_factors(72) == [2, 2, 2, 3, 3]
# s3: worked examples
assert 7 ** 2 == 49 and 2 * 2 * 2 == 2 ** 3 == 8
# s4: 7²
S4 = 7 ** 2
assert S4 == 49 and 7 * 2 == 14 and 7 + 2 == 9
# s5: which is a square number
assert 36 in SQUARES_100 and not any(n in SQUARES_100 for n in (18, 20, 32))
# s6: 2 × 2 × 2 × 2 × 2 = 2⁵
assert prod([2] * 5) == 2 ** 5 == 32 and 5 ** 2 == 25 and 2 ** 5 != 5 ** 2
# s7: 3⁴
S7 = 3 ** 4
assert S7 == 81 and 3 * 4 == 12 and 3 + 3 + 3 + 3 == 12 and 4 ** 3 == 64 and 3 ** 3 == 27
# s8: 72 in index form
assert 2 ** 3 * 3 ** 2 == 72 and 2 ** 2 * 3 ** 3 == 108 and 2 ** 3 * 3 == 24 and 6 ** 2 == 36
# s9: 2³ = 8, not 6
assert 2 ** 3 == 8 and 2 + 2 + 2 == 6 and 2 * 3 == 6
# s11: 2² × 5²
S11 = 2 ** 2 * 5 ** 2
assert S11 == 100 and 2 * 2 + 5 * 2 == 14 and (2 + 5) ** 2 == 49 and 2 * 2 * 5 == 20
# question bank
QB = 5 ** 3
assert QB == 125 and 5 * 3 == 15 and 5 ** 2 == 25
assert prod([3] * 4) == 3 ** 4 and 4 ** 3 == 64 != 81
# review
R1 = 6 ** 2
assert R1 == 36 and 6 * 2 == 12
R2 = 10 ** 3
assert R2 == 1000 and 10 * 3 == 30 and 10 ** 2 == 100


lesson = {
 "id": "g6-maths-05-squares-and-index-notation",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find squares of numbers, use index notation (base and index), work out powers, and write a prime factorisation in index form.", "textbook": BOOK}],
 "skills": [SKILL],
 "title": T("Squares and index notation", "مربع اور قوت کی شکل"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": FM_PRIMES}],
 "misconceptions": [
   {"id": "times_index", "description": "Multiplies the base by the index: 5² = 5 × 2 = 10."},
   {"id": "repeated_add", "description": "Adds the base instead of multiplying it: 2³ = 2 + 2 + 2 = 6."},
   {"id": "swap_base_index", "description": "Counts the base instead of how many times it is multiplied: writes 2 × 2 × 2 × 2 × 2 as 5²."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_index_means", "type": "recall", "step": {
     "id": "qb_index_means", "type": "choice",
     "prompt": T("In 4³, what does the small 3 tell you?", "4³ میں چھوٹا 3 کیا بتاتا ہے؟"),
     "options": [
       opt("times", "Multiply 4 by itself, using three 4s: 4 × 4 × 4.", "4 کو خود سے ضرب دیں، تین 4 لے کر: 4 × 4 × 4", True,
           "Yes! The index 3 says how many 4s are multiplied.", "جی ہاں! قوت 3 بتاتی ہے کہ کتنے 4 ضرب ہو رہے ہیں۔"),
       opt("mult3", "Multiply 4 by 3.", "4 کو 3 سے ضرب دیں۔", False,
           "4 × 3 = 12, but 4³ = 4 × 4 × 4 = 64.", "4 × 3 = 12، مگر 4³ = 4 × 4 × 4 = 64", "times_index"),
       opt("add3", "Add three 4s: 4 + 4 + 4.", "تین 4 جمع کریں: 4 + 4 + 4", False,
           "Index means multiply, not add: 4 × 4 × 4 = 64.", "قوت کا مطلب ضرب ہے، جمع نہیں: 4 × 4 × 4 = 64", "repeated_add"),
     ]}},
   {"id": "qb_five_cubed", "type": "apply", "step": number_question(
     "qb_five_cubed",
     T("Work out 5³.", "5³ معلوم کریں۔"),
     QB,
     T("5³ = 5 × 5 × 5. Start with 5 × 5 = 25.", "5³ = 5 × 5 × 5۔ پہلے 5 × 5 = 25"),
     T("Right! 5 × 5 × 5 = 125.", "درست! 5 × 5 × 5 = 125"),
     T("5 × 5 = 25, then 25 × 5 = 125.", "5 × 5 = 25، پھر 25 × 5 = 125"),
     common_wrong=[wrong(15, "That is 5 × 3. Multiply three 5s: 5 × 5 × 5 = 125.", "یہ 5 × 3 ہے۔ تین 5 ضرب دیں: 5 × 5 × 5 = 125", "times_index"),
                   wrong(25, "That is 5², only two 5s. 5³ needs three: 25 × 5 = 125.", "یہ 5² ہے، صرف دو 5۔ 5³ میں تین چاہییں: 25 × 5 = 125")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Bilal wrote 3 × 3 × 3 × 3 as 4³. What went wrong?", "بلال نے 3 × 3 × 3 × 3 کو 4³ لکھا۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("swap", "He swapped them. The base is 3 and there are four 3s, so it is 3⁴.", "اس نے الٹ دیا۔ اساس 3 ہے اور چار 3 ہیں، اس لیے یہ 3⁴ ہے۔", True,
           "Yes! Base = the number multiplied, index = how many times.", "جی ہاں! اساس = جو عدد ضرب ہو رہا ہے، قوت = کتنی بار۔"),
       opt("nothing", "Nothing. 4³ and 3⁴ are the same.", "کوئی غلطی نہیں۔ 4³ اور 3⁴ ایک ہی ہیں۔", False,
           "Check: 4³ = 64 but 3⁴ = 81. They are different.", "دیکھیں: 4³ = 64 مگر 3⁴ = 81۔ یہ مختلف ہیں۔", "swap_base_index"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_square", "front": T("What is a square number?", "مربع عدد کیا ہے؟"),
    "back": T("A number times itself, like 7² = 7 × 7 = 49. Its dots make a square: 1, 4, 9, 16, 25, 36 …", "کسی عدد کو خود سے ضرب دیں، جیسے 7² = 7 × 7 = 49۔ اس کے نقطے مربع بناتے ہیں: 1، 4، 9، 16، 25، 36 …")},
   {"id": "f_index", "front": T("In 2³, which is the base and which is the index?", "2³ میں اساس کون سا ہے اور قوت کون سی؟"),
    "back": T("Base 2, index 3: 2³ = 2 × 2 × 2 = 8.", "اساس 2، قوت 3: 2³ = 2 × 2 × 2 = 8")},
 ],
 "home_tasks": [{"id": "h_dots", "text": T(
   "Use bottle caps or buttons. Make squares: 1 by 1, 2 by 2, 3 by 3, up to 6 by 6. Count the caps in each square and write it like 3² = 9. Which numbers did you get?",
   "بوتل کے ڈھکن یا بٹن لیں۔ مربع بنائیں: 1 ضرب 1، 2 ضرب 2، 3 ضرب 3، 6 ضرب 6 تک۔ ہر مربع کے ڈھکن گنیں اور یوں لکھیں: 3² = 9۔ آپ کو کون سے اعداد ملے؟")}],
 "glossary": [T("Square number", "مربع عدد"), T("Index (power)", "قوت"), T("Base", "اساس"), T("Index form", "قوت کی شکل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Ali put 16 marbles in 4 rows of 4: a perfect square! He tried 15 marbles but could not make a square. Why?",
      "علی نے 16 کنچے 4، 4 کی 4 قطاروں میں رکھے: پورا مربع! اس نے 15 کنچوں سے کوشش کی مگر مربع نہ بنا۔ کیوں؟"),
    "text": T("Some numbers make a perfect square of dots. Today we learn about them, and a short way to write repeated multiplication. First, a quick check on prime factors.",
              "کچھ اعداد کے نقطے پورا مربع بناتے ہیں۔ آج ہم ان کے بارے میں سیکھیں گے، اور بار بار ضرب کو مختصر لکھنے کا طریقہ بھی۔ پہلے مفرد اجزائے ضربی کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Find the missing prime: 72 = 2 × 2 × 2 × 3 × ?", "غائب مفرد عدد معلوم کریں: 72 = 2 × 2 × 2 × 3 × ?"),
     S2,
     T("2 × 2 × 2 × 3 = 24. What times 24 makes 72?", "2 × 2 × 2 × 3 = 24۔ 24 کو کس سے ضرب دیں تو 72 بنے؟"),
     T("Right! 72 = 2 × 2 × 2 × 3 × 3. Keep this one; we will use it later.", "درست! 72 = 2 × 2 × 2 × 3 × 3۔ اسے یاد رکھیں؛ ہم بعد میں استعمال کریں گے۔"),
     T("2 × 2 × 2 × 3 = 24 and 72 ÷ 24 = 3.", "2 × 2 × 2 × 3 = 24 اور 72 ÷ 24 = 3"),
     common_wrong=[wrong(9, "9 is not prime (3 × 3). 72 ÷ 24 = 3.", "9 مفرد نہیں (3 × 3)۔ 72 ÷ 24 = 3")],
     qtype="recall", skill=FM_PRIMES),
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "16 = 4 × 4, a number times itself. That is why it makes a square!",
                     "16 = 4 × 4، ایک عدد خود سے ضرب۔ اسی لیے یہ مربع بناتا ہے!"),
    "text": T("A number times itself is its square. 7 × 7 = 49, written 7² and read \"7 squared\". 49 dots fit in 7 rows of 7, so 49 is a square number. The square numbers are 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 … The same short way works for more copies: 2 × 2 × 2 = 2³. The big number 2 is the base: the number being multiplied. The small number 3 is the index (or power): how many times the base is multiplied. So 2³ = 8, not 6.",
              "کسی عدد کو خود سے ضرب دیں تو اس کا مربع ملتا ہے۔ 7 × 7 = 49، جسے 7² لکھتے ہیں اور \"7 کا مربع\" پڑھتے ہیں۔ 49 نقطے 7، 7 کی 7 قطاروں میں آ جاتے ہیں، اس لیے 49 مربع عدد ہے۔ مربع اعداد یہ ہیں: 1، 4، 9، 16، 25، 36، 49، 64، 81، 100 … زیادہ بار ضرب کے لیے بھی یہی مختصر طریقہ ہے: 2 × 2 × 2 = 2³۔ بڑا عدد 2 اساس ہے: جو عدد ضرب ہو رہا ہے۔ چھوٹا عدد 3 قوت ہے: اساس کتنی بار ضرب ہو رہی ہے۔ اس لیے 2³ = 8، 6 نہیں۔")},
   number_question(
     "s4_seven_squared",
     T("Work out 7².", "7² معلوم کریں۔"),
     S4,
     T("7² means 7 × 7.", "7² کا مطلب ہے 7 × 7"),
     T("Right! 7 × 7 = 49.", "درست! 7 × 7 = 49"),
     T("7² = 7 × 7 = 49: 7 rows of 7 dots.", "7² = 7 × 7 = 49: نقطوں کی 7، 7 کی 7 قطاریں۔"),
     common_wrong=[wrong(14, "That is 7 × 2. Squared means 7 × 7 = 49.", "یہ 7 × 2 ہے۔ مربع کا مطلب 7 × 7 = 49", "times_index"),
                   wrong(9, "That adds 7 + 2. Squared means 7 × 7 = 49.", "یہ 7 + 2 جمع ہے۔ مربع کا مطلب 7 × 7 = 49")]),
   {"id": "s5_which_square", "type": "choice", "question_type": "recall",
    "prompt": T("Which of these is a square number?", "ان میں سے کون سا مربع عدد ہے؟"),
    "options": [
      opt("n36", "36", "36", True, "Yes! 36 = 6 × 6 = 6², so 36 dots make a 6 by 6 square.", "جی ہاں! 36 = 6 × 6 = 6²، اس لیے 36 نقطے 6 ضرب 6 کا مربع بناتے ہیں۔"),
      opt("n18", "18", "18", False, "18 = 9 × 2, not a number times itself. 4 × 4 = 16 and 5 × 5 = 25.", "18 = 9 × 2، کوئی عدد خود سے ضرب نہیں۔ 4 × 4 = 16 اور 5 × 5 = 25", "times_index"),
      opt("n20", "20", "20", False, "4 × 4 = 16 and 5 × 5 = 25, so 20 is not a square number.", "4 × 4 = 16 اور 5 × 5 = 25، اس لیے 20 مربع عدد نہیں۔"),
      opt("n32", "32", "32", False, "5 × 5 = 25 and 6 × 6 = 36, so 32 is not a square number.", "5 × 5 = 25 اور 6 × 6 = 36، اس لیے 32 مربع عدد نہیں۔"),
    ]},
   {"id": "s6_write_index", "type": "choice", "question_type": "apply",
    "prompt": T("Write 2 × 2 × 2 × 2 × 2 in index form.", "2 × 2 × 2 × 2 × 2 کو قوت کی شکل میں لکھیں۔"),
    "options": [
      opt("two_5", "2⁵", "2⁵", True, "Yes! The base is 2 and it is multiplied 5 times.", "جی ہاں! اساس 2 ہے اور یہ 5 بار ضرب ہو رہی ہے۔"),
      opt("five_2", "5²", "5²", False, "5² = 5 × 5. The number multiplied is 2, so the base is 2: 2⁵.", "5² = 5 × 5۔ ضرب ہونے والا عدد 2 ہے، اس لیے اساس 2 ہے: 2⁵", "swap_base_index"),
      opt("ten", "2 × 5", "2 × 5", False, "2 × 5 = 10, but 2 × 2 × 2 × 2 × 2 = 32. Write 2⁵.", "2 × 5 = 10، مگر 2 × 2 × 2 × 2 × 2 = 32۔ 2⁵ لکھیں۔", "times_index"),
    ]},
   number_question(
     "s7_three_power_four",
     T("Work out 3⁴.", "3⁴ معلوم کریں۔"),
     S7,
     T("3⁴ = 3 × 3 × 3 × 3. Go step by step: 3 × 3 = 9 …", "3⁴ = 3 × 3 × 3 × 3۔ قدم بہ قدم: 3 × 3 = 9 …"),
     T("Right! 3 × 3 × 3 × 3 = 81.", "درست! 3 × 3 × 3 × 3 = 81"),
     T("3 × 3 = 9, 9 × 3 = 27, 27 × 3 = 81.", "3 × 3 = 9، 9 × 3 = 27، 27 × 3 = 81"),
     common_wrong=[wrong(12, "That is 3 × 4. Multiply four 3s: 3 × 3 × 3 × 3 = 81.", "یہ 3 × 4 ہے۔ چار 3 ضرب دیں: 3 × 3 × 3 × 3 = 81", "times_index"),
                   wrong(27, "That is only three 3s. One more: 27 × 3 = 81.", "یہ صرف تین 3 ہیں۔ ایک اور: 27 × 3 = 81"),
                   wrong(64, "That is 4³ = 4 × 4 × 4. Here the base is 3: 3 × 3 × 3 × 3 = 81.", "یہ 4³ = 4 × 4 × 4 ہے۔ یہاں اساس 3 ہے: 3 × 3 × 3 × 3 = 81", "swap_base_index")]),
   {"id": "s8_seventy_two", "type": "choice", "question_type": "apply",
    "prompt": T("72 = 2 × 2 × 2 × 3 × 3. Which shows this in index form?", "72 = 2 × 2 × 2 × 3 × 3۔ کون سا اسے قوت کی شکل میں دکھاتا ہے؟"),
    "options": [
      opt("right", "2³ × 3²", "2³ × 3²", True, "Yes! Three 2s and two 3s: 8 × 9 = 72.", "جی ہاں! تین 2 اور دو 3: 8 × 9 = 72"),
      opt("swapped", "2² × 3³", "2² × 3³", False, "Count again: there are three 2s and two 3s. 2² × 3³ = 4 × 27 = 108.", "دوبارہ گنیں: تین 2 ہیں اور دو 3۔ 2² × 3³ = 4 × 27 = 108", "swap_base_index"),
      opt("one_three", "2³ × 3", "2³ × 3", False, "There are two 3s, so write 3². 2³ × 3 = 24.", "دو 3 ہیں، اس لیے 3² لکھیں۔ 2³ × 3 = 24"),
      opt("six_sq", "6²", "6²", False, "6² = 36, not 72. Count each prime: 2³ × 3².", "6² = 36، 72 نہیں۔ ہر مفرد عدد گنیں: 2³ × 3²"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hamza says 2³ = 6. What went wrong?", "حمزہ کہتا ہے 2³ = 6۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("mult", "2³ means 2 × 2 × 2 = 8. He did 2 × 3 (or 2 + 2 + 2).", "2³ کا مطلب ہے 2 × 2 × 2 = 8۔ اس نے 2 × 3 (یا 2 + 2 + 2) کیا۔", True,
          "Yes! The index tells how many 2s to multiply.", "جی ہاں! قوت بتاتی ہے کہ کتنے 2 ضرب دینے ہیں۔"),
      opt("nothing", "Nothing. 2 × 3 = 6.", "کوئی غلطی نہیں۔ 2 × 3 = 6", False,
          "2 × 3 = 6 is true, but 2³ is 2 × 2 × 2 = 8.", "2 × 3 = 6 درست ہے، مگر 2³ = 2 × 2 × 2 = 8", "times_index"),
      opt("nine", "2³ = 9, because 3 × 3 = 9.", "2³ = 9، کیونکہ 3 × 3 = 9", False,
          "The base is 2, not 3. 2³ = 2 × 2 × 2 = 8.", "اساس 2 ہے، 3 نہیں۔ 2³ = 2 × 2 × 2 = 8", "swap_base_index"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "My friend says 5² is 10, because 5 times 2 is 10. Is he right?",
                     "میرا دوست کہتا ہے 5² برابر 10 ہے، کیونکہ 5 ضرب 2 برابر 10۔ کیا وہ درست ہے؟"),
    "task": T("In your own words: what is 5², and why is it not 10?", "اپنے الفاظ میں بتائیں: 5² کتنا ہے، اور یہ 10 کیوں نہیں؟"),
    "key_idea": "5² means 5 × 5 = 25. The index 2 says how many 5s are multiplied together; it does not mean multiply 5 by 2.",
    "levels": {
      "got_it": "Says 5² = 25 because it means 5 × 5, and the 2 tells how many 5s are multiplied.",
      "partly": "Says 5² = 25 or 5 × 5 but does not say what the small 2 means, or says it is not 10 with no reason.",
      "not_yet": "Agrees that 5² = 10, or gives no reason."},
    "keywords": [
      ["5 × 5", "5 x 5", "5*5", "five times five", "5 ضرب 5", "خود سے ضرب", "itself"],
      ["25", "پچیس"],
      ["how many times", "two fives", "two 5s", "کتنی بار", "دو بار", "دو 5"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 5² = 5 × 5 = 25. The small 2 says how many 5s to multiply.",
                  "بہت خوب سمجھایا! 5² = 5 × 5 = 25۔ چھوٹا 2 بتاتا ہے کہ کتنے 5 ضرب دینے ہیں۔"),
      "partly": T("Good start! Now say what the small 2 tells us: how many 5s are multiplied?", "اچھی شروعات! اب بتائیں چھوٹا 2 کیا بتاتا ہے: کتنے 5 ضرب ہو رہے ہیں؟"),
      "not_yet": T("Remember: 7² = 7 × 7 = 49. So what is 5²?", "یاد کریں: 7² = 7 × 7 = 49۔ تو 5² کتنا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_product",
     T("Which number is 2² × 5²?", "2² × 5² کون سا عدد ہے؟"),
     S11,
     T("Work out each power first: 2² = 4 and 5² = 25.", "پہلے ہر قوت معلوم کریں: 2² = 4 اور 5² = 25"),
     T("Right! 4 × 25 = 100.", "درست! 4 × 25 = 100"),
     T("2² = 2 × 2 = 4, 5² = 5 × 5 = 25, and 4 × 25 = 100.", "2² = 2 × 2 = 4، 5² = 5 × 5 = 25، اور 4 × 25 = 100"),
     common_wrong=[wrong(14, "That is 2 × 2 + 5 × 2. Use 2² = 4 and 5² = 25, then 4 × 25 = 100.", "یہ 2 × 2 + 5 × 2 ہے۔ 2² = 4 اور 5² = 25 لیں، پھر 4 × 25 = 100", "times_index"),
                   wrong(20, "5² is 5 × 5, not just 5. 4 × 25 = 100.", "5² کا مطلب 5 × 5 ہے، صرف 5 نہیں۔ 4 × 25 = 100")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Index form is a short way to write long multiplications!", "قوت کی شکل لمبی ضربوں کو مختصر لکھنے کا طریقہ ہے!"),
    "text": T("A number times itself is its square: 7² = 7 × 7 = 49, and 49 dots make a 7 by 7 square. In 2³, 2 is the base and 3 is the index (power): 2³ = 2 × 2 × 2 = 8. Prime factors can be written in index form: 72 = 2 × 2 × 2 × 3 × 3 = 2³ × 3².",
              "کسی عدد کو خود سے ضرب دیں تو اس کا مربع ملتا ہے: 7² = 7 × 7 = 49، اور 49 نقطے 7 ضرب 7 کا مربع بناتے ہیں۔ 2³ میں 2 اساس ہے اور 3 قوت: 2³ = 2 × 2 × 2 = 8۔ مفرد اجزائے ضربی کو قوت کی شکل میں لکھ سکتے ہیں: 72 = 2 × 2 × 2 × 3 × 3 = 2³ × 3²"),
    "points": [T("5² is 5 × 5 = 25, not 5 × 2.", "5² کا مطلب 5 × 5 = 25 ہے، 5 × 2 نہیں۔"),
               T("The index counts how many times the base is multiplied.", "قوت گنتی ہے کہ اساس کتنی بار ضرب ہوئی۔")]},
 ],
 "review_questions": [
   {"id": "r_six_squared", "type": "recall", "skill": SKILL, "step": number_question(
     "r_six_squared",
     T("Work out 6².", "6² معلوم کریں۔"),
     R1,
     T("6² means 6 × 6.", "6² کا مطلب ہے 6 × 6"),
     T("Right! 6 × 6 = 36.", "درست! 6 × 6 = 36"),
     T("6² = 6 × 6 = 36.", "6² = 6 × 6 = 36"),
     common_wrong=[wrong(12, "That is 6 × 2. Squared means 6 × 6 = 36.", "یہ 6 × 2 ہے۔ مربع کا مطلب 6 × 6 = 36", "times_index")],
     qtype=None)},
   {"id": "r_ten_cubed", "type": "apply", "skill": SKILL, "step": number_question(
     "r_ten_cubed",
     T("Work out 10³.", "10³ معلوم کریں۔"),
     R2,
     T("10³ = 10 × 10 × 10.", "10³ = 10 × 10 × 10"),
     T("Right! 10 × 10 × 10 = 1000.", "درست! 10 × 10 × 10 = 1000"),
     T("10 × 10 = 100, then 100 × 10 = 1000.", "10 × 10 = 100، پھر 100 × 10 = 1000"),
     common_wrong=[wrong(30, "That is 10 × 3. Multiply three 10s: 1000.", "یہ 10 × 3 ہے۔ تین 10 ضرب دیں: 1000", "times_index"),
                   wrong(100, "That is 10², only two 10s. One more: 100 × 10 = 1000.", "یہ 10² ہے، صرف دو 10۔ ایک اور: 100 × 10 = 1000")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Factors and Multiples unit. No textbook text or exercises were used.",
   "Index forms are asked as choice questions (not typed answers), so children do not need to type superscripts.",
   "Urdu terms to check against the Punjab textbook: مربع / مربع عدد (square / square number), قوت (index / power), اساس (base), قوت کی شکل (index form).",
   "The numbers were worked out in content/sources/g6-maths-05/squares_index_notation.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
HOOK_SIDE = 4
assert HOOK_SIDE ** 2 == 16 and HOOK_SIDE ** 2 - 1 == 15
FIRST_SQUARES = SQUARES_100[:4]
assert FIRST_SQUARES == [1, 4, 9, 16]
T72_STOP = ladder(72, stop=72 // (2 * 2 * 2))
assert T72_STOP == (72, (2,), (36, (2,), (18, (2,), (9,))))
T72 = ladder(72)
assert prime_factors(72) == [2, 2, 2, 3, 3]
DOUBLING = [(1, 2), (2, 2), (2, 4)]
assert [r * c for r, c in DOUBLING] == [2, 2 ** 2, 2 ** 3]


def square_side(n, who_en="", who_ur=""):
    return side_array(n, n,
        f"{n} rows of {n} dots{who_en}, a square. {n} is written above the rows and {n} on the left.",
        f"نقطوں کی {n} قطاریں، ہر قطار میں {n} نقطے{who_ur}، یعنی ایک مربع۔ اوپر {n} اور بائیں طرف {n} لکھا ہے۔")


attach(lesson, {
    "s1_hook": arrays_figure(
        [dict(rows=HOOK_SIDE, cols=HOOK_SIDE, text=HOOK_SIDE ** 2),
         dict(rows=HOOK_SIDE, cols=HOOK_SIDE, text=HOOK_SIDE ** 2 - 1, dashed_last=1)],
        f"Left: {HOOK_SIDE ** 2} marbles in {HOOK_SIDE} rows of {HOOK_SIDE}, a full square, with {HOOK_SIDE ** 2} written under it. Right: {HOOK_SIDE ** 2 - 1} marbles in the same shape with the last corner marble missing (a dashed circle), with {HOOK_SIDE ** 2 - 1} written under it.",
        f"بائیں: {HOOK_SIDE ** 2} کنچے، {HOOK_SIDE} کی {HOOK_SIDE} قطاریں، پورا مربع، نیچے {HOOK_SIDE ** 2} لکھا ہے۔ دائیں: {HOOK_SIDE ** 2 - 1} کنچے اسی شکل میں مگر آخری کونے کا کنچا غائب ہے (ڈیش والا دائرہ)، نیچے {HOOK_SIDE ** 2 - 1} لکھا ہے۔"),
    "s2_foundation": tree_fig(T72_STOP, " 9 at the end is not split yet.", " آخر میں 9 ابھی توڑا نہیں گیا۔"),
    "s3_see_it": arrays_figure(
        [dict(rows=k, cols=k, text=f"{k}²") for k in range(1, len(FIRST_SQUARES) + 1)],
        "The first four square numbers as squares of dots: 1 dot (1²), 2 rows of 2 (2²), 3 rows of 3 (3²) and 4 rows of 4 (4²), with 1², 2², 3², 4² written under them.",
        "پہلے چار مربع اعداد نقطوں کے مربعوں کی صورت میں: 1 نقطہ (1²)، 2 کی 2 قطاریں (2²)، 3 کی 3 قطاریں (3²) اور 4 کی 4 قطاریں (4²)، نیچے 1²، 2²، 3²، 4² لکھا ہے۔"),
    "s4_seven_squared": square_side(7),
    "s8_seventy_two": tree_fig(T72),
    "s11_product": arrays_figure(
        [dict(rows=2, cols=2, text="2²"), dict(rows=5, cols=5, text="5²")],
        "Two squares of dots: 2 rows of 2 with 2² under it, and 5 rows of 5 with 5² under it.",
        "نقطوں کے دو مربع: 2 کی 2 قطاریں، نیچے 2² لکھا ہے، اور 5 کی 5 قطاریں، نیچے 5² لکھا ہے۔"),
    "s12_summary": arrays_figure(
        [dict(rows=r, cols=c, text="×".join(["2"] * k)) for k, (r, c) in enumerate(DOUBLING, start=1)],
        "Dots that double each time: 2 dots with 2 under them, 2 rows of 2 (4 dots) with 2×2 under them, and 2 rows of 4 (8 dots) with 2×2×2 under them.",
        "ہر بار دگنے ہونے والے نقطے: 2 نقطے، نیچے 2 لکھا ہے؛ 2 کی 2 قطاریں (4 نقطے)، نیچے 2×2؛ اور 4 کی 2 قطاریں (8 نقطے)، نیچے 2×2×2 لکھا ہے۔"),
    "r_six_squared": square_side(6),
})
write(lesson)

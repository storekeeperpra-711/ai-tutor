from common import (T, opt, say, wrong, number_question, write, factors,
                    REF, REVIEW, TIMES_TABLES, FM_FACTORS)

SKILL = FM_FACTORS

# s1, s3, s4: 12 laddoos
F12 = factors(12)
assert F12 == [1, 2, 3, 4, 6, 12] and len(F12) == 6
# s2
assert 6 * 7 == 42
# s5: 4 is not a factor of 18
assert factors(18) == [1, 2, 3, 6, 9, 18] and 18 % 4 != 0
# s6: the 5th multiple of 7
S6 = 7 * 5
assert S6 == 35 and 7 + 5 == 12
# s8: 471 is divisible by 3 (digit sum 12)
assert sum(map(int, "471")) == 12 and 471 % 3 == 0
# s9: 4 is a factor of 12, 12 is a multiple of 4
assert 12 % 4 == 0
# s11: the largest factor of 36 below 36
S11 = factors(36)[-2]
assert S11 == 18
# question bank and review
QB = len(factors(20))
assert factors(20) == [1, 2, 4, 5, 10, 20] and QB == 6
R1 = 9 * 4
assert R1 == 36
R2 = len(factors(15))
assert factors(15) == [1, 3, 5, 15] and R2 == 4


lesson = {
 "id": "g6-maths-05-factors-and-multiples",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find factors and multiples of a number, and use divisibility tests for 2, 3, 5 and 10.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Factors and multiples", "اجزائے ضربی اور اضعاف"),
 "estimated_minutes": 13,
 "prerequisites": [{"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "factor_multiple_swap", "description": "Mixes up factors and multiples: says 4 is a multiple of 12."},
   {"id": "missing_pairs", "description": "Forgets factors when listing them, especially 1 and the number itself."},
   {"id": "adds_for_multiple", "description": "Adds instead of multiplying to find a multiple: the 5th multiple of 7 is 12."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("Which sentence is true?", "کون سا جملہ درست ہے؟"),
     "options": [
       opt("right", "5 is a factor of 20, and 20 is a multiple of 5.", "5، 20 کا جزو ضربی ہے، اور 20، 5 کا ضعف ہے۔", True, "Yes! 5 divides 20 exactly: 20 = 4 × 5.", "جی ہاں! 5، 20 کو پورا تقسیم کرتا ہے: 20 = 4 × 5"),
       opt("swap", "20 is a factor of 5.", "20، 5 کا جزو ضربی ہے۔", False, "A factor is never bigger than the number. 5 is a factor of 20.", "جزو ضربی کبھی عدد سے بڑا نہیں ہوتا۔ 5، 20 کا جزو ضربی ہے۔", "factor_multiple_swap"),
       opt("mult", "5 is a multiple of 20.", "5، 20 کا ضعف ہے۔", False, "Multiples of 20 are 20, 40, 60 … 5 is a factor of 20.", "20 کے اضعاف 20، 40، 60 … ہیں۔ 5، 20 کا جزو ضربی ہے۔", "factor_multiple_swap"),
     ]}},
   {"id": "qb_count", "type": "apply", "step": number_question(
     "qb_count",
     T("How many factors does 20 have?", "20 کے کتنے اجزائے ضربی ہیں؟"),
     QB,
     T("Find the pairs: 1 × 20, 2 × 10, 4 × 5.", "جوڑے ڈھونڈیں: 1 × 20، 2 × 10، 4 × 5"),
     T("Right! 1, 2, 4, 5, 10 and 20: six factors.", "درست! 1، 2، 4، 5، 10 اور 20: چھ اجزائے ضربی۔"),
     T("1 × 20, 2 × 10, 4 × 5 give 1, 2, 4, 5, 10, 20: six factors.", "1 × 20، 2 × 10، 4 × 5 سے 1، 2، 4، 5، 10، 20: چھ اجزائے ضربی۔"),
     common_wrong=[wrong(3, "Each pair gives TWO factors: 3 pairs, 6 factors.", "ہر جوڑے میں دو اجزائے ضربی ہیں: 3 جوڑے، 6 اجزائے ضربی۔", "missing_pairs"),
                   wrong(4, "Don't forget 1 and 20 itself: 1, 2, 4, 5, 10, 20.", "1 اور خود 20 نہ بھولیں: 1، 2، 4، 5، 10، 20", "missing_pairs")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Maryam listed the factors of 16 as 2, 4, 8. What is missing?", "مریم نے 16 کے اجزائے ضربی 2، 4، 8 لکھے۔ کیا رہ گیا ہے؟"),
     "options": [
       opt("ends", "1 and 16: every number has 1 and itself as factors.", "1 اور 16: ہر عدد کے اجزائے ضربی میں 1 اور خود وہ عدد ہوتا ہے۔", True,
           "Yes! The factors of 16 are 1, 2, 4, 8, 16.", "جی ہاں! 16 کے اجزائے ضربی 1، 2، 4، 8، 16 ہیں۔"),
       opt("six", "6", "6", False, "16 ÷ 6 is not exact, so 6 is not a factor. 1 and 16 are missing.", "16 ÷ 6 پورا نہیں، اس لیے 6 جزو ضربی نہیں۔ 1 اور 16 رہ گئے ہیں۔"),
       opt("nothing", "Nothing.", "کچھ نہیں۔", False, "1 × 16 = 16, so 1 and 16 are factors too.", "1 × 16 = 16، اس لیے 1 اور 16 بھی اجزائے ضربی ہیں۔", "missing_pairs"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_words", "front": T("Factor or multiple?", "جزو ضربی یا ضعف؟"),
    "back": T("A factor divides a number exactly: 4 is a factor of 12. A multiple is in its times table: 12 is a multiple of 4.", "جزو ضربی عدد کو پورا تقسیم کرتا ہے: 4، 12 کا جزو ضربی ہے۔ ضعف پہاڑے میں آتا ہے: 12، 4 کا ضعف ہے۔")},
   {"id": "f_tests", "front": T("Divisibility tests for 2, 3, 5, 10", "2، 3، 5، 10 سے تقسیم کی جانچ"),
    "back": T("2: last digit even. 5: last digit 0 or 5. 10: last digit 0. 3: the sum of the digits divides by 3.", "2: آخری ہندسہ جفت۔ 5: آخری ہندسہ 0 یا 5۔ 10: آخری ہندسہ 0۔ 3: ہندسوں کا مجموعہ 3 سے تقسیم ہو۔")},
 ],
 "home_tasks": [{"id": "h_rows", "text": T(
   "Take 24 small things (beans, buttons or stones). Find every way to put them in equal rows. Write each way as a multiplication. What are the factors of 24?",
   "24 چھوٹی چیزیں لیں (دانے، بٹن یا کنکر)۔ انہیں برابر قطاروں میں رکھنے کے سب طریقے ڈھونڈیں۔ ہر طریقے کو ضرب کی شکل میں لکھیں۔ 24 کے اجزائے ضربی کیا ہیں؟")}],
 "glossary": [T("Factor", "جزو ضربی"), T("Multiple", "ضعف"), T("Divisible", "قابل تقسیم"), T("Divisibility test", "قابلِ تقسیم ہونے کی جانچ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Ayesha has 12 laddoos. She wants to put them in equal rows on a tray. How many different ways can she do it?",
      "عائشہ کے پاس 12 لڈو ہیں۔ وہ انہیں تھال میں برابر قطاروں میں رکھنا چاہتی ہے۔ وہ کتنے مختلف طریقوں سے رکھ سکتی ہے؟"),
    "text": T("Today we learn about factors and multiples. First, a quick times-tables check.", "آج ہم اجزائے ضربی اور اضعاف کے بارے میں سیکھیں گے۔ پہلے پہاڑوں کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Work out 6 × 7", "حل کریں: 6 × 7"),
     42,
     T("Count 7 sixes: 6, 12, 18 …", "چھ کو 7 بار گنیں: 6، 12، 18 …"),
     T("Right! 6 × 7 = 42.", "درست! 6 × 7 = 42"),
     T("6 × 7 = 42.", "6 × 7 = 42"),
     common_wrong=[wrong(13, "That is 6 + 7. Multiply: 6 × 7 = 42.", "یہ 6 + 7 ہے۔ ضرب دیں: 6 × 7 = 42")],
     qtype="recall", skill=TIMES_TABLES),
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "Each row arrangement is a pair of factors!", "قطاروں کی ہر ترتیب اجزائے ضربی کا ایک جوڑا ہے!"),
    "text": T("12 laddoos can go in 1 row of 12, 2 rows of 6, 3 rows of 4, 4 rows of 3, 6 rows of 2 or 12 rows of 1. The numbers that divide 12 exactly are its factors: 1, 2, 3, 4, 6, 12. The multiples of a number are its times table: the multiples of 4 are 4, 8, 12, 16, 20 … So 4 is a factor of 12, and 12 is a multiple of 4.",
              "12 لڈو 12 کی 1 قطار، 6 کی 2 قطاروں، 4 کی 3 قطاروں، 3 کی 4 قطاروں، 2 کی 6 قطاروں یا 1 کی 12 قطاروں میں رکھے جا سکتے ہیں۔ جو اعداد 12 کو پورا تقسیم کرتے ہیں وہ اس کے اجزائے ضربی ہیں: 1، 2، 3، 4، 6، 12۔ کسی عدد کے اضعاف اس کا پہاڑا ہیں: 4 کے اضعاف 4، 8، 12، 16، 20 … ہیں۔ اس لیے 4، 12 کا جزو ضربی ہے، اور 12، 4 کا ضعف ہے۔")},
   number_question(
     "s4_count",
     T("How many factors does 12 have?", "12 کے کتنے اجزائے ضربی ہیں؟"),
     len(F12),
     T("Pairs: 1 × 12, 2 × 6, 3 × 4. Count every number.", "جوڑے: 1 × 12، 2 × 6، 3 × 4۔ ہر عدد گنیں۔"),
     T("Right! 1, 2, 3, 4, 6, 12: six factors.", "درست! 1، 2، 3، 4، 6، 12: چھ اجزائے ضربی۔"),
     T("Three pairs give six factors: 1, 2, 3, 4, 6, 12.", "تین جوڑوں سے چھ اجزائے ضربی: 1، 2، 3، 4، 6، 12"),
     common_wrong=[wrong(3, "Each pair has two factors. 3 pairs make 6 factors.", "ہر جوڑے میں دو اجزائے ضربی ہیں۔ 3 جوڑے، 6 اجزائے ضربی۔", "missing_pairs"),
                   wrong(4, "Don't forget 1 and 12 itself.", "1 اور خود 12 نہ بھولیں۔", "missing_pairs")]),
   {"id": "s5_not_factor", "type": "choice", "question_type": "apply",
    "prompt": T("Which of these is NOT a factor of 18?", "ان میں سے کون سا 18 کا جزو ضربی نہیں ہے؟"),
    "options": [
      opt("four", "4", "4", True, "Yes! 18 ÷ 4 is 4 remainder 2, not exact.", "جی ہاں! 18 ÷ 4 کا باقی 2 بچتا ہے، پورا نہیں۔"),
      opt("three", "3", "3", False, "3 × 6 = 18, so 3 is a factor.", "3 × 6 = 18، اس لیے 3 جزو ضربی ہے۔"),
      opt("nine", "9", "9", False, "2 × 9 = 18, so 9 is a factor.", "2 × 9 = 18، اس لیے 9 جزو ضربی ہے۔"),
      opt("one", "1", "1", False, "1 is a factor of every number.", "1 ہر عدد کا جزو ضربی ہے۔", "missing_pairs"),
    ]},
   number_question(
     "s6_multiple",
     T("What is the 5th multiple of 7?", "7 کا پانچواں ضعف کیا ہے؟"),
     S6,
     T("Count in 7s five times: 7, 14, …", "7 کے حساب سے پانچ بار گنیں: 7، 14، …"),
     T("Right! 7, 14, 21, 28, 35.", "درست! 7، 14، 21، 28، 35"),
     T("The 5th multiple of 7 is 5 × 7 = 35.", "7 کا پانچواں ضعف 5 × 7 = 35 ہے۔"),
     common_wrong=[wrong(12, "That is 7 + 5. Multiply: 5 × 7 = 35.", "یہ 7 + 5 ہے۔ ضرب دیں: 5 × 7 = 35", "adds_for_multiple"),
                   wrong(42, "That is the 6th multiple. Count again: 7, 14, 21, 28, 35.", "یہ چھٹا ضعف ہے۔ دوبارہ گنیں: 7، 14، 21، 28، 35")]),
   {"id": "s7_tests", "type": "explain",
    "character": say("thinking", "Some quick tricks tell you if a number divides exactly!", "کچھ آسان طریقے بتا دیتے ہیں کہ عدد پورا تقسیم ہوتا ہے یا نہیں!"),
    "text": T("Divisible by 2: the last digit is even (0, 2, 4, 6, 8). By 5: the last digit is 0 or 5. By 10: the last digit is 0. By 3: add the digits; if the sum divides by 3, so does the number. 471: 4 + 7 + 1 = 12, and 12 divides by 3, so 471 does too.",
              "2 سے قابل تقسیم: آخری ہندسہ جفت ہو (0، 2، 4، 6، 8)۔ 5 سے: آخری ہندسہ 0 یا 5 ہو۔ 10 سے: آخری ہندسہ 0 ہو۔ 3 سے: ہندسے جمع کریں؛ اگر مجموعہ 3 سے تقسیم ہو تو عدد بھی ہوگا۔ 471: 4 + 7 + 1 = 12، اور 12، 3 سے تقسیم ہوتا ہے، اس لیے 471 بھی۔")},
   {"id": "s8_test_three", "type": "choice", "question_type": "apply",
    "prompt": T("Which of these numbers is divisible by 3?", "ان میں سے کون سا عدد 3 سے قابل تقسیم ہے؟"),
    "options": [
      opt("right", "471", "471", True, "Yes! 4 + 7 + 1 = 12, which divides by 3.", "جی ہاں! 4 + 7 + 1 = 12، جو 3 سے تقسیم ہوتا ہے۔"),
      opt("a", "472", "472", False, "4 + 7 + 2 = 13, which doesn't divide by 3.", "4 + 7 + 2 = 13، جو 3 سے تقسیم نہیں ہوتا۔"),
      opt("b", "203", "203", False, "2 + 0 + 3 = 5. Ending in 3 doesn't make it divisible by 3.", "2 + 0 + 3 = 5۔ آخر میں 3 ہونے سے 3 سے تقسیم نہیں ہوتا۔"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal says, \"4 is a multiple of 12.\" What went wrong?", "بلال کہتا ہے، \"4، 12 کا ضعف ہے۔\" کیا غلطی ہوئی؟"),
    "options": [
      opt("swap", "He swapped the words: 4 is a FACTOR of 12, and 12 is a multiple of 4.", "اس نے الفاظ بدل دیے: 4، 12 کا جزو ضربی ہے، اور 12، 4 کا ضعف ہے۔", True,
          "Yes! Multiples of 12 are 12, 24, 36 …; 4 is not one of them.", "جی ہاں! 12 کے اضعاف 12، 24، 36 … ہیں؛ 4 ان میں نہیں۔"),
      opt("nothing", "Nothing. 4 and 12 go together.", "کوئی غلطی نہیں۔ 4 اور 12 ساتھ آتے ہیں۔", False,
          "They do, but the other way round: 4 divides 12, so 4 is a factor of 12.", "آتے ہیں، مگر الٹ: 4، 12 کو تقسیم کرتا ہے، اس لیے 4، 12 کا جزو ضربی ہے۔", "factor_multiple_swap"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "I always mix up factors and multiples! Can you teach me the difference, using 3 and 12?",
                     "میں ہمیشہ اجزائے ضربی اور اضعاف میں الجھ جاتا ہوں! کیا آپ 3 اور 12 سے فرق سمجھا سکتے ہیں؟"),
    "task": T("In your own words: what is the difference between a factor and a multiple? Use 3 and 12.",
              "اپنے الفاظ میں بتائیں: جزو ضربی اور ضعف میں کیا فرق ہے؟ 3 اور 12 استعمال کریں۔"),
    "key_idea": "3 is a factor of 12 because 3 divides 12 exactly (12 ÷ 3 = 4). 12 is a multiple of 3 because it is in the 3 times table (3 × 4 = 12). Factors are small and divide in; multiples are big and come from multiplying.",
    "levels": {
      "got_it": "Says 3 is a factor of 12 because it divides 12 exactly, and 12 is a multiple of 3 because it is in the 3 times table (3 × 4).",
      "partly": "Gets one of the two right, or states both without a reason.",
      "not_yet": "Mixes them up, gives no answer, or the reasoning is wrong."},
    "keywords": [
      ["divide", "divides", "تقسیم", "taqseem", "÷"],
      ["times table", "multiply", "پہاڑا", "ضرب", "pahara", "zarb", "×"],
      ["factor", "multiple", "جزو", "ضعف", "juz", "zaaf"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 3 divides 12 exactly, so 3 is a factor; 12 is in the 3 times table, so 12 is a multiple of 3.",
                  "بہت خوب سمجھایا! 3، 12 کو پورا تقسیم کرتا ہے، اس لیے 3 جزو ضربی ہے؛ 12، 3 کے پہاڑے میں ہے، اس لیے 12، 3 کا ضعف ہے۔"),
      "partly": T("Good start! Now explain the other word too: which one divides, and which one is in the times table?", "اچھی شروعات! اب دوسرا لفظ بھی سمجھائیں: کون تقسیم کرتا ہے، اور کون پہاڑے میں آتا ہے؟"),
      "not_yet": T("Think: 12 ÷ 3 = 4 and 3 × 4 = 12. Which number divides the other? Which is in the other's times table?",
                   "سوچیں: 12 ÷ 3 = 4 اور 3 × 4 = 12۔ کون سا عدد دوسرے کو تقسیم کرتا ہے؟ کون دوسرے کے پہاڑے میں ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_largest",
     T("What is the largest factor of 36 that is smaller than 36?", "36 کا سب سے بڑا جزو ضربی کون سا ہے جو 36 سے چھوٹا ہو؟"),
     S11,
     T("Find the smallest factor bigger than 1, and pair it.", "1 سے بڑا سب سے چھوٹا جزو ضربی ڈھونڈیں، اور اس کا جوڑا بنائیں۔"),
     T("Right! 2 × 18 = 36, so 18.", "درست! 2 × 18 = 36، اس لیے 18"),
     T("The smallest factor after 1 is 2, and 36 ÷ 2 = 18.", "1 کے بعد سب سے چھوٹا جزو ضربی 2 ہے، اور 36 ÷ 2 = 18"),
     common_wrong=[wrong(12, "12 is a factor, but 18 is bigger: 2 × 18 = 36.", "12 جزو ضربی ہے، مگر 18 بڑا ہے: 2 × 18 = 36"),
                   wrong(6, "6 × 6 = 36, but 18 is a bigger factor.", "6 × 6 = 36، مگر 18 بڑا جزو ضربی ہے۔")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Factors divide in, multiples come out of the times table!", "اجزائے ضربی تقسیم کرتے ہیں، اضعاف پہاڑے سے نکلتے ہیں!"),
    "text": T("A factor divides a number exactly: the factors of 12 are 1, 2, 3, 4, 6, 12. A multiple is in a number's times table: 4, 8, 12, 16 … are multiples of 4. Find factors in pairs. Quick tests: 2 (even), 5 (ends 0 or 5), 10 (ends 0), 3 (digit sum divides by 3).",
              "جزو ضربی عدد کو پورا تقسیم کرتا ہے: 12 کے اجزائے ضربی 1، 2، 3، 4، 6، 12 ہیں۔ ضعف عدد کے پہاڑے میں ہوتا ہے: 4، 8، 12، 16 … 4 کے اضعاف ہیں۔ اجزائے ضربی جوڑوں میں ڈھونڈیں۔ آسان جانچ: 2 (جفت)، 5 (آخر میں 0 یا 5)، 10 (آخر میں 0)، 3 (ہندسوں کا مجموعہ 3 سے تقسیم)۔"),
    "points": [T("1 and the number itself are always factors.", "1 اور خود وہ عدد ہمیشہ اجزائے ضربی ہیں۔"),
               T("4 is a factor of 12; 12 is a multiple of 4.", "4، 12 کا جزو ضربی ہے؛ 12، 4 کا ضعف ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_multiple", "type": "apply", "skill": SKILL, "step": number_question(
     "r_multiple",
     T("What is the 4th multiple of 9?", "9 کا چوتھا ضعف کیا ہے؟"),
     R1,
     T("4 × 9.", "4 × 9"),
     T("Right! 9, 18, 27, 36.", "درست! 9، 18، 27، 36"),
     T("4 × 9 = 36.", "4 × 9 = 36"),
     common_wrong=[wrong(13, "That is 9 + 4. Multiply: 4 × 9 = 36.", "یہ 9 + 4 ہے۔ ضرب دیں: 4 × 9 = 36", "adds_for_multiple")],
     qtype=None)},
   {"id": "r_count", "type": "apply", "skill": SKILL, "step": number_question(
     "r_count",
     T("How many factors does 15 have?", "15 کے کتنے اجزائے ضربی ہیں؟"),
     R2,
     T("Pairs: 1 × 15, 3 × 5.", "جوڑے: 1 × 15، 3 × 5"),
     T("Right! 1, 3, 5, 15.", "درست! 1، 3، 5، 15"),
     T("Two pairs: 1, 3, 5, 15. That is 4 factors.", "دو جوڑے: 1، 3، 5، 15۔ یعنی 4 اجزائے ضربی۔"),
     common_wrong=[wrong(2, "Each pair gives two factors: 4 in all.", "ہر جوڑے میں دو اجزائے ضربی ہیں: کل 4", "missing_pairs")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Factors and Multiples unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-05. Fix the names and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: جزو ضربی / اجزائے ضربی (factor / factors), ضعف / اضعاف (multiple / multiples), قابل تقسیم (divisible).",
   "The numbers were worked out in content/sources/g6-maths-05/factors_and_multiples.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

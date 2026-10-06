from math import prod

from common import (T, opt, say, wrong, number_question, write, factors, is_prime, prime_factors,
                    REF, REVIEW, FM_FACTORS, FM_PRIMES)

SKILL = FM_PRIMES

# s1, s2: 7 has only two factors
assert factors(7) == [1, 7]
# s4
assert is_prime(29) and not is_prime(21) and not is_prime(27) and not is_prime(1)
# s5: primes below 20
PRIMES_20 = [n for n in range(1, 21) if is_prime(n)]
assert PRIMES_20 == [2, 3, 5, 7, 11, 13, 17, 19] and len(PRIMES_20) == 8
# s6: factor tree of 60
assert prime_factors(60) == [2, 2, 3, 5]
# s7
assert prime_factors(36) == [2, 2, 3, 3]
# s8: 84 = 2 × 2 × 3 × ?
S8 = 84 // (2 * 2 * 3)
assert S8 == 7 and prime_factors(84) == [2, 2, 3, 7]
# s9: 9 is odd but not prime
assert factors(9) == [1, 3, 9]
# s11: smallest prime factor of 91
S11 = prime_factors(91)[0]
assert S11 == 7 and prime_factors(91) == [7, 13]
# question bank and review
QB = 90 // (2 * 3 * 3)
assert QB == 5 and prime_factors(90) == [2, 3, 3, 5]
assert prod([2, 2, 2, 3]) == 24 and prime_factors(24) == [2, 2, 2, 3]
R1 = len([n for n in range(20, 31) if is_prime(n)])
assert [n for n in range(20, 31) if is_prime(n)] == [23, 29] and R1 == 2
R2 = prod([2, 3, 3, 5])
assert R2 == 90


lesson = {
 "id": "g6-maths-05-prime-numbers",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise prime and composite numbers and write a number as a product of prime factors.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Prime numbers and prime factors", "مفرد اعداد اور مفرد اجزائے ضربی"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": FM_FACTORS}],
 "misconceptions": [
   {"id": "odd_is_prime", "description": "Thinks every odd number is prime: 9, 15, 21 are prime."},
   {"id": "one_is_prime", "description": "Thinks 1 is a prime number."},
   {"id": "stops_early", "description": "Stops a factor tree before every branch ends in a prime: 24 = 4 × 6."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_two", "type": "recall", "step": {
     "id": "qb_two", "type": "choice",
     "prompt": T("Which sentence about 2 is true?", "2 کے بارے میں کون سا جملہ درست ہے؟"),
     "options": [
       opt("right", "2 is prime: its only factors are 1 and 2.", "2 مفرد ہے: اس کے اجزائے ضربی صرف 1 اور 2 ہیں۔", True, "Yes! 2 is the only even prime.", "جی ہاں! 2 واحد جفت مفرد عدد ہے۔"),
       opt("even", "2 is not prime because it is even.", "2 جفت ہے اس لیے مفرد نہیں۔", False, "Check its factors: only 1 and 2. So 2 is prime, the only even one.", "اس کے اجزائے ضربی دیکھیں: صرف 1 اور 2۔ اس لیے 2 مفرد ہے، واحد جفت۔", "odd_is_prime"),
       opt("comp", "2 is composite.", "2 مرکب ہے۔", False, "A composite number has more than 2 factors. 2 has only 1 and 2.", "مرکب عدد کے 2 سے زیادہ اجزائے ضربی ہوتے ہیں۔ 2 کے صرف 1 اور 2 ہیں۔"),
     ]}},
   {"id": "qb_missing", "type": "apply", "step": number_question(
     "qb_missing",
     T("Find the missing prime: 90 = 2 × 3 × 3 × ?", "غائب مفرد عدد معلوم کریں: 90 = 2 × 3 × 3 × ?"),
     QB,
     T("2 × 3 × 3 = 18. What times 18 makes 90?", "2 × 3 × 3 = 18۔ 18 کو کس سے ضرب دیں تو 90 بنے؟"),
     T("Right! 90 = 2 × 3 × 3 × 5.", "درست! 90 = 2 × 3 × 3 × 5"),
     T("2 × 3 × 3 = 18 and 90 ÷ 18 = 5.", "2 × 3 × 3 = 18 اور 90 ÷ 18 = 5"),
     common_wrong=[wrong(10, "10 is not prime (2 × 5). 90 ÷ 18 = 5.", "10 مفرد نہیں (2 × 5)۔ 90 ÷ 18 = 5", "stops_early")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Zainab wrote the prime factors of 24 as 4 × 6. What went wrong?", "زینب نے 24 کے مفرد اجزائے ضربی 4 × 6 لکھے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("stop", "4 and 6 are not prime. Keep going: 24 = 2 × 2 × 2 × 3.", "4 اور 6 مفرد نہیں۔ آگے بڑھیں: 24 = 2 × 2 × 2 × 3", True,
           "Yes! Every branch must end in a prime.", "جی ہاں! ہر شاخ مفرد عدد پر ختم ہونی چاہیے۔"),
       opt("nothing", "Nothing. 4 × 6 = 24.", "کوئی غلطی نہیں۔ 4 × 6 = 24", False,
           "4 × 6 = 24 is true, but 4 and 6 are not prime. 24 = 2 × 2 × 2 × 3.", "4 × 6 = 24 درست ہے، مگر 4 اور 6 مفرد نہیں۔ 24 = 2 × 2 × 2 × 3", "stops_early"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_prime", "front": T("What is a prime number?", "مفرد عدد کیا ہے؟"),
    "back": T("A number with exactly two factors: 1 and itself. 2, 3, 5, 7, 11, 13 … 1 is not prime.", "وہ عدد جس کے ٹھیک دو اجزائے ضربی ہوں: 1 اور خود وہ عدد۔ 2، 3، 5، 7، 11، 13 … 1 مفرد نہیں۔")},
   {"id": "f_tree", "front": T("60 as a product of primes?", "60 مفرد اجزائے ضربی کی شکل میں؟"),
    "back": T("60 = 2 × 2 × 3 × 5", "60 = 2 × 2 × 3 × 5")},
 ],
 "home_tasks": [{"id": "h_sieve", "text": T(
   "Write the numbers 1 to 50. Cross out 1. Circle 2 and cross out every other multiple of 2. Do the same for 3, 5 and 7. The circled and uncrossed numbers are the primes. How many are there?",
   "1 سے 50 تک اعداد لکھیں۔ 1 کاٹ دیں۔ 2 پر دائرہ لگائیں اور 2 کے باقی سب اضعاف کاٹ دیں۔ 3، 5 اور 7 کے ساتھ بھی ایسا کریں۔ دائرے والے اور نہ کٹے اعداد مفرد ہیں۔ یہ کتنے ہیں؟")}],
 "glossary": [T("Prime number", "مفرد عدد"), T("Composite number", "مرکب عدد"), T("Prime factor", "مفرد جزو ضربی"), T("Factor tree", "اجزائے ضربی کا درخت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Yesterday 12 laddoos fitted in many neat rows. Today Ayesha has 7. She can only make 1 row of 7, or 7 rows of 1! Why?",
      "کل 12 لڈو کئی صاف قطاروں میں آ گئے۔ آج عائشہ کے پاس 7 ہیں۔ وہ صرف 7 کی 1 قطار، یا 1 کی 7 قطاریں بنا سکتی ہے! کیوں؟"),
    "text": T("Some numbers can't be split into equal rows. Today we meet them. First, a quick check on factors.", "کچھ اعداد برابر قطاروں میں نہیں بٹ سکتے۔ آج ہم ان سے ملیں گے۔ پہلے اجزائے ضربی کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many factors does 7 have?", "7 کے کتنے اجزائے ضربی ہیں؟"),
     2,
     T("Which numbers divide 7 exactly?", "کون سے اعداد 7 کو پورا تقسیم کرتے ہیں؟"),
     T("Right! Only 1 and 7.", "درست! صرف 1 اور 7"),
     T("Only 1 × 7 = 7, so 7 has 2 factors: 1 and 7.", "صرف 1 × 7 = 7، اس لیے 7 کے 2 اجزائے ضربی ہیں: 1 اور 7"),
     common_wrong=[wrong(1, "Count 7 itself too: 1 and 7.", "خود 7 بھی گنیں: 1 اور 7")],
     qtype="recall", skill=FM_FACTORS),
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "Numbers like 7 are called prime numbers!", "7 جیسے اعداد مفرد اعداد کہلاتے ہیں!"),
    "text": T("A prime number has exactly two factors: 1 and itself. 2, 3, 5, 7, 11 and 13 are prime. A composite number has more than two factors, like 12. The number 1 has only one factor, so it is neither prime nor composite. 2 is the only even prime: every other even number divides by 2.",
              "مفرد عدد کے ٹھیک دو اجزائے ضربی ہوتے ہیں: 1 اور خود وہ عدد۔ 2، 3، 5، 7، 11 اور 13 مفرد ہیں۔ مرکب عدد کے دو سے زیادہ اجزائے ضربی ہوتے ہیں، جیسے 12۔ 1 کا صرف ایک جزو ضربی ہے، اس لیے یہ نہ مفرد ہے نہ مرکب۔ 2 واحد جفت مفرد عدد ہے: باقی ہر جفت عدد 2 سے تقسیم ہوتا ہے۔")},
   {"id": "s4_which_prime", "type": "choice", "question_type": "recall",
    "prompt": T("Which of these is a prime number?", "ان میں سے کون سا مفرد عدد ہے؟"),
    "options": [
      opt("p29", "29", "29", True, "Yes! Only 1 × 29 makes 29.", "جی ہاں! صرف 1 × 29 سے 29 بنتا ہے۔"),
      opt("p21", "21", "21", False, "21 = 3 × 7, so it is composite.", "21 = 3 × 7، اس لیے یہ مرکب ہے۔", "odd_is_prime"),
      opt("p27", "27", "27", False, "27 = 3 × 9, so it is composite.", "27 = 3 × 9، اس لیے یہ مرکب ہے۔", "odd_is_prime"),
      opt("p1", "1", "1", False, "1 has only one factor, so it is not prime.", "1 کا صرف ایک جزو ضربی ہے، اس لیے یہ مفرد نہیں۔", "one_is_prime"),
    ]},
   number_question(
     "s5_count_primes",
     T("How many prime numbers are there from 1 to 20?", "1 سے 20 تک کتنے مفرد اعداد ہیں؟"),
     len(PRIMES_20),
     T("List them: 2, 3, 5, 7, … Don't count 1.", "انہیں لکھیں: 2، 3، 5، 7، … 1 کو نہ گنیں۔"),
     T("Right! 2, 3, 5, 7, 11, 13, 17, 19.", "درست! 2، 3، 5، 7، 11، 13، 17، 19"),
     T("2, 3, 5, 7, 11, 13, 17, 19: eight primes.", "2، 3، 5، 7، 11، 13، 17، 19: آٹھ مفرد اعداد۔"),
     common_wrong=[wrong(9, "Did you count 1? 1 is not prime.", "کیا آپ نے 1 گنا؟ 1 مفرد نہیں۔", "one_is_prime"),
                   wrong(7, "Did you leave out 2? 2 is prime.", "کیا آپ نے 2 چھوڑ دیا؟ 2 مفرد ہے۔"),
                   wrong(10, "Odd numbers like 9 and 15 are not prime: 9 = 3 × 3, 15 = 3 × 5.", "9 اور 15 جیسے طاق اعداد مفرد نہیں: 9 = 3 × 3، 15 = 3 × 5", "odd_is_prime")]),
   {"id": "s6_tree", "type": "explain",
    "character": say("thinking", "Every composite number is built from primes. A factor tree finds them!", "ہر مرکب عدد مفرد اعداد سے بنتا ہے۔ اجزائے ضربی کا درخت انہیں ڈھونڈتا ہے!"),
    "text": T("Split 60 into two factors: 60 = 2 × 30. 2 is prime, so that branch stops. Split 30 = 2 × 15, and 15 = 3 × 5. Stop when every branch ends in a prime. So 60 = 2 × 2 × 3 × 5. This is called writing 60 as a product of prime factors. Any split works; you always get the same primes.",
              "60 کو دو اجزائے ضربی میں توڑیں: 60 = 2 × 30۔ 2 مفرد ہے، اس لیے وہ شاخ رک جاتی ہے۔ 30 = 2 × 15، اور 15 = 3 × 5۔ جب ہر شاخ مفرد عدد پر ختم ہو تو رک جائیں۔ اس لیے 60 = 2 × 2 × 3 × 5۔ اسے 60 کو مفرد اجزائے ضربی کے حاصل ضرب کی شکل میں لکھنا کہتے ہیں۔ کسی بھی طرح توڑیں؛ مفرد اعداد ہمیشہ وہی آتے ہیں۔")},
   {"id": "s7_thirty_six", "type": "choice", "question_type": "apply",
    "prompt": T("Which shows 36 as a product of prime factors?", "کون سا 36 کو مفرد اجزائے ضربی کے حاصل ضرب کی شکل میں دکھاتا ہے؟"),
    "options": [
      opt("right", "2 × 2 × 3 × 3", "2 × 2 × 3 × 3", True, "Yes! Every factor is prime and they multiply to 36.", "جی ہاں! ہر جزو مفرد ہے اور ان کا حاصل ضرب 36 ہے۔"),
      opt("four_nine", "4 × 9", "4 × 9", False, "4 and 9 are not prime. Split them: 2 × 2 × 3 × 3.", "4 اور 9 مفرد نہیں۔ انہیں توڑیں: 2 × 2 × 3 × 3", "stops_early"),
      opt("six_six", "6 × 6", "6 × 6", False, "6 is not prime: 6 = 2 × 3. So 2 × 3 × 2 × 3.", "6 مفرد نہیں: 6 = 2 × 3۔ اس لیے 2 × 3 × 2 × 3", "stops_early"),
    ]},
   number_question(
     "s8_missing",
     T("Find the missing prime: 84 = 2 × 2 × 3 × ?", "غائب مفرد عدد معلوم کریں: 84 = 2 × 2 × 3 × ?"),
     S8,
     T("2 × 2 × 3 = 12. What times 12 makes 84?", "2 × 2 × 3 = 12۔ 12 کو کس سے ضرب دیں تو 84 بنے؟"),
     T("Right! 84 = 2 × 2 × 3 × 7.", "درست! 84 = 2 × 2 × 3 × 7"),
     T("2 × 2 × 3 = 12 and 84 ÷ 12 = 7.", "2 × 2 × 3 = 12 اور 84 ÷ 12 = 7"),
     common_wrong=[wrong(14, "14 is not prime (2 × 7). 84 ÷ 12 = 7.", "14 مفرد نہیں (2 × 7)۔ 84 ÷ 12 = 7", "stops_early")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Saad says 9 is a prime number because it is odd. What went wrong?", "سعد کہتا ہے 9 مفرد عدد ہے کیونکہ یہ طاق ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("three", "9 = 3 × 3, so it has 3 factors (1, 3, 9). It is composite.", "9 = 3 × 3، اس لیے اس کے 3 اجزائے ضربی ہیں (1، 3، 9)۔ یہ مرکب ہے۔", True,
          "Yes! Odd doesn't mean prime: check the factors.", "جی ہاں! طاق کا مطلب مفرد نہیں: اجزائے ضربی دیکھیں۔"),
      opt("nothing", "Nothing. All odd numbers are prime.", "کوئی غلطی نہیں۔ سب طاق اعداد مفرد ہیں۔", False,
          "9, 15 and 21 are odd but not prime. 9 = 3 × 3.", "9، 15 اور 21 طاق ہیں مگر مفرد نہیں۔ 9 = 3 × 3", "odd_is_prime"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "My friend says 1 must be prime, because nothing divides it except 1. Is he right?",
                     "میرا دوست کہتا ہے 1 مفرد ہونا چاہیے، کیونکہ 1 کے سوا کوئی اسے تقسیم نہیں کرتا۔ کیا وہ درست ہے؟"),
    "task": T("In your own words: is 1 a prime number? Explain why or why not.", "اپنے الفاظ میں بتائیں: کیا 1 مفرد عدد ہے؟ وجہ بتائیں۔"),
    "key_idea": "1 is not prime. A prime has exactly two different factors, 1 and itself, but 1 has only one factor (1). So 1 is neither prime nor composite.",
    "levels": {
      "got_it": "Says 1 is not prime because a prime needs exactly two factors and 1 has only one.",
      "partly": "Says 1 is not prime but gives no reason, or mentions factors without counting them.",
      "not_yet": "Says 1 is prime, or gives no reason."},
    "keywords": [
      ["two factors", "2 factors", "دو اجزائے", "do ajza", "exactly two"],
      ["one factor", "only one", "ایک جزو", "صرف ایک", "sirf ek"],
      ["not prime", "مفرد نہیں", "neither", "نہ مفرد"]],
    "fallback_feedback": {
      "got_it": T("Well explained! A prime needs exactly two factors, but 1 has only one, so 1 is not prime.",
                  "بہت خوب سمجھایا! مفرد عدد کے ٹھیک دو اجزائے ضربی ہونے چاہییں، مگر 1 کا صرف ایک ہے، اس لیے 1 مفرد نہیں۔"),
      "partly": T("Good start! Now count: how many factors does 1 have, and how many does a prime need?", "اچھی شروعات! اب گنیں: 1 کے کتنے اجزائے ضربی ہیں، اور مفرد عدد کو کتنے چاہییں؟"),
      "not_yet": T("Remember: a prime has exactly two factors, like 7 (1 and 7). How many factors does 1 have?",
                   "یاد کریں: مفرد عدد کے ٹھیک دو اجزائے ضربی ہوتے ہیں، جیسے 7 (1 اور 7)۔ 1 کے کتنے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_smallest",
     T("91 is not prime. What is its smallest prime factor?", "91 مفرد نہیں ہے۔ اس کا سب سے چھوٹا مفرد جزو ضربی کیا ہے؟"),
     S11,
     T("Try dividing by 2, 3, 5, 7 in turn.", "باری باری 2، 3، 5، 7 سے تقسیم کر کے دیکھیں۔"),
     T("Right! 91 = 7 × 13.", "درست! 91 = 7 × 13"),
     T("91 is odd (not 2), 9 + 1 = 10 (not 3), doesn't end in 0 or 5 (not 5), and 91 ÷ 7 = 13. So 7.", "91 طاق ہے (2 نہیں)، 9 + 1 = 10 (3 نہیں)، آخر میں 0 یا 5 نہیں (5 نہیں)، اور 91 ÷ 7 = 13۔ اس لیے 7"),
     common_wrong=[wrong(1, "1 is not prime. Try 2, 3, 5, 7 …", "1 مفرد نہیں۔ 2، 3، 5، 7 … آزمائیں۔", "one_is_prime"),
                   wrong(13, "13 is a prime factor, but 7 is smaller: 91 = 7 × 13.", "13 مفرد جزو ضربی ہے، مگر 7 چھوٹا ہے: 91 = 7 × 13")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Primes are the building blocks of all numbers!", "مفرد اعداد تمام اعداد کی بنیادی اینٹیں ہیں!"),
    "text": T("A prime has exactly two factors, 1 and itself: 2, 3, 5, 7, 11, 13, 17, 19 … A composite number has more. 1 is neither, and 2 is the only even prime. Use a factor tree to write a number as a product of primes: 60 = 2 × 2 × 3 × 5.",
              "مفرد عدد کے ٹھیک دو اجزائے ضربی ہوتے ہیں، 1 اور خود وہ عدد: 2، 3، 5، 7، 11، 13، 17، 19 … مرکب عدد کے زیادہ ہوتے ہیں۔ 1 دونوں میں سے کوئی نہیں، اور 2 واحد جفت مفرد عدد ہے۔ عدد کو مفرد اعداد کے حاصل ضرب کی شکل میں لکھنے کے لیے اجزائے ضربی کا درخت بنائیں: 60 = 2 × 2 × 3 × 5"),
    "points": [T("Odd doesn't mean prime: 9 = 3 × 3.", "طاق کا مطلب مفرد نہیں: 9 = 3 × 3"),
               T("Every branch of a factor tree ends in a prime.", "اجزائے ضربی کے درخت کی ہر شاخ مفرد عدد پر ختم ہوتی ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_count", "type": "apply", "skill": SKILL, "step": number_question(
     "r_count",
     T("How many prime numbers are there from 20 to 30?", "20 سے 30 تک کتنے مفرد اعداد ہیں؟"),
     R1,
     T("Check the odd numbers: 21, 23, 25, 27, 29.", "طاق اعداد دیکھیں: 21، 23، 25، 27، 29"),
     T("Right! 23 and 29.", "درست! 23 اور 29"),
     T("21 = 3 × 7, 25 = 5 × 5, 27 = 3 × 9. Only 23 and 29 are prime.", "21 = 3 × 7، 25 = 5 × 5، 27 = 3 × 9۔ صرف 23 اور 29 مفرد ہیں۔"),
     common_wrong=[wrong(5, "Not every odd number is prime: 21, 25 and 27 are composite.", "ہر طاق عدد مفرد نہیں: 21، 25 اور 27 مرکب ہیں۔", "odd_is_prime")],
     qtype=None)},
   {"id": "r_product", "type": "recall", "skill": SKILL, "step": number_question(
     "r_product",
     T("Which number is 2 × 3 × 3 × 5?", "2 × 3 × 3 × 5 کون سا عدد ہے؟"),
     R2,
     T("Multiply step by step: 2 × 3 = 6, 6 × 3 = 18 …", "قدم بہ قدم ضرب دیں: 2 × 3 = 6، 6 × 3 = 18 …"),
     T("Right! 90.", "درست! 90"),
     T("2 × 3 = 6, 6 × 3 = 18, 18 × 5 = 90.", "2 × 3 = 6، 6 × 3 = 18، 18 × 5 = 90"),
     common_wrong=[wrong(13, "That adds them. Multiply: 2 × 3 × 3 × 5 = 90.", "یہ جمع ہے۔ ضرب دیں: 2 × 3 × 3 × 5 = 90")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Factors and Multiples unit. No textbook text or exercises were used.",
   "Urdu terms to check: مفرد عدد (prime number), مرکب عدد (composite number), اجزائے ضربی کا درخت (factor tree).",
   "The numbers were worked out in content/sources/g6-maths-05/prime_numbers.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

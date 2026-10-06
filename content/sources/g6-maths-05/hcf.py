from math import gcd, lcm

from common import (T, opt, say, wrong, number_question, write, factors, prime_factors,
                    REF, REVIEW, FM_FACTORS, FM_PRIMES, FM_HCF)

SKILL = FM_HCF


def common_factors(a, b):
    return [d for d in factors(a) if b % d == 0]


# s2
assert len(factors(18)) == 6
# s3, s4: 12 and 18
assert common_factors(12, 18) == [1, 2, 3, 6]
S4 = gcd(12, 18)
assert S4 == 6 and lcm(12, 18) == 36
# s5, s6: 24 and 36 by primes
assert prime_factors(24) == [2, 2, 2, 3] and prime_factors(36) == [2, 2, 3, 3]
S6 = gcd(24, 36)
assert S6 == 2 * 2 * 3 == 12 and lcm(24, 36) == 72
# s7: co-prime
S7 = gcd(8, 15)
assert S7 == 1 and lcm(8, 15) == 120
# s8: balloons
BUNCHES = gcd(12, 18)
S8 = 12 // BUNCHES
assert BUNCHES == 6 and S8 == 2 and 18 // BUNCHES == 3
# s9
assert gcd(10, 15) == 5 and lcm(10, 15) == 30
# s10: the HCF is never bigger than the smaller number
assert all(gcd(a, b) <= min(a, b) for a in range(1, 40) for b in range(1, 40))
# s11
S11 = gcd(42, 56)
assert prime_factors(42) == [2, 3, 7] and prime_factors(56) == [2, 2, 2, 7] and S11 == 14
# question bank and review
QB = gcd(16, 40)
assert QB == 8 and lcm(16, 40) == 80
R1 = gcd(20, 30)
assert R1 == 10
R2 = gcd(9, 14)
assert R2 == 1


lesson = {
 "id": "g6-maths-05-highest-common-factor",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the highest common factor (HCF) of two numbers by listing factors and by prime factorisation.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Highest common factor (HCF)", "عاد اعظم"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": FM_FACTORS}, {"skill": FM_PRIMES}],
 "misconceptions": [
   {"id": "hcf_lcm_swap", "description": "Gives a common multiple (often the LCM) instead of the HCF: HCF of 10 and 15 is 30."},
   {"id": "not_highest", "description": "Gives a common factor that is not the highest: HCF of 12 and 18 is 3."},
   {"id": "all_primes", "description": "Multiplies all the prime factors of both numbers instead of only the shared ones."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("What is the HCF of two numbers?", "دو اعداد کا عاد اعظم کیا ہوتا ہے؟"),
     "options": [
       opt("right", "The biggest number that divides both exactly.", "سب سے بڑا عدد جو دونوں کو پورا تقسیم کرے۔", True, "Yes! For 12 and 18 it is 6.", "جی ہاں! 12 اور 18 کا 6 ہے۔"),
       opt("lcm", "The smallest number both divide into.", "سب سے چھوٹا عدد جسے دونوں تقسیم کریں۔", False, "That is the LCM. The HCF divides both numbers.", "یہ ذو اضعاف اقل ہے۔ عاد اعظم دونوں اعداد کو تقسیم کرتا ہے۔", "hcf_lcm_swap"),
       opt("product", "The two numbers multiplied.", "دونوں اعداد کا حاصل ضرب۔", False, "That is bigger than both. The HCF divides both.", "یہ دونوں سے بڑا ہے۔ عاد اعظم دونوں کو تقسیم کرتا ہے۔", "hcf_lcm_swap"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find the HCF of 16 and 40.", "16 اور 40 کا عاد اعظم معلوم کریں۔"),
     QB,
     T("Factors of 16: 1, 2, 4, 8, 16. Which is the biggest that also divides 40?", "16 کے اجزائے ضربی: 1، 2، 4، 8، 16۔ ان میں سب سے بڑا کون سا 40 کو بھی تقسیم کرتا ہے؟"),
     T("Right! HCF = 8.", "درست! عاد اعظم = 8"),
     T("16 = 2 × 2 × 2 × 2, 40 = 2 × 2 × 2 × 5. Shared: 2 × 2 × 2 = 8.", "16 = 2 × 2 × 2 × 2، 40 = 2 × 2 × 2 × 5۔ مشترک: 2 × 2 × 2 = 8"),
     common_wrong=[wrong(80, "80 is a common multiple (the LCM). The HCF divides both: 8.", "80 مشترک ضعف (ذو اضعاف اقل) ہے۔ عاد اعظم دونوں کو تقسیم کرتا ہے: 8", "hcf_lcm_swap"),
                   wrong(4, "4 divides both, but 8 is higher.", "4 دونوں کو تقسیم کرتا ہے، مگر 8 بڑا ہے۔", "not_highest")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Rida says the HCF of 12 and 18 is 3, because 3 divides both. What went wrong?", "ردا کہتی ہے 12 اور 18 کا عاد اعظم 3 ہے، کیونکہ 3 دونوں کو تقسیم کرتا ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("highest", "3 is a common factor, but 6 is the highest one.", "3 مشترک جزو ضربی ہے، مگر سب سے بڑا 6 ہے۔", True,
           "Yes! Common factors are 1, 2, 3, 6; the highest is 6.", "جی ہاں! مشترک اجزائے ضربی 1، 2، 3، 6 ہیں؛ سب سے بڑا 6 ہے۔"),
       opt("nothing", "Nothing. 3 divides both.", "کوئی غلطی نہیں۔ 3 دونوں کو تقسیم کرتا ہے۔", False,
           "It does, but HCF means the HIGHEST common factor: 6.", "کرتا ہے، مگر عاد اعظم کا مطلب سب سے بڑا مشترک جزو ضربی ہے: 6", "not_highest"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_hcf", "front": T("What is the HCF?", "عاد اعظم کیا ہے؟"),
    "back": T("The highest common factor: the biggest number that divides both. HCF of 12 and 18 = 6.", "سب سے بڑا مشترک جزو ضربی: سب سے بڑا عدد جو دونوں کو تقسیم کرے۔ 12 اور 18 کا عاد اعظم = 6")},
   {"id": "f_primes", "front": T("HCF by prime factors?", "مفرد اجزائے ضربی سے عاد اعظم؟"),
    "back": T("Multiply the primes both numbers share. 24 = 2 × 2 × 2 × 3, 36 = 2 × 2 × 3 × 3: HCF = 2 × 2 × 3 = 12.", "وہ مفرد اعداد ضرب دیں جو دونوں میں مشترک ہوں۔ 24 = 2 × 2 × 2 × 3، 36 = 2 × 2 × 3 × 3: عاد اعظم = 2 × 2 × 3 = 12")},
 ],
 "home_tasks": [{"id": "h_packs", "text": T(
   "You have 20 sweets and 30 biscuits to pack into identical gift packs with nothing left over. What is the largest number of packs you can make? What goes in each?",
   "آپ کے پاس 20 ٹافیاں اور 30 بسکٹ ہیں جنہیں ایک جیسے تحفے کے پیکٹوں میں اس طرح بانٹنا ہے کہ کچھ نہ بچے۔ زیادہ سے زیادہ کتنے پیکٹ بن سکتے ہیں؟ ہر پیکٹ میں کیا ہوگا؟")}],
 "glossary": [T("Common factor", "مشترک جزو ضربی"), T("Highest common factor (HCF)", "عاد اعظم"), T("Co-prime", "باہم مفرد")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "We have 12 red and 18 green balloons to make identical bunches, none left over. What is the most bunches we can make?",
      "12 سرخ اور 18 سبز غباروں سے ایک جیسے گچھے بنانے ہیں، کوئی نہ بچے۔ زیادہ سے زیادہ کتنے گچھے بنیں گے؟"),
    "text": T("The number of bunches must divide 12 AND 18. Today we find the biggest such number. First, a quick check.", "گچھوں کی تعداد 12 اور 18 دونوں کو تقسیم کرنی چاہیے۔ آج ہم ایسا سب سے بڑا عدد ڈھونڈیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many factors does 18 have?", "18 کے کتنے اجزائے ضربی ہیں؟"),
     6,
     T("Pairs: 1 × 18, 2 × 9, 3 × 6.", "جوڑے: 1 × 18، 2 × 9، 3 × 6"),
     T("Right! 1, 2, 3, 6, 9, 18.", "درست! 1، 2، 3، 6، 9، 18"),
     T("Three pairs: 1, 2, 3, 6, 9, 18. Six factors.", "تین جوڑے: 1، 2، 3، 6، 9، 18۔ چھ اجزائے ضربی۔"),
     common_wrong=[wrong(3, "Each pair has two factors: 6.", "ہر جوڑے میں دو اجزائے ضربی ہیں: 6")],
     qtype="recall", skill=FM_FACTORS),
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "Find the factors they share, then pick the biggest!", "مشترک اجزائے ضربی ڈھونڈیں، پھر سب سے بڑا چنیں!"),
    "text": T("Factors of 12: 1, 2, 3, 4, 6, 12. Factors of 18: 1, 2, 3, 6, 9, 18. The common factors are 1, 2, 3 and 6. The biggest is 6, so the highest common factor (HCF) of 12 and 18 is 6. We can make 6 bunches.",
              "12 کے اجزائے ضربی: 1، 2، 3، 4، 6، 12۔ 18 کے اجزائے ضربی: 1، 2، 3، 6، 9، 18۔ مشترک اجزائے ضربی 1، 2، 3 اور 6 ہیں۔ سب سے بڑا 6 ہے، اس لیے 12 اور 18 کا عاد اعظم 6 ہے۔ ہم 6 گچھے بنا سکتے ہیں۔")},
   number_question(
     "s4_hcf",
     T("So what is the HCF of 12 and 18?", "تو 12 اور 18 کا عاد اعظم کیا ہے؟"),
     S4,
     T("The biggest number in both lists of factors.", "دونوں فہرستوں میں سب سے بڑا مشترک عدد۔"),
     T("Right! HCF = 6.", "درست! عاد اعظم = 6"),
     T("Common factors 1, 2, 3, 6: the highest is 6.", "مشترک اجزائے ضربی 1، 2، 3، 6: سب سے بڑا 6"),
     common_wrong=[wrong(36, "36 is a common multiple. The HCF divides both numbers: 6.", "36 مشترک ضعف ہے۔ عاد اعظم دونوں اعداد کو تقسیم کرتا ہے: 6", "hcf_lcm_swap"),
                   wrong(3, "3 is a common factor, but 6 is higher.", "3 مشترک جزو ضربی ہے، مگر 6 بڑا ہے۔", "not_highest")]),
   {"id": "s5_primes", "type": "explain",
    "character": say("thinking", "For bigger numbers, use prime factors!", "بڑے اعداد کے لیے مفرد اجزائے ضربی استعمال کریں!"),
    "text": T("24 = 2 × 2 × 2 × 3 and 36 = 2 × 2 × 3 × 3. Match the primes they share: two 2s and one 3. Multiply only the shared ones: HCF = 2 × 2 × 3 = 12.",
              "24 = 2 × 2 × 2 × 3 اور 36 = 2 × 2 × 3 × 3۔ جو مفرد اعداد دونوں میں ہیں انہیں ملائیں: دو 2 اور ایک 3۔ صرف مشترک کو ضرب دیں: عاد اعظم = 2 × 2 × 3 = 12")},
   number_question(
     "s6_by_primes",
     T("Find the HCF of 24 and 36.", "24 اور 36 کا عاد اعظم معلوم کریں۔"),
     S6,
     T("Shared primes: two 2s and one 3.", "مشترک مفرد اعداد: دو 2 اور ایک 3"),
     T("Right! HCF = 2 × 2 × 3 = 12.", "درست! عاد اعظم = 2 × 2 × 3 = 12"),
     T("24 = 2 × 2 × 2 × 3, 36 = 2 × 2 × 3 × 3. Shared: 2 × 2 × 3 = 12.", "24 = 2 × 2 × 2 × 3، 36 = 2 × 2 × 3 × 3۔ مشترک: 2 × 2 × 3 = 12"),
     common_wrong=[wrong(72, "72 is a common multiple. Multiply only the SHARED primes: 12.", "72 مشترک ضعف ہے۔ صرف مشترک مفرد اعداد ضرب دیں: 12", "all_primes"),
                   wrong(6, "6 divides both, but 12 is higher: there are two shared 2s.", "6 دونوں کو تقسیم کرتا ہے، مگر 12 بڑا ہے: مشترک 2 دو ہیں۔", "not_highest")]),
   number_question(
     "s7_coprime",
     T("Find the HCF of 8 and 15.", "8 اور 15 کا عاد اعظم معلوم کریں۔"),
     S7,
     T("8 = 2 × 2 × 2 and 15 = 3 × 5. Do they share any prime?", "8 = 2 × 2 × 2 اور 15 = 3 × 5۔ کیا کوئی مفرد عدد مشترک ہے؟"),
     T("Right! Only 1 divides both. Numbers like this are called co-prime.", "درست! صرف 1 دونوں کو تقسیم کرتا ہے۔ ایسے اعداد باہم مفرد کہلاتے ہیں۔"),
     T("No shared primes, so the only common factor is 1. HCF = 1.", "کوئی مشترک مفرد عدد نہیں، اس لیے واحد مشترک جزو ضربی 1 ہے۔ عاد اعظم = 1"),
     common_wrong=[wrong(120, "120 is a common multiple. The HCF divides both: only 1 does.", "120 مشترک ضعف ہے۔ عاد اعظم دونوں کو تقسیم کرتا ہے: صرف 1 کرتا ہے۔", "hcf_lcm_swap"),
                   wrong(0, "Every pair of numbers has 1 as a common factor. HCF = 1.", "ہر دو اعداد کا 1 مشترک جزو ضربی ہوتا ہے۔ عاد اعظم = 1")]),
   number_question(
     "s8_balloons",
     T("Back to the party: 12 red and 18 green balloons make 6 identical bunches. How many RED balloons are in each bunch?", "واپس دعوت پر: 12 سرخ اور 18 سبز غبارے 6 ایک جیسے گچھوں میں ہیں۔ ہر گچھے میں کتنے سرخ غبارے ہیں؟"),
     S8,
     T("Share 12 red balloons among 6 bunches.", "12 سرخ غبارے 6 گچھوں میں بانٹیں۔"),
     T("Right! 2 red and 3 green in each bunch.", "درست! ہر گچھے میں 2 سرخ اور 3 سبز۔"),
     T("12 ÷ 6 = 2 red (and 18 ÷ 6 = 3 green) in each bunch.", "12 ÷ 6 = 2 سرخ (اور 18 ÷ 6 = 3 سبز) ہر گچھے میں۔"),
     common_wrong=[wrong(3, "3 is the green ones: 18 ÷ 6. Red: 12 ÷ 6 = 2.", "3 سبز ہیں: 18 ÷ 6۔ سرخ: 12 ÷ 6 = 2"),
                   wrong(6, "6 is the number of bunches. Red in each: 12 ÷ 6 = 2.", "6 گچھوں کی تعداد ہے۔ ہر ایک میں سرخ: 12 ÷ 6 = 2")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Usman says the HCF of 10 and 15 is 30. What went wrong?", "عثمان کہتا ہے 10 اور 15 کا عاد اعظم 30 ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("swap", "30 is a common multiple. The HCF divides both: 5.", "30 مشترک ضعف ہے۔ عاد اعظم دونوں کو تقسیم کرتا ہے: 5", True,
          "Yes! 5 divides 10 and 15. The HCF can't be bigger than the smaller number.", "جی ہاں! 5، 10 اور 15 کو تقسیم کرتا ہے۔ عاد اعظم چھوٹے عدد سے بڑا نہیں ہو سکتا۔"),
      opt("product", "It should be 150, 10 × 15.", "یہ 150 ہونا چاہیے، 10 × 15", False,
          "That is even bigger. The HCF divides both numbers: 5.", "یہ اور بھی بڑا ہے۔ عاد اعظم دونوں اعداد کو تقسیم کرتا ہے: 5", "hcf_lcm_swap"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "30 doesn't divide 10 or 15. Common factors are 1 and 5: HCF = 5.", "30، 10 یا 15 کو تقسیم نہیں کرتا۔ مشترک اجزائے ضربی 1 اور 5: عاد اعظم = 5", "hcf_lcm_swap"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can the HCF of 12 and 18 ever be bigger than 12? Can you teach me why or why not?",
                     "کیا 12 اور 18 کا عاد اعظم کبھی 12 سے بڑا ہو سکتا ہے؟ کیا آپ مجھے وجہ سمجھا سکتے ہیں؟"),
    "task": T("In your own words: why can the HCF never be bigger than the smaller of the two numbers?",
              "اپنے الفاظ میں بتائیں: عاد اعظم دونوں اعداد میں سے چھوٹے عدد سے کبھی بڑا کیوں نہیں ہو سکتا؟"),
    "key_idea": "The HCF must divide both numbers, and a number bigger than 12 cannot divide 12 exactly. So the HCF is at most the smaller number.",
    "levels": {
      "got_it": "Explains that the HCF has to divide the smaller number, and a factor can't be bigger than the number it divides.",
      "partly": "Says the HCF is a factor of both, or that it is small, without linking it to the smaller number.",
      "not_yet": "Says it can be bigger, gives no reason, or confuses it with the LCM."},
    "keywords": [
      ["divide", "factor", "تقسیم", "جزو", "taqseem"],
      ["smaller", "12", "چھوٹا", "chota"],
      ["bigger", "can't", "never", "بڑا", "نہیں"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The HCF has to divide 12, and nothing bigger than 12 can divide 12.",
                  "بہت خوب سمجھایا! عاد اعظم کو 12 تقسیم کرنا ہے، اور 12 سے بڑا کوئی عدد 12 کو تقسیم نہیں کر سکتا۔"),
      "partly": T("Good start! Now say: can a number bigger than 12 divide 12 exactly?", "اچھی شروعات! اب بتائیں: کیا 12 سے بڑا کوئی عدد 12 کو پورا تقسیم کر سکتا ہے؟"),
      "not_yet": T("Remember, the HCF must divide BOTH numbers. Could 13, 14 or 15 divide 12?",
                   "یاد کریں، عاد اعظم کو دونوں اعداد تقسیم کرنے ہیں۔ کیا 13، 14 یا 15، 12 کو تقسیم کر سکتے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_bigger",
     T("Find the HCF of 42 and 56.", "42 اور 56 کا عاد اعظم معلوم کریں۔"),
     S11,
     T("42 = 2 × 3 × 7 and 56 = 2 × 2 × 2 × 7.", "42 = 2 × 3 × 7 اور 56 = 2 × 2 × 2 × 7"),
     T("Right! HCF = 2 × 7 = 14.", "درست! عاد اعظم = 2 × 7 = 14"),
     T("Shared primes: one 2 and one 7. HCF = 2 × 7 = 14.", "مشترک مفرد اعداد: ایک 2 اور ایک 7۔ عاد اعظم = 2 × 7 = 14"),
     common_wrong=[wrong(7, "7 is shared, but so is a 2: 2 × 7 = 14.", "7 مشترک ہے، مگر ایک 2 بھی: 2 × 7 = 14", "not_highest"),
                   wrong(2, "2 is shared, but so is 7: 2 × 7 = 14.", "2 مشترک ہے، مگر 7 بھی: 2 × 7 = 14", "not_highest")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can find the HCF two ways!", "اب آپ عاد اعظم دو طریقوں سے معلوم کر سکتے ہیں!"),
    "text": T("The HCF is the biggest number that divides both numbers. List the factors and pick the biggest common one, or multiply the prime factors both numbers share. HCF of 12 and 18 = 6; of 24 and 36 = 12. If the HCF is 1, the numbers are co-prime.",
              "عاد اعظم وہ سب سے بڑا عدد ہے جو دونوں اعداد کو تقسیم کرے۔ اجزائے ضربی لکھ کر سب سے بڑا مشترک چنیں، یا دونوں کے مشترک مفرد اجزائے ضربی ضرب دیں۔ 12 اور 18 کا عاد اعظم = 6؛ 24 اور 36 کا = 12۔ اگر عاد اعظم 1 ہو تو اعداد باہم مفرد ہیں۔"),
    "points": [T("The HCF is never bigger than the smaller number.", "عاد اعظم چھوٹے عدد سے کبھی بڑا نہیں ہوتا۔"),
               T("Use the HCF to split things into the most equal groups.", "چیزوں کو زیادہ سے زیادہ برابر گروہوں میں بانٹنے کے لیے عاد اعظم استعمال کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_hcf", "type": "apply", "skill": SKILL, "step": number_question(
     "r_hcf",
     T("Find the HCF of 20 and 30.", "20 اور 30 کا عاد اعظم معلوم کریں۔"),
     R1,
     T("Which is the biggest number that divides both?", "سب سے بڑا عدد کون سا ہے جو دونوں کو تقسیم کرے؟"),
     T("Right! HCF = 10.", "درست! عاد اعظم = 10"),
     T("20 = 2 × 2 × 5, 30 = 2 × 3 × 5. Shared: 2 × 5 = 10.", "20 = 2 × 2 × 5، 30 = 2 × 3 × 5۔ مشترک: 2 × 5 = 10"),
     common_wrong=[wrong(60, "60 is a common multiple. The HCF divides both: 10.", "60 مشترک ضعف ہے۔ عاد اعظم دونوں کو تقسیم کرتا ہے: 10", "hcf_lcm_swap"),
                   wrong(5, "5 divides both, but 10 is higher.", "5 دونوں کو تقسیم کرتا ہے، مگر 10 بڑا ہے۔", "not_highest")],
     qtype=None)},
   {"id": "r_coprime", "type": "recall", "skill": SKILL, "step": number_question(
     "r_coprime",
     T("Find the HCF of 9 and 14.", "9 اور 14 کا عاد اعظم معلوم کریں۔"),
     R2,
     T("9 = 3 × 3 and 14 = 2 × 7. Any shared prime?", "9 = 3 × 3 اور 14 = 2 × 7۔ کوئی مشترک مفرد عدد؟"),
     T("Right! They are co-prime: HCF = 1.", "درست! یہ باہم مفرد ہیں: عاد اعظم = 1"),
     T("No shared primes, so HCF = 1.", "کوئی مشترک مفرد عدد نہیں، اس لیے عاد اعظم = 1"),
     common_wrong=[wrong(126, "126 is a common multiple. Only 1 divides both.", "126 مشترک ضعف ہے۔ صرف 1 دونوں کو تقسیم کرتا ہے۔", "hcf_lcm_swap")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Factors and Multiples unit. No textbook text or exercises were used.",
   "Two methods are taught: listing common factors (small numbers) and shared prime factors (bigger numbers). Division method can be added if the Punjab textbook uses it.",
   "Urdu terms to check: عاد اعظم (HCF), مشترک جزو ضربی (common factor), باہم مفرد (co-prime).",
   "The numbers were worked out in content/sources/g6-maths-05/hcf.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

from math import gcd, lcm

from common import (T, opt, say, wrong, number_question, write, prime_factors,
                    REF, REVIEW, FM_FACTORS, FM_HCF, FM_LCM)
from figs import attach, venn, two_trees_fig, multiples_rows, area_rects, en_list, ur_list

SKILL = FM_LCM


def multiples(n, upto):
    return list(range(n, upto + 1, n))


# s2
assert gcd(18, 24) == 6
# s3, s4: buses every 4 and 6 minutes
assert multiples(4, 24) == [4, 8, 12, 16, 20, 24] and multiples(6, 24) == [6, 12, 18, 24]
S4 = lcm(4, 6)
assert S4 == 12 and 4 * 6 == 24 and gcd(4, 6) == 2
# s5, s6: 12 and 18 by primes
assert prime_factors(12) == [2, 2, 3] and prime_factors(18) == [2, 3, 3]
S6 = lcm(12, 18)
assert S6 == 2 * 2 * 3 * 3 == 36 and gcd(12, 18) == 6 and 12 * 18 == 216
# s7: one divides the other
S7 = lcm(5, 15)
assert S7 == 15 and 5 * 15 == 75
# s8: HCF x LCM = product
S8 = 8 * 12 // gcd(8, 12)
assert S8 == lcm(8, 12) == 24 and gcd(8, 12) == 4
# s9
assert lcm(6, 9) == 18 and 6 * 9 == 54 and gcd(6, 9) == 3
# s10: the LCM is never smaller than the bigger number
assert all(lcm(a, b) >= max(a, b) for a in range(1, 40) for b in range(1, 40))
# s11: three numbers
S11 = lcm(lcm(2, 3), 4)
assert S11 == 12 and 2 * 3 * 4 == 24
# question bank and review
QB = lcm(10, 15)
assert QB == 30 and gcd(10, 15) == 5 and 10 * 15 == 150
R1 = lcm(9, 12)
assert R1 == 36 and 9 * 12 == 108 and gcd(9, 12) == 3
R2 = lcm(7, 8)
assert R2 == 56 and gcd(7, 8) == 1


lesson = {
 "id": "g6-maths-05-lowest-common-multiple",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the lowest common multiple (LCM) of two or three numbers by listing multiples and by prime factorisation.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Lowest common multiple (LCM)", "ذو اضعاف اقل"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": FM_FACTORS}, {"skill": FM_HCF}],
 "misconceptions": [
   {"id": "lcm_hcf_swap", "description": "Gives a common factor (often the HCF) instead of the LCM: LCM of 4 and 6 is 2."},
   {"id": "always_multiply", "description": "Always multiplies the two numbers: LCM of 4 and 6 is 24, which is a common multiple but not the lowest."},
   {"id": "shared_primes_only", "description": "Multiplies only the shared prime factors, which gives the HCF."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("What is the LCM of two numbers?", "دو اعداد کا ذو اضعاف اقل کیا ہوتا ہے؟"),
     "options": [
       opt("right", "The smallest number that both numbers divide into.", "سب سے چھوٹا عدد جسے دونوں اعداد پورا تقسیم کریں۔", True, "Yes! For 4 and 6 it is 12.", "جی ہاں! 4 اور 6 کا 12 ہے۔"),
       opt("hcf", "The biggest number that divides both.", "سب سے بڑا عدد جو دونوں کو تقسیم کرے۔", False, "That is the HCF. The LCM is a multiple of both.", "یہ عاد اعظم ہے۔ ذو اضعاف اقل دونوں کا ضعف ہوتا ہے۔", "lcm_hcf_swap"),
       opt("product", "Always the two numbers multiplied.", "ہمیشہ دونوں اعداد کا حاصل ضرب۔", False, "That is a common multiple, but often not the lowest: 4 × 6 = 24, but the LCM is 12.", "یہ مشترک ضعف ہے، مگر اکثر سب سے چھوٹا نہیں: 4 × 6 = 24، مگر ذو اضعاف اقل 12 ہے۔", "always_multiply"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Find the LCM of 10 and 15.", "10 اور 15 کا ذو اضعاف اقل معلوم کریں۔"),
     QB,
     T("Multiples of 15: 15, 30, 45 ... Which is the first one 10 also divides?", "15 کے اضعاف: 15، 30، 45 ... پہلا کون سا ہے جسے 10 بھی تقسیم کرے؟"),
     T("Right! LCM = 30.", "درست! ذو اضعاف اقل = 30"),
     T("15, 30: 30 ÷ 10 = 3. So the LCM is 30.", "15، 30: 30 ÷ 10 = 3۔ اس لیے ذو اضعاف اقل 30 ہے۔"),
     common_wrong=[wrong(5, "5 is the HCF. The LCM is a multiple of both: 30.", "5 عاد اعظم ہے۔ ذو اضعاف اقل دونوں کا ضعف ہے: 30", "lcm_hcf_swap"),
                   wrong(150, "150 is a common multiple, but 30 is lower.", "150 مشترک ضعف ہے، مگر 30 چھوٹا ہے۔", "always_multiply")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Bilal says the LCM of 6 and 9 is 54, because 6 × 9 = 54. What went wrong?", "بلال کہتا ہے 6 اور 9 کا ذو اضعاف اقل 54 ہے، کیونکہ 6 × 9 = 54۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("lowest", "54 is a common multiple, but 18 is lower.", "54 مشترک ضعف ہے، مگر 18 چھوٹا ہے۔", True,
           "Yes! 6 and 9 share a 3, so the LCM is 54 ÷ 3 = 18.", "جی ہاں! 6 اور 9 میں 3 مشترک ہے، اس لیے ذو اضعاف اقل 54 ÷ 3 = 18 ہے۔"),
       opt("nothing", "Nothing. Multiply to get the LCM.", "کوئی غلطی نہیں۔ ضرب دینے سے ذو اضعاف اقل ملتا ہے۔", False,
           "Only when the numbers share no factor. 18 is a common multiple lower than 54.", "صرف تب جب اعداد میں کوئی جزو ضربی مشترک نہ ہو۔ 18 مشترک ضعف ہے جو 54 سے چھوٹا ہے۔", "always_multiply"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_lcm", "front": T("What is the LCM?", "ذو اضعاف اقل کیا ہے؟"),
    "back": T("The lowest common multiple: the smallest number both numbers divide into. LCM of 4 and 6 = 12.", "سب سے چھوٹا مشترک ضعف: سب سے چھوٹا عدد جسے دونوں اعداد تقسیم کریں۔ 4 اور 6 کا ذو اضعاف اقل = 12")},
   {"id": "f_rule", "front": T("HCF × LCM = ?", "عاد اعظم × ذو اضعاف اقل = ؟"),
    "back": T("The two numbers multiplied. For 8 and 12: 4 × 24 = 96 = 8 × 12.", "دونوں اعداد کا حاصل ضرب۔ 8 اور 12 کے لیے: 4 × 24 = 96 = 8 × 12")},
 ],
 "home_tasks": [{"id": "h_bells", "text": T(
   "One light blinks every 3 seconds and another every 4 seconds. They blink together now. Count with a clock: after how many seconds do they blink together again?",
   "ایک بتی ہر 3 سیکنڈ بعد اور دوسری ہر 4 سیکنڈ بعد جلتی ہے۔ ابھی دونوں ایک ساتھ جلی ہیں۔ گھڑی سے گنیں: کتنے سیکنڈ بعد دوبارہ ایک ساتھ جلیں گی؟")}],
 "glossary": [T("Common multiple", "مشترک ضعف"), T("Lowest common multiple (LCM)", "ذو اضعاف اقل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "One bus leaves every 4 minutes, another every 6 minutes. They just left together. When do they leave together again?",
      "ایک بس ہر 4 منٹ بعد چلتی ہے، دوسری ہر 6 منٹ بعد۔ ابھی دونوں ساتھ چلیں۔ دوبارہ کب ساتھ چلیں گی؟"),
    "text": T("The answer must be a multiple of 4 AND of 6. Today we find the smallest such number. First, a quick check.", "جواب 4 اور 6 دونوں کا ضعف ہونا چاہیے۔ آج ہم ایسا سب سے چھوٹا عدد ڈھونڈیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Find the HCF of 18 and 24.", "18 اور 24 کا عاد اعظم معلوم کریں۔"),
     6,
     T("The biggest number that divides both.", "سب سے بڑا عدد جو دونوں کو تقسیم کرے۔"),
     T("Right! HCF = 6.", "درست! عاد اعظم = 6"),
     T("18 = 2 × 3 × 3, 24 = 2 × 2 × 2 × 3. Shared: 2 × 3 = 6.", "18 = 2 × 3 × 3، 24 = 2 × 2 × 2 × 3۔ مشترک: 2 × 3 = 6"),
     common_wrong=[wrong(3, "3 divides both, but 6 is higher.", "3 دونوں کو تقسیم کرتا ہے، مگر 6 بڑا ہے۔")],
     qtype="recall", skill=FM_HCF),
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "List the multiples and find the first one they share!", "اضعاف لکھیں اور پہلا مشترک ڈھونڈیں!"),
    "text": T("Multiples of 4: 4, 8, 12, 16, 20, 24 ... Multiples of 6: 6, 12, 18, 24 ... The common multiples are 12, 24, ... The lowest is 12, so the lowest common multiple (LCM) of 4 and 6 is 12. The buses leave together again after 12 minutes.",
              "4 کے اضعاف: 4، 8، 12، 16، 20، 24 ... 6 کے اضعاف: 6، 12، 18، 24 ... مشترک اضعاف 12، 24، ... ہیں۔ سب سے چھوٹا 12 ہے، اس لیے 4 اور 6 کا ذو اضعاف اقل 12 ہے۔ بسیں 12 منٹ بعد دوبارہ ساتھ چلیں گی۔")},
   number_question(
     "s4_lcm",
     T("So what is the LCM of 4 and 6?", "تو 4 اور 6 کا ذو اضعاف اقل کیا ہے؟"),
     S4,
     T("The first number in both lists of multiples.", "دونوں فہرستوں میں پہلا مشترک عدد۔"),
     T("Right! LCM = 12.", "درست! ذو اضعاف اقل = 12"),
     T("Common multiples 12, 24, ...: the lowest is 12.", "مشترک اضعاف 12، 24، ...: سب سے چھوٹا 12"),
     common_wrong=[wrong(24, "24 is a common multiple, but 12 comes first.", "24 مشترک ضعف ہے، مگر 12 پہلے آتا ہے۔", "always_multiply"),
                   wrong(2, "2 is the HCF. The LCM is a multiple of both: 12.", "2 عاد اعظم ہے۔ ذو اضعاف اقل دونوں کا ضعف ہے: 12", "lcm_hcf_swap")]),
   {"id": "s5_primes", "type": "explain",
    "character": say("thinking", "For bigger numbers, prime factors help again!", "بڑے اعداد کے لیے پھر مفرد اجزائے ضربی مدد کرتے ہیں!"),
    "text": T("12 = 2 × 2 × 3 and 18 = 2 × 3 × 3. Take each prime the most times it appears in either number: two 2s (from 12) and two 3s (from 18). LCM = 2 × 2 × 3 × 3 = 36.",
              "12 = 2 × 2 × 3 اور 18 = 2 × 3 × 3۔ ہر مفرد عدد اتنی بار لیں جتنی بار وہ کسی ایک عدد میں سب سے زیادہ آئے: دو 2 (12 سے) اور دو 3 (18 سے)۔ ذو اضعاف اقل = 2 × 2 × 3 × 3 = 36")},
   number_question(
     "s6_by_primes",
     T("Find the LCM of 12 and 18.", "12 اور 18 کا ذو اضعاف اقل معلوم کریں۔"),
     S6,
     T("Two 2s and two 3s.", "دو 2 اور دو 3"),
     T("Right! LCM = 2 × 2 × 3 × 3 = 36.", "درست! ذو اضعاف اقل = 2 × 2 × 3 × 3 = 36"),
     T("12 = 2 × 2 × 3, 18 = 2 × 3 × 3. Take two 2s and two 3s: 36.", "12 = 2 × 2 × 3، 18 = 2 × 3 × 3۔ دو 2 اور دو 3 لیں: 36"),
     common_wrong=[wrong(6, "6 is the HCF (only the shared primes). The LCM takes them all: 36.", "6 عاد اعظم ہے (صرف مشترک مفرد اعداد)۔ ذو اضعاف اقل سب لیتا ہے: 36", "shared_primes_only"),
                   wrong(216, "216 = 12 × 18 is a common multiple, but 36 is lower.", "216 = 12 × 18 مشترک ضعف ہے، مگر 36 چھوٹا ہے۔", "always_multiply")]),
   number_question(
     "s7_divides",
     T("Find the LCM of 5 and 15.", "5 اور 15 کا ذو اضعاف اقل معلوم کریں۔"),
     S7,
     T("Is 15 already a multiple of 5?", "کیا 15 پہلے ہی 5 کا ضعف ہے؟"),
     T("Right! 15 is a multiple of 5, so the LCM is 15 itself.", "درست! 15، 5 کا ضعف ہے، اس لیے ذو اضعاف اقل خود 15 ہے۔"),
     T("15 ÷ 5 = 3, so 15 is a multiple of both. LCM = 15.", "15 ÷ 5 = 3، اس لیے 15 دونوں کا ضعف ہے۔ ذو اضعاف اقل = 15"),
     common_wrong=[wrong(75, "75 is a common multiple, but 15 is lower.", "75 مشترک ضعف ہے، مگر 15 چھوٹا ہے۔", "always_multiply"),
                   wrong(5, "5 is the HCF. 5 is not a multiple of 15.", "5 عاد اعظم ہے۔ 5، 15 کا ضعف نہیں۔", "lcm_hcf_swap")]),
   number_question(
     "s8_rule",
     T("A shortcut: HCF × LCM = the two numbers multiplied. The HCF of 8 and 12 is 4. Use 8 × 12 = 96 to find their LCM.", "ایک آسان طریقہ: عاد اعظم × ذو اضعاف اقل = دونوں اعداد کا حاصل ضرب۔ 8 اور 12 کا عاد اعظم 4 ہے۔ 8 × 12 = 96 سے ان کا ذو اضعاف اقل معلوم کریں۔"),
     S8,
     T("4 × LCM = 96. Divide 96 by 4.", "4 × ذو اضعاف اقل = 96۔ 96 کو 4 سے تقسیم کریں۔"),
     T("Right! LCM = 96 ÷ 4 = 24.", "درست! ذو اضعاف اقل = 96 ÷ 4 = 24"),
     T("96 ÷ 4 = 24. Check: 24 ÷ 8 = 3 and 24 ÷ 12 = 2.", "96 ÷ 4 = 24۔ جانچ: 24 ÷ 8 = 3 اور 24 ÷ 12 = 2"),
     common_wrong=[wrong(96, "96 is the product. Divide it by the HCF: 96 ÷ 4 = 24.", "96 حاصل ضرب ہے۔ اسے عاد اعظم سے تقسیم کریں: 96 ÷ 4 = 24", "always_multiply"),
                   wrong(384, "Divide by the HCF, don't multiply: 96 ÷ 4 = 24.", "عاد اعظم سے تقسیم کریں، ضرب نہیں: 96 ÷ 4 = 24")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Sana says the LCM of 6 and 9 is 3. What went wrong?", "ثنا کہتی ہے 6 اور 9 کا ذو اضعاف اقل 3 ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("swap", "3 is the HCF. The LCM is a multiple of both: 18.", "3 عاد اعظم ہے۔ ذو اضعاف اقل دونوں کا ضعف ہے: 18", True,
          "Yes! 18 ÷ 6 = 3 and 18 ÷ 9 = 2. The LCM can't be smaller than the bigger number.", "جی ہاں! 18 ÷ 6 = 3 اور 18 ÷ 9 = 2۔ ذو اضعاف اقل بڑے عدد سے چھوٹا نہیں ہو سکتا۔"),
      opt("product", "It should be 54, 6 × 9.", "یہ 54 ہونا چاہیے، 6 × 9", False,
          "54 is a common multiple, but 18 is lower.", "54 مشترک ضعف ہے، مگر 18 چھوٹا ہے۔", "always_multiply"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "3 is not a multiple of 6 or 9. It is the HCF. LCM = 18.", "3، 6 یا 9 کا ضعف نہیں۔ یہ عاد اعظم ہے۔ ذو اضعاف اقل = 18", "lcm_hcf_swap"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can the LCM of 4 and 6 ever be smaller than 6? Can you teach me why or why not?",
                     "کیا 4 اور 6 کا ذو اضعاف اقل کبھی 6 سے چھوٹا ہو سکتا ہے؟ کیا آپ مجھے وجہ سمجھا سکتے ہیں؟"),
    "task": T("In your own words: why can the LCM never be smaller than the bigger of the two numbers?",
              "اپنے الفاظ میں بتائیں: ذو اضعاف اقل دونوں اعداد میں سے بڑے عدد سے کبھی چھوٹا کیوں نہیں ہو سکتا؟"),
    "key_idea": "The LCM must be a multiple of both numbers, and every multiple of 6 is 6 or more. So the LCM is at least the bigger number.",
    "levels": {
      "got_it": "Explains that the LCM is a multiple of the bigger number, and multiples are never smaller than the number itself.",
      "partly": "Says the LCM is a multiple of both, or that it is big, without linking it to the bigger number.",
      "not_yet": "Says it can be smaller, gives no reason, or confuses it with the HCF."},
    "keywords": [
      ["multiple", "times", "ضعف", "zarb", "ضرب"],
      ["bigger", "6", "بڑا", "bara"],
      ["smaller", "can't", "never", "چھوٹا", "نہیں"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The LCM is a multiple of 6, and every multiple of 6 is 6 or more.",
                  "بہت خوب سمجھایا! ذو اضعاف اقل 6 کا ضعف ہے، اور 6 کا ہر ضعف 6 یا اس سے زیادہ ہوتا ہے۔"),
      "partly": T("Good start! Now say: can a multiple of 6 be smaller than 6?", "اچھی شروعات! اب بتائیں: کیا 6 کا کوئی ضعف 6 سے چھوٹا ہو سکتا ہے؟"),
      "not_yet": T("Remember, the LCM is a multiple of BOTH numbers. List the multiples of 6: 6, 12, 18 ... Are any smaller than 6?",
                   "یاد کریں، ذو اضعاف اقل دونوں اعداد کا ضعف ہے۔ 6 کے اضعاف لکھیں: 6، 12، 18 ... کیا کوئی 6 سے چھوٹا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_three",
     T("Find the LCM of 2, 3 and 4.", "2، 3 اور 4 کا ذو اضعاف اقل معلوم کریں۔"),
     S11,
     T("Multiples of 4: 4, 8, 12 ... Which is the first one 2 and 3 both divide?", "4 کے اضعاف: 4، 8، 12 ... پہلا کون سا ہے جسے 2 اور 3 دونوں تقسیم کریں؟"),
     T("Right! LCM = 12.", "درست! ذو اضعاف اقل = 12"),
     T("4, 8, 12: 12 ÷ 2 = 6 and 12 ÷ 3 = 4. LCM = 12.", "4، 8، 12: 12 ÷ 2 = 6 اور 12 ÷ 3 = 4۔ ذو اضعاف اقل = 12"),
     common_wrong=[wrong(24, "24 = 2 × 3 × 4 is a common multiple, but 12 is lower.", "24 = 2 × 3 × 4 مشترک ضعف ہے، مگر 12 چھوٹا ہے۔", "always_multiply"),
                   wrong(1, "1 is the HCF. The LCM is a multiple of all three: 12.", "1 عاد اعظم ہے۔ ذو اضعاف اقل تینوں کا ضعف ہے: 12", "lcm_hcf_swap")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can find the LCM two ways!", "اب آپ ذو اضعاف اقل دو طریقوں سے معلوم کر سکتے ہیں!"),
    "text": T("The LCM is the smallest number that both numbers divide into. List multiples and pick the first common one, or take every prime the most times it appears. LCM of 4 and 6 = 12; of 12 and 18 = 36. HCF × LCM = the two numbers multiplied.",
              "ذو اضعاف اقل وہ سب سے چھوٹا عدد ہے جسے دونوں اعداد تقسیم کریں۔ اضعاف لکھ کر پہلا مشترک چنیں، یا ہر مفرد عدد اتنی بار لیں جتنی بار وہ سب سے زیادہ آئے۔ 4 اور 6 کا ذو اضعاف اقل = 12؛ 12 اور 18 کا = 36۔ عاد اعظم × ذو اضعاف اقل = دونوں اعداد کا حاصل ضرب۔"),
    "points": [T("The LCM is never smaller than the bigger number.", "ذو اضعاف اقل بڑے عدد سے کبھی چھوٹا نہیں ہوتا۔"),
               T("Use the LCM to find when repeating things happen together again.", "بار بار ہونے والی چیزیں دوبارہ کب ساتھ ہوں گی، یہ جاننے کے لیے ذو اضعاف اقل استعمال کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_lcm", "type": "apply", "skill": SKILL, "step": number_question(
     "r_lcm",
     T("Find the LCM of 9 and 12.", "9 اور 12 کا ذو اضعاف اقل معلوم کریں۔"),
     R1,
     T("Multiples of 12: 12, 24, 36 ... Which does 9 divide?", "12 کے اضعاف: 12، 24، 36 ... ان میں سے کسے 9 تقسیم کرتا ہے؟"),
     T("Right! LCM = 36.", "درست! ذو اضعاف اقل = 36"),
     T("9 = 3 × 3, 12 = 2 × 2 × 3. Take two 2s and two 3s: 36.", "9 = 3 × 3، 12 = 2 × 2 × 3۔ دو 2 اور دو 3 لیں: 36"),
     common_wrong=[wrong(108, "108 = 9 × 12 is a common multiple, but 36 is lower.", "108 = 9 × 12 مشترک ضعف ہے، مگر 36 چھوٹا ہے۔", "always_multiply"),
                   wrong(3, "3 is the HCF. The LCM is a multiple of both: 36.", "3 عاد اعظم ہے۔ ذو اضعاف اقل دونوں کا ضعف ہے: 36", "lcm_hcf_swap")],
     qtype=None)},
   {"id": "r_coprime", "type": "recall", "skill": SKILL, "step": number_question(
     "r_coprime",
     T("7 and 8 share no factor except 1. Find their LCM.", "7 اور 8 میں 1 کے سوا کوئی جزو ضربی مشترک نہیں۔ ان کا ذو اضعاف اقل معلوم کریں۔"),
     R2,
     T("When the HCF is 1, the LCM is the two numbers multiplied.", "جب عاد اعظم 1 ہو تو ذو اضعاف اقل دونوں اعداد کا حاصل ضرب ہوتا ہے۔"),
     T("Right! LCM = 7 × 8 = 56.", "درست! ذو اضعاف اقل = 7 × 8 = 56"),
     T("HCF = 1, so LCM = 7 × 8 = 56.", "عاد اعظم = 1، اس لیے ذو اضعاف اقل = 7 × 8 = 56"),
     common_wrong=[wrong(1, "1 is the HCF. The LCM is 7 × 8 = 56.", "1 عاد اعظم ہے۔ ذو اضعاف اقل 7 × 8 = 56 ہے۔", "lcm_hcf_swap"),
                   wrong(15, "That is 7 + 8. Multiply: 56.", "یہ 7 + 8 ہے۔ ضرب دیں: 56")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Factors and Multiples unit. No textbook text or exercises were used.",
   "Two methods are taught: listing multiples (small numbers) and prime factors (bigger numbers), plus HCF × LCM = product. Division method can be added if the Punjab textbook uses it.",
   "Urdu terms to check: ذو اضعاف اقل (LCM), مشترک ضعف (common multiple).",
   "The numbers were worked out in content/sources/g6-maths-05/lcm.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
BUS_A, BUS_B, BUS_UPTO = 4, 6, 24
assert multiples(BUS_A, BUS_UPTO) == [4, 8, 12, 16, 20, 24] and multiples(BUS_B, BUS_UPTO) == [6, 12, 18, 24]
COMMON = [v for v in multiples(BUS_A, BUS_UPTO) if v % BUS_B == 0]
assert COMMON == [12, 24] and COMMON[0] == S4


def bus_rows(ring):
    extra_en = f" The numbers both lines land on, {en_list(COMMON)}, are circled." if ring else ""
    extra_ur = f" جن اعداد پر دونوں لکیریں اترتی ہیں، {ur_list(COMMON)}، ان کے گرد دائرہ ہے۔" if ring else ""
    return multiples_rows(BUS_A, BUS_B, BUS_UPTO,
        f"Two number lines from 0 to {BUS_UPTO}, one above the other. Top: jumps of {BUS_A} (+{BUS_A}) landing on {en_list(multiples(BUS_A, BUS_UPTO))}. Bottom: jumps of {BUS_B} (+{BUS_B}) landing on {en_list(multiples(BUS_B, BUS_UPTO))}.{extra_en}",
        f"0 سے {BUS_UPTO} تک دو عددی لکیریں، ایک دوسرے کے نیچے۔ اوپر: {BUS_A} کی چھلانگیں (+{BUS_A}) جو {ur_list(multiples(BUS_A, BUS_UPTO))} پر اترتی ہیں۔ نیچے: {BUS_B} کی چھلانگیں (+{BUS_B}) جو {ur_list(multiples(BUS_B, BUS_UPTO))} پر اترتی ہیں۔{extra_ur}",
        ring=ring)


def split_primes(a, b):
    """The primes of a and b as (only a, both, only b), repeats kept."""
    pa, pb = prime_factors(a), prime_factors(b)
    both, rest_b = [], list(pb)
    for p in pa:
        if p in rest_b:
            both.append(p)
            rest_b.remove(p)
    rest_a = list(pa)
    for p in both:
        rest_a.remove(p)
    return rest_a, both, rest_b


def lcm_venn(a, b):
    ra, both, rb = split_primes(a, b)
    every = ra + both + rb
    product = 1
    for p in every:
        product *= p
    assert product == lcm(a, b)
    return venn(ra, both, rb, (a, b),
        f"Two overlapping circles for the prime factors. Left circle, {a}: {' × '.join(map(str, prime_factors(a)))}. Right circle, {b}: {' × '.join(map(str, prime_factors(b)))}. Shared primes in the middle: {en_list(both)}. Only in {a}: {en_list(ra)}. Only in {b}: {en_list(rb)}. Every prime in the picture, multiplied, gives the LCM: {' × '.join(map(str, every))}.",
        f"مفرد اجزائے ضربی کے دو ایک دوسرے پر چڑھے دائرے۔ بائیں دائرہ، {a}: {' × '.join(map(str, prime_factors(a)))}۔ دائیں دائرہ، {b}: {' × '.join(map(str, prime_factors(b)))}۔ مشترک مفرد اعداد درمیان میں: {ur_list(both)}۔ صرف {a} میں: {ur_list(ra)}۔ صرف {b} میں: {ur_list(rb)}۔ تصویر کے سب مفرد اعداد کو ضرب دینے سے ذو اضعاف اقل ملتا ہے: {' × '.join(map(str, every))}۔")


S8_A, S8_B, S8_H = 8, 12, gcd(8, 12)
assert S8_H * S8 == S8_A * S8_B

attach(lesson, {
    "s1_hook": bus_rows(ring=False),
    "s2_foundation": two_trees_fig(18, 24),
    "s3_see_it": bus_rows(ring=True),
    "s5_primes": lcm_venn(12, 18),
    "s6_by_primes": two_trees_fig(12, 18),
    "s8_rule": area_rects([dict(h=S8_A, w=S8_B, area=S8_A * S8_B), dict(h=S8_H, w=S8, w_text="?", area=S8_A * S8_B)],
        f"Two rectangles with the same area, {S8_A * S8_B}. The first is {S8_A} by {S8_B}. The second is {S8_H} high, and its length is a question mark.",
        f"ایک جیسے رقبے، {S8_A * S8_B}، والے دو مستطیل۔ پہلا {S8_A} ضرب {S8_B} ہے۔ دوسرا {S8_H} اونچا ہے، اور اس کی لمبائی کی جگہ سوالیہ نشان ہے۔"),
    "s12_summary": lcm_venn(12, 18),
    "qb_apply": two_trees_fig(10, 15),
    "r_lcm": two_trees_fig(9, 12),
    "r_coprime": two_trees_fig(7, 8),
})
write(lesson)

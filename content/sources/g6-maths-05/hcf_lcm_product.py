from math import gcd, lcm

from common import (T, opt, say, wrong, number_question, write, prime_factors,
                    BOOK, REVIEW, FM_LCM, FM_HCF_LCM)
from figs import attach, area_rects, two_trees_fig, venn, en_list, ur_list

SKILL = FM_HCF_LCM


def other_number(hcf, lcm_, known):
    """The missing number: product ÷ the known number."""
    product = hcf * lcm_
    assert product % known == 0
    other = product // known
    assert gcd(known, other) == hcf and lcm(known, other) == lcm_
    return other


# s2: foundation
S2 = lcm(6, 8)
assert S2 == 24 and 6 * 8 == 48 and gcd(6, 8) == 2
# s3, s4: 12 and 18
assert prime_factors(12) == [2, 2, 3] and prime_factors(18) == [2, 3, 3]
assert gcd(12, 18) == 6 and lcm(12, 18) == 36
S4 = gcd(12, 18) * lcm(12, 18)
assert S4 == 216 == 12 * 18 and 6 + 36 == 42 and 12 + 18 == 30
# s5: 4 and 10
assert gcd(4, 10) == 2 and lcm(4, 10) == 20
S5 = gcd(4, 10) * lcm(4, 10)
assert S5 == 40 == 4 * 10 and 2 + 20 == 22 and 4 + 10 == 14
# s6: LCM from HCF, 15 and 20
assert gcd(15, 20) == 5 and 15 * 20 == 300
S6 = 15 * 20 // gcd(15, 20)
assert S6 == lcm(15, 20) == 60 and 300 * 5 == 1500
# s7: missing number, HCF 4, LCM 48, one number 12
S7 = other_number(4, 48, 12)
assert S7 == 16 and 4 * 48 == 192 and 48 // 12 == 4 and 12 * 48 == 576
# s8: missing number, HCF 3, LCM 36, one number 9
S8 = other_number(3, 36, 9)
assert S8 == 12 and 3 * 36 == 108 and 36 // 9 == 4 and 108 // 3 == 36
# s9: three numbers 2, 4, 6 — the rule fails
assert gcd(gcd(2, 4), 6) == 2 and lcm(lcm(2, 4), 6) == 12
assert 2 * 12 == 24 and 2 * 4 * 6 == 48 and 24 != 48
# s10: why it works, 12 and 18 by primes
assert gcd(12, 18) == 2 * 3 and lcm(12, 18) == 2 * 2 * 3 * 3
assert all(gcd(a, b) * lcm(a, b) == a * b for a in range(1, 60) for b in range(1, 60))
# s11: HCF 7, LCM 84, one number 21
S11 = other_number(7, 84, 21)
assert S11 == 28 and 7 * 84 == 588 and 84 // 21 == 4 and 7 + 84 == 91
# question bank
assert gcd(6, 10) == 2 and 6 * 10 == 60
QB = 6 * 10 // gcd(6, 10)
assert QB == lcm(6, 10) == 30 and 60 * 2 == 120
QB_ERR = other_number(5, 30, 10)
assert QB_ERR == 15 and 30 // 10 == 3 and 5 * 30 == 150
# review
R1 = other_number(4, 24, 8)
assert R1 == 12 and 24 // 8 == 3 and 4 + 24 == 28
assert gcd(9, 12) == 3 and lcm(9, 12) == 36
R2 = gcd(9, 12) * lcm(9, 12)
assert R2 == 108 == 9 * 12 and 3 + 36 == 39 and 9 + 12 == 21


lesson = {
 "id": "g6-maths-05-hcf-times-lcm",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Know that for two numbers HCF × LCM = the product of the numbers, and use it to find the LCM or a missing number.", "textbook": BOOK}],
 "skills": [SKILL],
 "title": T("HCF × LCM", "عاد اعظم × ذو اضعاف اقل"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": FM_LCM}],
 "misconceptions": [
   {"id": "sum_not_product", "description": "Thinks HCF × LCM equals the sum of the two numbers, or adds the HCF and LCM instead of multiplying."},
   {"id": "wrong_division", "description": "Divides the wrong numbers to find the missing number, e.g. LCM ÷ known number, or product ÷ HCF."},
   {"id": "three_numbers", "description": "Uses HCF × LCM = product for three numbers, where it does not hold."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("For two numbers, HCF × LCM is equal to ...", "دو اعداد کے لیے عاد اعظم × ذو اضعاف اقل برابر ہے ..."),
     "options": [
       opt("product", "the two numbers multiplied.", "دونوں اعداد کا حاصل ضرب۔", True,
           "Yes! For 12 and 18: 6 × 36 = 216 = 12 × 18.", "جی ہاں! 12 اور 18 کے لیے: 6 × 36 = 216 = 12 × 18"),
       opt("sum", "the two numbers added.", "دونوں اعداد کا مجموعہ۔", False,
           "Check 12 and 18: 6 × 36 = 216, but 12 + 18 = 30. It is the product.", "12 اور 18 سے جانچیں: 6 × 36 = 216، مگر 12 + 18 = 30۔ یہ حاصل ضرب ہے۔", "sum_not_product"),
       opt("lcm", "the LCM again.", "دوبارہ ذو اضعاف اقل۔", False,
           "Only when the HCF is 1. For 12 and 18 it is 216, not 36.", "صرف تب جب عاد اعظم 1 ہو۔ 12 اور 18 کے لیے یہ 216 ہے، 36 نہیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("The HCF of 6 and 10 is 2. Use HCF × LCM = 6 × 10 to find the LCM.", "6 اور 10 کا عاد اعظم 2 ہے۔ عاد اعظم × ذو اضعاف اقل = 6 × 10 سے ذو اضعاف اقل معلوم کریں۔"),
     QB,
     T("6 × 10 = 60. Divide 60 by the HCF.", "6 × 10 = 60۔ 60 کو عاد اعظم سے تقسیم کریں۔"),
     T("Right! LCM = 60 ÷ 2 = 30.", "درست! ذو اضعاف اقل = 60 ÷ 2 = 30"),
     T("60 ÷ 2 = 30. Check: 30 ÷ 6 = 5 and 30 ÷ 10 = 3.", "60 ÷ 2 = 30۔ جانچ: 30 ÷ 6 = 5 اور 30 ÷ 10 = 3"),
     common_wrong=[wrong(60, "60 is the product. Divide it by the HCF: 60 ÷ 2 = 30.", "60 حاصل ضرب ہے۔ اسے عاد اعظم سے تقسیم کریں: 60 ÷ 2 = 30"),
                   wrong(120, "Divide by the HCF, don't multiply: 60 ÷ 2 = 30.", "عاد اعظم سے تقسیم کریں، ضرب نہیں: 60 ÷ 2 = 30", "wrong_division")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Two numbers have HCF 5 and LCM 30. One number is 10. Hina says the other is 30 ÷ 10 = 3. What went wrong?",
                 "دو اعداد کا عاد اعظم 5 اور ذو اضعاف اقل 30 ہے۔ ایک عدد 10 ہے۔ حنا کہتی ہے دوسرا 30 ÷ 10 = 3 ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("product_first", "She should find the product 5 × 30 = 150 first, then 150 ÷ 10 = 15.", "پہلے حاصل ضرب 5 × 30 = 150 نکالنا تھا، پھر 150 ÷ 10 = 15", True,
           "Yes! Check: HCF of 10 and 15 is 5, LCM is 30.", "جی ہاں! جانچ: 10 اور 15 کا عاد اعظم 5 اور ذو اضعاف اقل 30 ہے۔"),
       opt("add", "She should add: 5 + 30 = 35.", "اسے جمع کرنا تھا: 5 + 30 = 35", False,
           "We multiply HCF and LCM, not add: 5 × 30 = 150, so the other number is 150 ÷ 10 = 15.", "ہم عاد اعظم اور ذو اضعاف اقل کو ضرب دیتے ہیں، جمع نہیں: 5 × 30 = 150، اس لیے دوسرا عدد 150 ÷ 10 = 15", "sum_not_product"),
       opt("nothing", "Nothing. The answer is 3.", "کوئی غلطی نہیں۔ جواب 3 ہے۔", False,
           "3 can't be right: the HCF 5 must divide both numbers. Use 5 × 30 = 150, then 150 ÷ 10 = 15.", "3 درست نہیں ہو سکتا: عاد اعظم 5 دونوں اعداد کو تقسیم کرتا ہے۔ 5 × 30 = 150، پھر 150 ÷ 10 = 15", "wrong_division"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_rule", "front": T("For two numbers, HCF × LCM = ?", "دو اعداد کے لیے عاد اعظم × ذو اضعاف اقل = ؟"),
    "back": T("The two numbers multiplied. 12 and 18: 6 × 36 = 216 = 12 × 18.", "دونوں اعداد کا حاصل ضرب۔ 12 اور 18: 6 × 36 = 216 = 12 × 18")},
   {"id": "f_missing", "front": T("How do you find a missing number from the HCF and LCM?", "عاد اعظم اور ذو اضعاف اقل سے گمشدہ عدد کیسے معلوم کریں؟"),
    "back": T("Multiply HCF × LCM, then divide by the number you know. HCF 3, LCM 36, one number 9: 108 ÷ 9 = 12.", "عاد اعظم × ذو اضعاف اقل نکالیں، پھر معلوم عدد سے تقسیم کریں۔ عاد اعظم 3، ذو اضعاف اقل 36، ایک عدد 9: 108 ÷ 9 = 12")},
 ],
 "home_tasks": [{"id": "h_check", "text": T(
   "Pick two numbers from your house, such as the number of spoons and the number of plates. Find their HCF and LCM, then check that HCF × LCM equals the two numbers multiplied. Show a family member.",
   "اپنے گھر سے دو اعداد چنیں، جیسے چمچوں اور پلیٹوں کی تعداد۔ ان کا عاد اعظم اور ذو اضعاف اقل معلوم کریں، پھر جانچیں کہ عاد اعظم × ذو اضعاف اقل دونوں اعداد کے حاصل ضرب کے برابر ہے۔ گھر کے کسی فرد کو دکھائیں۔")}],
 "glossary": [T("Highest common factor (HCF)", "عاد اعظم"), T("Lowest common multiple (LCM)", "ذو اضعاف اقل"), T("Product", "حاصل ضرب")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "The HCF and LCM of two numbers hide a secret. Multiply them together and something surprising appears. Shall we find it?",
      "دو اعداد کے عاد اعظم اور ذو اضعاف اقل میں ایک راز چھپا ہے۔ انہیں ضرب دیں تو کچھ حیران کن نکلتا ہے۔ ڈھونڈیں؟"),
    "text": T("Today we find a link between the HCF, the LCM and the two numbers. First, a quick check on the LCM.",
              "آج ہم عاد اعظم، ذو اضعاف اقل اور دونوں اعداد کا تعلق ڈھونڈیں گے۔ پہلے ذو اضعاف اقل پر ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Find the LCM of 6 and 8.", "6 اور 8 کا ذو اضعاف اقل معلوم کریں۔"),
     S2,
     T("Multiples of 8: 8, 16, 24 ... Which is the first one 6 also divides?", "8 کے اضعاف: 8، 16، 24 ... پہلا کون سا ہے جسے 6 بھی تقسیم کرے؟"),
     T("Right! LCM = 24.", "درست! ذو اضعاف اقل = 24"),
     T("8, 16, 24: 24 ÷ 6 = 4. So the LCM is 24.", "8، 16، 24: 24 ÷ 6 = 4۔ اس لیے ذو اضعاف اقل 24 ہے۔"),
     common_wrong=[wrong(48, "48 = 6 × 8 is a common multiple, but 24 is lower.", "48 = 6 × 8 مشترک ضعف ہے، مگر 24 چھوٹا ہے۔"),
                   wrong(2, "2 is the HCF. The LCM is a multiple of both: 24.", "2 عاد اعظم ہے۔ ذو اضعاف اقل دونوں کا ضعف ہے: 24")],
     qtype="recall", skill=FM_LCM),
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "Look what happens with 12 and 18!", "دیکھیں 12 اور 18 کے ساتھ کیا ہوتا ہے!"),
    "text": T("For 12 and 18, the HCF is 6 and the LCM is 36. Now multiply: HCF × LCM = 6 × 36 = 216. And the two numbers multiplied: 12 × 18 = 216. The same! For any two numbers, HCF × LCM = the product of the two numbers.",
              "12 اور 18 کا عاد اعظم 6 اور ذو اضعاف اقل 36 ہے۔ اب ضرب دیں: عاد اعظم × ذو اضعاف اقل = 6 × 36 = 216۔ اور دونوں اعداد کا حاصل ضرب: 12 × 18 = 216۔ ایک جیسا! کسی بھی دو اعداد کے لیے عاد اعظم × ذو اضعاف اقل = دونوں اعداد کا حاصل ضرب۔")},
   number_question(
     "s4_check",
     T("The HCF of 12 and 18 is 6 and the LCM is 36. Work out HCF × LCM.", "12 اور 18 کا عاد اعظم 6 اور ذو اضعاف اقل 36 ہے۔ عاد اعظم × ذو اضعاف اقل معلوم کریں۔"),
     S4,
     T("6 × 36. It should match 12 × 18.", "6 × 36۔ یہ 12 × 18 کے برابر ہونا چاہیے۔"),
     T("Right! 6 × 36 = 216 = 12 × 18.", "درست! 6 × 36 = 216 = 12 × 18"),
     T("6 × 36 = 216, and 12 × 18 = 216 too.", "6 × 36 = 216، اور 12 × 18 بھی 216 ہے۔"),
     common_wrong=[wrong(42, "That is 6 + 36. Multiply: 6 × 36 = 216.", "یہ 6 + 36 ہے۔ ضرب دیں: 6 × 36 = 216", "sum_not_product"),
                   wrong(30, "That is 12 + 18. The rule uses the product: 216.", "یہ 12 + 18 ہے۔ اصول حاصل ضرب استعمال کرتا ہے: 216", "sum_not_product")]),
   number_question(
     "s5_another",
     T("Try 4 and 10. Their HCF is 2 and their LCM is 20. What is HCF × LCM?", "4 اور 10 لیں۔ ان کا عاد اعظم 2 اور ذو اضعاف اقل 20 ہے۔ عاد اعظم × ذو اضعاف اقل کیا ہے؟"),
     S5,
     T("2 × 20. Then compare with 4 × 10.", "2 × 20۔ پھر 4 × 10 سے ملائیں۔"),
     T("Right! 2 × 20 = 40 = 4 × 10. The rule works again.", "درست! 2 × 20 = 40 = 4 × 10۔ اصول پھر کام کرتا ہے۔"),
     T("2 × 20 = 40, and 4 × 10 = 40.", "2 × 20 = 40، اور 4 × 10 = 40"),
     common_wrong=[wrong(22, "That is 2 + 20. Multiply: 2 × 20 = 40.", "یہ 2 + 20 ہے۔ ضرب دیں: 2 × 20 = 40", "sum_not_product"),
                   wrong(14, "That is 4 + 10. HCF × LCM is the product: 40.", "یہ 4 + 10 ہے۔ عاد اعظم × ذو اضعاف اقل حاصل ضرب ہے: 40", "sum_not_product")]),
   number_question(
     "s6_find_lcm",
     T("The HCF of 15 and 20 is 5. Use 15 × 20 = 300 to find their LCM.", "15 اور 20 کا عاد اعظم 5 ہے۔ 15 × 20 = 300 سے ان کا ذو اضعاف اقل معلوم کریں۔"),
     S6,
     T("5 × LCM = 300. Divide 300 by 5.", "5 × ذو اضعاف اقل = 300۔ 300 کو 5 سے تقسیم کریں۔"),
     T("Right! LCM = 300 ÷ 5 = 60.", "درست! ذو اضعاف اقل = 300 ÷ 5 = 60"),
     T("300 ÷ 5 = 60. Check: 60 ÷ 15 = 4 and 60 ÷ 20 = 3.", "300 ÷ 5 = 60۔ جانچ: 60 ÷ 15 = 4 اور 60 ÷ 20 = 3"),
     common_wrong=[wrong(300, "300 is the product. Divide it by the HCF: 300 ÷ 5 = 60.", "300 حاصل ضرب ہے۔ اسے عاد اعظم سے تقسیم کریں: 300 ÷ 5 = 60"),
                   wrong(1500, "Divide by the HCF, don't multiply: 300 ÷ 5 = 60.", "عاد اعظم سے تقسیم کریں، ضرب نہیں: 300 ÷ 5 = 60", "wrong_division")]),
   number_question(
     "s7_missing",
     T("Two numbers have HCF 4 and LCM 48. One number is 12. Find the other number.", "دو اعداد کا عاد اعظم 4 اور ذو اضعاف اقل 48 ہے۔ ایک عدد 12 ہے۔ دوسرا عدد معلوم کریں۔"),
     S7,
     T("First 4 × 48 = 192. That is the product of the two numbers. Divide by 12.", "پہلے 4 × 48 = 192۔ یہ دونوں اعداد کا حاصل ضرب ہے۔ 12 سے تقسیم کریں۔"),
     T("Right! 192 ÷ 12 = 16.", "درست! 192 ÷ 12 = 16"),
     T("4 × 48 = 192, and 192 ÷ 12 = 16. Check: HCF of 12 and 16 is 4.", "4 × 48 = 192، اور 192 ÷ 12 = 16۔ جانچ: 12 اور 16 کا عاد اعظم 4 ہے۔"),
     common_wrong=[wrong(4, "That is 48 ÷ 12. Find the product first: 4 × 48 = 192, then 192 ÷ 12 = 16.", "یہ 48 ÷ 12 ہے۔ پہلے حاصل ضرب: 4 × 48 = 192، پھر 192 ÷ 12 = 16", "wrong_division"),
                   wrong(576, "That is 12 × 48. Divide the product by 12: 192 ÷ 12 = 16.", "یہ 12 × 48 ہے۔ حاصل ضرب کو 12 سے تقسیم کریں: 192 ÷ 12 = 16", "wrong_division")]),
   number_question(
     "s8_missing_again",
     T("Two numbers have HCF 3 and LCM 36. One number is 9. Find the other number.", "دو اعداد کا عاد اعظم 3 اور ذو اضعاف اقل 36 ہے۔ ایک عدد 9 ہے۔ دوسرا عدد معلوم کریں۔"),
     S8,
     T("3 × 36 = 108. Divide by the number you know.", "3 × 36 = 108۔ معلوم عدد سے تقسیم کریں۔"),
     T("Right! 108 ÷ 9 = 12.", "درست! 108 ÷ 9 = 12"),
     T("3 × 36 = 108, and 108 ÷ 9 = 12. Check: LCM of 9 and 12 is 36.", "3 × 36 = 108، اور 108 ÷ 9 = 12۔ جانچ: 9 اور 12 کا ذو اضعاف اقل 36 ہے۔"),
     common_wrong=[wrong(36, "That is 108 ÷ 3, the LCM. Divide by the known number 9: 12.", "یہ 108 ÷ 3 ہے، یعنی ذو اضعاف اقل۔ معلوم عدد 9 سے تقسیم کریں: 12", "wrong_division"),
                   wrong(4, "That is 36 ÷ 9. Use the product: 108 ÷ 9 = 12.", "یہ 36 ÷ 9 ہے۔ حاصل ضرب استعمال کریں: 108 ÷ 9 = 12", "wrong_division")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("For 2, 4 and 6, the HCF is 2 and the LCM is 12. Adeel says 2 × 4 × 6 must be 2 × 12 = 24. What went wrong?",
                "2، 4 اور 6 کا عاد اعظم 2 اور ذو اضعاف اقل 12 ہے۔ عدیل کہتا ہے 2 × 4 × 6 لازماً 2 × 12 = 24 ہوگا۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("two_only", "The rule is only for two numbers. 2 × 4 × 6 = 48, not 24.", "یہ اصول صرف دو اعداد کے لیے ہے۔ 2 × 4 × 6 = 48، 24 نہیں۔", True,
          "Yes! HCF × LCM = 24, but the product is 48. With three numbers the rule breaks.", "جی ہاں! عاد اعظم × ذو اضعاف اقل = 24، مگر حاصل ضرب 48 ہے۔ تین اعداد میں اصول کام نہیں کرتا۔"),
      opt("add", "He should add: 2 + 12 = 14.", "اسے جمع کرنا تھا: 2 + 12 = 14", False,
          "Adding never gives the product. And 2 × 4 × 6 = 48, so the rule fails for three numbers.", "جمع سے حاصل ضرب نہیں ملتا۔ اور 2 × 4 × 6 = 48، اس لیے تین اعداد میں اصول کام نہیں کرتا۔", "sum_not_product"),
      opt("nothing", "Nothing. The answer is 24.", "کوئی غلطی نہیں۔ جواب 24 ہے۔", False,
          "Multiply it out: 2 × 4 × 6 = 48. The rule only works for two numbers.", "ضرب دے کر دیکھیں: 2 × 4 × 6 = 48۔ اصول صرف دو اعداد کے لیے ہے۔", "three_numbers"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "12 = 2 × 2 × 3 and 18 = 2 × 3 × 3. Can you teach me why HCF × LCM gives 12 × 18?",
                     "12 = 2 × 2 × 3 اور 18 = 2 × 3 × 3۔ سمجھائیں: عاد اعظم × ذو اضعاف اقل سے 12 × 18 کیوں ملتا ہے؟"),
    "task": T("Use the prime factors: HCF = 2 × 3 and LCM = 2 × 2 × 3 × 3. In your own words, why does HCF × LCM equal 12 × 18?",
              "مفرد اجزائے ضربی استعمال کریں: عاد اعظم = 2 × 3 اور ذو اضعاف اقل = 2 × 2 × 3 × 3۔ اپنے الفاظ میں بتائیں کہ عاد اعظم × ذو اضعاف اقل، 12 × 18 کے برابر کیوں ہے؟"),
    "key_idea": "The HCF takes the shared primes and the LCM takes all the primes once each. Together they use every prime factor of 12 and of 18 exactly once, which is the same as 12 × 18.",
    "levels": {
      "got_it": "Explains that together the HCF and LCM contain all the prime factors of both numbers (2, 2, 3 and 2, 3, 3), so their product equals 12 × 18.",
      "partly": "Notices both sides equal 216 or lists the primes, without saying that all the primes of both numbers are used.",
      "not_yet": "Gives no reason, adds the numbers, or confuses the HCF and LCM."},
    "keywords": [
      ["prime", "factor", "مفرد", "جزو"],
      ["2", "3", "all", "every", "سب", "تمام"],
      ["216", "same", "equal", "برابر", "ایک جیسا"]],
    "fallback_feedback": {
      "got_it": T("Well explained! HCF and LCM together hold all the primes of 12 and 18, so they multiply to 12 × 18.",
                  "بہت خوب سمجھایا! عاد اعظم اور ذو اضعاف اقل میں مل کر 12 اور 18 کے سارے مفرد اجزا ہیں، اس لیے ان کا حاصل ضرب 12 × 18 ہے۔"),
      "partly": T("Good start! Now count the primes: how many 2s and 3s are in HCF × LCM, and in 12 × 18?",
                  "اچھی شروعات! اب مفرد اعداد گنیں: عاد اعظم × ذو اضعاف اقل میں کتنے 2 اور 3 ہیں، اور 12 × 18 میں؟"),
      "not_yet": T("Write HCF × LCM as 2 × 3 × 2 × 2 × 3 × 3. Now write 12 × 18 as primes. What do you see?",
                   "عاد اعظم × ذو اضعاف اقل کو 2 × 3 × 2 × 2 × 3 × 3 لکھیں۔ اب 12 × 18 کو مفرد اعداد میں لکھیں۔ کیا نظر آتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_bigger",
     T("Two numbers have HCF 7 and LCM 84. One number is 21. Find the other number.", "دو اعداد کا عاد اعظم 7 اور ذو اضعاف اقل 84 ہے۔ ایک عدد 21 ہے۔ دوسرا عدد معلوم کریں۔"),
     S11,
     T("7 × 84 = 588. Divide by 21.", "7 × 84 = 588۔ 21 سے تقسیم کریں۔"),
     T("Right! 588 ÷ 21 = 28.", "درست! 588 ÷ 21 = 28"),
     T("7 × 84 = 588, and 588 ÷ 21 = 28. Check: HCF of 21 and 28 is 7.", "7 × 84 = 588، اور 588 ÷ 21 = 28۔ جانچ: 21 اور 28 کا عاد اعظم 7 ہے۔"),
     common_wrong=[wrong(4, "That is 84 ÷ 21. Find the product first: 7 × 84 = 588, then ÷ 21 = 28.", "یہ 84 ÷ 21 ہے۔ پہلے حاصل ضرب: 7 × 84 = 588، پھر ÷ 21 = 28", "wrong_division"),
                   wrong(91, "That is 7 + 84. Multiply, then divide: 588 ÷ 21 = 28.", "یہ 7 + 84 ہے۔ ضرب دیں، پھر تقسیم کریں: 588 ÷ 21 = 28", "sum_not_product")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you know the secret of HCF and LCM!", "اب آپ عاد اعظم اور ذو اضعاف اقل کا راز جانتے ہیں!"),
    "text": T("For two numbers, HCF × LCM = the two numbers multiplied. 12 and 18: 6 × 36 = 216 = 12 × 18. To find the LCM, divide the product by the HCF. To find a missing number, multiply HCF × LCM, then divide by the number you know.",
              "دو اعداد کے لیے عاد اعظم × ذو اضعاف اقل = دونوں اعداد کا حاصل ضرب۔ 12 اور 18: 6 × 36 = 216 = 12 × 18۔ ذو اضعاف اقل کے لیے حاصل ضرب کو عاد اعظم سے تقسیم کریں۔ گمشدہ عدد کے لیے عاد اعظم × ذو اضعاف اقل نکال کر معلوم عدد سے تقسیم کریں۔"),
    "points": [T("The rule works for two numbers only, not three.", "یہ اصول صرف دو اعداد کے لیے ہے، تین کے لیے نہیں۔"),
               T("Multiply HCF and LCM; never add them.", "عاد اعظم اور ذو اضعاف اقل کو ضرب دیں؛ جمع نہ کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_missing", "type": "apply", "skill": SKILL, "step": number_question(
     "r_missing",
     T("Two numbers have HCF 4 and LCM 24. One number is 8. Find the other number.", "دو اعداد کا عاد اعظم 4 اور ذو اضعاف اقل 24 ہے۔ ایک عدد 8 ہے۔ دوسرا عدد معلوم کریں۔"),
     R1,
     T("4 × 24 = 96. Divide by 8.", "4 × 24 = 96۔ 8 سے تقسیم کریں۔"),
     T("Right! 96 ÷ 8 = 12.", "درست! 96 ÷ 8 = 12"),
     T("4 × 24 = 96, and 96 ÷ 8 = 12.", "4 × 24 = 96، اور 96 ÷ 8 = 12"),
     common_wrong=[wrong(3, "That is 24 ÷ 8. Use the product: 96 ÷ 8 = 12.", "یہ 24 ÷ 8 ہے۔ حاصل ضرب استعمال کریں: 96 ÷ 8 = 12", "wrong_division"),
                   wrong(28, "That is 4 + 24. Multiply, then divide: 96 ÷ 8 = 12.", "یہ 4 + 24 ہے۔ ضرب دیں، پھر تقسیم کریں: 96 ÷ 8 = 12", "sum_not_product")],
     qtype=None)},
   {"id": "r_rule", "type": "recall", "skill": SKILL, "step": number_question(
     "r_rule",
     T("The HCF of 9 and 12 is 3 and the LCM is 36. What is HCF × LCM?", "9 اور 12 کا عاد اعظم 3 اور ذو اضعاف اقل 36 ہے۔ عاد اعظم × ذو اضعاف اقل کیا ہے؟"),
     R2,
     T("It equals 9 × 12.", "یہ 9 × 12 کے برابر ہے۔"),
     T("Right! 3 × 36 = 108 = 9 × 12.", "درست! 3 × 36 = 108 = 9 × 12"),
     T("3 × 36 = 108, the same as 9 × 12.", "3 × 36 = 108، جو 9 × 12 کے برابر ہے۔"),
     common_wrong=[wrong(39, "That is 3 + 36. Multiply: 108.", "یہ 3 + 36 ہے۔ ضرب دیں: 108", "sum_not_product"),
                   wrong(21, "That is 9 + 12. The rule uses the product: 108.", "یہ 9 + 12 ہے۔ اصول حاصل ضرب استعمال کرتا ہے: 108", "sum_not_product")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Factors and Multiples unit. No textbook text or exercises were used.",
   "Teaches HCF × LCM = product of two numbers, using it to find the LCM and a missing number, and shows once (s9) that it fails for three numbers.",
   "Urdu terms to check: عاد اعظم (HCF), ذو اضعاف اقل (LCM), حاصل ضرب (product), گمشدہ عدد (missing number).",
   "The numbers were worked out in content/sources/g6-maths-05/hcf_lcm_product.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
def same_area(h1, w1, h2, w2, area_text=None):
    """Two rectangles drawn to one scale with the same area: h1 by w1 and
    h2 by w2. area_text: written inside both (or None)."""
    assert h1 * w1 == h2 * w2
    return [dict(h=h1, w=w1, area=area_text), dict(h=h2, w=w2, area=area_text)]


def missing_side(hcf, lcm_, known, other):
    """HCF by LCM, and the known number by '?' (drawn to scale)."""
    assert hcf * lcm_ == known * other
    return area_rects([dict(h=hcf, w=lcm_), dict(h=known, w=other, w_text="?")],
        f"Two rectangles drawn to the same scale with the same area. The first is {hcf} by {lcm_} (HCF by LCM). The second is {known} high (the number we know), and its length is a question mark (the other number).",
        f"ایک ہی پیمانے پر بنے دو مستطیل جن کا رقبہ برابر ہے۔ پہلا {hcf} ضرب {lcm_} ہے (عاد اعظم ضرب ذو اضعاف اقل)۔ دوسرا {known} اونچا ہے (جو عدد معلوم ہے)، اور اس کی لمبائی کی جگہ سوالیہ نشان ہے (دوسرا عدد)۔")


def one_rect(h, w, what_en, what_ur):
    return area_rects([dict(h=h, w=w, area="?")],
        f"A rectangle {h} by {w} ({what_en}), with a question mark inside for its area.",
        f"{h} ضرب {w} کا ایک مستطیل ({what_ur})، اندر رقبے کی جگہ سوالیہ نشان۔", min_h=26)


def split_primes(a, b):
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


RA, BOTH, RB = split_primes(12, 18)
assert BOTH == [2, 3] and RA == [2] and RB == [3]
assert 2 * 3 == gcd(12, 18) and 2 * 2 * 3 * 3 == lcm(12, 18)
S3_AREA = 12 * 18
assert S3_AREA == S4

attach(lesson, {
    "s2_foundation": two_trees_fig(6, 8),
    "s3_see_it": area_rects(same_area(12, 18, gcd(12, 18), lcm(12, 18), S3_AREA),
        f"Two rectangles drawn to the same scale. The first is 12 by 18 (the two numbers). The second is {gcd(12, 18)} by {lcm(12, 18)} (HCF by LCM). Both have area {S3_AREA}, written inside.",
        f"ایک ہی پیمانے پر بنے دو مستطیل۔ پہلا 12 ضرب 18 ہے (دونوں اعداد)۔ دوسرا {gcd(12, 18)} ضرب {lcm(12, 18)} ہے (عاد اعظم ضرب ذو اضعاف اقل)۔ دونوں کا رقبہ {S3_AREA} ہے، جو اندر لکھا ہے۔"),
    "s4_check": one_rect(gcd(12, 18), lcm(12, 18), "HCF by LCM", "عاد اعظم ضرب ذو اضعاف اقل"),
    "s5_another": one_rect(gcd(4, 10), lcm(4, 10), "HCF by LCM", "عاد اعظم ضرب ذو اضعاف اقل"),
    "s6_find_lcm": area_rects([dict(h=15, w=20, area=15 * 20), dict(h=gcd(15, 20), w=S6, w_text="?")],
        f"Two rectangles drawn to the same scale with the same area. The first is 15 by 20, with its area {15 * 20} written inside. The second is {gcd(15, 20)} high (the HCF), and its length is a question mark (the LCM).",
        f"ایک ہی پیمانے پر بنے دو مستطیل جن کا رقبہ برابر ہے۔ پہلا 15 ضرب 20 ہے، اس کے اندر رقبہ {15 * 20} لکھا ہے۔ دوسرا {gcd(15, 20)} اونچا ہے (عاد اعظم)، اور اس کی لمبائی کی جگہ سوالیہ نشان ہے (ذو اضعاف اقل)۔"),
    "s7_missing": missing_side(4, 48, 12, S7),
    "s8_missing_again": missing_side(3, 36, 9, S8),
    "s10_explain_why": venn(RA, BOTH, RB, (12, 18),
        "Two overlapping circles for the prime factors. Left circle, 12: 2 × 2 × 3. Right circle, 18: 2 × 3 × 3. The shared primes 2 and 3 are in the middle (their product is the HCF). Only in 12: 2. Only in 18: 3. All the primes in the picture together make the LCM.",
        "مفرد اجزائے ضربی کے دو ایک دوسرے پر چڑھے دائرے۔ بائیں دائرہ، 12: 2 × 2 × 3۔ دائیں دائرہ، 18: 2 × 3 × 3۔ مشترک مفرد اعداد 2 اور 3 درمیان میں ہیں (ان کا حاصل ضرب عاد اعظم ہے)۔ صرف 12 میں: 2۔ صرف 18 میں: 3۔ تصویر کے سب مفرد اعداد مل کر ذو اضعاف اقل بناتے ہیں۔"),
    "s11_bigger": missing_side(7, 84, 21, S11),
    "s12_summary": area_rects(same_area(12, 18, gcd(12, 18), lcm(12, 18), S3_AREA),
        f"Two rectangles drawn to the same scale: 12 by 18, and {gcd(12, 18)} by {lcm(12, 18)} (HCF by LCM). Both have area {S3_AREA}, written inside.",
        f"ایک ہی پیمانے پر بنے دو مستطیل: 12 ضرب 18، اور {gcd(12, 18)} ضرب {lcm(12, 18)} (عاد اعظم ضرب ذو اضعاف اقل)۔ دونوں کا رقبہ {S3_AREA} ہے، جو اندر لکھا ہے۔"),
    "qb_apply": area_rects([dict(h=6, w=10, area=6 * 10), dict(h=gcd(6, 10), w=QB, w_text="?")],
        f"Two rectangles drawn to the same scale with the same area. The first is 6 by 10, with its area {6 * 10} written inside. The second is {gcd(6, 10)} high (the HCF), and its length is a question mark (the LCM).",
        f"ایک ہی پیمانے پر بنے دو مستطیل جن کا رقبہ برابر ہے۔ پہلا 6 ضرب 10 ہے، اس کے اندر رقبہ {6 * 10} لکھا ہے۔ دوسرا {gcd(6, 10)} اونچا ہے (عاد اعظم)، اور اس کی لمبائی کی جگہ سوالیہ نشان ہے (ذو اضعاف اقل)۔"),
    "qb_find_error": missing_side(5, 30, 10, QB_ERR),
    "r_missing": missing_side(4, 24, 8, R1),
    "r_rule": one_rect(gcd(9, 12), lcm(9, 12), "HCF by LCM", "عاد اعظم ضرب ذو اضعاف اقل"),
})
write(lesson)

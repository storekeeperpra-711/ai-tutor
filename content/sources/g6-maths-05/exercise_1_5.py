"""Practice set for Exercise 1.5 of the book: use HCF × LCM = the product
of the two numbers to find the LCM, the HCF or a missing number. The
questions are new; only the kinds of question follow the book."""
from math import gcd, lcm

from common import (T, opt, say, wrong, number_question, choice_question, practice_lesson,
                    practice_intro, write, EX_SKILL, FM_HCF_LCM)
from figs import attach, area_rects

SKILL = EX_SKILL["1.5"]


def other_number(hcf, lcm_, known):
    """The missing number: HCF × LCM ÷ the known number."""
    product = hcf * lcm_
    assert product % known == 0
    other = product // known
    assert gcd(known, other) == hcf and lcm(known, other) == lcm_
    return other


def missing_side(hcf, lcm_, known, other):
    """HCF by LCM, and the known number by '?' (drawn to scale)."""
    assert hcf * lcm_ == known * other
    return area_rects([dict(h=hcf, w=lcm_), dict(h=known, w=other, w_text="?")],
        f"Two rectangles drawn to the same scale with the same area. The first is {hcf} by {lcm_} (HCF by LCM). The second is {known} high (the number we know), and its length is a question mark (the other number).",
        f"ایک ہی پیمانے پر بنے دو مستطیل جن کا رقبہ برابر ہے۔ پہلا {hcf} ضرب {lcm_} ہے (عاد اعظم ضرب ذو اضعاف اقل)۔ دوسرا {known} اونچا ہے (جو عدد معلوم ہے)، اور اس کی لمبائی کی جگہ سوالیہ نشان ہے (دوسرا عدد)۔")


# q2: 18 and 24
assert gcd(18, 24) == 6 and lcm(18, 24) == 72
Q2 = gcd(18, 24) * lcm(18, 24)
assert Q2 == 432 == 18 * 24 and 6 + 72 == 78
# q3: product 540, HCF 6 -> LCM
assert gcd(18, 30) == 6 and 18 * 30 == 540
Q3 = 540 // 6
assert Q3 == 90 == lcm(18, 30) and 540 * 6 == 3240
# q4: 20 and 48, LCM 240 -> HCF
assert 20 * 48 == 960 and lcm(20, 48) == 240
Q4 = 960 // 240
assert Q4 == 4 == gcd(20, 48) and 960 - 240 == 720
# q5 to q9: missing numbers
Q5 = other_number(5, 60, 15)
assert Q5 == 20 and 5 * 60 == 300 and 60 // 15 == 4
Q6 = other_number(9, 108, 27)
assert Q6 == 36 and 9 * 108 == 972 and 108 // 27 == 4 and 972 // 9 == 108
Q7 = other_number(12, 180, 36)
assert Q7 == 60 and 12 * 180 == 2160 and 180 // 36 == 5
Q8 = other_number(14, 168, 42)
assert Q8 == 56 and 14 * 168 == 2352 and 168 // 42 == 4 and 14 + 168 == 182
Q9 = other_number(15, 450, 90)
assert Q9 == 75 and 15 * 450 == 6750 and 450 // 90 == 5
# q10: can HCF 8 and LCM 60 belong to two numbers? No: 8 does not divide 60
assert 60 % 8 != 0
assert all(not (gcd(a, b) == 8 and lcm(a, b) == 60) for a in range(1, 61) for b in range(1, 61))
# q11: product 2028, HCF 13 -> LCM
assert gcd(39, 52) == 13 and 39 * 52 == 2028
Q11 = 2028 // 13
assert Q11 == 156 == lcm(39, 52) and 2028 * 13 == 26364
# find error: HCF 6, LCM 84, one number 12; product divided by the HCF instead
FE = other_number(6, 84, 12)
assert FE == 42 and 6 * 84 == 504 and 504 // 6 == 84 and 504 // 12 == 42
# question bank
QB_REC = gcd(10, 25) * lcm(10, 25)
assert gcd(10, 25) == 5 and lcm(10, 25) == 50 and QB_REC == 250 == 10 * 25
QB_APP = other_number(8, 96, 24)
assert QB_APP == 32 and 8 * 96 == 768 and 96 // 24 == 4
assert 6 * 90 == 540 and gcd(18, 30) * lcm(18, 30) == 540 and 18 + 30 != 540
# review
R1 = other_number(6, 90, 18)
assert R1 == 30 and 6 * 90 == 540 and 90 // 18 == 5
R2 = 1440 // 12
assert gcd(24, 60) == 12 and 24 * 60 == 1440 and R2 == 120 == lcm(24, 60)


lesson = practice_lesson(
 "1.5", script="exercise_1_5.py",
 title=T("Exercise 1.5 practice: HCF × LCM", "مشق 1.5 کی پریکٹس: عاد اعظم × ذو اضعاف اقل"),
 outcome="Use HCF × LCM = the product of two numbers to find the LCM, the HCF or a missing number.",
 prerequisites=[FM_HCF_LCM],
 misconceptions=[
   {"id": "sum_not_product", "description": "Adds the HCF and LCM, or the two numbers, instead of multiplying."},
   {"id": "wrong_division", "description": "Divides the wrong numbers to find the missing number, e.g. LCM ÷ known number, or product ÷ HCF."},
   {"id": "hcf_must_divide", "description": "Does not see that the HCF always divides the LCM, so some pairs of HCF and LCM are impossible."},
 ],
 steps=[
   practice_intro("1.5",
     "Here you use the rule HCF × LCM = the two numbers multiplied to find a missing LCM, HCF or number.",
     "اس میں آپ اصول عاد اعظم × ذو اضعاف اقل = دونوں اعداد کا حاصل ضرب استعمال کر کے گمشدہ ذو اضعاف اقل، عاد اعظم یا عدد معلوم کریں گے۔",
     "Exercise 1.5 uses one rule again and again. Let's make it easy!",
     "مشق 1.5 میں ایک ہی اصول بار بار آتا ہے۔ آئیں اسے آسان بنائیں!"),
   choice_question(
     "q1_rule",
     T("For any two numbers, HCF × LCM is equal to ...", "کسی بھی دو اعداد کے لیے عاد اعظم × ذو اضعاف اقل برابر ہے ..."),
     [opt("product", "the product of the two numbers", "دونوں اعداد کے حاصل ضرب کے", True,
          "Yes! For 4 and 6: 2 × 12 = 24 = 4 × 6.", "جی ہاں! 4 اور 6 کے لیے: 2 × 12 = 24 = 4 × 6"),
      opt("sum", "the sum of the two numbers", "دونوں اعداد کے مجموعے کے", False,
          "For 4 and 6: 2 × 12 = 24, but 4 + 6 = 10. It is the product.", "4 اور 6 کے لیے: 2 × 12 = 24، مگر 4 + 6 = 10۔ یہ حاصل ضرب ہے۔", "sum_not_product"),
      opt("bigger", "the bigger number", "بڑے عدد کے", False,
          "For 4 and 6 it is 24, not 6. It is the product of the two numbers.", "4 اور 6 کے لیے یہ 24 ہے، 6 نہیں۔ یہ دونوں اعداد کا حاصل ضرب ہے۔")],
     qtype="recall"),
   number_question(
     "q2_check",
     T("The HCF of 18 and 24 is 6 and their LCM is 72. Work out HCF × LCM.", "18 اور 24 کا عاد اعظم 6 اور ذو اضعاف اقل 72 ہے۔ عاد اعظم × ذو اضعاف اقل معلوم کریں۔"),
     Q2,
     T("6 × 72. It should be the same as 18 × 24.", "6 × 72۔ یہ 18 × 24 کے برابر ہونا چاہیے۔"),
     T("Right! 6 × 72 = 432 = 18 × 24.", "درست! 6 × 72 = 432 = 18 × 24"),
     T("6 × 72 = 432, and 18 × 24 = 432 too.", "6 × 72 = 432، اور 18 × 24 بھی 432 ہے۔"),
     common_wrong=[wrong(78, "That is 6 + 72. Multiply: 6 × 72 = 432.", "یہ 6 + 72 ہے۔ ضرب دیں: 6 × 72 = 432", "sum_not_product")],
     qtype="recall"),
   number_question(
     "q3_find_lcm",
     T("The product of two numbers is 540 and their HCF is 6. Find their LCM.", "دو اعداد کا حاصل ضرب 540 اور عاد اعظم 6 ہے۔ ان کا ذو اضعاف اقل معلوم کریں۔"),
     Q3,
     T("6 × LCM = 540. Divide 540 by 6.", "6 × ذو اضعاف اقل = 540۔ 540 کو 6 سے تقسیم کریں۔"),
     T("Right! LCM = 540 ÷ 6 = 90.", "درست! ذو اضعاف اقل = 540 ÷ 6 = 90"),
     T("HCF × LCM = product, so LCM = 540 ÷ 6 = 90.", "عاد اعظم × ذو اضعاف اقل = حاصل ضرب، اس لیے ذو اضعاف اقل = 540 ÷ 6 = 90"),
     common_wrong=[wrong(3240, "Divide by the HCF, don't multiply: 540 ÷ 6 = 90.", "عاد اعظم سے تقسیم کریں، ضرب نہیں: 540 ÷ 6 = 90", "wrong_division"),
                   wrong(540, "540 is the product. LCM = 540 ÷ 6 = 90.", "540 حاصل ضرب ہے۔ ذو اضعاف اقل = 540 ÷ 6 = 90")]),
   number_question(
     "q4_find_hcf",
     T("The LCM of 20 and 48 is 240. Use the rule to find their HCF.", "20 اور 48 کا ذو اضعاف اقل 240 ہے۔ اصول سے ان کا عاد اعظم معلوم کریں۔"),
     Q4,
     T("20 × 48 = 960. HCF × 240 = 960.", "20 × 48 = 960۔ عاد اعظم × 240 = 960"),
     T("Right! HCF = 960 ÷ 240 = 4.", "درست! عاد اعظم = 960 ÷ 240 = 4"),
     T("20 × 48 = 960, so HCF = 960 ÷ 240 = 4. Check: 4 divides 20 and 48.", "20 × 48 = 960، اس لیے عاد اعظم = 960 ÷ 240 = 4۔ جانچ: 4، 20 اور 48 کو تقسیم کرتا ہے۔"),
     common_wrong=[wrong(720, "That is 960 − 240. Divide: 960 ÷ 240 = 4.", "یہ 960 − 240 ہے۔ تقسیم کریں: 960 ÷ 240 = 4", "wrong_division")]),
   number_question(
     "q5_missing",
     T("Two numbers have HCF 5 and LCM 60. One number is 15. Find the other number.", "دو اعداد کا عاد اعظم 5 اور ذو اضعاف اقل 60 ہے۔ ایک عدد 15 ہے۔ دوسرا عدد معلوم کریں۔"),
     Q5,
     T("5 × 60 = 300 is the product of the two numbers. Divide by 15.", "5 × 60 = 300 دونوں اعداد کا حاصل ضرب ہے۔ 15 سے تقسیم کریں۔"),
     T("Right! 300 ÷ 15 = 20.", "درست! 300 ÷ 15 = 20"),
     T("5 × 60 = 300, and 300 ÷ 15 = 20. Check: HCF of 15 and 20 is 5, LCM is 60.", "5 × 60 = 300، اور 300 ÷ 15 = 20۔ جانچ: 15 اور 20 کا عاد اعظم 5 اور ذو اضعاف اقل 60 ہے۔"),
     common_wrong=[wrong(4, "That is 60 ÷ 15. Find the product first: 5 × 60 = 300, then 300 ÷ 15 = 20.", "یہ 60 ÷ 15 ہے۔ پہلے حاصل ضرب: 5 × 60 = 300، پھر 300 ÷ 15 = 20", "wrong_division"),
                   wrong(60, "That is 300 ÷ 5, the LCM. Divide by the known number 15: 20.", "یہ 300 ÷ 5 ہے، یعنی ذو اضعاف اقل۔ معلوم عدد 15 سے تقسیم کریں: 20", "wrong_division")]),
   number_question(
     "q6_missing",
     T("Two numbers have HCF 9 and LCM 108. One number is 27. Find the other number.", "دو اعداد کا عاد اعظم 9 اور ذو اضعاف اقل 108 ہے۔ ایک عدد 27 ہے۔ دوسرا عدد معلوم کریں۔"),
     Q6,
     T("9 × 108 = 972. Divide by 27.", "9 × 108 = 972۔ 27 سے تقسیم کریں۔"),
     T("Right! 972 ÷ 27 = 36.", "درست! 972 ÷ 27 = 36"),
     T("9 × 108 = 972, and 972 ÷ 27 = 36. Check: HCF of 27 and 36 is 9.", "9 × 108 = 972، اور 972 ÷ 27 = 36۔ جانچ: 27 اور 36 کا عاد اعظم 9 ہے۔"),
     common_wrong=[wrong(4, "That is 108 ÷ 27. Use the product: 972 ÷ 27 = 36.", "یہ 108 ÷ 27 ہے۔ حاصل ضرب استعمال کریں: 972 ÷ 27 = 36", "wrong_division"),
                   wrong(108, "That is 972 ÷ 9, the LCM. Divide by 27: 36.", "یہ 972 ÷ 9 ہے، یعنی ذو اضعاف اقل۔ 27 سے تقسیم کریں: 36", "wrong_division")]),
   number_question(
     "q7_missing",
     T("The HCF of two numbers is 12 and their LCM is 180. One of the numbers is 36. What is the other?", "دو اعداد کا عاد اعظم 12 اور ذو اضعاف اقل 180 ہے۔ ان میں سے ایک عدد 36 ہے۔ دوسرا کیا ہے؟"),
     Q7,
     T("12 × 180 = 2160. Divide by 36.", "12 × 180 = 2160۔ 36 سے تقسیم کریں۔"),
     T("Right! 2160 ÷ 36 = 60.", "درست! 2160 ÷ 36 = 60"),
     T("12 × 180 = 2160, and 2160 ÷ 36 = 60. Check: LCM of 36 and 60 is 180.", "12 × 180 = 2160، اور 2160 ÷ 36 = 60۔ جانچ: 36 اور 60 کا ذو اضعاف اقل 180 ہے۔"),
     common_wrong=[wrong(5, "That is 180 ÷ 36. Find the product first: 2160 ÷ 36 = 60.", "یہ 180 ÷ 36 ہے۔ پہلے حاصل ضرب: 2160 ÷ 36 = 60", "wrong_division")]),
   number_question(
     "q8_missing",
     T("Two numbers have HCF 14 and LCM 168. One number is 42. Find the other number.", "دو اعداد کا عاد اعظم 14 اور ذو اضعاف اقل 168 ہے۔ ایک عدد 42 ہے۔ دوسرا عدد معلوم کریں۔"),
     Q8,
     T("14 × 168 = 2352. Divide by 42.", "14 × 168 = 2352۔ 42 سے تقسیم کریں۔"),
     T("Right! 2352 ÷ 42 = 56.", "درست! 2352 ÷ 42 = 56"),
     T("14 × 168 = 2352, and 2352 ÷ 42 = 56. Check: HCF of 42 and 56 is 14.", "14 × 168 = 2352، اور 2352 ÷ 42 = 56۔ جانچ: 42 اور 56 کا عاد اعظم 14 ہے۔"),
     common_wrong=[wrong(4, "That is 168 ÷ 42. Use the product: 2352 ÷ 42 = 56.", "یہ 168 ÷ 42 ہے۔ حاصل ضرب استعمال کریں: 2352 ÷ 42 = 56", "wrong_division"),
                   wrong(182, "That is 14 + 168. Multiply, then divide: 2352 ÷ 42 = 56.", "یہ 14 + 168 ہے۔ ضرب دیں، پھر تقسیم کریں: 2352 ÷ 42 = 56", "sum_not_product")]),
   number_question(
     "q9_missing_big",
     T("Two numbers have HCF 15 and LCM 450. One number is 90. Find the other number.", "دو اعداد کا عاد اعظم 15 اور ذو اضعاف اقل 450 ہے۔ ایک عدد 90 ہے۔ دوسرا عدد معلوم کریں۔"),
     Q9,
     T("15 × 450 = 6750. Divide by 90.", "15 × 450 = 6750۔ 90 سے تقسیم کریں۔"),
     T("Right! 6750 ÷ 90 = 75.", "درست! 6750 ÷ 90 = 75"),
     T("15 × 450 = 6750, and 6750 ÷ 90 = 75. Check: HCF of 90 and 75 is 15, LCM is 450.", "15 × 450 = 6750، اور 6750 ÷ 90 = 75۔ جانچ: 90 اور 75 کا عاد اعظم 15 اور ذو اضعاف اقل 450 ہے۔"),
     common_wrong=[wrong(5, "That is 450 ÷ 90. Find the product first: 6750 ÷ 90 = 75.", "یہ 450 ÷ 90 ہے۔ پہلے حاصل ضرب: 6750 ÷ 90 = 75", "wrong_division")]),
   choice_question(
     "q10_possible",
     T("Can two numbers have HCF 8 and LCM 60?", "کیا دو اعداد کا عاد اعظم 8 اور ذو اضعاف اقل 60 ہو سکتا ہے؟"),
     [opt("no", "No, because 8 does not divide 60.", "نہیں، کیونکہ 8، 60 کو تقسیم نہیں کرتا۔", True,
          "Yes! The HCF divides both numbers, and both numbers divide the LCM, so the HCF must divide the LCM.", "جی ہاں! عاد اعظم دونوں اعداد کو تقسیم کرتا ہے، اور دونوں اعداد ذو اضعاف اقل کو، اس لیے عاد اعظم کو ذو اضعاف اقل تقسیم کرنا چاہیے۔"),
      opt("yes", "Yes, 8 × 60 = 480, so the numbers multiply to 480.", "ہاں، 8 × 60 = 480، اس لیے اعداد کا حاصل ضرب 480 ہے۔", False,
          "The product would be 480, but the HCF must divide the LCM, and 60 ÷ 8 is not exact. So it is impossible.", "حاصل ضرب 480 ہوتا، مگر عاد اعظم کو ذو اضعاف اقل تقسیم کرنا چاہیے، اور 60 ÷ 8 پورا نہیں۔ اس لیے یہ ناممکن ہے۔", "hcf_must_divide"),
      opt("bigger", "No, because the HCF must be bigger than 10.", "نہیں، کیونکہ عاد اعظم 10 سے بڑا ہونا چاہیے۔", False,
          "An HCF can be any size. The problem is that 8 does not divide 60.", "عاد اعظم کسی بھی سائز کا ہو سکتا ہے۔ مسئلہ یہ ہے کہ 8، 60 کو تقسیم نہیں کرتا۔")]),
   number_question(
     "q11_product_lcm",
     T("The product of two numbers is 2028 and their HCF is 13. Find their LCM.", "دو اعداد کا حاصل ضرب 2028 اور عاد اعظم 13 ہے۔ ان کا ذو اضعاف اقل معلوم کریں۔"),
     Q11,
     T("13 × LCM = 2028. Divide 2028 by 13.", "13 × ذو اضعاف اقل = 2028۔ 2028 کو 13 سے تقسیم کریں۔"),
     T("Right! 2028 ÷ 13 = 156.", "درست! 2028 ÷ 13 = 156"),
     T("LCM = 2028 ÷ 13 = 156. (The numbers could be 39 and 52.)", "ذو اضعاف اقل = 2028 ÷ 13 = 156۔ (اعداد 39 اور 52 ہو سکتے ہیں۔)"),
     common_wrong=[wrong(26364, "Divide by the HCF, don't multiply: 2028 ÷ 13 = 156.", "عاد اعظم سے تقسیم کریں، ضرب نہیں: 2028 ÷ 13 = 156", "wrong_division")]),
   choice_question(
     "q12_find_error",
     T("Two numbers have HCF 6 and LCM 84. One number is 12. Sadia works out 6 × 84 = 504, then 504 ÷ 6 = 84, and says the other number is 84. What went wrong?", "دو اعداد کا عاد اعظم 6 اور ذو اضعاف اقل 84 ہے۔ ایک عدد 12 ہے۔ سعدیہ 6 × 84 = 504 نکالتی ہے، پھر 504 ÷ 6 = 84، اور کہتی ہے دوسرا عدد 84 ہے۔ کیا غلطی ہوئی؟"),
     [opt("known", "She divided by the HCF. She should divide by the number she knows: 504 ÷ 12 = 42.", "اس نے عاد اعظم سے تقسیم کیا۔ اسے معلوم عدد سے تقسیم کرنا تھا: 504 ÷ 12 = 42", True,
          "Yes! Check: HCF of 12 and 42 is 6, LCM is 84.", "جی ہاں! جانچ: 12 اور 42 کا عاد اعظم 6 اور ذو اضعاف اقل 84 ہے۔"),
      opt("add", "She should add 6 + 84.", "اسے 6 + 84 جمع کرنا تھا۔", False,
          "Multiplying 6 × 84 = 504 was right. Then divide by 12, the known number: 42.", "6 × 84 = 504 ضرب درست تھی۔ پھر معلوم عدد 12 سے تقسیم کریں: 42", "sum_not_product"),
      opt("nothing", "Nothing. The other number is 84.", "کوئی غلطی نہیں۔ دوسرا عدد 84 ہے۔", False,
          "12 × 84 = 1008, not 504. Divide the product by 12: 504 ÷ 12 = 42.", "12 × 84 = 1008، 504 نہیں۔ حاصل ضرب کو 12 سے تقسیم کریں: 504 ÷ 12 = 42", "wrong_division")],
     qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Super! One rule, and you can find any missing number.", "بہت اچھے! ایک اصول، اور آپ کوئی بھی گمشدہ عدد معلوم کر سکتے ہیں۔"),
    "text": T("For two numbers, HCF × LCM = the first number × the second number. To find a missing number, multiply HCF × LCM, then divide by the number you know. To find the LCM, divide the product by the HCF; to find the HCF, divide the product by the LCM.",
              "دو اعداد کے لیے عاد اعظم × ذو اضعاف اقل = پہلا عدد × دوسرا عدد۔ گمشدہ عدد کے لیے عاد اعظم × ذو اضعاف اقل نکالیں، پھر معلوم عدد سے تقسیم کریں۔ ذو اضعاف اقل کے لیے حاصل ضرب کو عاد اعظم سے تقسیم کریں؛ عاد اعظم کے لیے حاصل ضرب کو ذو اضعاف اقل سے۔"),
    "points": [T("Check your answer: find the HCF and LCM of the two numbers you got.", "اپنا جواب جانچیں: جو دو اعداد ملے ان کا عاد اعظم اور ذو اضعاف اقل نکالیں۔"),
               T("The HCF always divides the LCM.", "عاد اعظم ہمیشہ ذو اضعاف اقل کو تقسیم کرتا ہے۔")]},
 ],
 bank=[
   {"id": "qb_rule", "type": "recall", "step": number_question(
     "qb_rule",
     T("The HCF of 10 and 25 is 5 and their LCM is 50. What is HCF × LCM?", "10 اور 25 کا عاد اعظم 5 اور ذو اضعاف اقل 50 ہے۔ عاد اعظم × ذو اضعاف اقل کیا ہے؟"),
     QB_REC,
     T("It equals 10 × 25.", "یہ 10 × 25 کے برابر ہے۔"),
     T("Right! 5 × 50 = 250 = 10 × 25.", "درست! 5 × 50 = 250 = 10 × 25"),
     T("5 × 50 = 250, the same as 10 × 25.", "5 × 50 = 250، جو 10 × 25 کے برابر ہے۔"),
     common_wrong=[wrong(55, "That is 5 + 50. Multiply: 250.", "یہ 5 + 50 ہے۔ ضرب دیں: 250", "sum_not_product")],
     qtype=None)},
   {"id": "qb_missing", "type": "apply", "step": number_question(
     "qb_missing",
     T("Two numbers have HCF 8 and LCM 96. One number is 24. Find the other number.", "دو اعداد کا عاد اعظم 8 اور ذو اضعاف اقل 96 ہے۔ ایک عدد 24 ہے۔ دوسرا عدد معلوم کریں۔"),
     QB_APP,
     T("8 × 96 = 768. Divide by 24.", "8 × 96 = 768۔ 24 سے تقسیم کریں۔"),
     T("Right! 768 ÷ 24 = 32.", "درست! 768 ÷ 24 = 32"),
     T("8 × 96 = 768, and 768 ÷ 24 = 32. Check: HCF of 24 and 32 is 8.", "8 × 96 = 768، اور 768 ÷ 24 = 32۔ جانچ: 24 اور 32 کا عاد اعظم 8 ہے۔"),
     common_wrong=[wrong(4, "That is 96 ÷ 24. Use the product: 768 ÷ 24 = 32.", "یہ 96 ÷ 24 ہے۔ حاصل ضرب استعمال کریں: 768 ÷ 24 = 32", "wrong_division")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": choice_question(
     "qb_find_error",
     T("18 and 30 have HCF 6 and LCM 90. Imran says HCF × LCM should equal 18 + 30 = 48. What went wrong?", "18 اور 30 کا عاد اعظم 6 اور ذو اضعاف اقل 90 ہے۔ عمران کہتا ہے عاد اعظم × ذو اضعاف اقل کو 18 + 30 = 48 ہونا چاہیے۔ کیا غلطی ہوئی؟"),
     [opt("product", "It equals the product: 18 × 30 = 540 = 6 × 90.", "یہ حاصل ضرب کے برابر ہے: 18 × 30 = 540 = 6 × 90", True,
          "Yes! The rule uses the two numbers multiplied, not added.", "جی ہاں! اصول میں دونوں اعداد ضرب ہوتے ہیں، جمع نہیں۔"),
      opt("lcm", "It equals the LCM, 90.", "یہ ذو اضعاف اقل، 90، کے برابر ہے۔", False,
          "6 × 90 = 540, not 90. It equals 18 × 30.", "6 × 90 = 540، 90 نہیں۔ یہ 18 × 30 کے برابر ہے۔"),
      opt("nothing", "Nothing. It is 48.", "کوئی غلطی نہیں۔ یہ 48 ہے۔", False,
          "6 × 90 = 540, which is 18 × 30, not 18 + 30.", "6 × 90 = 540، جو 18 × 30 ہے، 18 + 30 نہیں۔", "sum_not_product")],
     qtype=None)},
 ],
 review=[
   {"id": "r_missing", "type": "apply", "step": number_question(
     "r_missing",
     T("Two numbers have HCF 6 and LCM 90. One number is 18. Find the other number.", "دو اعداد کا عاد اعظم 6 اور ذو اضعاف اقل 90 ہے۔ ایک عدد 18 ہے۔ دوسرا عدد معلوم کریں۔"),
     R1,
     T("6 × 90 = 540. Divide by 18.", "6 × 90 = 540۔ 18 سے تقسیم کریں۔"),
     T("Right! 540 ÷ 18 = 30.", "درست! 540 ÷ 18 = 30"),
     T("6 × 90 = 540, and 540 ÷ 18 = 30.", "6 × 90 = 540، اور 540 ÷ 18 = 30"),
     common_wrong=[wrong(5, "That is 90 ÷ 18. Use the product: 540 ÷ 18 = 30.", "یہ 90 ÷ 18 ہے۔ حاصل ضرب استعمال کریں: 540 ÷ 18 = 30", "wrong_division")],
     qtype=None)},
   {"id": "r_lcm", "type": "recall", "step": number_question(
     "r_lcm",
     T("The product of two numbers is 1440 and their HCF is 12. Find their LCM.", "دو اعداد کا حاصل ضرب 1440 اور عاد اعظم 12 ہے۔ ان کا ذو اضعاف اقل معلوم کریں۔"),
     R2,
     T("12 × LCM = 1440.", "12 × ذو اضعاف اقل = 1440"),
     T("Right! 1440 ÷ 12 = 120.", "درست! 1440 ÷ 12 = 120"),
     T("LCM = 1440 ÷ 12 = 120.", "ذو اضعاف اقل = 1440 ÷ 12 = 120"),
     common_wrong=[wrong(1440 * 12, "Divide by the HCF, don't multiply: 1440 ÷ 12 = 120.", "عاد اعظم سے تقسیم کریں، ضرب نہیں: 1440 ÷ 12 = 120", "wrong_division")],
     qtype=None)},
 ],
 glossary=[T("Highest common factor (HCF)", "عاد اعظم"), T("Lowest common multiple (LCM)", "ذو اضعاف اقل"), T("Product", "حاصل ضرب")],
 flashcards=[
   {"id": "f_missing", "front": T("HCF 5, LCM 60, one number 15. How do you find the other?", "عاد اعظم 5، ذو اضعاف اقل 60، ایک عدد 15۔ دوسرا کیسے معلوم کریں؟"),
    "back": T("5 × 60 = 300, then 300 ÷ 15 = 20.", "5 × 60 = 300، پھر 300 ÷ 15 = 20")},
   {"id": "f_possible", "front": T("Can the HCF be 8 when the LCM is 60?", "کیا ذو اضعاف اقل 60 ہو تو عاد اعظم 8 ہو سکتا ہے؟"),
    "back": T("No. The HCF always divides the LCM, and 8 does not divide 60.", "نہیں۔ عاد اعظم ہمیشہ ذو اضعاف اقل کو تقسیم کرتا ہے، اور 8، 60 کو تقسیم نہیں کرتا۔")},
 ],
 home_task={"id": "h_puzzle", "text": T(
   "Choose two numbers secretly and tell a family member their HCF, their LCM and one of the numbers. Can they find your other number with HCF × LCM?",
   "چپکے سے دو اعداد چنیں اور گھر کے کسی فرد کو ان کا عاد اعظم، ذو اضعاف اقل اور ایک عدد بتائیں۔ کیا وہ عاد اعظم × ذو اضعاف اقل سے آپ کا دوسرا عدد معلوم کر سکتے ہیں؟")},
 notes=["Covers the rule (q1, q2), finding the LCM or HCF from the product (q3, q4, q11), finding a missing number (q5 to q9) and why the HCF must divide the LCM (q10).",
        "Urdu terms to check: حاصل ضرب (product), گمشدہ عدد (missing number)."],
 minutes=16,
)

attach(lesson, {
    "q3_find_lcm": area_rects([dict(h=6, w=Q3, w_text="?", area=540)],
        "A rectangle with area 540 written inside. Its height is 6 (the HCF) and its length is a question mark (the LCM).",
        "ایک مستطیل جس کے اندر رقبہ 540 لکھا ہے۔ اس کی اونچائی 6 ہے (عاد اعظم) اور لمبائی کی جگہ سوالیہ نشان ہے (ذو اضعاف اقل)۔", min_h=40),
    "q5_missing": missing_side(5, 60, 15, Q5),
    "q7_missing": missing_side(12, 180, 36, Q7),
})
write(lesson)

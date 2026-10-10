"""Practice set for Exercise 4.3 of the book: percentage of a 100-grid,
percentage and fractions, a percentage of a quantity, finding the whole,
comparing by percentage and increasing or decreasing by a percentage. The
questions are new; only the kinds of question follow the book."""
from fractions import Fraction as F
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, EX_SKILL,
                    PC_MEANING, PC_CONVERT, PC_OF_AMOUNT, PC_FIND, PC_CHANGE, PC_WORD_PROBLEMS)

SKILL = EX_SKILL["4.3"]


def pct(p, amount):
    """p% of amount, exactly; must be a whole number."""
    x = F(p) * F(amount) / 100
    assert x.denominator == 1, (p, amount)
    return int(x)


def as_pct(part, whole):
    x = F(part) * 100 / F(whole)
    assert x.denominator == 1, (part, whole)
    return int(x)


# q1: 37 of the 100 squares are shaded
Q1 = as_pct(37, 100)
assert Q1 == 37
# q2: 45% as a fraction in the simplest form is 9/20
assert F(45, 100) == F(9, 20) and F(45, 100) != F(45, 10) and F(9, 20) != F(4, 5)
# q3: 7/25 as a percentage
Q3 = as_pct(7, 25)
assert Q3 == 28 and F(7, 25) == F(28, 100)
# q4: 35% of 240
Q4 = pct(35, 240)
assert Q4 == 84 and 240 - Q4 == 156 and 240 // 35 == 6
# q5: 15 out of 60 as a percentage
Q5 = as_pct(15, 60)
assert Q5 == 25 and 15 * 60 == 900
# q6: 12 is 20% of the whole
Q6 = 12 * 100 // 20
assert 12 * 100 % 20 == 0 and Q6 == 60 and pct(20, Q6) == 12 and F(20, 100) * 12 == F(12, 5)
# q7: Hamid 42/60, Bina 36/50
P7_H, P7_B = as_pct(42, 60), as_pct(36, 50)
assert (P7_H, P7_B) == (70, 72) and P7_B > P7_H and 42 > 36
# q8: salary Rs 40,000 up by 15%
Q8 = 40000 + pct(15, 40000)
assert Q8 == 46000 and pct(15, 40000) == 6000 and 40000 - 6000 == 34000
# q9: price Rs 2,500 reduced by 12%
Q9 = 2500 - pct(12, 2500)
assert Q9 == 2200 and pct(12, 2500) == 300 and 2500 + 300 == 2800
# q10: population from 8,000 to 9,200
Q10 = as_pct(9200 - 8000, 8000)
assert Q10 == 15 and F(1200, 9200) != F(15, 100) and 9200 - 8000 == 1200
# q11: 8% of 250 students absent; how many present
Q11 = 250 - pct(8, 250)
assert Q11 == 230 and pct(8, 250) == 20
# q12: 18% of a number is 54
Q12 = 54 * 100 // 18
assert 54 * 100 % 18 == 0 and Q12 == 300 and pct(18, Q12) == 54 and 54 // 18 == 3
assert F(18, 100) * 54 == F(972, 100)
# q13 (find error): price rose from 80 to 100; the rise is 20, so 20/80 = 25%
Q13 = as_pct(100 - 80, 80)
assert Q13 == 25 and as_pct(20, 100) == 20
# bank and review
QB_REC = as_pct(9, 20)
assert QB_REC == 45
QB_APP = pct(15, 360)
assert QB_APP == 54 and 360 - 54 == 306
R_REC = as_pct(3, 5)
assert R_REC == 60
R_APP = 600 + pct(10, 600)
assert R_APP == 660 and pct(10, 600) == 60

lesson = practice_lesson(
 "4.3", script="exercise_4_3.py",
 title=T("Exercise 4.3 practice: percentage", "مشق 4.3 کی پریکٹس: فیصد"),
 outcome="Express a fraction as a percentage and back, find a percentage of a quantity and the whole from a part, compare two quantities by percentage, and increase or decrease a quantity by a percentage.",
 prerequisites=[PC_MEANING, PC_CONVERT, PC_OF_AMOUNT, PC_FIND, PC_CHANGE, PC_WORD_PROBLEMS],
 misconceptions=[
   {"id": "pc_not_over_100", "description": "Writes a percent over 10 or 1000 instead of over 100 when changing it to a fraction."},
   {"id": "pc_not_simplified", "description": "Leaves the fraction as 45/100 or stops before it is in lowest terms."},
   {"id": "pc_of_whole", "description": "Gives the amount itself, or the whole minus the amount, when the percentage of it is asked."},
   {"id": "pc_times_whole", "description": "Multiplies the part by 100 but forgets to divide by the whole."},
   {"id": "pc_whole_as_part", "description": "Finds a percentage of the part when the whole is wanted, instead of dividing by the percentage."},
   {"id": "pc_compare_numbers", "description": "Compares the raw marks of two different totals instead of the percentages."},
   {"id": "pc_change_only", "description": "Gives the amount of the change instead of the new price or salary."},
   {"id": "pc_wrong_base", "description": "Finds a percentage change by dividing by the new value instead of the original one."},
   {"id": "stops_early", "description": "Finds the 1% value but does not multiply by 100 to get the whole."},
   {"id": "pc_wrong_way", "description": "Adds a percentage decrease or subtracts a percentage increase."},
 ],
 steps=[
   practice_intro("4.3",
     "Here you read percentages from a 100-grid, change percentages and fractions, find a percentage of a quantity or the whole, compare by percentage and work out a percentage increase or decrease.",
     "اس میں آپ 100 خانوں والے گرڈ سے فیصد پڑھیں گے، فیصد اور کسر بدلیں گے، کسی مقدار کا فیصد یا کل معلوم کریں گے، فیصد سے موازنہ کریں گے اور فیصد اضافہ یا کمی نکالیں گے۔",
     "Exercise 4.3 is about percentage. Ready?", "مشق 4.3 فیصد کے بارے میں ہے۔ تیار؟"),
   nq("q1_grid", ("A grid has 100 equal squares and 37 of them are shaded. What percentage of the grid is shaded?", "ایک گرڈ میں 100 برابر خانے ہیں اور ان میں سے 37 رنگین ہیں۔ گرڈ کا کتنا فیصد رنگین ہے؟"), Q1,
      ("Percent means out of 100.", "فیصد کا مطلب ہے سو میں سے۔"),
      ("Right! 37 out of 100 is 37%.", "درست! 100 میں سے 37، یعنی 37 فیصد۔"),
      ("There are 100 squares, so 37 shaded squares is 37 per cent, or 37%.", "کل 100 خانے ہیں، اس لیے 37 رنگین خانے 37 فی صد ہیں، یعنی 37%۔"),
      [(63, "That is the part not shaded. The shaded part is 37%.", "یہ رنگین نہ ہونے والا حصہ ہے۔ رنگین حصہ 37% ہے۔", "pc_of_whole")],
      qtype="recall"),
   ch("q2_to_fraction", ("Write 45% as a fraction in its simplest form.", "45% کو سادہ ترین کسر کی صورت میں لکھیں۔"),
      ("9/20", "9/20", "Yes! 45% = 45/100 and dividing the top and bottom by 5 gives 9/20.", "جی ہاں! 45% = 45/100 اور اوپر نیچے کو 5 سے تقسیم کرنے پر 9/20 ملتا ہے۔"),
      [("45/100", "45/100", "That is correct but not in its simplest form. Divide both by 5.", "یہ درست ہے مگر سادہ ترین صورت میں نہیں۔ دونوں کو 5 سے تقسیم کریں۔", "pc_not_simplified"),
       ("45/10", "45/10", "Percent means out of 100, not out of 10.", "فیصد کا مطلب سو میں سے ہے، دس میں سے نہیں۔", "pc_not_over_100"),
       ("4/5", "4/5", "4/5 is 80%. Put 45 over 100 and simplify.", "4/5 تو 80% ہے۔ 45 کو 100 پر لکھیں اور سادہ کریں۔")],
      0, qtype="recall"),
   {"id": "s_rules", "type": "explain",
    "character": say("thinking", "Per cent means out of 100. Put the number over 100.", "فیصد کا مطلب ہے سو میں سے۔ عدد کو 100 پر لکھیں۔"),
    "text": T("Per cent means out of 100, written %. To change a percentage into a fraction, put it over 100 and simplify: 45% = 45/100 = 9/20. To change a fraction into a percentage, make the denominator 100: 7/25 = 28/100 = 28%. To find a percentage of a quantity, multiply: 35% of 240 = 35/100 × 240 = 84. To express one quantity as a percentage of another, divide and multiply by 100: 15 out of 60 is 15/60 × 100 = 25%. To find the whole, the total is the given quantity divided by the percentage: if 12 is 20%, the whole is 12 ÷ 20 × 100 = 60. To increase by a percentage, add the amount: new = old + percentage of old. To decrease, subtract it. A percentage change is the change divided by the original, times 100.",
              "فیصد کا مطلب ہے سو میں سے، جسے % لکھتے ہیں۔ فیصد کو کسر بنانے کے لیے اسے 100 پر لکھیں اور سادہ کریں: 45% = 45/100 = 9/20۔ کسر کو فیصد بنانے کے لیے نسب نما 100 بنائیں: 7/25 = 28/100 = 28%۔ کسی مقدار کا فیصد نکالنے کے لیے ضرب دیں: 240 کا 35% = 35/100 × 240 = 84۔ ایک مقدار کو دوسری کے فیصد کے طور پر لکھنے کے لیے تقسیم کریں اور 100 سے ضرب دیں: 60 میں سے 15 یعنی 15/60 × 100 = 25%۔ کل معلوم کرنے کے لیے دی گئی مقدار کو فیصد سے تقسیم کریں: اگر 12، 20% ہے تو کل 12 ÷ 20 × 100 = 60۔ فیصد اضافے کے لیے رقم جمع کریں: نیا = پرانا + پرانے کا فیصد۔ کمی کے لیے گھٹائیں۔ فیصد تبدیلی تبدیلی کو اصل سے تقسیم کر کے 100 سے ضرب دینے سے ملتی ہے۔")},
   nq("q3_fraction_to_percent", ("Write 7/25 as a percentage.", "7/25 کو فیصد کی صورت میں لکھیں۔"), Q3,
      ("Make the denominator 100: what do you multiply 25 by?", "نسب نما 100 بنائیں: 25 کو کس سے ضرب دیں؟"),
      ("Right! 7/25 = 28/100 = 28%.", "درست! 7/25 = 28/100 = 28%"),
      ("25 × 4 = 100, so 7/25 = 28/100 = 28%.", "25 × 4 = 100، اس لیے 7/25 = 28/100 = 28%"),
      [(7, "7 out of 25 is not 7 out of 100. Multiply the top and bottom by 4: 28%.", "25 میں سے 7، 100 میں سے 7 نہیں ہوتا۔ اوپر اور نیچے کو 4 سے ضرب دیں: 28%", "pc_not_over_100")]),
   nq("q4_percent_of", ("Find 35% of 240 students.", "240 طلبہ کا 35% معلوم کریں۔"), Q4,
      ("35% = 35/100. Multiply it by 240.", "35% = 35/100۔ اسے 240 سے ضرب دیں۔"),
      ("Right! 35/100 × 240 = 84.", "درست! 35/100 × 240 = 84"),
      ("10% of 240 is 24, so 30% is 72 and 5% is 12. Together: 84.", "240 کا 10% یعنی 24، اس لیے 30% یعنی 72 اور 5% یعنی 12۔ کل: 84"),
      [(156, "That is the rest (240 − 84). 35% of 240 is 84.", "یہ باقی ہے (240 − 84)۔ 240 کا 35% ہے 84", "pc_of_whole"),
       (6, "That divides 240 by 35. Multiply 240 by 35/100: 84.", "یہ 240 کو 35 سے تقسیم کرتا ہے۔ 240 کو 35/100 سے ضرب دیں: 84", "pc_times_whole")]),
   nq("q5_as_percent", ("In a test, Waqas answers 15 questions correctly out of 60. What percentage is correct?", "ایک ٹیسٹ میں وقاص 60 میں سے 15 سوال درست حل کرتا ہے۔ کتنے فیصد درست ہیں؟"), Q5,
      ("Write 15 over 60, then multiply by 100.", "60 پر 15 لکھیں، پھر 100 سے ضرب دیں۔"),
      ("Right! 15/60 × 100 = 25%.", "درست! 15/60 × 100 = 25%"),
      ("15/60 = 1/4, and 1/4 × 100 = 25%.", "15/60 = 1/4 اور 1/4 × 100 = 25%"),
      [(900, "That multiplies 15 by 60. Divide 15 by 60, then multiply by 100: 25.", "یہ 15 کو 60 سے ضرب دیتا ہے۔ 15 کو 60 سے تقسیم کریں، پھر 100 سے ضرب دیں: 25", "pc_times_whole")]),
   nq("q6_find_whole", ("12 is 20% of a number. What is the number?", "12 کسی عدد کا 20% ہے۔ وہ عدد کیا ہے؟"), Q6,
      ("20% means 20 out of 100. 12 ÷ 20 gives 1%.", "20% کا مطلب 100 میں سے 20۔ 12 ÷ 20 سے 1% ملتا ہے۔"),
      ("Right! 1% is 12 ÷ 20 = 0.6, and 100% is 60.", "درست! 1% یعنی 12 ÷ 20 = 0.6، اور 100% یعنی 60۔"),
      ("Total quantity = given quantity ÷ percentage × 100 = 12 ÷ 20 × 100 = 60.", "کل مقدار = دی گئی مقدار ÷ فیصد × 100 = 12 ÷ 20 × 100 = 60"),
      [(2.4, "That is 20% of 12. The number is 12 ÷ 20 × 100 = 60.", "یہ 12 کا 20% ہے۔ عدد 12 ÷ 20 × 100 = 60 ہے۔", "pc_whole_as_part")]),
   ch("q7_compare", ("Hamid scores 42 out of 60. Bina scores 36 out of 50. Who did better, by percentage?", "حامد 60 میں سے 42 نمبر لیتا ہے۔ بینا 50 میں سے 36 نمبر لیتی ہے۔ فیصد کے لحاظ سے کس کا نتیجہ بہتر ہے؟"),
      ("Bina: 72% against Hamid's 70%", "بینا: 72%، جبکہ حامد کے 70%", "Yes! 42/60 × 100 = 70 and 36/50 × 100 = 72.", "جی ہاں! 42/60 × 100 = 70 اور 36/50 × 100 = 72"),
      [("Hamid, because 42 is more than 36", "حامد، کیونکہ 42، 36 سے زیادہ ہے", "The totals are different (60 and 50), so compare the percentages, not the marks.", "کل نمبر مختلف ہیں (60 اور 50)، اس لیے نمبروں کی بجائے فیصد کا موازنہ کریں۔", "pc_compare_numbers"),
       ("They did equally well", "دونوں کا نتیجہ برابر ہے", "42/60 is 70% and 36/50 is 72%. They are not equal.", "42/60 یعنی 70% اور 36/50 یعنی 72%۔ یہ برابر نہیں۔")],
      1),
   nq("q8_salary", ("A salary of Rs 40,000 is increased by 15%. What is the new salary in rupees?", "40,000 روپے کی تنخواہ میں 15% اضافہ ہوتا ہے۔ نئی تنخواہ کتنے روپے ہے؟"), Q8,
      ("Find 15% of 40,000 first, then add it.", "پہلے 40,000 کا 15% نکالیں، پھر اسے جمع کریں۔"),
      ("Right! 15% of 40,000 is 6,000 and 40,000 + 6,000 = 46,000.", "درست! 40,000 کا 15% یعنی 6,000 اور 40,000 + 6,000 = 46,000"),
      ("The rise is 15/100 × 40,000 = 6,000. New salary: 40,000 + 6,000 = 46,000.", "اضافہ 15/100 × 40,000 = 6,000 ہے۔ نئی تنخواہ: 40,000 + 6,000 = 46,000"),
      [(6000, "That is only the rise. Add it to the old salary: 46,000.", "یہ صرف اضافہ ہے۔ اسے پرانی تنخواہ میں جمع کریں: 46,000", "pc_change_only"),
       (34000, "An increase is added, not subtracted: 46,000.", "اضافہ جمع کیا جاتا ہے، گھٹایا نہیں جاتا: 46,000", "pc_wrong_way")]),
   nq("q9_discount", ("A bag costs Rs 2,500. In a sale its price is reduced by 12%. What is the sale price in rupees?", "ایک بیگ کی قیمت 2,500 روپے ہے۔ سیل میں اس کی قیمت 12% کم ہو جاتی ہے۔ سیل کی قیمت کتنے روپے ہے؟"), Q9,
      ("Find 12% of 2,500, then take it away.", "2,500 کا 12% نکالیں، پھر اسے گھٹائیں۔"),
      ("Right! 12% of 2,500 is 300 and 2,500 − 300 = 2,200.", "درست! 2,500 کا 12% یعنی 300 اور 2,500 − 300 = 2,200"),
      ("The reduction is 12/100 × 2,500 = 300. Sale price: 2,500 − 300 = 2,200.", "کمی 12/100 × 2,500 = 300 ہے۔ سیل کی قیمت: 2,500 − 300 = 2,200"),
      [(300, "That is only the reduction. Take it away from 2,500: 2,200.", "یہ صرف کمی ہے۔ اسے 2,500 میں سے گھٹائیں: 2,200", "pc_change_only"),
       (2800, "A decrease is subtracted, not added: 2,200.", "کمی گھٹائی جاتی ہے، جمع نہیں کی جاتی: 2,200", "pc_wrong_way")]),
   nq("q10_pop", ("The population of a village grew from 8,000 to 9,200. What is the percentage increase?", "ایک گاؤں کی آبادی 8,000 سے بڑھ کر 9,200 ہو گئی۔ فیصد اضافہ کتنا ہے؟"), Q10,
      ("The increase is 9,200 − 8,000. Divide it by the original population, 8,000.", "اضافہ 9,200 − 8,000 ہے۔ اسے اصل آبادی 8,000 سے تقسیم کریں۔"),
      ("Right! 1,200/8,000 × 100 = 15%.", "درست! 1,200/8,000 × 100 = 15%"),
      ("Increase = 1,200. As a percentage of the original: 1,200 ÷ 8,000 × 100 = 15%.", "اضافہ = 1,200۔ اصل کے فیصد کے طور پر: 1,200 ÷ 8,000 × 100 = 15%"),
      [(13, "That divides by the new population, 9,200. Divide the increase by the original, 8,000: 15.", "یہ نئی آبادی 9,200 سے تقسیم کرتا ہے۔ اضافے کو اصل آبادی 8,000 سے تقسیم کریں: 15", "pc_wrong_base"),
       (1200, "That is the increase itself. Divide it by 8,000 and multiply by 100: 15.", "یہ خود اضافہ ہے۔ اسے 8,000 سے تقسیم کریں اور 100 سے ضرب دیں: 15", "pc_change_only")]),
   nq("q11_present", ("In a school of 250 students, 8% are absent on one day. How many students are present?", "250 طلبہ کے ایک اسکول میں ایک دن 8% غیر حاضر ہیں۔ کتنے طلبہ حاضر ہیں؟"), Q11,
      ("Find the number absent, then take it from 250.", "غیر حاضر طلبہ کی تعداد نکالیں، پھر اسے 250 میں سے گھٹائیں۔"),
      ("Right! 20 are absent and 250 − 20 = 230.", "درست! 20 غیر حاضر ہیں اور 250 − 20 = 230"),
      ("8% of 250 = 20 absent. Present: 250 − 20 = 230.", "250 کا 8% = 20 غیر حاضر۔ حاضر: 250 − 20 = 230"),
      [(20, "That is the number absent. The question asks how many are present: 230.", "یہ غیر حاضر طلبہ کی تعداد ہے۔ سوال حاضر طلبہ کا ہے: 230", "pc_of_whole")]),
   nq("q12_whole", ("18% of a number is 54. What is the number?", "کسی عدد کا 18% ہے 54۔ وہ عدد کیا ہے؟"), Q12,
      ("1% is 54 ÷ 18. Then find 100%.", "1% یعنی 54 ÷ 18۔ پھر 100% نکالیں۔"),
      ("Right! 1% is 3, so 100% is 300.", "درست! 1% یعنی 3، اس لیے 100% یعنی 300"),
      ("54 ÷ 18 = 3 for 1%, and 3 × 100 = 300.", "54 ÷ 18 = 3 یعنی 1%، اور 3 × 100 = 300"),
      [(9.72, "That finds 18% of 54. 54 is already the 18%, so the number is 300.", "یہ 54 کا 18% نکالتا ہے۔ 54 پہلے سے 18% ہے، اس لیے عدد 300 ہے۔", "pc_whole_as_part"),
       (3, "That is 1%. Multiply by 100 to get the whole: 300.", "یہ 1% ہے۔ پورا حاصل کرنے کے لیے 100 سے ضرب دیں: 300", "stops_early")]),
   ch("q13_find_error", ("A price goes up from Rs 80 to Rs 100. Kamran says the increase is 20% because 20 ÷ 100 × 100 = 20. What went wrong?", "ایک قیمت 80 روپے سے بڑھ کر 100 روپے ہو جاتی ہے۔ کامران کہتا ہے اضافہ 20% ہے کیونکہ 20 ÷ 100 × 100 = 20۔ کیا غلطی ہوئی؟"),
      ("He divided by the new price. The change must be divided by the original price: 20 ÷ 80 × 100 = 25%.", "اس نے نئی قیمت سے تقسیم کیا۔ تبدیلی کو اصل قیمت سے تقسیم کرنا چاہیے: 20 ÷ 80 × 100 = 25%", "Yes! The rise of Rs 20 is 25% of the original Rs 80.", "جی ہاں! 20 روپے کا اضافہ اصل 80 روپے کا 25% ہے۔"),
      [("Nothing. 20% is the right answer.", "کوئی غلطی نہیں۔ 20% درست جواب ہے۔", "20% of 80 is only 16, not 20. The rise is 25%.", "80 کا 20% صرف 16 ہے، 20 نہیں۔ اضافہ 25% ہے۔", "pc_wrong_base"),
       ("The rise is Rs 20, not a percentage.", "اضافہ 20 روپے ہے، فیصد نہیں۔", "The question asks for the percentage increase, so compare Rs 20 with the original Rs 80: 25%.", "سوال فیصد اضافہ پوچھتا ہے، اس لیے 20 روپے کا اصل 80 روپے سے موازنہ کریں: 25%", "pc_change_only")],
      0, qtype="find_error"),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You worked with percentages.", "شاباش! آپ نے فیصد پر کام کیا۔"),
    "text": T("A percentage is a fraction out of 100. To find a percentage of a quantity, multiply. To write one quantity as a percentage of another, divide and multiply by 100. To find the whole, divide the given quantity by the percentage and multiply by 100. To increase or decrease by a percentage, find the percentage of the original and add or subtract it. A percentage change always uses the original value.",
              "فیصد 100 میں سے کسر ہے۔ کسی مقدار کا فیصد نکالنے کے لیے ضرب دیں۔ ایک مقدار کو دوسری کے فیصد کے طور پر لکھنے کے لیے تقسیم کریں اور 100 سے ضرب دیں۔ کل معلوم کرنے کے لیے دی گئی مقدار کو فیصد سے تقسیم کریں اور 100 سے ضرب دیں۔ فیصد اضافے یا کمی کے لیے اصل کا فیصد نکال کر جمع یا تفریق کریں۔ فیصد تبدیلی میں ہمیشہ اصل قیمت استعمال ہوتی ہے۔"),
    "points": [T("To compare, change both to percentages.", "موازنے کے لیے دونوں کو فیصد میں بدلیں۔"),
               T("Read the question: do you want the change or the new value?", "سوال پڑھیں: آپ کو تبدیلی چاہیے یا نئی قیمت؟")]},
 ],
 bank=[
   {"id": "qb_to_percent", "type": "recall", "step": nq("qb_to_percent", ("Write 9/20 as a percentage.", "9/20 کو فیصد کی صورت میں لکھیں۔"), QB_REC,
      ("20 × 5 = 100. Multiply the top by 5 too.", "20 × 5 = 100۔ اوپر والے عدد کو بھی 5 سے ضرب دیں۔"),
      ("Right! 9/20 = 45/100 = 45%.", "درست! 9/20 = 45/100 = 45%"), ("9 × 5 = 45 and 20 × 5 = 100, so 45%.", "9 × 5 = 45 اور 20 × 5 = 100، اس لیے 45%"),
      [(9, "9 out of 20 is not 9 out of 100. Multiply top and bottom by 5: 45%.", "20 میں سے 9، 100 میں سے 9 نہیں ہوتا۔ اوپر اور نیچے کو 5 سے ضرب دیں: 45%", "pc_not_over_100")], qtype=None)},
   {"id": "qb_percent_of", "type": "apply", "step": nq("qb_percent_of", ("Find 15% of 360.", "360 کا 15% معلوم کریں۔"), QB_APP,
      ("10% of 360 is 36. Half of that is 5%.", "360 کا 10% یعنی 36۔ اس کا آدھا 5% ہے۔"),
      ("Right! 36 + 18 = 54.", "درست! 36 + 18 = 54"), ("15/100 × 360 = 54.", "15/100 × 360 = 54"),
      [(306, "That is 360 − 54, the rest. 15% of 360 is 54.", "یہ 360 − 54 ہے، یعنی باقی۔ 360 کا 15% ہے 54", "pc_of_whole")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Mehwish says 30% of 50 is 30 × 50 = 1,500. What went wrong?", "مہوش کہتی ہے 50 کا 30% ہے 30 × 50 = 1,500۔ کیا غلطی ہوئی؟"),
      ("She forgot to divide by 100. 30/100 × 50 = 15.", "وہ 100 سے تقسیم کرنا بھول گئی۔ 30/100 × 50 = 15", "Yes! A percentage is out of 100.", "جی ہاں! فیصد سو میں سے ہوتا ہے۔"),
      [("Nothing. 1,500 is right.", "کوئی غلطی نہیں۔ 1,500 درست ہے۔", "30% of 50 cannot be more than 50.", "50 کا 30% اس سے زیادہ نہیں ہو سکتا۔", "pc_times_whole"),
       ("She should have added 30 and 50.", "اسے 30 اور 50 جمع کرنا چاہیے تھا۔", "Adding does not give a percentage of an amount. Multiply by 30/100: 15.", "جمع سے کسی رقم کا فیصد نہیں ملتا۔ 30/100 سے ضرب دیں: 15", "pc_of_whole")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_percent", "type": "recall", "step": nq("r_percent", ("Write 3/5 as a percentage.", "3/5 کو فیصد کی صورت میں لکھیں۔"), R_REC,
      ("5 × 20 = 100.", "5 × 20 = 100"),
      ("Right! 3/5 = 60/100 = 60%.", "درست! 3/5 = 60/100 = 60%"), ("3 × 20 = 60 and 5 × 20 = 100, so 60%.", "3 × 20 = 60 اور 5 × 20 = 100، اس لیے 60%"),
      [(3, "3 out of 5 is not 3 out of 100. Multiply top and bottom by 20: 60%.", "5 میں سے 3، 100 میں سے 3 نہیں ہوتا۔ اوپر اور نیچے کو 20 سے ضرب دیں: 60%", "pc_not_over_100")], qtype=None)},
   {"id": "r_increase", "type": "apply", "step": nq("r_increase", ("A bill of Rs 600 goes up by 10%. What is the new bill in rupees?", "600 روپے کا بل 10% بڑھ جاتا ہے۔ نیا بل کتنے روپے ہے؟"), R_APP,
      ("10% of 600 is 60. Add it.", "600 کا 10% یعنی 60۔ اسے جمع کریں۔"),
      ("Right! 600 + 60 = 660.", "درست! 600 + 60 = 660"), ("The rise is 60, so the new bill is 660.", "اضافہ 60 ہے، اس لیے نیا بل 660 ہے۔"),
      [(60, "That is only the rise. Add it to 600: 660.", "یہ صرف اضافہ ہے۔ اسے 600 میں جمع کریں: 660", "pc_change_only")], qtype=None)},
 ],
 glossary=[T("Per cent", "فی صد"), T("Percentage", "فیصد"), T("Percentage increase", "فیصد اضافہ"), T("Percentage decrease", "فیصد کمی"), T("Original value", "اصل قیمت")],
 flashcards=[
   {"id": "f_whole", "front": T("How do you find the whole when a part is given as a percentage?", "جب جزو فیصد میں دیا ہو تو کل کیسے معلوم کرتے ہیں؟"),
    "back": T("Divide the part by the percentage, then multiply by 100: if 12 is 20%, the whole is 60.", "جزو کو فیصد سے تقسیم کریں، پھر 100 سے ضرب دیں: اگر 12، 20% ہے تو کل 60 ہے۔")},
   {"id": "f_change", "front": T("How do you find a percentage increase?", "فیصد اضافہ کیسے معلوم کرتے ہیں؟"),
    "back": T("Increase ÷ original × 100. Always divide by the original value.", "اضافہ ÷ اصل × 100۔ ہمیشہ اصل قیمت سے تقسیم کریں۔")},
 ],
 home_task={"id": "h_sale", "text": T(
   "Find a sale notice or advertisement that shows a percentage off (or ask a shopkeeper). Write the old price and the discount, then work out the amount of the discount and the new price in your notebook.",
   "کوئی سیل کا اشتہار تلاش کریں جس میں فیصد رعایت ہو (یا دکاندار سے پوچھیں)۔ پرانی قیمت اور رعایت لکھیں، پھر رعایت کی رقم اور نئی قیمت اپنی کاپی میں نکالیں۔")},
 notes=["Covers percentage from a 100-grid (q1), percentage to fraction and back (q2, q3), a percentage of a quantity (q4, q11), one quantity as a percentage of another (q5), finding the whole (q6, q12), comparing by percentage (q7), percentage increase and decrease (q8, q9, q10) and a find-the-error question (q13).",
        "Each wrong answer is a real mistake: a percent over 10, a fraction left unsimplified, the rest instead of the part, forgetting to divide by 100, dividing by the new value, and giving the change instead of the new price.",
        "Urdu terms to check: فی صد / فیصد (per cent / percentage), فیصد اضافہ / فیصد کمی (percentage increase / decrease), اصل قیمت (original value)."],
 minutes=20,
)

write(lesson)

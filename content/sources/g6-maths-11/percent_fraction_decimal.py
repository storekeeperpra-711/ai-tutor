from fractions import Fraction as F

from common import (D, T, opt, say, wrong, number_question, write,
                    REF, REVIEW, DEC_PLACE_VALUE, PC_MEANING, PC_CONVERT, as_percent)

SKILL = PC_CONVERT


def to_decimal(p):
    return D(p) / 100


# s2: hundredths in 0.35
S2 = 35
assert D("0.35") * 100 == S2
# s4: 0.6 -> 60%
S4 = D("0.6") * 100
assert S4 == 60
# s5: 25% -> 0.25
S5 = to_decimal(25)
assert S5 == D("0.25")
# s6: 3/4 -> 75%
S6 = as_percent(3, 4)
assert S6 == 75
# s7: 40% = 2/5 in simplest form
assert F(40, 100) == F(2, 5)
# s8: 7% -> 0.07
S8 = to_decimal(7)
assert S8 == D("0.07")
# s9: 0.5 = 50%, not 5%
assert D("0.5") * 100 == 50
# s11: 9/25 -> 36%
S11 = as_percent(9, 25)
assert S11 == 36
# question bank and review
QB = D("0.45") * 100
assert QB == 45
R1 = to_decimal(80)
assert R1 == D("0.8")
R2 = as_percent(2, 5)
assert R2 == 40

lesson = {
 "id": "g6-maths-11-percents-fractions-decimals",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Change between percents, fractions and decimals.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Percents, fractions and decimals", "فیصد، کسریں اور اعشاریہ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": PC_MEANING}, {"skill": DEC_PLACE_VALUE}],
 "misconceptions": [
   {"id": "one_place", "description": "Moves the decimal point one place instead of two (0.6 = 6%, 7% = 0.7)."},
   {"id": "percent_is_decimal", "description": "Writes the percent number as the decimal without dividing by 100 (25% = 25)."},
   {"id": "not_simplest", "description": "Leaves the fraction over 100 or simplifies it wrongly."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("How do you change a decimal into a percent?", "اعشاریہ کو فیصد میں کیسے بدلتے ہیں؟"),
     "options": [
       opt("times100", "Multiply by 100", "100 سے ضرب دیں", True,
           "Yes! 0.3 × 100 = 30, so 0.3 = 30%.", "جی ہاں! 0.3 × 100 = 30، تو 0.3 = 30%"),
       opt("times10", "Multiply by 10", "10 سے ضرب دیں", False,
           "Percent is out of 100, so multiply by 100.", "فیصد 100 میں سے ہے، تو 100 سے ضرب دیں۔", "one_place"),
       opt("div100", "Divide by 100", "100 سے تقسیم کریں", False,
           "That goes the other way, from a percent to a decimal.", "یہ الٹا ہے، فیصد سے اعشاریہ۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Write 0.45 as a percent. Type just the number.", "0.45 کو فیصد میں لکھیں۔ صرف عدد لکھیں۔"),
     QB,
     T("Multiply by 100.", "100 سے ضرب دیں۔"),
     T("Right! 0.45 = 45%.", "درست! 0.45 = 45%"),
     T("0.45 × 100 = 45, so 45%.", "0.45 × 100 = 45، یعنی 45%"),
     common_wrong=[wrong(D("4.5"), "Multiply by 100, not 10: 45%.", "10 نہیں، 100 سے ضرب دیں: 45%", "one_place")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Bilal writes 3% as 0.3. What went wrong?", "بلال 3% کو 0.3 لکھتا ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("two", "Divide by 100: 3% = 0.03.", "100 سے تقسیم کریں: 3% = 0.03", True,
           "Yes! 0.3 would be 30%.", "جی ہاں! 0.3 تو 30% ہوتا۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "0.3 is 3 tenths, which is 30%. 3% is 3 hundredths: 0.03.", "0.3 یعنی 3 دسویں، جو 30% ہے۔ 3% یعنی 3 سوویں: 0.03", "one_place"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_to_dec", "front": T("Percent → decimal?", "فیصد ← اعشاریہ؟"),
    "back": T("Divide by 100. 25% = 0.25, 7% = 0.07.", "100 سے تقسیم۔ 25% = 0.25، 7% = 0.07")},
   {"id": "f_to_pc", "front": T("Decimal or fraction → percent?", "اعشاریہ یا کسر ← فیصد؟"),
    "back": T("Multiply by 100. 0.6 = 60%, 3/4 = 75%.", "100 سے ضرب۔ 0.6 = 60%، 3/4 = 75%")},
 ],
 "home_tasks": [{"id": "h_match", "text": T(
   "Make six small cards: 50%, 1/2, 25%, 1/4, 10% and 0.1. Mix them up and ask someone at home to find the pairs that mean the same amount.",
   "چھ چھوٹے کارڈ بنائیں: 50%، 1/2، 25%، 1/4، 10% اور 0.1۔ انہیں ملا دیں اور گھر کے کسی فرد سے کہیں کہ برابر مقدار والے جوڑے ڈھونڈے۔")}],
 "glossary": [T("Percent", "فیصد"), T("Decimal", "اعشاریہ"), T("Hundredths", "سوویں حصے"), T("Simplest form", "سادہ ترین شکل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Half a roti, 0.5 of a roti, 50% of a roti. Are these three different amounts, or the same?",
                     "آدھی روٹی، 0.5 روٹی، 50% روٹی۔ کیا یہ تین مختلف مقداریں ہیں یا ایک جیسی؟"),
    "text": T("Today we change between percents, fractions and decimals. First, a quick check on decimals.", "آج ہم فیصد، کسروں اور اعشاریہ کو ایک دوسرے میں بدلیں گے۔ پہلے اعشاریہ کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many hundredths are in 0.35?", "0.35 میں کتنے سوویں حصے ہیں؟"),
     S2,
     T("0.35 = 3 tenths and 5 hundredths. One tenth is 10 hundredths.", "0.35 = 3 دسویں اور 5 سوویں۔ ایک دسواں 10 سوویں کے برابر ہے۔"),
     T("Right! 0.35 = 35/100.", "درست! 0.35 = 35/100"),
     T("3 tenths = 30 hundredths, plus 5 more: 35.", "3 دسویں = 30 سوویں، اور 5 مزید: 35"),
     common_wrong=[wrong(5, "5 is only the hundredths digit. 3 tenths are 30 hundredths more: 35.", "5 صرف سوویں کا ہندسہ ہے۔ 3 دسویں مزید 30 سوویں ہیں: 35")],
     qtype="recall", skill=DEC_PLACE_VALUE),
   {"id": "s3_convert", "type": "explain",
    "character": say("happy", "They're all the same amount, just written three ways!", "یہ سب ایک ہی مقدار ہیں، بس تین طریقوں سے لکھی گئی!"),
    "text": T("A percent is hundredths. Percent to decimal: divide by 100, so the point moves two places left (25% = 0.25, 7% = 0.07). Decimal to percent: multiply by 100 (0.6 = 60%). Percent to fraction: write it over 100 and simplify (40% = 40/100 = 2/5). Fraction to percent: make the bottom 100 (3/4 = 75/100 = 75%).",
              "فیصد سوویں حصے ہیں۔ فیصد سے اعشاریہ: 100 سے تقسیم کریں، یعنی اعشاریہ دو جگہ بائیں (25% = 0.25، 7% = 0.07)۔ اعشاریہ سے فیصد: 100 سے ضرب دیں (0.6 = 60%)۔ فیصد سے کسر: 100 کے اوپر لکھیں اور سادہ کریں (40% = 40/100 = 2/5)۔ کسر سے فیصد: نیچے والا 100 بنائیں (3/4 = 75/100 = 75%)۔")},
   number_question(
     "s4_dec_to_pc",
     T("Write 0.6 as a percent. Type just the number.", "0.6 کو فیصد میں لکھیں۔ صرف عدد لکھیں۔"),
     S4,
     T("Multiply by 100.", "100 سے ضرب دیں۔"),
     T("Right! 0.6 = 60%.", "درست! 0.6 = 60%"),
     T("0.6 × 100 = 60, so 60%.", "0.6 × 100 = 60، یعنی 60%"),
     common_wrong=[wrong(6, "0.6 is 6 tenths, which is 60 hundredths: 60%.", "0.6 یعنی 6 دسویں، جو 60 سوویں ہیں: 60%", "one_place")]),
   number_question(
     "s5_pc_to_dec",
     T("Write 25% as a decimal.", "25% کو اعشاریہ میں لکھیں۔"),
     S5,
     T("Divide by 100: move the point two places left.", "100 سے تقسیم کریں: اعشاریہ دو جگہ بائیں۔"),
     T("Right! 25% = 0.25.", "درست! 25% = 0.25"),
     T("25 ÷ 100 = 0.25.", "25 ÷ 100 = 0.25"),
     common_wrong=[wrong(25, "Divide by 100 to get the decimal: 0.25.", "اعشاریہ کے لیے 100 سے تقسیم کریں: 0.25", "percent_is_decimal"),
                   wrong(D("2.5"), "That divides by 10. Divide by 100: 0.25.", "یہ 10 سے تقسیم ہے۔ 100 سے تقسیم کریں: 0.25", "one_place")]),
   number_question(
     "s6_frac_to_pc",
     T("Write 3/4 as a percent. Type just the number.", "3/4 کو فیصد میں لکھیں۔ صرف عدد لکھیں۔"),
     S6,
     T("3/4 = ?/100. Multiply top and bottom by 25.", "3/4 = ?/100۔ اوپر اور نیچے کو 25 سے ضرب دیں۔"),
     T("Right! 3/4 = 75%.", "درست! 3/4 = 75%"),
     T("3/4 = 75/100 = 75%.", "3/4 = 75/100 = 75%"),
     common_wrong=[wrong(34, "3/4 is not 34%. Make the bottom 100: 75/100 = 75%.", "3/4، 34% نہیں ہے۔ نیچے والا 100 بنائیں: 75/100 = 75%"),
                   wrong(25, "25% is 1/4. Three quarters is 3 × 25 = 75%.", "25% یعنی 1/4۔ تین چوتھائی 3 × 25 = 75% ہے۔")]),
   {"id": "s7_pc_to_frac", "type": "choice",
    "prompt": T("Write 40% as a fraction in its simplest form.", "40% کو سادہ ترین کسر میں لکھیں۔"),
    "options": [
      opt("two_fifths", "2/5", "2/5", True, "Yes! 40/100 = 4/10 = 2/5.", "جی ہاں! 40/100 = 4/10 = 2/5"),
      opt("forty", "40/100", "40/100", False, "That's right, but not the simplest form. Divide top and bottom by 20: 2/5.", "یہ درست ہے، لیکن سادہ ترین نہیں۔ اوپر اور نیچے کو 20 سے تقسیم کریں: 2/5", "not_simplest"),
      opt("four", "4/5", "4/5", False, "4/5 = 80/100. 40/100 simplifies to 2/5.", "4/5 = 80/100۔ 40/100 سادہ ہو کر 2/5 بنتا ہے۔", "not_simplest"),
    ]},
   number_question(
     "s8_small",
     T("Write 7% as a decimal.", "7% کو اعشاریہ میں لکھیں۔"),
     S8,
     T("7% is 7 hundredths.", "7% یعنی 7 سوویں۔"),
     T("Right! 7% = 0.07.", "درست! 7% = 0.07"),
     T("7 ÷ 100 = 0.07.", "7 ÷ 100 = 0.07"),
     common_wrong=[wrong(D("0.7"), "0.7 is 70%. 7% is 7 hundredths: 0.07.", "0.7 یعنی 70%۔ 7% یعنی 7 سوویں: 0.07", "one_place"),
                   wrong(7, "Divide by 100 to get the decimal: 0.07.", "اعشاریہ کے لیے 100 سے تقسیم کریں: 0.07", "percent_is_decimal")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Sara writes 0.5 = 5%. What went wrong?", "سارہ لکھتی ہے 0.5 = 5%۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("hundred", "Multiply by 100: 0.5 = 50%.", "100 سے ضرب دیں: 0.5 = 50%", True,
          "Yes! 0.5 is a half, and a half is 50%.", "جی ہاں! 0.5 آدھا ہے، اور آدھا 50% ہے۔"),
      opt("half_pc", "0.5 is 0.5%.", "0.5 یعنی 0.5%۔", False,
          "0.5 is a half, which is 50%.", "0.5 آدھا ہے، جو 50% ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "5% is only 5 out of 100. 0.5 is a half: 50%.", "5% صرف 100 میں سے 5 ہے۔ 0.5 آدھا ہے: 50%", "one_place"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why does the point move two places when we turn a percent into a decimal? Can you teach me?",
                     "فیصد کو اعشاریہ بناتے ہوئے اعشاریہ دو جگہ کیوں ہلتا ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why does 25% become 0.25?", "اپنے الفاظ میں بتائیں: 25%، 0.25 کیوں بن جاتا ہے؟"),
    "key_idea": "A percent is a number of hundredths. 25% is 25 hundredths, and the second place after the decimal point is the hundredths place, so 25 hundredths is 0.25. Dividing by 100 moves every digit two places.",
    "levels": {
      "got_it": "Says a percent means hundredths (out of 100), so dividing by 100 gives the decimal.",
      "partly": "Says divide by 100, without saying why.",
      "not_yet": "Gives no reason, or just repeats the rule."},
    "keywords": [
      ["hundredth", "100", "hundred", "سوویں", "سو"],
      ["divide", "تقسیم"],
      ["out of", "میں سے"]],
    "fallback_feedback": {
      "got_it": T("Well explained! A percent is hundredths, and that is two places after the point.", "بہت خوب! فیصد سوویں حصے ہیں، جو اعشاریہ کے بعد دوسری جگہ ہے۔"),
      "partly": T("Good start! Now say why dividing by 100 is the right thing to do.", "اچھی شروعات! اب بتائیں 100 سے تقسیم کرنا کیوں درست ہے۔"),
      "not_yet": T("Remember: 25% means 25 out of 100. How do you write 25 hundredths as a decimal?", "یاد کریں: 25% یعنی 100 میں سے 25۔ 25 سوویں کو اعشاریہ میں کیسے لکھتے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_twentyfifths",
     T("In a class, 9/25 of the children wear glasses. What percent is that? Type just the number.", "ایک کلاس میں 9/25 بچے عینک لگاتے ہیں۔ یہ کتنے فیصد ہے؟ صرف عدد لکھیں۔"),
     S11,
     T("25 × 4 = 100, so multiply the top by 4 too.", "25 × 4 = 100، تو اوپر والے کو بھی 4 سے ضرب دیں۔"),
     T("Right! 9/25 = 36/100 = 36%.", "درست! 9/25 = 36/100 = 36%"),
     T("9/25 = 36/100, so 36%.", "9/25 = 36/100، یعنی 36%"),
     common_wrong=[wrong(9, "Make the bottom 100 first: 9/25 = 36/100 = 36%.", "پہلے نیچے والا 100 بنائیں: 9/25 = 36/100 = 36%")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Half, 0.5 and 50%: you can switch between them now!", "آدھا، 0.5 اور 50%: اب آپ انہیں بدل سکتے ہیں!"),
    "text": T("Percents are hundredths. Percent to decimal: divide by 100. Decimal to percent: multiply by 100. Percent to fraction: put it over 100 and simplify. Fraction to percent: make the bottom 100. Good ones to know: 50% = 1/2 = 0.5, 25% = 1/4 = 0.25, 10% = 1/10 = 0.1.",
              "فیصد سوویں حصے ہیں۔ فیصد سے اعشاریہ: 100 سے تقسیم۔ اعشاریہ سے فیصد: 100 سے ضرب۔ فیصد سے کسر: 100 کے اوپر لکھ کر سادہ کریں۔ کسر سے فیصد: نیچے والا 100 بنائیں۔ یاد رکھنے والے: 50% = 1/2 = 0.5، 25% = 1/4 = 0.25، 10% = 1/10 = 0.1"),
    "points": [T("Percent ÷ 100 = decimal.", "فیصد ÷ 100 = اعشاریہ۔"),
               T("Decimal × 100 = percent.", "اعشاریہ × 100 = فیصد۔")]},
 ],
 "review_questions": [
   {"id": "r_dec", "type": "apply", "skill": SKILL, "step": number_question(
     "r_dec",
     T("Write 80% as a decimal.", "80% کو اعشاریہ میں لکھیں۔"),
     R1,
     T("Divide by 100.", "100 سے تقسیم کریں۔"),
     T("Right! 0.8.", "درست! 0.8"),
     T("80 ÷ 100 = 0.8.", "80 ÷ 100 = 0.8"),
     common_wrong=[wrong(8, "Divide by 100, not 10: 0.8.", "10 نہیں، 100 سے تقسیم کریں: 0.8", "one_place")],
     qtype=None)},
   {"id": "r_frac", "type": "apply", "skill": SKILL, "step": number_question(
     "r_frac",
     T("Write 2/5 as a percent. Type just the number.", "2/5 کو فیصد میں لکھیں۔ صرف عدد لکھیں۔"),
     R2,
     T("2/5 = ?/100", "2/5 = ?/100"),
     T("Right! 40%.", "درست! 40%"),
     T("2/5 = 40/100 = 40%.", "2/5 = 40/100 = 40%"),
     common_wrong=[wrong(25, "2/5 is not 25%. Make the bottom 100: 40/100 = 40%.", "2/5، 25% نہیں ہے۔ نیچے والا 100 بنائیں: 40/100 = 40%")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Percentages unit. No textbook text or exercises were used.",
   "Percents are presented as hundredths, linking straight back to decimal place value.",
   "Urdu terms to check: فیصد (percent), اعشاریہ (decimal), سوویں حصے (hundredths).",
   "The numbers were worked out in content/sources/g6-maths-11/percent_fraction_decimal.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

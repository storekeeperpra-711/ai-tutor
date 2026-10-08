from common import (T, opt, say, wrong, signed, number_question, write,
                    BOOK_LAWS, REVIEW, INT_MULTIPLY, INT_LAWS)
from figs import jumps_figure, chains_figure, area_model, attach

SKILL = INT_LAWS
S = signed


def b(n):
    """A negative number in brackets: (−3); a positive one as it is."""
    return f"({S(n)})" if n < 0 else str(n)


# s1, s3: commutative law
assert -4 + 9 == 9 + -4 == 5
assert -3 * 5 == 5 * -3 == -15
# not commutative: − and ÷
assert 7 - 3 != 3 - 7 and 8 / 2 != 2 / 8
# s2: foundation
assert -3 * 5 == -15
# s3, s5: associative law
assert (-6 + 4) + 10 == -6 + (4 + 10) == 8
assert ((-2) * 3) * 5 == (-2) * (3 * 5) == -30
# s3, s6: distributive law
assert -2 * (6 + 4) == (-2 * 6) + (-2 * 4) == -20
S6_FIRST_ONLY = -2 * 6 + 4
assert S6_FIRST_ONLY == -8 and S6_FIRST_ONLY != -20
# s7: mental sum (−4) × 23 = (−4) × 20 + (−4) × 3
assert -4 * 23 == -4 * 20 + -4 * 3 == -92
S7_FIRST_ONLY = -4 * 20 + 3
assert S7_FIRST_ONLY == -77
# s8: division by zero is not defined; 0 ÷ non-zero = 0
assert 0 // -9 == 0
# s9: Hamza's mistake
assert -3 * (4 + 5) == -27 and -3 * 4 + 5 == -7
# s11: which law
assert (-2 + 7) + 3 == -2 + (7 + 3) == 8
# question bank
assert -5 * (10 + 2) == -5 * 10 + -5 * 2 == -60
QB_FIRST_ONLY = -5 * 10 + 2
assert QB_FIRST_ONLY == -48
# review
assert 0 // -8 == 0
assert (-3) * ((-2) * 5) == ((-3) * (-2)) * 5 == 30


# ---------- pictures ----------

def tm(x, y):
    """A short product label for inside a picture: −2×6."""
    return f"{S(x)}×{S(y)}"


FIG_S1 = chains_figure(
    -5, 9, [[-4, 9], [9, -4]],
    "Two number lines from −5 to 9. Top: −4 + 9, a jump marked +9 from −4 right to 5. Bottom: 9 + (−4), a jump marked −4 from 9 left to 5. Both land on 5.",
    "−5 سے 9 تک دو عددی خط۔ اوپر: −4 + 9، +9 والی چھلانگ −4 سے دائیں 5 تک۔ نیچے: 9 + (−4)، −4 والی چھلانگ 9 سے بائیں 5 تک۔ دونوں 5 پر اترتی ہیں۔",
    every=5)

FIG_S3 = area_model(
    [6, 4], -2, [S(-2 * 6), S(-2 * 4)],
    "A multiplication grid for (−2) × (6 + 4): a rectangle with −2 on its side, split into two parts with 6 and 4 on top. The parts hold −12 and −8, and −12 + (−8) = −20.",
    "(−2) × (6 + 4) کے لیے ضرب کا خانہ: ایک مستطیل جس کی سائیڈ پر −2 ہے، دو حصوں میں بٹا ہوا، اوپر 6 اور 4۔ حصوں میں −12 اور −8 ہیں، اور −12 + (−8) = −20")

FIG_S5 = jumps_figure(
    -7, 9, [-6, 4 + 10], end_text="?",
    alt_en="A number line from −7 to 9. 4 + 10 is grouped first to make 14: one jump marked +14 starts at −6 and goes right to a question mark.",
    alt_ur="−7 سے 9 تک عددی خط۔ پہلے 4 + 10 کو ملا کر 14 بنایا: +14 والی ایک چھلانگ −6 سے شروع ہو کر دائیں ایک سوالیہ نشان تک جاتی ہے۔")

FIG_S6 = area_model(
    [6, 4], -2, [tm(-2, 6), tm(-2, 4)],
    "A multiplication grid for (−2) × (6 + 4): a rectangle with −2 on its side, split into two parts with 6 and 4 on top. One part says −2 × 6 and the other says −2 × 4.",
    "(−2) × (6 + 4) کے لیے ضرب کا خانہ: ایک مستطیل جس کی سائیڈ پر −2 ہے، دو حصوں میں بٹا ہوا، اوپر 6 اور 4۔ ایک حصے میں −2 × 6 اور دوسرے میں −2 × 4 لکھا ہے۔")

FIG_S7 = area_model(
    [20, 3], -4, [tm(-4, 20), tm(-4, 3)],
    "A multiplication grid for (−4) × 23: a rectangle with −4 on its side, split into a wide part with 20 on top and a thin part with 3 on top. The parts say −4 × 20 and −4 × 3.",
    "(−4) × 23 کے لیے ضرب کا خانہ: ایک مستطیل جس کی سائیڈ پر −4 ہے، ایک چوڑے حصے (اوپر 20) اور ایک پتلے حصے (اوپر 3) میں بٹا ہوا۔ حصوں میں −4 × 20 اور −4 × 3 لکھا ہے۔")

FIG_S9 = area_model(
    [4, 5], -3, [S(-3 * 4), "?"],
    "A multiplication grid for (−3) × (4 + 5): a rectangle with −3 on its side, split into two parts with 4 and 5 on top. The first part holds −12; the second part, for the 5, has a question mark: it must be multiplied by −3 too.",
    "(−3) × (4 + 5) کے لیے ضرب کا خانہ: ایک مستطیل جس کی سائیڈ پر −3 ہے، دو حصوں میں بٹا ہوا، اوپر 4 اور 5۔ پہلے حصے میں −12 ہے؛ دوسرے حصے میں، 5 کے لیے، سوالیہ نشان ہے: اسے بھی −3 سے ضرب دینا ہے۔")

FIG_S12 = chains_figure(
    -8, 10, [[-6, 4, 10], [-6, 4 + 10]],
    "Two number lines from −8 to 10, with a mark every 2. Top: (−6 + 4) + 10, a jump marked +4 from −6 to −2, then a jump marked +10 to 8. Bottom: −6 + (4 + 10), one jump marked +14 from −6 to 8. Both land on 8.",
    "−8 سے 10 تک دو عددی خط، ہر 2 پر ایک نشان۔ اوپر: (−6 + 4) + 10، +4 والی چھلانگ −6 سے −2 تک، پھر +10 والی چھلانگ 8 تک۔ نیچے: −6 + (4 + 10)، +14 والی ایک چھلانگ −6 سے 8 تک۔ دونوں 8 پر اترتی ہیں۔",
    every=5, ticks_every=2)

FIG_QB_APPLY = area_model(
    [10, 2], -5, [tm(-5, 10), tm(-5, 2)],
    "A multiplication grid for (−5) × (10 + 2): a rectangle with −5 on its side, split into a wide part with 10 on top and a thin part with 2 on top. The parts say −5 × 10 and −5 × 2.",
    "(−5) × (10 + 2) کے لیے ضرب کا خانہ: ایک مستطیل جس کی سائیڈ پر −5 ہے، ایک چوڑے حصے (اوپر 10) اور ایک پتلے حصے (اوپر 2) میں بٹا ہوا۔ حصوں میں −5 × 10 اور −5 × 2 لکھا ہے۔")

lesson = {
 "id": "g6-maths-04-laws-of-integers",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Use the commutative, associative and distributive laws with integers, and know that division by zero is not defined.", "textbook": BOOK_LAWS}],
 "skills": [SKILL],
 "title": T("Laws of integers", "صحیح اعداد کے قوانین"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": INT_MULTIPLY}],
 "misconceptions": [
   {"id": "subtraction_commutative", "description": "Thinks the order does not matter in subtraction (or division): 7 − 3 = 3 − 7."},
   {"id": "distributes_first_only", "description": "Multiplies only the first number in the bracket: −3 × (4 + 5) = −12 + 5."},
   {"id": "divide_by_zero_is_zero", "description": "Thinks any number divided by 0 is 0: (−7) ÷ 0 = 0."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_which_law", "type": "recall", "step": {
     "id": "qb_which_law", "type": "choice",
     "prompt": T(f"Which law says {b(-6)} × 2 = 2 × {b(-6)}?", f"کون سا قانون کہتا ہے کہ {b(-6)} × 2 = 2 × {b(-6)}؟"),
     "options": [
       opt("commutative", "Commutative law", "خاصیت مبادلہ", True,
           "Yes! Swapping the order does not change the answer.", "جی ہاں! ترتیب بدلنے سے جواب نہیں بدلتا۔"),
       opt("associative", "Associative law", "خاصیت تلازم", False,
           "The associative law is about grouping with brackets. Here the order is swapped: commutative.", "خاصیت تلازم قوسین سے گروہ بنانے کے بارے میں ہے۔ یہاں ترتیب بدلی ہے: خاصیت مبادلہ۔"),
       opt("distributive", "Distributive law", "خاصیت تقسیم", False,
           "The distributive law has a bracket with + inside. Here the order is swapped: commutative.", "خاصیت تقسیم میں قوسین کے اندر + ہوتا ہے۔ یہاں ترتیب بدلی ہے: خاصیت مبادلہ۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T(f"Work out {b(-5)} × (10 + 2) by multiplying each number in the bracket.", f"قوسین کے ہر عدد کو ضرب دے کر حل کریں: {b(-5)} × (10 + 2)"),
     -60,
     T("(−5) × 10 = −50 and (−5) × 2 = −10. Add them.", "(−5) × 10 = −50 اور (−5) × 2 = −10۔ انہیں جمع کریں۔"),
     T("Right! (−5) × (10 + 2) = −50 + (−10) = −60.", "درست! (−5) × (10 + 2) = −50 + (−10) = −60"),
     T("(−5) × 10 = −50 and (−5) × 2 = −10, so the answer is −60.", "(−5) × 10 = −50 اور (−5) × 2 = −10، اس لیے جواب −60 ہے۔"),
     common_wrong=[wrong(QB_FIRST_ONLY, "Multiply BOTH numbers in the bracket by −5: −50 + (−10) = −60.", "قوسین کے دونوں اعداد کو −5 سے ضرب دیں: −50 + (−10) = −60", "distributes_first_only"),
                   wrong(60, "Different signs give a negative answer: −60.", "مختلف علامتوں کا جواب منفی ہوتا ہے: −60")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T(f"Sana wrote 9 ÷ 0 = 0. What went wrong?", f"ثناء نے لکھا 9 ÷ 0 = 0۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("undefined", "Dividing by 0 is not defined, so 9 ÷ 0 has no answer.", "0 سے تقسیم کی تعریف نہیں، اس لیے 9 ÷ 0 کا کوئی جواب نہیں۔", True,
           "Yes! No number times 0 gives 9.", "جی ہاں! کوئی عدد ضرب 0، 9 نہیں دیتا۔"),
       opt("nine", "The answer should be 9.", "جواب 9 ہونا چاہیے۔", False,
           "Check: 9 × 0 = 0, not 9. Dividing by 0 is not defined.", "جانچیں: 9 × 0 = 0 ہے، 9 نہیں۔ 0 سے تقسیم کی تعریف نہیں۔"),
       opt("nothing", "Nothing. Anything with 0 gives 0.", "کوئی غلطی نہیں۔ 0 کے ساتھ ہر جواب 0 ہوتا ہے۔", False,
           "0 ÷ 9 = 0, but 9 ÷ 0 is not defined.", "0 ÷ 9 = 0 ہے، لیکن 9 ÷ 0 کی تعریف نہیں۔", "divide_by_zero_is_zero"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_laws", "front": T("Which operations can swap order?", "کن عملوں میں ترتیب بدل سکتے ہیں؟"),
    "back": T("+ and × only. −4 + 9 = 9 + (−4) and (−3) × 5 = 5 × (−3). Not − or ÷.", "صرف + اور ×۔ −4 + 9 = 9 + (−4) اور (−3) × 5 = 5 × (−3)۔ − اور ÷ میں نہیں۔")},
   {"id": "f_distribute", "front": T("(−2) × (6 + 4) = ?", "(−2) × (6 + 4) = ؟"),
    "back": T("(−2 × 6) + (−2 × 4) = −12 + (−8) = −20", "(−2 × 6) + (−2 × 4) = −12 + (−8) = −20")},
 ],
 "home_tasks": [{"id": "h_check", "text": T(
   "Pick two integers, one of them negative. Check that a + b = b + a and a × b = b × a. Then check a − b and b − a. Show someone at home what you found.",
   "دو صحیح اعداد چنیں، ایک منفی ہو۔ جانچیں کہ a + b = b + a اور a × b = b × a۔ پھر a − b اور b − a جانچیں۔ گھر میں کسی کو دکھائیں کہ آپ نے کیا پایا۔")}],
 "glossary": [T("Commutative law", "خاصیت مبادلہ"), T("Associative law", "خاصیت تلازم"),
              T("Distributive law", "خاصیت تقسیم"), T("Not defined", "غیر معین")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "I added −4 + 9 and my friend added 9 + (−4). We both got 5! Does order ever matter?",
      "میں نے −4 + 9 جمع کیا اور میرے دوست نے 9 + (−4)۔ دونوں کا جواب 5 آیا! کیا ترتیب کبھی اہم ہوتی ہے؟"),
    "text": T("Today we learn the laws of integers: rules that make sums easier. First, a quick multiplication check.",
              "آج ہم صحیح اعداد کے قوانین سیکھیں گے: ایسے اصول جو سوال آسان بناتے ہیں۔ پہلے ضرب کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T(f"Work out {b(-3)} × 5", f"حل کریں: {b(-3)} × 5"),
     -15,
     T("3 × 5 = 15. The signs are different.", "3 × 5 = 15۔ علامتیں مختلف ہیں۔"),
     T("Right! (−3) × 5 = −15.", "درست! (−3) × 5 = −15"),
     T("3 × 5 = 15, and different signs give a negative answer: −15.", "3 × 5 = 15، اور مختلف علامتوں کا جواب منفی ہوتا ہے: −15"),
     common_wrong=[wrong(15, "Different signs give a negative answer: −15.", "مختلف علامتوں کا جواب منفی ہوتا ہے: −15")],
     qtype="recall", skill=INT_MULTIPLY),
   {"id": "s3_laws", "type": "explain",
    "character": say("happy", "Three laws help us: swap, group, and share out!", "تین قوانین ہماری مدد کرتے ہیں: ترتیب بدلنا، گروہ بنانا، اور بانٹنا!"),
    "text": T("Commutative law: order does not matter for + and ×. (−3) × 5 = 5 × (−3) = −15. But 7 − 3 is not 3 − 7, and 8 ÷ 2 is not 2 ÷ 8. "
              "Associative law: for + and ×, grouping does not matter. (−6 + 4) + 10 = −6 + (4 + 10) = 8. "
              "Distributive law: multiply EACH number in the bracket. (−2) × (6 + 4) = (−2 × 6) + (−2 × 4) = −20. "
              "Zero: 0 ÷ (−9) = 0, but dividing by 0 is not defined.",
              "خاصیت مبادلہ: + اور × میں ترتیب سے فرق نہیں پڑتا۔ (−3) × 5 = 5 × (−3) = −15۔ لیکن 7 − 3 اور 3 − 7 برابر نہیں، اور 8 ÷ 2 اور 2 ÷ 8 بھی برابر نہیں۔ "
              "خاصیت تلازم: + اور × میں گروہ بدلنے سے فرق نہیں پڑتا۔ (−6 + 4) + 10 = −6 + (4 + 10) = 8۔ "
              "خاصیت تقسیم: قوسین کے ہر عدد کو ضرب دیں۔ (−2) × (6 + 4) = (−2 × 6) + (−2 × 4) = −20۔ "
              "صفر: 0 ÷ (−9) = 0، لیکن 0 سے تقسیم کی تعریف نہیں۔")},
   {"id": "s4_order", "type": "choice", "question_type": "apply",
    "prompt": T("Which one is TRUE?", "کون سا درست ہے؟"),
    "options": [
      opt("times", f"{b(-3)} × 5 = 5 × {b(-3)}", f"{b(-3)} × 5 = 5 × {b(-3)}", True,
          "Yes! Both are −15. Order does not matter for ×.", "جی ہاں! دونوں −15 ہیں۔ ضرب میں ترتیب سے فرق نہیں پڑتا۔"),
      opt("minus", "7 − 3 = 3 − 7", "7 − 3 = 3 − 7", False,
          "7 − 3 = 4 but 3 − 7 = −4. Order matters for −.", "7 − 3 = 4 لیکن 3 − 7 = −4۔ تفریق میں ترتیب اہم ہے۔", "subtraction_commutative"),
      opt("divide", "8 ÷ 2 = 2 ÷ 8", "8 ÷ 2 = 2 ÷ 8", False,
          "8 ÷ 2 = 4 but 2 ÷ 8 is less than 1. Order matters for ÷.", "8 ÷ 2 = 4 لیکن 2 ÷ 8 ایک سے کم ہے۔ تقسیم میں ترتیب اہم ہے۔", "subtraction_commutative"),
    ]},
   number_question(
     "s5_group",
     T("Group the easy numbers first: work out −6 + (4 + 10)", "آسان اعداد کا پہلے گروہ بنائیں: حل کریں −6 + (4 + 10)"),
     8,
     T("4 + 10 = 14. Then −6 + 14.", "4 + 10 = 14۔ پھر −6 + 14"),
     T("Right! −6 + 14 = 8. And (−6 + 4) + 10 = −2 + 10 = 8 too.", "درست! −6 + 14 = 8۔ اور (−6 + 4) + 10 = −2 + 10 = 8 بھی۔"),
     T("4 + 10 = 14, and −6 + 14 = 8.", "4 + 10 = 14، اور −6 + 14 = 8"),
     common_wrong=[wrong(-8, "14 is bigger than 6, so the answer is positive: 8.", "14، 6 سے بڑا ہے، اس لیے جواب مثبت ہے: 8"),
                   wrong(20, "−6 is negative, so take 6 away: 14 − 6 = 8.", "−6 منفی ہے، اس لیے 6 گھٹائیں: 14 − 6 = 8")]),
   number_question(
     "s6_distribute",
     T(f"Work out {b(-2)} × (6 + 4) by multiplying each number in the bracket.", f"قوسین کے ہر عدد کو ضرب دے کر حل کریں: {b(-2)} × (6 + 4)"),
     -20,
     T("(−2) × 6 = −12 and (−2) × 4 = −8. Add them.", "(−2) × 6 = −12 اور (−2) × 4 = −8۔ انہیں جمع کریں۔"),
     T("Right! −12 + (−8) = −20. Check: (−2) × 10 = −20.", "درست! −12 + (−8) = −20۔ جانچیں: (−2) × 10 = −20"),
     T("(−2) × 6 = −12 and (−2) × 4 = −8, so −12 + (−8) = −20.", "(−2) × 6 = −12 اور (−2) × 4 = −8، اس لیے −12 + (−8) = −20"),
     common_wrong=[wrong(S6_FIRST_ONLY, "Multiply the 4 by −2 as well: −12 + (−8) = −20.", "4 کو بھی −2 سے ضرب دیں: −12 + (−8) = −20", "distributes_first_only"),
                   wrong(20, "Different signs give a negative answer: −20.", "مختلف علامتوں کا جواب منفی ہوتا ہے: −20")]),
   number_question(
     "s7_mental",
     T(f"Make it easy: {b(-4)} × 23 = {b(-4)} × 20 + {b(-4)} × 3. What is the answer?", f"آسان بنائیں: {b(-4)} × 23 = {b(-4)} × 20 + {b(-4)} × 3۔ جواب کیا ہے؟"),
     -92,
     T("(−4) × 20 = −80 and (−4) × 3 = −12.", "(−4) × 20 = −80 اور (−4) × 3 = −12"),
     T("Right! −80 + (−12) = −92.", "درست! −80 + (−12) = −92"),
     T("(−4) × 20 = −80 and (−4) × 3 = −12, so the answer is −92.", "(−4) × 20 = −80 اور (−4) × 3 = −12، اس لیے جواب −92 ہے۔"),
     common_wrong=[wrong(S7_FIRST_ONLY, "Multiply the 3 by −4 too: −80 + (−12) = −92.", "3 کو بھی −4 سے ضرب دیں: −80 + (−12) = −92", "distributes_first_only"),
                   wrong(92, "Different signs give a negative answer: −92.", "مختلف علامتوں کا جواب منفی ہوتا ہے: −92")]),
   {"id": "s8_zero", "type": "choice", "question_type": "apply",
    "prompt": T(f"What is {b(-7)} ÷ 0?", f"{b(-7)} ÷ 0 کتنا ہے؟"),
    "options": [
      opt("undefined", "Not defined", "اس کی تعریف نہیں", True,
          "Yes! No number times 0 gives −7, so dividing by 0 is not defined.", "جی ہاں! کوئی عدد ضرب 0، −7 نہیں دیتا، اس لیے 0 سے تقسیم کی تعریف نہیں۔"),
      opt("zero", "0", "0", False,
          "0 ÷ (−7) = 0, but (−7) ÷ 0 is not defined.", "0 ÷ (−7) = 0 ہے، لیکن (−7) ÷ 0 کی تعریف نہیں۔", "divide_by_zero_is_zero"),
      opt("minus_seven", "−7", "−7", False,
          "Check: (−7) × 0 = 0, not −7. Dividing by 0 is not defined.", "جانچیں: (−7) × 0 = 0 ہے، −7 نہیں۔ 0 سے تقسیم کی تعریف نہیں۔"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T(f"Hamza wrote {b(-3)} × (4 + 5) = −12 + 5 = −7. What went wrong?", f"حمزہ نے لکھا {b(-3)} × (4 + 5) = −12 + 5 = −7۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("both", "He must multiply the 5 by −3 too: −12 + (−15) = −27.", "اسے 5 کو بھی −3 سے ضرب دینی تھی: −12 + (−15) = −27", True,
          "Yes! Multiply each number in the bracket. Check: (−3) × 9 = −27.", "جی ہاں! قوسین کے ہر عدد کو ضرب دیں۔ جانچیں: (−3) × 9 = −27"),
      opt("sign", "The answer should be positive: 7.", "جواب مثبت ہونا چاہیے: 7", False,
          "The real mistake is the 5: it must be multiplied by −3 too. The answer is −27.", "اصل غلطی 5 میں ہے: اسے بھی −3 سے ضرب دینی تھی۔ جواب −27 ہے۔"),
      opt("nothing", "Nothing. Multiply the first number only.", "کوئی غلطی نہیں۔ صرف پہلے عدد کو ضرب دیں۔", False,
          "Every number in the bracket is multiplied: (−3) × 4 and (−3) × 5. The answer is −27.", "قوسین کے ہر عدد کو ضرب دی جاتی ہے: (−3) × 4 اور (−3) × 5۔ جواب −27 ہے۔", "distributes_first_only"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "My cousin says 6 ÷ 0 = 0, because 0 ÷ 6 = 0. Can you teach us?",
                     "میرا کزن کہتا ہے 6 ÷ 0 = 0، کیونکہ 0 ÷ 6 = 0۔ کیا آپ ہمیں سمجھا سکتے ہیں؟"),
    "task": T("In your own words: why is 0 ÷ 6 = 0, but 6 ÷ 0 is not defined? Think: what number times 0 gives 6?",
              "اپنے الفاظ میں بتائیں: 0 ÷ 6 = 0 کیوں ہے، لیکن 6 ÷ 0 کی تعریف کیوں نہیں؟ سوچیں: کون سا عدد ضرب 0، 6 دیتا ہے؟"),
    "key_idea": "Division undoes multiplication. 0 ÷ 6 = 0 because 6 × 0 = 0. For 6 ÷ 0 we need a number that times 0 gives 6, but anything times 0 is 0, so there is no answer: it is not defined.",
    "levels": {
      "got_it": "Uses the check by multiplication: 6 × 0 = 0 so 0 ÷ 6 = 0, while nothing times 0 gives 6, so 6 ÷ 0 is not defined.",
      "partly": "States that dividing by 0 is not defined, or that order matters in ÷, without the multiplication reason.",
      "not_yet": "Agrees 6 ÷ 0 = 0, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["times 0", "× 0", "multiply", "ضرب", "zarb"],
      ["not defined", "no answer", "undefined", "تعریف نہیں", "کوئی جواب نہیں", "tareef"],
      ["0", "zero", "صفر", "sifar"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Anything times 0 is 0, so no number times 0 gives 6. That is why 6 ÷ 0 is not defined.",
                  "بہت خوب سمجھایا! ہر عدد ضرب 0، 0 ہوتا ہے، اس لیے کوئی عدد ضرب 0، 6 نہیں دیتا۔ اسی لیے 6 ÷ 0 کی تعریف نہیں۔"),
      "partly": T("Good start! Now check with multiplication: what number times 0 gives 6?", "اچھی شروعات! اب ضرب سے جانچیں: کون سا عدد ضرب 0، 6 دیتا ہے؟"),
      "not_yet": T("Look: 0 ÷ 6 = 0 because 6 × 0 = 0. Now, can any number times 0 give 6?",
                   "دیکھیں: 0 ÷ 6 = 0 کیونکہ 6 × 0 = 0۔ اب، کیا کوئی عدد ضرب 0، 6 دے سکتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_which_law", "type": "choice", "question_type": "recall",
    "prompt": T("(−2 + 7) + 3 = −2 + (7 + 3). Which law is this?", "(−2 + 7) + 3 = −2 + (7 + 3)۔ یہ کون سا قانون ہے؟"),
    "options": [
      opt("associative", "Associative law", "خاصیت تلازم", True,
          "Yes! Only the grouping changed. Both sides are 8.", "جی ہاں! صرف گروہ بدلا ہے۔ دونوں طرف 8 ہے۔"),
      opt("commutative", "Commutative law", "خاصیت مبادلہ", False,
          "The numbers stay in the same order. Only the brackets moved: associative.", "اعداد کی ترتیب وہی ہے۔ صرف قوسین بدلی ہیں: خاصیت تلازم۔"),
      opt("distributive", "Distributive law", "خاصیت تقسیم", False,
          "There is no multiplying here. Only the brackets moved: associative.", "یہاں ضرب نہیں ہے۔ صرف قوسین بدلی ہیں: خاصیت تلازم۔"),
    ]},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Swap, group, share out, and never divide by zero. Well done!", "ترتیب بدلیں، گروہ بنائیں، بانٹیں، اور کبھی 0 سے تقسیم نہ کریں۔ شاباش!"),
    "text": T("Commutative: −4 + 9 = 9 + (−4), (−3) × 5 = 5 × (−3), but not for − or ÷. Associative: (−6 + 4) + 10 = −6 + (4 + 10). Distributive: (−2) × (6 + 4) = (−2 × 6) + (−2 × 4) = −20. 0 ÷ (−9) = 0, but dividing by 0 is not defined.",
              "خاصیت مبادلہ: −4 + 9 = 9 + (−4)، (−3) × 5 = 5 × (−3)، لیکن − اور ÷ میں نہیں۔ خاصیت تلازم: (−6 + 4) + 10 = −6 + (4 + 10)۔ خاصیت تقسیم: (−2) × (6 + 4) = (−2 × 6) + (−2 × 4) = −20۔ 0 ÷ (−9) = 0، لیکن 0 سے تقسیم کی تعریف نہیں۔"),
    "points": [T("a × (b + c) = a × b + a × c", "a × (b + c) = a × b + a × c"), T("a ÷ 0: not defined", "a ÷ 0: تعریف نہیں")]},
 ],
 "review_questions": [
   {"id": "r_zero", "type": "apply", "skill": SKILL, "step": number_question(
     "r_zero",
     T(f"Work out 0 ÷ {b(-8)}", f"حل کریں: 0 ÷ {b(-8)}"),
     0,
     T("What number times −8 gives 0?", "کون سا عدد ضرب −8، 0 دیتا ہے؟"),
     T("Right! 0 ÷ (−8) = 0, because (−8) × 0 = 0.", "درست! 0 ÷ (−8) = 0، کیونکہ (−8) × 0 = 0"),
     T("0 divided by any non-zero number is 0.", "0 کو کسی بھی غیر صفر عدد سے تقسیم کریں تو جواب 0 ہوتا ہے۔"),
     common_wrong=[wrong(-8, "Check: (−8) × (−8) = 64, not 0. The answer is 0.", "جانچیں: (−8) × (−8) = 64 ہے، 0 نہیں۔ جواب 0 ہے۔")],
     qtype=None)},
   {"id": "r_group", "type": "apply", "skill": SKILL, "step": number_question(
     "r_group",
     T(f"Work out {b(-3)} × ({b(-2)} × 5)", f"حل کریں: {b(-3)} × ({b(-2)} × 5)"),
     30,
     T("Group it as ((−3) × (−2)) × 5 = 6 × 5.", "اسے یوں گروہ بنائیں: ((−3) × (−2)) × 5 = 6 × 5"),
     T("Right! Either way the answer is 30.", "درست! کسی بھی طرح جواب 30 ہے۔"),
     T("(−2) × 5 = −10, and (−3) × (−10) = 30.", "(−2) × 5 = −10، اور (−3) × (−10) = 30"),
     common_wrong=[wrong(-30, "Two negatives multiplied give a positive answer: 30.", "دو منفی اعداد کی ضرب مثبت ہوتی ہے: 30")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Laws of Integers chapter. No textbook text or exercises were used.",
   "The laws are taught by name and by example; children are not asked to write a, b, c proofs.",
   "Division by zero is shown as 'not defined' using the multiplication check (s8, s10).",
   "Urdu terms to check: خاصیت مبادلہ (commutative), خاصیت تلازم (associative), خاصیت تقسیم (distributive), غیر معین / تعریف نہیں (not defined).",
   "The numbers were worked out in content/sources/g6-maths-04/laws_of_integers.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
attach(lesson, {
    "s1_hook": FIG_S1, "s3_laws": FIG_S3, "s5_group": FIG_S5, "s6_distribute": FIG_S6,
    "s7_mental": FIG_S7, "s9_find_error": FIG_S9, "s12_summary": FIG_S12,
    "qb_apply": FIG_QB_APPLY,
})
write(lesson)

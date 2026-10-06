from common import (F, T, opt, say, wrong, frac, mixed, unsimplified, fraction_question, write,
                    REF, REVIEW, UNIT_FRACTIONS, TIMES_TABLES, MIXED)

SKILL = MIXED


def to_improper(whole: int, top: int, bottom: int) -> F:
    return F(whole * bottom + top, bottom)


def whole_added_to_top(whole: int, top: int, bottom: int) -> str:
    """The mistake: 2 1/2 -> 3/2 (adds the whole number to the numerator)."""
    return unsimplified(whole + top, bottom)


def forgot_the_extra(whole: int, top: int, bottom: int) -> str:
    """The mistake: 3 1/4 -> 12/4 (multiplies but forgets to add the numerator)."""
    return unsimplified(whole * bottom, bottom)


def swapped(x: F) -> str:
    """The mistake: 11/4 -> 3 2/4 (quotient and remainder swapped)."""
    q, r = divmod(x.numerator, x.denominator)
    return f"{r} {q}/{x.denominator}"


# s1, s3, s4, s5: Ali's 2 and a half rotis
ROTIS = to_improper(2, 1, 2)
assert ROTIS == F(5, 2) and frac(ROTIS) == "5/2" and mixed(ROTIS) == "2 1/2"
assert ROTIS > 1
assert whole_added_to_top(2, 1, 2) == "3/2"

# s6: 3 1/4 as an improper fraction
S6 = to_improper(3, 1, 4)
assert S6 == F(13, 4)
assert whole_added_to_top(3, 1, 4) == "4/4" and forgot_the_extra(3, 1, 4) == "12/4"

# s7: 7/2 back to a mixed number
assert divmod(7, 2) == (3, 1) and mixed(F(7, 2)) == "3 1/2"

# s8: 11 quarters of paratha
QUARTERS = F(11, 4)
assert divmod(11, 4) == (2, 3) and mixed(QUARTERS) == "2 3/4"
assert swapped(QUARTERS) == "3 2/4" and F(3) + F(2, 4) != QUARTERS

# s9: the number line, 0 to 4 in halves
LINE = {"min": 0, "max": 4, "step": 0.5}
assert F(LINE["step"]) == F(1, 2) and (ROTIS - LINE["min"]) / F(LINE["step"]) == 5

# s10: Hamza's mistake
assert whole_added_to_top(2, 1, 3) == "3/3" and to_improper(2, 1, 3) == F(7, 3)

# s11: explain 2 3/4 -> 11/4
assert to_improper(2, 3, 4) == F(11, 4)

# s12: Zara's milk packs
PACKS = 9
MILK = PACKS * F(1, 2)
assert MILK == F(9, 2) and mixed(MILK) == "4 1/2"
assert swapped(MILK) == "1 4/2"

# Question bank and review
assert mixed(F(17, 5)) == "3 2/5" and to_improper(4, 2, 3) == F(14, 3)
assert to_improper(1, 2, 5) == F(7, 5) and mixed(F(10, 3)) == "3 1/3"

lesson = {
 "id": "g6-maths-02-mixed-numbers",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Change mixed numbers to improper fractions and improper fractions to mixed numbers, and place them on a number line.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Mixed numbers and improper fractions", "مخلوط اعداد اور غیر واجب کسور"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": UNIT_FRACTIONS}, {"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "improper_less_than_one", "description": "Thinks every fraction is less than 1, so 5/2 must be a small amount."},
   {"id": "whole_added_to_top", "description": "Adds the whole number to the numerator (2 1/2 = 3/2) instead of changing the wholes into pieces."},
   {"id": "forgot_the_extra", "description": "Changes the wholes into pieces but forgets to add the extra pieces (3 1/4 = 12/4)."},
   {"id": "swapped_quotient_remainder", "description": "When changing to a mixed number, swaps the whole number and the remainder (11/4 = 3 2/4)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_which_improper", "type": "recall", "step": {
     "id": "qb_which_improper", "type": "choice",
     "prompt": T("Which of these is an improper fraction?", "ان میں سے غیر واجب کسر کون سی ہے؟"),
     "options": [
       opt("seven_thirds", "7/3", "7/3", True,
           "Yes! The numerator (7) is bigger than the denominator (3), so it is more than 1 whole.", "جی ہاں! شمار کنندہ (7) نسب نما (3) سے بڑا ہے، اس لیے یہ 1 پورے سے زیادہ ہے۔"),
       opt("three_sevenths", "3/7", "3/7", False,
           "3/7 is less than 1 whole: its numerator is smaller than its denominator.", "3/7 ایک پورے سے کم ہے: اس کا شمار کنندہ نسب نما سے چھوٹا ہے۔"),
       opt("mixed", "2 1/3", "2 1/3", False,
           "2 1/3 is a mixed number: a whole number and a fraction together.", "2 1/3 مخلوط عدد ہے: پورا عدد اور کسر ایک ساتھ۔"),
     ]}},
   {"id": "qb_seventeen_fifths", "type": "apply", "step": fraction_question(
     "qb_seventeen_fifths",
     T("Write 17/5 as a mixed number.", "17/5 کو مخلوط عدد کی شکل میں لکھیں۔"),
     mixed(F(17, 5)),
     T("17 ÷ 5 = ? remainder ?", "17 ÷ 5 = ? باقی ?"),
     T("Right! 17 ÷ 5 = 3 remainder 2, so 17/5 = 3 2/5.", "درست! 17 ÷ 5 = 3 باقی 2، اس لیے 17/5 = 3 2/5"),
     T("5 fifths make 1 whole. 17 ÷ 5 = 3 remainder 2: 3 wholes and 2 fifths left, so 3 2/5.", "5 پانچویں حصے 1 پورا بناتے ہیں۔ 17 ÷ 5 = 3 باقی 2: 3 پورے اور 2 پانچویں حصے بچے، یعنی 3 2/5"),
     common_wrong=[
       wrong(swapped(F(17, 5)), "You swapped them. The answer of the division (3) is the whole number; the remainder (2) goes on top.",
             "آپ نے جگہ بدل دی۔ تقسیم کا جواب (3) پورا عدد ہے؛ باقی (2) اوپر جاتا ہے۔", "swapped_quotient_remainder"),
       wrong(frac(F(17, 5)), "That is the fraction we started with. Write it as wholes and a fraction.", "یہ تو وہی کسر ہے جس سے شروع کیا۔ اسے پورے اور کسر کی شکل میں لکھیں۔")],
     qtype=None)},
   {"id": "qb_find_error_forgot", "type": "find_error", "step": {
     "id": "qb_find_error_forgot", "type": "choice",
     "prompt": T("Sana says 4 2/3 = 12/3. What went wrong?", "ثنا کہتی ہے 4 2/3 = 12/3۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("extra", "She changed 4 wholes to 12 thirds but forgot the 2 extra thirds: 4 2/3 = 14/3.", "اس نے 4 پوروں کو 12 تہائیاں بنایا لیکن 2 اضافی تہائیاں بھول گئی: 4 2/3 = 14/3", True,
           "Right! 12 thirds + 2 thirds = 14 thirds.", "درست! 12 تہائیاں + 2 تہائیاں = 14 تہائیاں۔"),
       opt("nothing", "Nothing. 4 × 3 = 12.", "کوئی غلطی نہیں۔ 4 × 3 = 12", False,
           "12/3 is exactly 4. Where did the 2/3 go?", "12/3 تو بالکل 4 ہے۔ 2/3 کہاں گیا؟", "forgot_the_extra"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_to_improper", "front": T("How do you change 2 1/2 into an improper fraction?", "2 1/2 کو غیر واجب کسر میں کیسے بدلتے ہیں؟"),
    "back": T("Wholes × denominator, then add the numerator: 2 × 2 + 1 = 5, so 2 1/2 = 5/2.", "پورے × نسب نما، پھر شمار کنندہ جمع کریں: 2 × 2 + 1 = 5، اس لیے 2 1/2 = 5/2")},
   {"id": "f_to_mixed", "front": T("How do you change 7/2 into a mixed number?", "7/2 کو مخلوط عدد میں کیسے بدلتے ہیں؟"),
    "back": T("Divide: 7 ÷ 2 = 3 remainder 1. So 7/2 = 3 1/2.", "تقسیم کریں: 7 ÷ 2 = 3 باقی 1۔ اس لیے 7/2 = 3 1/2")},
 ],
 "home_tasks": [{"id": "h_count_halves", "text": T(
   "At dinner, count the rotis or parathas on the plate. Imagine each one cut in half. How many halves would there be? Write it as a mixed number and as an improper fraction (for example 2 1/2 = 5/2).",
   "رات کے کھانے پر پلیٹ میں روٹیاں یا پراٹھے گنیں۔ سوچیں کہ ہر ایک کو آدھا کاٹ دیا گیا ہے۔ کتنے آدھے ٹکڑے ہوں گے؟ اسے مخلوط عدد اور غیر واجب کسر دونوں شکلوں میں لکھیں (مثلاً 2 1/2 = 5/2)۔")}],
 "glossary": [T("Fraction", "کسر"), T("Numerator", "شمار کنندہ"), T("Denominator", "نسب نما"),
              T("Mixed number", "مخلوط عدد"), T("Improper fraction", "غیر واجب کسر"), T("Proper fraction", "واجب کسر"),
              T("Remainder", "باقی"), T("Number line", "عددی خط")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Ali ate 2 rotis and a half. How many half pieces is that?",
                     "علی نے ڈھائی روٹیاں کھائیں۔ یہ کتنے آدھے ٹکڑے بنتے ہیں؟"),
    "text": T("2 and a half is written 2 1/2. Let's find out how many halves it is. First, a quick check.",
              "ڈھائی کو 2 1/2 لکھتے ہیں۔ آئیں معلوم کریں کہ اس میں کتنے آدھے ہیں۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": UNIT_FRACTIONS,
    "prompt": T("How many halves make one whole roti?", "کتنے آدھے مل کر ایک پوری روٹی بناتے ہیں؟"),
    "options": [
      opt("two", "2", "2", True, "Yes! 2 halves make 1 whole: 2/2 = 1.", "جی ہاں! 2 آدھے 1 پوری بناتے ہیں: 2/2 = 1"),
      opt("one", "1", "1", False, "One half is only part of the roti. How many halves cover it all?", "ایک آدھا تو روٹی کا صرف ایک حصہ ہے۔ کتنے آدھے پوری روٹی ڈھانپتے ہیں؟"),
      opt("four", "4", "4", False, "4 pieces would be quarters. Halves are 2 equal pieces.", "4 ٹکڑے چوتھائیاں ہوں گی۔ آدھے 2 برابر ٹکڑے ہوتے ہیں۔"),
    ]},
   {"id": "s3_predict", "type": "choice",
    "prompt": T("Guess first: 5/2 of a roti means 5 halves. Is that more or less than 1 whole roti?",
                "پہلے اندازہ لگائیں: 5/2 روٹی کا مطلب ہے 5 آدھے۔ کیا یہ 1 پوری روٹی سے زیادہ ہے یا کم؟"),
    "options": [
      opt("less", "Less: a fraction is always part of one thing", "کم: کسر ہمیشہ کسی چیز کا حصہ ہوتی ہے", False,
          "Many people think so. But 2 halves already make 1 roti, and here there are 5 halves. Let's test it.",
          "بہت سے لوگ ایسا سمجھتے ہیں۔ لیکن 2 آدھے تو 1 روٹی بنا دیتے ہیں، اور یہاں 5 آدھے ہیں۔ آئیں جانچیں۔", "improper_less_than_one"),
      opt("more", "More than 1 roti", "1 روٹی سے زیادہ", True,
          "Good thinking! 2 halves make 1 roti, so 5 halves are more than 1 roti.", "بہت خوب سوچا! 2 آدھے 1 روٹی بناتے ہیں، اس لیے 5 آدھے 1 روٹی سے زیادہ ہیں۔"),
      opt("same", "Exactly 1 roti", "پوری 1 روٹی", False,
          "1 roti is 2 halves, written 2/2. 5/2 has 3 more halves.", "1 روٹی 2 آدھے ہے، یعنی 2/2۔ 5/2 میں 3 آدھے اور ہیں۔"),
    ]},
   {"id": "s4_test_it", "type": "sim", "question_type": "apply", "renderer": "native", "sim_id": "fraction_bars",
    "prompt": T("Show Ali's 2 1/2 rotis. Use + to cut every roti into halves. Tap the halves Ali ate: 2 whole rotis and half of the third. Press Check.",
                "علی کی 2 1/2 روٹیاں دکھائیں۔ + دبا کر ہر روٹی کے آدھے کریں۔ وہ آدھے چھوئیں جو علی نے کھائے: 2 پوری روٹیاں اور تیسری کا آدھا۔ \"جانچیں\" دبائیں۔"),
    "params": {"wholes": 3, "max_cut": 6},
    "expected": {"result": "pieces", "checker": "numeric", "answer": str(ROTIS.numerator)},
    "hint": T("Each whole roti is 2 halves. Then add the last half.", "ہر پوری روٹی 2 آدھے ہے۔ پھر آخری آدھا جمع کریں۔"),
    "feedback_correct": T("Yes! 2 rotis are 4 halves, plus 1 half makes 5 halves. So 2 1/2 = 5/2.", "جی ہاں! 2 روٹیاں 4 آدھے ہیں، اور 1 آدھا ملا کر 5 آدھے۔ یعنی 2 1/2 = 5/2"),
    "feedback_wrong": T("2 whole rotis make 2 × 2 = 4 halves. Add the last half: 4 + 1 = 5 halves. 2 1/2 = 5/2.", "2 پوری روٹیاں 2 × 2 = 4 آدھے بناتی ہیں۔ آخری آدھا جمع کریں: 4 + 1 = 5 آدھے۔ 2 1/2 = 5/2"),
    "common_wrong": [
      wrong("3", "That is 3 halves, only 1 1/2 rotis. Each whole roti has 2 halves.", "یہ 3 آدھے ہیں، یعنی صرف 1 1/2 روٹی۔ ہر پوری روٹی میں 2 آدھے ہوتے ہیں۔", "whole_added_to_top"),
      wrong("4", "4 halves are the 2 whole rotis. Don't forget the last half!", "4 آدھے تو 2 پوری روٹیاں ہیں۔ آخری آدھا نہ بھولیں!", "forgot_the_extra"),
    ]},
   {"id": "s5_see_it", "type": "explain",
    "character": say("happy", "Two names for the same amount of roti!", "روٹی کی ایک ہی مقدار کے دو نام!"),
    "text": T("2 1/2 is a mixed number: a whole number and a fraction. 5/2 is an improper fraction: its numerator is bigger than its denominator, so it is more than 1. They are the same amount. To change 2 1/2: 2 wholes × 2 halves = 4 halves, plus 1 half = 5 halves. So 2 1/2 = (2 × 2 + 1)/2 = 5/2.",
              "2 1/2 مخلوط عدد ہے: پورا عدد اور کسر ایک ساتھ۔ 5/2 غیر واجب کسر ہے: اس کا شمار کنندہ نسب نما سے بڑا ہے، اس لیے یہ 1 سے زیادہ ہے۔ دونوں ایک جتنی مقدار ہیں۔ 2 1/2 کو بدلنے کے لیے: 2 پورے × 2 آدھے = 4 آدھے، اور 1 آدھا ملا کر 5 آدھے۔ یعنی 2 1/2 = (2 × 2 + 1)/2 = 5/2")},
   fraction_question(
     "s6_to_improper",
     T("A tailor has 3 1/4 metres of cloth. Write 3 1/4 as an improper fraction.", "ایک درزی کے پاس 3 1/4 میٹر کپڑا ہے۔ 3 1/4 کو غیر واجب کسر کی شکل میں لکھیں۔"),
     frac(S6),
     T("How many quarters are in 3 wholes? Then add the extra quarter.", "3 پوروں میں کتنی چوتھائیاں ہیں؟ پھر اضافی چوتھائی جمع کریں۔"),
     T("Right! 3 × 4 + 1 = 13, so 3 1/4 = 13/4.", "درست! 3 × 4 + 1 = 13، اس لیے 3 1/4 = 13/4"),
     T("3 wholes are 3 × 4 = 12 quarters. Add 1 more quarter: 13 quarters. 3 1/4 = 13/4.", "3 پورے 3 × 4 = 12 چوتھائیاں ہیں۔ 1 چوتھائی اور جمع کریں: 13 چوتھائیاں۔ 3 1/4 = 13/4"),
     common_wrong=[
       wrong(whole_added_to_top(3, 1, 4), "You added 3 to the top. But 3 wholes are 12 quarters, not 3.", "آپ نے اوپر 3 جمع کیا۔ لیکن 3 پورے 12 چوتھائیاں ہیں، 3 نہیں۔", "whole_added_to_top"),
       wrong(forgot_the_extra(3, 1, 4), "12/4 is the 3 wholes. Add the extra 1/4 too.", "12/4 تو 3 پورے ہیں۔ اضافی 1/4 بھی جمع کریں۔", "forgot_the_extra"),
       wrong(mixed(S6), "That is the mixed number we started with. Write it as one fraction with 4 at the bottom.", "یہ تو وہی مخلوط عدد ہے جس سے شروع کیا۔ اسے ایک کسر کی شکل میں لکھیں جس کے نیچے 4 ہو۔"),
     ]),
   {"id": "s7_other_way", "type": "explain",
    "character": say("thinking", "Now the other way: we divide!", "اب الٹی طرف: ہم تقسیم کریں گے!"),
    "text": T("To change 7/2 into a mixed number, ask: how many whole rotis do 7 halves make? Every 2 halves make 1 roti, so divide: 7 ÷ 2 = 3 remainder 1. That is 3 whole rotis and 1 half left over: 7/2 = 3 1/2. The answer of the division is the whole number; the remainder goes on top.",
              "7/2 کو مخلوط عدد میں بدلنے کے لیے پوچھیں: 7 آدھے کتنی پوری روٹیاں بناتے ہیں؟ ہر 2 آدھے 1 روٹی بناتے ہیں، اس لیے تقسیم کریں: 7 ÷ 2 = 3 باقی 1۔ یعنی 3 پوری روٹیاں اور 1 آدھا بچا: 7/2 = 3 1/2۔ تقسیم کا جواب پورا عدد ہے؛ باقی اوپر جاتا ہے۔")},
   fraction_question(
     "s8_to_mixed",
     T("Ayesha's mother cut parathas into quarters. There are 11 quarters on the plate: 11/4. Write 11/4 as a mixed number.",
       "عائشہ کی امی نے پراٹھوں کو چوتھائیوں میں کاٹا۔ پلیٹ میں 11 چوتھائیاں ہیں: 11/4۔ 11/4 کو مخلوط عدد کی شکل میں لکھیں۔"),
     mixed(QUARTERS),
     T("4 quarters make 1 paratha. 11 ÷ 4 = ? remainder ?", "4 چوتھائیاں 1 پراٹھا بناتی ہیں۔ 11 ÷ 4 = ? باقی ?"),
     T("Well done! 11 ÷ 4 = 2 remainder 3: 2 whole parathas and 3 quarters, 2 3/4.", "شاباش! 11 ÷ 4 = 2 باقی 3: 2 پورے پراٹھے اور 3 چوتھائیاں، یعنی 2 3/4"),
     T("11 ÷ 4 = 2 remainder 3. So there are 2 whole parathas and 3 quarters left: 11/4 = 2 3/4.", "11 ÷ 4 = 2 باقی 3۔ یعنی 2 پورے پراٹھے اور 3 چوتھائیاں بچیں: 11/4 = 2 3/4"),
     common_wrong=[
       wrong(swapped(QUARTERS), "You swapped them. 11 ÷ 4 = 2 remainder 3: the 2 is the wholes and the 3 goes on top.", "آپ نے جگہ بدل دی۔ 11 ÷ 4 = 2 باقی 3: 2 پورے ہیں اور 3 اوپر جاتا ہے۔", "swapped_quotient_remainder"),
       wrong(frac(QUARTERS), "That is the fraction we started with. Write it as whole parathas and a fraction.", "یہ تو وہی کسر ہے جس سے شروع کیا۔ اسے پورے پراٹھوں اور کسر کی شکل میں لکھیں۔"),
     ]),
   {"id": "s9_number_line", "type": "sim", "question_type": "apply", "renderer": "native", "sim_id": "number_line",
    "prompt": T("Put the marker on 2 1/2 on the number line. Press Check.", "عددی خط پر نشان کو 2 1/2 پر رکھیں۔ \"جانچیں\" دبائیں۔"),
    "params": dict(LINE),
    "expected": {"result": "value", "checker": "fraction", "answer": frac(ROTIS)},
    "hint": T("2 1/2 is between 2 and 3, half-way. Count the halves: it is 5/2.", "2 1/2، 2 اور 3 کے بالکل درمیان ہے۔ آدھے گنیں: یہ 5/2 ہے۔"),
    "feedback_correct": T("Yes! 2 1/2 = 5/2 is half-way between 2 and 3.", "جی ہاں! 2 1/2 = 5/2، 2 اور 3 کے بالکل درمیان ہے۔"),
    "feedback_wrong": T("Go past 2 by one more half: 2 1/2 = 5/2, half-way between 2 and 3.", "2 سے ایک آدھا آگے جائیں: 2 1/2 = 5/2، 2 اور 3 کے بالکل درمیان۔"),
    "common_wrong": [wrong(whole_added_to_top(2, 1, 2), "That is 3/2 = 1 1/2. 2 wholes are 4 halves, so 2 1/2 is 5 halves.", "یہ 3/2 = 1 1/2 ہے۔ 2 پورے 4 آدھے ہیں، اس لیے 2 1/2 پانچ آدھے ہے۔", "whole_added_to_top")]},
   {"id": "s10_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hamza says 2 1/3 = 3/3. What went wrong?", "حمزہ کہتا ہے 2 1/3 = 3/3۔ اس سے کیا غلطی ہوئی؟"),
    "options": [
      opt("added", "He added the 2 wholes to the top. 2 wholes are 6 thirds, so 2 1/3 = 7/3.", "اس نے 2 پوروں کو اوپر جمع کر دیا۔ 2 پورے 6 تہائیاں ہیں، اس لیے 2 1/3 = 7/3", True,
          "Yes! 3/3 is just 1 whole. 2 × 3 + 1 = 7, so 2 1/3 = 7/3.", "جی ہاں! 3/3 تو صرف 1 پورا ہے۔ 2 × 3 + 1 = 7، اس لیے 2 1/3 = 7/3"),
      opt("nothing", "Nothing, 2 + 1 = 3.", "کوئی غلطی نہیں، 2 + 1 = 3", False,
          "3/3 is only 1 whole, but 2 1/3 is more than 2. Something is missing.", "3/3 صرف 1 پورا ہے، جبکہ 2 1/3، 2 سے زیادہ ہے۔ کچھ کم ہے۔", "whole_added_to_top"),
      opt("bottom", "He should change the bottom: 2 1/3 = 1/6.", "اسے نیچے والا عدد بدلنا چاہیے: 2 1/3 = 1/6", False,
          "1/6 is less than 1! The pieces are still thirds, so the bottom stays 3.", "1/6 تو 1 سے بھی کم ہے! ٹکڑے اب بھی تہائیاں ہیں، اس لیے نیچے 3 ہی رہے گا۔"),
    ]},
   {"id": "s11_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? How does 2 3/4 turn into 11/4?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ 2 3/4 کیسے 11/4 بن جاتا ہے؟"),
    "task": T("In your own words: how do you change 2 3/4 into an improper fraction, and why does it work? You can use parathas cut into quarters.",
              "اپنے الفاظ میں بتائیں: 2 3/4 کو غیر واجب کسر میں کیسے بدلتے ہیں، اور یہ طریقہ کیوں درست ہے؟ آپ چوتھائیوں میں کٹے پراٹھوں کی مثال دے سکتے ہیں۔"),
    "key_idea": "Each whole is 4 quarters, so 2 wholes are 2 × 4 = 8 quarters. Add the 3 extra quarters: 8 + 3 = 11 quarters, so 2 3/4 = 11/4. It works because we count everything in quarters.",
    "levels": {
      "got_it": "Says each whole is 4 quarters so 2 wholes are 8 quarters (multiply), then adds the 3 quarters to get 11 quarters, 11/4.",
      "partly": "Gives the rule (multiply then add) or the answer 11/4, but does not say why (wholes become quarters).",
      "not_yet": "Adds the whole number to the numerator, gives no method, or the reasoning is wrong."},
    "keywords": [
      ["quarter", "4 pieces", "four pieces", "چوتھائ", "chothai", "chauthai", "chothaai"],
      ["multiply", "times", "8", "eight", "× 4", "x 4", "ضرب", "آٹھ", "zarb", "aath"],
      ["add", "plus", "11", "eleven", "جمع", "گیارہ", "jama", "gyarah", "gyara"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 2 parathas are 8 quarters, and 3 more quarters make 11 quarters: 11/4.",
                  "بہت خوب سمجھایا! 2 پراٹھے 8 چوتھائیاں ہیں، اور 3 چوتھائیاں ملا کر 11 چوتھائیاں: 11/4"),
      "partly": T("Good start! Now say why we multiply: how many quarters are in one whole paratha?",
                  "اچھی شروعات! اب بتائیں کہ ضرب کیوں دیتے ہیں: ایک پورے پراٹھے میں کتنی چوتھائیاں ہوتی ہیں؟"),
      "not_yet": T("Think of 2 parathas, each cut into 4 quarters, and 3 more quarters. How many quarters can you count?",
                   "سوچیں: 2 پراٹھے ہیں، ہر ایک 4 چوتھائیوں میں کٹا ہوا، اور 3 چوتھائیاں اور۔ آپ کتنی چوتھائیاں گن سکتے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   fraction_question(
     "s12_milk",
     T(f"Zara's family buys milk in half-litre packets. This week they used {PACKS} packets: {PACKS}/2 litres. How many litres is that? Write it as a mixed number.",
       f"زارا کے گھر والے آدھے لیٹر کے پیکٹ میں دودھ لیتے ہیں۔ اس ہفتے انہوں نے {PACKS} پیکٹ استعمال کیے: {PACKS}/2 لیٹر۔ یہ کتنے لیٹر ہیں؟ مخلوط عدد کی شکل میں لکھیں۔"),
     mixed(MILK),
     T("2 packets make 1 litre. 9 ÷ 2 = ? remainder ?", "2 پیکٹ 1 لیٹر بناتے ہیں۔ 9 ÷ 2 = ? باقی ?"),
     T("Right! 9 ÷ 2 = 4 remainder 1, so they used 4 1/2 litres.", "درست! 9 ÷ 2 = 4 باقی 1، اس لیے انہوں نے 4 1/2 لیٹر دودھ استعمال کیا۔"),
     T("Every 2 packets make 1 litre. 9 ÷ 2 = 4 remainder 1: 4 whole litres and half a litre, 4 1/2 litres.", "ہر 2 پیکٹ 1 لیٹر بناتے ہیں۔ 9 ÷ 2 = 4 باقی 1: 4 پورے لیٹر اور آدھا لیٹر، یعنی 4 1/2 لیٹر۔"),
     common_wrong=[
       wrong(swapped(MILK), "You swapped them. 9 ÷ 2 = 4 remainder 1: 4 is the whole litres and 1 goes on top.", "آپ نے جگہ بدل دی۔ 9 ÷ 2 = 4 باقی 1: 4 پورے لیٹر ہیں اور 1 اوپر جاتا ہے۔", "swapped_quotient_remainder"),
       wrong(frac(MILK), "The right amount, but please write it as a mixed number: whole litres and a fraction.", "مقدار درست ہے، لیکن اسے مخلوط عدد کی شکل میں لکھیں: پورے لیٹر اور کسر۔"),
     ]),
   {"id": "s13_summary", "type": "summary",
    "character": say("celebrating", "Now you can write the same amount in two ways!", "اب آپ ایک ہی مقدار کو دو طرح لکھ سکتے ہیں!"),
    "text": T("A mixed number (2 1/2) and an improper fraction (5/2) can show the same amount. Mixed to improper: multiply the whole number by the denominator and add the numerator. Improper to mixed: divide; the answer is the whole number and the remainder goes on top.",
              "مخلوط عدد (2 1/2) اور غیر واجب کسر (5/2) ایک ہی مقدار دکھا سکتے ہیں۔ مخلوط سے غیر واجب: پورے عدد کو نسب نما سے ضرب دیں اور شمار کنندہ جمع کریں۔ غیر واجب سے مخلوط: تقسیم کریں؛ جواب پورا عدد ہے اور باقی اوپر جاتا ہے۔"),
    "points": [T("2 1/2 = (2 × 2 + 1)/2 = 5/2", "2 1/2 = (2 × 2 + 1)/2 = 5/2"),
               T("11/4: 11 ÷ 4 = 2 remainder 3, so 11/4 = 2 3/4", "11/4: 11 ÷ 4 = 2 باقی 3، اس لیے 11/4 = 2 3/4"),
               T("An improper fraction is more than 1 (or equal to 1).", "غیر واجب کسر 1 سے زیادہ (یا 1 کے برابر) ہوتی ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_to_improper", "type": "apply", "skill": SKILL, "step": fraction_question(
     "r_to_improper",
     T("Write 1 2/5 as an improper fraction.", "1 2/5 کو غیر واجب کسر کی شکل میں لکھیں۔"),
     frac(to_improper(1, 2, 5)),
     T("1 whole is 5 fifths. Add the 2 fifths.", "1 پورا 5 پانچویں حصے ہے۔ 2 پانچویں حصے جمع کریں۔"),
     T("Right! 1 × 5 + 2 = 7, so 1 2/5 = 7/5.", "درست! 1 × 5 + 2 = 7، اس لیے 1 2/5 = 7/5"),
     T("1 whole = 5/5. Add 2/5: 7/5.", "1 پورا = 5/5۔ 2/5 جمع کریں: 7/5"),
     common_wrong=[wrong(whole_added_to_top(1, 2, 5), "You added 1 to the top. 1 whole is 5 fifths, not 1.", "آپ نے اوپر 1 جمع کیا۔ 1 پورا 5 پانچویں حصے ہے، 1 نہیں۔", "whole_added_to_top")],
     qtype=None)},
   {"id": "r_to_mixed", "type": "apply", "skill": SKILL, "step": fraction_question(
     "r_to_mixed",
     T("Write 10/3 as a mixed number.", "10/3 کو مخلوط عدد کی شکل میں لکھیں۔"),
     mixed(F(10, 3)),
     T("10 ÷ 3 = ? remainder ?", "10 ÷ 3 = ? باقی ?"),
     T("Right! 10 ÷ 3 = 3 remainder 1, so 10/3 = 3 1/3.", "درست! 10 ÷ 3 = 3 باقی 1، اس لیے 10/3 = 3 1/3"),
     T("10 ÷ 3 = 3 remainder 1: 3 wholes and 1 third, 3 1/3.", "10 ÷ 3 = 3 باقی 1: 3 پورے اور 1 تہائی، یعنی 3 1/3"),
     common_wrong=[wrong(swapped(F(10, 3)), "You swapped them: the 3 is the wholes and the remainder 1 goes on top.", "آپ نے جگہ بدل دی: 3 پورے ہیں اور باقی 1 اوپر جاتا ہے۔", "swapped_quotient_remainder")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Fractions unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the file is named g6-maths-02 to sit with the dividing-fractions lesson. Fix the name and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: مخلوط عدد (mixed number), غیر واجب کسر (improper fraction), واجب کسر (proper fraction), باقی (remainder), عددی خط (number line), and ڈھائی (two and a half) in the hook.",
   "The fraction checker accepts any equal value, so it can't insist on a form: where a step asks for a mixed number (s8, s12) or an improper fraction (s6), typing the starting form back is listed in common_wrong with feedback asking for the other form. That costs an attempt.",
   "Steps follow the lesson pattern: foundation check (s2), prediction (s3), concrete with the fraction bars (s4) then symbolic (s5, s6), the other way (s7, s8), number line (s9), find the error (s10), explain (s11), word problem (s12).",
   "The answers and the common wrong answers were worked out with Python's fractions module in content/sources/g6-maths-02/mixed_numbers.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

from common import (T, D, opt, say, wrong, dec, number_question, decimal_line, write,
                    REF, REVIEW, DEC_PLACE_VALUE, DEC_ADD_SUBTRACT)

SKILL = DEC_ADD_SUBTRACT


def misaligned(a, b):
    """The sum you get by lining up the last digits instead of the points:
    1.5 + 0.75 read as 0.15 + 0.75."""
    places = max(-D(a).as_tuple().exponent, -D(b).as_tuple().exponent)
    shift = lambda x: D(str(x).replace(".", "")) / D(10) ** places
    return shift(a) + shift(b)


# s1, s4: potatoes and onions
S4 = D("1.5") + D("0.75")
assert S4 == D("2.25") and misaligned("1.5", "0.75") == D("0.9")
# s2
assert D(75) / 100 == D("0.75")
# s5: 0.8 + 0.6 on the number line
S5 = D("0.8") + D("0.6")
assert S5 == D("1.4")
# s6, s7: 5 − 2.35
S7 = 5 - D("2.35")
assert S7 == D("2.65") and (5 - 2) + D("0.35") == D("3.35")
# s8: 3.6 − 1.25; bringing the 5 down gives 2.45
S8 = D("3.6") - D("1.25")
assert S8 == D("2.35")
assert D("2.45") == (3 - 1) + D("0.4") + D("0.05")
# s9: 4.2 + 1.35, lined up on the right
S9 = D("4.2") + D("1.35")
assert S9 == D("5.55") and misaligned("4.2", "1.35") == D("1.77")
# s11: ribbon
S11 = 2 - D("0.65")
assert S11 == D("1.35")
# question bank and review
QB = D("6.4") + D("2.85")
assert QB == D("9.25") and misaligned("6.4", "2.85") == D("3.49")
R1 = 7 - D("3.4")
assert R1 == D("3.6")
R2 = D("0.45") + D("0.8")
assert R2 == D("1.25") and D("0.45") + D("0.08") == D("0.53")


lesson = {
 "id": "g6-maths-03-adding-and-subtracting-decimals",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Add and subtract decimals by lining up the decimal points.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Adding and subtracting decimals", "اعشاریہ اعداد کی جمع اور تفریق"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": DEC_PLACE_VALUE}],
 "misconceptions": [
   {"id": "right_aligned", "description": "Lines up the last digits instead of the decimal points: 4.2 + 1.35 = 1.77."},
   {"id": "missing_zero", "description": "Does not fill an empty place with 0 when subtracting, and brings a digit straight down: 3.6 − 1.25 = 2.45."},
   {"id": "whole_only", "description": "Subtracts the whole numbers and keeps the decimal part: 5 − 2.35 = 3.35."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_first_step", "type": "recall", "step": {
     "id": "qb_first_step", "type": "choice",
     "prompt": T("What is the first thing to do when adding 6.4 + 2.85?", "6.4 + 2.85 جمع کرتے وقت سب سے پہلے کیا کریں؟"),
     "options": [
       opt("points", "Line up the decimal points, writing 6.4 as 6.40.", "اعشاری نقطے ایک سیدھ میں رکھیں، 6.4 کو 6.40 لکھیں۔", True, "Yes! Then add like whole numbers: 9.25.", "جی ہاں! پھر مکمل اعداد کی طرح جمع کریں: 9.25"),
       opt("right", "Line up the last digits on the right.", "دائیں طرف آخری ہندسے ایک سیدھ میں رکھیں۔", False, "That puts tenths under hundredths. Line up the points instead.", "اس سے دسواں، سوویں کے نیچے آ جاتا ہے۔ اس کے بجائے نقطے ایک سیدھ میں رکھیں۔", "right_aligned"),
       opt("drop", "Take away the points and add 64 + 285.", "نقطے ہٹا کر 64 + 285 جمع کریں۔", False, "64 + 285 mixes up the places. Line up the points.", "64 + 285 سے مقام گڈمڈ ہو جاتے ہیں۔ نقطے ایک سیدھ میں رکھیں۔", "right_aligned"),
     ]}},
   {"id": "qb_add", "type": "apply", "step": number_question(
     "qb_add",
     T("Work out 6.4 + 2.85", "حل کریں: 6.4 + 2.85"),
     QB,
     T("Write 6.40 + 2.85, lining up the points.", "نقطے ایک سیدھ میں رکھ کر 6.40 + 2.85 لکھیں۔"),
     T(f"Right! 6.40 + 2.85 = {dec(QB)}.", f"درست! 6.40 + 2.85 = {dec(QB)}"),
     T(f"6.40 + 2.85: hundredths 0 + 5 = 5, tenths 4 + 8 = 12 (carry 1), ones 6 + 2 + 1 = 9. So {dec(QB)}.", f"6.40 + 2.85: سوواں 0 + 5 = 5، دسواں 4 + 8 = 12 (1 حاصل)، اکائیاں 6 + 2 + 1 = 9۔ اس لیے {dec(QB)}"),
     common_wrong=[wrong(D("3.49"), "You lined up the last digits. Line up the points: 6.40 + 2.85.", "آپ نے آخری ہندسے ایک سیدھ میں رکھے۔ نقطے ایک سیدھ میں رکھیں: 6.40 + 2.85", "right_aligned")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Sana worked out 5 − 2.35 = 3.35. What went wrong?", "ثنا نے 5 − 2.35 = 3.35 حل کیا۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("zeros", "She only took away the 2. Write 5.00 − 2.35 = 2.65.", "اس نے صرف 2 تفریق کیا۔ 5.00 − 2.35 = 2.65 لکھیں۔", True,
           "Yes! The 0.35 must be taken away too.", "جی ہاں! 0.35 بھی تفریق کرنا ہے۔"),
       opt("nothing", "Nothing. 5 − 2 = 3.", "کوئی غلطی نہیں۔ 5 − 2 = 3", False,
           "2.35 is more than 2, so the answer must be less than 3: 2.65.", "2.35، 2 سے زیادہ ہے، اس لیے جواب 3 سے کم ہوگا: 2.65", "whole_only"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_line_up", "front": T("How do you add or subtract decimals?", "اعشاریہ کیسے جمع یا تفریق کرتے ہیں؟"),
    "back": T("Line up the decimal points. Fill empty places with 0. Add or subtract like whole numbers, and put the point in the answer straight below.",
              "اعشاری نقطے ایک سیدھ میں رکھیں۔ خالی مقام پر 0 لکھیں۔ مکمل اعداد کی طرح جمع یا تفریق کریں، اور جواب میں نقطہ سیدھا نیچے لگائیں۔")},
   {"id": "f_subtract", "front": T("5 − 2.35 = ?", "5 − 2.35 = ؟"),
    "back": T("Write 5.00 − 2.35 = 2.65.", "5.00 − 2.35 = 2.65 لکھیں۔")},
 ],
 "home_tasks": [{"id": "h_shopping", "text": T(
   "Ask an adult for the weights of 2 things bought at the market this week (like 1.5 kg potatoes and 0.75 kg onions). Add them. How much more is the heavier one?",
   "کسی بڑے سے اس ہفتے بازار سے خریدی گئی 2 چیزوں کا وزن پوچھیں (جیسے 1.5 کلوگرام آلو اور 0.75 کلوگرام پیاز)۔ انہیں جمع کریں۔ بھاری چیز کتنی زیادہ ہے؟")}],
 "glossary": [T("Sum", "مجموعہ"), T("Difference", "فرق"), T("Line up", "ایک سیدھ میں رکھنا")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Ammi buys 1.5 kg of potatoes and 0.75 kg of onions. How heavy is the bag?",
      "امی 1.5 کلوگرام آلو اور 0.75 کلوگرام پیاز خریدتی ہیں۔ تھیلا کتنا بھاری ہے؟"),
    "text": T("Today we add and subtract decimals. First, a quick check on place value.", "آج ہم اعشاریہ اعداد جمع اور تفریق کریں گے۔ پہلے مقامی قیمت کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Write 75/100 as a decimal.", "75/100 کو اعشاریہ میں لکھیں۔"),
     D("0.75"),
     T("Hundredths: two places after the point.", "سوواں: اعشاریہ کے بعد دو مقام۔"),
     T("Right! 75/100 = 0.75.", "درست! 75/100 = 0.75"),
     T("75 hundredths = 0.75.", "75 سوواں = 0.75"),
     common_wrong=[wrong(D("7.5"), "7.5 is more than 7! 75/100 is less than 1: 0.75.", "7.5 تو 7 سے زیادہ ہے! 75/100 ایک سے کم ہے: 0.75")],
     qtype="recall", skill=DEC_PLACE_VALUE),
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "The golden rule: line up the decimal points!", "سنہری اصول: اعشاری نقطے ایک سیدھ میں رکھیں!"),
    "text": T("Write the numbers one under the other with the points in a straight line. Fill empty places with 0: 1.5 becomes 1.50. Then add like whole numbers and put the point straight below: 1.50 + 0.75 = 2.25. Ones go under ones, tenths under tenths, hundredths under hundredths.",
              "اعداد کو ایک دوسرے کے نیچے اس طرح لکھیں کہ نقطے ایک سیدھی لکیر میں ہوں۔ خالی مقام پر 0 لکھیں: 1.5 کو 1.50 لکھیں۔ پھر مکمل اعداد کی طرح جمع کریں اور نقطہ سیدھا نیچے لگائیں: 1.50 + 0.75 = 2.25۔ اکائیاں اکائیوں کے نیچے، دسواں دسویں کے نیچے، سوواں سوویں کے نیچے۔")},
   number_question(
     "s4_bag",
     T("Work out 1.5 + 0.75 to find the weight of Ammi's bag in kg.", "امی کے تھیلے کا وزن کلوگرام میں معلوم کرنے کے لیے 1.5 + 0.75 حل کریں۔"),
     S4,
     T("Write 1.50 + 0.75.", "1.50 + 0.75 لکھیں۔"),
     T(f"Right! {dec(S4)} kg.", f"درست! {dec(S4)} کلوگرام۔"),
     T(f"1.50 + 0.75: 0 + 5 = 5, 5 + 7 = 12 (carry 1), 1 + 0 + 1 = 2. So {dec(S4)}.", f"1.50 + 0.75: 0 + 5 = 5، 5 + 7 = 12 (1 حاصل)، 1 + 0 + 1 = 2۔ اس لیے {dec(S4)}"),
     common_wrong=[wrong(D("0.9"), "You lined up the last digits. Line up the points: 1.50 + 0.75.", "آپ نے آخری ہندسے ایک سیدھ میں رکھے۔ نقطے ایک سیدھ میں رکھیں: 1.50 + 0.75", "right_aligned")]),
   decimal_line(
     "s5_jump",
     T("The marker is on 0.8. Move it to show 0.8 + 0.6. Press Check.", "نشان 0.8 پر ہے۔ اسے ہلا کر 0.8 + 0.6 دکھائیں۔ \"جانچیں\" دبائیں۔"),
     S5,
     T("0.6 is 6 jumps of 0.1 to the right.", "0.6 یعنی دائیں طرف 0.1 کی 6 چھلانگیں۔"),
     T("Yes! 0.8 + 0.6 = 1.4. You crossed 1!", "جی ہاں! 0.8 + 0.6 = 1.4۔ آپ 1 سے آگے نکل گئے!"),
     T("From 0.8: 0.9, 1, 1.1, 1.2, 1.3, 1.4.", "0.8 سے: 0.9، 1، 1.1، 1.2، 1.3، 1.4"),
     hi="2", start="0.8",
     common_wrong=[wrong("1.2", "Count 6 jumps of 0.1 from 0.8: you land on 1.4.", "0.8 سے 0.1 کی 6 چھلانگیں گنیں: آپ 1.4 پر پہنچتے ہیں۔")]),
   {"id": "s6_subtract", "type": "explain",
    "character": say("thinking", "Subtracting works the same way. Don't forget the zeros!", "تفریق بھی اسی طرح ہوتی ہے۔ صفر نہ بھولیں!"),
    "text": T("For 5 − 2.35, write 5 as 5.00 so both numbers have hundredths. Then subtract like whole numbers, borrowing when you need to: 5.00 − 2.35 = 2.65. Check: 2.65 + 2.35 = 5.",
              "5 − 2.35 کے لیے 5 کو 5.00 لکھیں تاکہ دونوں میں سوواں ہو۔ پھر مکمل اعداد کی طرح تفریق کریں، ضرورت ہو تو ادھار لیں: 5.00 − 2.35 = 2.65۔ جانچ: 2.65 + 2.35 = 5")},
   number_question(
     "s7_whole_minus",
     T("Work out 5 − 2.35", "حل کریں: 5 − 2.35"),
     S7,
     T("Write 5.00 − 2.35.", "5.00 − 2.35 لکھیں۔"),
     T(f"Right! 5 − 2.35 = {dec(S7)}.", f"درست! 5 − 2.35 = {dec(S7)}"),
     T(f"5.00 − 2.35 = {dec(S7)}. Check: {dec(S7)} + 2.35 = 5.", f"5.00 − 2.35 = {dec(S7)}۔ جانچ: {dec(S7)} + 2.35 = 5"),
     common_wrong=[wrong(D("3.35"), "You took away 2 but not the 0.35. Write 5.00 − 2.35.", "آپ نے 2 تفریق کیا مگر 0.35 نہیں۔ 5.00 − 2.35 لکھیں۔", "whole_only")]),
   number_question(
     "s8_fill_zero",
     T("Work out 3.6 − 1.25", "حل کریں: 3.6 − 1.25"),
     S8,
     T("Write 3.6 as 3.60 first.", "پہلے 3.6 کو 3.60 لکھیں۔"),
     T(f"Right! 3.60 − 1.25 = {dec(S8)}.", f"درست! 3.60 − 1.25 = {dec(S8)}"),
     T(f"3.60 − 1.25: borrow for the hundredths, 10 − 5 = 5; tenths 5 − 2 = 3; ones 3 − 1 = 2. So {dec(S8)}.", f"3.60 − 1.25: سوویں کے لیے ادھار لیں، 10 − 5 = 5؛ دسواں 5 − 2 = 3؛ اکائیاں 3 − 1 = 2۔ اس لیے {dec(S8)}"),
     common_wrong=[wrong(D("2.45"), "You brought the 5 straight down. 3.6 = 3.60, so it is 0 − 5 in the hundredths: borrow.", "آپ نے 5 سیدھا نیچے لکھ دیا۔ 3.6 = 3.60، اس لیے سوویں میں 0 − 5 ہے: ادھار لیں۔", "missing_zero")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Usman wrote 4.2 + 1.35 = 1.77. What went wrong?", "عثمان نے لکھا 4.2 + 1.35 = 1.77۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("align", "He lined up the last digits. With the points lined up: 4.20 + 1.35 = 5.55.", "اس نے آخری ہندسے ایک سیدھ میں رکھے۔ نقطے سیدھ میں رکھیں: 4.20 + 1.35 = 5.55", True,
          "Yes! Also, the answer must be more than 4.2, so 1.77 can't be right.", "جی ہاں! یہ بھی دیکھیں، جواب 4.2 سے زیادہ ہونا چاہیے، اس لیے 1.77 درست نہیں ہو سکتا۔"),
      opt("carry", "He forgot to carry.", "وہ حاصل بھول گیا۔", False,
          "There is nothing to carry here. The problem is the lining up: 4.20 + 1.35 = 5.55.", "یہاں کوئی حاصل نہیں۔ مسئلہ سیدھ کا ہے: 4.20 + 1.35 = 5.55", "right_aligned"),
      opt("nothing", "Nothing. 42 + 135 = 177.", "کوئی غلطی نہیں۔ 42 + 135 = 177", False,
          "4.2 is 4 and 2 tenths, not 42. Line up the points: 5.55.", "4.2 یعنی 4 اور 2 دسواں، 42 نہیں۔ نقطے سیدھ میں رکھیں: 5.55", "right_aligned"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we have to line up the decimal points? Can't we just line up the numbers on the right?",
                     "ہمیں اعشاری نقطے ایک سیدھ میں کیوں رکھنے پڑتے ہیں؟ کیا ہم صرف دائیں طرف سے اعداد سیدھ میں نہیں رکھ سکتے؟"),
    "task": T("In your own words: why must we line up the decimal points when adding 4.2 + 1.35?",
              "اپنے الفاظ میں بتائیں: 4.2 + 1.35 جمع کرتے وقت اعشاری نقطے ایک سیدھ میں رکھنا کیوں ضروری ہے؟"),
    "key_idea": "So that we add the same kinds of parts: ones with ones, tenths with tenths, hundredths with hundredths. Lining up on the right would add the 2 tenths to the 5 hundredths, which is wrong.",
    "levels": {
      "got_it": "Explains that lining up the points puts ones under ones, tenths under tenths and hundredths under hundredths, so like places are added.",
      "partly": "Says the points must be lined up or the answer is wrong, but does not mention places.",
      "not_yet": "Says it doesn't matter, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["tenths", "hundredths", "دسواں", "سوواں", "daswan", "sauwan"],
      ["place", "same", "مقام", "ایک جیسے", "muqam"],
      ["ones", "اکائی", "ikai"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Lining up the points puts tenths under tenths and hundredths under hundredths, so we add the same kinds of parts.",
                  "بہت خوب سمجھایا! نقطے سیدھ میں رکھنے سے دسواں دسویں کے نیچے اور سوواں سوویں کے نیچے آتا ہے، اس لیے ایک جیسے حصے جمع ہوتے ہیں۔"),
      "partly": T("Good start! Now say which places go under each other when the points are lined up.", "اچھی شروعات! اب بتائیں کہ نقطے سیدھ میں ہوں تو کون سے مقام ایک دوسرے کے نیچے آتے ہیں۔"),
      "not_yet": T("Think: in 4.2 the 2 is tenths, in 1.35 the 5 is hundredths. Should tenths be added to hundredths?",
                   "سوچیں: 4.2 میں 2 دسواں ہے، 1.35 میں 5 سوواں ہے۔ کیا دسواں، سوویں میں جمع ہونا چاہیے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_ribbon",
     T("Ayesha has a ribbon 2 m long. She cuts off 0.65 m for a gift. How many metres are left?", "عائشہ کے پاس 2 میٹر لمبا فیتہ ہے۔ وہ تحفے کے لیے 0.65 میٹر کاٹ لیتی ہے۔ کتنے میٹر باقی ہیں؟"),
     S11,
     T("Write 2.00 − 0.65.", "2.00 − 0.65 لکھیں۔"),
     T(f"Right! 2.00 − 0.65 = {dec(S11)} m.", f"درست! 2.00 − 0.65 = {dec(S11)} میٹر۔"),
     T(f"2.00 − 0.65 = {dec(S11)}. Check: {dec(S11)} + 0.65 = 2.", f"2.00 − 0.65 = {dec(S11)}۔ جانچ: {dec(S11)} + 0.65 = 2"),
     common_wrong=[wrong(D("2.65"), "Cutting off makes it shorter: subtract, 2.00 − 0.65.", "کاٹنے سے فیتہ چھوٹا ہوتا ہے: تفریق کریں، 2.00 − 0.65"),
                   wrong(D("1.45"), "Check the borrowing: 2.00 − 0.65 = 1.35. Check by adding back.", "ادھار دوبارہ دیکھیں: 2.00 − 0.65 = 1.35۔ واپس جمع کر کے جانچیں۔", "missing_zero")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Line up the points, and decimals are easy!", "نقطے سیدھ میں رکھیں، اور اعشاریہ آسان ہے!"),
    "text": T("To add or subtract decimals: line up the decimal points, fill empty places with zeros, then add or subtract like whole numbers and put the point straight below. 1.50 + 0.75 = 2.25 and 5.00 − 2.35 = 2.65. Check that the answer makes sense.",
              "اعشاریہ جمع یا تفریق کرنے کے لیے: اعشاری نقطے سیدھ میں رکھیں، خالی مقام پر صفر لکھیں، پھر مکمل اعداد کی طرح جمع یا تفریق کریں اور نقطہ سیدھا نیچے لگائیں۔ 1.50 + 0.75 = 2.25 اور 5.00 − 2.35 = 2.65۔ دیکھیں کہ جواب سمجھ میں آتا ہے۔"),
    "points": [T("4.2 + 1.35 = 5.55, not 1.77.", "4.2 + 1.35 = 5.55، نہ کہ 1.77"),
               T("Check a subtraction by adding back.", "تفریق کو واپس جمع کر کے جانچیں۔")]},
 ],
 "review_questions": [
   {"id": "r_subtract", "type": "apply", "skill": SKILL, "step": number_question(
     "r_subtract",
     T("Work out 7 − 3.4", "حل کریں: 7 − 3.4"),
     R1,
     T("Write 7.0 − 3.4.", "7.0 − 3.4 لکھیں۔"),
     T(f"Right! 7.0 − 3.4 = {dec(R1)}.", f"درست! 7.0 − 3.4 = {dec(R1)}"),
     T(f"7.0 − 3.4: borrow, 10 − 4 = 6 tenths; 6 − 3 = 3 ones. So {dec(R1)}.", f"7.0 − 3.4: ادھار لیں، 10 − 4 = 6 دسواں؛ 6 − 3 = 3 اکائیاں۔ اس لیے {dec(R1)}"),
     common_wrong=[wrong(D("4.4"), "You took away 3 but not the 0.4. Write 7.0 − 3.4.", "آپ نے 3 تفریق کیا مگر 0.4 نہیں۔ 7.0 − 3.4 لکھیں۔", "whole_only")],
     qtype=None)},
   {"id": "r_add", "type": "apply", "skill": SKILL, "step": number_question(
     "r_add",
     T("Work out 0.45 + 0.8", "حل کریں: 0.45 + 0.8"),
     R2,
     T("Write 0.45 + 0.80.", "0.45 + 0.80 لکھیں۔"),
     T(f"Right! 0.45 + 0.80 = {dec(R2)}.", f"درست! 0.45 + 0.80 = {dec(R2)}"),
     T(f"0.45 + 0.80: 5 + 0 = 5, 4 + 8 = 12 (carry 1), so {dec(R2)}.", f"0.45 + 0.80: 5 + 0 = 5، 4 + 8 = 12 (1 حاصل)، اس لیے {dec(R2)}"),
     common_wrong=[wrong(D("0.53"), "The 8 is 8 tenths, not 8 hundredths. Write 0.80.", "8 آٹھ دسواں ہے، آٹھ سوواں نہیں۔ 0.80 لکھیں۔", "right_aligned")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Decimals unit. No textbook text or exercises were used. Weights and lengths are made up for the sums.",
   "The common errors are worked out in the script: lining up on the right (4.2 + 1.35 = 1.77) and bringing a digit down without a zero (3.6 − 1.25 = 2.45).",
   "Urdu terms to check: حاصل (carry), ادھار (borrow) in column subtraction.",
   "The numbers were worked out in content/sources/g6-maths-03/adding_subtracting_decimals.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

from common import (T, opt, say, wrong, signed, number_question, number_line, write,
                    REF, REVIEW, INT_MEANING)
from figs import (NumberLine, number_line_figure, jumps_figure, two_thermometers, with_figure,
                  arrow_h, attach, LABEL_DY)

SKILL = INT_MEANING

# Murree −3 °C, Lahore 12 °C (s1).
MURREE, LAHORE = -3, 12
assert MURREE < 0 < LAHORE

# s5, s6, s9: compare negatives.
assert -2 > -7 and -3 > -8

# s7: order −5, 3, 0, −1.
ORDER = sorted([-5, 3, 0, -1])
assert ORDER == [-5, -1, 0, 3]

# s8: the opposite of 6.
assert -6 + 6 == 0


# ---------- pictures ----------

def deg(n):
    return f"{signed(n)}°C"


# s1: Lahore 12 °C and Murree −3 °C on two thermometers.
FIG_S1, _ = two_thermometers(
    -5, 15, LAHORE, MURREE,
    f"Two thermometers. The left one (Lahore) shows {LAHORE} °C, well above 0. The right one (Murree) shows {signed(MURREE)} °C: its liquid is 3 marks below 0.",
    f"دو تھرمامیٹر۔ بائیں والا (لاہور) {LAHORE} ڈگری دکھاتا ہے، 0 سے کافی اوپر۔ دائیں والا (مری) {signed(MURREE)} ڈگری دکھاتا ہے: اس کا مائع 0 سے 3 نشان نیچے ہے۔",
    under=(deg(LAHORE), deg(MURREE)))

# s3: from 0, three steps to the left land on −3.
FIG_S3 = jumps_figure(
    -5, 5, [0, -1, -1, MURREE + 2], text_of=lambda s: None,
    alt_en=f"A number line from −5 to 5. Three small jumps go left from 0 to −1, −2 and {signed(MURREE)}, where there is a dot. Negative numbers are on the left of 0, positive numbers on the right.",
    alt_ur=f"−5 سے 5 تک عددی خط۔ تین چھوٹی چھلانگیں 0 سے بائیں −1، −2 اور {signed(MURREE)} تک جاتی ہیں، جہاں ایک نقطہ ہے۔ منفی اعداد 0 کے بائیں، مثبت اعداد دائیں طرف ہیں۔")


def compare_line(lo, hi, a, b, alt_en, alt_ur):
    """Dots on a and b, and an arrow above pointing right: greater this way."""
    nl = NumberLine(lo, hi, 44, keys=(a, b))
    nl.mark(a)
    nl.mark(b)
    nl.items += arrow_h(16, nl.x(lo), nl.x(hi))
    return number_line_figure(alt_en, alt_ur, [nl], 44 + LABEL_DY + 14)


# s6: −2 is right of −7.
FIG_S6 = compare_line(
    -8, 2, -7, -2,
    "A number line from −8 to 2 with dots on −7 and −2. An arrow above points right: numbers get greater that way, so −2 is greater than −7.",
    "−8 سے 2 تک عددی خط جس پر −7 اور −2 پر نقطے ہیں۔ اوپر ایک تیر دائیں طرف اشارہ کرتا ہے: اس طرف اعداد بڑے ہوتے ہیں، اس لیے −2، −7 سے بڑا ہے۔")


def opposites(n, hidden, alt_en, alt_ur):
    nl = NumberLine(-n - 1, n + 1, 44, keys=(n, -n), hide=(-n,) if hidden else ())
    nl.mark(n)
    nl.mark(-n, "?" if hidden else None)
    nl.bracket(0, n, str(n))
    nl.bracket(-n, 0, str(n))
    return number_line_figure(alt_en, alt_ur, [nl], 44 + LABEL_DY + 14)


# s8: 6 is 6 steps right of 0; the same distance on the left is "?".
FIG_S8 = opposites(
    6, True,
    "A number line from −7 to 7. A dot on 6, with a measuring line from 0 to 6 marked 6. A second measuring line, also marked 6, goes the same distance to the left of 0, to a dot marked with a question mark.",
    "−7 سے 7 تک عددی خط۔ 6 پر ایک نقطہ، اور 0 سے 6 تک ایک ناپ کی لکیر جس پر 6 لکھا ہے۔ دوسری ناپ کی لکیر، اس پر بھی 6 لکھا ہے، 0 کے بائیں اتنا ہی فاصلہ جاتی ہے، ایک نقطے تک جس پر سوالیہ نشان ہے۔")

# s9: −8 and −3.
FIG_S9 = compare_line(
    -9, 1, -8, -3,
    "A number line from −9 to 1 with dots on −8 and −3. An arrow above points right, the way numbers get greater. −8 is further left than −3.",
    "−9 سے 1 تک عددی خط جس پر −8 اور −3 پر نقطے ہیں۔ اوپر ایک تیر دائیں طرف اشارہ کرتا ہے، جدھر اعداد بڑے ہوتے ہیں۔ −8، −3 سے زیادہ بائیں ہے۔")

# s10: −7 °C and −2 °C on two thermometers.
FIG_S10, _ = two_thermometers(
    -10, 5, -7, -2,
    "Two thermometers, both below 0. The left one shows −7 °C, with its liquid lower down. The right one shows −2 °C, higher up and warmer.",
    "دو تھرمامیٹر، دونوں 0 سے نیچے۔ بائیں والا −7 ڈگری دکھاتا ہے، اس کا مائع زیادہ نیچے ہے۔ دائیں والا −2 ڈگری دکھاتا ہے، اوپر اور زیادہ گرم۔",
    under=(deg(-7), deg(-2)))

# s12: the opposites 6 and −6.
FIG_S12 = opposites(
    6, False,
    "A number line from −7 to 7 with dots on −6 and 6. Two measuring lines, each marked 6, show that both are 6 steps from 0, one on each side.",
    "−7 سے 7 تک عددی خط جس پر −6 اور 6 پر نقطے ہیں۔ دو ناپ کی لکیریں، ہر ایک پر 6 لکھا ہے، دکھاتی ہیں کہ دونوں 0 سے 6 قدم دور ہیں، ایک ایک طرف۔")

# qb_find_error: −9 and −1.
FIG_QB_ERROR = compare_line(
    -10, 0, -9, -1,
    "A number line from −10 to 0 with dots on −9 and −1. An arrow above points right, the way numbers get greater. −1 is to the right of −9.",
    "−10 سے 0 تک عددی خط جس پر −9 اور −1 پر نقطے ہیں۔ اوپر ایک تیر دائیں طرف اشارہ کرتا ہے، جدھر اعداد بڑے ہوتے ہیں۔ −1، −9 کے دائیں طرف ہے۔")

lesson = {
 "id": "g6-maths-04-what-are-integers",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Know integers as whole numbers and their negatives, show them on a number line, and compare and order them.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("What are integers?", "صحیح اعداد کیا ہیں؟"),
 "estimated_minutes": 12,
 "prerequisites": [],
 "misconceptions": [
   {"id": "bigger_digit_bigger", "description": "Thinks −7 is greater than −2 because 7 is greater than 2."},
   {"id": "sign_ignored", "description": "Ignores the minus sign, putting −4 where 4 goes on the number line."},
   {"id": "zero_not_integer", "description": "Thinks zero is not an integer, or that it is negative."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_less_than_zero", "type": "recall", "step": {
     "id": "qb_less_than_zero", "type": "choice",
     "prompt": T("Which of these numbers is less than zero?", "ان میں سے کون سا عدد صفر سے کم ہے؟"),
     "options": [
       opt("neg", signed(-4), signed(-4), True, "Yes! −4 is a negative integer: it is 4 to the left of 0.", "جی ہاں! −4 منفی صحیح عدد ہے: یہ 0 سے 4 بائیں طرف ہے۔"),
       opt("zero", "0", "0", False, "0 is neither positive nor negative. It is the middle of the number line.", "0 نہ مثبت ہے نہ منفی۔ یہ عددی خط کا درمیان ہے۔", "zero_not_integer"),
       opt("pos", "4", "4", False, "4 is positive: it is to the right of 0.", "4 مثبت ہے: یہ 0 کے دائیں طرف ہے۔", "sign_ignored"),
     ]}},
   {"id": "qb_place", "type": "apply", "step": number_line(
     "qb_place",
     T("Put the marker on −7. Press Check.", "نشان کو −7 پر رکھیں۔ \"جانچیں\" دبائیں۔"),
     -7,
     T("Negative numbers are to the LEFT of 0.", "منفی اعداد 0 کے بائیں طرف ہیں۔"),
     T("Yes! −7 is 7 steps to the left of 0.", "جی ہاں! −7، 0 سے 7 قدم بائیں طرف ہے۔"),
     T("Start at 0 and count 7 steps to the left: that is −7.", "0 سے شروع کریں اور 7 قدم بائیں گنیں: یہ −7 ہے۔"),
     common_wrong=[wrong("7", "That is 7, to the right. −7 is the same distance to the LEFT of 0.", "یہ 7 ہے، دائیں طرف۔ −7 اتنا ہی فاصلہ 0 کے بائیں طرف ہے۔", "sign_ignored")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Ahmad says −9 is greater than −1, because 9 is greater than 1. Is he right?", "احمد کہتا ہے −9، −1 سے بڑا ہے، کیونکہ 9، 1 سے بڑا ہے۔ کیا وہ درست ہے؟"),
     "options": [
       opt("no", "No. −1 is to the right of −9, so −1 is greater.", "نہیں۔ −1، −9 کے دائیں طرف ہے، اس لیے −1 بڑا ہے۔", True,
           "Right! Owing Rs 1 is better than owing Rs 9: −1 > −9.", "درست! 1 روپیہ ادھار، 9 روپے ادھار سے بہتر ہے: −1 > −9"),
       opt("yes", "Yes. 9 is a bigger number.", "ہاں۔ 9 بڑا عدد ہے۔", False,
           "For negatives it flips: the further left, the smaller. −9 < −1.", "منفی اعداد میں الٹ ہو جاتا ہے: جتنا بائیں، اتنا چھوٹا۔ −9 < −1", "bigger_digit_bigger"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_integers", "front": T("What are integers?", "صحیح اعداد کیا ہیں؟"),
    "back": T("The whole numbers, their negatives and zero: … −3, −2, −1, 0, 1, 2, 3 …", "مکمل اعداد، ان کے منفی، اور صفر: … −3، −2، −1، 0، 1، 2، 3 …")},
   {"id": "f_compare", "front": T("Which is greater, −2 or −7?", "کون سا بڑا ہے، −2 یا −7؟"),
    "back": T("−2. On the number line, the number further right is greater. −2 °C is warmer than −7 °C.", "−2۔ عددی خط پر جو عدد زیادہ دائیں ہو وہ بڑا ہے۔ −2 ڈگری، −7 ڈگری سے زیادہ گرم ہے۔")},
 ],
 "home_tasks": [{"id": "h_weather", "text": T(
   "Watch or listen to the weather news, or ask an adult: what is the coldest city in Pakistan today? Is its temperature above or below zero? Write it as an integer.",
   "موسم کی خبریں دیکھیں یا سنیں، یا کسی بڑے سے پوچھیں: آج پاکستان کا سب سے ٹھنڈا شہر کون سا ہے؟ اس کا درجہ حرارت صفر سے اوپر ہے یا نیچے؟ اسے صحیح عدد کی شکل میں لکھیں۔")}],
 "glossary": [T("Integer", "صحیح عدد"), T("Negative", "منفی"), T("Positive", "مثبت"), T("Number line", "عددی خط"), T("Opposite", "مخالف عدد")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "On a winter night it is 12 °C in Lahore, but in Murree it is 3 degrees BELOW zero. How do we write that?",
      "سردیوں کی ایک رات لاہور میں 12 ڈگری ہے، مگر مری میں صفر سے 3 ڈگری نیچے۔ ہم اسے کیسے لکھیں؟"),
    "text": T("Some numbers are less than zero! Today we meet them. First, a quick check.",
              "کچھ اعداد صفر سے بھی کم ہوتے ہیں! آج ہم ان سے ملیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall",
    "prompt": T("On a number line, where is 8 compared with 3?", "عددی خط پر 8، 3 کے مقابلے میں کہاں ہے؟"),
    "options": [
      opt("right", "To the right, because 8 is greater", "دائیں طرف، کیونکہ 8 بڑا ہے", True,
          "Yes! Numbers get bigger as you go right.", "جی ہاں! دائیں جاتے ہوئے اعداد بڑے ہوتے جاتے ہیں۔"),
      opt("left", "To the left", "بائیں طرف", False,
          "Bigger numbers are further right: 3, 4, 5, 6, 7, 8.", "بڑے اعداد زیادہ دائیں ہوتے ہیں: 3، 4، 5، 6، 7، 8۔"),
    ]},
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "The number line keeps going, to the left of zero too!", "عددی خط صفر کے بائیں طرف بھی چلتا رہتا ہے!"),
    "text": T("Murree's temperature is −3 °C (\"minus three\" or \"negative three\"): 3 steps to the LEFT of 0. Numbers less than 0 are negative; numbers greater than 0 are positive; 0 is neither. The whole numbers, their negatives and 0 are called integers: … −3, −2, −1, 0, 1, 2, 3 … We use them for cold weather, depths below sea level and money owed.",
              "مری کا درجہ حرارت −3 ڈگری ہے (\"منفی تین\"): 0 سے 3 قدم بائیں طرف۔ 0 سے کم اعداد منفی ہیں؛ 0 سے بڑے اعداد مثبت ہیں؛ 0 نہ مثبت ہے نہ منفی۔ مکمل اعداد، ان کے منفی اور 0 مل کر صحیح اعداد کہلاتے ہیں: … −3، −2، −1، 0، 1، 2، 3 … یہ ٹھنڈے موسم، سطح سمندر سے نیچے گہرائی اور ادھار کے لیے استعمال ہوتے ہیں۔")},
   number_line(
     "s4_place",
     T("Put the marker on −4. Press Check.", "نشان کو −4 پر رکھیں۔ \"جانچیں\" دبائیں۔"),
     -4,
     T("Start at 0 and go 4 steps to the left.", "0 سے شروع کریں اور 4 قدم بائیں جائیں۔"),
     T("Yes! −4 is 4 steps to the left of 0.", "جی ہاں! −4، 0 سے 4 قدم بائیں طرف ہے۔"),
     T("−4 is 4 steps to the LEFT of 0.", "−4، 0 سے 4 قدم بائیں طرف ہے۔"),
     common_wrong=[wrong("4", "That is 4, to the right of 0. The minus sign means go LEFT.", "یہ 4 ہے، 0 کے دائیں طرف۔ منفی کی علامت کا مطلب ہے بائیں جائیں۔", "sign_ignored")]),
   {"id": "s5_compare", "type": "choice", "question_type": "apply",
    "prompt": T("Skardu is −7 °C and Murree is −2 °C. Which number is greater?", "سکردو میں −7 ڈگری اور مری میں −2 ڈگری ہے۔ کون سا عدد بڑا ہے؟"),
    "options": [
      opt("m2", signed(-2), signed(-2), True, "Yes! −2 is to the right of −7, and Murree is warmer.", "جی ہاں! −2، −7 کے دائیں طرف ہے، اور مری زیادہ گرم ہے۔"),
      opt("m7", signed(-7), signed(-7), False, "−7 is colder, so it is smaller. It is further left on the number line.", "−7 زیادہ ٹھنڈا ہے، اس لیے چھوٹا ہے۔ یہ عددی خط پر زیادہ بائیں ہے۔", "bigger_digit_bigger"),
    ]},
   {"id": "s6_compare_rule", "type": "explain",
    "character": say("thinking", "Further right means greater, even for negative numbers!", "زیادہ دائیں کا مطلب بڑا، منفی اعداد کے لیے بھی!"),
    "text": T("On the number line, the number further to the right is always greater. −2 is to the right of −7, so −2 > −7. Think of temperature: −2 °C is warmer than −7 °C. Every positive number is greater than 0, and 0 is greater than every negative number.",
              "عددی خط پر جو عدد زیادہ دائیں ہو وہ ہمیشہ بڑا ہوتا ہے۔ −2، −7 کے دائیں طرف ہے، اس لیے −2 > −7۔ درجہ حرارت کا سوچیں: −2 ڈگری، −7 ڈگری سے زیادہ گرم ہے۔ ہر مثبت عدد 0 سے بڑا ہے، اور 0 ہر منفی عدد سے بڑا ہے۔")},
   {"id": "s7_order", "type": "choice", "question_type": "apply",
    "prompt": T("Put these in order from smallest to greatest: −5, 3, 0, −1", "انہیں چھوٹے سے بڑے کی ترتیب میں رکھیں: −5، 3، 0، −1"),
    "options": [
      opt("right", "−5, −1, 0, 3", "−5، −1، 0، 3", True, "Yes! From left to right on the number line.", "جی ہاں! عددی خط پر بائیں سے دائیں۔"),
      opt("digits", "−1, −5, 0, 3", "−1، −5، 0، 3", False, "−5 is further left than −1, so −5 comes first.", "−5، −1 سے زیادہ بائیں ہے، اس لیے −5 پہلے آئے گا۔", "bigger_digit_bigger"),
      opt("zero", "0, −1, 3, −5", "0، −1، 3، −5", False, "Negative numbers are smaller than 0, so they come before it.", "منفی اعداد 0 سے چھوٹے ہیں، اس لیے یہ اس سے پہلے آئیں گے۔", "zero_not_integer"),
    ]},
   number_question(
     "s8_opposite",
     T("Every integer has an opposite, the same distance from 0 on the other side. What is the opposite of 6? Type it with a minus sign.", "ہر صحیح عدد کا ایک مخالف ہوتا ہے، جو دوسری طرف 0 سے اتنے ہی فاصلے پر ہو۔ 6 کا مخالف کیا ہے؟ منفی کی علامت کے ساتھ لکھیں۔"),
     -6,
     T("6 is 6 steps right of 0. Go 6 steps left instead.", "6، 0 سے 6 قدم دائیں ہے۔ اس کے بجائے 6 قدم بائیں جائیں۔"),
     T("Right! The opposite of 6 is −6.", "درست! 6 کا مخالف −6 ہے۔"),
     T("6 steps right of 0 is 6; 6 steps left is −6. So the opposite of 6 is −6.", "0 سے 6 قدم دائیں 6 ہے؛ 6 قدم بائیں −6۔ اس لیے 6 کا مخالف −6 ہے۔"),
     common_wrong=[wrong(6, "Add a minus sign: the opposite of 6 is on the other side of 0.", "منفی کی علامت لگائیں: 6 کا مخالف 0 کی دوسری طرف ہے۔", "sign_ignored")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal says −8 is greater than −3, because 8 is more than 3. What went wrong?", "بلال کہتا ہے −8، −3 سے بڑا ہے، کیونکہ 8، 3 سے زیادہ ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("flip", "With negatives, the bigger digit is further left, so −8 is smaller: −8 < −3.", "منفی اعداد میں بڑا ہندسہ زیادہ بائیں ہوتا ہے، اس لیے −8 چھوٹا ہے: −8 < −3", True,
          "Yes! −8 °C is colder than −3 °C.", "جی ہاں! −8 ڈگری، −3 ڈگری سے زیادہ ٹھنڈا ہے۔"),
      opt("nothing", "Nothing. 8 is more than 3.", "کوئی غلطی نہیں۔ 8، 3 سے زیادہ ہے۔", False,
          "That is true for 8 and 3, but −8 is further left than −3, so it is smaller.", "یہ 8 اور 3 کے لیے درست ہے، لیکن −8، −3 سے زیادہ بائیں ہے، اس لیے چھوٹا ہے۔", "bigger_digit_bigger"),
      opt("equal", "They are equal, because both are negative.", "یہ برابر ہیں، کیونکہ دونوں منفی ہیں۔", False,
          "They are at different places on the number line, so they are not equal.", "یہ عددی خط پر مختلف جگہوں پر ہیں، اس لیے برابر نہیں۔"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? 7 is bigger than 2, so why is −7 smaller than −2?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ 7، 2 سے بڑا ہے، تو −7، −2 سے چھوٹا کیوں ہے؟"),
    "task": T("In your own words: why is −7 smaller than −2? You can use a number line or the weather.",
              "اپنے الفاظ میں بتائیں: −7، −2 سے چھوٹا کیوں ہے؟ آپ عددی خط یا موسم کی مثال دے سکتے ہیں۔"),
    "key_idea": "−7 is further to the left of 0 than −2 on the number line, and numbers get smaller as you go left. −7 °C is colder than −2 °C.",
    "levels": {
      "got_it": "Says −7 is further left (further below zero) than −2 on the number line, so it is smaller; or uses temperature: −7 °C is colder.",
      "partly": "Says −7 is smaller or mentions left or cold, but does not explain why the bigger digit makes it smaller.",
      "not_yet": "Says −7 is bigger, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["left", "below", "further", "بائیں", "نیچے", "dur", "baen", "baayen", "neeche"],
      ["cold", "colder", "ٹھنڈ", "سرد", "thand", "sard"],
      ["number line", "zero", "عددی خط", "صفر", "sifar"]],
    "fallback_feedback": {
      "got_it": T("Well explained! −7 is further left of zero, so it is smaller, like −7 °C is colder than −2 °C.",
                  "بہت خوب سمجھایا! −7 صفر سے زیادہ بائیں ہے، اس لیے چھوٹا ہے، جیسے −7 ڈگری، −2 ڈگری سے زیادہ ٹھنڈا ہے۔"),
      "partly": T("Good start! Now say where −7 and −2 are on the number line.", "اچھی شروعات! اب بتائیں کہ −7 اور −2 عددی خط پر کہاں ہیں۔"),
      "not_yet": T("Think: which is colder, −7 °C or −2 °C? Is colder a bigger or a smaller temperature?",
                   "سوچیں: کون زیادہ ٹھنڈا ہے، −7 ڈگری یا −2 ڈگری؟ زیادہ ٹھنڈا بڑا درجہ حرارت ہے یا چھوٹا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_line(
     "s11_diver",
     T("A diver is 6 m below sea level. Sea level is 0. Show where she is on the number line.", "ایک غوطہ خور سطح سمندر سے 6 میٹر نیچے ہے۔ سطح سمندر 0 ہے۔ عددی خط پر دکھائیں کہ وہ کہاں ہے۔"),
     -6,
     T("Below sea level means a negative number.", "سطح سمندر سے نیچے کا مطلب منفی عدد ہے۔"),
     T("Yes! 6 m below sea level is −6.", "جی ہاں! سطح سمندر سے 6 میٹر نیچے −6 ہے۔"),
     T("Below 0 is negative: 6 m below is −6, 6 steps left of 0.", "0 سے نیچے منفی ہے: 6 میٹر نیچے −6 ہے، 0 سے 6 قدم بائیں۔"),
     common_wrong=[wrong("6", "6 would be 6 m ABOVE the sea. She is below: −6.", "6 کا مطلب سمندر سے 6 میٹر اوپر ہوتا۔ وہ نیچے ہے: −6", "sign_ignored")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you know numbers below zero!", "اب آپ صفر سے نیچے کے اعداد جانتے ہیں!"),
    "text": T("Integers are … −3, −2, −1, 0, 1, 2, 3 … Negative numbers are to the left of 0, positive numbers to the right. The number further right is greater, so −2 > −7. Every integer has an opposite: 6 and −6.",
              "صحیح اعداد … −3، −2، −1، 0، 1، 2، 3 … ہیں۔ منفی اعداد 0 کے بائیں، مثبت دائیں طرف ہیں۔ جو عدد زیادہ دائیں ہو وہ بڑا ہے، اس لیے −2 > −7۔ ہر صحیح عدد کا ایک مخالف ہوتا ہے: 6 اور −6۔"),
    "points": [T("−2 °C is warmer than −7 °C: −2 > −7", "−2 ڈگری، −7 ڈگری سے زیادہ گرم ہے: −2 > −7"),
               T("0 is neither positive nor negative.", "0 نہ مثبت ہے نہ منفی۔")]},
 ],
 "review_questions": [
   {"id": "r_temperature", "type": "apply", "skill": SKILL, "step": number_question(
     "r_temperature",
     T("It is 5 degrees below zero in Kalam. Write the temperature as an integer.", "کالام میں صفر سے 5 ڈگری نیچے ہے۔ درجہ حرارت کو صحیح عدد کی شکل میں لکھیں۔"),
     -5,
     T("Below zero means negative.", "صفر سے نیچے کا مطلب منفی ہے۔"),
     T("Right! −5 °C.", "درست! −5 ڈگری۔"),
     T("Below zero is negative: −5.", "صفر سے نیچے منفی ہے: −5"),
     common_wrong=[wrong(5, "5 would be above zero. Add a minus sign.", "5 کا مطلب صفر سے اوپر ہوتا۔ منفی کی علامت لگائیں۔", "sign_ignored")],
     qtype=None)},
   {"id": "r_compare", "type": "recall", "skill": SKILL, "step": {
     "id": "r_compare", "type": "choice",
     "prompt": T("Which is greater: −10 or −4?", "کون سا بڑا ہے: −10 یا −4؟"),
     "options": [
       opt("m4", signed(-4), signed(-4), True, "Yes! −4 is to the right of −10.", "جی ہاں! −4، −10 کے دائیں طرف ہے۔"),
       opt("m10", signed(-10), signed(-10), False, "−10 is further left, so it is smaller.", "−10 زیادہ بائیں ہے، اس لیے چھوٹا ہے۔", "bigger_digit_bigger"),
     ]}},
 ],
 "teacher_notes": [
   "Written fresh for the Integers unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-04. Fix the names and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: صحیح اعداد (integers), منفی (negative), مثبت (positive), عددی خط (number line), مخالف عدد (opposite / additive inverse).",
   "Number-line steps use the native number_line sim from −10 to 10 with whole-number ticks. Typed negative answers accept the keyboard minus and the − sign.",
   "Temperatures are realistic winter night values for the places named, not real readings.",
   "The numbers were worked out in content/sources/g6-maths-04/what_are_integers.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
attach(lesson, {
    "s1_hook": FIG_S1, "s3_see_it": FIG_S3, "s6_compare_rule": FIG_S6, "s8_opposite": FIG_S8,
    "s9_find_error": FIG_S9, "s10_explain_why": FIG_S10, "s12_summary": FIG_S12,
    "qb_find_error": FIG_QB_ERROR,
})
write(lesson)

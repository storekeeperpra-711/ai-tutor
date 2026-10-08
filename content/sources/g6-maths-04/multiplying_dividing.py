from common import (T, opt, say, wrong, signed, number_question, number_line, write,
                    REF, REVIEW, INT_ADD, INT_MULTIPLY)
from figs import jumps_figure, bar_pattern, label, attach

SKILL = INT_MULTIPLY
S = signed


def b(n):
    """A negative number in brackets: (−3); a positive one as it is."""
    return f"({S(n)})" if n < 0 else str(n)


def times(x, y):
    return f"{b(x)} × {b(y)}"


def over(x, y):
    return f"{b(x)} ÷ {b(y)}"


# s1, s4: 2 degrees colder every hour for 4 hours.
assert 4 * -2 == -8 == -2 + -2 + -2 + -2
# s2: foundation
assert -2 + -2 + -2 == -6
# s5: the pattern 3 × (−2), 2 × (−2), … (−2) × (−2)
PATTERN = [a * -2 for a in (3, 2, 1, 0, -1, -2)]
assert PATTERN == [-6, -4, -2, 0, 2, 4]
# s6, s7
assert -3 * -5 == 15 and -6 * 4 == -24
# s8, s9: division undoes multiplication
assert -12 // 3 == -4 and 3 * -4 == -12
assert -20 // -4 == 5 and -4 * 5 == -20
# s10: Ali
assert -7 * -3 == 21
# s12
assert 18 // -3 == -6 and -3 * -6 == 18
# question bank and review
assert -8 * -2 == 16 and -5 * 3 == -15 and -30 // 6 == -5 and -36 // -9 == 4 and 9 * -3 == -27


# ---------- pictures ----------

FIG_S1 = jumps_figure(
    -9, 1, [0, -2, -2, -2, -2], end_text="?",
    alt_en="A number line from −9 to 1. Starting at 0, four equal jumps, each marked −2, go to the left, one for each hour. The last one lands on a question mark.",
    alt_ur="−9 سے 1 تک عددی خط۔ 0 سے شروع ہو کر چار برابر چھلانگیں، ہر ایک پر −2 لکھا ہے، بائیں جاتی ہیں، ہر گھنٹے کے لیے ایک۔ آخری چھلانگ ایک سوالیہ نشان پر اترتی ہے۔")

FIG_S3 = jumps_figure(
    -7, 1, [0, -2, -2, -2],
    "A number line from −7 to 1. Starting at 0, three equal jumps, each marked −2, go left to −2, −4 and −6: three lots of −2 make −6.",
    "−7 سے 1 تک عددی خط۔ 0 سے شروع ہو کر تین برابر چھلانگیں، ہر ایک پر −2 لکھا ہے، بائیں −2، −4 اور −6 تک جاتی ہیں: −2 کے تین گروپ −6 بناتے ہیں۔")

_pattern = bar_pattern(
    [S(a) for a in (3, 2, 1, 0, -1, -2)], PATTERN,
    "Bars for n × (−2), with n = 3, 2, 1, 0, −1 and −2 written underneath. The answers are −6, −4, −2, 0, 2 and 4: the bars go down for the first three, there is no bar for 0, and then they go up. Each answer is 2 more than the one before.",
    "n × (−2) کے ستون، نیچے n = 3، 2، 1، 0، −1 اور −2 لکھا ہے۔ جواب −6، −4، −2، 0، 2 اور 4 ہیں: پہلے تین ستون نیچے جاتے ہیں، 0 کا کوئی ستون نہیں، پھر ستون اوپر جاتے ہیں۔ ہر جواب پچھلے سے 2 زیادہ ہے۔",
    unit=9, caption="n")
_pattern["items"].append(label((40, 18), "n×(−2)"))
FIG_S5 = _pattern

FIG_S7 = jumps_figure(
    -26, 2, [0, -6, -6, -6, -6], end_text="?", ticks_every=2,
    alt_en="A number line from −26 to 2, with a mark every 2. (−6) × 4 is four lots of −6: starting at 0, four equal jumps, each marked −6, go left. The last one lands on a question mark.",
    alt_ur="−26 سے 2 تک عددی خط، ہر 2 پر ایک نشان۔ (−6) × 4 کا مطلب −6 کے چار گروپ ہیں: 0 سے شروع ہو کر چار برابر چھلانگیں، ہر ایک پر −6 لکھا ہے، بائیں جاتی ہیں۔ آخری چھلانگ ایک سوالیہ نشان پر اترتی ہے۔")

FIG_S8 = jumps_figure(
    -13, 1, [0, -4, -4, -4],
    "A number line from −13 to 1. The jump from 0 to −12 is split into 3 equal jumps, each marked −4, landing on −4, −8 and −12. So (−12) ÷ 3 = −4.",
    "−13 سے 1 تک عددی خط۔ 0 سے −12 تک کا فاصلہ 3 برابر چھلانگوں میں بٹا ہے، ہر ایک پر −4 لکھا ہے، جو −4، −8 اور −12 پر اترتی ہیں۔ اس لیے (−12) ÷ 3 = −4")

FIG_S13 = jumps_figure(
    -9, 1, [0, -2, -2, -2, -2],
    "A number line from −9 to 1. Starting at 0, four equal jumps, each marked −2, go left to −2, −4, −6 and −8: 4 × (−2) = −8.",
    "−9 سے 1 تک عددی خط۔ 0 سے شروع ہو کر چار برابر چھلانگیں، ہر ایک پر −2 لکھا ہے، بائیں −2، −4، −6 اور −8 تک جاتی ہیں: 4 × (−2) = −8")

lesson = {
 "id": "g6-maths-04-multiplying-and-dividing-integers",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Multiply and divide integers using the sign rules.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Multiplying and dividing integers", "صحیح اعداد کی ضرب اور تقسیم"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": INT_ADD}],
 "misconceptions": [
   {"id": "two_negatives_negative", "description": "Thinks a negative times a negative is negative: (−3) × (−5) = −15."},
   {"id": "sign_dropped", "description": "Gets the size right but leaves off the minus sign when the signs are different."},
   {"id": "adds_instead", "description": "Adds the numbers instead of multiplying: (−3) × (−5) = −8."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("A negative number times a negative number gives …", "منفی عدد ضرب منفی عدد کا جواب …"),
     "options": [
       opt("pos", "a positive number", "مثبت عدد", True, "Yes! Same signs give a positive answer.", "جی ہاں! ایک جیسی علامتوں کا جواب مثبت ہوتا ہے۔"),
       opt("neg", "a negative number", "منفی عدد", False, "Same signs give a positive answer: (−2) × (−3) = 6.", "ایک جیسی علامتوں کا جواب مثبت ہوتا ہے: (−2) × (−3) = 6", "two_negatives_negative"),
       opt("zero", "zero", "صفر", False, "Only multiplying by 0 gives 0. (−2) × (−3) = 6.", "صرف 0 سے ضرب دینے پر 0 آتا ہے۔ (−2) × (−3) = 6"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T(f"Work out {over(-30, 6)}", f"حل کریں: {over(-30, 6)}"),
     -5,
     T("30 ÷ 6 = 5. The signs are different.", "30 ÷ 6 = 5۔ علامتیں مختلف ہیں۔"),
     T("Right! (−30) ÷ 6 = −5.", "درست! (−30) ÷ 6 = −5"),
     T("30 ÷ 6 = 5, and different signs give a negative answer: −5.", "30 ÷ 6 = 5، اور مختلف علامتوں کا جواب منفی ہوتا ہے: −5"),
     common_wrong=[wrong(5, "Different signs give a negative answer: −5.", "مختلف علامتوں کا جواب منفی ہوتا ہے: −5", "sign_dropped")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T(f"Nida wrote {times(-8, -2)} = −16. What went wrong?", f"ندا نے لکھا {times(-8, -2)} = −16۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("sign", "Both numbers are negative, so the answer is positive: 16.", "دونوں اعداد منفی ہیں، اس لیے جواب مثبت ہے: 16", True,
           "Yes! Same signs, positive answer.", "جی ہاں! ایک جیسی علامتیں، مثبت جواب۔"),
       opt("add", "She should add: −8 + (−2) = −10.", "اسے جمع کرنا چاہیے تھا: −8 + (−2) = −10", False,
           "The question says ×, so multiply. The sign is the mistake: the answer is 16.", "سوال میں × ہے، اس لیے ضرب دیں۔ غلطی علامت میں ہے: جواب 16 ہے۔", "adds_instead"),
       opt("nothing", "Nothing. 8 × 2 = 16 and the numbers are negative.", "کوئی غلطی نہیں۔ 8 × 2 = 16 اور اعداد منفی ہیں۔", False,
           "Two negatives multiplied give a positive: 16.", "دو منفی اعداد کی ضرب مثبت ہوتی ہے: 16", "two_negatives_negative"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_rules", "front": T("Sign rules for × and ÷", "ضرب اور تقسیم کی علامتوں کے اصول"),
    "back": T("Same signs: positive. Different signs: negative. (−3) × (−5) = 15, (−6) × 4 = −24.", "ایک جیسی علامتیں: مثبت۔ مختلف علامتیں: منفی۔ (−3) × (−5) = 15، (−6) × 4 = −24")},
   {"id": "f_divide", "front": T("(−20) ÷ (−4) = ?", "(−20) ÷ (−4) = ؟"),
    "back": T("5, because (−4) × 5 = −20.", "5، کیونکہ (−4) × 5 = −20")},
 ],
 "home_tasks": [{"id": "h_table", "text": T(
   "Make a times table for −3: 3 × (−3), 2 × (−3), 1 × (−3), 0 × (−3), (−1) × (−3), (−2) × (−3). What pattern do you see? Explain it to someone at home.",
   "−3 کا پہاڑا بنائیں: 3 × (−3)، 2 × (−3)، 1 × (−3)، 0 × (−3)، (−1) × (−3)، (−2) × (−3)۔ آپ کو کیا نمونہ نظر آتا ہے؟ گھر میں کسی کو سمجھائیں۔")}],
 "glossary": [T("Product", "حاصل ضرب"), T("Quotient", "حاصل تقسیم"), T("Sign rule", "علامت کا اصول")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "At night in Skardu it gets 2 degrees colder every hour. What is the change after 4 hours?",
      "سکردو میں رات کو ہر گھنٹے 2 ڈگری ٹھنڈ بڑھتی ہے۔ 4 گھنٹے بعد کتنی تبدیلی آئے گی؟"),
    "text": T("Today we multiply and divide integers. First, a quick check of adding.", "آج ہم صحیح اعداد کی ضرب اور تقسیم کریں گے۔ پہلے جمع کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Work out −2 + (−2) + (−2)", "حل کریں: −2 + (−2) + (−2)"),
     -6,
     T("Move 2 to the left, three times.", "تین بار 2 بائیں جائیں۔"),
     T("Right! −2 + (−2) + (−2) = −6.", "درست! −2 + (−2) + (−2) = −6"),
     T("All negative: 2 + 2 + 2 = 6, keep the minus: −6.", "سب منفی: 2 + 2 + 2 = 6، منفی رکھیں: −6"),
     common_wrong=[wrong(6, "All the numbers are negative, so the answer is negative: −6.", "سب اعداد منفی ہیں، اس لیے جواب منفی ہے: −6")],
     qtype="recall", skill=INT_ADD),
   {"id": "s3_see_it", "type": "explain",
    "character": say("happy", "Multiplying is adding again and again!", "ضرب بار بار جمع کرنا ہے!"),
    "text": T("−2 + (−2) + (−2) is three lots of −2, so 3 × (−2) = −6. In the same way, 4 hours of −2 degrees is 4 × (−2). A positive number times a negative number is negative.",
              "−2 + (−2) + (−2) تین بار −2 ہے، اس لیے 3 × (−2) = −6۔ اسی طرح، 4 گھنٹے تک −2 ڈگری، 4 × (−2) ہے۔ مثبت عدد ضرب منفی عدد کا جواب منفی ہوتا ہے۔")},
   number_line(
     "s4_colder",
     T(f"Show {times(4, -2)} on the number line: 4 jumps of −2 from 0. Press Check.", f"عددی خط پر {times(4, -2)} دکھائیں: 0 سے −2 کی 4 چھلانگیں۔ \"جانچیں\" دبائیں۔"),
     -8,
     T("Each jump is 2 to the left. Make 4 jumps.", "ہر چھلانگ 2 بائیں ہے۔ 4 چھلانگیں لگائیں۔"),
     T("Yes! 4 × (−2) = −8. It is 8 degrees colder.", "جی ہاں! 4 × (−2) = −8۔ 8 ڈگری زیادہ ٹھنڈ ہے۔"),
     T("−2, −4, −6, −8: four jumps of −2 land on −8.", "−2، −4، −6، −8: −2 کی چار چھلانگیں −8 پر پہنچتی ہیں۔"),
     common_wrong=[wrong("8", "That is 8 to the right. Each jump of −2 goes left.", "یہ 8 دائیں ہے۔ −2 کی ہر چھلانگ بائیں جاتی ہے۔", "sign_dropped"),
                   wrong("2", "That is 4 + (−2). Make 4 jumps of −2.", "یہ 4 + (−2) ہے۔ −2 کی 4 چھلانگیں لگائیں۔", "adds_instead")]),
   {"id": "s5_pattern", "type": "explain",
    "character": say("thinking", "What about a negative times a negative? Follow the pattern.", "منفی ضرب منفی کا کیا؟ نمونہ دیکھیں۔"),
    "text": T("3 × (−2) = −6, 2 × (−2) = −4, 1 × (−2) = −2, 0 × (−2) = 0. Each answer goes UP by 2. So (−1) × (−2) = 2 and (−2) × (−2) = 4. The rules: same signs give a positive answer; different signs give a negative answer.",
              "3 × (−2) = −6، 2 × (−2) = −4، 1 × (−2) = −2، 0 × (−2) = 0۔ ہر جواب 2 بڑھ جاتا ہے۔ اس لیے (−1) × (−2) = 2 اور (−2) × (−2) = 4۔ اصول: ایک جیسی علامتوں کا جواب مثبت؛ مختلف علامتوں کا جواب منفی۔")},
   number_question(
     "s6_neg_neg",
     T(f"Work out {times(-3, -5)}", f"حل کریں: {times(-3, -5)}"),
     15,
     T("3 × 5 = 15. Same signs.", "3 × 5 = 15۔ ایک جیسی علامتیں۔"),
     T("Right! (−3) × (−5) = 15.", "درست! (−3) × (−5) = 15"),
     T("3 × 5 = 15, and same signs give a positive answer: 15.", "3 × 5 = 15، اور ایک جیسی علامتوں کا جواب مثبت ہوتا ہے: 15"),
     common_wrong=[wrong(-15, "Both are negative: same signs give a POSITIVE answer, 15.", "دونوں منفی ہیں: ایک جیسی علامتوں کا جواب مثبت ہوتا ہے، 15", "two_negatives_negative"),
                   wrong(-8, "That adds them. Multiply: 3 × 5 = 15.", "یہ جمع ہے۔ ضرب دیں: 3 × 5 = 15", "adds_instead")]),
   number_question(
     "s7_neg_pos",
     T(f"Work out {times(-6, 4)}", f"حل کریں: {times(-6, 4)}"),
     -24,
     T("6 × 4 = 24. Different signs.", "6 × 4 = 24۔ مختلف علامتیں۔"),
     T("Right! (−6) × 4 = −24.", "درست! (−6) × 4 = −24"),
     T("6 × 4 = 24, and different signs give a negative answer: −24.", "6 × 4 = 24، اور مختلف علامتوں کا جواب منفی ہوتا ہے: −24"),
     common_wrong=[wrong(24, "Different signs give a negative answer: −24.", "مختلف علامتوں کا جواب منفی ہوتا ہے: −24", "sign_dropped"),
                   wrong(-2, "That adds them. Multiply: 6 × 4 = 24.", "یہ جمع ہے۔ ضرب دیں: 6 × 4 = 24", "adds_instead")]),
   {"id": "s8_divide", "type": "explain",
    "character": say("happy", "Division follows the same sign rules!", "تقسیم کے بھی یہی علامت کے اصول ہیں!"),
    "text": T("Division undoes multiplication. (−12) ÷ 3 = −4, because 3 × (−4) = −12. Same signs give a positive answer; different signs give a negative answer. Divide the numbers, then choose the sign.",
              "تقسیم، ضرب کا الٹ ہے۔ (−12) ÷ 3 = −4، کیونکہ 3 × (−4) = −12۔ ایک جیسی علامتوں کا جواب مثبت؛ مختلف علامتوں کا جواب منفی۔ پہلے اعداد تقسیم کریں، پھر علامت چنیں۔")},
   number_question(
     "s9_divide",
     T(f"Work out {over(-20, -4)}", f"حل کریں: {over(-20, -4)}"),
     5,
     T("20 ÷ 4 = 5. Same signs.", "20 ÷ 4 = 5۔ ایک جیسی علامتیں۔"),
     T("Right! (−20) ÷ (−4) = 5, because (−4) × 5 = −20.", "درست! (−20) ÷ (−4) = 5، کیونکہ (−4) × 5 = −20"),
     T("20 ÷ 4 = 5, and same signs give a positive answer: 5.", "20 ÷ 4 = 5، اور ایک جیسی علامتوں کا جواب مثبت ہوتا ہے: 5"),
     common_wrong=[wrong(-5, "Both are negative, so the answer is positive: 5.", "دونوں منفی ہیں، اس لیے جواب مثبت ہے: 5", "two_negatives_negative")]),
   {"id": "s10_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T(f"Ali wrote {times(-7, -3)} = −21. What went wrong?", f"علی نے لکھا {times(-7, -3)} = −21۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("sign", "Same signs give a positive answer: 21.", "ایک جیسی علامتوں کا جواب مثبت ہوتا ہے: 21", True,
          "Yes! (−7) × (−3) = 21.", "جی ہاں! (−7) × (−3) = 21"),
      opt("add", "He should get −10.", "جواب −10 ہونا چاہیے۔", False,
          "−10 is what you get by adding. This is ×: 7 × 3 = 21, and the answer is positive.", "−10 جمع کرنے سے آتا ہے۔ یہ ضرب ہے: 7 × 3 = 21، اور جواب مثبت ہے۔", "adds_instead"),
      opt("nothing", "Nothing. Negative numbers give negative answers.", "کوئی غلطی نہیں۔ منفی اعداد کا جواب منفی ہوتا ہے۔", False,
          "Not when there are two of them: a negative times a negative is positive.", "دو منفی اعداد ہوں تو نہیں: منفی ضرب منفی مثبت ہوتا ہے۔", "two_negatives_negative"),
    ]},
   {"id": "s11_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "My cousin says (−1) × (−2) must be negative because both numbers are negative. Can you teach us?",
                     "میرا کزن کہتا ہے (−1) × (−2) منفی ہوگا کیونکہ دونوں اعداد منفی ہیں۔ کیا آپ ہمیں سمجھا سکتے ہیں؟"),
    "task": T("In your own words: why is (−1) × (−2) equal to 2, not −2? You can use the pattern 2 × (−2), 1 × (−2), 0 × (−2) …",
              "اپنے الفاظ میں بتائیں: (−1) × (−2) کا جواب 2 کیوں ہے، −2 کیوں نہیں؟ آپ نمونہ 2 × (−2)، 1 × (−2)، 0 × (−2) … استعمال کر سکتے ہیں۔"),
    "key_idea": "In the pattern 2 × (−2) = −4, 1 × (−2) = −2, 0 × (−2) = 0, each answer goes up by 2, so the next one, (−1) × (−2), is 2. Same signs give a positive answer.",
    "levels": {
      "got_it": "Uses the pattern (answers going up by 2: −4, −2, 0, so next is 2), or explains that taking away negatives makes the answer go up.",
      "partly": "States the rule 'same signs give positive' without a reason, or starts the pattern without finishing it.",
      "not_yet": "Agrees it is negative, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["pattern", "goes up", "up by 2", "نمونہ", "بڑھ", "barh", "namoona"],
      ["same sign", "positive", "مثبت", "ایک جیسی", "musbat"],
      ["0", "zero", "صفر", "sifar"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The answers −4, −2, 0 go up by 2 each time, so (−1) × (−2) = 2.",
                  "بہت خوب سمجھایا! جواب −4، −2، 0 ہر بار 2 بڑھتے ہیں، اس لیے (−1) × (−2) = 2"),
      "partly": T("Good start! Now show the pattern: 1 × (−2) = −2, 0 × (−2) = 0. What comes next?", "اچھی شروعات! اب نمونہ دکھائیں: 1 × (−2) = −2، 0 × (−2) = 0۔ اس کے بعد کیا آئے گا؟"),
      "not_yet": T("Look: 2 × (−2) = −4, 1 × (−2) = −2, 0 × (−2) = 0. By how much does each answer go up? What comes next?",
                   "دیکھیں: 2 × (−2) = −4، 1 × (−2) = −2، 0 × (−2) = 0۔ ہر جواب کتنا بڑھتا ہے؟ اگلا کیا ہوگا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s12_share",
     T(f"Work out {over(18, -3)}", f"حل کریں: {over(18, -3)}"),
     -6,
     T("18 ÷ 3 = 6. Different signs.", "18 ÷ 3 = 6۔ مختلف علامتیں۔"),
     T("Right! 18 ÷ (−3) = −6, because (−3) × (−6) = 18.", "درست! 18 ÷ (−3) = −6، کیونکہ (−3) × (−6) = 18"),
     T("18 ÷ 3 = 6, and different signs give a negative answer: −6.", "18 ÷ 3 = 6، اور مختلف علامتوں کا جواب منفی ہوتا ہے: −6"),
     common_wrong=[wrong(6, "Different signs give a negative answer: −6.", "مختلف علامتوں کا جواب منفی ہوتا ہے: −6", "sign_dropped")]),
   {"id": "s13_summary", "type": "summary",
    "character": say("celebrating", "Two rules for × and ÷, and you know them both!", "ضرب اور تقسیم کے دو اصول، اور آپ دونوں جانتے ہیں!"),
    "text": T("Multiply or divide the numbers, then choose the sign. Same signs: positive. Different signs: negative. 4 × (−2) = −8, (−3) × (−5) = 15, (−20) ÷ (−4) = 5, 18 ÷ (−3) = −6.",
              "پہلے اعداد کی ضرب یا تقسیم کریں، پھر علامت چنیں۔ ایک جیسی علامتیں: مثبت۔ مختلف علامتیں: منفی۔ 4 × (−2) = −8، (−3) × (−5) = 15، (−20) ÷ (−4) = 5، 18 ÷ (−3) = −6"),
    "points": [T("(−) × (−) = (+)", "(−) × (−) = (+)"), T("(−) × (+) = (−)", "(−) × (+) = (−)")]},
 ],
 "review_questions": [
   {"id": "r_divide", "type": "apply", "skill": SKILL, "step": number_question(
     "r_divide",
     T(f"Work out {over(-36, -9)}", f"حل کریں: {over(-36, -9)}"),
     4,
     T("36 ÷ 9 = 4. Same signs.", "36 ÷ 9 = 4۔ ایک جیسی علامتیں۔"),
     T("Right! (−36) ÷ (−9) = 4.", "درست! (−36) ÷ (−9) = 4"),
     T("36 ÷ 9 = 4, and same signs give a positive answer.", "36 ÷ 9 = 4، اور ایک جیسی علامتوں کا جواب مثبت ہوتا ہے۔"),
     common_wrong=[wrong(-4, "Both are negative, so the answer is positive: 4.", "دونوں منفی ہیں، اس لیے جواب مثبت ہے: 4", "two_negatives_negative")],
     qtype=None)},
   {"id": "r_multiply", "type": "apply", "skill": SKILL, "step": number_question(
     "r_multiply",
     T(f"Work out {times(9, -3)}", f"حل کریں: {times(9, -3)}"),
     -27,
     T("9 × 3 = 27. Different signs.", "9 × 3 = 27۔ مختلف علامتیں۔"),
     T("Right! 9 × (−3) = −27.", "درست! 9 × (−3) = −27"),
     T("9 × 3 = 27, and different signs give a negative answer: −27.", "9 × 3 = 27، اور مختلف علامتوں کا جواب منفی ہوتا ہے: −27"),
     common_wrong=[wrong(27, "Different signs give a negative answer: −27.", "مختلف علامتوں کا جواب منفی ہوتا ہے: −27", "sign_dropped"),
                   wrong(6, "That adds them. Multiply: 9 × 3 = 27.", "یہ جمع ہے۔ ضرب دیں: 9 × 3 = 27", "adds_instead")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Integers unit. No textbook text or exercises were used.",
   "Negative numbers in × and ÷ are written in brackets: (−3) × (−5). Check this matches the Punjab textbook's style.",
   "The rule 'negative × negative = positive' is shown with a pattern (s5) and then explained by the child to the AI (s11).",
   "Urdu terms to check: حاصل ضرب (product), حاصل تقسیم (quotient).",
   "The numbers were worked out in content/sources/g6-maths-04/multiplying_dividing.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
attach(lesson, {
    "s1_hook": FIG_S1, "s3_see_it": FIG_S3, "s5_pattern": FIG_S5, "s7_neg_pos": FIG_S7,
    "s8_divide": FIG_S8, "s13_summary": FIG_S13,
})
write(lesson)

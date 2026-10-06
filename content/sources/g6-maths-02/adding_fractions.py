from math import lcm

from common import (F, T, opt, say, wrong, frac, unsimplified, fraction_question, write,
                    REF, REVIEW, TIMES_TABLES, EQUIVALENT, ADD_UNLIKE)

SKILL = ADD_UNLIKE


def tops_and_bottoms(a: F, b: F, sign=1) -> str:
    """The mistake: add (or subtract) the numerators and the denominators."""
    return unsimplified(a.numerator + sign * b.numerator, a.denominator + sign * b.denominator)


def only_bottoms(a: F, b: F, sign=1) -> str:
    """The mistake: change the denominators to the common one but keep the numerators."""
    d = lcm(a.denominator, b.denominator)
    return unsimplified(a.numerator + sign * b.numerator, d)


# s3: same-size pieces first: 1/4 + 2/4
LIKE = F(1, 4) + F(2, 4)
assert LIKE == F(3, 4) == F(0.75)
LIKE_WRONG = F(1 + 2, 4 + 4)
assert LIKE_WRONG == F(3, 8) == F(0.375)

# s1, s4-s6, s10, s11: Zara's half and Ali's third of a paratha
ZARA, ALI = F(1, 2), F(1, 3)
COMMON = lcm(2, 3)
assert COMMON == 6
EATEN = ZARA + ALI
assert EATEN == F(5, 6)
assert ZARA * COMMON == 3 and ALI * COMMON == 2 and EATEN * COMMON == 5
assert tops_and_bottoms(ZARA, ALI) == "2/5" and F(2, 5) < ZARA  # less than Zara alone!

# s7: Bilal's lassi
MORNING, EVENING = F(1, 4), F(2, 3)
LASSI = MORNING + EVENING
assert lcm(4, 3) == 12 and LASSI == F(11, 12)
assert tops_and_bottoms(MORNING, EVENING) == "3/7" and only_bottoms(MORNING, EVENING) == "3/12"

# s8: Ayesha's ribbon
RIBBON, USED = F(3, 4), F(1, 3)
LEFT = RIBBON - USED
assert LEFT == F(5, 12)
assert tops_and_bottoms(RIBBON, USED, -1) == "2/1" and only_bottoms(RIBBON, USED, -1) == "2/12"

# s9: an answer that needs simplifying
SIX = F(1, 2) + F(1, 6)
assert F(3, 6) + F(1, 6) == F(4, 6) == SIX == F(2, 3)
assert tops_and_bottoms(F(1, 2), F(1, 6)) == "2/8"

# Question bank and review
assert lcm(5, 2) == 10 and F(2, 5) + F(1, 2) == F(9, 10)
assert F(5, 6) - F(1, 2) == F(1, 3)
assert F(1, 2) - F(1, 5) == F(3, 10)

lesson = {
 "id": "g6-maths-02-adding-fractions",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Add and subtract fractions with different denominators by first changing them to equivalent fractions with a common denominator.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Adding and subtracting fractions", "کسور کی جمع اور تفریق"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": EQUIVALENT}, {"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "add_tops_and_bottoms", "description": "Adds the numerators and adds the denominators (1/2 + 1/3 = 2/5)."},
   {"id": "subtract_tops_and_bottoms", "description": "Subtracts the numerators and subtracts the denominators (3/4 − 1/3 = 2/1)."},
   {"id": "only_denominator_changed", "description": "Changes both fractions to the common denominator but does not change the numerators (1/4 + 2/3 = 3/12)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_common_denominator", "type": "recall", "step": {
     "id": "qb_common_denominator", "type": "choice",
     "prompt": T("To add 2/5 + 1/2, which common denominator can you use?", "2/5 + 1/2 جمع کرنے کے لیے کون سا مشترک نسب نما لے سکتے ہیں؟"),
     "options": [
       opt("ten", "10", "10", True,
           "Yes! Both 5 and 2 go into 10: 2/5 = 4/10 and 1/2 = 5/10.", "جی ہاں! 5 اور 2 دونوں 10 میں پورے آتے ہیں: 2/5 = 4/10 اور 1/2 = 5/10"),
       opt("seven", "7", "7", False,
           "7 is 5 + 2, but 5 and 2 don't go into 7. Find a number in the 5 times table and the 2 times table.", "7 تو 5 + 2 ہے، لیکن 5 اور 2 اس میں پورے نہیں آتے۔ ایسا عدد ڈھونڈیں جو 5 اور 2 دونوں کے پہاڑے میں ہو۔", "add_tops_and_bottoms"),
       opt("five", "5", "5", False,
           "Halves can't be written as fifths. Find a number that both 5 and 2 go into.", "آدھے کو پانچویں حصوں میں نہیں لکھا جا سکتا۔ ایسا عدد ڈھونڈیں جس میں 5 اور 2 دونوں پورے آئیں۔"),
     ]}},
   {"id": "qb_add_fifths_halves", "type": "apply", "step": fraction_question(
     "qb_add_fifths_halves",
     T("Work out 2/5 + 1/2.", "2/5 + 1/2 حل کریں۔"),
     frac(F(2, 5) + F(1, 2)),
     T("Change both to tenths first.", "پہلے دونوں کو دسویں حصوں میں بدلیں۔"),
     T("Right! 4/10 + 5/10 = 9/10.", "درست! 4/10 + 5/10 = 9/10"),
     T("2/5 = 4/10 and 1/2 = 5/10. So 4/10 + 5/10 = 9/10.", "2/5 = 4/10 اور 1/2 = 5/10۔ اس لیے 4/10 + 5/10 = 9/10"),
     common_wrong=[wrong(tops_and_bottoms(F(2, 5), F(1, 2)), "You added the tops and the bottoms. Make the pieces the same size first: tenths.",
                         "آپ نے اوپر اور نیچے والے عدد جمع کر دیے۔ پہلے ٹکڑے ایک جتنے کریں: دسویں حصے۔", "add_tops_and_bottoms")],
     qtype=None)},
   {"id": "qb_find_error_subtract", "type": "find_error", "step": {
     "id": "qb_find_error_subtract", "type": "choice",
     "prompt": T("Ali works out 5/6 − 1/2 like this: 5/6 − 1/6 = 4/6. What went wrong?", "علی 5/6 − 1/2 یوں حل کرتا ہے: 5/6 − 1/6 = 4/6۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("numerator", "He changed 1/2 to sixths but kept the 1 on top. 1/2 = 3/6, so the answer is 2/6 = 1/3.", "اس نے 1/2 کو چھٹے حصوں میں بدلا لیکن اوپر 1 ہی رہنے دیا۔ 1/2 = 3/6، اس لیے جواب 2/6 = 1/3 ہے۔", True,
           "Right! When the bottom is multiplied by 3, the top must be multiplied by 3 too.", "درست! جب نیچے والے کو 3 سے ضرب دیں تو اوپر والے کو بھی 3 سے ضرب دینی ہوتی ہے۔"),
       opt("nothing", "Nothing, 4/6 is right.", "کوئی غلطی نہیں، 4/6 درست ہے۔", False,
           "Is 1/2 the same as 1/6? Half a paratha is 3 sixths, not 1.", "کیا 1/2 اور 1/6 برابر ہیں؟ آدھا پراٹھا 3 چھٹے حصے ہے، 1 نہیں۔", "only_denominator_changed"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_add_unlike", "front": T("How do you add 1/2 + 1/3?", "1/2 + 1/3 کیسے جمع کرتے ہیں؟"),
    "back": T("Make the pieces the same size: 1/2 = 3/6 and 1/3 = 2/6. Then add the tops: 3/6 + 2/6 = 5/6.", "ٹکڑے ایک جتنے کریں: 1/2 = 3/6 اور 1/3 = 2/6۔ پھر اوپر والے جمع کریں: 3/6 + 2/6 = 5/6")},
   {"id": "f_not_two_fifths", "front": T("Is 1/2 + 1/3 = 2/5?", "کیا 1/2 + 1/3 = 2/5 ہے؟"),
    "back": T("No! 2/5 is less than 1/2. Never add the bottoms. 1/2 + 1/3 = 5/6.", "نہیں! 2/5 تو 1/2 سے بھی کم ہے۔ نیچے والے عدد کبھی جمع نہ کریں۔ 1/2 + 1/3 = 5/6")},
 ],
 "home_tasks": [{"id": "h_paper_strips", "text": T(
   "Take two paper strips of the same length. Fold one into 2 equal parts and the other into 3. Colour 1/2 of the first and 1/3 of the second. Now fold both into 6 parts. How many sixths are coloured altogether?",
   "ایک جتنی لمبی کاغذ کی دو پٹیاں لیں۔ ایک کو 2 برابر حصوں میں اور دوسری کو 3 میں تہہ کریں۔ پہلی کا 1/2 اور دوسری کا 1/3 رنگ دیں۔ اب دونوں کو 6 حصوں میں تہہ کریں۔ کل کتنے چھٹے حصے رنگے ہوئے ہیں؟")}],
 "glossary": [T("Fraction", "کسر"), T("Numerator", "شمار کنندہ"), T("Denominator", "نسب نما"),
              T("Common denominator", "مشترک نسب نما"), T("Equivalent fractions", "مساوی کسور"),
              T("Addition", "جمع"), T("Subtraction", "تفریق")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Zara ate half a paratha and Ali ate a third of it. How much did they eat together?",
      "زارا نے آدھا پراٹھا کھایا اور علی نے اس کا تیسرا حصہ۔ دونوں نے مل کر کتنا کھایا؟"),
    "text": T("Halves and thirds are pieces of different sizes. Let's find out how to add them. First, a quick check.",
              "آدھا اور تہائی مختلف سائز کے ٹکڑے ہیں۔ آئیں دیکھیں انہیں کیسے جمع کرتے ہیں۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "choice", "question_type": "recall", "skill": EQUIVALENT,
    "prompt": T("Which fraction is equal to 1/2?", "کون سی کسر 1/2 کے برابر ہے؟"),
    "options": [
      opt("three_sixths", "3/6", "3/6", True,
          "Yes! 1/2 = (1 × 3)/(2 × 3) = 3/6.", "جی ہاں! 1/2 = (1 × 3)/(2 × 3) = 3/6"),
      opt("one_sixth", "1/6", "1/6", False,
          "Only the bottom changed. 1/6 is much less than half.", "صرف نیچے والا عدد بدلا۔ 1/6 آدھے سے بہت کم ہے۔"),
      opt("two_thirds", "2/3", "2/3", False,
          "2/3 is 1/2 with 1 added to top and bottom. That changes the amount.", "2/3 میں 1/2 کے اوپر اور نیچے 1 جمع کیا گیا ہے۔ اس سے مقدار بدل جاتی ہے۔"),
    ]},
   {"id": "s3_same_size", "type": "number", "question_type": "apply",
    "prompt": T("Same-size pieces first. Bilal ate 1/4 of a chapati, then 2/4 more. How much did he eat? Write a fraction.",
                "پہلے ایک جتنے ٹکڑے۔ بلال نے چپاتی کا 1/4 کھایا، پھر 2/4 اور۔ اس نے کتنا کھایا؟ کسر لکھیں۔"),
    "answer": float(LIKE), "checker": "fraction", "require_simplest": True,
    "hint": T("1 quarter and 2 more quarters: how many quarters?", "1 چوتھائی اور 2 چوتھائیاں اور: کل کتنی چوتھائیاں؟"),
    "feedback_correct": T("Right! 1/4 + 2/4 = 3/4. The pieces are the same size, so just add the numerators.", "درست! 1/4 + 2/4 = 3/4۔ ٹکڑے ایک جتنے ہیں، اس لیے صرف شمار کنندہ جمع کریں۔"),
    "feedback_wrong": T("1 quarter + 2 quarters = 3 quarters. 1/4 + 2/4 = 3/4. The denominator stays 4.", "1 چوتھائی + 2 چوتھائیاں = 3 چوتھائیاں۔ 1/4 + 2/4 = 3/4۔ نسب نما 4 ہی رہتا ہے۔"),
    "common_wrong": [wrong(float(LIKE_WRONG), "3/8 is less than 1/2, but Bilal ate more than half! The pieces are still quarters, so keep 4 at the bottom.",
                           "3/8 تو آدھے سے کم ہے، لیکن بلال نے آدھی سے زیادہ کھائی! ٹکڑے اب بھی چوتھائیاں ہیں، اس لیے نیچے 4 ہی رکھیں۔", "add_tops_and_bottoms")]},
   {"id": "s4_predict", "type": "choice",
    "prompt": T("Guess first: Hamza says half a paratha plus a third of a paratha is 2/5 of a paratha (1 + 1 = 2 and 2 + 3 = 5). Is he right?",
                "پہلے اندازہ لگائیں: حمزہ کہتا ہے آدھا پراٹھا اور تہائی پراٹھا مل کر 2/5 پراٹھا ہے (1 + 1 = 2 اور 2 + 3 = 5)۔ کیا وہ درست ہے؟"),
    "options": [
      opt("yes", "Yes, add the tops and add the bottoms", "ہاں، اوپر والے جمع کریں اور نیچے والے جمع کریں", False,
          "It looks neat, but let's test it: 2/5 is less than 1/2. Can half plus more be less than half?",
          "یہ آسان لگتا ہے، لیکن آئیں جانچیں: 2/5 تو 1/2 سے کم ہے۔ کیا آدھا اور کچھ مزید مل کر آدھے سے کم ہو سکتا ہے؟", "add_tops_and_bottoms"),
      opt("no", "No, the answer must be more than 1/2", "نہیں، جواب 1/2 سے زیادہ ہونا چاہیے", True,
          "Good thinking! Zara alone ate 1/2, so together they ate more than 1/2. 2/5 is less.",
          "بہت خوب سوچا! اکیلے زارا نے 1/2 کھایا، اس لیے دونوں نے مل کر 1/2 سے زیادہ کھایا۔ 2/5 کم ہے۔"),
      opt("unsure", "We can't add halves and thirds", "آدھے اور تہائی جمع نہیں ہو سکتے", False,
          "We can! We just need pieces of the same size first. Let's see how.", "ہو سکتے ہیں! بس پہلے ٹکڑے ایک جتنے کرنے ہوں گے۔ آئیں دیکھیں کیسے۔"),
    ]},
   {"id": "s5_test_it", "type": "sim", "question_type": "apply", "renderer": "native", "sim_id": "fraction_bars",
    "prompt": T(f"Halves and thirds both fit into sixths. Use + to cut the paratha into {COMMON} pieces. Tap {int(ZARA * COMMON)} pieces for Zara's half and {int(ALI * COMMON)} for Ali's third. Press Check.",
                f"آدھے اور تہائی دونوں چھٹے حصوں میں پورے آتے ہیں۔ + دبا کر پراٹھے کے {COMMON} ٹکڑے کریں۔ زارا کے آدھے کے لیے {int(ZARA * COMMON)} ٹکڑے اور علی کے تہائی کے لیے {int(ALI * COMMON)} ٹکڑے چھوئیں۔ \"جانچیں\" دبائیں۔"),
    "params": {"wholes": 1, "max_cut": 12},
    "expected": {"result": "pieces", "checker": "numeric", "answer": str(int(EATEN * COMMON))},
    "hint": T("Cut into 6. Half of 6 pieces is 3; a third of 6 pieces is 2.", "6 ٹکڑے کریں۔ 6 ٹکڑوں کا آدھا 3 ہے؛ 6 ٹکڑوں کا تہائی 2 ہے۔"),
    "feedback_correct": T("Yes! 3 sixths + 2 sixths = 5 sixths. Together they ate 5/6 of the paratha.", "جی ہاں! 3 چھٹے حصے + 2 چھٹے حصے = 5 چھٹے حصے۔ دونوں نے مل کر پراٹھے کا 5/6 کھایا۔"),
    "feedback_wrong": T("Cut the paratha into 6. Zara's half is 3 pieces and Ali's third is 2 pieces: 5 pieces, or 5/6.", "پراٹھے کے 6 ٹکڑے کریں۔ زارا کا آدھا 3 ٹکڑے ہے اور علی کا تہائی 2 ٹکڑے: کل 5 ٹکڑے، یعنی 5/6"),
    "common_wrong": [wrong("2", "That is 1 piece for each child. But the pieces must be the same size: half the paratha is 3 sixths.",
                           "یہ ہر بچے کا 1 ٹکڑا ہے۔ لیکن ٹکڑے ایک جتنے ہونے چاہییں: آدھا پراٹھا 3 چھٹے حصے ہے۔", "add_tops_and_bottoms")]},
   {"id": "s6_see_it", "type": "explain",
    "character": say("talking", "Make the pieces the same size first, then add!", "پہلے ٹکڑے ایک جتنے کریں، پھر جمع کریں!"),
    "text": T("We can only add pieces of the same size. 2 and 3 both go into 6, so 6 is a common denominator. Change each fraction to an equivalent fraction: 1/2 = 3/6 and 1/3 = 2/6. Then add the numerators and keep the denominator: 3/6 + 2/6 = 5/6. Subtracting works the same way.",
              "ہم صرف ایک جتنے ٹکڑے جمع کر سکتے ہیں۔ 2 اور 3 دونوں 6 میں پورے آتے ہیں، اس لیے 6 مشترک نسب نما ہے۔ ہر کسر کو مساوی کسر میں بدلیں: 1/2 = 3/6 اور 1/3 = 2/6۔ پھر شمار کنندہ جمع کریں اور نسب نما وہی رکھیں: 3/6 + 2/6 = 5/6۔ تفریق بھی اسی طرح ہوتی ہے۔")},
   fraction_question(
     "s7_lassi",
     T("Bilal drank 1/4 of a jug of lassi in the morning and 2/3 of the jug in the evening. What fraction of the jug did he drink?",
       "بلال نے صبح لسی کے جگ کا 1/4 پیا اور شام کو جگ کا 2/3۔ اس نے جگ کا کتنا حصہ پیا؟"),
     frac(LASSI),
     T("4 and 3 both go into 12. Change both fractions to twelfths.", "4 اور 3 دونوں 12 میں پورے آتے ہیں۔ دونوں کسور کو بارہویں حصوں میں بدلیں۔"),
     T("Well done! 1/4 = 3/12 and 2/3 = 8/12, so 3/12 + 8/12 = 11/12.", "شاباش! 1/4 = 3/12 اور 2/3 = 8/12، اس لیے 3/12 + 8/12 = 11/12"),
     T("Use 12: 1/4 = 3/12 (× 3) and 2/3 = 8/12 (× 4). Then 3/12 + 8/12 = 11/12.", "12 لیں: 1/4 = 3/12 (× 3) اور 2/3 = 8/12 (× 4)۔ پھر 3/12 + 8/12 = 11/12"),
     common_wrong=[
       wrong(tops_and_bottoms(MORNING, EVENING), "You added the tops and the bottoms. 3/7 is less than 2/3, so it can't be right. Change to twelfths first.",
             "آپ نے اوپر اور نیچے والے عدد جمع کر دیے۔ 3/7 تو 2/3 سے بھی کم ہے، اس لیے درست نہیں ہو سکتا۔ پہلے بارہویں حصوں میں بدلیں۔", "add_tops_and_bottoms"),
       wrong(only_bottoms(MORNING, EVENING), "Good, 12 is the right denominator. But change the numerators too: 1/4 = 3/12 and 2/3 = 8/12.",
             "شاباش، 12 درست نسب نما ہے۔ لیکن شمار کنندہ بھی بدلیں: 1/4 = 3/12 اور 2/3 = 8/12", "only_denominator_changed"),
     ]),
   fraction_question(
     "s8_ribbon",
     T("Ayesha had 3/4 of a metre of ribbon. She used 1/3 of a metre to decorate a card. How much ribbon is left?",
       "عائشہ کے پاس 3/4 میٹر فیتہ تھا۔ اس نے کارڈ سجانے کے لیے 1/3 میٹر استعمال کیا۔ کتنا فیتہ بچا؟"),
     frac(LEFT),
     T("Use twelfths again: 3/4 = ?/12 and 1/3 = ?/12. Then subtract the numerators.", "پھر بارہویں حصے لیں: 3/4 = ?/12 اور 1/3 = ?/12۔ پھر شمار کنندہ تفریق کریں۔"),
     T("Right! 9/12 − 4/12 = 5/12 of a metre is left.", "درست! 9/12 − 4/12 = 5/12 میٹر بچا۔"),
     T("3/4 = 9/12 and 1/3 = 4/12. So 9/12 − 4/12 = 5/12 of a metre is left.", "3/4 = 9/12 اور 1/3 = 4/12۔ اس لیے 9/12 − 4/12 = 5/12 میٹر بچا۔"),
     common_wrong=[
       wrong(tops_and_bottoms(RIBBON, USED, -1), "You subtracted the tops and the bottoms: 2/1 is 2 whole metres, more than she started with! Change to twelfths first.",
             "آپ نے اوپر اور نیچے والے عدد تفریق کر دیے: 2/1 تو 2 پورے میٹر ہیں، شروع سے بھی زیادہ! پہلے بارہویں حصوں میں بدلیں۔", "subtract_tops_and_bottoms"),
       wrong(only_bottoms(RIBBON, USED, -1), "12 is right, but change the numerators too: 3/4 = 9/12 and 1/3 = 4/12.",
             "12 درست ہے، لیکن شمار کنندہ بھی بدلیں: 3/4 = 9/12 اور 1/3 = 4/12", "only_denominator_changed"),
     ]),
   fraction_question(
     "s9_simplify",
     T("Work out 1/2 + 1/6. Give your answer in its simplest form.", "1/2 + 1/6 حل کریں۔ جواب سادہ ترین شکل میں لکھیں۔"),
     frac(SIX),
     T("6 is a common denominator: 1/2 = 3/6. Add, then simplify.", "6 مشترک نسب نما ہے: 1/2 = 3/6۔ جمع کریں، پھر سادہ کریں۔"),
     T("Yes! 3/6 + 1/6 = 4/6 = 2/3.", "جی ہاں! 3/6 + 1/6 = 4/6 = 2/3"),
     T("1/2 = 3/6, so 3/6 + 1/6 = 4/6. 2 divides 4 and 6: 4/6 = 2/3.", "1/2 = 3/6، اس لیے 3/6 + 1/6 = 4/6۔ 2، 4 اور 6 دونوں کو تقسیم کرتا ہے: 4/6 = 2/3"),
     common_wrong=[wrong(tops_and_bottoms(F(1, 2), F(1, 6)), "You added the tops and the bottoms. Change 1/2 to sixths first.",
                         "آپ نے اوپر اور نیچے والے عدد جمع کر دیے۔ پہلے 1/2 کو چھٹے حصوں میں بدلیں۔", "add_tops_and_bottoms")]),
   {"id": "s10_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Look at Hamza's answer again: 1/2 + 1/3 = 2/5. What went wrong?", "حمزہ کا جواب پھر دیکھیں: 1/2 + 1/3 = 2/5۔ اس سے کیا غلطی ہوئی؟"),
    "options": [
      opt("bottoms", "He added the denominators. He should change both to sixths: 3/6 + 2/6 = 5/6.", "اس نے نسب نما جمع کر دیے۔ اسے دونوں کو چھٹے حصوں میں بدلنا چاہیے تھا: 3/6 + 2/6 = 5/6", True,
          "Yes! The denominator tells the size of the pieces. We don't add sizes; we make them the same, then count.",
          "جی ہاں! نسب نما ٹکڑوں کا سائز بتاتا ہے۔ ہم سائز جمع نہیں کرتے؛ پہلے ایک جتنے کرتے ہیں، پھر گنتے ہیں۔"),
      opt("nothing", "Nothing, 2/5 is right.", "کوئی غلطی نہیں، 2/5 درست ہے۔", False,
          "2/5 is less than 1/2, but Zara alone ate 1/2. Together it must be more.", "2/5 تو 1/2 سے کم ہے، جبکہ اکیلے زارا نے 1/2 کھایا۔ مل کر زیادہ ہونا چاہیے۔", "add_tops_and_bottoms"),
      opt("multiply", "He should multiply the denominators and keep the tops: 2/6.", "اسے نسب نما ضرب دینے چاہیے تھے اور اوپر والے وہی رکھنے تھے: 2/6", False,
          "6 is the right denominator, but the tops change too: 1/2 = 3/6 and 1/3 = 2/6.", "6 درست نسب نما ہے، لیکن اوپر والے بھی بدلتے ہیں: 1/2 = 3/6 اور 1/3 = 2/6", "only_denominator_changed"),
    ]},
   {"id": "s11_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? Why can't I just add the tops and the bottoms?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ میں اوپر اور نیچے والے عدد سیدھے جمع کیوں نہیں کر سکتا؟"),
    "task": T("In your own words: why is 1/2 + 1/3 not 2/5? Explain how to add them. You can use a paratha.",
              "اپنے الفاظ میں بتائیں: 1/2 + 1/3 کا جواب 2/5 کیوں نہیں؟ سمجھائیں کہ انہیں کیسے جمع کرتے ہیں۔ آپ پراٹھے کی مثال دے سکتے ہیں۔"),
    "key_idea": "Halves and thirds are pieces of different sizes, so they can't be counted together. Change both to the same size (sixths, a common denominator): 1/2 = 3/6 and 1/3 = 2/6, so the total is 5/6. 2/5 can't be right because it is less than 1/2.",
    "levels": {
      "got_it": "Says the pieces must be the same size (a common denominator), changes to sixths (3/6 and 2/6, or the answer 5/6), and/or says 2/5 is less than 1/2 so it can't be the total.",
      "partly": "Mentions same-size pieces, sixths or the answer 5/6, but does not explain why adding the bottoms is wrong or how the sixths are found.",
      "not_yet": "Says adding tops and bottoms is fine, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["same size", "same", "common", "equal", "برابر", "ایک جتن", "ایک جیس", "مشترک", "barabar", "ek jitn", "ek jais", "mushtarak"],
      ["sixth", "6", "چھٹ", "chhat", "chat"],
      ["less than half", "less", "smaller", "more than half", "کم", "چھوٹ", "زیادہ", "kam", "chhot", "zyada", "ziada"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Halves and thirds are different sizes, so first change both to sixths: 3/6 + 2/6 = 5/6.",
                  "بہت خوب سمجھایا! آدھا اور تہائی مختلف سائز کے ہیں، اس لیے پہلے دونوں کو چھٹے حصوں میں بدلیں: 3/6 + 2/6 = 5/6"),
      "partly": T("Good start! Now say why 2/5 can't be right: is it more or less than Zara's half?",
                  "اچھی شروعات! اب بتائیں کہ 2/5 درست کیوں نہیں ہو سکتا: کیا یہ زارا کے آدھے سے زیادہ ہے یا کم؟"),
      "not_yet": T("Think of a paratha cut into 6 pieces. How many pieces are half? How many are a third? How many altogether?",
                   "سوچیں: ایک پراٹھے کے 6 ٹکڑے ہیں۔ آدھا کتنے ٹکڑے ہے؟ تہائی کتنے ٹکڑے؟ کل کتنے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can add and subtract any fractions now!", "اب آپ کوئی بھی کسور جمع اور تفریق کر سکتے ہیں!"),
    "text": T("To add or subtract fractions with different denominators, first change them to equivalent fractions with a common denominator. Then add or subtract the numerators, keep the denominator, and simplify.",
              "مختلف نسب نما والی کسور جمع یا تفریق کرنے کے لیے پہلے انہیں مشترک نسب نما والی مساوی کسور میں بدلیں۔ پھر شمار کنندہ جمع یا تفریق کریں، نسب نما وہی رکھیں، اور جواب سادہ کریں۔"),
    "points": [T("1/2 + 1/3 = 3/6 + 2/6 = 5/6", "1/2 + 1/3 = 3/6 + 2/6 = 5/6"),
               T("Never add the denominators: 1/2 + 1/3 is not 2/5.", "نسب نما کبھی جمع نہ کریں: 1/2 + 1/3 کا جواب 2/5 نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_subtract", "type": "apply", "skill": SKILL, "step": fraction_question(
     "r_subtract",
     T("Work out 1/2 − 1/5.", "1/2 − 1/5 حل کریں۔"),
     frac(F(1, 2) - F(1, 5)),
     T("2 and 5 both go into 10.", "2 اور 5 دونوں 10 میں پورے آتے ہیں۔"),
     T("Right! 5/10 − 2/10 = 3/10.", "درست! 5/10 − 2/10 = 3/10"),
     T("1/2 = 5/10 and 1/5 = 2/10. So 5/10 − 2/10 = 3/10.", "1/2 = 5/10 اور 1/5 = 2/10۔ اس لیے 5/10 − 2/10 = 3/10"),
     common_wrong=[wrong(tops_and_bottoms(F(1, 2), F(1, 5), -1), "You subtracted the tops and the bottoms. Change both to tenths first.",
                         "آپ نے اوپر اور نیچے والے عدد تفریق کر دیے۔ پہلے دونوں کو دسویں حصوں میں بدلیں۔", "subtract_tops_and_bottoms")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Fractions unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the file is named g6-maths-02 to sit with the dividing-fractions lesson. Fix the name and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: مشترک نسب نما (common denominator), مساوی کسور (equivalent fractions), تہائی (third), چھٹا حصہ (sixth), بارہواں حصہ (twelfth), تفریق (subtraction).",
   "The lesson uses any common denominator the times tables give (here the smallest one). The LCM (ذو اضعاف اقل) is not named; add it if the textbook teaches it with this topic.",
   "Steps follow the lesson pattern: foundation check (s2), same denominators (s3), prediction (s4), concrete with the fraction bars (s5) then symbolic (s6), practice (s7 to s9), find the error (s10), explain (s11).",
   "The answers and the common wrong answers (adding tops and bottoms; changing only the denominator) were worked out with Python's fractions module in content/sources/g6-maths-02/adding_fractions.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

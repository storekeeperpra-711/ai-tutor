from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, DEC_PLACE_VALUE, SM_ORDER, SM_ESTIMATE, round_to)

SKILL = SM_ESTIMATE

# s2: the tenths digit of 4.75
S2 = 7
assert str("4.75").split(".")[1][0] == str(S2)
# s4: 487 to the nearest 100
S4 = round_to(487, 100)
assert S4 == 500
# s5: estimate 298 + 513 to the nearest 100
S5 = round_to(298, 100) + round_to(513, 100)
assert S5 == 800
# s6: 49 x 21 is about 50 x 20
assert round_to(49, 10) * round_to(21, 10) == 1000
# s7: estimate 6.8 x 4.1 to whole numbers
S7 = round_to("6.8", 1) * round_to("4.1", 1)
assert S7 == 28
# s8: 3462 to the nearest 10 (3500 would be the nearest 100)
S8 = round_to(3462, 10)
assert S8 == 3460 and round_to(3462, 100) == 3500
# s9: 52 x 38 is about 50 x 40 = 2000, so 476 can't be right
assert round_to(52, 10) * round_to(38, 10) == 2000 and 52 * 38 == 1976
# s11: Rs 198 + Rs 405 + Rs 99, each to the nearest 100
S11 = round_to(198, 100) + round_to(405, 100) + round_to(99, 100)
assert S11 == 700 and 198 + 405 + 99 == 702
# question bank and review
QB = round_to(762, 100)
assert QB == 800
assert round_to("19.8", 1) * 5 == 100 and 19.8 * 5 > 90
R1 = round_to(612, 100) - round_to(289, 100)
assert R1 == 300
R2 = round_to(45, 10)
assert R2 == 50

lesson = {
 "id": "g6-maths-13-estimation",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Round numbers to the nearest 10, 100 or whole number, and estimate to check an answer.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Rounding and estimating", "قریب ترین عدد اور اندازہ"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": SM_ORDER}, {"skill": DEC_PLACE_VALUE}],
 "misconceptions": [
   {"id": "rounds_down_always", "description": "Always rounds down (drops the digits) instead of looking at the next digit."},
   {"id": "wrong_place", "description": "Rounds to the wrong place, such as the nearest 100 when asked for the nearest 10."},
   {"id": "exact_not_estimate", "description": "Works out the exact answer when an estimate is asked for, or trusts an answer without checking it."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("Rounding 45 to the nearest 10, which do we get?", "45 کو قریب ترین 10 تک لانے پر کیا ملتا ہے؟"),
     "options": [
       opt("fifty", "50", "50", True, "Yes! A 5 rounds up.", "جی ہاں! 5 ہو تو اوپر جاتے ہیں۔"),
       opt("forty", "40", "40", False, "When the next digit is 5 or more, round up: 50.", "جب اگلا ہندسہ 5 یا زیادہ ہو تو اوپر جائیں: 50", "rounds_down_always"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Round 762 to the nearest 100.", "762 کو قریب ترین 100 تک لائیں۔"),
     QB,
     T("Look at the tens digit: 6.", "دہائی کا ہندسہ دیکھیں: 6"),
     T("Right! 800.", "درست! 800"),
     T("6 is 5 or more, so round up: 800.", "6، 5 یا زیادہ ہے، تو اوپر جائیں: 800"),
     common_wrong=[wrong(700, "The tens digit is 6, so round up to 800.", "دہائی کا ہندسہ 6 ہے، تو 800 تک اوپر جائیں۔", "rounds_down_always"),
                   wrong(760, "That is the nearest 10. To the nearest 100 it is 800.", "یہ قریب ترین 10 ہے۔ قریب ترین 100 تک 800 ہے۔", "wrong_place")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Kamran works out 19.8 × 5 and gets 9.9. How can an estimate show this is wrong?", "کامران 19.8 × 5 حل کرتا ہے اور اسے 9.9 ملتا ہے۔ اندازہ کیسے دکھاتا ہے کہ یہ غلط ہے؟"),
     "options": [
       opt("estimate", "19.8 is about 20, and 20 × 5 = 100, so 9.9 is far too small.", "19.8 تقریباً 20 ہے، اور 20 × 5 = 100، تو 9.9 بہت چھوٹا ہے۔", True,
           "Yes! The real answer is 99, close to 100.", "جی ہاں! اصل جواب 99 ہے، جو 100 کے قریب ہے۔"),
       opt("fine", "It looks fine.", "یہ ٹھیک لگتا ہے۔", False,
           "Estimate: 20 × 5 = 100. 9.9 is much too small.", "اندازہ: 20 × 5 = 100۔ 9.9 بہت چھوٹا ہے۔", "exact_not_estimate"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_round", "front": T("How to round?", "قریب ترین عدد کیسے؟"),
    "back": T("Look at the next digit: 5 or more, round up; 4 or less, round down.", "اگلا ہندسہ دیکھیں: 5 یا زیادہ تو اوپر؛ 4 یا کم تو نیچے۔")},
   {"id": "f_estimate", "front": T("Why estimate?", "اندازہ کیوں؟"),
    "back": T("To check an answer is about the right size.", "یہ جانچنے کے لیے کہ جواب تقریباً درست سائز کا ہے۔")},
 ],
 "home_tasks": [{"id": "h_bazaar", "text": T(
   "Next time your family buys a few things, round each price to the nearest 10 or 100 and estimate the total in your head. Then compare with the real bill.",
   "اگلی بار جب آپ کے گھر والے کچھ چیزیں خریدیں تو ہر قیمت کو قریب ترین 10 یا 100 تک لائیں اور دماغ میں کل کا اندازہ لگائیں۔ پھر اصل بل سے موازنہ کریں۔")}],
 "glossary": [T("Round", "قریب ترین عدد تک لانا"), T("Estimate", "اندازہ"), T("Nearest", "قریب ترین")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "The shopkeeper says Rs 198 + Rs 405 + Rs 99 is Rs 1700. Can we check quickly, without paper?",
                     "دکاندار کہتا ہے 198 + 405 + 99 روپے، 1700 روپے ہیں۔ کیا ہم کاغذ کے بغیر جلدی جانچ سکتے ہیں؟"),
    "text": T("Today we learn to round and estimate. First, a quick place value check.", "آج ہم قریب ترین عدد اور اندازہ سیکھیں گے۔ پہلے مقامی قیمت کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("In 4.75, which digit is in the tenths place?", "4.75 میں دسویں کے مقام پر کون سا ہندسہ ہے؟"),
     S2,
     T("The tenths place is the first digit after the point.", "دسواں مقام اعشاریہ کے بعد پہلا ہندسہ ہے۔"),
     T("Right! 7 tenths.", "درست! 7 دسویں"),
     T("4.75: 4 ones, 7 tenths, 5 hundredths.", "4.75: 4 اکائیاں، 7 دسویں، 5 سوویں"),
     common_wrong=[wrong(5, "5 is in the hundredths place. The tenths digit is 7.", "5 سوویں کے مقام پر ہے۔ دسویں کا ہندسہ 7 ہے۔")],
     qtype="recall", skill=DEC_PLACE_VALUE),
   {"id": "s3_round", "type": "explain",
    "character": say("happy", "Look one place to the right. 5 or more? Round up!", "ایک مقام دائیں دیکھیں۔ 5 یا زیادہ؟ اوپر جائیں!"),
    "text": T("To round to the nearest 100, look at the tens digit. If it is 5 or more, round up; if it is 4 or less, round down. 487 → 500, because the tens digit 8 is 5 or more. To estimate, round each number first, then work it out. An estimate tells you if an answer is about the right size.",
              "قریب ترین 100 تک لانے کے لیے دہائی کا ہندسہ دیکھیں۔ 5 یا زیادہ ہو تو اوپر جائیں؛ 4 یا کم ہو تو نیچے۔ 487 ← 500، کیونکہ دہائی کا ہندسہ 8 ہے۔ اندازے کے لیے پہلے ہر عدد کو قریب ترین تک لائیں، پھر حل کریں۔ اندازہ بتاتا ہے کہ جواب تقریباً درست سائز کا ہے یا نہیں۔")},
   number_question(
     "s4_round_100",
     T("Round 487 to the nearest 100.", "487 کو قریب ترین 100 تک لائیں۔"),
     S4,
     T("Look at the tens digit: 8.", "دہائی کا ہندسہ دیکھیں: 8"),
     T("Right! 500.", "درست! 500"),
     T("8 is 5 or more, so round up: 500.", "8، 5 یا زیادہ ہے، تو اوپر: 500"),
     common_wrong=[wrong(400, "The tens digit is 8, so round up to 500.", "دہائی کا ہندسہ 8 ہے، تو 500 تک اوپر جائیں۔", "rounds_down_always"),
                   wrong(490, "That is the nearest 10. To the nearest 100: 500.", "یہ قریب ترین 10 ہے۔ قریب ترین 100 تک: 500", "wrong_place")]),
   number_question(
     "s5_estimate_sum",
     T("Estimate 298 + 513 by rounding each number to the nearest 100.", "298 + 513 کا اندازہ لگائیں، ہر عدد کو قریب ترین 100 تک لا کر۔"),
     S5,
     T("298 → 300 and 513 → 500.", "298 ← 300 اور 513 ← 500"),
     T("Right! 300 + 500 = 800.", "درست! 300 + 500 = 800"),
     T("300 + 500 = 800. (The exact answer is 811.)", "300 + 500 = 800۔ (اصل جواب 811 ہے۔)"),
     common_wrong=[wrong(811, "That is the exact answer. The estimate is 300 + 500 = 800.", "یہ اصل جواب ہے۔ اندازہ 300 + 500 = 800 ہے۔", "exact_not_estimate"),
                   wrong(700, "298 rounds up to 300, not down to 200: 800.", "298، 300 تک اوپر جاتا ہے، 200 تک نیچے نہیں: 800", "rounds_down_always")]),
   {"id": "s6_about", "type": "choice",
    "prompt": T("About how much is 49 × 21?", "49 × 21 تقریباً کتنا ہے؟"),
    "options": [
      opt("thousand", "About 1000", "تقریباً 1000", True, "Yes! 50 × 20 = 1000. (Exactly 1029.)", "جی ہاں! 50 × 20 = 1000۔ (اصل 1029)"),
      opt("hundred", "About 100", "تقریباً 100", False, "50 × 20 is 1000, not 100.", "50 × 20 = 1000، 100 نہیں۔"),
      opt("ten_thousand", "About 10000", "تقریباً 10000", False, "50 × 20 is 1000, not 10000.", "50 × 20 = 1000، 10000 نہیں۔"),
    ]},
   number_question(
     "s7_decimals",
     T("Estimate 6.8 × 4.1 by rounding each number to the nearest whole number.", "6.8 × 4.1 کا اندازہ لگائیں، ہر عدد کو قریب ترین مکمل عدد تک لا کر۔"),
     S7,
     T("6.8 → 7 and 4.1 → 4.", "6.8 ← 7 اور 4.1 ← 4"),
     T("Right! 7 × 4 = 28.", "درست! 7 × 4 = 28"),
     T("7 × 4 = 28. (The exact answer is 27.88.)", "7 × 4 = 28۔ (اصل جواب 27.88 ہے۔)"),
     common_wrong=[wrong(24, "6.8 rounds up to 7, not down to 6: 7 × 4 = 28.", "6.8، 7 تک اوپر جاتا ہے، 6 تک نیچے نہیں: 7 × 4 = 28", "rounds_down_always")]),
   number_question(
     "s8_round_10",
     T("Round 3462 to the nearest 10.", "3462 کو قریب ترین 10 تک لائیں۔"),
     S8,
     T("Look at the ones digit: 2.", "اکائی کا ہندسہ دیکھیں: 2"),
     T("Right! 3460.", "درست! 3460"),
     T("2 is 4 or less, so round down: 3460.", "2، 4 یا کم ہے، تو نیچے: 3460"),
     common_wrong=[wrong(3500, "That is the nearest 100. To the nearest 10: 3460.", "یہ قریب ترین 100 ہے۔ قریب ترین 10 تک: 3460", "wrong_place"),
                   wrong(3470, "The ones digit is 2, so round down: 3460.", "اکائی کا ہندسہ 2 ہے، تو نیچے: 3460")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Hira works out 52 × 38 and gets 476. How can an estimate show it is wrong?", "حرا 52 × 38 حل کرتی ہے اور اسے 476 ملتا ہے۔ اندازہ کیسے دکھاتا ہے کہ یہ غلط ہے؟"),
    "options": [
      opt("estimate", "52 × 38 is about 50 × 40 = 2000, so 476 is far too small.", "52 × 38 تقریباً 50 × 40 = 2000 ہے، تو 476 بہت چھوٹا ہے۔", True,
          "Yes! The exact answer is 1976, close to 2000.", "جی ہاں! اصل جواب 1976 ہے، جو 2000 کے قریب ہے۔"),
      opt("fine", "It looks fine.", "یہ ٹھیک لگتا ہے۔", False,
          "Estimate: 50 × 40 = 2000. 476 is much too small.", "اندازہ: 50 × 40 = 2000۔ 476 بہت چھوٹا ہے۔", "exact_not_estimate"),
      opt("too_big", "476 is too big.", "476 بہت بڑا ہے۔", False,
          "It's the other way: the estimate 2000 is much bigger.", "الٹا ہے: اندازہ 2000 بہت بڑا ہے۔"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "If we can work out the exact answer, why bother estimating? Can you teach me?",
                     "اگر ہم اصل جواب نکال سکتے ہیں تو اندازہ کیوں لگائیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: how does an estimate help you, even when you can work out the exact answer?", "اپنے الفاظ میں بتائیں: اندازہ آپ کی مدد کیسے کرتا ہے، چاہے آپ اصل جواب نکال سکتے ہوں؟"),
    "key_idea": "An estimate is quick and easy to do in your head. It tells you roughly what size the answer should be, so you can catch big mistakes, like a wrong bill or a slip in working.",
    "levels": {
      "got_it": "Says an estimate is quick and shows roughly what the answer should be, so you can spot a big mistake.",
      "partly": "Says it is quick or easy, without saying it helps check answers.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["check", "mistake", "wrong", "جانچ", "غلطی", "غلط"],
      ["quick", "easy", "head", "جلدی", "آسان", "دماغ"],
      ["about", "roughly", "size", "تقریباً"]],
    "fallback_feedback": {
      "got_it": T("Well explained! An estimate quickly catches big mistakes.", "بہت خوب! اندازہ جلدی سے بڑی غلطیاں پکڑ لیتا ہے۔"),
      "partly": T("Good start! Now say how it helps you check an answer.", "اچھی شروعات! اب بتائیں یہ جواب جانچنے میں کیسے مدد کرتا ہے۔"),
      "not_yet": T("Think of the shopkeeper's bill of Rs 1700. How did an estimate help?", "دکاندار کے 1700 روپے کے بل کے بارے میں سوچیں۔ اندازے نے کیسے مدد کی؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_bill",
     T("Things cost Rs 198, Rs 405 and Rs 99. Round each price to the nearest 100 and estimate the total, in rupees.", "چیزوں کی قیمت 198، 405 اور 99 روپے ہے۔ ہر قیمت کو قریب ترین 100 تک لائیں اور کل کا اندازہ لگائیں، روپوں میں۔"),
     S11,
     T("198 → 200, 405 → 400, 99 → 100.", "198 ← 200، 405 ← 400، 99 ← 100"),
     T("Right! About Rs 700, so a bill of Rs 1700 is wrong.", "درست! تقریباً 700 روپے، تو 1700 روپے کا بل غلط ہے۔"),
     T("200 + 400 + 100 = 700. (Exactly Rs 702.)", "200 + 400 + 100 = 700۔ (اصل 702 روپے)"),
     common_wrong=[wrong(702, "That is the exact total. The estimate is 200 + 400 + 100 = 700.", "یہ اصل کل ہے۔ اندازہ 200 + 400 + 100 = 700 ہے۔", "exact_not_estimate"),
                   wrong(500, "198 rounds up to 200 and 99 up to 100: 700.", "198، 200 تک اور 99، 100 تک اوپر جاتا ہے: 700", "rounds_down_always")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can check any answer in your head!", "اب آپ کسی بھی جواب کو دماغ میں جانچ سکتے ہیں!"),
    "text": T("To round, look at the next digit to the right: 5 or more, round up; 4 or less, round down. To estimate, round each number first and then work it out. Use an estimate to check that an answer is about the right size.",
              "قریب ترین عدد کے لیے دائیں والا اگلا ہندسہ دیکھیں: 5 یا زیادہ تو اوپر؛ 4 یا کم تو نیچے۔ اندازے کے لیے پہلے ہر عدد کو قریب ترین تک لائیں، پھر حل کریں۔ اندازے سے جانچیں کہ جواب تقریباً درست سائز کا ہے۔"),
    "points": [T("5 or more: round up.", "5 یا زیادہ: اوپر۔"),
               T("Estimate to check answers.", "جواب جانچنے کے لیے اندازہ لگائیں۔")]},
 ],
 "review_questions": [
   {"id": "r_estimate", "type": "apply", "skill": SKILL, "step": number_question(
     "r_estimate",
     T("Estimate 612 − 289 by rounding each number to the nearest 100.", "612 − 289 کا اندازہ لگائیں، ہر عدد کو قریب ترین 100 تک لا کر۔"),
     R1,
     T("612 → 600 and 289 → 300.", "612 ← 600 اور 289 ← 300"),
     T("Right! 600 − 300 = 300.", "درست! 600 − 300 = 300"),
     T("600 − 300 = 300. (Exactly 323.)", "600 − 300 = 300۔ (اصل 323)"),
     common_wrong=[wrong(323, "That is the exact answer. The estimate is 600 − 300 = 300.", "یہ اصل جواب ہے۔ اندازہ 600 − 300 = 300 ہے۔", "exact_not_estimate"),
                   wrong(400, "289 rounds up to 300: 600 − 300 = 300.", "289، 300 تک اوپر جاتا ہے: 600 − 300 = 300", "rounds_down_always")],
     qtype=None)},
   {"id": "r_round", "type": "apply", "skill": SKILL, "step": number_question(
     "r_round",
     T("Round 45 to the nearest 10.", "45 کو قریب ترین 10 تک لائیں۔"),
     R2,
     T("The ones digit is 5.", "اکائی کا ہندسہ 5 ہے۔"),
     T("Right! 50.", "درست! 50"),
     T("5 rounds up: 50.", "5 ہو تو اوپر: 50"),
     common_wrong=[wrong(40, "A 5 rounds up: 50.", "5 ہو تو اوپر جائیں: 50", "rounds_down_always")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Simplification unit. No textbook text or exercises were used.",
   "Rounding follows the school rule: a 5 rounds up.",
   "Urdu terms to check: اندازہ (estimate), قریب ترین (nearest).",
   "The numbers were worked out in content/sources/g6-maths-13/estimation.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

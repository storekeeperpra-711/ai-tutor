from fractions import Fraction as F

from common import (D, T, opt, say, wrong, number_question, write,
                    REF, REVIEW, DEC_MULTIPLY_DIVIDE, FRACTIONS_MULTIPLY, SM_BRACKETS, SM_FRACTIONS_DECIMALS)

SKILL = SM_FRACTIONS_DECIMALS

# s2: 0.5 x 8
S2 = D("0.5") * 8
assert S2 == 4
# s4: 1/2 + 1/4 x 2 (left to right: 3/4 x 2 = 1.5)
assert (F(1, 2) + F(1, 4) * 2).denominator == 1
S4 = int(F(1, 2) + F(1, 4) * 2)
assert S4 == 1 and (F(1, 2) + F(1, 4)) * 2 == F(3, 2)
# s5: 2.5 + 1.5 x 4 (left to right: 16)
S5 = D("2.5") + D("1.5") * 4
assert S5 == D("8.5") and (D("2.5") + D("1.5")) * 4 == 16
# s6: (1/2 + 1/3) x 6 = 5; ignoring brackets 1/2 + 2 = 2.5
assert (F(1, 2) + F(1, 3)) * 6 == 5 and F(1, 2) + F(1, 3) * 6 == F(5, 2)
# s7: (0.6 + 0.4) x 7.5
S7 = (D("0.6") + D("0.4")) * D("7.5")
assert S7 == D("7.5")
# s8: 3/4 of (20 + 12)
assert (F(3, 4) * (20 + 12)).denominator == 1
S8 = int(F(3, 4) * (20 + 12))
assert S8 == 24 and F(3, 4) * 20 + 12 == 27
# s9: 1.2 + 0.8 x 5 is 5.2, not 10
assert D("1.2") + D("0.8") * 5 == D("5.2") and (D("1.2") + D("0.8")) * 5 == 10
# s11: 2.5 x 200 + 1/2 x 160 (forgetting the 1/2 gives 660)
S11 = D("2.5") * 200 + D("0.5") * 160
assert S11 == 580 and F(1, 2) * 160 == 80
# question bank and review
QB = D("4.5") - D("0.5") * 3
assert QB == 3 and (D("4.5") - D("0.5")) * 3 == 12
assert F(1, 2) * (10 + 6) == 8 and F(1, 2) * 10 + 6 == 11
R1 = (D("1.5") + D("2.5")) / 2
assert R1 == 2 and D("1.5") + D("2.5") / 2 == D("2.75")
assert (F(1, 3) * 9 + 2).denominator == 1
R2 = int(F(1, 3) * 9 + 2)
assert R2 == 5

lesson = {
 "id": "g6-maths-13-fractions-decimals",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Simplify expressions with fractions and decimals using BODMAS, reading 'of' as multiplication.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Simplifying with fractions and decimals", "کسور اور اعشاریہ کے ساتھ مختصر کرنا"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": SM_BRACKETS}, {"skill": DEC_MULTIPLY_DIVIDE}, {"skill": FRACTIONS_MULTIPLY}],
 "misconceptions": [
   {"id": "left_to_right_all", "description": "Forgets BODMAS when the numbers are fractions or decimals and works left to right."},
   {"id": "of_only_first", "description": "Applies 'of' to the first number only instead of the whole bracket."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_of", "type": "recall", "step": {
     "id": "qb_of", "type": "choice",
     "prompt": T("What does 'of' mean in '1/2 of 10'?", "'10 کا 1/2' میں 'کا' کا کیا مطلب ہے؟"),
     "options": [
       opt("times", "Multiply: 1/2 × 10", "ضرب: 1/2 × 10", True,
           "Yes! 1/2 of 10 = 1/2 × 10 = 5.", "جی ہاں! 10 کا 1/2 = 1/2 × 10 = 5"),
       opt("plus", "Add: 1/2 + 10", "جمع: 1/2 + 10", False,
           "'Of' means multiply: 1/2 × 10 = 5.", "'کا' کا مطلب ضرب ہے: 1/2 × 10 = 5"),
       opt("divide", "Divide: 1/2 ÷ 10", "تقسیم: 1/2 ÷ 10", False,
           "'Of' means multiply: half of 10 is 5.", "'کا' کا مطلب ضرب ہے: 10 کا آدھا 5 ہے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Simplify: 4.5 − 0.5 × 3", "مختصر کریں: 4.5 − 0.5 × 3"),
     QB,
     T("Do 0.5 × 3 first.", "پہلے 0.5 × 3 کریں۔"),
     T("Right! 4.5 − 1.5 = 3.", "درست! 4.5 − 1.5 = 3"),
     T("0.5 × 3 = 1.5, then 4.5 − 1.5 = 3.", "0.5 × 3 = 1.5، پھر 4.5 − 1.5 = 3"),
     common_wrong=[wrong(12, "That subtracts first. Multiply first: 4.5 − 1.5 = 3.", "یہ پہلے تفریق ہے۔ پہلے ضرب: 4.5 − 1.5 = 3", "left_to_right_all")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Rida writes 1/2 of (10 + 6) = 5 + 6 = 11. What is wrong?", "ردا لکھتی ہے: (10 + 6) کا 1/2 = 5 + 6 = 11۔ کیا غلطی ہے؟"),
     "options": [
       opt("bracket", "She should add first: 1/2 of 16 = 8.", "اسے پہلے جمع کرنا چاہیے: 16 کا 1/2 = 8", True,
           "Yes! 'Of' applies to the whole bracket.", "جی ہاں! 'کا' پوری قوسین پر لگتا ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "She halved only the 10. Half of the whole 16 is 8.", "اس نے صرف 10 کا آدھا لیا۔ پورے 16 کا آدھا 8 ہے۔", "of_only_first"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_of", "front": T("'of' in maths?", "ریاضی میں 'کا'؟"),
    "back": T("Multiply. 3/4 of 32 = 3/4 × 32 = 24.", "ضرب۔ 32 کا 3/4 = 3/4 × 32 = 24")},
   {"id": "f_same_rules", "front": T("BODMAS with decimals?", "اعشاریہ کے ساتھ BODMAS؟"),
    "back": T("Same rules: brackets, then × ÷, then + −.", "وہی قاعدے: قوسین، پھر × ÷، پھر + −۔")},
 ],
 "home_tasks": [{"id": "h_recipe", "text": T(
   "Find a recipe at home, or make one up. If you make 1/2 of it for 4 people and then add 2 extra rotis, write the number sentence and simplify it.",
   "گھر میں کوئی ترکیب دیکھیں یا خود بنائیں۔ اگر آپ 4 لوگوں کے لیے اس کا 1/2 بنائیں اور پھر 2 روٹیاں زیادہ، تو عددی جملہ لکھیں اور اسے مختصر کریں۔")}],
 "glossary": [T("Of (multiply)", "کا (ضرب)"), T("Fraction", "کسر"), T("Decimal", "اعشاریہ")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Does BODMAS still work with fractions and decimals? Let's find out!",
                     "کیا BODMAS کسور اور اعشاریہ کے ساتھ بھی چلتا ہے؟ آئیں دیکھیں!"),
    "text": T("Today we simplify with fractions and decimals. First, a quick decimal check.", "آج ہم کسور اور اعشاریہ کے ساتھ مختصر کریں گے۔ پہلے اعشاریہ کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("0.5 × 8 = ?", "0.5 × 8 = ?"),
     S2,
     T("0.5 is half.", "0.5 یعنی آدھا۔"),
     T("Right! 4.", "درست! 4"),
     T("Half of 8 is 4.", "8 کا آدھا 4 ہے۔"),
     common_wrong=[wrong(40, "0.5 is half, not 5: 0.5 × 8 = 4.", "0.5 آدھا ہے، 5 نہیں: 0.5 × 8 = 4")],
     qtype="recall", skill=DEC_MULTIPLY_DIVIDE),
   {"id": "s3_same_rules", "type": "explain",
    "character": say("happy", "Same rules as before! And 'of' just means multiply.", "وہی پرانے قاعدے! اور 'کا' کا مطلب صرف ضرب ہے۔"),
    "text": T("BODMAS works the same for fractions and decimals: brackets, then × and ÷, then + and −. The word 'of' means multiply, so 3/4 of 32 = 3/4 × 32 = 24. When 'of' comes before a bracket, work out the bracket first.",
              "BODMAS کسور اور اعشاریہ کے لیے بھی ویسے ہی چلتا ہے: قوسین، پھر × اور ÷، پھر + اور −۔ لفظ 'کا' کا مطلب ضرب ہے، تو 32 کا 3/4 = 3/4 × 32 = 24۔ جب 'کا' قوسین سے پہلے آئے تو پہلے قوسین حل کریں۔")},
   number_question(
     "s4_fraction",
     T("Simplify: 1/2 + 1/4 × 2", "مختصر کریں: 1/2 + 1/4 × 2"),
     S4,
     T("Do 1/4 × 2 first.", "پہلے 1/4 × 2 کریں۔"),
     T("Right! 1/2 + 1/2 = 1.", "درست! 1/2 + 1/2 = 1"),
     T("1/4 × 2 = 1/2, then 1/2 + 1/2 = 1.", "1/4 × 2 = 1/2، پھر 1/2 + 1/2 = 1"),
     common_wrong=[wrong(D("1.5"), "That adds first. Multiply first: 1/2 + 1/2 = 1.", "یہ پہلے جمع ہے۔ پہلے ضرب: 1/2 + 1/2 = 1", "left_to_right_all")]),
   number_question(
     "s5_decimal",
     T("Simplify: 2.5 + 1.5 × 4", "مختصر کریں: 2.5 + 1.5 × 4"),
     S5,
     T("Do 1.5 × 4 first.", "پہلے 1.5 × 4 کریں۔"),
     T("Right! 2.5 + 6 = 8.5.", "درست! 2.5 + 6 = 8.5"),
     T("1.5 × 4 = 6, then 2.5 + 6 = 8.5.", "1.5 × 4 = 6، پھر 2.5 + 6 = 8.5"),
     common_wrong=[wrong(16, "That adds first. Multiply first: 2.5 + 6 = 8.5.", "یہ پہلے جمع ہے۔ پہلے ضرب: 2.5 + 6 = 8.5", "left_to_right_all")]),
   {"id": "s6_choose", "type": "choice",
    "prompt": T("What is (1/2 + 1/3) × 6?", "(1/2 + 1/3) × 6 کتنا ہے؟"),
    "options": [
      opt("five", "5", "5", True, "Yes! 1/2 × 6 + 1/3 × 6 = 3 + 2 = 5, or 5/6 × 6 = 5.", "جی ہاں! 5/6 × 6 = 5"),
      opt("two_half", "2 1/2", "2 1/2", False, "That ignores the brackets. (5/6) × 6 = 5.", "یہ قوسین نظر انداز کرتا ہے۔ (5/6) × 6 = 5"),
      opt("three", "3", "3", False, "Multiply the whole bracket, not just 1/2: 5/6 × 6 = 5.", "صرف 1/2 کو نہیں، پوری قوسین کو ضرب دیں: 5/6 × 6 = 5", "of_only_first"),
    ]},
   number_question(
     "s7_decimal_bracket",
     T("Simplify: (0.6 + 0.4) × 7.5", "مختصر کریں: (0.6 + 0.4) × 7.5"),
     S7,
     T("Brackets first: 0.6 + 0.4 = 1.", "پہلے قوسین: 0.6 + 0.4 = 1"),
     T("Right! 1 × 7.5 = 7.5.", "درست! 1 × 7.5 = 7.5"),
     T("0.6 + 0.4 = 1, then 1 × 7.5 = 7.5.", "0.6 + 0.4 = 1، پھر 1 × 7.5 = 7.5"),
     common_wrong=[wrong(D("3.6"), "That ignores the brackets: (1) × 7.5 = 7.5.", "یہ قوسین نظر انداز کرتا ہے: (1) × 7.5 = 7.5")]),
   number_question(
     "s8_of",
     T("Simplify: 3/4 of (20 + 12)", "مختصر کریں: (20 + 12) کا 3/4"),
     S8,
     T("Brackets first, then 3/4 × 32.", "پہلے قوسین، پھر 3/4 × 32"),
     T("Right! 3/4 × 32 = 24.", "درست! 3/4 × 32 = 24"),
     T("20 + 12 = 32. 32 ÷ 4 = 8, 8 × 3 = 24.", "20 + 12 = 32۔ 32 ÷ 4 = 8، 8 × 3 = 24"),
     common_wrong=[wrong(27, "'Of' applies to the whole bracket: 3/4 of 32 = 24.", "'کا' پوری قوسین پر لگتا ہے: 32 کا 3/4 = 24", "of_only_first")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal simplifies 1.2 + 0.8 × 5 like this: 1.2 + 0.8 = 2, then 2 × 5 = 10. What went wrong?", "بلال 1.2 + 0.8 × 5 ایسے مختصر کرتا ہے: 1.2 + 0.8 = 2، پھر 2 × 5 = 10۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("times", "He should multiply first: 0.8 × 5 = 4, so 1.2 + 4 = 5.2.", "اسے پہلے ضرب دینی چاہیے: 0.8 × 5 = 4، تو 1.2 + 4 = 5.2", True,
          "Yes! BODMAS works the same with decimals.", "جی ہاں! BODMAS اعشاریہ کے ساتھ بھی ویسے ہی چلتا ہے۔"),
      opt("nothing", "Nothing, decimals are worked left to right.", "کوئی غلطی نہیں، اعشاریہ بائیں سے دائیں حل ہوتے ہیں۔", False,
          "The rules don't change for decimals. × before +: 5.2.", "اعشاریہ کے لیے قاعدے نہیں بدلتے۔ × پہلے، + بعد میں: 5.2", "left_to_right_all"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is 3/4 of (20 + 12) not the same as 3/4 of 20, plus 12? Can you teach me?",
                     "(20 + 12) کا 3/4، 20 کے 3/4 جمع 12 جیسا کیوں نہیں ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we add 20 + 12 first in 3/4 of (20 + 12)?", "اپنے الفاظ میں بتائیں: (20 + 12) کا 3/4 میں ہم پہلے 20 + 12 کیوں جمع کرتے ہیں؟"),
    "key_idea": "The bracket groups 20 and 12 into one amount, 32. 'Of' means we take 3/4 of that whole amount, so 3/4 × 32 = 24. Taking 3/4 of only the 20 leaves the 12 out.",
    "levels": {
      "got_it": "Says the bracket makes one amount (32), and 'of' means we take 3/4 of all of it, not just of the 20.",
      "partly": "Says brackets come first, without saying 'of' applies to the whole amount.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["bracket", "قوسین"],
      ["whole", "all", "32", "پورا", "سارا"],
      ["of", "multiply", "ضرب", "کا"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 'Of' applies to the whole amount inside the bracket.", "بہت خوب! 'کا' قوسین کے اندر پوری رقم پر لگتا ہے۔"),
      "partly": T("Good start! Now say what 'of' is taking 3/4 of.", "اچھی شروعات! اب بتائیں 'کا' کس چیز کا 3/4 لے رہا ہے۔"),
      "not_yet": T("Imagine Rs 20 and Rs 12 in one purse. What is 3/4 of all the money in the purse?", "سوچیں ایک بٹوے میں 20 روپے اور 12 روپے ہیں۔ بٹوے کے سارے پیسوں کا 3/4 کتنا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_shopping",
     T("Ammi buys 2.5 kg of rice at Rs 200 a kg and 1/2 kg of sugar at Rs 160 a kg. The total is 2.5 × 200 + 1/2 × 160. How many rupees is that?", "امی 200 روپے فی کلو کے حساب سے 2.5 کلو چاول اور 160 روپے فی کلو کے حساب سے 1/2 کلو چینی خریدتی ہیں۔ کل 2.5 × 200 + 1/2 × 160 ہے۔ یہ کتنے روپے ہیں؟"),
     S11,
     T("Do both × first: 500 and 80.", "پہلے دونوں ضرب کریں: 500 اور 80"),
     T("Right! 500 + 80 = Rs 580.", "درست! 500 + 80 = 580 روپے"),
     T("2.5 × 200 = 500, 1/2 × 160 = 80, 500 + 80 = 580.", "2.5 × 200 = 500، 1/2 × 160 = 80، 500 + 80 = 580"),
     common_wrong=[wrong(660, "Only half a kg of sugar: 1/2 × 160 = 80, so 500 + 80 = 580.", "چینی صرف آدھا کلو ہے: 1/2 × 160 = 80، تو 500 + 80 = 580")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Fractions, decimals, brackets: BODMAS handles them all!", "کسور، اعشاریہ، قوسین: BODMAS سب سنبھال لیتا ہے!"),
    "text": T("BODMAS is the same for fractions and decimals. 'Of' means multiply. When 'of' comes before brackets, work out the brackets first, then take the fraction of the whole amount.",
              "کسور اور اعشاریہ کے لیے BODMAS وہی ہے۔ 'کا' کا مطلب ضرب ہے۔ جب 'کا' قوسین سے پہلے آئے تو پہلے قوسین حل کریں، پھر پوری رقم کی کسر لیں۔"),
    "points": [T("'Of' means ×.", "'کا' کا مطلب × ہے۔"),
               T("Same BODMAS rules.", "وہی BODMAS قاعدے۔")]},
 ],
 "review_questions": [
   {"id": "r_decimal", "type": "apply", "skill": SKILL, "step": number_question(
     "r_decimal",
     T("Simplify: (1.5 + 2.5) ÷ 2", "مختصر کریں: (1.5 + 2.5) ÷ 2"),
     R1,
     T("Brackets first: 1.5 + 2.5 = 4.", "پہلے قوسین: 1.5 + 2.5 = 4"),
     T("Right! 4 ÷ 2 = 2.", "درست! 4 ÷ 2 = 2"),
     T("1.5 + 2.5 = 4, then 4 ÷ 2 = 2.", "1.5 + 2.5 = 4، پھر 4 ÷ 2 = 2"),
     common_wrong=[wrong(D("2.75"), "That ignores the brackets: 4 ÷ 2 = 2.", "یہ قوسین نظر انداز کرتا ہے: 4 ÷ 2 = 2")],
     qtype=None)},
   {"id": "r_fraction", "type": "apply", "skill": SKILL, "step": number_question(
     "r_fraction",
     T("Simplify: 1/3 × 9 + 2", "مختصر کریں: 1/3 × 9 + 2"),
     R2,
     T("Do 1/3 × 9 first.", "پہلے 1/3 × 9 کریں۔"),
     T("Right! 3 + 2 = 5.", "درست! 3 + 2 = 5"),
     T("1/3 × 9 = 3, then 3 + 2 = 5.", "1/3 × 9 = 3، پھر 3 + 2 = 5"),
     common_wrong=[wrong(3, "Don't forget the + 2: 3 + 2 = 5.", "+ 2 نہ بھولیں: 3 + 2 = 5")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Simplification unit. No textbook text or exercises were used.",
   "Every answer is a whole number or a simple decimal, so children type no fractions.",
   "Urdu terms to check: 'کا' as the word for 'of' (multiply).",
   "The numbers were worked out in content/sources/g6-maths-13/fractions_decimals.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

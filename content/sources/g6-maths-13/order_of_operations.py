from common import (D, T, opt, say, wrong, number_question, write,
                    REF, REVIEW, INT_MULTIPLY_DIVIDE, SM_ORDER)

SKILL = SM_ORDER

# s2: (-4) x 5
S2 = -4 * 5
assert S2 == -20
# s4: 3 + 4 x 5 (left to right would give 35)
S4 = 3 + 4 * 5
assert S4 == 23 and (3 + 4) * 5 == 35
# s5: 20 - 12 / 4 (left to right would give 2)
S5 = 20 - 12 // 4
assert S5 == 17 and (20 - 12) // 4 == 2
# s7: 40 / 8 x 2, left to right (right to left gives 2.5)
S7 = 40 // 8 * 2
assert S7 == 10
# s8: 30 - 10 + 5, left to right (right to left gives 15)
S8 = 30 - 10 + 5
assert S8 == 25 and 30 - (10 + 5) == 15
# s9: 6 + 6 / 3 is 8, not (6 + 6) / 3 = 4
assert 6 + 6 // 3 == 8 and (6 + 6) // 3 == 4
# s11: 25 + 3 x 40
S11 = 25 + 3 * 40
assert S11 == 145 and (25 + 3) * 40 == 1120
# question bank and review
QB = 7 + 2 * 6
assert QB == 19 and (7 + 2) * 6 == 54
assert 10 - 4 // 2 == 8 and (10 - 4) // 2 == 3
R1 = 50 - 5 * 6
assert R1 == 20 and (50 - 5) * 6 == 270
R2 = 5 + 36 // 4
assert R2 == 14

lesson = {
 "id": "g6-maths-13-order-of-operations",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Simplify expressions with +, −, × and ÷ using the correct order of operations.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Order of operations", "عملیات کی ترتیب"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": INT_MULTIPLY_DIVIDE}],
 "misconceptions": [
   {"id": "left_to_right_all", "description": "Works strictly from left to right, doing + or − before × or ÷."},
   {"id": "add_before_subtract", "description": "Always adds before subtracting (or multiplies before dividing) instead of going left to right."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("In 9 − 3 × 2, what do you do first?", "9 − 3 × 2 میں پہلے کیا کرتے ہیں؟"),
     "options": [
       opt("times", "3 × 2", "3 × 2", True,
           "Yes! × and ÷ come before + and −. 9 − 6 = 3.", "جی ہاں! × اور ÷ پہلے، + اور − بعد میں۔ 9 − 6 = 3"),
       opt("minus", "9 − 3", "9 − 3", False,
           "Multiplication comes before subtraction.", "ضرب تفریق سے پہلے آتی ہے۔", "left_to_right_all"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Simplify: 7 + 2 × 6", "مختصر کریں: 7 + 2 × 6"),
     QB,
     T("Do 2 × 6 first.", "پہلے 2 × 6 کریں۔"),
     T("Right! 7 + 12 = 19.", "درست! 7 + 12 = 19"),
     T("2 × 6 = 12, then 7 + 12 = 19.", "2 × 6 = 12، پھر 7 + 12 = 19"),
     common_wrong=[wrong(54, "That adds first. Multiply first: 7 + 12 = 19.", "یہ پہلے جمع ہے۔ پہلے ضرب: 7 + 12 = 19", "left_to_right_all")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Hamza works out 10 − 4 ÷ 2 = 6 ÷ 2 = 3. What is wrong?", "حمزہ 10 − 4 ÷ 2 = 6 ÷ 2 = 3 نکالتا ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("divide", "He should divide first: 4 ÷ 2 = 2, so 10 − 2 = 8.", "اسے پہلے تقسیم کرنی چاہیے: 4 ÷ 2 = 2، تو 10 − 2 = 8", True,
           "Yes! ÷ comes before −.", "جی ہاں! ÷، − سے پہلے آتا ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "He subtracted first. Divide first: 10 − 2 = 8.", "اس نے پہلے تفریق کی۔ پہلے تقسیم: 10 − 2 = 8", "left_to_right_all"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_order", "front": T("Which first: × ÷ or + −?", "پہلے کون: × ÷ یا + −؟"),
    "back": T("× and ÷ first, then + and −.", "پہلے × اور ÷، پھر + اور −۔")},
   {"id": "f_same", "front": T("Two of the same level, like − and +?", "ایک ہی درجے کے دو، جیسے − اور +؟"),
    "back": T("Work from left to right.", "بائیں سے دائیں حل کریں۔")},
 ],
 "home_tasks": [{"id": "h_puzzle", "text": T(
   "Write 2 + 3 × 4 on a paper and ask someone at home to work it out. Did they get 14 or 20? Explain the rule to them.",
   "کاغذ پر 2 + 3 × 4 لکھیں اور گھر میں کسی سے حل کروائیں۔ کیا انہیں 14 ملا یا 20؟ انہیں قاعدہ سمجھائیں۔")}],
 "glossary": [T("Order of operations", "عملیات کی ترتیب"), T("Simplify", "مختصر کرنا"), T("Expression", "عبارت")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Aisha says 3 + 4 × 5 is 35. Bilal says 23. Who is right?",
                     "عائشہ کہتی ہے 3 + 4 × 5 کا جواب 35 ہے۔ بلال کہتا ہے 23۔ کون درست ہے؟"),
    "text": T("Today we learn the order to do + − × ÷ in. First, a quick check.", "آج ہم سیکھیں گے کہ + − × ÷ کس ترتیب سے کرتے ہیں۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("(−4) × 5 = ?", "(−4) × 5 = ?"),
     S2,
     T("A negative times a positive is negative.", "منفی ضرب مثبت، منفی ہوتا ہے۔"),
     T("Right! −20.", "درست! −20"),
     T("4 × 5 = 20, and the sign is negative: −20.", "4 × 5 = 20، اور علامت منفی ہے: −20"),
     common_wrong=[wrong(20, "Keep the sign: negative × positive = negative, −20.", "علامت رکھیں: منفی × مثبت = منفی، −20")],
     qtype="recall", skill=INT_MULTIPLY_DIVIDE),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Times and divide first. Then add and take away. Same level? Left to right!", "ضرب اور تقسیم پہلے۔ پھر جمع اور تفریق۔ ایک ہی درجہ؟ بائیں سے دائیں!"),
    "text": T("Everyone agrees on one order so that a sum has only one answer. 1) Do × and ÷, going from left to right. 2) Then do + and −, going from left to right. So 3 + 4 × 5 = 3 + 20 = 23. Bilal is right.",
              "سب ایک ہی ترتیب مانتے ہیں تاکہ سوال کا ایک ہی جواب ہو۔ 1) × اور ÷ کریں، بائیں سے دائیں۔ 2) پھر + اور − کریں، بائیں سے دائیں۔ تو 3 + 4 × 5 = 3 + 20 = 23۔ بلال درست ہے۔")},
   number_question(
     "s4_times_first",
     T("Simplify: 3 + 4 × 5", "مختصر کریں: 3 + 4 × 5"),
     S4,
     T("Do 4 × 5 first.", "پہلے 4 × 5 کریں۔"),
     T("Right! 3 + 20 = 23.", "درست! 3 + 20 = 23"),
     T("4 × 5 = 20, then 3 + 20 = 23.", "4 × 5 = 20، پھر 3 + 20 = 23"),
     common_wrong=[wrong(35, "That adds first. Multiply first: 3 + 20 = 23.", "یہ پہلے جمع ہے۔ پہلے ضرب: 3 + 20 = 23", "left_to_right_all")]),
   number_question(
     "s5_divide_first",
     T("Simplify: 20 − 12 ÷ 4", "مختصر کریں: 20 − 12 ÷ 4"),
     S5,
     T("Do 12 ÷ 4 first.", "پہلے 12 ÷ 4 کریں۔"),
     T("Right! 20 − 3 = 17.", "درست! 20 − 3 = 17"),
     T("12 ÷ 4 = 3, then 20 − 3 = 17.", "12 ÷ 4 = 3، پھر 20 − 3 = 17"),
     common_wrong=[wrong(2, "That subtracts first. Divide first: 20 − 3 = 17.", "یہ پہلے تفریق ہے۔ پہلے تقسیم: 20 − 3 = 17", "left_to_right_all")]),
   {"id": "s6_which_first", "type": "choice",
    "prompt": T("In 18 − 6 × 2, which part do you work out first?", "18 − 6 × 2 میں کون سا حصہ پہلے حل کرتے ہیں؟"),
    "options": [
      opt("times", "6 × 2", "6 × 2", True, "Yes! Then 18 − 12 = 6.", "جی ہاں! پھر 18 − 12 = 6"),
      opt("minus", "18 − 6", "18 − 6", False, "× comes before −. Do 6 × 2 first.", "×، − سے پہلے آتا ہے۔ پہلے 6 × 2 کریں۔", "left_to_right_all"),
    ]},
   number_question(
     "s7_left_to_right",
     T("Simplify: 40 ÷ 8 × 2", "مختصر کریں: 40 ÷ 8 × 2"),
     S7,
     T("÷ and × are the same level. Go left to right: 40 ÷ 8 first.", "÷ اور × ایک ہی درجے کے ہیں۔ بائیں سے دائیں: پہلے 40 ÷ 8"),
     T("Right! 5 × 2 = 10.", "درست! 5 × 2 = 10"),
     T("40 ÷ 8 = 5, then 5 × 2 = 10.", "40 ÷ 8 = 5، پھر 5 × 2 = 10"),
     common_wrong=[wrong(D("2.5"), "Don't multiply first. Left to right: 40 ÷ 8 = 5, then 5 × 2 = 10.", "پہلے ضرب نہ کریں۔ بائیں سے دائیں: 40 ÷ 8 = 5، پھر 5 × 2 = 10", "add_before_subtract")]),
   number_question(
     "s8_minus_plus",
     T("Simplify: 30 − 10 + 5", "مختصر کریں: 30 − 10 + 5"),
     S8,
     T("− and + are the same level. Go left to right.", "− اور + ایک ہی درجے کے ہیں۔ بائیں سے دائیں حل کریں۔"),
     T("Right! 20 + 5 = 25.", "درست! 20 + 5 = 25"),
     T("30 − 10 = 20, then 20 + 5 = 25.", "30 − 10 = 20، پھر 20 + 5 = 25"),
     common_wrong=[wrong(15, "Don't add first. Left to right: 30 − 10 = 20, then 20 + 5 = 25.", "پہلے جمع نہ کریں۔ بائیں سے دائیں: 30 − 10 = 20، پھر 20 + 5 = 25", "add_before_subtract")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Sana works out 6 + 6 ÷ 3 like this: 6 + 6 = 12, then 12 ÷ 3 = 4. What went wrong?", "ثنا 6 + 6 ÷ 3 ایسے حل کرتی ہے: 6 + 6 = 12، پھر 12 ÷ 3 = 4۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("divide", "She should divide first: 6 ÷ 3 = 2, so 6 + 2 = 8.", "اسے پہلے تقسیم کرنی چاہیے: 6 ÷ 3 = 2، تو 6 + 2 = 8", True,
          "Yes! ÷ comes before +.", "جی ہاں! ÷، + سے پہلے آتا ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "She added first. ÷ comes before +, so the answer is 8.", "اس نے پہلے جمع کیا۔ ÷، + سے پہلے آتا ہے، تو جواب 8 ہے۔", "left_to_right_all"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why does everyone need to follow the same order? Can you teach me?",
                     "سب کو ایک ہی ترتیب کیوں ماننی چاہیے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we all agree to do × and ÷ before + and −?", "اپنے الفاظ میں بتائیں: ہم سب × اور ÷ کو + اور − سے پہلے کرنے پر کیوں متفق ہیں؟"),
    "key_idea": "If people worked in different orders, the same sum would give different answers (3 + 4 × 5 could be 23 or 35). One agreed order means everyone gets the same answer.",
    "levels": {
      "got_it": "Says without one agreed order, the same sum could give different answers, so everyone follows one rule to get the same answer.",
      "partly": "Says it is the rule, or that the answer changes, but not both.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["same", "one", "ایک", "ایک جیسا"],
      ["answer", "جواب"],
      ["different", "change", "مختلف", "بدل"]],
    "fallback_feedback": {
      "got_it": T("Well explained! One order means one answer for everyone.", "بہت خوب! ایک ترتیب کا مطلب ہے سب کے لیے ایک جواب۔"),
      "partly": T("Good start! Now say what would happen to the answer if people used different orders.", "اچھی شروعات! اب بتائیں اگر لوگ مختلف ترتیب استعمال کریں تو جواب کا کیا ہوگا۔"),
      "not_yet": T("Work out 3 + 4 × 5 adding first, then multiplying first. Do you get the same answer?", "3 + 4 × 5 پہلے جمع کر کے، پھر پہلے ضرب کر کے حل کریں۔ کیا ایک ہی جواب آتا ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_shopping",
     T("Ali buys a pen for Rs 25 and 3 notebooks at Rs 40 each. The total is 25 + 3 × 40. How many rupees is that?", "علی 25 روپے کا ایک قلم اور 40 روپے فی کاپی کے حساب سے 3 کاپیاں خریدتا ہے۔ کل 25 + 3 × 40 ہے۔ یہ کتنے روپے ہیں؟"),
     S11,
     T("Do 3 × 40 first.", "پہلے 3 × 40 کریں۔"),
     T("Right! 25 + 120 = Rs 145.", "درست! 25 + 120 = 145 روپے"),
     T("3 × 40 = 120, then 25 + 120 = 145.", "3 × 40 = 120، پھر 25 + 120 = 145"),
     common_wrong=[wrong(1120, "That adds first. 3 notebooks cost 120, so 25 + 120 = 145.", "یہ پہلے جمع ہے۔ 3 کاپیاں 120 کی ہیں، تو 25 + 120 = 145", "left_to_right_all")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you know the order, so you get the same answer as everyone!", "اب آپ ترتیب جانتے ہیں، اس لیے آپ کا جواب سب جیسا آئے گا!"),
    "text": T("First do × and ÷, from left to right. Then do + and −, from left to right. This order gives every sum one answer.",
              "پہلے × اور ÷ کریں، بائیں سے دائیں۔ پھر + اور − کریں، بائیں سے دائیں۔ یہ ترتیب ہر سوال کو ایک جواب دیتی ہے۔"),
    "points": [T("× ÷ before + −.", "× ÷ پہلے، + − بعد میں۔"),
               T("Same level: left to right.", "ایک ہی درجہ: بائیں سے دائیں۔")]},
 ],
 "review_questions": [
   {"id": "r_times", "type": "apply", "skill": SKILL, "step": number_question(
     "r_times",
     T("Simplify: 50 − 5 × 6", "مختصر کریں: 50 − 5 × 6"),
     R1,
     T("Do 5 × 6 first.", "پہلے 5 × 6 کریں۔"),
     T("Right! 50 − 30 = 20.", "درست! 50 − 30 = 20"),
     T("5 × 6 = 30, then 50 − 30 = 20.", "5 × 6 = 30، پھر 50 − 30 = 20"),
     common_wrong=[wrong(270, "That subtracts first. Multiply first: 50 − 30 = 20.", "یہ پہلے تفریق ہے۔ پہلے ضرب: 50 − 30 = 20", "left_to_right_all")],
     qtype=None)},
   {"id": "r_divide", "type": "apply", "skill": SKILL, "step": number_question(
     "r_divide",
     T("Simplify: 5 + 36 ÷ 4", "مختصر کریں: 5 + 36 ÷ 4"),
     R2,
     T("Do 36 ÷ 4 first.", "پہلے 36 ÷ 4 کریں۔"),
     T("Right! 5 + 9 = 14.", "درست! 5 + 9 = 14"),
     T("36 ÷ 4 = 9, then 5 + 9 = 14.", "36 ÷ 4 = 9، پھر 5 + 9 = 14"),
     common_wrong=[wrong(D("10.25"), "That adds first: (5 + 36) ÷ 4. Divide first: 5 + 9 = 14.", "یہ پہلے جمع ہے: (5 + 36) ÷ 4۔ پہلے تقسیم: 5 + 9 = 14", "left_to_right_all")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Simplification unit. No textbook text or exercises were used.",
   "Brackets come in the next lesson; this lesson only uses + − × ÷.",
   "Urdu terms to check: عملیات کی ترتیب (order of operations), مختصر کرنا (simplify).",
   "The numbers were worked out in content/sources/g6-maths-13/order_of_operations.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

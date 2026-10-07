from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SM_ORDER, SM_BRACKETS)

SKILL = SM_BRACKETS

# s2: 8 + 2 x 3
S2 = 8 + 2 * 3
assert S2 == 14
# s4: (8 + 2) x 3
S4 = (8 + 2) * 3
assert S4 == 30
# s5: 24 / (2 + 4) (without brackets 24 / 2 + 4 = 16)
S5 = 24 // (2 + 4)
assert S5 == 4 and 24 // 2 + 4 == 16
# s7: 50 - {6 x (3 + 2)}
S7 = 50 - (6 * (3 + 2))
assert S7 == 20
# s8: [20 - (4 + 6)] x 2 (ignoring brackets: 20 - 4 + 6 x 2 = 28)
S8 = (20 - (4 + 6)) * 2
assert S8 == 20 and 20 - 4 + 6 * 2 == 28
# s9: 3 x (4 + 5) is 27, not 3 x 4 + 5 = 17
assert 3 * (4 + 5) == 27 and 3 * 4 + 5 == 17
# s11: (150 + 90) / 3 (without brackets 150 + 90 / 3 = 180)
S11 = (150 + 90) // 3
assert S11 == 80 and 150 + 90 // 3 == 180
# question bank and review
QB = (9 - 3) * 4
assert QB == 24 and 9 - 3 * 4 == -3
assert 2 * (5 + 3) == 16 and 2 * 5 + 3 == 13
R1 = 60 // (5 + 7)
assert R1 == 5
R2 = (12 - (2 * 3)) + 4
assert R2 == 10

lesson = {
 "id": "g6-maths-13-brackets",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Simplify expressions with brackets ( ), { } and [ ] using BODMAS, working from the inside out.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Brackets and BODMAS", "قوسین اور BODMAS"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": SM_ORDER}],
 "misconceptions": [
   {"id": "ignores_brackets", "description": "Ignores the brackets and uses only × ÷ before + −."},
   {"id": "partial_distribute", "description": "Multiplies only the first number inside the brackets (3 × (4 + 5) = 12 + 5)."},
   {"id": "outside_first", "description": "Works the outer brackets before the inner ones."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("In [10 − {2 × (1 + 3)}], which part do you work out first?", "[10 − {2 × (1 + 3)}] میں کون سا حصہ پہلے حل کرتے ہیں؟"),
     "options": [
       opt("inner", "(1 + 3), the innermost brackets", "(1 + 3)، سب سے اندر والی قوسین", True,
           "Yes! Work from the inside out.", "جی ہاں! اندر سے باہر کی طرف حل کریں۔"),
       opt("outer", "10 − 2", "10 − 2", False,
           "Start with the innermost brackets: (1 + 3).", "سب سے اندر والی قوسین سے شروع کریں: (1 + 3)", "outside_first"),
       opt("times", "2 × 1", "2 × 1", False,
           "The ( ) brackets come first, so 1 + 3 before the ×.", "( ) پہلے آتی ہیں، تو × سے پہلے 1 + 3", "ignores_brackets"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Simplify: (9 − 3) × 4", "مختصر کریں: (9 − 3) × 4"),
     QB,
     T("Brackets first: 9 − 3.", "پہلے قوسین: 9 − 3"),
     T("Right! 6 × 4 = 24.", "درست! 6 × 4 = 24"),
     T("9 − 3 = 6, then 6 × 4 = 24.", "9 − 3 = 6، پھر 6 × 4 = 24"),
     common_wrong=[wrong(-3, "That ignores the brackets. Brackets first: 6 × 4 = 24.", "یہ قوسین نظر انداز کرتا ہے۔ پہلے قوسین: 6 × 4 = 24", "ignores_brackets")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Usman writes 2 × (5 + 3) = 10 + 3 = 13. What is wrong?", "عثمان 2 × (5 + 3) = 10 + 3 = 13 لکھتا ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("brackets", "He should add inside the brackets first: 2 × 8 = 16.", "اسے پہلے قوسین کے اندر جمع کرنا چاہیے: 2 × 8 = 16", True,
           "Yes! The whole bracket is multiplied by 2.", "جی ہاں! پوری قوسین کو 2 سے ضرب دی جاتی ہے۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "He multiplied only the 5. Work out the brackets first: 2 × 8 = 16.", "اس نے صرف 5 کو ضرب دی۔ پہلے قوسین حل کریں: 2 × 8 = 16", "partial_distribute"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_bodmas", "front": T("BODMAS?", "BODMAS؟"),
    "back": T("Brackets, then Division and Multiplication, then Addition and Subtraction.", "پہلے قوسین، پھر تقسیم اور ضرب، پھر جمع اور تفریق۔")},
   {"id": "f_kinds", "front": T("Order of brackets?", "قوسین کی ترتیب؟"),
    "back": T("( ) first, then { }, then [ ]: inside out.", "پہلے ( )، پھر { }، پھر [ ]: اندر سے باہر۔")},
 ],
 "home_tasks": [{"id": "h_brackets", "text": T(
   "Take the numbers 2, 3 and 4. Using + and × and one pair of brackets, how many different answers can you make? Which one is the biggest?",
   "عدد 2، 3 اور 4 لیں۔ + اور × اور ایک جوڑا قوسین سے آپ کتنے مختلف جواب بنا سکتے ہیں؟ سب سے بڑا کون سا ہے؟")}],
 "glossary": [T("Brackets", "قوسین"), T("BODMAS", "BODMAS"), T("Inside out", "اندر سے باہر")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "8 + 2 × 3 is 14. But what if we want to add first? Brackets can tell us!",
                     "8 + 2 × 3 کا جواب 14 ہے۔ لیکن اگر ہم پہلے جمع کرنا چاہیں؟ قوسین بتا سکتی ہیں!"),
    "text": T("Today we learn brackets and BODMAS. First, a quick check on the order of operations.", "آج ہم قوسین اور BODMAS سیکھیں گے۔ پہلے عملیات کی ترتیب کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Simplify: 8 + 2 × 3", "مختصر کریں: 8 + 2 × 3"),
     S2,
     T("× before +.", "× پہلے، + بعد میں۔"),
     T("Right! 8 + 6 = 14.", "درست! 8 + 6 = 14"),
     T("2 × 3 = 6, then 8 + 6 = 14.", "2 × 3 = 6، پھر 8 + 6 = 14"),
     common_wrong=[wrong(30, "That adds first. Multiply first: 8 + 6 = 14.", "یہ پہلے جمع ہے۔ پہلے ضرب: 8 + 6 = 14")],
     qtype="recall", skill=SM_ORDER),
   {"id": "s3_bodmas", "type": "explain",
    "character": say("happy", "Brackets jump the queue! Work inside them first, from the inside out.", "قوسین قطار توڑ دیتی ہیں! پہلے ان کے اندر حل کریں، اندر سے باہر۔"),
    "text": T("BODMAS gives the order: Brackets, then Division and Multiplication (left to right), then Addition and Subtraction (left to right). There are three kinds of brackets: ( ), { } and [ ]. Do ( ) first, then { }, then [ ]. So (8 + 2) × 3 = 10 × 3 = 30.",
              "BODMAS ترتیب بتاتا ہے: پہلے قوسین، پھر تقسیم اور ضرب (بائیں سے دائیں)، پھر جمع اور تفریق (بائیں سے دائیں)۔ قوسین تین قسم کی ہیں: ( )، { } اور [ ]۔ پہلے ( )، پھر { }، پھر [ ]۔ تو (8 + 2) × 3 = 10 × 3 = 30")},
   number_question(
     "s4_round",
     T("Simplify: (8 + 2) × 3", "مختصر کریں: (8 + 2) × 3"),
     S4,
     T("Brackets first: 8 + 2.", "پہلے قوسین: 8 + 2"),
     T("Right! 10 × 3 = 30.", "درست! 10 × 3 = 30"),
     T("8 + 2 = 10, then 10 × 3 = 30.", "8 + 2 = 10، پھر 10 × 3 = 30"),
     common_wrong=[wrong(14, "That ignores the brackets. Brackets first: 10 × 3 = 30.", "یہ قوسین نظر انداز کرتا ہے۔ پہلے قوسین: 10 × 3 = 30", "ignores_brackets"),
                   wrong(24, "Multiply the whole bracket, not just the 8: 10 × 3 = 30.", "صرف 8 کو نہیں، پوری قوسین کو ضرب دیں: 10 × 3 = 30", "partial_distribute")]),
   number_question(
     "s5_divide",
     T("Simplify: 24 ÷ (2 + 4)", "مختصر کریں: 24 ÷ (2 + 4)"),
     S5,
     T("Brackets first: 2 + 4.", "پہلے قوسین: 2 + 4"),
     T("Right! 24 ÷ 6 = 4.", "درست! 24 ÷ 6 = 4"),
     T("2 + 4 = 6, then 24 ÷ 6 = 4.", "2 + 4 = 6، پھر 24 ÷ 6 = 4"),
     common_wrong=[wrong(16, "That ignores the brackets. Brackets first: 24 ÷ 6 = 4.", "یہ قوسین نظر انداز کرتا ہے۔ پہلے قوسین: 24 ÷ 6 = 4", "ignores_brackets")]),
   {"id": "s6_which_first", "type": "choice",
    "prompt": T("In 5 × (6 − 2), which part do you work out first?", "5 × (6 − 2) میں کون سا حصہ پہلے حل کرتے ہیں؟"),
    "options": [
      opt("bracket", "6 − 2", "6 − 2", True, "Yes! Brackets first, then 5 × 4 = 20.", "جی ہاں! پہلے قوسین، پھر 5 × 4 = 20"),
      opt("times", "5 × 6", "5 × 6", False, "Brackets come before ×. Do 6 − 2 first.", "قوسین × سے پہلے آتی ہیں۔ پہلے 6 − 2 کریں۔", "ignores_brackets"),
    ]},
   number_question(
     "s7_curly",
     T("Simplify: 50 − {6 × (3 + 2)}", "مختصر کریں: 50 − {6 × (3 + 2)}"),
     S7,
     T("Inside out: (3 + 2) first, then { }.", "اندر سے باہر: پہلے (3 + 2)، پھر { }"),
     T("Right! 50 − 30 = 20.", "درست! 50 − 30 = 20"),
     T("3 + 2 = 5, 6 × 5 = 30, 50 − 30 = 20.", "3 + 2 = 5، 6 × 5 = 30، 50 − 30 = 20"),
     common_wrong=[wrong(32, "Multiply the whole bracket: 6 × 5 = 30, so 50 − 30 = 20.", "پوری قوسین کو ضرب دیں: 6 × 5 = 30، تو 50 − 30 = 20", "partial_distribute")]),
   number_question(
     "s8_square",
     T("Simplify: [20 − (4 + 6)] × 2", "مختصر کریں: [20 − (4 + 6)] × 2"),
     S8,
     T("(4 + 6) first, then the [ ], then × 2.", "پہلے (4 + 6)، پھر [ ]، پھر × 2"),
     T("Right! 10 × 2 = 20.", "درست! 10 × 2 = 20"),
     T("4 + 6 = 10, 20 − 10 = 10, 10 × 2 = 20.", "4 + 6 = 10، 20 − 10 = 10، 10 × 2 = 20"),
     common_wrong=[wrong(28, "That ignores the brackets. Inside out: [20 − 10] × 2 = 20.", "یہ قوسین نظر انداز کرتا ہے۔ اندر سے باہر: [20 − 10] × 2 = 20", "ignores_brackets")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Maria works out 3 × (4 + 5) like this: 3 × 4 = 12, then 12 + 5 = 17. What went wrong?", "ماریہ 3 × (4 + 5) ایسے حل کرتی ہے: 3 × 4 = 12، پھر 12 + 5 = 17۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("brackets", "She should add inside the brackets first: 3 × 9 = 27.", "اسے پہلے قوسین کے اندر جمع کرنا چاہیے: 3 × 9 = 27", True,
          "Yes! Brackets first, then multiply.", "جی ہاں! پہلے قوسین، پھر ضرب۔"),
      opt("order", "She should do 4 + 5 last.", "اسے 4 + 5 آخر میں کرنا چاہیے۔", False,
          "It's the other way: brackets come first.", "الٹا ہے: قوسین سب سے پہلے آتی ہیں۔", "ignores_brackets"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "She multiplied only the 4. The whole bracket is 9, so 3 × 9 = 27.", "اس نے صرف 4 کو ضرب دی۔ پوری قوسین 9 ہے، تو 3 × 9 = 27", "partial_distribute"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we need brackets at all? Can you teach me?",
                     "ہمیں قوسین کی ضرورت ہی کیوں ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why are (8 + 2) × 3 and 8 + 2 × 3 different?", "اپنے الفاظ میں بتائیں: (8 + 2) × 3 اور 8 + 2 × 3 مختلف کیوں ہیں؟"),
    "key_idea": "Normally × comes before +, so 8 + 2 × 3 = 8 + 6 = 14. Brackets change the order: they say add 8 + 2 first, so (8 + 2) × 3 = 10 × 3 = 30.",
    "levels": {
      "got_it": "Says brackets are worked out first, so the adding happens before the multiplying, which changes the answer.",
      "partly": "Says the brackets make it different, without saying they change the order.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["bracket", "قوسین"],
      ["first", "before", "پہلے"],
      ["order", "change", "ترتیب", "بدل"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Brackets change the order, so the answer changes.", "بہت خوب! قوسین ترتیب بدلتی ہیں، اس لیے جواب بدلتا ہے۔"),
      "partly": T("Good start! Now say which part gets done first in each one.", "اچھی شروعات! اب بتائیں ہر ایک میں کون سا حصہ پہلے ہوتا ہے۔"),
      "not_yet": T("Work out both. In which one do you add first?", "دونوں حل کریں۔ کس میں آپ پہلے جمع کرتے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_share",
     T("Three friends share Rs 150 and Rs 90 equally. Each gets (150 + 90) ÷ 3 rupees. How much is that?", "تین دوست 150 روپے اور 90 روپے برابر بانٹتے ہیں۔ ہر ایک کو (150 + 90) ÷ 3 روپے ملتے ہیں۔ یہ کتنے ہیں؟"),
     S11,
     T("Brackets first: 150 + 90.", "پہلے قوسین: 150 + 90"),
     T("Right! 240 ÷ 3 = Rs 80.", "درست! 240 ÷ 3 = 80 روپے"),
     T("150 + 90 = 240, then 240 ÷ 3 = 80.", "150 + 90 = 240، پھر 240 ÷ 3 = 80"),
     common_wrong=[wrong(180, "That ignores the brackets. All the money is shared: 240 ÷ 3 = 80.", "یہ قوسین نظر انداز کرتا ہے۔ سارے پیسے بانٹے جاتے ہیں: 240 ÷ 3 = 80", "ignores_brackets")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Brackets first, inside out. You've got BODMAS!", "پہلے قوسین، اندر سے باہر۔ آپ نے BODMAS سیکھ لیا!"),
    "text": T("BODMAS: Brackets first, then ÷ and × from left to right, then + and − from left to right. Work ( ), then { }, then [ ], from the inside out. Brackets can change the answer.",
              "BODMAS: پہلے قوسین، پھر ÷ اور × بائیں سے دائیں، پھر + اور − بائیں سے دائیں۔ پہلے ( )، پھر { }، پھر [ ]، اندر سے باہر۔ قوسین جواب بدل سکتی ہیں۔"),
    "points": [T("Brackets first, inside out.", "پہلے قوسین، اندر سے باہر۔"),
               T("Then × ÷, then + −.", "پھر × ÷، پھر + −۔")]},
 ],
 "review_questions": [
   {"id": "r_divide", "type": "apply", "skill": SKILL, "step": number_question(
     "r_divide",
     T("Simplify: 60 ÷ (5 + 7)", "مختصر کریں: 60 ÷ (5 + 7)"),
     R1,
     T("Brackets first: 5 + 7.", "پہلے قوسین: 5 + 7"),
     T("Right! 60 ÷ 12 = 5.", "درست! 60 ÷ 12 = 5"),
     T("5 + 7 = 12, then 60 ÷ 12 = 5.", "5 + 7 = 12، پھر 60 ÷ 12 = 5"),
     common_wrong=[wrong(19, "That ignores the brackets: 60 ÷ 12 = 5.", "یہ قوسین نظر انداز کرتا ہے: 60 ÷ 12 = 5", "ignores_brackets")],
     qtype=None)},
   {"id": "r_nested", "type": "apply", "skill": SKILL, "step": number_question(
     "r_nested",
     T("Simplify: {12 − (2 × 3)} + 4", "مختصر کریں: {12 − (2 × 3)} + 4"),
     R2,
     T("(2 × 3) first, then { }.", "پہلے (2 × 3)، پھر { }"),
     T("Right! 6 + 4 = 10.", "درست! 6 + 4 = 10"),
     T("2 × 3 = 6, 12 − 6 = 6, 6 + 4 = 10.", "2 × 3 = 6، 12 − 6 = 6، 6 + 4 = 10"),
     common_wrong=[wrong(2, "Work the { } first, then add 4: 6 + 4 = 10.", "پہلے { } حل کریں، پھر 4 جمع کریں: 6 + 4 = 10", "outside_first")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Simplification unit. No textbook text or exercises were used.",
   "BODMAS here skips Orders (powers), which Grade 6 does not need yet.",
   "Urdu terms to check: قوسین (brackets).",
   "The numbers were worked out in content/sources/g6-maths-13/brackets.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

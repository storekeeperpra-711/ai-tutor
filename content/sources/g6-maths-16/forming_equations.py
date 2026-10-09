from common import (T, opt, say, wrong, number_question, write, solves,
                    REF, REVIEW, ALG_EQUATIONS, EQ_CHECK, EQ_FORMING)

SKILL = EQ_FORMING

# s2: x + 5 = 12
S2 = 12 - 5
assert solves("x + 5 = 12", x=S2) and S2 == 7
# s5: a number plus 9 is 20
S5 = 20 - 9
assert solves("x + 9 = 20", x=S5) and S5 == 11 and 20 + 9 == 29
# s8: marbles: x + 7 = 25 (adding gives 32)
S8 = 25 - 7
assert solves("x + 7 = 25", x=S8) and S8 == 18 and 25 + 7 == 32
# s9: 3 times a number plus 4 is 19: 3x + 4 = 19, x = 5
assert solves("3x + 4 = 19", x=5) and not solves("3(x + 4) = 19", x=5)
# s11: 4 pens cost 120: 4x = 120
S11 = 120 // 4
assert solves("4x = 120", x=S11) and S11 == 30 and 120 * 4 == 480 and 120 - 4 == 116
# question bank and review
QB = 6 * 3
assert solves("x ÷ 3 = 6", x=QB) and QB == 18
R1 = 15 + 8
assert solves("x − 8 = 15", x=R1) and R1 == 23
R2 = 54 // 6
assert solves("6x = 54", x=R2) and R2 == 9 and 54 - 6 == 48

lesson = {
 "id": "g6-maths-16-forming-equations",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Turn a sentence or a short story into a linear equation and solve it.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Writing equations from words", "الفاظ سے مساوات بنانا"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": EQ_CHECK}, {"skill": ALG_EQUATIONS}],
 "misconceptions": [
   {"id": "less_than_order", "description": "Writes '5 less than a number' as 5 − x instead of x − 5."},
   {"id": "times_as_plus", "description": "Writes 'twice' or 'times' as + instead of ×."},
   {"id": "brackets_wrong", "description": "Puts brackets where the words don't need them, like 3(x + 4) for '3 times a number plus 4'."},
   {"id": "wrong_inverse", "description": "Solves x + a = b by adding a instead of subtracting it."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_is", "type": "recall", "step": {
     "id": "qb_is", "type": "choice",
     "prompt": T("In 'a number plus 4 is 10', which sign does the word 'is' become?", "'ایک عدد جمع 4 برابر ہے 10' میں لفظ 'ہے' کون سی علامت بنتا ہے؟"),
     "options": [
       opt("equals", "=", "=", True, "Yes! 'Is' means equals: x + 4 = 10.", "جی ہاں! 'ہے' یعنی برابر: x + 4 = 10"),
       opt("plus", "+", "+", False, "'Plus' is +. 'Is' is =: x + 4 = 10.", "'جمع' + ہے۔ 'ہے' = ہے: x + 4 = 10"),
       opt("times", "×", "×", False, "'Is' is =, not ×: x + 4 = 10.", "'ہے' = ہے، × نہیں: x + 4 = 10"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("A number divided by 3 is 6. Write the equation and find the number.", "ایک عدد کو 3 سے تقسیم کریں تو 6 آتا ہے۔ مساوات لکھیں اور عدد معلوم کریں۔"),
     QB,
     T("x ÷ 3 = 6. Undo ÷ 3 with × 3.", "x ÷ 3 = 6۔ ÷ 3 کو × 3 سے ختم کریں۔"),
     T("Right! x = 18.", "درست! x = 18"),
     T("x ÷ 3 = 6, so x = 6 × 3 = 18.", "x ÷ 3 = 6، تو x = 6 × 3 = 18"),
     common_wrong=[wrong(2, "Undo ÷ with ×, not ÷: 6 × 3 = 18.", "÷ کو × سے ختم کریں، ÷ سے نہیں: 6 × 3 = 18", "wrong_inverse")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("'Twice a number is 16.' Hamza writes x + 2 = 16. What is wrong?", "'ایک عدد کا دگنا 16 ہے۔' حمزہ لکھتا ہے x + 2 = 16۔ کیا غلطی ہے؟"),
     "options": [
       opt("times", "Twice means × 2: 2x = 16.", "دگنا یعنی × 2: 2x = 16", True,
           "Yes! Then x = 8.", "جی ہاں! پھر x = 8"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "Twice means 2 times, not plus 2: 2x = 16.", "دگنا یعنی 2 گنا، جمع 2 نہیں: 2x = 16", "times_as_plus"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_words", "front": T("'Is', 'twice', 'less than'?", "'ہے'، 'دگنا'، 'کم'؟"),
    "back": T("= , 2 × , subtract from the number.", "=، 2 ×، عدد میں سے تفریق")},
   {"id": "f_less", "front": T("'5 less than a number'?", "'ایک عدد سے 5 کم'؟"),
    "back": T("x − 5", "x − 5")},
 ],
 "home_tasks": [{"id": "h_story", "text": T(
   "Make a number story at home, like 'I had some sweets, I got 4 more and now I have 10.' Write it as an equation and solve it.",
   "گھر میں ایک عددی کہانی بنائیں، جیسے 'میرے پاس کچھ ٹافیاں تھیں، مجھے 4 اور ملیں اور اب میرے پاس 10 ہیں۔' اسے مساوات میں لکھیں اور حل کریں۔")}],
 "glossary": [T("Equation", "مساوات"), T("Twice", "دگنا"), T("Less than", "سے کم")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "'I think of a number, add 9 and get 20.' Can we write that in maths?",
                     "'میں ایک عدد سوچتا ہوں، 9 جمع کرتا ہوں اور 20 آتا ہے۔' کیا ہم اسے ریاضی میں لکھ سکتے ہیں؟"),
    "text": T("Today we turn words into equations, then solve them. First, a quick solving check.", "آج ہم الفاظ کو مساوات میں بدلیں گے، پھر انہیں حل کریں گے۔ پہلے حل کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Solve x + 5 = 12. What is x?", "x + 5 = 12 حل کریں۔ x کیا ہے؟"),
     S2,
     T("Take 5 from both sides.", "دونوں طرف سے 5 تفریق کریں۔"),
     T("Right! x = 7.", "درست! x = 7"),
     T("12 − 5 = 7.", "12 − 5 = 7"),
     common_wrong=[wrong(17, "Undo + 5 by subtracting: 12 − 5 = 7.", "+ 5 کو تفریق سے ختم کریں: 12 − 5 = 7", "wrong_inverse")],
     qtype="recall", skill=ALG_EQUATIONS),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Words become symbols. 'A number' becomes x, and 'is' becomes =!", "الفاظ علامتیں بن جاتے ہیں۔ 'ایک عدد' بنتا ہے x، اور 'ہے' بنتا ہے =!"),
    "text": T("Use a letter for the unknown number, like x. Then: 'plus', 'more than', 'added' → +. 'Minus', 'less than' → −. 'Times', 'twice' → ×. 'Divided by', 'shared' → ÷. 'Is', 'gives', 'makes' → =. Careful: '5 less than a number' is x − 5, not 5 − x.",
              "نامعلوم عدد کے لیے حرف استعمال کریں، جیسے x۔ پھر: 'جمع'، 'سے زیادہ' → +۔ 'تفریق'، 'سے کم' → −۔ 'گنا'، 'دگنا' → ×۔ 'تقسیم'، 'بانٹا' → ÷۔ 'ہے'، 'بنتا ہے' → =۔ دھیان دیں: 'ایک عدد سے 5 کم' یعنی x − 5، نہ کہ 5 − x۔")},
   {"id": "s4_plus", "type": "choice",
    "prompt": T("Which equation says 'a number plus 9 is 20'?", "کون سی مساوات کہتی ہے 'ایک عدد جمع 9 برابر 20'؟"),
    "options": [
      opt("plus", "x + 9 = 20", "x + 9 = 20", True, "Yes! Plus is +, and is is =.", "جی ہاں! جمع یعنی +، اور ہے یعنی ="),
      opt("times", "9x = 20", "9x = 20", False, "9x means 9 times x. The words say plus: x + 9 = 20.", "9x یعنی 9 گنا x۔ الفاظ جمع کہتے ہیں: x + 9 = 20", "times_as_plus"),
      opt("minus", "x − 9 = 20", "x − 9 = 20", False, "Plus means +, not −: x + 9 = 20.", "جمع یعنی +، − نہیں: x + 9 = 20"),
    ]},
   number_question(
     "s5_solve",
     T("Now solve x + 9 = 20. What is the number?", "اب x + 9 = 20 حل کریں۔ عدد کیا ہے؟"),
     S5,
     T("Take 9 from both sides.", "دونوں طرف سے 9 تفریق کریں۔"),
     T("Right! x = 11.", "درست! x = 11"),
     T("20 − 9 = 11. Check: 11 + 9 = 20.", "20 − 9 = 11۔ جانچ: 11 + 9 = 20"),
     common_wrong=[wrong(29, "Undo + 9 by subtracting: 20 − 9 = 11.", "+ 9 کو تفریق سے ختم کریں: 20 − 9 = 11", "wrong_inverse")]),
   {"id": "s6_twice", "type": "choice",
    "prompt": T("Which equation says 'twice a number is 18'?", "کون سی مساوات کہتی ہے 'ایک عدد کا دگنا 18 ہے'؟"),
    "options": [
      opt("twice", "2x = 18", "2x = 18", True, "Yes! Twice means 2 times.", "جی ہاں! دگنا یعنی 2 گنا۔"),
      opt("plus", "x + 2 = 18", "x + 2 = 18", False, "Twice means × 2, not + 2: 2x = 18.", "دگنا یعنی × 2، + 2 نہیں: 2x = 18", "times_as_plus"),
      opt("half", "x ÷ 2 = 18", "x ÷ 2 = 18", False, "That is half a number. Twice is 2x = 18.", "یہ عدد کا آدھا ہے۔ دگنا یعنی 2x = 18"),
    ]},
   {"id": "s7_less", "type": "choice",
    "prompt": T("Which equation says '5 less than a number is 12'?", "کون سی مساوات کہتی ہے 'ایک عدد سے 5 کم برابر 12'؟"),
    "options": [
      opt("x_minus", "x − 5 = 12", "x − 5 = 12", True, "Yes! Start with the number, then take 5 away.", "جی ہاں! عدد سے شروع کریں، پھر 5 نکالیں۔"),
      opt("five_minus", "5 − x = 12", "5 − x = 12", False, "That takes the number from 5. '5 less than a number' is x − 5.", "اس میں 5 میں سے عدد نکالا گیا۔ 'عدد سے 5 کم' یعنی x − 5", "less_than_order"),
      opt("plus", "x + 5 = 12", "x + 5 = 12", False, "'Less than' means subtract: x − 5 = 12.", "'سے کم' یعنی تفریق: x − 5 = 12"),
    ]},
   number_question(
     "s8_marbles",
     T("Ayesha has some marbles. She gets 7 more and now has 25. Write x + 7 = 25. How many did she have at first?", "عائشہ کے پاس کچھ کنچے ہیں۔ اسے 7 اور ملتے ہیں اور اب اس کے پاس 25 ہیں۔ x + 7 = 25 لکھیں۔ شروع میں اس کے پاس کتنے تھے؟"),
     S8,
     T("Take 7 from both sides.", "دونوں طرف سے 7 تفریق کریں۔"),
     T("Right! 18 marbles.", "درست! 18 کنچے"),
     T("25 − 7 = 18. Check: 18 + 7 = 25.", "25 − 7 = 18۔ جانچ: 18 + 7 = 25"),
     common_wrong=[wrong(32, "She had fewer at first. Subtract: 25 − 7 = 18.", "شروع میں کم تھے۔ تفریق کریں: 25 − 7 = 18", "wrong_inverse")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("'3 times a number, plus 4, is 19.' Bilal writes 3(x + 4) = 19. What went wrong?", "'ایک عدد کا 3 گنا، جمع 4، برابر 19۔' بلال لکھتا ہے 3(x + 4) = 19۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("no_brackets", "Only the number is multiplied by 3: 3x + 4 = 19.", "صرف عدد کو 3 سے ضرب ہے: 3x + 4 = 19", True,
          "Yes! Then x = 5, since 15 + 4 = 19.", "جی ہاں! پھر x = 5، کیونکہ 15 + 4 = 19"),
      opt("swap", "It should be 4x + 3 = 19.", "یہ 4x + 3 = 19 ہونا چاہیے۔", False,
          "The 3 multiplies the number and the 4 is added: 3x + 4 = 19.", "3 عدد کو ضرب دیتا ہے اور 4 جمع ہوتا ہے: 3x + 4 = 19"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "The brackets multiply the 4 by 3 too. The words say 3x + 4 = 19.", "قوسین 4 کو بھی 3 سے ضرب دیتی ہیں۔ الفاظ کہتے ہیں 3x + 4 = 19", "brackets_wrong"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "How do you turn a sentence into an equation? Can you teach me?",
                     "آپ ایک جملے کو مساوات میں کیسے بدلتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: how would you write 'a number times 4 is 36' as an equation? Explain each part.", "اپنے الفاظ میں بتائیں: 'ایک عدد کا 4 گنا 36 ہے' کو مساوات میں کیسے لکھیں گے؟ ہر حصے کی وضاحت کریں۔"),
    "key_idea": "Use x for the unknown number. 'Times 4' means × 4, so 4x. 'Is' means =. So 4x = 36, and x = 9.",
    "levels": {
      "got_it": "Uses a letter for the number, explains times → × and is → =, and writes 4x = 36.",
      "partly": "Writes 4x = 36 without explaining the parts.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["letter", "x", "حرف"],
      ["times", "multiply", "×", "ضرب", "گنا"],
      ["equal", "=", "is", "برابر"]],
    "fallback_feedback": {
      "got_it": T("Well explained! A letter, a sign for each word, and = for 'is'.", "بہت خوب! ایک حرف، ہر لفظ کی علامت، اور 'ہے' کے لیے ="),
      "partly": T("Good start! Now say what each word turned into.", "اچھی شروعات! اب بتائیں ہر لفظ کس علامت میں بدلا۔"),
      "not_yet": T("Use x for the number. What sign does 'times' become? And 'is'?", "عدد کے لیے x لیں۔ 'گنا' کون سی علامت بنتا ہے؟ اور 'ہے'؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_pens",
     T("A pen costs Rs x. 4 pens cost Rs 120, so 4x = 120. How much does one pen cost?", "ایک قلم x روپے کا ہے۔ 4 قلم 120 روپے کے ہیں، تو 4x = 120۔ ایک قلم کتنے کا ہے؟"),
     S11,
     T("Undo × 4 by dividing by 4.", "× 4 کو 4 سے تقسیم کرکے ختم کریں۔"),
     T("Right! Rs 30.", "درست! 30 روپے"),
     T("120 ÷ 4 = 30. Check: 4 × 30 = 120.", "120 ÷ 4 = 30۔ جانچ: 4 × 30 = 120"),
     common_wrong=[wrong(480, "Undo × with ÷: 120 ÷ 4 = 30.", "× کو ÷ سے ختم کریں: 120 ÷ 4 = 30", "wrong_inverse"),
                   wrong(116, "4x means 4 × x, so divide: 120 ÷ 4 = 30.", "4x یعنی 4 × x، تو تقسیم کریں: 120 ÷ 4 = 30")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Letter for the number, a sign for each word, then solve. Brilliant!", "عدد کے لیے حرف، ہر لفظ کی علامت، پھر حل۔ زبردست!"),
    "text": T("Use a letter for the unknown. Turn each word into a sign: plus +, less than −, times ×, divided by ÷, is =. Then solve and check your answer.",
              "نامعلوم کے لیے حرف لیں۔ ہر لفظ کو علامت میں بدلیں: جمع +، سے کم −، گنا ×، تقسیم ÷، ہے =۔ پھر حل کریں اور جواب جانچیں۔"),
    "points": [T("'Is' becomes =.", "'ہے' بنتا ہے ="),
               T("'5 less than x' is x − 5.", "'x سے 5 کم' یعنی x − 5")]},
 ],
 "review_questions": [
   {"id": "r_minus", "type": "apply", "skill": SKILL, "step": number_question(
     "r_minus",
     T("A number minus 8 is 15. Find the number.", "ایک عدد تفریق 8 برابر 15۔ عدد معلوم کریں۔"),
     R1,
     T("x − 8 = 15. Add 8 to both sides.", "x − 8 = 15۔ دونوں طرف 8 جمع کریں۔"),
     T("Right! 23.", "درست! 23"),
     T("15 + 8 = 23. Check: 23 − 8 = 15.", "15 + 8 = 23۔ جانچ: 23 − 8 = 15"),
     common_wrong=[wrong(7, "Undo − 8 by adding: 15 + 8 = 23.", "− 8 کو جمع سے ختم کریں: 15 + 8 = 23", "wrong_inverse")],
     qtype=None)},
   {"id": "r_times", "type": "apply", "skill": SKILL, "step": number_question(
     "r_times",
     T("6 times a number is 54. Find the number.", "ایک عدد کا 6 گنا 54 ہے۔ عدد معلوم کریں۔"),
     R2,
     T("6x = 54. Divide by 6.", "6x = 54۔ 6 سے تقسیم کریں۔"),
     T("Right! 9.", "درست! 9"),
     T("54 ÷ 6 = 9.", "54 ÷ 6 = 9"),
     common_wrong=[wrong(48, "'Times' means ×, so divide: 54 ÷ 6 = 9.", "'گنا' یعنی ×، تو تقسیم کریں: 54 ÷ 6 = 9", "times_as_plus")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Linear Equations unit. No textbook text or exercises were used.",
   "Children pick the right equation from choices rather than typing it, so the lesson needs no equation checker.",
   "Urdu wording of 'less than' (سے کم) needs a teacher's check: the word order differs from English.",
   "The numbers were worked out in content/sources/g6-maths-16/forming_equations.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

# ---------- pictures ----------
from figs import attach, step_says, balance, balance_eq, bars, Side, plus_bar, minus_bar, two_rows_alt

s2_fig, s2_eq = balance_eq(1, "x", 5, 12, S2)
S3 = 5 + 12            # the rule's example: 5 less than a number is 12
assert solves("x − 5 = 12", x=S3)
s3_fig, s3_eq = minus_bar(1, "x", 5, 12, S3,
                          pre=("'5 less than a number is 12', x − 5 = 12.", "'ایک عدد سے 5 کم، 12 ہے'، x − 5 = 12۔"))
s5_fig, s5_eq = plus_bar(1, "x", 9, 20, S5)
s8_fig, s8_eq = balance_eq(1, "x", 7, 25, S8,
                           pre=("Ayesha's marbles: the box is the marbles she had at first.", "عائشہ کے کنچے: ڈبہ وہ کنچے ہیں جو اس کے پاس پہلے تھے۔"))
s11_fig, s11_eq = plus_bar(4, "x", 0, 120, S11, pre=("4 pens, each costing Rs x, together cost Rs 120.", "4 قلم، ہر ایک x روپے کا، مل کر 120 روپے کے ہیں۔"))
r1_fig, r1_eq = minus_bar(1, "x", 8, 15, R1)
r2_fig, r2_eq = plus_bar(6, "x", 0, 54, R2)
for sid, texts in (("s2_foundation", [s2_eq]), ("s3_rule", ["5 less than a number"]), ("s5_solve", [s5_eq]),
                   ("s8_marbles", [s8_eq]), ("s11_pens", [s11_eq]), ("qb_apply", ["divided by 3 is 6"]),
                   ("r_minus", ["minus 8 is 15"]), ("r_times", ["6 times a number is 54"])):
    step_says(lesson, sid, *texts)
QB_PARTS = 3, 6        # a number divided by 3 is 6
assert QB == QB_PARTS[0] * QB_PARTS[1]

attach(lesson, {
    "s2_foundation": s2_fig,
    "s3_rule": s3_fig,
    "s5_solve": s5_fig,
    "s8_marbles": s8_fig,
    "s11_pens": s11_fig,
    "qb_apply": bars([[(QB, "x", "f")], [(QB_PARTS[1], QB_PARTS[1], "")] * QB_PARTS[0]],
                     *two_rows_alt(["x"], [QB_PARTS[1]] * QB_PARTS[0],
                                   pre=("A number x shared into 3 equal parts gives 6 in each part.",
                                        "ایک عدد x کو 3 برابر حصوں میں بانٹیں تو ہر حصے میں 6 آتا ہے۔"))),
    "r_minus": r1_fig,
    "r_times": r2_fig,
})
write(lesson)

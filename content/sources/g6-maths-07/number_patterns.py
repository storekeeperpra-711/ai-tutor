from common import (T, opt, say, wrong, number_question, write, value,
                    BOOK, REVIEW, ALG_SUBSTITUTION, ALG_SEQUENCES)

SKILL = ALG_SEQUENCES


def seq(rule, count=6):
    """The first terms of a sequence from its nth-term rule."""
    return [value(rule, n=n) for n in range(1, count + 1)]


# s2: 3n + 1 when n = 5 (reading 3n as 35: 36)
S2 = value("3n + 1", n=5)
assert S2 == 16
# s4: 5, 9, 13, 17, … (adding 1: 18)
assert seq("4n + 1", 4) == [5, 9, 13, 17]
S4 = seq("4n + 1", 5)[-1]
assert S4 == 21
# s5: 2, 4, 8, 16, … doubles (adding 2: 18)
S5 = 16 * 2
assert S5 == 32
# s6: 3, 8, 13, 18 adds 5
assert seq("5n − 2", 4) == [3, 8, 13, 18]
# s7: 10th term of 2n + 3 (reading 2n as 210: 213)
S7 = value("2n + 3", n=10)
assert S7 == 23
# s8: which term of 4n − 1 is 39 (putting 39 in: 155)
S8 = [n for n in range(1, 50) if value("4n − 1", n=n) == 39]
assert S8 == [10] and value("4n − 1", n=39) == 155
S8 = S8[0]
# s9: 6th term of 3n + 2 is 20, not 36 + 2
assert value("3n + 2", n=6) == 20
# s10: squares in a row of matchsticks: 4, 7, 10, … = 3n + 1
assert seq("3n + 1", 3) == [4, 7, 10]
# s11: 7, 11, 15, 19 … 20th term (4n only: 80)
assert seq("4n + 3", 4) == [7, 11, 15, 19]
S11 = value("4n + 3", n=20)
assert S11 == 83
# question bank: 50, 45, 40, 35, … ; 1, 4, 9, 16, …
QB = 35 - 5
assert QB == 30
assert [n * n for n in range(1, 6)] == [1, 4, 9, 16, 25]
# review: 4th term of 6n − 2; 3, 6, 12, 24, …
R1 = value("6n − 2", n=4)
assert R1 == 22
R2 = 24 * 2
assert R2 == 48

lesson = {
 "id": "g6-maths-07-number-patterns",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Continue number patterns, and use a rule like 3n + 1 to find any term of a sequence.", "textbook": f"{BOOK}, Patterns and sequences"}],
 "skills": [SKILL],
 "title": T("Number patterns and sequences", "اعداد کے نمونے اور سلسلے"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": ALG_SUBSTITUTION}],
 "misconceptions": [
   {"id": "joins_digits", "description": "Reads 3n with n = 5 as 35 instead of 3 × 5."},
   {"id": "always_add", "description": "Assumes every pattern adds the same number, even when it doubles or the gap grows."},
   {"id": "term_for_position", "description": "Puts the term's value in place of n instead of finding its position."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("What is the rule of the pattern 3, 7, 11, 15, …?", "نمونے 3، 7، 11، 15، … کا اصول کیا ہے؟"),
     "options": [
       opt("add_four", "Add 4", "4 جمع کریں", True, "Yes! Each term is 4 more than the one before.", "جی ہاں! ہر رکن پچھلے سے 4 زیادہ ہے۔"),
       opt("add_three", "Add 3", "3 جمع کریں", False, "3 + 3 = 6, not 7. The gap is 4.", "3 + 3 = 6، 7 نہیں۔ فرق 4 ہے۔"),
       opt("double", "Double it", "دگنا کریں", False, "3 doubled is 6, not 7. The gap is always 4.", "3 کا دگنا 6 ہے، 7 نہیں۔ فرق ہمیشہ 4 ہے۔", "always_add"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("What is the next term of 50, 45, 40, 35, …?", "50، 45، 40، 35، … کا اگلا رکن کیا ہے؟"),
     QB,
     T("The terms go down by 5.", "رکن 5، 5 کم ہوتے ہیں۔"),
     T("Right! 35 − 5 = 30.", "درست! 35 − 5 = 30"),
     T("Each term is 5 less: 35 − 5 = 30.", "ہر رکن 5 کم ہے: 35 − 5 = 30"),
     common_wrong=[wrong(40, "The pattern goes down, not up: 35 − 5 = 30.", "نمونہ نیچے جا رہا ہے، اوپر نہیں: 35 − 5 = 30")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Sana says the next term of 1, 4, 9, 16, … is 23, because 16 + 7 = 23. What is wrong?", "ثنا کہتی ہے کہ 1، 4، 9، 16، … کا اگلا رکن 23 ہے، کیونکہ 16 + 7 = 23۔ کیا غلطی ہے؟"),
     "options": [
       opt("growing_gap", "The gaps grow: +3, +5, +7, so next is +9: 25.", "فرق بڑھ رہا ہے: +3، +5، +7، تو اگلا +9: 25", True,
           "Yes! These are square numbers: 5 × 5 = 25.", "جی ہاں! یہ مربع اعداد ہیں: 5 × 5 = 25"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "The gaps are 3, 5, 7, so the next gap is 9: 25.", "فرق 3، 5، 7 ہیں، تو اگلا فرق 9: 25", "always_add"),
       opt("double", "She should double: 32.", "اسے دگنا کرنا چاہیے: 32", False,
           "4 isn't double 1. The gaps grow by 2: 16 + 9 = 25.", "4، 1 کا دگنا نہیں۔ فرق 2، 2 بڑھتا ہے: 16 + 9 = 25", "always_add"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_sequence", "front": T("Sequence?", "سلسلہ؟"),
    "back": T("Numbers in order that follow a rule, like 4, 7, 10, 13 (add 3).", "ترتیب میں اعداد جو کسی اصول پر چلیں، جیسے 4، 7، 10، 13 (3 جمع)")},
   {"id": "f_nth", "front": T("nth term 3n + 1?", "n واں رکن 3n + 1؟"),
    "back": T("Put the position in for n: the 5th term is 3 × 5 + 1 = 16.", "n کی جگہ مقام رکھیں: 5واں رکن 3 × 5 + 1 = 16")},
 ],
 "home_tasks": [{"id": "h_sticks", "text": T(
   "Make squares in a row with matchsticks or straws: 1 square, then 2, then 3. Count the sticks each time. Can you find the rule?",
   "ماچس کی تیلیوں یا اسٹرا سے ایک قطار میں مربع بنائیں: 1 مربع، پھر 2، پھر 3۔ ہر بار تیلیاں گنیں۔ کیا آپ اصول ڈھونڈ سکتے ہیں؟")}],
 "glossary": [T("Pattern", "نمونہ"), T("Sequence", "سلسلہ"), T("Term", "رکن"), T("Rule", "اصول")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "4, 7, 10, 13… What comes next? And what would the 100th number be?",
                     "4، 7، 10، 13… آگے کیا آئے گا؟ اور 100واں عدد کیا ہوگا؟"),
    "text": T("Today we find the rules behind number patterns, and use letters to find any term. First, a substitution warm-up.", "آج ہم اعداد کے نمونوں کے پیچھے اصول ڈھونڈیں گے، اور حروف سے کوئی بھی رکن نکالیں گے۔ پہلے قیمت رکھنے کا ایک سوال۔")},
   number_question(
     "s2_foundation",
     T("Find the value of 3n + 1 when n = 5.", "جب n = 5 ہو تو 3n + 1 کی قیمت معلوم کریں۔"),
     S2,
     T("3n means 3 × n.", "3n یعنی 3 × n"),
     T("Right! 3 × 5 + 1 = 16.", "درست! 3 × 5 + 1 = 16"),
     T("3 × 5 = 15, then 15 + 1 = 16.", "3 × 5 = 15، پھر 15 + 1 = 16"),
     common_wrong=[wrong(36, "3n is 3 × 5, not 35: 15 + 1 = 16.", "3n یعنی 3 × 5، 35 نہیں: 15 + 1 = 16", "joins_digits")],
     qtype="recall", skill=ALG_SUBSTITUTION),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Find the rule, and you can jump to any term without counting!", "اصول ڈھونڈ لیں، تو گنے بغیر کسی بھی رکن تک پہنچ سکتے ہیں!"),
    "text": T("A sequence is a list of numbers that follow a rule. Each number is a term. In 4, 7, 10, 13, … the rule is 'add 3'. We can also write a rule for the nth term: here it is 3n + 1. Put n = 1 to get 4, n = 2 to get 7, and n = 100 to get 301. Some patterns don't add the same amount: 2, 4, 8, 16 doubles each time.",
              "سلسلہ اعداد کی فہرست ہے جو کسی اصول پر چلتی ہے۔ ہر عدد ایک رکن ہے۔ 4، 7، 10، 13، … میں اصول '3 جمع کریں' ہے۔ ہم n ویں رکن کا اصول بھی لکھ سکتے ہیں: یہاں 3n + 1 ہے۔ n = 1 رکھیں تو 4، n = 2 رکھیں تو 7، اور n = 100 رکھیں تو 301۔ کچھ نمونوں میں ہر بار ایک جتنا جمع نہیں ہوتا: 2، 4، 8، 16 ہر بار دگنا ہوتا ہے۔")},
   number_question(
     "s4_next",
     T("What is the next term of 5, 9, 13, 17, …?", "5، 9، 13، 17، … کا اگلا رکن کیا ہے؟"),
     S4,
     T("How much is added each time?", "ہر بار کتنا جمع ہوتا ہے؟"),
     T("Right! Add 4: 17 + 4 = 21.", "درست! 4 جمع: 17 + 4 = 21"),
     T("The rule is add 4: 17 + 4 = 21.", "اصول 4 جمع کرنا ہے: 17 + 4 = 21"),
     common_wrong=[wrong(18, "The gap is 4, not 1: 17 + 4 = 21.", "فرق 4 ہے، 1 نہیں: 17 + 4 = 21")]),
   number_question(
     "s5_double",
     T("What is the next term of 2, 4, 8, 16, …?", "2، 4، 8، 16، … کا اگلا رکن کیا ہے؟"),
     S5,
     T("Look: 2 × 2 = 4, 4 × 2 = 8 …", "دیکھیں: 2 × 2 = 4، 4 × 2 = 8 …"),
     T("Right! Each term doubles: 32.", "درست! ہر رکن دگنا ہوتا ہے: 32"),
     T("The rule is 'double': 16 × 2 = 32.", "اصول 'دگنا' ہے: 16 × 2 = 32"),
     common_wrong=[wrong(18, "The gaps are 2, 4, 8, not always 2. Each term doubles: 32.", "فرق 2، 4، 8 ہیں، ہمیشہ 2 نہیں۔ ہر رکن دگنا ہوتا ہے: 32", "always_add"),
                   wrong(24, "Adding 8 again doesn't fit 2, 4, 8. Double: 32.", "دوبارہ 8 جمع کرنا 2، 4، 8 پر پورا نہیں اترتا۔ دگنا کریں: 32", "always_add")]),
   {"id": "s6_which_rule", "type": "choice",
    "prompt": T("What is the rule of 3, 8, 13, 18, …?", "3، 8، 13، 18، … کا اصول کیا ہے؟"),
    "options": [
      opt("add_five", "Add 5", "5 جمع کریں", True, "Yes! 3 + 5 = 8, 8 + 5 = 13.", "جی ہاں! 3 + 5 = 8، 8 + 5 = 13"),
      opt("add_three", "Add 3", "3 جمع کریں", False, "3 + 3 = 6, not 8. The gap is 5.", "3 + 3 = 6، 8 نہیں۔ فرق 5 ہے۔"),
      opt("double", "Double and add 2", "دگنا کر کے 2 جمع", False, "That gives 8, but then 18, not 13. The rule is add 5.", "اس سے 8 تو آتا ہے، مگر پھر 18، 13 نہیں۔ اصول 5 جمع کرنا ہے۔"),
    ]},
   number_question(
     "s7_tenth",
     T("A sequence has nth term 2n + 3. What is its 10th term?", "ایک سلسلے کا n واں رکن 2n + 3 ہے۔ اس کا 10واں رکن کیا ہے؟"),
     S7,
     T("Put n = 10 into 2n + 3.", "2n + 3 میں n = 10 رکھیں۔"),
     T("Right! 2 × 10 + 3 = 23.", "درست! 2 × 10 + 3 = 23"),
     T("2 × 10 = 20, then 20 + 3 = 23.", "2 × 10 = 20، پھر 20 + 3 = 23"),
     common_wrong=[wrong(213, "2n is 2 × 10, not 210: 20 + 3 = 23.", "2n یعنی 2 × 10، 210 نہیں: 20 + 3 = 23", "joins_digits")]),
   number_question(
     "s8_which_term",
     T("A sequence has nth term 4n − 1. Which term is 39? (Find n.)", "ایک سلسلے کا n واں رکن 4n − 1 ہے۔ 39 کون سا رکن ہے؟ (n معلوم کریں۔)"),
     S8,
     T("4n − 1 = 39, so 4n = 40.", "4n − 1 = 39، تو 4n = 40"),
     T("Right! The 10th term: 4 × 10 − 1 = 39.", "درست! 10واں رکن: 4 × 10 − 1 = 39"),
     T("4n = 40, so n = 10. Check: 4 × 10 − 1 = 39.", "4n = 40، تو n = 10۔ جانچ: 4 × 10 − 1 = 39"),
     common_wrong=[wrong(155, "39 is the term, not n. Solve 4n − 1 = 39: n = 10.", "39 رکن ہے، n نہیں۔ 4n − 1 = 39 حل کریں: n = 10", "term_for_position")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Ali finds the 6th term of 3n + 2. He writes 36 + 2 = 38. What is wrong?", "علی 3n + 2 کا چھٹا رکن نکالتا ہے۔ وہ لکھتا ہے 36 + 2 = 38۔ کیا غلطی ہے؟"),
    "options": [
      opt("times", "3n means 3 × 6 = 18, so the 6th term is 20.", "3n یعنی 3 × 6 = 18، تو چھٹا رکن 20 ہے۔", True,
          "Yes! A number next to a letter means multiply.", "جی ہاں! حرف کے ساتھ عدد یعنی ضرب۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "3n is 3 × 6, not 36: 18 + 2 = 20.", "3n یعنی 3 × 6، 36 نہیں: 18 + 2 = 20", "joins_digits"),
      opt("count", "He should count on 6 from 3: 9.", "اسے 3 سے 6 آگے گننا چاہیے: 9", False,
          "Put n = 6 into 3n + 2: 3 × 6 + 2 = 20.", "3n + 2 میں n = 6 رکھیں: 3 × 6 + 2 = 20"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "1 square takes 4 sticks, 2 squares take 7, 3 squares take 10. Why 3n + 1? Teach me!",
                     "1 مربع میں 4 تیلیاں، 2 میں 7، 3 میں 10۔ 3n + 1 کیوں؟ مجھے سکھائیں!"),
    "task": T("Squares in a row need 4, 7, 10, … matchsticks. Explain why n squares need 3n + 1 sticks.", "قطار میں مربعوں کے لیے 4، 7، 10، … تیلیاں لگتی ہیں۔ بتائیں کہ n مربعوں کے لیے 3n + 1 تیلیاں کیوں لگتی ہیں۔"),
    "key_idea": "The first square needs 4 sticks. Each new square shares a side with the one before, so it needs only 3 more. So n squares need 1 + 3n sticks: the 1 is the first side, and each square adds 3.",
    "levels": {
      "got_it": "Says each new square adds 3 sticks (it shares a side), and the extra 1 is the first side, so 3n + 1.",
      "partly": "Says 'add 3 each time' but doesn't explain the + 1, or the other way round.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["3", "three", "تین"],
      ["share", "same side", "مشترک"],
      ["1", "first", "پہلا", "ایک"],
      ["each", "every", "ہر"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 3 per square, plus 1 to start.", "بہت خوب! ہر مربع کی 3، اور شروع کی 1۔"),
      "partly": T("Good start! Where does the + 1 come from?", "اچھی شروعات! + 1 کہاں سے آتا ہے؟"),
      "not_yet": T("How many new sticks does each new square need? Why not 4?", "ہر نئے مربع کو کتنی نئی تیلیاں چاہئیں؟ 4 کیوں نہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_twentieth",
     T("The sequence 7, 11, 15, 19, … has nth term 4n + 3. What is the 20th term?", "سلسلے 7، 11، 15، 19، … کا n واں رکن 4n + 3 ہے۔ 20واں رکن کیا ہے؟"),
     S11,
     T("Put n = 20.", "n = 20 رکھیں۔"),
     T("Right! 4 × 20 + 3 = 83.", "درست! 4 × 20 + 3 = 83"),
     T("4 × 20 = 80, then 80 + 3 = 83.", "4 × 20 = 80، پھر 80 + 3 = 83"),
     common_wrong=[wrong(80, "Don't forget the + 3: 80 + 3 = 83.", "+ 3 نہ بھولیں: 80 + 3 = 83")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Patterns have rules, and rules let you find any term. Brilliant!", "نمونوں کے اصول ہوتے ہیں، اور اصول سے کوئی بھی رکن مل جاتا ہے۔ زبردست!"),
    "text": T("A sequence follows a rule. Find the gap between terms to continue it, but check: some patterns double or have growing gaps. A rule like 3n + 1 gives any term: put the position in for n. To find which term a number is, solve the rule equal to it.",
              "سلسلہ کسی اصول پر چلتا ہے۔ آگے بڑھانے کے لیے ارکان کا فرق دیکھیں، مگر جانچیں: کچھ نمونے دگنے ہوتے ہیں یا ان کا فرق بڑھتا ہے۔ 3n + 1 جیسا اصول کوئی بھی رکن دیتا ہے: n کی جگہ مقام رکھیں۔ کوئی عدد کون سا رکن ہے، یہ جاننے کے لیے اصول کو اس کے برابر رکھ کر حل کریں۔"),
    "points": [T("nth term: put n = position.", "n واں رکن: n = مقام رکھیں۔"),
               T("Check the gaps: add, double or growing?", "فرق دیکھیں: جمع، دگنا یا بڑھتا ہوا؟")]},
 ],
 "review_questions": [
   {"id": "r_term", "type": "apply", "skill": SKILL, "step": number_question(
     "r_term",
     T("A sequence has nth term 6n − 2. What is the 4th term?", "ایک سلسلے کا n واں رکن 6n − 2 ہے۔ چوتھا رکن کیا ہے؟"),
     R1,
     T("Put n = 4.", "n = 4 رکھیں۔"),
     T("Right! 6 × 4 − 2 = 22.", "درست! 6 × 4 − 2 = 22"),
     T("6 × 4 = 24, then 24 − 2 = 22.", "6 × 4 = 24، پھر 24 − 2 = 22"),
     common_wrong=[wrong(62, "6n is 6 × 4, not 64: 24 − 2 = 22.", "6n یعنی 6 × 4، 64 نہیں: 24 − 2 = 22", "joins_digits")],
     qtype=None)},
   {"id": "r_next", "type": "apply", "skill": SKILL, "step": number_question(
     "r_next",
     T("What is the next term of 3, 6, 12, 24, …?", "3، 6، 12، 24، … کا اگلا رکن کیا ہے؟"),
     R2,
     T("Look at how each term is made from the one before.", "دیکھیں ہر رکن پچھلے سے کیسے بنتا ہے۔"),
     T("Right! It doubles: 48.", "درست! یہ دگنا ہوتا ہے: 48"),
     T("Each term doubles: 24 × 2 = 48.", "ہر رکن دگنا ہوتا ہے: 24 × 2 = 48"),
     common_wrong=[wrong(36, "The gaps are 3, 6, 12, so each term doubles: 48.", "فرق 3، 6، 12 ہیں، تو ہر رکن دگنا ہوتا ہے: 48", "always_add")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh after matching the app with PCTB Mathematics 6 (Sub-domain 6, patterns and sequences). No textbook text or exercises were used.",
   "s8 (which term is 39?) uses the one-step equations of the earlier Simple equations lesson.",
   "Urdu terms to check: نمونہ (pattern), سلسلہ (sequence), رکن (term), اصول (rule).",
   "The numbers were worked out in content/sources/g6-maths-07/number_patterns.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import (attach, matchsticks, number_cards, seq_table, dot_squares, strip_figure,
                  en_list, ur_list)

HOOK = seq("3n + 1", 4)                      # sticks for 1, 2, 3, 4 squares
assert HOOK == [4, 7, 10, 13]
N2 = 5
assert value("3n + 1", n=N2) == S2
S4_SEQ = seq("4n + 1", 4)
S5_SEQ = [2, 4, 8, 16]
assert S5_SEQ[-1] * 2 == S5
S7_POS = [1, 2, 3, 4, 10]
S7_SEQ = seq("2n + 3", 4)
assert value("2n + 3", n=S7_POS[-1]) == S7
S8_SEQ = seq("4n − 1", 3)
TARGET8 = value("4n − 1", n=S8)
S11_POS = [1, 2, 3, 4, 20]
S11_SEQ = seq("4n + 3", 4)
assert value("4n + 3", n=S11_POS[-1]) == S11
BIG = 100                                    # summary: the 100th term
SUM_SEQ = seq("3n + 1", 3)
QB_RULE = seq("4n − 1", 4)
assert QB_RULE == [3, 7, 11, 15]
QB_SEQ = [50, 45, 40, 35]
assert QB_SEQ[-1] - 5 == QB
SQUARES = [1, 2, 3, 4]
R_SEQ = [3, 6, 12, 24]
assert R_SEQ[-1] * 2 == R2


def cards(values, en_what, ur_what, jumps=None, en_extra="", ur_extra=""):
    shown = [str(v) for v in values]
    return number_cards(values,
        f"Number cards in a row: {en_list(shown)}{en_what}, with a curved jump from each card to the next{en_extra}.",
        f"ایک قطار میں اعداد کے کارڈ: {ur_list(shown)}{ur_what}، ہر کارڈ سے اگلے تک ایک خم دار چھلانگ{ur_extra}۔",
        jumps=jumps)


def table(positions, terms, en, ur):
    return seq_table(positions, terms,
        f"A table with two rows. The top row, n, is the position of each term: {en_list(positions)}. The bottom row, T, is the term: {en_list(terms)}. {en}",
        f"دو قطاروں کی جدول۔ اوپر والی قطار n ہر رکن کا مقام ہے: {ur_list(positions)}۔ نیچے والی قطار T رکن ہے: {ur_list(terms)}۔ {ur}")


attach(lesson, {
    "s1_hook": matchsticks([1, 2, 3, 4],
        f"Rows of matchstick squares: 1, 2, 3 and 4 squares in a row, made of {en_list(HOOK)} sticks, with the number of sticks under each.",
        f"تیلیوں سے بنے مربعوں کی قطاریں: ایک قطار میں 1، 2، 3 اور 4 مربعے، جو {ur_list(HOOK)} تیلیوں سے بنے ہیں، ہر ایک کے نیچے تیلیوں کی تعداد۔",
        texts=[str(v) for v in HOOK]),
    "s2_foundation": strip_figure([("bags", 3, "n"), ("text", "+"), ("marbles", 1), ("text", f"n={N2}")],
        f"3 bags marked n, a plus sign and 1 marble, which is 3n + 1. Beside them: n={N2}, each bag holds {N2} marbles.",
        f"3 تھیلے جن پر n لکھا ہے، جمع کا نشان اور 1 کنچا، یعنی 3n + 1۔ ساتھ میں: n={N2}، ہر تھیلے میں {N2} کنچے ہیں۔"),
    "s3_rule": cards(HOOK, "", "", jumps=["+3"] * 3, en_extra=", each jump marked +3",
                     ur_extra="، ہر چھلانگ پر +3 لکھا ہے"),
    "s4_next": cards(S4_SEQ + ["?"], ", and a last card with a question mark", "، اور آخری کارڈ پر سوالیہ نشان"),
    "s5_double": cards(S5_SEQ + ["?"], ", and a last card with a question mark", "، اور آخری کارڈ پر سوالیہ نشان"),
    "s7_tenth": table(S7_POS, S7_SEQ + ["?"], "The 10th term has a question mark.", "دسویں رکن پر سوالیہ نشان ہے۔"),
    "s8_which_term": table([1, 2, 3, "?"], S8_SEQ + [TARGET8],
        f"The position of {TARGET8} has a question mark.", f"{TARGET8} کے مقام پر سوالیہ نشان ہے۔"),
    "s11_twentieth": table(S11_POS, S11_SEQ + ["?"], "The 20th term has a question mark.", "بیسویں رکن پر سوالیہ نشان ہے۔"),
    "s12_summary": table([1, 2, 3, BIG], SUM_SEQ + [value("3n + 1", n=BIG)],
        f"The rule 3n + 1 gives every term, even the {BIG}th: 3 × {BIG} + 1 = {value('3n + 1', n=BIG)}.",
        f"قاعدہ 3n + 1 ہر رکن دیتا ہے، {BIG} واں بھی: 3 × {BIG} + 1 = {value('3n + 1', n=BIG)}۔"),
    "qb_rule": cards(QB_RULE, "", ""),
    "qb_apply": cards(QB_SEQ + ["?"], ", and a last card with a question mark", "، اور آخری کارڈ پر سوالیہ نشان"),
    "qb_find_error": dot_squares(SQUARES,
        f"Square patterns of dots: {en_list([f'{k} by {k}' for k in SQUARES])}, which have {en_list([k * k for k in SQUARES])} dots.",
        f"نقطوں کے مربع نمونے: {ur_list([f'{k} ضرب {k}' for k in SQUARES])}، جن میں {ur_list([k * k for k in SQUARES])} نقطے ہیں۔"),
    "r_next": cards(R_SEQ + ["?"], ", and a last card with a question mark", "، اور آخری کارڈ پر سوالیہ نشان"),
})
write(lesson)

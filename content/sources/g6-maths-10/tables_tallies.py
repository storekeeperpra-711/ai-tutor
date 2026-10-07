from common import (T, opt, say, wrong, number_question, tally, table_text, write,
                    REF, REVIEW, TIMES_TABLES, DH_TABLES)

SKILL = DH_TABLES

# s4
S4 = 13
assert tally(S4) == "IIII/ IIII/ III" and tally(S4).count("I") == 11
# s5 to s7: favourite fruit votes
FRUIT = [(("Mango", "آم"), 8), (("Banana", "کیلا"), 5), (("Apple", "سیب"), 11), (("Orange", "کینو"), 6)]
FRUIT_EN, FRUIT_UR = table_text(FRUIT)
S5 = sum(v for _, v in FRUIT)
assert S5 == 30
S6 = 11 - 5
assert S6 == 6 and 11 + 5 == 16
assert max(FRUIT, key=lambda r: r[1])[0][0] == "Apple"
# s8: groups of five for 20
S8 = 20 // 5
assert S8 == 4 and tally(20).count("IIII/") == S8
# s9: IIII/ IIII/ II is 12; counting only the upright strokes gives 10
assert tally(12) == "IIII/ IIII/ II" and 4 + 4 + 2 == 10
# s11: three classes
S11 = 32 + 28 + 35
assert S11 == 95
# question bank and review
QB = 16
assert tally(QB) == "IIII/ IIII/ IIII/ I"
R1 = 9
assert tally(R1) == "IIII/ IIII"
BIRDS = [(("Sparrows", "چڑیاں"), 14), (("Crows", "کوّے"), 9), (("Parrots", "طوطے"), 5)]
BIRDS_EN, BIRDS_UR = table_text(BIRDS)
R2 = 14 - 5
assert R2 == 9 and 14 + 5 == 19

lesson = {
 "id": "g6-maths-10-tables-and-tallies",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Record data with tally marks, and read totals, differences and the largest group from a frequency table.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Tables and tally marks", "جدول اور ٹیلی کے نشان"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "skips_gate", "description": "Counts only the upright strokes of a tally group, so IIII/ is read as 4."},
   {"id": "adds_for_difference", "description": "Adds two counts when the question asks how many more."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_gate", "type": "recall", "step": {
     "id": "qb_gate", "type": "choice",
     "prompt": T("In tally marks, what does IIII/ (four lines and one across) stand for?", "ٹیلی کے نشانوں میں IIII/ (چار لکیریں اور ایک ترچھی) کا مطلب کیا ہے؟"),
     "options": [
       opt("five", "5", "5", True, "Yes! The line across is the fifth one.", "جی ہاں! ترچھی لکیر پانچویں ہے۔"),
       opt("four", "4", "4", False, "Count the line across too: 5.", "ترچھی لکیر بھی گنیں: 5۔", "skips_gate"),
       opt("ten", "10", "10", False, "One group is 5.", "ایک گروہ 5 ہے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T(f"How many do these tally marks show? {tally(QB)}", f"یہ ٹیلی کے نشان کتنے دکھاتے ہیں؟ {tally(QB)}"),
     QB,
     T("Three groups of 5, then 1 more.", "5 کے تین گروہ، پھر 1 اور۔"),
     T("Right! 16.", "درست! 16"),
     T("5 + 5 + 5 + 1 = 16.", "5 + 5 + 5 + 1 = 16"),
     common_wrong=[wrong(13, "Each group is 5, not 4: 5 + 5 + 5 + 1 = 16.", "ہر گروہ 5 ہے، 4 نہیں: 5 + 5 + 5 + 1 = 16", "skips_gate")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T(f"Votes: {BIRDS_EN}. Hira says 19 more children chose sparrows than parrots. What went wrong?",
                 f"ووٹ: {BIRDS_UR}۔ حرا کہتی ہے چڑیوں کو طوطوں سے 19 زیادہ بچوں نے چنا۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("subtract", "'How many more' means take away: 14 − 5 = 9.", "'کتنے زیادہ' کا مطلب نفی: 14 − 5 = 9", True,
           "Yes! She added instead of finding the difference.", "جی ہاں! اس نے فرق کی بجائے جمع کیا۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "14 + 5 = 19 is both together. 'How many more' is 14 − 5 = 9.", "14 + 5 = 19 دونوں مل کر ہیں۔ 'کتنے زیادہ' یعنی 14 − 5 = 9", "adds_for_difference"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_tally", "front": T("How do tally marks work?", "ٹیلی کے نشان کیسے کام کرتے ہیں؟"),
    "back": T("One stroke for each item. The fifth stroke goes across the first four: IIII/ = 5. Count in fives.", "ہر چیز کے لیے ایک لکیر۔ پانچویں لکیر پہلی چار کے اوپر ترچھی: IIII/ = 5۔ پانچ پانچ کر کے گنیں۔")},
   {"id": "f_more", "front": T("'How many more?'", "'کتنے زیادہ؟'"),
    "back": T("Take away: the bigger count minus the smaller.", "نفی کریں: بڑی گنتی میں سے چھوٹی۔")},
 ],
 "home_tasks": [{"id": "h_survey", "text": T(
   "Ask your family and neighbours their favourite colour. Keep a tally for each colour, then write the totals in a table. Which colour won?",
   "اپنے گھر والوں اور پڑوسیوں سے ان کا پسندیدہ رنگ پوچھیں۔ ہر رنگ کے لیے ٹیلی رکھیں، پھر کل تعداد جدول میں لکھیں۔ کون سا رنگ جیتا؟")}],
 "glossary": [T("Data", "مواد (ڈیٹا)"), T("Table", "جدول"), T("Tally marks", "ٹیلی کے نشان"), T("Total", "کل"), T("Frequency", "تعدد")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Your class votes for its favourite fruit. How can you count all the votes quickly, without losing track?",
                     "آپ کی جماعت پسندیدہ پھل کے لیے ووٹ دیتی ہے۔ آپ سب ووٹ جلدی، بغیر بھولے، کیسے گنیں گے؟"),
    "text": T("Today we record data with tally marks and read it from tables. First, a quick check.", "آج ہم ٹیلی کے نشانوں سے مواد لکھیں گے اور جدول سے پڑھیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("What is 5 × 3?", "5 × 3 کتنے ہیں؟"),
     15,
     T("Count in fives: 5, 10, 15.", "پانچ پانچ گنیں: 5، 10، 15"),
     T("Right! 15.", "درست! 15"),
     T("5 × 3 = 15.", "5 × 3 = 15"),
     common_wrong=[wrong(8, "8 is 5 + 3. Multiply: 5 × 3 = 15.", "8 یعنی 5 + 3۔ ضرب دیں: 5 × 3 = 15")],
     qtype="recall", skill=TIMES_TABLES),
   {"id": "s3_tally", "type": "explain",
    "character": say("happy", "Four lines, then one across. That makes a gate of five!", "چار لکیریں، پھر ایک ترچھی۔ یہ پانچ کا دروازہ بنتا ہے!"),
    "text": T("Tally marks: draw one line for each vote. The fifth line goes across the first four, written here as IIII/. So IIII/ IIII/ III is 5 + 5 + 3 = 13. A table (frequency table) lists each group with its total.",
              "ٹیلی کے نشان: ہر ووٹ کے لیے ایک لکیر۔ پانچویں لکیر پہلی چار کے اوپر ترچھی جاتی ہے، یہاں IIII/ لکھی گئی ہے۔ تو IIII/ IIII/ III یعنی 5 + 5 + 3 = 13۔ جدول (تعدد کا جدول) ہر گروہ اور اس کی کل تعداد دکھاتا ہے۔")},
   number_question(
     "s4_read_tally",
     T(f"How many do these tally marks show? {tally(S4)}", f"یہ ٹیلی کے نشان کتنے دکھاتے ہیں؟ {tally(S4)}"),
     S4,
     T("Two gates of 5, then 3.", "5 کے دو دروازے، پھر 3"),
     T("Right! 13.", "درست! 13"),
     T("5 + 5 + 3 = 13.", "5 + 5 + 3 = 13"),
     common_wrong=[wrong(11, "Each gate is 5, not 4: 5 + 5 + 3 = 13.", "ہر دروازہ 5 ہے، 4 نہیں: 5 + 5 + 3 = 13", "skips_gate"),
                   wrong(3, "Count the gates too: 5 + 5 + 3 = 13.", "دروازے بھی گنیں: 5 + 5 + 3 = 13")]),
   number_question(
     "s5_total",
     T(f"Favourite fruit votes: {FRUIT_EN}. How many children voted altogether?", f"پسندیدہ پھل کے ووٹ: {FRUIT_UR}۔ کل کتنے بچوں نے ووٹ دیا؟"),
     S5,
     T("Add all four numbers.", "چاروں عدد جمع کریں۔"),
     T("Right! 30 children.", "درست! 30 بچے"),
     T("8 + 5 + 11 + 6 = 30.", "8 + 5 + 11 + 6 = 30"),
     common_wrong=[wrong(4, "4 is the number of fruits. Add the votes: 30.", "4 پھلوں کی تعداد ہے۔ ووٹ جمع کریں: 30")]),
   number_question(
     "s6_more",
     T(f"Same votes: {FRUIT_EN}. How many more children chose apple than banana?", f"وہی ووٹ: {FRUIT_UR}۔ سیب کو کیلے سے کتنے زیادہ بچوں نے چنا؟"),
     S6,
     T("'How many more' means take away.", "'کتنے زیادہ' کا مطلب نفی۔"),
     T("Right! 11 − 5 = 6 more.", "درست! 11 − 5 = 6 زیادہ"),
     T("11 − 5 = 6.", "11 − 5 = 6"),
     common_wrong=[wrong(16, "16 is both together. 'How many more' is 11 − 5 = 6.", "16 دونوں مل کر ہیں۔ 'کتنے زیادہ' یعنی 11 − 5 = 6", "adds_for_difference")]),
   {"id": "s7_most", "type": "choice", "question_type": "apply",
    "prompt": T(f"Same votes: {FRUIT_EN}. Which fruit was the most popular?", f"وہی ووٹ: {FRUIT_UR}۔ سب سے زیادہ پسند کیا جانے والا پھل کون سا تھا؟"),
    "options": [
      opt("apple", "Apple", "سیب", True, "Yes! Apple has the most votes, 11.", "جی ہاں! سیب کے سب سے زیادہ ووٹ ہیں، 11۔"),
      opt("mango", "Mango", "آم", False, "Mango has 8. Apple has more: 11.", "آم کے 8 ہیں۔ سیب کے زیادہ ہیں: 11۔"),
      opt("banana", "Banana", "کیلا", False, "Banana has the fewest, 5. Look for the biggest number.", "کیلے کے سب سے کم، 5، ہیں۔ سب سے بڑا عدد دیکھیں۔"),
    ]},
   number_question(
     "s8_gates",
     T("How many full gates of five do you draw to show 20 votes in tally marks?", "20 ووٹ ٹیلی میں دکھانے کے لیے پانچ کے کتنے پورے دروازے بنائیں گے؟"),
     S8,
     T("20 ÷ 5.", "20 ÷ 5"),
     T("Right! 4 gates.", "درست! 4 دروازے"),
     T("20 ÷ 5 = 4.", "20 ÷ 5 = 4"),
     common_wrong=[wrong(5, "Each gate holds 5 votes: 20 ÷ 5 = 4 gates.", "ہر دروازے میں 5 ووٹ: 20 ÷ 5 = 4 دروازے")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Zain reads the tally IIII/ IIII/ II as 4 + 4 + 2 = 10. What went wrong?", "زین ٹیلی IIII/ IIII/ II کو 4 + 4 + 2 = 10 پڑھتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("gate", "He didn't count the lines across. Each gate is 5: 5 + 5 + 2 = 12.", "اس نے ترچھی لکیریں نہیں گنیں۔ ہر دروازہ 5 ہے: 5 + 5 + 2 = 12", True,
          "Yes! The line across is the fifth vote.", "جی ہاں! ترچھی لکیر پانچواں ووٹ ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "IIII/ is 5, not 4. The answer is 12.", "IIII/ پانچ ہے، چار نہیں۔ جواب 12 ہے۔", "skips_gate"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we draw the fifth tally line across the others? Can you teach me?",
                     "ہم پانچویں ٹیلی لکیر باقی کے اوپر ترچھی کیوں بناتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why do we cross every fifth tally mark?", "اپنے الفاظ میں بتائیں: ہم ہر پانچویں ٹیلی کو ترچھا کیوں کرتے ہیں؟"),
    "key_idea": "Crossing every fifth line makes groups of five, so you can count quickly in fives instead of counting every single line, and you make fewer mistakes.",
    "levels": {
      "got_it": "Says it makes groups of five that you can count in fives, so counting is faster or easier.",
      "partly": "Says it makes counting easier without mentioning groups of five, or the reverse.",
      "not_yet": "Gives no reason, or says it is just for decoration."},
    "keywords": [
      ["five", "5", "پانچ", "paanch"],
      ["group", "bundle", "گروہ", "گچھا"],
      ["quick", "fast", "easy", "count", "جلدی", "آسان", "گن"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Groups of five let you count in fives, fast and without mistakes.", "بہت خوب! پانچ کے گروہ سے پانچ پانچ کر کے، جلدی اور بغیر غلطی، گن سکتے ہیں۔"),
      "partly": T("Good start! Now say what the crossing line makes.", "اچھی شروعات! اب بتائیں ترچھی لکیر کیا بناتی ہے۔"),
      "not_yet": T("Try counting 23 single lines, then 4 gates and 3 lines. Which is quicker? Why?", "23 اکیلی لکیریں گنیں، پھر 4 دروازے اور 3 لکیریں۔ کون سا جلدی ہے؟ کیوں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_classes",
     T("Class 6A has 32 students, 6B has 28 and 6C has 35. How many students are there in Grade 6 altogether?", "جماعت 6A میں 32، 6B میں 28 اور 6C میں 35 طالب علم ہیں۔ چھٹی جماعت میں کل کتنے طالب علم ہیں؟"),
     S11,
     T("Add the three classes.", "تینوں جماعتیں جمع کریں۔"),
     T("Right! 95 students.", "درست! 95 طالب علم"),
     T("32 + 28 + 35 = 95.", "32 + 28 + 35 = 95"),
     common_wrong=[wrong(60, "That is only 6A and 6B. Add 6C too: 95.", "یہ صرف 6A اور 6B ہیں۔ 6C بھی جمع کریں: 95")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can count and read data now!", "اب آپ مواد گن اور پڑھ سکتے ہیں!"),
    "text": T("Tally marks group votes in fives: IIII/ is 5, so count in fives and add the leftovers. A table lists each group with its total. Add for 'altogether'; take away for 'how many more'.",
              "ٹیلی کے نشان ووٹوں کو پانچ کے گروہوں میں رکھتے ہیں: IIII/ پانچ ہے، تو پانچ پانچ گنیں اور بچ جانے والے جمع کریں۔ جدول ہر گروہ کی کل تعداد دکھاتا ہے۔ 'کل' کے لیے جمع؛ 'کتنے زیادہ' کے لیے نفی۔"),
    "points": [T("IIII/ = 5.", "IIII/ = 5۔"),
               T("'How many more' means take away.", "'کتنے زیادہ' یعنی نفی۔")]},
 ],
 "review_questions": [
   {"id": "r_tally", "type": "recall", "skill": SKILL, "step": number_question(
     "r_tally",
     T(f"How many do these tally marks show? {tally(R1)}", f"یہ ٹیلی کے نشان کتنے دکھاتے ہیں؟ {tally(R1)}"),
     R1,
     T("One gate of 5, then 4.", "5 کا ایک دروازہ، پھر 4"),
     T("Right! 9.", "درست! 9"),
     T("5 + 4 = 9.", "5 + 4 = 9"),
     common_wrong=[wrong(8, "The gate is 5: 5 + 4 = 9.", "دروازہ 5 ہے: 5 + 4 = 9", "skips_gate")],
     qtype=None)},
   {"id": "r_more", "type": "apply", "skill": SKILL, "step": number_question(
     "r_more",
     T(f"Birds seen: {BIRDS_EN}. How many more sparrows than parrots?", f"دیکھے گئے پرندے: {BIRDS_UR}۔ چڑیاں طوطوں سے کتنی زیادہ ہیں؟"),
     R2,
     T("14 − 5.", "14 − 5"),
     T("Right! 9 more.", "درست! 9 زیادہ"),
     T("14 − 5 = 9.", "14 − 5 = 9"),
     common_wrong=[wrong(19, "That adds them. 'How many more' is 14 − 5 = 9.", "یہ جمع ہے۔ 'کتنے زیادہ' یعنی 14 − 5 = 9", "adds_for_difference")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Data Handling unit. No textbook text or exercises were used.",
   "There are no pictures yet, so a tally group of five is written IIII/ and tables are written as short lists. Real tally marks on paper (the home task) help children see the 'gate'.",
   "Urdu terms to check: مواد / ڈیٹا (data), جدول (table), ٹیلی کے نشان (tally marks), تعدد (frequency).",
   "The numbers were worked out in content/sources/g6-maths-10/tables_tallies.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

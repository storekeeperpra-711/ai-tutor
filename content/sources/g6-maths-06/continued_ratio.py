from common import (T, opt, say, wrong, number_question, ratio_question,
                    continued_question, continued, simplest, simplest_all,
                    join, share, write, BOOK, REVIEW, RATIO_EQUIVALENT,
                    RATIO_SHARE, RATIO_CONTINUED)

SKILL = RATIO_CONTINUED

# s2: 12:18 in simplest form
S2 = simplest(12, 18)
assert S2 == (2, 3)
# s4: 10:15:20 in simplest form
S4 = simplest_all(10, 15, 20)
assert S4 == (2, 3, 4)
# s5: Rs 900 in 2:3:4, the smallest share (900 ÷ 3 = 300)
S5 = share(900, (2, 3, 4))
assert S5 == [200, 300, 400]
# s6: a:b = 2:3, b:c = 3:5
assert join((2, 3), (3, 5)) == (2, 3, 5)
# s7: a:b = 2:3, b:c = 4:5 (just joining gives 2:3:5)
S7 = join((2, 3), (4, 5))
assert S7 == (8, 12, 15)
# s8: flour:sugar:butter = 5:2:3, 500 g in all; sugar (500 ÷ 2 = 250)
S8 = share(500, (5, 2, 3))[1]
assert S8 == 100
# s9: a:b = 1:2, b:c = 3:4 is 3:6:8, not 1:2:4
assert join((1, 2), (3, 4)) == (3, 6, 8)
# s11: ages 3:4:5, sum 36; oldest (36 ÷ 3 = 12)
S11 = share(36, (3, 4, 5))[2]
assert S11 == 15
# question bank: Rs 120 in 1:2:3, largest (120 ÷ 3 = 40)
QB = share(120, (1, 2, 3))[2]
assert QB == 60
# review: 6:9:12 simplest; Rs 1,000 in 1:4:5, the middle share
R1 = simplest_all(6, 9, 12)
assert R1 == (2, 3, 4)
R2 = share(1000, (1, 4, 5))[1]
assert R2 == 400

lesson = {
 "id": "g6-maths-06-continued-ratio",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find and simplify a continued ratio of three quantities, and share an amount in a continued ratio.", "textbook": f"{BOOK}, 4.2 Ratio (continued ratio)"}],
 "skills": [SKILL],
 "title": T("Continued ratio", "مسلسل نسبت"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": RATIO_EQUIVALENT}, {"skill": RATIO_SHARE}],
 "misconceptions": [
   {"id": "joins_without_matching", "description": "Joins a:b and b:c into a:b:c without making the two b's the same."},
   {"id": "divides_by_count", "description": "Shares an amount by the number of people (3) instead of the total parts."},
   {"id": "not_all_terms", "description": "Divides only some terms of the ratio when simplifying."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("A continued ratio like 2:3:4 compares …", "2:3:4 جیسی مسلسل نسبت موازنہ کرتی ہے …"),
     "options": [
       opt("three", "three or more quantities", "تین یا زیادہ مقداروں کا", True,
           "Yes! 2:3:4 compares three quantities at once.", "جی ہاں! 2:3:4 ایک ساتھ تین مقداروں کا موازنہ کرتی ہے۔"),
       opt("two", "only two quantities", "صرف دو مقداروں کا", False,
           "A ratio like 2:3 compares two. A continued ratio compares three or more.", "2:3 جیسی نسبت دو کا موازنہ کرتی ہے۔ مسلسل نسبت تین یا زیادہ کا۔"),
       opt("time", "things that happen one after another", "ایک کے بعد ایک ہونے والی چیزوں کا", False,
           "'Continued' means the ratio carries on to a third term: a:b:c.", "'مسلسل' یعنی نسبت تیسرے حصے تک چلتی ہے: a:b:c"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("Share Rs 120 in the ratio 1:2:3. What is the largest share?", "120 روپے کو 1:2:3 کی نسبت سے بانٹیں۔ سب سے بڑا حصہ کتنا ہے؟"),
     QB,
     T("1 + 2 + 3 = 6 parts. One part is 120 ÷ 6.", "1 + 2 + 3 = 6 حصے۔ ایک حصہ 120 ÷ 6"),
     T("Right! One part is Rs 20, so 3 parts are Rs 60.", "درست! ایک حصہ 20 روپے، تو 3 حصے 60 روپے۔"),
     T("120 ÷ 6 = 20 for one part; 3 × 20 = 60.", "ایک حصہ 120 ÷ 6 = 20؛ 3 × 20 = 60"),
     common_wrong=[wrong(40, "Don't divide by 3 people: there are 1 + 2 + 3 = 6 parts. 3 × 20 = 60.", "3 لوگوں سے تقسیم نہ کریں: 1 + 2 + 3 = 6 حصے ہیں۔ 3 × 20 = 60", "divides_by_count")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Bilal simplifies 8:12:20 and writes 2:3:20. What is wrong?", "بلال 8:12:20 کو مختصر کر کے 2:3:20 لکھتا ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("all_terms", "Every term must be divided by 4: 2:3:5.", "ہر حصے کو 4 سے تقسیم کرنا ہے: 2:3:5", True,
           "Yes! Divide all three terms by the same number.", "جی ہاں! تینوں حصوں کو ایک ہی عدد سے تقسیم کریں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "He forgot to divide 20 by 4. 8:12:20 = 2:3:5.", "وہ 20 کو 4 سے تقسیم کرنا بھول گیا۔ 8:12:20 = 2:3:5", "not_all_terms"),
       opt("add", "He should add 4 to each term.", "اسے ہر حصے میں 4 جمع کرنا چاہیے۔", False,
           "Ratios are simplified by dividing every term: 2:3:5.", "نسبت کو ہر حصہ تقسیم کر کے مختصر کرتے ہیں: 2:3:5"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_continued", "front": T("Continued ratio?", "مسلسل نسبت؟"),
    "back": T("A ratio of three or more quantities, like a:b:c = 2:3:4.", "تین یا زیادہ مقداروں کی نسبت، جیسے a:b:c = 2:3:4")},
   {"id": "f_join", "front": T("a:b and b:c to a:b:c?", "a:b اور b:c سے a:b:c؟"),
    "back": T("Make the two b's the same first: 2:3 and 4:5 become 8:12 and 12:15, so 8:12:15.", "پہلے دونوں b برابر کریں: 2:3 اور 4:5 بنتے ہیں 8:12 اور 12:15، تو 8:12:15")},
 ],
 "home_tasks": [{"id": "h_recipe", "text": T(
   "Find a recipe at home with three main things (like rice, water and lentils). Write their amounts as a continued ratio and simplify it.",
   "گھر میں کوئی ترکیب ڈھونڈیں جس میں تین اہم چیزیں ہوں (جیسے چاول، پانی اور دال)۔ ان کی مقداریں مسلسل نسبت میں لکھیں اور مختصر کریں۔")}],
 "glossary": [T("Continued ratio", "مسلسل نسبت"), T("Term", "حصہ (رکن)"), T("Simplest form", "مختصر ترین شکل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Three friends share sweets: 2 for Ali, 3 for Bilal, 4 for Hamza. How do we write that as one ratio?",
                     "تین دوست مٹھائی بانٹتے ہیں: علی کی 2، بلال کی 3، حمزہ کی 4۔ اسے ایک نسبت میں کیسے لکھیں؟"),
    "text": T("Today we learn continued ratios: ratios of three quantities. First, simplify a ratio of two.", "آج ہم مسلسل نسبت سیکھیں گے: تین مقداروں کی نسبت۔ پہلے دو کی نسبت مختصر کریں۔")},
   ratio_question(
     "s2_foundation",
     T("Write 12:18 in its simplest form.", "12:18 کو مختصر ترین شکل میں لکھیں۔"),
     *S2,
     T("Divide both by 6.", "دونوں کو 6 سے تقسیم کریں۔"),
     T("Right! 12:18 = 2:3.", "درست! 12:18 = 2:3"),
     T("12 ÷ 6 = 2 and 18 ÷ 6 = 3, so 2:3.", "12 ÷ 6 = 2 اور 18 ÷ 6 = 3، تو 2:3"),
     common_wrong=[wrong("6:9", "6:9 is right but not simplest: divide by 3 again, 2:3.", "6:9 ٹھیک ہے مگر مختصر ترین نہیں: دوبارہ 3 سے تقسیم کریں، 2:3")],
     qtype="recall", skill=RATIO_EQUIVALENT),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Same rules as before, just one more term. Divide every term by the same number!", "وہی اصول، بس ایک حصہ اور۔ ہر حصے کو ایک ہی عدد سے تقسیم کریں!"),
    "text": T("A continued ratio compares three or more quantities: Ali : Bilal : Hamza = 2 : 3 : 4. To simplify it, divide every term by the same number: 10:15:20 = 2:3:4. To join a:b and b:c, the two b's must be the same: a:b = 2:3 and b:c = 3:5 give a:b:c = 2:3:5. To share an amount, add the parts (2 + 3 + 4 = 9), find one part, then multiply.",
              "مسلسل نسبت تین یا زیادہ مقداروں کا موازنہ کرتی ہے: علی : بلال : حمزہ = 2 : 3 : 4۔ اسے مختصر کرنے کے لیے ہر حصے کو ایک ہی عدد سے تقسیم کریں: 10:15:20 = 2:3:4۔ a:b اور b:c کو جوڑنے کے لیے دونوں b برابر ہونے چاہئیں: a:b = 2:3 اور b:c = 3:5 سے a:b:c = 2:3:5۔ کوئی رقم بانٹنے کے لیے حصے جمع کریں (2 + 3 + 4 = 9)، ایک حصہ نکالیں، پھر ضرب دیں۔")},
   continued_question(
     "s4_simplify",
     T("Write 10:15:20 in its simplest form.", "10:15:20 کو مختصر ترین شکل میں لکھیں۔"),
     S4,
     T("All three can be divided by 5.", "تینوں 5 سے تقسیم ہو سکتے ہیں۔"),
     T(f"Right! 10:15:20 = {continued(*S4)}.", f"درست! 10:15:20 = {continued(*S4)}"),
     T("Divide each term by 5: 2, 3, 4. So 2:3:4.", "ہر حصے کو 5 سے تقسیم کریں: 2، 3، 4۔ تو 2:3:4"),
     common_wrong=[wrong("2:3:20", "Divide the last term by 5 too: 20 ÷ 5 = 4. So 2:3:4.", "آخری حصہ بھی 5 سے تقسیم کریں: 20 ÷ 5 = 4۔ تو 2:3:4", "not_all_terms")]),
   number_question(
     "s5_share",
     T("Rs 900 is shared among three children in the ratio 2:3:4. What is the smallest share?", "900 روپے تین بچوں میں 2:3:4 کی نسبت سے بانٹے جاتے ہیں۔ سب سے چھوٹا حصہ کتنا ہے؟"),
     S5[0],
     T("2 + 3 + 4 = 9 parts. One part is 900 ÷ 9.", "2 + 3 + 4 = 9 حصے۔ ایک حصہ 900 ÷ 9"),
     T("Right! One part is Rs 100, so 2 parts are Rs 200.", "درست! ایک حصہ 100 روپے، تو 2 حصے 200 روپے۔"),
     T("900 ÷ 9 = 100; the smallest share is 2 × 100 = 200.", "900 ÷ 9 = 100؛ سب سے چھوٹا حصہ 2 × 100 = 200"),
     common_wrong=[wrong(300, "Don't divide by 3 children: there are 9 parts. 2 × 100 = 200.", "3 بچوں سے تقسیم نہ کریں: 9 حصے ہیں۔ 2 × 100 = 200", "divides_by_count")]),
   {"id": "s6_join", "type": "choice",
    "prompt": T("a:b = 2:3 and b:c = 3:5. What is a:b:c?", "a:b = 2:3 اور b:c = 3:5۔ a:b:c کیا ہے؟"),
    "options": [
      opt("two_three_five", "2:3:5", "2:3:5", True, "Yes! b is 3 in both, so they join at once.", "جی ہاں! دونوں میں b = 3 ہے، تو سیدھا جڑ جاتے ہیں۔"),
      opt("two_six_five", "2:6:5", "2:6:5", False, "Don't add the b's. b is 3 in both: 2:3:5.", "b جمع نہ کریں۔ دونوں میں b = 3 ہے: 2:3:5"),
      opt("five_three_two", "5:3:2", "5:3:2", False, "Keep the order a, b, c: 2:3:5.", "ترتیب a، b، c رکھیں: 2:3:5"),
    ]},
   continued_question(
     "s7_match",
     T("a:b = 2:3 and b:c = 4:5. Make the b's the same and write a:b:c.", "a:b = 2:3 اور b:c = 4:5۔ b برابر کریں اور a:b:c لکھیں۔"),
     S7,
     T("Make b = 12: 2:3 = 8:12 and 4:5 = 12:15.", "b = 12 بنائیں: 2:3 = 8:12 اور 4:5 = 12:15"),
     T(f"Right! a:b:c = {continued(*S7)}.", f"درست! a:b:c = {continued(*S7)}"),
     T("2:3 × 4 = 8:12 and 4:5 × 3 = 12:15, so a:b:c = 8:12:15.", "2:3 کو 4 سے ضرب = 8:12 اور 4:5 کو 3 سے ضرب = 12:15، تو a:b:c = 8:12:15"),
     common_wrong=[wrong("2:3:5", "b is 3 in one ratio and 4 in the other. Make both 12 first: 8:12:15.", "ایک نسبت میں b = 3 ہے اور دوسری میں 4۔ پہلے دونوں 12 بنائیں: 8:12:15", "joins_without_matching"),
                   wrong("2:7:5", "Don't add the b's. Make them equal: 8:12:15.", "b جمع نہ کریں۔ انہیں برابر کریں: 8:12:15", "joins_without_matching")]),
   number_question(
     "s8_recipe",
     T("A cake mix has flour, sugar and butter in the ratio 5:2:3. The mix weighs 500 g. How many grams of sugar are in it?", "کیک کے آمیزے میں آٹا، چینی اور مکھن 5:2:3 کی نسبت میں ہیں۔ آمیزہ 500 گرام کا ہے۔ اس میں کتنے گرام چینی ہے؟"),
     S8,
     T("5 + 2 + 3 = 10 parts. One part is 500 ÷ 10.", "5 + 2 + 3 = 10 حصے۔ ایک حصہ 500 ÷ 10"),
     T("Right! One part is 50 g, so sugar is 100 g.", "درست! ایک حصہ 50 گرام، تو چینی 100 گرام۔"),
     T("500 ÷ 10 = 50; sugar is 2 × 50 = 100 g.", "500 ÷ 10 = 50؛ چینی 2 × 50 = 100 گرام"),
     common_wrong=[wrong(250, "500 ÷ 2 halves it. Use all 10 parts: 2 × 50 = 100.", "500 ÷ 2 آدھا کرتا ہے۔ تمام 10 حصے لیں: 2 × 50 = 100")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("a:b = 1:2 and b:c = 3:4. Sana writes a:b:c = 1:2:4. What is wrong?", "a:b = 1:2 اور b:c = 3:4۔ ثنا a:b:c = 1:2:4 لکھتی ہے۔ کیا غلطی ہے؟"),
    "options": [
      opt("match", "The b's are 2 and 3. Make both 6: 3:6 and 6:8, so 3:6:8.", "b ایک میں 2 اور دوسرے میں 3 ہے۔ دونوں 6 بنائیں: 3:6 اور 6:8، تو 3:6:8", True,
          "Yes! The middle term must match before joining.", "جی ہاں! جوڑنے سے پہلے درمیانی حصہ برابر ہونا چاہیے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "In 1:2:4, b:c is 2:4 = 1:2, not 3:4. The answer is 3:6:8.", "1:2:4 میں b:c = 2:4 = 1:2 ہے، 3:4 نہیں۔ جواب 3:6:8 ہے۔", "joins_without_matching"),
      opt("add", "Add the ratios: 4:6.", "نسبتیں جمع کریں: 4:6", False,
          "Ratios are not added. Match the b's: 3:6:8.", "نسبتیں جمع نہیں ہوتیں۔ b برابر کریں: 3:6:8"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why can't I just write the numbers next to each other? Teach me!",
                     "میں اعداد کو ساتھ ساتھ کیوں نہیں لکھ سکتا؟ مجھے سکھائیں!"),
    "task": T("Ali : Bilal = 2 : 3 and Bilal : Hamza = 4 : 5. Explain why Ali : Bilal : Hamza is not 2 : 3 : 5.", "علی : بلال = 2 : 3 اور بلال : حمزہ = 4 : 5۔ بتائیں کہ علی : بلال : حمزہ، 2 : 3 : 5 کیوں نہیں ہے۔"),
    "key_idea": "Bilal is 3 parts in one ratio and 4 parts in the other, so the parts are different sizes. Make Bilal the same in both (12): 8:12 and 12:15. So Ali : Bilal : Hamza = 8 : 12 : 15.",
    "levels": {
      "got_it": "Says Bilal's parts differ (3 and 4), makes them the same (12), and gives 8:12:15.",
      "partly": "Says the b's must be the same but doesn't finish, or gives 8:12:15 without a reason.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["same", "equal", "برابر"],
      ["12", "twelve", "بارہ"],
      ["8:12:15", "8 : 12 : 15"],
      ["Bilal", "b", "بلال"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Bilal must be the same: 8:12:15.", "بہت خوب! بلال برابر ہونا چاہیے: 8:12:15"),
      "partly": T("Good start! Now make Bilal 12 in both ratios.", "اچھی شروعات! اب دونوں نسبتوں میں بلال کو 12 بنائیں۔"),
      "not_yet": T("Bilal is 3 in one ratio and 4 in the other. Can both be 12?", "بلال ایک نسبت میں 3 اور دوسری میں 4 ہے۔ کیا دونوں 12 ہو سکتے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_ages",
     T("The ages of three brothers are in the ratio 3:4:5. Their ages add up to 36 years. How old is the oldest?", "تین بھائیوں کی عمریں 3:4:5 کی نسبت میں ہیں۔ ان کی عمروں کا مجموعہ 36 سال ہے۔ سب سے بڑا کتنے سال کا ہے؟"),
     S11,
     T("3 + 4 + 5 = 12 parts. One part is 36 ÷ 12.", "3 + 4 + 5 = 12 حصے۔ ایک حصہ 36 ÷ 12"),
     T("Right! One part is 3 years, so the oldest is 15.", "درست! ایک حصہ 3 سال، تو سب سے بڑا 15 سال کا۔"),
     T("36 ÷ 12 = 3; the oldest is 5 × 3 = 15 years.", "36 ÷ 12 = 3؛ سب سے بڑا 5 × 3 = 15 سال"),
     common_wrong=[wrong(12, "Don't divide by 3 brothers: there are 12 parts. 5 × 3 = 15.", "3 بھائیوں سے تقسیم نہ کریں: 12 حصے ہیں۔ 5 × 3 = 15", "divides_by_count")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Two terms or three, the rules stay the same. Well done!", "دو حصے ہوں یا تین، اصول وہی رہتے ہیں۔ شاباش!"),
    "text": T("A continued ratio compares three or more quantities. Simplify by dividing every term by the same number. To join a:b and b:c, first make the b's the same. To share, add all the parts, find one part, then multiply.",
              "مسلسل نسبت تین یا زیادہ مقداروں کا موازنہ کرتی ہے۔ ہر حصے کو ایک ہی عدد سے تقسیم کر کے مختصر کریں۔ a:b اور b:c جوڑنے کے لیے پہلے b برابر کریں۔ بانٹنے کے لیے سب حصے جمع کریں، ایک حصہ نکالیں، پھر ضرب دیں۔"),
    "points": [T("Divide every term.", "ہر حصہ تقسیم کریں۔"),
               T("Match b before joining.", "جوڑنے سے پہلے b برابر کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_simplify", "type": "apply", "skill": SKILL, "step": continued_question(
     "r_simplify",
     T("Write 6:9:12 in its simplest form.", "6:9:12 کو مختصر ترین شکل میں لکھیں۔"),
     R1,
     T("All three can be divided by 3.", "تینوں 3 سے تقسیم ہو سکتے ہیں۔"),
     T("Right! 2:3:4.", "درست! 2:3:4"),
     T("6 ÷ 3, 9 ÷ 3, 12 ÷ 3: 2:3:4.", "6 ÷ 3، 9 ÷ 3، 12 ÷ 3: 2:3:4"),
     common_wrong=[wrong("2:3:12", "Divide 12 by 3 too: 2:3:4.", "12 کو بھی 3 سے تقسیم کریں: 2:3:4", "not_all_terms")],
     qtype=None)},
   {"id": "r_share", "type": "apply", "skill": SKILL, "step": number_question(
     "r_share",
     T("Rs 1,000 is shared in the ratio 1:4:5. What is the middle share (4 parts)?", "1,000 روپے 1:4:5 کی نسبت سے بانٹے جاتے ہیں۔ درمیانی حصہ (4 حصے) کتنا ہے؟"),
     R2,
     T("1 + 4 + 5 = 10 parts.", "1 + 4 + 5 = 10 حصے۔"),
     T("Right! 4 × 100 = Rs 400.", "درست! 4 × 100 = 400 روپے"),
     T("1,000 ÷ 10 = 100; 4 × 100 = 400.", "1,000 ÷ 10 = 100؛ 4 × 100 = 400"),
     common_wrong=[wrong(250, "1,000 ÷ 4 is not one part. There are 10 parts: 4 × 100 = 400.", "1,000 ÷ 4 ایک حصہ نہیں۔ 10 حصے ہیں: 4 × 100 = 400")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh after matching the app with PCTB Mathematics 6 (Sub-domain 4, continued ratio). No textbook text or exercises were used.",
   "Answers like 8:12:15 are typed and checked exactly (spaces don't matter), so a ratio that is right but not simplest is marked wrong with a hint.",
   "Urdu terms to check: مسلسل نسبت (continued ratio), حصہ / رکن (term). The book also uses antecedent and consequent; this lesson doesn't need them.",
   "The numbers were worked out in content/sources/g6-maths-06/continued_ratio.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import attach, counters, bars


def share_bars(parts, ask, total_text, alt_en, alt_ur):
    """One strip of equal boxes for each share; the share asked for is
    shaded and marked "?", all the strips together make total_text."""
    rows = [(p, None, "?" if i == ask else None, i == ask) for i, p in enumerate(parts)]
    return bars(rows, alt_en, alt_ur, total=total_text)


attach(lesson, {
  "s1_hook": counters(
    [(2, True, "2"), (3, True, "3"), (4, True, "4")],
    "Three rows of sweets: 2 dots for Ali, 3 dots for Bilal and 4 dots for Hamza.",
    "مٹھائیوں کی تین قطاریں: علی کے لیے 2 نقطے، بلال کے لیے 3 نقطے اور حمزہ کے لیے 4 نقطے۔"),
  "s3_rule": bars(
    [(2, None, "2", False), (3, None, "3", False), (4, None, "4", False)],
    "A bar model for 2 : 3 : 4: three strips of equal boxes, 2 boxes, 3 boxes and 4 boxes. A bracket joins all three strips and is marked 9, the total number of parts.",
    "2 : 3 : 4 کا پٹی ماڈل: برابر خانوں کی تین پٹیاں، 2 خانے، 3 خانے اور 4 خانے۔ ایک قوس تینوں پٹیوں کو ملاتی ہے اور اس پر 9 لکھا ہے، یعنی کل حصے۔",
    total=str(sum((2, 3, 4)))),
  "s5_share": share_bars(
    (2, 3, 4), 0, "Rs900",
    "A bar model: strips of 2, 3 and 4 equal boxes, joined by a bracket marked Rs 900. The smallest strip, 2 boxes, is shaded and marked with a question mark.",
    "پٹی ماڈل: 2، 3 اور 4 برابر خانوں کی پٹیاں، جنہیں Rs 900 لکھی قوس ملاتی ہے۔ سب سے چھوٹی پٹی، 2 خانے، بھری ہوئی ہے اور اس پر سوالیہ نشان ہے۔"),
  "s8_recipe": share_bars(
    (5, 2, 3), 1, "500g",
    "A bar model for flour, sugar and butter: strips of 5, 2 and 3 equal boxes, joined by a bracket marked 500 g. The sugar strip, 2 boxes, is shaded and marked with a question mark.",
    "آٹے، چینی اور مکھن کا پٹی ماڈل: 5، 2 اور 3 برابر خانوں کی پٹیاں، جنہیں 500 گرام لکھی قوس ملاتی ہے۔ چینی کی پٹی، 2 خانے، بھری ہوئی ہے اور اس پر سوالیہ نشان ہے۔"),
  "s11_ages": share_bars(
    (3, 4, 5), 2, "36",
    "A bar model for the three brothers' ages: strips of 3, 4 and 5 equal boxes, joined by a bracket marked 36. The oldest brother's strip, 5 boxes, is shaded and marked with a question mark.",
    "تین بھائیوں کی عمروں کا پٹی ماڈل: 3، 4 اور 5 برابر خانوں کی پٹیاں، جنہیں 36 لکھی قوس ملاتی ہے۔ سب سے بڑے بھائی کی پٹی، 5 خانے، بھری ہوئی ہے اور اس پر سوالیہ نشان ہے۔"),
  "qb_apply": share_bars(
    (1, 2, 3), 2, "Rs120",
    "A bar model: strips of 1, 2 and 3 equal boxes, joined by a bracket marked Rs 120. The largest strip, 3 boxes, is shaded and marked with a question mark.",
    "پٹی ماڈل: 1، 2 اور 3 برابر خانوں کی پٹیاں، جنہیں Rs 120 لکھی قوس ملاتی ہے۔ سب سے بڑی پٹی، 3 خانے، بھری ہوئی ہے اور اس پر سوالیہ نشان ہے۔"),
  "r_share": share_bars(
    (1, 4, 5), 1, "Rs1000",
    "A bar model: strips of 1, 4 and 5 equal boxes, joined by a bracket marked Rs 1,000. The middle strip, 4 boxes, is shaded and marked with a question mark.",
    "پٹی ماڈل: 1، 4 اور 5 برابر خانوں کی پٹیاں، جنہیں Rs 1,000 لکھی قوس ملاتی ہے۔ درمیانی پٹی، 4 خانے، بھری ہوئی ہے اور اس پر سوالیہ نشان ہے۔"),
})
write(lesson)

from common import (T, opt, say, wrong, ratio, share, write,
                    REF, REVIEW, TIMES_TABLES, RATIO_MEANING, RATIO_SHARE)

SKILL = RATIO_SHARE

# Nani's Rs 500 for Hamid and Saad, shared 2 : 3 (s1 to s4).
TOTAL = 500
HAMID, SAAD = share(TOTAL, (2, 3))
assert (HAMID, SAAD) == (200, 300) and HAMID + SAAD == TOTAL
ONE_PART = TOTAL // 5
assert ONE_PART == 100

# s5: parts in 3 : 4
assert 3 + 4 == 7 and 3 * 4 == 12

# s6: Rs 700 shared 3 : 4
SMALL_6, BIG_6 = share(700, (3, 4))
assert (SMALL_6, BIG_6) == (300, 400)

# s7: 36 marbles shared 1 : 2
AMNA_7, BILAL_7 = share(36, (1, 2))
assert (AMNA_7, BILAL_7) == (12, 24)

# s8: Umar shares 30 toffees 2 : 3 and divides by 2 instead of 5.
RIGHT_8 = share(30, (2, 3))
assert RIGHT_8 == [12, 18]
assert (30 // 2) * 2 == 30 and (30 // 2) * 3 == 45  # his answer: 30 and 45, total 75

# s9: 36 children, girls to boys 4 : 5
GIRLS_9, BOYS_9 = share(36, (4, 5))
assert (GIRLS_9, BOYS_9) == (16, 20)

# s11: 2 : 3, Hamid's 2 parts are Rs 80, so one part is 40 and Saad gets 120.
assert 80 // 2 == 40 and 40 * 3 == 120

# Question bank and review.
assert share(60, (1, 3)) == [15, 45]
assert share(45, (4, 5)) == [20, 25]
assert share(900, (2, 7)) == [200, 700]

lesson = {
 "id": "g6-maths-06-sharing-in-a-ratio",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Divide a quantity into two parts in a given ratio.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Sharing in a ratio", "نسبت میں تقسیم"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": RATIO_MEANING}, {"skill": TIMES_TABLES}],
 "misconceptions": [
   {"id": "share_equally", "description": "Shares the amount equally (half each) whatever the ratio."},
   {"id": "ratio_as_amounts", "description": "Gives the ratio numbers themselves as the shares (Rs 2 and Rs 3 out of Rs 500)."},
   {"id": "divide_by_people", "description": "Divides by the number of people, or by one term, instead of by the total number of parts."},
   {"id": "multiply_parts", "description": "Multiplies the terms of the ratio (3 × 4 = 12) instead of adding them to find the number of parts."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_first_step", "type": "recall", "step": {
     "id": "qb_first_step", "type": "choice",
     "prompt": T("You want to share Rs 60 in the ratio 1 : 3. What do you do first?", "آپ 60 روپے کو 1 : 3 کی نسبت میں تقسیم کرنا چاہتے ہیں۔ پہلے کیا کریں گے؟"),
     "options": [
       opt("a", "Add the parts: 1 + 3 = 4 parts.", "حصے جمع کریں: 1 + 3 = 4 حصے۔", True,
           "Yes! Then one part is 60 ÷ 4 = 15, so the shares are Rs 15 and Rs 45.", "جی ہاں! پھر ایک حصہ 60 ÷ 4 = 15، اس لیے حصے 15 روپے اور 45 روپے ہیں۔"),
       opt("b", "Halve it: Rs 30 each.", "آدھا کریں: ہر ایک کو 30 روپے۔", False,
           "Halving is for 1 : 1. Here one person gets 3 parts for every 1 part.", "آدھا کرنا 1 : 1 کے لیے ہے۔ یہاں ایک کو ہر 1 حصے کے مقابلے میں 3 حصے ملتے ہیں۔", "share_equally"),
       opt("c", "Multiply the parts: 1 × 3 = 3.", "حصوں کو ضرب دیں: 1 × 3 = 3۔", False,
           "Add the parts, don't multiply them: 1 + 3 = 4 parts.", "حصے جمع کریں، ضرب نہ دیں: 1 + 3 = 4 حصے۔", "multiply_parts"),
     ]}},
   {"id": "qb_share", "type": "apply", "step": {
     "id": "qb_share", "type": "number",
     "prompt": T("Share 45 apples between Asad and Hina in the ratio 4 : 5. How many apples does Hina get?", "45 سیب اسد اور حنا میں 4 : 5 کی نسبت سے تقسیم کریں۔ حنا کو کتنے سیب ملیں گے؟"),
     "answer": 25, "checker": "numeric",
     "hint": T("4 + 5 = 9 parts. How many apples is one part?", "4 + 5 = 9 حصے۔ ایک حصہ کتنے سیب ہے؟"),
     "feedback_correct": T("Right! One part is 45 ÷ 9 = 5, so Hina gets 5 × 5 = 25.", "درست! ایک حصہ 45 ÷ 9 = 5، اس لیے حنا کو 5 × 5 = 25 ملیں گے۔"),
     "feedback_wrong": T("9 parts: one part is 45 ÷ 9 = 5. Hina has 5 parts: 5 × 5 = 25.", "9 حصے: ایک حصہ 45 ÷ 9 = 5۔ حنا کے 5 حصے ہیں: 5 × 5 = 25"),
     "common_wrong": [wrong(20, "20 is Asad's share (4 parts). Hina has 5 parts.", "20 اسد کا حصہ ہے (4 حصے)۔ حنا کے 5 حصے ہیں۔"),
                      wrong(5, "5 is one part. Hina gets 5 parts.", "5 ایک حصہ ہے۔ حنا کو 5 حصے ملتے ہیں۔")]}},
   {"id": "qb_find_error_equal", "type": "find_error", "step": {
     "id": "qb_find_error_equal", "type": "choice",
     "prompt": T("Nida shares Rs 900 between two sisters in the ratio 2 : 7 and gives Rs 450 to each. Is she right?", "ندا 900 روپے دو بہنوں میں 2 : 7 کی نسبت سے تقسیم کرتی ہے اور ہر ایک کو 450 روپے دیتی ہے۔ کیا وہ درست ہے؟"),
     "options": [
       opt("no", "No. 9 parts of Rs 100: the sisters get Rs 200 and Rs 700.", "نہیں۔ 100 روپے کے 9 حصے: بہنوں کو 200 روپے اور 700 روپے ملیں گے۔", True,
           "Right! 2 + 7 = 9 parts, 900 ÷ 9 = 100, so Rs 200 and Rs 700.", "درست! 2 + 7 = 9 حصے، 900 ÷ 9 = 100، اس لیے 200 روپے اور 700 روپے۔"),
       opt("yes", "Yes. Sharing means everyone gets the same.", "ہاں۔ تقسیم کا مطلب ہے سب کو برابر ملے۔", False,
           "Equal shares would be 1 : 1. In 2 : 7 the second sister gets much more.", "برابر حصے 1 : 1 ہوتے۔ 2 : 7 میں دوسری بہن کو بہت زیادہ ملتا ہے۔", "share_equally"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_three_steps", "front": T("How do you share an amount in a ratio?", "کسی مقدار کو نسبت میں کیسے تقسیم کرتے ہیں؟"),
    "back": T("1. Add the parts. 2. Divide the amount by the parts to find one part. 3. Multiply one part by each number. Rs 500 in 2 : 3: 5 parts, one part Rs 100, shares Rs 200 and Rs 300.",
              "1۔ حصے جمع کریں۔ 2۔ مقدار کو حصوں سے تقسیم کر کے ایک حصہ معلوم کریں۔ 3۔ ایک حصے کو ہر عدد سے ضرب دیں۔ 500 روپے 2 : 3 میں: 5 حصے، ایک حصہ 100 روپے، حصے 200 روپے اور 300 روپے۔")},
   {"id": "f_check", "front": T("How can you check your shares?", "اپنے حصوں کو کیسے جانچیں؟"),
    "back": T("Add them: they must make the whole amount. 200 + 300 = 500.", "انہیں جمع کریں: یہ پوری مقدار کے برابر ہونے چاہییں۔ 200 + 300 = 500")},
 ],
 "home_tasks": [{"id": "h_share_beans", "text": T(
   "Take 20 beans or buttons. Share them between two cups in the ratio 1 : 3: put 1 in the first cup and 3 in the second, again and again until none are left. How many are in each cup?",
   "20 دانے یا بٹن لیں۔ انہیں دو پیالوں میں 1 : 3 کی نسبت سے تقسیم کریں: پہلے پیالے میں 1 اور دوسرے میں 3 ڈالیں، بار بار، جب تک کچھ نہ بچے۔ ہر پیالے میں کتنے ہیں؟")}],
 "glossary": [T("Ratio", "نسبت"), T("Share", "حصہ"), T("Part", "حصہ"), T("Total", "کل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious",
      "Nani gave Hamid and Saad Rs 500 for helping. Hamid helped 2 hours, Saad 3 hours. How should they share it fairly?",
      "نانی نے مدد پر حامد اور سعد کو 500 روپے دیے۔ حامد نے 2 گھنٹے، سعد نے 3 گھنٹے مدد کی۔ وہ انصاف سے کیسے بانٹیں؟"),
    "text": T("Saad worked more, so he should get more. They share it in the ratio 2 : 3. First, a quick check.",
              "سعد نے زیادہ کام کیا، اس لیے اسے زیادہ ملنا چاہیے۔ وہ اسے 2 : 3 کی نسبت میں بانٹتے ہیں۔ پہلے ایک چھوٹا سا سوال۔")},
   {"id": "s2_foundation", "type": "number", "question_type": "recall", "skill": TIMES_TABLES,
    "prompt": T("What is 500 ÷ 5?", "500 ÷ 5 کتنا ہے؟"),
    "answer": ONE_PART, "checker": "numeric",
    "hint": T("How many 5s make 50? Then think of 500.", "کتنے 5 مل کر 50 بنتے ہیں؟ پھر 500 کے بارے میں سوچیں۔"),
    "feedback_correct": T("Yes! 500 ÷ 5 = 100. We'll need this soon.", "جی ہاں! 500 ÷ 5 = 100۔ یہ ہمیں جلد کام آئے گا۔"),
    "feedback_wrong": T("5 × 100 = 500, so 500 ÷ 5 = 100.", "5 × 100 = 500، اس لیے 500 ÷ 5 = 100"),
    "common_wrong": [wrong(10, "5 × 10 = 50, not 500. Try 5 × 100.", "5 × 10 = 50 ہے، 500 نہیں۔ 5 × 100 آزمائیں۔")]},
   {"id": "s3_predict", "type": "choice",
    "prompt": T("Guess first: how should Hamid and Saad share Rs 500 in the ratio 2 : 3?",
                "پہلے اندازہ لگائیں: حامد اور سعد 500 روپے 2 : 3 کی نسبت میں کیسے بانٹیں؟"),
    "options": [
      opt("half", "Rs 250 each", "ہر ایک کو 250 روپے", False,
          "That is fair only if they worked the same time. Saad worked more.", "یہ تب انصاف ہوتا جب دونوں برابر کام کرتے۔ سعد نے زیادہ کام کیا۔", "share_equally"),
      opt("ratio_numbers", "Rs 2 and Rs 3", "2 روپے اور 3 روپے", False,
          "That only gives away Rs 5! All Rs 500 must be shared.", "اس طرح تو صرف 5 روپے بٹے! پورے 500 روپے بانٹنے ہیں۔", "ratio_as_amounts"),
      opt("right", "Rs 200 and Rs 300", "200 روپے اور 300 روپے", True,
          "Good thinking! Let's see how to work it out.", "بہت خوب سوچا! آئیں دیکھیں اسے کیسے نکالتے ہیں۔"),
    ]},
   {"id": "s4_method", "type": "explain",
    "character": say("happy", "Think of the money cut into equal parts!", "سوچیں کہ پیسے برابر حصوں میں کٹے ہوئے ہیں!"),
    "text": T(f"2 : 3 means Hamid gets 2 parts and Saad gets 3 parts, all the same size. 1. Add the parts: 2 + 3 = 5 parts. 2. Find one part: Rs {TOTAL} ÷ 5 = Rs {ONE_PART}. 3. Multiply: Hamid 2 × {ONE_PART} = Rs {HAMID}, Saad 3 × {ONE_PART} = Rs {SAAD}. Check: {HAMID} + {SAAD} = {TOTAL}.",
              f"2 : 3 کا مطلب ہے حامد کو 2 حصے اور سعد کو 3 حصے، سب ایک جتنے۔ 1۔ حصے جمع کریں: 2 + 3 = 5 حصے۔ 2۔ ایک حصہ معلوم کریں: {TOTAL} روپے ÷ 5 = {ONE_PART} روپے۔ 3۔ ضرب دیں: حامد 2 × {ONE_PART} = {HAMID} روپے، سعد 3 × {ONE_PART} = {SAAD} روپے۔ جانچیں: {HAMID} + {SAAD} = {TOTAL}")},
   {"id": "s5_parts", "type": "number", "question_type": "recall",
    "prompt": T("An amount is shared in the ratio 3 : 4. How many equal parts is it cut into?", "ایک مقدار 3 : 4 کی نسبت میں تقسیم کی جاتی ہے۔ اسے کتنے برابر حصوں میں کاٹا جاتا ہے؟"),
    "answer": 7, "checker": "numeric",
    "hint": T("One person gets 3 parts and the other gets 4.", "ایک کو 3 حصے ملتے ہیں اور دوسرے کو 4۔"),
    "feedback_correct": T("Right! 3 + 4 = 7 parts.", "درست! 3 + 4 = 7 حصے۔"),
    "feedback_wrong": T("Add the parts: 3 + 4 = 7.", "حصے جمع کریں: 3 + 4 = 7"),
    "common_wrong": [wrong(12, "Add the parts, don't multiply: 3 + 4 = 7.", "حصے جمع کریں، ضرب نہ دیں: 3 + 4 = 7", "multiply_parts"),
                     wrong(2, "There are 2 people, but 3 + 4 = 7 parts.", "لوگ 2 ہیں، لیکن حصے 3 + 4 = 7 ہیں۔", "divide_by_people")]},
   {"id": "s6_share", "type": "number", "question_type": "apply",
    "prompt": T("Abbu shares Rs 700 between Fatima and Zainab in the ratio 3 : 4. How much does Zainab get?", "ابو 700 روپے فاطمہ اور زینب میں 3 : 4 کی نسبت سے تقسیم کرتے ہیں۔ زینب کو کتنے ملیں گے؟"),
    "answer": BIG_6, "checker": "numeric",
    "hint": T("7 parts. One part is 700 ÷ 7. Zainab has 4 parts.", "7 حصے۔ ایک حصہ 700 ÷ 7۔ زینب کے 4 حصے ہیں۔"),
    "feedback_correct": T(f"Right! One part is Rs 100, so Zainab gets 4 × 100 = Rs {BIG_6} and Fatima Rs {SMALL_6}.", f"درست! ایک حصہ 100 روپے، اس لیے زینب کو 4 × 100 = {BIG_6} روپے اور فاطمہ کو {SMALL_6} روپے۔"),
    "feedback_wrong": T(f"3 + 4 = 7 parts, 700 ÷ 7 = 100. Zainab has 4 parts: 4 × 100 = Rs {BIG_6}.", f"3 + 4 = 7 حصے، 700 ÷ 7 = 100۔ زینب کے 4 حصے ہیں: 4 × 100 = {BIG_6} روپے۔"),
    "common_wrong": [
      wrong(350, "That is half. Zainab has 4 of the 7 parts, more than half.", "یہ آدھا ہے۔ زینب کے 7 میں سے 4 حصے ہیں، آدھے سے زیادہ۔", "share_equally"),
      wrong(SMALL_6, f"Rs {SMALL_6} is Fatima's share (3 parts). Zainab has 4 parts.", f"{SMALL_6} روپے فاطمہ کا حصہ ہے (3 حصے)۔ زینب کے 4 حصے ہیں۔"),
      wrong(4, "4 is how many parts Zainab gets. How much money is that?", "4 تو زینب کے حصوں کی تعداد ہے۔ یہ کتنے پیسے بنتے ہیں؟", "ratio_as_amounts"),
    ]},
   {"id": "s7_marbles", "type": "number", "question_type": "apply",
    "prompt": T("Amna and Bilal share 36 marbles in the ratio 1 : 2. How many marbles does Bilal get?", "آمنہ اور بلال 36 کنچے 1 : 2 کی نسبت سے بانٹتے ہیں۔ بلال کو کتنے کنچے ملیں گے؟"),
    "answer": BILAL_7, "checker": "numeric",
    "hint": T("1 + 2 = 3 parts. One part is 36 ÷ 3.", "1 + 2 = 3 حصے۔ ایک حصہ 36 ÷ 3۔"),
    "feedback_correct": T(f"Right! One part is 12, so Bilal gets 2 × 12 = {BILAL_7}.", f"درست! ایک حصہ 12، اس لیے بلال کو 2 × 12 = {BILAL_7} ملیں گے۔"),
    "feedback_wrong": T(f"3 parts: 36 ÷ 3 = 12. Bilal has 2 parts: 2 × 12 = {BILAL_7}.", f"3 حصے: 36 ÷ 3 = 12۔ بلال کے 2 حصے ہیں: 2 × 12 = {BILAL_7}"),
    "common_wrong": [
      wrong(18, "That is half each. Bilal gets 2 parts for Amna's 1.", "یہ ہر ایک کو آدھا ہے۔ بلال کو آمنہ کے 1 حصے کے مقابلے میں 2 حصے ملتے ہیں۔", "share_equally"),
      wrong(AMNA_7, f"{AMNA_7} is Amna's share (1 part). Bilal has 2 parts.", f"{AMNA_7} آمنہ کا حصہ ہے (1 حصہ)۔ بلال کے 2 حصے ہیں۔"),
    ]},
   {"id": "s8_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Umar shares 30 toffees in the ratio 2 : 3. He says: \"30 ÷ 2 = 15 for one part, so 2 × 15 = 30 and 3 × 15 = 45.\" What went wrong?",
                "عمر 30 ٹافیاں 2 : 3 کی نسبت سے بانٹتا ہے۔ وہ کہتا ہے: \"ایک حصہ 30 ÷ 2 = 15، اس لیے 2 × 15 = 30 اور 3 × 15 = 45۔\" کیا غلطی ہوئی؟"),
    "options": [
      opt("parts", "He divided by 2 instead of by all 5 parts. One part is 30 ÷ 5 = 6, so 12 and 18.", "اس نے تمام 5 حصوں کے بجائے 2 سے تقسیم کیا۔ ایک حصہ 30 ÷ 5 = 6، اس لیے 12 اور 18۔", True,
          "Yes! His shares make 75 toffees, but there are only 30. 12 + 18 = 30.", "جی ہاں! اس کے حصے 75 ٹافیاں بنتے ہیں، لیکن ٹافیاں صرف 30 ہیں۔ 12 + 18 = 30"),
      opt("nothing", "Nothing. The second share is bigger, as it should be.", "کوئی غلطی نہیں۔ دوسرے کو زیادہ ملا، جیسا ہونا چاہیے۔", False,
          "Check: 30 + 45 = 75, but there are only 30 toffees. Divide by all the parts.", "جانچیں: 30 + 45 = 75، لیکن ٹافیاں صرف 30 ہیں۔ تمام حصوں سے تقسیم کریں۔", "divide_by_people"),
      opt("half", "He should give 15 to each.", "اسے ہر ایک کو 15 دینی چاہییں۔", False,
          "15 each is 1 : 1. The ratio is 2 : 3, so the second share is bigger.", "ہر ایک کو 15 دینا 1 : 1 ہے۔ نسبت 2 : 3 ہے، اس لیے دوسرا حصہ بڑا ہے۔", "share_equally"),
    ]},
   {"id": "s9_class", "type": "number", "question_type": "apply",
    "prompt": T("A class of 36 children has girls and boys in the ratio 4 : 5. How many girls are there?", "36 بچوں کی ایک جماعت میں لڑکیوں اور لڑکوں کی نسبت 4 : 5 ہے۔ لڑکیاں کتنی ہیں؟"),
    "answer": GIRLS_9, "checker": "numeric",
    "hint": T("4 + 5 = 9 parts. How many children is one part?", "4 + 5 = 9 حصے۔ ایک حصہ کتنے بچے ہیں؟"),
    "feedback_correct": T(f"Right! One part is 36 ÷ 9 = 4, so {GIRLS_9} girls and {BOYS_9} boys.", f"درست! ایک حصہ 36 ÷ 9 = 4، اس لیے {GIRLS_9} لڑکیاں اور {BOYS_9} لڑکے۔"),
    "feedback_wrong": T(f"9 parts: 36 ÷ 9 = 4 children each. Girls have 4 parts: 4 × 4 = {GIRLS_9}.", f"9 حصے: 36 ÷ 9 = 4 بچے فی حصہ۔ لڑکیوں کے 4 حصے ہیں: 4 × 4 = {GIRLS_9}"),
    "common_wrong": [
      wrong(BOYS_9, f"{BOYS_9} is the boys (5 parts). Girls are named first: 4 parts.", f"{BOYS_9} لڑکے ہیں (5 حصے)۔ لڑکیاں پہلے آئی ہیں: 4 حصے۔"),
      wrong(4, "4 is the number of parts for girls. How many children is that?", "4 تو لڑکیوں کے حصوں کی تعداد ہے۔ یہ کتنے بچے بنتے ہیں؟", "ratio_as_amounts"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Can you teach me? Why do we add 2 + 3 before we divide the money?",
                     "کیا آپ مجھے سمجھا سکتے ہیں؟ پیسے تقسیم کرنے سے پہلے ہم 2 + 3 کیوں جمع کرتے ہیں؟"),
    "task": T("In your own words: when sharing Rs 500 in the ratio 2 : 3, why do we divide by 5?",
              "اپنے الفاظ میں بتائیں: 500 روپے کو 2 : 3 کی نسبت میں بانٹتے وقت ہم 5 سے کیوں تقسیم کرتے ہیں؟"),
    "key_idea": "Hamid gets 2 equal parts and Saad gets 3, so the money is cut into 2 + 3 = 5 equal parts. Dividing by 5 gives the size of one part (Rs 100); then Hamid gets 2 of them and Saad 3.",
    "levels": {
      "got_it": "Says the money is cut into 5 equal parts because 2 + 3 = 5 (2 for one, 3 for the other), and dividing by 5 gives one part.",
      "partly": "Says 2 + 3 = 5 or mentions parts, but does not explain that 5 is the total number of equal parts.",
      "not_yet": "Says because there are 2 people, gives no reason, or the reasoning is wrong."},
    "keywords": [
      ["part", "piece", "حص", "ٹکڑ", "hiss", "tukr", "tukd"],
      ["5", "five", "پانچ", "۵", "paanch", "panch"],
      ["equal", "same", "add", "total", "برابر", "جمع", "کل", "barabar", "jama", "kul"]],
    "fallback_feedback": {
      "got_it": T("Well explained! 2 parts plus 3 parts make 5 equal parts, so one part is Rs 500 ÷ 5 = Rs 100.",
                  "بہت خوب سمجھایا! 2 حصے اور 3 حصے مل کر 5 برابر حصے بنتے ہیں، اس لیے ایک حصہ 500 ÷ 5 = 100 روپے۔"),
      "partly": T("Good start! Now say what the 5 parts are, and who gets how many.",
                  "اچھی شروعات! اب بتائیں کہ 5 حصے کیا ہیں، اور کس کو کتنے ملتے ہیں۔"),
      "not_yet": T("Think: Hamid gets 2 equal parts and Saad gets 3. How many equal parts is the Rs 500 cut into?",
                   "سوچیں: حامد کو 2 برابر حصے ملتے ہیں اور سعد کو 3۔ 500 روپے کتنے برابر حصوں میں کٹتے ہیں؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_one_share_known", "type": "number", "question_type": "apply",
    "prompt": T("Hamid and Saad share some money in the ratio 2 : 3. Hamid gets Rs 80. How much does Saad get?", "حامد اور سعد کچھ پیسے 2 : 3 کی نسبت سے بانٹتے ہیں۔ حامد کو 80 روپے ملتے ہیں۔ سعد کو کتنے ملیں گے؟"),
    "answer": 120, "checker": "numeric",
    "hint": T("Hamid's Rs 80 is 2 parts. How much is one part?", "حامد کے 80 روپے 2 حصے ہیں۔ ایک حصہ کتنا ہے؟"),
    "feedback_correct": T("Right! One part is 80 ÷ 2 = 40, so Saad gets 3 × 40 = Rs 120.", "درست! ایک حصہ 80 ÷ 2 = 40، اس لیے سعد کو 3 × 40 = 120 روپے ملیں گے۔"),
    "feedback_wrong": T("2 parts are Rs 80, so one part is Rs 40. Saad has 3 parts: 3 × 40 = Rs 120.", "2 حصے 80 روپے ہیں، اس لیے ایک حصہ 40 روپے۔ سعد کے 3 حصے ہیں: 3 × 40 = 120 روپے۔"),
    "common_wrong": [
      wrong(40, "Rs 40 is one part. Saad gets 3 parts.", "40 روپے ایک حصہ ہے۔ سعد کو 3 حصے ملتے ہیں۔"),
      wrong(200, "Rs 200 is all the money (5 parts). Saad gets 3 parts.", "200 روپے کل پیسے ہیں (5 حصے)۔ سعد کو 3 حصے ملتے ہیں۔"),
      wrong(81, "Adding 1 doesn't keep the ratio. Find one part first: 80 ÷ 2.", "1 جمع کرنے سے نسبت برقرار نہیں رہتی۔ پہلے ایک حصہ معلوم کریں: 80 ÷ 2۔"),
    ]},
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can share anything fairly in a ratio!", "اب آپ کوئی بھی چیز نسبت میں انصاف سے بانٹ سکتے ہیں!"),
    "text": T("To share an amount in a ratio: add the parts, divide the amount by the number of parts to find one part, then multiply one part by each number of the ratio. Check that the shares add up to the whole amount.",
              "کسی مقدار کو نسبت میں بانٹنے کے لیے: حصے جمع کریں، مقدار کو حصوں کی تعداد سے تقسیم کر کے ایک حصہ معلوم کریں، پھر ایک حصے کو نسبت کے ہر عدد سے ضرب دیں۔ جانچیں کہ حصے مل کر پوری مقدار بنتے ہیں۔"),
    "points": [T("Rs 500 in 2 : 3 → 5 parts → Rs 100 each → Rs 200 and Rs 300", "500 روپے 2 : 3 میں ← 5 حصے ← ہر حصہ 100 روپے ← 200 روپے اور 300 روپے"),
               T("Add the parts; don't divide by the number of people.", "حصے جمع کریں؛ لوگوں کی تعداد سے تقسیم نہ کریں۔")]},
 ],
 "review_questions": [
   {"id": "r_share", "type": "apply", "skill": SKILL, "step": {
     "id": "r_share", "type": "number",
     "prompt": T("Share Rs 60 between Ahmed and Kiran in the ratio 1 : 3. How much does Kiran get?", "60 روپے احمد اور کرن میں 1 : 3 کی نسبت سے تقسیم کریں۔ کرن کو کتنے ملیں گے؟"),
     "answer": 45, "checker": "numeric",
     "hint": T("1 + 3 = 4 parts.", "1 + 3 = 4 حصے۔"),
     "feedback_correct": T("Right! One part is 60 ÷ 4 = 15, so Kiran gets 3 × 15 = 45.", "درست! ایک حصہ 60 ÷ 4 = 15، اس لیے کرن کو 3 × 15 = 45 ملیں گے۔"),
     "feedback_wrong": T("4 parts: 60 ÷ 4 = 15. Kiran has 3 parts: 3 × 15 = Rs 45.", "4 حصے: 60 ÷ 4 = 15۔ کرن کے 3 حصے ہیں: 3 × 15 = 45 روپے۔"),
     "common_wrong": [wrong(30, "That is half each. Kiran gets 3 parts for Ahmed's 1.", "یہ ہر ایک کو آدھا ہے۔ کرن کو احمد کے 1 حصے کے مقابلے میں 3 حصے ملتے ہیں۔", "share_equally"),
                      wrong(15, "Rs 15 is Ahmed's share (1 part). Kiran has 3 parts.", "15 روپے احمد کا حصہ ہے (1 حصہ)۔ کرن کے 3 حصے ہیں۔")]}},
   {"id": "r_find_error", "type": "find_error", "skill": SKILL, "step": {
     "id": "r_find_error", "type": "choice",
     "prompt": T("To share Rs 900 in the ratio 2 : 7, Saba gives Rs 2 and Rs 7. What went wrong?", "900 روپے 2 : 7 کی نسبت میں بانٹنے کے لیے صبا 2 روپے اور 7 روپے دیتی ہے۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("amounts", "2 and 7 are parts, not rupees. One part is 900 ÷ 9 = Rs 100, so Rs 200 and Rs 700.", "2 اور 7 حصے ہیں، روپے نہیں۔ ایک حصہ 900 ÷ 9 = 100 روپے، اس لیے 200 روپے اور 700 روپے۔", True,
           "Yes! The shares must add up to Rs 900.", "جی ہاں! حصے مل کر 900 روپے بننے چاہییں۔"),
       opt("nothing", "Nothing. That is the ratio 2 : 7.", "کوئی غلطی نہیں۔ یہی 2 : 7 کی نسبت ہے۔", False,
           "The ratio is right, but only Rs 9 was shared. All Rs 900 must be shared.", "نسبت ٹھیک ہے، لیکن صرف 9 روپے بٹے۔ پورے 900 روپے بانٹنے ہیں۔", "ratio_as_amounts"),
     ]}},
 ],
 "teacher_notes": [
   "Written fresh for the Ratio and Proportion unit. No textbook text or exercises were used.",
   "Unit number to be confirmed against the PCTB Grade 6 book: the files are named g6-maths-06. Fix the names and curriculum_refs if the unit differs.",
   "Urdu terms to check against the Punjab textbook: نسبت میں تقسیم (sharing in a ratio), حصہ (part / share), کل (total).",
   "The method is taught as three steps (add the parts, find one part, multiply), with a check that the shares add up to the total. Every amount divides exactly, so no step needs decimals.",
   "Steps: foundation division (s2), prediction (s3), the method (s4), counting parts (s5), sharing (s6, s7), find the error (s8), new context (s9), explain (s10), working back from one share (s11).",
   "The numbers were worked out in content/sources/g6-maths-06/sharing_in_a_ratio.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

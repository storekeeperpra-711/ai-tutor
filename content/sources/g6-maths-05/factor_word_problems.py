from math import gcd, lcm

from common import (T, opt, say, wrong, number_question, write, factors, is_prime, prime_factors,
                    REF, REVIEW, FM_FACTORS, FM_PRIMES, FM_HCF, FM_LCM, FM_WORD_PROBLEMS)

SKILL = FM_WORD_PROBLEMS

# s2: HCF or LCM?
assert lcm(3, 5) == 15
# s4: rows of 24 boys and 32 girls, each row one kind, all rows the same length
S4 = gcd(24, 32)
assert S4 == 8 and lcm(24, 32) == 96
# s5: two bells every 15 and 20 minutes, together at 8:00
S5 = lcm(15, 20)
assert S5 == 60 and gcd(15, 20) == 5
# s6: tiles: largest square tile for a 36 by 48 floor
S6 = gcd(36, 48)
assert S6 == 12 and lcm(36, 48) == 144
# s7: rotis in packs of 6, kebabs in packs of 8, same number of each
S7 = lcm(6, 8)
assert S7 == 24 and S7 // 6 == 4 and S7 // 8 == 3 and 6 * 8 == 48
# s8: how many packs of rotis
S8 = S7 // 6
assert S8 == 4
# s11: ribbons 30 and 45 cut into equal longest pieces; how many pieces in all
L11 = gcd(30, 45)
S11 = 30 // L11 + 45 // L11
assert L11 == 15 and S11 == 5
# unit test
assert factors(28) == [1, 2, 4, 7, 14, 28]
U1 = len(factors(28))
assert U1 == 6
assert [n for n in (21, 23, 25, 27) if is_prime(n)] == [23]
U3 = gcd(18, 30)
assert U3 == 6 and lcm(18, 30) == 90
U4 = lcm(6, 10)
assert U4 == 30 and 6 * 10 == 60 and gcd(6, 10) == 2
U5 = lcm(4, 10)
assert U5 == 20
# question bank and review
QB = gcd(16, 24)
assert QB == 8 and lcm(16, 24) == 48
R1 = lcm(12, 16)
assert R1 == 48 and gcd(12, 16) == 4
R2 = gcd(40, 56)
assert R2 == 8 and lcm(40, 56) == 280


lesson = {
 "id": "g6-maths-05-factor-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve real-life problems using HCF and LCM, and decide which one a problem needs.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("HCF and LCM word problems", "عاد اعظم اور ذو اضعاف اقل کے سوالات"),
 "estimated_minutes": 16,
 "prerequisites": [{"skill": FM_HCF}, {"skill": FM_LCM}, {"skill": FM_FACTORS}, {"skill": FM_PRIMES}],
 "misconceptions": [
   {"id": "wrong_tool", "description": "Uses the LCM when the problem asks to split into the largest equal groups (HCF), or the HCF when it asks when things happen together again (LCM)."},
   {"id": "stops_early", "description": "Finds the HCF or LCM but does not answer the actual question (number of pieces, number of packs, the time)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_which", "type": "recall", "step": {
     "id": "qb_which", "type": "choice",
     "prompt": T("Two lights blink every 6 and every 9 seconds. To find when they blink together again, which do you need?", "دو بتیاں ہر 6 اور ہر 9 سیکنڈ بعد جلتی ہیں۔ یہ جاننے کے لیے کہ دوبارہ کب ساتھ جلیں گی، کیا چاہیے؟"),
     "options": [
       opt("lcm", "The LCM", "ذو اضعاف اقل", True, "Yes! Together again means a common multiple: LCM = 18 seconds.", "جی ہاں! دوبارہ ساتھ کا مطلب مشترک ضعف: ذو اضعاف اقل = 18 سیکنڈ۔"),
       opt("hcf", "The HCF", "عاد اعظم", False, "The HCF splits things into groups. Together again needs the LCM: 18 seconds.", "عاد اعظم چیزوں کو گروہوں میں بانٹتا ہے۔ دوبارہ ساتھ کے لیے ذو اضعاف اقل: 18 سیکنڈ۔", "wrong_tool"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("16 apples and 24 oranges are shared into identical baskets with nothing left. What is the largest number of baskets?", "16 سیب اور 24 مالٹے ایک جیسی ٹوکریوں میں اس طرح بانٹے گئے کہ کچھ نہ بچے۔ زیادہ سے زیادہ کتنی ٹوکریاں؟"),
     QB,
     T("The number of baskets divides 16 and 24. Find the HCF.", "ٹوکریوں کی تعداد 16 اور 24 دونوں کو تقسیم کرے۔ عاد اعظم معلوم کریں۔"),
     T("Right! 8 baskets, each with 2 apples and 3 oranges.", "درست! 8 ٹوکریاں، ہر ایک میں 2 سیب اور 3 مالٹے۔"),
     T("HCF of 16 and 24 = 8.", "16 اور 24 کا عاد اعظم = 8"),
     common_wrong=[wrong(48, "48 is the LCM. Sharing into groups needs the HCF: 8.", "48 ذو اضعاف اقل ہے۔ گروہوں میں بانٹنے کے لیے عاد اعظم: 8", "wrong_tool"),
                   wrong(4, "4 baskets work, but 8 is the largest.", "4 ٹوکریاں بن سکتی ہیں، مگر سب سے زیادہ 8 ہیں۔")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Two buses leave every 15 and 20 minutes, together at 8:00. Zain says they meet again after 5 minutes. What went wrong?", "دو بسیں ہر 15 اور 20 منٹ بعد چلتی ہیں، 8 بجے ساتھ چلیں۔ زین کہتا ہے 5 منٹ بعد پھر ساتھ ہوں گی۔ کیا غلطی ہوئی؟"),
     "options": [
       opt("tool", "He found the HCF. Together again needs the LCM: 60 minutes.", "اس نے عاد اعظم نکالا۔ دوبارہ ساتھ کے لیے ذو اضعاف اقل: 60 منٹ۔", True,
           "Yes! After 5 minutes neither bus has left again. They meet at 9:00.", "جی ہاں! 5 منٹ بعد کوئی بس دوبارہ نہیں چلی۔ وہ 9 بجے ملیں گی۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "After 5 minutes neither bus has left again. LCM of 15 and 20 = 60 minutes.", "5 منٹ بعد کوئی بس دوبارہ نہیں چلی۔ 15 اور 20 کا ذو اضعاف اقل = 60 منٹ۔", "wrong_tool"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_which", "front": T("HCF or LCM?", "عاد اعظم یا ذو اضعاف اقل؟"),
    "back": T("Split into the largest equal groups or pieces: HCF. When do things happen together again, or the smallest amount both fit into: LCM.", "سب سے بڑے برابر گروہ یا ٹکڑے: عاد اعظم۔ چیزیں دوبارہ کب ساتھ ہوں، یا سب سے چھوٹی مقدار جس میں دونوں پورے آئیں: ذو اضعاف اقل۔")},
 ],
 "home_tasks": [{"id": "h_market", "text": T(
   "Find two things at home or in a shop sold in different pack sizes (for example eggs in 6s and 12s, or buns in 4s and 6s). What is the smallest number you could buy of each so you have the same amount?",
   "گھر یا دکان پر دو ایسی چیزیں ڈھونڈیں جو مختلف پیکٹوں میں ملتی ہوں (مثلاً انڈے 6 اور 12 کے، یا بن 4 اور 6 کے)۔ دونوں کی برابر تعداد کے لیے کم از کم کتنی خریدنی ہوں گی؟")}],
 "glossary": [T("Highest common factor (HCF)", "عاد اعظم"), T("Lowest common multiple (LCM)", "ذو اضعاف اقل")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Some problems need the HCF, some the LCM. How do we know which one?",
                     "کچھ سوالوں میں عاد اعظم چاہیے، کچھ میں ذو اضعاف اقل۔ ہمیں کیسے پتا چلے کہ کون سا؟"),
    "text": T("Today we solve real problems and learn to pick the right tool. First, a quick check.", "آج ہم اصل سوال حل کریں گے اور صحیح طریقہ چننا سیکھیں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("Find the LCM of 3 and 5.", "3 اور 5 کا ذو اضعاف اقل معلوم کریں۔"),
     15,
     T("Multiples of 5: 5, 10, 15 ... Which does 3 divide?", "5 کے اضعاف: 5، 10، 15 ... ان میں سے کسے 3 تقسیم کرتا ہے؟"),
     T("Right! LCM = 15.", "درست! ذو اضعاف اقل = 15"),
     T("5, 10, 15: 15 ÷ 3 = 5. LCM = 15.", "5، 10، 15: 15 ÷ 3 = 5۔ ذو اضعاف اقل = 15"),
     common_wrong=[wrong(1, "1 is the HCF. The LCM is a multiple of both: 15.", "1 عاد اعظم ہے۔ ذو اضعاف اقل دونوں کا ضعف ہے: 15")],
     qtype="recall", skill=FM_LCM),
   {"id": "s3_which", "type": "explain",
    "character": say("thinking", "Ask: am I splitting something up, or waiting for things to line up?",
                     "پوچھیں: کیا میں کچھ بانٹ رہا ہوں، یا چیزوں کے ایک ساتھ ہونے کا انتظار کر رہا ہوں؟"),
    "text": T("HCF: split things into the LARGEST equal groups, rows or pieces with nothing left over. The answer is no bigger than the numbers. LCM: when do repeating things happen TOGETHER again, or the SMALLEST amount both fit into. The answer is no smaller than the numbers.",
              "عاد اعظم: چیزوں کو سب سے بڑے برابر گروہوں، قطاروں یا ٹکڑوں میں بانٹنا، کچھ نہ بچے۔ جواب اعداد سے بڑا نہیں ہوتا۔ ذو اضعاف اقل: بار بار ہونے والی چیزیں دوبارہ کب ساتھ ہوں، یا سب سے چھوٹی مقدار جس میں دونوں پورے آئیں۔ جواب اعداد سے چھوٹا نہیں ہوتا۔")},
   number_question(
     "s4_rows",
     T("24 boys and 32 girls stand in rows for assembly. Each row has only boys or only girls, and all rows are the same length. What is the longest a row can be?", "اسمبلی میں 24 لڑکے اور 32 لڑکیاں قطاروں میں کھڑے ہیں۔ ہر قطار میں صرف لڑکے یا صرف لڑکیاں ہیں، اور سب قطاریں برابر لمبی ہیں۔ ایک قطار زیادہ سے زیادہ کتنی لمبی ہو سکتی ہے؟"),
     S4,
     T("The row length must divide 24 and 32. Splitting up: HCF.", "قطار کی لمبائی 24 اور 32 دونوں کو تقسیم کرے۔ بانٹنا: عاد اعظم۔"),
     T("Right! Rows of 8: 3 rows of boys and 4 rows of girls.", "درست! 8 کی قطاریں: لڑکوں کی 3 اور لڑکیوں کی 4 قطاریں۔"),
     T("HCF of 24 and 32 = 8.", "24 اور 32 کا عاد اعظم = 8"),
     common_wrong=[wrong(96, "96 is the LCM, more children than there are! Splitting up needs the HCF: 8.", "96 ذو اضعاف اقل ہے، بچوں سے بھی زیادہ! بانٹنے کے لیے عاد اعظم: 8", "wrong_tool"),
                   wrong(4, "Rows of 4 work, but 8 is longer.", "4 کی قطاریں بن سکتی ہیں، مگر 8 لمبی ہیں۔")]),
   number_question(
     "s5_bells",
     T("At school one bell rings every 15 minutes and another every 20 minutes. They ring together at 8:00. After how many minutes do they ring together again?", "اسکول میں ایک گھنٹی ہر 15 منٹ بعد اور دوسری ہر 20 منٹ بعد بجتی ہے۔ 8 بجے دونوں ساتھ بجیں۔ کتنے منٹ بعد دوبارہ ساتھ بجیں گی؟"),
     S5,
     T("Together again: LCM of 15 and 20.", "دوبارہ ساتھ: 15 اور 20 کا ذو اضعاف اقل۔"),
     T("Right! 60 minutes, so at 9:00.", "درست! 60 منٹ، یعنی 9 بجے۔"),
     T("Multiples of 20: 20, 40, 60. 60 ÷ 15 = 4. LCM = 60 minutes.", "20 کے اضعاف: 20، 40، 60۔ 60 ÷ 15 = 4۔ ذو اضعاف اقل = 60 منٹ"),
     common_wrong=[wrong(5, "5 is the HCF. After 5 minutes neither bell has rung again. LCM: 60.", "5 عاد اعظم ہے۔ 5 منٹ بعد کوئی گھنٹی دوبارہ نہیں بجی۔ ذو اضعاف اقل: 60", "wrong_tool"),
                   wrong(300, "300 = 15 × 20 works, but they meet sooner: 60.", "300 = 15 × 20 درست ضعف ہے، مگر وہ پہلے ملتی ہیں: 60")]),
   number_question(
     "s6_tiles",
     T("A room is 36 dm wide and 48 dm long. What is the side of the largest square tile that covers it exactly?", "ایک کمرہ 36 ڈیسی میٹر چوڑا اور 48 ڈیسی میٹر لمبا ہے۔ سب سے بڑی مربع ٹائل کی لمبائی کیا ہو جو اسے پورا ڈھانپ دے؟"),
     S6,
     T("The tile side must divide 36 and 48. Largest: HCF.", "ٹائل کی لمبائی 36 اور 48 دونوں کو تقسیم کرے۔ سب سے بڑی: عاد اعظم۔"),
     T("Right! 12 dm tiles: 3 across and 4 along.", "درست! 12 ڈیسی میٹر کی ٹائلیں: 3 چوڑائی میں اور 4 لمبائی میں۔"),
     T("36 = 2 × 2 × 3 × 3, 48 = 2 × 2 × 2 × 2 × 3. Shared: 2 × 2 × 3 = 12.", "36 = 2 × 2 × 3 × 3، 48 = 2 × 2 × 2 × 2 × 3۔ مشترک: 2 × 2 × 3 = 12"),
     common_wrong=[wrong(144, "144 is the LCM, bigger than the room! Use the HCF: 12.", "144 ذو اضعاف اقل ہے، کمرے سے بھی بڑا! عاد اعظم لیں: 12", "wrong_tool"),
                   wrong(6, "6 dm tiles fit, but 12 dm is larger.", "6 ڈیسی میٹر کی ٹائلیں آتی ہیں، مگر 12 بڑی ہیں۔")]),
   number_question(
     "s7_packs",
     T("Rotis come in packs of 6 and kebabs in packs of 8. Asma wants the same number of rotis and kebabs. What is the smallest number of each she can buy?", "روٹیاں 6 کے پیکٹ میں اور کباب 8 کے پیکٹ میں آتے ہیں۔ عاصمہ برابر روٹیاں اور کباب چاہتی ہے۔ کم از کم ہر ایک کتنا خریدے؟"),
     S7,
     T("The smallest amount both packs fit into: LCM of 6 and 8.", "سب سے چھوٹی مقدار جس میں دونوں پیکٹ پورے آئیں: 6 اور 8 کا ذو اضعاف اقل۔"),
     T("Right! 24 rotis and 24 kebabs.", "درست! 24 روٹیاں اور 24 کباب۔"),
     T("Multiples of 8: 8, 16, 24. 24 ÷ 6 = 4. LCM = 24.", "8 کے اضعاف: 8، 16، 24۔ 24 ÷ 6 = 4۔ ذو اضعاف اقل = 24"),
     common_wrong=[wrong(2, "2 is the HCF. You can't buy 2 rotis from packs of 6! LCM: 24.", "2 عاد اعظم ہے۔ 6 کے پیکٹ سے 2 روٹیاں نہیں ملتیں! ذو اضعاف اقل: 24", "wrong_tool"),
                   wrong(48, "48 = 6 × 8 works, but 24 is smaller.", "48 = 6 × 8 بھی ٹھیک ہے، مگر 24 چھوٹا ہے۔")]),
   number_question(
     "s8_how_many_packs",
     T("So Asma buys 24 rotis. How many packs of rotis is that?", "تو عاصمہ 24 روٹیاں خریدتی ہے۔ یہ روٹیوں کے کتنے پیکٹ ہوئے؟"),
     S8,
     T("Each pack has 6 rotis.", "ہر پیکٹ میں 6 روٹیاں ہیں۔"),
     T("Right! 4 packs of rotis (and 3 packs of kebabs).", "درست! روٹیوں کے 4 پیکٹ (اور کبابوں کے 3)۔"),
     T("24 ÷ 6 = 4 packs.", "24 ÷ 6 = 4 پیکٹ"),
     common_wrong=[wrong(3, "3 is the kebab packs: 24 ÷ 8. Rotis: 24 ÷ 6 = 4.", "3 کباب کے پیکٹ ہیں: 24 ÷ 8۔ روٹیاں: 24 ÷ 6 = 4"),
                   wrong(24, "24 is the number of rotis. Packs: 24 ÷ 6 = 4.", "24 روٹیوں کی تعداد ہے۔ پیکٹ: 24 ÷ 6 = 4", "stops_early")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("18 pencils and 27 erasers go into identical gift bags, nothing left. Hira says the most bags is 54. What went wrong?", "18 پنسلیں اور 27 ربڑ ایک جیسے تحفے کے تھیلوں میں ڈالے گئے، کچھ نہ بچا۔ حرا کہتی ہے زیادہ سے زیادہ 54 تھیلے ہیں۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("tool", "She found the LCM. Splitting into groups needs the HCF: 9 bags.", "اس نے ذو اضعاف اقل نکالا۔ گروہوں میں بانٹنے کے لیے عاد اعظم: 9 تھیلے۔", True,
          "Yes! 54 bags is more bags than there are pencils. HCF = 9: 2 pencils and 3 erasers each.", "جی ہاں! 54 تھیلے پنسلوں سے بھی زیادہ ہیں۔ عاد اعظم = 9: ہر ایک میں 2 پنسلیں اور 3 ربڑ۔"),
      opt("three", "It should be 3 bags.", "یہ 3 تھیلے ہونے چاہییں۔", False,
          "3 bags work, but 9 is the most: 9 divides 18 and 27.", "3 تھیلے بن سکتے ہیں، مگر زیادہ سے زیادہ 9 ہیں: 9، 18 اور 27 کو تقسیم کرتا ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "54 bags can't work with only 18 pencils. Use the HCF: 9.", "صرف 18 پنسلوں سے 54 تھیلے نہیں بن سکتے۔ عاد اعظم لیں: 9", "wrong_tool"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "How do you decide if a problem needs the HCF or the LCM? Can you teach me?",
                     "آپ کیسے فیصلہ کرتے ہیں کہ کسی سوال میں عاد اعظم چاہیے یا ذو اضعاف اقل؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: how do you know whether a word problem needs the HCF or the LCM? Give an example of each.",
              "اپنے الفاظ میں بتائیں: آپ کیسے جانتے ہیں کہ کسی سوال میں عاد اعظم چاہیے یا ذو اضعاف اقل؟ ہر ایک کی مثال دیں۔"),
    "key_idea": "Splitting things into the largest equal groups or pieces needs the HCF (answer no bigger than the numbers). Things repeating and meeting again, or the smallest amount both fit into, needs the LCM (answer no smaller than the numbers).",
    "levels": {
      "got_it": "Links HCF to splitting into largest equal groups and LCM to things happening together again (or smallest common amount), with an example of each.",
      "partly": "Describes one of the two correctly, or both without examples.",
      "not_yet": "Mixes them up or gives no rule."},
    "keywords": [
      ["split", "share", "group", "بانٹ", "گروہ", "baant"],
      ["together", "again", "repeat", "ساتھ", "دوبارہ", "saath"],
      ["hcf", "lcm", "عاد اعظم", "ذو اضعاف اقل"]],
    "fallback_feedback": {
      "got_it": T("Great rule! Splitting up: HCF. Lining up again: LCM.", "بہت اچھا اصول! بانٹنا: عاد اعظم۔ دوبارہ ساتھ ہونا: ذو اضعاف اقل۔"),
      "partly": T("Good start! Now give the other one: when do you use the HCF, and when the LCM?", "اچھی شروعات! اب دوسرا بتائیں: عاد اعظم کب اور ذو اضعاف اقل کب؟"),
      "not_yet": T("Think of the balloons (split into bunches) and the buses (leave together again). Which used the HCF?",
                   "غباروں (گچھوں میں بانٹنا) اور بسوں (دوبارہ ساتھ چلنا) کا سوچیں۔ کس میں عاد اعظم تھا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Factors and multiples unit. You can do it!",
                     "ٹیسٹ کا وقت! اجزائے ضربی اور اضعاف کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on factors, primes, HCF and LCM. Take your time.",
              "اس چھوٹے ٹیسٹ میں اجزائے ضربی، مفرد اعداد، عاد اعظم اور ذو اضعاف اقل کے سوال ہیں۔ آرام سے کریں۔")},
   number_question(
     "u1_factors",
     T("Test 1: How many factors does 28 have?", "ٹیسٹ 1: 28 کے کتنے اجزائے ضربی ہیں؟"),
     U1,
     T("Find the pairs: 1 × 28, 2 × 14 ...", "جوڑے ڈھونڈیں: 1 × 28، 2 × 14 ..."),
     T("Right! 1, 2, 4, 7, 14, 28.", "درست! 1، 2، 4، 7، 14، 28"),
     T("Pairs 1 × 28, 2 × 14, 4 × 7: six factors.", "جوڑے 1 × 28، 2 × 14، 4 × 7: چھ اجزائے ضربی"),
     common_wrong=[wrong(3, "Each pair has two factors: 6.", "ہر جوڑے میں دو اجزائے ضربی ہیں: 6"),
                   wrong(4, "You missed a pair: 4 × 7. Six factors.", "ایک جوڑا رہ گیا: 4 × 7۔ چھ اجزائے ضربی")],
     qtype="recall", skill=FM_FACTORS),
   {"id": "u2_prime", "type": "choice", "question_type": "recall", "skill": FM_PRIMES,
    "prompt": T("Test 2: Which of these is a prime number?", "ٹیسٹ 2: ان میں سے مفرد عدد کون سا ہے؟"),
    "options": [
      opt("n21", "21", "21", False, "21 = 3 × 7, so it is not prime.", "21 = 3 × 7، اس لیے مفرد نہیں۔"),
      opt("n23", "23", "23", True, "Yes! Only 1 and 23 divide 23.", "جی ہاں! 23 کو صرف 1 اور 23 تقسیم کرتے ہیں۔"),
      opt("n25", "25", "25", False, "25 = 5 × 5, so it is not prime.", "25 = 5 × 5، اس لیے مفرد نہیں۔"),
      opt("n27", "27", "27", False, "27 = 3 × 9, so it is not prime.", "27 = 3 × 9، اس لیے مفرد نہیں۔"),
    ]},
   number_question(
     "u3_hcf",
     T("Test 3: Find the HCF of 18 and 30.", "ٹیسٹ 3: 18 اور 30 کا عاد اعظم معلوم کریں۔"),
     U3,
     T("18 = 2 × 3 × 3, 30 = 2 × 3 × 5.", "18 = 2 × 3 × 3، 30 = 2 × 3 × 5"),
     T("Right! HCF = 2 × 3 = 6.", "درست! عاد اعظم = 2 × 3 = 6"),
     T("Shared primes: 2 and 3. HCF = 6.", "مشترک مفرد اعداد: 2 اور 3۔ عاد اعظم = 6"),
     common_wrong=[wrong(90, "90 is the LCM. The HCF divides both: 6.", "90 ذو اضعاف اقل ہے۔ عاد اعظم دونوں کو تقسیم کرتا ہے: 6"),
                   wrong(3, "3 divides both, but 6 is higher.", "3 دونوں کو تقسیم کرتا ہے، مگر 6 بڑا ہے۔")],
     qtype="apply", skill=FM_HCF),
   number_question(
     "u4_lcm",
     T("Test 4: Find the LCM of 6 and 10.", "ٹیسٹ 4: 6 اور 10 کا ذو اضعاف اقل معلوم کریں۔"),
     U4,
     T("Multiples of 10: 10, 20, 30 ... Which does 6 divide?", "10 کے اضعاف: 10، 20، 30 ... ان میں سے کسے 6 تقسیم کرتا ہے؟"),
     T("Right! LCM = 30.", "درست! ذو اضعاف اقل = 30"),
     T("10, 20, 30: 30 ÷ 6 = 5. LCM = 30.", "10، 20، 30: 30 ÷ 6 = 5۔ ذو اضعاف اقل = 30"),
     common_wrong=[wrong(60, "60 = 6 × 10 works, but 30 is lower.", "60 = 6 × 10 بھی ضعف ہے، مگر 30 چھوٹا ہے۔"),
                   wrong(2, "2 is the HCF. The LCM is a multiple of both: 30.", "2 عاد اعظم ہے۔ ذو اضعاف اقل دونوں کا ضعف ہے: 30")],
     qtype="apply", skill=FM_LCM),
   number_question(
     "u5_problem",
     T("Test 5: Ali visits the library every 4 days and Ayesha every 10 days. They met there today. In how many days do they meet there again?", "ٹیسٹ 5: علی ہر 4 دن بعد اور عائشہ ہر 10 دن بعد لائبریری جاتے ہیں۔ آج وہاں ملے۔ کتنے دن بعد دوبارہ ملیں گے؟"),
     U5,
     T("Meeting again: LCM of 4 and 10.", "دوبارہ ملنا: 4 اور 10 کا ذو اضعاف اقل۔"),
     T("Right! In 20 days.", "درست! 20 دن بعد۔"),
     T("Multiples of 10: 10, 20. 20 ÷ 4 = 5. LCM = 20 days.", "10 کے اضعاف: 10، 20۔ 20 ÷ 4 = 5۔ ذو اضعاف اقل = 20 دن"),
     common_wrong=[wrong(2, "2 is the HCF. Meeting again needs the LCM: 20.", "2 عاد اعظم ہے۔ دوبارہ ملنے کے لیے ذو اضعاف اقل: 20", "wrong_tool"),
                   wrong(40, "40 = 4 × 10 works, but they meet sooner: 20.", "40 = 4 × 10 بھی ٹھیک ہے، مگر وہ پہلے ملتے ہیں: 20")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You finished the Factors and multiples unit! Well done!",
                     "آپ نے اجزائے ضربی اور اضعاف کا باب مکمل کر لیا! شاباش!"),
    "text": T("Splitting into the largest equal groups, rows or pieces: use the HCF. Things repeating and happening together again, or the smallest amount both fit into: use the LCM. Then answer the real question (how many bags, what time).",
              "سب سے بڑے برابر گروہ، قطاریں یا ٹکڑے: عاد اعظم۔ بار بار ہونے والی چیزیں دوبارہ ساتھ، یا سب سے چھوٹی مقدار جس میں دونوں پورے آئیں: ذو اضعاف اقل۔ پھر اصل سوال کا جواب دیں (کتنے تھیلے، کیا وقت)۔"),
    "points": [T("HCF answers are no bigger than the numbers; LCM answers are no smaller.", "عاد اعظم کا جواب اعداد سے بڑا نہیں ہوتا؛ ذو اضعاف اقل کا جواب اعداد سے چھوٹا نہیں ہوتا۔"),
               T("Check your answer makes sense in the story.", "دیکھیں کہ جواب کہانی میں ٹھیک بیٹھتا ہے۔")]},
 ],
 "review_questions": [
   {"id": "r_lcm_problem", "type": "apply", "skill": SKILL, "step": number_question(
     "r_lcm_problem",
     T("Pens come in boxes of 12 and caps in bags of 16. What is the smallest number of pens and caps so each pen has one cap?", "قلم 12 کے ڈبے میں اور ڈھکن 16 کے تھیلے میں آتے ہیں۔ کم از کم کتنے قلم اور ڈھکن ہوں کہ ہر قلم کا ایک ڈھکن ہو؟"),
     R1,
     T("The smallest amount both fit into: LCM.", "سب سے چھوٹی مقدار جس میں دونوں پورے آئیں: ذو اضعاف اقل۔"),
     T("Right! 48 pens and 48 caps.", "درست! 48 قلم اور 48 ڈھکن۔"),
     T("Multiples of 16: 16, 32, 48. 48 ÷ 12 = 4. LCM = 48.", "16 کے اضعاف: 16، 32، 48۔ 48 ÷ 12 = 4۔ ذو اضعاف اقل = 48"),
     common_wrong=[wrong(4, "4 is the HCF. You need a common multiple: 48.", "4 عاد اعظم ہے۔ مشترک ضعف چاہیے: 48", "wrong_tool")],
     qtype=None)},
   {"id": "r_hcf_problem", "type": "recall", "skill": SKILL, "step": number_question(
     "r_hcf_problem",
     T("Two ropes, 40 m and 56 m, are cut into equal pieces as long as possible, nothing left. How long is each piece?", "دو رسیاں، 40 میٹر اور 56 میٹر، برابر اور جتنے لمبے ہو سکیں ٹکڑوں میں کاٹی گئیں، کچھ نہ بچا۔ ہر ٹکڑا کتنا لمبا ہے؟"),
     R2,
     T("Largest equal pieces: HCF of 40 and 56.", "سب سے لمبے برابر ٹکڑے: 40 اور 56 کا عاد اعظم۔"),
     T("Right! 8 m pieces.", "درست! 8 میٹر کے ٹکڑے۔"),
     T("40 = 2 × 2 × 2 × 5, 56 = 2 × 2 × 2 × 7. HCF = 8.", "40 = 2 × 2 × 2 × 5، 56 = 2 × 2 × 2 × 7۔ عاد اعظم = 8"),
     common_wrong=[wrong(280, "280 m is longer than both ropes! Use the HCF: 8.", "280 میٹر دونوں رسیوں سے لمبا ہے! عاد اعظم لیں: 8", "wrong_tool"),
                   wrong(4, "4 m pieces work, but 8 m is longer.", "4 میٹر کے ٹکڑے بن سکتے ہیں، مگر 8 میٹر لمبے ہیں۔")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Factors and Multiples unit. No textbook text or exercises were used.",
   "The main idea is choosing the tool: HCF for splitting into the largest equal parts, LCM for things lining up again. Step s8 checks that the child answers the actual question, not just the LCM.",
   "Steps u1 to u5 are a short unit test; each is tagged with the skill of the lesson it comes from.",
   "The numbers were worked out in content/sources/g6-maths-05/factor_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

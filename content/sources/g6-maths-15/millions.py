from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, WN_PLACE_VALUE, WN_SYSTEMS, LAKH, CRORE, MILLION, pk, intl)

SKILL = WN_SYSTEMS

# s2: thousands in a lakh
S2 = LAKH // 1000
assert S2 == 100
# s4: lakhs in a million
S4 = MILLION // LAKH
assert S4 == 10
# s5: 5 million in lakhs
S5 = 5 * MILLION // LAKH
assert S5 == 50
# s6: 2,500,000 in Pakistani commas
S6 = 2_500_000
assert intl(S6) == "2,500,000" and pk(S6) == "25,00,000" and S6 == 25 * LAKH
# s7: 3 crore in millions
S7 = 3 * CRORE // MILLION
assert S7 == 30
# s8: thousands in a million
S8 = MILLION // 1000
assert S8 == 1000
# s9: 1 crore = 10 million
assert CRORE == 10 * MILLION and MILLION == 10 * LAKH
# s11: 240 million in crore
S11 = 240 * MILLION // CRORE
assert S11 == 24
# question bank and review
QB = 7 * MILLION // LAKH
assert QB == 70
R1 = 2 * CRORE // MILLION
assert R1 == 20
R2 = 8 * MILLION // LAKH
assert R2 == 80

lesson = {
 "id": "g6-maths-15-millions",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Read and write large numbers in the international system (millions) and change between the Pakistani and international systems.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Millions: the international system", "ملین: بین الاقوامی نظام"),
 "estimated_minutes": 14,
 "prerequisites": [{"skill": WN_PLACE_VALUE}],
 "misconceptions": [
   {"id": "million_lakh", "description": "Thinks 1 million is 1 lakh, or 100 lakh."},
   {"id": "million_crore", "description": "Thinks 1 million is 1 crore."},
   {"id": "mixed_commas", "description": "Mixes Pakistani and international comma groups."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_million", "type": "recall", "step": {
     "id": "qb_million", "type": "choice",
     "prompt": T("1 million is the same as …", "1 ملین برابر ہے …"),
     "options": [
       opt("ten_lakh", "10 lakh", "10 لاکھ", True,
           "Yes! 1,000,000 = 10,00,000.", "جی ہاں! 1,000,000 = 10,00,000"),
       opt("crore", "1 crore", "1 کروڑ", False,
           "1 crore is 10 million. 1 million = 10 lakh.", "1 کروڑ 10 ملین ہے۔ 1 ملین = 10 لاکھ", "million_crore"),
       opt("lakh", "1 lakh", "1 لاکھ", False,
           "1 lakh is 1,00,000, which has 5 zeros. 1 million has 6: 10 lakh.", "1 لاکھ 1,00,000 ہے، 5 صفر۔ 1 ملین میں 6 ہیں: 10 لاکھ", "million_lakh"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("7 million is how many lakh?", "7 ملین کتنے لاکھ ہیں؟"),
     QB,
     T("1 million = 10 lakh.", "1 ملین = 10 لاکھ"),
     T("Right! 70 lakh.", "درست! 70 لاکھ"),
     T("7 × 10 = 70 lakh.", "7 × 10 = 70 لاکھ"),
     common_wrong=[wrong(7, "1 million is 10 lakh, not 1: 70 lakh.", "1 ملین 10 لاکھ ہے، 1 نہیں: 70 لاکھ", "million_lakh"),
                   wrong(700, "1 million is 10 lakh, not 100: 70 lakh.", "1 ملین 10 لاکھ ہے، 100 نہیں: 70 لاکھ", "million_lakh")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Ayesha writes 3,500,000 the Pakistani way as 3,50,00,000. What is wrong?", "عائشہ 3,500,000 کو پاکستانی طریقے سے 3,50,00,000 لکھتی ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("extra_zero", "She added a zero. It is 35,00,000 (35 lakh).", "اس نے ایک صفر زیادہ لگایا۔ یہ 35,00,000 (35 لاکھ) ہے۔", True,
           "Yes! Keep the same digits and only move the commas.", "جی ہاں! ہندسے وہی رکھیں، صرف کامے بدلیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "3,50,00,000 is 3.5 crore. 3,500,000 has 7 digits: 35,00,000.", "3,50,00,000 ساڑھے 3 کروڑ ہے۔ 3,500,000 میں 7 ہندسے ہیں: 35,00,000", "mixed_commas"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_million", "front": T("1 million?", "1 ملین؟"),
    "back": T("1,000,000 = 10 lakh.", "1,000,000 = 10 لاکھ")},
   {"id": "f_crore", "front": T("1 crore in millions?", "1 کروڑ کتنے ملین؟"),
    "back": T("10 million.", "10 ملین")},
 ],
 "home_tasks": [{"id": "h_population", "text": T(
   "Ask someone at home how many people live in Pakistan (about 240 million). Say it in crores too.",
   "گھر میں کسی سے پوچھیں کہ پاکستان میں کتنے لوگ رہتے ہیں (تقریباً 240 ملین)۔ اسے کروڑ میں بھی بتائیں۔")}],
 "glossary": [T("Million", "ملین (دس لاکھ)"), T("Billion", "ارب"), T("International system", "بین الاقوامی نظام")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "The news says 240 million people live in Pakistan. Is that more or less than a crore?",
                     "خبروں میں کہتے ہیں پاکستان میں 240 ملین لوگ رہتے ہیں۔ یہ ایک کروڑ سے زیادہ ہے یا کم؟"),
    "text": T("Today we learn the international system, with millions, and change numbers between it and lakhs and crores. First, a quick lakh check.", "آج ہم ملین والا بین الاقوامی نظام سیکھیں گے، اور اعداد کو اس سے لاکھ اور کروڑ میں بدلیں گے۔ پہلے لاکھ کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many thousands make 1 lakh?", "کتنے ہزار مل کر 1 لاکھ بنتے ہیں؟"),
     S2,
     T("1,00,000 ÷ 1000.", "1,00,000 ÷ 1000"),
     T("Right! 100 thousand.", "درست! 100 ہزار"),
     T("1,00,000 ÷ 1000 = 100.", "1,00,000 ÷ 1000 = 100"),
     common_wrong=[wrong(10, "10 thousand is 10,000. 1 lakh = 100 thousand.", "10 ہزار 10,000 ہے۔ 1 لاکھ = 100 ہزار")],
     qtype="recall", skill=WN_PLACE_VALUE),
   {"id": "s3_rule", "type": "explain",
    "character": say("happy", "Same number, different commas. Only the names change!", "عدد وہی، کامے مختلف۔ صرف نام بدلتے ہیں!"),
    "text": T("In the international system, put a comma after every 3 digits from the right: 1,000 is a thousand, 1,000,000 is a million, 1,000,000,000 is a billion. 1 million = 10 lakh. 10 million = 1 crore. 1 billion = 100 crore (1 arab). To change systems, keep the digits and move the commas: 2,500,000 = 25,00,000.",
              "بین الاقوامی نظام میں دائیں سے ہر 3 ہندسوں کے بعد کاما لگائیں: 1,000 ایک ہزار، 1,000,000 ایک ملین، 1,000,000,000 ایک بلین۔ 1 ملین = 10 لاکھ۔ 10 ملین = 1 کروڑ۔ 1 بلین = 100 کروڑ (1 ارب)۔ نظام بدلنے کے لیے ہندسے وہی رکھیں اور کامے بدلیں: 2,500,000 = 25,00,000")},
   number_question(
     "s4_million_lakh",
     T("1 million is how many lakh?", "1 ملین کتنے لاکھ ہیں؟"),
     S4,
     T("1,000,000 = 10,00,000.", "1,000,000 = 10,00,000"),
     T("Right! 10 lakh.", "درست! 10 لاکھ"),
     T("1,000,000 has 6 zeros. 1 lakh has 5. So 1 million = 10 lakh.", "1,000,000 میں 6 صفر ہیں۔ 1 لاکھ میں 5۔ تو 1 ملین = 10 لاکھ"),
     common_wrong=[wrong(1, "1 lakh is 1,00,000, smaller than a million: 10 lakh.", "1 لاکھ 1,00,000 ہے، ملین سے چھوٹا: 10 لاکھ", "million_lakh"),
                   wrong(100, "100 lakh is 1 crore. 1 million = 10 lakh.", "100 لاکھ 1 کروڑ ہے۔ 1 ملین = 10 لاکھ", "million_crore")]),
   number_question(
     "s5_five_million",
     T("5 million is how many lakh?", "5 ملین کتنے لاکھ ہیں؟"),
     S5,
     T("Each million is 10 lakh.", "ہر ملین 10 لاکھ ہے۔"),
     T("Right! 50 lakh.", "درست! 50 لاکھ"),
     T("5 × 10 = 50 lakh.", "5 × 10 = 50 لاکھ"),
     common_wrong=[wrong(5, "1 million is 10 lakh: 50 lakh.", "1 ملین 10 لاکھ ہے: 50 لاکھ", "million_lakh"),
                   wrong(500, "1 million is 10 lakh, not 100: 50 lakh.", "1 ملین 10 لاکھ ہے، 100 نہیں: 50 لاکھ", "million_crore")]),
   {"id": "s6_commas", "type": "choice",
    "prompt": T(f"Write {intl(S6)} with Pakistani commas.", f"{intl(S6)} کو پاکستانی طریقے سے کاما لگا کر لکھیں۔"),
    "options": [
      opt("pk", pk(S6), pk(S6), True, "Yes! 25 lakh.", "جی ہاں! 25 لاکھ"),
      opt("extra", "2,50,00,000", "2,50,00,000", False, "That adds a zero (2.5 crore). Keep the 7 digits: 25,00,000.", "اس میں ایک صفر زیادہ ہے (ڈھائی کروڑ)۔ 7 ہندسے رکھیں: 25,00,000", "mixed_commas"),
      opt("short", "2,50,000", "2,50,000", False, "That drops a zero (2.5 lakh). Keep the 7 digits: 25,00,000.", "اس میں ایک صفر کم ہے (ڈھائی لاکھ)۔ 7 ہندسے رکھیں: 25,00,000", "mixed_commas"),
    ]},
   number_question(
     "s7_crore_million",
     T("3 crore is how many million?", "3 کروڑ کتنے ملین ہیں؟"),
     S7,
     T("1 crore = 10 million.", "1 کروڑ = 10 ملین"),
     T("Right! 30 million.", "درست! 30 ملین"),
     T("3 × 10 = 30 million.", "3 × 10 = 30 ملین"),
     common_wrong=[wrong(3, "A crore is bigger than a million: 1 crore = 10 million, so 30.", "کروڑ ملین سے بڑا ہے: 1 کروڑ = 10 ملین، تو 30", "million_crore"),
                   wrong(300, "1 crore is 10 million, not 100: 30 million.", "1 کروڑ 10 ملین ہے، 100 نہیں: 30 ملین")]),
   number_question(
     "s8_thousands",
     T("How many thousands make 1 million?", "کتنے ہزار مل کر 1 ملین بنتے ہیں؟"),
     S8,
     T("1,000,000 ÷ 1,000.", "1,000,000 ÷ 1,000"),
     T("Right! 1000 thousands.", "درست! 1000 ہزار"),
     T("1,000,000 ÷ 1,000 = 1000.", "1,000,000 ÷ 1,000 = 1000"),
     common_wrong=[wrong(100, "100 thousand is 1 lakh. 1 million = 1000 thousand.", "100 ہزار 1 لاکھ ہے۔ 1 ملین = 1000 ہزار", "million_lakh")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Sana says 1 million is the same as 1 crore. What went wrong?", "ثنا کہتی ہے 1 ملین اور 1 کروڑ برابر ہیں۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("ten", "1 million = 10 lakh. 1 crore = 10 million.", "1 ملین = 10 لاکھ۔ 1 کروڑ = 10 ملین۔", True,
          "Yes! 1,000,000 has 6 zeros; 1,00,00,000 has 7.", "جی ہاں! 1,000,000 میں 6 صفر ہیں؛ 1,00,00,000 میں 7۔"),
      opt("lakh", "1 million = 1 lakh.", "1 ملین = 1 لاکھ۔", False,
          "1 lakh has 5 zeros, a million has 6: 1 million = 10 lakh.", "1 لاکھ میں 5 صفر، ملین میں 6: 1 ملین = 10 لاکھ", "million_lakh"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "Count the zeros: a million has 6, a crore has 7. A crore is 10 million.", "صفر گنیں: ملین میں 6، کروڑ میں 7۔ کروڑ 10 ملین ہے۔", "million_crore"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "How do you change 4,000,000 into lakhs? Can you teach me?",
                     "آپ 4,000,000 کو لاکھ میں کیسے بدلتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: how do you change a number from millions to lakhs? Use 4 million as your example.", "اپنے الفاظ میں بتائیں: ملین کو لاکھ میں کیسے بدلتے ہیں؟ 4 ملین کی مثال لیں۔"),
    "key_idea": "1 million = 10 lakh, so multiply the millions by 10: 4 million = 40 lakh. Or keep the digits 4000000 and put Pakistani commas: 40,00,000.",
    "levels": {
      "got_it": "Says 1 million = 10 lakh, so 4 million = 40 lakh (or rewrites the commas as 40,00,000).",
      "partly": "Gets 40 lakh with no reason, or gives the rule without the example.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["10", "ten", "دس"],
      ["40", "forty", "چالیس"],
      ["comma", "کاما"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Each million is 10 lakh.", "بہت خوب! ہر ملین 10 لاکھ ہے۔"),
      "partly": T("Good start! Now say how many lakh are in one million.", "اچھی شروعات! اب بتائیں ایک ملین میں کتنے لاکھ ہیں۔"),
      "not_yet": T("How many lakh make 1 million? Then what about 4 million?", "کتنے لاکھ سے 1 ملین بنتا ہے؟ پھر 4 ملین؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_population",
     T("Pakistan has about 240 million people. How many crore is that?", "پاکستان میں تقریباً 240 ملین لوگ ہیں۔ یہ کتنے کروڑ ہیں؟"),
     S11,
     T("10 million = 1 crore.", "10 ملین = 1 کروڑ"),
     T("Right! About 24 crore.", "درست! تقریباً 24 کروڑ"),
     T("240 ÷ 10 = 24 crore.", "240 ÷ 10 = 24 کروڑ"),
     common_wrong=[wrong(240, "A crore is 10 million, so divide by 10: 24 crore.", "کروڑ 10 ملین ہے، تو 10 سے تقسیم کریں: 24 کروڑ", "million_crore"),
                   wrong(2400, "That would be lakh. In crore, 240 ÷ 10 = 24.", "یہ لاکھ ہوں گے۔ کروڑ میں 240 ÷ 10 = 24")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Now you can read big numbers both ways, Pakistani and international!", "اب آپ بڑے اعداد دونوں طریقوں سے پڑھ سکتے ہیں، پاکستانی اور بین الاقوامی!"),
    "text": T("International commas go every 3 digits. 1 million = 10 lakh, 10 million = 1 crore, 1 billion = 100 crore. To change systems, keep the digits and move the commas.",
              "بین الاقوامی کامے ہر 3 ہندسوں کے بعد۔ 1 ملین = 10 لاکھ، 10 ملین = 1 کروڑ، 1 بلین = 100 کروڑ۔ نظام بدلنے کے لیے ہندسے وہی رکھیں اور کامے بدلیں۔"),
    "points": [T("1 million = 10 lakh.", "1 ملین = 10 لاکھ"),
               T("1 crore = 10 million.", "1 کروڑ = 10 ملین")]},
 ],
 "review_questions": [
   {"id": "r_crore", "type": "apply", "skill": SKILL, "step": number_question(
     "r_crore",
     T("2 crore is how many million?", "2 کروڑ کتنے ملین ہیں؟"),
     R1,
     T("1 crore = 10 million.", "1 کروڑ = 10 ملین"),
     T("Right! 20 million.", "درست! 20 ملین"),
     T("2 × 10 = 20.", "2 × 10 = 20"),
     common_wrong=[wrong(2, "1 crore is 10 million: 20.", "1 کروڑ 10 ملین ہے: 20", "million_crore")],
     qtype=None)},
   {"id": "r_lakh", "type": "apply", "skill": SKILL, "step": number_question(
     "r_lakh",
     T("8 million is how many lakh?", "8 ملین کتنے لاکھ ہیں؟"),
     R2,
     T("1 million = 10 lakh.", "1 ملین = 10 لاکھ"),
     T("Right! 80 lakh.", "درست! 80 لاکھ"),
     T("8 × 10 = 80.", "8 × 10 = 80"),
     common_wrong=[wrong(8, "1 million is 10 lakh: 80.", "1 ملین 10 لاکھ ہے: 80", "million_lakh"),
                   wrong(800, "1 million is 10 lakh, not 100: 80.", "1 ملین 10 لاکھ ہے، 100 نہیں: 80", "million_crore")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Whole Numbers unit. No textbook text or exercises were used.",
   "Pakistan's population (about 240 million, 24 crore) is rounded; it only gives the numbers a real-life feel.",
   "Urdu terms to check: ملین, بلین / ارب, بین الاقوامی نظام (international system).",
   "The numbers were worked out in content/sources/g6-maths-15/millions.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

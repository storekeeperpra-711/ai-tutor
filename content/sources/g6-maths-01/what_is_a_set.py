from common import (T, opt, say, wrong, number_question, write, show,
                    REF, REVIEW, FACTORS, SET_MEANING)

SKILL = SET_MEANING


def factors(n):
    return {d for d in range(1, n + 1) if n % d == 0}


def letters(word):
    return set(word)


# s2: number of factors of 12
S2 = len(factors(12))
assert S2 == 6
# s4: vowels
S4 = len(set("aeiou"))
assert S4 == 5
# s6: even numbers between 1 and 11
EVENS = {n for n in range(2, 11) if n % 2 == 0}
S6 = len(EVENS)
assert EVENS == {2, 4, 6, 8, 10} and S6 == 5
# s7: letters of PAKISTAN (A repeats)
S7 = len(letters("PAKISTAN"))
assert S7 == 7 and len("PAKISTAN") == 8
# s8: A = {1, 3, 5, 7}
A8 = {1, 3, 5, 7}
assert 5 in A8 and 4 not in A8 and 7 in A8
# s9: letters of APPLE
assert len(letters("APPLE")) == 4
# s11: factors of 18
F18 = factors(18)
S11 = len(F18)
assert F18 == {1, 2, 3, 6, 9, 18} and S11 == 6
# question bank and review
QB = len(letters("LAHORE"))
assert QB == 6
R1 = len({n for n in range(1, 10) if n % 2})
assert R1 == 5
R2 = len(letters("BALL"))
assert R2 == 3

lesson = {
 "id": "g6-maths-01-what-is-a-set",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Recognise a set as a well-defined collection, write it in braces, and use the signs ∈ and ∉.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("What is a set?", "سیٹ کیا ہے؟"),
 "estimated_minutes": 12,
 "prerequisites": [{"skill": FACTORS}],
 "misconceptions": [
   {"id": "repeats", "description": "Lists or counts a repeated element more than once."},
   {"id": "not_well_defined", "description": "Thinks any collection is a set, even one based on opinion (\"beautiful flowers\")."},
   {"id": "element_sign", "description": "Mixes up ∈ (is an element of) and ∉ (is not an element of)."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_element", "type": "recall", "step": {
     "id": "qb_element", "type": "choice",
     "prompt": T("What does 3 ∈ A mean?", "3 ∈ A کا کیا مطلب ہے؟"),
     "options": [
       opt("in", "3 is an element of set A", "3، سیٹ A کا رکن ہے", True,
           "Yes! ∈ means \"is an element of\".", "جی ہاں! ∈ کا مطلب ہے \"کا رکن ہے\"۔"),
       opt("not_in", "3 is not in set A", "3، سیٹ A میں نہیں ہے", False,
           "That would be 3 ∉ A, with a line through the sign.", "وہ 3 ∉ A ہوتا، نشان پر لکیر کے ساتھ۔", "element_sign"),
       opt("three", "A has 3 elements", "A کے 3 رکن ہیں", False,
           "∈ says one thing belongs to a set: 3 is an element of A.", "∈ بتاتا ہے کہ ایک چیز سیٹ میں شامل ہے: 3، A کا رکن ہے۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("How many elements are in the set of letters of the word LAHORE?", "لفظ LAHORE کے حروف کے سیٹ میں کتنے رکن ہیں؟"),
     QB,
     T("Write each different letter once.", "ہر مختلف حرف ایک بار لکھیں۔"),
     T("Right! {L, A, H, O, R, E} has 6 elements.", "درست! {L, A, H, O, R, E} کے 6 رکن ہیں۔"),
     T("L, A, H, O, R, E: 6 letters, none repeated.", "L، A، H، O، R، E: چھ حروف، کوئی دہرایا نہیں۔"),
     common_wrong=[wrong(5, "Count again: L, A, H, O, R, E is 6.", "دوبارہ گنیں: L، A، H، O، R، E یعنی 6")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Asad says \"the clever children in my class\" is a set. What is wrong?", "اسد کہتا ہے \"میری کلاس کے ذہین بچے\" ایک سیٹ ہے۔ کیا غلطی ہے؟"),
     "options": [
       opt("opinion", "\"Clever\" is an opinion, so it isn't clear who belongs.", "\"ذہین\" ایک رائے ہے، اس لیے واضح نہیں کون شامل ہے۔", True,
           "Yes! A set must be well defined: everyone must agree what is in it.", "جی ہاں! سیٹ واضح ہونا چاہیے: سب متفق ہوں کہ اس میں کیا ہے۔"),
       opt("nothing", "Nothing, it is a set.", "کوئی غلطی نہیں، یہ سیٹ ہے۔", False,
           "People could disagree about who is clever, so it is not well defined.", "لوگ اختلاف کر سکتے ہیں کہ کون ذہین ہے، اس لیے یہ واضح نہیں۔", "not_well_defined"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_set", "front": T("A set?", "سیٹ؟"),
    "back": T("A well-defined collection, written in braces: {2, 4, 6}. No element is written twice.", "واضح طور پر بیان کیا گیا مجموعہ، بریکٹ میں لکھا جاتا ہے: {2, 4, 6}۔ کوئی رکن دو بار نہیں لکھا جاتا۔")},
   {"id": "f_signs", "front": T("∈ and ∉?", "∈ اور ∉؟"),
    "back": T("5 ∈ A: 5 is in A. 4 ∉ A: 4 is not in A.", "5 ∈ A: 5، A میں ہے۔ 4 ∉ A: 4، A میں نہیں ہے۔")},
 ],
 "home_tasks": [{"id": "h_sets", "text": T(
   "Write three sets from your home, in braces: for example the set of people in your family, the set of colours on your school bag, or the set of letters in your name. Count the elements of each.",
   "اپنے گھر سے تین سیٹ بریکٹ میں لکھیں: مثلاً گھر کے افراد کا سیٹ، اسکول بیگ کے رنگوں کا سیٹ، یا آپ کے نام کے حروف کا سیٹ۔ ہر ایک کے رکن گنیں۔")}],
 "glossary": [T("Set", "سیٹ"), T("Element", "رکن"), T("Well defined", "واضح طور پر بیان کردہ"), T("Braces { }", "بریکٹ { }")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Days of the week, the vowels, players in a cricket team. What do these groups have in common?",
                     "ہفتے کے دن، حروفِ علت، کرکٹ ٹیم کے کھلاڑی۔ ان گروہوں میں کیا بات مشترک ہے؟"),
    "text": T("Today we learn about sets. First, a quick check on factors.", "آج ہم سیٹ کے بارے میں سیکھیں گے۔ پہلے اجزائے ضربی کا ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many factors does 12 have?", "12 کے کتنے اجزائے ضربی ہیں؟"),
     S2,
     T("1, 2, 3, … which numbers divide 12 exactly?", "1، 2، 3، … کون سے اعداد 12 کو پورا تقسیم کرتے ہیں؟"),
     T("Right! 1, 2, 3, 4, 6 and 12.", "درست! 1، 2، 3، 4، 6 اور 12"),
     T("1, 2, 3, 4, 6, 12: that is 6 factors.", "1، 2، 3، 4، 6، 12: یعنی 6 اجزائے ضربی"),
     common_wrong=[wrong(4, "Don't forget 1 and 12 itself: 6 factors.", "1 اور خود 12 کو نہ بھولیں: 6 اجزائے ضربی")],
     qtype="recall", skill=FACTORS),
   {"id": "s3_set", "type": "explain",
    "character": say("happy", "A set is a group where everyone agrees exactly what belongs!", "سیٹ ایسا گروہ ہے جس میں سب متفق ہوں کہ کیا شامل ہے!"),
    "text": T("A set is a well-defined collection: it must be clear what is in it. The things in a set are its elements. We write a set in braces, with commas: the vowels are {a, e, i, o, u}. Each element is written once, and the order does not matter. 5 ∈ A means 5 is an element of A; 4 ∉ A means 4 is not.",
              "سیٹ واضح طور پر بیان کیا گیا مجموعہ ہے: صاف پتا ہو کہ اس میں کیا ہے۔ سیٹ میں شامل چیزیں اس کے رکن کہلاتی ہیں۔ سیٹ کو بریکٹ میں، کاموں کے ساتھ لکھتے ہیں: حروفِ علت {a, e, i, o, u} ہیں۔ ہر رکن ایک بار لکھا جاتا ہے، اور ترتیب اہم نہیں۔ 5 ∈ A کا مطلب ہے 5، A کا رکن ہے؛ 4 ∉ A کا مطلب ہے 4 نہیں ہے۔")},
   number_question(
     "s4_vowels",
     T("How many elements are in {a, e, i, o, u}?", "{a, e, i, o, u} میں کتنے رکن ہیں؟"),
     S4,
     T("Count the letters between the braces.", "بریکٹ کے اندر حروف گنیں۔"),
     T("Right! 5 elements.", "درست! 5 رکن"),
     T("a, e, i, o, u: 5 elements.", "a، e، i، o، u: پانچ رکن"),
     common_wrong=[wrong(1, "The set is one thing, but it has 5 elements inside it.", "سیٹ ایک چیز ہے، لیکن اس کے اندر 5 رکن ہیں۔")]),
   {"id": "s5_well_defined", "type": "choice",
    "prompt": T("Which of these is a set?", "ان میں سے کون سا سیٹ ہے؟"),
    "options": [
      opt("days", "The days of the week", "ہفتے کے دن", True,
          "Yes! Everyone agrees on the 7 days.", "جی ہاں! سب 7 دنوں پر متفق ہیں۔"),
      opt("flowers", "Beautiful flowers", "خوبصورت پھول", False,
          "\"Beautiful\" is an opinion, so it isn't well defined.", "\"خوبصورت\" ایک رائے ہے، اس لیے یہ واضح نہیں۔", "not_well_defined"),
      opt("tall", "Tall boys in the school", "اسکول کے لمبے لڑکے", False,
          "How tall is \"tall\"? People would disagree, so it isn't well defined.", "\"لمبا\" کتنا لمبا؟ لوگ اختلاف کریں گے، اس لیے یہ واضح نہیں۔", "not_well_defined"),
    ]},
   number_question(
     "s6_evens",
     T("How many elements are in the set of even numbers between 1 and 11?", "1 اور 11 کے درمیان جفت اعداد کے سیٹ میں کتنے رکن ہیں؟"),
     S6,
     T("Write them out: {2, 4, …}.", "انہیں لکھیں: {2, 4, …}"),
     T(f"Right! {show(EVENS)} has 5 elements.", f"درست! {show(EVENS)} کے 5 رکن ہیں۔"),
     T(f"{show(EVENS)}: 5 elements.", f"{show(EVENS)}: پانچ رکن"),
     common_wrong=[wrong(4, "Don't forget 10: 2, 4, 6, 8, 10 is 5.", "10 کو نہ بھولیں: 2، 4، 6، 8، 10 یعنی 5"),
                   wrong(6, "12 is not between 1 and 11: 2, 4, 6, 8, 10 is 5.", "12، 1 اور 11 کے درمیان نہیں: 2، 4، 6، 8، 10 یعنی 5")]),
   number_question(
     "s7_pakistan",
     T("How many elements are in the set of letters of the word PAKISTAN?", "لفظ PAKISTAN کے حروف کے سیٹ میں کتنے رکن ہیں؟"),
     S7,
     T("A appears twice in the word, but only once in the set.", "لفظ میں A دو بار ہے، لیکن سیٹ میں ایک بار۔"),
     T("Right! {P, A, K, I, S, T, N} has 7 elements.", "درست! {P, A, K, I, S, T, N} کے 7 رکن ہیں۔"),
     T("P, A, K, I, S, T, N: 7, since A is written once.", "P، A، K، I، S، T، N: سات، کیونکہ A ایک بار لکھا جاتا ہے۔"),
     common_wrong=[wrong(8, "The word has 8 letters, but A repeats. In a set it is written once: 7.", "لفظ میں 8 حروف ہیں، لیکن A دہرایا گیا ہے۔ سیٹ میں یہ ایک بار لکھا جاتا ہے: 7", "repeats")]),
   {"id": "s8_signs", "type": "choice",
    "prompt": T(f"A = {show(A8)}. Which is true?", f"A = {show(A8)}۔ کون سا درست ہے؟"),
    "options": [
      opt("five", "5 ∈ A", "5 ∈ A", True, "Yes! 5 is in A.", "جی ہاں! 5، A میں ہے۔"),
      opt("four", "4 ∈ A", "4 ∈ A", False, "4 is not in A, so 4 ∉ A.", "4، A میں نہیں ہے، تو 4 ∉ A۔", "element_sign"),
      opt("seven", "7 ∉ A", "7 ∉ A", False, "7 is in A, so 7 ∈ A.", "7، A میں ہے، تو 7 ∈ A۔", "element_sign"),
    ]},
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Zain writes the set of letters of APPLE as {A, P, P, L, E}. What went wrong?", "زین لفظ APPLE کے حروف کا سیٹ {A, P, P, L, E} لکھتا ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("repeat", "P is written twice. It should be {A, P, L, E}.", "P دو بار لکھا ہے۔ یہ {A, P, L, E} ہونا چاہیے۔", True,
          "Yes! Each element is written only once.", "جی ہاں! ہر رکن صرف ایک بار لکھا جاتا ہے۔"),
      opt("order", "The letters are in the wrong order.", "حروف غلط ترتیب میں ہیں۔", False,
          "Order doesn't matter in a set. The problem is P written twice.", "سیٹ میں ترتیب اہم نہیں۔ مسئلہ P کا دو بار لکھا جانا ہے۔"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "P appears twice. In a set each element is written once: {A, P, L, E}.", "P دو بار ہے۔ سیٹ میں ہر رکن ایک بار لکھا جاتا ہے: {A, P, L, E}", "repeats"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why is \"the good cricketers of Pakistan\" not a set, but \"the players in today's team\" is? Can you teach me?",
                     "\"پاکستان کے اچھے کرکٹرز\" سیٹ کیوں نہیں، لیکن \"آج کی ٹیم کے کھلاڑی\" سیٹ کیوں ہے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is one of these a set and the other not?", "اپنے الفاظ میں بتائیں: ان میں سے ایک سیٹ کیوں ہے اور دوسرا کیوں نہیں؟"),
    "key_idea": "A set must be well defined: it must be clear to everyone what belongs. \"Good\" is an opinion, so people would disagree; the players in today's team are a definite list.",
    "levels": {
      "got_it": "Says a set must be clear or well defined, and \"good\" is an opinion that people could disagree about.",
      "partly": "Says \"good\" is an opinion, or that the team is a fixed list, but not both.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["opinion", "think", "disagree", "رائے", "سوچ", "اختلاف"],
      ["clear", "well defined", "exact", "واضح", "صاف"],
      ["list", "fixed", "team", "فہرست", "ٹیم"]],
    "fallback_feedback": {
      "got_it": T("Well explained! A set must be clear, and \"good\" is only an opinion.", "بہت خوب! سیٹ واضح ہونا چاہیے، اور \"اچھا\" صرف ایک رائے ہے۔"),
      "partly": T("Good start! Now say what makes the team a clear list.", "اچھی شروعات! اب بتائیں ٹیم واضح فہرست کیوں ہے۔"),
      "not_yet": T("Would everyone agree who the \"good\" cricketers are? Would everyone agree who is in today's team?", "کیا سب متفق ہوں گے کہ \"اچھے\" کرکٹر کون ہیں؟ کیا سب متفق ہوں گے کہ آج کی ٹیم میں کون ہے؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_factors",
     T("How many elements are in the set of factors of 18?", "18 کے اجزائے ضربی کے سیٹ میں کتنے رکن ہیں؟"),
     S11,
     T("Find every number that divides 18 exactly.", "ہر وہ عدد ڈھونڈیں جو 18 کو پورا تقسیم کرے۔"),
     T(f"Right! {show(F18)} has 6 elements.", f"درست! {show(F18)} کے 6 رکن ہیں۔"),
     T(f"{show(F18)}: 6 elements.", f"{show(F18)}: چھ رکن"),
     common_wrong=[wrong(4, "Include 1 and 18: {1, 2, 3, 6, 9, 18} has 6.", "1 اور 18 شامل کریں: {1, 2, 3, 6, 9, 18} کے 6 رکن ہیں۔")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can write and read sets now!", "اب آپ سیٹ لکھ اور پڑھ سکتے ہیں!"),
    "text": T("A set is a well-defined collection, written in braces with commas, like {2, 4, 6}. Its members are elements. Each element is written once and order does not matter. ∈ means \"is an element of\", and ∉ means \"is not an element of\".",
              "سیٹ واضح طور پر بیان کیا گیا مجموعہ ہے، جو بریکٹ میں کاموں کے ساتھ لکھا جاتا ہے، جیسے {2, 4, 6}۔ اس کے ارکان رکن کہلاتے ہیں۔ ہر رکن ایک بار لکھا جاتا ہے اور ترتیب اہم نہیں۔ ∈ کا مطلب \"کا رکن ہے\" اور ∉ کا مطلب \"کا رکن نہیں\" ہے۔"),
    "points": [T("Well defined: everyone agrees what is in it.", "واضح: سب متفق ہوں کہ اس میں کیا ہے۔"),
               T("Each element once; order doesn't matter.", "ہر رکن ایک بار؛ ترتیب اہم نہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_odds", "type": "apply", "skill": SKILL, "step": number_question(
     "r_odds",
     T("How many elements are in the set of odd numbers less than 10?", "10 سے چھوٹے طاق اعداد کے سیٹ میں کتنے رکن ہیں؟"),
     R1,
     T("{1, 3, …}", "{1, 3, …}"),
     T("Right! {1, 3, 5, 7, 9} has 5.", "درست! {1, 3, 5, 7, 9} کے 5 رکن ہیں۔"),
     T("1, 3, 5, 7, 9: 5 elements.", "1، 3، 5، 7، 9: پانچ رکن"),
     common_wrong=[wrong(4, "Don't forget 1: {1, 3, 5, 7, 9} has 5.", "1 کو نہ بھولیں: {1, 3, 5, 7, 9} کے 5 رکن ہیں۔")],
     qtype=None)},
   {"id": "r_ball", "type": "apply", "skill": SKILL, "step": number_question(
     "r_ball",
     T("How many elements are in the set of letters of the word BALL?", "لفظ BALL کے حروف کے سیٹ میں کتنے رکن ہیں؟"),
     R2,
     T("L repeats. Write it once.", "L دہرایا گیا ہے۔ اسے ایک بار لکھیں۔"),
     T("Right! {B, A, L} has 3.", "درست! {B, A, L} کے 3 رکن ہیں۔"),
     T("B, A, L: 3 elements.", "B، A، L: تین رکن"),
     common_wrong=[wrong(4, "L repeats, so it is written once: {B, A, L}, 3 elements.", "L دہرایا گیا ہے، تو ایک بار لکھا جاتا ہے: {B, A, L}، تین رکن", "repeats")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Sets unit. No textbook text or exercises were used.",
   "Sets of letters use English words (PAKISTAN, LAHORE) so the braces notation reads the same in both languages.",
   "Urdu terms to check: سیٹ (set), رکن (element), واضح طور پر بیان کردہ (well defined), حروفِ علت (vowels).",
   "The numbers were worked out in content/sources/g6-maths-01/what_is_a_set.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import attach, oval_figure, letter_tiles, number_line, en_list, ur_list, ordered

TEAM = list(range(1, 12))          # shirt numbers of a cricket team (the hook)
VOWELS = list("aeiou")
assert len(set(VOWELS)) == S4
OUT8 = 4                           # s8: 4 is not in A
assert OUT8 not in A8
SUMMARY = [2, 4, 6]
SUMMARY_OUT = 5
assert SUMMARY_OUT not in SUMMARY


def word_tiles(word):
    return letter_tiles(word,
        f"Tiles with the letters of the word {word}, one tile for each letter in order: {en_list(list(word))}.",
        f"لفظ {word} کے حروف کی ٹائلیں، ہر حرف کی ایک ٹائل ترتیب سے: {ur_list(list(word))}۔")


attach(lesson, {
    "s1_hook": oval_figure(TEAM,
        f"An oval holding the shirt numbers {TEAM[0]} to {TEAM[-1]} of the players in a cricket team.",
        f"ایک بیضوی شکل جس میں کرکٹ ٹیم کے کھلاڑیوں کی قمیضوں کے نمبر {TEAM[0]} سے {TEAM[-1]} تک ہیں۔"),
    "s3_set": oval_figure(VOWELS,
        f"An oval named V holding the vowels {en_list(VOWELS)}, each written once. V stands for the set of vowels.",
        f"V نام کی بیضوی شکل جس میں حروفِ علت {ur_list(VOWELS)} ہیں، ہر ایک ایک بار لکھا ہے۔ V حروفِ علت کا سیٹ ہے۔", name="V"),
    "s6_evens": number_line(1, 11,
        "A number line with the whole numbers from 1 to 11 written under it.",
        "ایک عددی لکیر جس کے نیچے 1 سے 11 تک کے مکمل اعداد لکھے ہیں۔"),
    "s7_pakistan": word_tiles("PAKISTAN"),
    "s8_signs": oval_figure(ordered(A8),
        f"An oval named A holding {en_list(ordered(A8))}. The number {OUT8} is written outside the oval.",
        f"A نام کی بیضوی شکل جس میں {ur_list(ordered(A8))} ہیں۔ عدد {OUT8} بیضوی شکل سے باہر لکھا ہے۔",
        name="A", outside=[OUT8]),
    "s9_find_error": word_tiles("APPLE"),
    "s12_summary": oval_figure(SUMMARY,
        f"An oval named A holding {en_list(SUMMARY)}, each written once. The number {SUMMARY_OUT} is outside the oval, so it is not an element of A.",
        f"A نام کی بیضوی شکل جس میں {ur_list(SUMMARY)} ہیں، ہر ایک ایک بار۔ عدد {SUMMARY_OUT} بیضوی شکل سے باہر ہے، اس لیے یہ A کا رکن نہیں۔",
        name="A", outside=[SUMMARY_OUT]),
    "qb_apply": word_tiles("LAHORE"),
    "r_odds": number_line(1, 9,
        "A number line with the whole numbers from 1 to 9 written under it.",
        "ایک عددی لکیر جس کے نیچے 1 سے 9 تک کے مکمل اعداد لکھے ہیں۔"),
    "r_ball": word_tiles("BALL"),
})
write(lesson)

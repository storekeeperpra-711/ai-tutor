from itertools import combinations

from common import (T, opt, say, wrong, number_question, write,
                    REF, REVIEW, SET_MEANING, SET_KINDS, SET_SUBSETS,
                    SET_UNION_INTERSECTION, SET_WORD_PROBLEMS)

SKILL = SET_WORD_PROBLEMS


def at_least_one(a, b, both):
    return a + b - both


# s2: n({1, 2} ∪ {2, 3})
S2 = len({1, 2} | {2, 3})
assert S2 == 3
# s4, s5: 20 cricket, 15 hockey, 8 both
S4 = at_least_one(20, 15, 8)
S5 = 20 - 8
assert S4 == 27 and S5 == 12
# s6: class of 40; 25 cricket, 18 hockey, 10 both -> neither
S6 = 40 - at_least_one(25, 18, 10)
assert S6 == 7
# s7: 50 people, 32 Punjabi, 28 Urdu, everyone speaks at least one -> both
S7 = 32 + 28 - 50
assert S7 == 10 and at_least_one(32, 28, S7) == 50
# s8: 12 only milk, 9 only bread, 5 both -> customers
S8 = 12 + 9 + 5
assert S8 == 26
# s9: 22 mangoes, 15 apples, 7 both -> 30, not 37
assert at_least_one(22, 15, 7) == 30
# unit test
U1 = len(set("KARACHI"))
assert U1 == 6
U2 = 0  # days of the week that start with Z
assert not [d for d in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] if d.startswith("Z")]
U3 = len([c for r in range(4) for c in combinations([1, 2, 3], r)])
assert U3 == 8
U4 = len({2, 4, 6} | {4, 8})
assert U4 == 4
U5 = at_least_one(18, 12, 5)
assert U5 == 25
# question bank and review
QB = at_least_one(14, 10, 4)
assert QB == 20
R1 = 15 - 6
assert R1 == 9
R2 = 35 - at_least_one(20, 12, 5)
assert R2 == 8

lesson = {
 "id": "g6-maths-01-set-word-problems",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Solve problems about two overlapping groups using union and intersection (Venn diagram thinking).", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Set word problems", "سیٹ کے عملی سوال"),
 "estimated_minutes": 18,
 "prerequisites": [{"skill": SET_UNION_INTERSECTION}, {"skill": SET_SUBSETS}, {"skill": SET_KINDS}, {"skill": SET_MEANING}],
 "misconceptions": [
   {"id": "adds_both_twice", "description": "Adds the two groups without taking away the children counted in both."},
   {"id": "only_vs_all", "description": "Gives everyone in a group when the question asks for \"only\" that group."},
   {"id": "forgets_neither", "description": "Forgets that some people may be in neither group."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_rule", "type": "recall", "step": {
     "id": "qb_rule", "type": "choice",
     "prompt": T("To find how many are in at least one of two groups, you…", "یہ معلوم کرنے کے لیے کہ دو گروہوں میں سے کم از کم ایک میں کتنے ہیں، آپ…"),
     "options": [
       opt("minus_both", "add the two groups, then take away those in both", "دونوں گروہ جمع کریں، پھر دونوں میں شامل نکال دیں", True,
           "Yes! Otherwise the \"both\" people are counted twice.", "جی ہاں! ورنہ \"دونوں\" والے دو بار گنے جاتے ہیں۔"),
       opt("add", "just add the two groups", "بس دونوں گروہ جمع کریں", False,
           "Then the people in both groups are counted twice. Take them away once.", "پھر دونوں گروہوں والے دو بار گنے جاتے ہیں۔ انہیں ایک بار نکالیں۔", "adds_both_twice"),
       opt("bigger", "take the bigger group", "بڑا گروہ لیں", False,
           "Add the groups and take away those in both.", "گروہ جمع کریں اور دونوں والے نکالیں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("14 children like kites, 10 like marbles, and 4 like both. How many like at least one of them?", "14 بچوں کو پتنگ پسند ہے، 10 کو کنچے، اور 4 کو دونوں۔ کتنے بچوں کو کم از کم ایک پسند ہے؟"),
     QB,
     T("14 + 10, then take away the 4 counted twice.", "14 + 10، پھر دو بار گنے گئے 4 نکالیں۔"),
     T("Right! 20.", "درست! 20"),
     T("14 + 10 − 4 = 20.", "14 + 10 − 4 = 20"),
     common_wrong=[wrong(24, "The 4 who like both were counted twice: 24 − 4 = 20.", "دونوں پسند کرنے والے 4 دو بار گنے گئے: 24 − 4 = 20", "adds_both_twice")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("15 children play ludo and 6 of them also play carrom. Imran says 15 play only ludo. What is wrong?", "15 بچے لڈو کھیلتے ہیں اور ان میں سے 6 کیرم بھی کھیلتے ہیں۔ عمران کہتا ہے 15 صرف لڈو کھیلتے ہیں۔ کیا غلطی ہے؟"),
     "options": [
       opt("minus", "6 of the 15 also play carrom, so only ludo is 15 − 6 = 9.", "15 میں سے 6 کیرم بھی کھیلتے ہیں، تو صرف لڈو 15 − 6 = 9", True,
           "Yes! \"Only\" leaves out the ones in both.", "جی ہاں! \"صرف\" میں دونوں والے شامل نہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "6 of them play carrom too. Only ludo: 15 − 6 = 9.", "ان میں سے 6 کیرم بھی کھیلتے ہیں۔ صرف لڈو: 15 − 6 = 9", "only_vs_all"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_atleast", "front": T("In at least one group?", "کم از کم ایک گروہ میں؟"),
    "back": T("A + B − both. 20 + 15 − 8 = 27.", "A + B − دونوں۔ 20 + 15 − 8 = 27")},
   {"id": "f_only", "front": T("Only in group A?", "صرف گروہ A میں؟"),
    "back": T("A − both. Neither: total − at least one.", "A − دونوں۔ کسی میں نہیں: کل − کم از کم ایک")},
 ],
 "home_tasks": [{"id": "h_survey", "text": T(
   "Ask 10 people at home or in your street: do you like tea? do you like lassi? Count how many like tea, how many like lassi, and how many like both. Check that tea + lassi − both + neither = 10.",
   "گھر یا گلی میں 10 لوگوں سے پوچھیں: کیا آپ کو چائے پسند ہے؟ لسی؟ گنیں کتنوں کو چائے، کتنوں کو لسی اور کتنوں کو دونوں پسند ہیں۔ جانچیں کہ چائے + لسی − دونوں + کوئی نہیں = 10")}],
 "glossary": [T("At least one", "کم از کم ایک"), T("Both", "دونوں"), T("Only", "صرف"), T("Neither", "کوئی بھی نہیں")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "20 children like cricket, 15 like hockey. Are there 35 children? Not if some like both!",
                     "20 بچوں کو کرکٹ پسند ہے، 15 کو ہاکی۔ کیا بچے 35 ہیں؟ نہیں، اگر کچھ کو دونوں پسند ہوں!"),
    "text": T("Today we use sets to solve real problems about groups. First, a quick check.", "آج ہم سیٹوں سے گروہوں کے اصل سوال حل کریں گے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many elements are in {1, 2} ∪ {2, 3}?", "{1, 2} ∪ {2, 3} میں کتنے رکن ہیں؟"),
     S2,
     T("2 is in both; write it once.", "2 دونوں میں ہے؛ اسے ایک بار لکھیں۔"),
     T("Right! {1, 2, 3}: 3.", "درست! {1, 2, 3}: تین"),
     T("{1, 2, 3}: 3 elements.", "{1, 2, 3}: تین رکن"),
     common_wrong=[wrong(4, "2 is counted twice. The union is {1, 2, 3}: 3.", "2 دو بار گنا گیا۔ اجتماع {1, 2, 3} ہے: 3")],
     qtype="recall", skill=SET_UNION_INTERSECTION),
   {"id": "s3_venn", "type": "explain",
    "character": say("thinking", "Picture two circles that overlap. The overlap holds the children in both groups.", "دو دائرے سوچیں جو ایک دوسرے پر چڑھے ہوں۔ درمیانی حصے میں دونوں گروہوں والے بچے ہیں۔"),
    "text": T("Draw two overlapping circles (a Venn diagram), one for each group. The overlap is the intersection: people in both. In at least one group = A + B − both, because adding counts the overlap twice. Only A = A − both. Neither = total − (at least one).",
              "دو ایک دوسرے پر چڑھے دائرے بنائیں (وین ڈایاگرام)، ہر گروہ کے لیے ایک۔ درمیانی حصہ تقاطع ہے: دونوں میں شامل لوگ۔ کم از کم ایک گروہ میں = A + B − دونوں، کیونکہ جمع کرنے سے درمیانی حصہ دو بار گنا جاتا ہے۔ صرف A = A − دونوں۔ کسی میں نہیں = کل − (کم از کم ایک)۔")},
   number_question(
     "s4_at_least_one",
     T("In a class, 20 children like cricket, 15 like hockey, and 8 like both. How many like at least one of the two games?", "ایک کلاس میں 20 بچوں کو کرکٹ پسند ہے، 15 کو ہاکی، اور 8 کو دونوں۔ کتنے بچوں کو کم از کم ایک کھیل پسند ہے؟"),
     S4,
     T("20 + 15 counts the 8 twice. Take them away once.", "20 + 15 میں 8 دو بار گنے گئے۔ انہیں ایک بار نکالیں۔"),
     T("Right! 27.", "درست! 27"),
     T("20 + 15 − 8 = 27.", "20 + 15 − 8 = 27"),
     common_wrong=[wrong(35, "The 8 who like both were counted twice: 35 − 8 = 27.", "دونوں پسند کرنے والے 8 دو بار گنے گئے: 35 − 8 = 27", "adds_both_twice"),
                   wrong(19, "Take the 8 away once, not twice: 20 + 15 − 8 = 27.", "8 کو ایک بار نکالیں، دو بار نہیں: 20 + 15 − 8 = 27")]),
   number_question(
     "s5_only",
     T("In the same class (20 cricket, 15 hockey, 8 both), how many like only cricket?", "اسی کلاس میں (20 کرکٹ، 15 ہاکی، 8 دونوں)، کتنوں کو صرف کرکٹ پسند ہے؟"),
     S5,
     T("Take the 8 who like both out of the cricket group.", "کرکٹ والوں میں سے دونوں پسند کرنے والے 8 نکالیں۔"),
     T("Right! 12.", "درست! 12"),
     T("20 − 8 = 12.", "20 − 8 = 12"),
     common_wrong=[wrong(20, "20 includes the 8 who also like hockey. Only cricket: 20 − 8 = 12.", "20 میں وہ 8 بھی ہیں جنہیں ہاکی بھی پسند ہے۔ صرف کرکٹ: 20 − 8 = 12", "only_vs_all")]),
   number_question(
     "s6_neither",
     T("A class has 40 children. 25 play cricket, 18 play hockey, and 10 play both. How many play neither game?", "ایک کلاس میں 40 بچے ہیں۔ 25 کرکٹ کھیلتے ہیں، 18 ہاکی، اور 10 دونوں۔ کتنے بچے کوئی بھی کھیل نہیں کھیلتے؟"),
     S6,
     T("First find how many play at least one: 25 + 18 − 10.", "پہلے کم از کم ایک کھیلنے والے نکالیں: 25 + 18 − 10"),
     T("Right! 40 − 33 = 7.", "درست! 40 − 33 = 7"),
     T("25 + 18 − 10 = 33 play at least one, so 40 − 33 = 7 play neither.", "25 + 18 − 10 = 33 کم از کم ایک کھیلتے ہیں، تو 40 − 33 = 7 کوئی نہیں کھیلتے۔"),
     common_wrong=[wrong(33, "33 play at least one game. Neither: 40 − 33 = 7.", "33 کم از کم ایک کھیل کھیلتے ہیں۔ کوئی نہیں: 40 − 33 = 7", "forgets_neither"),
                   wrong(0, "25 + 18 counts the 10 twice. 33 play, so 7 play neither.", "25 + 18 میں 10 دو بار گنے گئے۔ 33 کھیلتے ہیں، تو 7 کوئی نہیں کھیلتے۔", "adds_both_twice")]),
   number_question(
     "s7_both",
     T("At a village meeting there are 50 people. 32 speak Punjabi, 28 speak Urdu, and everyone speaks at least one. How many speak both?", "گاؤں کی ایک بیٹھک میں 50 لوگ ہیں۔ 32 پنجابی بولتے ہیں، 28 اردو، اور ہر کوئی کم از کم ایک بولتا ہے۔ کتنے لوگ دونوں بولتے ہیں؟"),
     S7,
     T("32 + 28 = 60, but there are only 50 people. Who was counted twice?", "32 + 28 = 60، لیکن لوگ صرف 50 ہیں۔ کون دو بار گنا گیا؟"),
     T("Right! 10 speak both.", "درست! 10 دونوں بولتے ہیں۔"),
     T("60 − 50 = 10 people were counted twice: they speak both.", "60 − 50 = 10 لوگ دو بار گنے گئے: وہ دونوں بولتے ہیں۔"),
     common_wrong=[wrong(60, "60 is more than the 50 people! The extra 10 speak both.", "60 تو 50 لوگوں سے زیادہ ہے! زائد 10 دونوں بولتے ہیں۔", "adds_both_twice"),
                   wrong(4, "32 − 28 doesn't help here. 32 + 28 − 50 = 10.", "32 − 28 یہاں کام نہیں آتا۔ 32 + 28 − 50 = 10")]),
   number_question(
     "s8_customers",
     T("At a shop, 12 customers bought only milk, 9 bought only bread, and 5 bought both. How many customers were there?", "ایک دکان پر 12 گاہکوں نے صرف دودھ خریدا، 9 نے صرف ڈبل روٹی، اور 5 نے دونوں۔ کل کتنے گاہک تھے؟"),
     S8,
     T("\"Only\" groups don't overlap, so add all three parts.", "\"صرف\" والے گروہ ایک دوسرے میں نہیں، تو تینوں حصے جمع کریں۔"),
     T("Right! 26 customers.", "درست! 26 گاہک"),
     T("12 + 9 + 5 = 26.", "12 + 9 + 5 = 26"),
     common_wrong=[wrong(21, "The 5 who bought both are customers too: 12 + 9 + 5 = 26.", "دونوں خریدنے والے 5 بھی گاہک ہیں: 12 + 9 + 5 = 26"),
                   wrong(16, "Here the groups are \"only\", so nothing is counted twice. Add all three: 26.", "یہاں گروہ \"صرف\" ہیں، تو کچھ دو بار نہیں گنا گیا۔ تینوں جمع کریں: 26")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("22 children like mangoes, 15 like apples, and 7 like both. Ayesha says 37 children like at least one. What went wrong?", "22 بچوں کو آم پسند ہیں، 15 کو سیب، اور 7 کو دونوں۔ عائشہ کہتی ہے 37 بچوں کو کم از کم ایک پسند ہے۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("twice", "She counted the 7 twice. It is 22 + 15 − 7 = 30.", "اس نے 7 کو دو بار گنا۔ یہ 22 + 15 − 7 = 30 ہے۔", True,
          "Yes! The overlap must only be counted once.", "جی ہاں! درمیانی حصہ صرف ایک بار گنا جائے۔"),
      opt("add_seven", "She should add the 7: 44.", "اسے 7 جمع کرنا چاہیے: 44", False,
          "The 7 are already inside the 22 and the 15. Take them away once: 30.", "7 پہلے ہی 22 اور 15 میں شامل ہیں۔ انہیں ایک بار نکالیں: 30"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "The 7 who like both are in both groups, so they were counted twice: 30.", "دونوں پسند کرنے والے 7 دونوں گروہوں میں ہیں، اس لیے دو بار گنے گئے: 30", "adds_both_twice"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "Why do we take away the children who like both, instead of just adding the two groups? Can you teach me?",
                     "ہم دونوں گروہ صرف جمع کرنے کے بجائے دونوں پسند کرنے والے بچے کیوں نکالتے ہیں؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is the number in at least one group A + B − both?", "اپنے الفاظ میں بتائیں: کم از کم ایک گروہ میں تعداد A + B − دونوں کیوں ہے؟"),
    "key_idea": "The children who are in both groups are counted once in A and again in B, so adding A + B counts them twice. Taking away the \"both\" number once leaves each child counted exactly once.",
    "levels": {
      "got_it": "Says the children in both groups are counted twice when adding, so they are taken away once.",
      "partly": "Says they are counted twice, or that we take them away, but not both.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["both", "overlap", "middle", "دونوں", "درمیان"],
      ["twice", "two times", "double", "دو بار"],
      ["once", "take away", "subtract", "ایک بار", "نکال", "نفی"]],
    "fallback_feedback": {
      "got_it": T("Well explained! The overlap is counted twice, so we take it away once.", "بہت خوب! درمیانی حصہ دو بار گنا جاتا ہے، اس لیے ایک بار نکالتے ہیں۔"),
      "partly": T("Good start! Now say how many times the \"both\" children are counted in A + B.", "اچھی شروعات! اب بتائیں A + B میں \"دونوں\" والے بچے کتنی بار گنے جاتے ہیں۔"),
      "not_yet": T("A child who likes cricket and hockey is in the 20 and also in the 15. How many times is that child counted in 20 + 15?", "جس بچے کو کرکٹ اور ہاکی دونوں پسند ہیں وہ 20 میں بھی ہے اور 15 میں بھی۔ 20 + 15 میں وہ کتنی بار گنا گیا؟")},
    "limit_per_day": 3, "max_attempts": 2},
   {"id": "s11_unit_test", "type": "explain",
    "character": say("encouraging", "Test time! Five questions from the whole Sets unit. You can do it!",
                     "ٹیسٹ کا وقت! سیٹ کے پورے باب سے پانچ سوال۔ آپ کر سکتے ہیں!"),
    "text": T("This short test has questions on writing sets, kinds of sets, subsets, union and a real-life problem. Take your time.",
              "اس چھوٹے ٹیسٹ میں سیٹ لکھنے، سیٹوں کی اقسام، ذیلی سیٹ، اجتماع اور ایک اصل زندگی کا سوال ہے۔ آرام سے کریں۔")},
   number_question(
     "u1_karachi",
     T("Test 1: How many elements are in the set of letters of the word KARACHI?", "ٹیسٹ 1: لفظ KARACHI کے حروف کے سیٹ میں کتنے رکن ہیں؟"),
     U1,
     T("A repeats. Write it once.", "A دہرایا گیا ہے۔ اسے ایک بار لکھیں۔"),
     T("Right! {K, A, R, C, H, I}: 6.", "درست! {K, A, R, C, H, I}: چھ"),
     T("K, A, R, C, H, I: 6 elements.", "K، A، R، C، H، I: چھ رکن"),
     common_wrong=[wrong(7, "The word has 7 letters, but A repeats: 6.", "لفظ میں 7 حروف ہیں، لیکن A دہرایا گیا ہے: 6")],
     qtype="recall", skill=SET_MEANING),
   number_question(
     "u2_empty",
     T("Test 2: How many elements are in the set of days of the week that start with the letter Z?", "ٹیسٹ 2: ہفتے کے ان دنوں کے سیٹ میں کتنے رکن ہیں جو انگریزی حرف Z سے شروع ہوتے ہیں؟"),
     U2,
     T("Does any day start with Z?", "کیا کوئی دن Z سے شروع ہوتا ہے؟"),
     T("Right! None: it is the empty set.", "درست! کوئی نہیں: یہ خالی سیٹ ہے۔"),
     T("No day starts with Z, so the set is { }: 0.", "کوئی دن Z سے شروع نہیں ہوتا، تو سیٹ { } ہے: صفر"),
     common_wrong=[wrong(7, "There are 7 days, but none starts with Z: 0.", "دن 7 ہیں، لیکن کوئی Z سے شروع نہیں ہوتا: 0")],
     qtype="apply", skill=SET_KINDS),
   number_question(
     "u3_subsets",
     T("Test 3: How many subsets does {1, 2, 3} have?", "ٹیسٹ 3: {1, 2, 3} کے کتنے ذیلی سیٹ ہیں؟"),
     U3,
     T("Count { } and the set itself too.", "{ } اور خود سیٹ بھی گنیں۔"),
     T("Right! 8.", "درست! 8"),
     T("2 × 2 × 2 = 8 subsets.", "2 × 2 × 2 = 8 ذیلی سیٹ"),
     common_wrong=[wrong(6, "Add { } and {1, 2, 3}: 8.", "{ } اور {1, 2, 3} شامل کریں: 8")],
     qtype="apply", skill=SET_SUBSETS),
   number_question(
     "u4_union",
     T("Test 4: How many elements are in {2, 4, 6} ∪ {4, 8}?", "ٹیسٹ 4: {2, 4, 6} ∪ {4, 8} میں کتنے رکن ہیں؟"),
     U4,
     T("4 is in both; write it once.", "4 دونوں میں ہے؛ اسے ایک بار لکھیں۔"),
     T("Right! {2, 4, 6, 8}: 4.", "درست! {2, 4, 6, 8}: چار"),
     T("{2, 4, 6, 8}: 4 elements.", "{2, 4, 6, 8}: چار رکن"),
     common_wrong=[wrong(5, "4 is counted twice. Write it once: 4 elements.", "4 دو بار گنا گیا۔ اسے ایک بار لکھیں: چار رکن")],
     qtype="apply", skill=SET_UNION_INTERSECTION),
   number_question(
     "u5_drinks",
     T("Test 5: 18 people like tea, 12 like lassi, and 5 like both. How many like at least one?", "ٹیسٹ 5: 18 لوگوں کو چائے پسند ہے، 12 کو لسی، اور 5 کو دونوں۔ کتنوں کو کم از کم ایک پسند ہے؟"),
     U5,
     T("18 + 12 − 5.", "18 + 12 − 5"),
     T("Right! 25.", "درست! 25"),
     T("18 + 12 − 5 = 25.", "18 + 12 − 5 = 25"),
     common_wrong=[wrong(30, "The 5 who like both were counted twice: 30 − 5 = 25.", "دونوں پسند کرنے والے 5 دو بار گنے گئے: 30 − 5 = 25", "adds_both_twice")],
     qtype="apply"),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "Sets unit complete! You can sort any group now.", "سیٹ کا باب مکمل! اب آپ کسی بھی گروہ کو ترتیب دے سکتے ہیں۔"),
    "text": T("For two overlapping groups, draw a Venn diagram. At least one group = A + B − both. Only A = A − both. Neither = total − at least one. If \"only\" groups are given, they don't overlap, so just add them.",
              "دو ایک دوسرے پر چڑھے گروہوں کے لیے وین ڈایاگرام بنائیں۔ کم از کم ایک گروہ = A + B − دونوں۔ صرف A = A − دونوں۔ کسی میں نہیں = کل − کم از کم ایک۔ اگر \"صرف\" والے گروہ دیے ہوں تو وہ ایک دوسرے میں نہیں، بس جمع کریں۔"),
    "points": [T("At least one: A + B − both.", "کم از کم ایک: A + B − دونوں۔"),
               T("Read \"only\" and \"neither\" carefully.", "\"صرف\" اور \"کسی میں نہیں\" غور سے پڑھیں۔")]},
 ],
 "review_questions": [
   {"id": "r_only", "type": "apply", "skill": SKILL, "step": number_question(
     "r_only",
     T("15 children read Urdu stories and 6 of them also read English stories. How many read only Urdu stories?", "15 بچے اردو کہانیاں پڑھتے ہیں اور ان میں سے 6 انگریزی کہانیاں بھی پڑھتے ہیں۔ کتنے بچے صرف اردو کہانیاں پڑھتے ہیں؟"),
     R1,
     T("Take the 6 out of the 15.", "15 میں سے 6 نکالیں۔"),
     T("Right! 9.", "درست! 9"),
     T("15 − 6 = 9.", "15 − 6 = 9"),
     common_wrong=[wrong(15, "6 of them read English too. Only Urdu: 15 − 6 = 9.", "ان میں سے 6 انگریزی بھی پڑھتے ہیں۔ صرف اردو: 15 − 6 = 9", "only_vs_all")],
     qtype=None)},
   {"id": "r_neither", "type": "apply", "skill": SKILL, "step": number_question(
     "r_neither",
     T("A class has 35 children. 20 have a cat, 12 have a parrot, and 5 have both. How many have neither?", "ایک کلاس میں 35 بچے ہیں۔ 20 کے پاس بلی ہے، 12 کے پاس طوطا، اور 5 کے پاس دونوں۔ کتنوں کے پاس کوئی بھی نہیں؟"),
     R2,
     T("At least one: 20 + 12 − 5. Then take that from 35.", "کم از کم ایک: 20 + 12 − 5۔ پھر اسے 35 میں سے نکالیں۔"),
     T("Right! 35 − 27 = 8.", "درست! 35 − 27 = 8"),
     T("20 + 12 − 5 = 27, and 35 − 27 = 8.", "20 + 12 − 5 = 27، اور 35 − 27 = 8"),
     common_wrong=[wrong(27, "27 have at least one pet. Neither: 35 − 27 = 8.", "27 کے پاس کم از کم ایک ہے۔ کوئی نہیں: 35 − 27 = 8", "forgets_neither"),
                   wrong(3, "20 + 12 counts the 5 twice: 27 have a pet, so 8 have neither.", "20 + 12 میں 5 دو بار گنے گئے: 27 کے پاس ہے، تو 8 کے پاس کوئی نہیں۔", "adds_both_twice")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Sets unit. No textbook text or exercises were used.",
   "There are no pictures yet, so Venn diagrams are described in words; children can draw the two circles on paper. The five-question unit test at the end covers every lesson of the unit.",
   "Urdu terms to check: وین ڈایاگرام (Venn diagram), کم از کم ایک (at least one), کسی میں نہیں (neither).",
   "The numbers were worked out in content/sources/g6-maths-01/set_word_problems.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
# ---------- pictures ----------
from figs import attach, venn, letter_tiles, en_list, ur_list

# Each problem's numbers, checked against the answers worked out above.
C4, H4, B4 = 20, 15, 8                 # s1, s4, s5, s12: cricket, hockey, both
assert at_least_one(C4, H4, B4) == S4 and C4 - B4 == S5
T6, C6, H6, B6 = 40, 25, 18, 10        # s6
assert T6 - at_least_one(C6, H6, B6) == S6
T7, P7, U7 = 50, 32, 28                # s7: Punjabi, Urdu, everyone speaks one
assert at_least_one(P7, U7, S7) == T7
M8, B8, BOTH8 = 12, 9, 5               # s8: only milk, only bread, both
assert M8 + B8 + BOTH8 == S8
M9, A9, B9 = 22, 15, 7                 # s9: mangoes, apples, both
TEA, LASSI, TL = 18, 12, 5             # u5
assert at_least_one(TEA, LASSI, TL) == U5
K, MB, KM = 14, 10, 4                  # qb_apply: kites, marbles, both
assert at_least_one(K, MB, KM) == QB
LUDO, LC = 15, 6                       # qb_find_error
URDU, UE = 15, 6                       # r_only
assert URDU - UE == R1
T_R, CAT, PARROT, CP = 35, 20, 12, 5   # r_neither
assert T_R - at_least_one(CAT, PARROT, CP) == R2


def named(letter, n=None):
    return letter if n is None else f"{letter}={n}"


def problem(en, ur, a, b, *, a_only=(), both=(), b_only=(), outside=(), universe=None):
    return venn(en, ur, names=(named(*a), named(*b)), a_only=[str(x) for x in a_only],
                both=[str(x) for x in both], b_only=[str(x) for x in b_only],
                outside=[str(x) for x in outside],
                universe=None if universe is None else str(universe), check=False)


CH_EN = f"Two overlapping circles: C is the {C4} children who like cricket and H is the {H4} who like hockey, written C={C4} and H={H4}."
CH_UR = f"دو ایک دوسرے پر چڑھے دائرے: C کرکٹ پسند کرنے والے {C4} بچے اور H ہاکی پسند کرنے والے {H4} بچے ہیں، لکھا ہے C={C4} اور H={H4}۔"

attach(lesson, {
    "s1_hook": problem(CH_EN + " A question mark is in the overlap: how many like both?",
                       CH_UR + " درمیانی حصے میں سوالیہ نشان ہے: کتنے دونوں پسند کرتے ہیں؟",
                       ("C", C4), ("H", H4), both=["?"]),
    "s3_venn": venn(
        "A Venn diagram: a rectangle U round two overlapping circles A and B. The overlap, shaded, is the people in both groups.",
        "وین ڈایاگرام: دو ایک دوسرے پر چڑھے دائروں A اور B کے گرد مستطیل U۔ رنگا ہوا مشترک حصہ دونوں گروہوں والے لوگ ہیں۔",
        shade="both", universe="U"),
    "s4_at_least_one": problem(CH_EN + f" The overlap holds {B4}, the children who like both.",
                               CH_UR + f" درمیانی حصے میں {B4} ہیں، جو دونوں پسند کرتے ہیں۔",
                               ("C", C4), ("H", H4), both=[B4]),
    "s5_only": problem(CH_EN + f" The overlap holds {B4}. The part of C outside the overlap has a question mark.",
                       CH_UR + f" درمیانی حصے میں {B4} ہیں۔ C کا جو حصہ درمیان سے باہر ہے اس پر سوالیہ نشان ہے۔",
                       ("C", C4), ("H", H4), a_only=["?"], both=[B4]),
    "s6_neither": problem(
        f"A rectangle for the whole class of {T6}, with {T6} in its corner. Inside it two overlapping circles: C={C6} for cricket and H={H6} for hockey, with {B6} in the overlap. A question mark outside both circles stands for the children who play neither.",
        f"پوری جماعت کے {T6} بچوں کا مستطیل، کونے میں {T6} لکھا ہے۔ اس کے اندر دو ایک دوسرے پر چڑھے دائرے: کرکٹ کے لیے C={C6} اور ہاکی کے لیے H={H6}، درمیانی حصے میں {B6}۔ دونوں دائروں سے باہر سوالیہ نشان ان بچوں کے لیے ہے جو کوئی کھیل نہیں کھیلتے۔",
        ("C", C6), ("H", H6), both=[B6], outside=["?"], universe=T6),
    "s7_both": problem(
        f"A rectangle for all {T7} people, with {T7} in its corner. Inside it two overlapping circles: Pb={P7} for the people who speak Punjabi and Ur={U7} for those who speak Urdu. The overlap has a question mark. Nobody is outside the circles.",
        f"تمام {T7} لوگوں کا مستطیل، کونے میں {T7} لکھا ہے۔ اس کے اندر دو ایک دوسرے پر چڑھے دائرے: پنجابی بولنے والوں کے لیے Pb={P7} اور اردو بولنے والوں کے لیے Ur={U7}۔ درمیانی حصے پر سوالیہ نشان ہے۔ دائروں سے باہر کوئی نہیں۔",
        ("Pb", P7), ("Ur", U7), both=["?"], universe=T7),
    "s8_customers": problem(
        f"Two overlapping circles: M for the customers who bought milk and B for those who bought bread. Only M holds {M8}, the overlap holds {BOTH8}, and only B holds {B8}.",
        f"دو ایک دوسرے پر چڑھے دائرے: دودھ خریدنے والے گاہکوں کے لیے M اور ڈبل روٹی خریدنے والوں کے لیے B۔ صرف M والے حصے میں {M8}، درمیانی حصے میں {BOTH8} اور صرف B والے حصے میں {B8} ہیں۔",
        ("M",), ("B",), a_only=[M8], both=[BOTH8], b_only=[B8]),
    "s9_find_error": problem(
        f"Two overlapping circles: M={M9} for the children who like mangoes and A={A9} for those who like apples, with {B9} in the overlap.",
        f"دو ایک دوسرے پر چڑھے دائرے: آم پسند کرنے والے بچوں کے لیے M={M9} اور سیب پسند کرنے والوں کے لیے A={A9}، درمیانی حصے میں {B9}۔",
        ("M", M9), ("A", A9), both=[B9]),
    "u5_drinks": problem(
        f"Two overlapping circles: T={TEA} for the people who like tea and L={LASSI} for those who like lassi, with {TL} in the overlap.",
        f"دو ایک دوسرے پر چڑھے دائرے: چائے پسند کرنے والوں کے لیے T={TEA} اور لسی پسند کرنے والوں کے لیے L={LASSI}، درمیانی حصے میں {TL}۔",
        ("T", TEA), ("L", LASSI), both=[TL]),
    "s12_summary": problem(
        CH_EN + f" The overlap holds {B4} who like both. Only cricket is {C4} − {B4} = {C4 - B4}, written in C, and only hockey is {H4} − {B4} = {H4 - B4}, written in H. Together {C4 - B4} + {B4} + {H4 - B4} = {S4} like at least one.",
        CH_UR + f" درمیانی حصے میں {B4} ہیں جو دونوں پسند کرتے ہیں۔ صرف کرکٹ {C4} − {B4} = {C4 - B4} ہیں، جو C میں لکھے ہیں، اور صرف ہاکی {H4} − {B4} = {H4 - B4} ہیں، جو H میں لکھے ہیں۔ مل کر {C4 - B4} + {B4} + {H4 - B4} = {S4} کم از کم ایک پسند کرتے ہیں۔",
        ("C", C4), ("H", H4), a_only=[C4 - B4], both=[B4], b_only=[H4 - B4]),
    "qb_apply": problem(
        f"Two overlapping circles: K={K} for the children who like kites and M={MB} for those who like marbles, with {KM} in the overlap.",
        f"دو ایک دوسرے پر چڑھے دائرے: پتنگ پسند کرنے والے بچوں کے لیے K={K} اور کنچے پسند کرنے والوں کے لیے M={MB}، درمیانی حصے میں {KM}۔",
        ("K", K), ("M", MB), both=[KM]),
    "qb_find_error": problem(
        f"Two overlapping circles: L={LUDO} for the children who play ludo and C for those who play carrom, with {LC} in the overlap.",
        f"دو ایک دوسرے پر چڑھے دائرے: لڈو کھیلنے والے بچوں کے لیے L={LUDO} اور کیرم کھیلنے والوں کے لیے C، درمیانی حصے میں {LC}۔",
        ("L", LUDO), ("C",), both=[LC]),
    "r_only": problem(
        f"Two overlapping circles: Ur={URDU} for the children who read Urdu stories and En for those who read English stories, with {UE} in the overlap. The part of Ur outside the overlap has a question mark.",
        f"دو ایک دوسرے پر چڑھے دائرے: اردو کہانیاں پڑھنے والے بچوں کے لیے Ur={URDU} اور انگریزی کہانیاں پڑھنے والوں کے لیے En، درمیانی حصے میں {UE}۔ Ur کا جو حصہ درمیان سے باہر ہے اس پر سوالیہ نشان ہے۔",
        ("Ur", URDU), ("En",), a_only=["?"], both=[UE]),
    "r_neither": problem(
        f"A rectangle for the whole class of {T_R}, with {T_R} in its corner. Inside it two overlapping circles: C={CAT} for the children with a cat and P={PARROT} for those with a parrot, with {CP} in the overlap. A question mark outside both circles stands for the children with neither.",
        f"پوری جماعت کے {T_R} بچوں کا مستطیل، کونے میں {T_R} لکھا ہے۔ اس کے اندر دو ایک دوسرے پر چڑھے دائرے: بلی والے بچوں کے لیے C={CAT} اور طوطے والوں کے لیے P={PARROT}، درمیانی حصے میں {CP}۔ دونوں دائروں سے باہر سوالیہ نشان ان بچوں کے لیے ہے جن کے پاس دونوں میں سے کوئی نہیں۔",
        ("C", CAT), ("P", PARROT), both=[CP], outside=["?"], universe=T_R),
    "u1_karachi": letter_tiles("KARACHI",
        f"Tiles with the letters of the word KARACHI, one tile for each letter in order: {en_list(list('KARACHI'))}.",
        f"لفظ KARACHI کے حروف کی ٹائلیں، ہر حرف کی ایک ٹائل ترتیب سے: {ur_list(list('KARACHI'))}۔"),
})
write(lesson)

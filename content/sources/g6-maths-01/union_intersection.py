from common import (T, opt, say, wrong, number_question, write, show,
                    REF, REVIEW, SET_SUBSETS, SET_UNION_INTERSECTION)

SKILL = SET_UNION_INTERSECTION


def factors(n):
    return {d for d in range(1, n + 1) if n % d == 0}


# s2: subsets of {x}
S2 = 2
assert S2 == 2 ** len({"x"})
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# s4: n(A ∪ B)
S4 = len(A | B)
assert S4 == 6 and len(A) + len(B) == 8
# s5: n(A ∩ B)
S5 = len(A & B)
assert S5 == 2
# s6: {a, b, c} ∩ {c, d} = {c}
assert {"a", "b", "c"} & {"c", "d"} == {"c"}
# s7: common factors of 12 and 18
F = factors(12) & factors(18)
S7 = len(F)
assert F == {1, 2, 3, 6} and S7 == 4
# s8: evens and odds are disjoint
S8 = len({2, 4, 6} & {1, 3, 5})
assert S8 == 0
# s9: {1, 2} ∪ {2, 3} = {1, 2, 3}
assert {1, 2} | {2, 3} == {1, 2, 3}
# s11: evens and multiples of 3 below 10
E = {n for n in range(1, 10) if n % 2 == 0}
M = {n for n in range(1, 10) if n % 3 == 0}
S11 = len(E | M)
assert E == {2, 4, 6, 8} and M == {3, 6, 9} and S11 == 6
# question bank and review
QB = len({1, 3, 5} | {1, 2, 3})
assert QB == 4
R1 = len({"a", "b", "c"} | {"c", "d"})
assert R1 == 4
R2 = len({5, 10, 15} & {10, 20})
assert R2 == 1

lesson = {
 "id": "g6-maths-01-union-and-intersection",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Find the union and intersection of two sets, recognise disjoint sets, and count their elements.", "textbook": REF}],
 "skills": [SKILL],
 "title": T("Union and intersection", "اجتماع اور تقاطع"),
 "estimated_minutes": 15,
 "prerequisites": [{"skill": SET_SUBSETS}],
 "misconceptions": [
   {"id": "double_count", "description": "Counts the shared elements twice in a union."},
   {"id": "union_intersection_swap", "description": "Mixes up union (in either set) and intersection (in both sets)."},
   {"id": "disjoint_not_empty", "description": "Thinks two sets with nothing in common still share some element."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_meaning", "type": "recall", "step": {
     "id": "qb_meaning", "type": "choice",
     "prompt": T("What is A ∩ B?", "A ∩ B کیا ہے؟"),
     "options": [
       opt("both", "The elements that are in both A and B", "وہ رکن جو A اور B دونوں میں ہیں", True,
           "Yes! ∩ is the intersection: what they share.", "جی ہاں! ∩ تقاطع ہے: جو دونوں میں مشترک ہے۔"),
       opt("either", "All the elements in A or B", "A یا B کے تمام رکن", False,
           "That is the union, A ∪ B. ∩ means in both.", "یہ اجتماع A ∪ B ہے۔ ∩ کا مطلب دونوں میں۔", "union_intersection_swap"),
       opt("only_a", "The elements only in A", "صرف A کے رکن", False,
           "∩ means in both A and B.", "∩ کا مطلب A اور B دونوں میں۔"),
     ]}},
   {"id": "qb_apply", "type": "apply", "step": number_question(
     "qb_apply",
     T("How many elements are in {1, 3, 5} ∪ {1, 2, 3}?", "{1, 3, 5} ∪ {1, 2, 3} میں کتنے رکن ہیں؟"),
     QB,
     T("Write every element once: {1, 2, 3, 5}.", "ہر رکن ایک بار لکھیں: {1, 2, 3, 5}"),
     T("Right! {1, 2, 3, 5} has 4.", "درست! {1, 2, 3, 5} کے 4 رکن ہیں۔"),
     T("{1, 2, 3, 5}: 4 elements. 1 and 3 are written once.", "{1, 2, 3, 5}: چار رکن۔ 1 اور 3 ایک بار لکھے جاتے ہیں۔"),
     common_wrong=[wrong(6, "1 and 3 are in both sets, so count them once: 4.", "1 اور 3 دونوں سیٹوں میں ہیں، انہیں ایک بار گنیں: 4", "double_count"),
                   wrong(2, "That is the intersection. The union has every element: 4.", "یہ تقاطع ہے۔ اجتماع میں ہر رکن ہوتا ہے: 4", "union_intersection_swap")],
     qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": {
     "id": "qb_find_error", "type": "choice",
     "prompt": T("Nida says {2, 4} ∩ {1, 3} = {1, 2, 3, 4}. What is wrong?", "ندا کہتی ہے {2, 4} ∩ {1, 3} = {1, 2, 3, 4}۔ کیا غلطی ہے؟"),
     "options": [
       opt("empty", "She found the union. They share nothing, so the intersection is { }.", "اس نے اجتماع نکالا۔ ان میں کچھ مشترک نہیں، تو تقاطع { } ہے۔", True,
           "Yes! These sets are disjoint.", "جی ہاں! یہ سیٹ جدا جدا ہیں۔"),
       opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
           "∩ means in both. No number is in both sets: { }.", "∩ کا مطلب دونوں میں۔ کوئی عدد دونوں میں نہیں: { }", "union_intersection_swap"),
     ]}},
 ]},
 "flashcards": [
   {"id": "f_union", "front": T("A ∪ B (union)?", "A ∪ B (اجتماع)؟"),
    "back": T("Everything in A or B, each written once.", "A یا B میں سب کچھ، ہر رکن ایک بار۔")},
   {"id": "f_inter", "front": T("A ∩ B (intersection)?", "A ∩ B (تقاطع)؟"),
    "back": T("Only what is in both. If nothing, the sets are disjoint.", "صرف جو دونوں میں ہو۔ کچھ نہ ہو تو سیٹ جدا جدا ہیں۔")},
 ],
 "home_tasks": [{"id": "h_friends", "text": T(
   "Write the set of foods you like and ask a friend or sibling for theirs. Find the union (foods either of you likes) and the intersection (foods you both like).",
   "اپنی پسندیدہ کھانوں کا سیٹ لکھیں اور کسی دوست یا بہن بھائی سے ان کا سیٹ پوچھیں۔ اجتماع (جو کسی ایک کو پسند ہوں) اور تقاطع (جو دونوں کو پسند ہوں) نکالیں۔")}],
 "glossary": [T("Union ∪", "اجتماع ∪"), T("Intersection ∩", "تقاطع ∩"), T("Disjoint sets", "جدا جدا سیٹ"), T("Common", "مشترک")],
 "steps": [
   {"id": "s1_hook", "type": "explain",
    "character": say("curious", "Ali's team and Sara's team share two players. If both teams come to the match, how many players are there?",
                     "علی کی ٹیم اور سارہ کی ٹیم کے دو کھلاڑی مشترک ہیں۔ اگر دونوں ٹیمیں میچ پر آئیں تو کتنے کھلاڑی ہوں گے؟"),
    "text": T("Today we join sets together and find what they share. First, a quick check.", "آج ہم سیٹوں کو ملائیں گے اور دیکھیں گے ان میں کیا مشترک ہے۔ پہلے ایک چھوٹا سا سوال۔")},
   number_question(
     "s2_foundation",
     T("How many subsets does {x} have?", "{x} کے کتنے ذیلی سیٹ ہیں؟"),
     S2,
     T("Don't forget the empty set.", "خالی سیٹ کو نہ بھولیں۔"),
     T("Right! { } and {x}.", "درست! { } اور {x}"),
     T("{ } and {x}: 2 subsets.", "{ } اور {x}: دو ذیلی سیٹ"),
     common_wrong=[wrong(1, "The empty set counts too: { } and {x}, 2.", "خالی سیٹ بھی گنا جاتا ہے: { } اور {x}، دو")],
     qtype="recall", skill=SET_SUBSETS),
   {"id": "s3_union", "type": "explain",
    "character": say("happy", "Union joins everything together. Intersection keeps only what is shared!", "اجتماع سب کچھ ملا دیتا ہے۔ تقاطع صرف مشترک رکھتا ہے!"),
    "text": T(f"The union A ∪ B has every element that is in A or B (or both), each written once. The intersection A ∩ B has only the elements in both. For A = {show(A)} and B = {show(B)}: A ∪ B = {show(A | B)} and A ∩ B = {show(A & B)}. If two sets share nothing, their intersection is {{ }} and they are called disjoint.",
              f"اجتماع A ∪ B میں ہر وہ رکن ہے جو A یا B (یا دونوں) میں ہو، ہر ایک ایک بار۔ تقاطع A ∩ B میں صرف وہ رکن ہیں جو دونوں میں ہوں۔ A = {show(A)} اور B = {show(B)} کے لیے: A ∪ B = {show(A | B)} اور A ∩ B = {show(A & B)}۔ اگر دو سیٹوں میں کچھ مشترک نہ ہو تو ان کا تقاطع {{ }} ہے اور وہ جدا جدا سیٹ کہلاتے ہیں۔")},
   number_question(
     "s4_union",
     T(f"A = {show(A)}, B = {show(B)}. How many elements are in A ∪ B?", f"A = {show(A)}، B = {show(B)}۔ A ∪ B میں کتنے رکن ہیں؟"),
     S4,
     T("3 and 4 are in both sets. Write them once.", "3 اور 4 دونوں سیٹوں میں ہیں۔ انہیں ایک بار لکھیں۔"),
     T(f"Right! {show(A | B)} has 6.", f"درست! {show(A | B)} کے 6 رکن ہیں۔"),
     T(f"A ∪ B = {show(A | B)}: 6 elements.", f"A ∪ B = {show(A | B)}: چھ رکن"),
     common_wrong=[wrong(8, "4 + 4 counts 3 and 4 twice. Write them once: 6.", "4 + 4 میں 3 اور 4 دو بار گنے گئے۔ انہیں ایک بار لکھیں: 6", "double_count"),
                   wrong(2, "That is the intersection. The union has everything: 6.", "یہ تقاطع ہے۔ اجتماع میں سب کچھ ہے: 6", "union_intersection_swap")]),
   number_question(
     "s5_intersection",
     T(f"A = {show(A)}, B = {show(B)}. How many elements are in A ∩ B?", f"A = {show(A)}، B = {show(B)}۔ A ∩ B میں کتنے رکن ہیں؟"),
     S5,
     T("Which numbers are in both sets?", "کون سے اعداد دونوں سیٹوں میں ہیں؟"),
     T(f"Right! {show(A & B)}: 2.", f"درست! {show(A & B)}: دو"),
     T(f"A ∩ B = {show(A & B)}: 2 elements.", f"A ∩ B = {show(A & B)}: دو رکن"),
     common_wrong=[wrong(6, "That is the union. Only 3 and 4 are in both: 2.", "یہ اجتماع ہے۔ صرف 3 اور 4 دونوں میں ہیں: 2", "union_intersection_swap")]),
   {"id": "s6_letters", "type": "choice",
    "prompt": T("P = {a, b, c} and Q = {c, d}. What is P ∩ Q?", "P = {a, b, c} اور Q = {c, d}۔ P ∩ Q کیا ہے؟"),
    "options": [
      opt("c", "{c}", "{c}", True, "Yes! Only c is in both.", "جی ہاں! صرف c دونوں میں ہے۔"),
      opt("all", "{a, b, c, d}", "{a, b, c, d}", False, "That is P ∪ Q. ∩ keeps only what is in both: {c}.", "یہ P ∪ Q ہے۔ ∩ صرف دونوں میں موجود رکھتا ہے: {c}", "union_intersection_swap"),
      opt("abd", "{a, b, d}", "{a, b, d}", False, "These are the ones not shared. The shared one is c: {c}.", "یہ وہ ہیں جو مشترک نہیں۔ مشترک c ہے: {c}"),
    ]},
   number_question(
     "s7_factors",
     T("A is the set of factors of 12 and B is the set of factors of 18. How many elements are in A ∩ B?", "A، 12 کے اجزائے ضربی کا سیٹ ہے اور B، 18 کے اجزائے ضربی کا سیٹ۔ A ∩ B میں کتنے رکن ہیں؟"),
     S7,
     T("A = {1, 2, 3, 4, 6, 12}, B = {1, 2, 3, 6, 9, 18}. Which are in both?", "A = {1, 2, 3, 4, 6, 12}، B = {1, 2, 3, 6, 9, 18}۔ کون سے دونوں میں ہیں؟"),
     T(f"Right! {show(F)}: the common factors. The biggest, 6, is the HCF.", f"درست! {show(F)}: مشترک اجزائے ضربی۔ سب سے بڑا، 6، عاد اعظم ہے۔"),
     T(f"A ∩ B = {show(F)}: 4 elements.", f"A ∩ B = {show(F)}: چار رکن"),
     common_wrong=[wrong(6, "6 is the highest common factor. The common factors are {1, 2, 3, 6}: 4.", "6 عاد اعظم ہے۔ مشترک اجزائے ضربی {1, 2, 3, 6} ہیں: 4"),
                   wrong(12, "Count only the factors in both sets: {1, 2, 3, 6}, 4.", "صرف دونوں سیٹوں والے اجزائے ضربی گنیں: {1, 2, 3, 6}، چار", "double_count")]),
   number_question(
     "s8_disjoint",
     T("X = {2, 4, 6} and Y = {1, 3, 5}. How many elements are in X ∩ Y?", "X = {2, 4, 6} اور Y = {1, 3, 5}۔ X ∩ Y میں کتنے رکن ہیں؟"),
     S8,
     T("Is any number in both sets?", "کیا کوئی عدد دونوں سیٹوں میں ہے؟"),
     T("Right! None: X and Y are disjoint.", "درست! کوئی نہیں: X اور Y جدا جدا ہیں۔"),
     T("No number is both even and odd: X ∩ Y = { }, 0 elements.", "کوئی عدد جفت اور طاق دونوں نہیں: X ∩ Y = { }، صفر رکن"),
     common_wrong=[wrong(6, "That is the union. No number is in both: 0.", "یہ اجتماع ہے۔ کوئی عدد دونوں میں نہیں: 0", "union_intersection_swap"),
                   wrong(1, "Not even one number is in both sets: 0.", "ایک عدد بھی دونوں سیٹوں میں نہیں: 0", "disjoint_not_empty")]),
   {"id": "s9_find_error", "type": "choice", "question_type": "find_error",
    "prompt": T("Bilal writes {1, 2} ∪ {2, 3} = {1, 2, 2, 3}. What went wrong?", "بلال لکھتا ہے {1, 2} ∪ {2, 3} = {1, 2, 2, 3}۔ کیا غلطی ہوئی؟"),
    "options": [
      opt("once", "2 is written twice. The union is {1, 2, 3}.", "2 دو بار لکھا ہے۔ اجتماع {1, 2, 3} ہے۔", True,
          "Yes! Each element is written once, even in a union.", "جی ہاں! اجتماع میں بھی ہر رکن ایک بار لکھا جاتا ہے۔"),
      opt("two", "The union is {2}.", "اجتماع {2} ہے۔", False,
          "{2} is the intersection. The union is {1, 2, 3}.", "{2} تقاطع ہے۔ اجتماع {1, 2, 3} ہے۔", "union_intersection_swap"),
      opt("nothing", "Nothing.", "کوئی غلطی نہیں۔", False,
          "2 appears twice. In a set it is written once: {1, 2, 3}.", "2 دو بار ہے۔ سیٹ میں یہ ایک بار لکھا جاتا ہے: {1, 2, 3}", "double_count"),
    ]},
   {"id": "s10_explain_why", "type": "ai_explain", "question_type": "explain", "task_kind": "explain",
    "character": say("curious", "A has 4 elements and B has 4, but A ∪ B has only 6. Where did the other 2 go? Can you teach me?",
                     "A کے 4 رکن ہیں اور B کے 4، لیکن A ∪ B کے صرف 6۔ باقی 2 کہاں گئے؟ کیا آپ مجھے سکھا سکتے ہیں؟"),
    "task": T("In your own words: why is n(A ∪ B) sometimes less than n(A) + n(B)?", "اپنے الفاظ میں بتائیں: n(A ∪ B) کبھی کبھی n(A) + n(B) سے کم کیوں ہوتا ہے؟"),
    "key_idea": "Elements in both sets (the intersection) would be counted twice by adding, but in the union each is written only once. So n(A ∪ B) = n(A) + n(B) − n(A ∩ B).",
    "levels": {
      "got_it": "Says the shared elements (in both sets) would be counted twice, but the union lists them once.",
      "partly": "Mentions shared elements or writing once, without linking it to the count.",
      "not_yet": "Gives no reason."},
    "keywords": [
      ["both", "shared", "common", "intersection", "دونوں", "مشترک", "تقاطع"],
      ["twice", "two times", "double", "دو بار"],
      ["once", "one time", "ایک بار"]],
    "fallback_feedback": {
      "got_it": T("Well explained! Shared elements are only counted once in the union.", "بہت خوب! مشترک رکن اجتماع میں صرف ایک بار گنے جاتے ہیں۔"),
      "partly": T("Good start! Now say what happens to the shared elements when you add 4 + 4.", "اچھی شروعات! اب بتائیں 4 + 4 جمع کرنے پر مشترک رکنوں کا کیا ہوتا ہے۔"),
      "not_yet": T("3 and 4 are in A and also in B. How many times are they counted in 4 + 4? How many times in A ∪ B?", "3 اور 4، A میں بھی ہیں اور B میں بھی۔ 4 + 4 میں یہ کتنی بار گنے گئے؟ A ∪ B میں کتنی بار؟")},
    "limit_per_day": 3, "max_attempts": 2},
   number_question(
     "s11_evens_threes",
     T("E is the set of even numbers less than 10, and M is the set of multiples of 3 less than 10. How many elements are in E ∪ M?", "E، 10 سے چھوٹے جفت اعداد کا سیٹ ہے، اور M، 10 سے چھوٹے 3 کے اضعاف کا سیٹ۔ E ∪ M میں کتنے رکن ہیں؟"),
     S11,
     T(f"E = {show(E)}, M = {show(M)}. 6 is in both.", f"E = {show(E)}، M = {show(M)}۔ 6 دونوں میں ہے۔"),
     T(f"Right! {show(E | M)} has 6.", f"درست! {show(E | M)} کے 6 رکن ہیں۔"),
     T(f"E ∪ M = {show(E | M)}: 6 elements.", f"E ∪ M = {show(E | M)}: چھ رکن"),
     common_wrong=[wrong(7, "6 is in both sets; write it once: 6 elements.", "6 دونوں سیٹوں میں ہے؛ اسے ایک بار لکھیں: چھ رکن", "double_count"),
                   wrong(1, "That is E ∩ M = {6}. The union has 6 elements.", "یہ E ∩ M = {6} ہے۔ اجتماع کے 6 رکن ہیں۔", "union_intersection_swap")]),
   {"id": "s12_summary", "type": "summary",
    "character": say("celebrating", "You can join sets and find what they share!", "اب آپ سیٹ ملا سکتے ہیں اور مشترک ڈھونڈ سکتے ہیں!"),
    "text": T("Union A ∪ B: everything in A or B, each element once. Intersection A ∩ B: only what is in both. Disjoint sets share nothing, so their intersection is { }. Counting: n(A ∪ B) = n(A) + n(B) − n(A ∩ B).",
              "اجتماع A ∪ B: A یا B میں سب کچھ، ہر رکن ایک بار۔ تقاطع A ∩ B: صرف جو دونوں میں ہو۔ جدا جدا سیٹوں میں کچھ مشترک نہیں، تو ان کا تقاطع { } ہے۔ گنتی: n(A ∪ B) = n(A) + n(B) − n(A ∩ B)"),
    "points": [T("∪: in either. ∩: in both.", "∪: کسی ایک میں۔ ∩: دونوں میں۔"),
               T("Shared elements are written once.", "مشترک رکن ایک بار لکھے جاتے ہیں۔")]},
 ],
 "review_questions": [
   {"id": "r_union", "type": "apply", "skill": SKILL, "step": number_question(
     "r_union",
     T("How many elements are in {a, b, c} ∪ {c, d}?", "{a, b, c} ∪ {c, d} میں کتنے رکن ہیں؟"),
     R1,
     T("c is in both; write it once.", "c دونوں میں ہے؛ اسے ایک بار لکھیں۔"),
     T("Right! {a, b, c, d}: 4.", "درست! {a, b, c, d}: چار"),
     T("{a, b, c, d}: 4 elements.", "{a, b, c, d}: چار رکن"),
     common_wrong=[wrong(5, "c is counted twice. Write it once: 4.", "c دو بار گنا گیا۔ اسے ایک بار لکھیں: 4", "double_count")],
     qtype=None)},
   {"id": "r_inter", "type": "apply", "skill": SKILL, "step": number_question(
     "r_inter",
     T("How many elements are in {5, 10, 15} ∩ {10, 20}?", "{5, 10, 15} ∩ {10, 20} میں کتنے رکن ہیں؟"),
     R2,
     T("Which number is in both?", "کون سا عدد دونوں میں ہے؟"),
     T("Right! {10}: 1.", "درست! {10}: ایک"),
     T("Only 10 is in both: 1 element.", "صرف 10 دونوں میں ہے: ایک رکن"),
     common_wrong=[wrong(4, "That is the union. Only 10 is in both: 1.", "یہ اجتماع ہے۔ صرف 10 دونوں میں ہے: 1", "union_intersection_swap")],
     qtype=None)},
 ],
 "teacher_notes": [
   "Written fresh for the Sets unit. No textbook text or exercises were used.",
   "Step 7 links the intersection to common factors and the HCF from the Factors unit.",
   "Urdu terms to check: اجتماع (union), تقاطع (intersection), جدا جدا سیٹ (disjoint sets), عاد اعظم (HCF).",
   "The numbers were worked out in content/sources/g6-maths-01/union_intersection.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}
write(lesson)

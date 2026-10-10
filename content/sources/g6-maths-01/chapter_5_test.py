"""Chapter 5 test (Sets), set out like the book's review exercise and a board
paper: multiple choice, short questions, then longer problems. The questions
are new; only the kinds of question follow the book. (The book has no union,
intersection or set-builder form, so none is tested.)"""
from itertools import combinations
from common import (T, say, nq, sq, ch, write, show, book_ref, REVIEW, CHAPTER_5_TEST,
                    SET_MEANING, SET_KINDS, SET_SUBSETS, SET_UNION_INTERSECTION, SET_WORD_PROBLEMS, SET_VENN)
import figs

SKILL = CHAPTER_5_TEST


def mcq(id, en, ur, right, wrongs, pos):
    return ch(id, ("MCQ: " + en, "کثیر انتخابی: " + ur), right, wrongs, pos, qtype="exam_style")


def short(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Short question: " + en, "مختصر سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def long_q(id, en, ur, answer, hint, good, bad, wrongs=()):
    return nq(id, ("Long question: " + en, "تفصیلی سوال: " + ur), answer, hint, good, bad, wrongs, qtype="exam_style")


def primes_between(a, b):
    return [k for k in range(a + 1, b) if k > 1 and all(k % d for d in range(2, k))]


def n_subsets(n):
    return sum(1 for r in range(n + 1) for _ in combinations(range(n), r))


# MCQs
S2 = {10, 20, 30, 40}
assert 25 not in S2 and 20 in S2 and 40 in S2
M3 = primes_between(20, 40)
assert M3 == [23, 29, 31, 37]
M3_WRONG = [[21, 23, 29, 31, 37], [23, 29, 31, 37, 41], [23, 29, 31]]
assert all(w != M3 for w in M3_WRONG) and 21 % 3 == 0 and 41 > 40
M4 = len(set("BANANA"))
assert M4 == 3 and len("BANANA") == 6
M5_DAYS = {"January": 31, "February": 28}
assert [n for n in range(7, 8) if n > 7] == []                       # natural numbers between 7 and 8
assert [n for n in range(8, 9) if n % 2 == 0] == [8]                 # even numbers between 7 and 9
assert primes_between(7, 12) == [11]
M6 = n_subsets(4)
assert M6 == 16 and n_subsets(3) == 8 and M6 - 1 == 15
assert {"a", "b", "c"} == {"c", "b", "a"} and {"a", "b"} != {"a", "b", "c"} and {1, 2, 3} != {4, 5, 6} and set() != {0}
# m8: Venn picture, A inside B inside U
U8 = list(range(1, 13))
B8 = [n for n in U8 if n % 3 == 0]
A8 = [n for n in U8 if n % 6 == 0]
assert B8 == [3, 6, 9, 12] and A8 == [6, 12] and set(A8) < set(B8) and 3 not in A8 and 5 not in B8
alt_en8 = ("A rectangle U holds the numbers 1 to 12. Inside it a circle B holds 3, 6, 9 and 12, and a smaller circle A sits inside B holding 6 and 12. "
           "3 and 9 are in B but outside A. 1, 2, 4, 5, 7, 8, 10 and 11 are in the rectangle but outside B.")
alt_ur8 = ("ایک مستطیل U میں 1 سے 12 تک اعداد ہیں۔ اس کے اندر دائرہ B ہے جس میں 3، 6، 9 اور 12 ہیں، اور B کے اندر ایک چھوٹا دائرہ A ہے جس میں 6 اور 12 ہیں۔ "
           "3 اور 9 دائرہ B میں ہیں مگر A سے باہر۔ 1، 2، 4، 5، 7، 8، 10 اور 11 مستطیل کے اندر مگر B سے باہر ہیں۔")
FIG8 = figs.u_venn(alt_en8, alt_ur8, U8, [("A", A8), ("B", B8)], "nested")
# short questions
S1 = [n for n in range(1, 100) if n % 5 == 0 and 12 < n < 32]
assert S1 == [15, 20, 25, 30] and [n for n in range(1, 100) if n % 5 == 0 and 10 <= n <= 30] != S1
U_S2 = list(range(1, 16))
A_S2 = [n for n in U_S2 if n % 3 == 0]
S2_OUT = len(U_S2) - len(A_S2)
assert A_S2 == [3, 6, 9, 12, 15] and S2_OUT == 10 and len(A_S2) == 5
S3 = n_subsets(3) - 1
assert S3 == 7 and n_subsets(3) == 8
S4 = len(set("MISSISSIPPI"))
assert S4 == 4 and len("MISSISSIPPI") == 11
# s5: two separate circles, multiples of 4 and of 7 in 1..14
U5 = list(range(1, 15))
A5 = [n for n in U5 if n % 4 == 0]
B5 = [n for n in U5 if n % 7 == 0]
assert A5 == [4, 8, 12] and B5 == [7, 14] and not set(A5) & set(B5)
S5 = len([n for n in U5 if n not in A5 and n not in B5])
assert S5 == 9 and len(A5) + len(B5) == 5
alt_en5 = ("A rectangle U holds the numbers 1 to 14. Inside it are two separate circles: A holds 4, 8 and 12, and B holds 7 and 14. "
           "1, 2, 3, 5, 6, 9, 10, 11 and 13 are in the rectangle but outside both circles.")
alt_ur5 = ("ایک مستطیل U میں 1 سے 14 تک اعداد ہیں۔ اس کے اندر دو الگ دائرے ہیں: A میں 4، 8 اور 12 اور B میں 7 اور 14 ہیں۔ "
           "1، 2، 3، 5، 6، 9، 10، 11 اور 13 مستطیل کے اندر مگر دونوں دائروں سے باہر ہیں۔")
FIG5 = figs.u_venn(alt_en5, alt_ur5, U5, [("A", A5), ("B", B5)], "apart")
# long questions
L1 = len([c for c in combinations("abcd", 2)])
assert L1 == 6 and n_subsets(4) == 16
L2 = next(n for n in range(1, 20) if 2 ** n == 64)
assert L2 == 6 and 64 // 2 == 32
L3_A = [n for n in range(1, 40) if n % 3 == 0]
L3_B = set("ABRACADABRA")
L3 = len(L3_A) - len(L3_B)
assert len(L3_A) == 13 and len(L3_B) == 5 and L3 == 8 and len(L3_A) + len(L3_B) == 18
U4 = list(range(1, 31))
L4_A = [n for n in U4 if n % 4 == 0]
L4_B = [n for n in U4 if n % 9 == 0]
assert not set(L4_A) & set(L4_B) and len(L4_A) == 7 and len(L4_B) == 3
L4 = len(U4) - len(L4_A) - len(L4_B)
assert L4 == 20 and len(U4) - len(L4_A) == 23 and len(U4) - len(L4_B) == 27
# question bank
QB2 = len(set("BOOK"))
assert QB2 == 3
QB3 = n_subsets(5)
assert QB3 == 32 and n_subsets(4) == 16
# review
R1 = len([n for n in range(1, 10) if n % 2])
assert R1 == 5
R2 = n_subsets(2) - 1
assert R2 == 3

lesson = {
 "id": "g6-maths-01-chapter-5-test",
 "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
 "curriculum_refs": [{"outcome": "Answer exam-style questions on the whole of chapter 5: well-defined sets, the signs for belongs to and does not belong to, tabular and descriptive form, empty, singleton, finite and infinite sets, cardinal numbers, subsets, equal and equivalent sets, and Venn diagrams.",
                      "textbook": book_ref("Review Exercise 5")}],
 "skills": [SKILL],
 "title": T("Chapter 5 test: Sets", "باب 5 کا ٹیسٹ: سیٹ"),
 "estimated_minutes": 25,
 "prerequisites": [{"skill": s} for s in (SET_MEANING, SET_KINDS, SET_SUBSETS, SET_UNION_INTERSECTION, SET_WORD_PROBLEMS, SET_VENN)],
 "misconceptions": [
   {"id": "opinion_is_set", "description": "Thinks a collection decided by opinion (tasty, famous, kind) is a set."},
   {"id": "sign_swapped", "description": "Mixes up the signs for belongs to and does not belong to, or reads them the wrong way round."},
   {"id": "repeated_element", "description": "Counts or writes a repeated letter more than once."},
   {"id": "wrong_list", "description": "Lists numbers that do not fit the rule, or leaves some out."},
   {"id": "empty_or_one", "description": "Mixes up the empty set with a singleton set, or takes {0} as empty."},
   {"id": "forgets_empty_self", "description": "Leaves out the empty set or the set itself when counting the subsets."},
   {"id": "proper_count", "description": "Counts all the subsets as the proper subsets."},
   {"id": "equal_means_equivalent", "description": "Thinks sets with the same number of elements are equal."},
   {"id": "subset_apart", "description": "Reads or draws a subset the wrong way round, or apart from its bigger set."},
   {"id": "inside_count", "description": "Gives the number inside the circles when the number outside is asked, or the other way round."},
   {"id": "counts_universal", "description": "Gives the number of elements of U instead of the number asked for."},
   {"id": "stops_early", "description": "Finds a middle result but does not answer the question asked."},
 ],
 "mastery_criteria": {SKILL: {"question_types": ["exam_style"], "days": 2}},
 "question_bank": {SKILL: [
   {"id": "qb_exam_set", "type": "exam_style", "step": ch(
     "qb_exam_set", ("Which of these is a set (well defined)?", "ان میں سے کون سا سیٹ ہے (واضح طور پر بیان کردہ)؟"),
     ("The months of the year", "سال کے مہینے", "Correct: there are exactly twelve, and everyone agrees.", "درست: ٹھیک بارہ ہیں اور سب متفق ہیں۔"),
     [("The best months of the year", "سال کے سب سے اچھے مہینے", "\"Best\" is an opinion, so it is not a set.", "\"سب سے اچھے\" رائے ہے، اس لیے یہ سیٹ نہیں۔", "opinion_is_set"),
      ("The warm days of a year", "سال کے گرم دن", "How warm is warm? There is no fixed rule, so it is not a set.", "کتنا گرم گرم ہوتا ہے؟ کوئی مقررہ اصول نہیں، اس لیے یہ سیٹ نہیں۔", "opinion_is_set")],
     1, qtype=None)},
   {"id": "qb_exam_count", "type": "exam_style", "step": nq(
     "qb_exam_count", ("How many elements are in the set of the letters of the word \"BOOK\"?", "لفظ \"BOOK\" کے حروف کے سیٹ میں کتنے ارکان ہیں؟"), QB2,
     ("O appears twice. Write it once.", "O دو بار آتا ہے۔ اسے ایک بار لکھیں۔"),
     ("Correct: {B, O, K}: 3.", "درست: {B, O, K}: 3"),
     ("The word has 4 letters but O repeats, so the set has 3 elements.", "لفظ میں 4 حروف ہیں مگر O دہراتا ہے، اس لیے سیٹ کے 3 ارکان ہیں۔"),
     [(4, "That counts O twice. Count it once: 3.", "یہ O کو دو بار گنتا ہے۔ ایک بار گنیں: 3", "repeated_element")], qtype=None)},
   {"id": "qb_exam_subsets", "type": "exam_style", "step": nq(
     "qb_exam_subsets", ("How many subsets does a set with 5 elements have?", "5 ارکان والے سیٹ کے کتنے ذیلی سیٹ ہوتے ہیں؟"), QB3,
     ("Each element doubles the number of subsets: 2 × 2 × 2 × 2 × 2.", "ہر رکن ذیلی سیٹ کی تعداد دگنی کر دیتا ہے: 2 × 2 × 2 × 2 × 2"),
     ("Correct: 2⁵ = 32.", "درست: 2⁵ = 32"),
     ("2 × 2 × 2 × 2 × 2 = 32 subsets.", "2 × 2 × 2 × 2 × 2 = 32 ذیلی سیٹ۔"),
     [(16, "That is for 4 elements. One more element doubles it: 32.", "یہ 4 ارکان کے لیے ہے۔ ایک اور رکن اسے دگنا کر دیتا ہے: 32", "forgets_empty_self")], qtype=None)},
 ]},
 "home_tasks": [{"id": "h_paper", "text": T(
   "Do Review Exercise 5 in your maths book in your notebook, setting out the working the way this test's answers do. Ask your teacher to check it.",
   "اپنی ریاضی کی کتاب کی اعادی مشق 5 اپنی کاپی میں حل کریں، اور کام اس ٹیسٹ کے جوابات کی طرح لکھیں۔ اپنے استاد سے جانچ کروائیں۔")}],
 "glossary": [T("Multiple choice", "کثیر انتخابی"), T("Short question", "مختصر سوال"), T("Long question", "تفصیلی سوال"),
              T("Model answer", "نمونہ جواب"), T("Review exercise", "اعادی مشق")],
 "steps": [
   {"id": "s1_paper", "type": "explain",
    "character": say("encouraging", "This is a test of the whole chapter, like the book's review exercise. Read each question carefully!",
                     "یہ پورے باب کا ٹیسٹ ہے، کتاب کی اعادی مشق کی طرح۔ ہر سوال غور سے پڑھیں!"),
    "text": T("This test goes with Review Exercise 5 of your maths book (PCTB Mathematics 6). It has three parts, like an exam paper: multiple choice questions (choose one answer), short questions (a few lines of working), and longer problems (full working in your notebook). The questions are new, not the book's.",
              "یہ ٹیسٹ آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی اعادی مشق 5 کے ساتھ ہے۔ اس کے تین حصے ہیں، امتحانی پرچے کی طرح: کثیر انتخابی سوال (ایک جواب چنیں)، مختصر سوال (چند سطروں کا کام)، اور تفصیلی سوال (پورا کام اپنی کاپی میں)۔ سوال نئے ہیں، کتاب والے نہیں۔")},
   mcq("m1_set", "Which of these collections is a set?", "ان مجموعوں میں سے کون سا سیٹ ہے؟",
       ("The four provinces of Pakistan", "پاکستان کے چار صوبے", "Correct: it is well defined, and everyone agrees on the members.", "درست: یہ واضح طور پر بیان کردہ ہے اور ارکان پر سب متفق ہیں۔"),
       [("The famous cricketers of Pakistan", "پاکستان کے مشہور کرکٹ کھلاڑی", "\"Famous\" is an opinion, so it is not a set.", "\"مشہور\" رائے ہے، اس لیے یہ سیٹ نہیں۔", "opinion_is_set"),
        ("The tastiest dishes", "سب سے مزے دار کھانے", "\"Tastiest\" is an opinion, so it is not a set.", "\"سب سے مزے دار\" رائے ہے، اس لیے یہ سیٹ نہیں۔", "opinion_is_set"),
        ("The kind teachers of a school", "اسکول کے مہربان اساتذہ", "\"Kind\" has no fixed rule, so it is not a set.", "\"مہربان\" کا کوئی مقررہ اصول نہیں، اس لیے یہ سیٹ نہیں۔", "opinion_is_set")], 2),
   mcq("m2_belongs", "S = {10, 20, 30, 40}. Which statement is true?", "S = {10, 20, 30, 40}۔ کون سا بیان درست ہے؟",
       ("25 ∉ S", "25 ∉ S", "Correct: 25 is not listed in S.", "درست: 25 سیٹ S میں نہیں لکھا۔"),
       [("20 ∉ S", "20 ∉ S", "20 is listed in S, so 20 ∈ S.", "20 سیٹ S میں لکھا ہے، اس لیے 20 ∈ S۔", "sign_swapped"),
        ("25 ∈ S", "25 ∈ S", "25 is not listed in S, so 25 ∉ S.", "25 سیٹ S میں نہیں لکھا، اس لیے 25 ∉ S۔", "sign_swapped"),
        ("40 ∉ S", "40 ∉ S", "40 is the last element of S, so 40 ∈ S.", "40، S کا آخری رکن ہے، اس لیے 40 ∈ S۔", "sign_swapped")], 1),
   mcq("m3_tabular", "The tabular form of the set of prime numbers between 20 and 40 is:", "20 اور 40 کے درمیان مفرد اعداد کے سیٹ کی جدولی شکل ہے:",
       (show(M3), show(M3), "Correct: 23, 29, 31 and 37 are the primes between 20 and 40.", "درست: 23، 29، 31 اور 37، 20 اور 40 کے درمیان مفرد اعداد ہیں۔"),
       [(show(M3_WRONG[0]), show(M3_WRONG[0]), "21 = 3 × 7 is not prime.", "21 = 3 × 7 مفرد نہیں۔", "wrong_list"),
        (show(M3_WRONG[1]), show(M3_WRONG[1]), "41 is more than 40. Between 20 and 40 leaves it out.", "41، 40 سے بڑا ہے۔ 20 اور 40 کے درمیان میں یہ شامل نہیں۔", "wrong_list"),
        (show(M3_WRONG[2]), show(M3_WRONG[2]), "That leaves out 37, which is prime.", "اس میں 37 رہ گیا جو مفرد ہے۔", "wrong_list")], 0),
   mcq("m4_cardinal", "If A is the set of the letters of the word \"BANANA\", then n(A) is:", "اگر A لفظ \"BANANA\" کے حروف کا سیٹ ہے تو n(A) ہے:",
       ("3", "3", "Correct: A = {B, A, N}.", "درست: A = {B, A, N}"),
       [("6", "6", "That counts every letter. A set writes each letter once.", "یہ ہر حرف گنتا ہے۔ سیٹ ہر حرف ایک بار لکھتا ہے۔", "repeated_element"),
        ("2", "2", "A and N are two letters, but B is also in the word.", "A اور N دو حروف ہیں مگر B بھی لفظ میں ہے۔"),
        ("4", "4", "There are only three different letters: B, A, N.", "صرف تین مختلف حروف ہیں: B، A، N", "repeated_element")], 3),
   mcq("m5_empty", "Which of these is the empty set?", "ان میں سے کون سا خالی سیٹ ہے؟",
       ("The natural numbers between 7 and 8", "7 اور 8 کے درمیان قدرتی اعداد", "Correct: there is no whole number between 7 and 8.", "درست: 7 اور 8 کے درمیان کوئی مکمل عدد نہیں۔"),
       [("The set {0}", "سیٹ {0}", "{0} has one element, 0. The empty set has none.", "{0} کا ایک رکن ہے، 0۔ خالی سیٹ کا کوئی رکن نہیں۔", "empty_or_one"),
        ("The even numbers between 7 and 9", "7 اور 9 کے درمیان جفت اعداد", "8 is even and between 7 and 9. That is one element: {8}.", "8 جفت ہے اور 7 اور 9 کے درمیان ہے۔ یہ ایک رکن ہے: {8}", "empty_or_one"),
        ("The prime numbers between 7 and 12", "7 اور 12 کے درمیان مفرد اعداد", "11 is prime. That is one element: {11}.", "11 مفرد ہے۔ یہ ایک رکن ہے: {11}", "empty_or_one")], 2),
   mcq("m6_subsets", "A set has 4 elements. The number of its subsets is:", "ایک سیٹ کے 4 ارکان ہیں۔ اس کے ذیلی سیٹ کی تعداد ہے:",
       ("16", "16", "Correct: 2 × 2 × 2 × 2 = 16.", "درست: 2 × 2 × 2 × 2 = 16"),
       [("8", "8", "That is for 3 elements. With 4 elements double it: 16.", "یہ 3 ارکان کے لیے ہے۔ 4 ارکان کے لیے دگنا کریں: 16", "forgets_empty_self"),
        ("15", "15", "That is the number of proper subsets. The set itself counts too: 16.", "یہ حقیقی ذیلی سیٹ کی تعداد ہے۔ خود سیٹ بھی گنا جاتا ہے: 16", "proper_count"),
        ("4", "4", "That is the number of elements, not the number of subsets.", "یہ ارکان کی تعداد ہے، ذیلی سیٹ کی نہیں۔")], 1),
   mcq("m7_equal", "Which pair is a pair of equal sets?", "کون سا جوڑا برابر سیٹوں کا ہے؟",
       ("{a, b, c} and {c, b, a}", "{a, b, c} اور {c, b, a}", "Correct: the same elements, only in a different order.", "درست: ارکان وہی ہیں، صرف ترتیب مختلف ہے۔"),
       [("{a, b} and {a, b, c}", "{a, b} اور {a, b, c}", "The second set has c as well, so they are not equal.", "دوسرے سیٹ میں c بھی ہے، اس لیے یہ برابر نہیں۔", "subset_apart"),
        ("{1, 2, 3} and {4, 5, 6}", "{1, 2, 3} اور {4, 5, 6}", "They have the same number of elements, but different ones: equivalent, not equal.", "ان کے ارکان کی تعداد برابر ہے مگر ارکان مختلف: ہم قوت، برابر نہیں۔", "equal_means_equivalent"),
        ("{ } and {0}", "{ } اور {0}", "{ } has no element and {0} has one, so they are not equal.", "{ } کا کوئی رکن نہیں اور {0} کا ایک ہے، اس لیے یہ برابر نہیں۔", "empty_or_one")], 0),
   mcq("m8_venn", "Look at the Venn diagram. Which statement is true?", "وین ڈایاگرام دیکھیں۔ کون سا بیان درست ہے؟",
       ("A ⊂ B", "A ⊂ B", "Correct: circle A is inside circle B, so A is a proper subset of B.", "درست: دائرہ A، دائرہ B کے اندر ہے، اس لیے A، B کا حقیقی ذیلی سیٹ ہے۔"),
       [("B ⊂ A", "B ⊂ A", "B is the bigger circle. 3 and 9 are in B but not in A.", "B بڑا دائرہ ہے۔ 3 اور 9، B میں ہیں مگر A میں نہیں۔", "subset_apart"),
        ("3 ∈ A", "3 ∈ A", "3 is in circle B but outside circle A, so 3 ∉ A.", "3 دائرہ B میں ہے مگر دائرہ A سے باہر، اس لیے 3 ∉ A۔", "sign_swapped"),
        ("5 ∈ B", "5 ∈ B", "5 is in the rectangle but outside circle B, so 5 ∉ B.", "5 مستطیل میں ہے مگر دائرہ B سے باہر، اس لیے 5 ∉ B۔", "sign_swapped")], 0),
   {"id": "s_short", "type": "explain",
    "text": T("Short questions. Work each one out in your notebook, then type the answer.",
              "مختصر سوال۔ ہر ایک اپنی کاپی میں حل کریں، پھر جواب لکھیں۔")},
   sq("q1_tabular", ("Short question: Write the set of the multiples of 5 greater than 12 and less than 32 in tabular form (like {1, 2, 3}).", "مختصر سوال: 12 سے بڑے اور 32 سے چھوٹے 5 کے اضعاف کا سیٹ جدولی شکل میں لکھیں (جیسے {1, 2, 3})۔"), S1,
      ("List 15, 20, ... and stop before 32.", "15، 20، ... لکھیں اور 32 سے پہلے رک جائیں۔"),
      ("Correct: {15, 20, 25, 30}.", "درست: {15, 20, 25, 30}"),
      ("Model answer: the multiples of 5 after 12 are 15, 20, 25, 30 (35 is more than 32). So the set is {15, 20, 25, 30}.", "نمونہ جواب: 12 کے بعد 5 کے اضعاف 15، 20، 25، 30 ہیں (35، 32 سے بڑا ہے)۔ اس لیے سیٹ {15, 20, 25, 30} ہے۔"),
      [("{10, 15, 20, 25, 30}", "10 is not greater than 12. Start at 15: {15, 20, 25, 30}.", "10، 12 سے بڑا نہیں۔ 15 سے شروع کریں: {15, 20, 25, 30}", "wrong_list"),
       ("{15, 20, 25}", "That leaves out 30, which is less than 32: {15, 20, 25, 30}.", "اس میں 30 رہ گیا جو 32 سے چھوٹا ہے: {15, 20, 25, 30}", "wrong_list")], qtype="exam_style"),
   short("q2_outside", "U = {1, 2, 3, ..., 15} and A is the set of the multiples of 3 in U. In a Venn diagram, how many numbers are written inside the rectangle but outside circle A?", "U = {1, 2, 3, ..., 15} اور A، U کے 3 کے اضعاف کا سیٹ ہے۔ وین ڈایاگرام میں مستطیل کے اندر مگر دائرہ A کے باہر کتنے اعداد لکھے جائیں گے؟", S2_OUT,
      ("A = {3, 6, 9, 12, 15}. Take its numbers away from all 15.", "A = {3, 6, 9, 12, 15}۔ اس کے اعداد کل 15 میں سے نکالیں۔"),
      ("Correct: 15 − 5 = 10.", "درست: 15 − 5 = 10"),
      ("Model answer: A = {3, 6, 9, 12, 15} has 5 elements. 15 − 5 = 10 numbers are outside the circle.", "نمونہ جواب: A = {3, 6, 9, 12, 15} کے 5 ارکان ہیں۔ 15 − 5 = 10 اعداد دائرے کے باہر ہیں۔"),
      [(5, "That is the number inside the circle. Outside: 10.", "یہ دائرے کے اندر کی تعداد ہے۔ باہر: 10", "inside_count"),
       (15, "That is all of U. Take away the 5 inside the circle: 10.", "یہ سارا U ہے۔ دائرے کے اندر کے 5 نکالیں: 10", "counts_universal")]),
   short("q3_proper", "How many proper subsets does the set {x, y, z} have?", "سیٹ {x, y, z} کے کتنے حقیقی ذیلی سیٹ ہیں؟", S3,
      ("All subsets: 2 × 2 × 2. Take away the set itself.", "تمام ذیلی سیٹ: 2 × 2 × 2۔ خود سیٹ نکال دیں۔"),
      ("Correct: 8 − 1 = 7.", "درست: 8 − 1 = 7"),
      ("Model answer: 2³ = 8 subsets. The set itself is improper, so 8 − 1 = 7 are proper.", "نمونہ جواب: 2³ = 8 ذیلی سیٹ۔ خود سیٹ غیر حقیقی ہے، اس لیے 8 − 1 = 7 حقیقی ہیں۔"),
      [(8, "That is all the subsets. The set itself is not a proper subset: 7.", "یہ تمام ذیلی سیٹ ہیں۔ خود سیٹ حقیقی ذیلی سیٹ نہیں: 7", "proper_count"),
       (6, "That also leaves out the empty set, which is a proper subset: 7.", "اس میں خالی سیٹ بھی نکل گیا جو حقیقی ذیلی سیٹ ہے: 7", "forgets_empty_self")]),
   short("q4_letters", "How many elements has the set of the letters of the word \"MISSISSIPPI\"?", "لفظ \"MISSISSIPPI\" کے حروف کے سیٹ کے کتنے ارکان ہیں؟", S4,
      ("Write each different letter once.", "ہر مختلف حرف ایک بار لکھیں۔"),
      ("Correct: {M, I, S, P}: 4.", "درست: {M, I, S, P}: 4"),
      ("Model answer: the different letters are M, I, S, P, so the set has 4 elements.", "نمونہ جواب: مختلف حروف M، I، S، P ہیں، اس لیے سیٹ کے 4 ارکان ہیں۔"),
      [(11, "That counts every letter. A set writes each letter once: 4.", "یہ ہر حرف گنتا ہے۔ سیٹ ہر حرف ایک بار لکھتا ہے: 4", "repeated_element")]),
   short("q5_two_circles", "Look at the Venn diagram. How many numbers of U are outside both circles?", "وین ڈایاگرام دیکھیں۔ U کے کتنے اعداد دونوں دائروں سے باہر ہیں؟", S5,
      ("Count the numbers in the rectangle that are not inside A or B.", "مستطیل کے وہ اعداد گنیں جو A یا B کے اندر نہیں۔"),
      ("Correct: 14 − 3 − 2 = 9.", "درست: 14 − 3 − 2 = 9"),
      ("Model answer: A has 3 numbers and B has 2, so 14 − 3 − 2 = 9 numbers are outside both circles.", "نمونہ جواب: A میں 3 اور B میں 2 اعداد ہیں، اس لیے 14 − 3 − 2 = 9 اعداد دونوں دائروں سے باہر ہیں۔"),
      [(5, "That is the number inside the circles. Outside both: 9.", "یہ دائروں کے اندر کی تعداد ہے۔ دونوں سے باہر: 9", "inside_count"),
       (14, "That is all of U. Take away those inside the circles: 9.", "یہ سارا U ہے۔ دائروں کے اندر والے نکالیں: 9", "counts_universal")]),
   {"id": "s_long", "type": "explain",
    "text": T("Longer problems. Write full working in your notebook, then type the final answer.",
              "تفصیلی سوالات۔ اپنی کاپی میں پورا کام لکھیں، پھر آخری جواب لکھیں۔")},
   long_q("l1_pairs", "How many subsets of {a, b, c, d} have exactly 2 elements?", "{a, b, c, d} کے کتنے ذیلی سیٹ میں بالکل 2 ارکان ہیں؟", L1,
      ("List them in order: {a, b}, {a, c}, {a, d}, then those starting with b, then c.", "ترتیب سے لکھیں: {a, b}، {a, c}، {a, d}، پھر وہ جو b سے شروع ہوں، پھر c سے۔"),
      ("Correct: 3 + 2 + 1 = 6.", "درست: 3 + 2 + 1 = 6"),
      ("Model answer: {a, b}, {a, c}, {a, d}, {b, c}, {b, d}, {c, d}. That is 6 subsets. (Do not count {b, a}: it is the same set as {a, b}.)", "نمونہ جواب: {a, b}، {a, c}، {a, d}، {b, c}، {b, d}، {c, d}۔ یعنی 6 ذیلی سیٹ۔ ({b, a} نہ گنیں: یہ {a, b} ہی ہے۔)"),
      [(12, "That counts {a, b} and {b, a} as different. They are the same set: 6.", "یہ {a, b} اور {b, a} کو مختلف گنتا ہے۔ یہ ایک ہی سیٹ ہے: 6", "equal_means_equivalent"),
       (4, "That is the number of elements of the set, not the number of 2-element subsets: 6.", "یہ سیٹ کے ارکان کی تعداد ہے، 2 ارکان والے ذیلی سیٹ کی نہیں: 6", "stops_early")]),
   long_q("l2_reverse", "A set has 64 subsets. How many elements does it have?", "ایک سیٹ کے 64 ذیلی سیٹ ہیں۔ اس کے کتنے ارکان ہیں؟", L2,
      ("Double 1 again and again: 2, 4, 8 ... until you reach 64. Count the doublings.", "1 کو بار بار دگنا کریں: 2، 4، 8 ... جب تک 64 نہ آ جائے۔ دگنا کرنے کی تعداد گنیں۔"),
      ("Correct: 2⁶ = 64, so 6 elements.", "درست: 2⁶ = 64، اس لیے 6 ارکان"),
      ("Model answer: 2, 4, 8, 16, 32, 64 is six doublings, so 2⁶ = 64 and the set has 6 elements.", "نمونہ جواب: 2، 4، 8، 16، 32، 64 چھ بار دگنا کرنا ہے، اس لیے 2⁶ = 64 اور سیٹ کے 6 ارکان ہیں۔"),
      [(32, "That is half of 64, not the number of elements. Count the doublings: 6.", "یہ 64 کا نصف ہے، ارکان کی تعداد نہیں۔ دگنا کرنے کی تعداد گنیں: 6", "stops_early"),
       (7, "2⁷ = 128, which is too big. 2⁶ = 64: 6 elements.", "2⁷ = 128 بہت بڑا ہے۔ 2⁶ = 64: 6 ارکان", "forgets_empty_self")]),
   long_q("l3_cardinal", "A is the set of the multiples of 3 less than 40, and B is the set of the letters of the word \"ABRACADABRA\". How many more elements does A have than B?", "A، 40 سے چھوٹے 3 کے اضعاف کا سیٹ ہے، اور B لفظ \"ABRACADABRA\" کے حروف کا سیٹ ہے۔ A کے ارکان B سے کتنے زیادہ ہیں؟", L3,
      ("Find n(A) and n(B) first, then subtract. Write the repeated letters once.", "پہلے n(A) اور n(B) معلوم کریں، پھر گھٹائیں۔ دہرائے ہوئے حروف ایک بار لکھیں۔"),
      ("Correct: 13 − 5 = 8.", "درست: 13 − 5 = 8"),
      ("Model answer: A = {3, 6, ..., 39} has 13 elements. B = {A, B, R, C, D} has 5. 13 − 5 = 8.", "نمونہ جواب: A = {3, 6, ..., 39} کے 13 ارکان ہیں۔ B = {A, B, R, C, D} کے 5 ہیں۔ 13 − 5 = 8"),
      [(13, "That is n(A) only. Subtract n(B), which is 5: 8.", "یہ صرف n(A) ہے۔ n(B) یعنی 5 گھٹائیں: 8", "stops_early"),
       (18, "That adds them. \"How many more\" means subtract: 8.", "یہ انھیں جمع کرتا ہے۔ \"کتنے زیادہ\" کا مطلب ہے گھٹانا: 8", None),
       (2, "That counts all 11 letters of ABRACADABRA (13 − 11). B has 5 different letters: 8.", "یہ ABRACADABRA کے سارے 11 حروف گنتا ہے (13 − 11)۔ B کے 5 مختلف حروف ہیں: 8", "repeated_element")]),
   long_q("l4_venn", "U = {1, 2, 3, ..., 30}. P is the set of the multiples of 4 in U and Q is the set of the multiples of 9 in U. They have no number in common, so their circles are drawn apart. How many numbers are written outside both circles?", "U = {1, 2, 3, ..., 30}۔ P، U کے 4 کے اضعاف کا سیٹ ہے اور Q، U کے 9 کے اضعاف کا سیٹ ہے۔ ان میں کوئی عدد مشترک نہیں، اس لیے ان کے دائرے الگ بنتے ہیں۔ دونوں دائروں سے باہر کتنے اعداد لکھے جائیں گے؟", L4,
      ("Find n(P) and n(Q), then take both away from 30.", "n(P) اور n(Q) معلوم کریں، پھر دونوں کو 30 میں سے نکالیں۔"),
      ("Correct: 30 − 7 − 3 = 20.", "درست: 30 − 7 − 3 = 20"),
      ("Model answer: P = {4, 8, 12, 16, 20, 24, 28} has 7 numbers and Q = {9, 18, 27} has 3. Outside both: 30 − 7 − 3 = 20.", "نمونہ جواب: P = {4, 8, 12, 16, 20, 24, 28} کے 7 اور Q = {9, 18, 27} کے 3 اعداد ہیں۔ دونوں سے باہر: 30 − 7 − 3 = 20"),
      [(23, "That takes away only P (7). Take away Q (3) too: 20.", "یہ صرف P (7) نکالتا ہے۔ Q (3) بھی نکالیں: 20", "stops_early"),
       (10, "That is the number inside the circles (7 + 3). Outside: 20.", "یہ دائروں کے اندر کی تعداد ہے (7 + 3)۔ باہر: 20", "inside_count")]),
   {"id": "s_end_summary", "type": "summary",
    "character": say("celebrating", "You finished the chapter 5 test. Well done!", "آپ نے باب 5 کا ٹیسٹ مکمل کر لیا۔ شاباش!"),
    "text": T("In the exam: a set must be well defined, and each element is written once inside { }. Use ∈ and ∉ for belongs and does not belong. A set with n elements has 2ⁿ subsets, including { } and the set itself, and all of them but the set itself are proper. Equal sets have the same elements; equivalent sets have the same number. In a Venn diagram the rectangle is U, circles are subsets, a subset goes inside the bigger circle, and n(U) is the number inside the circles plus the number outside.",
              "امتحان میں: سیٹ واضح طور پر بیان کردہ ہونا چاہیے اور ہر رکن ایک بار { } کے اندر لکھا جاتا ہے۔ ∈ اور ∉ تعلق رکھتا ہے اور تعلق نہیں رکھتا کے لیے استعمال کریں۔ n ارکان والے سیٹ کے 2ⁿ ذیلی سیٹ ہوتے ہیں، جن میں { } اور خود سیٹ شامل ہیں، اور خود سیٹ کے سوا سب حقیقی ہیں۔ برابر سیٹوں کے ارکان ایک جیسے ہوتے ہیں؛ ہم قوت سیٹوں کے ارکان کی تعداد برابر ہوتی ہے۔ وین ڈایاگرام میں مستطیل U ہے، دائرے ذیلی سیٹ ہیں، ذیلی سیٹ بڑے دائرے کے اندر جاتا ہے، اور n(U) دائروں کے اندر اور باہر کے ارکان کا مجموعہ ہے۔"),
    "points": [T("Check a count by listing the elements.", "گنتی کو ارکان لکھ کر جانچیں۔"),
               T("Write the unit or the set sign with each answer.", "ہر جواب کے ساتھ اکائی یا سیٹ کی علامت لکھیں۔")]},
 ],
 "review_questions": [
   {"id": "r_exam_count", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_count", ("How many elements are in the set of the odd numbers less than 10?", "10 سے چھوٹے طاق اعداد کے سیٹ میں کتنے ارکان ہیں؟"), R1,
     ("List 1, 3, 5 ... and stop before 10.", "1، 3، 5 ... لکھیں اور 10 سے پہلے رک جائیں۔"),
     ("Correct: 1, 3, 5, 7, 9: 5.", "درست: 1، 3، 5، 7، 9: 5"), ("1, 3, 5, 7, 9 are 5 numbers.", "1، 3، 5، 7، 9 یعنی 5 اعداد۔"),
     [(4, "That leaves out one odd number. List them all: 5.", "اس میں ایک طاق عدد رہ گیا۔ سب لکھیں: 5", "wrong_list")], qtype=None)},
   {"id": "r_exam_proper", "type": "exam_style", "skill": SKILL, "step": nq(
     "r_exam_proper", ("How many proper subsets does {p, q} have?", "{p, q} کے کتنے حقیقی ذیلی سیٹ ہیں؟"), R2,
     ("The subsets are { }, {p}, {q}, {p, q}. Which one is improper?", "ذیلی سیٹ { }، {p}، {q}، {p, q} ہیں۔ غیر حقیقی کون سا ہے؟"),
     ("Correct: 3.", "درست: 3"), ("4 subsets minus the set itself: 3.", "4 ذیلی سیٹ منفی خود سیٹ: 3"),
     [(4, "That is all the subsets. Take away the set itself: 3.", "یہ تمام ذیلی سیٹ ہیں۔ خود سیٹ نکال دیں: 3", "proper_count")], qtype=None)},
 ],
 "teacher_notes": [
   "A chapter test to use with Review Exercise 5 of the PCTB Mathematics 6 book, in the style of a paper: multiple choice, short questions, then longer problems. Only the kinds of question come from the book; every question, number and story here is new, because the book may not be copied. The book has no union, intersection or set-builder form, so none is tested.",
   "It has its own skill (maths.sets.chapter_5_test), with the chapter's sets skills as prerequisites, and is mastered with exam_style questions, like g9-maths-05-board-exam-practice.",
   "Urdu terms to check: کثیر انتخابی (multiple choice), مختصر سوال / تفصیلی سوال (short / long question), نمونہ جواب (model answer), اعادی مشق (review exercise), ذیلی سیٹ / حقیقی ذیلی سیٹ (subset / proper subset), ہم قوت (equivalent), وین ڈایاگرام (Venn diagram).",
   "The numbers were worked out in content/sources/g6-maths-01/chapter_5_test.py; edit that script, not this file.",
 ],
 "review": REVIEW,
}

figs.attach(lesson, {"m8_venn": FIG8, "q5_two_circles": FIG5})
write(lesson)

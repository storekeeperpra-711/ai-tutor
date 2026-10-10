"""Practice set for Exercise 5.3 of the book: read the elements of a set from
a Venn diagram, and say how to draw the Venn diagram of a universal set U and
its subsets. The questions are new; only the kinds of question follow the
book. (The book has no union or intersection, so none is tested.)"""
from common import (T, say, nq, ch, practice_lesson, practice_intro, write, show,
                    EX_SKILL, SET_SUBSETS, SET_VENN)
import figs

SKILL = EX_SKILL["5.3"]


def U_text(universe):
    """The universe in words for the alt text."""
    return universe


def alt_one(universe, name, members):
    out = [e for e in universe if e not in members]
    en = (f"A rectangle U holds the numbers or letters {figs.en_list(universe)}. Inside it a circle {name} holds {figs.en_list(members)}. "
          f"{figs.en_list(out)} {'is' if len(out) == 1 else 'are'} in the rectangle but outside the circle.")
    ur = (f"ایک مستطیل U میں {figs.ur_list(universe)} ہیں۔ اس کے اندر ایک دائرہ {name} ہے جس میں {figs.ur_list(members)} ہیں۔ "
          f"{figs.ur_list(out)} مستطیل کے اندر مگر دائرے سے باہر ہیں۔")
    return en, ur


def alt_apart(universe, a, b):
    (na, ma), (nb, mb) = a, b
    out = [e for e in universe if e not in ma and e not in mb]
    en = (f"A rectangle U holds {figs.en_list(universe)}. Inside it are two separate circles: {na} holds {figs.en_list(ma)} and {nb} holds {figs.en_list(mb)}. "
          f"{figs.en_list(out)} are in the rectangle but outside both circles.")
    ur = (f"ایک مستطیل U میں {figs.ur_list(universe)} ہیں۔ اس کے اندر دو الگ دائرے ہیں: {na} میں {figs.ur_list(ma)} اور {nb} میں {figs.ur_list(mb)} ہیں۔ "
          f"{figs.ur_list(out)} مستطیل کے اندر مگر دونوں دائروں سے باہر ہیں۔")
    return en, ur


def alt_nested(universe, a, b):
    (na, ma), (nb, mb) = a, b
    only = [e for e in mb if e not in ma]
    out = [e for e in universe if e not in mb]
    en = (f"A rectangle U holds {figs.en_list(universe)}. Inside it a circle {nb} holds {figs.en_list(mb)}, and a smaller circle {na} sits inside {nb} holding {figs.en_list(ma)}. "
          f"{figs.en_list(only)} are in {nb} but outside {na}. {figs.en_list(out)} are in the rectangle but outside {nb}.")
    ur = (f"ایک مستطیل U میں {figs.ur_list(universe)} ہیں۔ اس کے اندر دائرہ {nb} ہے جس میں {figs.ur_list(mb)} ہیں، اور {nb} کے اندر ایک چھوٹا دائرہ {na} ہے جس میں {figs.ur_list(ma)} ہیں۔ "
          f"{figs.ur_list(only)} دائرہ {nb} میں ہیں مگر {na} سے باہر۔ {figs.ur_list(out)} مستطیل کے اندر مگر {nb} سے باہر ہیں۔")
    return en, ur


# q1-q3: U = 1 to 12, A = the primes
U1 = list(range(1, 13))
A1 = [n for n in U1 if n > 1 and all(n % d for d in range(2, n))]
OUT1 = [n for n in U1 if n not in A1]
assert A1 == [2, 3, 5, 7, 11] and len(A1) == 5 and len(OUT1) == 7 and len(U1) == 12
assert len(A1) + len(OUT1) == len(U1)
FIG1 = figs.u_venn(*alt_one(U1, "A", A1), U1, [("A", A1)], "one")
# q4-q5: U = 1 to 10, B = even numbers, A = multiples of 4 (A inside B)
U4 = list(range(1, 11))
B4 = [n for n in U4 if n % 2 == 0]
A4 = [n for n in U4 if n % 4 == 0]
assert B4 == [2, 4, 6, 8, 10] and A4 == [4, 8] and set(A4) < set(B4)
Q5 = len(set(B4) - set(A4))
assert Q5 == 3 and len(B4) == 5 and len(A4) == 2 and 6 not in A4 and 7 not in B4
FIG4 = figs.u_venn(*alt_nested(U4, ("A", A4), ("B", B4)), U4, [("A", A4), ("B", B4)], "nested")
# q6: U = 1 to 12, A = multiples of 3, B = multiples of 5 (two separate circles)
U6 = list(range(1, 13))
A6 = [n for n in U6 if n % 3 == 0]
B6 = [n for n in U6 if n % 5 == 0]
OUT6 = [n for n in U6 if n not in A6 and n not in B6]
assert A6 == [3, 6, 9, 12] and B6 == [5, 10] and not set(A6) & set(B6)
Q6 = len(OUT6)
assert OUT6 == [1, 2, 4, 7, 8, 11] and Q6 == 6 and len(A6) + len(B6) == 6
FIG6 = figs.u_venn(*alt_apart(U6, ("A", A6), ("B", B6)), U6, [("A", A6), ("B", B6)], "apart")
# q6b: A in words
assert [n for n in U6 if n % 6 == 0] == [6, 12] and [n for n in U6 if n % 4 == 0] == [4, 8, 12]
assert [n for n in U6 if n % 2 == 0] != A6
# q7: where does 3 go when U = 1 to 8 and A = even numbers
U7 = list(range(1, 9))
A7 = [n for n in U7 if n % 2 == 0]
assert A7 == [2, 4, 6, 8] and 3 in U7 and 3 not in A7
# q8: {2, 4} inside {1, 2, 3, 4}
assert {2, 4} < {1, 2, 3, 4}
# q9: a wrong drawing: E should hold 2, 4, 6, 8 but the picture has 9 in it too
U9 = list(range(1, 10))
E9 = [n for n in U9 if n % 2 == 0]
E9_DRAWN = E9 + [9]
assert E9 == [2, 4, 6, 8] and 9 % 2 == 1 and len(E9_DRAWN) == 5
FIG9 = figs.u_venn(*alt_one(U9, "E", E9_DRAWN), U9, [("E", E9_DRAWN)], "one")
# q10: 4 inside, 5 outside
Q10 = 4 + 5
assert Q10 == 9
# q11: letters a to h, V = the vowels
U11 = list("abcdefgh")
V11 = [c for c in U11 if c in "aeiou"]
Q11 = len([c for c in U11 if c not in V11])
assert V11 == ["a", "e"] and Q11 == 6 and len(U11) == 8
# bank and review
UB = list(range(1, 10))
OB = [n for n in UB if n % 2]
assert OB == [1, 3, 5, 7, 9] and len(UB) - len(OB) == 4
FIGB = figs.u_venn(*alt_one(UB, "O", OB), UB, [("O", OB)], "one")
QB_APP = 6 + 3
assert QB_APP == 9
R1 = 12 - 5
assert R1 == 7
UR = list("LAHORE")
VR = [c for c in UR if c in "AEIOU"]
R2 = len(UR) - len(VR)
assert VR == ["A", "O", "E"] and R2 == 3

lesson = practice_lesson(
 "5.3", script="exercise_5_3.py",
 title=T("Exercise 5.3 practice: Venn diagrams", "مشق 5.3 کی پریکٹس: وین ڈایاگرام"),
 outcome="Read the elements of a set from a Venn diagram, and say how to draw the Venn diagram of a universal set and its subsets.",
 prerequisites=[SET_SUBSETS, SET_VENN],
 misconceptions=[
   {"id": "counts_universal", "description": "Counts every element of the rectangle U when asked for the elements or the number of elements of a set."},
   {"id": "outside_is_in", "description": "Thinks an element written in the rectangle but outside a circle belongs to that set."},
   {"id": "outside_universe", "description": "Writes an element outside the rectangle U instead of inside it, outside the circles."},
   {"id": "subset_apart", "description": "Draws a subset as a separate or overlapping circle instead of inside the bigger set's circle."},
   {"id": "inside_count", "description": "Gives the number inside a circle when the number outside it is asked, or the other way round."},
   {"id": "misses_the_odd_one", "description": "Does not notice an element drawn in a circle where it does not belong."},
 ],
 steps=[
   practice_intro("5.3",
     "Here you read the elements of a set from a Venn diagram and decide how to draw a universal set and its subsets.",
     "اس میں آپ وین ڈایاگرام سے سیٹ کے ارکان پڑھیں گے اور طے کریں گے کہ عالمی سیٹ اور اس کے ذیلی سیٹ کیسے بنائے جائیں۔",
     "Exercise 5.3 is about Venn diagrams. Ready?", "مشق 5.3 وین ڈایاگرام کے بارے میں ہے۔ تیار؟"),
   nq("q1_inside", ("Look at the Venn diagram. How many numbers are inside circle A?", "وین ڈایاگرام دیکھیں۔ دائرہ A کے اندر کتنے اعداد ہیں؟"), len(A1),
      ("Count only what is inside the circle, not the whole rectangle.", "صرف دائرے کے اندر والے گنیں، پورا مستطیل نہیں۔"),
      ("Right! 2, 3, 5, 7 and 11: 5.", "درست! 2، 3، 5، 7 اور 11: 5"),
      ("The circle A holds 2, 3, 5, 7 and 11. That is 5 numbers.", "دائرہ A میں 2، 3، 5، 7 اور 11 ہیں۔ یعنی 5 اعداد۔"),
      [(12, "12 is all the numbers in U. Count only those inside the circle: 5.", "12 تو U کے تمام اعداد ہیں۔ صرف دائرے کے اندر والے گنیں: 5", "counts_universal")],
      qtype="recall"),
   ch("q2_elements", ("Look at the same diagram. Which is the set A in tabular form?", "اسی ڈایاگرام کو دیکھیں۔ سیٹ A کی جدولی شکل کون سی ہے؟"),
      (show(A1), show(A1), "Yes! A holds exactly the numbers inside its circle.", "جی ہاں! A میں بالکل وہی اعداد ہیں جو اس کے دائرے کے اندر ہیں۔"),
      [(show(OUT1), show(OUT1), "Those are the numbers outside the circle. A is what is inside.", "یہ دائرے سے باہر کے اعداد ہیں۔ A وہ ہے جو اندر ہے۔", "outside_is_in"),
       (show(U1), show(U1), "That is the whole universal set U, not just A.", "یہ پورا عالمی سیٹ U ہے، صرف A نہیں۔", "counts_universal"),
       (show([2, 3, 5, 7]), show([2, 3, 5, 7]), "11 is inside the circle too. Check every number.", "11 بھی دائرے کے اندر ہے۔ ہر عدد دیکھیں۔")],
      1, qtype="recall"),
   nq("q3_outside", ("In the same diagram, how many numbers of U are outside circle A?", "اسی ڈایاگرام میں U کے کتنے اعداد دائرہ A سے باہر ہیں؟"), len(OUT1),
      ("U has 12 numbers. How many of them are inside A?", "U میں 12 اعداد ہیں۔ ان میں سے کتنے A کے اندر ہیں؟"),
      ("Right! 12 − 5 = 7: 1, 4, 6, 8, 9, 10, 12.", "درست! 12 − 5 = 7: 1، 4، 6، 8، 9، 10، 12"),
      ("Outside the circle but inside the rectangle: 1, 4, 6, 8, 9, 10, 12. That is 7 numbers.", "دائرے سے باہر مگر مستطیل کے اندر: 1، 4، 6، 8، 9، 10، 12۔ یعنی 7 اعداد۔"),
      [(5, "That is the number inside the circle. We want the number outside: 7.", "یہ دائرے کے اندر والوں کی تعداد ہے۔ ہمیں باہر والوں کی چاہیے: 7", "inside_count"),
       (12, "That is all of U. Take away the 5 inside the circle: 7.", "یہ سارا U ہے۔ دائرے کے اندر والے 5 نکالیں: 7", "counts_universal")]),
   {"id": "s_rules", "type": "explain",
    "character": say("thinking", "The rectangle is U. Circles are subsets. Look where each element sits.", "مستطیل U ہے۔ دائرے ذیلی سیٹ ہیں۔ دیکھیں ہر رکن کہاں لکھا ہے۔"),
    "text": T("In a Venn diagram the universal set U is a rectangle and each set is a circle inside it. An element inside a circle belongs to that set. An element in the rectangle but outside the circle is in U but not in that set. Every element of U is written inside the rectangle, never outside it. If B is a subset of A, draw the circle of B inside the circle of A. If two sets share no elements, draw their circles apart. The number of elements of U is the number inside the circles plus the number outside them.",
              "وین ڈایاگرام میں عالمی سیٹ U مستطیل ہے اور ہر سیٹ اس کے اندر ایک دائرہ ہے۔ دائرے کے اندر کا رکن اس سیٹ سے تعلق رکھتا ہے۔ مستطیل کے اندر مگر دائرے سے باہر کا رکن U میں ہے مگر اس سیٹ میں نہیں۔ U کا ہر رکن مستطیل کے اندر لکھا جاتا ہے، باہر کبھی نہیں۔ اگر B، A کا ذیلی سیٹ ہو تو B کا دائرہ A کے دائرے کے اندر بنائیں۔ اگر دو سیٹوں میں کوئی رکن مشترک نہ ہو تو ان کے دائرے الگ الگ بنائیں۔ U کے ارکان کی تعداد دائروں کے اندر اور باہر کے ارکان کا مجموعہ ہے۔")},
   ch("q4_nested", ("In this diagram, which statement is true?", "اس ڈایاگرام میں کون سا بیان درست ہے؟"),
      ("A ⊂ B", "A ⊂ B", "Yes! Circle A is inside circle B, so every element of A is in B.", "جی ہاں! دائرہ A، دائرہ B کے اندر ہے، اس لیے A کا ہر رکن B میں ہے۔"),
      [("B ⊂ A", "B ⊂ A", "B is the bigger circle. It has 2, 6 and 10, which are not in A.", "B بڑا دائرہ ہے۔ اس میں 2، 6 اور 10 ہیں جو A میں نہیں۔", "subset_apart"),
       ("6 ∈ A", "6 ∈ A", "6 is in circle B but outside circle A, so 6 ∉ A.", "6 دائرہ B میں ہے مگر دائرہ A سے باہر، اس لیے 6 ∉ A۔", "outside_is_in"),
       ("7 ∈ B", "7 ∈ B", "7 is in the rectangle but outside both circles, so 7 ∉ B.", "7 مستطیل کے اندر مگر دونوں دائروں سے باہر ہے، اس لیے 7 ∉ B۔", "outside_is_in")],
      0),
   nq("q5_in_b_not_a", ("In the same diagram, how many numbers are in circle B but not in circle A?", "اسی ڈایاگرام میں کتنے اعداد دائرہ B میں ہیں مگر دائرہ A میں نہیں؟"), Q5,
      ("B has 5 numbers. Some of them are also inside A.", "B میں 5 اعداد ہیں۔ ان میں سے کچھ A کے اندر بھی ہیں۔"),
      ("Right! 2, 6 and 10: 3.", "درست! 2، 6 اور 10: 3"),
      ("B holds 2, 4, 6, 8, 10. Take away 4 and 8, which are in A: 2, 6, 10 are left: 3.", "B میں 2، 4، 6، 8، 10 ہیں۔ 4 اور 8 نکال دیں جو A میں ہیں: 2، 6، 10 بچتے ہیں: 3"),
      [(5, "That is all the numbers in B. Leave out those that are also in A: 3.", "یہ B کے تمام اعداد ہیں۔ وہ چھوڑ دیں جو A میں بھی ہیں: 3", "inside_count"),
       (2, "That is the number of elements of A. We want those in B only: 3.", "یہ A کے ارکان کی تعداد ہے۔ ہمیں صرف B والے چاہییں: 3", "inside_count")]),
   nq("q6_outside_both", ("In this diagram, how many numbers of U are outside both circles?", "اس ڈایاگرام میں U کے کتنے اعداد دونوں دائروں سے باہر ہیں؟"), Q6,
      ("Count the numbers in the rectangle that are not inside either circle.", "مستطیل کے وہ اعداد گنیں جو کسی دائرے کے اندر نہیں۔"),
      ("Right! 1, 2, 4, 7, 8, 11: 6.", "درست! 1، 2، 4، 7، 8، 11: 6"),
      ("Circle A has 4 numbers and circle B has 2. U has 12, and 12 − 4 − 2 = 6 numbers are outside both.", "دائرہ A میں 4 اعداد اور دائرہ B میں 2 ہیں۔ U میں 12 ہیں، اور 12 − 4 − 2 = 6 اعداد دونوں سے باہر ہیں۔"),
      [(12, "That is all of U. Take away those inside the circles: 6.", "یہ سارا U ہے۔ دائروں کے اندر والے نکالیں: 6", "counts_universal"),
       (4, "That is the number inside circle A. Count the numbers outside both circles: 6.", "یہ دائرہ A کے اندر کی تعداد ہے۔ دونوں دائروں سے باہر کے اعداد گنیں: 6", "inside_count")]),
   ch("q7_describe", ("In the same diagram, how would you describe circle A in words?", "اسی ڈایاگرام میں دائرہ A کو الفاظ میں کیسے بیان کریں گے؟"),
      ("The multiples of 3 in U", "U کے 3 کے اضعاف", "Yes! 3, 6, 9 and 12 are the multiples of 3 up to 12.", "جی ہاں! 3، 6، 9 اور 12، 12 تک 3 کے اضعاف ہیں۔"),
      [("The multiples of 6 in U", "U کے 6 کے اضعاف", "The multiples of 6 are only 6 and 12. A also holds 3 and 9.", "6 کے اضعاف صرف 6 اور 12 ہیں۔ A میں 3 اور 9 بھی ہیں۔"),
       ("The even numbers in U", "U کے جفت اعداد", "A holds 3 and 9, which are odd, and leaves out 2, 4, 8.", "A میں 3 اور 9 ہیں جو طاق ہیں، اور 2، 4، 8 اس میں نہیں۔"),
       ("The multiples of 4 in U", "U کے 4 کے اضعاف", "The multiples of 4 are 4, 8, 12. That is a different set.", "4 کے اضعاف 4، 8، 12 ہیں۔ یہ ایک اور سیٹ ہے۔")],
      2),
   ch("q8_draw_outside", ("You draw U = {1, 2, 3, 4, 5, 6, 7, 8} and a circle A = {2, 4, 6, 8}. Where do you write 3?", "آپ U = {1, 2, 3, 4, 5, 6, 7, 8} اور دائرہ A = {2, 4, 6, 8} بناتے ہیں۔ 3 کہاں لکھیں گے؟"),
      ("Inside the rectangle, outside circle A", "مستطیل کے اندر، دائرہ A کے باہر", "Yes! 3 is in U but not in A.", "جی ہاں! 3، U میں ہے مگر A میں نہیں۔"),
      [("Inside circle A", "دائرہ A کے اندر", "3 is odd, so it is not in A.", "3 طاق ہے، اس لیے A میں نہیں۔", "outside_is_in"),
       ("Outside the rectangle", "مستطیل کے باہر", "3 is in U, so it goes inside the rectangle. Every element of U is inside it.", "3، U میں ہے، اس لیے مستطیل کے اندر جائے گا۔ U کا ہر رکن اس کے اندر ہوتا ہے۔", "outside_universe"),
       ("On the line of the circle", "دائرے کی لکیر پر", "An element is never on the line. It is either inside the circle or outside it.", "رکن کبھی لکیر پر نہیں ہوتا۔ وہ دائرے کے اندر ہوتا ہے یا باہر۔")],
      0, qtype="apply"),
   ch("q9_draw_subset", ("B = {2, 4} and A = {1, 2, 3, 4}, so B is a subset of A. How should you draw their circles?", "B = {2, 4} اور A = {1, 2, 3, 4}، اس لیے B، A کا ذیلی سیٹ ہے۔ ان کے دائرے کیسے بنائیں گے؟"),
      ("The circle B inside the circle A", "دائرہ B، دائرہ A کے اندر", "Yes! Every element of B is also in A, so B sits inside A.", "جی ہاں! B کا ہر رکن A میں بھی ہے، اس لیے B، A کے اندر ہوتا ہے۔"),
      [("Two separate circles", "دو الگ دائرے", "Separate circles mean no shared elements. But 2 and 4 are in both sets.", "الگ دائروں کا مطلب ہے کوئی رکن مشترک نہیں۔ مگر 2 اور 4 دونوں سیٹوں میں ہیں۔", "subset_apart"),
       ("The circle A inside the circle B", "دائرہ A، دائرہ B کے اندر", "That is the wrong way round. B is the smaller set, so B goes inside A.", "یہ الٹا ہے۔ B چھوٹا سیٹ ہے، اس لیے B، A کے اندر جائے گا۔", "subset_apart"),
       ("Two circles of the same size on top of each other", "ایک دوسرے پر دو برابر دائرے", "That would mean the sets are equal. A has 1 and 3 as well.", "اس کا مطلب ہوتا کہ سیٹ برابر ہیں۔ A میں 1 اور 3 بھی ہیں۔", "subset_apart")],
      1, qtype="apply"),
   ch("q10_find_error", ("Mehr drew this Venn diagram for U = {1, 2, 3, 4, 5, 6, 7, 8, 9} and E = the even numbers. What is wrong with it?", "مہر نے U = {1, 2, 3, 4, 5, 6, 7, 8, 9} اور E = جفت اعداد کے لیے یہ وین ڈایاگرام بنایا۔ اس میں کیا غلطی ہے؟"),
      ("9 is odd, so it must be outside circle E.", "9 طاق ہے، اس لیے اسے دائرہ E کے باہر ہونا چاہیے۔", "Yes! The even numbers are 2, 4, 6, 8 only.", "جی ہاں! جفت اعداد صرف 2، 4، 6، 8 ہیں۔"),
      [("Nothing. The diagram is correct.", "کوئی غلطی نہیں۔ ڈایاگرام درست ہے۔", "Look at each number in the circle. 9 is not even.", "دائرے کے ہر عدد کو دیکھیں۔ 9 جفت نہیں۔", "misses_the_odd_one"),
       ("2 should be outside circle E.", "2 کو دائرہ E کے باہر ہونا چاہیے۔", "2 is even, so it belongs in E.", "2 جفت ہے، اس لیے E میں آتا ہے۔"),
       ("The circle should be as big as the rectangle.", "دائرہ مستطیل جتنا بڑا ہونا چاہیے۔", "Then E would hold all of U. E is only the even numbers.", "تب E میں سارا U آ جاتا۔ E صرف جفت اعداد ہیں۔", "counts_universal")],
      0, qtype="find_error"),
   nq("q11_total", ("In a Venn diagram, circle K holds 4 numbers and 5 numbers of U are outside it. How many numbers does U have?", "ایک وین ڈایاگرام میں دائرہ K میں 4 اعداد ہیں اور U کے 5 اعداد اس سے باہر ہیں۔ U میں کتنے اعداد ہیں؟"), Q10,
      ("U is everything in the rectangle: inside the circle and outside it.", "U مستطیل کی ہر چیز ہے: دائرے کے اندر اور باہر۔"),
      ("Right! 4 + 5 = 9.", "درست! 4 + 5 = 9"),
      ("The numbers inside the circle and outside it make up all of U: 4 + 5 = 9.", "دائرے کے اندر اور باہر کے اعداد مل کر سارا U بنتے ہیں: 4 + 5 = 9"),
      [(5, "That is only the numbers outside the circle. Add the 4 inside: 9.", "یہ صرف دائرے سے باہر کے اعداد ہیں۔ اندر کے 4 بھی جمع کریں: 9", "inside_count"),
       (4, "That is only the numbers inside the circle. Add the 5 outside: 9.", "یہ صرف دائرے کے اندر کے اعداد ہیں۔ باہر کے 5 بھی جمع کریں: 9", "inside_count")]),
   nq("q12_letters", ("U = {a, b, c, d, e, f, g, h} and V is the set of vowels in U. When you draw the Venn diagram, how many letters are written outside circle V?", "U = {a, b, c, d, e, f, g, h} اور V، U کے حروفِ علت کا سیٹ ہے۔ وین ڈایاگرام بنائیں تو دائرہ V کے باہر کتنے حروف لکھے جائیں گے؟"), Q11,
      ("The vowels in U are a and e. The other letters of U go outside the circle.", "U میں حروفِ علت a اور e ہیں۔ U کے باقی حروف دائرے کے باہر جاتے ہیں۔"),
      ("Right! b, c, d, f, g, h: 6.", "درست! b، c، d، f، g، h: 6"),
      ("V = {a, e}. The other 8 − 2 = 6 letters go outside the circle.", "V = {a, e}۔ باقی 8 − 2 = 6 حروف دائرے کے باہر جاتے ہیں۔"),
      [(2, "That is the number inside the circle (a and e). Outside: 6.", "یہ دائرے کے اندر کی تعداد ہے (a اور e)۔ باہر: 6", "inside_count"),
       (8, "That is all of U. Take away the 2 vowels: 6.", "یہ سارا U ہے۔ 2 حروفِ علت نکالیں: 6", "counts_universal")]),
   {"id": "s_summary", "type": "summary",
    "character": say("celebrating", "Well done! You can read and draw Venn diagrams.", "شاباش! آپ وین ڈایاگرام پڑھ اور بنا سکتے ہیں۔"),
    "text": T("The rectangle is U and each circle is a subset. Inside a circle means in the set. In the rectangle but outside the circle means in U but not in the set. Every element of U is inside the rectangle. A subset's circle goes inside the bigger set's circle, and sets with nothing in common are drawn apart. n(U) is the number inside the circles plus the number outside them.",
              "مستطیل U ہے اور ہر دائرہ ایک ذیلی سیٹ۔ دائرے کے اندر کا مطلب سیٹ میں ہے۔ مستطیل کے اندر مگر دائرے کے باہر کا مطلب U میں ہے مگر سیٹ میں نہیں۔ U کا ہر رکن مستطیل کے اندر ہوتا ہے۔ ذیلی سیٹ کا دائرہ بڑے سیٹ کے دائرے کے اندر جاتا ہے، اور جن سیٹوں میں کچھ مشترک نہ ہو انھیں الگ بنایا جاتا ہے۔ n(U) دائروں کے اندر اور باہر کے ارکان کا مجموعہ ہے۔"),
    "points": [T("Check each number against the rule of its circle.", "ہر عدد کو اس کے دائرے کے اصول سے ملا کر دیکھیں۔"),
               T("Inside plus outside is the whole of U.", "اندر اور باہر مل کر پورا U بنتا ہے۔")]},
 ],
 bank=[
   {"id": "qb_read", "type": "recall", "step": nq("qb_read", ("Look at the Venn diagram. How many numbers are inside circle O?", "وین ڈایاگرام دیکھیں۔ دائرہ O کے اندر کتنے اعداد ہیں؟"), len(OB),
      ("Count only the numbers inside the circle.", "صرف دائرے کے اندر کے اعداد گنیں۔"),
      ("Right! 1, 3, 5, 7, 9: 5.", "درست! 1، 3، 5، 7، 9: 5"), ("Inside circle O: 1, 3, 5, 7, 9. That is 5.", "دائرہ O کے اندر: 1، 3، 5، 7، 9۔ یعنی 5۔"),
      [(9, "That is all of U. Count only those inside the circle: 5.", "یہ سارا U ہے۔ صرف دائرے کے اندر والے گنیں: 5", "counts_universal")], qtype=None)},
   {"id": "qb_total", "type": "apply", "step": nq("qb_total", ("A circle holds 6 elements and 3 elements of U are outside it. How many elements does U have?", "ایک دائرے میں 6 ارکان ہیں اور U کے 3 ارکان اس سے باہر ہیں۔ U کے کتنے ارکان ہیں؟"), QB_APP,
      ("Add the elements inside and outside.", "اندر اور باہر کے ارکان جمع کریں۔"),
      ("Right! 6 + 3 = 9.", "درست! 6 + 3 = 9"), ("Inside plus outside make U: 6 + 3 = 9.", "اندر اور باہر مل کر U بنتا ہے: 6 + 3 = 9"),
      [(3, "That is only the outside. Add the 6 inside: 9.", "یہ صرف باہر والے ہیں۔ اندر کے 6 بھی جمع کریں: 9", "inside_count")], qtype=None)},
   {"id": "qb_find_error", "type": "find_error", "step": ch("qb_find_error",
      ("Ahmed has A = {1, 2, 3, 4} and B = {2, 4}. He draws B as a circle apart from circle A. What went wrong?", "احمد کے پاس A = {1, 2, 3, 4} اور B = {2, 4} ہیں۔ وہ B کا دائرہ A کے دائرے سے الگ بناتا ہے۔ کیا غلطی ہوئی؟"),
      ("B is a subset of A, so the circle of B must be inside the circle of A.", "B، A کا ذیلی سیٹ ہے، اس لیے B کا دائرہ A کے دائرے کے اندر ہونا چاہیے۔", "Yes! 2 and 4 are in A too.", "جی ہاں! 2 اور 4 A میں بھی ہیں۔"),
      [("Nothing. Every set gets its own separate circle.", "کوئی غلطی نہیں۔ ہر سیٹ کا اپنا الگ دائرہ ہوتا ہے۔", "A subset goes inside the bigger set's circle.", "ذیلی سیٹ بڑے سیٹ کے دائرے کے اندر جاتا ہے۔", "subset_apart"),
       ("B should be drawn outside the rectangle.", "B کو مستطیل کے باہر بنانا چاہیے۔", "Every set drawn in a Venn diagram sits inside U.", "وین ڈایاگرام کا ہر سیٹ U کے اندر ہوتا ہے۔", "outside_universe")],
      0, qtype=None)},
 ],
 review=[
   {"id": "r_outside", "type": "recall", "step": nq("r_outside", ("U has 12 elements and circle C holds 5 of them. How many are outside circle C?", "U کے 12 ارکان ہیں اور دائرہ C میں ان میں سے 5 ہیں۔ دائرہ C کے باہر کتنے ہیں؟"), R1,
      ("Take the ones inside the circle away from all of U.", "پورے U میں سے دائرے کے اندر والے نکالیں۔"),
      ("Right! 12 − 5 = 7.", "درست! 12 − 5 = 7"), ("12 − 5 = 7 elements are outside.", "12 − 5 = 7 ارکان باہر ہیں۔"),
      [(5, "That is the number inside. Outside: 7.", "یہ اندر کی تعداد ہے۔ باہر: 7", "inside_count")], qtype=None)},
   {"id": "r_letters", "type": "apply", "step": nq("r_letters", ("U is the letters of the word \"LAHORE\" and V is the set of its vowels. How many letters are written outside circle V?", "U لفظ \"LAHORE\" کے حروف ہیں اور V اس کے حروفِ علت کا سیٹ ہے۔ دائرہ V کے باہر کتنے حروف لکھے جائیں گے؟"), R2,
      ("The vowels are A, O, E. The rest go outside the circle.", "حروفِ علت A، O، E ہیں۔ باقی دائرے کے باہر جاتے ہیں۔"),
      ("Right! L, H, R: 3.", "درست! L، H، R: 3"), ("6 letters, 3 of them vowels, so 3 are outside.", "6 حروف ہیں، ان میں 3 حروفِ علت ہیں، اس لیے 3 باہر ہیں۔"),
      [(6, "That is all of U. Take away the 3 vowels: 3.", "یہ سارا U ہے۔ 3 حروفِ علت نکالیں: 3", "counts_universal")], qtype=None)},
 ],
 glossary=[T("Venn diagram", "وین ڈایاگرام"), T("Universal set", "عالمی سیٹ"), T("Subset", "ذیلی سیٹ"), T("Element", "رکن"), T("Circle", "دائرہ"), T("Rectangle", "مستطیل")],
 flashcards=[
   {"id": "f_venn", "front": T("What do the rectangle and the circles of a Venn diagram show?", "وین ڈایاگرام کا مستطیل اور دائرے کیا دکھاتے ہیں؟"),
    "back": T("The rectangle is the universal set U. Each circle is a subset of U.", "مستطیل عالمی سیٹ U ہے۔ ہر دائرہ U کا ذیلی سیٹ ہے۔")},
   {"id": "f_draw_subset", "front": T("How do you draw a subset of a set?", "کسی سیٹ کا ذیلی سیٹ کیسے بنائیں؟"),
    "back": T("Draw its circle inside the bigger set's circle.", "اس کا دائرہ بڑے سیٹ کے دائرے کے اندر بنائیں۔")},
 ],
 home_task={"id": "h_venn_home", "text": T(
   "Draw a big rectangle for U, the 10 numbers 1 to 10. Draw a circle for the even numbers and write the numbers in the right places. Then draw a smaller circle inside it for the multiples of 4. Show it to a friend and ask where 7 goes.",
   "U کے لیے بڑا مستطیل بنائیں، جس میں 1 سے 10 تک 10 اعداد ہوں۔ جفت اعداد کے لیے ایک دائرہ بنائیں اور اعداد صحیح جگہوں پر لکھیں۔ پھر اس کے اندر 4 کے اضعاف کے لیے ایک چھوٹا دائرہ بنائیں۔ کسی دوست کو دکھائیں اور پوچھیں کہ 7 کہاں جائے گا۔")},
 notes=["Covers reading the elements and the number of elements of a set from a Venn diagram (q1, q2, q3, q5, q6), describing a set drawn in a diagram (q7), deciding where to draw elements and subsets (q8, q9, q12), a find-the-error question about a drawing (q10) and counting n(U) (q11).",
        "Each wrong answer is a real mistake: counting the whole rectangle, reading outside as inside, the inside and outside numbers swapped, a subset drawn apart from its bigger set, and not noticing an element drawn in the wrong place.",
        "The pictures are built by figs.u_venn, which checks that every number or letter sits inside exactly the circles of its sets (q10's wrong drawing is made by giving the wrong members on purpose). Urdu terms to check: وین ڈایاگرام (Venn diagram), عالمی سیٹ (universal set), مستطیل / دائرہ (rectangle / circle)."],
 minutes=18,
)

figs.attach(lesson, {
    "q1_inside": FIG1, "q2_elements": FIG1, "q3_outside": FIG1,
    "q4_nested": FIG4, "q5_in_b_not_a": FIG4,
    "q6_outside_both": FIG6, "q7_describe": FIG6,
    "q10_find_error": FIG9,
    "qb_read": FIGB,
})
write(lesson)

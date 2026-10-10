import json
import sys
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "content" / "sources"))

from why import WHY  # noqa: E402
from why_steps import add_why  # noqa: E402

REF = "PCTB Mathematics 6 (SNC 2022), Sub-domain 4: Rate, Ratio and Percentage"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from other units that these lessons build on.
UNIT_FRACTIONS = "maths.fractions.unit_fraction_meaning"
TIMES_TABLES = "maths.multiplication.facts"
EQUIVALENT_FRACTIONS = "maths.fractions.equivalent"

# Skills of the Ratio and Proportion unit.
RATIO_MEANING = "maths.ratio.meaning"
RATIO_EQUIVALENT = "maths.ratio.equivalent"
RATIO_SHARE = "maths.ratio.share"
RATIO_PROPORTION = "maths.ratio.proportion"
UNITARY = "maths.ratio.unitary_method"
RATIO_WORD_PROBLEMS = "maths.ratio.word_problems"
# Added after matching the PCTB Mathematics 6 book (Sub-domain 4).
RATIO_RATE = "maths.ratio.rate"
RATIO_CONTINUED = "maths.ratio.continued"

BOOK = "PCTB Mathematics 6 (SNC 2022), Sub-domain 4: Rate, Ratio and Percentage"


def T(en, ur):
    return {"en": en, "ur": ur}


def opt(id, en, ur, correct, fen, fur, mis=None):
    o = {"id": id, "text": T(en, ur), "correct": correct, "feedback": T(fen, fur)}
    if mis:
        o["misconception_id"] = mis
    return o


def say(emotion, en, ur):
    return {"emotion": emotion, "say": T(en, ur)}


def wrong(answer, en, ur, mis=None):
    w = {"answer": answer, "feedback": T(en, ur)}
    if mis:
        w["misconception_id"] = mis
    return w


def ratio(a: int, b: int) -> str:
    """A ratio written as given: 4:6 stays 4:6."""
    return f"{a}:{b}"


def continued(*parts: int) -> str:
    """A continued ratio written as given: 2:3:4."""
    return ":".join(str(p) for p in parts)


def simplest_all(*parts: int) -> tuple[int, ...]:
    g = gcd(*parts)
    return tuple(p // g for p in parts)


def join(ab: tuple[int, int], bc: tuple[int, int]) -> tuple[int, int, int]:
    """a:b:c from a:b and b:c, making the two b's the same first."""
    (a, b1), (b2, c) = ab, bc
    m = b1 * b2 // gcd(b1, b2)
    return simplest_all(a * m // b1, m, c * m // b2)


def continued_question(id, prompt, parts, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None, character=None):
    """A typed continued ratio like 2:3:4, checked exactly (spaces don't matter)."""
    step = {"id": id, "type": "text_check"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    if character:
        step["character"] = character
    step.update({
        "prompt": prompt, "checker": "text", "expected": continued(*parts),
        "accept": [continued(*parts).replace(":", "∶")],
        "hint": hint, "feedback_correct": good, "feedback_wrong": bad,
    })
    if common_wrong:
        step["common_wrong"] = list(common_wrong)
    return step


assert join((2, 3), (3, 5)) == (2, 3, 5) and join((2, 3), (4, 5)) == (8, 12, 15)


def simplest(a: int, b: int) -> tuple[int, int]:
    g = gcd(a, b)
    return a // g, b // g


def same_ratio(a, b, c, d) -> bool:
    return F(a, b) == F(c, d)


def share(total: int, parts: tuple[int, ...]) -> list[int]:
    """Shares [total] in the ratio [parts]; every share is a whole number."""
    one, rest = divmod(total, sum(parts))
    assert rest == 0, (total, parts)
    return [p * one for p in parts]


def ratio_question(id, prompt, a: int, b: int, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None, character=None):
    """A typed-ratio step: '3:5', '3 : 5' and '3 to 5' are all accepted.

    The text checker compares exactly (spaces don't matter), so the answer
    must be the one ratio the question asks for, already in the form asked."""
    step = {"id": id, "type": "text_check"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    if character:
        step["character"] = character
    step.update({
        "prompt": prompt, "checker": "text", "expected": ratio(a, b),
        "accept": [f"{a} to {b}", f"{a}∶{b}"],
        "hint": hint, "feedback_correct": good, "feedback_wrong": bad,
    })
    if common_wrong:
        step["common_wrong"] = list(common_wrong)
    return step


def number_question(id, prompt, answer: int, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None, character=None):
    """A step whose answer is a whole number."""
    step = {"id": id, "type": "number"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    if character:
        step["character"] = character
    step.update({"prompt": prompt, "answer": answer, "checker": "numeric",
                 "hint": hint, "feedback_correct": good, "feedback_wrong": bad})
    if common_wrong:
        step["common_wrong"] = list(common_wrong)
    return step


def missing_term(a: int, b: int, c: int) -> int:
    """d in a : b :: c : d, from extremes × extremes = means × means."""
    d = F(b * c, a)
    assert d.denominator == 1, (a, b, c)
    assert a * d == b * c
    return int(d)


def check_lesson(lesson):
    """Checks before writing: no common wrong answer equals the right one,
    and Mithu's lines are short."""
    def steps():
        yield from lesson["steps"]
        for qs in lesson["question_bank"].values():
            for q in qs:
                yield q["step"]
        for q in lesson.get("review_questions", []):
            yield q["step"]
    for step in steps():
        if step["type"] == "text_check":
            right = {x.replace(" ", "") for x in [step["expected"], *step.get("accept", [])]}
            for w in step.get("common_wrong", []):
                assert w["answer"].replace(" ", "") not in right, step["id"]
        if step["type"] == "number":
            assert step["answer"] not in [w["answer"] for w in step.get("common_wrong", [])], step["id"]
        if step["type"] == "choice":
            assert sum(o["correct"] for o in step["options"]) == 1, step["id"]
        line = step.get("character")
        if line:
            for lang in ("en", "ur"):
                assert len(line["say"][lang].split()) <= 30, (step["id"], lang)


def write(lesson):
    add_why(lesson, WHY)
    check_lesson(lesson)
    path = ROOT / "content" / "lessons" / f"{lesson['id']}.json"
    path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", path.name)


# ---------------------------------------------------------------------------
# Practice sets that go with the book's exercises of chapter 4 (Rate, Ratio and
# Percentage), and the chapter test. The chapter's lessons are in this unit and
# in the Percentages unit (g6-maths-11), so Exercise 4.3 has a maths.percent
# skill and Exercise 4.4 a maths.time skill. Each practice lesson has its own
# skill, with the chapter's skills it practises as prerequisites.
RATIO_SPEED = "maths.ratio.speed"
TIME_CLOCK = "maths.time.clock_24"
PC_MEANING = "maths.percent.meaning"
PC_CONVERT = "maths.percent.convert"
PC_OF_AMOUNT = "maths.percent.of_amount"
PC_FIND = "maths.percent.find_percent"
PC_CHANGE = "maths.percent.change"
PC_WORD_PROBLEMS = "maths.percent.word_problems"
EX_SKILL = {"4.1": "maths.ratio.ex_4_1", "4.2": "maths.ratio.ex_4_2", "4.3": "maths.percent.ex_4_3",
            "4.4": "maths.time.ex_4_4", "4.5": "maths.ratio.ex_4_5"}
CHAPTER_4_TEST = "maths.ratio.chapter_4_test"


def book_ref(part):
    """'Exercise 4.1' -> the textbook string for curriculum_refs."""
    return f"{BOOK}, {part}"


def nq(id, prompt, answer, hint, good, bad, wrongs=(), qtype="apply"):
    """number_question with (en, ur) tuples; wrongs are (answer, en, ur, misconception)."""
    return number_question(id, T(*prompt), answer, T(*hint), T(*good), T(*bad),
                           common_wrong=[wrong(a, en, ur, mis) for a, en, ur, mis in wrongs], qtype=qtype)


def rq(id, prompt, parts, hint, good, bad, wrongs=(), qtype="apply"):
    """A typed ratio (two terms) or continued ratio (three); wrongs are (text, en, ur, misconception)."""
    cw = [wrong(a, en, ur, mis) for a, en, ur, mis in wrongs]
    if len(parts) == 2:
        return ratio_question(id, T(*prompt), *parts, T(*hint), T(*good), T(*bad), common_wrong=cw, qtype=qtype)
    return continued_question(id, T(*prompt), parts, T(*hint), T(*good), T(*bad), common_wrong=cw, qtype=qtype)


def accepted_time(text):
    """Other ways a child may type the same time: 9:10, 0910, 09.10."""
    hour, m = text.split(":")
    return sorted({f"{hour}{m}", f"{hour}.{m}", f"{int(hour)}:{m}", f"{int(hour)}.{m}"} - {text})


def tq(id, prompt, expected, hint, good, bad, wrongs=(), qtype="apply"):
    """A typed 24-hour time like 15:45 (1545 and 15.45 are accepted too)."""
    step = {"id": id, "type": "text_check"}
    if qtype:
        step["question_type"] = qtype
    acc = accepted_time(expected)
    step.update({"prompt": T(*prompt), "checker": "text", "expected": expected, "accept": acc,
                 "hint": T(*hint), "feedback_correct": T(*good), "feedback_wrong": T(*bad)})
    if wrongs:
        cw = [wrong(a, en, ur, mis) for a, en, ur, mis in wrongs]
        assert all(w["answer"] not in {expected, *acc} for w in cw), id
        step["common_wrong"] = cw
    return step


def ch(id, prompt, right, wrongs, pos, qtype="apply"):
    """A choice step with (en, ur) prompt. right is (en, ur, feedback_en,
    feedback_ur); each wrong is the same plus an optional misconception. The
    right option goes at index pos."""
    options = [opt("x", right[0], right[1], True, right[2], right[3])]
    for w in wrongs:
        options.append(opt("x", w[0], w[1], False, w[2], w[3], w[4] if len(w) > 4 else None))
    options.insert(pos, options.pop(0))
    for k, o in enumerate(options):
        o["id"] = "abcd"[k]
    step = {"id": id, "type": "choice"}
    if qtype:
        step["question_type"] = qtype
    step.update({"prompt": T(*prompt), "options": options})
    return step


def practice_lesson(ex, *, script, title, outcome, prerequisites, misconceptions, steps,
                    bank, review, glossary, flashcards, home_task, notes, minutes=18):
    """A practice set to use next to Exercise `ex` of the book: its own
    skill, mastered with recall, apply and find_error questions."""
    skill = EX_SKILL[ex]
    return {
        "id": "g6-maths-06-exercise-" + ex.replace(".", "-"),
        "version": 1, "schema": "0.2", "subject": "maths", "grade": 6, "tier": "middle",
        "curriculum_refs": [{"outcome": outcome, "textbook": book_ref(f"Exercise {ex}")}],
        "skills": [skill],
        "title": title,
        "estimated_minutes": minutes,
        "prerequisites": [{"skill": s} for s in prerequisites],
        "misconceptions": misconceptions,
        "mastery_criteria": {skill: {"question_types": ["recall", "apply", "find_error"], "days": 2}},
        "question_bank": {skill: bank},
        "flashcards": flashcards,
        "home_tasks": [home_task],
        "glossary": glossary,
        "steps": steps,
        "review_questions": [dict(q, skill=skill) for q in review],
        "teacher_notes": [
            f"A practice set to use next to Exercise {ex} of the PCTB Mathematics 6 book. Only the exercise number and the kinds of question come from the book; every question, number and story here is new, because the book may not be copied.",
            *notes,
            f"The numbers were worked out in content/sources/g6-maths-06/{script}; edit that script, not this file.",
        ],
        "review": REVIEW,
    }


def practice_intro(ex, kinds_en, kinds_ur, line_en, line_ur):
    """The first step: which exercise of the book this set goes with."""
    return {"id": "s1_intro", "type": "explain",
            "character": say("encouraging", line_en, line_ur),
            "text": T(f"This practice set goes with Exercise {ex} of your maths book (PCTB Mathematics 6). {kinds_en} The questions are new, not the book's, and go from easy to harder. You can keep your book open beside you.",
                      f"یہ پریکٹس آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی مشق {ex} کے ساتھ ہے۔ {kinds_ur} سوال نئے ہیں، کتاب والے نہیں، اور آسان سے مشکل کی طرف جاتے ہیں۔ آپ اپنی کتاب ساتھ کھول کر رکھ سکتے ہیں۔")}

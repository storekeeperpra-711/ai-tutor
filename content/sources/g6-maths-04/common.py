import json
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "content" / "sources"))

from why import WHY  # noqa: E402
from why_steps import add_why  # noqa: E402

REF = "PCTB Mathematics 6 (SNC 2022), Sub-domains 2 and 3: Integers, Laws of Integers"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from earlier work that these lessons build on.
TIMES_TABLES = "maths.multiplication.facts"

# Skills of the Integers unit.
INT_MEANING = "maths.integers.meaning"
INT_ADD = "maths.integers.add"
INT_SUBTRACT = "maths.integers.subtract"
INT_MULTIPLY = "maths.integers.multiply_divide"
INT_WORD_PROBLEMS = "maths.integers.word_problems"
INT_ABSOLUTE = "maths.integers.absolute_value"
INT_LAWS = "maths.integers.laws"

# The book chapters the gap lessons (absolute value, laws of integers) match.
BOOK_INTEGERS = "PCTB Mathematics 6 (SNC 2022), Sub-domain 2: Integers"
BOOK_LAWS = "PCTB Mathematics 6 (SNC 2022), Sub-domain 3: Laws of Integers"


# Practice sets that go with the book's exercises of chapter 2 (Integers), and
# the chapter test. Each has its own skill, with the unit's skills it
# practises as prerequisites.
EXERCISES = ("2.1", "2.2")
EX_SKILL = {ex: "maths.integers.ex_" + ex.replace(".", "_") for ex in EXERCISES}
CHAPTER_TEST = "maths.integers.chapter_2_test"

# Chapter 3 (Laws of Integers): its lessons are in this unit and in the
# Simplification unit (g6-maths-13). Exercise 3.3 is about BODMAS, so its
# skill belongs with the simplification skills.
SM_ORDER = "maths.simplify.order_of_operations"
SM_BRACKETS = "maths.simplify.brackets"
SM_FRACTIONS_DECIMALS = "maths.simplify.fractions_decimals"
SM_WORD_PROBLEMS = "maths.simplify.word_problems"
EX_SKILL.update({"3.1": "maths.integers.ex_3_1", "3.2": "maths.integers.ex_3_2",
                 "3.3": "maths.simplify.ex_3_3"})
CHAPTER_3_TEST = "maths.integers.chapter_3_test"


def book_ref(part):
    """'Exercise 2.1' -> the textbook string for curriculum_refs."""
    base = BOOK_LAWS if part.rstrip().split()[-1].startswith("3") else BOOK_INTEGERS
    return f"{base}, {part}"


def num(x):
    """A Fraction or Decimal as a plain JSON number: Fraction(7, 2) -> 3.5, 4 -> 4."""
    if isinstance(x, F):
        return x.numerator if x.denominator == 1 else float(x)
    return x


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







def number_question(id, prompt, answer: int, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None, character=None):
    """A step whose answer is a whole number."""
    step = {"id": id, "type": "number"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    if character:
        step["character"] = character
    step.update({"prompt": prompt, "answer": num(answer), "checker": "numeric",
                 "hint": hint, "feedback_correct": good, "feedback_wrong": bad})
    if common_wrong:
        step["common_wrong"] = [dict(w, answer=num(w["answer"])) for w in common_wrong]
    return step



def choice_question(id, prompt, options, *, qtype="apply", skill=None, character=None):
    """A step where one of the options is right."""
    step = {"id": id, "type": "choice"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    if character:
        step["character"] = character
    step.update({"prompt": prompt, "options": options})
    return step


def practice_lesson(ex, *, script, title, outcome, prerequisites, misconceptions, steps,
                    bank, review, glossary, flashcards, home_task, notes, minutes=18):
    """A practice set to use next to Exercise `ex` of the book: its own
    skill, mastered with recall, apply and find_error questions."""
    skill = EX_SKILL[ex]
    return {
        "id": "g6-maths-04-exercise-" + ex.replace(".", "-"),
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
            f"The numbers were worked out in content/sources/g6-maths-04/{script}; edit that script, not this file.",
        ],
        "review": REVIEW,
    }


def practice_intro(ex, kinds_en, kinds_ur, line_en, line_ur):
    """The first step: which exercise of the book this set goes with."""
    return {"id": "s1_intro", "type": "explain",
            "character": say("encouraging", line_en, line_ur),
            "text": T(f"This practice set goes with Exercise {ex} of your maths book (PCTB Mathematics 6). {kinds_en} The questions are new, not the book's, and go from easy to harder. You can keep your book open beside you.",
                      f"یہ پریکٹس آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی مشق {ex} کے ساتھ ہے۔ {kinds_ur} سوال نئے ہیں، کتاب والے نہیں، اور آسان سے مشکل کی طرف جاتے ہیں۔ آپ اپنی کتاب ساتھ کھول کر رکھ سکتے ہیں۔")}


def nq(id, prompt, answer, hint, good, bad, wrongs=(), qtype="apply"):
    """number_question with (en, ur) tuples; wrongs are (answer, en, ur, misconception)."""
    return number_question(id, T(*prompt), answer, T(*hint), T(*good), T(*bad),
                           common_wrong=[wrong(a, en, ur, mis) for a, en, ur, mis in wrongs], qtype=qtype)


def ch(id, prompt, right, wrongs, pos, qtype="apply"):
    """choice_question with (en, ur) prompt. right is (en, ur, feedback_en,
    feedback_ur); each wrong is the same plus an optional misconception. The
    right option goes at index pos."""
    options = [opt("x", right[0], right[1], True, right[2], right[3])]
    for w in wrongs:
        options.append(opt("x", w[0], w[1], False, w[2], w[3], w[4] if len(w) > 4 else None))
    options.insert(pos, options.pop(0))
    for k, o in enumerate(options):
        o["id"] = "abcd"[k]
    return choice_question(id, T(*prompt), options, qtype=qtype)


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
            for w in step.get("common_wrong", []):
                assert w["answer"].replace(" ", "") != step["expected"].replace(" ", ""), step["id"]
        if step["type"] == "sim":
            exp = step["expected"]["answer"]
            assert exp not in [w["answer"] for w in step.get("common_wrong", [])], step["id"]
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


def signed(n: int) -> str:
    """-3 as −3 (a real minus sign, easy to read), 4 as 4."""
    return f"−{-n}" if n < 0 else str(n)


def number_line(id, prompt, answer: int, hint, good, bad, *, lo=-10, hi=10, start=0, common_wrong=(), qtype="apply", skill=None):
    """A number-line step: the child moves the marker to [answer]."""
    assert lo <= answer <= hi and lo <= start <= hi
    step = {"id": id, "type": "sim"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    step.update({
        "renderer": "native", "sim_id": "number_line", "prompt": prompt,
        "params": {"min": lo, "max": hi, "step": 1, "start": start},
        "expected": {"result": "value", "checker": "numeric", "answer": str(answer)},
        "hint": hint, "feedback_correct": good, "feedback_wrong": bad,
    })
    if common_wrong:
        step["common_wrong"] = list(common_wrong)
    return step

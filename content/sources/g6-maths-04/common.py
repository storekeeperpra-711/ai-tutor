import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

REF = "PCTB Grade 6 Mathematics (unit to be confirmed): Integers"
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
    step.update({"prompt": prompt, "answer": answer, "checker": "numeric",
                 "hint": hint, "feedback_correct": good, "feedback_wrong": bad})
    if common_wrong:
        step["common_wrong"] = list(common_wrong)
    return step



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

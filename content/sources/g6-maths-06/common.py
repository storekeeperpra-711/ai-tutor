import json
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

REF = "PCTB Grade 6 Mathematics (unit to be confirmed): Ratio and Proportion"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from other units that these lessons build on.
UNIT_FRACTIONS = "maths.fractions.unit_fraction_meaning"
TIMES_TABLES = "maths.multiplication.facts"
EQUIVALENT_FRACTIONS = "maths.fractions.equivalent"

# Skills of the Ratio and Proportion unit.
RATIO_MEANING = "maths.ratio.meaning"
RATIO_EQUIVALENT = "maths.ratio.equivalent"
RATIO_SHARE = "maths.ratio.share"


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
    check_lesson(lesson)
    path = ROOT / "content" / "lessons" / f"{lesson['id']}.json"
    path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", path.name)

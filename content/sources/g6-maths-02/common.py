import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

REF = "Not a chapter of PCTB Mathematics 6 (SNC 2022) (revision unit): Fractions"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills of the Fractions unit (dividing by a fraction is taught in its own,
# hand-written lesson: g6-maths-02-dividing-fractions).
UNIT_FRACTIONS = "maths.fractions.unit_fraction_meaning"
TIMES_TABLES = "maths.multiplication.facts"
EQUIVALENT = "maths.fractions.equivalent"
ADD_UNLIKE = "maths.fractions.add_unlike"
MIXED = "maths.fractions.mixed_numbers"
MULTIPLY = "maths.fractions.multiply"
DIVIDE = "maths.fractions.divide_by_fraction"
WORD_PROBLEMS = "maths.fractions.word_problems"


def T(en, ur):
    return {"en": en, "ur": ur}


def opt(id, en, ur, correct, fen, fur, mis=None):
    o = {"id": id, "text": T(en, ur), "correct": correct, "feedback": T(fen, fur)}
    if mis:
        o["misconception_id"] = mis
    return o


def say(emotion, en, ur):
    return {"emotion": emotion, "say": T(en, ur)}


def frac(x: F) -> str:
    """3/4, or 2 for a whole number."""
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def unsimplified(n: int, d: int) -> str:
    """A fraction written as given, not reduced (6/8 stays 6/8)."""
    return f"{n}/{d}"


def mixed(x: F) -> str:
    """2 1/2 for 5/2; a fraction below 1 or a whole number as it is."""
    x = F(x)
    whole, rest = divmod(x.numerator, x.denominator)
    if whole == 0 or rest == 0:
        return frac(x)
    return f"{whole} {rest}/{x.denominator}"


def wrong(answer, en, ur, mis=None):
    w = {"answer": answer, "feedback": T(en, ur)}
    if mis:
        w["misconception_id"] = mis
    return w


def fraction_question(id, prompt, answer: str, hint, good, bad, *, common_wrong=(), qtype="apply", simplest=True, skill=None, character=None):
    """A typed-fraction step checked exactly by the fraction checker.

    `answer` is written the way the step expects it (5/6 or 2 3/4), so a
    student who types it back sees it in the same form."""
    step = {"id": id, "type": "text_check"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    if character:
        step["character"] = character
    step.update({
        "prompt": prompt, "checker": "fraction", "expected": answer,
        "hint": hint, "feedback_correct": good, "feedback_wrong": bad,
    })
    if simplest:
        step["require_simplest"] = True
    if common_wrong:
        step["common_wrong"] = list(common_wrong)
    return step


def check_lesson(lesson):
    """Checks the scripts can make before writing: every typed fraction
    answer differs in value from each of its common wrong answers (unless
    the wrong one is the right value in the wrong form, which the lesson
    says on purpose), and Mithu's lines are short."""
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
        if step["type"] == "number":
            assert step["answer"] not in [w["answer"] for w in step.get("common_wrong", [])], step["id"]
        line = step.get("character")
        if line:
            for lang in ("en", "ur"):
                assert len(line["say"][lang].split()) <= 30, (step["id"], lang)


def write(lesson):
    check_lesson(lesson)
    path = ROOT / "content" / "lessons" / f"{lesson['id']}.json"
    path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", path.name)

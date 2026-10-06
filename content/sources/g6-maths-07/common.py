import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

REF = "PCTB Grade 6 Mathematics (unit to be confirmed): Introduction to Algebra"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from earlier work that these lessons build on.
TIMES_TABLES = "maths.multiplication.facts"

# Skills of the Introduction to Algebra unit.
ALG_VARIABLES = "maths.algebra.variables"
ALG_SUBSTITUTION = "maths.algebra.substitution"
ALG_LIKE_TERMS = "maths.algebra.expressions_basic"
ALG_EQUATIONS = "maths.algebra.simple_equations"
ALG_WORD_PROBLEMS = "maths.algebra.word_problems"


def value(expr, **values):
    """The value of a simple expression: value("3n + 2", n=4) is 14.
    A number before a letter means multiply (3n is 3 × n)."""
    import re
    code = re.sub(r"(\d)([a-z])", r"\1*\2", expr.replace("−", "-").replace("×", "*"))
    return eval(code, {}, values)


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



def text_question(id, prompt, expected, hint, good, bad, *, accept=(), common_wrong=(), qtype="apply", skill=None):
    """A step whose answer is typed text, like 3n + 2. Spaces and capitals
    don't matter; [accept] lists other right ways to write it."""
    step = {"id": id, "type": "text_check"}
    if qtype:
        step["question_type"] = qtype
    if skill:
        step["skill"] = skill
    step.update({"prompt": prompt, "checker": "text", "expected": expected})
    if accept:
        step["accept"] = list(accept)
    step.update({"hint": hint, "feedback_correct": good, "feedback_wrong": bad})
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

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "content" / "sources"))

from why import WHY  # noqa: E402
from why_steps import add_why  # noqa: E402

REF = "PCTB Mathematics 6 (SNC 2022), Sub-domain 6: Algebraic Expressions"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from earlier work that these lessons build on.
TIMES_TABLES = "maths.multiplication.facts"

# Skills of the Introduction to Algebra unit.
ALG_VARIABLES = "maths.algebra.variables"
ALG_SUBSTITUTION = "maths.algebra.substitution"
ALG_LIKE_TERMS = "maths.algebra.expressions_basic"
ALG_EQUATIONS = "maths.algebra.simple_equations"
ALG_WORD_PROBLEMS = "maths.algebra.word_problems"
# Added after matching the PCTB Mathematics 6 book (Sub-domain 6).
ALG_SEQUENCES = "maths.algebra.sequences"
ALG_TERMS = "maths.algebra.terms"
ALG_ADD_SUBTRACT = "maths.algebra.add_subtract"

BOOK = "PCTB Mathematics 6 (SNC 2022), Sub-domain 6: Algebraic Expressions"


def term(coef, var):
    """One term without its sign: term(1, 'a') is 'a', term(7, '') is '7'."""
    if not var:
        return str(abs(coef))
    return var if abs(coef) == 1 else f"{abs(coef)}{var}"


def expr(*terms, minus="-"):
    """An expression from (coefficient, letter) pairs, zero terms left out:
    expr((7, 'a'), (1, 'b'), (-3, '')) is '7a + b - 3'."""
    out = ""
    for coef, var in terms:
        if coef == 0:
            continue
        if not out:
            out = ("-" if coef < 0 else "") + term(coef, var)
        else:
            out += f" {minus if coef < 0 else '+'} " + term(coef, var)
    return out or "0"


def expr_forms(*terms):
    """Every order a child might write the same expression in, without spaces."""
    from itertools import permutations
    kept = [t for t in terms if t[0] != 0]
    return sorted({expr(*p).replace(" ", "") for p in permutations(kept)})


def collect(*terms):
    """Adds like terms: collect((3, 'a'), (2, 'b'), (4, 'a')) is ((7, 'a'), (2, 'b'))."""
    total = {}
    for coef, var in terms:
        total[var] = total.get(var, 0) + coef
    letters = sorted(v for v in total if v) + ([""] if "" in total else [])
    return tuple((total[v], v) for v in letters)


def negate(*terms):
    return tuple((-c, v) for c, v in terms)


assert expr((7, "a"), (1, "b"), (-3, "")) == "7a + b - 3"
assert collect((3, "a"), (2, "b"), (4, "a"), (1, "b")) == ((7, "a"), (3, "b"))
assert "b+7a" in expr_forms((7, "a"), (1, "b"))


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
    add_why(lesson, WHY)
    check_lesson(lesson)
    path = ROOT / "content" / "lessons" / f"{lesson['id']}.json"
    path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", path.name)

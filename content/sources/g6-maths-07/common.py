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
            right = {x.replace(" ", "").lower() for x in [step["expected"], *step.get("accept", [])]}
            for w in step.get("common_wrong", []):
                assert w["answer"].replace(" ", "").lower() not in right, step["id"]
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


# ---------------------------------------------------------------------------
# Practice sets that go with the book's exercises of chapter 6 (Algebraic
# Expressions), and the chapter test. Each practice lesson has its own skill,
# with the chapter's skills it practises as prerequisites.
EX_SKILL = {"6.1": "maths.algebra.ex_6_1", "6.2": "maths.algebra.ex_6_2", "6.3": "maths.algebra.ex_6_3",
            "6.4": "maths.algebra.ex_6_4", "6.5": "maths.algebra.ex_6_5"}
CHAPTER_6_TEST = "maths.algebra.chapter_6_test"


def book_ref(part):
    """'Exercise 6.1' -> the textbook string for curriculum_refs."""
    return f"{REF}, {part}"


def m(n):
    """A number for reading text, with the real minus sign."""
    return str(n).replace("-", "\u2212")


def show(terms):
    """An expression for feedback text: real minus sign, e.g. 7a \u2212 3."""
    return expr(*terms, minus="\u2212").replace("-", "\u2212")


def nq(id, prompt, answer, hint, good, bad, wrongs=(), qtype="apply"):
    """number_question with (en, ur) tuples; wrongs are (answer, en, ur, misconception)."""
    assert isinstance(answer, int), id
    for w in wrongs:
        assert w[0] != answer, id
    return number_question(id, T(*prompt), answer, T(*hint), T(*good), T(*bad),
                           common_wrong=[wrong(a, en, ur, mis) for a, en, ur, mis in wrongs], qtype=qtype)


def aq(id, prompt, terms, hint, good, bad, wrongs=(), qtype="apply"):
    """A typed expression such as 5x + 9; the terms may come in any order.
    terms is a list of (coefficient, letter) pairs, already collected. wrongs
    are (terms, en, ur, misconception): each is worked out, and must differ
    from the right answer."""
    expected = expr(*terms)
    forms = [f for f in expr_forms(*terms) if f != expected.replace(" ", "")]
    cw = []
    for wt, en, ur, mis in wrongs:
        assert collect(*wt) != collect(*terms), (id, wt)
        assert expr(*wt).replace(" ", "") not in expr_forms(*terms), (id, wt)
        cw.append(wrong(expr(*wt), en, ur, mis))
    return text_question(id, T(*prompt), expected, T(*hint), T(*good), T(*bad),
                         accept=forms, common_wrong=cw, qtype=qtype)


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
        "id": "g6-maths-07-exercise-" + ex.replace(".", "-"),
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
            f"The numbers were worked out in content/sources/g6-maths-07/{script}; edit that script, not this file.",
        ],
        "review": REVIEW,
    }


def practice_intro(ex, kinds_en, kinds_ur, line_en, line_ur):
    """The first step: which exercise of the book this set goes with."""
    return {"id": "s1_intro", "type": "explain",
            "character": say("encouraging", line_en, line_ur),
            "text": T(f"This practice set goes with Exercise {ex} of your maths book (PCTB Mathematics 6). {kinds_en} The questions are new, not the book's, and go from easy to harder. You can keep your book open beside you.",
                      f"یہ پریکٹس آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی مشق {ex} کے ساتھ ہے۔ {kinds_ur} سوال نئے ہیں، کتاب والے نہیں، اور آسان سے مشکل کی طرف جاتے ہیں۔ آپ اپنی کتاب ساتھ کھول کر رکھ سکتے ہیں۔")}

import json
import sys
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "content" / "sources"))

from why import WHY  # noqa: E402
from why_steps import add_why  # noqa: E402

REF = "PCTB Mathematics 6 (SNC 2022), Sub-domain 7: Linear Equations"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}

# Skills from earlier work that these lessons build on.
ALG_SUBSTITUTION = "maths.algebra.substitution"
ALG_EQUATIONS = "maths.algebra.simple_equations"
WN_PROPERTIES = "maths.whole.properties"

# Skills of the Linear Equations unit.
EQ_CHECK = "maths.equations.check_solution"
EQ_FORMING = "maths.equations.forming"
EQ_TWO_STEP = "maths.equations.two_step"
EQ_BRACKETS = "maths.equations.brackets"
EQ_WORD_PROBLEMS = "maths.equations.word_problems"
EQ_RECOGNISE = "maths.equations.equation_or_expression"


def value(expr, **values):
    """The value of a simple expression: value("3n + 2", n=4) is 14.
    A number before a letter means multiply (3n is 3 × n)."""
    import re
    code = re.sub(r"(\d)([a-z(])", r"\1*\2", expr.replace("−", "-").replace("×", "*").replace("÷", "/"))
    return eval(code, {}, values)


def solves(equation, **values):
    """True if the values make both sides of the equation equal."""
    left, right = equation.split("=")
    return value(left, **values) == value(right, **values)


assert value("3n + 2", n=4) == 14 and value("3(x + 2)", x=5) == 21
assert solves("2x + 3 = 11", x=4) and not solves("2x + 3 = 11", x=3)


def num(x):
    """A Decimal as a plain JSON number: D('0.70') -> 0.7, D('3') -> 3."""
    if isinstance(x, D):
        x = x.normalize()
        return int(x) if x == x.to_integral_value() else float(x)
    return x


def dec(x) -> str:
    """A Decimal as children write it: 0.7, 12.05, 3."""
    x = D(x).normalize()
    return f"{x:f}" if x != x.to_integral_value() else str(int(x))


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



def number_question(id, prompt, answer, hint, good, bad, *, common_wrong=(), qtype="apply", skill=None, character=None):
    """A step whose answer is a number. A Decimal answer is written as a JSON number."""
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



def text_question(id, prompt, expected, hint, good, bad, *, accept=(), common_wrong=(), qtype="apply", skill=None):
    """A step whose answer is typed text, like x + 5 = 12. Spaces and capitals
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
# Practice sets that go with the book's exercises of chapter 7 (Linear
# Expression and Equations), and the chapter test. Each practice lesson has
# its own skill, with the chapter's skills it practises as prerequisites.
ALG_VARIABLES = "maths.algebra.variables"
ALG_TERMS = "maths.algebra.terms"
EX_SKILL = {"7.1": "maths.equations.ex_7_1", "7.2": "maths.equations.ex_7_2"}
CHAPTER_7_TEST = "maths.equations.chapter_7_test"


def book_ref(part):
    """'Exercise 7.1' -> the textbook string for curriculum_refs."""
    return f"{REF}, {part}"


def m(n):
    """A number or equation for reading text, with the real minus sign."""
    return str(n).replace("-", "\u2212")


def solve(equation, letter="x"):
    """The one whole number that solves the equation (checked by trying all)."""
    found = [v for v in range(-500, 501) if solves(equation, **{letter: v})]
    assert len(found) == 1, (equation, found)
    return found[0]


def nq(id, prompt, answer, hint, good, bad, wrongs=(), qtype="apply"):
    """number_question with (en, ur) tuples; wrongs are (answer, en, ur, misconception).
    The answer may be a whole number or a Decimal."""
    for w in wrongs:
        assert w[0] != answer, id
    return number_question(id, T(*prompt), answer, T(*hint), T(*good), T(*bad),
                           common_wrong=[wrong(a, en, ur, mis) for a, en, ur, mis in wrongs], qtype=qtype)


def eq_q(id, prompt, forms, values, hint, good, bad, wrongs=(), qtype="apply"):
    """A typed equation such as x + 5 = 12. forms are other right ways to write
    it; the first is the one shown. Each is checked to hold for `values`
    (the unknown's value in the story) and every wrong equation is checked
    not to. Typing a hyphen for the minus sign is accepted too."""
    for f in forms:
        assert solves(f, **values), (id, f)
    right = {f.replace(" ", "") for f in forms}
    accept = []
    for f in forms[1:] + [f.replace("\u2212", "-") for f in forms]:
        if f != forms[0] and f not in accept:
            accept.append(f)
    cw = []
    for eq, en, ur, mis in wrongs:
        assert not solves(eq, **values) and eq.replace(" ", "") not in right, (id, eq)
        cw.append(wrong(eq, en, ur, mis))
    return text_question(id, T(*prompt), forms[0], T(*hint), T(*good), T(*bad),
                         accept=accept, common_wrong=cw, qtype=qtype)


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
        "id": "g6-maths-16-exercise-" + ex.replace(".", "-"),
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
            f"The numbers were worked out in content/sources/g6-maths-16/{script}; edit that script, not this file.",
        ],
        "review": REVIEW,
    }


def practice_intro(ex, kinds_en, kinds_ur, line_en, line_ur):
    """The first step: which exercise of the book this set goes with."""
    return {"id": "s1_intro", "type": "explain",
            "character": say("encouraging", line_en, line_ur),
            "text": T(f"This practice set goes with Exercise {ex} of your maths book (PCTB Mathematics 6). {kinds_en} The questions are new, not the book's, and go from easy to harder. You can keep your book open beside you.",
                      f"یہ پریکٹس آپ کی ریاضی کی کتاب (پنجاب ٹیکسٹ بک بورڈ، ریاضی 6) کی مشق {ex} کے ساتھ ہے۔ {kinds_ur} سوال نئے ہیں، کتاب والے نہیں، اور آسان سے مشکل کی طرف جاتے ہیں۔ آپ اپنی کتاب ساتھ کھول کر رکھ سکتے ہیں۔")}

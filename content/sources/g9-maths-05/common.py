import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import plane  # noqa: E402

REF = "PCTB Grade 9 Mathematics (NCP 2023), Unit 5: Linear Equations and Inequalities"
REVIEW = {"status": "draft", "reviewed_by": None, "date": None}


def T(en, ur):
    return {"en": en, "ur": ur}


def opt(id, en, ur, correct, fen, fur, mis=None):
    o = {"id": id, "text": T(en, ur), "correct": correct, "feedback": T(fen, fur)}
    if mis:
        o["misconception_id"] = mis
    return o


def say(emotion, en, ur):
    return {"emotion": emotion, "say": T(en, ur)}


def num(n: Fraction) -> str:
    return str(n.numerator) if n.denominator == 1 else f"{n.numerator}/{n.denominator}"


def corners(constraints):
    return plane.corners(constraints)


def corner_text(points):
    return ", ".join(plane.describe(p) for p in points)


def values(objective, points):
    return [(p, plane.value(objective, p)) for p in points]


def best(objective, points, biggest=True):
    vals = values(objective, points)
    pick = max if biggest else min
    target = pick(v for _, v in vals)
    winners = [p for p, v in vals if v == target]
    assert len(winners) == 1, (objective, winners)
    return winners[0], target


def table(objective, points, name="z"):
    """'(0, 0): z = 0; (4, 0): z = 12' for working."""
    return "; ".join(f"{plane.describe(p)}: {name} = {num(v)}" for p, v in values(objective, points))


def region_sim(id, constraints, prompt, hint, good, wrong, *, x_max, y_max, objective=None, qtype="apply", x_min=0, y_min=0, character=None):
    params = {"constraints": constraints, "x_min": x_min, "x_max": x_max, "y_min": y_min, "y_max": y_max}
    if objective:
        params["objective"] = objective
    step = {
        "id": id, "type": "sim", "question_type": qtype, "renderer": "native", "sim_id": "feasible_region",
        "prompt": prompt, "params": params,
        "expected": {"result": "corners", "checker": "points", "answer": corner_text(corners(constraints))},
        "hint": hint, "feedback_correct": good, "feedback_wrong": wrong,
    }
    if character:
        step["character"] = character
    return step


def write(lesson):
    path = ROOT / "content" / "lessons" / f"{lesson['id']}.json"
    path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", path.name)

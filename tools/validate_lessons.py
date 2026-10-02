#!/usr/bin/env python3
"""Check lesson files against the lesson schema and the rules a schema can't express.

Usage:
    python tools/validate_lessons.py                 # every file in content/lessons/
    python tools/validate_lessons.py path/to/a.json  # only the given files

Exits with status 1 if any lesson has a problem, printing one line per problem.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "content" / "schema" / "lesson.schema.json"
LESSONS_DIR = ROOT / "content" / "lessons"

FILE_NAME = re.compile(r"^g([0-9]|1[0-2])-[a-z][a-z_]*-[0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*\.json$")


def load_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)


def all_steps(lesson: dict):
    """Yield (where, step) for every step in the lesson, including nested ones."""
    for step in lesson.get("steps", []):
        yield "steps", step
    for alt in lesson.get("alternatives", []):
        for step in alt.get("steps", []):
            yield f"alternatives/{alt.get('id')}", step
    for skill, questions in lesson.get("question_bank", {}).items():
        for q in questions:
            yield f"question_bank/{skill}", q.get("step", {})
    for q in lesson.get("review_questions", []):
        yield "review_questions", q.get("step", {})


def check_rules(lesson: dict, path: Path) -> list[str]:
    """Rules that JSON Schema can't express. Assumes the schema already passed."""
    problems = []

    if not FILE_NAME.match(path.name):
        problems.append(f"file name '{path.name}' must look like g6-maths-02-dividing-fractions.json")
    if lesson["id"] != path.stem:
        problems.append(f"id '{lesson['id']}' must equal the file name '{path.stem}'")
    grade_in_id = int(lesson["id"].split("-")[0][1:])
    if grade_in_id != lesson["grade"]:
        problems.append(f"grade {lesson['grade']} doesn't match the id (g{grade_in_id})")
    subject_in_id = lesson["id"].split("-")[1]
    if subject_in_id != lesson["subject"]:
        problems.append(f"subject '{lesson['subject']}' doesn't match the id ('{subject_in_id}')")

    seen = set()
    for step in lesson["steps"]:
        if step["id"] in seen:
            problems.append(f"step id '{step['id']}' is used twice")
        seen.add(step["id"])

    misconceptions = {m["id"] for m in lesson["misconceptions"]}
    for where, step in all_steps(lesson):
        refs = [o.get("misconception_id") for o in step.get("options", [])]
        refs += [w.get("misconception_id") for w in step.get("common_wrong", [])]
        for ref in refs:
            if ref is not None and ref not in misconceptions:
                problems.append(f"{where}/{step['id']}: misconception '{ref}' is not in misconceptions")

        if step.get("type") == "choice" and not any(o["correct"] for o in step["options"]):
            problems.append(f"{where}/{step['id']}: choice step has no correct option")

        if step.get("type") == "number":
            answers = [w["answer"] for w in step.get("common_wrong", [])]
            if step["answer"] in answers:
                problems.append(f"{where}/{step['id']}: the correct answer is also listed in common_wrong")

        if step.get("type") == "text_check":
            def squash(text: str) -> str:
                return "".join(text.split()).lower()
            right = {squash(step["expected"]), *(squash(a) for a in step.get("accept", []))}
            if step["checker"] != "linear_equation" and any(
                squash(w["answer"]) in right for w in step.get("common_wrong", [])
            ):
                problems.append(f"{where}/{step['id']}: a correct answer is also listed in common_wrong")
            if "accept" in step and step["checker"] != "text":
                problems.append(f"{where}/{step['id']}: 'accept' only works with the text checker")

    skills = set(lesson["skills"])
    for field in ("mastery_criteria", "question_bank"):
        for skill in lesson[field]:
            if skill not in skills:
                problems.append(f"{field}: skill '{skill}' is not in skills")
    for q in lesson.get("review_questions", []):
        if "skill" in q and q["skill"] not in skills:
            problems.append(f"review_questions/{q['id']}: skill '{q['skill']}' is not in skills")

    # Steps may test the lesson's skills or a prerequisite (foundation check).
    known = skills | {p["skill"] for p in lesson["prerequisites"]}
    for where, step in all_steps(lesson):
        if "skill" in step and step["skill"] not in known:
            problems.append(f"{where}/{step['id']}: skill '{step['skill']}' is not a skill or prerequisite of this lesson")

    step_ids = {step["id"] for step in lesson["steps"]}
    for alt in lesson.get("alternatives", []):
        if "for_step" in alt and alt["for_step"] not in step_ids:
            problems.append(f"alternatives/{alt['id']}: for_step '{alt['for_step']}' is not a step")

    # Mastery must be reachable: every required question type needs a question.
    available = evidence_types(lesson)
    for skill, criteria in lesson["mastery_criteria"].items():
        for qtype in criteria["question_types"]:
            if qtype not in available.get(skill, set()):
                problems.append(
                    f"mastery_criteria/{skill}: no '{qtype}' question (tag a step with question_type or add one to question_bank)"
                )

    return problems


def evidence_types(lesson: dict) -> dict[str, set[str]]:
    """Question types the lesson can ask, per skill (steps, alternatives, bank, reviews)."""
    default = lesson["skills"][0]
    found: dict[str, set[str]] = {}
    for step in lesson["steps"] + [s for alt in lesson.get("alternatives", []) for s in alt["steps"]]:
        if "question_type" in step:
            found.setdefault(step.get("skill", default), set()).add(step["question_type"])
    for skill, questions in lesson["question_bank"].items():
        for q in questions:
            found.setdefault(q.get("skill", skill), set()).add(q["type"])
    for q in lesson.get("review_questions", []):
        found.setdefault(q.get("skill", default), set()).add(q["type"])
    return found


def check_prerequisite_loops(lessons: list[dict]) -> list[str]:
    """Skills must not depend on themselves through prerequisites."""
    needs: dict[str, set[str]] = {}
    for lesson in lessons:
        for skill in lesson["skills"]:
            needs.setdefault(skill, set()).update(p["skill"] for p in lesson["prerequisites"])

    problems = []
    state: dict[str, str] = {}

    def visit(skill: str, path: list[str]) -> None:
        if state.get(skill) == "done":
            return
        if state.get(skill) == "visiting":
            loop = path[path.index(skill):] + [skill]
            problems.append("prerequisite loop: " + " -> ".join(loop))
            return
        state[skill] = "visiting"
        for need in sorted(needs.get(skill, ())):
            visit(need, path + [skill])
        state[skill] = "done"

    for skill in sorted(needs):
        visit(skill, [])
    return problems


def validate_file(path: Path, validator: Draft202012Validator) -> list[str]:
    try:
        lesson = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"not valid JSON: {e}"]

    errors = sorted(validator.iter_errors(lesson), key=lambda e: list(e.absolute_path))
    if errors:
        return [f"{'/'.join(map(str, e.absolute_path)) or '(top level)'}: {e.message}" for e in errors]
    return check_rules(lesson, path)


def main(argv: list[str]) -> int:
    validator = load_validator()
    paths = [Path(p) for p in argv] or sorted(LESSONS_DIR.glob("*.json"))
    if not paths:
        print("No lesson files found.")
        return 0

    failed = 0
    valid = []
    for path in paths:
        problems = validate_file(path, validator)
        if not problems:
            valid.append(json.loads(path.read_text(encoding="utf-8")))
        if problems:
            failed += 1
            print(f"FAIL {path.name}")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"ok   {path.name}")

    loops = check_prerequisite_loops(valid)
    for problem in loops:
        print(f"FAIL {problem}")

    print(f"\n{len(paths) - failed} of {len(paths)} lessons valid.")
    return 1 if failed or loops else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

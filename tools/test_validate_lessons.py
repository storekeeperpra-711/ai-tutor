"""Tests for validate_lessons.py. Run: python -m unittest discover tools"""

import copy
import json
import tempfile
import unittest
from pathlib import Path

import validate_lessons as v

SAMPLE = v.LESSONS_DIR / "g6-maths-02-dividing-fractions.json"


class ValidateLessonsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = v.load_validator()
        cls.lesson = json.loads(SAMPLE.read_text(encoding="utf-8"))

    def check(self, lesson, name=None):
        name = name or f"{lesson['id']}.json"
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / name
            path.write_text(json.dumps(lesson, ensure_ascii=False), encoding="utf-8")
            return v.validate_file(path, self.validator)

    def mutated(self):
        return copy.deepcopy(self.lesson)

    def assertProblem(self, problems, text):
        self.assertTrue(any(text in p for p in problems), f"'{text}' not in {problems}")

    def test_sample_lesson_is_valid(self):
        self.assertEqual(v.validate_file(SAMPLE, self.validator), [])

    def test_missing_urdu_text(self):
        lesson = self.mutated()
        del lesson["title"]["ur"]
        self.assertProblem(self.check(lesson), "'ur' is a required property")

    def test_empty_text(self):
        lesson = self.mutated()
        lesson["steps"][0]["text"]["en"] = ""
        self.assertTrue(self.check(lesson))

    def test_ai_must_output_draft_or_known_status(self):
        lesson = self.mutated()
        lesson["review"]["status"] = "published"
        self.assertProblem(self.check(lesson), "review/status")

    def test_unknown_field_rejected(self):
        lesson = self.mutated()
        lesson["difficulty"] = "hard"
        self.assertProblem(self.check(lesson), "Additional properties")

    def test_id_must_match_file_name(self):
        self.assertProblem(self.check(self.lesson, name="g6-maths-02-other.json"), "must equal the file name")

    def test_grade_must_match_id(self):
        lesson = self.mutated()
        lesson["grade"] = 7
        self.assertProblem(self.check(lesson), "doesn't match the id")

    def test_duplicate_step_id(self):
        lesson = self.mutated()
        lesson["steps"][1]["id"] = lesson["steps"][0]["id"]
        self.assertProblem(self.check(lesson), "used twice")

    def test_unknown_misconception(self):
        lesson = self.mutated()
        lesson["steps"][2]["options"][0]["misconception_id"] = "made_up"
        self.assertProblem(self.check(lesson), "'made_up' is not in misconceptions")

    def test_choice_needs_a_correct_option(self):
        lesson = self.mutated()
        for option in lesson["steps"][1]["options"]:
            option["correct"] = False
        self.assertProblem(self.check(lesson), "no correct option")

    def test_correct_answer_not_in_common_wrong(self):
        lesson = self.mutated()
        step = next(s for s in lesson["steps"] if s["type"] == "number")
        step["common_wrong"].append({"answer": step["answer"], "feedback": {"en": "x", "ur": "x"}})
        self.assertProblem(self.check(lesson), "also listed in common_wrong")

    def test_mastery_skill_must_be_listed(self):
        lesson = self.mutated()
        lesson["mastery_criteria"]["maths.other.skill"] = {"question_types": ["recall"], "days": 1}
        self.assertProblem(self.check(lesson), "'maths.other.skill' is not in skills")

    def test_number_step_needs_hint(self):
        lesson = self.mutated()
        step = next(s for s in lesson["steps"] if s["type"] == "number")
        del step["hint"]
        self.assertProblem(self.check(lesson), "'hint' is a required property")


    def test_text_check_common_wrong_must_be_wrong(self):
        lesson = json.loads((v.LESSONS_DIR / "g10-chemistry-15-balancing-equations.json").read_text(encoding="utf-8"))
        step = next(s for s in lesson["steps"] if s["type"] == "text_check")
        step["common_wrong"] = [{"answer": step["expected"].replace(" ", ""), "feedback": {"en": "x", "ur": "x"}}]
        self.assertProblem(self.check(lesson), "a correct answer is also listed in common_wrong")

    def test_text_check_needs_known_checker(self):
        lesson = json.loads((v.LESSONS_DIR / "g10-chemistry-15-balancing-equations.json").read_text(encoding="utf-8"))
        step = next(s for s in lesson["steps"] if s["type"] == "text_check")
        step["checker"] = "magic"
        self.assertTrue(self.check(lesson))


    def test_mastery_needs_a_question_of_each_type(self):
        lesson = self.mutated()
        lesson["mastery_criteria"]["maths.fractions.divide_by_fraction"]["question_types"].append("exam_style")
        self.assertProblem(self.check(lesson), "no 'exam_style' question")

    def test_step_skill_must_be_known(self):
        lesson = self.mutated()
        lesson["steps"][1]["skill"] = "maths.unknown.skill"
        self.assertProblem(self.check(lesson), "is not a skill or prerequisite")

    def test_alternative_must_point_at_a_step(self):
        lesson = self.mutated()
        lesson["alternatives"][0]["for_step"] = "no_such_step"
        self.assertProblem(self.check(lesson), "for_step 'no_such_step'")

    def test_prerequisite_loop(self):
        a = {"skills": ["maths.a.one"], "prerequisites": [{"skill": "maths.b.two"}]}
        b = {"skills": ["maths.b.two"], "prerequisites": [{"skill": "maths.a.one"}]}
        problems = v.check_prerequisite_loops([a, b])
        self.assertProblem(problems, "prerequisite loop")
        self.assertEqual(v.check_prerequisite_loops([a]), [])


if __name__ == "__main__":
    unittest.main()

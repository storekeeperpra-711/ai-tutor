import json
import tempfile
import unittest
from pathlib import Path

import upload


class DictStore:
    def __init__(self, docs=None):
        self.docs = dict(docs or {})
        self.writes = []

    def get(self, path):
        doc = self.docs.get(path)
        return json.loads(json.dumps(doc)) if doc is not None else None

    def set(self, path, data):
        self.writes.append(path)
        self.docs[path] = data

    def delete(self, path):
        self.writes.append(f"delete {path}")
        self.docs.pop(path, None)


def lesson(lesson_id, title="Hello"):
    content = upload.canonical({"id": lesson_id, "title": {"en": title, "ur": title}})
    return upload.LocalLesson(lesson_id, content, upload.fingerprint(content))


def publish(lessons, target, reviews=None):
    changes = upload.plan(lessons, target, reviews)
    upload.apply(changes, lessons, target, "2026-10-03T00:00:00+00:00", mark_for_review=reviews is None)
    return {c.id: c for c in changes}


class FingerprintTest(unittest.TestCase):
    def test_same_lesson_same_hash_whatever_the_spacing(self):
        a = upload.canonical(json.loads('{"b": 1, "a": [1, 2]}'))
        b = upload.canonical(json.loads('{\n  "a": [1,2],\n  "b": 1\n}'))
        self.assertEqual(upload.fingerprint(a), upload.fingerprint(b))

    def test_any_change_changes_the_hash(self):
        self.assertNotEqual(lesson("x", "Hello").hash, lesson("x", "Hello!").hash)

    def test_urdu_kept_as_text(self):
        self.assertIn("سلام", upload.canonical({"t": "سلام"}))

    def test_real_lessons_load(self):
        lessons = upload.load_local(upload.validate_lessons.LESSONS_DIR)
        self.assertGreaterEqual(len(lessons), 4)
        for found in lessons:
            self.assertEqual(json.loads(found.content)["id"], found.id)

    def test_lesson_id_comes_from_the_file(self):
        with tempfile.TemporaryDirectory() as folder:
            Path(folder, "a.json").write_text('{"id": "g9-maths-01-x"}', encoding="utf-8")
            self.assertEqual(upload.load_local(Path(folder))[0].id, "g9-maths-01-x")


class DevTest(unittest.TestCase):
    def test_first_publish_is_version_1_and_waits_for_review(self):
        dev = DictStore()
        changes = publish([lesson("a")], dev)
        self.assertEqual(changes["a"].action, "new")
        published = dev.docs["published_lessons/a"]
        self.assertEqual(published["version"], 1)
        self.assertEqual(json.loads(published["content"])["id"], "a")
        self.assertEqual(dev.docs["lesson_catalog/current"]["lessons"]["a"]["version"], 1)
        self.assertEqual(dev.docs["lesson_reviews/a"]["status"], "in_review")

    def test_catalog_written_after_the_lessons(self):
        dev = DictStore()
        publish([lesson("a"), lesson("b")], dev)
        self.assertEqual(dev.writes[-1], "lesson_catalog/current")

    def test_unchanged_lesson_is_not_written_again(self):
        dev = DictStore()
        publish([lesson("a")], dev)
        dev.writes.clear()
        changes = publish([lesson("a")], dev)
        self.assertEqual(changes["a"].action, "unchanged")
        self.assertEqual(dev.writes, [])

    def test_changed_lesson_is_a_new_version_and_goes_back_to_review(self):
        dev = DictStore()
        publish([lesson("a")], dev)
        dev.docs["lesson_reviews/a"]["status"] = "approved"
        changes = publish([lesson("a", "Changed")], dev)
        self.assertEqual(changes["a"].action, "update")
        self.assertEqual(dev.docs["published_lessons/a"]["version"], 2)
        self.assertEqual(dev.docs["lesson_reviews/a"]["status"], "in_review")
        self.assertEqual(dev.docs["lesson_reviews/a"]["hash"], lesson("a", "Changed").hash)

    def test_deleted_lesson_is_removed(self):
        dev = DictStore()
        publish([lesson("a"), lesson("b")], dev)
        changes = publish([lesson("a")], dev)
        self.assertEqual(changes["b"].action, "remove")
        self.assertNotIn("b", dev.docs["lesson_catalog/current"]["lessons"])
        self.assertNotIn("published_lessons/b", dev.docs)


class ProdTest(unittest.TestCase):
    def setUp(self):
        self.reviews = DictStore()
        publish([lesson("a"), lesson("b")], self.reviews)

    def approve(self, found):
        self.reviews.docs[f"lesson_reviews/{found.id}"] = {"hash": found.hash, "status": "approved"}

    def test_only_approved_lessons_are_published(self):
        self.approve(lesson("a"))
        prod = DictStore()
        changes = publish([lesson("a"), lesson("b")], prod, self.reviews)
        self.assertEqual(changes["a"].action, "new")
        self.assertEqual(changes["b"].action, "waiting")
        self.assertEqual(set(prod.docs["lesson_catalog/current"]["lessons"]), {"a"})
        self.assertNotIn("published_lessons/b", prod.docs)

    def test_prod_never_gets_review_documents(self):
        self.approve(lesson("a"))
        prod = DictStore()
        publish([lesson("a")], prod, self.reviews)
        self.assertFalse(any(path.startswith("lesson_reviews/") for path in prod.docs))

    def test_needs_changes_is_not_published(self):
        self.reviews.docs["lesson_reviews/a"] = {"hash": lesson("a").hash, "status": "changes_requested"}
        prod = DictStore()
        changes = publish([lesson("a")], prod, self.reviews)
        self.assertEqual(changes["a"].action, "waiting")
        self.assertNotIn("lesson_catalog/current", prod.docs)

    def test_lesson_changed_after_approval_keeps_the_approved_version(self):
        self.approve(lesson("a"))
        prod = DictStore()
        publish([lesson("a")], prod, self.reviews)
        changes = publish([lesson("a", "Changed")], prod, self.reviews)
        self.assertEqual(changes["a"].action, "waiting")
        self.assertIn("v1 stays", changes["a"].note)
        self.assertEqual(prod.docs["published_lessons/a"]["hash"], lesson("a").hash)

        self.approve(lesson("a", "Changed"))
        changes = publish([lesson("a", "Changed")], prod, self.reviews)
        self.assertEqual(changes["a"].action, "update")
        self.assertEqual(prod.docs["published_lessons/a"]["version"], 2)


if __name__ == "__main__":
    unittest.main()

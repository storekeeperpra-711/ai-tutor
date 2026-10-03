"""Publishes lessons to Firestore, with versions (Phase 8).

Run by the "Publish lessons" GitHub Action, or by hand:

    python tools/upload.py dev           # every lesson, as a draft for review
    python tools/upload.py prod          # only lessons a teacher approved
    python tools/upload.py dev --dry-run # show what would change

Credentials come from environment variables holding the Firebase key file's
text: FIREBASE_SERVICE_ACCOUNT (the target project) and, for prod,
FIREBASE_SERVICE_ACCOUNT_DEV (where the reviews are). Needs
`pip install -r tools/upload-requirements.txt`.

Firestore layout, in each project:

    lesson_catalog/current     lessons: {id: {version, hash}}, updated_at
    published_lessons/{id}     version, hash, content (the lesson's JSON), published_at
    lesson_reviews/{id}        hash, status (in_review | approved | changes_requested),
                               ... (dev only; written by the review screens)

A lesson's hash is a fingerprint of its content, so any change makes a new
version. Prod gets a lesson only when its exact hash was approved in dev; a
lesson changed after approval keeps its old approved version in prod until
it is approved again.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_lessons  # noqa: E402

CATALOG = "lesson_catalog/current"
PUBLISHED = "published_lessons"
REVIEWS = "lesson_reviews"

# Bumped when the app needs a newer reader for published lessons.
CONTENT_FORMAT = 1


class Store(Protocol):
    """The few Firestore calls we need, so tests can use a dict."""

    def get(self, path: str) -> dict | None: ...

    def set(self, path: str, data: dict) -> None: ...

    def delete(self, path: str) -> None: ...


@dataclass(frozen=True)
class LocalLesson:
    id: str
    content: str  # canonical JSON
    hash: str


@dataclass(frozen=True)
class Change:
    id: str
    action: str  # new, update, remove, unchanged, waiting
    version: int
    hash: str
    note: str = ""

    def line(self) -> str:
        text = f"{self.action:<9} {self.id}"
        if self.action != "remove":
            text += f"  v{self.version} ({self.hash[:8]})"
        return text + (f"  {self.note}" if self.note else "")


def canonical(lesson: dict) -> str:
    """The lesson as compact JSON with sorted keys: the same lesson always
    gives the same text, whatever the file's spacing."""
    return json.dumps(lesson, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def fingerprint(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]


def load_local(lessons_dir: Path) -> list[LocalLesson]:
    found = []
    for path in sorted(lessons_dir.glob("*.json")):
        content = canonical(json.loads(path.read_text(encoding="utf-8")))
        lesson_id = json.loads(content)["id"]
        found.append(LocalLesson(lesson_id, content, fingerprint(content)))
    return found


def approved_hash(reviews: Store, lesson_id: str) -> str | None:
    review = reviews.get(f"{REVIEWS}/{lesson_id}")
    if review and review.get("status") == "approved":
        return review.get("hash")
    return None


def plan(lessons: list[LocalLesson], target: Store, reviews: Store | None) -> list[Change]:
    """What publishing would change. With [reviews] (prod), only approved
    versions are published."""
    catalog = (target.get(CATALOG) or {}).get("lessons", {})
    changes = []
    for lesson in lessons:
        current = catalog.get(lesson.id)
        old_version = current["version"] if current else 0
        if reviews is not None and approved_hash(reviews, lesson.id) != lesson.hash:
            note = "not approved yet"
            if current:
                note += f"; v{old_version} stays"
            changes.append(Change(lesson.id, "waiting", old_version, lesson.hash, note))
        elif current and current["hash"] == lesson.hash:
            changes.append(Change(lesson.id, "unchanged", old_version, lesson.hash))
        else:
            action = "update" if current else "new"
            changes.append(Change(lesson.id, action, old_version + 1, lesson.hash))
    local_ids = {lesson.id for lesson in lessons}
    for lesson_id, entry in sorted(catalog.items()):
        if lesson_id not in local_ids:
            changes.append(Change(lesson_id, "remove", entry["version"], entry["hash"]))
    return changes


def apply(changes: list[Change], lessons: list[LocalLesson], target: Store, now: str, mark_for_review: bool) -> None:
    """Writes the lessons first and the catalog last, so a phone never sees a
    catalog entry whose lesson isn't there yet."""
    by_id = {lesson.id: lesson for lesson in lessons}
    catalog = dict((target.get(CATALOG) or {}).get("lessons", {}))
    for change in changes:
        if change.action in ("new", "update"):
            target.set(
                f"{PUBLISHED}/{change.id}",
                {
                    "version": change.version,
                    "hash": change.hash,
                    "format": CONTENT_FORMAT,
                    "content": by_id[change.id].content,
                    "published_at": now,
                },
            )
            catalog[change.id] = {"version": change.version, "hash": change.hash}
            if mark_for_review:
                review = target.get(f"{REVIEWS}/{change.id}") or {}
                if review.get("hash") != change.hash:
                    target.set(
                        f"{REVIEWS}/{change.id}",
                        {"hash": change.hash, "version": change.version, "status": "in_review", "submitted_at": now},
                    )
        elif change.action == "remove":
            catalog.pop(change.id, None)
    if any(c.action in ("new", "update", "remove") for c in changes):
        target.set(CATALOG, {"lessons": catalog, "format": CONTENT_FORMAT, "updated_at": now})
    for change in changes:
        if change.action == "remove":
            target.delete(f"{PUBLISHED}/{change.id}")


class FirestoreStore:
    """A Firestore project, reached with a service account."""

    def __init__(self, key_json: str, name: str):
        import firebase_admin
        from firebase_admin import credentials, firestore

        key = json.loads(key_json)
        app = firebase_admin.initialize_app(credentials.Certificate(key), name=name)
        self._db = firestore.client(app)
        self.project = key.get("project_id", "?")

    def get(self, path: str) -> dict | None:
        snapshot = self._db.document(path).get()
        return snapshot.to_dict() if snapshot.exists else None

    def set(self, path: str, data: dict) -> None:
        self._db.document(path).set(data)

    def delete(self, path: str) -> None:
        self._db.document(path).delete()


def key_from_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        sys.exit(f"{name} is not set. In GitHub it comes from the repository secrets (docs/setup/ai-setup.md).")
    return value


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("target", choices=["dev", "prod"])
    parser.add_argument("--dry-run", action="store_true", help="show what would change; write nothing")
    args = parser.parse_args(argv)

    print("Checking lessons...")
    if validate_lessons.main([]) != 0:
        print("\nNothing published: fix the lessons above first.")
        return 1

    lessons = load_local(validate_lessons.LESSONS_DIR)
    target = FirestoreStore(key_from_env("FIREBASE_SERVICE_ACCOUNT"), "target")
    reviews = None
    if args.target == "prod":
        reviews = FirestoreStore(key_from_env("FIREBASE_SERVICE_ACCOUNT_DEV"), "reviews")
        if reviews.project == target.project:
            sys.exit("The dev and prod keys are for the same Firebase project.")

    changes = plan(lessons, target, reviews)
    print(f"\nLessons for {args.target} ({target.project}):")
    for change in changes:
        print("  " + change.line())
    if args.dry_run:
        print("\nDry run: nothing written.")
        return 0

    from datetime import datetime, timezone

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    apply(changes, lessons, target, now, mark_for_review=args.target == "dev")
    published = sum(c.action in ("new", "update") for c in changes)
    removed = sum(c.action == "remove" for c in changes)
    print(f"\nPublished {published}, removed {removed}.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

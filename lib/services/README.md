# services

Things the screens use that are not screens.

| File | What |
|---|---|
| `local_db.dart` | On-phone SQLite database (drift): profiles, lesson progress, step results, the sync queue |
| `auth_service.dart` | Firebase sign-in: the phone's anonymous account, parent and teacher email accounts |
| `remote_store.dart` | Firestore reads and writes (layout in docs/plan/03-phase-3.md) |
| `sync_service.dart` | Copies the queue to Firestore when online |
| `connectivity.dart` | Online or offline |
| `profiles.dart` | Current learner, PIN hashing, ids |
| `account_actions.dart` | Sign up, sign in, sign out, add and remove learners |

Coming later: content download/cache (Phase 8), AI client (Phase 6), audio (Phase 7).

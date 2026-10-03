import 'dart:async';
import 'dart:convert';

import 'package:crypto/crypto.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../models/lesson.dart';
import '../models/lesson_step.dart';
import '../services/auth_service.dart';
import '../services/connectivity.dart';
import '../services/local_db.dart';
import '../services/remote_store.dart';
import 'lesson_repository.dart';

/// The newest published-lesson format this app reads (CONTENT_FORMAT in
/// tools/upload.py).
const supportedLessonFormat = 1;

/// The upload tool's fingerprint of a lesson's JSON text.
String lessonFingerprint(String content) =>
    sha256.convert(utf8.encode(content)).toString().substring(0, 16);

/// Downloads lessons published with tools/upload.py (Phase 8), so new and
/// corrected lessons reach phones without a new app version.
///
/// Costs one Firestore read per check, plus one per changed lesson.
class LessonUpdater {
  LessonUpdater({
    required this.db,
    required this.remote,
    DateTime Function()? now,
  }) : _now = now ?? DateTime.now;

  final LocalDb db;
  final RemoteStore remote;
  final DateTime Function() _now;

  /// Checks at most this often, unless forced.
  static const checkEvery = Duration(hours: 1);

  DateTime? _lastCheck;
  var _running = false;

  /// Downloads new and changed lessons and forgets removed ones. Returns
  /// whether anything changed. Never throws: offline, it changes nothing.
  Future<bool> update({bool force = false}) async {
    final now = _now();
    if (_running) return false;
    if (!force &&
        _lastCheck != null &&
        now.difference(_lastCheck!) < checkEvery) {
      return false;
    }
    _running = true;
    var changed = false;
    try {
      final catalog = await remote.fetchLessonCatalog();
      final saved = {for (final l in await db.allDownloadedLessons()) l.id: l};
      for (final MapEntry(key: id, value: entry) in catalog.entries) {
        if (saved[id]?.hash == entry.hash) continue;
        final published = await remote.fetchPublishedLesson(id);
        if (published == null || !readable(id, published)) continue;
        await db.saveDownloadedLesson(
          DownloadedLesson(
            id: id,
            version: published.version,
            hash: published.hash,
            content: published.content,
            downloadedAt: now,
          ),
        );
        changed = true;
      }
      for (final id in saved.keys) {
        if (catalog.containsKey(id)) continue;
        await db.deleteDownloadedLesson(id);
        changed = true;
      }
      _lastCheck = now;
    } catch (_) {
      // Offline or a server problem: try again next time.
    } finally {
      _running = false;
    }
    return changed;
  }

  /// Whether this app can show [published]. One it can't (made for a newer
  /// app, or damaged) is skipped, and the phone keeps what it had.
  static bool readable(String id, PublishedLesson published) {
    if (published.format > supportedLessonFormat) return false;
    if (lessonFingerprint(published.content) != published.hash) return false;
    try {
      final json = jsonDecode(published.content) as Map<String, dynamic>;
      final lesson = Lesson.fromJson(json);
      return lesson.id == id && !_hasUnknownSteps(lesson);
    } catch (_) {
      return false;
    }
  }

  static bool _hasUnknownSteps(Lesson lesson) => [
    ...lesson.steps,
    for (final a in lesson.alternatives) ...a.steps,
    for (final q in lesson.questionBank.values.expand((q) => q)) q.step,
    for (final q in lesson.reviewQuestions) q.step,
  ].any((s) => s is UnsupportedStep);
}

/// Checks for lessons when the phone is online and signed in.
final lessonUpdaterProvider = Provider<LessonUpdater>((ref) {
  final updater = LessonUpdater(
    db: ref.watch(localDbProvider),
    remote: ref.watch(remoteStoreProvider),
  );
  Future<void> check() => checkLessons(ref, updater);

  ref.listen(onlineProvider, (previous, next) {
    if (next.value ?? false) unawaited(check());
  }, fireImmediately: true);
  ref.listen(authUserProvider, (previous, next) {
    if (next.value != null) unawaited(check());
  });
  return updater;
});

/// Checks for lessons (at most hourly unless [force]) and refreshes the
/// lesson lists if any changed. Returns whether any did.
Future<bool> checkLessons(
  Ref ref,
  LessonUpdater updater, {
  bool force = false,
}) async {
  // Published lessons are only readable when signed in.
  if (ref.read(authServiceProvider).currentUser == null) return false;
  final changed = await updater.update(force: force);
  if (changed && ref.mounted) {
    ref
      ..invalidate(lessonIdsProvider)
      ..invalidate(lessonProvider);
  }
  return changed;
}

/// Checks for new lessons right now, e.g. when a teacher opens the review
/// list.
final checkLessonsNowProvider = Provider<Future<bool> Function()>(
  (ref) =>
      () => checkLessons(ref, ref.read(lessonUpdaterProvider), force: true),
);

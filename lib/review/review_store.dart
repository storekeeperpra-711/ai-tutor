import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/services.dart' show appFlavor;
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../services/auth_service.dart';

/// Where a lesson version is in teacher review (Phase 8).
enum ReviewStatus {
  inReview('in_review'),
  approved('approved'),
  changesRequested('changes_requested');

  const ReviewStatus(this.wire);

  /// The value in Firestore.
  final String wire;

  static ReviewStatus parse(Object? value) => values.firstWhere(
    (s) => s.wire == value,
    orElse: () => ReviewStatus.inReview,
  );
}

/// `lesson_reviews/{lessonId}`: the version waiting for review (written by
/// tools/upload.py) and the teacher's decision.
class LessonReview {
  const LessonReview({
    required this.lessonId,
    required this.hash,
    required this.version,
    required this.status,
    this.reviewer,
  });

  final String lessonId;

  /// The fingerprint of the version under review.
  final String hash;
  final int version;
  final ReviewStatus status;

  /// Who decided, once someone has.
  final String? reviewer;
}

/// A teacher's note on a step, or on the whole lesson ([generalNote]).
class ReviewNote {
  const ReviewNote({
    required this.stepId,
    required this.text,
    required this.author,
    required this.hash,
    this.createdAt,
  });

  final String stepId;
  final String text;
  final String author;

  /// The lesson version the note is about.
  final String hash;

  /// null until the server has stamped it.
  final DateTime? createdAt;
}

/// [ReviewNote.stepId] for a note about the whole lesson.
const generalNote = 'general';

/// Teacher review in Firestore, behind an interface so tests can use a
/// fake. Only reviewers can read or write any of it (firestore.rules).
abstract class ReviewStore {
  /// Whether the signed-in account may review lessons.
  Future<bool> isReviewer();

  Future<List<LessonReview>> reviews();

  /// Notes on [lessonId], oldest first.
  Future<List<ReviewNote>> notes(String lessonId);

  Future<void> addNote(String lessonId, ReviewNote note);

  /// Approves the version [hash], or asks for changes.
  Future<void> decide(
    String lessonId, {
    required String hash,
    required bool approved,
    required String reviewer,
  });
}

class FirestoreReviewStore implements ReviewStore {
  FirestoreReviewStore(this._db);

  final FirebaseFirestore _db;

  CollectionReference<Map<String, dynamic>> get _reviews =>
      _db.collection('lesson_reviews');

  // Reviews change on the server; a cached copy could approve an old one.
  static const _fresh = GetOptions(source: Source.server);

  @override
  Future<bool> isReviewer() async {
    try {
      await _db.doc('config/reviewers').get(_fresh);
      return true;
    } on FirebaseException catch (e) {
      if (e.code == 'permission-denied') return false;
      rethrow;
    }
  }

  @override
  Future<List<LessonReview>> reviews() async {
    final snap = await _reviews.get(_fresh);
    return [for (final doc in snap.docs) reviewFromJson(doc.id, doc.data())];
  }

  @override
  Future<List<ReviewNote>> notes(String lessonId) async {
    final snap = await _reviews
        .doc(lessonId)
        .collection('notes')
        .orderBy('created_at')
        .get(_fresh);
    return [for (final doc in snap.docs) noteFromJson(doc.data())];
  }

  @override
  Future<void> addNote(String lessonId, ReviewNote note) =>
      _reviews.doc(lessonId).collection('notes').add({
        'step_id': note.stepId,
        'text': note.text,
        'author': note.author,
        'hash': note.hash,
        'created_at': FieldValue.serverTimestamp(),
      });

  @override
  Future<void> decide(
    String lessonId, {
    required String hash,
    required bool approved,
    required String reviewer,
  }) => _reviews.doc(lessonId).update({
    'status':
        (approved ? ReviewStatus.approved : ReviewStatus.changesRequested).wire,
    'approved_hash': approved ? hash : null,
    'reviewer': reviewer,
    'decided_at': FieldValue.serverTimestamp(),
  });
}

LessonReview reviewFromJson(String lessonId, Map<String, dynamic> json) =>
    LessonReview(
      lessonId: lessonId,
      hash: json['hash'] as String,
      version: (json['version'] as num? ?? 0).toInt(),
      status: ReviewStatus.parse(json['status']),
      reviewer: json['reviewer'] as String?,
    );

ReviewNote noteFromJson(Map<String, dynamic> json) => ReviewNote(
  stepId: json['step_id'] as String,
  text: json['text'] as String,
  author: json['author'] as String,
  hash: json['hash'] as String,
  createdAt: switch (json['created_at']) {
    final Timestamp t => t.toDate(),
    final DateTime d => d,
    _ => null,
  },
);

final reviewStoreProvider = Provider<ReviewStore>(
  (ref) => throw UnimplementedError('Override in main() before use'),
);

/// Whether the review screens are offered: only in the dev app, where
/// teachers review drafts (docs/plan/08-phase-8.md).
final reviewOfferedProvider = Provider<bool>((ref) => appFlavor == 'dev');

/// Why the signed-in account can or can't review.
enum ReviewAccess { signedOut, unverified, notReviewer, reviewer }

final reviewAccessProvider = FutureProvider<ReviewAccess>((ref) async {
  final user = ref.watch(authUserProvider).value;
  if (user == null || !user.isAdult) return ReviewAccess.signedOut;
  if (!user.emailVerified) return ReviewAccess.unverified;
  return await ref.watch(reviewStoreProvider).isReviewer()
      ? ReviewAccess.reviewer
      : ReviewAccess.notReviewer;
});

final reviewsProvider = FutureProvider<List<LessonReview>>((ref) async {
  final reviews = await ref.watch(reviewStoreProvider).reviews();
  return reviews..sort((a, b) => a.lessonId.compareTo(b.lessonId));
});

final reviewNotesProvider = FutureProvider.family<List<ReviewNote>, String>(
  (ref, lessonId) => ref.watch(reviewStoreProvider).notes(lessonId),
);

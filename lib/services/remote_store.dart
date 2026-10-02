import 'dart:convert';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'local_db.dart';

/// Account roles, stored in `accounts/{uid}.role`.
enum AccountRole { device, parent, teacher }

/// Firestore, behind an interface so tests can use a fake.
///
/// Layout (see docs/plan/03-phase-3.md and firestore.rules):
/// ```
/// accounts/{uid}                                   role
/// accounts/{uid}/students/{studentId}              first_name, grade, ...
/// accounts/{uid}/students/{studentId}/progress/{lessonId}
/// ```
abstract class RemoteStore {
  Future<void> setRole(String uid, AccountRole role);
  Future<void> putStudent(String uid, Student student);

  /// One merged write per upload: where to resume plus the new answers.
  Future<void> putProgress(String uid, ProgressUpload upload);

  Future<void> deleteStudent(String uid, String studentId);

  /// Everything saved in the account, to restore it on a new phone.
  Future<RemoteData> fetchAll(String uid);
}

class FirestoreRemoteStore implements RemoteStore {
  FirestoreRemoteStore(this._db);

  final FirebaseFirestore _db;

  DocumentReference<Map<String, dynamic>> _account(String uid) =>
      _db.collection('accounts').doc(uid);

  CollectionReference<Map<String, dynamic>> _students(String uid) =>
      _account(uid).collection('students');

  @override
  Future<void> setRole(String uid, AccountRole role) =>
      _account(uid).set({'role': role.name}, SetOptions(merge: true));

  @override
  Future<void> putStudent(String uid, Student student) =>
      _students(uid).doc(student.id).set(studentToJson(student));

  @override
  Future<void> putProgress(String uid, ProgressUpload upload) =>
      _students(uid)
          .doc(upload.progress.studentId)
          .collection('progress')
          .doc(upload.progress.lessonId)
          .set(progressToJson(upload), SetOptions(merge: true));

  @override
  Future<void> deleteStudent(String uid, String studentId) async {
    final student = _students(uid).doc(studentId);
    final progress = await student.collection('progress').get();
    final batch = _db.batch();
    for (final doc in progress.docs) {
      batch.delete(doc.reference);
    }
    batch.delete(student);
    await batch.commit();
  }

  @override
  Future<RemoteData> fetchAll(String uid) async {
    final account = await _account(uid).get();
    final students = <Student>[];
    final progress = <LessonProgress>[];
    final steps = <StepResultRow>[];
    for (final doc in (await _students(uid).get()).docs) {
      students.add(studentFromJson(doc.id, doc.data()));
      final lessons = await doc.reference.collection('progress').get();
      for (final p in lessons.docs) {
        final (row, stepRows) = progressFromJson(doc.id, p.id, p.data());
        progress.add(row);
        steps.addAll(stepRows);
      }
    }
    return RemoteData(
      role: account.data()?['role'] as String?,
      students: students,
      progress: progress,
      steps: steps,
    );
  }
}

// JSON conversion, shared with the test fake.

DateTime _date(Object? value) => switch (value) {
  final Timestamp t => t.toDate(),
  final DateTime d => d,
  _ => DateTime.fromMillisecondsSinceEpoch(0),
};

Map<String, Object?> studentToJson(Student s) => {
  'first_name': s.firstName,
  'grade': s.grade,
  'avatar': s.avatar,
  'pin_hash': s.pinHash,
  'created_at': Timestamp.fromDate(s.createdAt),
  'consent_at': Timestamp.fromDate(s.consentAt),
};

Student studentFromJson(String id, Map<String, dynamic> json) => Student(
  id: id,
  firstName: json['first_name'] as String,
  grade: json['grade'] as int,
  avatar: json['avatar'] as String,
  pinHash: json['pin_hash'] as String?,
  createdAt: _date(json['created_at']),
  consentAt: _date(json['consent_at']),
  synced: true,
);

Map<String, Object?> progressToJson(ProgressUpload upload) {
  final p = upload.progress;
  return {
    'lesson_version': p.lessonVersion,
    'next_step': p.nextStep,
    'completed': p.completed,
    'updated_at': Timestamp.fromDate(p.updatedAt),
    // With a merged write, only these steps change; earlier ones stay.
    'steps': {
      for (final r in upload.steps)
        r.stepId: {
          'correct': r.correct,
          'attempts': r.attempts,
          'misconceptions': jsonDecode(r.misconceptions),
          'at': Timestamp.fromDate(r.answeredAt),
        },
    },
  };
}

(LessonProgress, List<StepResultRow>) progressFromJson(
  String studentId,
  String lessonId,
  Map<String, dynamic> json,
) {
  final steps = (json['steps'] as Map<String, dynamic>? ?? {}).entries.map((e) {
    final step = e.value as Map<String, dynamic>;
    return StepResultRow(
      studentId: studentId,
      lessonId: lessonId,
      stepId: e.key,
      correct: step['correct'] as bool?,
      attempts: step['attempts'] as int? ?? 0,
      misconceptions: jsonEncode(step['misconceptions'] ?? []),
      answeredAt: _date(step['at']),
      synced: true,
    );
  }).toList();
  return (
    LessonProgress(
      studentId: studentId,
      lessonId: lessonId,
      lessonVersion: json['lesson_version'] as int? ?? 1,
      nextStep: json['next_step'] as int? ?? 0,
      completed: json['completed'] as bool? ?? false,
      updatedAt: _date(json['updated_at']),
    ),
    steps,
  );
}

final remoteStoreProvider = Provider<RemoteStore>(
  (ref) => throw UnimplementedError('Override in main() before use'),
);

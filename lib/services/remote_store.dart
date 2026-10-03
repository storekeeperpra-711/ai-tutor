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
/// accounts/{uid}/students/{studentId}/skills/{skill}
/// accounts/{uid}/students/{studentId}/reports/{week}   (written by the server)
/// ai_queue/{id}                                    answers waiting for AI
/// ```
abstract class RemoteStore {
  Future<void> setRole(String uid, AccountRole role);
  Future<void> putStudent(String uid, Student student);

  /// One merged write per upload: where to resume plus the new answers.
  Future<void> putProgress(String uid, ProgressUpload upload);

  /// The mastery engine's state for one child and skill.
  Future<void> putSkill(String uid, SkillStateRow row);

  Future<void> deleteStudent(String uid, String studentId);

  /// Everything saved in the account, to restore it on a new phone.
  Future<RemoteData> fetchAll(String uid);

  /// An answer that waits for the batch job's AI reply (Phase 6).
  Future<void> putQueuedAnswer(String uid, QueuedAnswer answer);

  /// The server's replies to queued answers, by id. Answers still waiting
  /// are left out.
  Future<Map<String, QueueReply>> fetchReplies(String uid, List<String> ids);

  /// Weekly notes for parents, newest first.
  Future<List<WeeklyReport>> fetchReports(String uid, String studentId);
}

/// The batch job's reply to a queued answer.
class QueueReply {
  const QueueReply({required this.status, this.level, this.reply});

  /// answered or failed.
  final String status;
  final String? level;
  final String? reply;
}

/// A weekly note for parents (Phase 6).
class WeeklyReport {
  const WeeklyReport({
    required this.week,
    required this.noteEn,
    required this.noteUr,
    required this.stats,
  });

  /// The Sunday it was written, e.g. 2026-10-04.
  final String week;
  final String noteEn;
  final String noteUr;

  /// lessons_finished, questions_answered, active_days, skills_mastered, ...
  final Map<String, int> stats;
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
  Future<void> putSkill(String uid, SkillStateRow row) =>
      _students(uid)
          .doc(row.studentId)
          .collection('skills')
          .doc(row.skill)
          .set(skillToJson(row));

  @override
  Future<void> deleteStudent(String uid, String studentId) async {
    final student = _students(uid).doc(studentId);
    final progress = await student.collection('progress').get();
    final skills = await student.collection('skills').get();
    final reports = await student.collection('reports').get();
    final queued = await _db
        .collection('ai_queue')
        .where('uid', isEqualTo: uid)
        .where('student_id', isEqualTo: studentId)
        .get();
    final batch = _db.batch();
    for (final doc in [
      ...progress.docs,
      ...skills.docs,
      ...reports.docs,
      ...queued.docs,
    ]) {
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
    final skills = <SkillStateRow>[];
    for (final doc in (await _students(uid).get()).docs) {
      students.add(studentFromJson(doc.id, doc.data()));
      final lessons = await doc.reference.collection('progress').get();
      for (final p in lessons.docs) {
        final (row, stepRows) = progressFromJson(doc.id, p.id, p.data());
        progress.add(row);
        steps.addAll(stepRows);
      }
      for (final k in (await doc.reference.collection('skills').get()).docs) {
        skills.add(skillFromJson(doc.id, k.data()));
      }
    }
    return RemoteData(
      role: account.data()?['role'] as String?,
      students: students,
      progress: progress,
      steps: steps,
      skills: skills,
    );
  }

  @override
  Future<void> putQueuedAnswer(String uid, QueuedAnswer answer) =>
      _db.collection('ai_queue').doc(answer.id).set(queuedToJson(uid, answer));

  @override
  Future<Map<String, QueueReply>> fetchReplies(
    String uid,
    List<String> ids,
  ) async {
    final replies = <String, QueueReply>{};
    // Firestore allows up to 30 ids in one `whereIn`.
    for (var i = 0; i < ids.length; i += 30) {
      final chunk = ids.sublist(i, (i + 30).clamp(0, ids.length));
      final snap = await _db
          .collection('ai_queue')
          .where('uid', isEqualTo: uid)
          .where(FieldPath.documentId, whereIn: chunk)
          .get();
      for (final doc in snap.docs) {
        final status = doc.data()['status'] as String?;
        if (status == 'answered' || status == 'failed' || status == 'skipped') {
          replies[doc.id] = QueueReply(
            status: status == 'answered' ? 'answered' : 'failed',
            level: doc.data()['level'] as String?,
            reply: doc.data()['reply'] as String?,
          );
        }
      }
    }
    return replies;
  }

  @override
  Future<List<WeeklyReport>> fetchReports(String uid, String studentId) async {
    final snap = await _students(uid)
        .doc(studentId)
        .collection('reports')
        .orderBy('week', descending: true)
        .limit(8)
        .get();
    return [for (final doc in snap.docs) reportFromJson(doc.data())];
  }
}

// JSON conversion, shared with the test fake.

Map<String, Object?> queuedToJson(String uid, QueuedAnswer a) => {
  'uid': uid,
  'student_id': a.studentId,
  'lesson_id': a.lessonId,
  'step_id': a.stepId,
  'lang': a.lang,
  'answer': a.answer,
  'created_at': Timestamp.fromDate(a.createdAt),
  'status': 'waiting',
};

WeeklyReport reportFromJson(Map<String, dynamic> json) {
  final note = json['note'] as Map<String, dynamic>? ?? {};
  final stats = json['stats'] as Map<String, dynamic>? ?? {};
  return WeeklyReport(
    week: json['week'] as String? ?? '',
    noteEn: note['en'] as String? ?? '',
    noteUr: note['ur'] as String? ?? '',
    stats: {
      for (final e in stats.entries)
        if (e.value is num) e.key: (e.value as num).toInt(),
    },
  );
}

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

/// The skill state's own fields (snake_case JSON) plus `updated_at`.
Map<String, Object?> skillToJson(SkillStateRow row) => {
  ...jsonDecode(row.data) as Map<String, dynamic>,
  'updated_at': Timestamp.fromDate(row.updatedAt),
};

SkillStateRow skillFromJson(String studentId, Map<String, dynamic> json) {
  final data = Map.of(json)..remove('updated_at');
  return SkillStateRow(
    studentId: studentId,
    skill: json['skill'] as String,
    data: jsonEncode(data),
    updatedAt: _date(json['updated_at']),
    synced: true,
  );
}

final remoteStoreProvider = Provider<RemoteStore>(
  (ref) => throw UnimplementedError('Override in main() before use'),
);

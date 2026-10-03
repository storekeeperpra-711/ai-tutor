import 'dart:math';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

/// A teacher's class (Phase 9). Families join it with its [code].
class SchoolClass {
  const SchoolClass({
    required this.id,
    required this.name,
    required this.code,
    required this.teacherUid,
  });

  final String id;
  final String name;
  final String code;
  final String teacherUid;
}

/// What a family sees before joining: the class name, from its code.
typedef ClassInfo = ({String id, String name});

/// A lesson a teacher assigned to a class.
class Assignment {
  const Assignment({
    required this.id,
    required this.lessonId,
    required this.createdAt,
    this.due,
  });

  final String id;
  final String lessonId;
  final DateTime createdAt;
  final DateTime? due;
}

/// What the teacher sees about one child, kept up to date by the family's
/// phone. First name and grade only: no PIN, no picture, no other family
/// data, and none of it goes to AI.
class ClassMember {
  const ClassMember({
    required this.uid,
    required this.studentId,
    required this.firstName,
    required this.grade,
    required this.joinedAt,
    this.updatedAt,
    this.skills = const [],
    this.misconceptions = const [],
    this.lessons = const [],
  });

  /// The family's account.
  final String uid;
  final String studentId;
  final String firstName;
  final int grade;
  final DateTime joinedAt;

  /// null until the server has stamped it.
  final DateTime? updatedAt;
  final List<MemberSkill> skills;
  final List<MemberMisconception> misconceptions;
  final List<MemberLesson> lessons;

  /// The document id in `classes/{id}/members`.
  String get docId => memberDocId(uid, studentId);
}

String memberDocId(String uid, String studentId) => '${uid}_$studentId';

/// One skill the child has started. [level] is a `MasteryLevel` name.
typedef MemberSkill = ({
  String skill,
  String level,
  bool needsHelp,
  String? lastDay,
  String? nextReview,
});

/// How often a lesson's misconception came up in the child's answers.
typedef MemberMisconception = ({String lessonId, String id, int count});

/// A lesson the child has opened.
typedef MemberLesson = ({String lessonId, bool completed, int nextStep});

/// Classes in Firestore, behind an interface so tests can use a fake.
///
/// Layout (see firestore.rules):
/// ```
/// class_codes/{CODE}                    class_id, name
/// classes/{classId}                     teacher_uid, name, code, created_at
/// classes/{classId}/families/{uid}      joined_at (lets a family read the class)
/// classes/{classId}/members/{uid}_{studentId}   a child's summary
/// classes/{classId}/assignments/{id}    lesson_id, due, created_at
/// ```
abstract class ClassStore {
  // For teachers.

  /// Creates a class with a new code.
  Future<SchoolClass> createClass(String teacherUid, String name);

  Future<List<SchoolClass>> classesOf(String teacherUid);

  Future<List<ClassMember>> members(String classId);

  /// Assigned lessons, oldest first.
  Future<List<Assignment>> assignments(String classId);

  Future<void> assign(
    String classId, {
    required String lessonId,
    DateTime? due,
  });

  Future<void> unassign(String classId, String assignmentId);

  /// Deletes the class with its code, members and lessons.
  Future<void> deleteClass(SchoolClass schoolClass);

  // For families.

  /// The class with [code], or null if there is none.
  Future<ClassInfo?> findClass(String code);

  /// Writes a child's summary. [join] also records the family in the class
  /// (the first time, or from a new account).
  Future<void> putMember(String classId, ClassMember member, {bool join});

  /// Removes a child's summary; [lastChild] also removes the family.
  Future<void> removeMember(
    String classId,
    String uid,
    String studentId, {
    bool lastChild,
  });
}

/// Letters and digits that can't be mistaken for each other (no I, O, 0, 1).
const classCodeAlphabet = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
const classCodeLength = 6;

String newClassCode([Random? random]) {
  final r = random ?? Random.secure();
  return String.fromCharCodes([
    for (var i = 0; i < classCodeLength; i++)
      classCodeAlphabet.codeUnitAt(r.nextInt(classCodeAlphabet.length)),
  ]);
}

/// A code as typed: any case, with spaces or dashes.
String normalizeClassCode(String typed) =>
    typed.toUpperCase().replaceAll(RegExp('[^A-Z0-9]'), '');

class FirestoreClassStore implements ClassStore {
  FirestoreClassStore(this._db);

  final FirebaseFirestore _db;

  CollectionReference<Map<String, dynamic>> get _classes =>
      _db.collection('classes');

  // Classes change on other phones; a cached copy would be out of date.
  static const _fresh = GetOptions(source: Source.server);

  @override
  Future<SchoolClass> createClass(String teacherUid, String name) async {
    // The rules refuse a code that is taken, so try another.
    for (var attempt = 0; ; attempt++) {
      final code = newClassCode();
      final ref = _classes.doc();
      final batch = _db.batch()
        ..set(ref, {
          'teacher_uid': teacherUid,
          'name': name,
          'code': code,
          'created_at': FieldValue.serverTimestamp(),
        })
        ..set(_db.collection('class_codes').doc(code), {
          'class_id': ref.id,
          'name': name,
        });
      try {
        await batch.commit();
        return SchoolClass(
          id: ref.id,
          name: name,
          code: code,
          teacherUid: teacherUid,
        );
      } on FirebaseException catch (e) {
        if (e.code != 'permission-denied' || attempt >= 4) rethrow;
      }
    }
  }

  @override
  Future<List<SchoolClass>> classesOf(String teacherUid) async {
    final snap = await _classes
        .where('teacher_uid', isEqualTo: teacherUid)
        .get(_fresh);
    return [for (final d in snap.docs) classFromJson(d.id, d.data())]
      ..sort((a, b) => a.name.compareTo(b.name));
  }

  @override
  Future<List<ClassMember>> members(String classId) async {
    final snap = await _classes.doc(classId).collection('members').get(_fresh);
    return [for (final d in snap.docs) memberFromJson(d.data())]
      ..sort((a, b) => a.firstName.compareTo(b.firstName));
  }

  @override
  Future<List<Assignment>> assignments(String classId) async {
    final snap = await _classes
        .doc(classId)
        .collection('assignments')
        .get(_fresh);
    return [for (final d in snap.docs) assignmentFromJson(d.id, d.data())]
      ..sort((a, b) => a.createdAt.compareTo(b.createdAt));
  }

  @override
  Future<void> assign(
    String classId, {
    required String lessonId,
    DateTime? due,
  }) => _classes.doc(classId).collection('assignments').add({
    'lesson_id': lessonId,
    'due': due == null ? null : Timestamp.fromDate(due),
    'created_at': FieldValue.serverTimestamp(),
  });

  @override
  Future<void> unassign(String classId, String assignmentId) => _classes
      .doc(classId)
      .collection('assignments')
      .doc(assignmentId)
      .delete();

  @override
  Future<void> deleteClass(SchoolClass schoolClass) async {
    final doc = _classes.doc(schoolClass.id);
    final batch = _db.batch();
    for (final sub in ['members', 'families', 'assignments']) {
      for (final d in (await doc.collection(sub).get(_fresh)).docs) {
        batch.delete(d.reference);
      }
    }
    batch
      ..delete(_db.collection('class_codes').doc(schoolClass.code))
      ..delete(doc);
    await batch.commit();
  }

  @override
  Future<ClassInfo?> findClass(String code) async {
    if (code.length != classCodeLength) return null;
    final snap = await _db.collection('class_codes').doc(code).get(_fresh);
    final data = snap.data();
    if (data == null) return null;
    return (id: data['class_id'] as String, name: data['name'] as String);
  }

  @override
  Future<void> putMember(
    String classId,
    ClassMember member, {
    bool join = false,
  }) async {
    final doc = _classes.doc(classId);
    final batch = _db.batch();
    if (join) {
      batch.set(doc.collection('families').doc(member.uid), {
        'joined_at': FieldValue.serverTimestamp(),
      });
    }
    batch.set(
      doc.collection('members').doc(member.docId),
      memberToJson(member),
    );
    await batch.commit();
  }

  @override
  Future<void> removeMember(
    String classId,
    String uid,
    String studentId, {
    bool lastChild = false,
  }) async {
    final doc = _classes.doc(classId);
    final batch = _db.batch()
      ..delete(doc.collection('members').doc(memberDocId(uid, studentId)));
    if (lastChild) batch.delete(doc.collection('families').doc(uid));
    await batch.commit();
  }
}

// JSON conversion, shared with the test fake.

DateTime? _date(Object? value) => switch (value) {
  final Timestamp t => t.toDate(),
  final DateTime d => d,
  _ => null,
};

SchoolClass classFromJson(String id, Map<String, dynamic> json) => SchoolClass(
  id: id,
  name: json['name'] as String,
  code: json['code'] as String,
  teacherUid: json['teacher_uid'] as String,
);

Assignment assignmentFromJson(String id, Map<String, dynamic> json) =>
    Assignment(
      id: id,
      lessonId: json['lesson_id'] as String,
      due: _date(json['due']),
      createdAt: _date(json['created_at']) ?? DateTime.now(),
    );

/// The summary without `updated_at` (the server sets it).
Map<String, Object?> memberToJson(ClassMember m) => {
  ...memberSummaryJson(m),
  'updated_at': FieldValue.serverTimestamp(),
};

/// What the phone compares to tell whether the summary changed.
Map<String, Object?> memberSummaryJson(ClassMember m) => {
  'uid': m.uid,
  'student_id': m.studentId,
  'first_name': m.firstName,
  'grade': m.grade,
  'joined_at': Timestamp.fromDate(m.joinedAt),
  'skills': [
    for (final s in m.skills)
      {
        'skill': s.skill,
        'level': s.level,
        'needs_help': s.needsHelp,
        'last_day': s.lastDay,
        'next_review': s.nextReview,
      },
  ],
  'misconceptions': [
    for (final x in m.misconceptions)
      {'lesson_id': x.lessonId, 'id': x.id, 'count': x.count},
  ],
  'lessons': [
    for (final l in m.lessons)
      {
        'lesson_id': l.lessonId,
        'completed': l.completed,
        'next_step': l.nextStep,
      },
  ],
};

ClassMember memberFromJson(Map<String, dynamic> json) => ClassMember(
  uid: json['uid'] as String,
  studentId: json['student_id'] as String,
  firstName: json['first_name'] as String,
  grade: (json['grade'] as num).toInt(),
  joinedAt: _date(json['joined_at']) ?? DateTime.now(),
  updatedAt: _date(json['updated_at']),
  skills: [
    for (final s
        in (json['skills'] as List? ?? const []).cast<Map<String, dynamic>>())
      (
        skill: s['skill'] as String,
        level: s['level'] as String,
        needsHelp: s['needs_help'] as bool? ?? false,
        lastDay: s['last_day'] as String?,
        nextReview: s['next_review'] as String?,
      ),
  ],
  misconceptions: [
    for (final x
        in (json['misconceptions'] as List? ?? const [])
            .cast<Map<String, dynamic>>())
      (
        lessonId: x['lesson_id'] as String,
        id: x['id'] as String,
        count: (x['count'] as num).toInt(),
      ),
  ],
  lessons: [
    for (final l
        in (json['lessons'] as List? ?? const []).cast<Map<String, dynamic>>())
      (
        lessonId: l['lesson_id'] as String,
        completed: l['completed'] as bool? ?? false,
        nextStep: (l['next_step'] as num? ?? 0).toInt(),
      ),
  ],
);

final classStoreProvider = Provider<ClassStore>(
  (ref) => throw UnimplementedError('Override in main() before use'),
);

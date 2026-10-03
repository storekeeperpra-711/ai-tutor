import 'dart:async';
import 'dart:convert';

import 'package:firebase_core/firebase_core.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../app/preferences.dart';
import '../mastery/curriculum.dart';
import '../mastery/skill_state.dart';
import '../services/auth_service.dart';
import '../services/local_db.dart';
import '../services/mastery_service.dart';
import 'class_store.dart';

/// Builds what a class's teacher sees about one child: first name, grade,
/// the skills started with their level, how often each misconception came
/// up, and the lessons opened. Lists are sorted so an unchanged summary
/// gives the same JSON.
ClassMember classSummary({
  required String uid,
  required Student student,
  required DateTime joinedAt,
  required Map<String, SkillState> states,
  required Map<String, LessonProgress> progress,
  required List<StepResultRow> steps,
  required Curriculum curriculum,
}) {
  final skills = [
    for (final s in states.values)
      if (s.level(curriculum.criteriaFor(s.skill)) case final level
          when level != MasteryLevel.notStarted)
        (
          skill: s.skill,
          level: level.name,
          needsHelp: s.needsHelp,
          lastDay: s.lastAnswered == null ? null : dayKey(s.lastAnswered!),
          nextReview: s.nextReview == null ? null : dayKey(s.nextReview!),
        ),
  ]..sort((a, b) => a.skill.compareTo(b.skill));

  final counts = <(String, String), int>{};
  for (final r in steps) {
    for (final id in (jsonDecode(r.misconceptions) as List).cast<String>()) {
      counts.update((r.lessonId, id), (n) => n + 1, ifAbsent: () => 1);
    }
  }
  final misconceptions = [
    for (final MapEntry(key: (lessonId, id), value: count) in counts.entries)
      (lessonId: lessonId, id: id, count: count),
  ]..sort((a, b) => '${a.lessonId}/${a.id}'.compareTo('${b.lessonId}/${b.id}'));

  final lessons = [
    for (final p in progress.values)
      (lessonId: p.lessonId, completed: p.completed, nextStep: p.nextStep),
  ]..sort((a, b) => a.lessonId.compareTo(b.lessonId));

  return ClassMember(
    uid: uid,
    studentId: student.id,
    firstName: student.firstName,
    grade: student.grade,
    joinedAt: joinedAt,
    skills: skills,
    misconceptions: misconceptions,
    lessons: lessons,
  );
}

/// Why joining a class didn't work.
enum ClassProblem { notFound, noConnection }

class ClassException implements Exception {
  const ClassException(this.problem);
  final ClassProblem problem;
}

/// Joining and leaving classes on the family phone, and keeping each
/// child's summary and the assigned lessons up to date (Phase 9).
class ClassService {
  ClassService(this.ref);

  final Ref ref;

  /// A summary that changed is shared at most this often (it changes with
  /// nearly every answer; this keeps Firestore writes low).
  static const shareEvery = Duration(minutes: 15);

  /// Assigned lessons are fetched at most this often.
  static const fetchEvery = Duration(hours: 1);
  static const fetchedAtKey = 'classes.fetchedAt';

  LocalDb get _db => ref.read(localDbProvider);
  ClassStore get _store => ref.read(classStoreProvider);

  String _uid() {
    final uid = ref.read(authServiceProvider).currentUser?.uid;
    if (uid == null) throw const ClassException(ClassProblem.noConnection);
    return uid;
  }

  /// Looks up a class by the code a parent typed. Needs internet.
  Future<ClassInfo> find(String typed) async {
    _uid();
    final ClassInfo? found;
    try {
      found = await _store.findClass(normalizeClassCode(typed));
    } catch (_) {
      throw const ClassException(ClassProblem.noConnection);
    }
    if (found == null) throw const ClassException(ClassProblem.notFound);
    return found;
  }

  /// Joins [student] to [found] after a parent agreed, and shares the
  /// summary straight away. Needs internet.
  Future<void> join(Student student, ClassInfo found, {DateTime? now}) async {
    final uid = _uid();
    final at = now ?? DateTime.now();
    final membership = ClassMembership(
      studentId: student.id,
      classId: found.id,
      className: found.name,
      joinedAt: at,
    );
    try {
      await _share(uid, membership, at);
    } catch (_) {
      throw const ClassException(ClassProblem.noConnection);
    }
    await _db.joinClass(membership);
    await _db.markShared(
      student.id,
      found.id,
      uid: uid,
      summary: await _summaryKey(uid, membership),
      at: at,
    );
    unawaited(_fetchAssignments({found.id}, at).catchError((_) {}));
  }

  /// Takes [student] out of a class, which deletes their summary there.
  Future<void> leave(String studentId, String classId) async {
    final uid = ref.read(authServiceProvider).currentUser?.uid;
    final all = await _db.allMemberships();
    final lastChild = !all.any(
      (m) => m.classId == classId && m.studentId != studentId,
    );
    await _db.leaveClass(studentId, classId);
    if (uid != null) {
      // Firestore sends the delete later if the phone is offline.
      unawaited(
        _store
            .removeMember(classId, uid, studentId, lastChild: lastChild)
            .catchError((_) {}),
      );
    }
  }

  /// Before a child's profile is removed from the phone.
  Future<void> leaveAll(String studentId) async {
    for (final m in await _db.membershipsOf(studentId)) {
      await leave(studentId, m.classId);
    }
  }

  /// Shares summaries that changed and fetches assigned lessons, each
  /// only as often as allowed. Called by the sync service.
  Future<void> sync(String uid, {DateTime? now}) async {
    final at = now ?? DateTime.now();
    final memberships = await _db.allMemberships();
    if (memberships.isEmpty) return;
    for (final m in memberships) {
      final summary = await _summaryKey(uid, m);
      final newAccount = m.sharedUid != uid;
      if (!newAccount &&
          (m.sharedSummary == summary ||
              (m.sharedAt != null &&
                  at.difference(m.sharedAt!) < shareEvery))) {
        continue;
      }
      try {
        await _share(uid, m, at, join: newAccount);
      } on FirebaseException catch (e) {
        // The teacher deleted the class.
        if (e.code == 'permission-denied') {
          await _db.leaveClass(m.studentId, m.classId);
          continue;
        }
        rethrow;
      }
      await _db.markShared(
        m.studentId,
        m.classId,
        uid: uid,
        summary: summary,
        at: at,
      );
    }
    final prefs = ref.read(sharedPreferencesProvider);
    final last = DateTime.fromMillisecondsSinceEpoch(
      prefs.getInt(fetchedAtKey) ?? 0,
    );
    if (at.difference(last) >= fetchEvery) {
      final left = await _db.allMemberships();
      await _fetchAssignments({for (final m in left) m.classId}, at);
    }
  }

  Future<void> _fetchAssignments(Set<String> classIds, DateTime at) async {
    for (final id in classIds) {
      final List<Assignment> list;
      try {
        list = await _store.assignments(id);
      } on FirebaseException catch (e) {
        if (e.code != 'permission-denied') rethrow;
        // The teacher deleted the class.
        for (final m in await _db.allMemberships()) {
          if (m.classId == id) await _db.leaveClass(m.studentId, id);
        }
        continue;
      }
      await _db.replaceAssignments(id, [
        for (final a in list)
          ClassAssignment(
            classId: id,
            id: a.id,
            lessonId: a.lessonId,
            due: a.due,
            createdAt: a.createdAt,
          ),
      ]);
    }
    await ref
        .read(sharedPreferencesProvider)
        .setInt(fetchedAtKey, at.millisecondsSinceEpoch);
  }

  Future<ClassMember?> _summary(String uid, ClassMembership m) async {
    final student = await _db.student(m.studentId);
    if (student == null) return null;
    return classSummary(
      uid: uid,
      student: student,
      joinedAt: m.joinedAt,
      states: await _db.skillStatesOf(m.studentId),
      progress: await _db.progressOf(m.studentId),
      steps: await _db.stepResultsOf(m.studentId),
      curriculum: await ref.read(curriculumProvider.future),
    );
  }

  /// The summary as JSON, to tell whether it changed since last shared.
  Future<String> _summaryKey(String uid, ClassMembership m) async {
    final summary = await _summary(uid, m);
    if (summary == null) return '';
    return jsonEncode(memberSummaryJson(summary)..remove('joined_at'));
  }

  Future<void> _share(
    String uid,
    ClassMembership m,
    DateTime at, {
    bool join = true,
  }) async {
    final summary = await _summary(uid, m);
    if (summary == null) return;
    await _store.putMember(m.classId, summary, join: join);
  }
}

final classServiceProvider = Provider<ClassService>(ClassService.new);

/// The classes a child is in.
final membershipsProvider =
    StreamProvider.family<List<ClassMembership>, String>(
      (ref, studentId) =>
          ref.watch(localDbProvider).watchMemberships(studentId),
    );

/// Lessons a child's teachers assigned.
final assignmentsProvider =
    StreamProvider.family<List<ClassAssignment>, String>(
      (ref, studentId) =>
          ref.watch(localDbProvider).watchAssignmentsFor(studentId),
    );

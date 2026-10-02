import 'dart:convert';

import 'package:drift/drift.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../lessons/step_result.dart';
import '../mastery/skill_state.dart';

part 'local_db.g.dart';

/// Child profiles on this phone. Minimal personal data: first name, grade
/// and a picture.
@DataClassName('Student')
class Students extends Table {
  TextColumn get id => text()();
  TextColumn get firstName => text().withLength(min: 1, max: 30)();

  /// -1 = Nursery, 0 = Prep, 1 to 12 = Grade 1 to 12.
  IntColumn get grade => integer()();

  /// One of [avatarIds].
  TextColumn get avatar => text()();

  /// `salt:sha256` of the child's PIN, or null for picture-only login.
  TextColumn get pinHash => text().nullable()();
  DateTimeColumn get createdAt => dateTime()();

  /// When a parent or guardian agreed to save this child's data.
  DateTimeColumn get consentAt => dateTime()();
  BoolColumn get synced => boolean().withDefault(const Constant(false))();

  @override
  Set<Column> get primaryKey => {id};
}

/// Where each child is in each lesson.
@DataClassName('LessonProgress')
class LessonProgressTable extends Table {
  @override
  String get tableName => 'lesson_progress';

  TextColumn get studentId => text().references(Students, #id)();
  TextColumn get lessonId => text()();
  IntColumn get lessonVersion => integer()();

  /// Index of the step to show when the lesson is opened again.
  IntColumn get nextStep => integer()();
  BoolColumn get completed => boolean()();
  DateTimeColumn get updatedAt => dateTime()();

  @override
  Set<Column> get primaryKey => {studentId, lessonId};
}

/// One finished step. Rows with `synced = false` are the queue of answers
/// waiting to be copied to Firestore.
@DataClassName('StepResultRow')
class StepResults extends Table {
  TextColumn get studentId => text().references(Students, #id)();
  TextColumn get lessonId => text()();
  TextColumn get stepId => text()();

  /// null for steps without a question.
  BoolColumn get correct => boolean().nullable()();
  IntColumn get attempts => integer()();

  /// JSON list of misconception ids.
  TextColumn get misconceptions => text().withDefault(const Constant('[]'))();
  DateTimeColumn get answeredAt => dateTime()();
  BoolColumn get synced => boolean().withDefault(const Constant(false))();

  @override
  Set<Column> get primaryKey => {studentId, lessonId, stepId};
}

/// What the mastery engine knows about each child and skill (Phase 4).
@DataClassName('SkillStateRow')
class SkillStates extends Table {
  TextColumn get studentId => text().references(Students, #id)();
  TextColumn get skill => text()();

  /// [SkillState] as JSON.
  TextColumn get data => text()();
  DateTimeColumn get updatedAt => dateTime()();
  BoolColumn get synced => boolean().withDefault(const Constant(false))();

  @override
  Set<Column> get primaryKey => {studentId, skill};
}

/// The pictures a child can choose from.
const avatarIds = [
  'cat',
  'star',
  'flower',
  'sun',
  'moon',
  'tree',
  'car',
  'bird',
  'cricket',
  'cake',
];

/// Everything about one child's lesson that still has to reach Firestore.
class ProgressUpload {
  const ProgressUpload({required this.progress, required this.steps});

  final LessonProgress progress;
  final List<StepResultRow> steps;
}

/// The on-phone database. Everything is saved here first, so lessons work
/// without internet; the sync service copies it to Firestore.
@DriftDatabase(
  tables: [Students, LessonProgressTable, StepResults, SkillStates],
)
class LocalDb extends _$LocalDb {
  LocalDb(super.executor);

  @override
  int get schemaVersion => 2;

  @override
  MigrationStrategy get migration => MigrationStrategy(
    onUpgrade: (m, from, to) async {
      if (from < 2) await m.createTable(skillStates);
    },
    beforeOpen: (details) async {
      await customStatement('PRAGMA foreign_keys = ON');
    },
  );

  // Profiles

  Stream<List<Student>> watchStudents() => (select(
    students,
  )..orderBy([(s) => OrderingTerm(expression: s.createdAt)])).watch();

  Future<Student?> student(String id) =>
      (select(students)..where((s) => s.id.equals(id))).getSingleOrNull();

  Future<void> addStudent(Student student) =>
      into(students).insert(student.copyWith(synced: false));

  Future<void> deleteStudent(String id) => transaction(() async {
    await (delete(stepResults)..where((r) => r.studentId.equals(id))).go();
    await (delete(skillStates)..where((r) => r.studentId.equals(id))).go();
    await (delete(
      lessonProgressTable,
    )..where((p) => p.studentId.equals(id))).go();
    await (delete(students)..where((s) => s.id.equals(id))).go();
  });

  // Progress

  Future<LessonProgress?> progress(String studentId, String lessonId) =>
      (select(lessonProgressTable)..where(
            (p) => p.studentId.equals(studentId) & p.lessonId.equals(lessonId),
          ))
          .getSingleOrNull();

  Stream<Map<String, LessonProgress>> watchProgress(String studentId) =>
      (select(lessonProgressTable)..where((p) => p.studentId.equals(studentId)))
          .watch()
          .map((rows) => {for (final r in rows) r.lessonId: r});

  /// Saves one finished step and where to resume, in one transaction.
  /// This is the only write per step (spec D9).
  Future<void> recordStep({
    required String studentId,
    required String lessonId,
    required int lessonVersion,
    required int stepIndex,
    required int stepCount,
    required StepResult result,
    DateTime? now,
  }) {
    final at = now ?? DateTime.now();
    final finished = stepIndex >= stepCount - 1;
    return transaction(() async {
      await into(stepResults).insertOnConflictUpdate(
        StepResultsCompanion.insert(
          studentId: studentId,
          lessonId: lessonId,
          stepId: result.stepId,
          correct: Value(result.correct),
          attempts: result.attempts,
          misconceptions: Value(jsonEncode(result.misconceptionIds)),
          answeredAt: at,
          synced: const Value(false),
        ),
      );
      await into(lessonProgressTable).insertOnConflictUpdate(
        LessonProgressTableCompanion.insert(
          studentId: studentId,
          lessonId: lessonId,
          lessonVersion: lessonVersion,
          nextStep: finished ? stepCount : stepIndex + 1,
          completed: finished,
          updatedAt: at,
        ),
      );
    });
  }

  // Mastery (Phase 4)

  static Map<String, SkillState> _decode(List<SkillStateRow> rows) => {
    for (final r in rows)
      r.skill: SkillState.fromJson(jsonDecode(r.data) as Map<String, dynamic>),
  };

  /// Every skill state of [studentId], by skill.
  Future<Map<String, SkillState>> skillStatesOf(String studentId) async =>
      _decode(
        await (select(
          skillStates,
        )..where((s) => s.studentId.equals(studentId))).get(),
      );

  Stream<Map<String, SkillState>> watchSkillStates(String studentId) => (select(
    skillStates,
  )..where((s) => s.studentId.equals(studentId))).watch().map(_decode);

  /// Changes one skill state in a transaction, so answers saved at the
  /// same moment can't overwrite each other.
  Future<SkillState> updateSkillState(
    String studentId,
    String skill,
    SkillState Function(SkillState current) change, {
    DateTime? now,
  }) => transaction(() async {
    final row =
        await (select(skillStates)..where(
              (s) => s.studentId.equals(studentId) & s.skill.equals(skill),
            ))
            .getSingleOrNull();
    final current = row == null
        ? SkillState(skill: skill)
        : SkillState.fromJson(jsonDecode(row.data) as Map<String, dynamic>);
    final next = change(current);
    await saveSkillState(studentId, next, now: now);
    return next;
  });

  Future<void> saveSkillState(
    String studentId,
    SkillState state, {
    DateTime? now,
  }) => into(skillStates).insertOnConflictUpdate(
    SkillStatesCompanion.insert(
      studentId: studentId,
      skill: state.skill,
      data: jsonEncode(state.toJson()),
      updatedAt: now ?? DateTime.now(),
      synced: const Value(false),
    ),
  );

  Future<List<SkillStateRow>> unsyncedSkillStates() =>
      (select(skillStates)..where((s) => s.synced.equals(false))).get();

  /// Marks an uploaded skill state as synced, unless it changed meanwhile.
  Future<void> markSkillSynced(SkillStateRow row) =>
      (update(skillStates)..where(
            (s) =>
                s.studentId.equals(row.studentId) &
                s.skill.equals(row.skill) &
                s.updatedAt.equals(row.updatedAt),
          ))
          .write(const SkillStatesCompanion(synced: Value(true)));

  // Sync queue

  Selectable<int> _pendingCount() {
    final count = stepResults.stepId.count();
    return (selectOnly(stepResults)
          ..addColumns([count])
          ..where(stepResults.synced.equals(false)))
        .map((row) => row.read(count) ?? 0);
  }

  /// Answers waiting to be copied to Firestore.
  Stream<int> watchPendingCount() => _pendingCount().watchSingle();

  Future<int> pendingCount() => _pendingCount().getSingle();

  Future<List<Student>> unsyncedStudents() =>
      (select(students)..where((s) => s.synced.equals(false))).get();

  Future<void> markStudentSynced(String id) =>
      (update(students)..where((s) => s.id.equals(id))).write(
        const StudentsCompanion(synced: Value(true)),
      );

  /// One upload per lesson that has unsynced answers.
  Future<List<ProgressUpload>> pendingUploads() async {
    final rows = await (select(
      stepResults,
    )..where((r) => r.synced.equals(false))).get();
    final byLesson = <(String, String), List<StepResultRow>>{};
    for (final r in rows) {
      (byLesson[(r.studentId, r.lessonId)] ??= []).add(r);
    }
    return [
      for (final MapEntry(key: (studentId, lessonId), value: steps)
          in byLesson.entries)
        if (await progress(studentId, lessonId) case final p?)
          ProgressUpload(progress: p, steps: steps),
    ];
  }

  /// Marks uploaded answers as synced, unless the step was answered again
  /// while the upload was on its way.
  Future<void> markStepsSynced(List<StepResultRow> uploaded) =>
      transaction(() async {
        for (final r in uploaded) {
          await (update(stepResults)..where(
                (s) =>
                    s.studentId.equals(r.studentId) &
                    s.lessonId.equals(r.lessonId) &
                    s.stepId.equals(r.stepId) &
                    s.answeredAt.equals(r.answeredAt),
              ))
              .write(const StepResultsCompanion(synced: Value(true)));
        }
      });

  /// After signing in to a different account, everything on the phone has
  /// to be uploaded to that account.
  Future<void> markAllUnsynced() => transaction(() async {
    await update(students).write(const StudentsCompanion(synced: Value(false)));
    await update(stepResults)
        .write(const StepResultsCompanion(synced: Value(false)));
    await update(skillStates)
        .write(const SkillStatesCompanion(synced: Value(false)));
  });

  /// Adds profiles and progress saved in the account (for example from
  /// another phone). Local answers win where both have the same step.
  Future<void> mergeRemote(RemoteData data) => transaction(() async {
    for (final s in data.students) {
      await into(students).insertOnConflictUpdate(s.copyWith(synced: true));
    }
    for (final p in data.progress) {
      final local = await progress(p.studentId, p.lessonId);
      if (local == null || p.updatedAt.isAfter(local.updatedAt)) {
        await into(lessonProgressTable).insertOnConflictUpdate(p);
      }
    }
    for (final r in data.steps) {
      await into(stepResults)
          .insert(r.copyWith(synced: true), mode: InsertMode.insertOrIgnore);
    }
    for (final r in data.skills) {
      final local =
          await (select(skillStates)..where(
                (s) =>
                    s.studentId.equals(r.studentId) & s.skill.equals(r.skill),
              ))
              .getSingleOrNull();
      if (local == null || r.updatedAt.isAfter(local.updatedAt)) {
        await into(skillStates)
            .insertOnConflictUpdate(r.copyWith(synced: true));
      }
    }
  });

  /// Removes every profile from this phone (when an adult signs out).
  Future<void> clearAll() => transaction(() async {
    await delete(stepResults).go();
    await delete(skillStates).go();
    await delete(lessonProgressTable).go();
    await delete(students).go();
  });
}

/// Profiles and progress read back from Firestore.
class RemoteData {
  const RemoteData({
    this.role,
    this.students = const [],
    this.progress = const [],
    this.steps = const [],
    this.skills = const [],
  });

  /// `device`, `parent` or `teacher`.
  final String? role;
  final List<Student> students;
  final List<LessonProgress> progress;
  final List<StepResultRow> steps;
  final List<SkillStateRow> skills;
}

/// The phone's database. Opened in main(); tests use an in-memory one.
final localDbProvider = Provider<LocalDb>(
  (ref) => throw UnimplementedError('Override in main() before use'),
);

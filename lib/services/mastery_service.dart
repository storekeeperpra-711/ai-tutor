import 'dart:async';
import 'dart:convert';

import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../app/preferences.dart';
import '../app/theme/age_tier.dart';
import '../lessons/lesson_repository.dart';
import '../lessons/step_result.dart';
import '../mastery/curriculum.dart';
import '../mastery/daily_plan.dart';
import '../mastery/evidence.dart';
import '../mastery/skill_state.dart';
import '../models/lesson.dart';
import '../models/lesson_step.dart';
import 'local_db.dart';
import 'profiles.dart';
import 'sync_service.dart';

/// All bundled lessons as a skills graph. Lessons that fail to load are
/// left out (the previewer shows their errors).
final curriculumProvider = FutureProvider<Curriculum>((ref) async {
  final ids = await ref.watch(lessonIdsProvider.future);
  final lessons = <Lesson>[];
  for (final id in ids) {
    try {
      lessons.add(await ref.watch(lessonProvider(id).future));
    } catch (_) {
      // Skipped.
    }
  }
  return Curriculum(lessons);
});

/// Mastery per skill for one child.
final skillStatesProvider =
    StreamProvider.family<Map<String, SkillState>, String>(
      (ref, studentId) =>
          ref.watch(localDbProvider).watchSkillStates(studentId),
    );

/// Feeds answers to the mastery engine and saves the result.
class MasteryService {
  MasteryService(this.ref);

  final Ref ref;

  /// Records a finished lesson step. Returns the new skill state, or null
  /// if the step isn't mastery evidence.
  Future<SkillState?> recordStep(
    String studentId,
    Lesson lesson,
    LessonStep step,
    StepResult result, {
    DateTime? at,
  }) async {
    final e = evidenceFor(lesson, step, result, at ?? DateTime.now());
    return e == null ? null : _record(studentId, e);
  }

  /// Records a question from the daily plan.
  Future<SkillState?> recordQuestion(
    String studentId,
    PlanQuestion q,
    StepResult result, {
    DateTime? at,
  }) async {
    final lesson = (await ref.read(curriculumProvider.future))
        .lesson(q.lessonId);
    if (lesson == null) return null;
    final e = evidenceFor(
      lesson,
      q.step,
      result,
      at ?? DateTime.now(),
      questionType: q.type,
      skill: q.skill,
      itemId: q.id,
    );
    return e == null ? null : _record(studentId, e);
  }

  Future<SkillState> _record(String studentId, Evidence e) async {
    final curriculum = await ref.read(curriculumProvider.future);
    final criteria = curriculum.criteriaFor(e.skill);
    final state = await ref
        .read(localDbProvider)
        .updateSkillState(
          studentId,
          e.skill,
          (s) => s.record(e, criteria),
          now: e.at,
        );
    unawaited(ref.read(syncServiceProvider).sync());
    return state;
  }
}

final masteryServiceProvider = Provider<MasteryService>(MasteryService.new);

/// Today's plan for a child. It is built once a day and saved, so it
/// stays the same all day while the child works through it.
final todayPlanProvider = FutureProvider.family<DailyPlan, String>((
  ref,
  studentId,
) async {
  final curriculum = await ref.watch(curriculumProvider.future);
  final progress = await ref.watch(progressProvider(studentId).future);
  final positions = {
    for (final p in progress.values)
      p.lessonId: (nextStep: p.nextStep, completed: p.completed),
  };
  final now = DateTime.now();
  final prefs = ref.read(sharedPreferencesProvider);
  final key = 'plan.$studentId';
  final saved = prefs.getString(key);
  if (saved != null) {
    final json = jsonDecode(saved) as Map<String, dynamic>;
    if (json['day'] == dayKey(now)) {
      return planFromKeys(
        now,
        (json['keys'] as List<dynamic>).cast(),
        curriculum,
        lessons: positions,
      );
    }
  }

  final db = ref.read(localDbProvider);
  final student = await db.student(studentId);
  final plan = buildDailyPlan(
    curriculum: curriculum,
    states: await db.skillStatesOf(studentId),
    lessons: positions,
    now: now,
    studentId: studentId,
    // Shorter for the youngest children (spec C1).
    minutes: student != null && tierForGrade(student.grade) == AgeTier.early
        ? 10
        : 15,
  );
  await prefs.setString(
    key,
    jsonEncode({'day': dayKey(now), 'keys': plan.keys}),
  );
  return plan;
});

/// Plan items marked done today that the engine can't see (flashcards,
/// home tasks).
final planDoneProvider = NotifierProvider.family<PlanDone, Set<String>, String>(
  PlanDone.new,
);

class PlanDone extends Notifier<Set<String>> {
  PlanDone(this.studentId);

  final String studentId;

  String get _key => 'planDone.$studentId.${dayKey(DateTime.now())}';

  @override
  Set<String> build() =>
      ref.read(sharedPreferencesProvider).getStringList(_key)?.toSet() ?? {};

  Future<void> markDone(String itemKey) async {
    state = {...state, itemKey};
    await ref.read(sharedPreferencesProvider).setStringList(_key, [...state]);
  }
}

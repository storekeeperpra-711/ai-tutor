import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../mastery/curriculum.dart';
import '../../mastery/skill_state.dart';
import '../../models/lesson.dart';
import '../../models/lesson_step.dart';
import '../../services/local_db.dart';
import '../../services/mastery_service.dart';
import '../../services/profiles.dart';

/// Badges for effort and understanding, never for streaks (spec C3).
/// They are worked out from the child's saved answers, so they sync with
/// them and come back on a new phone.
enum EffortBadge {
  firstLesson,
  triedAgain,
  explained,
  checkedPhoto,
  cameBack,
  fiveDays,
}

/// The three effort stars of a finished lesson.
class LessonStars {
  const LessonStars({
    required this.finished,
    required this.keptTrying,
    required this.explained,
  });

  /// Finished the lesson.
  final bool finished;

  /// Tried again after a mistake, or never needed to.
  final bool keptTrying;

  /// Explained in their own words; in a lesson with nothing to explain,
  /// answered every question.
  final bool explained;

  int get count => [finished, keptTrying, explained].where((s) => s).length;
}

bool _isExplain(LessonStep? step) => step is AiExplainStep;

/// One answered step, saved or from the visit just finished.
typedef StepAnswer = ({String stepId, bool? correct, int attempts});

StepAnswer answerOf(StepResultRow r) =>
    (stepId: r.stepId, correct: r.correct, attempts: r.attempts);

/// The stars for [lesson] from its answered steps.
LessonStars starsFor(
  Lesson lesson,
  Iterable<StepAnswer> answers, {
  required bool completed,
}) {
  final mine = answers.toList();
  final steps = {for (final s in lesson.steps) s.id: s};
  final questions = mine.where((r) => r.correct != null);
  final hasExplain = lesson.steps.any(_isExplain);
  return LessonStars(
    finished: completed,
    keptTrying:
        completed &&
        (questions.any((r) => r.attempts > 1) ||
            questions.every((r) => r.correct == true)),
    explained: hasExplain
        ? mine.any((r) => _isExplain(steps[r.stepId]))
        : completed &&
              lesson.steps.whereType<QuestionStep>().every(
                (q) => mine.any((r) => r.stepId == q.id),
              ),
  );
}

DateTime _day(DateTime t) => DateTime(t.year, t.month, t.day);

/// The badges earned from everything saved so far.
Set<EffortBadge> badgesFor({
  required Curriculum curriculum,
  required Iterable<LessonProgress> progress,
  required List<StepResultRow> steps,
  required Iterable<SkillState> skills,
  required DateTime now,
}) {
  LessonStep? stepOf(StepResultRow r) {
    final lesson = curriculum.lesson(r.lessonId);
    return lesson?.steps.where((s) => s.id == r.stepId).firstOrNull;
  }

  final days = {
    for (final r in steps) _day(r.answeredAt),
    for (final s in skills)
      for (final at in s.recent.values) _day(at),
  }.where((d) => d.year == now.year && d.month == now.month);

  return {
    if (progress.any((p) => p.completed)) EffortBadge.firstLesson,
    if (steps.any((r) => r.attempts > 1 && stepOf(r) is! PhotoCheckStep))
      EffortBadge.triedAgain,
    if (steps.any((r) => _isExplain(stepOf(r)))) EffortBadge.explained,
    if (steps.any((r) => r.attempts > 1 && stepOf(r) is PhotoCheckStep))
      EffortBadge.checkedPhoto,
    if (skills.any((s) => s.correctDays.length >= 2)) EffortBadge.cameBack,
    if (days.length >= 5) EffortBadge.fiveDays,
  };
}

/// Every finished step of a child.
final stepResultsProvider = StreamProvider.family<List<StepResultRow>, String>(
  (ref, studentId) => ref.watch(localDbProvider).watchStepResults(studentId),
);

/// A child's badges, kept up to date as they learn.
final badgesProvider = Provider.family<Set<EffortBadge>, String>((
  ref,
  studentId,
) {
  final curriculum = ref.watch(curriculumProvider).value;
  final progress = ref.watch(progressProvider(studentId)).value;
  final steps = ref.watch(stepResultsProvider(studentId)).value;
  final skills = ref.watch(skillStatesProvider(studentId)).value;
  if (curriculum == null ||
      progress == null ||
      steps == null ||
      skills == null) {
    return const {};
  }
  return badgesFor(
    curriculum: curriculum,
    progress: progress.values,
    steps: steps,
    skills: skills.values,
    now: DateTime.now(),
  );
});

/// Stars per finished lesson, by lesson id.
final starsProvider = Provider.family<Map<String, int>, String>((
  ref,
  studentId,
) {
  final curriculum = ref.watch(curriculumProvider).value;
  final progress = ref.watch(progressProvider(studentId)).value ?? const {};
  final steps = ref.watch(stepResultsProvider(studentId)).value ?? const [];
  if (curriculum == null) return const {};
  return {
    for (final p in progress.values)
      if (p.completed)
        if (curriculum.lesson(p.lessonId) case final lesson?)
          p.lessonId: starsFor(lesson, [
            for (final r in steps)
              if (r.lessonId == p.lessonId) answerOf(r),
          ], completed: true).count,
  };
});

/// The lesson to suggest after [lesson]: the next unfinished one in the
/// same subject, or null.
Lesson? nextLessonAfter(
  Curriculum curriculum,
  Lesson lesson,
  Map<String, LessonProgress> progress,
) {
  final list = curriculum.lessons;
  final start = list.indexWhere((l) => l.id == lesson.id);
  return list
      .skip(start + 1)
      .where(
        (l) => l.subject == lesson.subject && progress[l.id]?.completed != true,
      )
      .firstOrNull;
}

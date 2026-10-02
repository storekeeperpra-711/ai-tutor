import '../models/lesson.dart';
import 'curriculum.dart';
import 'skill_state.dart';

/// What to do when a student is stuck (spec B3): change the approach,
/// never repeat the same thing forever.
sealed class StuckAdvice {
  const StuckAdvice();
}

/// Explain the step another way.
class ShowAlternative extends StuckAdvice {
  const ShowAlternative(this.alternative);
  final Alternative alternative;
}

/// Go back to an earlier skill that isn't secure yet.
class GoBackToPrerequisite extends StuckAdvice {
  const GoBackToPrerequisite({required this.skill, required this.lessonId});
  final String skill;
  final String lessonId;
}

/// Suggest a short break.
class TakeABreak extends StuckAdvice {
  const TakeABreak();
}

/// Suggest a break and mark the skill for a parent or teacher.
class GetHelp extends StuckAdvice {
  const GetHelp();
}

/// Advice after a question step that wasn't right on the first try.
/// [state] already includes that answer. [shownAlternatives] are the ids
/// already shown in this visit, so the same one isn't repeated.
StuckAdvice? adviseWhenStuck({
  required SkillState state,
  required Lesson lesson,
  required String stepId,
  required Curriculum curriculum,
  required Map<String, SkillState> states,
  Set<String> shownAlternatives = const {},
}) {
  final stuck = state.stuck;
  if (stuck == 0) return null;
  if (state.needsHelp) return const GetHelp();
  if (stuck >= needsHelpAfter - 1) return const TakeABreak();

  final alternative = lesson.alternatives
      .where(
        (a) =>
            (a.forStep == null || a.forStep == stepId) &&
            !shownAlternatives.contains(a.id),
      )
      .firstOrNull;
  final gap = weakPrerequisite(state.skill, curriculum, states);

  return switch ((stuck, alternative, gap)) {
    (1, final a?, _) => ShowAlternative(a),
    (1, null, final g?) => g,
    (_, _, final g?) => g,
    (_, final a?, null) => ShowAlternative(a),
    _ => null,
  };
}

/// A prerequisite the student has tried and is still learning, with a
/// lesson to go back to.
GoBackToPrerequisite? weakPrerequisite(
  String skill,
  Curriculum curriculum,
  Map<String, SkillState> states,
) {
  for (final p in curriculum.prerequisitesOf(skill)) {
    final state = states[p];
    final lessonId = curriculum.lessonFor(p);
    if (state != null &&
        lessonId != null &&
        state.level(curriculum.criteriaFor(p)) == MasteryLevel.learning) {
      return GoBackToPrerequisite(skill: p, lessonId: lessonId);
    }
  }
  return null;
}

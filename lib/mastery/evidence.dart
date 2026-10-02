import '../lessons/step_result.dart';
import '../models/lesson.dart';
import '../models/lesson_step.dart';
import 'curriculum.dart';
import 'skill_state.dart';

/// Turns a finished step into mastery evidence. Steps without a
/// `question_type` (explanations, predictions) are not evidence.
/// [itemId] defaults to `lessonId/stepId`.
Evidence? evidenceFor(
  Lesson lesson,
  LessonStep step,
  StepResult result,
  DateTime at, {
  String? questionType,
  String? skill,
  String? itemId,
}) {
  if (step is! QuestionStep || result.correct == null) return null;
  final type = questionType ?? (step as QuestionStep).questionType;
  if (type == null) return null;
  return Evidence(
    skill: skill ?? Curriculum.skillOf(lesson, step as QuestionStep),
    itemId: itemId ?? '${lesson.id}/${step.id}',
    at: at,
    questionType: type,
    firstTry: result.correct!,
    solved: result.solved ?? result.correct!,
  );
}

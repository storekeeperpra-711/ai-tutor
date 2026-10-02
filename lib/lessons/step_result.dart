/// What happened in one step. The player saves these and feeds them to
/// the mastery engine.
class StepResult {
  const StepResult({
    required this.stepId,
    this.correct,
    this.solved,
    this.attempts = 0,
    this.misconceptionIds = const [],
  });

  final String stepId;

  /// Right on the first try. null for steps without a question (explain,
  /// summary).
  final bool? correct;

  /// Right in the end, after hints or retries. null without a question.
  final bool? solved;
  final int attempts;

  /// Misconceptions the student's wrong answers pointed to.
  final List<String> misconceptionIds;
}

typedef StepDone = void Function(StepResult result);

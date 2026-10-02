/// What happened in one step. The player collects these; Phase 3 saves
/// them and Phase 4 feeds them to the mastery engine.
class StepResult {
  const StepResult({
    required this.stepId,
    this.correct,
    this.attempts = 0,
    this.misconceptionIds = const [],
  });

  final String stepId;

  /// null for steps without a question (explain, summary).
  final bool? correct;
  final int attempts;

  /// Misconceptions the student's wrong answers pointed to.
  final List<String> misconceptionIds;
}

typedef StepDone = void Function(StepResult result);

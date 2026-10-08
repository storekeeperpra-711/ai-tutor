import 'package:flutter/material.dart';

import '../../models/lesson_step.dart';
import '../answer_checking.dart';
import '../step_result.dart';
import 'answer_step_view.dart';

/// The student types a fraction, a chemical equation, algebra working or
/// a short text answer, and the step's checker decides.
class TextCheckStepView extends StatelessWidget {
  const TextCheckStepView({
    super.key,
    required this.step,
    required this.onDone,
  });

  final TextCheckStep step;
  final StepDone onDone;

  @override
  Widget build(BuildContext context) => AnswerStepView(
    stepId: step.id,
    prompt: step.prompt,
    hint: step.hint,
    feedbackCorrect: step.feedbackCorrect,
    feedbackWrong: step.feedbackWrong,
    maxAttempts: step.maxAttempts,
    character: step.character,
    figure: step.figure,
    multiline: step.multiline,
    check: (input, l10n, language) =>
        checkTextStep(step, input, l10n, language),
    onDone: onDone,
  );
}

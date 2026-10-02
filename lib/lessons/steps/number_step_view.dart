import 'package:flutter/material.dart';

import '../../models/lesson_step.dart';
import '../answer_checking.dart';
import '../step_result.dart';
import 'answer_step_view.dart';

/// The student types a number (or a fraction, with the fraction checker).
class NumberStepView extends StatelessWidget {
  const NumberStepView({super.key, required this.step, required this.onDone});

  final NumberStep step;
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
    unit: step.unit,
    numberKeyboard: step.checker == 'numeric',
    check: (input, l10n, language) =>
        checkNumberStep(step, input, l10n, language),
    onDone: onDone,
  );
}

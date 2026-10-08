import 'package:flutter/material.dart';

import '../../character/mithu_bubble.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../lesson_figure.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

class ExplainStepView extends StatelessWidget {
  const ExplainStepView({super.key, required this.step, required this.onDone});

  final ExplainStep step;
  final StepDone onDone;

  @override
  Widget build(BuildContext context) {
    return StepScaffold(
      buttonLabel: AppLocalizations.of(context).continueButton,
      onPressed: () => onDone(StepResult(stepId: step.id)),
      children: [
        if (step.character != null) ...[
          MithuBubble(line: step.character!),
          const SizedBox(height: 24),
        ],
        StepPrompt(
          step.text,
          figure: step.figure,
          style: Theme.of(context).textTheme.titleLarge,
        ),
      ],
    );
  }
}

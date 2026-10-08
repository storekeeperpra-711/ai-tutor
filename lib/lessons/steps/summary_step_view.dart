import 'package:flutter/material.dart';

import '../../character/mithu_bubble.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../lesson_figure.dart';
import '../lesson_text.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

class SummaryStepView extends StatelessWidget {
  const SummaryStepView({super.key, required this.step, required this.onDone});

  final SummaryStep step;
  final StepDone onDone;

  @override
  Widget build(BuildContext context) {
    final textTheme = Theme.of(context).textTheme;
    return StepScaffold(
      buttonLabel: AppLocalizations.of(context).continueButton,
      onPressed: () => onDone(StepResult(stepId: step.id)),
      children: [
        if (step.character != null) ...[
          MithuBubble(line: step.character!),
          const SizedBox(height: 24),
        ],
        StepPrompt(step.text, figure: step.figure, style: textTheme.titleLarge),
        const SizedBox(height: 16),
        for (final point in step.points)
          ListTile(
            leading: const Icon(Icons.check_circle, color: Color(0xFF43A047)),
            title: LessonText(point, style: textTheme.bodyLarge),
          ),
      ],
    );
  }
}

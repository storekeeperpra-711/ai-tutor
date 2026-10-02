import 'package:flutter/material.dart';

import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

/// Shown for step types the app can't play yet, so the lesson still works.
class UnsupportedStepView extends StatelessWidget {
  const UnsupportedStepView({
    super.key,
    required this.step,
    required this.onDone,
  });

  final LessonStep step;
  final StepDone onDone;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return StepScaffold(
      buttonLabel: l10n.continueButton,
      onPressed: () => onDone(StepResult(stepId: step.id)),
      children: [
        const Icon(Icons.construction, size: 48),
        const SizedBox(height: 16),
        Text(l10n.stepNotSupported(step.type), textAlign: TextAlign.center),
      ],
    );
  }
}

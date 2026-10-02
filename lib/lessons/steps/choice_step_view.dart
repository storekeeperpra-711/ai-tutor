import 'package:flutter/material.dart';

import '../../character/mithu_bubble.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../lesson_text.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

/// Multiple choice. Every option has its own feedback. A wrong option is
/// greyed out and the student tries again, so the step always ends with
/// the right idea (and the options run out, so it can't loop forever).
class ChoiceStepView extends StatefulWidget {
  const ChoiceStepView({super.key, required this.step, required this.onDone});

  final ChoiceStep step;
  final StepDone onDone;

  @override
  State<ChoiceStepView> createState() => _ChoiceStepViewState();
}

class _ChoiceStepViewState extends State<ChoiceStepView> {
  final _tried = <String>{};
  ChoiceOption? _last;

  bool get _solved => _last?.correct ?? false;

  void _pick(ChoiceOption option) => setState(() {
    _tried.add(option.id);
    _last = option;
  });

  void _finish() {
    final wrong = widget.step.options.where(
      (o) => _tried.contains(o.id) && !o.correct,
    );
    widget.onDone(
      StepResult(
        stepId: widget.step.id,
        correct: wrong.isEmpty,
        // The right option is always found in the end.
        solved: true,
        attempts: _tried.length,
        misconceptionIds: [
          for (final o in wrong)
            if (o.misconceptionId != null) o.misconceptionId!,
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final step = widget.step;
    final textTheme = Theme.of(context).textTheme;
    return StepScaffold(
      buttonLabel: AppLocalizations.of(context).continueButton,
      onPressed: _solved ? _finish : null,
      children: [
        if (step.character != null) ...[
          MithuBubble(line: step.character!),
          const SizedBox(height: 24),
        ],
        LessonText(step.prompt, style: textTheme.titleLarge),
        const SizedBox(height: 16),
        for (final option in step.options)
          Padding(
            padding: const EdgeInsets.only(bottom: 8),
            child: OutlinedButton(
              key: Key('option-${option.id}'),
              onPressed: _solved || _tried.contains(option.id)
                  ? null
                  : () => _pick(option),
              style: _solved && option.correct
                  ? OutlinedButton.styleFrom(
                      side: const BorderSide(
                        color: Color(0xFF43A047),
                        width: 2,
                      ),
                    )
                  : null,
              child: Align(
                alignment: AlignmentDirectional.centerStart,
                child: LessonText(option.text, style: textTheme.titleMedium),
              ),
            ),
          ),
        if (_last != null)
          FeedbackBox(
            good: _last!.correct,
            child: LessonText(_last!.feedback, style: textTheme.bodyLarge),
          ),
      ],
    );
  }
}

import 'package:flutter/material.dart';

import '../../character/mithu_bubble.dart';
import '../../checkers/numeric_checker.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../../models/localized_text.dart';
import '../lesson_text.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

/// The student types a number. Feedback names the exact mistake when the
/// answer is a known common wrong answer; otherwise the hint is shown.
/// After `maxAttempts` wrong answers the full working is shown and the
/// student moves on (never an endless loop).
class NumberStepView extends StatefulWidget {
  const NumberStepView({super.key, required this.step, required this.onDone});

  final NumberStep step;
  final StepDone onDone;

  @override
  State<NumberStepView> createState() => _NumberStepViewState();
}

enum _State { answering, correct, outOfAttempts }

class _NumberStepViewState extends State<NumberStepView> {
  final _controller = TextEditingController();
  var _state = _State.answering;
  var _attempts = 0;
  final _misconceptions = <String>[];

  /// Feedback for the latest wrong answer, if it was a common wrong one.
  LocalizedText? _specificFeedback;
  var _unreadable = false;

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _check() {
    final step = widget.step;
    final value = parseNumber(_controller.text);
    if (value == null) {
      setState(() => _unreadable = true);
      return;
    }

    setState(() {
      _unreadable = false;
      _attempts++;
      if (numbersMatch(value, step.answer, tolerance: step.tolerance)) {
        _state = _State.correct;
        return;
      }
      final known = step.commonWrong
          .where((w) => numbersMatch(value, w.answer))
          .firstOrNull;
      _specificFeedback = known?.feedback;
      if (known?.misconceptionId != null) {
        _misconceptions.add(known!.misconceptionId!);
      }
      if (_attempts >= step.maxAttempts) _state = _State.outOfAttempts;
    });
  }

  void _finish() => widget.onDone(
    StepResult(
      stepId: widget.step.id,
      correct: _state == _State.correct && _attempts == 1,
      attempts: _attempts,
      misconceptionIds: _misconceptions,
    ),
  );

  @override
  Widget build(BuildContext context) {
    final step = widget.step;
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final answering = _state == _State.answering;

    return StepScaffold(
      buttonKey: Key(answering ? 'step-check' : 'step-continue'),
      buttonLabel: answering ? l10n.checkButton : l10n.continueButton,
      onPressed: answering ? _check : _finish,
      children: [
        if (step.character != null) ...[
          MithuBubble(line: step.character!),
          const SizedBox(height: 24),
        ],
        LessonText(step.prompt, style: textTheme.titleLarge),
        const SizedBox(height: 16),
        TextField(
          key: const Key('number-input'),
          controller: _controller,
          enabled: answering,
          // Numbers are typed left-to-right even in Urdu.
          textDirection: TextDirection.ltr,
          keyboardType: const TextInputType.numberWithOptions(
            decimal: true,
            signed: true,
          ),
          style: textTheme.headlineSmall,
          decoration: InputDecoration(
            labelText: l10n.answerLabel,
            suffixText: step.unit?.of(context),
            border: const OutlineInputBorder(),
          ),
          onSubmitted: answering ? (_) => _check() : null,
        ),
        if (_unreadable)
          FeedbackBox(good: false, child: Text(l10n.typeANumber)),
        if (_state == _State.correct)
          FeedbackBox(
            good: true,
            child: LessonText(step.feedbackCorrect, style: textTheme.bodyLarge),
          ),
        if (_state == _State.outOfAttempts)
          FeedbackBox(
            good: false,
            child: LessonText(step.feedbackWrong, style: textTheme.bodyLarge),
          ),
        if (answering && _attempts > 0)
          FeedbackBox(
            good: false,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                if (_specificFeedback != null)
                  LessonText(_specificFeedback!, style: textTheme.bodyLarge)
                else
                  Text(l10n.tryAgain, style: textTheme.bodyLarge),
                const SizedBox(height: 8),
                Text('${l10n.hintLabel}:', style: textTheme.labelLarge),
                LessonText(step.hint, style: textTheme.bodyLarge),
              ],
            ),
          ),
      ],
    );
  }
}

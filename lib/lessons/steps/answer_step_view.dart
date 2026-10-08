import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../character/mithu_bubble.dart';
import '../../character/sounds.dart';
import '../../l10n/app_localizations.dart';
import '../../models/figure.dart';
import '../../models/lesson_step.dart';
import '../../models/localized_text.dart';
import '../answer_checking.dart';
import '../lesson_figure.dart';
import '../lesson_text.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

typedef AnswerChecker = AnswerCheck Function(
  String input,
  AppLocalizations l10n,
  String languageCode,
);

/// Shared screen for steps where the student types an answer (number and
/// text_check). Wrong answers get feedback naming the mistake, plus the
/// hint. After `maxAttempts` wrong answers the full working is shown and
/// the student moves on (never an endless loop). Unreadable answers and
/// "almost" answers (right value, wrong form) don't use up an attempt.
class AnswerStepView extends ConsumerStatefulWidget {
  const AnswerStepView({
    super.key,
    required this.stepId,
    required this.prompt,
    required this.hint,
    required this.feedbackCorrect,
    required this.feedbackWrong,
    required this.maxAttempts,
    required this.check,
    required this.onDone,
    this.character,
    this.figure,
    this.unit,
    this.multiline = false,
    this.numberKeyboard = false,
  });

  final String stepId;
  final LocalizedText prompt;
  final LocalizedText hint;
  final LocalizedText feedbackCorrect;
  final LocalizedText feedbackWrong;
  final int maxAttempts;
  final AnswerChecker check;
  final StepDone onDone;
  final CharacterLine? character;
  final StepFigure? figure;
  final LocalizedText? unit;
  final bool multiline;
  final bool numberKeyboard;

  @override
  ConsumerState<AnswerStepView> createState() => _AnswerStepViewState();
}

enum _Phase { answering, correct, outOfAttempts }

class _AnswerStepViewState extends ConsumerState<AnswerStepView> {
  final _controller = TextEditingController();
  var _phase = _Phase.answering;
  var _attempts = 0;
  final _misconceptions = <String>[];
  AnswerCheck? _last;
  var _checks = 0;

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _check() {
    final l10n = AppLocalizations.of(context);
    final language = Localizations.localeOf(context).languageCode;
    final result = widget.check(_controller.text, l10n, language);
    ref.playSound(result.correct ? Sound.right : Sound.tryAgain);
    setState(() {
      _last = result;
      _checks++;
      if (result.correct) {
        _attempts++;
        _phase = _Phase.correct;
        return;
      }
      if (!result.countsAsAttempt) return;
      _attempts++;
      if (result.misconceptionId != null) {
        _misconceptions.add(result.misconceptionId!);
      }
      if (_attempts >= widget.maxAttempts) _phase = _Phase.outOfAttempts;
    });
  }

  void _finish() => widget.onDone(
    StepResult(
      stepId: widget.stepId,
      correct: _phase == _Phase.correct && _attempts == 1,
      solved: _phase == _Phase.correct,
      attempts: _attempts,
      misconceptionIds: _misconceptions,
    ),
  );

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final answering = _phase == _Phase.answering;
    final last = _last;

    return StepScaffold(
      buttonKey: Key(answering ? 'step-check' : 'step-continue'),
      buttonLabel: answering ? l10n.checkButton : l10n.continueButton,
      onPressed: answering ? _check : _finish,
      children: [
        if (widget.character != null) ...[
          MithuBubble(
            line: widget.character!,
            reaction: _last == null
                ? null
                : (correct: _last!.correct, attempt: _checks),
          ),
          const SizedBox(height: 24),
        ],
        StepPrompt(
          widget.prompt,
          figure: widget.figure,
          style: textTheme.titleLarge,
        ),
        const SizedBox(height: 16),
        TextField(
          key: const Key('answer-input'),
          controller: _controller,
          enabled: answering,
          // Numbers, formulas and equations are written left-to-right
          // even in Urdu.
          textDirection: TextDirection.ltr,
          keyboardType: widget.multiline
              ? TextInputType.multiline
              : widget.numberKeyboard
              ? const TextInputType.numberWithOptions(
                  decimal: true,
                  signed: true,
                )
              : TextInputType.text,
          minLines: widget.multiline ? 3 : 1,
          maxLines: widget.multiline ? 8 : 1,
          autocorrect: false,
          enableSuggestions: false,
          style: textTheme.headlineSmall,
          decoration: InputDecoration(
            labelText: l10n.answerLabel,
            helperText: widget.multiline ? l10n.answerHintMultiline : null,
            suffixText: widget.unit?.of(context),
            border: const OutlineInputBorder(),
          ),
          onSubmitted: answering && !widget.multiline ? (_) => _check() : null,
        ),
        if (_phase == _Phase.correct)
          FeedbackBox(
            good: true,
            child: LessonText(
              widget.feedbackCorrect,
              style: textTheme.bodyLarge,
            ),
          ),
        if (_phase == _Phase.outOfAttempts)
          FeedbackBox(
            good: false,
            child: LessonText(widget.feedbackWrong, style: textTheme.bodyLarge),
          ),
        if (answering && last != null)
          FeedbackBox(
            good: false,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(last.message ?? l10n.tryAgain, style: textTheme.bodyLarge),
                if (last.countsAsAttempt) ...[
                  const SizedBox(height: 8),
                  Text('${l10n.hintLabel}:', style: textTheme.labelLarge),
                  LessonText(widget.hint, style: textTheme.bodyLarge),
                ],
              ],
            ),
          ),
        if (last != null)
          Padding(
            padding: const EdgeInsets.only(top: 4),
            child: Text(l10n.checkedByCode, style: textTheme.labelSmall),
          ),
      ],
    );
  }
}

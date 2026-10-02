import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../app/motion.dart';
import '../../character/mithu_bubble.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../../sims/native/native_sims.dart';
import '../../sims/sim_host.dart';
import '../answer_checking.dart';
import '../lesson_text.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

/// A simulation step. The child plays with the simulation (WebView or
/// native) and presses its Check button; the app then checks the result
/// with the same checkers as typed answers. Without `expected`, the step
/// is for exploring and the child can carry on at any time.
class SimStepView extends ConsumerStatefulWidget {
  const SimStepView({super.key, required this.step, required this.onDone});

  final SimStep step;
  final StepDone onDone;

  @override
  ConsumerState<SimStepView> createState() => SimStepViewState();
}

enum _Phase { answering, correct, outOfAttempts, failed }

class SimStepViewState extends ConsumerState<SimStepView> {
  var _phase = _Phase.answering;
  var _attempts = 0;
  final _misconceptions = <String>[];
  AnswerCheck? _last;
  final _feedbackKey = GlobalKey();

  /// Scrolls new feedback into view (it is below the simulation).
  void _showFeedback() => WidgetsBinding.instance.addPostFrameCallback((_) {
    final target = _feedbackKey.currentContext;
    if (target != null && target.mounted) {
      Scrollable.ensureVisible(
        target,
        duration: const Duration(milliseconds: 300),
        alignmentPolicy: ScrollPositionAlignmentPolicy.keepVisibleAtEnd,
      ).ignore();
    }
  });

  /// The simulation reported something. Also used by tests, which have
  /// no WebView, to report a result directly.
  void onSimEvent(SimEvent e) {
    if (!mounted) return;
    switch (e.event) {
      case 'error':
        if (_phase == _Phase.answering) {
          setState(() => _phase = _Phase.failed);
          _showFeedback();
        }
      case 'result':
        _onResult(e.data);
    }
  }

  void _onResult(Map<String, dynamic> data) {
    final step = widget.step;
    if (step.expected == null || _phase != _Phase.answering) return;
    final l10n = AppLocalizations.of(context);
    final language = Localizations.localeOf(context).languageCode;
    final check = checkSimResult(step, data, l10n, language);
    setState(() {
      _last = check;
      if (check.correct) {
        _attempts++;
        _phase = _Phase.correct;
        return;
      }
      if (!check.countsAsAttempt) return;
      _attempts++;
      if (check.misconceptionId != null) {
        _misconceptions.add(check.misconceptionId!);
      }
      if (_attempts >= step.maxAttempts) _phase = _Phase.outOfAttempts;
    });
    _showFeedback();
  }

  void _finish() {
    final question = widget.step.expected != null && _phase != _Phase.failed;
    widget.onDone(
      StepResult(
        stepId: widget.step.id,
        correct: question ? _phase == _Phase.correct && _attempts == 1 : null,
        solved: question ? _phase == _Phase.correct : null,
        attempts: _attempts,
        misconceptionIds: _misconceptions,
      ),
    );
  }

  Widget _simulation(String language) {
    final step = widget.step;
    final args = SimArgs(
      step: step,
      language: language,
      onEvent: onSimEvent,
      reduceMotion: reduceMotion(context),
    );
    if (step.isWebView) return ref.read(webSimBuilderProvider)(args);
    final builder = nativeSims[step.simId];
    if (builder == null) {
      WidgetsBinding.instance.addPostFrameCallback(
        (_) => onSimEvent(const SimEvent('error')),
      );
      return const SizedBox.shrink();
    }
    return builder(args);
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final language = Localizations.localeOf(context).languageCode;
    final step = widget.step;
    final explore = step.expected == null;
    final done = switch (_phase) {
      _Phase.answering => explore,
      _ => true,
    };
    final last = _last;

    final feedback = <Widget>[
      if (_phase == _Phase.failed)
        FeedbackBox(
          good: false,
          child: Text(l10n.simCouldNotStart, style: textTheme.bodyLarge),
        ),
      if (_phase == _Phase.correct)
        FeedbackBox(
          good: true,
          child: LessonText(step.feedbackCorrect!, style: textTheme.bodyLarge),
        ),
      if (_phase == _Phase.outOfAttempts)
        FeedbackBox(
          good: false,
          child: LessonText(step.feedbackWrong!, style: textTheme.bodyLarge),
        ),
      if (_phase == _Phase.answering && last != null)
        FeedbackBox(
          good: false,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(last.message ?? l10n.tryAgain, style: textTheme.bodyLarge),
              if (last.countsAsAttempt && step.hint != null) ...[
                const SizedBox(height: 8),
                Text('${l10n.hintLabel}:', style: textTheme.labelLarge),
                LessonText(step.hint!, style: textTheme.bodyLarge),
              ],
            ],
          ),
        ),
      if (last != null)
        Padding(
          padding: const EdgeInsets.only(top: 4),
          child: Text(l10n.checkedByCode, style: textTheme.labelSmall),
        ),
    ];

    // The simulation gets a fixed, generous height; the prompt and the
    // feedback scroll around it on small phones.
    final simHeight = (MediaQuery.sizeOf(context).height * 0.62).clamp(
      400.0,
      560.0,
    );
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Expanded(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                if (step.character != null) ...[
                  MithuBubble(line: step.character!),
                  const SizedBox(height: 12),
                ],
                LessonText(step.prompt, style: textTheme.titleMedium),
                const SizedBox(height: 12),
                SizedBox(
                  height: simHeight,
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(12),
                    child: DecoratedBox(
                      key: const Key('sim-area'),
                      decoration: BoxDecoration(
                        border: Border.all(
                          color: Theme.of(context).dividerColor,
                        ),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: _phase == _Phase.failed
                          ? const Center(
                              child: Icon(Icons.extension_off, size: 48),
                            )
                          // Keyed by language, so switching language
                          // restarts the simulation in the new language.
                          : KeyedSubtree(
                              key: ValueKey('${step.id}-$language'),
                              child: _simulation(language),
                            ),
                    ),
                  ),
                ),
                if (!done && feedback.isEmpty)
                  Padding(
                    padding: const EdgeInsets.only(top: 8),
                    child: Text(
                      l10n.simUseActivity,
                      textAlign: TextAlign.center,
                      style: textTheme.bodySmall,
                    ),
                  ),
                KeyedSubtree(
                  key: _feedbackKey,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: feedback,
                  ),
                ),
              ],
            ),
          ),
        ),
        SafeArea(
          top: false,
          child: Padding(
            padding: const EdgeInsets.all(16),
            child: FilledButton(
              key: const Key('step-continue'),
              onPressed: done ? _finish : null,
              child: Text(l10n.continueButton),
            ),
          ),
        ),
      ],
    );
  }
}

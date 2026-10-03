import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../app/motion.dart';
import '../../character/mithu_bubble.dart';
import '../../character/mithu_controller.dart';
import '../../character/narrator.dart';
import '../../character/number_pictures.dart';
import '../../character/sounds.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../lesson_text.dart';
import '../step_result.dart';
import 'picture_step_parts.dart';

enum _Phase { counting, correct, outOfAttempts }

/// Tap mangoes to drop them in the basket; Mithu counts each one aloud.
/// Tap a mango in the basket to take it out again. The tick checks the
/// count. No reading needed: right and wrong show in Mithu's face and a
/// sound.
class TapCountStepView extends ConsumerStatefulWidget {
  const TapCountStepView({super.key, required this.step, required this.onDone});

  final TapCountStep step;
  final StepDone onDone;

  @override
  ConsumerState<TapCountStepView> createState() => _TapCountStepViewState();
}

class _TapCountStepViewState extends ConsumerState<TapCountStepView> {
  final _mithu = MithuController();
  late final Narrator _narrator = ref.read(narratorProvider);

  /// Which mangoes (by position on the tree) are in the basket, in order.
  final _basket = <int>[];
  var _phase = _Phase.counting;
  var _attempts = 0;
  MithuReaction? _reaction;

  @override
  void dispose() {
    _narrator.stop();
    _mithu.dispose();
    super.dispose();
  }

  void _toggle(int mango) {
    if (_phase != _Phase.counting) return;
    setState(() {
      if (!_basket.remove(mango)) _basket.add(mango);
      _reaction = null;
    });
    ref.playSound(Sound.basket);
    sayNumber(_narrator, _mithu, context, _basket.length);
  }

  void _check() {
    final right = _basket.length == widget.step.count;
    _attempts++;
    ref.playSound(right ? Sound.right : Sound.tryAgain);
    setState(() {
      _reaction = (correct: right, attempt: _attempts);
      if (right) {
        _phase = _Phase.correct;
      } else if (_attempts >= widget.step.maxAttempts) {
        // Show the right number of mangoes, and say it.
        _phase = _Phase.outOfAttempts;
        _basket
          ..clear()
          ..addAll(List.generate(widget.step.count, (i) => i));
      }
    });
    if (_phase != _Phase.counting) {
      sayNumber(_narrator, _mithu, context, widget.step.count);
    }
  }

  void _finish() => widget.onDone(
    StepResult(
      stepId: widget.step.id,
      correct: _phase == _Phase.correct && _attempts == 1,
      solved: _phase == _Phase.correct,
      attempts: _attempts,
    ),
  );

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final step = widget.step;
    final counting = _phase == _Phase.counting;
    final still = reduceMotion(context);
    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        if (step.character != null)
          MithuBubble(
            line: step.character!,
            reaction: _reaction,
            controller: _mithu,
          ),
        const SizedBox(height: 8),
        LessonText(step.prompt, style: Theme.of(context).textTheme.titleMedium),
        const SizedBox(height: 16),
        // The tree: mangoes still to pick.
        Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: const Color(0xFFC8E6C9),
            borderRadius: BorderRadius.circular(40),
          ),
          child: Wrap(
            alignment: WrapAlignment.center,
            spacing: 8,
            runSpacing: 8,
            children: [
              for (var i = 0; i < step.shown; i++)
                SizedBox.square(
                  dimension: 76,
                  child: _basket.contains(i)
                      ? null
                      : InkResponse(
                          key: Key('mango-$i'),
                          onTap: () => _toggle(i),
                          child: const Mango(size: 72),
                        ),
                ),
            ],
          ),
        ),
        const SizedBox(height: 16),
        // The basket.
        AnimatedContainer(
          key: const Key('basket'),
          duration: still ? Duration.zero : const Duration(milliseconds: 250),
          constraints: const BoxConstraints(minHeight: 110),
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: const Color(0xFFD7B98E),
            borderRadius: const BorderRadius.vertical(
              bottom: Radius.circular(48),
              top: Radius.circular(12),
            ),
            border: Border.all(
              color: switch (_phase) {
                _Phase.correct => Colors.green,
                _Phase.outOfAttempts => Colors.amber,
                _ => const Color(0xFF8D6E63),
              },
              width: 5,
            ),
          ),
          child: Wrap(
            alignment: WrapAlignment.center,
            spacing: 4,
            runSpacing: 4,
            children: [
              for (final i in _basket)
                InkResponse(
                  key: Key('basket-mango-$i'),
                  onTap: () => _toggle(i),
                  child: const Mango(size: 56),
                ),
            ],
          ),
        ),
        const SizedBox(height: 24),
        if (counting)
          BigIconButton(
            key: const Key('step-check'),
            icon: Icons.check_rounded,
            label: l10n.checkButton,
            onPressed: _basket.isEmpty ? null : _check,
          )
        else
          BigIconButton(
            key: const Key('step-continue'),
            icon: Icons.arrow_forward_rounded,
            label: l10n.continueButton,
            color: Colors.green,
            onPressed: _finish,
          ),
      ],
    );
  }
}

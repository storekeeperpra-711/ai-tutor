import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';

import '../../app/motion.dart';
import '../../character/mithu_bubble.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson_step.dart';
import '../lesson_text.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

/// A small animation with an optional line of text. With "Less movement"
/// on, it shows the last frame as a still picture.
class LottieStepView extends StatefulWidget {
  const LottieStepView({super.key, required this.step, required this.onDone});

  final LottieStep step;
  final StepDone onDone;

  @override
  State<LottieStepView> createState() => _LottieStepViewState();
}

class _LottieStepViewState extends State<LottieStepView>
    with SingleTickerProviderStateMixin {
  late final _controller = AnimationController(
    vsync: this,
    animationBehavior: AnimationBehavior.preserve,
  );

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _play() {
    if (reduceMotion(context)) {
      _controller.value = 1;
    } else if (widget.step.loop) {
      _controller.repeat();
    } else {
      _controller.forward(from: 0);
    }
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final step = widget.step;
    return StepScaffold(
      buttonLabel: l10n.continueButton,
      onPressed: () => widget.onDone(StepResult(stepId: step.id)),
      children: [
        if (step.character != null) ...[
          MithuBubble(line: step.character!),
          const SizedBox(height: 16),
        ],
        GestureDetector(
          // Tap to watch it again.
          onTap: step.loop ? null : _play,
          child: AspectRatio(
            aspectRatio: 1,
            child: Lottie.asset(
              'assets/lottie/${step.src}',
              key: const Key('lottie'),
              controller: _controller,
              onLoaded: (composition) {
                _controller.duration = composition.duration;
                _play();
              },
              errorBuilder: (_, _, _) =>
                  const Center(child: Icon(Icons.image_not_supported)),
            ),
          ),
        ),
        if (step.text != null) ...[
          const SizedBox(height: 16),
          LessonText(
            step.text!,
            style: Theme.of(context).textTheme.titleMedium,
            textAlign: TextAlign.center,
          ),
        ],
      ],
    );
  }
}

import 'package:flutter/material.dart';

import '../../app/motion_widgets.dart';
import '../../app/theme/app_theme.dart';

/// Common layout for every step: scrollable content and, at the bottom,
/// one big action button (Continue / Check / Finish).
class StepScaffold extends StatelessWidget {
  const StepScaffold({
    super.key,
    required this.children,
    required this.buttonLabel,
    required this.onPressed,
    this.buttonKey = const Key('step-continue'),
  });

  final List<Widget> children;
  final String buttonLabel;

  /// null disables the button.
  final VoidCallback? onPressed;
  final Key buttonKey;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Expanded(
          // A step has only a few widgets, so build them all at once
          // (a ListView would skip feedback that is still off-screen).
          child: SingleChildScrollView(
            padding: const EdgeInsets.fromLTRB(20, 12, 20, 16),
            // Each new step slides in (its state is new, so this runs once).
            child: EnterAnimation(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: children,
              ),
            ),
          ),
        ),
        SafeArea(
          top: false,
          child: Padding(
            padding: const EdgeInsets.fromLTRB(20, 4, 20, 20),
            child: SizedBox(
              width: double.infinity,
              child: Pressable(
                child: FilledButton(
                  key: buttonKey,
                  onPressed: onPressed,
                  child: Text(buttonLabel),
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }
}

/// Coloured box for feedback after an answer.
class FeedbackBox extends StatelessWidget {
  const FeedbackBox({super.key, required this.good, required this.child});

  final bool good;
  final Widget child;

  @override
  Widget build(BuildContext context) {
    // Gentle colours: a wrong answer is part of learning, not a failure.
    final ink = good ? const Color(0xFF14532D) : const Color(0xFF7A3B00);
    return EnterAnimation(
      key: Key(good ? 'feedback-good' : 'feedback-try'),
      child: Container(
        margin: const EdgeInsets.only(top: 16),
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: good ? AppColors.greenSoft : AppColors.orangeSoft,
          borderRadius: BorderRadius.circular(AppRadius.tile),
        ),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Icon(
              good ? Icons.check_circle_rounded : Icons.lightbulb_rounded,
              color: good ? AppColors.green : AppColors.orange,
            ),
            const SizedBox(width: 10),
            Expanded(
              child: DefaultTextStyle.merge(
                style: TextStyle(color: ink),
                child: child,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

/// One answer to choose: a numbered tile that turns green when it is the
/// right answer and fades once tried.
class ChoiceTile extends StatelessWidget {
  const ChoiceTile({
    super.key,
    required this.number,
    required this.child,
    required this.onPressed,
    this.right = false,
    this.tried = false,
  });

  final int number;
  final Widget child;

  /// null when it can't be chosen (already tried, or the step is solved).
  final VoidCallback? onPressed;
  final bool right;
  final bool tried;

  @override
  Widget build(BuildContext context) {
    final radius = BorderRadius.circular(AppRadius.button);
    final tile = AnimatedOpacity(
      duration: const Duration(milliseconds: 200),
      opacity: tried && !right ? 0.5 : 1,
      child: Material(
        color: right ? AppColors.greenSoft : const Color(0xFFFAF9FF),
        shape: RoundedRectangleBorder(
          borderRadius: radius,
          side: BorderSide(
            color: right ? AppColors.green : AppColors.line,
            width: 2,
          ),
        ),
        child: InkWell(
          borderRadius: radius,
          onTap: onPressed,
          child: ConstrainedBox(
            constraints: const BoxConstraints(minHeight: 56),
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
              child: Row(
                children: [
                  Container(
                    width: 30,
                    height: 30,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      color: right ? AppColors.green : AppColors.lilacSoft,
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: right
                        ? const Icon(
                            Icons.check_rounded,
                            size: 18,
                            color: Colors.white,
                          )
                        : Text(
                            '$number',
                            style: const TextStyle(
                              fontFamily: latinFontFamily,
                              fontWeight: FontWeight.w900,
                              color: Color(0xFF4B3CC4),
                            ),
                          ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(child: child),
                ],
              ),
            ),
          ),
        ),
      ),
    );
    return Semantics(
      button: true,
      enabled: onPressed != null,
      child: onPressed == null ? tile : Pressable(child: tile),
    );
  }
}

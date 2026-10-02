import 'package:flutter/material.dart';

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
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: children,
            ),
          ),
        ),
        SafeArea(
          top: false,
          child: Padding(
            padding: const EdgeInsets.all(16),
            child: SizedBox(
              width: double.infinity,
              child: FilledButton(
                key: buttonKey,
                onPressed: onPressed,
                child: Text(buttonLabel),
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
    final colors = Theme.of(context).colorScheme;
    return Container(
      key: Key(good ? 'feedback-good' : 'feedback-try'),
      margin: const EdgeInsets.only(top: 16),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        // Gentle colours: a wrong answer is part of learning, not a failure.
        color: good ? const Color(0xFFE8F5E9) : const Color(0xFFFFF3E0),
        border: Border.all(
          color: good ? const Color(0xFF43A047) : const Color(0xFFFFA726),
        ),
        borderRadius: BorderRadius.circular(12),
      ),
      child: DefaultTextStyle.merge(
        style: TextStyle(color: colors.onSurface),
        child: child,
      ),
    );
  }
}

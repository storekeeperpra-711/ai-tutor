import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';

import '../../app/motion.dart';

/// A short celebration over everything (lesson finished, a new mastery
/// level). It doesn't block the screen and removes itself. With "Less
/// movement" on, only the message shows, without the burst.
void celebrate(BuildContext context, String message) {
  final overlay = Overlay.maybeOf(context, rootOverlay: true);
  if (overlay == null) return;
  late final OverlayEntry entry;
  entry = OverlayEntry(
    builder: (_) => _Celebration(
      message: message,
      still: reduceMotion(context),
      onDone: () => entry.remove(),
    ),
  );
  overlay.insert(entry);
}

class _Celebration extends StatefulWidget {
  const _Celebration({
    required this.message,
    required this.still,
    required this.onDone,
  });

  final String message;
  final bool still;
  final VoidCallback onDone;

  @override
  State<_Celebration> createState() => _CelebrationState();
}

class _CelebrationState extends State<_Celebration>
    with SingleTickerProviderStateMixin {
  // Drives the fade and how long it stays. Always runs, even with less
  // movement, so the message is shown for the same time and then goes.
  late final _controller =
      AnimationController(
          vsync: this,
          duration: const Duration(milliseconds: 1800),
          animationBehavior: AnimationBehavior.preserve,
        )
        ..addStatusListener((s) {
          if (s == AnimationStatus.completed) widget.onDone();
        })
        ..forward();

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final opacity = widget.still
        ? const AlwaysStoppedAnimation(1.0)
        : CurvedAnimation(
            parent: _controller,
            curve: const Interval(0.75, 1, curve: Curves.easeIn),
          ).drive(Tween(begin: 1.0, end: 0.0));
    return IgnorePointer(
      child: FadeTransition(
        opacity: opacity,
        child: Center(
          key: const Key('celebration'),
          child: Stack(
            alignment: Alignment.center,
            children: [
              if (!widget.still)
                SizedBox.square(
                  dimension: 280,
                  child: Lottie.asset(
                    'assets/lottie/celebrate.json',
                    controller: _controller,
                    errorBuilder: (_, _, _) => const SizedBox.shrink(),
                  ),
                ),
              Material(
                color: Theme.of(context).colorScheme.primaryContainer,
                elevation: 4,
                borderRadius: BorderRadius.circular(16),
                child: Padding(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 20,
                    vertical: 12,
                  ),
                  child: Text(
                    widget.message,
                    textAlign: TextAlign.center,
                    style: Theme.of(context).textTheme.titleLarge,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

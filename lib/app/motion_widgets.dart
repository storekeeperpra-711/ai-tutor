import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'motion.dart';
import 'theme/age_tier.dart';
import 'theme/app_theme.dart';

/// The new look's movement (Shahid's reference video, 2026-10-05): a new
/// screen rises with a curved top edge, cards float in one after another,
/// pressed things sink a little, numbers count up and soft dots drift
/// behind headers. Each is short and cheap, so it stays smooth on a
/// low-cost phone, and each is skipped when "Less movement" (or the
/// phone's own "remove animations") is on.

/// A new screen rises from the bottom with a curved top edge; the screen
/// under it sinks back a little. Going back reverses it.
class WavePageTransitionsBuilder extends PageTransitionsBuilder {
  const WavePageTransitionsBuilder();

  @override
  Duration get transitionDuration => const Duration(milliseconds: 420);

  @override
  Widget buildTransitions<T>(
    PageRoute<T> route,
    BuildContext context,
    Animation<double> animation,
    Animation<double> secondaryAnimation,
    Widget child,
  ) {
    if (reduceMotion(context)) {
      return FadeTransition(opacity: animation, child: child);
    }
    final rise = CurvedAnimation(
      parent: animation,
      curve: Curves.easeOutCubic,
      reverseCurve: Curves.easeInCubic,
    );
    final sink = Tween<double>(begin: 1, end: 0.96).animate(
      CurvedAnimation(parent: secondaryAnimation, curve: Curves.easeOut),
    );
    return ScaleTransition(
      scale: sink,
      child: AnimatedBuilder(
        animation: rise,
        child: child,
        builder: (context, child) => rise.value >= 1
            ? child!
            : ClipPath(clipper: WaveClipper(rise.value), child: child),
      ),
    );
  }
}

/// The part of a rising screen that is showing: everything below a top
/// edge that bulges upwards in the middle, flattening as it arrives.
class WaveClipper extends CustomClipper<Path> {
  const WaveClipper(this.progress);

  /// 0 = nothing showing, 1 = the whole screen.
  final double progress;

  @override
  Path getClip(Size size) {
    final p = progress.clamp(0.0, 1.0);
    final bulge = 90 * (1 - p) * math.min(p * 4, 1);
    final edge = size.height * (1 - p) + bulge;
    return Path()
      ..moveTo(0, edge)
      ..quadraticBezierTo(size.width / 2, edge - 2 * bulge, size.width, edge)
      ..lineTo(size.width, size.height)
      ..lineTo(0, size.height)
      ..close();
  }

  @override
  bool shouldReclip(WaveClipper old) => old.progress != progress;
}

/// Fades and slides [child] up into place when it first appears; with an
/// [index], items in a list arrive one after another.
class EnterAnimation extends StatefulWidget {
  const EnterAnimation({super.key, this.index = 0, required this.child});

  /// Position in a list: each step waits a little longer (up to 8 steps).
  final int index;
  final Widget child;

  static const duration = Duration(milliseconds: 380);
  static const stagger = Duration(milliseconds: 60);

  @override
  State<EnterAnimation> createState() => _EnterAnimationState();
}

class _EnterAnimationState extends State<EnterAnimation>
    with SingleTickerProviderStateMixin {
  // The wait before an item's turn is the start of one longer animation,
  // so there is no separate timer.
  late final _wait = EnterAnimation.stagger * math.min(widget.index, 8);
  late final _controller = AnimationController(
    vsync: this,
    duration: _wait + EnterAnimation.duration,
  );
  late final _curve = CurvedAnimation(
    parent: _controller,
    curve: Interval(
      _wait.inMicroseconds / _controller.duration!.inMicroseconds,
      1,
      curve: Curves.easeOutCubic,
    ),
  );
  var _started = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (_started) return;
    _started = true;
    if (reduceMotion(context)) {
      _controller.value = 1;
    } else {
      _controller.forward();
    }
  }

  @override
  void dispose() {
    _curve.dispose();
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => FadeTransition(
    opacity: _curve,
    child: SlideTransition(
      position: Tween(
        begin: const Offset(0, 0.08),
        end: Offset.zero,
      ).animate(_curve),
      child: widget.child,
    ),
  );
}

/// Sinks [child] a little while a finger is on it. It only watches the
/// finger, so the buttons and cards inside still get the tap.
class Pressable extends StatefulWidget {
  const Pressable({super.key, required this.child});

  final Widget child;

  @override
  State<Pressable> createState() => _PressableState();
}

class _PressableState extends State<Pressable> {
  var _down = false;

  void _set(bool down) {
    if (down != _down) setState(() => _down = down);
  }

  @override
  Widget build(BuildContext context) {
    if (reduceMotion(context)) return widget.child;
    return Listener(
      onPointerDown: (_) => _set(true),
      onPointerUp: (_) => _set(false),
      onPointerCancel: (_) => _set(false),
      child: AnimatedScale(
        scale: _down ? 0.96 : 1,
        duration: const Duration(milliseconds: 120),
        curve: Curves.easeOut,
        child: widget.child,
      ),
    );
  }
}

/// A whole number that counts up to [value] when it appears or changes.
class CountUp extends StatelessWidget {
  const CountUp({
    super.key,
    required this.value,
    this.style,
    this.format = _plain,
  });

  final int value;
  final TextStyle? style;

  /// Turns the number shown into text, e.g. `(n) => '$n%'`.
  final String Function(int) format;

  static String _plain(int n) => '$n';

  @override
  Widget build(BuildContext context) {
    if (reduceMotion(context)) return Text(format(value), style: style);
    return TweenAnimationBuilder<double>(
      tween: Tween(begin: 0, end: value.toDouble()),
      duration: const Duration(milliseconds: 900),
      curve: Curves.easeOutCubic,
      builder: (context, v, _) => Text(format(v.round()), style: style),
    );
  }
}

/// A few soft coloured dots drifting slowly, painted behind a header.
/// One painter, one slow timer and no shadows, so it costs very little.
/// The dots drift once round (14 s) when the screen opens and then rest,
/// so a cheap phone isn't kept drawing; still when movement is reduced.
class FloatingDots extends StatefulWidget {
  const FloatingDots({super.key, this.colors = _colors});

  final List<Color> colors;

  static const _colors = [
    Color(0x335B4BDB),
    Color(0x332E9D5B),
    Color(0x33E06A00),
    Color(0x339D1F5C),
  ];

  @override
  State<FloatingDots> createState() => _FloatingDotsState();
}

class _FloatingDotsState extends State<FloatingDots>
    with SingleTickerProviderStateMixin {
  late final _controller = AnimationController(
    vsync: this,
    duration: const Duration(seconds: 14),
  );

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (reduceMotion(context)) {
      _controller.stop();
    } else if (!_controller.isAnimating && !_controller.isCompleted) {
      _controller.forward();
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => IgnorePointer(
    child: RepaintBoundary(
      child: CustomPaint(
        painter: DotsPainter(_controller, widget.colors),
        size: Size.infinite,
      ),
    ),
  );
}

class DotsPainter extends CustomPainter {
  DotsPainter(this.time, this.colors) : super(repaint: time);

  final Animation<double> time;
  final List<Color> colors;

  /// (x, y, radius, how far it drifts) as parts of the area, fixed so the
  /// picture is the same each time.
  static const _dots = [
    (0.08, 0.20, 0.035, 0.05),
    (0.86, 0.12, 0.05, 0.04),
    (0.70, 0.62, 0.025, 0.06),
    (0.22, 0.78, 0.045, 0.04),
    (0.95, 0.85, 0.03, 0.05),
    (0.45, 0.08, 0.02, 0.06),
  ];

  @override
  void paint(Canvas canvas, Size size) {
    final t = time.value * 2 * math.pi;
    final paint = Paint();
    for (final (i, (x, y, r, drift)) in _dots.indexed) {
      paint.color = colors[i % colors.length];
      final dx = math.sin(t + i * 1.7) * drift * size.width;
      final dy = math.cos(t * (i.isEven ? 1 : -1) + i) * drift * size.height;
      canvas.drawCircle(
        Offset(x * size.width + dx, y * size.height + dy),
        r * size.shortestSide * 2,
        paint,
      );
    }
  }

  @override
  bool shouldRepaint(DotsPainter old) => old.colors != colors;
}

/// The screen background of the new look: the age group's soft colour at
/// the top, fading into the plain background.
class TintedBackground extends ConsumerWidget {
  const TintedBackground({super.key, required this.child, this.dots = false});

  final Widget child;

  /// Floating dots behind the top of the screen.
  final bool dots;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final tint = tierStyles[ref.watch(ageTierProvider)]!.tint;
    return DecoratedBox(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
          colors: [tint, AppColors.background],
          stops: const [0, 0.5],
        ),
      ),
      child: dots
          ? Stack(
              children: [
                const Positioned(
                  top: 0,
                  left: 0,
                  right: 0,
                  height: 260,
                  child: FloatingDots(),
                ),
                child,
              ],
            )
          : child,
    );
  }
}

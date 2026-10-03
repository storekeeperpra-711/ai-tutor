import 'dart:math' as math;

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

import '../app/motion.dart';

/// Mithu's moods (spec C2, plus "curious" for wrong answers). Names match
/// the lesson JSON `character.emotion` values.
enum MithuMood {
  idle,
  talking,
  happy,
  thinking,
  encouraging,
  surprised,
  celebrating,
  curious;

  /// The mood named in a lesson; unknown names fall back to [idle].
  static MithuMood parse(String? name) =>
      values.where((m) => m.name == name).firstOrNull ?? idle;
}

/// Mithu, the rose-ringed parakeet, drawn in code (Phase 7 decision 1).
///
/// Everything outside this file talks to Mithu only through [mood] and
/// [mouth], so a Rive character can replace the drawing later.
class MithuView extends StatefulWidget {
  const MithuView({super.key, required this.mood, this.size = 96, this.mouth});

  final MithuMood mood;
  final double size;

  /// How far the beak is open (0 to 1) while Mithu speaks; follows the
  /// loudness of the recording. Null: closed, or a gentle loop when
  /// [mood] is [MithuMood.talking].
  final ValueListenable<double>? mouth;

  @override
  State<MithuView> createState() => _MithuViewState();
}

class _MithuViewState extends State<MithuView>
    with SingleTickerProviderStateMixin {
  // One slow loop drives every movement (sway, hop, flap, blink). It plays
  // a couple of times when Mithu appears or changes mood, then rests, so
  // Mithu draws the eye when something happens and not all the time.
  late final _loop = AnimationController(
    vsync: this,
    duration: const Duration(milliseconds: 2400),
  );
  static const _loops = 2;
  var _still = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final still = reduceMotion(context);
    if (still == _still && _loop.lastElapsedDuration != null) return;
    _still = still;
    _play();
  }

  @override
  void didUpdateWidget(MithuView old) {
    super.didUpdateWidget(old);
    if (old.mood != widget.mood) _play();
  }

  void _play() {
    if (_still) {
      _loop.stop();
      _loop.value = 0;
    } else {
      _loop.repeat(count: _loops);
    }
  }

  @override
  void dispose() {
    _loop.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final mouth = widget.mouth;
    return Semantics(
      label: 'Mithu (${widget.mood.name})',
      image: true,
      child: SizedBox.square(
        dimension: widget.size,
        child: RepaintBoundary(
          child: AnimatedBuilder(
            animation: Listenable.merge([_loop, ?mouth]),
            builder: (context, _) => CustomPaint(
              painter: MithuPainter(
                mood: widget.mood,
                phase: _loop.value % 1,
                mouth: mouth?.value,
                still: _still,
              ),
            ),
          ),
        ),
      ),
    );
  }
}

/// Paints Mithu in a 100 × 100 box, scaled to the widget's size.
class MithuPainter extends CustomPainter {
  MithuPainter({
    required this.mood,
    required this.phase,
    this.mouth,
    this.still = false,
  });

  final MithuMood mood;

  /// 0 to 1, looping.
  final double phase;
  final double? mouth;
  final bool still;

  static const _green = Color(0xFF4CAF50);
  static const _darkGreen = Color(0xFF2E7D32);
  static const _lightGreen = Color(0xFFA5D6A7);
  static const _beak = Color(0xFFE53935);
  static const _beakDark = Color(0xFFB71C1C);
  static const _ringPink = Color(0xFFF48FB1);
  static const _ringBlack = Color(0xFF212121);

  double get _wave => math.sin(phase * 2 * math.pi);

  /// How open the beak is, 0 to 1.
  double get _beakOpen {
    if (mouth != null) return mouth!.clamp(0.0, 1.0);
    return switch (mood) {
      MithuMood.talking =>
        still ? 0.4 : (math.sin(phase * 2 * math.pi * 8) + 1) / 2 * 0.8,
      MithuMood.surprised => 0.7,
      MithuMood.celebrating || MithuMood.happy => 0.35,
      _ => 0,
    };
  }

  /// Eyes closed for a short moment once per loop.
  bool get _blinking =>
      !still &&
      phase > 0.92 &&
      phase < 0.97 &&
      mood != MithuMood.happy &&
      mood != MithuMood.surprised;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.save();
    canvas.scale(size.width / 100, size.height / 100);

    // Whole-body movement.
    final dy = switch (mood) {
      MithuMood.happy || MithuMood.celebrating => -6 * _wave.abs(),
      _ => 1.2 * _wave,
    };
    final sway = mood == MithuMood.idle || mood == MithuMood.talking
        ? 0.03 * _wave
        : 0.0;
    canvas.translate(50, 60 + dy);
    canvas.rotate(sway);
    canvas.translate(-50, -60);

    _paintTail(canvas);
    _paintBody(canvas);
    _paintFeet(canvas);
    _paintWings(canvas);

    // The head tilts when curious or thinking.
    canvas.save();
    final tilt = switch (mood) {
      MithuMood.curious => -0.28,
      MithuMood.thinking => 0.12,
      _ => 0.0,
    };
    canvas.translate(50, 40);
    canvas.rotate(tilt);
    canvas.translate(-50, -40);
    _paintHead(canvas);
    canvas.restore();

    canvas.restore();

    // Extras outside the body's movement.
    canvas.save();
    canvas.scale(size.width / 100, size.height / 100);
    if (mood == MithuMood.curious) _paintQuestionMark(canvas);
    if (mood == MithuMood.celebrating) _paintConfetti(canvas);
    if (mood == MithuMood.thinking) _paintThoughtDots(canvas);
    canvas.restore();
  }

  Paint _fill(Color color) => Paint()
    ..color = color
    ..isAntiAlias = true;

  Paint _shaded(Rect rect, Color light, Color dark) => Paint()
    ..shader = RadialGradient(
      center: const Alignment(-0.35, -0.45),
      radius: 0.95,
      colors: [light, dark],
    ).createShader(rect);

  void _paintTail(Canvas canvas) {
    final tail = Path()
      ..moveTo(46, 78)
      ..quadraticBezierTo(44, 92, 40, 99)
      ..lineTo(47, 98)
      ..quadraticBezierTo(50, 90, 54, 79)
      ..close();
    canvas.drawPath(tail, _fill(_darkGreen));
    final tail2 = Path()
      ..moveTo(52, 78)
      ..quadraticBezierTo(54, 90, 56, 98)
      ..lineTo(61, 95)
      ..quadraticBezierTo(58, 88, 57, 77)
      ..close();
    canvas.drawPath(tail2, _fill(const Color(0xFF388E3C)));
  }

  void _paintBody(Canvas canvas) {
    final rect = Rect.fromCenter(
      center: const Offset(50, 62),
      width: 40,
      height: 40,
    );
    canvas.drawOval(rect, _shaded(rect, _lightGreen, _green));
    final belly = Rect.fromCenter(
      center: const Offset(52, 67),
      width: 24,
      height: 26,
    );
    canvas.drawOval(belly, _fill(const Color(0xFFC5E1A5)));
  }

  void _paintFeet(Canvas canvas) {
    final paint = Paint()
      ..color = const Color(0xFF8D6E63)
      ..strokeWidth = 2.6
      ..strokeCap = StrokeCap.round
      ..style = PaintingStyle.stroke;
    for (final x in [44.0, 55.0]) {
      canvas.drawLine(Offset(x, 80), Offset(x, 85), paint);
      canvas.drawLine(Offset(x - 3, 86), Offset(x + 3, 86), paint);
    }
  }

  void _paintWings(Canvas canvas) {
    // Angle of each wing: 0 rests on the body, positive lifts it.
    final flap = still ? 0.5 : (_wave + 1) / 2;
    final (double left, double right) = switch (mood) {
      MithuMood.celebrating => (1.3 + 0.5 * flap, 1.3 + 0.5 * flap),
      MithuMood.encouraging => (0.0, 1.9),
      MithuMood.thinking => (0.0, 2.4),
      MithuMood.surprised => (0.6, 0.6),
      MithuMood.happy => (0.25 * flap, 0.25 * flap),
      _ => (0.0, 0.0),
    };
    _paintWing(canvas, const Offset(35, 56), left, mirror: false);
    _paintWing(canvas, const Offset(65, 56), right, mirror: true);
  }

  void _paintWing(
    Canvas canvas,
    Offset shoulder,
    double lift, {
    required bool mirror,
  }) {
    canvas.save();
    canvas.translate(shoulder.dx, shoulder.dy);
    if (mirror) canvas.scale(-1, 1);
    canvas.rotate(lift);
    final wing = Path()
      ..moveTo(0, 0)
      ..quadraticBezierTo(-9, 8, -5, 24)
      ..quadraticBezierTo(3, 16, 4, 2)
      ..close();
    const rect = Rect.fromLTWH(-9, 0, 14, 24);
    canvas.drawPath(wing, _shaded(rect, const Color(0xFF66BB6A), _darkGreen));
    // Flight feathers.
    final line = Paint()
      ..color = const Color(0xFF1B5E20)
      ..strokeWidth = 0.8
      ..style = PaintingStyle.stroke;
    canvas.drawLine(const Offset(-3, 10), const Offset(-4, 20), line);
    canvas.drawLine(const Offset(0, 9), const Offset(-1, 18), line);
    canvas.restore();
  }

  void _paintHead(Canvas canvas) {
    // Neck ring (black then pink) under the head.
    final ring = Paint()
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round;
    final ringRect = Rect.fromCenter(
      center: const Offset(50, 40),
      width: 32,
      height: 30,
    );
    canvas.drawArc(
      ringRect,
      0.35,
      2.45,
      false,
      ring
        ..color = _ringBlack
        ..strokeWidth = 2.0,
    );
    canvas.drawArc(
      ringRect.inflate(2.4),
      0.3,
      2.55,
      false,
      ring
        ..color = _ringPink
        ..strokeWidth = 2.2,
    );

    // Crest feathers rise when surprised.
    if (mood == MithuMood.surprised || mood == MithuMood.celebrating) {
      final crest = Path()
        ..moveTo(44, 24)
        ..lineTo(42, 13)
        ..lineTo(48, 22)
        ..lineTo(50, 11)
        ..lineTo(53, 22)
        ..lineTo(58, 14)
        ..lineTo(56, 25)
        ..close();
      canvas.drawPath(crest, _fill(_green));
    }

    final head = Rect.fromCenter(
      center: const Offset(50, 36),
      width: 32,
      height: 30,
    );
    canvas.drawOval(head, _shaded(head, const Color(0xFFC8E6C9), _green));
    // Blue-grey cheek wash, as on real rose-ringed parakeets.
    canvas.drawOval(
      Rect.fromCenter(center: const Offset(56, 42), width: 10, height: 6),
      _fill(const Color(0x3364B5F6)),
    );

    _paintEye(canvas, const Offset(57, 33));
    _paintBeak(canvas);
  }

  void _paintEye(Canvas canvas, Offset c) {
    final happyEyes =
        mood == MithuMood.happy ||
        mood == MithuMood.celebrating ||
        mood == MithuMood.encouraging;
    if (_blinking || happyEyes) {
      final stroke = Paint()
        ..color = _ringBlack
        ..strokeWidth = 1.6
        ..strokeCap = StrokeCap.round
        ..style = PaintingStyle.stroke;
      if (happyEyes) {
        // A smiling "^" eye.
        canvas.drawArc(
          Rect.fromCenter(center: c.translate(0, 1.5), width: 7, height: 6),
          math.pi,
          math.pi,
          false,
          stroke,
        );
      } else {
        canvas.drawLine(c.translate(-3, 0), c.translate(3, 0), stroke);
      }
      return;
    }
    final big = mood == MithuMood.surprised ? 1.35 : 1.0;
    // Where the eye looks: up when thinking, at the child otherwise.
    final look = switch (mood) {
      MithuMood.thinking => const Offset(0.4, -1.4),
      MithuMood.curious => const Offset(1, 0.3),
      _ => const Offset(0.8, 0),
    };
    canvas.drawCircle(c, 4.6 * big, _fill(Colors.white));
    canvas.drawCircle(
      c,
      4.6 * big,
      Paint()
        ..color = const Color(0xFFFF8A65)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 0.9,
    );
    canvas.drawCircle(c + look, 2.5 * big, _fill(_ringBlack));
    canvas.drawCircle(
      c + look + const Offset(-0.9, -0.9),
      0.9,
      _fill(Colors.white),
    );
  }

  void _paintBeak(Canvas canvas) {
    final open = _beakOpen * 5;
    // Lower beak swings down as Mithu talks.
    final lower = Path()
      ..moveTo(60, 41)
      ..quadraticBezierTo(66, 43 + open, 64, 46 + open)
      ..quadraticBezierTo(61, 46 + open * 0.6, 59, 43)
      ..close();
    canvas.drawPath(lower, _fill(_beakDark));
    // Upper beak: the parakeet's hooked red beak.
    final upper = Path()
      ..moveTo(58, 36)
      ..quadraticBezierTo(68, 34, 69, 41)
      ..quadraticBezierTo(69, 45, 65, 46)
      ..quadraticBezierTo(66, 42, 59, 42)
      ..close();
    const rect = Rect.fromLTWH(58, 34, 11, 12);
    canvas.drawPath(upper, _shaded(rect, const Color(0xFFFF7961), _beak));
  }

  void _paintQuestionMark(Canvas canvas) {
    final painter = TextPainter(
      text: const TextSpan(
        text: '?',
        style: TextStyle(
          fontSize: 22,
          fontWeight: FontWeight.bold,
          color: Color(0xFFFFA726),
        ),
      ),
      textDirection: TextDirection.ltr,
    )..layout();
    painter.paint(canvas, Offset(74, 6 + (still ? 0 : 2 * _wave)));
  }

  void _paintThoughtDots(Canvas canvas) {
    final paint = _fill(const Color(0xFF90A4AE));
    for (var i = 0; i < 3; i++) {
      final up = still ? 0.0 : 1.5 * math.sin((phase + i * 0.2) * 2 * math.pi);
      canvas.drawCircle(
        Offset(70.0 + i * 7, 18.0 - i * 4 + up),
        1.6 + i * 0.6,
        paint,
      );
    }
  }

  void _paintConfetti(Canvas canvas) {
    const colors = [
      Color(0xFFFFC107),
      Color(0xFFE91E63),
      Color(0xFF03A9F4),
      Color(0xFF8BC34A),
    ];
    final random = math.Random(7);
    for (var i = 0; i < 14; i++) {
      final x = random.nextDouble() * 100;
      final fall = still ? 0.0 : phase * 30;
      final y = (random.nextDouble() * 50 + fall) % 50;
      canvas.drawRect(
        Rect.fromCenter(center: Offset(x, y), width: 3, height: 2),
        _fill(colors[i % colors.length]),
      );
    }
  }

  @override
  bool shouldRepaint(MithuPainter old) =>
      old.mood != mood ||
      old.phase != phase ||
      old.mouth != mouth ||
      old.still != still;
}

import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../models/localized_text.dart';

/// Number words for Mithu to say while counting (1 to 10).
LocalizedText numberWord(int n) => LocalizedText(
  en: const [
    'zero', 'one', 'two', 'three', 'four', 'five', //
    'six', 'seven', 'eight', 'nine', 'ten',
  ][n.clamp(0, 10)],
  ur: const [
    'صفر', 'ایک', 'دو', 'تین', 'چار', 'پانچ', //
    'چھ', 'سات', 'آٹھ', 'نو', 'دس',
  ][n.clamp(0, 10)],
);

/// [n] in the app's digits: Urdu digits (۳) in Urdu.
String localDigits(int n, String languageCode) => languageCode == 'ur'
    ? n.toString().split('').map((c) => '۰۱۲۳۴۵۶۷۸۹'[int.parse(c)]).join()
    : '$n';

/// A ripe mango, drawn in code.
class Mango extends StatelessWidget {
  const Mango({super.key, this.size = 64});

  final double size;

  @override
  Widget build(BuildContext context) => SizedBox.square(
    dimension: size,
    child: CustomPaint(painter: _MangoPainter()),
  );
}

class _MangoPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 100, size.height / 100);
    // Body: a tilted, slightly kidney-shaped oval.
    canvas.save();
    canvas.translate(50, 56);
    canvas.rotate(-0.5);
    final body = Rect.fromCenter(center: Offset.zero, width: 62, height: 80);
    canvas.drawOval(
      body,
      Paint()
        ..shader = const RadialGradient(
          center: Alignment(-0.4, -0.5),
          radius: 1,
          colors: [Color(0xFFFFEB3B), Color(0xFFFFA000), Color(0xFFE65100)],
          stops: [0, 0.6, 1],
        ).createShader(body),
    );
    canvas.restore();
    // Stem and leaf.
    canvas.drawLine(
      const Offset(62, 20),
      const Offset(66, 10),
      Paint()
        ..color = const Color(0xFF6D4C41)
        ..strokeWidth = 4
        ..strokeCap = StrokeCap.round,
    );
    final leaf = Path()
      ..moveTo(66, 12)
      ..quadraticBezierTo(84, 0, 96, 10)
      ..quadraticBezierTo(82, 22, 66, 12)
      ..close();
    canvas.drawPath(leaf, Paint()..color = const Color(0xFF43A047));
  }

  @override
  bool shouldRepaint(_MangoPainter old) => false;
}

/// A number as a picture card: mangoes, dots, fingers or the digit.
class NumberPictureView extends StatelessWidget {
  const NumberPictureView({
    super.key,
    required this.kind,
    required this.value,
    this.size = 120,
  });

  final String kind;
  final int value;
  final double size;

  @override
  Widget build(BuildContext context) {
    final language = Localizations.localeOf(context).languageCode;
    return Semantics(
      label: localDigits(value, language),
      excludeSemantics: true,
      child: SizedBox.square(
        dimension: size,
        child: switch (kind) {
          'mangoes' => Center(
            child: Wrap(
              alignment: WrapAlignment.center,
              children: [
                for (var i = 0; i < value; i++)
                  Mango(size: size / (value > 4 ? 3.2 : 2.4)),
              ],
            ),
          ),
          'dots' => CustomPaint(painter: _DotsPainter(value)),
          'fingers' => CustomPaint(painter: _HandPainter(value)),
          _ => FittedBox(
            child: Padding(
              padding: const EdgeInsets.all(8),
              child: Text(
                localDigits(value, language),
                style: const TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 96,
                  height: 1,
                  color: Color(0xFF3949AB),
                ),
              ),
            ),
          ),
        },
      ),
    );
  }
}

/// Dots laid out like the faces of a dice (up to 6), then in rows.
class _DotsPainter extends CustomPainter {
  _DotsPainter(this.n);

  final int n;

  static const _dice = {
    1: [Offset(.5, .5)],
    2: [Offset(.25, .25), Offset(.75, .75)],
    3: [Offset(.25, .25), Offset(.5, .5), Offset(.75, .75)],
    4: [Offset(.25, .25), Offset(.75, .25), Offset(.25, .75), Offset(.75, .75)],
    5: [
      Offset(.25, .25), Offset(.75, .25), Offset(.5, .5), //
      Offset(.25, .75), Offset(.75, .75),
    ],
    6: [
      Offset(.25, .2), Offset(.75, .2), Offset(.25, .5), //
      Offset(.75, .5), Offset(.25, .8), Offset(.75, .8),
    ],
  };

  @override
  void paint(Canvas canvas, Size size) {
    final points =
        _dice[n] ??
        [
          for (var i = 0; i < n; i++)
            Offset(0.15 + (i % 4) * 0.233, 0.2 + (i ~/ 4) * 0.3),
        ];
    final r = size.width * (n > 6 ? 0.07 : 0.09);
    final paint = Paint()..color = const Color(0xFFE53935);
    for (final p in points) {
      canvas.drawCircle(
        Offset(p.dx * size.width, p.dy * size.height),
        r,
        paint,
      );
    }
  }

  @override
  bool shouldRepaint(_DotsPainter old) => old.n != n;
}

/// A hand holding up [n] fingers (0 to 5), thumb last.
class _HandPainter extends CustomPainter {
  _HandPainter(this.n);

  final int n;

  @override
  void paint(Canvas canvas, Size size) {
    canvas.scale(size.width / 100, size.height / 100);
    final skin = Paint()..color = const Color(0xFFFFCC80);
    final line = Paint()
      ..color = const Color(0xFFBF8B4A)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.5;
    // Fingers, left to right: little finger to index finger.
    const xs = [30.0, 42.0, 54.0, 66.0];
    const heights = [26.0, 34.0, 38.0, 34.0];
    final up = n.clamp(0, 5);
    final fingersUp = math.min(up, 4);
    for (var i = 0; i < 4; i++) {
      // Index finger goes up first, then middle, ring, little.
      final raised = 3 - i < fingersUp;
      final h = raised ? heights[i] : 8.0;
      final r = RRect.fromRectAndRadius(
        Rect.fromLTWH(xs[i] - 5, 48 - h, 10, h + 8),
        const Radius.circular(5),
      );
      canvas.drawRRect(r, skin);
      canvas.drawRRect(r, line);
    }
    // Palm.
    final palm = RRect.fromRectAndRadius(
      const Rect.fromLTWH(24, 44, 50, 46),
      const Radius.circular(14),
    );
    canvas.drawRRect(palm, skin);
    canvas.drawRRect(palm, line);
    // Thumb: out to the side for 5, folded across the palm otherwise.
    canvas.save();
    canvas.translate(74, 66);
    canvas.rotate(up == 5 ? -0.9 : 0.35);
    final thumb = RRect.fromRectAndRadius(
      Rect.fromLTWH(-6, up == 5 ? -26 : -10, 12, up == 5 ? 30 : 14),
      const Radius.circular(6),
    );
    canvas.drawRRect(thumb, skin);
    canvas.drawRRect(thumb, line);
    canvas.restore();
  }

  @override
  bool shouldRepaint(_HandPainter old) => old.n != n;
}

import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../app/theme/app_theme.dart';
import '../models/figure.dart';
import '../models/localized_text.dart';
import 'lesson_text.dart';

/// A step's text or prompt and, under it, the step's figure if it has one.
class StepPrompt extends StatelessWidget {
  const StepPrompt(this.text, {super.key, this.figure, this.style});

  final LocalizedText text;
  final StepFigure? figure;
  final TextStyle? style;

  @override
  Widget build(BuildContext context) {
    final prompt = LessonText(text, style: style);
    if (figure == null) return prompt;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [prompt, const SizedBox(height: 16), LessonFigure(figure!)],
    );
  }
}

/// Draws a lesson figure (see [StepFigure]) on a white card, scaled to the
/// screen width. Screen readers read its alt text in the app's language.
class LessonFigure extends StatelessWidget {
  const LessonFigure(this.figure, {super.key = const Key('step-figure')});

  final StepFigure figure;

  /// Tall figures are made smaller so the question stays on screen.
  static const maxHeight = 320.0;

  @override
  Widget build(BuildContext context) {
    final labelStyle = TextStyle(
      fontFamily: latinFontFamily,
      fontWeight: FontWeight.w800,
      fontSize: MediaQuery.textScalerOf(context).scale(16),
      color: AppColors.ink,
    );
    return Semantics(
      image: true,
      label: figure.alt.of(context),
      child: ExcludeSemantics(
        child: Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(AppRadius.tile),
            border: Border.all(color: AppColors.line, width: 2),
          ),
          child: LayoutBuilder(
            builder: (context, constraints) {
              final aspect = figure.width / figure.height;
              final width = math.min(constraints.maxWidth, maxHeight * aspect);
              return Center(
                child: SizedBox(
                  width: width,
                  height: width / aspect,
                  child: CustomPaint(
                    painter: FigurePainter(figure, labelStyle: labelStyle),
                  ),
                ),
              );
            },
          ),
        ),
      ),
    );
  }
}

/// Paints a [StepFigure]. Strokes keep the same thickness whatever the
/// figure's scale, thick enough to see on a small, dim phone screen.
class FigurePainter extends CustomPainter {
  FigurePainter(this.figure, {required this.labelStyle});

  final StepFigure figure;
  final TextStyle labelStyle;

  static const strokeWidth = 3.0;
  static const dotRadius = 4.5;
  static const dash = 8.0;
  static const gap = 6.0;

  @override
  void paint(Canvas canvas, Size size) {
    final scale = size.width / figure.width;
    Offset at(Offset p) => p * scale;

    for (final item in figure.items) {
      // Shapes are lilac, lines and marks dark ink; dashed lines (mirror
      // and construction lines) are orange so they stand out.
      final stroke = Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = strokeWidth
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round
        ..color = item.dashed
            ? AppColors.orange
            : switch (item.kind) {
                'polygon' || 'circle' => AppColors.lilac,
                _ => AppColors.ink,
              };
      final fill = Paint()..color = AppColors.lilacSoft;

      switch (item.kind) {
        case 'polygon':
          final path = Path()..addPolygon(item.offsets.map(at).toList(), true);
          if (item.fill) canvas.drawPath(path, fill);
          _stroke(canvas, path, stroke, item.dashed);
        case 'line':
          final from = at(item.fromOffset!), to = at(item.toOffset!);
          final path = Path()
            ..moveTo(from.dx, from.dy)
            ..lineTo(to.dx, to.dy);
          _stroke(canvas, path, stroke, item.dashed);
        case 'circle':
          final circle = Rect.fromCircle(
            center: at(item.centerOffset!),
            radius: item.radius * scale,
          );
          final path = Path()..addOval(circle);
          if (item.fill) canvas.drawPath(path, fill);
          _stroke(canvas, path, stroke, item.dashed);
        case 'arc':
          final circle = Rect.fromCircle(
            center: at(item.centerOffset!),
            radius: item.radius * scale,
          );
          final path = Path()
            ..addArc(circle, _radians(item.start), _radians(item.sweep));
          _stroke(canvas, path, stroke, item.dashed);
        case 'point':
          canvas.drawCircle(
            at(item.atOffset!),
            dotRadius,
            Paint()..color = AppColors.ink,
          );
        case 'label':
          _label(canvas, item.text ?? '', at(item.atOffset!));
      }
    }
  }

  static double _radians(double degrees) => degrees * math.pi / 180;

  void _stroke(Canvas canvas, Path path, Paint paint, bool dashed) {
    if (!dashed) {
      canvas.drawPath(path, paint);
      return;
    }
    for (final metric in path.computeMetrics()) {
      for (var d = 0.0; d < metric.length; d += dash + gap) {
        canvas.drawPath(metric.extractPath(d, d + dash), paint);
      }
    }
  }

  /// Labels are centred on their point and always left-to-right (they
  /// are letters, numbers and angles, the same in Urdu and English).
  void _label(Canvas canvas, String text, Offset center) {
    final painter = TextPainter(
      text: TextSpan(text: text, style: labelStyle),
      textDirection: TextDirection.ltr,
    )..layout();
    painter.paint(
      canvas,
      center - Offset(painter.width / 2, painter.height / 2),
    );
    painter.dispose();
  }

  @override
  bool shouldRepaint(FigurePainter oldDelegate) =>
      oldDelegate.figure != figure || oldDelegate.labelStyle != labelStyle;
}

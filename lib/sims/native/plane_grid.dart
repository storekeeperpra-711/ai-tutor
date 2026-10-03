import 'dart:math' as math;
import 'dart:ui';

/// The part of the xy-plane an interactive shows, fitted into a box with
/// square grid cells, and how to go between grid and screen.
class PlaneView {
  PlaneView({
    required this.xMin,
    required this.xMax,
    required this.yMin,
    required this.yMax,
    required Size box,
  }) : unit = math.min(
         (box.width - 2 * _pad) / (xMax - xMin),
         (box.height - 2 * _pad) / (yMax - yMin),
       ) {
    _origin = Offset(
      (box.width - unit * (xMax - xMin)) / 2 - xMin * unit,
      (box.height + unit * (yMax - yMin)) / 2 + yMin * unit,
    );
  }

  /// Room around the grid for the numbers on the axes.
  static const _pad = 20.0;

  final int xMin;
  final int xMax;
  final int yMin;
  final int yMax;

  /// Pixels per grid unit.
  final double unit;
  late final Offset _origin;

  Offset at(num x, num y) => _origin + Offset(x * unit, -y * unit);

  /// The grid position under a screen position.
  (double, double) gridAt(Offset local) =>
      ((local.dx - _origin.dx) / unit, -(local.dy - _origin.dy) / unit);

  /// The nearest whole-number point inside the view.
  math.Point<int> latticeAt(Offset local) {
    final (x, y) = gridAt(local);
    return math.Point(x.round().clamp(xMin, xMax), y.round().clamp(yMin, yMax));
  }

  /// The corners of the view, anticlockwise.
  List<(double, double)> get rect => [
    (xMin.toDouble(), yMin.toDouble()),
    (xMax.toDouble(), yMin.toDouble()),
    (xMax.toDouble(), yMax.toDouble()),
    (xMin.toDouble(), yMax.toDouble()),
  ];

  /// Grid lines, the axes and their numbers.
  void paintGrid(Canvas canvas, Color color) {
    final grid = Paint()
      ..color = color.withValues(alpha: 0.15)
      ..strokeWidth = 1;
    final axis = Paint()
      ..color = color
      ..strokeWidth = 2;
    for (var x = xMin; x <= xMax; x++) {
      canvas.drawLine(at(x, yMin), at(x, yMax), x == 0 ? axis : grid);
    }
    for (var y = yMin; y <= yMax; y++) {
      canvas.drawLine(at(xMin, y), at(xMax, y), y == 0 ? axis : grid);
    }
    final every = math.max(1, (24 / unit).ceil());
    final style = TextStyle(color: color, fontSize: 12);
    void label(String text, Offset centre) {
      final builder =
          ParagraphBuilder(ParagraphStyle(textAlign: TextAlign.center))
            ..pushStyle(style)
            ..addText(text);
      final paragraph = builder.build()
        ..layout(const ParagraphConstraints(width: 32));
      canvas.drawParagraph(
        paragraph,
        centre - Offset(16, paragraph.height / 2),
      );
    }

    final yAxis = 0.clamp(yMin, yMax);
    final xAxis = 0.clamp(xMin, xMax);
    for (var x = xMin; x <= xMax; x++) {
      if (x != 0 && x % every == 0) {
        label('$x', at(x, yAxis) + const Offset(0, 12));
      }
    }
    for (var y = yMin; y <= yMax; y++) {
      if (y != 0 && y % every == 0) {
        label('$y', at(xAxis, y) - const Offset(14, 0));
      }
    }
    label('0', at(xAxis, yAxis) + const Offset(-10, 12));
  }
}

/// The part of [polygon] where `a·x + b·y + c ≤ 0` (Sutherland–Hodgman).
List<(double, double)> clipPolygon(
  List<(double, double)> polygon,
  double a,
  double b,
  double c,
) {
  double f((double, double) p) => a * p.$1 + b * p.$2 + c;
  final out = <(double, double)>[];
  for (var i = 0; i < polygon.length; i++) {
    final p = polygon[i];
    final q = polygon[(i + 1) % polygon.length];
    final fp = f(p);
    final fq = f(q);
    if (fp <= 0) out.add(p);
    if ((fp < 0 && fq > 0) || (fp > 0 && fq < 0)) {
      final t = fp / (fp - fq);
      out.add((p.$1 + t * (q.$1 - p.$1), p.$2 + t * (q.$2 - p.$2)));
    }
  }
  return out;
}

/// Where the line `a·x + b·y + c = 0` crosses the view, or null.
(Offset, Offset)? lineInView(PlaneView view, double a, double b, double c) {
  // The view clipped to the line's two sides meets along the line itself.
  final below = clipPolygon(view.rect, a, b, c);
  final onLine = [
    for (final p in below)
      if ((a * p.$1 + b * p.$2 + c).abs() < 1e-6) p,
  ];
  if (onLine.length < 2) return null;
  return (
    view.at(onLine.first.$1, onLine.first.$2),
    view.at(onLine.last.$1, onLine.last.$2),
  );
}

void drawPolygon(
  Canvas canvas,
  PlaneView view,
  List<(double, double)> polygon,
  Paint paint,
) {
  if (polygon.length < 3) return;
  final path = Path()
    ..moveTo(
      view.at(polygon[0].$1, polygon[0].$2).dx,
      view.at(polygon[0].$1, polygon[0].$2).dy,
    );
  for (final p in polygon.skip(1)) {
    final o = view.at(p.$1, p.$2);
    path.lineTo(o.dx, o.dy);
  }
  canvas.drawPath(path..close(), paint);
}

/// A straight line, solid or dashed.
void drawLine(
  Canvas canvas,
  Offset from,
  Offset to,
  Paint paint, {
  bool dashed = false,
}) {
  if (!dashed) {
    canvas.drawLine(from, to, paint);
    return;
  }
  const dash = 10.0;
  const gap = 7.0;
  final length = (to - from).distance;
  if (length == 0) return;
  final dir = (to - from) / length;
  for (var d = 0.0; d < length; d += dash + gap) {
    canvas.drawLine(
      from + dir * d,
      from + dir * math.min(d + dash, length),
      paint,
    );
  }
}

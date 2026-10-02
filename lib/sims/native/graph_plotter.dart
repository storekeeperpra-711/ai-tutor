import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../checkers/rational.dart';
import '../../l10n/app_localizations.dart';
import '../sim_host.dart';
import 'common.dart';

/// A coordinate grid with a straight line through two points. The child
/// drags the points (or moves them with the arrow buttons) and sees
/// `y = mx + c` change.
///
/// Params: `size` (half-width of the grid, default 5), `points` as
/// `[[x1, y1], [x2, y2]]` to start from. Reports `m` and `c` (as exact
/// fractions like `1/2`).
class GraphPlotter extends StatefulWidget {
  const GraphPlotter({super.key, required this.args});

  final SimArgs args;

  @override
  State<GraphPlotter> createState() => _GraphPlotterState();
}

class _GraphPlotterState extends State<GraphPlotter> {
  late final int _size = intParam(widget.args, 'size', 5, min: 2, max: 10);
  late final List<math.Point<int>> _points = _startPoints();
  var _selected = 0;

  List<math.Point<int>> _startPoints() {
    final raw = widget.args.params['points'];
    if (raw is List && raw.length == 2) {
      try {
        return [
          for (final p in raw.cast<List<dynamic>>())
            math.Point(
              (p[0] as num).round().clamp(-_size, _size),
              (p[1] as num).round().clamp(-_size, _size),
            ),
        ];
      } on Object {
        // Fall through to the default.
      }
    }
    return [const math.Point(0, 0), const math.Point(1, 1)];
  }

  /// Slope and y-intercept, or null for a vertical line.
  (Rational, Rational)? get _line {
    final [a, b] = _points;
    if (a.x == b.x) return null;
    final m = Rational(b.y - a.y, b.x - a.x);
    return (m, Rational(a.y) - m * Rational(a.x));
  }

  void _move(int dx, int dy) => setState(() {
    final p = _points[_selected];
    _points[_selected] = math.Point(
      (p.x + dx).clamp(-_size, _size),
      (p.y + dy).clamp(-_size, _size),
    );
  });

  math.Point<int> _gridAt(Offset local, Size box) {
    final unit = box.shortestSide / (2 * _size + 1);
    final origin = Offset(box.width / 2, box.height / 2);
    return math.Point(
      ((local.dx - origin.dx) / unit).round().clamp(-_size, _size),
      (-(local.dy - origin.dy) / unit).round().clamp(-_size, _size),
    );
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final line = _line;
    final equation = line == null
        ? 'x = ${_points[0].x}'
        : lineEquation(line.$1, line.$2);

    return Directionality(
      textDirection: TextDirection.ltr,
      child: Column(
        children: [
          Expanded(
            child: LayoutBuilder(
              builder: (context, box) {
                final size = Size(box.maxWidth, box.maxHeight);
                return GestureDetector(
                  key: const Key('graph'),
                  onPanStart: (d) {
                    final g = _gridAt(d.localPosition, size);
                    final near = _points.indexed
                        .map((e) => (e.$1, e.$2.squaredDistanceTo(g)))
                        .reduce((a, b) => a.$2 <= b.$2 ? a : b);
                    setState(() => _selected = near.$1);
                  },
                  onPanUpdate: (d) => setState(
                    () => _points[_selected] = _gridAt(d.localPosition, size),
                  ),
                  child: CustomPaint(
                    painter: _GridPainter(
                      size: _size,
                      points: List.of(_points),
                      selected: _selected,
                      color: Theme.of(context).colorScheme.onSurface,
                    ),
                    child: const SizedBox.expand(),
                  ),
                );
              },
            ),
          ),
          Text(
            equation,
            key: const Key('graph-equation'),
            style: Theme.of(context).textTheme.titleLarge,
          ),
          Wrap(
            alignment: WrapAlignment.center,
            spacing: 4,
            children: [
              for (final (i, name) in ['A', 'B'].indexed)
                ChoiceChip(
                  key: Key('point-$i'),
                  label: Text('$name (${_points[i].x}, ${_points[i].y})'),
                  selected: _selected == i,
                  onSelected: (_) => setState(() => _selected = i),
                ),
              for (final (key, icon, dx, dy) in [
                ('move-left', Icons.arrow_back, -1, 0),
                ('move-down', Icons.arrow_downward, 0, -1),
                ('move-up', Icons.arrow_upward, 0, 1),
                ('move-right', Icons.arrow_forward, 1, 0),
              ])
                IconButton.outlined(
                  key: Key(key),
                  onPressed: () => _move(dx, dy),
                  icon: Icon(icon),
                ),
            ],
          ),
          SimCheckBar(
            onCheck: () => reportResult(widget.args, {
              if (line != null) ...{
                'm': line.$1.toString(),
                'c': line.$2.toString(),
              } else
                'vertical': true,
              'equation': equation,
            }),
          ),
          Text(l10n.graphHint, style: Theme.of(context).textTheme.bodySmall),
        ],
      ),
    );
  }
}

/// `y = mx + c` as a student writes it: `y = 2x + 1`, `y = (1/2)x - 3`,
/// `y = -x`, `y = 4`.
String lineEquation(Rational m, Rational c) {
  final mx = switch (m) {
    _ when m.isZero => '',
    _ when m == Rational.one => 'x',
    _ when m == -Rational.one => '-x',
    _ when m.isInteger => '${m}x',
    _ => '($m)x',
  };
  if (mx.isEmpty) return 'y = $c';
  if (c.isZero) return 'y = $mx';
  return c.numerator < 0 ? 'y = $mx - ${-c}' : 'y = $mx + $c';
}

class _GridPainter extends CustomPainter {
  _GridPainter({
    required this.size,
    required this.points,
    required this.selected,
    required this.color,
  });

  final int size;
  final List<math.Point<int>> points;
  final int selected;
  final Color color;

  @override
  void paint(Canvas canvas, Size box) {
    final unit = box.shortestSide / (2 * size + 1);
    final origin = Offset(box.width / 2, box.height / 2);
    Offset at(num x, num y) => origin + Offset(x * unit, -y * unit);

    final grid = Paint()
      ..color = color.withValues(alpha: 0.15)
      ..strokeWidth = 1;
    final axis = Paint()
      ..color = color
      ..strokeWidth = 2;
    for (var i = -size; i <= size; i++) {
      canvas
        ..drawLine(at(i, -size), at(i, size), i == 0 ? axis : grid)
        ..drawLine(at(-size, i), at(size, i), i == 0 ? axis : grid);
    }

    final [a, b] = points;
    canvas
      ..save()
      ..clipRect(Rect.fromPoints(at(-size, size), at(size, -size)));
    final line = Paint()
      ..color = const Color(0xFF00897B)
      ..strokeWidth = 3;
    if (a.x == b.x) {
      canvas.drawLine(at(a.x, -size), at(a.x, size), line);
    } else {
      final m = (b.y - a.y) / (b.x - a.x);
      final c = a.y - m * a.x;
      canvas.drawLine(at(-size, m * -size + c), at(size, m * size + c), line);
    }
    canvas.restore();
    for (final (i, p) in points.indexed) {
      canvas.drawCircle(
        at(p.x, p.y),
        i == selected ? 11 : 8,
        Paint()
          ..color = i == selected
              ? const Color(0xFFFB8C00)
              : const Color(0xFF6A1B9A),
      );
    }
  }

  @override
  bool shouldRepaint(_GridPainter old) => true;
}

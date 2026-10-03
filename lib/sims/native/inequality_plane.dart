import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../checkers/rational.dart';
import '../../l10n/app_localizations.dart';
import '../sim_host.dart';
import 'common.dart';
import 'graph_plotter.dart' show lineEquation;
import 'plane_grid.dart';

/// Showing an inequality in x and y on a graph: the child puts the
/// boundary line through two points (like the graph plotter), chooses a
/// solid line (≤ ≥, the line is included) or a dashed one (< >), and taps
/// the side to shade.
///
/// Params: `size` (half-width of the grid, default 5), `points` as
/// `[[x1, y1], [x2, y2]]` to start from. Reports `inequality`, e.g.
/// `y <= 2x + 1` or `x > 3`, for the linear_inequality_2d checker.
class InequalityPlane extends StatefulWidget {
  const InequalityPlane({super.key, required this.args});

  final SimArgs args;

  @override
  State<InequalityPlane> createState() => _InequalityPlaneState();
}

class _InequalityPlaneState extends State<InequalityPlane> {
  late final int _size = intParam(widget.args, 'size', 5, min: 2, max: 10);
  late final List<math.Point<int>> _points = _startPoints();
  var _selected = 0;
  var _solid = true;

  /// The shaded side: above the line (right of it, if it is upright), or
  /// below. Null until the child taps a side.
  bool? _upper;
  var _askedForSide = false;

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

  bool get _sameSpot => _points[0] == _points[1];

  /// The boundary as `a·x + b·y + c = 0`, with "above" (or "right")
  /// where it is positive.
  (double, double, double) get _line {
    final [p, q] = _points;
    if (p.x == q.x) return (1, 0, -p.x.toDouble());
    final m = (q.y - p.y) / (q.x - p.x);
    return (-m, 1, -(p.y - m * p.x));
  }

  String get _inequality {
    final [p, q] = _points;
    final op = '${_upper! ? '>' : '<'}${_solid ? '=' : ''}';
    if (p.x == q.x) return 'x $op ${p.x}';
    final m = Rational(q.y - p.y, q.x - p.x);
    final c = Rational(p.y) - m * Rational(p.x);
    return lineEquation(m, c).replaceFirst(' = ', ' $op ');
  }

  /// As printed: y ≤ 2x + 1.
  String get _pretty => _inequality
      .replaceFirst('<=', '≤')
      .replaceFirst('>=', '≥')
      .replaceAll('-', '−');

  void _move(int dx, int dy) => setState(() {
    final p = _points[_selected];
    _points[_selected] = math.Point(
      (p.x + dx).clamp(-_size, _size),
      (p.y + dy).clamp(-_size, _size),
    );
  });

  PlaneView _view(Size box) =>
      PlaneView(xMin: -_size, xMax: _size, yMin: -_size, yMax: _size, box: box);

  void _shadeAt(Offset local, Size box) {
    if (_sameSpot) return;
    final (x, y) = _view(box).gridAt(local);
    final (a, b, c) = _line;
    final value = a * x + b * y + c;
    if (value.abs() < 0.2) return; // On the line: not a side.
    setState(() {
      _upper = value > 0;
      _askedForSide = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    return Directionality(
      textDirection: TextDirection.ltr,
      child: Column(
        children: [
          Expanded(
            child: LayoutBuilder(
              builder: (context, box) {
                final size = Size(box.maxWidth, box.maxHeight);
                final view = _view(size);
                return GestureDetector(
                  key: const Key('plane'),
                  onTapUp: (d) => _shadeAt(d.localPosition, size),
                  onPanStart: (d) {
                    final g = view.latticeAt(d.localPosition);
                    final near = _points.indexed
                        .map((e) => (e.$1, e.$2.squaredDistanceTo(g)))
                        .reduce((a, b) => a.$2 <= b.$2 ? a : b);
                    setState(() => _selected = near.$1);
                  },
                  onPanUpdate: (d) => setState(
                    () => _points[_selected] = view.latticeAt(d.localPosition),
                  ),
                  child: CustomPaint(
                    painter: _PlanePainter(
                      view: view,
                      points: List.of(_points),
                      selected: _selected,
                      line: _sameSpot ? null : _line,
                      solid: _solid,
                      upper: _upper,
                      color: Theme.of(context).colorScheme.onSurface,
                    ),
                    child: const SizedBox.expand(),
                  ),
                );
              },
            ),
          ),
          Text(
            _upper == null || _sameSpot ? ' ' : _pretty,
            key: const Key('plane-inequality'),
            style: textTheme.titleLarge,
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
            extra: [
              SegmentedButton<bool>(
                key: const Key('line-kind'),
                segments: [
                  ButtonSegment(value: true, label: Text(l10n.lineSolid)),
                  ButtonSegment(value: false, label: Text(l10n.lineDashed)),
                ],
                selected: {_solid},
                onSelectionChanged: (v) => setState(() => _solid = v.single),
              ),
              IconButton.outlined(
                key: const Key('shade-swap'),
                tooltip: l10n.shadeOtherSide,
                onPressed: () => setState(() {
                  _upper = !(_upper ?? false);
                  _askedForSide = false;
                }),
                icon: const Icon(Icons.swap_vert),
              ),
            ],
            onCheck: () {
              if (_upper == null || _sameSpot) {
                setState(() => _askedForSide = true);
                return;
              }
              reportResult(widget.args, {'inequality': _inequality});
            },
          ),
          if (_askedForSide)
            Text(
              l10n.planeNoSide,
              key: const Key('plane-hint'),
              style: textTheme.bodyMedium?.copyWith(
                color: Theme.of(context).colorScheme.error,
              ),
            ),
        ],
      ),
    );
  }
}

class _PlanePainter extends CustomPainter {
  _PlanePainter({
    required this.view,
    required this.points,
    required this.selected,
    required this.line,
    required this.solid,
    required this.upper,
    required this.color,
  });

  final PlaneView view;
  final List<math.Point<int>> points;
  final int selected;
  final (double, double, double)? line;
  final bool solid;
  final bool? upper;
  final Color color;

  static const _shade = Color(0xFF00897B);

  @override
  void paint(Canvas canvas, Size box) {
    view.paintGrid(canvas, color);
    if (line case (final a, final b, final c)?) {
      if (upper != null) {
        // The shaded side is where the line's value has this sign.
        final s = upper! ? -1.0 : 1.0;
        drawPolygon(
          canvas,
          view,
          clipPolygon(view.rect, s * a, s * b, s * c),
          Paint()..color = _shade.withValues(alpha: 0.25),
        );
      }
      if (lineInView(view, a, b, c) case (final from, final to)?) {
        drawLine(
          canvas,
          from,
          to,
          Paint()
            ..color = _shade
            ..strokeWidth = 3,
          dashed: !solid,
        );
      }
    }
    for (final (i, p) in points.indexed) {
      canvas.drawCircle(
        view.at(p.x, p.y),
        i == selected ? 11 : 8,
        Paint()
          ..color = i == selected
              ? const Color(0xFFFB8C00)
              : const Color(0xFF6A1B9A),
      );
    }
  }

  @override
  bool shouldRepaint(_PlanePainter old) => true;
}

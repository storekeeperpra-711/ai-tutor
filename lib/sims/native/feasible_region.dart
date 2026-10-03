import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../checkers/half_plane_checker.dart';
import '../../checkers/rational.dart';
import '../../l10n/app_localizations.dart';
import '../sim_host.dart';
import 'common.dart';
import 'plane_grid.dart';

/// Several inequalities in x and y drawn together: each boundary line, and
/// the region where all of them are true shaded. The child taps the
/// corners of the region. With an objective like `3x + 2y`, each marked
/// point shows its value, for linear programming.
///
/// Params: `constraints` (inequalities, e.g. `["x + y <= 6", "x >= 0"]`),
/// `x_min` (0), `x_max` (10), `y_min` (0), `y_max` (10), `objective`
/// (optional). Reports `corners`, e.g. `(0, 0), (4, 0), (0, 3)`, for the
/// points checker.
class FeasibleRegion extends StatefulWidget {
  const FeasibleRegion({super.key, required this.args});

  final SimArgs args;

  @override
  State<FeasibleRegion> createState() => _FeasibleRegionState();
}

class _FeasibleRegionState extends State<FeasibleRegion> {
  late final int _xMin = intParam(widget.args, 'x_min', 0, min: -20, max: 19);
  late final int _xMax = intParam(
    widget.args,
    'x_max',
    10,
    min: _xMin + 1,
    max: _xMin + 20,
  );
  late final int _yMin = intParam(widget.args, 'y_min', 0, min: -20, max: 19);
  late final int _yMax = intParam(
    widget.args,
    'y_max',
    10,
    min: _yMin + 1,
    max: _yMin + 20,
  );
  late final List<HalfPlane> _constraints = [
    for (final c in (widget.args.params['constraints'] as List? ?? const []))
      ?_tryParse('$c'),
  ];
  late final Linear2? _objective = _tryObjective();
  final _marked = <math.Point<int>>[];
  var _askedForCorners = false;

  static HalfPlane? _tryParse(String text) {
    try {
      return parseHalfPlane(text);
    } on FormatException {
      return null;
    }
  }

  Linear2? _tryObjective() {
    final text = widget.args.params['objective'];
    if (text is! String) return null;
    try {
      return parseLinear2(text);
    } on FormatException {
      return null;
    }
  }

  PlaneView _view(Size box) =>
      PlaneView(xMin: _xMin, xMax: _xMax, yMin: _yMin, yMax: _yMax, box: box);

  void _toggle(math.Point<int> p) => setState(() {
    _askedForCorners = false;
    if (!_marked.remove(p) && _marked.length < 12) _marked.add(p);
  });

  String _label(math.Point<int> p) {
    final point = '(${p.x}, ${p.y})';
    final objective = _objective;
    if (objective == null) return point;
    final value = objective.valueAt(Rational(p.x), Rational(p.y));
    return '$point: ${widget.args.params['objective']} = $value';
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
                  key: const Key('region'),
                  onTapUp: (d) => _toggle(view.latticeAt(d.localPosition)),
                  child: CustomPaint(
                    painter: _RegionPainter(
                      view: view,
                      constraints: _constraints,
                      marked: List.of(_marked),
                      color: Theme.of(context).colorScheme.onSurface,
                    ),
                    child: const SizedBox.expand(),
                  ),
                );
              },
            ),
          ),
          Wrap(
            alignment: WrapAlignment.center,
            spacing: 4,
            runSpacing: 4,
            children: [
              if (_marked.isEmpty)
                Text(l10n.regionNoCorners, style: textTheme.bodyMedium),
              for (final p in _marked)
                InputChip(
                  key: Key('corner-${p.x}-${p.y}'),
                  label: Text(_label(p)),
                  onDeleted: () => _toggle(p),
                ),
            ],
          ),
          SimCheckBar(
            extra: [
              OutlinedButton.icon(
                key: const Key('region-clear'),
                onPressed: _marked.isEmpty
                    ? null
                    : () => setState(_marked.clear),
                icon: const Icon(Icons.clear),
                label: Text(l10n.regionClear),
              ),
            ],
            onCheck: () {
              if (_marked.isEmpty) {
                setState(() => _askedForCorners = true);
                return;
              }
              reportResult(widget.args, {
                'corners': _marked.map((p) => '(${p.x}, ${p.y})').join(', '),
              });
            },
          ),
          Text(
            l10n.regionHint,
            key: const Key('region-hint'),
            style: _askedForCorners
                ? textTheme.bodyMedium?.copyWith(
                    color: Theme.of(context).colorScheme.error,
                  )
                : textTheme.bodySmall,
          ),
        ],
      ),
    );
  }
}

class _RegionPainter extends CustomPainter {
  _RegionPainter({
    required this.view,
    required this.constraints,
    required this.marked,
    required this.color,
  });

  final PlaneView view;
  final List<HalfPlane> constraints;
  final List<math.Point<int>> marked;
  final Color color;

  static const _shade = Color(0xFF00897B);

  @override
  void paint(Canvas canvas, Size box) {
    view.paintGrid(canvas, color);
    var region = view.rect;
    for (final h in constraints) {
      final l = h.lhs;
      region = clipPolygon(
        region,
        l.a.toDouble(),
        l.b.toDouble(),
        l.c.toDouble(),
      );
    }
    drawPolygon(
      canvas,
      view,
      region,
      Paint()..color = _shade.withValues(alpha: 0.3),
    );
    final line = Paint()
      ..color = _shade
      ..strokeWidth = 2.5;
    for (final h in constraints) {
      final l = h.lhs;
      if (lineInView(view, l.a.toDouble(), l.b.toDouble(), l.c.toDouble())
          case (final from, final to)?) {
        drawLine(canvas, from, to, line, dashed: !h.inclusive);
      }
    }
    for (final p in marked) {
      canvas.drawCircle(
        view.at(p.x, p.y),
        9,
        Paint()..color = const Color(0xFFFB8C00),
      );
    }
  }

  @override
  bool shouldRepaint(_RegionPainter old) => true;
}

import 'package:flutter/material.dart';

import '../../l10n/app_localizations.dart';
import '../sim_host.dart';
import 'common.dart';

/// Showing an inequality on a number line: the child taps a whole number,
/// chooses a filled dot (the number is included: ≤ ≥) or an open dot
/// (< >), and the direction of the arrow.
///
/// Params: `min` (-6), `max` (6), `variable` (x). Reports `inequality`,
/// e.g. `x <= 4`, for the linear_inequality checker.
class InequalityLine extends StatefulWidget {
  const InequalityLine({super.key, required this.args});

  final SimArgs args;

  @override
  State<InequalityLine> createState() => _InequalityLineState();
}

class _InequalityLineState extends State<InequalityLine> {
  late final int _min = intParam(widget.args, 'min', -6, min: -50, max: 49);
  late final int _max = intParam(
    widget.args,
    'max',
    6,
    min: _min + 1,
    max: _min + 24,
  );
  late final String _variable =
      widget.args.params['variable'] as String? ?? 'x';
  late int _at = 0.clamp(_min, _max);
  var _filled = true;
  var _right = true;

  String get _inequality =>
      '$_variable ${_right ? '>' : '<'}${_filled ? '=' : ''} $_at';

  /// The same, as printed: x ≥ 4.
  String get _pretty =>
      '$_variable ${_right ? (_filled ? '≥' : '>') : (_filled ? '≤' : '<')} $_at';

  int _numberAt(double dx, double width) {
    const pad = 24.0;
    final t = ((dx - pad) / (width - 2 * pad) * (_max - _min)).round();
    return (_min + t).clamp(_min, _max);
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final colours = Theme.of(context).colorScheme;
    return Directionality(
      textDirection: TextDirection.ltr,
      child: Column(
        children: [
          Expanded(
            child: LayoutBuilder(
              builder: (context, box) => GestureDetector(
                key: const Key('inequality-line'),
                onTapDown: (d) => setState(
                  () => _at = _numberAt(d.localPosition.dx, box.maxWidth),
                ),
                onHorizontalDragUpdate: (d) => setState(
                  () => _at = _numberAt(d.localPosition.dx, box.maxWidth),
                ),
                child: CustomPaint(
                  painter: _RayPainter(
                    min: _min,
                    max: _max,
                    at: _at,
                    filled: _filled,
                    right: _right,
                    line: colours.onSurface,
                    ray: const Color(0xFFFB8C00),
                  ),
                  child: const SizedBox.expand(),
                ),
              ),
            ),
          ),
          Text(
            _pretty,
            key: const Key('inequality-value'),
            style: Theme.of(context).textTheme.headlineSmall,
          ),
          SimCheckBar(
            extra: [
              IconButton.outlined(
                key: const Key('line-left'),
                onPressed: _at > _min ? () => setState(() => _at--) : null,
                icon: const Icon(Icons.chevron_left),
              ),
              IconButton.outlined(
                key: const Key('line-right'),
                onPressed: _at < _max ? () => setState(() => _at++) : null,
                icon: const Icon(Icons.chevron_right),
              ),
              SegmentedButton<bool>(
                key: const Key('dot-kind'),
                segments: [
                  ButtonSegment(
                    value: true,
                    icon: const Icon(Icons.circle),
                    label: Text(l10n.dotFilled),
                  ),
                  ButtonSegment(
                    value: false,
                    icon: const Icon(Icons.circle_outlined),
                    label: Text(l10n.dotOpen),
                  ),
                ],
                selected: {_filled},
                onSelectionChanged: (v) => setState(() => _filled = v.single),
              ),
              SegmentedButton<bool>(
                key: const Key('ray-direction'),
                segments: const [
                  ButtonSegment(value: false, icon: Icon(Icons.arrow_back)),
                  ButtonSegment(value: true, icon: Icon(Icons.arrow_forward)),
                ],
                selected: {_right},
                onSelectionChanged: (v) => setState(() => _right = v.single),
              ),
            ],
            onCheck: () =>
                reportResult(widget.args, {'inequality': _inequality}),
          ),
        ],
      ),
    );
  }
}

class _RayPainter extends CustomPainter {
  _RayPainter({
    required this.min,
    required this.max,
    required this.at,
    required this.filled,
    required this.right,
    required this.line,
    required this.ray,
  });

  final int min;
  final int max;
  final int at;
  final bool filled;
  final bool right;
  final Color line;
  final Color ray;

  @override
  void paint(Canvas canvas, Size size) {
    const pad = 24.0;
    final y = size.height * 0.55;
    final gap = (size.width - 2 * pad) / (max - min);
    double xOf(int n) => pad + (n - min) * gap;
    final paint = Paint()
      ..color = line
      ..strokeWidth = 2;
    canvas.drawLine(
      Offset(pad - 12, y),
      Offset(size.width - pad + 12, y),
      paint,
    );
    final every = gap < 22 ? 2 : 1;
    for (var n = min; n <= max; n++) {
      final x = xOf(n);
      canvas.drawLine(Offset(x, y - 8), Offset(x, y + 8), paint);
      if ((n - min) % every == 0 || n == 0) {
        final text = TextPainter(
          text: TextSpan(
            text: '$n',
            style: TextStyle(
              color: line,
              fontSize: 15,
              fontWeight: n == 0 ? FontWeight.bold : null,
            ),
          ),
          textDirection: TextDirection.ltr,
        )..layout();
        text.paint(canvas, Offset(x - text.width / 2, y + 12));
      }
    }

    // The solutions: a thick ray from the dot to the end, with an arrow.
    final start = xOf(at);
    final end = right ? size.width - pad + 12 : pad - 12;
    final rayY = y - 22;
    final rayPaint = Paint()
      ..color = ray
      ..strokeWidth = 6
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(Offset(start, rayY), Offset(end, rayY), rayPaint);
    final tip = right ? 1 : -1;
    canvas.drawPath(
      Path()
        ..moveTo(end + tip * 6, rayY)
        ..lineTo(end - tip * 10, rayY - 10)
        ..lineTo(end - tip * 10, rayY + 10)
        ..close(),
      Paint()..color = ray,
    );
    final dot = Offset(start, rayY);
    canvas.drawCircle(dot, 11, Paint()..color = filled ? ray : Colors.white);
    canvas.drawCircle(
      dot,
      11,
      Paint()
        ..color = ray
        ..style = PaintingStyle.stroke
        ..strokeWidth = 4,
    );
  }

  @override
  bool shouldRepaint(_RayPainter old) =>
      old.at != at ||
      old.filled != filled ||
      old.right != right ||
      old.line != line;
}

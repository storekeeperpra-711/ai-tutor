import 'package:flutter/material.dart';

import '../../checkers/rational.dart';
import '../../l10n/app_localizations.dart';
import '../sim_host.dart';
import 'common.dart';

/// A number line with ticks every `step`. The child drags the marker
/// (or uses the arrow buttons) to a number.
///
/// Params: `min` (0), `max` (2), `step` (0.25), `start` (min),
/// `labels`: `fraction` (default) or `decimal`. Reports `value`.
class NumberLine extends StatefulWidget {
  const NumberLine({super.key, required this.args});

  final SimArgs args;

  @override
  State<NumberLine> createState() => _NumberLineState();
}

class _NumberLineState extends State<NumberLine> {
  late final Rational _min = _rational('min', 0);
  late final Rational _step = _rational('step', 0.25);
  late final int _ticks = () {
    final max = _rational('max', 2);
    final n = ((max - _min) / _step).toDouble().floor();
    return n.clamp(1, 60);
  }();
  late int _at = ((_rational('start', _min.toDouble()) - _min) / _step)
      .toDouble()
      .round()
      .clamp(0, _ticks);
  late final bool _fractions = widget.args.params['labels'] != 'decimal';

  Rational _rational(String key, double fallback) {
    final value = doubleParam(widget.args, key, fallback);
    return Rational.tryParseDecimal('$value') ?? Rational.zero;
  }

  Rational _valueAt(int tick) => _min + _step * Rational(tick);

  String _label(Rational v) =>
      _fractions || v.isInteger ? v.toString() : v.toDouble().toString();

  void _moveTo(int tick) => setState(() => _at = tick.clamp(0, _ticks));

  int _tickAt(double dx, double width) {
    const pad = 24.0;
    final t = ((dx - pad) / (width - 2 * pad) * _ticks).round();
    return t.clamp(0, _ticks);
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final value = _valueAt(_at);
    return Directionality(
      textDirection: TextDirection.ltr,
      child: Column(
        children: [
          Expanded(
            child: LayoutBuilder(
              builder: (context, box) => GestureDetector(
                key: const Key('number-line'),
                onTapDown: (d) =>
                    _moveTo(_tickAt(d.localPosition.dx, box.maxWidth)),
                onHorizontalDragUpdate: (d) =>
                    _moveTo(_tickAt(d.localPosition.dx, box.maxWidth)),
                child: CustomPaint(
                  painter: _LinePainter(
                    ticks: _ticks,
                    at: _at,
                    label: (i) => _label(_valueAt(i)),
                    isWhole: (i) => _valueAt(i).isInteger,
                    color: Theme.of(context).colorScheme.onSurface,
                  ),
                  child: const SizedBox.expand(),
                ),
              ),
            ),
          ),
          Text(
            l10n.numberLineValue(_label(value)),
            key: const Key('number-line-value'),
            style: Theme.of(context).textTheme.titleLarge,
          ),
          SimCheckBar(
            extra: [
              IconButton.outlined(
                key: const Key('line-left'),
                onPressed: _at > 0 ? () => _moveTo(_at - 1) : null,
                icon: const Icon(Icons.arrow_back),
              ),
              IconButton.outlined(
                key: const Key('line-right'),
                onPressed: _at < _ticks ? () => _moveTo(_at + 1) : null,
                icon: const Icon(Icons.arrow_forward),
              ),
            ],
            onCheck: () =>
                reportResult(widget.args, {'value': value.toString()}),
          ),
        ],
      ),
    );
  }
}

class _LinePainter extends CustomPainter {
  _LinePainter({
    required this.ticks,
    required this.at,
    required this.label,
    required this.isWhole,
    required this.color,
  });

  final int ticks;
  final int at;
  final String Function(int tick) label;
  final bool Function(int tick) isWhole;
  final Color color;

  @override
  void paint(Canvas canvas, Size size) {
    const pad = 24.0;
    final y = size.height * 0.5;
    final paint = Paint()
      ..color = color
      ..strokeWidth = 3;
    canvas.drawLine(Offset(pad, y), Offset(size.width - pad, y), paint);
    final gap = (size.width - 2 * pad) / ticks;
    // Label every whole number, and fractions only when there is room.
    final labelFractions = gap > 36;
    for (var i = 0; i <= ticks; i++) {
      final x = pad + i * gap;
      final whole = isWhole(i);
      canvas.drawLine(
        Offset(x, y - (whole ? 14 : 8)),
        Offset(x, y + (whole ? 14 : 8)),
        paint..strokeWidth = whole ? 3 : 2,
      );
      if (whole || labelFractions) {
        final text = TextPainter(
          text: TextSpan(
            text: label(i),
            style: TextStyle(
              color: color,
              fontSize: whole ? 16 : 12,
              fontWeight: whole ? FontWeight.bold : null,
            ),
          ),
          textDirection: TextDirection.ltr,
        )..layout();
        text.paint(canvas, Offset(x - text.width / 2, y + 18));
      }
    }
    final mx = pad + at * gap;
    final marker = Path()
      ..moveTo(mx, y - 6)
      ..lineTo(mx - 14, y - 34)
      ..lineTo(mx + 14, y - 34)
      ..close();
    canvas.drawPath(marker, Paint()..color = const Color(0xFFFB8C00));
  }

  @override
  bool shouldRepaint(_LinePainter old) =>
      old.at != at || old.ticks != ticks || old.color != color;
}

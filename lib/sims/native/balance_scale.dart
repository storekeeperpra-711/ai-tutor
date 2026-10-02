import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../checkers/linear_equation_checker.dart';
import '../../l10n/app_localizations.dart';
import '../sim_host.dart';
import 'common.dart';

/// A balance scale for equations like `2x + 3 = 11`. x-boxes and 1-weights
/// sit on two pans. The child takes things away from one side or both,
/// or shares both sides into equal groups. Taking from only one side
/// tips the scale (misconception: "do it to one side only").
///
/// Params: `equation` (whole numbers, no negatives). Reports `x` once
/// one side is a single x-box and the other only weights, plus
/// `balanced` and `moves`.
class BalanceScale extends StatefulWidget {
  const BalanceScale({super.key, required this.args});

  final SimArgs args;

  @override
  State<BalanceScale> createState() => _BalanceScaleState();
}

/// What is on the pans: x-boxes and 1-weights on each side.
@immutable
class Pans {
  const Pans(this.leftX, this.leftOnes, this.rightX, this.rightOnes);

  final int leftX;
  final int leftOnes;
  final int rightX;
  final int rightOnes;

  /// Reads `ax + b = cx + d` with whole numbers from 0 up; null otherwise.
  static Pans? parse(String equation) {
    try {
      final e = parseLinearEquation(equation);
      final values = [e.left.a, e.left.b, e.right.a, e.right.b];
      if (values.any((v) => !v.isInteger || v.numerator < 0)) return null;
      return Pans(
        values[0].numerator,
        values[1].numerator,
        values[2].numerator,
        values[3].numerator,
      );
    } on FormatException {
      return null;
    }
  }

  double leftWeight(double x) => leftX * x + leftOnes;
  double rightWeight(double x) => rightX * x + rightOnes;

  /// The value the scale shows for x, once x is on its own.
  int? get isolatedX {
    if (leftX == 1 && leftOnes == 0 && rightX == 0) return rightOnes;
    if (rightX == 1 && rightOnes == 0 && leftX == 0) return leftOnes;
    return null;
  }

  /// Both sides can be shared into this many equal groups (the number of
  /// x-boxes), so one group of each is kept.
  int? get shareBy {
    final n = leftX > 0 && rightX == 0
        ? leftX
        : rightX > 0 && leftX == 0
        ? rightX
        : 0;
    if (n < 2) return null;
    return [leftX, leftOnes, rightX, rightOnes].every((v) => v % n == 0)
        ? n
        : null;
  }

  Pans divide(int n) =>
      Pans(leftX ~/ n, leftOnes ~/ n, rightX ~/ n, rightOnes ~/ n);
}

class _BalanceScaleState extends State<BalanceScale> {
  late final Pans? _start = Pans.parse(
    widget.args.params['equation'] as String? ?? '',
  );
  late final List<Pans> _history = [if (_start != null) _start];

  /// The real value of x, for how far the scale tips.
  late final double _x = _start == null
      ? 0
      : switch (parseLinearEquation(widget.args.params['equation'] as String)
            .solution) {
          OneSolution(:final value) => value.toDouble(),
          _ => 0,
        };

  @override
  void initState() {
    super.initState();
    if (_start == null) {
      WidgetsBinding.instance.addPostFrameCallback(
        (_) => widget.args.onEvent(
          const SimEvent('error', {'message': 'bad equation'}),
        ),
      );
    }
  }

  Pans get _pans => _history.last;
  bool get _balanced =>
      (_pans.leftWeight(_x) - _pans.rightWeight(_x)).abs() < 1e-9;

  void _apply(Pans next) => setState(() => _history.add(next));

  @override
  Widget build(BuildContext context) {
    if (_start == null) return const SizedBox.shrink();
    final l10n = AppLocalizations.of(context);
    final p = _pans;
    final share = _balanced ? p.shareBy : null;

    Widget side(String id, String title, {required bool left}) {
      final xs = left ? p.leftX : p.rightX;
      final ones = left ? p.leftOnes : p.rightOnes;
      Pans take({int x = 0, int one = 0}) => left
          ? Pans(p.leftX - x, p.leftOnes - one, p.rightX, p.rightOnes)
          : Pans(p.leftX, p.leftOnes, p.rightX - x, p.rightOnes - one);
      return Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Text(title, style: Theme.of(context).textTheme.labelLarge),
          Wrap(
            alignment: WrapAlignment.center,
            spacing: 4,
            children: [
              OutlinedButton(
                key: Key('$id-one'),
                onPressed: ones > 0 ? () => _apply(take(one: 1)) : null,
                child: Text(l10n.scaleTakeOne),
              ),
              OutlinedButton(
                key: Key('$id-x'),
                onPressed: xs > 0 ? () => _apply(take(x: 1)) : null,
                child: Text(l10n.scaleTakeX),
              ),
            ],
          ),
        ],
      );
    }

    return Column(
      children: [
        Expanded(
          child: Padding(
            padding: const EdgeInsets.all(8),
            child: Semantics(
              label: _balanced ? l10n.scaleBalanced : l10n.scaleTipped,
              child: TweenAnimationBuilder<double>(
                tween: Tween(end: _tilt(p)),
                duration: MediaQuery.disableAnimationsOf(context)
                    ? Duration.zero
                    : const Duration(milliseconds: 400),
                curve: Curves.easeOutBack,
                builder: (context, tilt, _) => CustomPaint(
                  key: const Key('scale'),
                  painter: _ScalePainter(
                    pans: p,
                    tilt: tilt,
                    color: Theme.of(context).colorScheme.onSurface,
                  ),
                  child: const SizedBox.expand(),
                ),
              ),
            ),
          ),
        ),
        Text(
          _balanced ? l10n.scaleBalanced : l10n.scaleTipped,
          key: const Key('scale-state'),
          style: TextStyle(
            color: _balanced
                ? const Color(0xFF2E7D32)
                : const Color(0xFFE65100),
            fontWeight: FontWeight.bold,
          ),
        ),
        Directionality(
          textDirection: TextDirection.ltr,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Expanded(child: side('left', l10n.scaleLeft, left: true)),
              Expanded(child: side('right', l10n.scaleRight, left: false)),
            ],
          ),
        ),
        SimCheckBar(
          onUndo: _history.length > 1
              ? () => setState(_history.removeLast)
              : null,
          extra: [
            if (share != null)
              OutlinedButton.icon(
                key: const Key('scale-share'),
                onPressed: () => _apply(p.divide(share)),
                icon: const Icon(Icons.call_split),
                label: Text(l10n.scaleShare(share)),
              ),
          ],
          onCheck: () => reportResult(widget.args, {
            'x': ?p.isolatedX,
            'balanced': _balanced,
            'moves': _history.length - 1,
          }),
        ),
      ],
    );
  }

  /// Radians; positive tips the right side down.
  double _tilt(Pans p) {
    final diff = p.rightWeight(_x) - p.leftWeight(_x);
    return (diff.sign * math.min(diff.abs() / 4, 1)) * 0.25;
  }
}

class _ScalePainter extends CustomPainter {
  _ScalePainter({required this.pans, required this.tilt, required this.color});

  final Pans pans;
  final double tilt;
  final Color color;

  static const _xColor = Color(0xFF00897B);
  static const _oneColor = Color(0xFFFB8C00);

  @override
  void paint(Canvas canvas, Size size) {
    final line = Paint()
      ..color = color
      ..strokeWidth = 4
      ..strokeCap = StrokeCap.round;
    final pivot = Offset(size.width / 2, size.height * 0.35);
    final base = Offset(size.width / 2, size.height - 4);
    canvas
      ..drawLine(pivot, base, line)
      ..drawLine(base.translate(-40, 0), base.translate(40, 0), line);

    final half = size.width * 0.4;
    final dx = math.cos(tilt) * half;
    final dy = math.sin(tilt) * half;
    final leftEnd = pivot.translate(-dx, -dy);
    final rightEnd = pivot.translate(dx, dy);
    canvas
      ..drawLine(leftEnd, rightEnd, line)
      ..drawCircle(pivot, 6, Paint()..color = color);

    final panWidth = size.width * 0.36;
    final panDrop = size.height * 0.12;
    _pan(canvas, leftEnd, panWidth, panDrop, pans.leftX, pans.leftOnes, line);
    _pan(
      canvas,
      rightEnd,
      panWidth,
      panDrop,
      pans.rightX,
      pans.rightOnes,
      line,
    );
  }

  void _pan(
    Canvas canvas,
    Offset hook,
    double width,
    double drop,
    int xs,
    int ones,
    Paint line,
  ) {
    final thin = Paint()
      ..color = line.color
      ..strokeWidth = 2;
    final tray = hook.translate(0, drop);
    canvas
      ..drawLine(hook, tray.translate(-width / 2, 0), thin)
      ..drawLine(hook, tray.translate(width / 2, 0), thin)
      ..drawLine(
        tray.translate(-width / 2, 0),
        tray.translate(width / 2, 0),
        line,
      );

    // Items stack upwards from the tray, several to a row.
    const item = 22.0;
    final perRow = math.max(1, (width / (item + 4)).floor());
    final items = [
      for (var i = 0; i < xs; i++) true,
      for (var i = 0; i < ones; i++) false,
    ];
    for (var i = 0; i < items.length; i++) {
      final row = i ~/ perRow;
      final col = i % perRow;
      final inRow = math.min(perRow, items.length - row * perRow);
      final left = tray.dx - inRow * (item + 4) / 2 + col * (item + 4);
      final rect = Rect.fromLTWH(
        left,
        tray.dy - (row + 1) * (item + 4),
        item,
        item,
      );
      if (items[i]) {
        canvas.drawRRect(
          RRect.fromRectAndRadius(rect, const Radius.circular(4)),
          Paint()..color = _xColor,
        );
        _label(canvas, rect, 'x');
      } else {
        canvas.drawOval(rect, Paint()..color = _oneColor);
        _label(canvas, rect, '1');
      }
    }
  }

  void _label(Canvas canvas, Rect rect, String text) {
    final painter = TextPainter(
      text: TextSpan(
        text: text,
        style: const TextStyle(
          color: Colors.white,
          fontWeight: FontWeight.bold,
          fontSize: 13,
        ),
      ),
      textDirection: TextDirection.ltr,
    )..layout();
    painter.paint(
      canvas,
      rect.center - Offset(painter.width / 2, painter.height / 2),
    );
  }

  @override
  bool shouldRepaint(_ScalePainter old) =>
      old.pans != pans || old.tilt != tilt || old.color != color;
}

import 'package:flutter/material.dart';

import '../../l10n/app_localizations.dart';
import '../sim_host.dart';
import 'common.dart';

/// Fraction bars: `wholes` bars (rotis, ribbons). The child chooses how
/// many pieces to cut each one into, then taps pieces to count them.
///
/// Params: `wholes` (default 2), `start_cut` (default 1), `max_cut`
/// (default 12). Reports `pieces` (pieces tapped), `cut` and `total`.
class FractionBars extends StatefulWidget {
  const FractionBars({super.key, required this.args});

  final SimArgs args;

  @override
  State<FractionBars> createState() => _FractionBarsState();
}

class _FractionBarsState extends State<FractionBars> {
  late final int _wholes = intParam(widget.args, 'wholes', 2, min: 1, max: 6);
  late final int _maxCut = intParam(
    widget.args,
    'max_cut',
    12,
    min: 2,
    max: 12,
  );
  late int _cut = intParam(widget.args, 'start_cut', 1, min: 1, max: _maxCut);
  final _chosen = <(int, int)>{};

  void _setCut(int cut) => setState(() {
    _cut = cut;
    _chosen.clear();
  });

  void _toggle(int bar, int piece) => setState(() {
    if (!_chosen.remove((bar, piece))) _chosen.add((bar, piece));
  });

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final colors = Theme.of(context).colorScheme;
    return Column(
      children: [
        Expanded(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(12),
            child: Column(
              children: [
                for (var bar = 0; bar < _wholes; bar++)
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 6),
                    child: SizedBox(
                      height: 52,
                      // Bars always run left to right, like a number line.
                      child: Directionality(
                        textDirection: TextDirection.ltr,
                        child: Row(
                          children: [
                            for (var piece = 0; piece < _cut; piece++)
                              Expanded(
                                child: GestureDetector(
                                  key: Key('piece-$bar-$piece'),
                                  onTap: () => _toggle(bar, piece),
                                  child: AnimatedContainer(
                                    duration: const Duration(milliseconds: 150),
                                    margin: const EdgeInsets.all(1.5),
                                    decoration: BoxDecoration(
                                      color: _chosen.contains((bar, piece))
                                          ? const Color(0xFFFFB74D)
                                          : const Color(0xFFFFE0B2),
                                      border: Border.all(
                                        color: const Color(0xFF8D6E63),
                                        width: 1.5,
                                      ),
                                      borderRadius: BorderRadius.circular(6),
                                    ),
                                    alignment: Alignment.center,
                                    child: _cut <= 8
                                        ? Text(
                                            '1/$_cut',
                                            style: TextStyle(
                                              fontSize: 12,
                                              color: colors.onSurface,
                                            ),
                                          )
                                        : null,
                                  ),
                                ),
                              ),
                          ],
                        ),
                      ),
                    ),
                  ),
                const SizedBox(height: 8),
                Text(
                  l10n.fractionBarsChosen(_chosen.length),
                  key: const Key('pieces-chosen'),
                  style: Theme.of(context).textTheme.titleMedium,
                ),
              ],
            ),
          ),
        ),
        SimStepper(
          id: 'cut',
          label: l10n.fractionBarsCut,
          value: '$_cut',
          onMinus: _cut > 1 ? () => _setCut(_cut - 1) : null,
          onPlus: _cut < _maxCut ? () => _setCut(_cut + 1) : null,
        ),
        SimCheckBar(
          onCheck: () => reportResult(widget.args, {
            'pieces': _chosen.length,
            'cut': _cut,
            'total': _cut * _wholes,
          }),
        ),
      ],
    );
  }
}

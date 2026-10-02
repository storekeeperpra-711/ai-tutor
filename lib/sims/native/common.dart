import 'package:flutter/material.dart';

import '../../l10n/app_localizations.dart';
import '../sim_host.dart';

/// The big Check button under every native interactive. It reports the
/// interactive's current state as the result.
class SimCheckBar extends StatelessWidget {
  const SimCheckBar({
    super.key,
    required this.onCheck,
    this.onUndo,
    this.extra = const [],
  });

  final VoidCallback onCheck;
  final VoidCallback? onUndo;
  final List<Widget> extra;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return Padding(
      padding: const EdgeInsets.all(8),
      child: Wrap(
        alignment: WrapAlignment.center,
        spacing: 8,
        runSpacing: 8,
        children: [
          ...extra,
          if (onUndo != null)
            OutlinedButton.icon(
              key: const Key('sim-undo'),
              onPressed: onUndo,
              icon: const Icon(Icons.undo),
              label: Text(l10n.simUndo),
            ),
          FilledButton.tonalIcon(
            key: const Key('sim-check'),
            onPressed: onCheck,
            icon: const Icon(Icons.check),
            label: Text(l10n.checkButton),
          ),
        ],
      ),
    );
  }
}

/// A − value + control with big touch targets.
class SimStepper extends StatelessWidget {
  const SimStepper({
    super.key,
    required this.id,
    required this.label,
    required this.value,
    required this.onMinus,
    required this.onPlus,
  });

  /// Keys are `$id-minus` and `$id-plus`.
  final String id;
  final String label;
  final String value;
  final VoidCallback? onMinus;
  final VoidCallback? onPlus;

  @override
  Widget build(BuildContext context) {
    final textTheme = Theme.of(context).textTheme;
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(label, style: textTheme.labelLarge, textAlign: TextAlign.center),
        Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            IconButton.outlined(
              key: Key('$id-minus'),
              iconSize: 28,
              onPressed: onMinus,
              icon: const Icon(Icons.remove),
            ),
            SizedBox(
              width: 56,
              child: Text(
                value,
                key: Key('$id-value'),
                textAlign: TextAlign.center,
                textDirection: TextDirection.ltr,
                style: textTheme.headlineSmall,
              ),
            ),
            IconButton.outlined(
              key: Key('$id-plus'),
              iconSize: 28,
              onPressed: onPlus,
              icon: const Icon(Icons.add),
            ),
          ],
        ),
      ],
    );
  }
}

/// Reports a result to the step.
void reportResult(SimArgs args, Map<String, dynamic> data) =>
    args.onEvent(SimEvent('result', data));

/// Reads a whole-number param, with a default and limits.
int intParam(SimArgs args, String key, int fallback, {int min = 0, int? max}) {
  final v = args.params[key];
  final n = v is num ? v.round() : fallback;
  return n.clamp(min, max ?? 1 << 30);
}

double doubleParam(SimArgs args, String key, double fallback) {
  final v = args.params[key];
  return v is num ? v.toDouble() : fallback;
}

import 'package:flutter/material.dart';

import '../../checkers/chem_equation_checker.dart';
import '../../l10n/app_localizations.dart';
import '../sim_host.dart';
import 'common.dart';

/// Balance a chemical equation by changing only the big numbers in front
/// (coefficients), never the small ones (subscripts). A table shows the
/// atoms of each element on both sides.
///
/// Params: `equation`, e.g. `H2 + O2 -> H2O` (coefficients in it are the
/// starting values). Reports `equation` with the child's coefficients
/// and `balanced`.
class AtomBalancer extends StatefulWidget {
  const AtomBalancer({super.key, required this.args});

  final SimArgs args;

  @override
  State<AtomBalancer> createState() => _AtomBalancerState();
}

class _AtomBalancerState extends State<AtomBalancer> {
  static const _max = 9;

  ChemEquation? _equation;
  late final List<int> _coefficients;

  @override
  void initState() {
    super.initState();
    try {
      _equation = parseEquation(
        widget.args.params['equation'] as String? ?? '',
      );
    } on Object {
      _equation = null;
    }
    final e = _equation;
    _coefficients = e == null
        ? []
        : [
            for (final t in [...e.left, ...e.right]) t.coefficient,
          ];
    if (e == null) {
      WidgetsBinding.instance.addPostFrameCallback(
        (_) => widget.args.onEvent(
          const SimEvent('error', {'message': 'bad equation'}),
        ),
      );
    }
  }

  List<Term> _side(List<Term> terms, int offset) => [
    for (var i = 0; i < terms.length; i++)
      Term(_coefficients[offset + i], terms[i].formula, terms[i].atoms),
  ];

  String _write(List<Term> left, List<Term> right) {
    String side(List<Term> terms) => terms
        .map((t) => '${t.coefficient == 1 ? '' : t.coefficient}${t.formula}')
        .join(' + ');
    return '${side(left)} -> ${side(right)}';
  }

  @override
  Widget build(BuildContext context) {
    final e = _equation;
    if (e == null) return const SizedBox.shrink();
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final left = _side(e.left, 0);
    final right = _side(e.right, e.left.length);
    final leftCount = ChemEquation.count(left);
    final rightCount = ChemEquation.count(right);
    final elements = {...leftCount.keys, ...rightCount.keys}.toList();
    final balanced = elements.every((el) => leftCount[el] == rightCount[el]);

    Widget term(int index, Term t) => Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        IconButton.outlined(
          key: Key('coef-$index-plus'),
          onPressed: _coefficients[index] < _max
              ? () => setState(() => _coefficients[index]++)
              : null,
          icon: const Icon(Icons.add),
        ),
        Text.rich(
          TextSpan(
            children: [
              TextSpan(
                text: '${t.coefficient}',
                style: textTheme.headlineSmall?.copyWith(
                  color: const Color(0xFF1565C0),
                  fontWeight: FontWeight.bold,
                ),
              ),
              TextSpan(
                text: subscriptDigits(t.formula),
                style: textTheme.headlineSmall,
              ),
            ],
          ),
          key: Key('term-$index'),
        ),
        IconButton.outlined(
          key: Key('coef-$index-minus'),
          onPressed: _coefficients[index] > 1
              ? () => setState(() => _coefficients[index]--)
              : null,
          icon: const Icon(Icons.remove),
        ),
      ],
    );

    var index = 0;
    final terms = <Widget>[];
    for (final (i, t) in left.indexed) {
      if (i > 0) terms.add(const _Sign('+'));
      terms.add(term(index++, t));
    }
    terms.add(const _Sign('→'));
    for (final (i, t) in right.indexed) {
      if (i > 0) terms.add(const _Sign('+'));
      terms.add(term(index++, t));
    }

    return Directionality(
      // Chemistry is written left to right in Urdu too.
      textDirection: TextDirection.ltr,
      child: Column(
        children: [
          Expanded(
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(8),
              child: Column(
                children: [
                  Wrap(
                    alignment: WrapAlignment.center,
                    crossAxisAlignment: WrapCrossAlignment.center,
                    children: terms,
                  ),
                  const SizedBox(height: 12),
                  Table(
                    key: const Key('atom-table'),
                    border: TableBorder.all(
                      color: Theme.of(context).dividerColor,
                    ),
                    defaultVerticalAlignment: TableCellVerticalAlignment.middle,
                    children: [
                      TableRow(
                        children: [
                          const SizedBox.shrink(),
                          _Cell(l10n.atomsLeft, bold: true),
                          _Cell(l10n.atomsRight, bold: true),
                          const SizedBox.shrink(),
                        ],
                      ),
                      for (final el in elements)
                        TableRow(
                          children: [
                            _Cell(el, bold: true),
                            _Cell('${leftCount[el] ?? 0}'),
                            _Cell('${rightCount[el] ?? 0}'),
                            Icon(
                              leftCount[el] == rightCount[el]
                                  ? Icons.check_circle
                                  : Icons.cancel,
                              color: leftCount[el] == rightCount[el]
                                  ? const Color(0xFF2E7D32)
                                  : const Color(0xFFE65100),
                            ),
                          ],
                        ),
                    ],
                  ),
                  if (balanced)
                    Padding(
                      padding: const EdgeInsets.only(top: 8),
                      child: Text(
                        l10n.atomsBalanced,
                        key: const Key('atoms-balanced'),
                        style: textTheme.titleMedium?.copyWith(
                          color: const Color(0xFF2E7D32),
                        ),
                      ),
                    ),
                ],
              ),
            ),
          ),
          SimCheckBar(
            onCheck: () => reportResult(widget.args, {
              'equation': _write(left, right),
              'balanced': balanced,
            }),
          ),
        ],
      ),
    );
  }
}

/// H2O -> H₂O for display.
String subscriptDigits(String formula) => formula.replaceAllMapped(
  RegExp('[0-9]'),
  (m) => '₀₁₂₃₄₅₆₇₈₉'[int.parse(m[0]!)],
);

class _Sign extends StatelessWidget {
  const _Sign(this.text);
  final String text;

  @override
  Widget build(BuildContext context) => Padding(
    padding: const EdgeInsets.symmetric(horizontal: 6),
    child: Text(text, style: Theme.of(context).textTheme.headlineSmall),
  );
}

class _Cell extends StatelessWidget {
  const _Cell(this.text, {this.bold = false});
  final String text;
  final bool bold;

  @override
  Widget build(BuildContext context) => Padding(
    padding: const EdgeInsets.all(6),
    child: Text(
      text,
      textAlign: TextAlign.center,
      style: TextStyle(fontWeight: bold ? FontWeight.bold : null),
    ),
  );
}

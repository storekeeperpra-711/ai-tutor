/// Checks a balanced chemical equation typed by a student, such as
/// `2H2 + O2 -> 2H2O`, and names the exact mistake when it is wrong.
library;

import 'normalize.dart';
import 'rational.dart';

/// All element symbols. Case matters: Co is cobalt, CO is carbon monoxide.
const elementSymbols = {
  'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', //
  'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe',
  'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr',
  'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
  'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm',
  'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W',
  'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
  'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf',
  'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
  'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og',
};

/// One substance with its coefficient, e.g. `2H2O`.
class Term {
  const Term(this.coefficient, this.formula, this.atoms);

  final int coefficient;

  /// As written, without the coefficient or state symbol, e.g. `Ca(OH)2`.
  final String formula;

  /// Atoms in one unit of the formula, e.g. {Ca: 1, O: 2, H: 2}.
  final Map<String, int> atoms;

  /// The same key for the same atoms however the formula is written,
  /// so `Ca(OH)2` and `CaO2H2` match.
  String get key =>
      (atoms.keys.toList()..sort()).map((e) => '$e${atoms[e]}').join();
}

class ChemEquation {
  const ChemEquation(this.left, this.right);

  final List<Term> left;
  final List<Term> right;

  /// Total atoms of each element on one side.
  static Map<String, int> count(List<Term> side) {
    final total = <String, int>{};
    for (final term in side) {
      term.atoms.forEach((element, n) {
        total[element] = (total[element] ?? 0) + n * term.coefficient;
      });
    }
    return total;
  }
}

/// Why an equation could not be read, or what is wrong with it.
enum ChemMistake {
  unreadable,
  unknownElement,
  wrongSubstances,
  changedSubscript,
  unbalanced,
  notLowestCoefficients,
}

class ChemResult {
  const ChemResult.correct() : mistake = null, details = const {};
  const ChemResult(this.mistake, [this.details = const {}]);

  /// null when the equation is correct.
  final ChemMistake? mistake;

  /// Facts for the feedback text, depending on the mistake:
  /// - unknownElement: `symbol`
  /// - changedSubscript: `student` (formula written), `expected`
  /// - unbalanced: `element`, `left`, `right` (atom counts)
  /// - notLowestCoefficients: `divisor`
  final Map<String, Object> details;

  bool get isCorrect => mistake == null;
}

class ChemParseException implements Exception {
  const ChemParseException(this.mistake, [this.details = const {}]);
  final ChemMistake mistake;
  final Map<String, Object> details;
}

/// Reads an equation. Accepts `->`, `→`, `=` or `=>` between the sides,
/// subscripts as `H2O` or `H₂O`, brackets `Ca(OH)2` and state symbols
/// `(aq) (s) (l) (g)`. Throws [ChemParseException].
ChemEquation parseEquation(String input) {
  var text = normalizeInput(input)
      .replaceAll('=>', '->')
      .replaceAll(RegExp(r'\((aq|s|l|g)\)'), '');
  if (!text.contains('->')) text = text.replaceAll('=', '->');
  final sides = text.split('->');
  if (sides.length != 2) throw const ChemParseException(ChemMistake.unreadable);
  return ChemEquation(_parseSide(sides[0]), _parseSide(sides[1]));
}

List<Term> _parseSide(String side) {
  final parts = side.split('+').map((p) => p.trim()).toList();
  if (parts.any((p) => p.isEmpty)) {
    throw const ChemParseException(ChemMistake.unreadable);
  }
  return parts.map(_parseTerm).toList();
}

Term _parseTerm(String text) {
  final match = RegExp(r'^(\d*)\s*(.+)$').firstMatch(text)!;
  final coefficient = match[1]!.isEmpty ? 1 : int.parse(match[1]!);
  if (coefficient == 0) throw const ChemParseException(ChemMistake.unreadable);
  final formula = match[2]!.replaceAll(' ', '');
  final parser = _FormulaParser(formula);
  final atoms = parser.parseGroup();
  if (!parser.done || atoms.isEmpty) {
    throw const ChemParseException(ChemMistake.unreadable);
  }
  return Term(coefficient, formula, atoms);
}

/// Reads formulas like `Ca(OH)2` or `Al2(SO4)3` into atom counts.
class _FormulaParser {
  _FormulaParser(this.text);

  final String text;
  var _pos = 0;

  bool get done => _pos == text.length;

  Map<String, int> parseGroup() {
    final atoms = <String, int>{};
    while (_pos < text.length) {
      final c = text[_pos];
      if (c == '(' || c == '[') {
        _pos++;
        final inner = parseGroup();
        if (_pos >= text.length || (text[_pos] != ')' && text[_pos] != ']')) {
          throw const ChemParseException(ChemMistake.unreadable);
        }
        _pos++;
        final n = _readCount();
        inner.forEach((e, k) => atoms[e] = (atoms[e] ?? 0) + k * n);
      } else if (c == ')' || c == ']') {
        return atoms;
      } else if (_isUpper(c)) {
        var symbol = c;
        _pos++;
        while (_pos < text.length && _isLower(text[_pos])) {
          symbol += text[_pos++];
        }
        if (!elementSymbols.contains(symbol)) {
          throw ChemParseException(ChemMistake.unknownElement, {
            'symbol': symbol,
          });
        }
        final n = _readCount();
        atoms[symbol] = (atoms[symbol] ?? 0) + n;
      } else if (_isLower(c)) {
        // A formula never starts a symbol with a small letter (e.g. "o2").
        var word = '';
        while (_pos < text.length && RegExp('[A-Za-z]').hasMatch(text[_pos])) {
          word += text[_pos++];
        }
        throw ChemParseException(ChemMistake.unknownElement, {'symbol': word});
      } else {
        throw const ChemParseException(ChemMistake.unreadable);
      }
    }
    return atoms;
  }

  int _readCount() {
    final start = _pos;
    while (_pos < text.length && _isDigit(text[_pos])) {
      _pos++;
    }
    if (start == _pos) return 1;
    final n = int.parse(text.substring(start, _pos));
    if (n == 0) throw const ChemParseException(ChemMistake.unreadable);
    return n;
  }

  static bool _isUpper(String c) =>
      c.compareTo('A') >= 0 && c.compareTo('Z') <= 0;
  static bool _isLower(String c) =>
      c.compareTo('a') >= 0 && c.compareTo('z') <= 0;
  static bool _isDigit(String c) =>
      c.compareTo('0') >= 0 && c.compareTo('9') <= 0;
}

/// Checks [input] against the correct balanced equation [expected].
/// The order of substances on each side doesn't matter.
ChemResult checkChemEquation(String input, String expected) {
  final ChemEquation answer;
  try {
    answer = parseEquation(input);
  } on ChemParseException catch (e) {
    return ChemResult(e.mistake, e.details);
  }
  final target = parseEquation(expected);

  // 1. Same substances on each side?
  for (final (studentSide, targetSide) in [
    (answer.left, target.left),
    (answer.right, target.right),
  ]) {
    final studentKeys = studentSide.map((t) => t.key).toSet();
    final targetKeys = targetSide.map((t) => t.key).toSet();
    if (studentKeys.length == targetKeys.length &&
        studentKeys.containsAll(targetKeys)) {
      continue;
    }
    // A formula with the right elements but different small numbers means
    // the student changed a subscript to balance it.
    for (final written in studentSide.where(
      (t) => !targetKeys.contains(t.key),
    )) {
      final changed = targetSide.where(
        (t) =>
            !studentKeys.contains(t.key) &&
            t.atoms.keys.toSet().containsAll(written.atoms.keys) &&
            written.atoms.keys.toSet().containsAll(t.atoms.keys),
      );
      if (changed.isNotEmpty) {
        return ChemResult(ChemMistake.changedSubscript, {
          'student': written.formula,
          'expected': changed.first.formula,
        });
      }
    }
    return const ChemResult(ChemMistake.wrongSubstances);
  }

  // 2. Same number of each atom on both sides?
  final left = ChemEquation.count(answer.left);
  final right = ChemEquation.count(answer.right);
  final elements = {...left.keys, ...right.keys}.toList()..sort();
  for (final element in elements) {
    if (left[element] != right[element]) {
      return ChemResult(ChemMistake.unbalanced, {
        'element': element,
        'left': left[element] ?? 0,
        'right': right[element] ?? 0,
      });
    }
  }

  // 3. Smallest whole-number coefficients?
  final divisor = gcdOf([
    ...answer.left.map((t) => t.coefficient),
    ...answer.right.map((t) => t.coefficient),
  ]);
  if (divisor > 1) {
    return ChemResult(ChemMistake.notLowestCoefficients, {'divisor': divisor});
  }
  return const ChemResult.correct();
}

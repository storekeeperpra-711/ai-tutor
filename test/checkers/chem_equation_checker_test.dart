import 'package:ai_tutor/checkers/chem_equation_checker.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  const water = '2H2 + O2 -> 2H2O';

  group('parsing', () {
    test('reads brackets, subscripts and state symbols', () {
      final eq = parseEquation('Ca(OH)₂(aq) + 2HCl(aq) → CaCl2(aq) + 2H2O(l)');
      expect(eq.left.first.atoms, {'Ca': 1, 'O': 2, 'H': 2});
      expect(eq.left.last.coefficient, 2);
      expect(ChemEquation.count(eq.right), {'Ca': 1, 'Cl': 2, 'H': 4, 'O': 2});
    });

    test('reads nested groups', () {
      final eq = parseEquation('Al2(SO4)3 = Al2(SO4)3');
      expect(eq.left.first.atoms, {'Al': 2, 'S': 3, 'O': 12});
    });
  });

  group('checkChemEquation', () {
    test('accepts a correct equation in any order and arrow style', () {
      for (final answer in [
        '2H2 + O2 -> 2H2O',
        'O2 + 2H2 → 2H₂O',
        '2 H2 + O2 = 2 H2O',
        '2H2(g) + O2(g) => 2H2O(l)',
        '۲H2 + O2 -> ۲H2O',
      ]) {
        expect(
          checkChemEquation(answer, water).isCorrect,
          isTrue,
          reason: answer,
        );
      }
    });

    test('names the unbalanced element and the counts', () {
      final result = checkChemEquation('H2 + O2 -> H2O', water);
      expect(result.mistake, ChemMistake.unbalanced);
      expect(result.details, {'element': 'O', 'left': 2, 'right': 1});
    });

    test('detects a changed subscript', () {
      final result = checkChemEquation('H2 + O2 -> H2O2', water);
      expect(result.mistake, ChemMistake.changedSubscript);
      expect(result.details, {'student': 'H2O2', 'expected': 'H2O'});
    });

    test('detects unknown element symbols, including wrong capitals', () {
      expect(
        checkChemEquation('2H2 + o2 -> 2H2O', water).details['symbol'],
        'o',
      );
      final nacl = checkChemEquation(
        '2Na + Cl2 -> 2Nacl',
        '2Na + Cl2 -> 2NaCl',
      );
      expect(nacl.mistake, ChemMistake.unknownElement);
      expect(nacl.details['symbol'], 'Nacl');
      expect(
        checkChemEquation('2H2 + O2 -> 2Xy2O', water).details['symbol'],
        'Xy',
      );
    });

    test('detects wrong or missing substances', () {
      expect(
        checkChemEquation('2H2 + O2 -> 2H2O + CO2', water).mistake,
        ChemMistake.wrongSubstances,
      );
      expect(
        checkChemEquation('2H2 -> 2H2O', water).mistake,
        ChemMistake.wrongSubstances,
      );
    });

    test('detects coefficients that are not the smallest', () {
      final result = checkChemEquation('4H2 + 2O2 -> 4H2O', water);
      expect(result.mistake, ChemMistake.notLowestCoefficients);
      expect(result.details['divisor'], 2);
    });

    test('reports unreadable input', () {
      for (final answer in [
        '',
        'water',
        '2H2 + O2',
        'H2 + -> H2O',
        '0H2 + O2 -> H2O',
        'H2(O -> H2O',
      ]) {
        expect(
          checkChemEquation(answer, water).mistake,
          ChemMistake.unreadable,
          reason: answer,
        );
      }
    });

    test('works for a harder equation', () {
      const expected = 'C3H8 + 5O2 -> 3CO2 + 4H2O';
      expect(
        checkChemEquation('C3H8 + 5O2 → 3CO2 + 4H2O', expected).isCorrect,
        isTrue,
      );
      final result = checkChemEquation('C3H8 + O2 -> 3CO2 + 4H2O', expected);
      expect(result.details, {'element': 'O', 'left': 2, 'right': 10});
    });
  });
}

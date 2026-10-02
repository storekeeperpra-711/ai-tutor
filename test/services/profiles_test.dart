import 'package:ai_tutor/app/theme/age_tier.dart';
import 'package:ai_tutor/services/profiles.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('a PIN is stored only as a salted hash', () {
    final stored = hashPin('1234');
    expect(stored, isNot(contains('1234')));
    expect(checkPin('1234', stored), isTrue);
    expect(checkPin('4321', stored), isFalse);
    // The same PIN for two children gives different hashes.
    expect(hashPin('1234'), isNot(stored));
  });

  test('new ids are random and Firestore-safe', () {
    final ids = List.generate(100, (_) => newId());
    expect(ids.toSet(), hasLength(100));
    expect(ids.every((id) => RegExp(r'^[A-Za-z0-9]{20}$').hasMatch(id)), true);
  });

  test('class decides the age tier', () {
    expect(tierForGrade(-1), AgeTier.early);
    expect(tierForGrade(2), AgeTier.early);
    expect(tierForGrade(5), AgeTier.primary);
    expect(tierForGrade(6), AgeTier.middle);
    expect(tierForGrade(10), AgeTier.older);
  });
}

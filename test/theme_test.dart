import 'package:ai_tutor/app/theme/age_tier.dart';
import 'package:ai_tutor/app/theme/app_theme.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('every age tier has a style', () {
    for (final tier in AgeTier.values) {
      expect(tierStyles[tier], isNotNull, reason: tier.name);
    }
  });

  test('younger tiers get bigger buttons and text', () {
    final early = buildTheme(AgeTier.early, const Locale('en'));
    final older = buildTheme(AgeTier.older, const Locale('en'));

    double buttonHeight(ThemeData t) =>
        t.filledButtonTheme.style!.minimumSize!.resolve({})!.height;

    expect(buttonHeight(early), greaterThan(buttonHeight(older)));
    expect(
      early.textTheme.bodyLarge!.fontSize,
      greaterThan(older.textTheme.bodyLarge!.fontSize!),
    );
  });

  test('Urdu uses Nastaliq with a taller line height', () {
    final urdu = buildTheme(AgeTier.older, const Locale('ur'));
    final english = buildTheme(AgeTier.older, const Locale('en'));

    expect(urdu.textTheme.bodyLarge!.fontFamily, urduFontFamily);
    expect(urdu.textTheme.bodyLarge!.height, urduLineHeight);
    expect(english.textTheme.bodyLarge!.fontFamily, isNot(urduFontFamily));
  });

  test('each tier has its own main colour', () {
    final themes = AgeTier.values
        .map((t) => buildTheme(t, const Locale('en')).colorScheme.primary)
        .toSet();
    expect(themes.length, AgeTier.values.length);
  });
}

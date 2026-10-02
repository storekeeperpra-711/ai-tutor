import 'package:flutter/material.dart';

import 'age_tier.dart';

/// Font family name registered in pubspec.yaml.
const urduFontFamily = 'NotoNastaliqUrdu';

/// Nastaliq letters reach far above and below the line, so Urdu text
/// needs extra line height or it gets clipped.
const urduLineHeight = 2.0;

/// Visual settings that differ per age tier.
class TierStyle {
  const TierStyle({
    required this.seedColor,
    required this.textScale,
    required this.minTapSize,
  });

  /// Main colour; Material derives the full colour scheme from it.
  final Color seedColor;

  /// Multiplies every font size. Young children get bigger text.
  final double textScale;

  /// Minimum height of buttons, in logical pixels. Young children get
  /// very big buttons (spec C1).
  final double minTapSize;
}

const tierStyles = <AgeTier, TierStyle>{
  // Bright and playful, very big buttons.
  AgeTier.early: TierStyle(
    seedColor: Color(0xFFFF9800),
    textScale: 1.3,
    minTapSize: 72,
  ),
  // Warm green (Mithu's colour), big buttons.
  AgeTier.primary: TierStyle(
    seedColor: Color(0xFF43A047),
    textScale: 1.15,
    minTapSize: 60,
  ),
  // Less childish.
  AgeTier.middle: TierStyle(
    seedColor: Color(0xFF00897B),
    textScale: 1.05,
    minTapSize: 52,
  ),
  // Clean and focused.
  AgeTier.older: TierStyle(
    seedColor: Color(0xFF3949AB),
    textScale: 1.0,
    minTapSize: 48,
  ),
};

/// Builds the app theme for an age tier and language.
ThemeData buildTheme(AgeTier tier, Locale locale) {
  final style = tierStyles[tier]!;
  final isUrdu = locale.languageCode == 'ur';

  final base = ThemeData(
    colorScheme: ColorScheme.fromSeed(seedColor: style.seedColor),
    fontFamily: isUrdu ? urduFontFamily : null,
  );

  // ThemeData's text theme has no font sizes until it is localized, so
  // start from Material's sizes ("tall" for scripts like Urdu) to scale them.
  final geometry = isUrdu ? Typography.tall2021 : Typography.englishLike2021;
  var textTheme = geometry
      .merge(base.textTheme)
      .apply(fontSizeFactor: style.textScale);
  if (isUrdu) textTheme = _withLineHeight(textTheme, urduLineHeight);

  final minSize = Size(style.minTapSize, style.minTapSize);
  return base.copyWith(
    textTheme: textTheme,
    filledButtonTheme: FilledButtonThemeData(
      style: FilledButton.styleFrom(minimumSize: minSize),
    ),
    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(minimumSize: minSize),
    ),
    listTileTheme: ListTileThemeData(minTileHeight: style.minTapSize),
  );
}

TextTheme _withLineHeight(TextTheme t, double height) {
  TextStyle? h(TextStyle? s) => s?.copyWith(height: height);
  return t.copyWith(
    displayLarge: h(t.displayLarge),
    displayMedium: h(t.displayMedium),
    displaySmall: h(t.displaySmall),
    headlineLarge: h(t.headlineLarge),
    headlineMedium: h(t.headlineMedium),
    headlineSmall: h(t.headlineSmall),
    titleLarge: h(t.titleLarge),
    titleMedium: h(t.titleMedium),
    titleSmall: h(t.titleSmall),
    bodyLarge: h(t.bodyLarge),
    bodyMedium: h(t.bodyMedium),
    bodySmall: h(t.bodySmall),
    labelLarge: h(t.labelLarge),
    labelMedium: h(t.labelMedium),
    labelSmall: h(t.labelSmall),
  );
}

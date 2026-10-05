import 'package:flutter/material.dart';

import '../motion_widgets.dart';
import 'age_tier.dart';

/// Font family name registered in pubspec.yaml.
const urduFontFamily = 'NotoNastaliqUrdu';

/// Nastaliq letters reach far above and below the line, so Urdu text
/// needs extra line height or it gets clipped.
const urduLineHeight = 2.0;

/// Font for English text (Nunito, SIL Open Font License,
/// assets/fonts/Nunito-OFL.txt): round and friendly, easy for children.
const latinFontFamily = 'Nunito';

/// The app's colours (the "new look" mock-ups, 2026-10-05): soft lilac
/// backgrounds, white cards, dark ink text and pastel tiles.
abstract final class AppColors {
  static const ink = Color(0xFF1E1B3A);
  static const muted = Color(0xFF5E5A7A);
  static const background = Color(0xFFF7F6FB);
  static const line = Color(0xFFE2DEF5);
  static const lilac = Color(0xFF5B4BDB);
  static const lilacSoft = Color(0xFFECE8FF);
  static const green = Color(0xFF2E9D5B);
  static const greenDark = Color(0xFF1F7A45);
  static const greenSoft = Color(0xFFE3F6EC);
  static const orange = Color(0xFFE06A00);
  static const orangeSoft = Color(0xFFFFEBDD);
  static const sky = Color(0xFF1D5FA8);
  static const skySoft = Color(0xFFE2F0FF);
  static const pink = Color(0xFF9D1F5C);
  static const pinkSoft = Color(0xFFFCE4EF);

  /// Pastel tile colours, in turn, with a matching dark colour for the
  /// icon and text on them.
  static const tiles = [
    (soft: greenSoft, strong: greenDark),
    (soft: lilacSoft, strong: Color(0xFF4B3CC4)),
    (soft: orangeSoft, strong: Color(0xFF8A3F06)),
    (soft: skySoft, strong: sky),
    (soft: pinkSoft, strong: pink),
  ];
}

/// Visual settings that differ per age tier.
class TierStyle {
  const TierStyle({
    required this.seedColor,
    required this.textScale,
    required this.minTapSize,
    required this.tint,
  });

  /// Main colour (buttons, progress, selected things).
  final Color seedColor;

  /// Multiplies every font size. Young children get bigger text.
  final double textScale;

  /// Minimum height of buttons, in logical pixels. Young children get
  /// very big buttons (spec C1).
  final double minTapSize;

  /// The soft colour at the top of each screen's background.
  final Color tint;
}

const tierStyles = <AgeTier, TierStyle>{
  // Warm orange, very big buttons.
  AgeTier.early: TierStyle(
    seedColor: AppColors.orange,
    textScale: 1.3,
    minTapSize: 72,
    tint: Color(0xFFFFE9D4),
  ),
  // Mithu's green, big buttons.
  AgeTier.primary: TierStyle(
    seedColor: AppColors.green,
    textScale: 1.15,
    minTapSize: 60,
    tint: Color(0xFFDDF4E7),
  ),
  // Calm blue.
  AgeTier.middle: TierStyle(
    seedColor: Color(0xFF3F5FD0),
    textScale: 1.05,
    minTapSize: 52,
    tint: Color(0xFFE2ECFF),
  ),
  // Lilac, clean and focused.
  AgeTier.older: TierStyle(
    seedColor: AppColors.lilac,
    textScale: 1.0,
    minTapSize: 48,
    tint: Color(0xFFE9E4FF),
  ),
};

/// Rounded corners used across the app.
abstract final class AppRadius {
  static const card = 24.0;
  static const button = 18.0;
  static const tile = 22.0;
}

/// Builds the app theme for an age tier and language.
ThemeData buildTheme(AgeTier tier, Locale locale) {
  final style = tierStyles[tier]!;
  final isUrdu = locale.languageCode == 'ur';

  final scheme = ColorScheme.fromSeed(
    seedColor: style.seedColor,
    primary: style.seedColor,
    onPrimary: Colors.white,
    surface: Colors.white,
    onSurface: AppColors.ink,
    onSurfaceVariant: AppColors.muted,
    outline: AppColors.line,
    outlineVariant: AppColors.line,
  );
  final base = ThemeData(
    colorScheme: scheme,
    fontFamily: isUrdu ? urduFontFamily : latinFontFamily,
    scaffoldBackgroundColor: AppColors.background,
  );

  // ThemeData's text theme has no font sizes until it is localized, so
  // start from Material's sizes ("tall" for scripts like Urdu) to scale them.
  final geometry = isUrdu ? Typography.tall2021 : Typography.englishLike2021;
  var textTheme = geometry
      .merge(base.textTheme)
      .apply(fontSizeFactor: style.textScale)
      .apply(bodyColor: AppColors.ink, displayColor: AppColors.ink);
  textTheme = _bolder(textTheme);
  if (isUrdu) textTheme = _withLineHeight(textTheme, urduLineHeight);

  final minSize = Size(style.minTapSize, style.minTapSize);
  final buttonShape = RoundedRectangleBorder(
    borderRadius: BorderRadius.circular(AppRadius.button),
  );
  final buttonText = textTheme.labelLarge!.copyWith(
    fontSize: textTheme.titleMedium!.fontSize,
    fontWeight: FontWeight.w800,
  );
  final fieldBorder = OutlineInputBorder(
    borderRadius: BorderRadius.circular(AppRadius.button),
    borderSide: const BorderSide(color: AppColors.line, width: 1.5),
  );
  return base.copyWith(
    textTheme: textTheme,
    appBarTheme: AppBarTheme(
      backgroundColor: AppColors.background,
      surfaceTintColor: Colors.transparent,
      foregroundColor: AppColors.ink,
      elevation: 0,
      scrolledUnderElevation: 0,
      centerTitle: true,
      titleTextStyle: textTheme.titleLarge!.copyWith(
        fontWeight: FontWeight.w900,
      ),
    ),
    cardTheme: CardThemeData(
      color: Colors.white,
      surfaceTintColor: Colors.transparent,
      elevation: 2,
      shadowColor: const Color(0x225B4BDB),
      margin: const EdgeInsets.symmetric(vertical: 6),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(AppRadius.card),
      ),
      clipBehavior: Clip.antiAlias,
    ),
    filledButtonTheme: FilledButtonThemeData(
      style: FilledButton.styleFrom(
        minimumSize: minSize,
        shape: buttonShape,
        textStyle: buttonText,
        padding: const EdgeInsets.symmetric(horizontal: 22),
      ),
    ),
    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(
        minimumSize: minSize,
        shape: buttonShape,
        textStyle: buttonText,
        foregroundColor: AppColors.ink,
        backgroundColor: Colors.white,
        side: const BorderSide(color: AppColors.line, width: 2),
        padding: const EdgeInsets.symmetric(horizontal: 22),
      ),
    ),
    textButtonTheme: TextButtonThemeData(
      style: TextButton.styleFrom(
        shape: buttonShape,
        textStyle: buttonText.copyWith(fontSize: textTheme.bodyLarge!.fontSize),
      ),
    ),
    iconButtonTheme: IconButtonThemeData(
      style: IconButton.styleFrom(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
      ),
    ),
    chipTheme: ChipThemeData(
      shape: const StadiumBorder(),
      side: const BorderSide(color: AppColors.line, width: 1.5),
      backgroundColor: Colors.white,
      selectedColor: AppColors.ink,
      checkmarkColor: Colors.white,
      labelStyle: textTheme.labelLarge!.copyWith(
        fontWeight: FontWeight.w800,
        color: WidgetStateColor.resolveWith(
          (states) => states.contains(WidgetState.selected)
              ? Colors.white
              : AppColors.ink,
        ),
      ),
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: Colors.white,
      border: fieldBorder,
      enabledBorder: fieldBorder,
      focusedBorder: fieldBorder.copyWith(
        borderSide: BorderSide(color: style.seedColor, width: 2),
      ),
    ),
    switchTheme: SwitchThemeData(
      trackColor: WidgetStateProperty.resolveWith(
        (states) => states.contains(WidgetState.selected)
            ? AppColors.green
            : AppColors.line,
      ),
      thumbColor: const WidgetStatePropertyAll(Colors.white),
      trackOutlineColor: const WidgetStatePropertyAll(Colors.transparent),
    ),
    progressIndicatorTheme: ProgressIndicatorThemeData(
      color: style.seedColor,
      linearTrackColor: AppColors.lilacSoft,
      linearMinHeight: 10,
      borderRadius: BorderRadius.circular(999),
    ),
    listTileTheme: ListTileThemeData(
      minTileHeight: style.minTapSize,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      iconColor: AppColors.muted,
    ),
    dividerTheme: const DividerThemeData(color: Color(0xFFF0EEF7)),
    snackBarTheme: SnackBarThemeData(
      behavior: SnackBarBehavior.floating,
      backgroundColor: AppColors.ink,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
    ),
    dialogTheme: DialogThemeData(
      backgroundColor: Colors.white,
      surfaceTintColor: Colors.transparent,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(AppRadius.card),
      ),
    ),
    pageTransitionsTheme: const PageTransitionsTheme(
      builders: {
        TargetPlatform.android: WavePageTransitionsBuilder(),
        TargetPlatform.iOS: WavePageTransitionsBuilder(),
        TargetPlatform.linux: WavePageTransitionsBuilder(),
        TargetPlatform.macOS: WavePageTransitionsBuilder(),
        TargetPlatform.windows: WavePageTransitionsBuilder(),
      },
    ),
  );
}

/// Titles and labels are bold in the new look. Both fonts are variable
/// fonts; Flutter sets their weight from the font weight by itself.
TextTheme _bolder(TextTheme t) {
  TextStyle? w(TextStyle? s, FontWeight weight) =>
      s?.copyWith(fontWeight: weight);
  return t.copyWith(
    displayLarge: w(t.displayLarge, FontWeight.w900),
    displayMedium: w(t.displayMedium, FontWeight.w900),
    displaySmall: w(t.displaySmall, FontWeight.w900),
    headlineLarge: w(t.headlineLarge, FontWeight.w900),
    headlineMedium: w(t.headlineMedium, FontWeight.w900),
    headlineSmall: w(t.headlineSmall, FontWeight.w900),
    titleLarge: w(t.titleLarge, FontWeight.w900),
    titleMedium: w(t.titleMedium, FontWeight.w800),
    titleSmall: w(t.titleSmall, FontWeight.w800),
    bodyLarge: w(t.bodyLarge, FontWeight.w600),
    bodyMedium: w(t.bodyMedium, FontWeight.w600),
    bodySmall: w(t.bodySmall, FontWeight.w600),
    labelLarge: w(t.labelLarge, FontWeight.w800),
    labelMedium: w(t.labelMedium, FontWeight.w800),
    labelSmall: w(t.labelSmall, FontWeight.w700),
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

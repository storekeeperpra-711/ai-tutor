import 'package:flutter/widgets.dart';
import 'package:json_annotation/json_annotation.dart';

part 'localized_text.g.dart';

/// Student-facing text in English and Urdu: `{"en": "...", "ur": "..."}`.
@JsonSerializable()
class LocalizedText {
  const LocalizedText({required this.en, required this.ur});

  factory LocalizedText.fromJson(Map<String, dynamic> json) =>
      _$LocalizedTextFromJson(json);

  final String en;
  final String ur;

  /// The text in the given language (falls back to English).
  String inLanguage(String languageCode) => languageCode == 'ur' ? ur : en;

  /// The text in the app's current language.
  String of(BuildContext context) =>
      inLanguage(Localizations.localeOf(context).languageCode);
}

import '../../l10n/app_localizations.dart';

/// "Nursery", "Prep" or "Grade 6", in the app's language.
String gradeName(AppLocalizations l10n, int grade) => switch (grade) {
  -1 => l10n.gradeNursery,
  0 => l10n.gradePrep,
  _ => l10n.gradeNumber(grade),
};

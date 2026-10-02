// ignore: unused_import
import 'package:intl/intl.dart' as intl;

import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for English (`en`).
class AppLocalizationsEn extends AppLocalizations {
  AppLocalizationsEn([String locale = 'en']) : super(locale);

  @override
  String get appTitle => 'AI Tutor';

  @override
  String get homeWelcome => 'Welcome! Your lessons will appear here.';

  @override
  String get settingsTitle => 'Settings';

  @override
  String get languageLabel => 'Language';

  @override
  String get ageTierLabel => 'Age group (developer setting)';

  @override
  String get tierEarly => 'Nursery to Grade 2';

  @override
  String get tierPrimary => 'Grades 3 to 5';

  @override
  String get tierMiddle => 'Grades 6 to 8';

  @override
  String get tierOlder => 'Grades 9 to 12';

  @override
  String get urduTestTitle => 'Urdu text test';
}

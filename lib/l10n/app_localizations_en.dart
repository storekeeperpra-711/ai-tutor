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

  @override
  String get continueButton => 'Continue';

  @override
  String get checkButton => 'Check';

  @override
  String get finishButton => 'Finish';

  @override
  String get answerLabel => 'Your answer';

  @override
  String get hintLabel => 'Hint';

  @override
  String get tryAgain => 'Not yet. Look at the hint and try again.';

  @override
  String get typeANumber => 'Please type a number, like 8 or ۸.';

  @override
  String stepNotSupported(String type) {
    return 'This kind of step ($type) can\'t be played yet. Tap Continue to skip it.';
  }

  @override
  String stepProgress(int current, int total) {
    return 'Step $current of $total';
  }

  @override
  String get lessonLoadError => 'This lesson could not be opened.';

  @override
  String get lessonsPreviewTitle => 'Lessons (developer preview)';

  @override
  String minutesShort(int count) {
    return '$count min';
  }

  @override
  String get switchLanguage => 'Switch language';
}

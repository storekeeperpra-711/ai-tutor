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

  @override
  String get fractionUnreadable =>
      'Write a fraction like 3/4, or a mixed number like 1 1/2.';

  @override
  String get fractionNotSimplest =>
      'That\'s the right value! Now write it in lowest terms: divide the top and bottom by the same number.';

  @override
  String get chemUnreadable =>
      'I couldn\'t read that equation. Write it like this: 2H2 + O2 -> 2H2O';

  @override
  String chemUnknownElement(String symbol) {
    return '\"$symbol\" is not an element symbol. A symbol starts with a capital letter and any second letter is small: Co is cobalt, but CO is carbon and oxygen.';
  }

  @override
  String get chemWrongSubstances =>
      'Check the substances. Use exactly the ones in the question, without adding or leaving out any.';

  @override
  String chemChangedSubscript(String student, String expected) {
    return 'You wrote $student. To balance an equation, change only the big numbers in front. The small numbers inside $expected must stay the same, or it becomes a different substance.';
  }

  @override
  String chemUnbalanced(String element, int left, int right) {
    return 'Count the $element atoms: $left on the left and $right on the right. Change a number in front of a substance to make them equal.';
  }

  @override
  String chemNotLowest(int divisor) {
    return 'It\'s balanced! But all the numbers in front can be divided by $divisor. Use the smallest whole numbers.';
  }

  @override
  String linearUnreadable(int line) {
    return 'I couldn\'t read line $line. Write each line as an equation, like 2x + 3 = 11.';
  }

  @override
  String linearBrokenStep(int line) {
    return 'Line $line doesn\'t keep the scale balanced. Whatever you do to one side, do exactly the same to the other side.';
  }

  @override
  String linearNotFinished(String variable) {
    return 'Good so far! Keep going until one line says $variable = a number.';
  }

  @override
  String get answerUnreadable =>
      'I couldn\'t read that answer. Please try writing it again.';

  @override
  String get answerHintMultiline => 'Write each step on a new line.';

  @override
  String get checkedByCode => 'Checked by the app';
}

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
  String get homeWelcome => 'Welcome! Add a learner to begin.';

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

  @override
  String get whoIsLearning => 'Who is learning?';

  @override
  String get addLearner => 'Add a learner';

  @override
  String get firstNameLabel => 'First name';

  @override
  String get firstNameHelp => 'Only the first name, please.';

  @override
  String get gradeLabel => 'Class';

  @override
  String get gradeNursery => 'Nursery';

  @override
  String get gradePrep => 'Prep';

  @override
  String gradeNumber(int grade) {
    return 'Grade $grade';
  }

  @override
  String get pictureLabel => 'Choose a picture';

  @override
  String get pinOptionalLabel => 'PIN (optional, 4 digits)';

  @override
  String get pinHelp => 'A PIN keeps brothers and sisters out of this profile.';

  @override
  String get pinTooShort => 'A PIN has 4 digits.';

  @override
  String get consentLabel =>
      'I am this child\'s parent or guardian, and I agree to save their first name, class and progress.';

  @override
  String get saveButton => 'Save';

  @override
  String get cancelButton => 'Cancel';

  @override
  String get enterPin => 'Enter your PIN';

  @override
  String get wrongPin => 'That PIN is not right. Try again.';

  @override
  String helloName(String name) {
    return 'Hello, $name!';
  }

  @override
  String get switchLearner => 'Switch learner';

  @override
  String get lessonsTitle => 'Your lessons';

  @override
  String get noLessonsYet => 'New lessons are coming soon.';

  @override
  String get lessonStart => 'Start';

  @override
  String lessonContinue(int step, int total) {
    return 'Continue at step $step of $total';
  }

  @override
  String get lessonDone => 'Done';

  @override
  String get offlineStatus => 'Offline: your work is saved on this phone';

  @override
  String waitingToSync(int count) {
    return 'Answers waiting to go online: $count';
  }

  @override
  String get accountTitle => 'Parent and teacher account';

  @override
  String get accountPhoneOnly =>
      'Learners\' work is backed up online. Sign in or create an account so you can get it back on a new phone.';

  @override
  String signedInAs(String email) {
    return 'Signed in as $email';
  }

  @override
  String get emailLabel => 'Email';

  @override
  String get passwordLabel => 'Password (at least 6 characters)';

  @override
  String get roleParent => 'Parent';

  @override
  String get roleTeacher => 'Teacher';

  @override
  String get createAccount => 'Create account';

  @override
  String get signIn => 'Sign in';

  @override
  String get signOut => 'Sign out';

  @override
  String get signOutConfirm =>
      'Sign out and remove the learners from this phone? Their work stays in your account.';

  @override
  String signOutUnsynced(int count) {
    return '$count answers are not online yet and will be lost if you sign out now.';
  }

  @override
  String get authWrongPassword => 'The email or password is not right.';

  @override
  String get authEmailInUse =>
      'This email already has an account. Please sign in instead.';

  @override
  String get authWeakPassword => 'Please use at least 6 characters.';

  @override
  String get authInvalidEmail => 'Please check the email address.';

  @override
  String get authNoConnection =>
      'No internet. Please try again when you are online.';

  @override
  String get authOther => 'Something went wrong. Please try again.';

  @override
  String get teacherToolsSoon =>
      'Teacher tools (classes and homework) are coming soon.';

  @override
  String get learnersTitle => 'Learners on this phone';

  @override
  String get removeLearner => 'Remove learner';

  @override
  String removeLearnerConfirm(String name) {
    return 'Remove $name and all of their progress?';
  }

  @override
  String get removeButton => 'Remove';
}

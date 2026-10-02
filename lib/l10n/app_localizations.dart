import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:intl/intl.dart' as intl;

import 'app_localizations_en.dart';
import 'app_localizations_ur.dart';

// ignore_for_file: type=lint

/// Callers can lookup localized strings with an instance of AppLocalizations
/// returned by `AppLocalizations.of(context)`.
///
/// Applications need to include `AppLocalizations.delegate()` in their app's
/// `localizationDelegates` list, and the locales they support in the app's
/// `supportedLocales` list. For example:
///
/// ```dart
/// import 'l10n/app_localizations.dart';
///
/// return MaterialApp(
///   localizationsDelegates: AppLocalizations.localizationsDelegates,
///   supportedLocales: AppLocalizations.supportedLocales,
///   home: MyApplicationHome(),
/// );
/// ```
///
/// ## Update pubspec.yaml
///
/// Please make sure to update your pubspec.yaml to include the following
/// packages:
///
/// ```yaml
/// dependencies:
///   # Internationalization support.
///   flutter_localizations:
///     sdk: flutter
///   intl: any # Use the pinned version from flutter_localizations
///
///   # Rest of dependencies
/// ```
///
/// ## iOS Applications
///
/// iOS applications define key application metadata, including supported
/// locales, in an Info.plist file that is built into the application bundle.
/// To configure the locales supported by your app, you’ll need to edit this
/// file.
///
/// First, open your project’s ios/Runner.xcworkspace Xcode workspace file.
/// Then, in the Project Navigator, open the Info.plist file under the Runner
/// project’s Runner folder.
///
/// Next, select the Information Property List item, select Add Item from the
/// Editor menu, then select Localizations from the pop-up menu.
///
/// Select and expand the newly-created Localizations item then, for each
/// locale your application supports, add a new item and select the locale
/// you wish to add from the pop-up menu in the Value field. This list should
/// be consistent with the languages listed in the AppLocalizations.supportedLocales
/// property.
abstract class AppLocalizations {
  AppLocalizations(String locale)
    : localeName = intl.Intl.canonicalizedLocale(locale.toString());

  final String localeName;

  static AppLocalizations of(BuildContext context) {
    return Localizations.of<AppLocalizations>(context, AppLocalizations)!;
  }

  static const LocalizationsDelegate<AppLocalizations> delegate =
      _AppLocalizationsDelegate();

  /// A list of this localizations delegate along with the default localizations
  /// delegates.
  ///
  /// Returns a list of localizations delegates containing this delegate along with
  /// GlobalMaterialLocalizations.delegate, GlobalCupertinoLocalizations.delegate,
  /// and GlobalWidgetsLocalizations.delegate.
  ///
  /// Additional delegates can be added by appending to this list in
  /// MaterialApp. This list does not have to be used at all if a custom list
  /// of delegates is preferred or required.
  static const List<LocalizationsDelegate<dynamic>> localizationsDelegates =
      <LocalizationsDelegate<dynamic>>[
        delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ];

  /// A list of this localizations delegate's supported locales.
  static const List<Locale> supportedLocales = <Locale>[
    Locale('en'),
    Locale('ur'),
  ];

  /// App name shown in the title bar.
  ///
  /// In en, this message translates to:
  /// **'AI Tutor'**
  String get appTitle;

  /// Placeholder text on the home screen until lessons exist (Phase 1).
  ///
  /// In en, this message translates to:
  /// **'Welcome! Your lessons will appear here.'**
  String get homeWelcome;

  /// Title of the settings screen and tooltip of the settings button.
  ///
  /// In en, this message translates to:
  /// **'Settings'**
  String get settingsTitle;

  /// Heading above the language choice.
  ///
  /// In en, this message translates to:
  /// **'Language'**
  String get languageLabel;

  /// Heading above the age-tier choice. Developer-only for now; later the tier comes from the student's grade.
  ///
  /// In en, this message translates to:
  /// **'Age group (developer setting)'**
  String get ageTierLabel;

  /// Age tier name.
  ///
  /// In en, this message translates to:
  /// **'Nursery to Grade 2'**
  String get tierEarly;

  /// Age tier name.
  ///
  /// In en, this message translates to:
  /// **'Grades 3 to 5'**
  String get tierPrimary;

  /// Age tier name.
  ///
  /// In en, this message translates to:
  /// **'Grades 6 to 8'**
  String get tierMiddle;

  /// Age tier name.
  ///
  /// In en, this message translates to:
  /// **'Grades 9 to 12'**
  String get tierOlder;

  /// Developer screen for checking Urdu font rendering.
  ///
  /// In en, this message translates to:
  /// **'Urdu text test'**
  String get urduTestTitle;

  /// Button that moves to the next lesson step.
  ///
  /// In en, this message translates to:
  /// **'Continue'**
  String get continueButton;

  /// Button that checks the student's answer.
  ///
  /// In en, this message translates to:
  /// **'Check'**
  String get checkButton;

  /// Button on the last lesson step.
  ///
  /// In en, this message translates to:
  /// **'Finish'**
  String get finishButton;

  /// Label of the answer box in number questions.
  ///
  /// In en, this message translates to:
  /// **'Your answer'**
  String get answerLabel;

  /// Label before a hint.
  ///
  /// In en, this message translates to:
  /// **'Hint'**
  String get hintLabel;

  /// Shown after a wrong answer that has no specific feedback.
  ///
  /// In en, this message translates to:
  /// **'Not yet. Look at the hint and try again.'**
  String get tryAgain;

  /// Shown when the answer box doesn't contain a number.
  ///
  /// In en, this message translates to:
  /// **'Please type a number, like 8 or ۸.'**
  String get typeANumber;

  /// Shown for lesson step types added in later phases.
  ///
  /// In en, this message translates to:
  /// **'This kind of step ({type}) can\'t be played yet. Tap Continue to skip it.'**
  String stepNotSupported(String type);

  /// Progress label in the lesson player.
  ///
  /// In en, this message translates to:
  /// **'Step {current} of {total}'**
  String stepProgress(int current, int total);

  /// Shown when a lesson file can't be read.
  ///
  /// In en, this message translates to:
  /// **'This lesson could not be opened.'**
  String get lessonLoadError;

  /// Title of the developer lesson list. Shows drafts too.
  ///
  /// In en, this message translates to:
  /// **'Lessons (developer preview)'**
  String get lessonsPreviewTitle;

  /// Lesson length.
  ///
  /// In en, this message translates to:
  /// **'{count} min'**
  String minutesShort(int count);

  /// Tooltip of the English/Urdu toggle button.
  ///
  /// In en, this message translates to:
  /// **'Switch language'**
  String get switchLanguage;

  /// Fraction answer could not be read.
  ///
  /// In en, this message translates to:
  /// **'Write a fraction like 3/4, or a mixed number like 1 1/2.'**
  String get fractionUnreadable;

  /// Fraction answer is equal but can be simplified.
  ///
  /// In en, this message translates to:
  /// **'That\'s the right value! Now write it in lowest terms: divide the top and bottom by the same number.'**
  String get fractionNotSimplest;

  /// Chemical equation could not be read.
  ///
  /// In en, this message translates to:
  /// **'I couldn\'t read that equation. Write it like this: 2H2 + O2 -> 2H2O'**
  String get chemUnreadable;

  /// Unknown element symbol in a chemical equation.
  ///
  /// In en, this message translates to:
  /// **'\"{symbol}\" is not an element symbol. A symbol starts with a capital letter and any second letter is small: Co is cobalt, but CO is carbon and oxygen.'**
  String chemUnknownElement(String symbol);

  /// Chemical equation has wrong or missing substances.
  ///
  /// In en, this message translates to:
  /// **'Check the substances. Use exactly the ones in the question, without adding or leaving out any.'**
  String get chemWrongSubstances;

  /// Student changed a subscript to balance.
  ///
  /// In en, this message translates to:
  /// **'You wrote {student}. To balance an equation, change only the big numbers in front. The small numbers inside {expected} must stay the same, or it becomes a different substance.'**
  String chemChangedSubscript(String student, String expected);

  /// Atoms of one element are not balanced.
  ///
  /// In en, this message translates to:
  /// **'Count the {element} atoms: {left} on the left and {right} on the right. Change a number in front of a substance to make them equal.'**
  String chemUnbalanced(String element, int left, int right);

  /// Balanced but coefficients not in lowest terms.
  ///
  /// In en, this message translates to:
  /// **'It\'s balanced! But all the numbers in front can be divided by {divisor}. Use the smallest whole numbers.'**
  String chemNotLowest(int divisor);

  /// A line of algebra working could not be read.
  ///
  /// In en, this message translates to:
  /// **'I couldn\'t read line {line}. Write each line as an equation, like 2x + 3 = 11.'**
  String linearUnreadable(int line);

  /// A line of working is not equivalent to the previous one.
  ///
  /// In en, this message translates to:
  /// **'Line {line} doesn\'t keep the scale balanced. Whatever you do to one side, do exactly the same to the other side.'**
  String linearBrokenStep(int line);

  /// Working is correct but has not reached the answer.
  ///
  /// In en, this message translates to:
  /// **'Good so far! Keep going until one line says {variable} = a number.'**
  String linearNotFinished(String variable);

  /// Fallback when an answer can't be read.
  ///
  /// In en, this message translates to:
  /// **'I couldn\'t read that answer. Please try writing it again.'**
  String get answerUnreadable;

  /// Helper text under a multi-line answer box.
  ///
  /// In en, this message translates to:
  /// **'Write each step on a new line.'**
  String get answerHintMultiline;

  /// Small label on feedback that the app's own checker (not AI) decided.
  ///
  /// In en, this message translates to:
  /// **'Checked by the app'**
  String get checkedByCode;
}

class _AppLocalizationsDelegate
    extends LocalizationsDelegate<AppLocalizations> {
  const _AppLocalizationsDelegate();

  @override
  Future<AppLocalizations> load(Locale locale) {
    return SynchronousFuture<AppLocalizations>(lookupAppLocalizations(locale));
  }

  @override
  bool isSupported(Locale locale) =>
      <String>['en', 'ur'].contains(locale.languageCode);

  @override
  bool shouldReload(_AppLocalizationsDelegate old) => false;
}

AppLocalizations lookupAppLocalizations(Locale locale) {
  // Lookup logic when only language code is specified.
  switch (locale.languageCode) {
    case 'en':
      return AppLocalizationsEn();
    case 'ur':
      return AppLocalizationsUr();
  }

  throw FlutterError(
    'AppLocalizations.delegate failed to load unsupported locale "$locale". This is likely '
    'an issue with the localizations generation tool. Please file an issue '
    'on GitHub with a reproducible sample app and the gen-l10n configuration '
    'that was used.',
  );
}

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

  /// Home screen text before any child profile exists.
  ///
  /// In en, this message translates to:
  /// **'Welcome! Add a learner to begin.'**
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

  /// Heading of the profile picker.
  ///
  /// In en, this message translates to:
  /// **'Who is learning?'**
  String get whoIsLearning;

  /// Button and screen title for adding a child profile.
  ///
  /// In en, this message translates to:
  /// **'Add a learner'**
  String get addLearner;

  /// Label of the child's first-name box.
  ///
  /// In en, this message translates to:
  /// **'First name'**
  String get firstNameLabel;

  /// Helper text: we keep minimal personal data.
  ///
  /// In en, this message translates to:
  /// **'Only the first name, please.'**
  String get firstNameHelp;

  /// Label of the class (grade) choice.
  ///
  /// In en, this message translates to:
  /// **'Class'**
  String get gradeLabel;

  /// School class name.
  ///
  /// In en, this message translates to:
  /// **'Nursery'**
  String get gradeNursery;

  /// School class name (the year before Grade 1).
  ///
  /// In en, this message translates to:
  /// **'Prep'**
  String get gradePrep;

  /// School class name, e.g. Grade 6.
  ///
  /// In en, this message translates to:
  /// **'Grade {grade}'**
  String gradeNumber(int grade);

  /// Heading above the profile pictures.
  ///
  /// In en, this message translates to:
  /// **'Choose a picture'**
  String get pictureLabel;

  /// Label of the optional PIN box.
  ///
  /// In en, this message translates to:
  /// **'PIN (optional, 4 digits)'**
  String get pinOptionalLabel;

  /// Helper text under the PIN box.
  ///
  /// In en, this message translates to:
  /// **'A PIN keeps brothers and sisters out of this profile.'**
  String get pinHelp;

  /// Error when the PIN is not 4 digits.
  ///
  /// In en, this message translates to:
  /// **'A PIN has 4 digits.'**
  String get pinTooShort;

  /// Parental consent tick box when adding a child.
  ///
  /// In en, this message translates to:
  /// **'I am this child\'s parent or guardian, and I agree to save their first name, class and progress.'**
  String get consentLabel;

  /// Save button.
  ///
  /// In en, this message translates to:
  /// **'Save'**
  String get saveButton;

  /// Cancel button.
  ///
  /// In en, this message translates to:
  /// **'Cancel'**
  String get cancelButton;

  /// Title of the PIN pad.
  ///
  /// In en, this message translates to:
  /// **'Enter your PIN'**
  String get enterPin;

  /// Shown after a wrong PIN.
  ///
  /// In en, this message translates to:
  /// **'That PIN is not right. Try again.'**
  String get wrongPin;

  /// Greeting on the home screen.
  ///
  /// In en, this message translates to:
  /// **'Hello, {name}!'**
  String helloName(String name);

  /// Button to go back to the profile picker.
  ///
  /// In en, this message translates to:
  /// **'Switch learner'**
  String get switchLearner;

  /// Heading above the lesson list.
  ///
  /// In en, this message translates to:
  /// **'Your lessons'**
  String get lessonsTitle;

  /// Shown when no lessons are published yet.
  ///
  /// In en, this message translates to:
  /// **'New lessons are coming soon.'**
  String get noLessonsYet;

  /// Lesson not started yet.
  ///
  /// In en, this message translates to:
  /// **'Start'**
  String get lessonStart;

  /// Lesson started but not finished.
  ///
  /// In en, this message translates to:
  /// **'Continue at step {step} of {total}'**
  String lessonContinue(int step, int total);

  /// Lesson finished.
  ///
  /// In en, this message translates to:
  /// **'Done'**
  String get lessonDone;

  /// Friendly connection state. Never blocks the lesson.
  ///
  /// In en, this message translates to:
  /// **'Offline: your work is saved on this phone'**
  String get offlineStatus;

  /// Number of saved answers not yet copied to the account.
  ///
  /// In en, this message translates to:
  /// **'Answers waiting to go online: {count}'**
  String waitingToSync(int count);

  /// Account screen title and button tooltip.
  ///
  /// In en, this message translates to:
  /// **'Parent and teacher account'**
  String get accountTitle;

  /// Shown when the phone is not linked to an adult account.
  ///
  /// In en, this message translates to:
  /// **'Learners\' work is backed up online. Sign in or create an account so you can get it back on a new phone.'**
  String get accountPhoneOnly;

  /// Account status.
  ///
  /// In en, this message translates to:
  /// **'Signed in as {email}'**
  String signedInAs(String email);

  /// Email box label.
  ///
  /// In en, this message translates to:
  /// **'Email'**
  String get emailLabel;

  /// Password box label.
  ///
  /// In en, this message translates to:
  /// **'Password (at least 6 characters)'**
  String get passwordLabel;

  /// Account type.
  ///
  /// In en, this message translates to:
  /// **'Parent'**
  String get roleParent;

  /// Account type.
  ///
  /// In en, this message translates to:
  /// **'Teacher'**
  String get roleTeacher;

  /// Button.
  ///
  /// In en, this message translates to:
  /// **'Create account'**
  String get createAccount;

  /// Button.
  ///
  /// In en, this message translates to:
  /// **'Sign in'**
  String get signIn;

  /// Button.
  ///
  /// In en, this message translates to:
  /// **'Sign out'**
  String get signOut;

  /// Confirmation before signing out.
  ///
  /// In en, this message translates to:
  /// **'Sign out and remove the learners from this phone? Their work stays in your account.'**
  String get signOutConfirm;

  /// Warning before signing out with unsynced answers.
  ///
  /// In en, this message translates to:
  /// **'{count} answers are not online yet and will be lost if you sign out now.'**
  String signOutUnsynced(int count);

  /// Sign-in error.
  ///
  /// In en, this message translates to:
  /// **'The email or password is not right.'**
  String get authWrongPassword;

  /// Sign-up error.
  ///
  /// In en, this message translates to:
  /// **'This email already has an account. Please sign in instead.'**
  String get authEmailInUse;

  /// Sign-up error.
  ///
  /// In en, this message translates to:
  /// **'Please use at least 6 characters.'**
  String get authWeakPassword;

  /// Sign-in error.
  ///
  /// In en, this message translates to:
  /// **'Please check the email address.'**
  String get authInvalidEmail;

  /// Sign-in error.
  ///
  /// In en, this message translates to:
  /// **'No internet. Please try again when you are online.'**
  String get authNoConnection;

  /// Sign-in error.
  ///
  /// In en, this message translates to:
  /// **'Something went wrong. Please try again.'**
  String get authOther;

  /// Shown to teachers until Phase 9.
  ///
  /// In en, this message translates to:
  /// **'Teacher tools (classes and homework) are coming soon.'**
  String get teacherToolsSoon;

  /// Heading of the learner list on the account screen.
  ///
  /// In en, this message translates to:
  /// **'Learners on this phone'**
  String get learnersTitle;

  /// Tooltip of the remove button.
  ///
  /// In en, this message translates to:
  /// **'Remove learner'**
  String get removeLearner;

  /// Confirmation before removing a child profile.
  ///
  /// In en, this message translates to:
  /// **'Remove {name} and all of their progress?'**
  String removeLearnerConfirm(String name);

  /// Button.
  ///
  /// In en, this message translates to:
  /// **'Remove'**
  String get removeButton;

  /// Heading of the daily plan card.
  ///
  /// In en, this message translates to:
  /// **'Today\'s plan'**
  String get todaysPlan;

  /// How long today's plan takes.
  ///
  /// In en, this message translates to:
  /// **'About {minutes} minutes'**
  String planMinutes(int minutes);

  /// Plan item: a spaced review question.
  ///
  /// In en, this message translates to:
  /// **'Review: {title}'**
  String planReview(String title);

  /// Plan item: practice on the current skill.
  ///
  /// In en, this message translates to:
  /// **'Practice: {title}'**
  String planPractice(String title);

  /// Plan item: one question from another topic.
  ///
  /// In en, this message translates to:
  /// **'A mixed question'**
  String get planMixed;

  /// Plan item: an explain or find-the-error question.
  ///
  /// In en, this message translates to:
  /// **'Explain it or find the mistake'**
  String get planExplain;

  /// Plan item: a lesson to start or continue.
  ///
  /// In en, this message translates to:
  /// **'Lesson: {title}'**
  String planLesson(String title);

  /// Plan item: a real-world task away from the phone.
  ///
  /// In en, this message translates to:
  /// **'A task to do at home'**
  String get planHomeTask;

  /// Plan item: flashcards for a topic already understood.
  ///
  /// In en, this message translates to:
  /// **'Flashcards: {title}'**
  String planFlashcards(String title);

  /// Button that starts the plan's questions.
  ///
  /// In en, this message translates to:
  /// **'Start practice'**
  String get startPractice;

  /// Shown when every plan item is done.
  ///
  /// In en, this message translates to:
  /// **'All done for today. Well done!'**
  String get planAllDone;

  /// Button that marks a home task or flashcards as done.
  ///
  /// In en, this message translates to:
  /// **'Done'**
  String get markDone;

  /// Flashcards screen title.
  ///
  /// In en, this message translates to:
  /// **'Flashcards'**
  String get flashcardsTitle;

  /// Help text on the flashcards screen.
  ///
  /// In en, this message translates to:
  /// **'Tap the card to turn it over.'**
  String get flashcardTapToTurn;

  /// Button on the flashcards screen.
  ///
  /// In en, this message translates to:
  /// **'Next card'**
  String get nextCard;

  /// Title of the home task dialog.
  ///
  /// In en, this message translates to:
  /// **'Home task'**
  String get homeTaskTitle;

  /// Practice screen title.
  ///
  /// In en, this message translates to:
  /// **'Practice'**
  String get practiceTitle;

  /// Shown after a practice session.
  ///
  /// In en, this message translates to:
  /// **'Well done! {right} of {total} right the first time.'**
  String practiceDone(int right, int total);

  /// Mastery level.
  ///
  /// In en, this message translates to:
  /// **'Not started'**
  String get levelNotStarted;

  /// Mastery level.
  ///
  /// In en, this message translates to:
  /// **'Learning'**
  String get levelLearning;

  /// Mastery level.
  ///
  /// In en, this message translates to:
  /// **'Practising'**
  String get levelPractising;

  /// Mastery level.
  ///
  /// In en, this message translates to:
  /// **'Mastered'**
  String get levelMastered;

  /// Mastery level: still remembered weeks later.
  ///
  /// In en, this message translates to:
  /// **'Secure'**
  String get levelSecure;

  /// Title when an alternative explanation is shown to a stuck student.
  ///
  /// In en, this message translates to:
  /// **'Let\'s try it another way.'**
  String get tryAnotherWay;

  /// Offer to go back to a prerequisite lesson.
  ///
  /// In en, this message translates to:
  /// **'Let\'s look at an earlier idea first: {title}'**
  String stuckPrerequisite(String title);

  /// Button to open the prerequisite lesson.
  ///
  /// In en, this message translates to:
  /// **'Open that lesson'**
  String get openLesson;

  /// Button to continue the current lesson.
  ///
  /// In en, this message translates to:
  /// **'Keep going'**
  String get keepGoing;

  /// Suggests a break after repeated mistakes.
  ///
  /// In en, this message translates to:
  /// **'This one is tricky. A short break can help. Your work is saved.'**
  String get stuckBreak;

  /// Suggests asking an adult after many mistakes.
  ///
  /// In en, this message translates to:
  /// **'This one is tricky. Ask a parent or teacher to look at it with you. Your work is saved.'**
  String get stuckHelp;

  /// Button that leaves the lesson for a break.
  ///
  /// In en, this message translates to:
  /// **'Take a break'**
  String get takeBreak;

  /// On the account screen, under a learner who is stuck.
  ///
  /// In en, this message translates to:
  /// **'Needs help with: {topics}'**
  String needsHelpWith(String topics);

  /// A simulation reported no answer yet.
  ///
  /// In en, this message translates to:
  /// **'Finish the activity, then press Check.'**
  String get simNoResult;

  /// Under a simulation before the child has answered.
  ///
  /// In en, this message translates to:
  /// **'Try the activity, then press its Check button.'**
  String get simUseActivity;

  /// A simulation failed to load.
  ///
  /// In en, this message translates to:
  /// **'This activity can\'t start on this phone. Let\'s carry on.'**
  String get simCouldNotStart;

  /// Undo the last move in an interactive.
  ///
  /// In en, this message translates to:
  /// **'Undo'**
  String get simUndo;

  /// Fraction bars: stepper for how many pieces to cut each whole into.
  ///
  /// In en, this message translates to:
  /// **'Pieces in each one'**
  String get fractionBarsCut;

  /// Fraction bars: how many pieces are tapped.
  ///
  /// In en, this message translates to:
  /// **'Pieces chosen: {count}'**
  String fractionBarsChosen(int count);

  /// Balance scale: remove one weight from this side.
  ///
  /// In en, this message translates to:
  /// **'Take 1'**
  String get scaleTakeOne;

  /// Balance scale: remove one x-box from this side.
  ///
  /// In en, this message translates to:
  /// **'Take x'**
  String get scaleTakeX;

  /// Balance scale: left pan.
  ///
  /// In en, this message translates to:
  /// **'Left side'**
  String get scaleLeft;

  /// Balance scale: right pan.
  ///
  /// In en, this message translates to:
  /// **'Right side'**
  String get scaleRight;

  /// Balance scale: both sides weigh the same.
  ///
  /// In en, this message translates to:
  /// **'Balanced'**
  String get scaleBalanced;

  /// Balance scale: the scale has tipped.
  ///
  /// In en, this message translates to:
  /// **'Not balanced!'**
  String get scaleTipped;

  /// Balance scale: divide both sides into n equal groups and keep one.
  ///
  /// In en, this message translates to:
  /// **'Share into {n} groups'**
  String scaleShare(int n);

  /// Atom balancer: atoms on the left side.
  ///
  /// In en, this message translates to:
  /// **'Left'**
  String get atomsLeft;

  /// Atom balancer: atoms on the right side.
  ///
  /// In en, this message translates to:
  /// **'Right'**
  String get atomsRight;

  /// Atom balancer: equation is balanced.
  ///
  /// In en, this message translates to:
  /// **'Every element is balanced!'**
  String get atomsBalanced;

  /// Number line: the marked value.
  ///
  /// In en, this message translates to:
  /// **'Your number: {value}'**
  String numberLineValue(String value);

  /// Graph plotter: how to move the points.
  ///
  /// In en, this message translates to:
  /// **'Drag a point, or pick A or B and use the arrows.'**
  String get graphHint;

  /// A video failed to load; the summary follows.
  ///
  /// In en, this message translates to:
  /// **'The video can\'t play right now. Here is what it shows:'**
  String get videoCouldNotPlay;

  /// Video play button.
  ///
  /// In en, this message translates to:
  /// **'Play'**
  String get videoPlay;

  /// Video pause button.
  ///
  /// In en, this message translates to:
  /// **'Pause'**
  String get videoPause;

  /// Video replay button.
  ///
  /// In en, this message translates to:
  /// **'Watch again'**
  String get videoReplay;

  /// Toggle captions on a video.
  ///
  /// In en, this message translates to:
  /// **'Captions'**
  String get videoCaptions;

  /// Settings switch that turns off most animations.
  ///
  /// In en, this message translates to:
  /// **'Less movement'**
  String get lessMotion;

  /// Explains the Less movement setting.
  ///
  /// In en, this message translates to:
  /// **'Fewer animations. Some children focus better, and it saves battery.'**
  String get lessMotionHint;

  /// Celebration after the last step of a lesson.
  ///
  /// In en, this message translates to:
  /// **'Lesson finished! Well done.'**
  String get lessonFinished;

  /// Celebration when a skill reaches a new mastery level.
  ///
  /// In en, this message translates to:
  /// **'{topic}: {level}!'**
  String levelUp(String topic, String level);

  /// Developer screen listing every simulation.
  ///
  /// In en, this message translates to:
  /// **'Simulations (developer)'**
  String get simGalleryTitle;

  /// Shown while the AI checks an explanation.
  ///
  /// In en, this message translates to:
  /// **'Mithu is reading your answer…'**
  String get aiThinking;

  /// Small label on feedback written by AI.
  ///
  /// In en, this message translates to:
  /// **'Checked by AI'**
  String get checkedByAi;

  /// Small label on feedback from the offline keyword check.
  ///
  /// In en, this message translates to:
  /// **'Checked by keywords'**
  String get checkedByKeywords;

  /// The answer was checked offline and waits for AI feedback.
  ///
  /// In en, this message translates to:
  /// **'No internet right now. Mithu will look at your answer later.'**
  String get aiQueued;

  /// A daily AI limit was reached.
  ///
  /// In en, this message translates to:
  /// **'Mithu has helped a lot today, so the app checked this one.'**
  String get aiLimitReached;

  /// Button to edit an explanation and check it again.
  ///
  /// In en, this message translates to:
  /// **'Improve my answer'**
  String get improveAnswer;

  /// Help under the explanation box.
  ///
  /// In en, this message translates to:
  /// **'Write in English, Urdu or Roman Urdu.'**
  String get explainInputHelp;

  /// Explanation level: shows the idea.
  ///
  /// In en, this message translates to:
  /// **'Got it!'**
  String get levelGotIt;

  /// Explanation level: part of the idea.
  ///
  /// In en, this message translates to:
  /// **'Partly there'**
  String get levelPartly;

  /// Explanation level: not the idea yet.
  ///
  /// In en, this message translates to:
  /// **'Not yet'**
  String get levelNotYet;

  /// Button: open the camera for notebook working.
  ///
  /// In en, this message translates to:
  /// **'Take a photo'**
  String get photoTake;

  /// Button: pick a photo from the gallery.
  ///
  /// In en, this message translates to:
  /// **'Choose a photo'**
  String get photoChoose;

  /// Button: type the working instead of a photo.
  ///
  /// In en, this message translates to:
  /// **'Type my answer instead'**
  String get photoTypeInstead;

  /// Shown while the AI reads a photo.
  ///
  /// In en, this message translates to:
  /// **'Mithu is reading your working…'**
  String get photoReading;

  /// Above the working the AI read from the photo.
  ///
  /// In en, this message translates to:
  /// **'Mithu read this. Fix anything that is wrong, then press Check.'**
  String get photoConfirm;

  /// The photo could not be read.
  ///
  /// In en, this message translates to:
  /// **'Mithu couldn\'t read that photo. Try again in good light, or type your answer.'**
  String get photoUnreadable;

  /// No connection for a photo check.
  ///
  /// In en, this message translates to:
  /// **'Photos need internet. Type your working instead.'**
  String get photoOffline;

  /// Daily photo limit reached.
  ///
  /// In en, this message translates to:
  /// **'Mithu has read enough photos today. Type your working instead.'**
  String get photoLimit;

  /// Label of the box with the working.
  ///
  /// In en, this message translates to:
  /// **'Your working (one step per line)'**
  String get photoWorkingLabel;

  /// Small label: the AI read the photo.
  ///
  /// In en, this message translates to:
  /// **'Read by AI'**
  String get readByAi;

  /// Small label: the AI explained the checker's verdict.
  ///
  /// In en, this message translates to:
  /// **'Explained by AI'**
  String get explainedByAi;

  /// Shown while the AI explains a wrong answer.
  ///
  /// In en, this message translates to:
  /// **'Mithu is looking at where it went wrong…'**
  String get photoExplaining;

  /// Button to try a photo step again.
  ///
  /// In en, this message translates to:
  /// **'Try again'**
  String get tryAgainButton;

  /// Screen with AI replies to answers that waited offline.
  ///
  /// In en, this message translates to:
  /// **'Mithu\'s notes'**
  String get mithuNotesTitle;

  /// Home card when AI replies arrived.
  ///
  /// In en, this message translates to:
  /// **'Mithu has new notes for you ({count})'**
  String mithuNotesNew(int count);

  /// An answer still waiting for AI feedback.
  ///
  /// In en, this message translates to:
  /// **'Waiting for Mithu'**
  String get mithuNotesWaiting;

  /// AI feedback for a queued answer failed.
  ///
  /// In en, this message translates to:
  /// **'Mithu couldn\'t look at this one.'**
  String get mithuNotesFailed;

  /// No queued answers.
  ///
  /// In en, this message translates to:
  /// **'No notes yet.'**
  String get mithuNotesEmpty;

  /// Button and title for the weekly parent report.
  ///
  /// In en, this message translates to:
  /// **'Weekly report'**
  String get weeklyReport;

  /// No weekly report exists.
  ///
  /// In en, this message translates to:
  /// **'No report yet. Reports are written on Sunday evenings for children who practised that week.'**
  String get weeklyReportNone;

  /// Numbers of a weekly report.
  ///
  /// In en, this message translates to:
  /// **'{days} days of practice · {lessons} lessons finished · {questions} questions answered'**
  String weeklyReportStats(int days, int lessons, int questions);

  /// Something needs a connection.
  ///
  /// In en, this message translates to:
  /// **'Connect to the internet and try again.'**
  String get needsInternet;

  /// Cost dashboard title.
  ///
  /// In en, this message translates to:
  /// **'AI use and cost'**
  String get aiCostsTitle;

  /// Cost dashboard shows every student (admin).
  ///
  /// In en, this message translates to:
  /// **'All students in the project'**
  String get aiCostsAll;

  /// Cost dashboard shows this account's students.
  ///
  /// In en, this message translates to:
  /// **'Students on this account'**
  String get aiCostsMine;

  /// Total estimated AI cost.
  ///
  /// In en, this message translates to:
  /// **'Last 7 days: {cost}'**
  String aiCostsTotal(String cost);

  /// One student's AI use on one day.
  ///
  /// In en, this message translates to:
  /// **'{calls} calls · {text} text · {photo} photos · {cost}'**
  String aiCostsRow(int calls, int text, int photo, String cost);

  /// Cost dashboard is empty.
  ///
  /// In en, this message translates to:
  /// **'No AI use in the last 7 days.'**
  String get aiCostsEmpty;

  /// Speaker button next to Mithu's speech bubble.
  ///
  /// In en, this message translates to:
  /// **'Listen to Mithu'**
  String get listenToMithu;

  /// Dev builds only: this line has no recorded voice yet.
  ///
  /// In en, this message translates to:
  /// **'Phone voice (no recording yet)'**
  String get phoneVoiceLabel;

  /// Dev screen title: narration recorder.
  ///
  /// In en, this message translates to:
  /// **'Record Mithu\'s voice'**
  String get recorderTitle;

  /// Instructions at the top of the narration recorder.
  ///
  /// In en, this message translates to:
  /// **'Find a quiet room. Hold the phone a hand\'s width from your mouth, tap Record, read the line warmly, and tap Stop. Keep each line under 30 seconds.'**
  String get recorderHelp;

  /// Filter switch in the narration recorder.
  ///
  /// In en, this message translates to:
  /// **'Only lines without a voice'**
  String get recorderMissingOnly;

  /// Start recording a line.
  ///
  /// In en, this message translates to:
  /// **'Record'**
  String get recorderRecord;

  /// Stop recording.
  ///
  /// In en, this message translates to:
  /// **'Stop'**
  String get recorderStop;

  /// Play back a recorded line.
  ///
  /// In en, this message translates to:
  /// **'Listen'**
  String get recorderPlay;

  /// Delete a recording made on this phone.
  ///
  /// In en, this message translates to:
  /// **'Delete'**
  String get recorderDelete;

  /// Line status: recorded with the dev recorder.
  ///
  /// In en, this message translates to:
  /// **'Recorded on this phone (not sent yet)'**
  String get recorderStatusPhone;

  /// Line status: a recording is bundled with the app.
  ///
  /// In en, this message translates to:
  /// **'Voice is in the app'**
  String get recorderStatusApp;

  /// Line status: no recording.
  ///
  /// In en, this message translates to:
  /// **'No voice yet'**
  String get recorderStatusMissing;

  /// Warning after a recording over 30 seconds.
  ///
  /// In en, this message translates to:
  /// **'Longer than 30 seconds: please record it shorter.'**
  String get recorderTooLong;

  /// Microphone permission was refused.
  ///
  /// In en, this message translates to:
  /// **'The app may not use the microphone. Allow it in the phone\'s settings.'**
  String get recorderNoMic;

  /// Share all recordings made on this phone.
  ///
  /// In en, this message translates to:
  /// **'Send recordings'**
  String get recorderExport;

  /// Explains what to do with exported recordings.
  ///
  /// In en, this message translates to:
  /// **'Send them to yourself (for example to Google Drive), then attach all the files in the project chat. Claude adds them to the app.'**
  String get recorderExportHelp;

  /// Export with nothing recorded.
  ///
  /// In en, this message translates to:
  /// **'No recordings on this phone yet.'**
  String get recorderNothingToSend;

  /// Settings switch for sound effects.
  ///
  /// In en, this message translates to:
  /// **'Sounds'**
  String get soundsSetting;

  /// Subtitle of the Sounds switch.
  ///
  /// In en, this message translates to:
  /// **'Small sounds for taps and answers'**
  String get soundsSettingHint;

  /// Settings switch: show the parrot character.
  ///
  /// In en, this message translates to:
  /// **'Show Mithu'**
  String get mithuSetting;

  /// Subtitle of the Show Mithu switch.
  ///
  /// In en, this message translates to:
  /// **'Mithu the parrot helps in lessons'**
  String get mithuSettingHint;

  /// Effort badge.
  ///
  /// In en, this message translates to:
  /// **'First lesson finished'**
  String get badgeFirstLesson;

  /// Effort badge.
  ///
  /// In en, this message translates to:
  /// **'Tried again after a mistake'**
  String get badgeTriedAgain;

  /// Effort badge.
  ///
  /// In en, this message translates to:
  /// **'Explained in your own words'**
  String get badgeExplained;

  /// Effort badge.
  ///
  /// In en, this message translates to:
  /// **'Fixed your work after a photo check'**
  String get badgeCheckedPhoto;

  /// Effort badge.
  ///
  /// In en, this message translates to:
  /// **'Came back to review'**
  String get badgeCameBack;

  /// Effort badge. Not a streak: any 5 days.
  ///
  /// In en, this message translates to:
  /// **'Learned on 5 different days this month'**
  String get badgeFiveDays;

  /// Heading of the badge shelf.
  ///
  /// In en, this message translates to:
  /// **'Your badges'**
  String get badgesTitle;

  /// Badge shelf count.
  ///
  /// In en, this message translates to:
  /// **'{count} of {total} badges'**
  String badgesEarned(int count, int total);

  /// Celebration: star for finishing the lesson.
  ///
  /// In en, this message translates to:
  /// **'You finished'**
  String get starFinished;

  /// Celebration: star for trying again after mistakes.
  ///
  /// In en, this message translates to:
  /// **'You kept trying'**
  String get starKeptTrying;

  /// Celebration: star for explaining (or answering every question).
  ///
  /// In en, this message translates to:
  /// **'You explained your thinking'**
  String get starExplained;

  /// Celebration praise line.
  ///
  /// In en, this message translates to:
  /// **'Well done! Your hard work is paying off.'**
  String get praise1;

  /// Celebration praise line.
  ///
  /// In en, this message translates to:
  /// **'Great effort! Mithu is proud of you.'**
  String get praise2;

  /// Celebration praise line.
  ///
  /// In en, this message translates to:
  /// **'You did it! Mistakes help us learn.'**
  String get praise3;

  /// Celebration: button to the next lesson.
  ///
  /// In en, this message translates to:
  /// **'Next: {title}'**
  String nextLesson(String title);

  /// Celebration: next step when there's no next lesson.
  ///
  /// In en, this message translates to:
  /// **'Come back tomorrow for a quick review.'**
  String get comeBackTomorrow;

  /// Celebration: go back to the home screen.
  ///
  /// In en, this message translates to:
  /// **'Home'**
  String get backHome;
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

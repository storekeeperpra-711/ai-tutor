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
      'I am this child\'s parent or guardian. I have read the privacy note, and I agree to save their first name, class and progress, and to Mithu\'s AI help.';

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
  String get allSubjects => 'All';

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
  String get learnersTitle => 'Learners on this phone';

  @override
  String get removeLearner => 'Remove learner';

  @override
  String removeLearnerConfirm(String name) {
    return 'Remove $name and all of their progress?';
  }

  @override
  String get removeButton => 'Remove';

  @override
  String get todaysPlan => 'Today\'s plan';

  @override
  String planMinutes(int minutes) {
    return 'About $minutes minutes';
  }

  @override
  String planReview(String title) {
    return 'Review: $title';
  }

  @override
  String planPractice(String title) {
    return 'Practice: $title';
  }

  @override
  String get planMixed => 'A mixed question';

  @override
  String get planExplain => 'Explain it or find the mistake';

  @override
  String planLesson(String title) {
    return 'Lesson: $title';
  }

  @override
  String get planHomeTask => 'A task to do at home';

  @override
  String planFlashcards(String title) {
    return 'Flashcards: $title';
  }

  @override
  String get startPractice => 'Start practice';

  @override
  String get planAllDone => 'All done for today. Well done!';

  @override
  String get markDone => 'Done';

  @override
  String get flashcardsTitle => 'Flashcards';

  @override
  String get flashcardTapToTurn => 'Tap the card to turn it over.';

  @override
  String get nextCard => 'Next card';

  @override
  String get homeTaskTitle => 'Home task';

  @override
  String get practiceTitle => 'Practice';

  @override
  String practiceDone(int right, int total) {
    return 'Well done! $right of $total right the first time.';
  }

  @override
  String get levelNotStarted => 'Not started';

  @override
  String get levelLearning => 'Learning';

  @override
  String get levelPractising => 'Practising';

  @override
  String get levelMastered => 'Mastered';

  @override
  String get levelSecure => 'Secure';

  @override
  String get tryAnotherWay => 'Let\'s try it another way.';

  @override
  String stuckPrerequisite(String title) {
    return 'Let\'s look at an earlier idea first: $title';
  }

  @override
  String get openLesson => 'Open that lesson';

  @override
  String get keepGoing => 'Keep going';

  @override
  String get stuckBreak =>
      'This one is tricky. A short break can help. Your work is saved.';

  @override
  String get stuckHelp =>
      'This one is tricky. Ask a parent or teacher to look at it with you. Your work is saved.';

  @override
  String get takeBreak => 'Take a break';

  @override
  String needsHelpWith(String topics) {
    return 'Needs help with: $topics';
  }

  @override
  String get simNoResult => 'Finish the activity, then press Check.';

  @override
  String get simUseActivity => 'Try the activity, then press its Check button.';

  @override
  String get simCouldNotStart =>
      'This activity can\'t start on this phone. Let\'s carry on.';

  @override
  String get simUndo => 'Undo';

  @override
  String get fractionBarsCut => 'Pieces in each one';

  @override
  String fractionBarsChosen(int count) {
    return 'Pieces chosen: $count';
  }

  @override
  String get scaleTakeOne => 'Take 1';

  @override
  String get scaleTakeX => 'Take x';

  @override
  String get scaleLeft => 'Left side';

  @override
  String get scaleRight => 'Right side';

  @override
  String get scaleBalanced => 'Balanced';

  @override
  String get scaleTipped => 'Not balanced!';

  @override
  String scaleShare(int n) {
    return 'Share into $n groups';
  }

  @override
  String get atomsLeft => 'Left';

  @override
  String get atomsRight => 'Right';

  @override
  String get atomsBalanced => 'Every element is balanced!';

  @override
  String numberLineValue(String value) {
    return 'Your number: $value';
  }

  @override
  String get graphHint => 'Drag a point, or pick A or B and use the arrows.';

  @override
  String get videoCouldNotPlay =>
      'The video can\'t play right now. Here is what it shows:';

  @override
  String get videoPlay => 'Play';

  @override
  String get videoPause => 'Pause';

  @override
  String get videoReplay => 'Watch again';

  @override
  String get videoCaptions => 'Captions';

  @override
  String get lessMotion => 'Less movement';

  @override
  String get lessMotionHint =>
      'Fewer animations. Some children focus better, and it saves battery.';

  @override
  String get lessonFinished => 'Lesson finished! Well done.';

  @override
  String levelUp(String topic, String level) {
    return '$topic: $level!';
  }

  @override
  String get simGalleryTitle => 'Simulations (developer)';

  @override
  String get aiThinking => 'Mithu is reading your answer…';

  @override
  String get checkedByAi => 'Checked by AI';

  @override
  String get checkedByKeywords => 'Checked by keywords';

  @override
  String get aiQueued =>
      'No internet right now. Mithu will look at your answer later.';

  @override
  String get aiLimitReached =>
      'Mithu has helped a lot today, so the app checked this one.';

  @override
  String get improveAnswer => 'Improve my answer';

  @override
  String get explainInputHelp => 'Write in English, Urdu or Roman Urdu.';

  @override
  String get levelGotIt => 'Got it!';

  @override
  String get levelPartly => 'Partly there';

  @override
  String get levelNotYet => 'Not yet';

  @override
  String get photoTake => 'Take a photo';

  @override
  String get photoChoose => 'Choose a photo';

  @override
  String get photoTypeInstead => 'Type my answer instead';

  @override
  String get photoReading => 'Mithu is reading your working…';

  @override
  String get photoConfirm =>
      'Mithu read this. Fix anything that is wrong, then press Check.';

  @override
  String get photoUnreadable =>
      'Mithu couldn\'t read that photo. Try again in good light, or type your answer.';

  @override
  String get photoOffline => 'Photos need internet. Type your working instead.';

  @override
  String get photoLimit =>
      'Mithu has read enough photos today. Type your working instead.';

  @override
  String get photoWorkingLabel => 'Your working (one step per line)';

  @override
  String get readByAi => 'Read by AI';

  @override
  String get explainedByAi => 'Explained by AI';

  @override
  String get photoExplaining => 'Mithu is looking at where it went wrong…';

  @override
  String get tryAgainButton => 'Try again';

  @override
  String get mithuNotesTitle => 'Mithu\'s notes';

  @override
  String mithuNotesNew(int count) {
    return 'Mithu has new notes for you ($count)';
  }

  @override
  String get mithuNotesWaiting => 'Waiting for Mithu';

  @override
  String get mithuNotesFailed => 'Mithu couldn\'t look at this one.';

  @override
  String get mithuNotesEmpty => 'No notes yet.';

  @override
  String get needsInternet => 'Connect to the internet and try again.';

  @override
  String get aiCostsTitle => 'AI use and cost';

  @override
  String get aiCostsAll => 'All students in the project';

  @override
  String get aiCostsMine => 'Students on this account';

  @override
  String aiCostsTotal(String cost) {
    return 'Last 7 days: $cost';
  }

  @override
  String aiCostsRow(int calls, int text, int photo, String cost) {
    return '$calls calls · $text text · $photo photos · $cost';
  }

  @override
  String get aiCostsEmpty => 'No AI use in the last 7 days.';

  @override
  String get listenToMithu => 'Listen to Mithu';

  @override
  String get phoneVoiceLabel => 'Phone voice (no recording yet)';

  @override
  String get recorderTitle => 'Record Mithu\'s voice';

  @override
  String get recorderHelp =>
      'Find a quiet room. Hold the phone a hand\'s width from your mouth, tap Record, read the line warmly, and tap Stop. Keep each line under 30 seconds.';

  @override
  String get recorderMissingOnly => 'Only lines without a voice';

  @override
  String get recorderRecord => 'Record';

  @override
  String get recorderStop => 'Stop';

  @override
  String get recorderPlay => 'Listen';

  @override
  String get recorderDelete => 'Delete';

  @override
  String get recorderStatusPhone => 'Recorded on this phone (not sent yet)';

  @override
  String get recorderStatusApp => 'Voice is in the app';

  @override
  String get recorderStatusMissing => 'No voice yet';

  @override
  String get recorderTooLong =>
      'Longer than 30 seconds: please record it shorter.';

  @override
  String get recorderNoMic =>
      'The app may not use the microphone. Allow it in the phone\'s settings.';

  @override
  String get recorderExport => 'Send recordings';

  @override
  String get recorderExportHelp =>
      'Send them to yourself (for example to Google Drive), then attach all the files in the project chat. Claude adds them to the app.';

  @override
  String get recorderNothingToSend => 'No recordings on this phone yet.';

  @override
  String get soundsSetting => 'Sounds';

  @override
  String get soundsSettingHint => 'Small sounds for taps and answers';

  @override
  String get mithuSetting => 'Show Mithu';

  @override
  String get mithuSettingHint => 'Mithu the parrot helps in lessons';

  @override
  String get badgeFirstLesson => 'First lesson finished';

  @override
  String get badgeTriedAgain => 'Tried again after a mistake';

  @override
  String get badgeExplained => 'Explained in your own words';

  @override
  String get badgeCheckedPhoto => 'Fixed your work after a photo check';

  @override
  String get badgeCameBack => 'Came back to review';

  @override
  String get badgeFiveDays => 'Learned on 5 different days this month';

  @override
  String get badgesTitle => 'Your badges';

  @override
  String badgesEarned(int count, int total) {
    return '$count of $total badges';
  }

  @override
  String get starFinished => 'You finished';

  @override
  String get starKeptTrying => 'You kept trying';

  @override
  String get starExplained => 'You explained your thinking';

  @override
  String get praise1 => 'Well done! Your hard work is paying off.';

  @override
  String get praise2 => 'Great effort! Mithu is proud of you.';

  @override
  String get praise3 => 'You did it! Mistakes help us learn.';

  @override
  String nextLesson(String title) {
    return 'Next: $title';
  }

  @override
  String get comeBackTomorrow => 'Come back tomorrow for a quick review.';

  @override
  String get backHome => 'Home';

  @override
  String earlyGreeting(String name) {
    return 'Assalam o Alaikum, $name! Let\'s play and learn.';
  }

  @override
  String get playButton => 'Play';

  @override
  String get mithuTip1 =>
      'Tip: if you get stuck, read the question again slowly.';

  @override
  String get mithuTip2 => 'Tip: mistakes are how our brains grow. Try again!';

  @override
  String get mithuTip3 => 'Tip: explain your answer to someone at home.';

  @override
  String questTitle(String subject) {
    return '$subject quest';
  }

  @override
  String questProgress(int done, int total) {
    return '$done of $total lessons done';
  }

  @override
  String get questDone => 'Quest complete! Keep reviewing to stay strong.';

  @override
  String secureSkills(int count, int total) {
    return '$count of $total skills secure';
  }

  @override
  String subjectLevel(int level) {
    return 'Level $level';
  }

  @override
  String get subjectsTitle => 'Your subjects';

  @override
  String get masteryBySubject => 'Mastery by subject';

  @override
  String masteredSkills(int count, int total) {
    return '$count of $total skills mastered';
  }

  @override
  String examCountdown(int days) {
    String _temp0 = intl.Intl.pluralLogic(
      days,
      locale: localeName,
      other: '$days days to your board exam',
      one: '1 day to your board exam',
    );
    return '$_temp0';
  }

  @override
  String get examToday =>
      'Your board exam is today. You\'ve prepared well. Good luck!';

  @override
  String get examSetPrompt => 'Set your board exam date to see a countdown';

  @override
  String get examDateSetting => 'Board exam date';

  @override
  String get examDateNotSet => 'Not set';

  @override
  String get examDateClear => 'Clear';

  @override
  String get subjectMaths => 'Maths';

  @override
  String get subjectChemistry => 'Chemistry';

  @override
  String get subjectPhysics => 'Physics';

  @override
  String get subjectBiology => 'Biology';

  @override
  String get subjectScience => 'Science';

  @override
  String get subjectEnglish => 'English';

  @override
  String get subjectUrdu => 'Urdu';

  @override
  String get reviewTitle => 'Review lessons';

  @override
  String get reviewSignIn =>
      'Sign in with your teacher account to review lessons.';

  @override
  String get reviewSignInButton => 'Sign in';

  @override
  String reviewVerify(String email) {
    return 'First we check that $email is your email. Tap the button, then open the link we email you.';
  }

  @override
  String get reviewSendLink => 'Email me the link';

  @override
  String get reviewLinkSent => 'Sent. Check your inbox, and the spam folder.';

  @override
  String get reviewCheckAgain => 'I\'ve opened the link';

  @override
  String reviewNotReviewer(String email) {
    return '$email can\'t review lessons yet. Ask the app\'s owner to add it.';
  }

  @override
  String get reviewNothing => 'No lessons to review.';

  @override
  String get reviewStatusInReview => 'Waiting for review';

  @override
  String get reviewStatusApproved => 'Approved';

  @override
  String get reviewStatusChanges => 'Needs changes';

  @override
  String reviewVersion(int version) {
    return 'Version $version';
  }

  @override
  String get reviewPlay => 'Play the lesson';

  @override
  String get reviewPlayHint =>
      'Play it as a child would. On any step, tap the note button to write what should change.';

  @override
  String get reviewWholeLesson => 'Whole lesson';

  @override
  String reviewStep(int number) {
    return 'Step $number';
  }

  @override
  String get reviewAddNote => 'Add a note';

  @override
  String get reviewNoteHint => 'What should change?';

  @override
  String get reviewSave => 'Save';

  @override
  String get reviewApprove => 'Approve';

  @override
  String reviewApproveConfirm(int version) {
    return 'Approve version $version? Children will get it the next time lessons are published.';
  }

  @override
  String get reviewOldVersion =>
      'This phone has a different version of this lesson. Update before reviewing.';

  @override
  String get reviewUpdate => 'Update lessons';

  @override
  String get reviewError =>
      'Couldn\'t reach the server. Check the internet and try again.';

  @override
  String reviewDecidedBy(String email) {
    return 'Decided by $email';
  }

  @override
  String inequalityUnreadable(int line) {
    return 'I couldn\'t read line $line. Write each line as an inequality, like 2x + 3 < 11.';
  }

  @override
  String inequalityBrokenStep(int line) {
    return 'Line $line changes the answer. Whatever you do to one side, do exactly the same to the other side.';
  }

  @override
  String inequalityWrongDirection(int line) {
    return 'Look at the sign in line $line. When you multiply or divide both sides by a negative number, the sign flips: < becomes >. Otherwise it stays the same.';
  }

  @override
  String inequalityNotFinished(String variable) {
    return 'Good so far! Keep going until one line says $variable < a number (or >, ≤, ≥).';
  }

  @override
  String get dotFilled => 'Filled';

  @override
  String get dotOpen => 'Open';

  @override
  String get halfPlaneUnreadable =>
      'Write one inequality with x and y, like y <= 2x + 1.';

  @override
  String get halfPlaneWrongLine =>
      'The boundary line is not right. Find two points on the line and check them.';

  @override
  String get halfPlaneWrongSide =>
      'The line is right, but the answer is on its other side. Test a point such as (0, 0).';

  @override
  String get halfPlaneWrongBoundary =>
      'Nearly! Is the line itself included? ≤ and ≥ include it (a solid line); < and > do not (a dashed line).';

  @override
  String get pointsUnreadable =>
      'Write the points like (2, 3), with commas between them.';

  @override
  String pointsWrongPoint(String point) {
    return '$point is not one of the corners. Check it in every inequality.';
  }

  @override
  String pointsMissing(int count) {
    String _temp0 = intl.Intl.pluralLogic(
      count,
      locale: localeName,
      other: 'Right so far, but $count corners are missing.',
      one: 'Right so far, but one corner is missing.',
    );
    return '$_temp0';
  }

  @override
  String get lineSolid => 'Solid';

  @override
  String get lineDashed => 'Dashed';

  @override
  String get shadeOtherSide => 'Other side';

  @override
  String get planeNoSide => 'Tap the side of the line to shade.';

  @override
  String get regionHint => 'Tap the corners of the shaded region.';

  @override
  String get regionClear => 'Clear';

  @override
  String get regionNoCorners => 'No corners marked yet.';

  @override
  String get classesButton => 'Classes';

  @override
  String classesTitle(String name) {
    return '$name\'s classes';
  }

  @override
  String get classesNone => 'Not in a class yet.';

  @override
  String get classCodeLabel => 'Class code from the teacher';

  @override
  String get findClass => 'Find class';

  @override
  String get classNotFound =>
      'No class has this code. Please check the code with the teacher.';

  @override
  String get classNoConnection =>
      'This needs internet. Please try again when you are online.';

  @override
  String classFound(String className) {
    return 'Class: $className';
  }

  @override
  String classConsent(String name) {
    return 'I agree that this class\'s teacher can see $name\'s first name, grade and progress in lessons. The name is never sent to AI. I can take $name out of the class at any time.';
  }

  @override
  String get joinClass => 'Join class';

  @override
  String get leaveClass => 'Leave';

  @override
  String leaveClassConfirm(String name, String className) {
    return 'Take $name out of $className? The teacher will no longer see $name\'s progress.';
  }

  @override
  String planAssigned(String title) {
    return 'From your teacher: $title';
  }

  @override
  String planDue(String date) {
    return 'By $date';
  }

  @override
  String get myClasses => 'My classes';

  @override
  String get newClass => 'New class';

  @override
  String get classNameLabel => 'Class name (for example: 9 A Maths)';

  @override
  String get createButton => 'Create';

  @override
  String get noClassesYet =>
      'No classes yet. Create one and give its code to the parents.';

  @override
  String classCode(String code) {
    return 'Code: $code';
  }

  @override
  String get classCodeHelp =>
      'Parents open Account in the app, tap the classes button next to their child, and type this code.';

  @override
  String get classMembers => 'Students';

  @override
  String get noMembersYet => 'No students yet.';

  @override
  String memberProgress(int mastered, int started) {
    return '$mastered of $started skills mastered';
  }

  @override
  String get classAssignments => 'Assigned lessons';

  @override
  String get assignLesson => 'Assign a lesson';

  @override
  String get noAssignments => 'No lessons assigned yet.';

  @override
  String assignmentDone(int done, int total) {
    return '$done of $total finished';
  }

  @override
  String get setDueDate => 'Set a due date';

  @override
  String get deleteClass => 'Delete class';

  @override
  String deleteClassConfirm(String className) {
    return 'Delete $className? Its code stops working and the students\' summaries are deleted.';
  }

  @override
  String get commonMistakes => 'Common mistakes';

  @override
  String mistakeStudents(String names) {
    return 'Made by: $names';
  }

  @override
  String get dashboardTitle => 'Teacher dashboard';

  @override
  String get dashboardSignIn =>
      'Sign in with your teacher account from the app.';

  @override
  String get createTeacherAccount => 'Create a teacher account';

  @override
  String get tabMastery => 'Mastery';

  @override
  String get tabMistakes => 'Mistakes';

  @override
  String get tabNeedsHelp => 'Needs help';

  @override
  String get tabLessons => 'Lessons';

  @override
  String get noMistakesYet => 'No mistakes recorded yet.';

  @override
  String get nobodyStuck => 'Nobody is stuck right now.';

  @override
  String lastTried(String day) {
    return 'Last tried $day';
  }

  @override
  String mistakeIn(String lesson) {
    return 'In: $lesson';
  }

  @override
  String finishedBy(String names) {
    return 'Finished: $names';
  }

  @override
  String notFinishedBy(String names) {
    return 'Not yet: $names';
  }

  @override
  String get reportButton => 'Report';

  @override
  String reportTitle(String name) {
    return '$name\'s week';
  }

  @override
  String get reportListen => 'Listen';

  @override
  String get reportStop => 'Stop';

  @override
  String get reportLearnedHeading => 'Learned';

  @override
  String get reportPracticeHeading => 'Practice';

  @override
  String get reportHomeHeading => 'At home';

  @override
  String get reportEffortHeading => 'Effort';

  @override
  String reportLearned(String name, String skills) {
    return 'This week $name learned: $skills.';
  }

  @override
  String reportLearnedNone(String name) {
    return '$name is still working towards the next skill. That is normal; understanding takes time.';
  }

  @override
  String reportWorkingOn(String skills) {
    return 'Working on: $skills.';
  }

  @override
  String reportNeedsHelp(String name, String skill) {
    return '$name finds $skill hard. Please sit with $name for a few minutes while they practise.';
  }

  @override
  String reportReview(String skill, String day) {
    return '$skill comes back for practice on $day.';
  }

  @override
  String get reportPracticeNone => 'Nothing needs extra practice right now.';

  @override
  String get reportHomeNone => 'No home activity this week.';

  @override
  String reportEffort(String name, int days, int questions) {
    return '$name practised on $days of the last 7 days and answered $questions questions.';
  }

  @override
  String get reportNoUrduVoice =>
      'This phone has no Urdu voice yet, so the report is read in English. To add Urdu: open the phone\'s Settings, search for \"Text-to-speech\", choose Google, then \"Install voice data\" and Urdu.';

  @override
  String get reportNoVoice =>
      'This phone can\'t read aloud. The pictures show the report.';

  @override
  String get reportMithuNote => 'Mithu\'s note';

  @override
  String get phoneCheckTitle => 'Phone check';

  @override
  String get phoneCheckRefresh => 'Check again';

  @override
  String get phoneCheckMemory => 'Memory used now';

  @override
  String get phoneCheckMemoryMost => 'Most memory used';

  @override
  String get phoneCheckPictures => 'Pictures in memory';

  @override
  String get phoneCheckSavedMedia => 'Saved videos';

  @override
  String get phoneCheckDownloadedLessons => 'Downloaded lessons';

  @override
  String get phoneCheckClearMedia => 'Remove saved videos';

  @override
  String get dataSaver => 'Data saver';

  @override
  String get dataSaverHelp =>
      'Videos download only on Wi-Fi, or when you tap Download.';

  @override
  String dataUsedThisWeek(String amount) {
    return 'Mobile data used in the last 7 days: $amount';
  }

  @override
  String get downloadsTitle => 'Downloads';

  @override
  String get downloadsHelp =>
      'Save a lesson\'s videos before going somewhere without signal. Saving uses data now, even with Data saver on.';

  @override
  String get downloadsNone =>
      'All videos are inside the app. There is nothing to download.';

  @override
  String downloadSaved(String size) {
    return 'Saved on this phone ($size)';
  }

  @override
  String get downloadNotSaved => 'Not saved';

  @override
  String get downloadSave => 'Download';

  @override
  String get downloadRemove => 'Remove from this phone';

  @override
  String get downloadFailed =>
      'Couldn\'t download. Check the internet and try again.';

  @override
  String get videoNeedsData =>
      'This video will download on Wi-Fi. Here is what it shows:';

  @override
  String get videoUseData => 'Watch now (uses mobile data)';

  @override
  String get phoneCheckDataWifi => 'Wi-Fi data, last 7 days';

  @override
  String get phoneCheckDataMobile => 'Mobile data, last 7 days';

  @override
  String get privacyTitle => 'Privacy note';

  @override
  String get privacyIntro =>
      'This note says what AI Tutor keeps about your child, where it is kept, who can see it and for how long.';

  @override
  String get privacyKeptTitle => 'What we keep';

  @override
  String get privacyKept =>
      'Your child\'s first name, class, picture and PIN (scrambled, so no one can read it), and their learning: lessons, answers, skills and badges. We never ask for a surname, an address, a phone number or a photo of your child.';

  @override
  String get privacyWhereTitle => 'Where it is kept';

  @override
  String get privacyWhere =>
      'On this phone, and in your account on Google\'s Firebase servers, so that progress is safe if the phone is lost or changed.';

  @override
  String get privacyAiTitle => 'Mithu\'s AI help';

  @override
  String get privacyAi =>
      'When your child types an explanation, or takes a photo of their working, it is sent to Claude, an AI made by the company Anthropic, which writes Mithu\'s feedback. Your child\'s name is never sent. Phone numbers, emails and addresses are removed before sending. Photos are not kept after they are read. Anthropic\'s rules say it does not use this to train its AI. You can turn AI help off in Settings; the app then checks answers by itself.';

  @override
  String get privacyWhoTitle => 'Who can see it';

  @override
  String get privacyWho =>
      'You. A teacher, only if you join your child to their class: they see your child\'s first name and progress in that class. The app\'s small team can read AI messages, without names, to keep children safe and fix mistakes. No one else, and nothing is sold or used for adverts.';

  @override
  String get privacyHowLongTitle => 'How long it is kept';

  @override
  String get privacyHowLong =>
      'Your child\'s profile and progress are kept until you delete them. AI messages are kept for 90 days for safety checks, then deleted. Daily counts of AI use (numbers only) are kept to watch costs.';

  @override
  String get privacySafetyTitle => 'Keeping children safe';

  @override
  String get privacySafety =>
      'If your child writes something that suggests they are upset or unsafe, Mithu kindly asks them to talk to a parent or teacher they trust, and the message is marked for the team to read.';

  @override
  String get privacyChoicesTitle => 'Your choices';

  @override
  String get privacyChoices =>
      'To remove a child and all their progress, tap the family button at the top of the home screen, then the bin next to the child. You can take a child out of a class at any time. You can turn AI help off in Settings.';

  @override
  String get privacyListen => 'Listen';

  @override
  String get privacyStop => 'Stop';

  @override
  String get aiHelpSetting => 'Mithu\'s AI help';

  @override
  String get aiHelpSettingHint =>
      'Sends typed explanations and photos of working to an AI for feedback, without names. When off, the app checks answers by itself.';

  @override
  String get photoAiOff =>
      'Mithu\'s AI help is off, so please type your answer instead.';

  @override
  String get learningTotalsTitle => 'Learning in the whole project';

  @override
  String learningTotalsRow(
    int students,
    int lessons,
    int finished,
    int questions,
    int firstTry,
    int aiCalls,
  ) {
    return '$students children · $lessons lessons ($finished finished) · $questions questions ($firstTry right first time) · $aiCalls AI checks';
  }

  @override
  String get phoneCheckCrashes => 'Crashes, last 7 days';

  @override
  String get privacyCrashTitle => 'Crash reports';

  @override
  String get privacyCrash =>
      'If the app crashes, a report goes to Google\'s Firebase Crashlytics so we can fix it. It has the phone model, the Android version and where in the app it crashed, never a name or an email. There is no advertising and no Google Analytics in the app.';

  @override
  String get navHome => 'Home';

  @override
  String get navLessons => 'Lessons';

  @override
  String get navBadges => 'Badges';

  @override
  String get badgesIntro =>
      'You earn badges for effort: finishing a lesson, trying again, explaining your thinking and coming back each day.';

  @override
  String get courseTitle => 'My course';

  @override
  String coursePercent(int percent) {
    return '$percent% done';
  }

  @override
  String courseLessonsDone(int done, int total) {
    return '$done of $total lessons done';
  }

  @override
  String get courseDoneMeans =>
      'Done means you finished the lesson. Review questions on later days help you remember it.';

  @override
  String get lessonNotStarted => 'Not started';

  @override
  String lessonAtStep(int step, int total) {
    return 'Step $step of $total';
  }

  @override
  String get otherLessons => 'Other lessons';

  @override
  String skillLevel(String level) {
    return 'Skill: $level';
  }
}

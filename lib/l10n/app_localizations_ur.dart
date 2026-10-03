// ignore: unused_import
import 'package:intl/intl.dart' as intl;

import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for Urdu (`ur`).
class AppLocalizationsUr extends AppLocalizations {
  AppLocalizationsUr([String locale = 'ur']) : super(locale);

  @override
  String get appTitle => 'اے آئی ٹیوٹر';

  @override
  String get homeWelcome => 'خوش آمدید! شروع کرنے کے لیے طالب علم شامل کریں۔';

  @override
  String get settingsTitle => 'ترتیبات';

  @override
  String get languageLabel => 'زبان';

  @override
  String get ageTierLabel => 'عمر کا گروپ (ڈویلپر کی ترتیب)';

  @override
  String get tierEarly => 'نرسری سے دوسری جماعت';

  @override
  String get tierPrimary => 'تیسری سے پانچویں جماعت';

  @override
  String get tierMiddle => 'چھٹی سے آٹھویں جماعت';

  @override
  String get tierOlder => 'نویں سے بارہویں جماعت';

  @override
  String get urduTestTitle => 'اردو متن کی جانچ';

  @override
  String get continueButton => 'آگے چلیں';

  @override
  String get checkButton => 'جانچیں';

  @override
  String get finishButton => 'ختم کریں';

  @override
  String get answerLabel => 'آپ کا جواب';

  @override
  String get hintLabel => 'اشارہ';

  @override
  String get tryAgain => 'ابھی نہیں۔ اشارہ دیکھیں اور دوبارہ کوشش کریں۔';

  @override
  String get typeANumber => 'براہِ کرم کوئی عدد لکھیں، جیسے 8 یا ۸۔';

  @override
  String stepNotSupported(String type) {
    return 'اس قسم کا مرحلہ ($type) ابھی نہیں چل سکتا۔ آگے بڑھنے کے لیے \"آگے چلیں\" دبائیں۔';
  }

  @override
  String stepProgress(int current, int total) {
    return 'مرحلہ $current از $total';
  }

  @override
  String get lessonLoadError => 'یہ سبق نہیں کھل سکا۔';

  @override
  String get lessonsPreviewTitle => 'اسباق (ڈویلپر پیش منظر)';

  @override
  String minutesShort(int count) {
    return '$count منٹ';
  }

  @override
  String get switchLanguage => 'زبان بدلیں';

  @override
  String get fractionUnreadable =>
      'کسر اس طرح لکھیں: 3/4، یا مخلوط عدد اس طرح: 1 1/2';

  @override
  String get fractionNotSimplest =>
      'قیمت بالکل درست ہے! اب اسے مختصر ترین شکل میں لکھیں: اوپر اور نیچے والے عدد کو ایک ہی عدد سے تقسیم کریں۔';

  @override
  String get chemUnreadable =>
      'یہ مساوات پڑھی نہیں جا سکی۔ اسے اس طرح لکھیں: 2H2 + O2 -> 2H2O';

  @override
  String chemUnknownElement(String symbol) {
    return '\"$symbol\" کسی عنصر کی علامت نہیں ہے۔ علامت بڑے حرف سے شروع ہوتی ہے اور دوسرا حرف چھوٹا ہوتا ہے: Co کوبالٹ ہے، لیکن CO کاربن اور آکسیجن ہیں۔';
  }

  @override
  String get chemWrongSubstances =>
      'مادّے دوبارہ دیکھیں۔ بالکل وہی مادّے لکھیں جو سوال میں ہیں، نہ کوئی زیادہ کریں نہ کوئی چھوڑیں۔';

  @override
  String chemChangedSubscript(String student, String expected) {
    return 'آپ نے $student لکھا۔ مساوات متوازن کرنے کے لیے صرف آگے والے بڑے عدد بدلیں۔ $expected کے اندر والے چھوٹے عدد ویسے ہی رہنے چاہئیں، ورنہ مادّہ ہی بدل جاتا ہے۔';
  }

  @override
  String chemUnbalanced(String element, int left, int right) {
    return '$element کے ایٹم گنیں: بائیں طرف $left اور دائیں طرف $right۔ کسی مادّے کے آگے والا عدد بدل کر انہیں برابر کریں۔';
  }

  @override
  String chemNotLowest(int divisor) {
    return 'مساوات متوازن ہے! لیکن آگے والے سب عدد $divisor سے تقسیم ہو سکتے ہیں۔ سب سے چھوٹے مکمل عدد استعمال کریں۔';
  }

  @override
  String linearUnreadable(int line) {
    return 'سطر $line پڑھی نہیں جا سکی۔ ہر سطر مساوات کی شکل میں لکھیں، جیسے 2x + 3 = 11';
  }

  @override
  String linearBrokenStep(int line) {
    return 'سطر $line میں ترازو کا توازن نہیں رہا۔ ایک طرف جو بھی کریں، دوسری طرف بھی بالکل وہی کریں۔';
  }

  @override
  String linearNotFinished(String variable) {
    return 'اب تک ٹھیک ہے! اس وقت تک جاری رکھیں جب تک کسی سطر میں $variable = کوئی عدد نہ آ جائے۔';
  }

  @override
  String get answerUnreadable =>
      'یہ جواب پڑھا نہیں جا سکا۔ براہِ کرم دوبارہ لکھیں۔';

  @override
  String get answerHintMultiline => 'ہر قدم نئی سطر میں لکھیں۔';

  @override
  String get checkedByCode => 'ایپ نے جانچا';

  @override
  String get whoIsLearning => 'کون پڑھ رہا ہے؟';

  @override
  String get addLearner => 'نیا طالب علم شامل کریں';

  @override
  String get firstNameLabel => 'پہلا نام';

  @override
  String get firstNameHelp => 'صرف پہلا نام لکھیں۔';

  @override
  String get gradeLabel => 'جماعت';

  @override
  String get gradeNursery => 'نرسری';

  @override
  String get gradePrep => 'پریپ';

  @override
  String gradeNumber(int grade) {
    return 'جماعت $grade';
  }

  @override
  String get pictureLabel => 'تصویر چنیں';

  @override
  String get pinOptionalLabel => 'پن (اختیاری، 4 ہندسے)';

  @override
  String get pinHelp => 'پن سے بہن بھائی یہ پروفائل نہیں کھول سکیں گے۔';

  @override
  String get pinTooShort => 'پن میں 4 ہندسے ہوتے ہیں۔';

  @override
  String get consentLabel =>
      'میں اس بچے کا والد، والدہ یا سرپرست ہوں، اور اس کا پہلا نام، جماعت اور پیش رفت محفوظ کرنے کی اجازت دیتا ہوں۔';

  @override
  String get saveButton => 'محفوظ کریں';

  @override
  String get cancelButton => 'منسوخ کریں';

  @override
  String get enterPin => 'اپنا پن لکھیں';

  @override
  String get wrongPin => 'یہ پن درست نہیں۔ دوبارہ کوشش کریں۔';

  @override
  String helloName(String name) {
    return 'السلام علیکم، $name!';
  }

  @override
  String get switchLearner => 'طالب علم بدلیں';

  @override
  String get lessonsTitle => 'آپ کے سبق';

  @override
  String get noLessonsYet => 'نئے سبق جلد آ رہے ہیں۔';

  @override
  String get lessonStart => 'شروع کریں';

  @override
  String lessonContinue(int step, int total) {
    return 'مرحلہ $step از $total سے جاری رکھیں';
  }

  @override
  String get lessonDone => 'مکمل';

  @override
  String get offlineStatus => 'آف لائن: آپ کا کام اس فون پر محفوظ ہے';

  @override
  String waitingToSync(int count) {
    return 'آن لائن جانے کے منتظر جوابات: $count';
  }

  @override
  String get accountTitle => 'والدین اور اساتذہ کا اکاؤنٹ';

  @override
  String get accountPhoneOnly =>
      'طلبہ کا کام آن لائن محفوظ ہوتا ہے۔ سائن اِن کریں یا اکاؤنٹ بنائیں تاکہ نئے فون پر بھی یہ واپس مل سکے۔';

  @override
  String signedInAs(String email) {
    return '$email کے طور پر سائن اِن ہیں';
  }

  @override
  String get emailLabel => 'ای میل';

  @override
  String get passwordLabel => 'پاس ورڈ (کم از کم 6 حروف)';

  @override
  String get roleParent => 'والدین';

  @override
  String get roleTeacher => 'استاد';

  @override
  String get createAccount => 'اکاؤنٹ بنائیں';

  @override
  String get signIn => 'سائن اِن';

  @override
  String get signOut => 'سائن آؤٹ';

  @override
  String get signOutConfirm =>
      'سائن آؤٹ کر کے طلبہ کو اس فون سے ہٹا دیں؟ ان کا کام آپ کے اکاؤنٹ میں محفوظ رہے گا۔';

  @override
  String signOutUnsynced(int count) {
    return '$count جوابات ابھی آن لائن نہیں گئے، اور ابھی سائن آؤٹ کرنے سے ضائع ہو جائیں گے۔';
  }

  @override
  String get authWrongPassword => 'ای میل یا پاس ورڈ درست نہیں۔';

  @override
  String get authEmailInUse =>
      'اس ای میل کا اکاؤنٹ پہلے سے موجود ہے۔ سائن اِن کریں۔';

  @override
  String get authWeakPassword => 'کم از کم 6 حروف استعمال کریں۔';

  @override
  String get authInvalidEmail => 'ای میل ایڈریس چیک کریں۔';

  @override
  String get authNoConnection =>
      'انٹرنیٹ نہیں ہے۔ آن لائن ہونے پر دوبارہ کوشش کریں۔';

  @override
  String get authOther => 'کچھ غلط ہو گیا۔ دوبارہ کوشش کریں۔';

  @override
  String get teacherToolsSoon =>
      'اساتذہ کے ٹولز (کلاسیں اور ہوم ورک) جلد آ رہے ہیں۔';

  @override
  String get learnersTitle => 'اس فون پر طلبہ';

  @override
  String get removeLearner => 'طالب علم ہٹائیں';

  @override
  String removeLearnerConfirm(String name) {
    return '$name اور ان کی تمام پیش رفت ہٹا دیں؟';
  }

  @override
  String get removeButton => 'ہٹائیں';

  @override
  String get todaysPlan => 'آج کا منصوبہ';

  @override
  String planMinutes(int minutes) {
    return 'تقریباً $minutes منٹ';
  }

  @override
  String planReview(String title) {
    return 'دہرائی: $title';
  }

  @override
  String planPractice(String title) {
    return 'مشق: $title';
  }

  @override
  String get planMixed => 'ملا جلا سوال';

  @override
  String get planExplain => 'وضاحت کریں یا غلطی ڈھونڈیں';

  @override
  String planLesson(String title) {
    return 'سبق: $title';
  }

  @override
  String get planHomeTask => 'گھر پر کرنے کا کام';

  @override
  String planFlashcards(String title) {
    return 'فلیش کارڈ: $title';
  }

  @override
  String get startPractice => 'مشق شروع کریں';

  @override
  String get planAllDone => 'آج کا کام مکمل۔ شاباش!';

  @override
  String get markDone => 'ہو گیا';

  @override
  String get flashcardsTitle => 'فلیش کارڈ';

  @override
  String get flashcardTapToTurn => 'کارڈ پلٹنے کے لیے اس پر ٹیپ کریں۔';

  @override
  String get nextCard => 'اگلا کارڈ';

  @override
  String get homeTaskTitle => 'گھر کا کام';

  @override
  String get practiceTitle => 'مشق';

  @override
  String practiceDone(int right, int total) {
    return 'شاباش! $total میں سے $right پہلی کوشش میں درست۔';
  }

  @override
  String get levelNotStarted => 'شروع نہیں ہوا';

  @override
  String get levelLearning => 'سیکھ رہے ہیں';

  @override
  String get levelPractising => 'مشق جاری ہے';

  @override
  String get levelMastered => 'سیکھ لیا';

  @override
  String get levelSecure => 'پکا یاد ہے';

  @override
  String get tryAnotherWay => 'آئیے اسے دوسرے طریقے سے دیکھتے ہیں۔';

  @override
  String stuckPrerequisite(String title) {
    return 'پہلے ایک پچھلا خیال دوبارہ دیکھتے ہیں: $title';
  }

  @override
  String get openLesson => 'وہ سبق کھولیں';

  @override
  String get keepGoing => 'جاری رکھیں';

  @override
  String get stuckBreak =>
      'یہ مشکل ہے۔ تھوڑا سا وقفہ مدد کر سکتا ہے۔ آپ کا کام محفوظ ہے۔';

  @override
  String get stuckHelp =>
      'یہ مشکل ہے۔ والدین یا استاد سے کہیں کہ آپ کے ساتھ اسے دیکھیں۔ آپ کا کام محفوظ ہے۔';

  @override
  String get takeBreak => 'وقفہ لیں';

  @override
  String needsHelpWith(String topics) {
    return 'ان میں مدد چاہیے: $topics';
  }

  @override
  String get simNoResult => 'سرگرمی مکمل کریں، پھر \"جانچیں\" دبائیں۔';

  @override
  String get simUseActivity =>
      'سرگرمی کر کے دیکھیں، پھر اس کا \"جانچیں\" بٹن دبائیں۔';

  @override
  String get simCouldNotStart =>
      'یہ سرگرمی اس فون پر شروع نہیں ہو سکی۔ آئیں آگے چلیں۔';

  @override
  String get simUndo => 'واپس';

  @override
  String get fractionBarsCut => 'ہر ایک میں کتنے ٹکڑے';

  @override
  String fractionBarsChosen(int count) {
    return 'چُنے گئے ٹکڑے: $count';
  }

  @override
  String get scaleTakeOne => '1 ہٹائیں';

  @override
  String get scaleTakeX => 'x ہٹائیں';

  @override
  String get scaleLeft => 'بائیں طرف';

  @override
  String get scaleRight => 'دائیں طرف';

  @override
  String get scaleBalanced => 'برابر';

  @override
  String get scaleTipped => 'برابر نہیں!';

  @override
  String scaleShare(int n) {
    return '$n برابر حصوں میں بانٹیں';
  }

  @override
  String get atomsLeft => 'بائیں';

  @override
  String get atomsRight => 'دائیں';

  @override
  String get atomsBalanced => 'ہر عنصر برابر ہے!';

  @override
  String numberLineValue(String value) {
    return 'آپ کا عدد: $value';
  }

  @override
  String get graphHint =>
      'کسی نقطے کو کھینچیں، یا A یا B چُن کر تیر استعمال کریں۔';

  @override
  String get videoCouldNotPlay =>
      'ویڈیو ابھی نہیں چل سکتی۔ اس میں یہ دکھایا گیا ہے:';

  @override
  String get videoPlay => 'چلائیں';

  @override
  String get videoPause => 'روکیں';

  @override
  String get videoReplay => 'دوبارہ دیکھیں';

  @override
  String get videoCaptions => 'سب ٹائٹل';

  @override
  String get lessMotion => 'کم حرکت';

  @override
  String get lessMotionHint =>
      'کم اینیمیشن۔ کچھ بچے بہتر توجہ دیتے ہیں، اور بیٹری بچتی ہے۔';

  @override
  String get lessonFinished => 'سبق مکمل! شاباش۔';

  @override
  String levelUp(String topic, String level) {
    return '$topic: $level!';
  }

  @override
  String get simGalleryTitle => 'سمولیشنز (ڈویلپر)';

  @override
  String get aiThinking => 'مٹھو آپ کا جواب پڑھ رہا ہے…';

  @override
  String get checkedByAi => 'اے آئی نے جانچا';

  @override
  String get checkedByKeywords => 'اہم الفاظ سے جانچا';

  @override
  String get aiQueued =>
      'ابھی انٹرنیٹ نہیں ہے۔ مٹھو بعد میں آپ کا جواب دیکھے گا۔';

  @override
  String get aiLimitReached =>
      'مٹھو آج بہت مدد کر چکا ہے، اس لیے اس جواب کو ایپ نے جانچا۔';

  @override
  String get improveAnswer => 'اپنا جواب بہتر کریں';

  @override
  String get explainInputHelp => 'انگریزی، اردو یا رومن اردو میں لکھیں۔';

  @override
  String get levelGotIt => 'سمجھ گئے!';

  @override
  String get levelPartly => 'کچھ حد تک';

  @override
  String get levelNotYet => 'ابھی نہیں';

  @override
  String get photoTake => 'تصویر لیں';

  @override
  String get photoChoose => 'تصویر منتخب کریں';

  @override
  String get photoTypeInstead => 'اس کے بجائے جواب لکھیں';

  @override
  String get photoReading => 'مٹھو آپ کا حل پڑھ رہا ہے…';

  @override
  String get photoConfirm =>
      'مٹھو نے یہ پڑھا۔ جو غلط پڑھا گیا ہو اسے ٹھیک کریں، پھر جانچیں دبائیں۔';

  @override
  String get photoUnreadable =>
      'مٹھو یہ تصویر نہیں پڑھ سکا۔ اچھی روشنی میں دوبارہ کوشش کریں، یا اپنا جواب لکھیں۔';

  @override
  String get photoOffline =>
      'تصویر کے لیے انٹرنیٹ چاہیے۔ اس کے بجائے اپنا حل لکھیں۔';

  @override
  String get photoLimit =>
      'مٹھو آج کافی تصویریں پڑھ چکا ہے۔ اس کے بجائے اپنا حل لکھیں۔';

  @override
  String get photoWorkingLabel => 'آپ کا حل (ہر قدم الگ لائن پر)';

  @override
  String get readByAi => 'اے آئی نے پڑھا';

  @override
  String get explainedByAi => 'اے آئی نے سمجھایا';

  @override
  String get photoExplaining => 'مٹھو دیکھ رہا ہے کہ غلطی کہاں ہوئی…';

  @override
  String get tryAgainButton => 'دوبارہ کوشش کریں';

  @override
  String get mithuNotesTitle => 'مٹھو کے نوٹس';

  @override
  String mithuNotesNew(int count) {
    return 'مٹھو کے آپ کے لیے نئے نوٹس ($count)';
  }

  @override
  String get mithuNotesWaiting => 'مٹھو کا انتظار ہے';

  @override
  String get mithuNotesFailed => 'مٹھو اسے نہیں دیکھ سکا۔';

  @override
  String get mithuNotesEmpty => 'ابھی کوئی نوٹ نہیں۔';

  @override
  String get weeklyReport => 'ہفتہ وار رپورٹ';

  @override
  String get weeklyReportNone =>
      'ابھی کوئی رپورٹ نہیں۔ رپورٹ اتوار کی شام ان بچوں کے لیے لکھی جاتی ہے جنہوں نے اس ہفتے مشق کی۔';

  @override
  String weeklyReportStats(int days, int lessons, int questions) {
    return 'مشق کے $days دن · $lessons سبق مکمل · $questions سوالوں کے جواب';
  }

  @override
  String get needsInternet => 'انٹرنیٹ سے جڑیں اور دوبارہ کوشش کریں۔';

  @override
  String get aiCostsTitle => 'اے آئی کا استعمال اور خرچ';

  @override
  String get aiCostsAll => 'پروجیکٹ کے تمام طلبہ';

  @override
  String get aiCostsMine => 'اس اکاؤنٹ کے طلبہ';

  @override
  String aiCostsTotal(String cost) {
    return 'پچھلے 7 دن: $cost';
  }

  @override
  String aiCostsRow(int calls, int text, int photo, String cost) {
    return '$calls بار · $text تحریر · $photo تصاویر · $cost';
  }

  @override
  String get aiCostsEmpty => 'پچھلے 7 دنوں میں اے آئی استعمال نہیں ہوا۔';

  @override
  String get listenToMithu => 'مٹھو کو سنیں';

  @override
  String get phoneVoiceLabel => 'فون کی آواز (ابھی ریکارڈنگ نہیں)';

  @override
  String get recorderTitle => 'مٹھو کی آواز ریکارڈ کریں';

  @override
  String get recorderHelp =>
      'خاموش کمرہ چنیں۔ فون منہ سے ایک ہاتھ دور رکھیں، ریکارڈ دبائیں، جملہ پیار سے پڑھیں اور روکیں دبائیں۔ ہر جملہ 30 سیکنڈ سے کم رکھیں۔';

  @override
  String get recorderMissingOnly => 'صرف بغیر آواز والے جملے';

  @override
  String get recorderRecord => 'ریکارڈ';

  @override
  String get recorderStop => 'روکیں';

  @override
  String get recorderPlay => 'سنیں';

  @override
  String get recorderDelete => 'مٹائیں';

  @override
  String get recorderStatusPhone => 'اس فون پر ریکارڈ ہوا (ابھی بھیجا نہیں)';

  @override
  String get recorderStatusApp => 'آواز ایپ میں ہے';

  @override
  String get recorderStatusMissing => 'ابھی آواز نہیں';

  @override
  String get recorderTooLong =>
      '30 سیکنڈ سے لمبا ہے: براہ کرم چھوٹا ریکارڈ کریں۔';

  @override
  String get recorderNoMic =>
      'ایپ کو مائیکروفون کی اجازت نہیں۔ فون کی سیٹنگز میں اجازت دیں۔';

  @override
  String get recorderExport => 'ریکارڈنگز بھیجیں';

  @override
  String get recorderExportHelp =>
      'انہیں خود کو بھیجیں (مثلاً گوگل ڈرائیو پر)، پھر تمام فائلیں پروجیکٹ چیٹ میں لگائیں۔ Claude انہیں ایپ میں شامل کر دے گا۔';

  @override
  String get recorderNothingToSend => 'اس فون پر ابھی کوئی ریکارڈنگ نہیں۔';
}

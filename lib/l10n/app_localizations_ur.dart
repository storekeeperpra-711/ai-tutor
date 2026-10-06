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
      'میں اس بچے کا والد، والدہ یا سرپرست ہوں۔ میں نے رازداری کا نوٹ پڑھ لیا ہے، اور اس کا پہلا نام، جماعت اور پیش رفت محفوظ کرنے اور مٹھو کی اے آئی مدد کی اجازت دیتا ہوں۔';

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
  String get allSubjects => 'سب';

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

  @override
  String get soundsSetting => 'آوازیں';

  @override
  String get soundsSettingHint => 'ٹیپ اور جوابات کے لیے چھوٹی آوازیں';

  @override
  String get mithuSetting => 'مٹھو دکھائیں';

  @override
  String get mithuSettingHint => 'مٹھو طوطا اسباق میں مدد کرتا ہے';

  @override
  String get badgeFirstLesson => 'پہلا سبق مکمل';

  @override
  String get badgeTriedAgain => 'غلطی کے بعد دوبارہ کوشش کی';

  @override
  String get badgeExplained => 'اپنے الفاظ میں سمجھایا';

  @override
  String get badgeCheckedPhoto => 'تصویر کی جانچ کے بعد اپنا کام درست کیا';

  @override
  String get badgeCameBack => 'دہرائی کے لیے واپس آئے';

  @override
  String get badgeFiveDays => 'اس مہینے 5 مختلف دن پڑھا';

  @override
  String get badgesTitle => 'آپ کے بیجز';

  @override
  String badgesEarned(int count, int total) {
    return '$total میں سے $count بیجز';
  }

  @override
  String get starFinished => 'آپ نے مکمل کیا';

  @override
  String get starKeptTrying => 'آپ کوشش کرتے رہے';

  @override
  String get starExplained => 'آپ نے اپنی سوچ سمجھائی';

  @override
  String get praise1 => 'شاباش! آپ کی محنت رنگ لا رہی ہے۔';

  @override
  String get praise2 => 'زبردست کوشش! مٹھو کو آپ پر فخر ہے۔';

  @override
  String get praise3 => 'آپ نے کر دکھایا! غلطیاں ہمیں سکھاتی ہیں۔';

  @override
  String nextLesson(String title) {
    return 'اگلا: $title';
  }

  @override
  String get comeBackTomorrow => 'کل ایک چھوٹی سی دہرائی کے لیے واپس آئیں۔';

  @override
  String get backHome => 'ہوم';

  @override
  String earlyGreeting(String name) {
    return 'السلام علیکم $name! آئیں کھیلیں اور سیکھیں۔';
  }

  @override
  String get playButton => 'کھیلیں';

  @override
  String get mithuTip1 => 'مشورہ: اگر اٹک جائیں تو سوال دوبارہ آہستہ پڑھیں۔';

  @override
  String get mithuTip2 =>
      'مشورہ: غلطیوں سے ہمارا دماغ بڑھتا ہے۔ دوبارہ کوشش کریں!';

  @override
  String get mithuTip3 => 'مشورہ: اپنا جواب گھر میں کسی کو سمجھائیں۔';

  @override
  String questTitle(String subject) {
    return '$subject کی مہم';
  }

  @override
  String questProgress(int done, int total) {
    return '$total میں سے $done اسباق مکمل';
  }

  @override
  String get questDone => 'مہم مکمل! مضبوط رہنے کے لیے دہرائی کرتے رہیں۔';

  @override
  String secureSkills(int count, int total) {
    return '$total میں سے $count مہارتیں پکی';
  }

  @override
  String subjectLevel(int level) {
    return 'لیول $level';
  }

  @override
  String get subjectsTitle => 'آپ کے مضامین';

  @override
  String get masteryBySubject => 'مضمون کے لحاظ سے مہارت';

  @override
  String masteredSkills(int count, int total) {
    return '$total میں سے $count مہارتیں حاصل';
  }

  @override
  String examCountdown(int days) {
    String _temp0 = intl.Intl.pluralLogic(
      days,
      locale: localeName,
      other: 'بورڈ امتحان میں $days دن',
      one: 'بورڈ امتحان میں 1 دن',
    );
    return '$_temp0';
  }

  @override
  String get examToday =>
      'آپ کا بورڈ امتحان آج ہے۔ آپ نے اچھی تیاری کی ہے۔ کامیابی ہو!';

  @override
  String get examSetPrompt =>
      'الٹی گنتی دیکھنے کے لیے اپنے بورڈ امتحان کی تاریخ لکھیں';

  @override
  String get examDateSetting => 'بورڈ امتحان کی تاریخ';

  @override
  String get examDateNotSet => 'طے نہیں';

  @override
  String get examDateClear => 'ہٹائیں';

  @override
  String get subjectMaths => 'ریاضی';

  @override
  String get subjectChemistry => 'کیمسٹری';

  @override
  String get subjectPhysics => 'فزکس';

  @override
  String get subjectBiology => 'حیاتیات';

  @override
  String get subjectScience => 'سائنس';

  @override
  String get subjectEnglish => 'انگریزی';

  @override
  String get subjectUrdu => 'اردو';

  @override
  String get reviewTitle => 'اسباق کا جائزہ';

  @override
  String get reviewSignIn =>
      'اسباق کا جائزہ لینے کے لیے اپنے استاد اکاؤنٹ سے سائن ان کریں۔';

  @override
  String get reviewSignInButton => 'سائن ان کریں';

  @override
  String reviewVerify(String email) {
    return 'پہلے ہم تصدیق کریں گے کہ $email آپ کی ای میل ہے۔ بٹن دبائیں، پھر ای میل میں آنے والا لنک کھولیں۔';
  }

  @override
  String get reviewSendLink => 'مجھے لنک ای میل کریں';

  @override
  String get reviewLinkSent =>
      'بھیج دیا گیا۔ اپنا ان باکس اور اسپام فولڈر دیکھیں۔';

  @override
  String get reviewCheckAgain => 'میں نے لنک کھول لیا';

  @override
  String reviewNotReviewer(String email) {
    return '$email ابھی اسباق کا جائزہ نہیں لے سکتا۔ ایپ کے مالک سے کہیں کہ اسے شامل کریں۔';
  }

  @override
  String get reviewNothing => 'جائزے کے لیے کوئی سبق نہیں۔';

  @override
  String get reviewStatusInReview => 'جائزے کا منتظر';

  @override
  String get reviewStatusApproved => 'منظور شدہ';

  @override
  String get reviewStatusChanges => 'تبدیلی درکار';

  @override
  String reviewVersion(int version) {
    return 'ورژن $version';
  }

  @override
  String get reviewPlay => 'سبق چلائیں';

  @override
  String get reviewPlayHint =>
      'اسے بچے کی طرح چلائیں۔ کسی بھی مرحلے پر نوٹ کا بٹن دبا کر لکھیں کہ کیا بدلنا چاہیے۔';

  @override
  String get reviewWholeLesson => 'پورا سبق';

  @override
  String reviewStep(int number) {
    return 'مرحلہ $number';
  }

  @override
  String get reviewAddNote => 'نوٹ لکھیں';

  @override
  String get reviewNoteHint => 'کیا بدلنا چاہیے؟';

  @override
  String get reviewSave => 'محفوظ کریں';

  @override
  String get reviewApprove => 'منظور کریں';

  @override
  String reviewApproveConfirm(int version) {
    return 'ورژن $version منظور کریں؟ اگلی بار اسباق شائع ہونے پر یہ بچوں تک پہنچ جائے گا۔';
  }

  @override
  String get reviewOldVersion =>
      'اس فون پر اس سبق کا دوسرا ورژن ہے۔ جائزے سے پہلے اپ ڈیٹ کریں۔';

  @override
  String get reviewUpdate => 'اسباق اپ ڈیٹ کریں';

  @override
  String get reviewError =>
      'سرور سے رابطہ نہیں ہو سکا۔ انٹرنیٹ دیکھ کر دوبارہ کوشش کریں۔';

  @override
  String reviewDecidedBy(String email) {
    return 'فیصلہ: $email';
  }

  @override
  String inequalityUnreadable(int line) {
    return 'سطر $line پڑھی نہیں جا سکی۔ ہر سطر نامساوات کی شکل میں لکھیں، جیسے 2x + 3 < 11';
  }

  @override
  String inequalityBrokenStep(int line) {
    return 'سطر $line سے جواب بدل گیا۔ ایک طرف جو بھی کریں، دوسری طرف بھی بالکل وہی کریں۔';
  }

  @override
  String inequalityWrongDirection(int line) {
    return 'سطر $line میں علامت دیکھیں۔ جب دونوں طرف کو منفی عدد سے ضرب یا تقسیم کریں تو علامت الٹ جاتی ہے: < بن جاتا ہے >۔ ورنہ وہی رہتی ہے۔';
  }

  @override
  String inequalityNotFinished(String variable) {
    return 'اب تک ٹھیک ہے! اس وقت تک جاری رکھیں جب تک کسی سطر میں $variable < کوئی عدد (یا >، ≤، ≥) نہ آ جائے۔';
  }

  @override
  String get dotFilled => 'بھرا ہوا';

  @override
  String get dotOpen => 'خالی';

  @override
  String get halfPlaneUnreadable =>
      'x اور y کے ساتھ ایک نامساوات لکھیں، جیسے y <= 2x + 1';

  @override
  String get halfPlaneWrongLine =>
      'حدی خط درست نہیں۔ خط پر دو نقطے ڈھونڈیں اور انہیں جانچیں۔';

  @override
  String get halfPlaneWrongSide =>
      'خط درست ہے، مگر جواب اس کی دوسری طرف ہے۔ کوئی نقطہ جیسے (0, 0) آزمائیں۔';

  @override
  String get halfPlaneWrongBoundary =>
      'تقریباً! کیا خط خود شامل ہے؟ ≤ اور ≥ میں شامل ہے (سیدھی لکیر)؛ < اور > میں نہیں (ٹوٹی لکیر)۔';

  @override
  String get pointsUnreadable =>
      'نقطے (2, 3) کی طرح لکھیں، ان کے درمیان کاما لگائیں۔';

  @override
  String pointsWrongPoint(String point) {
    return '$point کونوں میں سے نہیں۔ اسے ہر نامساوات میں جانچیں۔';
  }

  @override
  String pointsMissing(int count) {
    String _temp0 = intl.Intl.pluralLogic(
      count,
      locale: localeName,
      other: 'اب تک درست، مگر $count کونے رہ گئے ہیں۔',
      one: 'اب تک درست، مگر ایک کونا رہ گیا ہے۔',
    );
    return '$_temp0';
  }

  @override
  String get lineSolid => 'سیدھی';

  @override
  String get lineDashed => 'ٹوٹی';

  @override
  String get shadeOtherSide => 'دوسری طرف';

  @override
  String get planeNoSide => 'خط کی وہ طرف ٹیپ کریں جسے رنگنا ہے۔';

  @override
  String get regionHint => 'رنگے ہوئے حصے کے کونوں پر ٹیپ کریں۔';

  @override
  String get regionClear => 'مٹائیں';

  @override
  String get regionNoCorners => 'ابھی کوئی کونا نہیں چنا۔';

  @override
  String get classesButton => 'کلاسیں';

  @override
  String classesTitle(String name) {
    return '$name کی کلاسیں';
  }

  @override
  String get classesNone => 'ابھی کسی کلاس میں نہیں۔';

  @override
  String get classCodeLabel => 'استاد کا دیا ہوا کلاس کوڈ';

  @override
  String get findClass => 'کلاس تلاش کریں';

  @override
  String get classNotFound =>
      'اس کوڈ کی کوئی کلاس نہیں ملی۔ براہِ کرم استاد سے کوڈ دوبارہ پوچھیں۔';

  @override
  String get classNoConnection =>
      'اس کے لیے انٹرنیٹ چاہیے۔ انٹرنیٹ ملنے پر دوبارہ کوشش کریں۔';

  @override
  String classFound(String className) {
    return 'کلاس: $className';
  }

  @override
  String classConsent(String name) {
    return 'میں اجازت دیتا/دیتی ہوں کہ اس کلاس کا استاد $name کا پہلا نام، جماعت اور اسباق میں ترقی دیکھ سکے۔ نام کبھی AI کو نہیں بھیجا جاتا۔ میں جب چاہوں $name کو کلاس سے نکال سکتا/سکتی ہوں۔';
  }

  @override
  String get joinClass => 'کلاس میں شامل کریں';

  @override
  String get leaveClass => 'چھوڑیں';

  @override
  String leaveClassConfirm(String name, String className) {
    return '$name کو $className سے نکالیں؟ اس کے بعد استاد $name کی ترقی نہیں دیکھ سکے گا۔';
  }

  @override
  String planAssigned(String title) {
    return 'استاد کی طرف سے: $title';
  }

  @override
  String planDue(String date) {
    return '$date تک';
  }

  @override
  String get myClasses => 'میری کلاسیں';

  @override
  String get newClass => 'نئی کلاس';

  @override
  String get classNameLabel => 'کلاس کا نام (مثلاً: 9 A ریاضی)';

  @override
  String get createButton => 'بنائیں';

  @override
  String get noClassesYet =>
      'ابھی کوئی کلاس نہیں۔ ایک کلاس بنائیں اور اس کا کوڈ والدین کو دیں۔';

  @override
  String classCode(String code) {
    return 'کوڈ: $code';
  }

  @override
  String get classCodeHelp =>
      'والدین ایپ میں اکاؤنٹ کھولیں، اپنے بچے کے ساتھ کلاسوں والا بٹن دبائیں، اور یہ کوڈ لکھیں۔';

  @override
  String get classMembers => 'طلبہ';

  @override
  String get noMembersYet => 'ابھی کوئی طالب علم نہیں۔';

  @override
  String memberProgress(int mastered, int started) {
    return '$started میں سے $mastered مہارتیں پکی';
  }

  @override
  String get classAssignments => 'دیے گئے اسباق';

  @override
  String get assignLesson => 'سبق دیں';

  @override
  String get noAssignments => 'ابھی کوئی سبق نہیں دیا گیا۔';

  @override
  String assignmentDone(int done, int total) {
    return '$total میں سے $done نے مکمل کیا';
  }

  @override
  String get setDueDate => 'آخری تاریخ مقرر کریں';

  @override
  String get deleteClass => 'کلاس ختم کریں';

  @override
  String deleteClassConfirm(String className) {
    return '$className ختم کریں؟ اس کا کوڈ کام نہیں کرے گا اور طلبہ کی معلومات مٹ جائیں گی۔';
  }

  @override
  String get commonMistakes => 'عام غلطیاں';

  @override
  String mistakeStudents(String names) {
    return 'جنہوں نے کی: $names';
  }

  @override
  String get dashboardTitle => 'اساتذہ کا ڈیش بورڈ';

  @override
  String get dashboardSignIn => 'ایپ والے اپنے استاد اکاؤنٹ سے سائن اِن کریں۔';

  @override
  String get createTeacherAccount => 'استاد اکاؤنٹ بنائیں';

  @override
  String get tabMastery => 'مہارت';

  @override
  String get tabMistakes => 'غلطیاں';

  @override
  String get tabNeedsHelp => 'مدد چاہیے';

  @override
  String get tabLessons => 'اسباق';

  @override
  String get noMistakesYet => 'ابھی کوئی غلطی درج نہیں ہوئی۔';

  @override
  String get nobodyStuck => 'اس وقت کوئی نہیں اٹکا۔';

  @override
  String lastTried(String day) {
    return 'آخری کوشش $day';
  }

  @override
  String mistakeIn(String lesson) {
    return 'سبق: $lesson';
  }

  @override
  String finishedBy(String names) {
    return 'مکمل کیا: $names';
  }

  @override
  String notFinishedBy(String names) {
    return 'ابھی نہیں: $names';
  }

  @override
  String get reportButton => 'رپورٹ';

  @override
  String reportTitle(String name) {
    return '$name کا ہفتہ';
  }

  @override
  String get reportListen => 'سنیں';

  @override
  String get reportStop => 'روکیں';

  @override
  String get reportLearnedHeading => 'سیکھا';

  @override
  String get reportPracticeHeading => 'مشق';

  @override
  String get reportHomeHeading => 'گھر پر';

  @override
  String get reportEffortHeading => 'محنت';

  @override
  String reportLearned(String name, String skills) {
    return 'اس ہفتے $name نے سیکھا: $skills۔';
  }

  @override
  String reportLearnedNone(String name) {
    return '$name کی اگلی مہارت پر محنت جاری ہے۔ یہ معمول کی بات ہے؛ سمجھنے میں وقت لگتا ہے۔';
  }

  @override
  String reportWorkingOn(String skills) {
    return 'ابھی اس پر کام جاری ہے: $skills۔';
  }

  @override
  String reportNeedsHelp(String name, String skill) {
    return '$name کو $skill مشکل لگ رہا ہے۔ مشق کے وقت چند منٹ $name کے ساتھ بیٹھیں۔';
  }

  @override
  String reportReview(String skill, String day) {
    return '$skill کی مشق $day کو دوبارہ آئے گی۔';
  }

  @override
  String get reportPracticeNone => 'اس وقت کسی چیز کی اضافی مشق کی ضرورت نہیں۔';

  @override
  String get reportHomeNone => 'اس ہفتے گھر کی کوئی سرگرمی نہیں۔';

  @override
  String reportEffort(String name, int days, int questions) {
    return '$name نے پچھلے 7 دنوں میں سے $days دن مشق کی اور $questions سوالوں کے جواب دیے۔';
  }

  @override
  String get reportNoUrduVoice =>
      'اس فون میں ابھی اردو آواز نہیں، اس لیے رپورٹ انگریزی میں پڑھی جائے گی۔ اردو شامل کرنے کے لیے: فون کی سیٹنگز کھولیں، \"Text-to-speech\" تلاش کریں، Google چنیں، پھر \"Install voice data\" اور Urdu۔';

  @override
  String get reportNoVoice =>
      'یہ فون بول کر نہیں پڑھ سکتا۔ تصویریں رپورٹ دکھاتی ہیں۔';

  @override
  String get reportMithuNote => 'مٹھو کا پیغام';

  @override
  String get phoneCheckTitle => 'فون کی جانچ';

  @override
  String get phoneCheckRefresh => 'دوبارہ جانچیں';

  @override
  String get phoneCheckMemory => 'اس وقت استعمال ہونے والی میموری';

  @override
  String get phoneCheckMemoryMost => 'سب سے زیادہ استعمال ہونے والی میموری';

  @override
  String get phoneCheckPictures => 'میموری میں تصویریں';

  @override
  String get phoneCheckSavedMedia => 'محفوظ ویڈیوز';

  @override
  String get phoneCheckDownloadedLessons => 'ڈاؤن لوڈ کیے گئے اسباق';

  @override
  String get phoneCheckClearMedia => 'محفوظ ویڈیوز ہٹائیں';

  @override
  String get dataSaver => 'ڈیٹا کی بچت';

  @override
  String get dataSaverHelp =>
      'ویڈیوز صرف وائی فائی پر، یا ڈاؤن لوڈ دبانے پر ڈاؤن لوڈ ہوں گی۔';

  @override
  String dataUsedThisWeek(String amount) {
    return 'پچھلے 7 دن میں استعمال ہونے والا موبائل ڈیٹا: $amount';
  }

  @override
  String get downloadsTitle => 'ڈاؤن لوڈز';

  @override
  String get downloadsHelp =>
      'سگنل کے بغیر جگہ جانے سے پہلے سبق کی ویڈیوز محفوظ کر لیں۔ محفوظ کرنے میں ابھی ڈیٹا استعمال ہوگا، چاہے ڈیٹا کی بچت آن ہو۔';

  @override
  String get downloadsNone =>
      'تمام ویڈیوز ایپ کے اندر موجود ہیں۔ کچھ ڈاؤن لوڈ کرنے کی ضرورت نہیں۔';

  @override
  String downloadSaved(String size) {
    return 'اس فون پر محفوظ ہے ($size)';
  }

  @override
  String get downloadNotSaved => 'محفوظ نہیں';

  @override
  String get downloadSave => 'ڈاؤن لوڈ کریں';

  @override
  String get downloadRemove => 'اس فون سے ہٹائیں';

  @override
  String get downloadFailed =>
      'ڈاؤن لوڈ نہیں ہو سکا۔ انٹرنیٹ چیک کر کے دوبارہ کوشش کریں۔';

  @override
  String get videoNeedsData =>
      'یہ ویڈیو وائی فائی پر ڈاؤن لوڈ ہوگی۔ اس میں یہ دکھایا گیا ہے:';

  @override
  String get videoUseData => 'ابھی دیکھیں (موبائل ڈیٹا استعمال ہوگا)';

  @override
  String get phoneCheckDataWifi => 'وائی فائی ڈیٹا، پچھلے 7 دن';

  @override
  String get phoneCheckDataMobile => 'موبائل ڈیٹا، پچھلے 7 دن';

  @override
  String get privacyTitle => 'رازداری کا نوٹ';

  @override
  String get privacyIntro =>
      'یہ نوٹ بتاتا ہے کہ اے آئی ٹیوٹر آپ کے بچے کے بارے میں کیا محفوظ رکھتا ہے، کہاں رکھتا ہے، اسے کون دیکھ سکتا ہے اور کتنی دیر تک۔';

  @override
  String get privacyKeptTitle => 'ہم کیا رکھتے ہیں';

  @override
  String get privacyKept =>
      'آپ کے بچے کا پہلا نام، جماعت، تصویر اور پن (چھپا کر، تاکہ کوئی اسے پڑھ نہ سکے)، اور اس کی پڑھائی: اسباق، جوابات، مہارتیں اور بیج۔ ہم کبھی خاندانی نام، پتا، فون نمبر یا بچے کی تصویر نہیں مانگتے۔';

  @override
  String get privacyWhereTitle => 'یہ کہاں رکھا جاتا ہے';

  @override
  String get privacyWhere =>
      'اسی فون پر، اور گوگل کے فائر بیس سرورز پر آپ کے اکاؤنٹ میں، تاکہ فون گم ہو جائے یا بدل جائے تو بھی پیش رفت محفوظ رہے۔';

  @override
  String get privacyAiTitle => 'مٹھو کی اے آئی مدد';

  @override
  String get privacyAi =>
      'جب آپ کا بچہ کوئی وضاحت لکھتا ہے، یا اپنے حل کی تصویر لیتا ہے، تو وہ کلاڈ کو بھیجی جاتی ہے، جو اینتھروپک کمپنی کا بنایا ہوا اے آئی ہے اور مٹھو کا جواب لکھتا ہے۔ بچے کا نام کبھی نہیں بھیجا جاتا۔ بھیجنے سے پہلے فون نمبر، ای میل اور پتے ہٹا دیے جاتے ہیں۔ تصویریں پڑھنے کے بعد نہیں رکھی جاتیں۔ اینتھروپک کے قواعد کے مطابق وہ اس سے اپنا اے آئی نہیں سکھاتی۔ آپ ترتیبات میں اے آئی مدد بند کر سکتے ہیں؛ پھر ایپ خود جوابات چیک کرتی ہے۔';

  @override
  String get privacyWhoTitle => 'اسے کون دیکھ سکتا ہے';

  @override
  String get privacyWho =>
      'آپ۔ استاد، صرف اگر آپ بچے کو ان کی کلاس میں شامل کریں: وہ اس کلاس میں بچے کا پہلا نام اور پیش رفت دیکھتے ہیں۔ ایپ کی چھوٹی ٹیم بچوں کی حفاظت اور غلطیاں ٹھیک کرنے کے لیے اے آئی کے پیغامات بغیر ناموں کے پڑھ سکتی ہے۔ اور کوئی نہیں، اور کچھ بھی بیچا یا اشتہاروں کے لیے استعمال نہیں کیا جاتا۔';

  @override
  String get privacyHowLongTitle => 'یہ کتنی دیر رکھا جاتا ہے';

  @override
  String get privacyHowLong =>
      'بچے کی پروفائل اور پیش رفت اس وقت تک رکھی جاتی ہے جب تک آپ اسے حذف نہ کریں۔ اے آئی کے پیغامات حفاظتی جانچ کے لیے 90 دن رکھے جاتے ہیں، پھر حذف کر دیے جاتے ہیں۔ اے آئی کے روزانہ استعمال کی گنتی (صرف نمبر) خرچ پر نظر رکھنے کے لیے رکھی جاتی ہے۔';

  @override
  String get privacySafetyTitle => 'بچوں کی حفاظت';

  @override
  String get privacySafety =>
      'اگر آپ کا بچہ کوئی ایسی بات لکھے جس سے لگے کہ وہ پریشان ہے یا محفوظ نہیں، تو مٹھو پیار سے کہتا ہے کہ وہ کسی بھروسے والے والدین یا استاد سے بات کرے، اور وہ پیغام ٹیم کے پڑھنے کے لیے نشان زد ہو جاتا ہے۔';

  @override
  String get privacyChoicesTitle => 'آپ کے اختیارات';

  @override
  String get privacyChoices =>
      'بچے اور اس کی تمام پیش رفت کو ہٹانے کے لیے ہوم اسکرین کے اوپر خاندان والا بٹن دبائیں، پھر بچے کے ساتھ کوڑے دان کا نشان دبائیں۔ آپ کسی بھی وقت بچے کو کلاس سے نکال سکتے ہیں۔ آپ ترتیبات میں اے آئی مدد بند کر سکتے ہیں۔';

  @override
  String get privacyListen => 'سنیں';

  @override
  String get privacyStop => 'روکیں';

  @override
  String get aiHelpSetting => 'مٹھو کی اے آئی مدد';

  @override
  String get aiHelpSettingHint =>
      'لکھی ہوئی وضاحتیں اور حل کی تصویریں بغیر نام کے اے آئی کو بھیجتا ہے۔ بند ہو تو ایپ خود جوابات چیک کرتی ہے۔';

  @override
  String get photoAiOff =>
      'مٹھو کی اے آئی مدد بند ہے، اس لیے اپنا جواب لکھ دیں۔';

  @override
  String get learningTotalsTitle => 'پورے منصوبے میں پڑھائی';

  @override
  String learningTotalsRow(
    int students,
    int lessons,
    int finished,
    int questions,
    int firstTry,
    int aiCalls,
  ) {
    return '$students بچے · $lessons اسباق ($finished مکمل) · $questions سوالات ($firstTry پہلی بار درست) · $aiCalls اے آئی جانچ';
  }

  @override
  String get phoneCheckCrashes => 'کریش، پچھلے 7 دن';

  @override
  String get privacyCrashTitle => 'کریش کی رپورٹیں';

  @override
  String get privacyCrash =>
      'اگر ایپ بند ہو جائے (کریش)، تو اسے ٹھیک کرنے کے لیے ایک رپورٹ گوگل کے فائر بیس کریش لِٹکس کو جاتی ہے۔ اس میں فون کا ماڈل، اینڈرائیڈ کا ورژن اور یہ کہ ایپ کہاں بند ہوئی شامل ہوتا ہے، کبھی کوئی نام یا ای میل نہیں۔ ایپ میں کوئی اشتہار اور کوئی گوگل اینالیٹکس نہیں ہے۔';

  @override
  String get navHome => 'گھر';

  @override
  String get navLessons => 'اسباق';

  @override
  String get navBadges => 'بیجز';

  @override
  String get badgesIntro =>
      'بیجز محنت پر ملتے ہیں: سبق مکمل کرنا، دوبارہ کوشش کرنا، اپنی سوچ بتانا اور روز واپس آنا۔';
}

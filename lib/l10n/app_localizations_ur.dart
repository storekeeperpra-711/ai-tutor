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
}

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
  String get homeWelcome => 'خوش آمدید! آپ کے سبق یہاں نظر آئیں گے۔';

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
}

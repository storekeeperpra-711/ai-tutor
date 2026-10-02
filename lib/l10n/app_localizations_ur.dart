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
}

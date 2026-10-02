import 'package:flutter/widgets.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'preferences.dart';

/// Languages the app supports. Every student-facing string exists in both.
const supportedLocales = [Locale('en'), Locale('ur')];

/// The app's current language. Remembered on the device between launches.
final localeProvider = NotifierProvider<LocaleController, Locale>(
  LocaleController.new,
);

class LocaleController extends Notifier<Locale> {
  static const _key = 'locale';

  @override
  Locale build() {
    final code = ref.read(sharedPreferencesProvider).getString(_key);
    return supportedLocales.firstWhere(
      (l) => l.languageCode == code,
      orElse: () => supportedLocales.first,
    );
  }

  Future<void> setLocale(Locale locale) async {
    state = locale;
    await ref
        .read(sharedPreferencesProvider)
        .setString(_key, locale.languageCode);
  }
}

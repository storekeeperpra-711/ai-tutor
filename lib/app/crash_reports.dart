import 'dart:convert';

import 'package:firebase_crashlytics/firebase_crashlytics.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'preferences.dart';

/// Crashes counted on this phone, by day, for the Phone check screen
/// (Phase 10). Only counts are kept, for the last 7 days.
class CrashCounter {
  CrashCounter(this._prefs);

  static const _key = 'crashes.days';
  static const keepDays = 7;

  final SharedPreferences _prefs;

  static String _day(DateTime t) =>
      '${t.year.toString().padLeft(4, '0')}-'
      '${t.month.toString().padLeft(2, '0')}-'
      '${t.day.toString().padLeft(2, '0')}';

  Map<String, int> _read() {
    try {
      final saved = jsonDecode(_prefs.getString(_key) ?? '{}') as Map;
      return {
        for (final e in saved.entries) '${e.key}': (e.value as num).toInt(),
      };
    } catch (_) {
      return {};
    }
  }

  /// Adds one crash to today's count and forgets days older than a week.
  Future<void> add(DateTime now) async {
    final days = _read();
    final today = _day(now);
    days[today] = (days[today] ?? 0) + 1;
    final oldest = _day(now.subtract(const Duration(days: keepDays - 1)));
    days.removeWhere((day, _) => day.compareTo(oldest) < 0);
    await _prefs.setString(_key, jsonEncode(days));
  }

  /// Crashes in the last 7 days (today included).
  int lastWeek(DateTime now) {
    final oldest = _day(now.subtract(const Duration(days: keepDays - 1)));
    return _read().entries
        .where((e) => e.key.compareTo(oldest) >= 0)
        .fold(0, (sum, e) => sum + e.value);
  }
}

final crashCounterProvider = Provider<CrashCounter>(
  (ref) => CrashCounter(ref.watch(sharedPreferencesProvider)),
);

/// Sends app crashes to Firebase Crashlytics (Phase 10). Crashlytics gets
/// the phone model, the Android version and where the app crashed; the app
/// never gives it a name, an email or an account id, and there is no Google
/// Analytics. Debug builds report nothing. Each crash is also counted on
/// the phone for the Phone check screen.
Future<void> setUpCrashReports(SharedPreferences prefs) async {
  final crashlytics = FirebaseCrashlytics.instance;
  await crashlytics.setCrashlyticsCollectionEnabled(!kDebugMode);
  final counter = CrashCounter(prefs);

  final showError = FlutterError.onError;
  FlutterError.onError = (details) {
    showError?.call(details);
    unawaitedSafe(counter.add(DateTime.now()));
    unawaitedSafe(crashlytics.recordFlutterFatalError(details));
  };
  // Errors outside Flutter's own code (for example in a background task).
  PlatformDispatcher.instance.onError = (error, stack) {
    unawaitedSafe(counter.add(DateTime.now()));
    unawaitedSafe(crashlytics.recordError(error, stack, fatal: true));
    return true;
  };
  // A crash in Android's own code closes the app before Dart can count it;
  // Crashlytics tells us about it on the next start.
  try {
    if (await crashlytics.didCrashOnPreviousExecution()) {
      await counter.add(DateTime.now());
    }
  } catch (_) {}
}

/// Runs [future] without waiting, ignoring its errors (a crash report must
/// never cause another crash).
void unawaitedSafe(Future<void> future) {
  future.catchError((Object _) {});
}

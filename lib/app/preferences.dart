import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Small on-device settings store (language, age tier).
///
/// It is loaded once in `main()` and passed in with `overrideWithValue`,
/// so the rest of the app can read settings without waiting.
final sharedPreferencesProvider = Provider<SharedPreferences>(
  (ref) => throw UnimplementedError('Override in main() before use'),
);

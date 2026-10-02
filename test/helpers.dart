import 'package:ai_tutor/app/app.dart';
import 'package:ai_tutor/app/preferences.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Builds the full app with an in-memory settings store.
Future<Widget> buildTestApp({Map<String, Object> prefs = const {}}) async {
  SharedPreferences.setMockInitialValues(prefs);
  final store = await SharedPreferences.getInstance();
  return ProviderScope(
    overrides: [sharedPreferencesProvider.overrideWithValue(store)],
    child: const AiTutorApp(),
  );
}

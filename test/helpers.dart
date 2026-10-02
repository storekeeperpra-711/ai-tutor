import 'package:ai_tutor/app/app.dart';
import 'package:ai_tutor/app/preferences.dart';
import 'package:ai_tutor/services/auth_service.dart';
import 'package:ai_tutor/services/connectivity.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:ai_tutor/services/remote_store.dart';
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'fakes.dart';

/// Builds the full app with an in-memory settings store and a pretend
/// Firebase ([backend]).
Future<Widget> buildTestApp({
  Map<String, Object> prefs = const {},
  FakeBackend? backend,
}) async {
  // Each test starts with fresh asset loading (cached futures from an
  // earlier test belong to that test's fake clock).
  rootBundle.clear();
  SharedPreferences.setMockInitialValues(prefs);
  final store = await SharedPreferences.getInstance();
  final fake = backend ?? FakeBackend();
  return ProviderScope(
    overrides: [
      sharedPreferencesProvider.overrideWithValue(store),
      localDbProvider.overrideWithValue(fake.db),
      authServiceProvider.overrideWithValue(fake.auth),
      remoteStoreProvider.overrideWithValue(fake.remote),
      onlineProvider.overrideWith((ref) => fake.onlineStream),
    ],
    child: const AiTutorApp(),
  );
}

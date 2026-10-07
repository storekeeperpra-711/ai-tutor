import 'package:ai_tutor/ai/ai_service.dart';
import 'package:ai_tutor/ai/photo_picker.dart';
import 'package:ai_tutor/app/app.dart';
import 'package:ai_tutor/app/preferences.dart';
import 'package:ai_tutor/character/narrator.dart';
import 'package:ai_tutor/character/sounds.dart';
import 'package:ai_tutor/classes/class_store.dart';
import 'package:ai_tutor/data/data_usage.dart';
import 'package:ai_tutor/media/media_cache.dart';
import 'package:ai_tutor/reports/report_voice.dart';
import 'package:ai_tutor/review/review_store.dart';
import 'package:ai_tutor/services/auth_service.dart';
import 'package:ai_tutor/services/connectivity.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:ai_tutor/services/remote_store.dart';
import 'package:flutter/services.dart';
import 'package:ai_tutor/lessons/hidden_units.dart';
import 'package:ai_tutor/lessons/steps/video_step_view.dart';
import 'package:ai_tutor/sims/sim_host.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'fakes.dart';

/// Builds the full app with an in-memory settings store and a pretend
/// Firebase ([backend]).
Future<Widget> buildTestApp({
  Map<String, Object> prefs = const {},
  FakeBackend? backend,
  bool reviewOffered = false,
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
      // Most tests play the Fractions lesson, which children don't see.
      hiddenUnitsProvider.overrideWithValue(const {}),
      localDbProvider.overrideWithValue(fake.db),
      authServiceProvider.overrideWithValue(fake.auth),
      remoteStoreProvider.overrideWithValue(fake.remote),
      reviewStoreProvider.overrideWithValue(fake.reviews),
      classStoreProvider.overrideWithValue(fake.classes),
      reviewOfferedProvider.overrideWithValue(reviewOffered),
      onlineProvider.overrideWith((ref) => fake.onlineStream),
      onWifiProvider.overrideWith((ref) => fake.wifiStream),
      appByteCounterProvider.overrideWithValue(() async => fake.appBytes),
      aiServiceProvider.overrideWithValue(fake.ai),
      narratorProvider.overrideWithValue(fake.narrator),
      reportVoiceProvider.overrideWithValue(fake.reportVoice),
      soundPlayerProvider.overrideWithValue(fake.sounds),
      mediaCacheProvider.overrideWithValue(fake.media),
      photoPickerProvider.overrideWithValue((source) async => fake.photo),
      // Widget tests have no WebView and can't play video.
      webSimBuilderProvider.overrideWithValue(
        (args) => SizedBox.expand(key: Key('fake-web-sim-${args.step.src}')),
      ),
      videoControllerFactoryProvider.overrideWithValue(
        (video, captions) async => throw UnsupportedError('no video in tests'),
      ),
    ],
    child: const AiTutorApp(),
  );
}

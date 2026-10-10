import 'dart:async';
import 'dart:io';

import 'package:ai_tutor/app/preferences.dart';
import 'package:ai_tutor/character/narrator.dart';
import 'package:ai_tutor/character/voice_lines.dart';
import 'package:ai_tutor/character/voice_recorder.dart';
import 'package:ai_tutor/features/debug/narration_recorder_screen.dart';
import 'package:ai_tutor/l10n/app_localizations.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../fakes.dart';

class _FakeMic implements VoiceRecorder {
  final _levels = StreamController<double>.broadcast();
  String? path;

  @override
  Future<bool> start(String path) async {
    this.path = path;
    return true;
  }

  @override
  Stream<double> get levels => _levels.stream;

  void speak(List<double> levels) => levels.forEach(_levels.add);

  @override
  Future<void> stop() async => File(path!).writeAsBytesSync([1, 2, 3]);
}

Future<void> tapKey(WidgetTester tester, String key) async {
  await tester.ensureVisible(find.byKey(Key(key)));
  await tester.pumpAndSettle();
  await tester.tap(find.byKey(Key(key)));
}

void main() {
  late Directory dir;
  late LocalDb db;
  setUp(() {
    dir = Directory.systemTemp.createTempSync('voice');
    db = FakeBackend().db;
  });
  tearDown(() async {
    dir.deleteSync(recursive: true);
    await db.close();
  });

  testWidgets('records a line with its mouth track, then lists it', (
    tester,
  ) async {
    rootBundle.clear();
    SharedPreferences.setMockInitialValues({});
    final prefs = await SharedPreferences.getInstance();
    final mic = _FakeMic();
    final narrator = FakeNarrator();
    await tester.pumpWidget(
      ProviderScope(
        overrides: [
          sharedPreferencesProvider.overrideWithValue(prefs),
          localDbProvider.overrideWithValue(db),
          voiceLibraryProvider.overrideWithValue(
            VoiceLibrary(recordingsDir: dir),
          ),
          voiceRecorderProvider.overrideWithValue(mic),
          narratorProvider.overrideWithValue(narrator),
        ],
        child: const MaterialApp(
          localizationsDelegates: AppLocalizations.localizationsDelegates,
          supportedLocales: AppLocalizations.supportedLocales,
          home: NarrationRecorderScreen(),
        ),
      ),
    );
    await tester.pumpAndSettle();

    const name = 'g6-maths-02-dividing-fractions__s1_hook_ur.m4a';
    expect(find.text('No voice yet'), findsWidgets);
    await tester.scrollUntilVisible(find.byKey(const Key('voice-$name')), 600);

    await tapKey(tester, 'record-$name');
    await tester.pumpAndSettle();
    mic.speak([0, 0.5, 1, 0.5]);
    await tapKey(tester, 'stop-$name');
    await tester.pumpAndSettle();

    expect(File('${dir.path}/$name').existsSync(), isTrue);
    expect(
      File('${dir.path}/${mouthFileName(name)}').readAsStringSync(),
      '0595',
    );
    expect(find.text('Recorded on this phone (not sent yet)'), findsOneWidget);

    await tapKey(tester, 'play-$name');
    expect(narrator.said.single.fileName, name);

    await tapKey(tester, 'delete-$name');
    await tester.pumpAndSettle();
    expect(File('${dir.path}/$name').existsSync(), isFalse);
  });
}

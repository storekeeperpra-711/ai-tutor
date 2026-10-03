import 'dart:convert';
import 'dart:io';

import 'package:ai_tutor/lessons/lesson_repository.dart';
import 'package:ai_tutor/lessons/lesson_updates.dart';
import 'package:ai_tutor/services/auth_service.dart';
import 'package:ai_tutor/services/connectivity.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:ai_tutor/services/remote_store.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';

const bundledId = 'g9-maths-05-solving-linear-equations';
const newId = 'g9-maths-06-new-lesson';

/// A copy of a bundled lesson, with a new id and title.
Map<String, Object?> lessonJson({String id = newId, String title = 'New'}) {
  final json = jsonDecode(
    File('content/lessons/$bundledId.json').readAsStringSync(),
  ) as Map<String, Object?>;
  return {
    ...json,
    'id': id,
    'title': {'en': title, 'ur': title},
  };
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late FakeBackend backend;
  late DateTime now;
  late LessonUpdater updater;

  setUp(() {
    backend = FakeBackend();
    now = DateTime(2026, 10, 3, 9);
    updater = LessonUpdater(
      db: backend.db,
      remote: backend.remote,
      now: () => now,
    );
  });

  tearDown(() => backend.db.close());

  Future<List<String>> savedIds() async => [
    for (final l in await backend.db.allDownloadedLessons()) l.id,
  ];

  test('fingerprints match tools/upload.py', () {
    // python3 -c "import upload; print(upload.fingerprint('{\"id\":\"سلام\"}'))"
    expect(lessonFingerprint('{"id":"سلام"}'), '6c9a9afa7c65e770');
  });

  test('downloads a published lesson and keeps it', () async {
    backend.remote.publishLesson(lessonJson());
    expect(await updater.update(), isTrue);
    final saved = await backend.db.downloadedLesson(newId);
    expect(saved?.version, 1);
    expect(jsonDecode(saved!.content)['id'], newId);
  });

  test('checks at most once an hour, and only downloads changes', () async {
    backend.remote.publishLesson(lessonJson());
    await updater.update();
    expect(backend.remote.lessonReads, 2);

    expect(await updater.update(), isFalse);
    expect(backend.remote.lessonReads, 2, reason: 'checked too soon');

    now = now.add(LessonUpdater.checkEvery);
    expect(await updater.update(), isFalse);
    expect(backend.remote.lessonReads, 3, reason: 'only the catalog');

    backend.remote.publishLesson(lessonJson(title: 'Fixed'), version: 2);
    expect(await updater.update(force: true), isTrue);
    final saved = await backend.db.downloadedLesson(newId);
    expect(saved?.version, 2);
    expect(jsonDecode(saved!.content)['title']['en'], 'Fixed');
  });

  test('forgets a lesson that was unpublished', () async {
    backend.remote.publishLesson(lessonJson());
    await updater.update();
    backend.remote.docs['lesson_catalog/current'] = {'lessons': {}};
    expect(await updater.update(force: true), isTrue);
    expect(await savedIds(), isEmpty);
  });

  test('offline it changes nothing and tries again next time', () async {
    backend.remote.publishLesson(lessonJson());
    backend.setOnline(false);
    expect(await updater.update(), isFalse);
    backend.setOnline(true);
    expect(await updater.update(), isTrue, reason: 'no hour to wait');
  });

  group('skips a lesson this app cannot show', () {
    Future<void> expectSkipped(
      void Function(Map<String, Object?> doc) spoil,
    ) async {
      backend.remote.publishLesson(lessonJson());
      spoil(backend.remote.docs['published_lessons/$newId']!);
      expect(await updater.update(), isFalse);
      expect(await savedIds(), isEmpty);
    }

    test('made for a newer app', () => expectSkipped((d) => d['format'] = 2));

    test(
      'damaged on the way',
      () => expectSkipped((d) {
        d['content'] = (d['content']! as String).replaceFirst('New', 'Nwe');
      }),
    );

    test('with a step type this app does not know', () async {
      final json = lessonJson();
      json['steps'] = [
        ...json['steps']! as List,
        {'id': 'x', 'type': 'hologram'},
      ];
      backend.remote.publishLesson(json);
      expect(await updater.update(), isFalse);
    });

    test(
      'stored under another lesson id',
      () => expectSkipped((d) {
        final content = jsonEncode(lessonJson(id: bundledId));
        d['content'] = content;
        d['hash'] = lessonFingerprint(content);
      }),
    );
  });

  group('in the app', () {
    late ProviderContainer container;

    setUp(() {
      rootBundle.clear();
      container = ProviderContainer(
        overrides: [
          localDbProvider.overrideWithValue(backend.db),
          remoteStoreProvider.overrideWithValue(backend.remote),
          authServiceProvider.overrideWithValue(backend.auth),
          onlineProvider.overrideWith((ref) => backend.onlineStream),
        ],
      );
    });

    tearDown(() => container.dispose());

    test('a downloaded lesson replaces the bundled one', () async {
      backend.remote.publishLesson(lessonJson(id: bundledId, title: 'Newer'));
      await updater.update();
      final lesson = await container.read(lessonProvider(bundledId).future);
      expect(lesson.title.en, 'Newer');
    });

    test('new lessons appear once the phone is signed in', () async {
      backend.remote.publishLesson(lessonJson());
      // Kept running, as the app does.
      container.listen(lessonUpdaterProvider, (_, _) {});
      expect(
        await container.read(lessonIdsProvider.future),
        isNot(contains(newId)),
      );

      await backend.auth.ensureSignedIn();
      await pumpEventQueue();
      final ids = await container.read(lessonIdsProvider.future);
      expect(ids, containsAll([newId, bundledId]));
      final lesson = await container.read(lessonProvider(newId).future);
      expect(lesson.title.en, 'New');
    });
  });
}

import 'dart:async';

import 'package:ai_tutor/l10n/app_localizations.dart';
import 'package:ai_tutor/lessons/steps/video_step_view.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:ai_tutor/models/localized_text.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:video_player/video_player.dart';
import 'package:video_player_platform_interface/video_player_platform_interface.dart';

/// A pretend video player: every video is 60 seconds long.
class FakeVideoPlatform extends VideoPlayerPlatform {
  final created = <int>[];
  final disposed = <int>[];
  final seeks = <Duration>[];
  final playing = <int>{};
  final _events = <int, StreamController<VideoEvent>>{};
  var _next = 0;

  @override
  Future<void> init() async {}

  @override
  Future<int?> createWithOptions(VideoCreationOptions options) async {
    final id = _next++;
    created.add(id);
    _events[id] = StreamController<VideoEvent>()
      ..add(
        VideoEvent(
          eventType: VideoEventType.initialized,
          duration: const Duration(seconds: 60),
          size: const Size(320, 180),
        ),
      );
    return id;
  }

  @override
  Stream<VideoEvent> videoEventsFor(int playerId) => _events[playerId]!.stream;

  @override
  Future<void> dispose(int playerId) async {
    disposed.add(playerId);
    playing.remove(playerId);
  }

  @override
  Future<void> play(int playerId) async => playing.add(playerId);

  @override
  Future<void> pause(int playerId) async => playing.remove(playerId);

  @override
  Future<void> seekTo(int playerId, Duration position) async =>
      seeks.add(position);

  @override
  Future<Duration> getPosition(int playerId) async =>
      const Duration(seconds: 25);

  @override
  Future<void> setLooping(int playerId, bool looping) async {}

  @override
  Future<void> setVolume(int playerId, double volume) async {}

  @override
  Future<void> setPlaybackSpeed(int playerId, double speed) async {}

  @override
  Widget buildViewWithOptions(VideoViewOptions options) =>
      const SizedBox.expand();
}

void main() {
  testWidgets('the video is freed in the background and comes back paused '
      'at the same place', (tester) async {
    final platform = FakeVideoPlatform();
    VideoPlayerPlatform.instance = platform;
    tester.binding.handleAppLifecycleStateChanged(AppLifecycleState.resumed);
    const text = LocalizedText(en: 'Falling', ur: 'گرنا');
    await tester.pumpWidget(
      ProviderScope(
        overrides: [
          videoControllerFactoryProvider.overrideWithValue(
            (video, captions) async =>
                VideoPlayerController.networkUrl(Uri.parse('https://v.mp4')),
          ),
        ],
        child: MaterialApp(
          localizationsDelegates: AppLocalizations.localizationsDelegates,
          supportedLocales: AppLocalizations.supportedLocales,
          home: Scaffold(
            body: VideoStepView(
              step: const VideoStep(
                id: 'v1',
                type: 'video',
                src: LocalizedText(en: 'https://v.mp4', ur: 'https://v.mp4'),
                summary: text,
              ),
              onDone: (_) {},
            ),
          ),
        ),
      ),
    );
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('video')), findsOneWidget);
    expect(platform.playing, {0});

    // Let the player read its position (it polls while playing).
    await tester.pump(const Duration(milliseconds: 600));

    tester.binding.handleAppLifecycleStateChanged(AppLifecycleState.inactive);
    tester.binding.handleAppLifecycleStateChanged(AppLifecycleState.hidden);
    // No frames are drawn while hidden; let the player close for real.
    await tester.runAsync(
      () => Future<void>.delayed(const Duration(milliseconds: 50)),
    );
    expect(platform.disposed, [0]);

    tester.binding.handleAppLifecycleStateChanged(AppLifecycleState.inactive);
    await tester.runAsync(
      () => Future<void>.delayed(const Duration(milliseconds: 50)),
    );
    await tester.pumpAndSettle();
    expect(platform.created, [0, 1]);
    expect(platform.seeks.last, const Duration(seconds: 25));
    expect(platform.playing, isEmpty);
    expect(find.byKey(const Key('video')), findsOneWidget);

    tester.binding.handleAppLifecycleStateChanged(AppLifecycleState.resumed);
    await tester.pumpWidget(const SizedBox());
    await tester.runAsync(
      () => Future<void>.delayed(const Duration(milliseconds: 50)),
    );
    expect(platform.disposed, [0, 1]);
  });
}

import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:video_player/video_player.dart';

import '../../character/mithu_bubble.dart';
import '../../data/data_saver.dart';
import '../../l10n/app_localizations.dart';
import '../../media/media_cache.dart';
import '../../models/lesson_step.dart';
import '../lesson_text.dart';
import '../step_result.dart';
import 'step_scaffold.dart';

/// Makes the player for a video. A provider, so widget tests (which
/// can't play video) can swap it.
typedef VideoControllerFactory = Future<VideoPlayerController> Function(
  MediaSource video,
  Future<ClosedCaptionFile>? captions,
);

final videoControllerFactoryProvider = Provider<VideoControllerFactory>((ref) {
  final cache = ref.watch(mediaCacheProvider);
  return (video, captions) async => switch (video) {
    AssetMedia(:final asset) => VideoPlayerController.asset(
      asset,
      closedCaptionFile: captions,
    ),
    LinkMedia(:final url) => VideoPlayerController.file(
      await cache.file(url),
      closedCaptionFile: captions,
    ),
  };
});

/// A short video in the child's language, with captions. The child can
/// always carry on; if the video can't play, its summary is shown
/// instead, so a lesson never gets stuck on a video.
class VideoStepView extends ConsumerStatefulWidget {
  const VideoStepView({super.key, required this.step, required this.onDone});

  final VideoStep step;
  final StepDone onDone;

  @override
  ConsumerState<VideoStepView> createState() => _VideoStepViewState();
}

class _VideoStepViewState extends ConsumerState<VideoStepView> {
  VideoPlayerController? _controller;
  var _failed = false;
  var _captions = true;
  String? _language;

  /// The video isn't saved and Data saver is on, on mobile data: the
  /// child (or parent) can choose to use data, or read the summary.
  var _waitingForWifi = false;

  /// Where the video was when the app went into the background.
  Duration? _resumeAt;
  var _hidden = false;
  late final AppLifecycleListener _lifecycle;

  @override
  void initState() {
    super.initState();
    _lifecycle = AppLifecycleListener(onHide: _release, onShow: _restore);
  }

  /// Frees the video's memory while the app is out of sight (a cheap
  /// phone may need it for another app), remembering the place.
  Future<void> _release() async {
    _hidden = true;
    final controller = _controller;
    if (controller == null) return;
    _resumeAt = controller.value.position;
    controller.removeListener(_onTick);
    setState(() => _controller = null);
    await controller.dispose();
  }

  /// Loads the video again at the same place, paused, when the app is
  /// back.
  void _restore() {
    _hidden = false;
    final at = _resumeAt;
    final language = _language;
    if (at == null || language == null) return;
    _resumeAt = null;
    unawaited(_load(language, at: at));
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final language = Localizations.localeOf(context).languageCode;
    if (language != _language) {
      _language = language;
      unawaited(_load(language));
    }
  }

  Future<void> _load(
    String language, {
    Duration? at,
    bool useData = false,
  }) async {
    final old = _controller;
    setState(() {
      _controller = null;
      _failed = false;
      _waitingForWifi = false;
    });
    await old?.dispose();

    final step = widget.step;
    final cache = ref.read(mediaCacheProvider);
    final video = MediaSource.of(step.src.inLanguage(language), 'videos');
    if (video is LinkMedia &&
        !useData &&
        !ref.read(autoDownloadProvider) &&
        !await cache.isSaved(video.url)) {
      if (mounted && language == _language) {
        setState(() => _waitingForWifi = true);
      }
      return;
    }
    final captionPath = step.captions?.inLanguage(language);
    final captions = captionPath == null
        ? null
        : cache
              .text(MediaSource.of(captionPath, 'videos'))
              .then<ClosedCaptionFile>(WebVTTCaptionFile.new);
    try {
      final controller = await ref.read(videoControllerFactoryProvider)(
        video,
        captions,
      );
      await controller.initialize();
      if (!mounted || language != _language) {
        await controller.dispose();
        return;
      }
      controller.addListener(_onTick);
      setState(() => _controller = controller);
      if (at == null) {
        // A video that finished loading in the background waits.
        if (!_hidden) await controller.play();
      } else {
        await controller.seekTo(at);
      }
    } on Object {
      if (mounted && language == _language) setState(() => _failed = true);
    }
  }

  void _onTick() {
    if (mounted) setState(() {});
  }

  @override
  void dispose() {
    _lifecycle.dispose();
    _controller
      ?..removeListener(_onTick)
      ..dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final step = widget.step;
    final controller = _controller;
    final value = controller?.value;
    final ended =
        value != null &&
        value.isInitialized &&
        value.position >= value.duration &&
        !value.isPlaying;

    return StepScaffold(
      buttonLabel: l10n.continueButton,
      onPressed: () => widget.onDone(StepResult(stepId: step.id)),
      children: [
        if (step.character != null) ...[
          MithuBubble(line: step.character!),
          const SizedBox(height: 16),
        ],
        if (step.title != null) ...[
          LessonText(step.title!, style: textTheme.titleLarge),
          const SizedBox(height: 12),
        ],
        if (_waitingForWifi)
          Container(
            key: const Key('video-wait-wifi'),
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Theme.of(context).colorScheme.surfaceContainerHighest,
              borderRadius: BorderRadius.circular(12),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    const Icon(Icons.wifi_off, size: 32),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Text(
                        l10n.videoNeedsData,
                        style: textTheme.labelLarge,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                LessonText(step.summary, style: textTheme.bodyLarge),
                const SizedBox(height: 12),
                OutlinedButton.icon(
                  key: const Key('video-use-data'),
                  icon: const Icon(Icons.download),
                  label: Text(l10n.videoUseData),
                  onPressed: () => _load(_language ?? 'en', useData: true),
                ),
              ],
            ),
          )
        else if (_failed)
          FeedbackBox(
            key: const Key('video-fallback'),
            good: false,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(l10n.videoCouldNotPlay, style: textTheme.labelLarge),
                const SizedBox(height: 8),
                LessonText(step.summary, style: textTheme.bodyLarge),
              ],
            ),
          )
        else if (controller == null || value == null || !value.isInitialized)
          const AspectRatio(
            aspectRatio: 16 / 9,
            child: Center(child: CircularProgressIndicator()),
          )
        else ...[
          AspectRatio(
            key: const Key('video'),
            aspectRatio: value.aspectRatio,
            child: Stack(
              alignment: Alignment.bottomCenter,
              children: [
                VideoPlayer(controller),
                if (_captions)
                  ClosedCaption(
                    text: value.caption.text,
                    textStyle: textTheme.titleMedium?.copyWith(
                      color: Colors.white,
                    ),
                  ),
              ],
            ),
          ),
          VideoProgressIndicator(
            controller,
            allowScrubbing: true,
            padding: const EdgeInsets.symmetric(vertical: 8),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              IconButton.filledTonal(
                key: const Key('video-play'),
                iconSize: 36,
                tooltip: ended
                    ? l10n.videoReplay
                    : value.isPlaying
                    ? l10n.videoPause
                    : l10n.videoPlay,
                icon: Icon(
                  ended
                      ? Icons.replay
                      : value.isPlaying
                      ? Icons.pause
                      : Icons.play_arrow,
                ),
                onPressed: () async {
                  if (ended) await controller.seekTo(Duration.zero);
                  await (value.isPlaying && !ended
                      ? controller.pause()
                      : controller.play());
                },
              ),
              if (step.captions != null) ...[
                const SizedBox(width: 16),
                IconButton(
                  key: const Key('video-captions'),
                  tooltip: l10n.videoCaptions,
                  isSelected: _captions,
                  icon: const Icon(Icons.closed_caption_off),
                  selectedIcon: const Icon(Icons.closed_caption),
                  onPressed: () => setState(() => _captions = !_captions),
                ),
              ],
            ],
          ),
        ],
      ],
    );
  }
}

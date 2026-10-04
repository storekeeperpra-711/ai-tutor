import 'dart:async';
import 'dart:io';

import 'package:flutter/services.dart';
import 'package:flutter_cache_manager/flutter_cache_manager.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../models/lesson.dart';
import '../models/lesson_step.dart';

/// Where a lesson's media file comes from: bundled in the app, or a link.
sealed class MediaSource {
  const MediaSource();

  /// [path] is a file name in `assets/$folder/` or an https link.
  factory MediaSource.of(String path, String folder) =>
      path.startsWith('https://')
      ? LinkMedia(path)
      : AssetMedia('assets/$folder/$path');
}

class AssetMedia extends MediaSource {
  const AssetMedia(this.asset);
  final String asset;
}

class LinkMedia extends MediaSource {
  const LinkMedia(this.url);
  final String url;
}

/// Downloads linked media once and keeps it on the phone, so a video
/// watched again (or opened offline later) costs no more data.
///
/// Saved media is kept under [maxBytes] (Phase 10): when a download takes
/// it over, the files used longest ago are removed first.
class MediaCache {
  MediaCache({
    BaseCacheManager? manager,
    CacheInfoRepository? repo,
    this.maxBytes = defaultMaxBytes,
  }) : _givenManager = manager,
       _givenRepo = repo;

  static const defaultMaxBytes = 300 * 1024 * 1024;

  // Made on first use, so a screen that never needs media touches no
  // files.
  static final _config = Config('lessonMedia');
  final BaseCacheManager? _givenManager;
  final CacheInfoRepository? _givenRepo;
  late final BaseCacheManager _manager = _givenManager ?? CacheManager(_config);
  late final CacheInfoRepository _repo = _givenRepo ?? _config.repo;
  final int maxBytes;

  /// The file for [url]: from the cache, or downloaded now.
  Future<File> file(String url) async {
    final file = await _manager.getSingleFile(url);
    unawaited(trim(keep: {url}).catchError((Object _) {}));
    return file;
  }

  /// Bytes of media saved on the phone.
  Future<int> usedBytes() async {
    await _repo.open();
    return (await _repo.getAllObjects()).fold<int>(
      0,
      (sum, o) => sum + (o.length ?? 0),
    );
  }

  /// Removes the files used longest ago until the total is at most
  /// [maxBytes]. Files in [keep] (the lesson open now) stay.
  Future<void> trim({Set<String> keep = const {}}) async {
    await _repo.open();
    final saved = await _repo.getAllObjects();
    var total = saved.fold<int>(0, (sum, o) => sum + (o.length ?? 0));
    if (total <= maxBytes) return;
    saved.sort(
      (a, b) => (a.touched ?? a.validTill).compareTo(b.touched ?? b.validTill),
    );
    for (final o in saved) {
      if (total <= maxBytes) break;
      if (keep.contains(o.key)) continue;
      await _manager.removeFile(o.key);
      total -= o.length ?? 0;
    }
  }

  /// Removes all saved media (the Phone check screen's button).
  Future<void> clear() => _manager.emptyCache();

  /// Text of a bundled or linked file (captions).
  Future<String> text(MediaSource source) async => switch (source) {
    AssetMedia(:final asset) => rootBundle.loadString(asset),
    LinkMedia(:final url) => (await file(url)).readAsString(),
  };

  /// Whether [url] is saved on the phone (so playing it uses no data).
  Future<bool> isSaved(String url) async {
    await _repo.open();
    return await _repo.get(url) != null;
  }

  /// Bytes saved of [urls].
  Future<int> savedBytesOf(Set<String> urls) async {
    await _repo.open();
    return (await _repo.getAllObjects())
        .where((o) => urls.contains(o.key))
        .fold<int>(0, (sum, o) => sum + (o.length ?? 0));
  }

  /// Downloads [urls] now (the Downloads screen, or a parent choosing to
  /// use mobile data). Throws when offline.
  Future<void> download(Set<String> urls) async {
    await Future.wait([for (final url in urls) _manager.downloadFile(url)]);
    await trim(keep: urls);
  }

  /// Removes [urls] from the phone.
  Future<void> remove(Set<String> urls) async {
    for (final url in urls) {
      await _manager.removeFile(url);
    }
  }

  /// The linked videos and captions of [lesson] in [language] (bundled
  /// ones need no download).
  static Set<String> linksOf(Lesson lesson, String language) => {
    for (final step in lesson.steps.whereType<VideoStep>())
      for (final path in [
        step.src.inLanguage(language),
        ?step.captions?.inLanguage(language),
      ])
        if (path.startsWith('https://')) path,
  };

  /// Starts downloading the linked videos (and captions) of [lesson] in
  /// [language], so they are ready by the time the child reaches them.
  /// Errors are ignored: the video step tries again and has a fallback.
  /// The caller checks Data saver first.
  void prefetch(Lesson lesson, String language) {
    final links = linksOf(lesson, language);
    if (links.isEmpty) return;
    unawaited(download(links).catchError((Object _) {}));
  }
}

final mediaCacheProvider = Provider<MediaCache>((ref) => MediaCache());

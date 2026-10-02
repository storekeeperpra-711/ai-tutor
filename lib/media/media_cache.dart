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
class MediaCache {
  MediaCache([BaseCacheManager? manager])
    : _manager = manager ?? DefaultCacheManager();

  final BaseCacheManager _manager;

  /// The file for [url]: from the cache, or downloaded now.
  Future<File> file(String url) => _manager.getSingleFile(url);

  /// Text of a bundled or linked file (captions).
  Future<String> text(MediaSource source) async => switch (source) {
    AssetMedia(:final asset) => rootBundle.loadString(asset),
    LinkMedia(:final url) => (await file(url)).readAsString(),
  };

  /// Starts downloading the linked videos (and captions) of [lesson] in
  /// [language], so they are ready by the time the child reaches them.
  /// Errors are ignored: the video step tries again and has a fallback.
  void prefetch(Lesson lesson, String language) {
    for (final step in lesson.steps.whereType<VideoStep>()) {
      for (final path in [
        step.src.inLanguage(language),
        ?step.captions?.inLanguage(language),
      ]) {
        if (path.startsWith('https://')) {
          _manager.downloadFile(path).ignore();
        }
      }
    }
  }
}

final mediaCacheProvider = Provider<MediaCache>((ref) => MediaCache());

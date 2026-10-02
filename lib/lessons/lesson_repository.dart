import 'dart:convert';

import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../models/lesson.dart';

/// Folder of lesson files, bundled into the app (see pubspec.yaml).
const lessonsFolder = 'content/lessons/';

/// IDs of all lessons bundled in the app, sorted.
/// Later (Phase 8) lessons will also be downloaded from Firebase.
final lessonIdsProvider = FutureProvider<List<String>>((ref) async {
  final manifest = await AssetManifest.loadFromAssetBundle(rootBundle);
  return manifest
      .listAssets()
      .where((p) => p.startsWith(lessonsFolder) && p.endsWith('.json'))
      .map((p) => p.substring(lessonsFolder.length, p.length - '.json'.length))
      .toList()
    ..sort();
});

/// One lesson, read from its JSON file.
final lessonProvider = FutureProvider.family<Lesson, String>(
  (ref, id) async {
    final text = await rootBundle.loadString('$lessonsFolder$id.json');
    return Lesson.fromJson(jsonDecode(text) as Map<String, dynamic>);
  },
  // A broken lesson file won't fix itself, so don't retry.
  retry: (retryCount, error) => null,
);

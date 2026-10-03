import 'dart:convert';

import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../models/lesson.dart';
import '../services/local_db.dart';

/// Folder of lesson files, bundled into the app (see pubspec.yaml).
const lessonsFolder = 'content/lessons/';

/// IDs of all lessons: the ones bundled in the app plus the ones downloaded
/// from Firestore (lesson_updates.dart), sorted.
final lessonIdsProvider = FutureProvider<List<String>>((ref) async {
  final manifest = await AssetManifest.loadFromAssetBundle(rootBundle);
  final bundled = manifest
      .listAssets()
      .where((p) => p.startsWith(lessonsFolder) && p.endsWith('.json'))
      .map((p) => p.substring(lessonsFolder.length, p.length - '.json'.length));
  final downloaded = await ref.watch(localDbProvider).allDownloadedLessons();
  return {...bundled, for (final l in downloaded) l.id}.toList()..sort();
});

/// One lesson: the downloaded version if there is one, else the bundled
/// file.
final lessonProvider = FutureProvider.family<Lesson, String>(
  (ref, id) async {
    final downloaded = await ref.watch(localDbProvider).downloadedLesson(id);
    final text =
        downloaded?.content ??
        await rootBundle.loadString('$lessonsFolder$id.json');
    return Lesson.fromJson(jsonDecode(text) as Map<String, dynamic>);
  },
  // A broken lesson file won't fix itself, so don't retry.
  retry: (retryCount, error) => null,
);

import 'dart:convert';
import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:http/http.dart' as http;
import 'package:path_provider/path_provider.dart';

import '../ai/ai_service.dart';

/// Mithu's recorded voice from the AI server (worker/src/voice.ts), made
/// once with Gemini by tools/voice/make_voice.py. When a lesson opens, its
/// recordings in the child's language are downloaded (about 100 KB a
/// lesson) and kept on the phone; VoiceLibrary then plays them. With no
/// connection, or before a line is recorded, Mithu uses the phone's voice.
class VoiceDownloads {
  VoiceDownloads({required this.baseUrl, http.Client? client, this.folderDir})
    : _client = client ?? http.Client();

  final String baseUrl;
  final http.Client _client;

  /// Where downloads go; null for the app's documents folder.
  final Directory? folderDir;

  Map<String, String>? _index;
  DateTime? _indexTime;

  /// Kept apart from the dev recorder's folder, so a fresh download never
  /// replaces a line someone just recorded on this phone.
  Future<Directory> folder() async {
    final dir =
        folderDir ??
        Directory(
          '${(await getApplicationDocumentsDirectory()).path}/voice-downloads',
        );
    dir.createSync(recursive: true);
    return dir;
  }

  /// Which recordings the server has, and their versions (asked again
  /// after an hour, so new recordings show up the same day).
  Future<Map<String, String>> _serverIndex() async {
    final time = _indexTime;
    if (_index != null &&
        time != null &&
        DateTime.now().difference(time) < const Duration(hours: 1)) {
      return _index!;
    }
    final res = await _client
        .get(Uri.parse('$baseUrl/v1/voice/index'))
        .timeout(const Duration(seconds: 20));
    if (res.statusCode != 200) return const {};
    final files = (jsonDecode(res.body) as Map)['files'] as Map? ?? const {};
    _indexTime = DateTime.now();
    return _index = {for (final e in files.entries) '${e.key}': '${e.value}'};
  }

  /// Downloads [lessonId]'s recordings in [language] that are missing or
  /// out of date. Returns how many were downloaded; never throws.
  Future<int> prepare(String lessonId, String language) async {
    if (baseUrl.isEmpty) return 0;
    try {
      final wanted = (await _serverIndex()).entries.where(
        (e) =>
            e.key.startsWith('${lessonId}__') &&
            e.key.endsWith('_$language.m4a'),
      );
      final dir = await folder();
      final versionsFile = File('${dir.path}/versions.json');
      final versions = versionsFile.existsSync()
          ? Map<String, dynamic>.from(
              jsonDecode(versionsFile.readAsStringSync()) as Map,
            )
          : <String, dynamic>{};
      var count = 0;
      for (final MapEntry(key: name, value: version) in wanted) {
        final audio = File('${dir.path}/$name');
        if (versions[name] == version && audio.existsSync()) continue;
        final mouthName = '${name.substring(0, name.length - 4)}.mouth';
        final got = await Future.wait([
          _download(name, version),
          _download(mouthName, version),
        ]);
        if (got.any((b) => b == null)) continue;
        File('${dir.path}/$mouthName').writeAsBytesSync(got[1]!);
        // Written whole, then renamed, so a cut-off download never plays.
        final part = File('${audio.path}.part')..writeAsBytesSync(got[0]!);
        part.renameSync(audio.path);
        versions[name] = version;
        count++;
      }
      if (count > 0) versionsFile.writeAsStringSync(jsonEncode(versions));
      return count;
    } catch (e) {
      // Offline, a slow network or a server hiccup: try again next lesson.
      debugPrint('Mithu voice download stopped: $e');
      return 0;
    }
  }

  Future<List<int>?> _download(String name, String version) async {
    final res = await _client
        .get(Uri.parse('$baseUrl/v1/voice/$name?v=$version'))
        .timeout(const Duration(seconds: 30));
    return res.statusCode == 200 ? res.bodyBytes : null;
  }
}

final voiceDownloadsProvider = Provider<VoiceDownloads>(
  (ref) => VoiceDownloads(baseUrl: aiServerUrl()),
);

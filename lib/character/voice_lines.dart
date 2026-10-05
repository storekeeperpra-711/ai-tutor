import 'dart:io';

import 'package:flutter/services.dart';
import 'package:path_provider/path_provider.dart';

import '../models/lesson_step.dart';

/// Recorded Mithu lines live flat in assets/audio/ (Flutter doesn't bundle
/// sub-folders), named after the lesson, step and language:
/// `g6-maths-02-dividing-fractions__s1_hook_ur.m4a`. Each recording has a
/// mouth file next to it (`.mouth`): how loud the voice is, 20 times a
/// second, as digits 0 to 9, which moves Mithu's beak.
const audioAssetDir = 'assets/audio';

String voiceFileName(String lessonId, String stepId, String language) =>
    '${lessonId}__${stepId}_$language.m4a';

String mouthFileName(String audioFile) =>
    '${audioFile.substring(0, audioFile.lastIndexOf('.'))}.mouth';

/// How loud a recording is over time, for the beak.
class MouthTrack {
  const MouthTrack(this.levels);

  static const perSecond = 20;

  /// 0 to 1, [perSecond] values a second.
  final List<double> levels;

  factory MouthTrack.parse(String text) => MouthTrack([
    for (final c in text.trim().split(''))
      if (int.tryParse(c) case final n?) n / 9,
  ]);

  /// From microphone loudness in dBFS (about -60 quiet to 0 loud).
  static double levelFromDb(double db) => ((db + 50) / 40).clamp(0.0, 1.0);

  String encode() => levels.map((l) => (l * 9).round().clamp(0, 9)).join();

  Duration get length =>
      Duration(milliseconds: levels.length * 1000 ~/ perSecond);

  double at(Duration position) {
    if (levels.isEmpty) return 0;
    final i = position.inMilliseconds * perSecond ~/ 1000;
    return i < 0 || i >= levels.length ? 0 : levels[i];
  }
}

/// A recording of one line, from the app's files or a dev recording.
class Recording {
  const Recording({
    required this.path,
    required this.isAsset,
    required this.mouth,
  });

  final String path;
  final bool isAsset;
  final MouthTrack mouth;
}

/// One Mithu line in a lesson, in one language.
class VoiceLine {
  const VoiceLine({
    required this.line,
    required this.language,
    this.lessonId,
    this.stepId,
  });

  final CharacterLine line;
  final String language;
  final String? lessonId;
  final String? stepId;

  String get text => line.say.inLanguage(language);

  /// The file name this line's recording has (or would have).
  String? get fileName =>
      line.audio?[language] ??
      (lessonId != null && stepId != null
          ? voiceFileName(lessonId!, stepId!, language)
          : null);
}

/// Finds recordings: first one just made with the dev recorder on this
/// phone, then one downloaded from the AI server (voice_downloads.dart),
/// then one bundled with the app.
class VoiceLibrary {
  VoiceLibrary({AssetBundle? bundle, this.recordingsDir, this.downloadsDir})
    : _bundle = bundle ?? rootBundle;

  final AssetBundle _bundle;

  /// Where the dev recorder saves; null to use the app's documents folder.
  final Directory? recordingsDir;

  /// Where downloads are kept; null to use the app's documents folder
  /// (the same folder as VoiceDownloads.folder).
  final Directory? downloadsDir;
  Set<String>? _assets;

  Future<Directory> recordings() async {
    final dir =
        recordingsDir ??
        Directory('${(await getApplicationDocumentsDirectory()).path}/voice');
    dir.createSync(recursive: true);
    return dir;
  }

  Future<Directory> _downloads() async =>
      downloadsDir ??
      Directory(
        '${(await getApplicationDocumentsDirectory()).path}/voice-downloads',
      );

  Future<Set<String>> _bundled() async => _assets ??= {
    for (final key in (await AssetManifest.loadFromAssetBundle(
      _bundle,
    )).listAssets())
      if (key.startsWith('$audioAssetDir/')) key,
  };

  Future<Recording?> find(VoiceLine voice) async {
    final name = voice.fileName;
    if (name == null) return null;
    for (final folder in [recordings, _downloads]) {
      try {
        final dir = await folder();
        final file = File('${dir.path}/$name');
        final mouth = File('${dir.path}/${mouthFileName(name)}');
        if (file.existsSync()) {
          return Recording(
            path: file.path,
            isAsset: false,
            mouth: MouthTrack.parse(
              mouth.existsSync() ? mouth.readAsStringSync() : '',
            ),
          );
        }
      } on Exception {
        // No documents folder (tests): only bundled recordings.
      }
    }
    final assets = await _bundled();
    final path = '$audioAssetDir/$name';
    if (!assets.contains(path)) return null;
    final mouthPath = '$audioAssetDir/${mouthFileName(name)}';
    return Recording(
      path: path,
      isAsset: true,
      mouth: MouthTrack.parse(
        assets.contains(mouthPath) ? await _bundle.loadString(mouthPath) : '',
      ),
    );
  }
}

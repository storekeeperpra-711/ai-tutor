import 'dart:async';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:record/record.dart';

import 'voice_lines.dart';

/// The microphone, for the narration recorder (a dev tool).
abstract class VoiceRecorder {
  /// False when the microphone may not be used.
  Future<bool> start(String path);

  /// Loudness while recording, 0 to 1, [MouthTrack.perSecond] times a second.
  Stream<double> get levels;

  Future<void> stop();
}

final voiceRecorderProvider = Provider<VoiceRecorder>((ref) {
  final recorder = MicVoiceRecorder();
  ref.onDispose(recorder.dispose);
  return recorder;
});

class MicVoiceRecorder implements VoiceRecorder {
  final _recorder = AudioRecorder();

  @override
  Future<bool> start(String path) async {
    if (!await _recorder.hasPermission()) return false;
    await _recorder.start(
      // Small files: speech in mono AAC is about 6 KB a second.
      const RecordConfig(
        encoder: AudioEncoder.aacLc,
        sampleRate: 22050,
        numChannels: 1,
        bitRate: 48000,
      ),
      path: path,
    );
    return true;
  }

  @override
  Stream<double> get levels => _recorder
      .onAmplitudeChanged(
        const Duration(milliseconds: 1000 ~/ MouthTrack.perSecond),
      )
      .map((a) => MouthTrack.levelFromDb(a.current));

  @override
  Future<void> stop() => _recorder.stop();

  Future<void> dispose() => _recorder.dispose();
}

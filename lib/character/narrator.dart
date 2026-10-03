import 'dart:async';
import 'dart:math' as math;

import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:just_audio/just_audio.dart';

import 'mithu_controller.dart';
import 'voice_lines.dart';

/// How a line was spoken.
enum VoiceKind { recorded, device, none }

/// Speaks Mithu's lines: the recording when there is one (with the beak
/// following the voice), otherwise the phone's text-to-speech.
abstract class Narrator {
  /// Says [voice] with [mithu]'s beak moving; completes when done or
  /// stopped. Saying a new line stops the one before.
  Future<VoiceKind> say(VoiceLine voice, MithuController mithu);

  /// Whether [voice] has a real recording (for the "needs a voice" label).
  Future<bool> hasRecording(VoiceLine voice);

  Future<void> stop();
}

final voiceLibraryProvider = Provider<VoiceLibrary>((ref) => VoiceLibrary());

final narratorProvider = Provider<Narrator>((ref) {
  final narrator = DeviceNarrator(ref.watch(voiceLibraryProvider));
  ref.onDispose(narrator.dispose);
  return narrator;
});

class DeviceNarrator implements Narrator {
  DeviceNarrator(this.library);

  final VoiceLibrary library;
  AudioPlayer? _player;
  FlutterTts? _tts;
  Timer? _mouthTimer;
  MithuController? _speaking;
  Completer<void>? _done;
  final _random = math.Random();

  @override
  Future<bool> hasRecording(VoiceLine voice) async =>
      await library.find(voice) != null;

  @override
  Future<VoiceKind> say(VoiceLine voice, MithuController mithu) async {
    await stop();
    final done = _done = Completer<void>();
    _speaking = mithu;
    try {
      final recording = await library.find(voice);
      if (done.isCompleted) return VoiceKind.none;
      mithu.speaking = true;
      if (recording != null) {
        await _play(recording, mithu, done);
        return VoiceKind.recorded;
      }
      return await _speak(voice, mithu, done)
          ? VoiceKind.device
          : VoiceKind.none;
    } catch (e) {
      debugPrint('Mithu could not speak: $e');
      return VoiceKind.none;
    } finally {
      if (identical(_done, done)) _finish();
    }
  }

  Future<void> _play(
    Recording recording,
    MithuController mithu,
    Completer<void> done,
  ) async {
    final player = _player ??= AudioPlayer();
    if (recording.isAsset) {
      await player.setAsset(recording.path);
    } else {
      await player.setFilePath(recording.path);
    }
    _mouthTimer = Timer.periodic(const Duration(milliseconds: 50), (_) {
      mithu.mouth.value = recording.mouth.at(player.position);
    });
    final ended = player.playerStateStream.firstWhere(
      (s) => s.processingState == ProcessingState.completed,
    );
    unawaited(player.play());
    await Future.any([ended, done.future]);
  }

  /// The phone's voice: Urdu if the phone has it, otherwise the English
  /// text. Returns false when there is no voice at all.
  Future<bool> _speak(
    VoiceLine voice,
    MithuController mithu,
    Completer<void> done,
  ) async {
    final tts = _tts ??= FlutterTts();
    await tts.awaitSpeakCompletion(true);
    var text = voice.text;
    if (voice.language == 'ur' &&
        await tts.isLanguageAvailable('ur-PK') == true) {
      await tts.setLanguage('ur-PK');
    } else {
      await tts.setLanguage('en-US');
      text = voice.line.say.en;
    }
    // No recording to follow: the beak moves with a made-up rhythm.
    _mouthTimer = Timer.periodic(const Duration(milliseconds: 110), (_) {
      mithu.mouth.value = 0.15 + _random.nextDouble() * 0.7;
    });
    await Future.any([tts.speak(text), done.future]);
    return true;
  }

  void _finish() {
    _mouthTimer?.cancel();
    _mouthTimer = null;
    _speaking?.speaking = false;
    _speaking = null;
    if (_done?.isCompleted == false) _done!.complete();
    _done = null;
  }

  @override
  Future<void> stop() async {
    if (_done == null) return;
    _finish();
    try {
      await _player?.stop();
      await _tts?.stop();
    } catch (_) {}
  }

  void dispose() {
    _finish();
    _player?.dispose();
    _tts?.stop();
  }
}

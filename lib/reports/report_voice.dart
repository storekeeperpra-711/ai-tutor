import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_tts/flutter_tts.dart';

/// The phone's own text-to-speech, for reading the parent report aloud
/// (decided 2026-10-03: free, offline, no recordings).
abstract class ReportVoice {
  /// Whether the phone can speak [languageCode] ('en' or 'ur').
  Future<bool> canSpeak(String languageCode);

  /// Says [text] and completes when done (or stopped).
  Future<void> speak(String text, String languageCode);

  Future<void> stop();
}

class DeviceReportVoice implements ReportVoice {
  FlutterTts? _tts;

  static String _tag(String languageCode) =>
      languageCode == 'ur' ? 'ur-PK' : 'en-US';

  Future<FlutterTts> _engine() async {
    final tts = _tts;
    if (tts != null) return tts;
    final created = _tts = FlutterTts();
    await created.awaitSpeakCompletion(true);
    // A little slower than normal, for listeners who don't read.
    await created.setSpeechRate(0.42);
    return created;
  }

  @override
  Future<bool> canSpeak(String languageCode) async {
    try {
      final tts = await _engine();
      return await tts.isLanguageAvailable(_tag(languageCode)) == true;
    } catch (_) {
      return false;
    }
  }

  @override
  Future<void> speak(String text, String languageCode) async {
    final tts = await _engine();
    await tts.setLanguage(_tag(languageCode));
    await tts.speak(text);
  }

  @override
  Future<void> stop() async {
    try {
      await _tts?.stop();
    } catch (_) {}
  }
}

final reportVoiceProvider = Provider<ReportVoice>((ref) {
  final voice = DeviceReportVoice();
  ref.onDispose(voice.stop);
  return voice;
});

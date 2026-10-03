import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:just_audio/just_audio.dart';

import 'feel_settings.dart';

/// The app's sound effects (made by tools/sounds/make_sounds.py).
enum Sound {
  tap('tap'),
  basket('basket'),
  right('right'),
  tryAgain('try_again'),
  celebrate('celebrate');

  const Sound(this.file);
  final String file;

  String get asset => 'assets/sounds/$file.wav';
}

abstract class SoundPlayer {
  void play(Sound sound);
}

final soundPlayerProvider = Provider<SoundPlayer>((ref) {
  final player = JustAudioSounds();
  ref.onDispose(player.dispose);
  return player;
});

extension PlaySound on WidgetRef {
  /// Plays [sound] if the Sounds setting is on.
  void playSound(Sound sound) {
    if (read(soundsOnProvider)) read(soundPlayerProvider).play(sound);
  }
}

class JustAudioSounds implements SoundPlayer {
  final _players = <Sound, AudioPlayer>{};

  @override
  Future<void> play(Sound sound) async {
    try {
      final player = _players[sound] ??= AudioPlayer();
      if (player.audioSource == null) await player.setAsset(sound.asset);
      await player.seek(Duration.zero);
      await player.play();
    } catch (e) {
      debugPrint('Sound ${sound.file} could not play: $e');
    }
  }

  void dispose() {
    for (final p in _players.values) {
      p.dispose();
    }
  }
}

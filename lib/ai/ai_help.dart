import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../app/preferences.dart';

/// Mithu's AI help (Phase 10): on by default, and a parent can turn it off
/// in Settings. While it is off, nothing is sent to the AI server: typed
/// explanations are checked by their keywords on the phone, and photo
/// steps ask the student to type their answer.
class AiHelp extends Notifier<bool> {
  static const _key = 'aiHelp';

  @override
  bool build() => ref.read(sharedPreferencesProvider).getBool(_key) ?? true;

  Future<void> set(bool value) async {
    state = value;
    await ref.read(sharedPreferencesProvider).setBool(_key, value);
  }
}

final aiHelpProvider = NotifierProvider<AiHelp, bool>(AiHelp.new);

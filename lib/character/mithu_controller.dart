import 'dart:async';

import 'package:flutter/foundation.dart';

import 'mithu.dart';

/// What Mithu is doing right now: the mood and, while a line is spoken,
/// how far the beak is open. Steps and screens change Mithu only through
/// this, so the drawing behind [MithuView] can be swapped (for Rive) later.
class MithuController extends ChangeNotifier {
  MithuController({MithuMood mood = MithuMood.idle})
    : _base = mood,
      _mood = mood;

  /// How long Mithu looks curious after a wrong answer before encouraging.
  static const curiousFor = Duration(milliseconds: 1500);

  MithuMood _base;
  MithuMood _mood;
  Timer? _timer;
  var _speaking = false;

  /// Beak opening, 0 to 1, while speaking (set by the narration player).
  final mouth = ValueNotifier<double>(0);

  MithuMood get mood => _speaking ? MithuMood.talking : _mood;
  bool get speaking => _speaking;

  /// The mood the lesson asks for; shown until an answer changes it.
  set base(MithuMood value) {
    if (value == _base) return;
    _base = value;
    _set(value);
  }

  /// Mithu reacts to an answer: happy when right; curious, then
  /// encouraging, when wrong. Never disappointed.
  void react({required bool correct}) {
    if (correct) {
      _set(MithuMood.happy);
    } else {
      _set(MithuMood.curious);
      _timer = Timer(curiousFor, () => _set(MithuMood.encouraging));
    }
  }

  void celebrate() => _set(MithuMood.celebrating);

  /// Back to the lesson's mood.
  void reset() => _set(_base);

  set speaking(bool value) {
    if (value == _speaking) return;
    _speaking = value;
    if (!value) mouth.value = 0;
    notifyListeners();
  }

  void _set(MithuMood value) {
    _timer?.cancel();
    _timer = null;
    _mood = value;
    notifyListeners();
  }

  @override
  void dispose() {
    _timer?.cancel();
    mouth.dispose();
    super.dispose();
  }
}

import 'package:flutter/widgets.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'preferences.dart';

/// The "Less movement" setting. When on (or when the phone's own
/// "remove animations" setting is on), the app sets
/// `MediaQuery.disableAnimations`, so every screen can simply check
/// [reduceMotion].
final lessMotionProvider = NotifierProvider<LessMotion, bool>(LessMotion.new);

class LessMotion extends Notifier<bool> {
  static const _key = 'lessMotion';

  @override
  bool build() => ref.read(sharedPreferencesProvider).getBool(_key) ?? false;

  Future<void> set(bool value) async {
    state = value;
    await ref.read(sharedPreferencesProvider).setBool(_key, value);
  }
}

/// True if animations should be skipped here.
bool reduceMotion(BuildContext context) =>
    MediaQuery.maybeDisableAnimationsOf(context) ?? false;

/// Turns animations off below this widget when "Less movement" is on.
class MotionScope extends ConsumerWidget {
  const MotionScope({super.key, required this.child});

  final Widget child;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    if (!ref.watch(lessMotionProvider)) return child;
    return MediaQuery(
      data: MediaQuery.of(context).copyWith(disableAnimations: true),
      child: child,
    );
  }
}

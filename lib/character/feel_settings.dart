import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../app/preferences.dart';
import '../app/theme/age_tier.dart';
import '../services/profiles.dart';

/// A yes/no setting for the child using the app (brothers and sisters
/// often share a phone). Its default follows the age tier until changed.
class _TierSwitch extends Notifier<bool> {
  _TierSwitch(this._key, this._defaultFor);

  final String _key;
  final bool Function(AgeTier) _defaultFor;

  String get _studentKey {
    final id = ref.read(currentStudentProvider)?.id;
    return id == null ? _key : '$_key.$id';
  }

  @override
  bool build() {
    ref.watch(currentStudentProvider);
    return ref.read(sharedPreferencesProvider).getBool(_studentKey) ??
        _defaultFor(ref.watch(ageTierProvider));
  }

  Future<void> set(bool value) async {
    state = value;
    await ref.read(sharedPreferencesProvider).setBool(_studentKey, value);
  }
}

/// Sound effects: on for Nursery to Grade 5, off for Grades 6 to 12.
final soundsOnProvider = NotifierProvider<_TierSwitch, bool>(
  () => _TierSwitch(
    'soundsOn',
    (tier) => tier == AgeTier.early || tier == AgeTier.primary,
  ),
);

/// Mithu on screen: off by default for Grades 9 to 12 (Phase 7 decision 5).
final mithuOnProvider = NotifierProvider<_TierSwitch, bool>(
  () => _TierSwitch('mithuOn', (tier) => tier != AgeTier.older),
);

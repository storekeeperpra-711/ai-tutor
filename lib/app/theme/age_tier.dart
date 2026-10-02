import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../preferences.dart';

/// The four age groups from the spec (Part C1). Names match the lesson
/// JSON `tier` field: early, primary, middle, older.
enum AgeTier { early, primary, middle, older }

/// The age tier used for the app's look. For now it is a developer setting;
/// later it will come from the signed-in student's grade (Phase 3).
final ageTierProvider = NotifierProvider<AgeTierController, AgeTier>(
  AgeTierController.new,
);

class AgeTierController extends Notifier<AgeTier> {
  static const _key = 'ageTier';

  @override
  AgeTier build() {
    final name = ref.read(sharedPreferencesProvider).getString(_key);
    return AgeTier.values.firstWhere(
      (t) => t.name == name,
      orElse: () => AgeTier.older,
    );
  }

  Future<void> setTier(AgeTier tier) async {
    state = tier;
    await ref.read(sharedPreferencesProvider).setString(_key, tier.name);
  }
}

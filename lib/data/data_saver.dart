import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../app/preferences.dart';
import '../services/connectivity.dart';

/// Data saver (Phase 10): on by default, because most families pay for
/// mobile data. While it is on, lesson videos download only on Wi-Fi or
/// when someone taps Download. Lesson text, progress and AI help are
/// small and still use mobile data.
class DataSaver extends Notifier<bool> {
  static const _key = 'dataSaver';

  @override
  bool build() => ref.read(sharedPreferencesProvider).getBool(_key) ?? true;

  Future<void> set(bool value) async {
    state = value;
    await ref.read(sharedPreferencesProvider).setBool(_key, value);
  }
}

final dataSaverProvider = NotifierProvider<DataSaver, bool>(DataSaver.new);

/// Whether videos may download by themselves right now.
final autoDownloadProvider = Provider<bool>(
  (ref) =>
      !ref.watch(dataSaverProvider) ||
      (ref.watch(onWifiProvider).value ?? false),
);

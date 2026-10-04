import 'dart:async';
import 'dart:convert';

import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../app/preferences.dart';
import '../mastery/skill_state.dart';
import '../services/connectivity.dart';

/// Bytes this app has sent and received since the phone started, from
/// Android (MainActivity.kt). Null where Android can't tell (and in tests).
typedef AppByteCounter = Future<int?> Function();

const _traffic = MethodChannel('pk.aitutor/traffic');

final appByteCounterProvider = Provider<AppByteCounter>(
  (ref) => () async {
    try {
      return await _traffic.invokeMethod<int>('bytes');
    } on Object {
      return null;
    }
  },
);

/// Data used over the last 7 days, in bytes.
typedef WeekUsage = ({int wifi, int mobile});

/// Counts the data the app uses, split into Wi-Fi and mobile data, for
/// the last 7 days (Phase 10). It reads Android's own count for the app
/// now and then, and gives what was used since the last reading to the
/// connection the phone was on. Stored in the settings store; nothing
/// leaves the phone.
class DataUsageMeter extends Notifier<WeekUsage> {
  static const _lastKey = 'data.last';
  static const _daysKey = 'data.days';

  /// Days kept, today included.
  static const days = 7;

  @override
  WeekUsage build() => _week(_load(), DateTime.now());

  Map<String, List<int>> _load() {
    final text = ref.read(sharedPreferencesProvider).getString(_daysKey);
    if (text == null) return {};
    try {
      return {
        for (final MapEntry(:key, :value)
            in (jsonDecode(text) as Map<String, dynamic>).entries)
          key: [for (final n in value as List) n as int],
      };
    } on Object {
      return {};
    }
  }

  WeekUsage _week(Map<String, List<int>> byDay, DateTime now) {
    final keep = _daysUpTo(now);
    var wifi = 0, mobile = 0;
    for (final MapEntry(:key, :value) in byDay.entries) {
      if (!keep.contains(key)) continue;
      wifi += value[0];
      mobile += value[1];
    }
    return (wifi: wifi, mobile: mobile);
  }

  Set<String> _daysUpTo(DateTime now) => {
    for (var i = 0; i < days; i++)
      dayKey(dayOf(now).subtract(Duration(days: i))),
  };

  /// Reads Android's count and gives the data used since the last reading
  /// to Wi-Fi or mobile data ([onWifi]: the connection it was used on).
  Future<void> sample({required bool onWifi, DateTime? now}) async {
    final total = await ref.read(appByteCounterProvider)();
    if (total == null || !ref.mounted) return;
    now ??= DateTime.now();
    final prefs = ref.read(sharedPreferencesProvider);
    final last = prefs.getInt(_lastKey);
    await prefs.setInt(_lastKey, total);
    if (last == null) return;
    // Android starts counting again from 0 when the phone restarts.
    final used = total >= last ? total - last : total;
    if (used == 0) return;

    final keep = _daysUpTo(now);
    final byDay = _load()..removeWhere((day, _) => !keep.contains(day));
    final today = byDay.putIfAbsent(dayKey(now), () => [0, 0]);
    today[onWifi ? 0 : 1] += used;
    await prefs.setString(_daysKey, jsonEncode(byDay));
    if (ref.mounted) state = _week(byDay, now);
  }
}

final dataUsageProvider = NotifierProvider<DataUsageMeter, WeekUsage>(
  DataUsageMeter.new,
);

/// Takes readings when the app starts, comes back, goes into the
/// background, and when the phone switches between Wi-Fi and mobile data.
/// Watched by the app's root widget.
final dataUsageSamplerProvider = Provider<void>((ref) {
  bool onWifi() => ref.read(onWifiProvider).value ?? false;
  Future<void> sample(bool wifi) =>
      ref.read(dataUsageProvider.notifier).sample(onWifi: wifi);

  ref.listen(onWifiProvider, (previous, next) {
    // Data used before the switch was on the old connection.
    unawaited(sample(previous?.value ?? next.value ?? false));
  });
  final lifecycle = AppLifecycleListener(
    onShow: () => unawaited(sample(onWifi())),
    onHide: () => unawaited(sample(onWifi())),
  );
  ref.onDispose(lifecycle.dispose);
  unawaited(sample(onWifi()));
});

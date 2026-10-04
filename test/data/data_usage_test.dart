import 'package:ai_tutor/app/preferences.dart';
import 'package:ai_tutor/data/data_saver.dart';
import 'package:ai_tutor/data/data_usage.dart';
import 'package:ai_tutor/services/connectivity.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  const mb = 1024 * 1024;
  int? androidCount;

  Future<ProviderContainer> make({
    Map<String, Object> prefs = const {},
    bool wifi = false,
  }) async {
    SharedPreferences.setMockInitialValues(prefs);
    final store = await SharedPreferences.getInstance();
    final container = ProviderContainer(
      overrides: [
        sharedPreferencesProvider.overrideWithValue(store),
        appByteCounterProvider.overrideWithValue(() async => androidCount),
        onWifiProvider.overrideWith((ref) => Stream.value(wifi)),
      ],
    );
    addTearDown(container.dispose);
    return container;
  }

  setUp(() => androidCount = null);

  group('data used', () {
    final day = DateTime(2026, 10, 4, 12);

    test('splits what was used between Wi-Fi and mobile data', () async {
      final container = await make();
      final meter = container.read(dataUsageProvider.notifier);

      androidCount = 100 * mb;
      await meter.sample(onWifi: false, now: day); // the first reading
      expect(container.read(dataUsageProvider), (wifi: 0, mobile: 0));

      androidCount = 103 * mb;
      await meter.sample(onWifi: false, now: day);
      androidCount = 113 * mb;
      await meter.sample(onWifi: true, now: day);
      expect(container.read(dataUsageProvider), (
        wifi: 10 * mb,
        mobile: 3 * mb,
      ));
    });

    test('a phone restart starts Android counting from 0 again', () async {
      final container = await make();
      final meter = container.read(dataUsageProvider.notifier);
      androidCount = 50 * mb;
      await meter.sample(onWifi: false, now: day);
      androidCount = 2 * mb;
      await meter.sample(onWifi: false, now: day);
      expect(container.read(dataUsageProvider).mobile, 2 * mb);
    });

    test('only the last 7 days count', () async {
      final container = await make();
      final meter = container.read(dataUsageProvider.notifier);
      androidCount = 0;
      await meter.sample(onWifi: false, now: day);
      androidCount = 4 * mb;
      await meter.sample(onWifi: false, now: day);
      androidCount = 5 * mb;
      await meter.sample(onWifi: false, now: day.add(const Duration(days: 6)));
      expect(container.read(dataUsageProvider).mobile, 5 * mb);

      // A week later the first day is gone.
      androidCount = 6 * mb;
      await meter.sample(onWifi: false, now: day.add(const Duration(days: 7)));
      expect(container.read(dataUsageProvider).mobile, 2 * mb);
    });
  });

  group('data saver', () {
    test('is on by default: videos wait for Wi-Fi', () async {
      final container = await make();
      container.listen(onWifiProvider, (_, _) {});
      await container.read(onWifiProvider.future);
      expect(container.read(dataSaverProvider), isTrue);
      expect(container.read(autoDownloadProvider), isFalse);
    });

    test('on Wi-Fi videos download by themselves', () async {
      final container = await make(wifi: true);
      container.listen(onWifiProvider, (_, _) {});
      await container.read(onWifiProvider.future);
      expect(container.read(autoDownloadProvider), isTrue);
    });

    test('turned off, videos download on mobile data too', () async {
      final container = await make();
      await container.read(dataSaverProvider.notifier).set(false);
      expect(container.read(autoDownloadProvider), isTrue);
    });
  });
}

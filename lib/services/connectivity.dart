import 'package:connectivity_plus/connectivity_plus.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

/// True while the phone has a network connection (Wi-Fi or mobile data).
/// It can be true without real internet; the sync queue handles that.
final onlineProvider = StreamProvider<bool>((ref) async* {
  final connectivity = Connectivity();
  bool hasNetwork(List<ConnectivityResult> results) =>
      results.any((r) => r != ConnectivityResult.none);
  yield hasNetwork(await connectivity.checkConnectivity());
  yield* connectivity.onConnectivityChanged.map(hasNetwork);
});

/// True while the phone is on Wi-Fi (or a cable), where data is usually
/// free; false on mobile data or offline (Phase 10, Data saver).
final onWifiProvider = StreamProvider<bool>((ref) async* {
  final connectivity = Connectivity();
  bool onWifi(List<ConnectivityResult> results) => results.any(
    (r) => r == ConnectivityResult.wifi || r == ConnectivityResult.ethernet,
  );
  yield onWifi(await connectivity.checkConnectivity());
  yield* connectivity.onConnectivityChanged.map(onWifi);
});

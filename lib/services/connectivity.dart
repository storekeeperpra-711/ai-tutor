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

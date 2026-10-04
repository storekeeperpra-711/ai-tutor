import 'package:flutter/widgets.dart';

/// Pictures kept in memory, at most (Flutter's default is 100 MB, too
/// much for a 2 GB phone running a WebView or video at the same time).
const imageCacheBytes = 40 * 1024 * 1024;

/// Firestore's copy of data on the phone, at most (default 100 MB).
/// Old data is removed first; writes waiting to be sent are never lost.
const firestoreCacheBytes = 40 * 1024 * 1024;

/// Sets the memory limits and frees cached pictures when Android says
/// memory is low (Phase 10). Call once at start-up.
void applyMemoryLimits() {
  PaintingBinding.instance.imageCache.maximumSizeBytes = imageCacheBytes;
  WidgetsBinding.instance.addObserver(_MemoryPressure());
}

class _MemoryPressure with WidgetsBindingObserver {
  @override
  void didHaveMemoryPressure() {
    PaintingBinding.instance.imageCache
      ..clear()
      ..clearLiveImages();
  }
}

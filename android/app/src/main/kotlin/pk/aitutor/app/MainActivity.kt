package pk.aitutor.app

import android.net.TrafficStats
import android.os.Process
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel

class MainActivity : FlutterActivity() {
    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        // Bytes this app has sent and received since the phone started
        // (Phase 10: the data-used counter). Null when Android can't tell.
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, "pk.aitutor/traffic")
            .setMethodCallHandler { call, result ->
                if (call.method == "bytes") {
                    val uid = Process.myUid()
                    val received = TrafficStats.getUidRxBytes(uid)
                    val sent = TrafficStats.getUidTxBytes(uid)
                    val unsupported = TrafficStats.UNSUPPORTED.toLong()
                    if (received == unsupported || sent == unsupported) {
                        result.success(null)
                    } else {
                        result.success(received + sent)
                    }
                } else {
                    result.notImplemented()
                }
            }
    }
}

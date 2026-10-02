import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

import 'sim_host.dart';

/// One HTML simulation from assets/sims/ (spec C, simulation protocol).
///
/// - Calls `initSim(config)` when the page has loaded.
/// - Listens on the `TutorBridge` JavaScript channel.
/// - Blocks every navigation away from the simulation file.
///
/// The WebView exists only while this step is on screen, so there is
/// never more than one, and it is disposed with the step.
class WebSimView extends StatefulWidget {
  const WebSimView({super.key, required this.args});

  final SimArgs args;

  @override
  State<WebSimView> createState() => _WebSimViewState();
}

class _WebSimViewState extends State<WebSimView> {
  late final WebViewController _controller;
  late final String _asset = 'assets/sims/${widget.args.step.src}';

  @override
  void initState() {
    super.initState();
    _controller = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setBackgroundColor(Colors.white)
      ..addJavaScriptChannel('TutorBridge', onMessageReceived: _onMessage)
      ..setNavigationDelegate(
        NavigationDelegate(
          onNavigationRequest: (request) => isSimUrl(request.url, _asset)
              ? NavigationDecision.navigate
              : NavigationDecision.prevent,
          onPageFinished: (_) => unawaited(_start()),
          onWebResourceError: (error) {
            if (error.isForMainFrame ?? true) {
              widget.args.onEvent(
                SimEvent('error', {'message': error.description}),
              );
            }
          },
        ),
      );
    unawaited(_controller.loadFlutterAsset(_asset));
  }

  Future<void> _start() async {
    try {
      await _controller.runJavaScript(
        'initSim(${jsonEncode(widget.args.config)});',
      );
    } on Object catch (e) {
      widget.args.onEvent(SimEvent('error', {'message': '$e'}));
    }
  }

  void _onMessage(JavaScriptMessage message) {
    final event = parseSimMessage(message.message);
    if (event != null && mounted) widget.args.onEvent(event);
  }

  @override
  Widget build(BuildContext context) => WebViewWidget(controller: _controller);
}

/// True only for the simulation file itself (in the app's assets).
bool isSimUrl(String url, String asset) {
  final uri = Uri.tryParse(url);
  if (uri == null || uri.hasQuery || uri.hasFragment) return false;
  return (uri.scheme == 'file' || uri.scheme == 'asset') &&
      uri.path.endsWith('/$asset');
}

/// Reads a TutorBridge message: `{"event": "...", "data": {...}}`.
/// Anything else is ignored.
SimEvent? parseSimMessage(String message) {
  try {
    final json = jsonDecode(message);
    if (json is! Map<String, dynamic>) return null;
    final event = json['event'];
    final data = json['data'] ?? const <String, dynamic>{};
    if (event is! String || data is! Map<String, dynamic>) return null;
    return SimEvent(event, data);
  } on FormatException {
    return null;
  }
}

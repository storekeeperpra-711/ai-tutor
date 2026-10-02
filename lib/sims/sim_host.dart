import 'package:flutter/widgets.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../models/lesson_step.dart';
import 'web_sim_view.dart';

/// What a simulation tells the step: `ready`, `result` (with data) or
/// `error`. The same for WebView simulations and native interactives.
class SimEvent {
  const SimEvent(this.event, [this.data = const {}]);

  final String event;
  final Map<String, dynamic> data;
}

typedef SimListener = void Function(SimEvent event);

/// Everything a simulation needs to start.
class SimArgs {
  const SimArgs({
    required this.step,
    required this.language,
    required this.onEvent,
    this.reduceMotion = false,
  });

  final SimStep step;

  /// en or ur.
  final String language;
  final SimListener onEvent;

  /// "Less movement": simulations should skip decorative animation.
  final bool reduceMotion;

  Map<String, dynamic> get params => step.params;

  /// The config passed to `initSim` in a WebView simulation.
  Map<String, dynamic> get config => {
    'lang': language,
    'reduce_motion': reduceMotion,
    ...step.params,
  };
}

typedef SimBuilder = Widget Function(SimArgs args);

/// Builds the WebView for `renderer: webview`. A provider, so widget
/// tests (which have no WebView) can swap in a fake.
final webSimBuilderProvider = Provider<SimBuilder>(
  (ref) =>
      (args) => WebSimView(args: args),
);

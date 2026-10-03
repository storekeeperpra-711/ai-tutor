import 'package:flutter/material.dart';

import '../../l10n/app_localizations.dart';
import '../../lessons/steps_screen.dart';
import '../../models/lesson_step.dart';
import '../../models/localized_text.dart';

/// Every simulation and native interactive with example settings, to try
/// them on a real phone (developer builds only).
class SimGalleryScreen extends StatelessWidget {
  const SimGalleryScreen({super.key});

  static const _examples = <(String, String, Map<String, dynamic>)>[
    ('webview', 'roti_strips.html', {'rotis': 2, 'piece': 4}),
    ('webview', 'falling_objects.html', {'height': 2}),
    ('native', 'fraction_bars', {'wholes': 2}),
    ('native', 'balance_scale', {'equation': '2x + 3 = 11'}),
    ('native', 'atom_balancer', {'equation': 'CH4 + O2 -> CO2 + H2O'}),
    ('native', 'inequality_line', {'min': -6, 'max': 6}),
    ('native', 'number_line', {'min': 0, 'max': 3, 'step': 0.5}),
    ('native', 'graph_plotter', {'size': 5}),
  ];

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(l10n.simGalleryTitle)),
      body: ListView(
        children: [
          for (final (renderer, name, params) in _examples)
            ListTile(
              key: Key('gallery-$name'),
              leading: Icon(
                renderer == 'webview' ? Icons.public_off : Icons.widgets,
              ),
              title: Text(name),
              subtitle: Text('$renderer  $params'),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute<void>(
                  builder: (_) => StepsScreen(
                    title: name,
                    lessonId: 'dev-sim-gallery',
                    steps: [
                      SimStep(
                        id: 'try',
                        type: 'sim',
                        renderer: renderer,
                        src: renderer == 'webview' ? name : null,
                        simId: renderer == 'native' ? name : null,
                        params: params,
                        prompt: const LocalizedText(
                          en: 'Try it out.',
                          ur: 'آزما کر دیکھیں۔',
                        ),
                      ),
                    ],
                    onStepDone: (_, _) async {},
                  ),
                ),
              ),
            ),
        ],
      ),
    );
  }
}

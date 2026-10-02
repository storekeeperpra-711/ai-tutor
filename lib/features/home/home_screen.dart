import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../l10n/app_localizations.dart';

/// Placeholder home screen. The real home screens per age tier come in
/// Phase 7.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return Scaffold(
      appBar: AppBar(
        title: Text(l10n.appTitle),
        actions: [
          IconButton(
            icon: const Icon(Icons.settings),
            tooltip: l10n.settingsTitle,
            onPressed: () => context.push('/settings'),
          ),
        ],
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                l10n.homeWelcome,
                style: Theme.of(context).textTheme.headlineSmall,
                textAlign: TextAlign.center,
              ),
              if (kDebugMode) ...[
                const SizedBox(height: 24),
                FilledButton(
                  key: const Key('open-previewer'),
                  onPressed: () => context.push('/dev/lessons'),
                  child: Text(l10n.lessonsPreviewTitle),
                ),
                const SizedBox(height: 12),
                OutlinedButton(
                  onPressed: () => context.push('/debug/urdu'),
                  child: Text(l10n.urduTestTitle),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }
}

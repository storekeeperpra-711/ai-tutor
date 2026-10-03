import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../app/locale_controller.dart';
import '../../app/motion.dart';
import '../../app/theme/age_tier.dart';
import '../../character/feel_settings.dart';
import '../../l10n/app_localizations.dart';

/// Language names are always shown in their own language, so a student
/// can find their language even if the app is in the other one.
const _languageNames = {'en': 'English', 'ur': 'اردو'};

class SettingsScreen extends ConsumerWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final locale = ref.watch(localeProvider);
    final tier = ref.watch(ageTierProvider);
    final heading = Theme.of(context).textTheme.titleMedium;

    return Scaffold(
      appBar: AppBar(title: Text(l10n.settingsTitle)),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Text(l10n.languageLabel, style: heading),
          RadioGroup<String>(
            groupValue: locale.languageCode,
            onChanged: (code) {
              if (code != null) {
                ref.read(localeProvider.notifier).setLocale(Locale(code));
              }
            },
            child: Column(
              children: [
                for (final l in supportedLocales)
                  RadioListTile<String>(
                    key: Key('language-${l.languageCode}'),
                    value: l.languageCode,
                    title: Text(_languageNames[l.languageCode]!),
                  ),
              ],
            ),
          ),
          const Divider(height: 32),
          SwitchListTile(
            key: const Key('less-motion'),
            title: Text(l10n.lessMotion),
            subtitle: Text(l10n.lessMotionHint),
            value: ref.watch(lessMotionProvider),
            onChanged: (v) => ref.read(lessMotionProvider.notifier).set(v),
          ),
          SwitchListTile(
            key: const Key('sounds-on'),
            title: Text(l10n.soundsSetting),
            subtitle: Text(l10n.soundsSettingHint),
            value: ref.watch(soundsOnProvider),
            onChanged: (v) => ref.read(soundsOnProvider.notifier).set(v),
          ),
          SwitchListTile(
            key: const Key('mithu-on'),
            title: Text(l10n.mithuSetting),
            subtitle: Text(l10n.mithuSettingHint),
            value: ref.watch(mithuOnProvider),
            onChanged: (v) => ref.read(mithuOnProvider.notifier).set(v),
          ),
          ListTile(
            key: const Key('open-ai-costs'),
            leading: const Icon(Icons.payments_outlined),
            title: Text(l10n.aiCostsTitle),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => context.push('/ai-costs'),
          ),
          const Divider(height: 32),
          Text(l10n.ageTierLabel, style: heading),
          RadioGroup<AgeTier>(
            groupValue: tier,
            onChanged: (t) {
              if (t != null) ref.read(ageTierProvider.notifier).setTier(t);
            },
            child: Column(
              children: [
                for (final t in AgeTier.values)
                  RadioListTile<AgeTier>(
                    key: Key('tier-${t.name}'),
                    value: t,
                    title: Text(_tierName(l10n, t)),
                  ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

String _tierName(AppLocalizations l10n, AgeTier tier) => switch (tier) {
  AgeTier.early => l10n.tierEarly,
  AgeTier.primary => l10n.tierPrimary,
  AgeTier.middle => l10n.tierMiddle,
  AgeTier.older => l10n.tierOlder,
};

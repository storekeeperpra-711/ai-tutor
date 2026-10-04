import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../ai/ai_help.dart';
import '../../app/locale_controller.dart';
import '../../app/motion.dart';
import '../../app/theme/age_tier.dart';
import '../../character/feel_settings.dart';
import '../../data/data_saver.dart';
import '../../data/data_usage.dart';
import '../phone_check/phone_check_screen.dart' show megabytes;
import '../home/home_parts.dart';
import '../../l10n/app_localizations.dart';
import '../../review/review_store.dart';

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
      appBar: AppBar(
        // A long press opens the hidden Phone check screen (for testers).
        title: GestureDetector(
          key: const Key('settings-title'),
          onLongPress: () => context.push('/phone-check'),
          child: Text(l10n.settingsTitle),
        ),
      ),
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
          if (tier == AgeTier.middle || tier == AgeTier.older)
            const _ExamDateTile(),
          ListTile(
            key: const Key('open-ai-costs'),
            leading: const Icon(Icons.payments_outlined),
            title: Text(l10n.aiCostsTitle),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => context.push('/ai-costs'),
          ),
          if (ref.watch(reviewOfferedProvider))
            ListTile(
              key: const Key('open-review'),
              leading: const Icon(Icons.fact_check_outlined),
              title: Text(l10n.reviewTitle),
              trailing: const Icon(Icons.chevron_right),
              onTap: () => context.push('/review'),
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
          const Divider(height: 32),
          SwitchListTile(
            key: const Key('data-saver'),
            secondary: const Icon(Icons.data_saver_on),
            title: Text(l10n.dataSaver),
            subtitle: Text(l10n.dataSaverHelp),
            value: ref.watch(dataSaverProvider),
            onChanged: (v) => ref.read(dataSaverProvider.notifier).set(v),
          ),
          Padding(
            padding: const EdgeInsetsDirectional.only(start: 72, end: 16),
            child: Text(
              l10n.dataUsedThisWeek(
                megabytes(ref.watch(dataUsageProvider).mobile),
              ),
              key: const Key('data-used-mobile'),
            ),
          ),
          ListTile(
            key: const Key('open-downloads'),
            leading: const Icon(Icons.download_for_offline_outlined),
            title: Text(l10n.downloadsTitle),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => context.push('/downloads'),
          ),
          const Divider(height: 32),
          SwitchListTile(
            key: const Key('ai-help'),
            secondary: const Icon(Icons.auto_awesome_outlined),
            title: Text(l10n.aiHelpSetting),
            subtitle: Text(l10n.aiHelpSettingHint),
            value: ref.watch(aiHelpProvider),
            onChanged: (v) => ref.read(aiHelpProvider.notifier).set(v),
          ),
          ListTile(
            key: const Key('open-privacy'),
            leading: const Icon(Icons.privacy_tip_outlined),
            title: Text(l10n.privacyTitle),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => context.push('/privacy'),
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

/// The board exam date, for the countdown on the home screen.
class _ExamDateTile extends ConsumerWidget {
  const _ExamDateTile();

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final date = ref.watch(examDateProvider);
    final now = DateTime.now();
    return ListTile(
      key: const Key('exam-date'),
      leading: const Icon(Icons.event_rounded),
      title: Text(l10n.examDateSetting),
      subtitle: Text(
        date == null
            ? l10n.examDateNotSet
            : MaterialLocalizations.of(context).formatFullDate(date),
      ),
      trailing: date == null
          ? null
          : TextButton(
              key: const Key('exam-date-clear'),
              onPressed: () => ref.read(examDateProvider.notifier).set(null),
              child: Text(l10n.examDateClear),
            ),
      onTap: () async {
        final picked = await showDatePicker(
          context: context,
          initialDate: date ?? now.add(const Duration(days: 120)),
          firstDate: DateTime(now.year, now.month, now.day),
          lastDate: DateTime(now.year + 2, 12, 31),
        );
        if (picked != null) {
          await ref.read(examDateProvider.notifier).set(picked);
        }
      },
    );
  }
}

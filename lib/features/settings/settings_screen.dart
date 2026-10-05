import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../ai/ai_help.dart';
import '../../app/locale_controller.dart';
import '../../app/motion.dart';
import '../../app/motion_widgets.dart';
import '../../app/theme/app_theme.dart';
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

    return TintedBackground(
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          // A long press opens the hidden Phone check screen (for testers).
          title: GestureDetector(
            key: const Key('settings-title'),
            onLongPress: () => context.push('/phone-check'),
            child: Text(l10n.settingsTitle),
          ),
        ),
        // A short page, so every setting is built at once (and can be
        // scrolled to).
        body: SingleChildScrollView(
          padding: const EdgeInsets.fromLTRB(20, 8, 20, 24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              _Section(
                index: 0,
                title: l10n.languageLabel,
                children: [
                  Padding(
                    padding: const EdgeInsets.fromLTRB(12, 4, 12, 12),
                    child: Row(
                      children: [
                        for (final (i, l) in supportedLocales.indexed) ...[
                          if (i > 0) const SizedBox(width: 10),
                          Expanded(
                            child: _LanguageButton(
                              key: Key('language-${l.languageCode}'),
                              label: _languageNames[l.languageCode]!,
                              selected: locale.languageCode == l.languageCode,
                              onTap: () => ref
                                  .read(localeProvider.notifier)
                                  .setLocale(Locale(l.languageCode)),
                            ),
                          ),
                        ],
                      ],
                    ),
                  ),
                ],
              ),
              _Section(
                index: 1,
                children: [
                  SwitchListTile(
                    key: const Key('ai-help'),
                    secondary: const _IconTile(Icons.auto_awesome_outlined, 1),
                    title: Text(l10n.aiHelpSetting),
                    subtitle: Text(l10n.aiHelpSettingHint),
                    value: ref.watch(aiHelpProvider),
                    onChanged: (v) => ref.read(aiHelpProvider.notifier).set(v),
                  ),
                  SwitchListTile(
                    key: const Key('data-saver'),
                    secondary: const _IconTile(Icons.data_saver_on, 0),
                    title: Text(l10n.dataSaver),
                    subtitle: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(l10n.dataSaverHelp),
                        Text(
                          l10n.dataUsedThisWeek(
                            megabytes(ref.watch(dataUsageProvider).mobile),
                          ),
                          key: const Key('data-used-mobile'),
                        ),
                      ],
                    ),
                    isThreeLine: true,
                    value: ref.watch(dataSaverProvider),
                    onChanged: (v) =>
                        ref.read(dataSaverProvider.notifier).set(v),
                  ),
                  SwitchListTile(
                    key: const Key('sounds-on'),
                    secondary: const _IconTile(Icons.volume_up_rounded, 2),
                    title: Text(l10n.soundsSetting),
                    subtitle: Text(l10n.soundsSettingHint),
                    value: ref.watch(soundsOnProvider),
                    onChanged: (v) =>
                        ref.read(soundsOnProvider.notifier).set(v),
                  ),
                  SwitchListTile(
                    key: const Key('mithu-on'),
                    secondary: const _IconTile(Icons.flutter_dash, 0),
                    title: Text(l10n.mithuSetting),
                    subtitle: Text(l10n.mithuSettingHint),
                    value: ref.watch(mithuOnProvider),
                    onChanged: (v) => ref.read(mithuOnProvider.notifier).set(v),
                  ),
                  SwitchListTile(
                    key: const Key('less-motion'),
                    secondary: const _IconTile(
                      Icons.motion_photos_paused_outlined,
                      3,
                    ),
                    title: Text(l10n.lessMotion),
                    subtitle: Text(l10n.lessMotionHint),
                    value: ref.watch(lessMotionProvider),
                    onChanged: (v) =>
                        ref.read(lessMotionProvider.notifier).set(v),
                  ),
                ],
              ),
              _Section(
                index: 2,
                children: [
                  ListTile(
                    key: const Key('open-downloads'),
                    leading: const _IconTile(
                      Icons.download_for_offline_outlined,
                      3,
                    ),
                    title: Text(l10n.downloadsTitle),
                    trailing: const Icon(Icons.chevron_right),
                    onTap: () => context.push('/downloads'),
                  ),
                  ListTile(
                    key: const Key('open-privacy'),
                    leading: const _IconTile(Icons.privacy_tip_outlined, 1),
                    title: Text(l10n.privacyTitle),
                    trailing: const Icon(Icons.chevron_right),
                    onTap: () => context.push('/privacy'),
                  ),
                  if (tier == AgeTier.middle || tier == AgeTier.older)
                    const _ExamDateTile(),
                  ListTile(
                    key: const Key('open-ai-costs'),
                    leading: const _IconTile(Icons.payments_outlined, 0),
                    title: Text(l10n.aiCostsTitle),
                    trailing: const Icon(Icons.chevron_right),
                    onTap: () => context.push('/ai-costs'),
                  ),
                  if (ref.watch(reviewOfferedProvider))
                    ListTile(
                      key: const Key('open-review'),
                      leading: const _IconTile(Icons.fact_check_outlined, 4),
                      title: Text(l10n.reviewTitle),
                      trailing: const Icon(Icons.chevron_right),
                      onTap: () => context.push('/review'),
                    ),
                ],
              ),
              _Section(
                index: 3,
                title: l10n.ageTierLabel,
                children: [
                  RadioGroup<AgeTier>(
                    groupValue: tier,
                    onChanged: (t) {
                      if (t != null) {
                        ref.read(ageTierProvider.notifier).setTier(t);
                      }
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
            ],
          ),
        ),
      ),
    );
  }
}

/// A white rounded card holding one group of settings.
class _Section extends StatelessWidget {
  const _Section({required this.index, required this.children, this.title});

  final int index;
  final String? title;
  final List<Widget> children;

  @override
  Widget build(BuildContext context) => EnterAnimation(
    index: index,
    child: Card(
      margin: const EdgeInsets.only(bottom: 14),
      clipBehavior: Clip.antiAlias,
      child: Padding(
        padding: const EdgeInsets.symmetric(vertical: 6),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            if (title != null)
              Padding(
                padding: const EdgeInsets.fromLTRB(16, 10, 16, 4),
                child: Text(
                  title!,
                  style: Theme.of(context).textTheme.titleMedium,
                ),
              ),
            ...children,
          ],
        ),
      ),
    ),
  );
}

/// A setting's icon on a pastel square.
class _IconTile extends StatelessWidget {
  const _IconTile(this.icon, this.colorIndex);

  final IconData icon;
  final int colorIndex;

  @override
  Widget build(BuildContext context) {
    final colors = AppColors.tiles[colorIndex % AppColors.tiles.length];
    return Container(
      width: 40,
      height: 40,
      decoration: BoxDecoration(
        color: colors.soft,
        borderRadius: BorderRadius.circular(12),
      ),
      child: Icon(icon, color: colors.strong, size: 22),
    );
  }
}

/// One language, as a big button: filled when chosen.
class _LanguageButton extends StatelessWidget {
  const _LanguageButton({
    super.key,
    required this.label,
    required this.selected,
    required this.onTap,
  });

  final String label;
  final bool selected;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) => Semantics(
    selected: selected,
    button: true,
    child: Pressable(
      child: Material(
        color: selected ? AppColors.lilac : AppColors.lilacSoft,
        borderRadius: BorderRadius.circular(AppRadius.button),
        child: InkWell(
          borderRadius: BorderRadius.circular(AppRadius.button),
          onTap: onTap,
          child: SizedBox(
            height: 52,
            child: Center(
              child: Text(
                label,
                style: TextStyle(
                  fontSize: 17,
                  fontWeight: FontWeight.w900,
                  color: selected ? Colors.white : AppColors.ink,
                ),
              ),
            ),
          ),
        ),
      ),
    ),
  );
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
      leading: const _IconTile(Icons.event_rounded, 2),
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

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../app/locale_controller.dart';
import '../../l10n/app_localizations.dart';

/// App-bar button that flips between English and Urdu.
class LanguageToggle extends ConsumerWidget {
  const LanguageToggle({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final isUrdu = ref.watch(localeProvider).languageCode == 'ur';
    return TextButton(
      key: const Key('language-toggle'),
      onPressed: () => ref
          .read(localeProvider.notifier)
          .setLocale(Locale(isUrdu ? 'en' : 'ur')),
      child: Tooltip(
        message: AppLocalizations.of(context).switchLanguage,
        // Shows the language you switch to, in that language.
        child: Text(isUrdu ? 'English' : 'اردو'),
      ),
    );
  }
}

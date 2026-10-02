import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../l10n/app_localizations.dart';
import 'locale_controller.dart';
import 'router.dart';
import 'theme/age_tier.dart';
import 'theme/app_theme.dart';

/// The root widget: wires together routing, theme and language.
///
/// Setting `locale` to Urdu makes Flutter lay out every screen right-to-left
/// automatically, so screens should use start/end (not left/right) spacing.
class AiTutorApp extends ConsumerWidget {
  const AiTutorApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final locale = ref.watch(localeProvider);
    final tier = ref.watch(ageTierProvider);

    return MaterialApp.router(
      onGenerateTitle: (context) => AppLocalizations.of(context).appTitle,
      routerConfig: ref.watch(routerProvider),
      theme: buildTheme(tier, locale),
      locale: locale,
      supportedLocales: supportedLocales,
      // A "DEV" ribbon so the test version is never mistaken for the real one.
      builder: appFlavor == 'dev'
          ? (context, child) => Banner(
              message: 'DEV',
              location: BannerLocation.topStart,
              child: child!,
            )
          : null,
      debugShowCheckedModeBanner: false,
      localizationsDelegates: const [
        AppLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
    );
  }
}

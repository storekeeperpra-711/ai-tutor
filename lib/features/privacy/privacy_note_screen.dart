import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/app_localizations.dart';
import '../../reports/report_voice.dart';

/// The parts of the privacy note, as (heading, paragraph); the first has
/// no heading.
List<(String?, String)> privacyNoteParts(AppLocalizations l10n) => [
  (null, l10n.privacyIntro),
  (l10n.privacyKeptTitle, l10n.privacyKept),
  (l10n.privacyWhereTitle, l10n.privacyWhere),
  (l10n.privacyAiTitle, l10n.privacyAi),
  (l10n.privacyCrashTitle, l10n.privacyCrash),
  (l10n.privacyWhoTitle, l10n.privacyWho),
  (l10n.privacyHowLongTitle, l10n.privacyHowLong),
  (l10n.privacySafetyTitle, l10n.privacySafety),
  (l10n.privacyChoicesTitle, l10n.privacyChoices),
];

/// The privacy note for parents (Phase 10): what is kept, where, who sees
/// it and for how long. Listen reads it aloud with the phone's own voice,
/// for parents who don't read; without an Urdu voice it reads the English.
class PrivacyNoteScreen extends ConsumerStatefulWidget {
  const PrivacyNoteScreen({super.key});

  @override
  ConsumerState<PrivacyNoteScreen> createState() => _PrivacyNoteScreenState();
}

class _PrivacyNoteScreenState extends ConsumerState<PrivacyNoteScreen> {
  late final ReportVoice _speaker = ref.read(reportVoiceProvider);

  /// The language the phone can read the note in, or null if none.
  String? _voiceLanguage;
  var _checked = false;

  /// The part being read, or null.
  int? _reading;
  var _stopped = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (!_checked) {
      _checked = true;
      unawaited(_checkVoice());
    }
  }

  Future<void> _checkVoice() async {
    final lang = Localizations.localeOf(context).languageCode;
    final voice = await _speaker.canSpeak(lang)
        ? lang
        : lang != 'en' && await _speaker.canSpeak('en')
        ? 'en'
        : null;
    if (mounted) setState(() => _voiceLanguage = voice);
  }

  @override
  void dispose() {
    _stopped = true;
    unawaited(_speaker.stop());
    super.dispose();
  }

  Future<void> _listen() async {
    final lang = _voiceLanguage!;
    final parts = privacyNoteParts(lookupAppLocalizations(Locale(lang)));
    _stopped = false;
    for (var i = 0; i < parts.length && !_stopped; i++) {
      setState(() => _reading = i);
      final (heading, text) = parts[i];
      await _speaker.speak(heading == null ? text : '$heading. $text', lang);
      if (!mounted) return;
    }
    setState(() => _reading = null);
  }

  Future<void> _stop() async {
    _stopped = true;
    await _speaker.stop();
    if (mounted) setState(() => _reading = null);
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final colors = Theme.of(context).colorScheme;
    return Scaffold(
      appBar: AppBar(title: Text(l10n.privacyTitle)),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          if (_voiceLanguage != null)
            Padding(
              padding: const EdgeInsets.only(bottom: 16),
              child: _reading == null
                  ? FilledButton.icon(
                      key: const Key('privacy-listen'),
                      style: FilledButton.styleFrom(
                        minimumSize: const Size.fromHeight(64),
                      ),
                      icon: const Icon(Icons.volume_up_rounded, size: 32),
                      label: Text(l10n.privacyListen),
                      onPressed: _listen,
                    )
                  : OutlinedButton.icon(
                      key: const Key('privacy-stop'),
                      style: OutlinedButton.styleFrom(
                        minimumSize: const Size.fromHeight(64),
                      ),
                      icon: const Icon(Icons.stop_rounded, size: 32),
                      label: Text(l10n.privacyStop),
                      onPressed: _stop,
                    ),
            ),
          for (final (i, (heading, text)) in privacyNoteParts(l10n).indexed)
            AnimatedContainer(
              key: Key('privacy-part-$i'),
              duration: const Duration(milliseconds: 200),
              margin: const EdgeInsets.only(bottom: 12),
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: _reading == i
                    ? colors.primaryContainer
                    : Colors.transparent,
                borderRadius: BorderRadius.circular(8),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  if (heading != null)
                    Padding(
                      padding: const EdgeInsets.only(bottom: 4),
                      child: Text(heading, style: textTheme.titleMedium),
                    ),
                  Text(text, style: textTheme.bodyLarge),
                ],
              ),
            ),
        ],
      ),
    );
  }
}

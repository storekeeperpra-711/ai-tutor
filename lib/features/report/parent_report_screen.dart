import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/app_localizations.dart';
import '../../reports/parent_report.dart';
import '../../reports/report_voice.dart';
import '../../services/auth_service.dart';
import '../../services/local_db.dart';
import '../../services/mastery_service.dart';
import '../../services/profiles.dart';
import '../../services/remote_store.dart';

/// A child's report for the last 7 days, made on the phone.
final parentReportProvider = FutureProvider.autoDispose
    .family<ParentReport, String>((ref, studentId) async {
      final db = ref.watch(localDbProvider);
      return buildParentReport(
        states: await db.skillStatesOf(studentId),
        progress: await db.progressOf(studentId),
        steps: await db.stepResultsOf(studentId),
        curriculum: await ref.watch(curriculumProvider.future),
        now: DateTime.now(),
      );
    });

/// Mithu's AI note from Sunday, when there is one and the phone is online.
final mithuNoteProvider = FutureProvider.autoDispose
    .family<WeeklyReport?, String>((ref, studentId) async {
      final user = ref.watch(authServiceProvider).currentUser;
      if (user == null) return null;
      final reports = await ref
          .watch(remoteStoreProvider)
          .fetchReports(user.uid, studentId);
      return reports.firstOrNull;
    });

/// The parent report (Phase 9, task 9.1): big pictures for each part, and
/// a big Listen button that reads it aloud with the phone's own voice,
/// one sentence at a time, highlighting the sentence being read. Works
/// offline and uses no AI.
class ParentReportScreen extends ConsumerStatefulWidget {
  const ParentReportScreen({super.key, required this.studentId});

  final String studentId;

  @override
  ConsumerState<ParentReportScreen> createState() => _ParentReportScreenState();
}

/// Which voice the phone has for the app's language.
enum _Voice { checking, own, english, none }

class _ParentReportScreenState extends ConsumerState<ParentReportScreen> {
  var _voice = _Voice.checking;

  /// The sentence being read, or null.
  int? _reading;
  var _stopped = false;
  late final ReportVoice _speaker = ref.read(reportVoiceProvider);

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (_voice == _Voice.checking) unawaited(_checkVoice());
  }

  Future<void> _checkVoice() async {
    final lang = Localizations.localeOf(context).languageCode;
    final voice = await _speaker.canSpeak(lang)
        ? _Voice.own
        : lang != 'en' && await _speaker.canSpeak('en')
        ? _Voice.english
        : _Voice.none;
    if (mounted) setState(() => _voice = voice);
  }

  @override
  void dispose() {
    _stopped = true;
    unawaited(_speaker.stop());
    super.dispose();
  }

  Future<void> _listen(List<ReportSentence> sentences) async {
    _stopped = false;
    for (var i = 0; i < sentences.length && !_stopped; i++) {
      setState(() => _reading = i);
      final lang = _voice == _Voice.english
          ? 'en'
          : Localizations.localeOf(context).languageCode;
      await _speaker.speak(sentences[i].text, lang);
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
    final student = ref
        .watch(studentsProvider)
        .value
        ?.where((s) => s.id == widget.studentId)
        .firstOrNull;
    final report = ref.watch(parentReportProvider(widget.studentId)).value;
    final curriculum = ref.watch(curriculumProvider).value;
    if (student == null || report == null || curriculum == null) {
      return Scaffold(
        appBar: AppBar(),
        body: const Center(child: CircularProgressIndicator()),
      );
    }
    final name = student.firstName;
    final shown = reportSentences(
      report,
      l10n: l10n,
      name: name,
      curriculum: curriculum,
    );
    final spoken = _voice == _Voice.english
        ? reportSentences(
            report,
            l10n: lookupAppLocalizations(const Locale('en')),
            name: name,
            curriculum: curriculum,
          )
        : shown;
    final note = ref.watch(mithuNoteProvider(widget.studentId)).value;
    final urdu = Localizations.localeOf(context).languageCode == 'ur';

    Widget part(ReportPart p, IconData icon, String heading, Widget picture) {
      final colors = Theme.of(context).colorScheme;
      return Card(
        key: Key('report-part-${p.name}'),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Column(
                children: [
                  Icon(icon, size: 56, color: colors.primary),
                  const SizedBox(height: 8),
                  picture,
                ],
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      heading,
                      style: Theme.of(context).textTheme.titleLarge,
                    ),
                    for (final (i, s) in shown.indexed)
                      if (s.part == p)
                        AnimatedContainer(
                          key: Key('report-sentence-$i'),
                          duration: const Duration(milliseconds: 200),
                          margin: const EdgeInsets.only(top: 6),
                          padding: const EdgeInsets.all(6),
                          decoration: BoxDecoration(
                            color: _reading == i
                                ? colors.primaryContainer
                                : Colors.transparent,
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Text(
                            s.text,
                            style: Theme.of(context).textTheme.bodyLarge,
                          ),
                        ),
                  ],
                ),
              ),
            ],
          ),
        ),
      );
    }

    return Scaffold(
      appBar: AppBar(title: Text(l10n.reportTitle(name))),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          if (_reading == null)
            FilledButton.icon(
              key: const Key('report-listen'),
              style: FilledButton.styleFrom(
                minimumSize: const Size.fromHeight(72),
                textStyle: Theme.of(context).textTheme.headlineSmall,
              ),
              icon: const Icon(Icons.play_arrow, size: 40),
              label: Text(l10n.reportListen),
              onPressed: _voice == _Voice.own || _voice == _Voice.english
                  ? () => _listen(spoken)
                  : null,
            )
          else
            FilledButton.tonalIcon(
              key: const Key('report-stop'),
              style: FilledButton.styleFrom(
                minimumSize: const Size.fromHeight(72),
                textStyle: Theme.of(context).textTheme.headlineSmall,
              ),
              icon: const Icon(Icons.stop, size: 40),
              label: Text(l10n.reportStop),
              onPressed: _stop,
            ),
          if (_voice == _Voice.english || _voice == _Voice.none)
            Padding(
              padding: const EdgeInsets.only(top: 8),
              child: Text(
                _voice == _Voice.english
                    ? l10n.reportNoUrduVoice
                    : l10n.reportNoVoice,
                key: const Key('report-voice-help'),
              ),
            ),
          const SizedBox(height: 16),
          part(
            ReportPart.learned,
            Icons.star,
            l10n.reportLearnedHeading,
            _Stars(count: report.learned.length),
          ),
          part(
            ReportPart.practice,
            Icons.event,
            l10n.reportPracticeHeading,
            report.needsHelp.isEmpty
                ? const SizedBox.shrink()
                : Icon(
                    Icons.front_hand,
                    size: 32,
                    color: Theme.of(context).colorScheme.error,
                  ),
          ),
          part(
            ReportPart.home,
            Icons.home,
            l10n.reportHomeHeading,
            const SizedBox.shrink(),
          ),
          part(
            ReportPart.effort,
            Icons.directions_walk,
            l10n.reportEffortHeading,
            _Days(practised: report.daysPractised),
          ),
          if (note != null)
            Card(
              key: const Key('report-mithu-note'),
              child: ListTile(
                leading: const Icon(Icons.chat_bubble_outline, size: 40),
                title: Text(l10n.reportMithuNote),
                subtitle: Text(urdu ? note.noteUr : note.noteEn),
              ),
            ),
        ],
      ),
    );
  }
}

/// One star per skill learned this week (up to five), grey if none.
class _Stars extends StatelessWidget {
  const _Stars({required this.count});

  final int count;

  @override
  Widget build(BuildContext context) => Semantics(
    label: '$count',
    excludeSemantics: true,
    child: Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        for (var i = 0; i < (count == 0 ? 1 : count.clamp(1, 5)); i++)
          Icon(
            Icons.star,
            size: 20,
            color: count == 0 ? Colors.grey : Colors.amber,
          ),
      ],
    ),
  );
}

/// Seven dots, filled for each day practised (no streaks: the order of
/// the days doesn't matter).
class _Days extends StatelessWidget {
  const _Days({required this.practised});

  final int practised;

  @override
  Widget build(BuildContext context) => Semantics(
    label: '$practised / 7',
    excludeSemantics: true,
    child: SizedBox(
      width: 64,
      child: Wrap(
        spacing: 2,
        runSpacing: 2,
        children: [
          for (var i = 0; i < 7; i++)
            Icon(
              i < practised ? Icons.circle : Icons.circle_outlined,
              size: 12,
              color: Theme.of(context).colorScheme.primary,
            ),
        ],
      ),
    ),
  );
}

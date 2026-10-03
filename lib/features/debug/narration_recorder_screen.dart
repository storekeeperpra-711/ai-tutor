import 'dart:async';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:share_plus/share_plus.dart';

import '../../character/mithu_controller.dart';
import '../../character/narrator.dart';
import '../../character/voice_lines.dart';
import '../../character/voice_recorder.dart';
import '../../l10n/app_localizations.dart';
import '../../lessons/lesson_repository.dart';
import '../../models/lesson.dart';

/// Every Mithu line in every lesson, in each language.
List<VoiceLine> voiceLinesOf(Lesson lesson) {
  final steps = [
    ...lesson.steps,
    for (final alt in lesson.alternatives) ...alt.steps,
    for (final qs in lesson.questionBank.values)
      for (final q in qs) q.step,
    for (final q in lesson.reviewQuestions) q.step,
  ];
  return [
    for (final step in steps)
      if (step.character case final line?)
        for (final language in const ['ur', 'en'])
          VoiceLine(
            line: line,
            language: language,
            lessonId: lesson.id,
            stepId: step.id,
          ),
  ];
}

enum _Status { phone, app, missing }

/// Dev tool: record Mithu's lines on the phone, listen back, and send the
/// files so they can be added to the app (Phase 7 decision 3).
class NarrationRecorderScreen extends ConsumerStatefulWidget {
  const NarrationRecorderScreen({super.key});

  @override
  ConsumerState<NarrationRecorderScreen> createState() =>
      _NarrationRecorderScreenState();
}

class _NarrationRecorderScreenState
    extends ConsumerState<NarrationRecorderScreen> {
  static const maxLength = Duration(seconds: 30);

  final _mithu = MithuController();
  final _status = <String, _Status>{};
  var _missingOnly = true;
  String? _recording;
  final _levels = <double>[];
  StreamSubscription<double>? _levelSub;
  Timer? _limit;

  late final VoiceLibrary _library = ref.read(voiceLibraryProvider);
  late final Narrator _narrator = ref.read(narratorProvider);
  late final VoiceRecorder _recorder = ref.read(voiceRecorderProvider);

  @override
  void dispose() {
    _limit?.cancel();
    _levelSub?.cancel();
    if (_recording != null) _recorder.stop();
    _narrator.stop();
    _mithu.dispose();
    super.dispose();
  }

  Future<void> _refresh(List<VoiceLine> lines) async {
    final dir = await _library.recordings();
    for (final line in lines) {
      final name = line.fileName!;
      final status = File('${dir.path}/$name').existsSync()
          ? _Status.phone
          : await _library.find(line) != null
          ? _Status.app
          : _Status.missing;
      _status[name] = status;
    }
    if (mounted) setState(() {});
  }

  Future<void> _record(VoiceLine line) async {
    final l10n = AppLocalizations.of(context);
    final messenger = ScaffoldMessenger.of(context);
    await _narrator.stop();
    final dir = await _library.recordings();
    final name = line.fileName!;
    _levels.clear();
    if (!await _recorder.start('${dir.path}/$name')) {
      messenger.showSnackBar(SnackBar(content: Text(l10n.recorderNoMic)));
      return;
    }
    _levelSub = _recorder.levels.listen(_levels.add);
    // Stops by itself a little after the limit, so a forgotten Stop
    // doesn't fill the phone.
    _limit = Timer(maxLength + const Duration(seconds: 5), () => _stop(line));
    setState(() => _recording = name);
  }

  Future<void> _stop(VoiceLine line) async {
    final l10n = AppLocalizations.of(context);
    final messenger = ScaffoldMessenger.of(context);
    _limit?.cancel();
    if (_levelSub case final sub?) unawaited(sub.cancel());
    _levelSub = null;
    await _recorder.stop();
    final dir = await _library.recordings();
    final name = line.fileName!;
    final track = MouthTrack(List.of(_levels));
    File('${dir.path}/${mouthFileName(name)}')
        .writeAsStringSync(track.encode());
    if (track.length > maxLength) {
      messenger.showSnackBar(SnackBar(content: Text(l10n.recorderTooLong)));
    }
    setState(() {
      _recording = null;
      _status[name] = _Status.phone;
    });
  }

  Future<void> _delete(VoiceLine line) async {
    final dir = await _library.recordings();
    final name = line.fileName!;
    for (final file in [name, mouthFileName(name)]) {
      final f = File('${dir.path}/$file');
      if (f.existsSync()) f.deleteSync();
    }
    await _refresh([line]);
  }

  Future<void> _export() async {
    final l10n = AppLocalizations.of(context);
    final messenger = ScaffoldMessenger.of(context);
    final dir = await _library.recordings();
    final files = dir.listSync().whereType<File>().toList()
      ..sort((a, b) => a.path.compareTo(b.path));
    if (files.isEmpty) {
      messenger.showSnackBar(
        SnackBar(content: Text(l10n.recorderNothingToSend)),
      );
      return;
    }
    await SharePlus.instance.share(
      ShareParams(
        files: [for (final f in files) XFile(f.path)],
        text: l10n.recorderExportHelp,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final ids = ref.watch(lessonIdsProvider).value ?? const <String>[];
    final lines = [
      for (final id in ids)
        if (ref.watch(lessonProvider(id)).value case final lesson?)
          ...voiceLinesOf(lesson),
    ];
    final unknown = lines.where((l) => !_status.containsKey(l.fileName));
    if (unknown.isNotEmpty) _refresh(unknown.toList());
    final shown = [
      for (final line in lines)
        if (!_missingOnly ||
            _status[line.fileName] != _Status.app ||
            _recording == line.fileName)
          line,
    ];

    return Scaffold(
      appBar: AppBar(
        title: Text(l10n.recorderTitle),
        actions: [
          IconButton(
            key: const Key('recorder-export'),
            tooltip: l10n.recorderExport,
            icon: const Icon(Icons.ios_share),
            onPressed: _export,
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Text(l10n.recorderHelp, style: textTheme.bodyMedium),
          SwitchListTile(
            key: const Key('recorder-missing-only'),
            title: Text(l10n.recorderMissingOnly),
            value: _missingOnly,
            onChanged: (v) => setState(() => _missingOnly = v),
          ),
          for (final line in shown) _tile(context, line),
          const SizedBox(height: 16),
          Text(l10n.recorderExportHelp, style: textTheme.bodySmall),
        ],
      ),
    );
  }

  Widget _tile(BuildContext context, VoiceLine line) {
    final l10n = AppLocalizations.of(context);
    final textTheme = Theme.of(context).textTheme;
    final name = line.fileName!;
    final status = _status[name];
    final recording = _recording == name;
    final busy = _recording != null && !recording;
    return Card(
      key: Key('voice-$name'),
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              '${line.lessonId} · ${line.stepId} · ${line.language}',
              style: textTheme.labelSmall,
            ),
            const SizedBox(height: 4),
            Directionality(
              textDirection: line.language == 'ur'
                  ? TextDirection.rtl
                  : TextDirection.ltr,
              child: Text(line.text, style: textTheme.titleMedium),
            ),
            const SizedBox(height: 4),
            Text(switch (status) {
              _Status.phone => l10n.recorderStatusPhone,
              _Status.app => l10n.recorderStatusApp,
              _ => l10n.recorderStatusMissing,
            }, style: textTheme.labelMedium),
            Wrap(
              spacing: 8,
              children: [
                if (recording)
                  FilledButton.icon(
                    key: Key('stop-$name'),
                    style: FilledButton.styleFrom(
                      backgroundColor: Colors.red.shade700,
                    ),
                    icon: const Icon(Icons.stop),
                    label: Text(l10n.recorderStop),
                    onPressed: () => _stop(line),
                  )
                else
                  FilledButton.icon(
                    key: Key('record-$name'),
                    icon: const Icon(Icons.mic),
                    label: Text(l10n.recorderRecord),
                    onPressed: busy ? null : () => _record(line),
                  ),
                if (status != _Status.missing && !recording)
                  OutlinedButton.icon(
                    key: Key('play-$name'),
                    icon: const Icon(Icons.play_arrow),
                    label: Text(l10n.recorderPlay),
                    onPressed: busy ? null : () => _narrator.say(line, _mithu),
                  ),
                if (status == _Status.phone && !recording)
                  TextButton(
                    key: Key('delete-$name'),
                    onPressed: busy ? null : () => _delete(line),
                    child: Text(l10n.recorderDelete),
                  ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

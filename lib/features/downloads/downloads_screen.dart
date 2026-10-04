import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/app_localizations.dart';
import '../../lessons/lesson_repository.dart';
import '../../media/media_cache.dart';
import '../../models/lesson.dart';
import '../phone_check/phone_check_screen.dart' show megabytes;

/// A lesson with videos to download, in one language.
typedef LessonDownload = ({Lesson lesson, Set<String> links, int savedBytes});

/// Every lesson whose videos are links (not inside the app), with how much
/// of it is saved on the phone.
final lessonDownloadsProvider = FutureProvider.autoDispose
    .family<List<LessonDownload>, String>((ref, language) async {
      final cache = ref.watch(mediaCacheProvider);
      final result = <LessonDownload>[];
      for (final id in await ref.watch(lessonIdsProvider.future)) {
        final Lesson lesson;
        try {
          lesson = await ref.watch(lessonProvider(id).future);
        } on Object {
          continue;
        }
        final links = MediaCache.linksOf(lesson, language);
        if (links.isEmpty) continue;
        result.add((
          lesson: lesson,
          links: links,
          savedBytes: await cache.savedBytesOf(links),
        ));
      }
      return result;
    });

/// Downloads (Phase 10): a parent can save a lesson's videos before going
/// somewhere without signal, or remove them to free space. Downloads asked
/// for here run on any connection, Data saver or not.
class DownloadsScreen extends ConsumerStatefulWidget {
  const DownloadsScreen({super.key});

  @override
  ConsumerState<DownloadsScreen> createState() => _DownloadsScreenState();
}

class _DownloadsScreenState extends ConsumerState<DownloadsScreen> {
  /// Lessons downloading now.
  final _busy = <String>{};

  /// Lessons whose last download failed (shown on the lesson's row).
  final _failed = <String>{};

  Future<void> _change(LessonDownload d, {required bool save}) async {
    setState(() {
      _busy.add(d.lesson.id);
      _failed.remove(d.lesson.id);
    });
    try {
      final cache = ref.read(mediaCacheProvider);
      await (save ? cache.download(d.links) : cache.remove(d.links));
    } on Object {
      if (mounted) setState(() => _failed.add(d.lesson.id));
    } finally {
      if (mounted) {
        setState(() => _busy.remove(d.lesson.id));
        ref.invalidate(lessonDownloadsProvider);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final language = Localizations.localeOf(context).languageCode;
    final downloads = ref.watch(lessonDownloadsProvider(language));

    return Scaffold(
      appBar: AppBar(title: Text(l10n.downloadsTitle)),
      body: switch (downloads) {
        AsyncData(value: final list) when list.isEmpty => Padding(
          padding: const EdgeInsets.all(24),
          child: Text(
            l10n.downloadsNone,
            key: const Key('downloads-none'),
            style: Theme.of(context).textTheme.titleMedium,
          ),
        ),
        AsyncData(value: final list) => ListView(
          padding: const EdgeInsets.all(8),
          children: [
            Padding(
              padding: const EdgeInsets.all(8),
              child: Text(l10n.downloadsHelp),
            ),
            for (final d in list)
              ListTile(
                key: Key('download-${d.lesson.id}'),
                leading: Icon(
                  d.savedBytes > 0
                      ? Icons.download_done
                      : Icons.cloud_download_outlined,
                ),
                title: Text(d.lesson.title.inLanguage(language)),
                subtitle: _failed.contains(d.lesson.id)
                    ? Text(
                        l10n.downloadFailed,
                        key: Key('download-failed-${d.lesson.id}'),
                        style: TextStyle(
                          color: Theme.of(context).colorScheme.error,
                        ),
                      )
                    : Text(
                        d.savedBytes > 0
                            ? l10n.downloadSaved(megabytes(d.savedBytes))
                            : l10n.downloadNotSaved,
                      ),
                trailing: _busy.contains(d.lesson.id)
                    ? const SizedBox.square(
                        dimension: 24,
                        child: CircularProgressIndicator(strokeWidth: 3),
                      )
                    : d.savedBytes > 0
                    ? IconButton(
                        key: Key('download-remove-${d.lesson.id}'),
                        tooltip: l10n.downloadRemove,
                        icon: const Icon(Icons.delete_outline),
                        onPressed: () => _change(d, save: false),
                      )
                    : IconButton.filledTonal(
                        key: Key('download-save-${d.lesson.id}'),
                        tooltip: l10n.downloadSave,
                        icon: const Icon(Icons.download),
                        onPressed: () => _change(d, save: true),
                      ),
              ),
          ],
        ),
        AsyncError(:final error) => Center(child: Text('$error')),
        _ => const Center(child: CircularProgressIndicator()),
      },
    );
  }
}

import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../app/memory_limits.dart';
import '../../l10n/app_localizations.dart';
import '../../media/media_cache.dart';
import '../../services/local_db.dart';

/// The app's memory use in bytes: now, and the most it has used since
/// it started. A provider, so tests can give fixed numbers.
final memoryUseProvider = Provider<({int now, int most}) Function()>(
  (ref) =>
      () => (now: ProcessInfo.currentRss, most: ProcessInfo.maxRss),
);

/// What the Phone check screen shows.
typedef PhoneCheck = ({
  int memoryNow,
  int memoryMost,
  int pictures,
  int savedMedia,
  int downloadedLessons,
});

final phoneCheckProvider = FutureProvider.autoDispose<PhoneCheck>((ref) async {
  final memory = ref.watch(memoryUseProvider)();
  return (
    memoryNow: memory.now,
    memoryMost: memory.most,
    pictures: PaintingBinding.instance.imageCache.currentSizeBytes,
    savedMedia: await ref.watch(mediaCacheProvider).usedBytes(),
    downloadedLessons:
        (await ref.watch(localDbProvider).allDownloadedLessons()).length,
  );
});

/// "123.4 MB".
String megabytes(int bytes) =>
    '${(bytes / (1024 * 1024)).toStringAsFixed(1)} MB';

/// A hidden screen for Shahid and testers (Phase 10): how much memory and
/// storage the app uses on this phone. Opened by a long press on the
/// Settings title.
class PhoneCheckScreen extends ConsumerWidget {
  const PhoneCheckScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final check = ref.watch(phoneCheckProvider);

    Widget row(String key, IconData icon, String title, String value) =>
        ListTile(
          key: Key('phone-check-$key'),
          leading: Icon(icon),
          title: Text(title),
          trailing: Text(value, style: Theme.of(context).textTheme.titleMedium),
        );

    return Scaffold(
      appBar: AppBar(
        title: Text(l10n.phoneCheckTitle),
        actions: [
          IconButton(
            key: const Key('phone-check-refresh'),
            tooltip: l10n.phoneCheckRefresh,
            icon: const Icon(Icons.refresh),
            onPressed: () => ref.invalidate(phoneCheckProvider),
          ),
        ],
      ),
      body: switch (check) {
        AsyncData(:final value) => ListView(
          padding: const EdgeInsets.all(8),
          children: [
            row(
              'memory',
              Icons.memory,
              l10n.phoneCheckMemory,
              megabytes(value.memoryNow),
            ),
            row(
              'memory-most',
              Icons.trending_up,
              l10n.phoneCheckMemoryMost,
              megabytes(value.memoryMost),
            ),
            row(
              'pictures',
              Icons.image_outlined,
              l10n.phoneCheckPictures,
              '${megabytes(value.pictures)} / ${megabytes(imageCacheBytes)}',
            ),
            row(
              'media',
              Icons.video_library_outlined,
              l10n.phoneCheckSavedMedia,
              '${megabytes(value.savedMedia)} / '
                  '${megabytes(ref.watch(mediaCacheProvider).maxBytes)}',
            ),
            row(
              'lessons',
              Icons.menu_book_outlined,
              l10n.phoneCheckDownloadedLessons,
              '${value.downloadedLessons}',
            ),
            const SizedBox(height: 16),
            Center(
              child: OutlinedButton.icon(
                key: const Key('phone-check-clear-media'),
                icon: const Icon(Icons.delete_outline),
                label: Text(l10n.phoneCheckClearMedia),
                onPressed: () async {
                  await ref.read(mediaCacheProvider).clear();
                  ref.invalidate(phoneCheckProvider);
                },
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

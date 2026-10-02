import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../l10n/app_localizations.dart';
import '../../lessons/lesson_repository.dart';
import '../../lessons/lesson_text.dart';
import '../common/language_toggle.dart';

/// Developer previewer: every bundled lesson, including drafts.
/// Broken lesson files are listed with their error instead of crashing.
class LessonListScreen extends ConsumerWidget {
  const LessonListScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final ids = ref.watch(lessonIdsProvider);
    return Scaffold(
      appBar: AppBar(
        title: Text(l10n.lessonsPreviewTitle),
        actions: const [LanguageToggle()],
      ),
      body: switch (ids) {
        AsyncData(:final value) => ListView(
          children: [for (final id in value) _LessonTile(id: id)],
        ),
        AsyncError(:final error) => Center(child: Text('$error')),
        _ => const Center(child: CircularProgressIndicator()),
      },
    );
  }
}

class _LessonTile extends ConsumerWidget {
  const _LessonTile({required this.id});

  final String id;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final lesson = ref.watch(lessonProvider(id));
    return switch (lesson) {
      AsyncData(:final value) => ListTile(
        key: Key('lesson-$id'),
        title: LessonText(value.title),
        subtitle: Text(
          '$id · ${AppLocalizations.of(context).minutesShort(value.estimatedMinutes)}',
          textDirection: TextDirection.ltr,
        ),
        trailing: Chip(label: Text(value.review.status)),
        onTap: () => context.push('/lesson/$id'),
      ),
      AsyncError(:final error) => ListTile(
        key: Key('lesson-$id'),
        leading: const Icon(Icons.error, color: Colors.red),
        title: Text(id),
        subtitle: Text('$error'),
      ),
      _ => ListTile(title: Text(id)),
    };
  }
}

import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../l10n/app_localizations.dart';
import '../../lessons/lesson_player_screen.dart';
import '../../lessons/lesson_repository.dart';
import '../../lessons/lesson_text.dart';
import '../../lessons/lesson_updates.dart';
import '../../models/lesson.dart';
import '../../review/review_store.dart';
import '../../services/auth_service.dart';
import '../../services/local_db.dart';

/// Teacher review in the dev app (Phase 8): the lessons waiting for review,
/// once the account is a verified reviewer.
class ReviewListScreen extends ConsumerStatefulWidget {
  const ReviewListScreen({super.key});

  @override
  ConsumerState<ReviewListScreen> createState() => _ReviewListScreenState();
}

class _ReviewListScreenState extends ConsumerState<ReviewListScreen> {
  @override
  void initState() {
    super.initState();
    // Reviewers should see the newest drafts, not wait an hour.
    unawaited(updateLessonsNow(ref));
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final access = ref.watch(reviewAccessProvider);
    return Scaffold(
      appBar: AppBar(title: Text(l10n.reviewTitle)),
      body: switch (access) {
        AsyncData(value: ReviewAccess.reviewer) => const _ReviewList(),
        AsyncData(:final value) => _AccessHelp(access: value),
        AsyncError() => _Retry(
          onRetry: () => ref.invalidate(reviewAccessProvider),
        ),
        _ => const Center(child: CircularProgressIndicator()),
      },
    );
  }
}

/// Downloads new drafts now and refreshes the lesson lists.
Future<void> updateLessonsNow(WidgetRef ref) =>
    ref.read(checkLessonsNowProvider)();

class _Retry extends StatelessWidget {
  const _Retry({required this.onRetry});

  final VoidCallback onRetry;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return _Message(
      key: const Key('review-error'),
      text: l10n.reviewError,
      actions: [
        FilledButton(onPressed: onRetry, child: Text(l10n.tryAgainButton)),
      ],
    );
  }
}

class _Message extends StatelessWidget {
  const _Message({super.key, required this.text, this.actions = const []});

  final String text;
  final List<Widget> actions;

  @override
  Widget build(BuildContext context) => ListView(
    padding: const EdgeInsets.all(24),
    children: [
      Text(text, style: Theme.of(context).textTheme.titleMedium),
      for (final action in actions) ...[const SizedBox(height: 16), action],
    ],
  );
}

/// Explains the one thing missing before this account can review.
class _AccessHelp extends ConsumerStatefulWidget {
  const _AccessHelp({required this.access});

  final ReviewAccess access;

  @override
  ConsumerState<_AccessHelp> createState() => _AccessHelpState();
}

class _AccessHelpState extends ConsumerState<_AccessHelp> {
  var _sent = false;
  var _failed = false;

  Future<void> _try(Future<void> Function(AuthService auth) action) async {
    setState(() => _failed = false);
    try {
      await action(ref.read(authServiceProvider));
    } catch (_) {
      if (mounted) setState(() => _failed = true);
    }
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final email = ref.watch(authUserProvider).value?.email ?? '';
    return switch (widget.access) {
      ReviewAccess.signedOut => _Message(
        key: const Key('review-sign-in'),
        text: l10n.reviewSignIn,
        actions: [
          FilledButton(
            onPressed: () => context.push('/account'),
            child: Text(l10n.reviewSignInButton),
          ),
        ],
      ),
      ReviewAccess.unverified => _Message(
        key: const Key('review-verify'),
        text: l10n.reviewVerify(email),
        actions: [
          FilledButton(
            key: const Key('review-send-link'),
            onPressed: () => _try((auth) async {
              await auth.sendVerificationEmail();
              if (mounted) setState(() => _sent = true);
            }),
            child: Text(l10n.reviewSendLink),
          ),
          if (_sent) Text(l10n.reviewLinkSent),
          OutlinedButton(
            key: const Key('review-check-again'),
            onPressed: () => _try((auth) async {
              await auth.refreshUser();
              ref.invalidate(reviewAccessProvider);
            }),
            child: Text(l10n.reviewCheckAgain),
          ),
          if (_failed) Text(l10n.reviewError),
        ],
      ),
      ReviewAccess.notReviewer || ReviewAccess.reviewer => _Message(
        key: const Key('review-not-reviewer'),
        text: l10n.reviewNotReviewer(email),
        actions: [
          OutlinedButton(
            onPressed: () => ref.invalidate(reviewAccessProvider),
            child: Text(l10n.tryAgainButton),
          ),
        ],
      ),
    };
  }
}

class _ReviewList extends ConsumerWidget {
  const _ReviewList();

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    return switch (ref.watch(reviewsProvider)) {
      AsyncData(value: final reviews) when reviews.isEmpty => _Message(
        text: l10n.reviewNothing,
      ),
      AsyncData(value: final reviews) => RefreshIndicator(
        onRefresh: () async {
          await updateLessonsNow(ref);
          ref.invalidate(reviewsProvider);
        },
        child: ListView(
          children: [
            // Waiting first, then needing changes, then approved.
            for (final status in [
              ReviewStatus.inReview,
              ReviewStatus.changesRequested,
              ReviewStatus.approved,
            ])
              for (final review in reviews.where((r) => r.status == status))
                _ReviewTile(review: review),
          ],
        ),
      ),
      AsyncError() => _Retry(onRetry: () => ref.invalidate(reviewsProvider)),
      _ => const Center(child: CircularProgressIndicator()),
    };
  }
}

class _ReviewTile extends ConsumerWidget {
  const _ReviewTile({required this.review});

  final LessonReview review;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final lesson = ref.watch(lessonProvider(review.lessonId)).value;
    return ListTile(
      key: Key('review-${review.lessonId}'),
      title: lesson == null ? Text(review.lessonId) : LessonText(lesson.title),
      subtitle: Text(l10n.reviewVersion(review.version)),
      trailing: StatusChip(status: review.status),
      onTap: () => context.push('/review/${review.lessonId}'),
    );
  }
}

class StatusChip extends StatelessWidget {
  const StatusChip({super.key, required this.status});

  final ReviewStatus status;

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final scheme = Theme.of(context).colorScheme;
    final (label, colour) = switch (status) {
      ReviewStatus.inReview => (
        l10n.reviewStatusInReview,
        scheme.secondaryContainer,
      ),
      ReviewStatus.approved => (
        l10n.reviewStatusApproved,
        Colors.green.shade100,
      ),
      ReviewStatus.changesRequested => (
        l10n.reviewStatusChanges,
        Colors.orange.shade100,
      ),
    };
    return Chip(
      key: Key('status-${status.wire}'),
      label: Text(label),
      backgroundColor: colour,
    );
  }
}

/// The review currently stored for [lessonId], or null.
final _reviewOfProvider = Provider.family<AsyncValue<LessonReview?>, String>(
  (ref, lessonId) => ref
      .watch(reviewsProvider)
      .whenData(
        (reviews) => reviews.where((r) => r.lessonId == lessonId).firstOrNull,
      ),
);

/// The fingerprint of the lesson version on this phone (null for a lesson
/// that was never downloaded).
final _localHashProvider = FutureProvider.family<String?, String>((
  ref,
  lessonId,
) async {
  ref.watch(lessonProvider(lessonId));
  return (await ref.watch(localDbProvider).downloadedLesson(lessonId))?.hash;
});

/// One lesson under review: play it, read and add notes, and decide.
class ReviewLessonScreen extends ConsumerWidget {
  const ReviewLessonScreen({super.key, required this.lessonId});

  final String lessonId;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final review = ref.watch(_reviewOfProvider(lessonId));
    final lesson = ref.watch(lessonProvider(lessonId));
    final localHash = ref.watch(_localHashProvider(lessonId));
    final notes = ref.watch(reviewNotesProvider(lessonId));
    return Scaffold(
      appBar: AppBar(
        title: lesson.value == null
            ? Text(lessonId)
            : LessonText(lesson.value!.title),
      ),
      body: switch ((review, lesson, localHash)) {
        (
          AsyncData(value: final r?),
          AsyncData(value: final l),
          AsyncData(value: final h),
        ) =>
          _ReviewBody(
            review: r,
            lesson: l,
            sameVersion: h == r.hash,
            notes: notes.value ?? const [],
          ),
        (AsyncData(value: null), _, _) => _Message(text: l10n.reviewNothing),
        (AsyncError(), _, _) ||
        (_, AsyncError(), _) ||
        (_, _, AsyncError()) => _Retry(
          onRetry: () => ref
            ..invalidate(reviewsProvider)
            ..invalidate(lessonProvider(lessonId)),
        ),
        _ => const Center(child: CircularProgressIndicator()),
      },
    );
  }
}

class _ReviewBody extends ConsumerStatefulWidget {
  const _ReviewBody({
    required this.review,
    required this.lesson,
    required this.sameVersion,
    required this.notes,
  });

  final LessonReview review;
  final Lesson lesson;

  /// The phone shows the exact version under review.
  final bool sameVersion;
  final List<ReviewNote> notes;

  @override
  ConsumerState<_ReviewBody> createState() => _ReviewBodyState();
}

class _ReviewBodyState extends ConsumerState<_ReviewBody> {
  var _busy = false;
  var _failed = false;

  Future<void> _run(Future<void> Function() action) async {
    setState(() {
      _busy = true;
      _failed = false;
    });
    try {
      await action();
    } catch (_) {
      _failed = true;
    }
    if (mounted) setState(() => _busy = false);
  }

  Future<void> _decide({required bool approved}) async {
    final l10n = AppLocalizations.of(context);
    if (approved) {
      final ok = await showDialog<bool>(
        context: context,
        builder: (context) => AlertDialog(
          content: Text(l10n.reviewApproveConfirm(widget.review.version)),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context, false),
              child: Text(l10n.cancelButton),
            ),
            FilledButton(
              key: const Key('confirm-approve'),
              onPressed: () => Navigator.pop(context, true),
              child: Text(l10n.reviewApprove),
            ),
          ],
        ),
      );
      if (ok != true) return;
    }
    await _run(() async {
      await ref
          .read(reviewStoreProvider)
          .decide(
            widget.lesson.id,
            hash: widget.review.hash,
            approved: approved,
            reviewer: reviewerEmail(ref),
          );
      ref.invalidate(reviewsProvider);
    });
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final review = widget.review;
    final notesFor = <String, List<ReviewNote>>{};
    for (final note in widget.notes.where((n) => n.hash == review.hash)) {
      (notesFor[note.stepId] ??= []).add(note);
    }
    final canReview = widget.sameVersion && !_busy;
    return ListView(
      padding: const EdgeInsets.symmetric(vertical: 8),
      children: [
        ListTile(
          title: Text(l10n.reviewVersion(review.version)),
          subtitle: review.reviewer == null
              ? null
              : Text(l10n.reviewDecidedBy(review.reviewer!)),
          trailing: StatusChip(status: review.status),
        ),
        if (!widget.sameVersion)
          Card(
            key: const Key('review-old-version'),
            margin: const EdgeInsets.all(16),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(l10n.reviewOldVersion),
                  const SizedBox(height: 8),
                  FilledButton(
                    key: const Key('review-update'),
                    onPressed: _busy
                        ? null
                        : () => _run(() async {
                            await updateLessonsNow(ref);
                            ref
                              ..invalidate(_localHashProvider(review.lessonId))
                              ..invalidate(reviewsProvider);
                          }),
                    child: Text(l10n.reviewUpdate),
                  ),
                ],
              ),
            ),
          ),
        Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              FilledButton.icon(
                key: const Key('review-play'),
                icon: const Icon(Icons.play_arrow),
                label: Text(l10n.reviewPlay),
                onPressed: canReview
                    ? () => context.push('/review/${review.lessonId}/play')
                    : null,
              ),
              const SizedBox(height: 8),
              Text(l10n.reviewPlayHint),
            ],
          ),
        ),
        const Divider(),
        _NotesSection(
          key: const Key('notes-general'),
          title: l10n.reviewWholeLesson,
          stepId: generalNote,
          review: review,
          notes: notesFor[generalNote] ?? const [],
          enabled: canReview,
        ),
        for (final (i, step) in widget.lesson.steps.indexed)
          _NotesSection(
            key: Key('notes-${step.id}'),
            title: '${l10n.reviewStep(i + 1)} · ${step.type}',
            subtitle: step.id,
            stepId: step.id,
            review: review,
            notes: notesFor[step.id] ?? const [],
            enabled: canReview,
          ),
        const Divider(),
        if (_failed)
          Padding(
            padding: const EdgeInsets.all(16),
            child: Text(
              l10n.reviewError,
              style: TextStyle(color: Theme.of(context).colorScheme.error),
            ),
          ),
        Padding(
          padding: const EdgeInsets.all(16),
          child: Wrap(
            spacing: 12,
            runSpacing: 12,
            alignment: WrapAlignment.end,
            children: [
              OutlinedButton(
                key: const Key('review-changes'),
                onPressed: canReview ? () => _decide(approved: false) : null,
                child: Text(l10n.reviewStatusChanges),
              ),
              FilledButton(
                key: const Key('review-approve'),
                onPressed: canReview ? () => _decide(approved: true) : null,
                child: Text(l10n.reviewApprove),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

/// The signed-in reviewer's email, as the rules expect it.
String reviewerEmail(WidgetRef ref) =>
    (ref.read(authServiceProvider).currentUser?.email ?? '').toLowerCase();

class _NotesSection extends ConsumerWidget {
  const _NotesSection({
    super.key,
    required this.title,
    required this.stepId,
    required this.review,
    required this.notes,
    required this.enabled,
    this.subtitle,
  });

  final String title;
  final String? subtitle;
  final String stepId;
  final LessonReview review;
  final List<ReviewNote> notes;
  final bool enabled;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        ListTile(
          title: Text(title),
          subtitle: subtitle == null
              ? null
              : Text(subtitle!, textDirection: TextDirection.ltr),
          trailing: IconButton(
            key: Key('add-note-$stepId'),
            tooltip: l10n.reviewAddNote,
            icon: const Icon(Icons.edit_note),
            onPressed: enabled
                ? () => addReviewNote(context, ref, review, stepId)
                : null,
          ),
        ),
        for (final note in notes)
          Padding(
            padding: const EdgeInsetsDirectional.fromSTEB(32, 0, 16, 8),
            child: Text('${note.text}\n— ${note.author}'),
          ),
      ],
    );
  }
}

/// Asks for a note on [stepId] and saves it. Returns whether it was saved.
Future<bool> addReviewNote(
  BuildContext context,
  WidgetRef ref,
  LessonReview review,
  String stepId,
) async {
  final text = await showDialog<String>(
    context: context,
    builder: (context) => const _NoteDialog(),
  );
  if (text == null || text.trim().isEmpty) return false;
  try {
    await ref
        .read(reviewStoreProvider)
        .addNote(
          review.lessonId,
          ReviewNote(
            stepId: stepId,
            text: text.trim(),
            author: reviewerEmail(ref),
            hash: review.hash,
          ),
        );
    ref.invalidate(reviewNotesProvider(review.lessonId));
    return true;
  } catch (_) {
    if (context.mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(AppLocalizations.of(context).reviewError)),
      );
    }
    return false;
  }
}

class _NoteDialog extends StatefulWidget {
  const _NoteDialog();

  @override
  State<_NoteDialog> createState() => _NoteDialogState();
}

class _NoteDialogState extends State<_NoteDialog> {
  final _text = TextEditingController();

  @override
  void dispose() {
    _text.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    return AlertDialog(
      title: Text(l10n.reviewAddNote),
      content: TextField(
        key: const Key('note-text'),
        controller: _text,
        autofocus: true,
        maxLines: 5,
        minLines: 2,
        maxLength: 2000,
        decoration: InputDecoration(hintText: l10n.reviewNoteHint),
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context),
          child: Text(l10n.cancelButton),
        ),
        FilledButton(
          key: const Key('note-save'),
          onPressed: () => Navigator.pop(context, _text.text),
          child: Text(l10n.reviewSave),
        ),
      ],
    );
  }
}

/// Plays a lesson for review: like a child sees it, with a note button.
class ReviewPlayerScreen extends ConsumerWidget {
  const ReviewPlayerScreen({super.key, required this.lessonId});

  final String lessonId;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final review = ref.watch(_reviewOfProvider(lessonId)).value;
    return LessonPlayerScreen(
      lessonId: lessonId,
      onNote: (context, step) {
        if (review != null) {
          unawaited(addReviewNote(context, ref, review, step.id));
        }
      },
    );
  }
}

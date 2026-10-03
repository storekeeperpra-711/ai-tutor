import 'package:ai_tutor/review/review_store.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import '../fakes.dart';
import '../helpers.dart';
import '../lessons/lesson_updates_test.dart' show bundledId, lessonJson;
import '../lessons/play_helpers.dart';
import 'profiles_and_progress_test.dart' show goBack;

const teacher = 'teacher@school.pk';

/// A backend with [bundledId] published as a draft and waiting for review.
FakeBackend draftBackend() {
  final backend = FakeBackend();
  backend.remote.publishLesson(lessonJson(id: bundledId, title: 'Draft'));
  backend.reviews
    ..reviewers.add(teacher)
    ..submit(bundledId);
  backend.auth.accounts[teacher] = ('secret1', 'adult-1');
  return backend;
}

Future<void> openReview(
  WidgetTester tester,
  FakeBackend backend, {
  bool offered = true,
}) async {
  await tester.pumpWidget(
    await buildTestApp(backend: backend, reviewOffered: offered),
  );
  await tester.pumpAndSettle();
  await tester.tap(find.byTooltip('Settings'));
  await tester.pumpAndSettle();
  if (offered) await tapKey(tester, 'open-review');
}

Future<void> writeNote(WidgetTester tester, String key, String text) async {
  await tapKey(tester, key);
  await tester.enterText(find.byKey(const Key('note-text')), text);
  await tapKey(tester, 'note-save');
  await tester.pumpAndSettle();
}

Future<void> scrollToTop(WidgetTester tester) async {
  await tester.fling(find.byType(ListView).first, const Offset(0, 3000), 3000);
  await tester.pumpAndSettle();
}

Future<void> scrollTo(WidgetTester tester, Finder finder) => tester
    .scrollUntilVisible(finder, 300, scrollable: find.byType(Scrollable).first);

void main() {
  setUp(() {
    final view =
        TestWidgetsFlutterBinding.instance.platformDispatcher.views.first;
    view.physicalSize = const Size(1080, 2340);
    view.devicePixelRatio = 3;
  });

  tearDown(() {
    TestWidgetsFlutterBinding.instance.platformDispatcher.views.first
      ..resetPhysicalSize()
      ..resetDevicePixelRatio();
  });

  testWidgets(
    'a teacher verifies their email, plays a draft, adds notes and approves',
    (tester) async {
      final backend = draftBackend();
      await backend.auth.signIn(teacher, 'secret1');
      await openReview(tester, backend);

      expect(find.byKey(const Key('review-verify')), findsOneWidget);
      await tapKey(tester, 'review-send-link');
      expect(backend.auth.verificationsSent, [teacher]);
      backend.auth.verified.add(teacher);
      await tapKey(tester, 'review-check-again');
      await tester.pumpAndSettle();

      expect(find.byKey(const Key('status-in_review')), findsOneWidget);
      await tapKey(tester, 'review-$bundledId');
      await tester.pumpAndSettle();
      expect(find.text('Draft'), findsWidgets);
      expect(find.byKey(const Key('review-old-version')), findsNothing);

      await writeNote(tester, 'add-note-general', 'Too long for Grade 9.');
      expect(find.textContaining('Too long for Grade 9.'), findsOneWidget);

      await scrollToTop(tester);
      await tapKey(tester, 'review-play');
      await tester.pumpAndSettle();
      await writeNote(tester, 'review-note', 'Say "equation" in Urdu too.');
      await goBack(tester);

      final notes = backend.reviews.notesOf[bundledId]!;
      expect([for (final n in notes) n.stepId], [generalNote, 's1_scale']);
      expect(notes.every((n) => n.author == teacher), isTrue);
      expect(find.textContaining('in Urdu too'), findsOneWidget);

      final approve = find.byKey(const Key('review-approve'));
      await scrollTo(tester, approve);
      await tester.tap(approve);
      await tester.pumpAndSettle();
      await tapKey(tester, 'confirm-approve');
      await tester.pumpAndSettle();
      final review = backend.reviews.docs[bundledId]!;
      expect(review.status, ReviewStatus.approved);
      expect(review.reviewer, teacher);
      await scrollToTop(tester);
      expect(find.byKey(const Key('status-approved')), findsOneWidget);
    },
  );

  testWidgets('pulling down the list shows the newest version', (tester) async {
    final backend = draftBackend();
    backend.auth.verified.add(teacher);
    await backend.auth.signIn(teacher, 'secret1');
    await openReview(tester, backend);

    // A corrected version is published after the phone downloaded v1.
    backend.remote.publishLesson(
      lessonJson(id: bundledId, title: 'Draft 2'),
      version: 2,
    );
    backend.reviews.submit(bundledId);
    await tapKey(tester, 'review-$bundledId');
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('review-old-version')), findsNothing);
    await goBack(tester);
    await tester.drag(find.byType(ListView).first, const Offset(0, 300));
    await tester.pumpAndSettle();
    await tapKey(tester, 'review-$bundledId');
    await tester.pumpAndSettle();
    expect(find.text('Version 2'), findsOneWidget);
  });

  testWidgets('a review screen with a stale version blocks approval', (
    tester,
  ) async {
    final backend = draftBackend();
    backend.auth.verified.add(teacher);
    await backend.auth.signIn(teacher, 'secret1');
    await openReview(tester, backend);

    // The review moved on to a version this phone doesn't have yet.
    backend.remote.publishLesson(
      lessonJson(id: bundledId, title: 'Draft 2'),
      version: 2,
    );
    backend.reviews.submit(bundledId);
    final saved = backend.remote.docs['published_lessons/$bundledId']!;
    backend.remote.docs['lesson_catalog/current'] = {'lessons': {}};
    await tester.drag(find.byType(ListView).first, const Offset(0, 300));
    await tester.pumpAndSettle();
    await tapKey(tester, 'review-$bundledId');
    await tester.pumpAndSettle();

    expect(find.byKey(const Key('review-old-version')), findsOneWidget);
    final approve = find.byKey(const Key('review-approve'));
    await scrollTo(tester, approve);
    expect(tester.widget<FilledButton>(approve).onPressed, isNull);

    // Back in the catalog: updating fixes it.
    backend.remote.publishLesson(
      lessonJson(id: bundledId, title: 'Draft 2'),
      version: saved['version']! as int,
    );
    await scrollToTop(tester);
    await tapKey(tester, 'review-update');
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('review-old-version')), findsNothing);
    await scrollTo(tester, approve);
    expect(tester.widget<FilledButton>(approve).onPressed, isNotNull);
  });

  testWidgets('only listed teachers get in', (tester) async {
    final backend = draftBackend();
    await openReview(tester, backend);
    expect(find.byKey(const Key('review-sign-in')), findsOneWidget);

    backend.auth.accounts['other@school.pk'] = ('secret1', 'adult-2');
    backend.auth.verified.add('other@school.pk');
    await backend.auth.signIn('other@school.pk', 'secret1');
    await tester.pumpAndSettle();
    expect(find.byKey(const Key('review-not-reviewer')), findsOneWidget);
    expect(find.textContaining('other@school.pk'), findsOneWidget);
  });

  testWidgets('the real app has no review screens', (tester) async {
    await openReview(tester, draftBackend(), offered: false);
    expect(find.byKey(const Key('open-review')), findsNothing);
  });
}

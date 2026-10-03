import 'package:ai_tutor/character/narrator.dart';
import 'package:ai_tutor/character/sounds.dart';
import 'package:ai_tutor/ai/ai_service.dart';
import 'package:ai_tutor/ai/photo_picker.dart';
import 'package:ai_tutor/app/preferences.dart';
import 'package:ai_tutor/l10n/app_localizations.dart';
import 'package:ai_tutor/lessons/answer_checking.dart';
import 'package:ai_tutor/lessons/step_registry.dart';
import 'package:ai_tutor/lessons/step_result.dart';
import 'package:ai_tutor/models/lesson_step.dart';
import 'package:ai_tutor/services/auth_service.dart';
import 'package:ai_tutor/services/connectivity.dart';
import 'package:ai_tutor/services/local_db.dart';
import 'package:ai_tutor/services/profiles.dart';
import 'package:ai_tutor/services/remote_store.dart';
import 'package:ai_tutor/services/sync_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../fakes.dart';
import '../lessons/play_helpers.dart';
import '../mastery/lessons.dart';

const g6 = 'g6-maths-02-dividing-fractions';
const g9 = 'g9-maths-05-solving-linear-equations';

T stepOf<T extends LessonStep>(String lessonId) =>
    loadLessonJson(lessonJson(lessonId)).steps.whereType<T>().single;

class _Fixed extends CurrentStudent {
  _Fixed(this.student);
  final Student? student;
  @override
  Student? build() => student;
}

/// Plays one step on its own, as the lesson player would, for student s1.
class StepHarness {
  StepHarness(this.backend);

  final FakeBackend backend;
  StepResult? result;
  late ProviderContainer container;

  Future<void> pump(
    WidgetTester tester,
    LessonStep step, {
    required String lessonId,
    String language = 'en',
    bool withStudent = true,
  }) async {
    SharedPreferences.setMockInitialValues({});
    final prefs = await SharedPreferences.getInstance();
    final s1 = student('s1');
    if (withStudent) await backend.db.addStudent(s1);
    await tester.pumpWidget(
      ProviderScope(
        overrides: [
          sharedPreferencesProvider.overrideWithValue(prefs),
          localDbProvider.overrideWithValue(backend.db),
          authServiceProvider.overrideWithValue(backend.auth),
          remoteStoreProvider.overrideWithValue(backend.remote),
          onlineProvider.overrideWith((ref) => backend.onlineStream),
          aiServiceProvider.overrideWithValue(backend.ai),
          narratorProvider.overrideWithValue(backend.narrator),
          soundPlayerProvider.overrideWithValue(backend.sounds),
          photoPickerProvider.overrideWithValue(
            (source) async => backend.photo,
          ),
          currentStudentProvider.overrideWith(
            () => _Fixed(withStudent ? s1 : null),
          ),
        ],
        child: MaterialApp(
          locale: Locale(language),
          localizationsDelegates: AppLocalizations.localizationsDelegates,
          supportedLocales: AppLocalizations.supportedLocales,
          home: Scaffold(
            body: Consumer(
              builder: (context, ref, _) {
                container = ProviderScope.containerOf(context);
                return buildStep(step, (r) => result = r, lessonId: lessonId);
              },
            ),
          ),
        ),
      ),
    );
    await tester.pumpAndSettle();
  }
}

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

  group('ai_explain', () {
    late FakeBackend backend;
    late StepHarness harness;
    late AiExplainStep step;

    setUp(() {
      backend = FakeBackend();
      harness = StepHarness(backend);
      step = stepOf<AiExplainStep>(g6);
      backend.ai.keywords[step.id] = step.keywords;
    });

    Future<void> answer(WidgetTester tester, String text) async {
      await tester.enterText(find.byKey(const Key('answer-input')), text);
      await tapKey(tester, 'step-check');
    }

    String text(WidgetTester tester, String key) =>
        tester.widget<Text>(find.byKey(Key(key))).data!;

    testWidgets('online, Mithu answers with AI and the label says so', (
      tester,
    ) async {
      await harness.pump(tester, step, lessonId: g6);
      await answer(
        tester,
        'Each roti has 2 halves so we count how many halves: 6',
      );
      expect(backend.ai.explained, hasLength(1));
      expect(text(tester, 'ai-reply'), 'AI (en): got_it');
      expect(find.byKey(const Key('ai-level-got_it')), findsOneWidget);
      expect(text(tester, 'checked-by'), 'Checked by AI');
      await tapKey(tester, 'step-continue');
      expect(harness.result!.correct, isTrue);
      expect(harness.result!.attempts, 1);
    });

    testWidgets('asks for Urdu feedback in Urdu', (tester) async {
      await harness.pump(tester, step, lessonId: g6, language: 'ur');
      await answer(tester, 'ہر روٹی کے دو آدھے ہوتے ہیں، کتنے آدھے گنیں تو چھ');
      expect(text(tester, 'ai-reply'), 'AI (ur): got_it');
      expect(text(tester, 'checked-by'), 'اے آئی نے جانچا');
    });

    testWidgets('a partly answer can be improved, then counts as solved', (
      tester,
    ) async {
      await harness.pump(tester, step, lessonId: g6);
      await answer(tester, 'because of the halves');
      expect(find.byKey(const Key('ai-level-partly')), findsOneWidget);
      await tapKey(tester, 'ai-improve');
      await answer(tester, 'We count how many halves fit: 3 rotis give six');
      expect(find.byKey(const Key('ai-level-got_it')), findsOneWidget);
      // Only two tries: no more "improve".
      expect(find.byKey(const Key('ai-improve')), findsNothing);
      await tapKey(tester, 'step-continue');
      expect(
        (
          harness.result!.correct,
          harness.result!.solved,
          harness.result!.attempts,
        ),
        (false, true, 2),
      );
    });

    testWidgets(
      'offline, keywords check it, it waits for Mithu, and the reply arrives later',
      (tester) async {
        backend.setOnline(false);
        await harness.pump(tester, step, lessonId: g6);
        await answer(tester, 'I think dividing makes it smaller');
        expect(find.byKey(const Key('ai-level-not_yet')), findsOneWidget);
        expect(text(tester, 'ai-reply'), step.fallbackFeedback.notYet.en);
        expect(text(tester, 'checked-by'), 'Checked by keywords');
        expect(text(tester, 'ai-note'), contains('Mithu will look'));

        final queued = await backend.db.answersToUpload();
        expect(queued.single.answer, 'I think dividing makes it smaller');
        expect(queued.single.stepId, step.id);

        // Back online: the answer goes up; the batch job answers; the
        // next sync brings the reply down.
        backend.setOnline(true);
        await tester.runAsync(() async {
          await backend.auth.ensureSignedIn();
          final sync = harness.container.read(syncServiceProvider);
          await sync.sync();
          final doc = backend.remote.docs['ai_queue/${queued.single.id}']!;
          expect(
            (doc['status'], doc['student_id'], doc['lang']),
            ('waiting', 's1', 'en'),
          );
          backend.remote.answerQueued(
            queued.single.id,
            level: 'partly',
            reply: 'Good thinking! How many halves are in one roti?',
          );
          await sync.sync();
        });
        final row = (await backend.db.answersAwaitingReply());
        expect(row, isEmpty);
        final saved = await backend.db.select(backend.db.aiQueue).get();
        expect(saved.single.status, 'answered');
        expect(saved.single.reply, startsWith('Good thinking'));
      },
    );

    testWidgets('after a daily limit the keywords check it and nothing waits', (
      tester,
    ) async {
      backend.ai.fallbackReason = 'step_limit';
      await harness.pump(tester, step, lessonId: g6);
      await answer(tester, 'We count how many halves fit: 3 rotis give six');
      expect(find.byKey(const Key('ai-level-got_it')), findsOneWidget);
      expect(text(tester, 'checked-by'), 'Checked by keywords');
      expect(text(tester, 'ai-note'), contains('helped a lot today'));
      expect(await backend.db.answersToUpload(), isEmpty);
    });

    testWidgets('without a student (lesson preview) it never calls the AI', (
      tester,
    ) async {
      await harness.pump(tester, step, lessonId: g6, withStudent: false);
      await answer(tester, 'We count how many halves fit: 3 rotis give six');
      expect(backend.ai.explained, isEmpty);
      expect(text(tester, 'checked-by'), 'Checked by keywords');
    });
  });

  group('photo_check', () {
    late FakeBackend backend;
    late StepHarness harness;
    late PhotoCheckStep step;

    setUp(() {
      backend = FakeBackend();
      harness = StepHarness(backend);
      step = stepOf<PhotoCheckStep>(g9);
    });

    String label(WidgetTester tester) =>
        tester.widget<Text>(find.byKey(const Key('checked-by'))).data!;

    testWidgets(
      'a notebook photo with a deliberate mistake is caught by the checker',
      (tester) async {
        // Line 3 is wrong: 2x - 7 = 5 gives 2x = 12, not 2x = -2.
        backend.ai.photoLines = [
          '4x - 7 = 2x + 5',
          '2x - 7 = 5',
          '2x = -2',
          'x = -1',
        ];
        await harness.pump(tester, step, lessonId: g9);
        await tapKey(tester, 'photo-camera');
        expect(backend.ai.photosRead, 1);
        expect(find.text(backend.ai.photoLines.join('\n')), findsOneWidget);
        expect(find.textContaining('Mithu read this'), findsOneWidget);

        await tapKey(tester, 'step-check');
        expect(find.byKey(const Key('feedback-try')), findsOneWidget);
        expect(
          tester.widget<Text>(find.byKey(const Key('checker-message'))).data,
          startsWith("Line 3 doesn't keep the scale balanced"),
        );
        // The AI only explains what the checker found.
        expect(backend.ai.verdicts.single, startsWith('Line 3'));
        expect(find.byKey(const Key('ai-reply')), findsOneWidget);
        expect(
          label(tester),
          'Read by AI · Checked by the app · Explained by AI',
        );

        // Second try: correct working.
        await tapKey(tester, 'photo-try-again');
        backend.ai.photoLines = [
          '4x - 7 = 2x + 5',
          '2x - 7 = 5',
          '2x = 12',
          'x = 6',
        ];
        await tapKey(tester, 'photo-camera');
        await tapKey(tester, 'step-check');
        expect(find.byKey(const Key('feedback-good')), findsOneWidget);
        expect(label(tester), 'Read by AI · Checked by the app');
        expect(backend.ai.verdicts, hasLength(1)); // no AI for a right answer
        await tapKey(tester, 'step-continue');
        expect(
          (
            harness.result!.correct,
            harness.result!.solved,
            harness.result!.attempts,
          ),
          (false, true, 2),
        );
      },
    );

    testWidgets('the student can fix a misread line before it is checked', (
      tester,
    ) async {
      backend.ai.photoLines = ['4x - 7 = 2x + 5', '2x - 7 = 5', '2x = 17'];
      await harness.pump(tester, step, lessonId: g9);
      await tapKey(tester, 'photo-camera');
      await tester.enterText(
        find.byKey(const Key('answer-input')),
        '4x - 7 = 2x + 5\n2x - 7 = 5\n2x = 12\nx = 6',
      );
      await tapKey(tester, 'step-check');
      expect(find.byKey(const Key('feedback-good')), findsOneWidget);
    });

    testWidgets('offline, the student types the working and the app checks', (
      tester,
    ) async {
      backend.setOnline(false);
      await harness.pump(tester, step, lessonId: g9);
      await tapKey(tester, 'photo-camera');
      expect(find.textContaining('Photos need internet'), findsOneWidget);
      await tester.enterText(
        find.byKey(const Key('answer-input')),
        '4x - 7 = 2x + 5\n2x = 12\nx = 6',
      );
      await tapKey(tester, 'step-check');
      expect(find.byKey(const Key('feedback-good')), findsOneWidget);
      expect(label(tester), 'Checked by the app');
    });

    testWidgets('a wrong typed answer offline shows the checker and the hint', (
      tester,
    ) async {
      backend.setOnline(false);
      await harness.pump(tester, step, lessonId: g9);
      await tapKey(tester, 'photo-type');
      await tester.enterText(
        find.byKey(const Key('answer-input')),
        '4x - 7 = 2x + 5\n6x = 12',
      );
      await tapKey(tester, 'step-check');
      expect(find.textContaining('Line 2'), findsOneWidget);
      expect(find.textContaining('First take 2x away'), findsOneWidget);
      expect(find.byKey(const Key('ai-reply')), findsNothing);
    });

    testWidgets('an unreadable photo asks for another photo', (tester) async {
      backend.ai.photoReadable = false;
      await harness.pump(tester, step, lessonId: g9);
      await tapKey(tester, 'photo-camera');
      expect(find.textContaining("couldn't read that photo"), findsOneWidget);
      expect(find.byKey(const Key('photo-gallery')), findsOneWidget);
    });

    testWidgets('after the photo limit the student types instead', (
      tester,
    ) async {
      backend.ai.fallbackReason = 'student_limit';
      await harness.pump(tester, step, lessonId: g9);
      await tapKey(tester, 'photo-gallery');
      expect(find.textContaining('enough photos today'), findsOneWidget);
      expect(find.byKey(const Key('answer-input')), findsOneWidget);
    });

    testWidgets('three wrong tries show the full working', (tester) async {
      backend.setOnline(false);
      await harness.pump(tester, step, lessonId: g9);
      for (var i = 0; i < 3; i++) {
        await tapKey(tester, 'photo-type');
        await tester.enterText(
          find.byKey(const Key('answer-input')),
          '4x - 7 = 2x + 5\nx = 1',
        );
        await tapKey(tester, 'step-check');
        if (i < 2) await tapKey(tester, 'photo-try-again');
      }
      expect(find.textContaining('divide both sides by 2'), findsOneWidget);
      await tapKey(tester, 'step-continue');
      expect(harness.result!.solved, isFalse);
    });
  });

  test('the photo step checks final answers too', () async {
    final l10n = await AppLocalizations.delegate.load(const Locale('en'));
    PhotoCheckStep photo(String checker, String expected) =>
        PhotoCheckStep.fromJson({
          'id': 'p',
          'type': 'photo_check',
          'problem': {'en': 'p', 'ur': 'p'},
          'checker': checker,
          'expected': expected,
          'hint': {'en': 'h', 'ur': 'h'},
          'feedback_correct': {'en': 'c', 'ur': 'c'},
          'correct_working': {'en': 'w', 'ur': 'w'},
        });
    bool ok(PhotoCheckStep s, String input) =>
        checkPhotoStep(s, input, l10n, 'en').correct;

    final numeric = photo('numeric', '6');
    expect(ok(numeric, '3 ÷ ½\n= 6'), isTrue);
    expect(ok(numeric, 'x = ۶'), isTrue);
    expect(ok(numeric, '= 5'), isFalse);
    final fraction = photo('fraction', '3/4');
    expect(ok(fraction, '6/8 = 3/4'), isTrue);
    final chem = photo('chem_equation', '2H2 + O2 -> 2H2O');
    expect(ok(chem, 'H2 + O2 -> H2O\n2H2 + O2 → 2H₂O'), isTrue);
    expect(ok(chem, '2H2 + O2 -> H2O2'), isFalse);
  });
}

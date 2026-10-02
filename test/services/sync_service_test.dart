import 'package:ai_tutor/mastery/skill_state.dart';
import 'package:ai_tutor/services/remote_store.dart';
import 'package:ai_tutor/services/sync_service.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../fakes.dart';

void main() {
  late FakeBackend backend;
  late SyncService sync;

  setUp(() async {
    SharedPreferences.setMockInitialValues({});
    backend = FakeBackend();
    sync = SyncService(
      db: backend.db,
      remote: backend.remote,
      auth: backend.auth,
      prefs: await SharedPreferences.getInstance(),
    );
    await backend.auth.ensureSignedIn();
    await backend.db.addStudent(student('ayesha'));
  });

  tearDown(() => backend.db.close());

  String uidNow() => backend.auth.currentUser!.uid;

  test('uploads the profile, the role and each answer', () async {
    await answer(backend.db, 'ayesha', 0);
    await sync.sync();

    expect(backend.remote.docs['accounts/${uidNow()}']!['role'], 'device');
    expect(
      backend
          .remote
          .docs['accounts/${uidNow()}/students/ayesha']!['first_name'],
      'Ayesha',
    );
    final doc = backend.remote.progressDoc(uidNow(), 'ayesha', 'lesson-a')!;
    expect(doc['next_step'], 1);
    expect((doc['steps'] as Map).keys, ['s0']);
    expect(await backend.db.pendingCount(), 0);
  });

  test('one write per lesson per round, not per tap', () async {
    await sync.sync();
    final before = backend.remote.writes;
    await answer(backend.db, 'ayesha', 0);
    await sync.sync();
    expect(backend.remote.writes - before, 1);
    // Nothing new: nothing written.
    await sync.sync();
    expect(backend.remote.writes - before, 1);
  });

  test('offline answers wait, then sync when the connection is back', () async {
    await answer(backend.db, 'ayesha', 0);
    await sync.sync();

    backend.setOnline(false);
    await answer(backend.db, 'ayesha', 1);
    await answer(backend.db, 'ayesha', 2);
    final waiting = sync.sync(); // held, like Firestore offline
    await pumpEventQueue();
    expect(await backend.db.pendingCount(), 2);
    expect(
      backend.remote.progressDoc(uidNow(), 'ayesha', 'lesson-a')!['next_step'],
      1,
    );

    backend.setOnline(true);
    await waiting;
    final doc = backend.remote.progressDoc(uidNow(), 'ayesha', 'lesson-a')!;
    expect(doc['next_step'], 3);
    // Merged writes keep the earlier answers too.
    expect((doc['steps'] as Map).keys, containsAll(['s0', 's1', 's2']));
    expect(await backend.db.pendingCount(), 0);
  });

  test('answers saved during an upload go in the next round', () async {
    backend.setOnline(false);
    await answer(backend.db, 'ayesha', 0);
    final first = sync.sync();
    await pumpEventQueue();
    await answer(backend.db, 'ayesha', 1);
    await sync.sync(); // folded into the running round
    backend.setOnline(true);
    await first;
    expect(
      backend.remote.progressDoc(uidNow(), 'ayesha', 'lesson-a')!['next_step'],
      2,
    );
    expect(await backend.db.pendingCount(), 0);
  });

  test('without sign-in (offline first launch) nothing is lost', () async {
    await backend.auth.signOut();
    backend.setOnline(false);
    await answer(backend.db, 'ayesha', 0);
    await sync.sync();
    expect(await backend.db.pendingCount(), 1);

    backend.setOnline(true);
    await backend.auth.ensureSignedIn();
    await sync.sync();
    expect(await backend.db.pendingCount(), 0);
  });

  test('switching to another account uploads everything to it', () async {
    await answer(backend.db, 'ayesha', 0);
    await sync.sync();
    final phoneUid = uidNow();

    backend.auth.accounts['mother@example.com'] = ('secret1', 'mother');
    final user = await backend.auth.signIn('mother@example.com', 'secret1');
    await sync.useAccount(user);
    await sync.sync();

    expect(uidNow(), isNot(phoneUid));
    expect(backend.remote.docs['accounts/mother/students/ayesha'], isNotNull);
    expect(
      backend.remote.progressDoc('mother', 'ayesha', 'lesson-a'),
      isNotNull,
    );
    // An adult account's role is not overwritten with "device".
    expect(backend.remote.docs['accounts/mother'], isNull);
  });

  test('a new phone gets the learners back from the account', () async {
    await answer(backend.db, 'ayesha', 0);
    await answer(backend.db, 'ayesha', 1);
    await sync.sync();
    await backend.remote.setRole(uidNow(), AccountRole.parent);

    final data = await backend.remote.fetchAll(uidNow());
    final newPhone = FakeBackend();
    addTearDown(newPhone.db.close);
    await newPhone.db.mergeRemote(data);

    expect(data.role, 'parent');
    expect((await newPhone.db.student('ayesha'))!.firstName, 'Ayesha');
    expect((await newPhone.db.progress('ayesha', 'lesson-a'))!.nextStep, 2);
    expect(await newPhone.db.pendingCount(), 0);
  });

  test('skill states sync, and come back on a new phone', () async {
    final at = DateTime(2026, 10, 5, 17);
    await backend.db.updateSkillState(
      'ayesha',
      'maths.fractions.divide_by_fraction',
      (s) => s.record(
        Evidence(
          skill: s.skill,
          itemId: 'lesson-a/s0',
          at: at,
          firstTry: true,
          solved: true,
          questionType: 'recall',
        ),
        null,
      ),
      now: at,
    );
    expect(await backend.db.unsyncedSkillStates(), hasLength(1));
    await sync.sync();
    expect(await backend.db.unsyncedSkillStates(), isEmpty);
    final doc = backend
        .remote
        .docs['accounts/${uidNow()}/students/ayesha/skills/maths.fractions.divide_by_fraction']!;
    expect(doc['first_try_correct'], 1);

    final newPhone = FakeBackend();
    addTearDown(newPhone.db.close);
    await newPhone.db.mergeRemote(await backend.remote.fetchAll(uidNow()));
    final states = await newPhone.db.skillStatesOf('ayesha');
    expect(states['maths.fractions.divide_by_fraction']!.firstTryCorrect, 1);
    expect(await newPhone.db.unsyncedSkillStates(), isEmpty);
  });
}

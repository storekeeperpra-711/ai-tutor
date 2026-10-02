import 'dart:async';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../app/preferences.dart';
import 'auth_service.dart';
import 'connectivity.dart';
import 'local_db.dart';
import 'remote_store.dart';

/// Copies what is saved on the phone to Firestore.
///
/// Every write is idempotent (the same document gets the same data), so
/// sending something twice after a lost connection is harmless.
class SyncService {
  SyncService({
    required this.db,
    required this.remote,
    required this.auth,
    required this.prefs,
  });

  final LocalDb db;
  final RemoteStore remote;
  final AuthService auth;
  final SharedPreferences prefs;

  /// The account the phone's data was last uploaded to.
  static const syncedUidKey = 'syncedUid';

  var _running = false;
  var _again = false;

  /// Uploads everything waiting. Safe to call often: calls made while an
  /// upload runs are folded into one more round. Never throws; whatever
  /// fails stays in the queue for the next call.
  Future<void> sync() async {
    if (_running) {
      _again = true;
      return;
    }
    _running = true;
    try {
      do {
        _again = false;
        await _syncOnce();
      } while (_again);
    } catch (_) {
      // Offline or a server problem: the queue keeps everything.
    } finally {
      _running = false;
    }
  }

  Future<void> _syncOnce() async {
    final user = auth.currentUser;
    if (user == null) return;
    await useAccount(user);
    final uid = user.uid;
    for (final student in await db.unsyncedStudents()) {
      await remote.putStudent(uid, student);
      await db.markStudentSynced(student.id);
    }
    for (final upload in await db.pendingUploads()) {
      await remote.putProgress(uid, upload);
      await db.markStepsSynced(upload.steps);
    }
    for (final row in await db.unsyncedSkillStates()) {
      await remote.putSkill(uid, row);
      await db.markSkillSynced(row);
    }
  }

  /// Call when [user] may be a different account from the last upload:
  /// everything on the phone then has to go to the new account.
  Future<void> useAccount(AppUser user) async {
    final last = prefs.getString(syncedUidKey);
    if (last == user.uid) return;
    if (last != null) await db.markAllUnsynced();
    // The phone's own account; adult accounts get their role at sign-up.
    if (!user.isAdult) await remote.setRole(user.uid, AccountRole.device);
    await prefs.setString(syncedUidKey, user.uid);
  }

  /// Forgets the account (after signing out).
  Future<void> forgetAccount() => prefs.remove(syncedUidKey);
}

final syncServiceProvider = Provider<SyncService>((ref) {
  final service = SyncService(
    db: ref.watch(localDbProvider),
    remote: ref.watch(remoteStoreProvider),
    auth: ref.watch(authServiceProvider),
    prefs: ref.watch(sharedPreferencesProvider),
  );
  // Back online: sign in if needed, then upload the queue.
  ref.listen(onlineProvider, (previous, next) {
    if (next.value ?? false) {
      unawaited(service.auth.ensureSignedIn().then((_) => service.sync()));
    }
  }, fireImmediately: true);
  ref.listen(authUserProvider, (previous, next) {
    if (next.value != null) unawaited(service.sync());
  });
  return service;
});

/// Answers saved on the phone but not yet in the account.
final pendingSyncCountProvider = StreamProvider<int>(
  (ref) => ref.watch(localDbProvider).watchPendingCount(),
);

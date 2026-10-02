import 'dart:async';

import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../app/preferences.dart';
import 'auth_service.dart';
import 'local_db.dart';
import 'profiles.dart';
import 'remote_store.dart';
import 'sync_service.dart';

/// The adult account's role on this phone, remembered for the account
/// screen (`parent` or `teacher`).
const accountRoleKey = 'accountRole';

/// Signing in and out, and adding and removing learners.
class AccountActions {
  AccountActions(this.ref);

  final Ref ref;

  LocalDb get _db => ref.read(localDbProvider);
  AuthService get _auth => ref.read(authServiceProvider);
  RemoteStore get _remote => ref.read(remoteStoreProvider);
  SyncService get _sync => ref.read(syncServiceProvider);

  Future<void> signUp(String email, String password, AccountRole role) async {
    final user = await _auth.signUp(email, password);
    await _sync.useAccount(user);
    await _remote.setRole(user.uid, role);
    await ref
        .read(sharedPreferencesProvider)
        .setString(accountRoleKey, role.name);
    unawaited(_sync.sync());
  }

  /// Signs in and brings back the account's learners and progress.
  /// Learners already on this phone are added to the account.
  Future<void> signIn(String email, String password) async {
    final user = await _auth.signIn(email, password);
    await _sync.useAccount(user);
    final data = await _remote.fetchAll(user.uid);
    await _db.mergeRemote(data);
    if (data.role != null) {
      await ref
          .read(sharedPreferencesProvider)
          .setString(accountRoleKey, data.role!);
    }
    unawaited(_sync.sync());
  }

  /// Removes the learners from this phone; their work stays in the account.
  Future<void> signOut() async {
    ref.read(currentStudentProvider.notifier).clear();
    await _db.clearAll();
    await _sync.forgetAccount();
    await ref.read(sharedPreferencesProvider).remove(accountRoleKey);
    await _auth.signOut();
    unawaited(_auth.ensureSignedIn());
  }

  Future<Student> addStudent({
    required String firstName,
    required int grade,
    required String avatar,
    String? pin,
  }) async {
    final now = DateTime.now();
    final student = Student(
      id: newId(),
      firstName: firstName.trim(),
      grade: grade,
      avatar: avatar,
      pinHash: pin == null || pin.isEmpty ? null : hashPin(pin),
      createdAt: now,
      consentAt: now,
      synced: false,
    );
    await _db.addStudent(student);
    unawaited(_sync.sync());
    return student;
  }

  Future<void> removeStudent(Student student) async {
    if (ref.read(currentStudentProvider)?.id == student.id) {
      ref.read(currentStudentProvider.notifier).clear();
    }
    await _db.deleteStudent(student.id);
    final uid = _auth.currentUser?.uid;
    if (uid != null) {
      // Firestore queues the delete itself if the phone is offline.
      unawaited(_remote.deleteStudent(uid, student.id).catchError((_) {}));
    }
  }
}

final accountActionsProvider = Provider<AccountActions>(AccountActions.new);

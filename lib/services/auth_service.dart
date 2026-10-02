import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

/// Who is signed in: the phone itself (anonymous) or a parent or teacher.
class AppUser {
  const AppUser({required this.uid, this.email});

  final String uid;

  /// null for the phone's own anonymous account.
  final String? email;

  bool get isAdult => email != null;
}

/// Why signing in failed, for a friendly message.
enum AuthProblem {
  wrongPassword,
  emailInUse,
  weakPassword,
  invalidEmail,
  noConnection,
  other,
}

class AuthException implements Exception {
  const AuthException(this.problem);
  final AuthProblem problem;
}

/// Sign-in, behind an interface so tests can use a fake.
abstract class AuthService {
  AppUser? get currentUser;
  Stream<AppUser?> get userChanges;

  /// Signs the phone in anonymously if nobody is signed in. Fails quietly
  /// without internet; the app works anyway and tries again later.
  Future<void> ensureSignedIn();

  /// Creates a parent or teacher account. If the phone was signed in
  /// anonymously, that account becomes the new one, keeping its data.
  Future<AppUser> signUp(String email, String password);

  /// Signs in to an existing parent or teacher account.
  Future<AppUser> signIn(String email, String password);

  Future<void> signOut();
}

class FirebaseAuthService implements AuthService {
  FirebaseAuthService(this._auth);

  final FirebaseAuth _auth;

  static AppUser? _toAppUser(User? user) =>
      user == null ? null : AppUser(uid: user.uid, email: user.email);

  @override
  AppUser? get currentUser => _toAppUser(_auth.currentUser);

  @override
  Stream<AppUser?> get userChanges => _auth.userChanges().map(_toAppUser);

  @override
  Future<void> ensureSignedIn() async {
    if (_auth.currentUser != null) return;
    try {
      await _auth.signInAnonymously();
    } on FirebaseException {
      // Offline or not set up yet: try again when the connection is back.
    }
  }

  @override
  Future<AppUser> signUp(String email, String password) => _guard(() async {
    final credential = EmailAuthProvider.credential(
      email: email,
      password: password,
    );
    final current = _auth.currentUser;
    final result = current != null && current.isAnonymous
        ? await current.linkWithCredential(credential)
        : await _auth.createUserWithEmailAndPassword(
            email: email,
            password: password,
          );
    return _toAppUser(result.user)!;
  });

  @override
  Future<AppUser> signIn(String email, String password) => _guard(() async {
    final result = await _auth.signInWithEmailAndPassword(
      email: email,
      password: password,
    );
    return _toAppUser(result.user)!;
  });

  @override
  Future<void> signOut() => _auth.signOut();

  Future<T> _guard<T>(Future<T> Function() action) async {
    try {
      return await action();
    } on FirebaseAuthException catch (e) {
      throw AuthException(switch (e.code) {
        'wrong-password' ||
        'user-not-found' ||
        'invalid-credential' => AuthProblem.wrongPassword,
        'email-already-in-use' ||
        'credential-already-in-use' => AuthProblem.emailInUse,
        'weak-password' => AuthProblem.weakPassword,
        'invalid-email' => AuthProblem.invalidEmail,
        'network-request-failed' => AuthProblem.noConnection,
        _ => AuthProblem.other,
      });
    }
  }
}

final authServiceProvider = Provider<AuthService>(
  (ref) => throw UnimplementedError('Override in main() before use'),
);

/// The signed-in user, updated as they sign in and out.
final authUserProvider = StreamProvider<AppUser?>((ref) {
  final auth = ref.watch(authServiceProvider);
  return auth.userChanges;
});

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../app/preferences.dart';
import '../classes/class_store.dart';
import '../services/auth_service.dart';
import '../services/mastery_service.dart';
import '../services/remote_store.dart';
import 'dashboard_app.dart';
import 'dashboard_data.dart';

/// The Firebase web app's settings. The deploy workflow passes them with
/// --dart-define (deploy-dashboard.yml); they are public, not secrets.
const firebaseWebOptions = FirebaseOptions(
  apiKey: String.fromEnvironment('FIREBASE_API_KEY'),
  appId: String.fromEnvironment('FIREBASE_APP_ID'),
  messagingSenderId: String.fromEnvironment('FIREBASE_SENDER_ID'),
  projectId: String.fromEnvironment('FIREBASE_PROJECT_ID'),
  authDomain: String.fromEnvironment('FIREBASE_AUTH_DOMAIN'),
  storageBucket: String.fromEnvironment('FIREBASE_STORAGE_BUCKET'),
);

/// The teacher dashboard website. Build it with
/// `flutter build web -t lib/dashboard/main_dashboard.dart`.
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(options: firebaseWebOptions);
  final prefs = await SharedPreferences.getInstance();
  final firestore = FirebaseFirestore.instance;

  runApp(
    ProviderScope(
      overrides: [
        sharedPreferencesProvider.overrideWithValue(prefs),
        authServiceProvider.overrideWithValue(
          FirebaseAuthService(FirebaseAuth.instance),
        ),
        remoteStoreProvider.overrideWithValue(FirestoreRemoteStore(firestore)),
        classStoreProvider.overrideWithValue(FirestoreClassStore(firestore)),
        // No phone database here: lessons come from the bundle and
        // Firestore.
        curriculumProvider.overrideWith(
          (ref) => ref.watch(dashboardCurriculumProvider.future),
        ),
      ],
      child: const DashboardApp(),
    ),
  );
}

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:drift_flutter/drift_flutter.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'app/app.dart';
import 'app/preferences.dart';
import 'classes/class_store.dart';
import 'review/review_store.dart';
import 'services/auth_service.dart';
import 'services/local_db.dart';
import 'services/remote_store.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  // Connects to the Firebase project of this flavor (dev or prod), using
  // android/app/src/<flavor>/google-services.json.
  await Firebase.initializeApp();
  // Firestore keeps a copy on the phone and queues writes while offline.
  FirebaseFirestore.instance.settings = const Settings(
    persistenceEnabled: true,
  );
  final prefs = await SharedPreferences.getInstance();

  runApp(
    ProviderScope(
      overrides: [
        sharedPreferencesProvider.overrideWithValue(prefs),
        localDbProvider.overrideWithValue(
          LocalDb(driftDatabase(name: 'ai_tutor')),
        ),
        authServiceProvider.overrideWithValue(
          FirebaseAuthService(FirebaseAuth.instance),
        ),
        remoteStoreProvider.overrideWithValue(
          FirestoreRemoteStore(FirebaseFirestore.instance),
        ),
        reviewStoreProvider.overrideWithValue(
          FirestoreReviewStore(FirebaseFirestore.instance),
        ),
        classStoreProvider.overrideWithValue(
          FirestoreClassStore(FirebaseFirestore.instance),
        ),
      ],
      child: const AiTutorApp(),
    ),
  );
}

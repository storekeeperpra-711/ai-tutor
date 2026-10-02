import 'dart:async';

import 'package:drift/drift.dart';

/// Runs before every test file.
Future<void> testExecutable(FutureOr<void> Function() testMain) async {
  // Each test opens its own in-memory database on purpose.
  driftRuntimeOptions.dontWarnAboutMultipleDatabases = true;
  await testMain();
}

import 'dart:convert';
import 'dart:math';

import 'package:crypto/crypto.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../app/theme/age_tier.dart';
import 'local_db.dart';

/// All child profiles on this phone, oldest first.
final studentsProvider = StreamProvider<List<Student>>(
  (ref) => ref.watch(localDbProvider).watchStudents(),
);

/// The child using the app now, or null on the "Who is learning?" screen.
/// Kept in memory only, so after a restart each child picks themselves
/// again (and enters their PIN).
final currentStudentProvider = NotifierProvider<CurrentStudent, Student?>(
  CurrentStudent.new,
);

class CurrentStudent extends Notifier<Student?> {
  @override
  Student? build() => null;

  void select(Student student) {
    state = student;
    // The app's look follows the child's class.
    ref.read(ageTierProvider.notifier).setTier(tierForGrade(student.grade));
  }

  void clear() => state = null;
}

/// Each child's progress in every lesson, by lesson id.
final progressProvider =
    StreamProvider.family<Map<String, LessonProgress>, String>(
      (ref, studentId) => ref.watch(localDbProvider).watchProgress(studentId),
    );

/// Classes from Nursery (-1) and Prep (0) to Grade 12.
const grades = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

AgeTier tierForGrade(int grade) => switch (grade) {
  <= 2 => AgeTier.early,
  <= 5 => AgeTier.primary,
  <= 8 => AgeTier.middle,
  _ => AgeTier.older,
};

final _random = Random.secure();

/// A random id like Firestore's own, so ids made offline never clash.
String newId() {
  const chars =
      'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  return List.generate(20, (_) => chars[_random.nextInt(chars.length)]).join();
}

/// Stores a PIN as `salt:sha256(salt + pin)`, never the PIN itself.
String hashPin(String pin, {String? salt}) {
  final s = salt ?? newId();
  return '$s:${sha256.convert(utf8.encode('$s$pin'))}';
}

bool checkPin(String pin, String stored) {
  final salt = stored.split(':').first;
  return hashPin(pin, salt: salt) == stored;
}

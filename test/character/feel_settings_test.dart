import 'package:ai_tutor/app/preferences.dart';
import 'package:ai_tutor/character/feel_settings.dart';
import 'package:ai_tutor/services/profiles.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../fakes.dart';

void main() {
  test(
    'sounds and Mithu follow the age tier, then each child\'s choice',
    () async {
      SharedPreferences.setMockInitialValues({});
      final prefs = await SharedPreferences.getInstance();
      final container = ProviderContainer(
        overrides: [sharedPreferencesProvider.overrideWithValue(prefs)],
      );
      addTearDown(container.dispose);
      final current = container.read(currentStudentProvider.notifier);

      current.select(student('small', grade: 1));
      expect(container.read(soundsOnProvider), isTrue);
      expect(container.read(mithuOnProvider), isTrue);

      current.select(student('teen', grade: 10));
      expect(container.read(soundsOnProvider), isFalse);
      expect(container.read(mithuOnProvider), isFalse);
      await container.read(mithuOnProvider.notifier).set(true);
      expect(container.read(mithuOnProvider), isTrue);

      current.select(student('middle', grade: 7));
      expect(container.read(soundsOnProvider), isFalse);
      expect(container.read(mithuOnProvider), isTrue);

      // The older child's choice is kept for them only.
      current.select(student('teen', grade: 10));
      expect(container.read(mithuOnProvider), isTrue);
      expect(prefs.getBool('mithuOn.teen'), isTrue);
    },
  );
}

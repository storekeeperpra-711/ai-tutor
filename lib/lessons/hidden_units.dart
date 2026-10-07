/// Units kept in the app but not shown to children.
library;

import 'package:flutter_riverpod/flutter_riverpod.dart';

/// Grade 6 units that are not chapters of the PCTB Mathematics 6 book
/// (SNC 2022): Fractions, Decimals, Profit and loss and Whole numbers.
/// Their lessons stay saved (and open in the lesson previewer), but the
/// home screen, the daily plan and the teacher website leave them out.
/// tools/voice/make_voice.py records their voice last; keep the two lists
/// the same.
const hiddenUnits = {
  'g6-maths-02',
  'g6-maths-03',
  'g6-maths-12',
  'g6-maths-15',
};

/// The hidden units; tests that play a hidden lesson override it.
final hiddenUnitsProvider = Provider<Set<String>>((ref) => hiddenUnits);

/// Whether the lesson [id] belongs to one of the [hidden] units.
bool isHiddenLesson(String id, [Set<String> hidden = hiddenUnits]) =>
    hidden.any((u) => id.startsWith('$u-'));

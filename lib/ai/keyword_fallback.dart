import '../checkers/normalize.dart';
import 'ai_service.dart';

/// Scores an explanation without AI (offline, a used-up limit or an
/// error): each keyword group is one idea, written in English, Urdu and
/// Roman Urdu. All ideas found = got it, some = partly, none = not yet.
/// A very short answer is at most "partly", however many words match.
AiLevel scoreByKeywords(String answer, List<List<String>> groups) {
  final text = _normalize(answer);
  if (groups.isEmpty || text.isEmpty) return AiLevel.notYet;
  final found = groups
      .where((g) => g.any((word) => text.contains(_normalize(word))))
      .length;
  if (found == 0) return AiLevel.notYet;
  final words = text.split(RegExp(r'\s+')).length;
  return found == groups.length && words >= 5 ? AiLevel.gotIt : AiLevel.partly;
}

/// Lower case, standard digits, one space between words, and the Arabic
/// forms of ی and ک that some keyboards type.
String _normalize(String text) =>
    normalizeInput(text)
        .toLowerCase()
        .replaceAll('ي', 'ی')
        .replaceAll('ى', 'ی')
        .replaceAll('ك', 'ک')
        .replaceAll(RegExp(r'\s+'), ' ')
        .trim();

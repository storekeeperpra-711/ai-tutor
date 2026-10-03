import '../checkers/chem_equation_checker.dart';
import '../checkers/fraction_checker.dart';
import '../checkers/linear_equation_checker.dart';
import '../checkers/normalize.dart';
import '../checkers/numeric_checker.dart';
import '../checkers/rational.dart';
import '../l10n/app_localizations.dart';
import '../models/lesson_step.dart';

/// The result of checking one answer, ready to show to the student.
class AnswerCheck {
  const AnswerCheck.correct()
    : correct = true,
      countsAsAttempt = true,
      message = null,
      misconceptionId = null;

  const AnswerCheck.wrong(this.message, {this.misconceptionId})
    : correct = false,
      countsAsAttempt = true;

  /// The answer couldn't be read. Doesn't use up an attempt.
  const AnswerCheck.unreadable(this.message)
    : correct = false,
      countsAsAttempt = false,
      misconceptionId = null;

  /// Right value but not in the required form (e.g. not simplified).
  /// Doesn't use up an attempt either.
  const AnswerCheck.almost(this.message)
    : correct = false,
      countsAsAttempt = false,
      misconceptionId = null;

  final bool correct;
  final bool countsAsAttempt;

  /// Feedback naming the exact mistake, in the student's language.
  /// null means: show the general "try again" and the hint.
  final String? message;
  final String? misconceptionId;
}

/// Checks the answer to a `number` step.
AnswerCheck checkNumberStep(
  NumberStep step,
  String input,
  AppLocalizations l10n,
  String languageCode,
) {
  final value = parseRational(input);
  if (value == null) {
    return AnswerCheck.unreadable(
      step.checker == 'fraction' ? l10n.fractionUnreadable : l10n.typeANumber,
    );
  }

  if (step.checker == 'fraction') {
    final expected = _rationalOf(step.answer);
    final result = checkFraction(
      input,
      expected,
      requireSimplest: step.requireSimplest,
    );
    if (result.verdict == FractionVerdict.notSimplest) {
      return AnswerCheck.almost(l10n.fractionNotSimplest);
    }
    if (result.isCorrect) return const AnswerCheck.correct();
  } else if (numbersMatch(
    value.toDouble(),
    step.answer,
    tolerance: step.tolerance,
  )) {
    return const AnswerCheck.correct();
  }

  final known = step.commonWrong
      .where((w) => numbersMatch(value.toDouble(), w.answer))
      .firstOrNull;
  return AnswerCheck.wrong(
    known?.feedback.inLanguage(languageCode),
    misconceptionId: known?.misconceptionId,
  );
}

/// Checks the answer to a `text_check` step with the step's checker.
AnswerCheck checkTextStep(
  TextCheckStep step,
  String input,
  AppLocalizations l10n,
  String languageCode,
) {
  // A known common wrong answer gets its own feedback first.
  final squashed = _squash(input);
  final known = step.commonWrong
      .where((w) => _squash(w.answer) == squashed)
      .firstOrNull;
  if (known != null) {
    return AnswerCheck.wrong(
      known.feedback.inLanguage(languageCode),
      misconceptionId: known.misconceptionId,
    );
  }

  switch (step.checker) {
    case 'fraction':
      final result = checkFraction(
        input,
        parseRational(step.expected)!,
        requireSimplest: step.requireSimplest,
      );
      return switch (result.verdict) {
        FractionVerdict.correct => const AnswerCheck.correct(),
        FractionVerdict.notSimplest => AnswerCheck.almost(
          l10n.fractionNotSimplest,
        ),
        FractionVerdict.unreadable => AnswerCheck.unreadable(
          l10n.fractionUnreadable,
        ),
        FractionVerdict.wrong => const AnswerCheck.wrong(null),
      };

    case 'chem_equation':
      final result = checkChemEquation(input, step.expected);
      final d = result.details;
      return switch (result.mistake) {
        null => const AnswerCheck.correct(),
        ChemMistake.unreadable => AnswerCheck.unreadable(l10n.chemUnreadable),
        ChemMistake.unknownElement => AnswerCheck.unreadable(
          l10n.chemUnknownElement(d['symbol']! as String),
        ),
        ChemMistake.wrongSubstances => AnswerCheck.wrong(
          l10n.chemWrongSubstances,
        ),
        ChemMistake.changedSubscript => AnswerCheck.wrong(
          l10n.chemChangedSubscript(
            d['student']! as String,
            d['expected']! as String,
          ),
        ),
        ChemMistake.unbalanced => AnswerCheck.wrong(
          l10n.chemUnbalanced(
            d['element']! as String,
            d['left']! as int,
            d['right']! as int,
          ),
        ),
        ChemMistake.notLowestCoefficients => AnswerCheck.almost(
          l10n.chemNotLowest(d['divisor']! as int),
        ),
      };

    case 'linear_equation':
      final result = checkLinearWorking(
        input,
        step.expected,
        variable: step.variable,
      );
      return switch (result.mistake) {
        null => const AnswerCheck.correct(),
        LinearMistake.unreadable => AnswerCheck.unreadable(
          l10n.linearUnreadable(result.details['line']! as int),
        ),
        LinearMistake.brokenStep => AnswerCheck.wrong(
          l10n.linearBrokenStep(result.details['line']! as int),
        ),
        LinearMistake.notFinished => AnswerCheck.almost(
          l10n.linearNotFinished(step.variable),
        ),
      };

    case 'text':
      if (squashed.isEmpty) {
        return AnswerCheck.unreadable(l10n.answerUnreadable);
      }
      final accepted = [step.expected, ...step.accept].map(_squash);
      return accepted.contains(squashed)
          ? const AnswerCheck.correct()
          : const AnswerCheck.wrong(null);

    default:
      throw ArgumentError('Unknown checker ${step.checker}');
  }
}

/// Lower case, standard digits and symbols, no spaces: for comparing
/// typed answers.
String _squash(String text) =>
    normalizeInput(text).toLowerCase().replaceAll(RegExp(r'\s+'), '');

/// The exact fraction for a lesson's number (e.g. 0.75 -> 3/4).
Rational _rationalOf(double value) =>
    parseRational(value.toString()) ?? Rational.zero;

/// Checks a simulation's result against the `sim` step's `expected`,
/// with the same checkers (and feedback) as typed answers.
AnswerCheck checkSimResult(
  SimStep step,
  Map<String, dynamic> data,
  AppLocalizations l10n,
  String languageCode,
) {
  final expected = step.expected!;
  final value = data[expected.result];
  if (value == null) return AnswerCheck.unreadable(l10n.simNoResult);
  final input = switch (value) {
    final num n when n == n.roundToDouble() => n.toInt().toString(),
    _ => value.toString(),
  };

  if (expected.checker == 'numeric') {
    return checkNumberStep(
      NumberStep(
        id: step.id,
        type: 'number',
        prompt: step.prompt,
        answer: double.parse(expected.answer),
        checker: 'numeric',
        tolerance: expected.tolerance,
        hint: step.hint!,
        feedbackCorrect: step.feedbackCorrect!,
        feedbackWrong: step.feedbackWrong!,
        commonWrong: [
          for (final w in step.commonWrong)
            if (double.tryParse(w.answer) case final a?)
              CommonWrong(
                answer: a,
                feedback: w.feedback,
                misconceptionId: w.misconceptionId,
              ),
        ],
      ),
      input,
      l10n,
      languageCode,
    );
  }
  return checkTextStep(
    TextCheckStep(
      id: step.id,
      type: 'text_check',
      prompt: step.prompt,
      checker: expected.checker,
      expected: expected.answer,
      hint: step.hint!,
      feedbackCorrect: step.feedbackCorrect!,
      feedbackWrong: step.feedbackWrong!,
      commonWrong: step.commonWrong,
    ),
    input,
    l10n,
    languageCode,
  );
}

/// Checks a `photo_check` answer: working read from a photo (and confirmed
/// by the student) or typed. `linear_equation` checks every line; the other
/// checkers check the final answer.
AnswerCheck checkPhotoStep(
  PhotoCheckStep step,
  String input,
  AppLocalizations l10n,
  String languageCode,
) {
  final lines = input
      .split('\n')
      .map((l) => l.trim())
      .where((l) => l.isNotEmpty);
  if (lines.isEmpty) return AnswerCheck.unreadable(l10n.answerUnreadable);
  final last = lines.last;

  if (step.checker == 'numeric') {
    return checkNumberStep(
      NumberStep(
        id: step.id,
        type: 'number',
        prompt: step.problem,
        answer: double.parse(step.expected),
        checker: 'numeric',
        tolerance: step.tolerance,
        hint: step.hint,
        feedbackCorrect: step.feedbackCorrect,
        feedbackWrong: step.correctWorking,
        commonWrong: [
          for (final w in step.commonWrong)
            if (double.tryParse(w.answer) case final a?)
              CommonWrong(
                answer: a,
                feedback: w.feedback,
                misconceptionId: w.misconceptionId,
              ),
        ],
      ),
      _afterEquals(last),
      l10n,
      languageCode,
    );
  }
  return checkTextStep(
    TextCheckStep(
      id: step.id,
      type: 'text_check',
      prompt: step.problem,
      checker: step.checker,
      expected: step.expected,
      variable: step.variable,
      requireSimplest: step.requireSimplest,
      multiline: step.checksWorking,
      hint: step.hint,
      feedbackCorrect: step.feedbackCorrect,
      feedbackWrong: step.correctWorking,
      commonWrong: step.commonWrong,
    ),
    switch (step.checker) {
      'linear_equation' => lines.join('\n'),
      'fraction' => _afterEquals(last),
      _ => last,
    },
    l10n,
    languageCode,
  );
}

/// "x = 3/4" -> "3/4": a final answer written as an equation.
String _afterEquals(String line) => line.contains('=')
    ? line.substring(line.lastIndexOf('=') + 1).trim()
    : line;

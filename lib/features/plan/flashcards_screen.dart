import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../l10n/app_localizations.dart';
import '../../lessons/lesson_repository.dart';
import '../../lessons/lesson_text.dart';
import '../../services/mastery_service.dart';
import '../../services/profiles.dart';

/// A lesson's flashcards: tap to turn over, then the next card. Shown only
/// for topics already understood (spec B4).
class FlashcardsScreen extends ConsumerStatefulWidget {
  const FlashcardsScreen({super.key, required this.lessonId});

  final String lessonId;

  @override
  ConsumerState<FlashcardsScreen> createState() => _FlashcardsScreenState();
}

class _FlashcardsScreenState extends ConsumerState<FlashcardsScreen> {
  var _index = 0;
  var _turned = false;

  Future<void> _finish() async {
    final student = ref.read(currentStudentProvider);
    if (student != null) {
      await ref
          .read(planDoneProvider(student.id).notifier)
          .markDone('cards:${widget.lessonId}');
    }
    if (mounted) Navigator.of(context).pop();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final lesson = ref.watch(lessonProvider(widget.lessonId)).value;
    final cards = lesson?.flashcards ?? const [];
    final textTheme = Theme.of(context).textTheme;
    return Scaffold(
      appBar: AppBar(title: Text(l10n.flashcardsTitle)),
      body: cards.isEmpty
          ? const Center(child: CircularProgressIndicator())
          : Padding(
              padding: const EdgeInsets.all(24),
              child: Column(
                children: [
                  Text(l10n.flashcardTapToTurn),
                  const SizedBox(height: 16),
                  Expanded(
                    child: InkWell(
                      key: const Key('flashcard'),
                      onTap: () => setState(() => _turned = !_turned),
                      child: Card(
                        color: _turned
                            ? Theme.of(context).colorScheme.secondaryContainer
                            : null,
                        child: Center(
                          child: Padding(
                            padding: const EdgeInsets.all(24),
                            child: LessonText(
                              _turned
                                  ? cards[_index].back
                                  : cards[_index].front,
                              style: textTheme.headlineSmall,
                              textAlign: TextAlign.center,
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: 16),
                  Text('${_index + 1} / ${cards.length}'),
                  const SizedBox(height: 16),
                  SizedBox(
                    width: double.infinity,
                    child: FilledButton(
                      key: const Key('flashcard-next'),
                      onPressed: () => _index < cards.length - 1
                          ? setState(() {
                              _index++;
                              _turned = false;
                            })
                          : _finish(),
                      child: Text(
                        _index < cards.length - 1
                            ? l10n.nextCard
                            : l10n.markDone,
                      ),
                    ),
                  ),
                ],
              ),
            ),
    );
  }
}

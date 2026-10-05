import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../app/motion_widgets.dart';
import '../../app/theme/age_tier.dart';
import '../../character/mithu_bubble.dart';
import '../../character/sounds.dart';
import '../../l10n/app_localizations.dart';
import '../../models/lesson.dart';
import '../../models/lesson_step.dart';
import '../../models/localized_text.dart';
import '../../services/local_db.dart';
import '../../services/profiles.dart';
import '../effort/effort.dart';
import 'home_parts.dart';

/// Home for Nursery to Grade 2: a path through a village, one stop per
/// lesson with its stars, Mithu greeting the child, and one big Play
/// button. Nothing needs reading: Mithu says the greeting aloud and every
/// button is a picture.
class EarlyHome extends ConsumerWidget {
  const EarlyHome({super.key, required this.student});

  final Student student;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final l10n = AppLocalizations.of(context);
    final lessons = lessonsForTier(
      ref.watch(visibleLessonsProvider),
      AgeTier.early,
    );
    final progress = ref.watch(progressProvider(student.id)).value ?? const {};
    final stars = ref.watch(starsProvider(student.id));
    final next = nextLessonFor(lessons, progress);
    final greeting = LocalizedText(
      en: lookupAppLocalizations(const Locale('en'))
          .earlyGreeting(student.firstName),
      ur: lookupAppLocalizations(const Locale('ur'))
          .earlyGreeting(student.firstName),
    );

    return Column(
      key: const Key('early-home'),
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        EnterAnimation(
          child: Card(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(32),
            ),
            shadowColor: const Color(0x33B46E28),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  MithuBubble(
                    line: CharacterLine(emotion: 'happy', say: greeting),
                  ),
                  if (next != null) ...[
                    const SizedBox(height: 12),
                    Pressable(
                      child: SizedBox(
                        height: 96,
                        child: FilledButton.icon(
                          key: const Key('play-next'),
                          style: FilledButton.styleFrom(
                            backgroundColor: _playOrange,
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(28),
                            ),
                            elevation: 0,
                            textStyle: Theme.of(context)
                                .textTheme
                                .headlineMedium
                                ?.copyWith(fontWeight: FontWeight.w900),
                          ),
                          icon: const Icon(Icons.play_arrow_rounded, size: 64),
                          label: Text(l10n.playButton),
                          onPressed: () {
                            ref.playSound(Sound.tap);
                            context.push('/lesson/${next.id}');
                          },
                        ),
                      ),
                    ),
                  ],
                ],
              ),
            ),
          ),
        ),
        const SizedBox(height: 16),
        VillagePath(
          lessons: lessons,
          progress: progress,
          stars: stars,
          current: next?.id,
          onOpen: (lesson) {
            ref.playSound(Sound.tap);
            context.push('/lesson/${lesson.id}');
          },
        ),
      ],
    );
  }
}

const _playOrange = Color(0xFFF2820C);
const _doneGreen = Color(0xFF2E9D5B);
const _later = Color(0xFFEFE9E1);

/// Places on the path, in order. Each lesson stop gets the next one.
const _places = [
  Icons.home_rounded, // a house
  Icons.water_drop_rounded, // the well
  Icons.park_rounded, // the mango tree
  Icons.agriculture_rounded, // the fields
  Icons.mosque_rounded, // the mosque
  Icons.storefront_rounded, // the shop
  Icons.school_rounded, // the school
];

const _placeColors = [
  Color(0xFFFF8A65),
  Color(0xFF4FC3F7),
  Color(0xFF81C784),
  Color(0xFFFFD54F),
  Color(0xFFBA68C8),
  Color(0xFFF06292),
  Color(0xFF7986CB),
];

/// A winding path with a stop per lesson, zig-zagging down the screen.
class VillagePath extends StatelessWidget {
  const VillagePath({
    super.key,
    required this.lessons,
    required this.progress,
    required this.stars,
    required this.current,
    required this.onOpen,
  });

  final List<Lesson> lessons;
  final Map<String, LessonProgress> progress;
  final Map<String, int> stars;
  final String? current;
  final void Function(Lesson) onOpen;

  static const _rowHeight = 150.0;

  /// Where stop [i] sits across the path, 0 (left) to 1 (right).
  static double _across(int i) => 0.5 + 0.3 * math.sin(i * math.pi / 2);

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, box) {
        final width = box.maxWidth;
        final centres = [
          for (var i = 0; i < lessons.length; i++)
            Offset(width * _across(i), _rowHeight * i + 56),
        ];
        return SizedBox(
          height: _rowHeight * lessons.length,
          child: Stack(
            children: [
              Positioned.fill(
                child: CustomPaint(painter: _PathPainter(centres)),
              ),
              for (final (i, lesson) in lessons.indexed)
                Positioned(
                  left: centres[i].dx - 60,
                  top: centres[i].dy - 48,
                  width: 120,
                  child: _Stop(
                    lesson: lesson,
                    index: i,
                    done: progress[lesson.id]?.completed == true,
                    stars: stars[lesson.id] ?? 0,
                    current: lesson.id == current,
                    onTap: () => onOpen(lesson),
                  ),
                ),
            ],
          ),
        );
      },
    );
  }
}

class _PathPainter extends CustomPainter {
  _PathPainter(this.centres);

  final List<Offset> centres;

  @override
  void paint(Canvas canvas, Size size) {
    if (centres.length < 2) return;
    final path = Path()..moveTo(centres.first.dx, centres.first.dy);
    for (var i = 1; i < centres.length; i++) {
      final a = centres[i - 1];
      final b = centres[i];
      final midY = (a.dy + b.dy) / 2;
      path.cubicTo(a.dx, midY, b.dx, midY, b.dx, b.dy);
    }
    canvas.drawPath(
      path,
      Paint()
        ..color = const Color(0xFFD7B98E)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 28
        ..strokeCap = StrokeCap.round,
    );
    // Little stones along the dirt path.
    canvas.drawPath(
      path,
      Paint()
        ..color = const Color(0xFFBF9F6F)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 4
        ..strokeCap = StrokeCap.round,
    );
  }

  @override
  bool shouldRepaint(_PathPainter old) => old.centres != centres;
}

class _Stop extends StatelessWidget {
  const _Stop({
    required this.lesson,
    required this.index,
    required this.done,
    required this.stars,
    required this.current,
    required this.onTap,
  });

  final Lesson lesson;
  final int index;
  final bool done;
  final int stars;
  final bool current;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final color = _placeColors[index % _placeColors.length];
    return Semantics(
      button: true,
      label: lesson.title.of(context),
      child: Column(
        children: [
          InkResponse(
            key: Key('village-stop-${lesson.id}'),
            onTap: onTap,
            radius: 48,
            child: Container(
              width: 88,
              height: 88,
              decoration: BoxDecoration(
                color: done
                    ? _doneGreen
                    : current
                    ? Colors.white
                    : _later,
                borderRadius: BorderRadius.circular(30),
                border: current
                    ? Border.all(color: _playOrange, width: 4)
                    : null,
                boxShadow: [
                  BoxShadow(
                    color: done
                        ? const Color(0xFF1F7A45)
                        : current
                        ? _playOrange.withValues(alpha: 0.5)
                        : const Color(0xFFE2D6C6),
                    offset: current ? Offset.zero : const Offset(0, 4),
                    blurRadius: current ? 18 : 0,
                    spreadRadius: current ? 2 : 0,
                  ),
                ],
              ),
              child: Icon(
                done ? Icons.check_rounded : _places[index % _places.length],
                size: 48,
                color: done ? Colors.white : color,
              ),
            ),
          ),
          const SizedBox(height: 4),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              for (var i = 0; i < 3; i++)
                Icon(
                  i < stars ? Icons.star_rounded : Icons.star_outline_rounded,
                  size: 24,
                  color: i < stars
                      ? const Color(0xFFF2A20C)
                      : const Color(0xFFD9D4C8),
                ),
            ],
          ),
        ],
      ),
    );
  }
}

/// Units: the chapters lessons belong to, for the course progress view.
library;

import '../models/lesson.dart';
import '../models/localized_text.dart';

/// The unit of lesson [id]: the first three parts of the id, like
/// `g6-maths-05` for `g6-maths-05-hcf`.
String unitIdOf(String id) => id.split('-').take(3).join('-');

/// Unit names. A unit missing here is shown by its subject and number.
const unitTitles = <String, LocalizedText>{
  'g0-maths-01': LocalizedText(en: 'Counting', ur: 'گنتی'),
  'g6-maths-01': LocalizedText(en: 'Sets', ur: 'سیٹ'),
  'g6-maths-02': LocalizedText(en: 'Fractions', ur: 'کسور'),
  'g6-maths-03': LocalizedText(en: 'Decimals', ur: 'اعشاریے'),
  'g6-maths-04': LocalizedText(en: 'Integers', ur: 'صحیح اعداد'),
  'g6-maths-05': LocalizedText(
    en: 'Factors and multiples',
    ur: 'اجزائے ضربی اور اضعاف',
  ),
  'g6-maths-06': LocalizedText(
    en: 'Rate, ratio and proportion',
    ur: 'شرح، نسبت اور تناسب',
  ),
  'g6-maths-07': LocalizedText(en: 'Algebraic expressions', ur: 'الجبری جملے'),
  'g6-maths-08': LocalizedText(en: 'Perimeter and area', ur: 'احاطہ اور رقبہ'),
  'g6-maths-09': LocalizedText(en: 'Angles', ur: 'زاویے'),
  'g6-maths-10': LocalizedText(en: 'Data handling', ur: 'مواد کا انتظام'),
  'g6-maths-11': LocalizedText(en: 'Percentages', ur: 'فیصد'),
  'g6-maths-12': LocalizedText(en: 'Profit and loss', ur: 'نفع اور نقصان'),
  'g6-maths-13': LocalizedText(
    en: 'BODMAS and simplifying',
    ur: 'BODMAS اور سادہ کرنا',
  ),
  'g6-maths-14': LocalizedText(
    en: 'Surface area and volume',
    ur: 'سطحی رقبہ اور حجم',
  ),
  'g6-maths-15': LocalizedText(en: 'Whole numbers', ur: 'مکمل اعداد'),
  'g6-maths-16': LocalizedText(en: 'Linear equations', ur: 'خطی مساوات'),
  'g6-maths-17': LocalizedText(en: 'Probability', ur: 'احتمال'),
  'g6-maths-18': LocalizedText(en: 'Symmetry', ur: 'تشاکل'),
  'g6-maths-19': LocalizedText(
    en: 'Geometrical constructions',
    ur: 'ہندسی تعمیرات',
  ),
  'g9-maths-05': LocalizedText(
    en: 'Linear equations and inequalities',
    ur: 'خطی مساوات اور نامساوات',
  ),
  'g10-chemistry-15': LocalizedText(
    en: 'Chemical equations',
    ur: 'کیمیائی مساوات',
  ),
};

/// A chapter of the book: its title and its lessons, in teaching order
/// (each chapter's unit test last).
class BookChapter {
  const BookChapter(this.title, this.lessons);

  final LocalizedText title;
  final List<String> lessons;
}

/// A domain of the book (like "Numbers and Operations") and its chapters.
class BookDomain {
  const BookDomain(this.title, this.chapters);

  final LocalizedText title;
  final List<BookChapter> chapters;
}

/// The contents of the PCTB Mathematics 6 book (SNC 2022), with the
/// lessons that teach each chapter. Units the book has no chapter for are
/// placed in the nearest one: Simplification (BODMAS) is in Laws of
/// Integers as in the book, Percentages in Rate, Ratio and Percentage,
/// Perimeter and area in Surface Area and Volume, and Angles in
/// Geometrical Constructions. A new Grade 6 lesson must be added here, or
/// it is shown after the book under "More practice".
const grade6Book = [
  BookDomain(
    LocalizedText(en: 'Numbers and Operations', ur: 'اعداد اور عملیات'),
    [
      BookChapter(
        LocalizedText(en: 'Factors and Multiples', ur: 'اجزائے ضربی اور اضعاف'),
        [
          'g6-maths-05-factors-and-multiples',
          'g6-maths-05-prime-numbers',
          'g6-maths-05-highest-common-factor',
          'g6-maths-05-lowest-common-multiple',
          'g6-maths-05-hcf-times-lcm',
          'g6-maths-05-squares-and-index-notation',
          'g6-maths-05-factor-word-problems',
          'g6-maths-05-exercise-1-1',
          'g6-maths-05-exercise-1-2',
          'g6-maths-05-exercise-1-3',
          'g6-maths-05-exercise-1-4',
          'g6-maths-05-exercise-1-5',
          'g6-maths-05-exercise-1-6',
          'g6-maths-05-chapter-1-test',
        ],
      ),
      BookChapter(LocalizedText(en: 'Integers', ur: 'صحیح اعداد'), [
        'g6-maths-04-what-are-integers',
        'g6-maths-04-absolute-value',
        'g6-maths-04-exercise-2-1',
        'g6-maths-04-exercise-2-2',
        'g6-maths-04-chapter-2-test',
      ]),
      BookChapter(
        LocalizedText(en: 'Laws of Integers', ur: 'صحیح اعداد کے قوانین'),
        [
          'g6-maths-04-adding-integers',
          'g6-maths-04-subtracting-integers',
          'g6-maths-04-multiplying-and-dividing-integers',
          'g6-maths-04-laws-of-integers',
          'g6-maths-04-integer-word-problems',
          'g6-maths-13-order-of-operations',
          'g6-maths-13-brackets',
          'g6-maths-13-fractions-decimals',
          'g6-maths-13-estimation',
          'g6-maths-13-simplification-word-problems',
          'g6-maths-04-exercise-3-1',
          'g6-maths-04-exercise-3-2',
          'g6-maths-04-exercise-3-3',
          'g6-maths-04-chapter-3-test',
        ],
      ),
      BookChapter(
        LocalizedText(
          en: 'Rate, Ratio and Percentage',
          ur: 'شرح، نسبت اور فیصد',
        ),
        [
          'g6-maths-06-what-is-a-ratio',
          'g6-maths-06-equivalent-ratios',
          'g6-maths-06-sharing-in-a-ratio',
          'g6-maths-06-continued-ratio',
          'g6-maths-06-proportion',
          'g6-maths-06-unitary-method',
          'g6-maths-06-rate',
          'g6-maths-11-what-is-a-percent',
          'g6-maths-11-percents-fractions-decimals',
          'g6-maths-11-percent-of-an-amount',
          'g6-maths-11-finding-the-percentage',
          'g6-maths-11-percentage-change',
          'g6-maths-11-percent-word-problems',
          'g6-maths-06-24-hour-clock',
          'g6-maths-06-speed',
          'g6-maths-06-ratio-word-problems',
          'g6-maths-06-exercise-4-1',
          'g6-maths-06-exercise-4-2',
          'g6-maths-06-exercise-4-3',
          'g6-maths-06-exercise-4-4',
          'g6-maths-06-exercise-4-5',
          'g6-maths-06-chapter-4-test',
        ],
      ),
      BookChapter(LocalizedText(en: 'Sets', ur: 'سیٹ'), [
        'g6-maths-01-what-is-a-set',
        'g6-maths-01-kinds-of-sets',
        'g6-maths-01-subsets',
        'g6-maths-01-universal-set-and-venn-diagrams',
        'g6-maths-01-union-and-intersection',
        'g6-maths-01-set-word-problems',
        'g6-maths-01-exercise-5-1',
        'g6-maths-01-exercise-5-2',
        'g6-maths-01-exercise-5-3',
        'g6-maths-01-chapter-5-test',
      ]),
    ],
  ),
  BookDomain(LocalizedText(en: 'Algebra', ur: 'الجبرا'), [
    BookChapter(LocalizedText(en: 'Algebraic Expressions', ur: 'الجبری جملے'), [
      'g6-maths-07-letters-for-numbers',
      'g6-maths-07-terms-and-coefficients',
      'g6-maths-07-substitution',
      'g6-maths-07-number-patterns',
      'g6-maths-07-like-terms',
      'g6-maths-07-adding-subtracting-expressions',
      'g6-maths-07-simple-equations',
      'g6-maths-07-algebra-word-problems',
      'g6-maths-07-exercise-6-1',
      'g6-maths-07-exercise-6-2',
      'g6-maths-07-exercise-6-3',
      'g6-maths-07-exercise-6-4',
      'g6-maths-07-exercise-6-5',
      'g6-maths-07-chapter-6-test',
    ]),
    BookChapter(
      LocalizedText(
        en: 'Linear Expressions and Equations',
        ur: 'خطی جملے اور مساوات',
      ),
      [
        'g6-maths-16-equations-and-expressions',
        'g6-maths-16-checking-solutions',
        'g6-maths-16-forming-equations',
        'g6-maths-16-two-step-equations',
        'g6-maths-16-equations-with-brackets',
        'g6-maths-16-equation-word-problems',
        'g6-maths-16-exercise-7-1',
        'g6-maths-16-exercise-7-2',
        'g6-maths-16-chapter-7-test',
      ],
    ),
  ]),
  BookDomain(LocalizedText(en: 'Measurement', ur: 'پیمائش'), [
    BookChapter(
      LocalizedText(en: 'Surface Area and Volume', ur: 'سطحی رقبہ اور حجم'),
      [
        'g6-maths-08-perimeter',
        'g6-maths-08-area-of-rectangles',
        'g6-maths-08-compound-shapes',
        'g6-maths-08-area-of-triangles',
        'g6-maths-08-parallelogram-and-trapezium',
        'g6-maths-08-area-of-a-path',
        'g6-maths-08-area-word-problems',
        'g6-maths-14-solids',
        'g6-maths-14-volume-cuboid',
        'g6-maths-14-volume-cube',
        'g6-maths-14-surface-area',
        'g6-maths-14-solids-word-problems',
        'g6-maths-08-exercise-8-1',
        'g6-maths-08-exercise-8-2',
        'g6-maths-14-exercise-8-3',
        'g6-maths-14-chapter-8-test',
      ],
    ),
  ]),
  BookDomain(LocalizedText(en: 'Geometry', ur: 'جیومیٹری'), [
    BookChapter(LocalizedText(en: 'Symmetry', ur: 'تشاکل'), [
      'g6-maths-18-1d-2d-3d-shapes',
      'g6-maths-18-parallel-lines-and-transversal',
      'g6-maths-18-line-symmetry',
      'g6-maths-18-rotational-symmetry',
      'g6-maths-18-exercise-9-1',
      'g6-maths-18-exercise-9-2',
      'g6-maths-18-exercise-9-3',
      'g6-maths-18-chapter-9-test',
    ]),
    BookChapter(
      LocalizedText(en: 'Geometrical Constructions', ur: 'ہندسی تعمیرات'),
      [
        'g6-maths-09-types-of-angles',
        'g6-maths-09-angles-on-a-line',
        'g6-maths-09-complementary-supplementary',
        'g6-maths-09-angles-in-a-triangle',
        'g6-maths-09-angle-word-problems',
        'g6-maths-19-bisectors-and-perpendiculars',
        'g6-maths-19-constructing-angles',
        'g6-maths-19-unknown-angles-and-construction-problems',
        'g6-maths-19-exercise-10-1',
        'g6-maths-19-exercise-10-2',
        'g6-maths-09-exercise-10-3',
        'g6-maths-19-chapter-10-test',
      ],
    ),
  ]),
  BookDomain(
    LocalizedText(en: 'Statistics and Probability', ur: 'شماریات اور احتمال'),
    [
      BookChapter(LocalizedText(en: 'Data Management', ur: 'مواد کا انتظام'), [
        'g6-maths-10-tables-and-tallies',
        'g6-maths-10-kinds-of-data',
        'g6-maths-10-bar-graphs',
        'g6-maths-10-pie-charts-and-multiple-bar-graphs',
        'g6-maths-10-average-mean',
        'g6-maths-10-median',
        'g6-maths-10-mode-and-range',
        'g6-maths-10-data-word-problems',
        'g6-maths-10-exercise-11-1',
        'g6-maths-10-exercise-11-2',
        'g6-maths-10-exercise-11-3',
        'g6-maths-10-exercise-11-4',
        'g6-maths-10-chapter-11-test',
      ]),
      BookChapter(LocalizedText(en: 'Probability', ur: 'احتمال'), [
        'g6-maths-17-sample-space',
        'g6-maths-17-probability-of-an-event',
        'g6-maths-17-likelihood',
        'g6-maths-17-probability-word-problems',
      ]),
    ],
  ),
];

/// The order lessons are taught in, for units that are not in the book
/// (each unit test last). Lessons not listed come after, by
/// [teachingOrder].
const lessonOrder = <String, List<String>>{
  'g6-maths-02': [
    'g6-maths-02-equivalent-fractions',
    'g6-maths-02-adding-fractions',
    'g6-maths-02-mixed-numbers',
    'g6-maths-02-multiplying-fractions',
    'g6-maths-02-dividing-fractions',
    'g6-maths-02-fraction-word-problems',
  ],
  'g6-maths-03': [
    'g6-maths-03-decimals-and-place-value',
    'g6-maths-03-comparing-decimals',
    'g6-maths-03-adding-and-subtracting-decimals',
    'g6-maths-03-multiplying-and-dividing-decimals',
    'g6-maths-03-decimal-word-problems',
  ],
  'g6-maths-12': [
    'g6-maths-12-profit-and-loss',
    'g6-maths-12-profit-loss-percent',
    'g6-maths-12-selling-price',
    'g6-maths-12-bills-and-change',
    'g6-maths-12-profit-loss-word-problems',
  ],
  'g6-maths-15': [
    'g6-maths-15-lakhs-and-crores',
    'g6-maths-15-millions',
    'g6-maths-15-comparing-numbers',
    'g6-maths-15-properties',
    'g6-maths-15-whole-number-word-problems',
  ],
};

/// One unit (a chapter of the book, or one of our own units) and its
/// lessons, in teaching order.
class CourseUnit {
  const CourseUnit({required this.id, required this.lessons, this.name});

  final String id;
  final List<Lesson> lessons;

  /// The chapter's title in the book; null for our own units.
  final LocalizedText? name;

  LocalizedText get title {
    if (name case final name?) return name;
    if (unitTitles[id] case final title?) return title;
    final number = id.split('-').last;
    return LocalizedText(en: 'Unit $number', ur: 'یونٹ $number');
  }
}

/// A group of units under one heading: a domain of the book, "More
/// practice" for lessons the book has no chapter for, or (with no title)
/// the units of other classes.
class CourseDomain {
  const CourseDomain({required this.title, required this.units});

  final LocalizedText? title;
  final List<CourseUnit> units;
}

const morePractice = LocalizedText(en: 'More practice', ur: 'مزید مشق');

/// [lessons] grouped like the book: its domains and chapters in book
/// order (chapter ids `g6-book-01` to `g6-book-12`), then the units the
/// book has no chapter for. Lessons of other grades are grouped by unit,
/// by grade then id, under no heading.
List<CourseDomain> courseDomains(List<Lesson> lessons) {
  final byId = {for (final l in lessons) l.id: l};
  final used = <String>{};
  final domains = <CourseDomain>[];
  var number = 0;
  for (final domain in grade6Book) {
    final units = <CourseUnit>[];
    for (final chapter in domain.chapters) {
      number++;
      final found = [for (final id in chapter.lessons) ?byId[id]];
      if (found.isEmpty) continue;
      used.addAll(found.map((l) => l.id));
      units.add(
        CourseUnit(
          id: 'g6-book-${number.toString().padLeft(2, '0')}',
          lessons: found,
          name: chapter.title,
        ),
      );
    }
    if (units.isNotEmpty) {
      // Numbered as in the book's contents: "1. Numbers and Operations".
      final n = grade6Book.indexOf(domain) + 1;
      final title = LocalizedText(
        en: '$n. ${domain.title.en}',
        ur: '$n. ${domain.title.ur}',
      );
      domains.add(CourseDomain(title: title, units: units));
    }
  }
  final rest = lessons.where((l) => !used.contains(l.id)).toList();
  final extra = _units(rest.where((l) => l.grade == 6).toList());
  if (extra.isNotEmpty) {
    domains.add(CourseDomain(title: morePractice, units: extra));
  }
  final others = _units(rest.where((l) => l.grade != 6).toList());
  if (others.isNotEmpty) {
    domains.add(CourseDomain(title: null, units: others));
  }
  return domains;
}

/// [lessons] grouped by their unit id, by grade then id.
List<CourseUnit> _units(List<Lesson> lessons) {
  final byUnit = <String, List<Lesson>>{};
  for (final l in lessons) {
    (byUnit[unitIdOf(l.id)] ??= []).add(l);
  }
  final ids = byUnit.keys.toList()
    ..sort((a, b) {
      final ga = byUnit[a]!.first.grade, gb = byUnit[b]!.first.grade;
      return ga != gb ? ga.compareTo(gb) : a.compareTo(b);
    });
  return [
    for (final id in ids)
      CourseUnit(id: id, lessons: _ordered(id, byUnit[id]!)),
  ];
}

List<Lesson> _ordered(String unit, List<Lesson> lessons) {
  final listed = lessonOrder[unit] ?? const <String>[];
  int place(Lesson l) => listed.indexOf(l.id);
  return [
    ...lessons.where((l) => place(l) >= 0).toList()
      ..sort((a, b) => place(a).compareTo(place(b))),
    ...teachingOrder(lessons.where((l) => place(l) < 0).toList()),
  ];
}

/// [lessons] so that each comes after the lessons teaching its
/// prerequisites; otherwise by id.
List<Lesson> teachingOrder(List<Lesson> lessons) {
  final left = List.of(lessons)..sort((a, b) => a.id.compareTo(b.id));
  final ordered = <Lesson>[];
  final taught = <String>{};
  final teachable = {for (final l in left) ...l.skills};
  while (left.isNotEmpty) {
    final next = left.firstWhere(
      (l) => l.prerequisites
          .map((p) => p.skill)
          .where(teachable.contains)
          .where((s) => !l.skills.contains(s))
          .every(taught.contains),
      orElse: () => left.first,
    );
    left.remove(next);
    ordered.add(next);
    taught.addAll(next.skills);
  }
  return ordered;
}

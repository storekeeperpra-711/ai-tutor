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

/// Grade 6 units in the order of the PCTB Mathematics 6 book (SNC 2022).
/// Units not listed come after, by id.
const _bookOrder = [
  'g6-maths-05',
  'g6-maths-04',
  'g6-maths-13',
  'g6-maths-06',
  'g6-maths-11',
  'g6-maths-01',
  'g6-maths-07',
  'g6-maths-16',
  'g6-maths-08',
  'g6-maths-14',
  'g6-maths-18',
  'g6-maths-09',
  'g6-maths-19',
  'g6-maths-10',
  'g6-maths-17',
];

/// The order lessons are taught in, per unit (the book's order, with each
/// unit test last). Lessons not listed come after, by [teachingOrder].
const lessonOrder = <String, List<String>>{
  'g6-maths-05': [
    'g6-maths-05-factors-and-multiples',
    'g6-maths-05-prime-numbers',
    'g6-maths-05-highest-common-factor',
    'g6-maths-05-lowest-common-multiple',
    'g6-maths-05-hcf-times-lcm',
    'g6-maths-05-squares-and-index-notation',
    'g6-maths-05-factor-word-problems',
  ],
  'g6-maths-04': [
    'g6-maths-04-what-are-integers',
    'g6-maths-04-absolute-value',
    'g6-maths-04-adding-integers',
    'g6-maths-04-subtracting-integers',
    'g6-maths-04-multiplying-and-dividing-integers',
    'g6-maths-04-laws-of-integers',
    'g6-maths-04-integer-word-problems',
  ],
  'g6-maths-13': [
    'g6-maths-13-order-of-operations',
    'g6-maths-13-brackets',
    'g6-maths-13-fractions-decimals',
    'g6-maths-13-estimation',
    'g6-maths-13-simplification-word-problems',
  ],
  'g6-maths-06': [
    'g6-maths-06-what-is-a-ratio',
    'g6-maths-06-equivalent-ratios',
    'g6-maths-06-continued-ratio',
    'g6-maths-06-sharing-in-a-ratio',
    'g6-maths-06-proportion',
    'g6-maths-06-unitary-method',
    'g6-maths-06-rate',
    'g6-maths-06-24-hour-clock',
    'g6-maths-06-speed',
    'g6-maths-06-ratio-word-problems',
  ],
  'g6-maths-11': [
    'g6-maths-11-what-is-a-percent',
    'g6-maths-11-percents-fractions-decimals',
    'g6-maths-11-percent-of-an-amount',
    'g6-maths-11-finding-the-percentage',
    'g6-maths-11-percentage-change',
    'g6-maths-11-percent-word-problems',
  ],
  'g6-maths-01': [
    'g6-maths-01-what-is-a-set',
    'g6-maths-01-kinds-of-sets',
    'g6-maths-01-subsets',
    'g6-maths-01-universal-set-and-venn-diagrams',
    'g6-maths-01-union-and-intersection',
    'g6-maths-01-set-word-problems',
  ],
  'g6-maths-07': [
    'g6-maths-07-number-patterns',
    'g6-maths-07-letters-for-numbers',
    'g6-maths-07-terms-and-coefficients',
    'g6-maths-07-substitution',
    'g6-maths-07-like-terms',
    'g6-maths-07-adding-subtracting-expressions',
    'g6-maths-07-simple-equations',
    'g6-maths-07-algebra-word-problems',
  ],
  'g6-maths-16': [
    'g6-maths-16-equations-and-expressions',
    'g6-maths-16-checking-solutions',
    'g6-maths-16-forming-equations',
    'g6-maths-16-two-step-equations',
    'g6-maths-16-equations-with-brackets',
    'g6-maths-16-equation-word-problems',
  ],
  'g6-maths-08': [
    'g6-maths-08-perimeter',
    'g6-maths-08-area-of-rectangles',
    'g6-maths-08-area-of-triangles',
    'g6-maths-08-parallelogram-and-trapezium',
    'g6-maths-08-compound-shapes',
    'g6-maths-08-area-of-a-path',
    'g6-maths-08-area-word-problems',
  ],
  'g6-maths-14': [
    'g6-maths-14-solids',
    'g6-maths-14-surface-area',
    'g6-maths-14-volume-cuboid',
    'g6-maths-14-volume-cube',
    'g6-maths-14-solids-word-problems',
  ],
  'g6-maths-18': [
    'g6-maths-18-1d-2d-3d-shapes',
    'g6-maths-18-parallel-lines-and-transversal',
    'g6-maths-18-line-symmetry',
    'g6-maths-18-rotational-symmetry',
  ],
  'g6-maths-09': [
    'g6-maths-09-types-of-angles',
    'g6-maths-09-angles-on-a-line',
    'g6-maths-09-complementary-supplementary',
    'g6-maths-09-angles-in-a-triangle',
    'g6-maths-09-angle-word-problems',
  ],
  'g6-maths-19': [
    'g6-maths-19-bisectors-and-perpendiculars',
    'g6-maths-19-constructing-angles',
    'g6-maths-19-unknown-angles-and-construction-problems',
  ],
  'g6-maths-10': [
    'g6-maths-10-kinds-of-data',
    'g6-maths-10-tables-and-tallies',
    'g6-maths-10-bar-graphs',
    'g6-maths-10-pie-charts-and-multiple-bar-graphs',
    'g6-maths-10-average-mean',
    'g6-maths-10-median',
    'g6-maths-10-mode-and-range',
    'g6-maths-10-data-word-problems',
  ],
  'g6-maths-17': [
    'g6-maths-17-sample-space',
    'g6-maths-17-probability-of-an-event',
    'g6-maths-17-likelihood',
    'g6-maths-17-probability-word-problems',
  ],
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

/// One unit and its lessons, in teaching order.
class CourseUnit {
  const CourseUnit({required this.id, required this.lessons});

  final String id;
  final List<Lesson> lessons;

  LocalizedText get title {
    if (unitTitles[id] case final title?) return title;
    final number = id.split('-').last;
    return LocalizedText(en: 'Unit $number', ur: 'یونٹ $number');
  }
}

/// [lessons] grouped into units: by grade, then book order, then id.
/// Inside a unit, a lesson comes after the lessons that teach the skills
/// it needs.
List<CourseUnit> courseUnits(List<Lesson> lessons) {
  final byUnit = <String, List<Lesson>>{};
  for (final l in lessons) {
    (byUnit[unitIdOf(l.id)] ??= []).add(l);
  }
  int rank(String unit) {
    final i = _bookOrder.indexOf(unit);
    return i < 0 ? _bookOrder.length : i;
  }

  final ids = byUnit.keys.toList()
    ..sort((a, b) {
      final ga = byUnit[a]!.first.grade, gb = byUnit[b]!.first.grade;
      if (ga != gb) return ga.compareTo(gb);
      final r = rank(a).compareTo(rank(b));
      return r != 0 ? r : a.compareTo(b);
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

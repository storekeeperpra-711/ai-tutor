// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'figure.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

StepFigure _$StepFigureFromJson(Map<String, dynamic> json) =>
    $checkedCreate('StepFigure', json, ($checkedConvert) {
      final val = StepFigure(
        width: $checkedConvert('width', (v) => (v as num).toDouble()),
        height: $checkedConvert('height', (v) => (v as num).toDouble()),
        alt: $checkedConvert(
          'alt',
          (v) => LocalizedText.fromJson(v as Map<String, dynamic>),
        ),
        items: $checkedConvert(
          'items',
          (v) => (v as List<dynamic>)
              .map((e) => FigureItem.fromJson(e as Map<String, dynamic>))
              .toList(),
        ),
      );
      return val;
    });

FigureItem _$FigureItemFromJson(Map<String, dynamic> json) =>
    $checkedCreate('FigureItem', json, ($checkedConvert) {
      final val = FigureItem(
        kind: $checkedConvert('kind', (v) => v as String),
        points: $checkedConvert(
          'points',
          (v) =>
              (v as List<dynamic>?)
                  ?.map(
                    (e) => (e as List<dynamic>)
                        .map((e) => (e as num).toDouble())
                        .toList(),
                  )
                  .toList() ??
              const [],
        ),
        from: $checkedConvert(
          'from',
          (v) =>
              (v as List<dynamic>?)?.map((e) => (e as num).toDouble()).toList(),
        ),
        to: $checkedConvert(
          'to',
          (v) =>
              (v as List<dynamic>?)?.map((e) => (e as num).toDouble()).toList(),
        ),
        center: $checkedConvert(
          'center',
          (v) =>
              (v as List<dynamic>?)?.map((e) => (e as num).toDouble()).toList(),
        ),
        at: $checkedConvert(
          'at',
          (v) =>
              (v as List<dynamic>?)?.map((e) => (e as num).toDouble()).toList(),
        ),
        radius: $checkedConvert('radius', (v) => (v as num?)?.toDouble() ?? 0),
        start: $checkedConvert('start', (v) => (v as num?)?.toDouble() ?? 0),
        sweep: $checkedConvert('sweep', (v) => (v as num?)?.toDouble() ?? 0),
        fill: $checkedConvert('fill', (v) => v as bool? ?? false),
        style: $checkedConvert('style', (v) => v as String? ?? 'solid'),
        text: $checkedConvert('text', (v) => v as String?),
      );
      return val;
    });

import 'dart:ui' show Offset;

import 'package:json_annotation/json_annotation.dart';

import 'localized_text.dart';

part 'figure.g.dart';

/// A simple drawing in a lesson step (lines, shapes, angle marks, labels),
/// drawn by the app itself, so it needs no image file and works offline.
/// Coordinates are in a [width] x [height] box with (0, 0) at the top left
/// and y going down; the app scales the box to fit the screen.
@JsonSerializable()
class StepFigure {
  const StepFigure({
    required this.width,
    required this.height,
    required this.alt,
    required this.items,
  });

  factory StepFigure.fromJson(Map<String, dynamic> json) =>
      _$StepFigureFromJson(json);

  final double width;
  final double height;

  /// What the picture shows, in words (for screen readers).
  final LocalizedText alt;
  final List<FigureItem> items;
}

/// One thing in a figure. Which fields are set depends on [kind]:
/// polygon (points, fill), line (from, to), circle (center, radius, fill),
/// arc (center, radius, start, sweep), point (at) or label (at, text).
@JsonSerializable()
class FigureItem {
  const FigureItem({
    required this.kind,
    this.points = const [],
    this.from,
    this.to,
    this.center,
    this.at,
    this.radius = 0,
    this.start = 0,
    this.sweep = 0,
    this.fill = false,
    this.style = 'solid',
    this.text,
  });

  factory FigureItem.fromJson(Map<String, dynamic> json) =>
      _$FigureItemFromJson(json);

  final String kind;
  final List<List<double>> points;
  final List<double>? from;
  final List<double>? to;
  final List<double>? center;
  final List<double>? at;
  final double radius;

  /// Degrees from the +x direction, turning clockwise on screen.
  final double start;
  final double sweep;
  final bool fill;

  /// solid or dashed (a mirror line or construction line).
  final String style;

  /// A label's text: a letter, a number or an angle, the same in every
  /// language.
  final String? text;

  bool get dashed => style == 'dashed';

  List<Offset> get offsets => [for (final p in points) _offset(p)!];
  Offset? get fromOffset => _offset(from);
  Offset? get toOffset => _offset(to);
  Offset? get centerOffset => _offset(center);
  Offset? get atOffset => _offset(at);

  static Offset? _offset(List<double>? p) =>
      p == null ? null : Offset(p[0], p[1]);
}

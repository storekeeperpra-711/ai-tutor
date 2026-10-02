import 'package:flutter/material.dart';

/// A child's profile picture: a big, colourful icon children can recognise
/// without reading.
class StudentAvatar extends StatelessWidget {
  const StudentAvatar({super.key, required this.avatar, this.size = 64});

  final String avatar;
  final double size;

  static const pictures = <String, (IconData, Color)>{
    'cat': (Icons.pets, Color(0xFFEF6C00)),
    'star': (Icons.star, Color(0xFFF9A825)),
    'flower': (Icons.local_florist, Color(0xFFD81B60)),
    'sun': (Icons.wb_sunny, Color(0xFFFF8F00)),
    'moon': (Icons.nightlight_round, Color(0xFF3949AB)),
    'tree': (Icons.park, Color(0xFF2E7D32)),
    'car': (Icons.directions_car, Color(0xFFC62828)),
    'bird': (Icons.flutter_dash, Color(0xFF00897B)),
    'cricket': (Icons.sports_cricket, Color(0xFF6D4C41)),
    'cake': (Icons.cake, Color(0xFF8E24AA)),
  };

  @override
  Widget build(BuildContext context) {
    final (icon, color) = pictures[avatar] ?? (Icons.face, Colors.blueGrey);
    return CircleAvatar(
      radius: size / 2,
      backgroundColor: color,
      child: Icon(icon, color: Colors.white, size: size * 0.6),
    );
  }
}

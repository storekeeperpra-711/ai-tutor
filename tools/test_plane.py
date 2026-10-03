"""Tests for plane.py. Run: python -m unittest discover -s tools -p 'test_*.py'"""

import unittest
from fractions import Fraction as F

import plane


class HalfPlaneTest(unittest.TestCase):
    def test_same_region_same_numbers(self):
        # The same cases as test/checkers/half_plane_checker_test.dart.
        for a, b in [
            ("y <= 2x + 1", "2x - y >= -1"),
            ("y <= 2x + 1", "-4x + 2y <= 2"),
            ("x + y < 4", "2(x + y) < 8"),
            ("y > (1/2)x - 3", "y > x/2 - 3"),
            ("x >= 2", "2 <= x"),
            ("3x + 2y <= 12", "3x + 2y ≤ 12"),
        ]:
            self.assertEqual(plane.parse_half_plane(a), plane.parse_half_plane(b), (a, b))

    def test_side_and_line(self):
        h = plane.parse_half_plane("x + y <= 4")
        self.assertTrue(h.contains((F(2), F(2))))
        self.assertFalse(h.contains((F(3), F(2))))
        self.assertFalse(plane.parse_half_plane("x + y < 4").contains((F(2), F(2))))

    def test_not_half_planes(self):
        for bad in ["", "y = 2x", "3 < 4", "xy < 4", "y < 2x <= 3", "y < 1/0"]:
            self.assertFalse(plane.is_half_plane(bad), bad)


class CornersTest(unittest.TestCase):
    def test_corners_of_a_region(self):
        self.assertEqual(
            plane.corners(["x + y <= 6", "x <= 4", "x >= 0", "y >= 0"]),
            [(0, 0), (0, 6), (4, 0), (4, 2)],
        )

    def test_a_line_that_does_not_touch_the_region_adds_no_corner(self):
        self.assertEqual(
            plane.corners(["x <= 2", "y <= 2", "x >= 0", "y >= 0", "x + y <= 10"]),
            [(0, 0), (0, 2), (2, 0), (2, 2)],
        )

    def test_fraction_corners(self):
        self.assertIn((F(3, 2), F(3, 2)), plane.corners(["x + y <= 3", "y <= x", "y >= 0"]))

    def test_open_or_empty_regions(self):
        with self.assertRaisesRegex(ValueError, "not closed"):
            plane.corners(["x >= 0", "y >= 0", "x + y >= 2"])
        with self.assertRaisesRegex(ValueError, "no corner"):
            plane.corners(["x + y <= 1", "x + y >= 3", "x >= 0", "y >= 0"])

    def test_objective(self):
        self.assertEqual(plane.value("3x + 2y", (F(4), F(2))), 16)


class PointsTest(unittest.TestCase):
    def test_read_and_write(self):
        points = plane.parse_points("(0, 0), (3/2, -1) and (4,2)")
        self.assertEqual(points, [(0, 0), (F(3, 2), -1), (4, 2)])
        self.assertEqual(plane.describe(points[1]), "(3/2, -1)")
        with self.assertRaises(ValueError):
            plane.parse_points("(0, 0) x")


if __name__ == "__main__":
    unittest.main()

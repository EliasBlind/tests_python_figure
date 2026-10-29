import math
import unittest

from src.circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_unit_radius(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_area_integer(self):
        self.assertAlmostEqual(area(3), 28.274333882308138)

    def test_area_float(self):
        self.assertAlmostEqual(area(0.5), 0.7853981633974483)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_integer(self):
        self.assertAlmostEqual(perimeter(3), 18.84955592153876)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    @unittest.expectedFailure
    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-1)

    @unittest.expectedFailure
    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == "__main__":
    unittest.main()

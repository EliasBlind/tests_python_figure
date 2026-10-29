import unittest

from src.triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_integer(self):
        self.assertEqual(area(4, 3), 6)

    def test_area_float(self):
        self.assertAlmostEqual(area(2, 4.8), 4.8)

    def test_area_zero_height(self):
        self.assertEqual(area(5, 0), 0)

    def test_perimeter_integer(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3), 7.0)

    @unittest.expectedFailure
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-4, 3)

    @unittest.expectedFailure
    def test_perimeter_impossible_triangle(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)


if __name__ == "__main__":
    unittest.main()

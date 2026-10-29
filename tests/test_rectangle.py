import unittest

from src.rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_square_case(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_integer(self):
        self.assertEqual(area(2, 3), 6)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4), 10.0)

    def test_area_commutative(self):
        self.assertEqual(area(4, 7), area(7, 4))

    def test_perimeter_integer(self):
        self.assertEqual(perimeter(2, 3), 10)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5), 8.0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-2, 3)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-2, 3)


if __name__ == "__main__":
    unittest.main()

import unittest

from src.square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_integer(self):
        self.assertEqual(area(3), 9)

    def test_area_float(self):
        self.assertAlmostEqual(area(1.5), 2.25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_integer(self):
        self.assertEqual(perimeter(3), 12)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5), 10.0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    @unittest.expectedFailure
    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-3)

    @unittest.expectedFailure
    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-3)


if __name__ == "__main__":
    unittest.main()

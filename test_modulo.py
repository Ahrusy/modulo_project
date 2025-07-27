# test_modulo.py

import unittest
from modulo import modulo

class TestModuloFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 5), 0)

    def test_negative_dividend(self):
        self.assertEqual(modulo(-10, 3), 2)

    def test_negative_divisor(self):
        self.assertEqual(modulo(10, -3), 1)

    def test_both_negative(self):
        self.assertEqual(modulo(-10, -3), 2)

    def test_zero_dividend(self):
        self.assertEqual(modulo(0, 5), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modulo(5, 0)

if __name__ == '__main__':
    unittest.main()
import unittest
from modulo import modulo

class TestModuloFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 5), 0)

    def test_negative_dividend(self):
        self.assertEqual(modulo(-10, 3), 2)

    def test_negative_divisor(self):
        self.assertEqual(modulo(10, -3), -2)  # исправлено

    def test_both_negative(self):
        self.assertEqual(modulo(-10, -3), -1)  # исправлено

    def test_zero_dividend(self):
        self.assertEqual(modulo(0, 5), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modulo(5, 0)

if __name__ == '__main__':
    unittest.main()

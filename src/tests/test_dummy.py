import unittest
from .. import dummy

class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = dummy.Calculator()
        return super().setUp()
    
    def test_addition_valid(self):
        expected = 2
        self.assertEqual(self.calc.add(2), expected)

    def test_multiplication_valid(self):
        expected = 8
        self.calc.add(2)
        self.assertEqual(self.calc.multiply(4), expected)

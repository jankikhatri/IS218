import unittest

from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction
from MathOperations.Multiplication import Multiplication
from MathOperations.Division import Division

class MyTestCase(unittest.TestCase):

    def test_MO_addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MO_subtract(self):
        self.assertEqual((-1, Subtraction.subtract(1, 2)))

    def test_MO_multiply(self):
        self.assertEqual(2, Multiplication.multiply(1, 2))

    def test_MO_divide(self):
        self.assertEqual(2, Division.divide(2, 1))

    def test_MO_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

if __name__ == '__main__':
    unittest.main()
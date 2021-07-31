import unittest
import TestProperties

from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculator_instantiate(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_addition(self):
        test_data = CsvReader(TestProperties.ADDITION_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_calculator_division(self):
        test_data = CsvReader(TestProperties.DIVISION_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_calculator_multiplication(self):
        test_data = CsvReader(TestProperties.MULTIPLICATION_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_calculator_square(self):
        test_data = CsvReader(TestProperties.SQUARE_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_calculator_square_root(self):
        test_data = CsvReader(TestProperties.SQUARE_ROOT_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_calculator_subtraction(self):
        test_data = CsvReader(TestProperties.SUBTRACTION_FILE_NAME).data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()

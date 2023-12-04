import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_calculation_add(self):
        result = Calculator.calculation(5, 3, '+')
        self.assertEqual(result, 8)

    def test_calculation_subtract(self):
        result = Calculator.calculation(5, 3, '-')
        self.assertEqual(result, 2)

    def test_calculation_multiply(self):
        result = Calculator.calculation(5, 3, '*')
        self.assertEqual(result, 15)

    def test_calculation_divide(self):
        result = Calculator.calculation(10, 2, '/')
        self.assertEqual(result, 5)

    def test_calculation_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator.calculation(5, 0, '/')

    def test_calculation_invalid_operator(self):
        with self.assertRaises(ValueError):
            Calculator.calculation(5, 3, '%')

    def test_square_root_extraction_positive_number(self):
        result = Calculator.square_root_extraction(25)
        self.assertEqual(result, 5)

    def test_square_root_extraction_zero(self):
        with self.assertRaises(ArithmeticError):
            Calculator.square_root_extraction(0)

    def test_square_root_extraction_negative_number(self):
        with self.assertRaises(ArithmeticError):
            Calculator.square_root_extraction(-25)

    def test_calculating_discount_positive_values(self):
        result = Calculator.calculating_discount(100, 20)
        self.assertEqual(result, 80)

    def test_calculating_discount_negative_purchase_amount(self):
        with self.assertRaises(ArithmeticError):
            Calculator.calculating_discount(-100, 20)

    def test_calculating_discount_negative_discount_amount(self):
        with self.assertRaises(ArithmeticError):
            Calculator.calculating_discount(100, -20)

    def test_calculating_discount_discount_more_than_100(self):
        with self.assertRaises(ArithmeticError):
            Calculator.calculating_discount(100, 120)


if __name__ == '__main__':
    unittest.main()

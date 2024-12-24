import unittest
from classes import *
from operations.rational_operations import RationalOperations
from operations.polynomial_operation import PolynomialOperations


class TestPolynomialOperations(unittest.TestCase):

    def setUp(self):
        # Инициализация тестовых многочленов:
        # poly1 = 3x^2 + 2x + 1
        # poly2 = 4x^2 + 3x + 2  
        # poly3 = 5x^3 + 3x^2 + x
        self.poly1 = create_polynomial("3x^2+2x+1")
        self.poly2 = create_polynomial("4x^2+3x+2")
        self.poly3 = create_polynomial("5x^3+3x^2+x")

    def test_add_polynomials(self):
        # Тестирование P-1: Сложение многочленов
        # (3x^2+2x+1) + (5x^3+3x^2+x) = 5x^3+6x^2+3x+1
        result = PolynomialOperations.ADD_PP_P(self.poly1, self.poly3)
        expected = create_polynomial("5x^3+6x^2+3x+1")
        self.assertEqual(result, expected)

    def test_sub_polynomials(self):
        # Тестирование P-2: Вычитание многочленов
        # (3x^2+2x+1) - (4x^2+3x+2) = -x^2-x-1
        result = PolynomialOperations.SUB_PP_P(self.poly1, self.poly2)
        expected = create_polynomial("-x^2-x-1")
        self.assertEqual(result, expected)

    def test_multiply_polynomial_by_rational(self):
        # Тестирование P-3: Умножение многочлена на рациональное число
        # (3x^2+2x+1) * 2 = 6x^2+4x+2
        q = Rational(Integer("2"), Natural("3"))  # 2
        result = PolynomialOperations.MUL_PQ_P(self.poly1, q)
        print(result)
        expected = create_polynomial("2x^2+(4/3)x+(2/3)")
        self.assertEqual(result, expected)

    def test_multiply_polynomial_by_xk(self):
        # Тестирование P-4: Умножение многочлена на x^k
        # (3x^2+2x+1) * x^2 = 3x^4+2x^3+x^2
        k = Natural("2")  # x^2
        result = PolynomialOperations.MUL_Pxk_P(self.poly1, k)
        expected = create_polynomial("3x^4+2x^3+x^2")
        self.assertEqual(result, expected)

    def test_gcf_polynomials(self):
        # Тестирование P-11: Наибольший общий делитель многочленов
        result = PolynomialOperations.GCF_PP_P(self.poly1, self.poly2)
        expected = create_polynomial("x^2+x+1")
        self.assertEqual(result, expected)

    def test_derivative_polynomial(self):
        # Тестирование P-12: Производная многочлена
        # d/dx(3x^2+2x+1) = 6x+2
        result = PolynomialOperations.DER_P_P(self.poly1)
        expected = create_polynomial("6x+2")
        self.assertEqual(result, expected)

    def test_divide_polynomials(self):
        # Тестирование P-9: Деление многочленов
        # (4x^3+2x-11) ÷ (x+5) = 4x^2-20x+102
        dividend = create_polynomial("4x^3+2x-11")
        divisor = create_polynomial("x+5")
        result = PolynomialOperations.DIV_PP_P(dividend, divisor)
        expected = create_polynomial("4x^2 - 20x + 102")
        self.assertEqual(result, expected)
    
    def test_remainder_polynomials(self):
        # Тестирование P-10: Остаток от деления многочленов
        # (4x^3+2x-11) mod (x+5) = -521
        dividend = create_polynomial("4x^3+2x-11")
        divisor = create_polynomial("x+5")
        result = PolynomialOperations.MOD_PP_P(dividend, divisor)
        expected = create_polynomial("-521")
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
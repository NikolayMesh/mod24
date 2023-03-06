import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator()

    def test_adding_success(self):
        assert self.calculator.adding(1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calculator.adding(1, 1) == 3

    def test_squareroot_success(self):
        assert self.calculator.squareroot(25) == 5

    def test_multiply_success(self):
        assert self.calculator.multiply(2, 2) == 4

    def test_subtraction_success(self):
        assert self.calculator.subtraction(2, 2) == 0

    def test_degree_success(self):
        assert self.calculator.degree(2, 3) == 8

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(1, 0)

    def teardown(self):
        print('Выполнение метода Terndown')
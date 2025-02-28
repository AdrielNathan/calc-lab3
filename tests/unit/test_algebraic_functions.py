import sys
import os
import pytest

# Ajouter le dossier parent au chemin Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.utils import add, subtract, multiply, divide, exponent

class TestCalculator:
    def test_addition(self):
        assert add(2, 2) == 4

    def test_subtraction(self):
        assert subtract(4, 2) == 2

    def test_multiplication(self):
        assert multiply(3, 3) == 9

    def test_division(self):
        assert divide(10, 2) == 5

    def test_division_by_zero(self):
        with pytest.raises(ValueError):
            divide(5, 0)

    def test_exponent(self):  
        assert exponent(2, 3) == 8
        assert exponent(5, 0) == 1
        assert exponent(10, 2) == 100

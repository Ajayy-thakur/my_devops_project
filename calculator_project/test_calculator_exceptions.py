# test_calculator_exceptions.py
import pytest
from calculator import Calculator

def test_div_zero():
    calc = Calculator()
    # ye test check karega ki divide by zero exception raise hota hai ya nahi
    with pytest.raises(ValueError):
        calc.div(10, 0)

def test_div_normal():
    calc = Calculator()
    result = calc.div(10, 2)
    assert result == 5, f"Expected 5 but got {result}"


from calculator import Calculator

def test_add_debug():
    calc = Calculator()
    result = calc.add(2, 3)
    print("Debug: add(2,3) =", result)
    assert result == 5, f"Expected 5 but got {result}"

def test_subtract_debug():
    calc = Calculator()
    result = calc.subtract(5, 3)
    print("Debug: subtract(5,3) =", result)
    assert result == 2, f"Expected 2 but got {result}"


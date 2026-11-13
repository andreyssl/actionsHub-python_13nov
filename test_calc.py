from calc import calculate


def test_addition():
    assert calculate(10, "+", 3) == 13

def test_subtraction():
    assert calculate(10, "-", 3) == 7

def test_multiplication():
    assert calculate(10, "*", 3) == 30

def test_division():
    assert calculate(10, "/", 2) == 5

def test_invalid_operator():
    assert calculate(10, "%", 3) is None

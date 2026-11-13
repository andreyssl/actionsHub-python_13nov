from calc import calculate


def test_addition():
    assert calculate(10, "+", 3) == 13 #is going to pass

def test_subtraction():
    assert calculate(10, "-", 3) == 7 #will fail

def test_multiplication():
    assert calculate(10, "*", 3) == 30#will fail

def test_division():
    assert calculate(10, "/", 2) == 5#will fail

def test_modulo():
    assert calculate(10, "%", 3) == 1 

def test_invalid_operator():
    assert calculate(10, "//", 3) is None #will fail




# first test passed and invalid operator is passed as well, others failed

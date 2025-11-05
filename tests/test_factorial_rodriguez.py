from funciones.factorial import factorial

def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_factorial_negative():
    assert factorial(-3) is None

def test_factorial_non_int():
    # comprobamos comportamiento si no es entero
    assert factorial(3.5) is None

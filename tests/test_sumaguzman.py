from funciones.sumaguzman import sumar

def test_suma():
    assert suma(4,5) is True    # 4 es par, debería devolver True
    assert suma(7,5) is False   # 7 es impar, debería devolver False

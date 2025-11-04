from funciones.NumparMeza import es_par

def test_es_par():
    assert es_par(4) is True    # 4 es par, debería devolver True
    assert es_par(7) is False   # 7 es impar, debería devolver False

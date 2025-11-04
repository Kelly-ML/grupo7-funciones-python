 #tests/test_es_par.py
from funciones.NumparMeza import es_par

def test_es_par():
  assert es_par(4) is True
  assert es_par(7) is False

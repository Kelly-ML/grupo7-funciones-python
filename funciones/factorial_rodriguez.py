import math

def factorial(n):
    """Devuelve el factorial de un número entero no negativo."""
    if not isinstance(n, int) or n < 0:
        return None
    return math.factorial(n)
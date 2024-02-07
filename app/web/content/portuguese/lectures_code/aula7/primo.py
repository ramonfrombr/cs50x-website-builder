import math

def eh_primo(n):
    """Determina se um número inteiro não negativo é primo."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
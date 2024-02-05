# Adiciona docstring à função.


def miau(n):
    """Miau n vezes."""
    return "miau\n" * n


numero = int(input("Número: "))
miaus = miau(numero)
print(miaus, end="")
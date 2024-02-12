# Añade docstring a la función.


def maullar(n):
    """Maulla n veces."""
    return "miau\n" * n


numero = int(input("Número: "))
maullidos = maullar(numero)
print(maullidos, end="")
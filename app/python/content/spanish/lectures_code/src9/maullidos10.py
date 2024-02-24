# Utiliza formato de docstring de Sphinx


def maullar(n):
    """
    Maulla n veces.

    :param n: Número de veces para maullar
    :type n: int
    :raise TypeError: Si n no es un int
    :return: Un string de n maullidos, uno por línea
    :rtype: str
    """
    return "miau\n" * n


numero = int(input("Número: "))
maullidos = maullar(numero)
print(maullidos, end="")
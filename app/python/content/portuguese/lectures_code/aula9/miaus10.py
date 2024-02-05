# Usa o formato de docstring do Sphinx


def miau(n):
    """
    Miau n vezes.

    :param n: Número de vezes para miau
    :type n: int
    :raise TypeError: Se n não for um int
    :return: Uma string de n mias, um por linha
    :rtype: str
    """
    return "miau\n" * n


numero = int(input("Número: "))
miaus = miau(numero)
print(miaus, end="")
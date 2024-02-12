from calculator2 import cuadrado


def principal():
    probar_cuadrado()


def probar_cuadrado():
    assert cuadrado(2) == 4
    assert cuadrado(3) == 9


if __name__ == "__main__":
    principal()
from calculator5 import cuadrado


def probar_cuadrado():
    assert cuadrado(2) == 4
    assert cuadrado(3) == 9
    assert cuadrado(-2) == 4
    assert cuadrado(-3) == 9
    assert cuadrado(0) == 0
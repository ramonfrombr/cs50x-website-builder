from calculadora6 import cuadrado


def probar_positiva():
    assert cuadrado(1) == 1
    assert cuadrado(2) == 4
    assert cuadrado(3) == 9


def probar_negativa():
    assert cuadrado(-1) == 1
    assert cuadrado(-2) == 4
    assert cuadrado(-3) == 9


def probar_cero():
    assert cuadrado(0) == 0
import pytest

from calculadora import cuadrado


def test_positivo():
    assert cuadrado(2) == 4
    assert cuadrado(3) == 9


def test_negativo():
    assert cuadrado(-2) == 4
    assert cuadrado(-3) == 9


def test_cero():
    assert cuadrado(0) == 0


def test_str():
    with pytest.raises(TypeError):
        cuadrado("gato")
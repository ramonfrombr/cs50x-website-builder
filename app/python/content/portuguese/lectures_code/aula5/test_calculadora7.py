import pytest

from calculadora import quadrado


def test_positivo():
    assert quadrado(2) == 4
    assert quadrado(3) == 9


def test_negativo():
    assert quadrado(-2) == 4
    assert quadrado(-3) == 9


def test_zero():
    assert quadrado(0) == 0


def test_str():
    with pytest.raises(TypeError):
        quadrado("gato")
from ola1 import ola


def test_padrao():
    assert ola() == "olá, mundo"


def test_argumento():
    assert ola("David") == "olá, David"
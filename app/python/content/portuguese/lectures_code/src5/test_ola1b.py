from ola1 import ola


def test_padrao():
    assert ola() == "olá, mundo"


def test_argumento():
    for nome in ["Hermione", "Harry", "Ron"]:
        assert ola(nome) == f"olá, {nome}"
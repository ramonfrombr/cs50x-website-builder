from calculadora import quadrado


def test_positivo():
    assert quadrado(1) == 1
    assert quadrado(2) == 4
    assert quadrado(3) == 9


def test_negativo():
    assert quadrado(-1) == 1
    assert quadrado(-2) == 4
    assert quadrado(-3) == 9


def test_zero():
    assert quadrado(0) == 0
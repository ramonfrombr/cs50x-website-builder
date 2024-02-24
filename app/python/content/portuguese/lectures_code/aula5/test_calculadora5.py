from calculadora import quadrado


def test_quadrado():
    assert quadrado(2) == 4
    assert quadrado(3) == 9
    assert quadrado(-2) == 4
    assert quadrado(-3) == 9
    assert quadrado(0) == 0
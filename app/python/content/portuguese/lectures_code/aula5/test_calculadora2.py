from calculadora import quadrado


def principal():
    test_quadrado()


def test_quadrado():
    assert quadrado(2) == 4
    assert quadrado(3) == 9


se __name__ == "__main__":
    principal()
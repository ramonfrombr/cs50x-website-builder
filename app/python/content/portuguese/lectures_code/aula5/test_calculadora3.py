from calculadora import quadrado


def principal():
    test_quadrado()


def test_quadrado():
    try:
        assert quadrado(2) == 4
    except AssertionError:
        print("O quadrado de 2 não era 4")
    try:
        assert quadrado(3) == 9
    except AssertionError:
        print("O quadrado de 3 não era 9")


if __name__ == "__main__":
    principal()
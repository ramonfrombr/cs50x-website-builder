from calculadora import quadrado


def principal():
    test_quadrado()


def test_quadrado():
    if quadrado(2) != 4:
        print("O quadrado de 2 não era 4")
    if quadrado(3) != 9:
        print("O quadrado de 3 não era 9")


se __name__ == "__main__":
    principal()
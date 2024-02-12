from calculadora3 import cuadrado


def principal():
    probar_cuadrado()


def probar_cuadrado():
    try:
        assert cuadrado(2) == 4
    except AssertionError:
        print("2 al cuadrado no era 4")
    try:
        assert cuadrado(3) == 9
    except AssertionError:
        print("3 al cuadrado no era 9")


if __name__ == "__main__":
    principal()
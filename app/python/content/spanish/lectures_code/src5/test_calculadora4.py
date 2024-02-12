from calculadora4 import cuadrado


def principal():
    probar_cuadrado()


def probar_cuadrado():
    try:
        assert cuadrado(2) == 4
    except AssertionError:
        print("2 al cuadrado no fue 4")
    try:
        assert cuadrado(3) == 9
    except AssertionError:
        print("3 al cuadrado no fue 9")
    try:
        assert cuadrado(-2) == 4
    except AssertionError:
        print("-2 al cuadrado no fue 4")
    try:
        assert cuadrado(-3) == 9
    except AssertionError:
        print("-3 al cuadrado no fue 9")
    try:
        assert cuadrado(0) == 0
    except AssertionError:
        print("0 al cuadrado no fue 0")


if __name__ == "__main__":
    principal()
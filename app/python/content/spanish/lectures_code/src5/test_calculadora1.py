from calculadora1 import cuadrado


def principal():
    probar_cuadrado()


def probar_cuadrado():
    if cuadrado(2) != 4:
        print("El cuadrado de 2 no fue 4")
    if cuadrado(3) != 9:
        print("El cuadrado de 3 no fue 9")


if __name__ == "__main__":
    principal()
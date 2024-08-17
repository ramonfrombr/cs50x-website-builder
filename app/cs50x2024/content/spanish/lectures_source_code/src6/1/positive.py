# Abstracción y alcance

from cs50 import get_int


def main():
    i = get_positive_int()
    print(i)


# Solicita al usuario un número entero positivo
def get_positive_int():
    while True:
        n = get_int("Número entero positivo: ")
        if n > 0:
            break
    return n


main()
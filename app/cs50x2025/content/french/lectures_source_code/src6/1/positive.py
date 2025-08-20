# Abstraction et portée

from cs50 import get_int


def main():
    i = get_positive_int()
    print(i)


# Demander à l'utilisateur un entier positif
def get_positive_int():
    while True:
        n = get_int("Entier positif : ")
        if n > 0:
            break
    return n


main()
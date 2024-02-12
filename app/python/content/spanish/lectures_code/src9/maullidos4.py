# Tipos incompatibles en la asignación


def maullar(n: int):
    for _ in range(n):
        print("miau")


numero: int = input("Número: ")
maullar(numero)
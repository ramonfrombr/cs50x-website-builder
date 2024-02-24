# Tipos incompatíveis na atribuição


def miau(n: int):
    for _ in range(n):
        print("miau")


numero: int = input("Número: ")
miau(numero)
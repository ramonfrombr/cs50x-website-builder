# Demonstração de TypeError


def miau(n):
    for _ in range(n):
        print("miau")


numero = input("Número: ")
miau(numero)
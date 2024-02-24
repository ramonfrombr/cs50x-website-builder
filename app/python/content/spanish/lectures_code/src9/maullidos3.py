# Argumento ... tiene un tipo incompatible


def maullar(n: int):
    for _ in range(n):
        print("miau")


numero = input("Número: ")
maullar(numero)
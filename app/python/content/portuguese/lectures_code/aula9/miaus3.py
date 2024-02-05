# Argumento ... tem tipo incompatível


def miau(n: int):
    for _ in range(n):
        print("miau")


numero = input("Número: ")
miau(numero)
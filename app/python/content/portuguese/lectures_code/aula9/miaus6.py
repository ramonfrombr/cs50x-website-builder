# Imprime None porque miau é confundido como tendo um valor de retorno


def miau(n: int):
    for _ in range(n):
        print("miau")


numero: int = int(input("Número: "))
miaus: str = miau(numero)
print(miaus)
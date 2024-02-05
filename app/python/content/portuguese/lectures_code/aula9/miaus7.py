# Anota o valor de retorno, ... não retorna um valor


def miau(n: int) -> None:
    for _ in range(n):
        print("miau")


numero: int = int(input("Número: "))
miaus: str = miau(numero)
print(miaus)
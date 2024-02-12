# Anota el valor de retorno, ... no devuelve un valor


def maullar(n: int) -> None:
    for _ in range(n):
        print("miau")


numero: int = int(input("Número: "))
maullidos: str = maullar(numero)
print(maullidos)
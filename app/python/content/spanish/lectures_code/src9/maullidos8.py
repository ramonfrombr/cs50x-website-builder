# Éxito


def maullar(n: int) -> str:
    return "miau\n" * n


numero: int = int(input("Número: "))
maullidos: str = maullar(numero)
print(maullidos, end="")
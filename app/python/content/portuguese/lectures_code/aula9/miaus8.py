# Sucesso

def miau(n: int) -> str:
    return "miau\n" * n

numero: int = int(input("Número: "))
miaus: str = miau(numero)
print(miaus, end="")
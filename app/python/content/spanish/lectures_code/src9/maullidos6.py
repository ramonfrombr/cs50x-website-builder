# Imprime None porque meow se equivoca al tener un valor de retorno

def maullar(n: int):
    for _ in range(n):
        print("miau")

numero: int = int(input("Número: "))
maullidos: str = maullar(numero)
print(maullidos)
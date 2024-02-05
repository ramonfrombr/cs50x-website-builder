# Demonstração de expressões condicionais (operadores ternários)


def principal():
    x = int(input("Qual é o valor de x? "))
    if par(x):
        print("Par")
    else:
        print("Ímpar")


def par(n):
    return True if n % 2 == 0 else False


principal()
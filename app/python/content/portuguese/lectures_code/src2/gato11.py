# Demonstração de definição de funções


def principal():
    miau(receber_numero())


def receber_numero():
    while True:
        n = int(input("Qual é o número? "))
        if n > 1:
            return n


def miau(n):
    for _ in range(n):
        print("miau")


principal()
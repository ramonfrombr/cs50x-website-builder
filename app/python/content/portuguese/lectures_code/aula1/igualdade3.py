# Demonstra o retorno do valor de uma expressão booleana

def principal():
    x = int(input("Qual é o valor de x? "))
    if par(x):
        print("Par")
    else:
        print("Ímpar")

def par(n):
    return n % 2 == 0

principal()
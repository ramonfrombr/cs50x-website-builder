# Demonstra uma função que retorna um booleano

def principal():
    x = int(input("Qual é o valor de x? "))
    if par(x):
        print("Par")
    else:
        print("Ímpar")

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

principal()
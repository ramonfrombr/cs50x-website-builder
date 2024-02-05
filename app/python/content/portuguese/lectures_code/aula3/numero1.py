# Captura um ValueError

try:
    x = int(input("Qual é o valor de x? "))
    print(f"x é {x}")
except ValueError:
    print("x não é um número inteiro")
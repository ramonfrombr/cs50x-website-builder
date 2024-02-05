# Demonstração de um NameError

try:
    x = int(input("Qual é o valor de x? "))
except ValueError:
    print("x não é um número inteiro")

print(f"x é {x}")
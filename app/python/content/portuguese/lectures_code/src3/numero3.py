# Demonstração de else

try:
    x = int(input("Qual é o valor de x? "))
except ValueError:
    print("x não é um número inteiro")
else:
    print(f"x é {x}")
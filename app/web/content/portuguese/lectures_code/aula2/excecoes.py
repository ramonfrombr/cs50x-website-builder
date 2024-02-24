import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Erro: Entrada inválida")
    sys.exit(1)

try:
    resultado = x / y
except ZeroDivisionError:
    print("Erro: Não é possível dividir por 0")
    sys.exit(1)

print(f"x / y = {resultado}")
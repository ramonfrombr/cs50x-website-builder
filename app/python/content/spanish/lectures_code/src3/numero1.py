# Captura un ValueError

try:
    x = int(input("¿Cuál es el valor de x? "))
    print(f"x es {x}")
except ValueError:
    print("x no es un número entero")
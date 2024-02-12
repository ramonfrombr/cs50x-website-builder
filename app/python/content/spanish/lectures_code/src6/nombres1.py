# Almacena nombres en una lista

nombres = []

for _ in range(3):
    nombres.append(input("¿Cuál es tu nombre? "))

for nombre in sorted(nombres):
    print(f"hola, {nombre}")
# Agrega nombres a una lista para ordenar

nombres = []

with open("nombres.txt") as archivo:
    for linea in archivo:
        nombres.append(linea.rstrip())

for nombre in sorted(nombres):
    print(f"hola, {nombre}")
# Lee de un archivo, una línea a la vez

with open("nombres.txt") as archivo:
    for linea in archivo:
        print("¡Hola,", linea.rstrip(), "!")
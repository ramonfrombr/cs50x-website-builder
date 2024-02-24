# Lee de un archivo

with open("nombres.txt") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    print("hola,", linea.rstrip())
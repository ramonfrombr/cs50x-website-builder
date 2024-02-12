# Escribe en un archivo

nombre = input("¿Cuál es tu nombre? ")

archivo = open("nombres.txt", "w")
archivo.write(nombre)
archivo.close()
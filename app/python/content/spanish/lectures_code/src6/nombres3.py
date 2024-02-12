# Añade al final de un archivo

nombre = input("¿Cuál es tu nombre? ")

archivo = open("nombres.txt", "a")
archivo.write(f"{nombre}\n")
archivo.close()
# Agrega un administrador de contexto

nombre = input("¿Cuál es tu nombre? ")

with open("nombres.txt", "a") as archivo:
    archivo.write(f"{nombre}\n")
# Desempaqueta una lista

with open("students0.csv") as archivo:
    for linea in archivo:
        nombre, casa = linea.rstrip().split(",")
        print(f"{nombre} está en {casa}")
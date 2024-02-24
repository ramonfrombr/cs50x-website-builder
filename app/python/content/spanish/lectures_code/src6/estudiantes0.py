# Lee un archivo CSV

with open("students0.csv") as archivo:
    for linea in archivo:
        fila = linea.rstrip().split(",")
        print(f"{fila[0]} está en {fila[1]}")
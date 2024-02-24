# Lee un archivo CSV usando csv.reader

import csv

estudiantes = []

with open("estudiantes1.csv") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        estudiantes.append({"nombre": fila[0], "hogar": fila[1]})

for estudiante in sorted(estudiantes, key=lambda estudiante: estudiante["nombre"]):
    print(f"{estudiante['nombre']} es de {estudiante['hogar']}")
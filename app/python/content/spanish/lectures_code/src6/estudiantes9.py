# Lee un archivo CSV usando csv.DictReader

import csv

estudiantes = []

with open("students2.csv") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        estudiantes.append({"nombre": fila["nombre"], "hogar": fila["hogar"]})

for estudiante in sorted(estudiantes, key=lambda estudiante: estudiante["nombre"]):
    print(f"{estudiante['nombre']} es de {estudiante['hogar']}")
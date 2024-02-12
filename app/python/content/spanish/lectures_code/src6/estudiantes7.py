# Ordena una lista de diccionarios utilizando una función lambda

estudiantes = []

with open("students0.csv") as archivo:
    for linea in archivo:
        nombre, casa = linea.rstrip().split(",")
        estudiantes.append({"nombre": nombre, "casa": casa})

for estudiante in sorted(estudiantes, key=lambda estudiante: estudiante["nombre"]):
    print(f"{estudiante['nombre']} está en {estudiante['casa']}")
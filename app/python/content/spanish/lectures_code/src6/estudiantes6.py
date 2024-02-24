# Ordena una lista de diccionarios utilizando una función

estudiantes = []

with open("students0.csv") as archivo:
    for linea in archivo:
        nombre, casa = linea.rstrip().split(",")
        estudiantes.append({"nombre": nombre, "casa": casa})


def obtener_nombre(estudiante):
    return estudiante["nombre"]


for estudiante in sorted(estudiantes, key=obtener_nombre):
    print(f"{estudiante['nombre']} está en {estudiante['casa']}")
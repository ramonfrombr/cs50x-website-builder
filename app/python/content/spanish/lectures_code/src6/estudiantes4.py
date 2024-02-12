# Lee un archivo CSV en una lista de objetos dict, creando el dict primero

estudiantes = []

with open("students0.csv") as archivo:
    for linea in archivo:
        nombre, casa = linea.rstrip().split(",")
        estudiante = {"nombre": nombre, "casa": casa}
        estudiantes.append(estudiante)

for estudiante in estudiantes:
    print(f"{estudiante['nombre']} está en {estudiante['casa']}")
# Lee un archivo CSV en una lista de objetos de diccionario, creando primero un diccionario vacío

estudiantes = []

with open("estudiantes0.csv") as archivo:
    for linea in archivo:
        nombre, casa = linea.rstrip().split(",")
        estudiante = {}
        estudiante["nombre"] = nombre
        estudiante["casa"] = casa
        estudiantes.append(estudiante)

for estudiante in estudiantes:
    print(f"{estudiante['nombre']} está en {estudiante['casa']}")
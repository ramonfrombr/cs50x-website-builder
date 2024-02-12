# Lee un archivo CSV y crea una lista de objetos tipo diccionario

estudiantes = []

with open("estudiantes0.csv") as archivo:
    for linea in archivo:
        nombre, casa = linea.rstrip().split(",")
        estudiantes.append({"nombre": nombre, "casa": casa})

for estudiante in estudiantes:
    print(f"{estudiante['nombre']} está en {estudiante['casa']}")
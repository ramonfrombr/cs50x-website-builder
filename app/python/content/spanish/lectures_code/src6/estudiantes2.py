# Ordena una lista de cadenas de texto

estudiantes = []

with open("estudiantes0.csv") as archivo:
    for linea in archivo:
        nombre, casa = linea.rstrip().split(",")
        estudiantes.append(f"{nombre} está en {casa}")

for estudiante in sorted(estudiantes):
    print(estudiante)
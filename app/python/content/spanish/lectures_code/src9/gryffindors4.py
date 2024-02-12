# Crea una lista de diccionarios usando un bucle

estudiantes = ["Hermione", "Harry", "Ron"]

gryffindors = []

for estudiante in estudiantes:
    gryffindors.append({"nombre": estudiante, "casa": "Gryffindor"})

print(gryffindors)
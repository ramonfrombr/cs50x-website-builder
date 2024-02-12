# Utiliza comprensión de diccionarios en vez

estudiantes = ["Hermione", "Harry", "Ron"]

gryffindor = [{"nombre": estudiante, "casa": "Gryffindor"} for estudiante in estudiantes]

print(gryffindor)
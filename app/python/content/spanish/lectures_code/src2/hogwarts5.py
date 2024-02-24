# Demuestra la iteración sobre una lista de objetos de diccionarios

estudiantes = [
    {"nombre": "Hermione", "casa": "Gryffindor", "patronus": "Nutria"},
    {"nombre": "Harry", "casa": "Gryffindor", "patronus": "Venado"},
    {"nombre": "Ron", "casa": "Gryffindor", "patronus": "Terrier Jack Russell"},
    {"nombre": "Draco", "casa": "Slytherin", "patronus": None},
]

for estudiante in estudiantes:
    print(estudiante["nombre"], estudiante["casa"], estudiante["patronus"], sep=", ")
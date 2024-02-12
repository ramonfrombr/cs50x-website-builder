# Utiliza el filtro y la clave con lambda

estudiantes = [
    {"nombre": "Hermione", "casa": "Gryffindor"},
    {"nombre": "Harry", "casa": "Gryffindor"},
    {"nombre": "Ron", "casa": "Gryffindor"},
    {"nombre": "Draco", "casa": "Slytherin"},
]


def es_gryffindor(estudiante):
    return estudiante["casa"] == "Gryffindor"


gryffindors = filter(es_gryffindor, estudiantes)

for gryffindor in sorted(gryffindors, key=lambda estudiante: estudiante["nombre"]):
    print(gryffindor["nombre"])
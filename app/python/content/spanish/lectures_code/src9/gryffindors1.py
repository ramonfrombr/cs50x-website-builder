# Filtra por casa usando list comprehension

estudiantes = [
    {"nombre": "Hermione", "casa": "Gryffindor"},
    {"nombre": "Harry", "casa": "Gryffindor"},
    {"nombre": "Ron", "casa": "Gryffindor"},
    {"nombre": "Draco", "casa": "Slytherin"},
]

gryffindors = [
    estudiante["nombre"] for estudiante in estudiantes if estudiante["casa"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
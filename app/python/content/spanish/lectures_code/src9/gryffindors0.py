# Filtra por casa usando bucle

estudiantes = [
    {"nombre": "Hermione", "casa": "Gryffindor"},
    {"nombre": "Harry", "casa": "Gryffindor"},
    {"nombre": "Ron", "casa": "Gryffindor"},
    {"nombre": "Draco", "casa": "Slytherin"},
]

gryffindors = []
for estudiante in estudiantes:
    if estudiante["casa"] == "Gryffindor":
        gryffindors.append(estudiante["nombre"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)
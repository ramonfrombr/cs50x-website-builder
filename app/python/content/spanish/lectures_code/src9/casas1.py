# Filtra las casas duplicadas utilizando un conjunto

estudiantes = [
    {"nombre": "Hermione", "casa": "Gryffindor"},
    {"nombre": "Harry", "casa": "Gryffindor"},
    {"nombre": "Ron", "casa": "Gryffindor"},
    {"nombre": "Draco", "casa": "Slytherin"},
    {"nombre": "Padma", "casa": "Ravenclaw"},
]

casas = set()
for estudiante in estudiantes:
    casas.add(estudiante["casa"])

for casa in sorted(casas):
    print(casa)
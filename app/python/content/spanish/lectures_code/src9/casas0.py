# Filtra las casas duplicadas utilizando un bucle

estudiantes = [
    {"nombre": "Hermione", "casa": "Gryffindor"},
    {"nombre": "Harry", "casa": "Gryffindor"},
    {"nombre": "Ron", "casa": "Gryffindor"},
    {"nombre": "Draco", "casa": "Slytherin"},
    {"nombre": "Padma", "casa": "Ravenclaw"},
]

casas = []
for estudiante in estudiantes:
    if estudiante["casa"] not in casas:
        casas.append(estudiante["casa"])

for casa in sorted(casas):
    print(casa)
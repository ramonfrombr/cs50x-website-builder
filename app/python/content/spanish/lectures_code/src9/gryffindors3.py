# Usa filter con lambda

estudiantes = [
    {"nombre": "Hermione", "casa": "Gryffindor"},
    {"nombre": "Harry", "casa": "Gryffindor"},
    {"nombre": "Ron", "casa": "Gryffindor"},
    {"nombre": "Draco", "casa": "Slytherin"},
]

gryffindor = filter(lambda estudiante: estudiante["casa"] == "Gryffindor", estudiantes)

for gryffindor in sorted(gryffindor, key=lambda estudiante: estudiante["nombre"]):
    print(gryffindor["nombre"])
# Demuestra cómo iterar sobre e indexar un diccionario.

estudiantes = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for estudiante in estudiantes:
    print(estudiante, estudiantes[estudiante], sep=", ")
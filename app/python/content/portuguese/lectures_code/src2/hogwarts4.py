# Demonstração de iteração e indexação em um dicionário

estudantes = {
    "Hermione": "Grifinória",
    "Harry": "Grifinória",
    "Ron": "Grifinória",
    "Draco": "Sonserina",
}

for estudante in estudantes:
    print(estudante, estudantes[estudante], sep=", ")
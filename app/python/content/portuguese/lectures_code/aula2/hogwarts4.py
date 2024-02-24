# Demonstração de iteração e indexação em um dicionário

alunos = {
    "Hermione": "Grifinória",
    "Harry": "Grifinória",
    "Ron": "Grifinória",
    "Draco": "Sonserina",
}

for aluno in alunos:
    print(aluno, alunos[aluno], sep=", ")
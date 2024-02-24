# Demonstrates iterating over a list of dict objects

alunos = [
    {"nome": "Hermione", "casa": "Grifinória", "patrono": "Lontra"},
    {"nome": "Harry", "casa": "Grifinória", "patrono": "Cervo"},
    {"nome": "Ron", "casa": "Grifinória", "patrono": "Jack Russel Terrier"},
    {"nome": "Draco", "casa": "Sonseria", "patrono": None},
]

for aluno in alunos:
    print(aluno["nome"], aluno["casa"], aluno["patrono"], sep=", ")
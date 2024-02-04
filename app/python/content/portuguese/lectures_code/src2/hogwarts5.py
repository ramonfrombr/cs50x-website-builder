# Demonstrates iterating over a list of dict objects

estudantes = [
    {"nome": "Hermione", "casa": "Grifinória", "patrono": "Lontra"},
    {"nome": "Harry", "casa": "Grifinória", "patrono": "Veado"},
    {"nome": "Ron", "casa": "Grifinória", "patrono": "Terrier"},
    {"nome": "Draco", "casa": "Sonseria", "patrono": None},
]

for aluno in estudantes:
    print(aluno["nome"], aluno["casa"], aluno["patrono"], sep=", ")
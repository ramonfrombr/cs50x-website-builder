# Usa filtro com lambda

alunos = [
    {"nome": "Hermione", "casa": "Grifinória"},
    {"nome": "Harry", "casa": "Grifinória"},
    {"nome": "Ron", "casa": "Grifinória"},
    {"nome": "Draco", "casa": "Sonserina"},
]

grifinorias = filter(lambda a: a["casa"] == "Grifinória", alunos)

for grifinoria in sorted(grifinorias, key=lambda a: a["nome"]):
    print(grifinoria["nome"])
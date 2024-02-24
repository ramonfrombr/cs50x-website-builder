# Filtra casas duplicadas usando um conjunto

alunos = [
    {"nome": "Hermione", "casa": "Grifinória"},
    {"nome": "Harry", "casa": "Grifinória"},
    {"nome": "Ron", "casa": "Grifinória"},
    {"nome": "Draco", "casa": "Sonserina"},
    {"nome": "Padma", "casa": "Corvinal"},
]

casas = set()
for aluno in alunos:
    casas.add(aluno["casa"])

for casa in sorted(casas):
    print(casa)
# Filtra casas duplicadas usando loop

alunos = [
    {"nome": "Hermione", "casa": "Grifinória"},
    {"nome": "Harry", "casa": "Grifinória"},
    {"nome": "Ron", "casa": "Grifinória"},
    {"nome": "Draco", "casa": "Sonserina"},
    {"nome": "Padma", "casa": "Corvinal"},
]

casas = []
for aluno in alunos:
    if aluno["casa"] not in casas:
        casas.append(aluno["casa"])

for casa in sorted(casas):
    print(casa)
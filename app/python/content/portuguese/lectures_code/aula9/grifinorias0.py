# Filtra por casa usando loop

alunos = [
    {"nome": "Hermione", "casa": "Grifinória"},
    {"nome": "Harry", "casa": "Grifinória"},
    {"nome": "Ron", "casa": "Grifinória"},
    {"nome": "Draco", "casa": "Sonserina"},
]

grifinorias = []
for aluno in alunos:
    if aluno["casa"] == "Grifinória":
        grifinorias.append(aluno["nome"])

for grifinoria in sorted(grifinorias):
    print(grifinoria)
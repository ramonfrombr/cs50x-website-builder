# Filtra por casa usando list comprehension

alunos = [
    {"nome": "Hermione", "casa": "Grifinória"},
    {"nome": "Harry", "casa": "Grifinória"},
    {"nome": "Ron", "casa": "Grifinória"},
    {"nome": "Draco", "casa": "Sonserina"},
]

grifinorias = [
    aluno["nome"] for aluno in alunos if aluno["casa"] == "Grifinória"
]

for grifinoria in sorted(grifinorias):
    print(grifinoria)
# Usa o filtro e a chave com lambda

alunos = [
    {"nome": "Hermione", "casa": "Grifinória"},
    {"nome": "Harry", "casa": "Grifinória"},
    {"nome": "Ron", "casa": "Grifinória"},
    {"nome": "Draco", "casa": "Sonserina"},
]


def e_grifinoria(a):
    return a["casa"] == "Grifinória"


grifinorias = filter(e_grifinoria, alunos)

for grifinoria in sorted(grifinorias, key=lambda a: a["nome"]):
    print(grifinoria["nome"])
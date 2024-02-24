# Ordena uma lista de dicionários usando uma função

alunos = []

with open("estudantes0.csv") as arquivo:
    for linha in arquivo:
        nome, casa = linha.rstrip().split(",")
        alunos.append({"nome": nome, "casa": casa})


def selecionar_nome(aluno):
    return aluno["nome"]


for aluno in sorted(alunos, key=selecionar_nome):
    print(f"{aluno['nome']} é de {aluno['casa']}")
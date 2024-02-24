# Ordena uma lista de dicionários usando uma função lambda

alunos = []

with open("estudantes0.csv") as arquivo:
    for linha in arquivo:
        nome, casa = linha.rstrip().split(",")
        alunos.append({"nome": nome, "casa": casa})

for aluno in sorted(alunos, key=lambda aluno: aluno["nome"]):
    print(f"{aluno['nome']} é de {aluno['casa']}")
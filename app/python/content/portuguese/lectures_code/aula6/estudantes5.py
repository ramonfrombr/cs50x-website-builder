# Lê um arquivo CSV em uma lista de objetos dicionário

alunos = []

with open("estudantes0.csv") as arquivo:
    for linha in arquivo:
        nome, casa = linha.rstrip().split(",")
        alunos.append({"nome": nome, "casa": casa})

for aluno in alunos:
    print(f"{aluno['nome']} é de {aluno['casa']}")
# Lê um arquivo CSV em uma lista de objetos dict, criando o dict primeiro

alunos = []

with open("estudantes0.csv") as arquivo:
    for linha in arquivo:
        nome, casa = linha.rstrip().split(",")
        aluno = {"nome": nome, "casa": casa}
        alunos.append(aluno)

for aluno in alunos:
    print(f"{aluno['nome']} é de {aluno['casa']}")
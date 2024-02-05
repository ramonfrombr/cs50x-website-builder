# Lê um arquivo CSV usando csv.reader

import csv

alunos = []

with open("estudantes1.csv") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        alunos.append({"nome": linha[0], "casa": linha[1]})

for aluno in sorted(alunos, key=lambda aluno: aluno["nome"]):
    print(f"{aluno['nome']} é de {aluno['casa']}")
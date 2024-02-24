# Lê um arquivo CSV usando csv.DictReader

import csv

alunos = []

with open("estudantes2.csv") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        alunos.append({"nome": linha["nome"], "casa": linha["casa"]})

for aluno in sorted(alunos, key=lambda aluno: aluno["nome"]):
    print(f"{aluno['nome']} é de {aluno['casa']}")
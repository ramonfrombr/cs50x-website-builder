# Ordena uma lista de strings

alunos = []

with open("estudantes0.csv") as arquivo:
    for linha in arquivo:
        nome, casa = linha.rstrip().split(",")
        alunos.append(f"{nome} é de {casa}")

for aluno in sorted(alunos):
    print(aluno)
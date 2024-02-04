# Lê de um arquivo

with open("nomes.txt") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print("olá,", linha.rstrip())
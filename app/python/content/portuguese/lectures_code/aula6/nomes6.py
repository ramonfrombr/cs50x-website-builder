# Lê de um arquivo, uma linha de cada vez

with open("nomes.txt") as arquivo:
    for linha in arquivo:
        print("olá,", linha.rstrip())
# Lê um arquivo CSV

with open("estudantes0.csv") as arquivo:
    for linha in arquivo:
        linha_formatada = linha.rstrip().split(",")
        print(f"{linha_formatada[0]} é de {linha_formatada[1]}")
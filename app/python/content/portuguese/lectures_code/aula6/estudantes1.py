# Desempacota uma lista

with open("estudantes0.csv") as arquivo:
    for linha in arquivo:
        nome, casa = linha.rstrip().split(",")
        print(f"{nome} é de {casa}")
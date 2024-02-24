# Acrescenta gerenciador de contexto

nome = input("Qual é o seu nome? ")

with open("nomes.txt", "a") as arquivo:
    arquivo.write(f"{nome}\n")
# Adiciona gerenciador de contexto

nome = input("Qual é o seu nome? ")

com open("nomes.txt", "a") como arquivo:
    arquivo.write(f"{nome}\n")
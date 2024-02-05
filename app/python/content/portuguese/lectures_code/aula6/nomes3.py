# Adiciona ao arquivo

nome = input("Qual é o seu nome? ")

arquivo = open("nomes.txt", "a")
arquivo.write(f"{nome}\n")
arquivo.close()
# Escreve em um arquivo

nome = input("Qual é o seu nome? ")

arquivo = open("nomes.txt", "w")
arquivo.write(nome)
arquivo.close()
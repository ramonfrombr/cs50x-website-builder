# Escreve um arquivo CSV usando csv.DictWriter

import csv

name = input("Qual é o seu nome? ")
casa = input("Onde fica sua casa? ")

with open("estudantes2.csv", "a") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["nome", "casa"])
    escritor.writerow({"nome": nome, "casa": casa})
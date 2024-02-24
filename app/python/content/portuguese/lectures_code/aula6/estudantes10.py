# Escreve um arquivo CSV usando csv.writer

import csv

nome = input("Qual é o seu nome? ")
casa = input("Onde fica a sua casa? ")

with open("estudantes2.csv", "a") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([nome, casa])
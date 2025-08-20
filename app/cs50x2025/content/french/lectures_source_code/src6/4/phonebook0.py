# Sauvegarde les noms et numéros dans un fichier CSV

import csv
from cs50 import get_string

# Ouvre le fichier CSV
file = open("phonebook.csv", "a")

# Récupère le nom et le numéro
name = get_string("Name: ")
number = get_string("Number: ")

# Imprime dans le fichier
writer = csv.writer(file)
writer.writerow((name, number))

# Ferme le fichier
file.close()
# Enregistre les noms et numéros dans un fichier CSV

import csv
from cs50 import get_string

# Récupère le nom et le numéro
name = get_string("Nom : ")
number = get_string("Numéro : ")

# Ouvre le fichier CSV
with open("phonebook.csv", "a") as file:

    # Imprime dans le fichier
    writer = csv.writer(file)
    writer.writerow((name, number))
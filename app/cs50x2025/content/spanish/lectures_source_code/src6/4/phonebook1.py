# Guarda nombres y números al archivo CSV

import csv
from cs50 import get_string

# Obtén el nombre y número
name = get_string("Nombre: ")
number = get_string("Número: ")

# Abre el archivo CSV
with open("phonebook.csv", "a") as file:

    # Imprime al archivo
    writer = csv.writer(file)
    writer.writerow((name, number))
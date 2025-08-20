# Guarda nombres y números en un archivo CSV

import csv
from cs50 import get_string

# Abre el archivo CSV
file = open("phonebook.csv", "a")

# Obten nombre y número
name = get_string("Nombre: ")
number = get_string("Número: ")

# Escribe en el archivo
writer = csv.writer(file)
writer.writerow((name, number))

# Cierra el archivo
file.close()
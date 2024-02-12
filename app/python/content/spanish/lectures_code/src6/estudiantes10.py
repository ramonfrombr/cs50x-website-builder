# Escribe un archivo CSV usando csv.writer

import csv

nombre = input("¿Cuál es tu nombre? ")
hogar = input("¿Dónde está tu hogar? ")

with open("estudiantes2.csv", "a") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow([nombre, hogar])
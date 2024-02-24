# Escribe un archivo CSV utilizando csv.DictWriter

import csv

nombre = input("¿Cuál es tu nombre? ")
hogar = input("¿Dónde está tu hogar? ")

with open("estudiantes2.csv", "a") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["nombre", "hogar"])
    escritor.writerow({"nombre": nombre, "hogar": hogar})
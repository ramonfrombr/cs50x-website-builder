# Utiliza re.search

import re

nombre = input("¿Cuál es tu nombre? ").strip()
coincidencias = re.search(r"^(.+), (.+)$", nombre)
if coincidencias:
    apellido, nombre = coincidencias.groups()
    nombre = nombre + " " + apellido
print(f"hola, {nombre}")
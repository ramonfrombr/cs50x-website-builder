# Usa .group

import re

nombre = input("¿Cuál es tu nombre? ").strip()
coincidencias = re.search(r"^(.+), (.+)$", nombre)
if coincidencias:
    nombre = coincidencias.group(2) + " " + coincidencias.group(1)
print(f"hola, {nombre}")
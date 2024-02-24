# Usa el operador marsupial

import re

nombre = input("¿Cuál es tu nombre? ").strip()
if coincidencias := re.search(r"^(.+), (.+)$", nombre):
    nombre = coincidencias.group(2) + " " + coincidencias.group(1)
print(f"hola, {nombre}")
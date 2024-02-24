# Usa .group

import re

nome = input("Qual é o seu nome? ").strip()
correspondencias = re.search(r"^(.+), (.+)$", nome)
if correspondencias:
    nome = correspondencias.group(2) + " " + correspondencias.group(1)
print(f"olá, {nome}")
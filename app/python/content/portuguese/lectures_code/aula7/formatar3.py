# Usa operador de morsa

import re

nome = input("Qual é o seu nome? ").strip()
if correspondencias := re.search(r"^(.+), (.+)$", nome):
    nome = correspondencias.group(2) + " " + correspondencias.group(1)
print(f"olá, {nome}")
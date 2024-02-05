# Usa re.search

import re

nome = input("Qual é o seu nome? ").strip()
correspondencias = re.search(r"^(.+), (.+)$", nome)
if correspondencias:
    sobrenome, nome = correspondencias.groups()
    nome_completo = nome + " " + sobrenome
print(f"olá, {nome_completo}")
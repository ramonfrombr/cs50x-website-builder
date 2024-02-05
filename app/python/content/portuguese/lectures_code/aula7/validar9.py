# Adiciona classe de caracteres

import re

email = input("Qual é o seu email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Válido")
else:
    print("Inválido")
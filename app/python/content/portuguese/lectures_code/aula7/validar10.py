# Substitui a classe de caracteres por \w

import re

email = input("Qual é o seu email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Válido")
else:
    print("Inválido")
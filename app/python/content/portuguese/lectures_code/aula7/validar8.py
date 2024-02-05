# Adiciona ^ e $ ao regex

import re

email = input("Qual é o seu email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Válido")
else:
    print("Inválido")
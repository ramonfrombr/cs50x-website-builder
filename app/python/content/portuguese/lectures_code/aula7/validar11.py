# Adiciona re.IGNORECASE

import re

email = input("Qual é o seu email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Válido")
else:
    print("Inválido")
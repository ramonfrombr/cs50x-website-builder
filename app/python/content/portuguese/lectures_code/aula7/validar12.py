# Adiciona subdomínio opcional

import re

email = input("Qual é o seu email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Válido")
else:
    print("Inválido")
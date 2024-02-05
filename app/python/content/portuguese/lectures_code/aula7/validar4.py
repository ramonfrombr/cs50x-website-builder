# Valida o endereço de email verificando o '@' com regex

import re

email = input("Qual é o seu email? ").strip()

if re.search("@", email):
    print("Válido")
else:
    print("Inválido")
# Añade re.IGNORECASE

import re

email = input("¿Cuál es tu correo electrónico? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Válido")
else:
    print("Inválido")
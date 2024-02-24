# Agrega clase de caracteres

import re

email = input("¿Cuál es tu correo electrónico? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Válido")
else:
    print("Inválido")
# Reemplaza la clase de caracteres con \w

import re

email = input("¿Cuál es tu correo electrónico? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Válido")
else:
    print("Inválido")
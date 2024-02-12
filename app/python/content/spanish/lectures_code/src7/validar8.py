# Agrega ^ y $ a la expresión regular

import re

email = input("¿Cuál es tu correo electrónico? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Válido")
else:
    print("Inválido")
# Agrega .*

import re

correo = input("¿Cuál es tu correo electrónico? ").strip()

if re.search(".*@.*", correo):
    print("Válido")
else:
    print("Inválido")
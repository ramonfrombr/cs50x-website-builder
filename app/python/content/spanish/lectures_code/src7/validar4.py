# Valida la dirección de correo electrónico verificando el símbolo @ con regex

import re

email = input("¿Cuál es tu correo electrónico? ").strip()

if re.search("@", email):
    print("Válido")
else:
    print("Inválido")
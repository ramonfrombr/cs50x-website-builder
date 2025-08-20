# Operadores lógicos, utilizando expresiones regulares

import re
from cs50 import get_string

# Le pide al usuario que esté de acuerdo
s = get_string("¿Estás de acuerdo?\n")

# Verifica si está de acuerdo
if re.search("^y(es)?$", s, re.IGNORECASE):
    print("De acuerdo.")
elif re.search("^no?$", s, re.IGNORECASE):
    print("No de acuerdo.")
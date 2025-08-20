# Capitaliza una copia de una cadena

from cs50 import get_string

# Obtener una cadena
s = get_string("s: ")

# Copiar cadena
t = s

# Capitalizar copia
t = t.capitalize()

# Imprimir cadenas
print(f"s: {s}")
print(f"t: {t}")
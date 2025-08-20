# Operadores lógicos, usando listas

from cs50 import get_string

# Le pide al usuario que acepte
s = get_string("¿Está de acuerdo?\n")

# Verifica si está de acuerdo
if s.lower() in ["y", "yes"]:
    print("Acordado.")
elif s.lower() in ["n", "no"]:
    print("No acordado.")
#Operadores lógicos

from cs50 import get_string

# Solicitar al usuario que acepte
s = get_string("¿Aceptás?\n")

# Comprobar si aceptó
if s == "Y" or s == "y":
    print("Aceptado.")
elif s == "N" or s == "n":
    print("No aceptado.")
# Condiciones y operadores relacionales

from cs50 import get_int

# Solicita al usuario un valor para x
x = get_int("x: ")

# Solicita al usuario un valor para y
y = get_int("y: ")

# Compara x e y
if x < y:
    print("x es menor que y")
elif x > y:
    print("x es mayor que y")
else:
    print("x es igual a y")
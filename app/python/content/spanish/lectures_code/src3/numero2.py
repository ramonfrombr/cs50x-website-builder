# Demuestra un NameError

try:
    x = int(input("¿Qué es x? "))
except ValueError:
    print("x no es un entero")

print(f"x es {x}")
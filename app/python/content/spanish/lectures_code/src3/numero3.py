# Demuestra el "else"

try:
    x = int(input("¿Cuál es x? "))
except ValueError:
    print("x no es un entero")
else:
    print(f"x es {x}")
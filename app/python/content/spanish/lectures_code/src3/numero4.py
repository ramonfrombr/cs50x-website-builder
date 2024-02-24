# Agrega un bucle

while True:
    try:
        x = int(input("¿Qué es x? "))
    except ValueError:
        print("x no es un número entero")
    else:
        break

print(f"x es {x}")
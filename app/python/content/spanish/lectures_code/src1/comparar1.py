# Demuestra condiciones mutuamente excluyentes

x = int(input("¿Qué es x? "))
y = int(input("¿Qué es y? "))

if x < y:
    print("x es menor que y")
elif x > y:
    print("x es mayor que y")
elif x == y:
    print("x es igual a y")
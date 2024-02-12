# Demuestra cómo definir una función con un valor de retorno

def principal():
    x = int(input("¿Cuál es x? "))
    print("El cuadrado de x es", cuadrado(x))

def cuadrado(n):
    return n * n

principal()
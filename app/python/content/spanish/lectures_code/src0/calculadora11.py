# Muestra la definición de una función con un valor de retorno

def principal():
    x = int(input("¿Cuál es el valor de x? "))
    print("x al cuadrado es", cuadrado(x))

def cuadrado(n):
    return n * n

principal()
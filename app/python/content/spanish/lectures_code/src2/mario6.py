# Imprime cuadrado de ladrillos usando una función con un bucle y multiplicación de cadenas

def principal():
    imprimir_cuadrado(3)

def imprimir_cuadrado(tamano):
    for _ in range(tamano):
        print("#" * tamano)

principal()
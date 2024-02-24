# Imprime un cuadrado de ladrillos usando una función con un bucle y multiplicación de str

def principal():
    imprimir_cuadrado(3)

def imprimir_cuadrado(tamano):
    for _ in range(tamano):
        imprimir_linea(tamano)

def imprimir_linea(ancho):
    print("#" * ancho)

principal()
# Imprime un cuadrado de ladrillos usando una función con bucles anidados

def principal():
    imprimir_cuadrado(3)

def imprimir_cuadrado(tamano):
    for i in range(tamano):
        for j in range(tamano):
            print("#", end="")
        print()

principal()
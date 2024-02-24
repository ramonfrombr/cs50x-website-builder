# Prueba una función con funciones múltiples a través de pytest

def principal():
    x = int(input("¿Cuál es x? "))
    print("El cuadrado de x es", cuadrado(x))


def cuadrado(n):
    return n * n


if __name__ == "__main__":
    principal()
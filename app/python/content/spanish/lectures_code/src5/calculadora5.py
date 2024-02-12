# Prueba una función con una función a través de pytest

def main():
    x = int(input("¿Cuál es x? "))
    print("El cuadrado de x es", cuadrado(x))

def cuadrado(n):
    return n * n

if __name__ == "__main__":
    main()
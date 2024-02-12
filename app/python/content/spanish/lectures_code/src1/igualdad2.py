# Demuestra expresiones condicionales (operadores ternarios)

def principal():
    x = int(input("¿Cuál es el valor de x? "))
    if es_par(x):
        print("Par")
    else:
        print("Impar")

def es_par(n):
    return True if n % 2 == 0 else False

principal()
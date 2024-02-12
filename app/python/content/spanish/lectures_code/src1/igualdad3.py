# Demuestra devolver el valor de una expresión booleana

def principal():
    x = int(input("¿Cuál es x? "))
    if es_par(x):
        print("Par")
    else:
        print("Impar")

def es_par(n):
    return n % 2 == 0

principal()
# Demuestra una función que retorna un booleano

def principal():
    x = int(input("¿Cuál es x? "))
    if es_par(x):
        print("Par")
    else:
        print("Impar")

def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

principal()
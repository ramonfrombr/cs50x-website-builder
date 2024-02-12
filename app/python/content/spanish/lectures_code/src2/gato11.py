# Demuestra la definición de funciones

def principal():
    maullar(recibir_numero())


def recibir_numero():
    while True:
        n = int(input("¿Cuál es n? "))
        if n > 1:
            return n


def maullar(n):
    for _ in range(n):
        print("miau")


principal()
# Añade pasar


def principal():
    x = recibir_entero()
    print(f"x es {x}")


def recibir_entero():
    while True:
        try:
            return int(input("¿Cuál es x? "))
        except ValueError:
            pass


principal()
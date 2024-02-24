# Elimina break


def principal():
    x = recibir_entero()
    print(f"x es {x}")


def recibir_entero():
    while True:
        try:
            x = int(input("¿Cuál es x? "))
        except ValueError:
            print("x no es un entero")
        else:
            return x


principal()
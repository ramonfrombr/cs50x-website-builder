# Añade funciones, usa break y return

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
            break
    return x


principal()
# Tiene la función que devuelve un str en lugar de


def principal():
    nombre = input("¿Cuál es tu nombre? ")
    print(hola(nombre))


def hola(nombre="mundo"):
    return f"hola, {nombre}"


if __name__ == "__main__":
    principal()
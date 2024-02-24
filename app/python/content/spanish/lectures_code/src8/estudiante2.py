# Devuelve estudiante como tupla, desempaquetándolo


def principal():
    nombre, casa = recibir_estudiante()
    print(f"{nombre} de {casa}")


def recibir_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return nombre, casa


if __name__ == "__main__":
    principal()
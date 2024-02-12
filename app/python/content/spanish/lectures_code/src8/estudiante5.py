# Almacena al estudiante como una lista (mutable)


def principal():
    estudiante = recibir_estudiante()
    if estudiante[0] == "Padma":
        estudiante[1] = "Ravenclaw"
    print(f"{estudiante[0]} de {estudiante[1]}")


def recibir_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return [nombre, casa]


if __name__ == "__main__":
    principal()
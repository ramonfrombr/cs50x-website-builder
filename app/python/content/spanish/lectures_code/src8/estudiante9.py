# Define la clase para un estudiante


class Estudiante:
    ...


def principal():
    estudiante = recibir_estudiante()
    print(f"{estudiante.nombre} de la casa {estudiante.casa}")


def recibir_estudiante():
    estudiante = Estudiante()
    estudiante.nombre = input("Nombre: ")
    estudiante.casa = input("Casa: ")
    return estudiante


if __name__ == "__main__":
    principal()
# Agrega validación en __init__ usando raise


class Estudiante:
    def __init__(self, nombre, casa):
        if not nombre:
            raise ValueError("Nombre faltante")
        if casa not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Casa inválida")
        self.nombre = nombre
        self.casa = casa


def principal():
    estudiante = crear_estudiante()
    print(f"{estudiante.nombre} de la casa {estudiante.casa}")


def crear_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return Estudiante(nombre, casa)


if __name__ == "__main__":
    principal()
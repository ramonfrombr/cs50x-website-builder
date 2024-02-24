# Imprime estudiante sin __str__


class Estudiante:
    def __init__(self, nombre, casa):
        if not nombre:
            raise ValueError("Falta el nombre")
        if casa not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Casa inválida")
        self.nombre = nombre
        self.casa = casa


def principal():
    estudiante = crear_estudiante()
    print(estudiante)


def crear_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return Estudiante(nombre, casa)


if __name__ == "__main__":
    principal()
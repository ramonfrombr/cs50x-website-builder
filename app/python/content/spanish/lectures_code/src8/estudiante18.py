# Agrega @property para casa


class Estudiante:
    def __init__(self, nombre, casa):
        if not nombre:
            raise ValueError("Nombre inválido")
        self.nombre = nombre
        self.casa = casa

    def __str__(self):
        return f"{self.nombre} de la casa {self.casa}"

    @property
    def casa(self):
        return self._casa

    @casa.setter
    def casa(self, casa):
        if casa not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Casa inválida")
        self._casa = casa


def principal():
    estudiante = crear_estudiante()
    print(estudiante)


def crear_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return Estudiante(nombre, casa)


if __name__ == "__main__":
    principal()
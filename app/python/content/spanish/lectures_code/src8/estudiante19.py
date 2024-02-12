# Añade @property para el nombre

class Estudiante:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa

    def __str__(self):
        return f"{self.nombre} de {self.casa}"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("Nombre inválido")
        self._nombre = nombre

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
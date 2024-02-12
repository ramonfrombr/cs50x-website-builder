# Mueve get_student dentro de la clase Estudiante

class Estudiante:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa

    def __str__(self):
        return f"{self.nombre} de la casa {self.casa}"

    @classmethod
    def crear(cls):
        nombre = input("Nombre: ")
        casa = input("Casa: ")
        return cls(nombre, casa)


def principal():
    estudiante = Estudiante.crear()
    print(estudiante)


if __name__ == "__main__":
    principal()
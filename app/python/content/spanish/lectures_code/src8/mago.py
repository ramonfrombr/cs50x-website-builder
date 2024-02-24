# Demuestra la herencia [tal vez no agregar la verificación de errores `if`]

class Mago:
    def __init__(self, nombre):
        if not nombre:
            raise ValueError("Falta el nombre")
        self.nombre = nombre

    ...


class Estudiante(Mago):
    def __init__(self, nombre, casa):
        super().__init__(nombre)
        self.casa = casa

    ...


class Profesor(Mago):
    def __init__(self, nombre, asignatura):
        super().__init__(nombre)
        self.asignatura = asignatura

    ...


mago = Mago("Albus")
estudiante = Estudiante("Harry", "Gryffindor")
profesor = Profesor("Severus", "Defensa contra las Artes Oscuras")
...
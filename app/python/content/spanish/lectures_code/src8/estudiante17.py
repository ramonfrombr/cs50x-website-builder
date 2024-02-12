# Elimina el Patronus por simplicidad, evita la verificación de errores configurando el atributo

class Estudiante:
    def __init__(self, nombre, casa):
        if not nombre:
            raise ValueError("Nombre inválido")
        if casa not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Casa inválida")
        self.nombre = nombre
        self.casa = casa

    def __str__(self):
        return f"{self.nombre} de {self.casa}"

def principal():
    estudiante = crear_estudiante()
    estudiante.casa = "Calle Privet, número Cuatro"
    print(estudiante)

def crear_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return Estudiante(nombre, casa)

if __name__ == "__main__":
    principal()
# Solicita también el patrónus, pero aún no lo muestra

class Estudiante:
    def __init__(self, nombre, casa, patronus):
        if not nombre:
            raise ValueError("Falta el nombre")
        if casa not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Casa inválida")
        self.nombre = nombre
        self.casa = casa
        self.patronus = patronus

    def __str__(self):
        return f"{self.nombre} de la casa {self.casa}"

def main():
    estudiante = crear_estudiante()
    print(estudiante)

def crear_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    patronus = input("Patronus: ")
    return Estudiante(nombre, casa, patronus)

if __name__ == "__main__":
    main()
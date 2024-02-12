# Agrega el método encantar para lanzar un encanto

class Estudiante:
    def __init__(self, nombre, casa, patronus=None):
        if not nombre:
            raise ValueError("Falta el nombre")
        if casa not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Casa inválida")
        if patronus and patronus not in ["Ciervo", "Nutria", "Jack Russell terrier"]:
            raise ValueError("Patronus inválido")
        self.nombre = nombre
        self.casa = casa
        self.patronus = patronus

    def __str__(self):
        return f"{self.nombre} de la casa {self.casa}"

    def encantar(self):
        match self.patronus:
            case "Ciervo":
                return "🐴"
            case "Nutria":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    estudiante = crear_estudiante()
    print("Expecto Patronum!")
    print(estudiante.encantar())


def crear_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    patronus = input("Patronus: ") or None
    return Estudiante(nombre, casa, patronus)


if __name__ == "__main__":
    main()
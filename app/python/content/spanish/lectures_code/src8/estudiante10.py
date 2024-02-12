# Agrega __init__

class Estudiante:
    def __init__(self, nombre, casa):
        self.nombre = nombre
        self.casa = casa

def principal():
    estudiante = recibir_estudiante()
    print(f"{estudiante.nombre} de {estudiante.casa}")

def recibir_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    estudiante = Estudiante(nombre, casa)
    return estudiante

if __name__ == "__main__":
    principal()
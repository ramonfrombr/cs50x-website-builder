# Almacena el estudiante como un diccionario

def principal():
    estudiante = recibir_estudiante()
    print(f"{estudiante['nombre']} de la {estudiante['casa']}")


def recibir_estudiante():
    estudiante = {}
    estudiante["nombre"] = input("Nombre: ")
    estudiante["casa"] = input("Casa: ")
    return estudiante


if __name__ == "__main__":
    principal()
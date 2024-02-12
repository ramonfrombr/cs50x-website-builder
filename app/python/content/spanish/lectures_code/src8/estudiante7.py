# Elimina una variable innecesaria

def principal():
    estudiante = recibir_estudiante()
    print(f"{estudiante['nombre']} de {estudiante['casa']}")


def recibir_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return {"nombre": nombre, "casa": casa}


if __name__ == "__main__":
    principal()
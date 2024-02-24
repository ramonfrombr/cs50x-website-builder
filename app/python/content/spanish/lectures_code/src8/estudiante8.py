# Demuestra la mutabilidad de los diccionarios


def principal():
    estudiante = recibir_estudiante()
    if estudiante["nombre"] == "Padma":
        estudiante["casa"] = "Ravenclaw"
    print(f"{estudiante['nombre']} de la casa {estudiante['casa']}")


def recibir_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return {"nombre": nombre, "casa": casa}


if __name__ == "__main__":
    principal()
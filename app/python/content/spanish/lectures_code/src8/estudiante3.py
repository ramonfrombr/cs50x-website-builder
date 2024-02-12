# Retorna el estudiante como una tupla, sin desempacarlo

def principal():
    estudiante = recibir_estudiante()
    print(f"{estudiante[0]} de la casa {estudiante[1]}")

def recibir_estudiante():
    nombre = input("Nombre: ")
    casa = input("Casa: ")
    return (nombre, casa)

if __name__ == "__main__":
    principal()
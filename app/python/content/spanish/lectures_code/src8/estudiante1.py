# Modulariza la obtención del nombre y la casa del estudiante

def principal():
    nombre = recibir_nombre()
    casa = recibir_casa()
    print(f"{nombre} de {casa}")

def recibir_nombre():
    return input("Nombre: ")

def recibir_casa():
    return input("Casa: ")

if __name__ == "__main__":
    principal()
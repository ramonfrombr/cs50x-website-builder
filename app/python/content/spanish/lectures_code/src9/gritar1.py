# Pasa una lista


def principal():
    gritar(["Esto", "es", "CS50"])


def gritar(palabras):
    en_mayusculas = []
    for palabra in palabras:
        en_mayusculas.append(palabra.upper())
    print(*en_mayusculas)


if __name__ == "__main__":
    principal()
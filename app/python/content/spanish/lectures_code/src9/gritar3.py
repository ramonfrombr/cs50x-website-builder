# Usos de map

def principal():
    gritar("Esto", "es", "CS50")


def gritar(*palabras):
    en_mayusculas = map(str.upper, palabras)
    print(*en_mayusculas)


if __name__ == "__main__":
    principal()
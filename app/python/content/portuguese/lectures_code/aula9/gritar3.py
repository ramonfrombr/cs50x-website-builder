# Utiliza map


def principal():
    gritar("Este", "é", "o", "CS50")


def gritar(*palavras):
    maiusculas = map(str.upper, palavras)
    print(*maiusculas)


if __name__ == "__main__":
    principal()
# Passa uma lista

def principal():
    gritar(["Isso", "é", "CS50"])


def gritar(palavras):
    maiusculas = []
    for palavra in palavras:
        maiusculas.append(palavra.upper())
    print(*maiusculas)


if __name__ == "__main__":
    principal()
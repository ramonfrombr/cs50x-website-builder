# Usa comprensión de listas

def principal():
    gritar("Esto", "es", "CS50")

def gritar(*palabras):
    mayusculas = [palabra.upper() for palabra in palabras]
    print(*mayusculas)

if __name__ == "__main__":
    principal()
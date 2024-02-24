# Código de lenguaje Python de ciencias de la computación a traducir

# Función a probar
def principal():
    nombre = input("¿Cuál es tu nombre? ")
    hola(nombre)

# Función para saludar
def hola(nombre="mundo"):
    print("hola,", nombre)

if __name__ == "__main__":
    principal()
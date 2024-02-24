# Demuestra cómo definir una función principal

def principal():
    nombre = input("¿Cuál es tu nombre? ")
    hola(nombre)

def hola(para="mundo"):
    print("¡Hola,", para, "!")

principal()
# Muestra cómo definir una función con un parámetro con un valor predeterminado

def hola(para="mundo"):
    print("hola,", para)

hola()
nombre = input("¿Cuál es tu nombre? ")
hola(nombre)
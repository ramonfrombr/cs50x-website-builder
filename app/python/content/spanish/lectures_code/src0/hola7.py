# Muestra las funciones de cadenas

nombre = input("¿Cuál es tu nombre? ").strip().title()
primero, segundo = nombre.split(" ")
print(f"hola, {primero}")
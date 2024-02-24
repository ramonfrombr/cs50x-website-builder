# Reformatea "apellido, nombre" como "nombre apellido"

nombre = input("¿Cuál es tu nombre? ").strip()
if "," in nombre:
    apellido, nombre = nombre.split(", ")
    nombre = f"{nombre} {apellido}"
print(f"hola, {nombre}")
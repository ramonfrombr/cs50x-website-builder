# Elimina espacios en blanco antes de comparar

respuesta = input("¿Estás de acuerdo? ").strip()
if respuesta == "sí":
    print("De acuerdo")
else:
    print("No de acuerdo")
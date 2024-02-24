# Poner en minúscula la cadena antes de comparar

respuesta = input("¿Estás de acuerdo? ").strip().lower()
if respuesta == "sí":
    print("De acuerdo")
else:
    print("No de acuerdo")
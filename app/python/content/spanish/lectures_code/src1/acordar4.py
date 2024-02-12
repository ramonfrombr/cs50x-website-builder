# Compara múltiples cadenas

respuesta = input("¿Estás de acuerdo? ").strip().lower()
if respuesta.startswith("s"):
    print("De acuerdo")
else:
    print("No de acuerdo")
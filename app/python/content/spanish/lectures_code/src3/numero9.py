# Agrega solicitud

def principal():
    x = recibir_entero("¿Cuál es x? ")
    print(f"x es {x}")

def recibir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            pass

principal()
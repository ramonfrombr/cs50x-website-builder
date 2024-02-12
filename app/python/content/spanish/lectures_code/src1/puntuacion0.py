# Demuestra desigualdades and operadores lógicos

puntuacion = int(input("puntuacion: "))

if puntuacion >= 90 and puntuacion <= 100:
    print("Grado: A")
elif puntuacion >= 80 and puntuacion < 90:
    print("Grado: B")
elif puntuacion >= 70 and puntuacion < 80:
    print("Grado: C")
elif puntuacion >= 60 and puntuacion < 70:
    print("Grado: D")
else:
    print("Grado: F")
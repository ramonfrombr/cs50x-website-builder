# Demuestra comparaciones encadenadas

puntuacion = int(input("Puntuación: "))

if 90 <= puntuacion <= 100:
    print("Grado: A")
elif 80 <= puntuacion < 90:
    print("Grado: B")
elif 70 <= puntuacion < 80:
    print("Grado: C")
elif 60 <= puntuacion < 70:
    print("Grado: D")
else:
    print("Grado: F")
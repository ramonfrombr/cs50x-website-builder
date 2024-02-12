# Demuestra desigualdades y operadores lógicos

puntuación = int(input("Puntuación: "))

if 90 <= puntuación and puntuación <= 100:
    print("Grado: A")
elif 80 <= puntuación and puntuación < 90:
    print("Grado: B")
elif 70 <= puntuación and puntuación < 80:
    print("Grado: C")
elif 60 <= puntuación and puntuación < 70:
    print("Grado: D")
else:
    print("Grado: F")
# Introduce continuar, detener

while True:
    n = int(input("¿Cuál es n? "))
    if n <= 0:
        continue
    else:
        break

for _ in range(n):
    print("miau")